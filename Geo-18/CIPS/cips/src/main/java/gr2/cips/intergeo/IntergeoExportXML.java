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
import org.w3c.dom.Document;
import org.w3c.dom.Element;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import java.io.File;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class IntergeoExportXML {
	private Intergeo intergeo;
	private String xmlFilePath;
	private Element xmlRootElement;
	private Element xmlElements;
	private Element xmlConstraints;
	private DocumentBuilderFactory docFactory;
	private DocumentBuilder docBuilder;
	private Document doc;

	public IntergeoExportXML(Intergeo intergeo, String xmlFilePath) {
		this.intergeo = intergeo;
		this.xmlFilePath = xmlFilePath;

		try {
			docFactory = DocumentBuilderFactory.newInstance();
			docBuilder = docFactory.newDocumentBuilder();
			doc = docBuilder.newDocument();

			xmlRootElement = doc.createElement("construction");
			doc.appendChild(xmlRootElement);

			xmlElements = doc.createElement("elements");
			xmlRootElement.appendChild(xmlElements);
			xmlConstraints = doc.createElement("constraints");
			xmlRootElement.appendChild(xmlConstraints);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public boolean export() throws TransformerException {
		for (IntergeoElement intergeoElement : intergeo.getIntegeoElements()) {
			if (intergeoElement instanceof IntergeoFreePoint) {
				appendXMLFreePoint((IntergeoFreePoint) intergeoElement);
			} else if (intergeoElement instanceof IntergeoPointIntersectionOfTwoLines) {
				appendXMLIntergeoPointIntersectionOfTwoLines((IntergeoPointIntersectionOfTwoLines) intergeoElement);
			} else if (intergeoElement instanceof IntergeoMidPointOfTwoPoints) {
				appendXMLIntergeoMidPointOfTwoPoints((IntergeoMidPointOfTwoPoints) intergeoElement);
			} else if (intergeoElement instanceof IntergeoPointOnCircle) {
				appendXMLIntergeoPointOnCircle((IntergeoPointOnCircle) intergeoElement);
			} else if (intergeoElement instanceof IntergeoPointOnLine) {
				appendXMLIntergeoPointLine((IntergeoPointOnLine) intergeoElement);
			} else if (intergeoElement instanceof IntergeoLineThroughTwoPoints) {
				appendXMLIntergeoLineThroughTwoPoints((IntergeoLineThroughTwoPoints) intergeoElement);
			} else if (intergeoElement instanceof IntergeoLineParallelToLineThroughPoint) {
				appendXMLIntergeoLineParallelToLineThroughPoint(
						(IntergeoLineParallelToLineThroughPoint) intergeoElement);
			} else if (intergeoElement instanceof IntergeoLinePerpendicularToLineThroughPoint) {
				appendXMLIntergeoLinePerpendicularToLineThroughPoint(
						(IntergeoLinePerpendicularToLineThroughPoint) intergeoElement);
			} else if (intergeoElement instanceof IntergeoLineAngularBisectorOfThreePoints) {
				appendXMLIntergeoLineAngularBisectorOfThreePoints(
						(IntergeoLineAngularBisectorOfThreePoints) intergeoElement);
			} else if (intergeoElement instanceof IntergeoCircleByCenterAndPoint) {
				appendXMLIntergeoCircleByCenterAndPoint((IntergeoCircleByCenterAndPoint) intergeoElement);
			} else if (intergeoElement instanceof IntergeoCircleByThreePoints) {
				appendXMLIntergeoCircleByThreePoints((IntergeoCircleByThreePoints) intergeoElement);
			}
		}

		TransformerFactory transformerFactory = TransformerFactory.newInstance();
		Transformer transformer = transformerFactory.newTransformer();
		DOMSource source = new DOMSource(doc);
		StreamResult result = new StreamResult(new File(xmlFilePath));
		transformer.setOutputProperty(OutputKeys.INDENT, "yes");
		transformer.setOutputProperty("{http://xml.apache.org/xslt}indent-amount", "2");
		transformer.transform(source, result);

		return true;
	}

	private void appendXMLFreePoint(IntergeoFreePoint intergeoFreePoint) {
		Element xmlPointE = doc.createElement("point");
		xmlPointE.setAttribute("id", intergeoFreePoint.getID());
		Element xmlHomogeneousCoordinates = doc.createElement("homogeneous_coordinates");
		Element xmlDoubleX = doc.createElement("double");
		xmlDoubleX.appendChild(doc.createTextNode("" + intergeoFreePoint.getX()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleX);
		Element xmlDoubleY = doc.createElement("double");
		xmlDoubleY.appendChild(doc.createTextNode("" + intergeoFreePoint.getY()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleY);
		Element xmlDoubleW = doc.createElement("double");
		xmlDoubleW.appendChild(doc.createTextNode("" + intergeoFreePoint.getW()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleW);
		xmlPointE.appendChild(xmlHomogeneousCoordinates);
		xmlElements.appendChild(xmlPointE);

		Element xmlFree_Point = doc.createElement("free_point");
		Element xmlPointC = doc.createElement("point");
		xmlPointC.setAttribute("out", "true");
		xmlPointC.appendChild(doc.createTextNode(intergeoFreePoint.getID()));
		xmlFree_Point.appendChild(xmlPointC);
		xmlConstraints.appendChild(xmlFree_Point);
	}

	private void appendXMLIntergeoPointIntersectionOfTwoLines(
		IntergeoPointIntersectionOfTwoLines intergeoPointIntersectionOfTwoLines) {
		Element xmlPointE = doc.createElement("point");
		xmlPointE.setAttribute("id", intergeoPointIntersectionOfTwoLines.getID());
		Element xmlHomogeneousCoordinates = doc.createElement("homogeneous_coordinates");
		Element xmlDoubleX = doc.createElement("double");
		xmlDoubleX.appendChild(doc.createTextNode("" + intergeoPointIntersectionOfTwoLines.getX()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleX);
		Element xmlDoubleY = doc.createElement("double");
		xmlDoubleY.appendChild(doc.createTextNode("" + intergeoPointIntersectionOfTwoLines.getY()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleY);
		Element xmlDoubleW = doc.createElement("double");
		xmlDoubleW.appendChild(doc.createTextNode("" + intergeoPointIntersectionOfTwoLines.getW()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleW);
		xmlPointE.appendChild(xmlHomogeneousCoordinates);
		xmlElements.appendChild(xmlPointE);

		Element xmlPointIntersectionOfTwoLines = doc.createElement("point_intersection_of_two_lines");
		Element xmlPointC = doc.createElement("point");
		xmlPointC.setAttribute("out", "true");
		xmlPointC.appendChild(doc.createTextNode(intergeoPointIntersectionOfTwoLines.getID()));
		Element xmlLine1 = doc.createElement("line");
		xmlLine1.appendChild(doc.createTextNode(intergeoPointIntersectionOfTwoLines.getLine1().getID()));
		Element xmlLine2 = doc.createElement("line");
		xmlLine2.appendChild(doc.createTextNode(intergeoPointIntersectionOfTwoLines.getLine2().getID()));
		xmlPointIntersectionOfTwoLines.appendChild(xmlPointC);
		xmlPointIntersectionOfTwoLines.appendChild(xmlLine1);
		xmlPointIntersectionOfTwoLines.appendChild(xmlLine2);
		xmlConstraints.appendChild(xmlPointIntersectionOfTwoLines);
	}

	private void appendXMLIntergeoMidPointOfTwoPoints(IntergeoMidPointOfTwoPoints intergeoMidPointOfTwoPoints) {
		Element xmlPointE = doc.createElement("point");
		xmlPointE.setAttribute("id", intergeoMidPointOfTwoPoints.getID());
		Element xmlHomogeneousCoordinates = doc.createElement("homogeneous_coordinates");
		Element xmlDoubleX = doc.createElement("double");
		xmlDoubleX.appendChild(doc.createTextNode("" + intergeoMidPointOfTwoPoints.getX()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleX);
		Element xmlDoubleY = doc.createElement("double");
		xmlDoubleY.appendChild(doc.createTextNode("" + intergeoMidPointOfTwoPoints.getY()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleY);
		Element xmlDoubleW = doc.createElement("double");
		xmlDoubleW.appendChild(doc.createTextNode("" + intergeoMidPointOfTwoPoints.getW()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleW);
		xmlPointE.appendChild(xmlHomogeneousCoordinates);
		xmlElements.appendChild(xmlPointE);

		Element xmlMidpointOfTwoPoints = doc.createElement("midpoint_of_two_points");
		Element xmlPointC = doc.createElement("point");
		xmlPointC.setAttribute("out", "true");
		xmlPointC.appendChild(doc.createTextNode(intergeoMidPointOfTwoPoints.getID()));
		Element xmlPoint1 = doc.createElement("point");
		xmlPoint1.appendChild(doc.createTextNode(intergeoMidPointOfTwoPoints.getPoint1().getID()));
		Element xmlPoint2 = doc.createElement("point");
		xmlPoint2.appendChild(doc.createTextNode(intergeoMidPointOfTwoPoints.getPoint2().getID()));
		xmlMidpointOfTwoPoints.appendChild(xmlPointC);
		xmlMidpointOfTwoPoints.appendChild(xmlPoint1);
		xmlMidpointOfTwoPoints.appendChild(xmlPoint2);
		xmlConstraints.appendChild(xmlMidpointOfTwoPoints);
	}

	private void appendXMLIntergeoPointOnCircle(IntergeoPointOnCircle intergeoPointOnCircle) {
		Element xmlPointE = doc.createElement("point");
		xmlPointE.setAttribute("id", intergeoPointOnCircle.getID());
		Element xmlHomogeneousCoordinates = doc.createElement("homogeneous_coordinates");
		Element xmlDoubleX = doc.createElement("double");
		xmlDoubleX.appendChild(doc.createTextNode("" + intergeoPointOnCircle.getX()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleX);
		Element xmlDoubleY = doc.createElement("double");
		xmlDoubleY.appendChild(doc.createTextNode("" + intergeoPointOnCircle.getY()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleY);
		Element xmlDoubleW = doc.createElement("double");
		xmlDoubleW.appendChild(doc.createTextNode("" + intergeoPointOnCircle.getW()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleW);
		xmlPointE.appendChild(xmlHomogeneousCoordinates);
		xmlElements.appendChild(xmlPointE);

		Element xmlPointOnCircle = doc.createElement("point_on_circle");
		Element xmlPointC = doc.createElement("point");
		xmlPointC.setAttribute("out", "true");
		xmlPointC.appendChild(doc.createTextNode(intergeoPointOnCircle.getID()));
		Element xmlCircle = doc.createElement("circle");
		xmlCircle.appendChild(doc.createTextNode(intergeoPointOnCircle.getCircle().getID()));
		xmlPointOnCircle.appendChild(xmlPointC);
		xmlPointOnCircle.appendChild(xmlCircle);
		xmlConstraints.appendChild(xmlPointOnCircle);
	}

	private void appendXMLIntergeoPointLine(IntergeoPointOnLine intergeoPointOnLine) {
		Element xmlPointE = doc.createElement("point");
		xmlPointE.setAttribute("id", intergeoPointOnLine.getID());
		Element xmlHomogeneousCoordinates = doc.createElement("homogeneous_coordinates");
		Element xmlDoubleX = doc.createElement("double");
		xmlDoubleX.appendChild(doc.createTextNode("" + intergeoPointOnLine.getX()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleX);
		Element xmlDoubleY = doc.createElement("double");
		xmlDoubleY.appendChild(doc.createTextNode("" + intergeoPointOnLine.getY()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleY);
		Element xmlDoubleW = doc.createElement("double");
		xmlDoubleW.appendChild(doc.createTextNode("" + intergeoPointOnLine.getW()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleW);
		xmlPointE.appendChild(xmlHomogeneousCoordinates);
		xmlElements.appendChild(xmlPointE);

		Element xmlPointOnLine = doc.createElement("point_on_line");
		Element xmlPointC = doc.createElement("point");
		xmlPointC.setAttribute("out", "true");
		xmlPointC.appendChild(doc.createTextNode(intergeoPointOnLine.getID()));
		Element xmlLine = doc.createElement("line");
		xmlLine.appendChild(doc.createTextNode(intergeoPointOnLine.getLine().getID()));
		xmlPointOnLine.appendChild(xmlPointC);
		xmlPointOnLine.appendChild(xmlLine);
		xmlConstraints.appendChild(xmlPointOnLine);
	}

	private void appendXMLIntergeoLineThroughTwoPoints(IntergeoLineThroughTwoPoints intergeoLineThroughTwoPoints) {
		Element xmlLineE = doc.createElement("line");
		xmlLineE.setAttribute("id", intergeoLineThroughTwoPoints.getID());
		Element xmlHomogeneousCoordinates = doc.createElement("homogeneous_coordinates");
		Element xmlDoubleX = doc.createElement("double");
		xmlDoubleX.appendChild(doc.createTextNode("" + intergeoLineThroughTwoPoints.getA()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleX);
		Element xmlDoubleY = doc.createElement("double");
		xmlDoubleY.appendChild(doc.createTextNode("" + intergeoLineThroughTwoPoints.getB()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleY);
		Element xmlDoubleW = doc.createElement("double");
		xmlDoubleW.appendChild(doc.createTextNode("" + intergeoLineThroughTwoPoints.getC()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleW);
		xmlLineE.appendChild(xmlHomogeneousCoordinates);
		xmlElements.appendChild(xmlLineE);

		Element xmlLineThroughTwoPoints = doc.createElement("line_through_two_points");
		Element xmlLineC = doc.createElement("line");
		xmlLineC.setAttribute("out", "true");
		xmlLineC.appendChild(doc.createTextNode(intergeoLineThroughTwoPoints.getID()));
		Element xmlPoint1 = doc.createElement("point");
		xmlPoint1.appendChild(doc.createTextNode(intergeoLineThroughTwoPoints.getPoint1().getID()));
		Element xmlPoint2 = doc.createElement("point");
		xmlPoint2.appendChild(doc.createTextNode(intergeoLineThroughTwoPoints.getPoint2().getID()));
		xmlLineThroughTwoPoints.appendChild(xmlLineC);
		xmlLineThroughTwoPoints.appendChild(xmlPoint1);
		xmlLineThroughTwoPoints.appendChild(xmlPoint2);
		xmlConstraints.appendChild(xmlLineThroughTwoPoints);
	}

	public void appendXMLIntergeoLineParallelToLineThroughPoint(
			IntergeoLineParallelToLineThroughPoint intergeoLineParallelToLineThroughPoint) {
		Element xmlLineE = doc.createElement("line");
		xmlLineE.setAttribute("id", intergeoLineParallelToLineThroughPoint.getID());
		Element xmlHomogeneousCoordinates = doc.createElement("homogeneous_coordinates");
		Element xmlDoubleX = doc.createElement("double");
		xmlDoubleX.appendChild(doc.createTextNode("" + intergeoLineParallelToLineThroughPoint.getA()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleX);
		Element xmlDoubleY = doc.createElement("double");
		xmlDoubleY.appendChild(doc.createTextNode("" + intergeoLineParallelToLineThroughPoint.getB()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleY);
		Element xmlDoubleW = doc.createElement("double");
		xmlDoubleW.appendChild(doc.createTextNode("" + intergeoLineParallelToLineThroughPoint.getC()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleW);
		xmlLineE.appendChild(xmlHomogeneousCoordinates);
		xmlElements.appendChild(xmlLineE);

		Element xmlLineParallelToLineThroughPoint = doc.createElement("line_parallel_to_line_through_point");
		Element xmlLineC = doc.createElement("line");
		xmlLineC.setAttribute("out", "true");
		xmlLineC.appendChild(doc.createTextNode(intergeoLineParallelToLineThroughPoint.getID()));
		Element xmlPointC = doc.createElement("point");
		xmlPointC.appendChild(doc.createTextNode(intergeoLineParallelToLineThroughPoint.getPoint().getID()));
		Element xmlLineParallelC = doc.createElement("line");
		xmlLineParallelC.appendChild(doc.createTextNode(intergeoLineParallelToLineThroughPoint.getLine().getID()));
		xmlLineParallelToLineThroughPoint.appendChild(xmlLineC);
		xmlLineParallelToLineThroughPoint.appendChild(xmlPointC);
		xmlLineParallelToLineThroughPoint.appendChild(xmlLineParallelC);
		xmlConstraints.appendChild(xmlLineParallelToLineThroughPoint);
	}

	public void appendXMLIntergeoLinePerpendicularToLineThroughPoint(
			IntergeoLinePerpendicularToLineThroughPoint intergeoLinePerpendicularToLineThroughPoint) {
		Element xmlLineE = doc.createElement("line");
		xmlLineE.setAttribute("id", intergeoLinePerpendicularToLineThroughPoint.getID());
		Element xmlHomogeneousCoordinates = doc.createElement("homogeneous_coordinates");
		Element xmlDoubleX = doc.createElement("double");
		xmlDoubleX.appendChild(doc.createTextNode("" + intergeoLinePerpendicularToLineThroughPoint.getA()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleX);
		Element xmlDoubleY = doc.createElement("double");
		xmlDoubleY.appendChild(doc.createTextNode("" + intergeoLinePerpendicularToLineThroughPoint.getB()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleY);
		Element xmlDoubleW = doc.createElement("double");
		xmlDoubleW.appendChild(doc.createTextNode("" + intergeoLinePerpendicularToLineThroughPoint.getC()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleW);
		xmlLineE.appendChild(xmlHomogeneousCoordinates);
		xmlElements.appendChild(xmlLineE);

		Element xmlLineParallelToLineThroughPoint = doc.createElement("line_perpendicular_to_line_through_point");
		Element xmlLineC = doc.createElement("line");
		xmlLineC.setAttribute("out", "true");
		xmlLineC.appendChild(doc.createTextNode(intergeoLinePerpendicularToLineThroughPoint.getID()));
		Element xmlPointC = doc.createElement("point");
		xmlPointC.appendChild(doc.createTextNode(intergeoLinePerpendicularToLineThroughPoint.getPoint().getID()));
		Element xmlLineParallelC = doc.createElement("line");
		xmlLineParallelC.appendChild(doc.createTextNode(intergeoLinePerpendicularToLineThroughPoint.getLine().getID()));
		xmlLineParallelToLineThroughPoint.appendChild(xmlLineC);
		xmlLineParallelToLineThroughPoint.appendChild(xmlPointC);
		xmlLineParallelToLineThroughPoint.appendChild(xmlLineParallelC);
		xmlConstraints.appendChild(xmlLineParallelToLineThroughPoint);
	}

	public void appendXMLIntergeoLineAngularBisectorOfThreePoints(
			IntergeoLineAngularBisectorOfThreePoints intergeoLineAngularBisectorOfThreePoints) {
		Element xmlLineE = doc.createElement("line");
		xmlLineE.setAttribute("id", intergeoLineAngularBisectorOfThreePoints.getID());
		Element xmlHomogeneousCoordinates = doc.createElement("homogeneous_coordinates");
		Element xmlDoubleX = doc.createElement("double");
		xmlDoubleX.appendChild(doc.createTextNode("" + intergeoLineAngularBisectorOfThreePoints.getA()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleX);
		Element xmlDoubleY = doc.createElement("double");
		xmlDoubleY.appendChild(doc.createTextNode("" + intergeoLineAngularBisectorOfThreePoints.getB()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleY);
		Element xmlDoubleW = doc.createElement("double");
		xmlDoubleW.appendChild(doc.createTextNode("" + intergeoLineAngularBisectorOfThreePoints.getC()));
		xmlHomogeneousCoordinates.appendChild(xmlDoubleW);
		xmlLineE.appendChild(xmlHomogeneousCoordinates);
		xmlElements.appendChild(xmlLineE);

		Element xmlLineParallelToLineThroughPoint = doc.createElement("line_angular_bisector_of_three_points");
		Element xmlLineC = doc.createElement("line");
		xmlLineC.setAttribute("out", "true");
		xmlLineC.appendChild(doc.createTextNode(intergeoLineAngularBisectorOfThreePoints.getID()));
		Element xmlPoint1 = doc.createElement("point");
		xmlPoint1.appendChild(doc.createTextNode(intergeoLineAngularBisectorOfThreePoints.getPoint1().getID()));
		Element xmlPoint2 = doc.createElement("point");
		xmlPoint2.appendChild(doc.createTextNode(intergeoLineAngularBisectorOfThreePoints.getPoint2().getID()));
		Element xmlPoint3 = doc.createElement("point");
		xmlPoint3.appendChild(doc.createTextNode(intergeoLineAngularBisectorOfThreePoints.getPoint3().getID()));
		xmlLineParallelToLineThroughPoint.appendChild(xmlLineC);
		xmlLineParallelToLineThroughPoint.appendChild(xmlPoint1);
		xmlLineParallelToLineThroughPoint.appendChild(xmlPoint2);
		xmlLineParallelToLineThroughPoint.appendChild(xmlPoint3);
		xmlConstraints.appendChild(xmlLineParallelToLineThroughPoint);
	}

	public void appendXMLIntergeoCircleByCenterAndPoint(IntergeoCircleByCenterAndPoint intergeoCircleByCenterAndPoint) {
		Element xmlCircleE = doc.createElement("circle");
		xmlCircleE.setAttribute("id", intergeoCircleByCenterAndPoint.getID());
		Element xmlMatrix = doc.createElement("matrix");
		Element xmlDoubleM00 = doc.createElement("double");
		xmlDoubleM00.appendChild(doc.createTextNode("" + intergeoCircleByCenterAndPoint.getQuadraticMatrix()[0][0]));
		xmlMatrix.appendChild(xmlDoubleM00);
		Element xmlDoubleM10 = doc.createElement("double");
		xmlDoubleM10.appendChild(doc.createTextNode("" + intergeoCircleByCenterAndPoint.getQuadraticMatrix()[1][0]));
		xmlMatrix.appendChild(xmlDoubleM10);
		Element xmlDoubleM20 = doc.createElement("double");
		xmlDoubleM20.appendChild(doc.createTextNode("" + intergeoCircleByCenterAndPoint.getQuadraticMatrix()[2][0]));
		xmlMatrix.appendChild(xmlDoubleM20);
		Element xmlDoubleM01 = doc.createElement("double");
		xmlDoubleM01.appendChild(doc.createTextNode("" + intergeoCircleByCenterAndPoint.getQuadraticMatrix()[0][1]));
		xmlMatrix.appendChild(xmlDoubleM01);
		Element xmlDoubleM11 = doc.createElement("double");
		xmlDoubleM11.appendChild(doc.createTextNode("" + intergeoCircleByCenterAndPoint.getQuadraticMatrix()[1][1]));
		xmlMatrix.appendChild(xmlDoubleM11);
		Element xmlDoubleM21 = doc.createElement("double");
		xmlDoubleM21.appendChild(doc.createTextNode("" + intergeoCircleByCenterAndPoint.getQuadraticMatrix()[2][1]));
		xmlMatrix.appendChild(xmlDoubleM21);
		Element xmlDoubleM02 = doc.createElement("double");
		xmlDoubleM02.appendChild(doc.createTextNode("" + intergeoCircleByCenterAndPoint.getQuadraticMatrix()[0][2]));
		xmlMatrix.appendChild(xmlDoubleM02);
		Element xmlDoubleM12 = doc.createElement("double");
		xmlDoubleM12.appendChild(doc.createTextNode("" + intergeoCircleByCenterAndPoint.getQuadraticMatrix()[1][2]));
		xmlMatrix.appendChild(xmlDoubleM12);
		Element xmlDoubleM22 = doc.createElement("double");
		xmlDoubleM22.appendChild(doc.createTextNode("" + intergeoCircleByCenterAndPoint.getQuadraticMatrix()[2][2]));
		xmlMatrix.appendChild(xmlDoubleM22);
		xmlCircleE.appendChild(xmlMatrix);
		xmlElements.appendChild(xmlCircleE);

		Element xmlCircleByCenterAndPoint = doc.createElement("circle_by_center_and_point");
		Element xmlCircleC = doc.createElement("circle");
		xmlCircleC.setAttribute("out", "true");
		xmlCircleC.appendChild(doc.createTextNode(intergeoCircleByCenterAndPoint.getID()));
		Element xmlPoint1 = doc.createElement("point");
		xmlPoint1.appendChild(doc.createTextNode(intergeoCircleByCenterAndPoint.getCenterPoint().getID()));
		Element xmlPoint2 = doc.createElement("point");
		xmlPoint2.appendChild(doc.createTextNode(intergeoCircleByCenterAndPoint.getThroughPoint().getID()));
		xmlCircleByCenterAndPoint.appendChild(xmlCircleC);
		xmlCircleByCenterAndPoint.appendChild(xmlPoint1);
		xmlCircleByCenterAndPoint.appendChild(xmlPoint2);
		xmlConstraints.appendChild(xmlCircleByCenterAndPoint);
	}

	public void appendXMLIntergeoCircleByThreePoints(IntergeoCircleByThreePoints intergeoCircleByThreePoints) {
		Element xmlCircleE = doc.createElement("circle");
		xmlCircleE.setAttribute("id", intergeoCircleByThreePoints.getID());
		Element xmlMatrix = doc.createElement("matrix");
		Element xmlDoubleM00 = doc.createElement("double");
		xmlDoubleM00.appendChild(doc.createTextNode("" + intergeoCircleByThreePoints.getQuadraticMatrix()[0][0]));
		xmlMatrix.appendChild(xmlDoubleM00);
		Element xmlDoubleM10 = doc.createElement("double");
		xmlDoubleM10.appendChild(doc.createTextNode("" + intergeoCircleByThreePoints.getQuadraticMatrix()[1][0]));
		xmlMatrix.appendChild(xmlDoubleM10);
		Element xmlDoubleM20 = doc.createElement("double");
		xmlDoubleM20.appendChild(doc.createTextNode("" + intergeoCircleByThreePoints.getQuadraticMatrix()[2][0]));
		xmlMatrix.appendChild(xmlDoubleM20);
		Element xmlDoubleM01 = doc.createElement("double");
		xmlDoubleM01.appendChild(doc.createTextNode("" + intergeoCircleByThreePoints.getQuadraticMatrix()[0][1]));
		xmlMatrix.appendChild(xmlDoubleM01);
		Element xmlDoubleM11 = doc.createElement("double");
		xmlDoubleM11.appendChild(doc.createTextNode("" + intergeoCircleByThreePoints.getQuadraticMatrix()[1][1]));
		xmlMatrix.appendChild(xmlDoubleM11);
		Element xmlDoubleM21 = doc.createElement("double");
		xmlDoubleM21.appendChild(doc.createTextNode("" + intergeoCircleByThreePoints.getQuadraticMatrix()[2][1]));
		xmlMatrix.appendChild(xmlDoubleM21);
		Element xmlDoubleM02 = doc.createElement("double");
		xmlDoubleM02.appendChild(doc.createTextNode("" + intergeoCircleByThreePoints.getQuadraticMatrix()[0][2]));
		xmlMatrix.appendChild(xmlDoubleM02);
		Element xmlDoubleM12 = doc.createElement("double");
		xmlDoubleM12.appendChild(doc.createTextNode("" + intergeoCircleByThreePoints.getQuadraticMatrix()[1][2]));
		xmlMatrix.appendChild(xmlDoubleM12);
		Element xmlDoubleM22 = doc.createElement("double");
		xmlDoubleM22.appendChild(doc.createTextNode("" + intergeoCircleByThreePoints.getQuadraticMatrix()[2][2]));
		xmlMatrix.appendChild(xmlDoubleM22);
		xmlCircleE.appendChild(xmlMatrix);
		xmlElements.appendChild(xmlCircleE);

		Element xmlCircleByThreePoints = doc.createElement("circle_by_three_points");
		Element xmlCircleC = doc.createElement("circle");
		xmlCircleC.setAttribute("out", "true");
		xmlCircleC.appendChild(doc.createTextNode(intergeoCircleByThreePoints.getID()));
		Element xmlPoint1 = doc.createElement("point");
		xmlPoint1.appendChild(doc.createTextNode(intergeoCircleByThreePoints.getPoint1().getID()));
		Element xmlPoint2 = doc.createElement("point");
		xmlPoint2.appendChild(doc.createTextNode(intergeoCircleByThreePoints.getPoint2().getID()));
		Element xmlPoint3 = doc.createElement("point");
		xmlPoint3.appendChild(doc.createTextNode(intergeoCircleByThreePoints.getPoint3().getID()));
		xmlCircleByThreePoints.appendChild(xmlCircleC);
		xmlCircleByThreePoints.appendChild(xmlPoint1);
		xmlCircleByThreePoints.appendChild(xmlPoint2);
		xmlCircleByThreePoints.appendChild(xmlPoint3);
		xmlConstraints.appendChild(xmlCircleByThreePoints);
	}
}
