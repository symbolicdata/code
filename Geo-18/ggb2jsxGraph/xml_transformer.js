const geogebraBoilerplate = `<?xml version="1.0" encoding="utf-8"?>
<geogebra>
<euclidianView>
	<coordSystem xZero="215.0" yZero="315.0" scale="50.0" yscale="50.0"/>
	<evSettings axes="true" grid="true" gridIsBold="false" pointCapturing="3" rightAngleStyle="1" checkboxSize="26" gridType="3"/>
</euclidianView>
<kernel>
	<decimals val="2"/>
	<angleUnit val="degree"/>
</kernel>
<construction>
</construction>
</geogebra>`;

const GGB_HIGHLIGHT_RED = '<objColor r="255" g="0" b="0" alpha="0.0"/>';
const GGB_HIGHLIGHT_BLUE = '<objColor r="50" g="50" b="220" alpha="0.0"/>';
const GGB_HIGHLIGHT_DARK_BLUE = '<objColor r="20" g="20" b="120" alpha="0.0"/>';
const GGB_HIGHLIGHT_GREY = '<objColor r="150" g="150" b="150" alpha="0.0"/>';
const GGB_COORDS_SLIDER = '<coords x="1" y="1" z="1"/>';
const getGgbCoordsCircleSlider = () => {
    const coords = circleSliderCoordGenerator.next().value;
    return `<coords x="${coords[0]}" y="${coords[1]}" z="1"/>`;
}
const GGB_ELEMENT_HIDDEN = '<show object="false" label="false"/>';
const GGB_LINE_DASHED = '<lineStyle type="15"/>';

// to keep track of ids of construction tools used by macros
// so we don't use them multiple times
let macroIdRepository = {};
let propExplanations = [];
// ids of elements that turn out to be part of a prop later on and need to be highlighted accordingly
let retroactiveHighlights = [];
let circleSliderCoordGenerator = createCircleSliderCoordGenerator();

// construction tools that are entirely equivalent between Geoproof/GeoGebra, including parameters and their order
const commandNameMapping = {
    'p_bisector': 'LineBisector',
    'intersection_point': 'Intersect',
    'midpoint': 'Midpoint',
    'pp_line': 'Line',
    'ortho_line': 'OrthogonalLine',
    'par_line': 'Line',
    'pc_circle': 'Circle',
    'p3_circle': 'Circle'
};
// any construction tools not covered by the above
// callback arguments are always (...inputs, output)
const commandMacroMapping = {
    'altitude': function (pointTop, pointBase1, pointBase2, finalOutput) {
        const lineId = `base of ${finalOutput}`;
        const returnStr =
            createCommandXml('Line', [pointBase1, pointBase2], lineId, 'line', [GGB_LINE_DASHED, GGB_HIGHLIGHT_GREY]) +
            createCommandXml('OrthogonalLine', [pointTop, lineId], finalOutput, 'line');
        markIdUsed(lineId);
        return returnStr;
    },
    'pedalpoint': function (point, line, finalOutput) {
        const orthogonalLineId = generateToolId('ortho', point, line);
        const returnStr =
            createCommandXml('OrthogonalLine', [point, line], orthogonalLineId, 'line', [GGB_LINE_DASHED, GGB_HIGHLIGHT_GREY]) +
            createCommandXml('Intersect', [line, orthogonalLineId], finalOutput, 'point');
        markIdUsed(orthogonalLineId);
        return returnStr;
    },
    'median': function (pointTop, pointBase1, pointBase2, finalOutput) {
        const midpointId = generateToolId('mid', pointBase1, pointBase2);
        const returnStr =
            createCommandXml('Midpoint', [pointBase1, pointBase2], midpointId, 'point') +
            createCommandXml('Line', [pointTop, midpointId], finalOutput, 'line');
        markIdUsed(midpointId);
        return returnStr;
    },
    'line_slider': function (line, finalOutput) {
        return createCommandXml('Point', [line], finalOutput, 'point', [GGB_COORDS_SLIDER, GGB_HIGHLIGHT_DARK_BLUE]);
    },
    'varpoint': function (A, B, finalOutput) {
        const lineId = generateToolId('line', A, B);
        const returnStr =
            createCommandXml('Line', [A, B], lineId, 'line') +
            createCommandXml('Point', [lineId], finalOutput, 'point', [GGB_COORDS_SLIDER, GGB_HIGHLIGHT_DARK_BLUE]);
        markIdUsed(lineId);
        return returnStr;
    },
    'circle_slider': function (pointMid, pointOnCircle, finalOutput) {
        const circleId = generateToolId('circle', pointMid, pointOnCircle);
        const returnStr =
            createCommandXml('Circle', [pointMid, pointOnCircle], circleId, 'circle') +
            createCommandXml('Point', [circleId], finalOutput, 'point', [getGgbCoordsCircleSlider(), GGB_HIGHLIGHT_DARK_BLUE]);
        markIdUsed(circleId);
        return returnStr;
    },
    'orthocenter': function (A, B, C, finalOutput) {
        const alt1Id = generateToolId('altitude', A, B, C);
        const alt2Id = generateToolId('altitude', B, C, A);
        const returnStr =
            this['altitude'](A, B, C, alt1Id) +
            this['altitude'](B, C, A, alt2Id) +
            createCommandXml('Intersect', [alt1Id, alt2Id], finalOutput, 'point');
        markIdUsed(alt1Id, alt2Id);
        return returnStr;
    },
    'circumcenter': function (A, B, C, finalOutput) {
        const perpBisector1Id = generateToolId('perpBisector', A, B);
        const perpBisector2Id = generateToolId('perpBisector', B, C);
        const returnStr =
            createCommandXml('LineBisector', [A, B], perpBisector1Id, 'line') +
            createCommandXml('LineBisector', [B, C], perpBisector2Id, 'line') +
            createCommandXml('Intersect', [perpBisector1Id, perpBisector2Id], finalOutput, 'point');
        markIdUsed(perpBisector1Id, perpBisector2Id);
        return returnStr;
    }
};

