package gr2.cips.jsxgraph;

import gr2.cips.jsxgraph.model.JSXGraphCircleGlider;
import gr2.cips.jsxgraph.model.JSXGraphCircumCircle;
import gr2.cips.jsxgraph.model.JSXGraphElement;
import gr2.cips.jsxgraph.model.JSXGraphFixedPoint;
import gr2.cips.jsxgraph.model.JSXGraphIntersection;
import gr2.cips.jsxgraph.model.JSXGraphLine;
import gr2.cips.jsxgraph.model.JSXGraphLineGlider;
import gr2.cips.jsxgraph.model.JSXGraphMidPoint;
import gr2.cips.jsxgraph.model.JSXGraphP3Bisector;
import gr2.cips.jsxgraph.model.JSXGraphPCCircle;
import gr2.cips.jsxgraph.model.JSXGraphParallel;
import gr2.cips.jsxgraph.model.JSXGraphParameter;
import gr2.cips.jsxgraph.model.JSXGraphPerpendicular;
import gr2.cips.jsxgraph.model.JSXGraphPoint;
import gr2.cips.jsxgraph.model.JSXGraphVarPoint;
import net.lingala.zip4j.core.ZipFile;
import net.lingala.zip4j.exception.ZipException;
import org.apache.commons.io.FilenameUtils;
import org.apache.log4j.Logger;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class JSXGraphExportVisualization {
	final static Logger logger = Logger.getLogger(JSXGraphExportVisualization.class);
	final static String HTML_TEMPLATE_PATH = "Visualization/VisualizationTemplate.html";
	final static String JSXGRAPH_CORE_SOURCE_PATH = "Visualization/JSXGraphCore.zip";
	private JSXGraph jSXGraph;
	private String visualizationFilePath;

	public JSXGraphExportVisualization(JSXGraph jSXGraph, String visualizationFilePath) {
		this.jSXGraph = jSXGraph;
		setVisualizationFilePath(visualizationFilePath);
	}

	public void setJSXGraph(JSXGraph jSXGraph) {
		this.jSXGraph = jSXGraph;
	}

	public void setVisualizationFilePath(String visualizationFilePath) {
		if (!FilenameUtils.getExtension(visualizationFilePath).equals("html")) {
			visualizationFilePath += ".html";
		}
		this.visualizationFilePath = visualizationFilePath;
	}

	public JSXGraph getJSXGraph() {
		return this.jSXGraph;
	}

	public String getVisualizationFilePath() {
		return this.visualizationFilePath;
	}

	public void visualize() {
		List<JSXGraphElement> jsxGraphElements = getJSXGraph().getJSXGraphElements();
		String board = visualizeJSXGraphParameters(getParameters(jsxGraphElements), jsxGraphElements) + System.lineSeparator();
		board = board + "\t\t\tvar e = [];" + System.lineSeparator();
		for (JSXGraphElement jsxGraphElement : jsxGraphElements) {
			if (jsxGraphElement instanceof JSXGraphPoint) {
				jsxGraphElement.setProperties(JSXGraphElement.INDEPENDENT_POINT_PROP);
				board += visualizeJSXGraphPoint((JSXGraphPoint) jsxGraphElement);
				logger.info("point ID:" + jsxGraphElement.getID() + " has been visualized");
			} else if (jsxGraphElement instanceof JSXGraphMidPoint) {
				jsxGraphElement.setProperties(JSXGraphElement.DEPENDENT_POINT_PROP);
				board += visualizeJSXGraphMidPoint((JSXGraphMidPoint) jsxGraphElement);
				logger.info("midpoint ID:" + jsxGraphElement.getID() + " has been visualized");
			} else if (jsxGraphElement instanceof JSXGraphIntersection) {
				jsxGraphElement.setProperties(JSXGraphElement.DEPENDENT_POINT_PROP);
				board += visualizeJSXGraphIntersection((JSXGraphIntersection) jsxGraphElement);
				logger.info("intersection ID:" + jsxGraphElement.getID() + " has been visualized");
			} else if (jsxGraphElement instanceof JSXGraphVarPoint) {
				jsxGraphElement.setProperties(JSXGraphElement.DEPENDENT_POINT_PROP);
				board += visualizeJSXGraphVarPoint((JSXGraphVarPoint) jsxGraphElement);
				logger.info("varpoint ID:" + jsxGraphElement.getID() + " has been visualized");
			} else if (jsxGraphElement instanceof JSXGraphFixedPoint) {
				jsxGraphElement.setProperties(JSXGraphElement.DEPENDENT_POINT_PROP);
				board += visualizeJSXGraphFixedPoint((JSXGraphFixedPoint) jsxGraphElement);
				logger.info("fixedpoint ID:" + jsxGraphElement.getID() + " has been visualized");
			} else if (jsxGraphElement instanceof JSXGraphLineGlider) {
				jsxGraphElement.setProperties("");
				board += visualizeJSXGraphLineGlider((JSXGraphLineGlider) jsxGraphElement);
				logger.info("line_glider ID:" + jsxGraphElement.getID() + " has been visualized");
			} else if (jsxGraphElement instanceof JSXGraphCircleGlider) {
				jsxGraphElement.setProperties("");
				board += visualizeJSXGraphCircleGlider((JSXGraphCircleGlider) jsxGraphElement);
				logger.info("circle_glider ID:" + jsxGraphElement.getID() + " has been visualized");
			} else if (jsxGraphElement instanceof JSXGraphLine) {
				jsxGraphElement.setProperties(JSXGraphElement.INDEPENDENT_LINE_PROP);
				board += visualizeJSXGraphLine((JSXGraphLine) jsxGraphElement);
				logger.info("line ID:" + jsxGraphElement.getID() + " has been visualized");
			} else if (jsxGraphElement instanceof JSXGraphParallel) {
				jsxGraphElement.setProperties(JSXGraphElement.DEPENDENT_LINE_PROP);
				board += visualizeJSXGraphParallel((JSXGraphParallel) jsxGraphElement);
				logger.info("parallel ID:" + jsxGraphElement.getID() + " has been visualized");
			} else if (jsxGraphElement instanceof JSXGraphPerpendicular) {
				jsxGraphElement.setProperties(JSXGraphElement.DEPENDENT_LINE_PROP);
				board += visualizeJSXGraphPerpendicular((JSXGraphPerpendicular) jsxGraphElement);
				logger.info("perpendicular ID:" + jsxGraphElement.getID() + " has been visualized");
			} else if (jsxGraphElement instanceof JSXGraphP3Bisector) {
				jsxGraphElement.setProperties(JSXGraphElement.DEPENDENT_LINE_PROP);
				board += visualizeJSXGraphP3Bisector((JSXGraphP3Bisector) jsxGraphElement);
				logger.info("bisector ID:" + jsxGraphElement.getID() + " has been visualized");
			} else if (jsxGraphElement instanceof JSXGraphPCCircle) {
				jsxGraphElement.setProperties("");
				board += visualizeJSXGraphPCCircle((JSXGraphPCCircle) jsxGraphElement);
				logger.info("pccircle ID:" + jsxGraphElement.getID() + " has been visualized");
			} else if (jsxGraphElement instanceof JSXGraphCircumCircle) {
				jsxGraphElement.setProperties("");
				board += visualizeJSXGraphCircumCircle((JSXGraphCircumCircle) jsxGraphElement);
				logger.info("circumcircle ID:" + jsxGraphElement.getID() + " has been visualized");
			}
		}
		board += visualizeJSXGraphRelation(getParameters(jsxGraphElements), jsxGraphElements);
		String htmlContent = readHTMLTemplate().replace("TITLE_PATTERN", getJSXGraph().getTitle())
				.replace("BOARD_PATTERN", board);

		if (exportVisualization(htmlContent)) {
			logger.info("Visualization successfully completed");
			logger.info("Visualization has been saved in " + getVisualizationFilePath());
		} else {
			logger.error("Visualization failed");
		}
	}

	private String visualizeJSXGraphParameters(List<JSXGraphParameter> parameters,
			List<JSXGraphElement> jsxGraphElements) {
		String parameterVisualiztion = "";
		ArrayList<String> allParameters = new ArrayList<>();
		for (JSXGraphParameter parameter : parameters) {
			if (!parameter.isConstant()) {
				int yCoord = 26 - parameters.indexOf(parameter) * 3;
				parameterVisualiztion += "\t\t\tvar " + parameter.getID() + "= board.create('slider',[[40," + yCoord
						+ "],[60," + yCoord + "],[-20,0,20]],{name:'" + parameter.getID() + " ("
						+ getPointForParameter(parameter, jsxGraphElements) + ")" + "',snapWidth:-1});"
						+ System.lineSeparator();
				parameterVisualiztion += "\t\t\t" + parameter.getID() + ".setValue(" + parameter.getValue() + ");"
						+ System.lineSeparator();
				allParameters.add(parameter.getID());
			}
		}
		parameterVisualiztion += "\t\t\t" + "var parameters = ["
				+ String.join(", ", allParameters) + "];" + System.lineSeparator();
		return parameterVisualiztion;
	}

	private String getPointForParameter(final JSXGraphParameter parameter, final List<JSXGraphElement> jsxGraphElements) {
		String name = "";
		for (JSXGraphElement jsxGraphElement : jsxGraphElements) {
			if (jsxGraphElement instanceof JSXGraphPoint &&
					(((JSXGraphPoint) jsxGraphElement).getXElement().equals(parameter)
					|| (((JSXGraphPoint) jsxGraphElement).getYElement().equals(parameter)
					|| ((JSXGraphPoint) jsxGraphElement).getWElement().equals(parameter)))) {
				name = jsxGraphElement.getID();
			}
		}
		return name;
	}

	private String visualizeJSXGraphRelation(List<JSXGraphParameter> parameters,
			List<JSXGraphElement> jsxGraphElements) {
		String relation = System.lineSeparator();
		for (JSXGraphParameter parameter : parameters) {
			if (!parameter.isConstant()) {
				String parameterID = parameter.getID();
				String name = "";
				relation = relation + "\t\t\t" + parameterID + ".on('drag', function(){" + System.lineSeparator();
				for (JSXGraphElement jsxGraphElement : jsxGraphElements) {
					String newRelation = "";
					if (jsxGraphElement instanceof JSXGraphPoint) {
						newRelation = visualizeJSXGraphPointRelation(parameterID, (JSXGraphPoint) jsxGraphElement);
					} else if (jsxGraphElement instanceof JSXGraphVarPoint) {
						newRelation = visualizeJSXGraphVarPointRelation(parameterID, (JSXGraphVarPoint) jsxGraphElement);
					} else if (jsxGraphElement instanceof JSXGraphLineGlider) {
						newRelation = visualizeJSXGraphLineGliderRelation(parameterID,
								(JSXGraphLineGlider) jsxGraphElement);
					} else if (jsxGraphElement instanceof JSXGraphCircleGlider) {
						newRelation = visualizeJSXGraphCircleGliderRelation(parameterID,
								(JSXGraphCircleGlider) jsxGraphElement);
					}
					Matcher matcher = Pattern.compile("//name:(.*)").matcher(newRelation);
					if (matcher.find())
						name += matcher.group(1);
					relation += newRelation;
				}
				relation += "\t\t\t});" + System.lineSeparator();

				relation += "\t\t\t" + parameterID + ".setName('" + parameterID + " (" + name + ")')"
						+ System.lineSeparator();
			}
		}
		return relation;
	}

	private String visualizeJSXGraphPointRelation(String parameterID, JSXGraphPoint jsxGraphPoint) {
		String pointRelation = "";
		String xElementID = jsxGraphPoint.getXElement().getID();
		String yElementID = jsxGraphPoint.getYElement().getID();
		if (xElementID.equals(parameterID) || yElementID.equals(parameterID)) {
			xElementID = (xElementID.contains(JSXGraphParameter.CONST_IDENTITY)
					? xElementID.replace(JSXGraphParameter.CONST_IDENTITY, "")
					: xElementID + ".Value()");
			yElementID = (yElementID.contains(JSXGraphParameter.CONST_IDENTITY)
					? yElementID.replace(JSXGraphParameter.CONST_IDENTITY, "")
					: yElementID + ".Value()");
			pointRelation = "\t\t\t\te[" + getIndexByElement(jsxGraphPoint) + "].setPosition(JXG.COORDS_BY_USER,["
					+ xElementID + "," + yElementID + "]); //name:" + jsxGraphPoint.getID() + System.lineSeparator();
		}
		return pointRelation;
	}

	private String visualizeJSXGraphVarPointRelation(String parameterID, JSXGraphVarPoint jsxGraphVarPoint) {
		String varpointRelation = "";
		int point1Index = getIndexByElement(jsxGraphVarPoint.getPoint1());
		int point2Index = getIndexByElement(jsxGraphVarPoint.getPoint2());
		String varPointParameterID = jsxGraphVarPoint.getParameter().getID();
		if (varPointParameterID.equals(parameterID)) {
			varpointRelation = "\t\t\t\te[" + getIndexByElement(jsxGraphVarPoint) + "].setPosition(JXG.COORDS_BY_USER,["
					+ "getLineSliderX(e[" + point1Index + "].X(),e[" + point2Index + "].X()," + varPointParameterID
					+ ".Value()),getLineSliderY(e[" + point1Index + "].Y(),e[" + point2Index + "].Y(),"
					+ varPointParameterID + ".Value())]); //name:" + jsxGraphVarPoint.getID() + System.lineSeparator();
		}
		return varpointRelation;
	}

	private String visualizeJSXGraphLineGliderRelation(String parameterID, JSXGraphLineGlider jsxGraphLineGlider) {
		String lineGliderRelation = "";
		int lineIndex = getIndexByElement(jsxGraphLineGlider.getLine());
		String lineGliderParameterID = jsxGraphLineGlider.getParameter().getID();
		if (lineGliderParameterID.equals(parameterID)) {
			lineGliderParameterID = (lineGliderParameterID.contains(JSXGraphParameter.CONST_IDENTITY)
					? lineGliderParameterID.replace(JSXGraphParameter.CONST_IDENTITY, "")
					: lineGliderParameterID + ".Value()");
			String tempString = "e[" + lineIndex + "].point1.X(),e[" + lineIndex + "].point2.X(),e[" + lineIndex
					+ "].point1.Y(),e[" + lineIndex + "].point2.Y(),";
			lineGliderRelation = "\t\t\t\te[" + getIndexByElement(jsxGraphLineGlider)
					+ "].setPosition(JXG.COORDS_BY_USER,[" + "getLineSliderX(" + tempString + lineGliderParameterID
					+ "),getLineSliderY(" + tempString + lineGliderParameterID + ")]); //name:"
					+ jsxGraphLineGlider.getID() + System.lineSeparator();
		}
		return lineGliderRelation;
	}

	private String visualizeJSXGraphCircleGliderRelation(String parameterID,
			JSXGraphCircleGlider jsxGraphCircleGlider) {
		String circleGliderRelation = "";
		int circleIndex = getIndexByElement(jsxGraphCircleGlider.getCircle());
		String circleGliderParameterID = jsxGraphCircleGlider.getParameter().getID();
		if (circleGliderParameterID.equals(parameterID)) {
			circleGliderParameterID = (circleGliderParameterID.contains(JSXGraphParameter.CONST_IDENTITY)
					? circleGliderParameterID.replace(JSXGraphParameter.CONST_IDENTITY, "")
					: circleGliderParameterID + ".Value()");
			circleGliderRelation = "\t\t\t\te[" + getIndexByElement(jsxGraphCircleGlider)
					+ "].setPosition(JXG.COORDS_BY_USER,[" + "getCircleSliderX(e[" + circleIndex + "].center.X(),e["
					+ circleIndex + "].radius," + circleGliderParameterID + "),getCircleSliderY(e[" + circleIndex
					+ "].center.Y(),e[" + circleIndex + "].radius," + circleGliderParameterID + ")]) //name:"
					+ jsxGraphCircleGlider.getID() + System.lineSeparator();
		}
		return circleGliderRelation;
	}

	private String visualizeJSXGraphPoint(JSXGraphPoint jsxGraphPoint) {
		return "\t\t\te[" + getIndexByElement(jsxGraphPoint) + "] = board.create('point', [" + jsxGraphPoint.getW()
				+ "," + jsxGraphPoint.getX() + "," + jsxGraphPoint.getY() + "], {name:'" + jsxGraphPoint.getID() + "',"
				+ jsxGraphPoint.getProperties() + "})" + System.lineSeparator();
	}

	private String visualizeJSXGraphMidPoint(JSXGraphMidPoint jsxGraphMidPoint) {
		return "\t\t\te[" + getIndexByElement(jsxGraphMidPoint) + "] = board.create('midpoint', [e["
				+ getIndexByElement(jsxGraphMidPoint.getPoint1()) + "],e["
				+ getIndexByElement(jsxGraphMidPoint.getPoint2()) + "]], {name:'" + jsxGraphMidPoint.getID() + "',"
				+ jsxGraphMidPoint.getProperties() + "})" + System.lineSeparator();
	}

	private String visualizeJSXGraphIntersection(JSXGraphIntersection jsxGraphIntersection) {
		return "\t\t\te[" + getIndexByElement(jsxGraphIntersection) + "] = board.create('intersection', [e["
				+ getIndexByElement(jsxGraphIntersection.getElement1()) + "],e["
				+ getIndexByElement(jsxGraphIntersection.getElement2()) + "],0], {name:'" + jsxGraphIntersection.getID()
				+ "'," + jsxGraphIntersection.getProperties() + "})" + System.lineSeparator();
	}

	private String visualizeJSXGraphVarPoint(JSXGraphVarPoint jsxGraphVarPoint) {
		return "\t\t\te[" + getIndexByElement(jsxGraphVarPoint) + "] = board.create('point', ["
				+ jsxGraphVarPoint.getW() + "," + jsxGraphVarPoint.getX() + "," + jsxGraphVarPoint.getY() + "], {name:'"
				+ jsxGraphVarPoint.getID() + "'," + jsxGraphVarPoint.getProperties() + "})" + System.lineSeparator();
	}

	private String visualizeJSXGraphFixedPoint(JSXGraphFixedPoint jsxGraphFixedPoint) {
		return "\t\t\te[" + getIndexByElement(jsxGraphFixedPoint) + "] = board.create('point', ["
				+ jsxGraphFixedPoint.getW() + "," + jsxGraphFixedPoint.getX() + "," + jsxGraphFixedPoint.getY()
				+ "], {name:'" + jsxGraphFixedPoint.getID() + "'," + jsxGraphFixedPoint.getProperties() + "})"
				+ System.lineSeparator();
	}

	private String visualizeJSXGraphLineGlider(JSXGraphLineGlider jsxGraphLineGlider) {
		return "\t\t\te[" + getIndexByElement(jsxGraphLineGlider) + "] = board.create('glider', ["
				+ jsxGraphLineGlider.getX() + "," + jsxGraphLineGlider.getY() + ",e["
				+ getIndexByElement(jsxGraphLineGlider.getLine()) + "]], {name:'" + jsxGraphLineGlider.getID() + "',"
				+ jsxGraphLineGlider.getProperties() + "})" + System.lineSeparator();

	}

	private String visualizeJSXGraphCircleGlider(JSXGraphCircleGlider jsxGraphCircleGlider) {
		return "\t\t\te[" + getIndexByElement(jsxGraphCircleGlider) + "] = board.create('glider', ["
				+ jsxGraphCircleGlider.getX() + "," + jsxGraphCircleGlider.getY() + ",e["
				+ getIndexByElement(jsxGraphCircleGlider.getCircle()) + "]], {name:'" + jsxGraphCircleGlider.getID()
				+ "'," + jsxGraphCircleGlider.getProperties() + "})" + System.lineSeparator();

	}

	private String visualizeJSXGraphLine(JSXGraphLine jsxGraphLine) {
		return "\t\t\te[" + getIndexByElement(jsxGraphLine) + "] = board.create('line', [e["
				+ getIndexByElement(jsxGraphLine.getPoint1()) + "],e[" + getIndexByElement(jsxGraphLine.getPoint2())
				+ "]], {name:'" + jsxGraphLine.getID() + "'," + jsxGraphLine.getProperties() + "})"
				+ System.lineSeparator();
	}

	private String visualizeJSXGraphParallel(JSXGraphParallel jsxGraphParallel) {
		return "\t\t\te[" + getIndexByElement(jsxGraphParallel) + "] = board.create('parallel', [e["
				+ getIndexByElement(jsxGraphParallel.getLine()) + "],e["
				+ getIndexByElement(jsxGraphParallel.getPoint()) + "]], {name:'" + jsxGraphParallel.getID() + "',"
				+ jsxGraphParallel.getProperties() + "})" + System.lineSeparator();
	}

	private String visualizeJSXGraphPerpendicular(JSXGraphPerpendicular jsxGraphPerpendicular) {
		return "\t\t\te[" + getIndexByElement(jsxGraphPerpendicular) + "] = board.create('perpendicular', [e["
				+ getIndexByElement(jsxGraphPerpendicular.getLine()) + "],e["
				+ getIndexByElement(jsxGraphPerpendicular.getPoint()) + "]], {name:'" + jsxGraphPerpendicular.getID()
				+ "'," + jsxGraphPerpendicular.getProperties() + "})" + System.lineSeparator();
	}

	private String visualizeJSXGraphP3Bisector(JSXGraphP3Bisector jsxGraphP3Bisector) {
		return "\t\t\te[" + getIndexByElement(jsxGraphP3Bisector) + "] = board.create('bisector', [e["
				+ getIndexByElement(jsxGraphP3Bisector.getPoint1()) + "],e["
				+ getIndexByElement(jsxGraphP3Bisector.getPoint2()) + "],e["
				+ getIndexByElement(jsxGraphP3Bisector.getPoint3()) + "]], {name:'" + jsxGraphP3Bisector.getID() + "',"
				+ jsxGraphP3Bisector.getProperties() + "})" + System.lineSeparator();
	}

	private String visualizeJSXGraphPCCircle(JSXGraphPCCircle jsxGraphPCCircle) {
		return "\t\t\te[" + getIndexByElement(jsxGraphPCCircle) + "] = board.create('circle', [e["
				+ getIndexByElement(jsxGraphPCCircle.getCenterPoint()) + "],e["
				+ getIndexByElement(jsxGraphPCCircle.getThroughPoint()) + "]], {name:'" + jsxGraphPCCircle.getID() + "'"
				+ jsxGraphPCCircle.getProperties() + "})" + System.lineSeparator();
	}

	private String visualizeJSXGraphCircumCircle(JSXGraphCircumCircle jsxGraphCircumCircle) {
		return "\t\t\te[" + getIndexByElement(jsxGraphCircumCircle) + "] = board.create('circumcircle', [e["
				+ getIndexByElement(jsxGraphCircumCircle.getPoint1()) + "],e["
				+ getIndexByElement(jsxGraphCircumCircle.getPoint2()) + "],e["
				+ getIndexByElement(jsxGraphCircumCircle.getPoint3()) + "]], {name:'" + jsxGraphCircumCircle.getID()
				+ "'," + jsxGraphCircumCircle.getProperties() + "})" + System.lineSeparator();
	}

	private int getIndexByElement(JSXGraphElement jsxGraphElement) {
		return getJSXGraph().getJSXGraphElements().indexOf(jsxGraphElement);
	}

	private List<JSXGraphParameter> getParameters(List<JSXGraphElement> jsxGraphElements) {
		List<JSXGraphParameter> jsxGraphParamters = new ArrayList<JSXGraphParameter>();
		for (JSXGraphElement jsxGraphElement : jsxGraphElements) {
			if (jsxGraphElement instanceof JSXGraphParameter) {
				jsxGraphParamters.add((JSXGraphParameter) jsxGraphElement);
			}
		}
		return jsxGraphParamters;
	}

	private String readHTMLTemplate() {
		ClassLoader classLoader = getClass().getClassLoader();
		StringBuilder contentBuilder = new StringBuilder();

		try (BufferedReader bufferedReader = new BufferedReader(
				new InputStreamReader(classLoader.getResourceAsStream(HTML_TEMPLATE_PATH)))) {
			String line;
			while ((line = bufferedReader.readLine()) != null) {
				contentBuilder.append(line).append(System.lineSeparator());
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		return contentBuilder.toString();
	}

	private boolean exportJSXGraphCore() {
		try {
			InputStream inputStream = ClassLoader.getSystemClassLoader().getResourceAsStream(JSXGRAPH_CORE_SOURCE_PATH);
			if (inputStream == null) {
				return false;
			}

			File tempJSXGraphCoreFile = File.createTempFile(String.valueOf(inputStream.hashCode()), ".tmp");
			tempJSXGraphCoreFile.deleteOnExit();

			try (FileOutputStream fileOutputStream = new FileOutputStream(tempJSXGraphCoreFile)) {
				byte[] buffer = new byte[1024];
				int bytesRead;
				while ((bytesRead = inputStream.read(buffer)) != -1) {
					fileOutputStream.write(buffer, 0, bytesRead);
				}
			}
			ZipFile zipFile = new ZipFile(tempJSXGraphCoreFile.getAbsolutePath());
			zipFile.extractAll(
					FilenameUtils.getFullPathNoEndSeparator(new File(getVisualizationFilePath()).getAbsolutePath()));
		} catch (ZipException | IOException e) {
			e.printStackTrace();
			return false;
		}
		return true;
	}

	private boolean exportVisualization(String htmlContent) {
		if (!exportJSXGraphCore())
			return false;
		try (BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(getVisualizationFilePath()))) {
			bufferedWriter.write(htmlContent);
		} catch (IOException e) {
			e.printStackTrace();
			return false;
		}
		return true;
	}

}
