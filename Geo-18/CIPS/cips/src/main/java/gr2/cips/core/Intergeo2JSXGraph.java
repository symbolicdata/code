package gr2.cips.core;

import gr2.cips.intergeo.Intergeo;
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
import gr2.cips.jsxgraph.JSXGraph;
import gr2.cips.jsxgraph.model.JSXGraphCircleGlider;
import gr2.cips.jsxgraph.model.JSXGraphCircumCircle;
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
import org.apache.log4j.Logger;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class Intergeo2JSXGraph {
	final static Logger logger = Logger.getLogger(Intergeo2JSXGraph.class);
	private Intergeo intergeo;

	public Intergeo2JSXGraph() {

	}

	public Intergeo2JSXGraph(Intergeo intergeo) {
		this.intergeo = intergeo;
	}

	public void setIntergeo(Intergeo intergeo) {
		this.intergeo = intergeo;
	}

	public Intergeo getIntergeo() {
		return this.intergeo;
	}

	public JSXGraph convert() {
		JSXGraph jsxGraph = new JSXGraph();
		if (getIntergeo().getTitle() != null) {
			jsxGraph.setTitle(getIntergeo().getTitle());
		}
		for (IntergeoElement intergeoElement : intergeo.getIntegeoElements()) {
			if (intergeoElement instanceof IntergeoFreePoint) {
				JSXGraphParameter xParameter = (JSXGraphParameter) jsxGraph
						.getElementByID(JSXGraphParameter.CONST_IDENTITY + intergeoElement.getX());
				JSXGraphParameter yParameter = (JSXGraphParameter) jsxGraph
						.getElementByID(JSXGraphParameter.CONST_IDENTITY + intergeoElement.getY());
				if (xParameter == null) {
					xParameter = new JSXGraphParameter(JSXGraphParameter.CONST_IDENTITY + intergeoElement.getX(),
							intergeoElement.getX());
					jsxGraph.addElement(xParameter);
				}
				if (yParameter == null) {
					yParameter = new JSXGraphParameter(JSXGraphParameter.CONST_IDENTITY + intergeoElement.getY(),
							intergeoElement.getY());
					jsxGraph.addElement(yParameter);
				}
				jsxGraph.addElement(new JSXGraphPoint(intergeoElement.getID(), xParameter, yParameter,
						jsxGraph.getElementByID(JSXGraphParameter.CONST_IDENTITY + String.valueOf(1.0))));
				logger.info("free_point ID:" + intergeoElement.getID() + " has been converted to JSXGraph point");
			} else if (intergeoElement instanceof IntergeoMidPointOfTwoPoints) {
				jsxGraph.addElement(new JSXGraphMidPoint(intergeoElement.getID(),
						jsxGraph.getElementByID(((IntergeoMidPointOfTwoPoints) intergeoElement).getPoint1().getID()),
						jsxGraph.getElementByID(((IntergeoMidPointOfTwoPoints) intergeoElement).getPoint2().getID())));
				logger.info("midpoint_of_two_points" + " ID:" + intergeoElement.getID()
						+ " has been converted to JSXGraph midpoint");
			} else if (intergeoElement instanceof IntergeoPointIntersectionOfTwoLines) {
				jsxGraph.addElement(new JSXGraphIntersection(intergeoElement.getID(),
						jsxGraph.getElementByID(
								((IntergeoPointIntersectionOfTwoLines) intergeoElement).getLine1().getID()),
						jsxGraph.getElementByID(
								((IntergeoPointIntersectionOfTwoLines) intergeoElement).getLine2().getID())));
				logger.info("point_intersection_of_two_lines" + " ID:" + intergeoElement.getID()
						+ " has been converted to JSXGraph intersection");
			} else if (intergeoElement instanceof IntergeoPointOnCircle) {
				JSXGraphParameter parameter = (JSXGraphParameter) jsxGraph.getElementByID(
						JSXGraphParameter.CONST_IDENTITY + ((IntergeoPointOnCircle) intergeoElement).getParameter());
				if (parameter == null) {
					parameter = new JSXGraphParameter(
							JSXGraphParameter.CONST_IDENTITY + ((IntergeoPointOnCircle) intergeoElement).getParameter(),
							((IntergeoPointOnCircle) intergeoElement).getParameter());
					jsxGraph.addElement(parameter);
				}
				jsxGraph.addElement(new JSXGraphCircleGlider(intergeoElement.getID(),
						jsxGraph.getElementByID(((IntergeoPointOnCircle) intergeoElement).getCircle().getID()),
						parameter));
				logger.info("point_on_circle" + " ID:" + intergeoElement.getID()
						+ " has been converted to JSXGraph circle glider");
			} else if (intergeoElement instanceof IntergeoPointOnLine) {
				JSXGraphParameter parameter = (JSXGraphParameter) jsxGraph.getElementByID(
						JSXGraphParameter.CONST_IDENTITY + ((IntergeoPointOnLine) intergeoElement).getParameter());
				if (parameter == null) {
					parameter = new JSXGraphParameter(
							JSXGraphParameter.CONST_IDENTITY + ((IntergeoPointOnLine) intergeoElement).getParameter(),
							((IntergeoPointOnLine) intergeoElement).getParameter());
					jsxGraph.addElement(parameter);
				}
				jsxGraph.addElement(new JSXGraphLineGlider(intergeoElement.getID(),
						jsxGraph.getElementByID(((IntergeoPointOnLine) intergeoElement).getLine().getID()), parameter));
				logger.info("point_on_line" + " ID:" + intergeoElement.getID()
						+ " has been converted to JSXGraph line glider");
			} else if (intergeoElement instanceof IntergeoLineThroughTwoPoints) {
				jsxGraph.addElement(new JSXGraphLine(intergeoElement.getID(),
						jsxGraph.getElementByID(((IntergeoLineThroughTwoPoints) intergeoElement).getPoint1().getID()),
						jsxGraph.getElementByID(((IntergeoLineThroughTwoPoints) intergeoElement).getPoint2().getID())));
				logger.info("line_through_two_points" + " ID:" + intergeoElement.getID()
						+ " has been converted to JSXGraph line");
			} else if (intergeoElement instanceof IntergeoLineParallelToLineThroughPoint) {
				jsxGraph.addElement(new JSXGraphParallel(intergeoElement.getID(),
						jsxGraph.getElementByID(
								((IntergeoLineParallelToLineThroughPoint) intergeoElement).getPoint().getID()),
						jsxGraph.getElementByID(
								((IntergeoLineParallelToLineThroughPoint) intergeoElement).getLine().getID())));
				logger.info("line_parallel_to_line_through_point" + " ID:" + intergeoElement.getID()
						+ " has been converted to JSXGraph parallel");
			} else if (intergeoElement instanceof IntergeoLinePerpendicularToLineThroughPoint) {
				jsxGraph.addElement(new JSXGraphPerpendicular(intergeoElement.getID(),
						jsxGraph.getElementByID(
								((IntergeoLinePerpendicularToLineThroughPoint) intergeoElement).getPoint().getID()),
						jsxGraph.getElementByID(
								((IntergeoLinePerpendicularToLineThroughPoint) intergeoElement).getLine().getID())));
				logger.info("line_perpendicular_to_line_through_point" + " ID:" + intergeoElement.getID()
						+ " has been converted to JSXGraph perpendicular");
			} else if (intergeoElement instanceof IntergeoLineAngularBisectorOfThreePoints) {
				jsxGraph.addElement(new JSXGraphP3Bisector(intergeoElement.getID(),
						jsxGraph.getElementByID(
								((IntergeoLineAngularBisectorOfThreePoints) intergeoElement).getPoint1().getID()),
						jsxGraph.getElementByID(
								((IntergeoLineAngularBisectorOfThreePoints) intergeoElement).getPoint2().getID()),
						jsxGraph.getElementByID(
								((IntergeoLineAngularBisectorOfThreePoints) intergeoElement).getPoint3().getID())));
				logger.info("line_angular_bisector_of_three_points" + " ID:" + intergeoElement.getID()
						+ " has been converted to JSXGraph bisector");
			} else if (intergeoElement instanceof IntergeoCircleByCenterAndPoint) {
				jsxGraph.addElement(new JSXGraphPCCircle(intergeoElement.getID(),
						jsxGraph.getElementByID(
								((IntergeoCircleByCenterAndPoint) intergeoElement).getCenterPoint().getID()),
						jsxGraph.getElementByID(
								((IntergeoCircleByCenterAndPoint) intergeoElement).getThroughPoint().getID())));
				logger.info("circle_by_center_and_point" + " ID:" + intergeoElement.getID()
						+ " has been converted to JSXGraph circle");
			} else if (intergeoElement instanceof IntergeoCircleByThreePoints) {
				jsxGraph.addElement(new JSXGraphCircumCircle(intergeoElement.getID(),
						jsxGraph.getElementByID(((IntergeoCircleByThreePoints) intergeoElement).getPoint1().getID()),
						jsxGraph.getElementByID(((IntergeoCircleByThreePoints) intergeoElement).getPoint2().getID()),
						jsxGraph.getElementByID(((IntergeoCircleByThreePoints) intergeoElement).getPoint3().getID())));
				logger.info("circle_by_three_points" + " ID:" + intergeoElement.getID()
						+ " has been converted to JSXGraph circumcircle");
			}
		}
		logger.info("Conversion successfully completed");
		return jsxGraph;
	}
}