const propMacroMapping = {
    'eq_dist': function (A, B, C, D) {
        const firstLineId = generateToolId('dist', A, B);
        const secondLineId = generateToolId('dist', C, D);
        const returnStr =
            createCommandXml('Segment', [A, B], firstLineId, 'line', GGB_HIGHLIGHT_RED) +
            createCommandXml('Segment', [C, D], secondLineId, 'line', GGB_HIGHLIGHT_RED);
        markIdUsed(firstLineId, secondLineId);
        propExplanations.push(`Distance (${A}, ${B}) is equal to distance (${C}, ${D})`)
        return returnStr;
    },
    'eq_angle': function (A, B, C, D, E, F) {
        const firstAngleId = generateToolId('ang', A, B, C);
        const secondAngleId = generateToolId('ang', D, E, F);
        const returnStr =
            createCommandXml('Angle', [A, B, C], firstAngleId, 'angle', GGB_HIGHLIGHT_RED) +
            createCommandXml('Angle', [D, E, F], secondAngleId, 'angle', GGB_HIGHLIGHT_RED);
        markIdUsed(firstAngleId, secondAngleId);
        propExplanations.push(`Angle (${A}, ${B}, ${C}) is equal to angle (${D}, ${E}, ${F})`)
        return returnStr;
    },
    'is_concurrent': function (...lines) {
        const intersectionId = generateToolId('inter', ...lines);
        const returnStr = createCommandXml('Intersect', lines, intersectionId, 'point', GGB_HIGHLIGHT_RED);
        markIdUsed(intersectionId);
        propExplanations.push(`Lines ${lines.join(', ')} are concurrent`);
        return returnStr;
    },
    'is_collinear': function (...points) {
        const lineId = generateToolId('line', ...points);
        const returnStr = createCommandXml('Line', points.slice(0, 2), lineId, 'line', GGB_HIGHLIGHT_RED);
        markIdUsed(lineId);
        propExplanations.push(`Points ${points.join(', ')} are collinear`);
        return returnStr;
    },
    'is_concyclic': function (...points) {
        const circleId = generateToolId('circle', ...points);
        const returnStr = createCommandXml('Circle', points.slice(0, 3), circleId, 'circle', GGB_HIGHLIGHT_RED);
        markIdUsed(circleId);
        propExplanations.push(`Points ${points.join(', ')} are concyclic`);
        return returnStr;
    },
    'is_parallel': function (g, f) {
        retroactiveHighlights.push(g, f);
        propExplanations.push(`Lines ${g} and ${f} are parallel`);
    },
    'is_orthogonal': function (g, f) {
        retroactiveHighlights.push(g, f);
        propExplanations.push(`Lines ${g} and ${f} are orthogonal`);
    }
};

function markIdUsed(...ids) {
    for (const id of ids) macroIdRepository[id] = true;
}

