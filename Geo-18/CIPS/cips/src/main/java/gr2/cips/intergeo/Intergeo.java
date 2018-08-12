package gr2.cips.intergeo;

import gr2.cips.intergeo.model.IntergeoCircleByCenterAndPoint;
import gr2.cips.intergeo.model.IntergeoCircleByThreePoints;
import gr2.cips.intergeo.model.IntergeoElement;
import gr2.cips.intergeo.model.IntergeoFreePoint;
import gr2.cips.intergeo.model.IntergeoLineAngularBisectorOfThreePoints;
import gr2.cips.intergeo.model.IntergeoLineParallelToLineThroughPoint;
import gr2.cips.intergeo.model.IntergeoLinePerpendicularToLineThroughPoint;
import gr2.cips.intergeo.model.IntergeoLineThroughTwoPoints;
import gr2.cips.intergeo.model.IntergeoMidPointOfTwoPoints;
import gr2.cips.intergeo.model.IntergeoPointIntersectionOfTwoLines;
import gr2.cips.intergeo.model.IntergeoPointOnCircle;
import gr2.cips.intergeo.model.IntergeoPointOnLine;
import org.apache.commons.lang3.math.NumberUtils;
import org.apache.log4j.Logger;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.TransformerException;
import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class Intergeo {
	final static Logger logger = Logger.getLogger(Intergeo.class);
	private List<IntergeoElement> integeoElements;
	private String title;

	public Intergeo() {
		integeoElements = new ArrayList<IntergeoElement>();
	}

	public void setIntergeoElements(List<IntergeoElement> integeoElements) {
		this.integeoElements = integeoElements;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public List<IntergeoElement> getIntegeoElements() {
		return this.integeoElements;
	}

	public String getTitle() {
		return this.title;
	}

	public boolean loadFromFile(String intergeoFilePath) throws IOException {
		try {
			File intergeoFile = new File(intergeoFilePath);
			DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
			DocumentBuilder documentBuilder = documentBuilderFactory.newDocumentBuilder();
			Document document = documentBuilder.parse(intergeoFile);

			document.getDocumentElement().normalize();

			Path path = Paths.get(intergeoFilePath);
			setTitle(path.getFileName().toString());

			if (document.getElementsByTagName("elements").getLength() == 1) {
				NodeList elementsChildNodes = document.getElementsByTagName("elements").item(0).getChildNodes();
				for (int i = 0; i < elementsChildNodes.getLength(); i++) {
					if (elementsChildNodes.item(i).getNodeName().equals("point")) {
						IntergeoFreePoint intergeoFreePoint = parseFreePoint(elementsChildNodes.item(i));
						if (intergeoFreePoint != null) {
							addElement(intergeoFreePoint);
							logger.info("Found free_point: ID:" + intergeoFreePoint.getID() + ", "
									+ intergeoFreePoint.toString());
						} else {
							logger.error("Error while parsing free_point: ID:"
									+ elementsChildNodes.item(i).getAttributes().getNamedItem("id").getNodeValue());
							return false;
						}

					}
				}
			}

			if (document.getElementsByTagName("constraints").getLength() == 1) {
				NodeList constraintsChildNodes = document.getElementsByTagName("constraints").item(0).getChildNodes();
				for (int i = 0; i < constraintsChildNodes.getLength(); i++) {
					if (constraintsChildNodes.item(i).getNodeName().equals("midpoint_of_two_points")) {
						IntergeoMidPointOfTwoPoints intergeoMidPointOfTwoPoints = parseMidPointOfTwoPoints(
								constraintsChildNodes.item(i));
						if (intergeoMidPointOfTwoPoints != null) {
							removeElementByID(intergeoMidPointOfTwoPoints.getID());
							addElement(intergeoMidPointOfTwoPoints);
							logger.info("Found midpoint_of_two_points: ID:" + intergeoMidPointOfTwoPoints.getID() + ", "
									+ intergeoMidPointOfTwoPoints.toString());
						} else {
							logger.error("Error while parsing midpoint_of_two_points: ID:"
									+ constraintsChildNodes.item(i).getAttributes().getNamedItem("id").getNodeValue());
							return false;
						}
					} else if (constraintsChildNodes.item(i).getNodeName().equals("point_intersection_of_two_lines")) {
						IntergeoPointIntersectionOfTwoLines intergeoPointIntersectionOfTwoLines = parsePointIntersectionOfTwoLines(
								constraintsChildNodes.item(i));
						if (intergeoPointIntersectionOfTwoLines != null) {
							removeElementByID(intergeoPointIntersectionOfTwoLines.getID());
							addElement(intergeoPointIntersectionOfTwoLines);
							logger.info("Found point_intersection_of_two_lines: ID:"
									+ intergeoPointIntersectionOfTwoLines.getID() + ", "
									+ intergeoPointIntersectionOfTwoLines.toString());
						} else {
							logger.error("Error while parsing point_intersection_of_two_lines: ID:"
									+ constraintsChildNodes.item(i).getAttributes().getNamedItem("id").getNodeValue());
							return false;
						}
					} else if (constraintsChildNodes.item(i).getNodeName().equals("point_on_circle")) {
						IntergeoPointOnCircle intergeoPointOnCircle = parsePointOnCircle(constraintsChildNodes.item(i));
						if (intergeoPointOnCircle != null) {
							removeElementByID(intergeoPointOnCircle.getID());
							addElement(intergeoPointOnCircle);
							logger.info("Found point_on_circle: ID:" + intergeoPointOnCircle.getID() + ", "
									+ intergeoPointOnCircle.toString());
						} else {
							logger.error("Error while parsing point_on_circle: ID:"
									+ constraintsChildNodes.item(i).getAttributes().getNamedItem("id").getNodeValue());
							return false;
						}
					} else if (constraintsChildNodes.item(i).getNodeName().equals("point_on_line")) {
						IntergeoPointOnLine intergeoPointOnLine = parsePointOnLine(constraintsChildNodes.item(i));
						if (intergeoPointOnLine != null) {
							removeElementByID(intergeoPointOnLine.getID());
							addElement(intergeoPointOnLine);
							logger.info("Found point_on_line: ID:" + intergeoPointOnLine.getID() + ", "
									+ intergeoPointOnLine.toString());
						} else {
							logger.error("Error while parsing point_on_line: ID:"
									+ constraintsChildNodes.item(i).getAttributes().getNamedItem("id").getNodeValue());
							return false;
						}
					}

					else if (constraintsChildNodes.item(i).getNodeName().equals("line_through_two_points")) {
						IntergeoLineThroughTwoPoints intergeoLineThroughTwoPoints = parseLineThroughTwoPoints(
								constraintsChildNodes.item(i));
						if (intergeoLineThroughTwoPoints != null) {
							addElement(intergeoLineThroughTwoPoints);
							logger.info("Found line_through_two_points: ID:" + intergeoLineThroughTwoPoints.getID()
									+ ", " + intergeoLineThroughTwoPoints.toString());
						} else {
							logger.error("Error while parsing line_through_two_points: ID:"
									+ constraintsChildNodes.item(i).getAttributes().getNamedItem("id").getNodeValue());
							return false;
						}
					} else if (constraintsChildNodes.item(i).getNodeName()
							.equals("line_parallel_to_line_through_point")) {
						IntergeoLineParallelToLineThroughPoint intergeoLineParallelToLineThroughPoint = parseLineParallelToLineThroughPoint(
								constraintsChildNodes.item(i));
						if (intergeoLineParallelToLineThroughPoint != null) {
							addElement(intergeoLineParallelToLineThroughPoint);
							logger.info("Found line_parallel_to_line_through_point: ID:"
									+ intergeoLineParallelToLineThroughPoint.getID() + ", "
									+ intergeoLineParallelToLineThroughPoint.toString());
						} else {
							logger.error("Error while parsing line_parallel_to_line_through_point: ID:"
									+ constraintsChildNodes.item(i).getAttributes().getNamedItem("id").getNodeValue());
							return false;
						}
					} else if (constraintsChildNodes.item(i).getNodeName()
							.equals("line_perpendicular_to_line_through_point")) {
						IntergeoLinePerpendicularToLineThroughPoint intergeoLinePerpendicularToLineThroughPoint = parseIntergeoLinePerpendicularToLineThroughPoint(
								constraintsChildNodes.item(i));
						if (intergeoLinePerpendicularToLineThroughPoint != null) {
							addElement(intergeoLinePerpendicularToLineThroughPoint);
							logger.info("Found line_perpendicular_to_line_through_point: ID:"
									+ intergeoLinePerpendicularToLineThroughPoint.getID() + ", "
									+ intergeoLinePerpendicularToLineThroughPoint.toString());
						} else {
							logger.error("Error while parsing line_perpendicular_to_line_through_point: ID:"
									+ constraintsChildNodes.item(i).getAttributes().getNamedItem("id").getNodeValue());
							return false;
						}
					} else if (constraintsChildNodes.item(i).getNodeName()
							.equals("line_angular_bisector_of_three_points")) {
						IntergeoLineAngularBisectorOfThreePoints intergeoLineAngularBisectorOfThreePoints = parseLineAngularBisectorOfThreePoints(
								constraintsChildNodes.item(i));
						if (intergeoLineAngularBisectorOfThreePoints != null) {
							addElement(intergeoLineAngularBisectorOfThreePoints);
							logger.info("Found line_angular_bisector_of_three_points: ID:"
									+ intergeoLineAngularBisectorOfThreePoints.getID() + ", "
									+ intergeoLineAngularBisectorOfThreePoints.toString());
						} else {
							logger.error("Error while parsing line_angular_bisector_of_three_points: ID:"
									+ constraintsChildNodes.item(i).getAttributes().getNamedItem("id").getNodeValue());
							return false;
						}
					} else if (constraintsChildNodes.item(i).getNodeName().equals("circle_by_center_and_point")) {
						IntergeoCircleByCenterAndPoint intergeoCircleByCenterAndPoint = parseCircleByCenterAndPoint(
								constraintsChildNodes.item(i));
						if (intergeoCircleByCenterAndPoint != null) {
							addElement(intergeoCircleByCenterAndPoint);
							logger.info("Found circle_by_center_and_point: ID:" + intergeoCircleByCenterAndPoint.getID()
									+ ", " + intergeoCircleByCenterAndPoint.toString());
						} else {
							logger.error("Error while parsing circle_by_center_and_point: ID:"
									+ constraintsChildNodes.item(i).getAttributes().getNamedItem("id").getNodeValue());
							return false;
						}
					} else if (constraintsChildNodes.item(i).getNodeName().equals("circle_by_three_points")) {
						IntergeoCircleByThreePoints intergeoCircleByThreePoints = parseCircleByThreePoints(
								constraintsChildNodes.item(i));
						if (intergeoCircleByThreePoints != null) {
							addElement(intergeoCircleByThreePoints);
							logger.info("Found circle_by_three_points: ID:" + intergeoCircleByThreePoints.getID() + ", "
									+ intergeoCircleByThreePoints.toString());
						} else {
							logger.error("Error while parsing circle_by_three_points: ID:"
									+ constraintsChildNodes.item(i).getAttributes().getNamedItem("id").getNodeValue());
							return false;
						}
					}
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
			return false;
		}
		return true;
	}

	public IntergeoFreePoint parseFreePoint(Node rawNode) {
		if (rawNode.getChildNodes().getLength() == 3) {
			if (rawNode.getChildNodes().item(1).getNodeName().equals("homogeneous_coordinates")) {
				NodeList doubleList = rawNode.getChildNodes().item(1).getChildNodes();
				if (doubleList.getLength() == 7) {
					String id = rawNode.getAttributes().getNamedItem("id").getNodeValue();
					double x = NumberUtils.toDouble(doubleList.item(1).getFirstChild().getNodeValue());
					double y = NumberUtils.toDouble(doubleList.item(3).getFirstChild().getNodeValue());
					return new IntergeoFreePoint(id, x, y, 1.0);
				}
			}
		}
		return null;
	}

	public IntergeoMidPointOfTwoPoints parseMidPointOfTwoPoints(Node rawNode) {
		if (rawNode.getChildNodes().getLength() == 7) {
			String id = rawNode.getChildNodes().item(1).getFirstChild().getNodeValue();
			IntergeoElement point1 = getElementByID(rawNode.getChildNodes().item(3).getFirstChild().getNodeValue());
			IntergeoElement point2 = getElementByID(rawNode.getChildNodes().item(5).getFirstChild().getNodeValue());
			return new IntergeoMidPointOfTwoPoints(id, point1, point2);
		}
		return null;
	}

	public IntergeoPointIntersectionOfTwoLines parsePointIntersectionOfTwoLines(Node rawNode) {
		if (rawNode.getChildNodes().getLength() == 7) {
			String id = rawNode.getChildNodes().item(1).getFirstChild().getNodeValue();
			IntergeoElement line1 = getElementByID(rawNode.getChildNodes().item(3).getFirstChild().getNodeValue());
			IntergeoElement line2 = getElementByID(rawNode.getChildNodes().item(5).getFirstChild().getNodeValue());
			return new IntergeoPointIntersectionOfTwoLines(id, line1, line2);
		}
		return null;
	}

	public IntergeoPointOnCircle parsePointOnCircle(Node rawNode) {
		if (rawNode.getChildNodes().getLength() == 5) {
			String id = rawNode.getChildNodes().item(1).getFirstChild().getNodeValue();
			IntergeoElement point = getElementByID(id);
			IntergeoElement circle = getElementByID(rawNode.getChildNodes().item(3).getFirstChild().getNodeValue());
			return new IntergeoPointOnCircle(id, circle, point.getX(), point.getY(), 1.0);
		}
		return null;
	}

	public IntergeoPointOnLine parsePointOnLine(Node rawNode) {
		if (rawNode.getChildNodes().getLength() == 5) {
			String id = rawNode.getChildNodes().item(1).getFirstChild().getNodeValue();
			IntergeoElement point = getElementByID(id);
			IntergeoElement line = getElementByID(rawNode.getChildNodes().item(3).getFirstChild().getNodeValue());
			return new IntergeoPointOnLine(id, line, point.getX(), point.getY(), 1.0);
		}
		return null;
	}

	public IntergeoLineThroughTwoPoints parseLineThroughTwoPoints(Node rawNode) {
		if (rawNode.getChildNodes().getLength() == 7) {
			String id = rawNode.getChildNodes().item(1).getFirstChild().getNodeValue();
			IntergeoElement point1 = getElementByID(rawNode.getChildNodes().item(3).getFirstChild().getNodeValue());
			IntergeoElement point2 = getElementByID(rawNode.getChildNodes().item(5).getFirstChild().getNodeValue());
			return new IntergeoLineThroughTwoPoints(id, point1, point2);
		}
		return null;
	}

	public IntergeoLineParallelToLineThroughPoint parseLineParallelToLineThroughPoint(Node rawNode) {
		if (rawNode.getChildNodes().getLength() == 7) {
			String id = rawNode.getChildNodes().item(1).getFirstChild().getNodeValue();
			IntergeoElement point = getElementByID(rawNode.getChildNodes().item(3).getFirstChild().getNodeValue());
			IntergeoElement line = getElementByID(rawNode.getChildNodes().item(5).getFirstChild().getNodeValue());
			return new IntergeoLineParallelToLineThroughPoint(id, point, line);
		}
		return null;
	}

	public IntergeoLinePerpendicularToLineThroughPoint parseIntergeoLinePerpendicularToLineThroughPoint(Node rawNode) {
		if (rawNode.getChildNodes().getLength() == 7) {
			String id = rawNode.getChildNodes().item(1).getFirstChild().getNodeValue();
			IntergeoElement point = getElementByID(rawNode.getChildNodes().item(3).getFirstChild().getNodeValue());
			IntergeoElement line = getElementByID(rawNode.getChildNodes().item(5).getFirstChild().getNodeValue());
			return new IntergeoLinePerpendicularToLineThroughPoint(id, point, line);
		}
		return null;
	}

	public IntergeoLineAngularBisectorOfThreePoints parseLineAngularBisectorOfThreePoints(Node rawNode) {
		if (rawNode.getChildNodes().getLength() == 9) {
			String id = rawNode.getChildNodes().item(1).getFirstChild().getNodeValue();
			IntergeoElement point1 = getElementByID(rawNode.getChildNodes().item(3).getFirstChild().getNodeValue());
			IntergeoElement point2 = getElementByID(rawNode.getChildNodes().item(5).getFirstChild().getNodeValue());
			IntergeoElement point3 = getElementByID(rawNode.getChildNodes().item(7).getFirstChild().getNodeValue());
			return new IntergeoLineAngularBisectorOfThreePoints(id, point1, point2, point3);
		}
		return null;
	}

	public IntergeoCircleByCenterAndPoint parseCircleByCenterAndPoint(Node rawNode) {
		if (rawNode.getChildNodes().getLength() == 7) {
			String id = rawNode.getChildNodes().item(1).getFirstChild().getNodeValue();
			IntergeoElement centerPoint = getElementByID(
					rawNode.getChildNodes().item(3).getFirstChild().getNodeValue());
			IntergeoElement throughPoint = getElementByID(
					rawNode.getChildNodes().item(5).getFirstChild().getNodeValue());
			return new IntergeoCircleByCenterAndPoint(id, centerPoint, throughPoint);
		}
		return null;
	}

	public IntergeoCircleByThreePoints parseCircleByThreePoints(Node rawNode) {
		if (rawNode.getChildNodes().getLength() == 9) {
			String id = rawNode.getChildNodes().item(1).getFirstChild().getNodeValue();
			IntergeoElement point1 = getElementByID(rawNode.getChildNodes().item(3).getFirstChild().getNodeValue());
			IntergeoElement point2 = getElementByID(rawNode.getChildNodes().item(5).getFirstChild().getNodeValue());
			IntergeoElement point3 = getElementByID(rawNode.getChildNodes().item(7).getFirstChild().getNodeValue());
			return new IntergeoCircleByThreePoints(id, point1, point2, point3);
		}
		return null;
	}

	public void addElement(IntergeoElement intergeoElement) {
		this.integeoElements.add(intergeoElement);
	}

	public IntergeoElement getElementByID(String id) {
		for (IntergeoElement intergeoElement : integeoElements) {
			if (intergeoElement.getID().equals(id)) {
				return intergeoElement;
			}
		}
		return null;
	}

	public void removeElementByID(String id) {
		integeoElements.remove(getElementByID(id));
	}

	public void exportXML(String xmlFilePath) throws TransformerException {
		IntergeoExportXML intergeoExportXML = new IntergeoExportXML(this, xmlFilePath);
		if (intergeoExportXML.export()) {
			logger.info("File has been saved in " + xmlFilePath);
		}
	}
}