function transformXml(inputXml) {
    const $inputXml = $($.parseXML(inputXml));
    const $resultXml = $($.parseXML(geogebraBoilerplate));
    const $construction = $resultXml.find('construction');

    const $freePoints = $inputXml.find('Points Point');
    const freePointGenerator = createCoordGenerator();
    $freePoints.each((i, elem) => {
        $construction.append(transformFreePointXml(elem, freePointGenerator));
    });

    const $assignments = $inputXml.find('Assignments').children();
    $assignments.each((i, elem) => {
        $construction.append(transformCommandXml(elem));
    });

    const $props = $inputXml.find('Conclusions prop');
    $props.each((i, elem) => {
        $construction.append(transformPropXml(elem));
    });

    for (let i = 0; i < retroactiveHighlights.length; i++) {
        const $el = $construction.find(`element[label="${retroactiveHighlights[i]}"]`);
        if (!$el) continue;
        $el.find('objColor').remove();
        $el.append(GGB_HIGHLIGHT_RED);
    }

    return new XMLSerializer().serializeToString($resultXml[0]);
}

function* createCoordGenerator() {
    yield [0, 1];
    yield [1, 0];
    yield [2, 1.5];
    yield [0.7, 3];
    yield [3, 2];
}

// create new circle slider default positions by roughly moving around the circle in 37° increments
// this generator is shared for all sliders, even if they're on different circles
function* createCircleSliderCoordGenerator() {
    let angle = 0;
    const angleStep = 37 * 180 / Math.PI;
    while (true) {
        angle += angleStep;
        yield [1000 * Math.cos(angle), 1000 * Math.sin(angle)];
    }
}

function createCommandXml(commandName, inputIds, outputId, outputType, additionalElementData) {
    // check if outputId has been used already, so we don't get duplicates
    if (macroIdRepository[outputId]) return '';

    const inputsIdsAsAttributes = inputIds.map((str, i) => `a${i}="${str}"`);
    return (`
        <command name="${commandName}">
            <input ${inputsIdsAsAttributes.join(' ')}/>
            <output a0="${outputId}"/>
        </command>
        ${additionalElementData ?
            `<element type="${outputType}" label="${outputId}">
                ${typeof additionalElementData === 'Array' ? additionalElementData.join('\n') : additionalElementData}
            </element>` :
            `<element type="${outputType}" label="${outputId}"/>`}
        `
    );
}

function transformFreePointXml(inputXmlElement, freePointGenerator) {
    const pointId = cleanId(inputXmlElement.getAttribute('id'));
    const coords = freePointGenerator.next().value;
    if (!coords) fatalError("Not enough free point coordinates available");
    return (
        `<element type="point" label="${pointId}">
            <coords x="${coords[0]}" y="${coords[1]}" z="1.0"/>
            ${GGB_HIGHLIGHT_BLUE}
        </element>`
    );
}

function transformCommandXml(inputXmlElement) {
    const outputId = cleanId(inputXmlElement.getAttribute('id'));
    const outputType = inputXmlElement.nodeName.toLowerCase();
    const commandCallStr = inputXmlElement.textContent;
    if (!commandCallStr) return '';
    const command = parseCommand(commandCallStr);
    console.log(`command ${command.name} with inputs ${command.inputs} and output ${outputId}`);
    const mappedCommandName = commandNameMapping[command.name];
    if (!mappedCommandName) {
        if (command.name in commandMacroMapping) {
            return commandMacroMapping[command.name](...command.inputs, outputId);
        }
        fatalError("Unknown command " + command.name);
    }
    return createCommandXml(mappedCommandName, command.inputs, outputId, outputType);
}

function transformPropXml(inputXmlElement) {
    const commandCallStr = inputXmlElement.textContent;
    if (!commandCallStr) return '';
    const command = parseCommand(commandCallStr);
    console.log(`prop ${command.name} with inputs ${command.inputs}`);
    if (command.name in propMacroMapping) {
        return propMacroMapping[command.name](...command.inputs);
    } else {
        fatalError("Unknown prop " + command.name);
    }
    return '';
}

function fatalError(msg) {
    alert(msg);
    throw msg;
}

function resetData() {
    macroIdRepository = {};
    propExplanations = [];
    retroactiveHighlights = [];
    circleSliderCoordGenerator = createCircleSliderCoordGenerator();
}

// removes leading $
// fixes subscript for multi-digit numbers (by putting underscores in front every digit after the first one)
function cleanId(originalId) {
    return originalId.substr(1).replace(/\d+/g, (match) => match.split('').join('_'));
}

function generateToolId(toolName, ...inputs) {
    return `${toolName}(${inputs.join(', ')})`;
}

function parseCommand(commandStr) {
    const uncleanInputIds = commandStr.substring(commandStr.indexOf('[') + 1, commandStr.indexOf(']')).split(',');
    return {
        name: commandStr.substring(0, commandStr.indexOf('[')),
        inputs: uncleanInputIds.map(str => str.trim()).filter(str => str.startsWith('$')).map(cleanId)
    }
}
