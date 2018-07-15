package gr2.cips.core;

import gr2.cips.geoproofscheme.GeoProofScheme;
import gr2.cips.geoproofscheme.model.GeoProofSchemeAltitude;
import gr2.cips.geoproofscheme.model.GeoProofSchemeCircleSlider;
import gr2.cips.geoproofscheme.model.GeoProofSchemeElement;
import gr2.cips.geoproofscheme.model.GeoProofSchemeFixedPoint;
import gr2.cips.geoproofscheme.model.GeoProofSchemeFreePoint;
import gr2.cips.geoproofscheme.model.GeoProofSchemeIntersectionPoint;
import gr2.cips.geoproofscheme.model.GeoProofSchemeLineSlider;
import gr2.cips.geoproofscheme.model.GeoProofSchemeMedian;
import gr2.cips.geoproofscheme.model.GeoProofSchemeMidPoint;
import gr2.cips.geoproofscheme.model.GeoProofSchemeOrthoLine;
import gr2.cips.geoproofscheme.model.GeoProofSchemeP3Bisector;
import gr2.cips.geoproofscheme.model.GeoProofSchemeP3Circle;
import gr2.cips.geoproofscheme.model.GeoProofSchemePBisector;
import gr2.cips.geoproofscheme.model.GeoProofSchemePCCircle;
import gr2.cips.geoproofscheme.model.GeoProofSchemePPLine;
import gr2.cips.geoproofscheme.model.GeoProofSchemeParLine;
import gr2.cips.geoproofscheme.model.GeoProofSchemeParameter;
import gr2.cips.geoproofscheme.model.GeoProofSchemeVarPoint;
import gr2.cips.jsxgraph.JSXGraph;
import gr2.cips.jsxgraph.model.JSXGraphCircleGlider;
import gr2.cips.jsxgraph.model.JSXGraphCircumCircle;
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
import org.apache.log4j.Logger;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class GeoProofScheme2JSXGraph {
	final static Logger logger = Logger.getLogger(GeoProofScheme2JSXGraph.class);
	private GeoProofScheme geoProofScheme;

	public GeoProofScheme2JSXGraph() {

	}

	public GeoProofScheme2JSXGraph(GeoProofScheme geoProofScheme) {
		this.geoProofScheme = geoProofScheme;
	}

	public void setGeoProofScheme(GeoProofScheme geoProofScheme) {
		this.geoProofScheme = geoProofScheme;
	}

	public GeoProofScheme getGeoProofScheme() {
		return this.geoProofScheme;
	}

	public JSXGraph convert() {
		JSXGraph jsxGraph = new JSXGraph();
		if (getGeoProofScheme().getTitle() != null) {
			jsxGraph.setTitle(getGeoProofScheme().getTitle());
		} else {
			jsxGraph.setTitle("");
		}

		for (GeoProofSchemeElement geoProofSchemeElement : geoProofScheme.getGeoProofSchemeElements()) {
			if (geoProofSchemeElement instanceof GeoProofSchemeParameter) {
				jsxGraph.addElement(
						new JSXGraphParameter(geoProofSchemeElement.getID(), geoProofSchemeElement.getValue()));
			} else if (geoProofSchemeElement instanceof GeoProofSchemeFreePoint) {
				jsxGraph.addElement(new JSXGraphPoint(geoProofSchemeElement.getID(),
						jsxGraph.getElementByID(
								((GeoProofSchemeFreePoint) geoProofSchemeElement).getXParameter().getID()),
						jsxGraph.getElementByID(
								((GeoProofSchemeFreePoint) geoProofSchemeElement).getYParameter().getID()),
						jsxGraph.getElementByID(JSXGraphParameter.CONST_IDENTITY + String.valueOf(1.0))));
				logger.info("point ID:" + geoProofSchemeElement.getID() + " has been converted to JSXGraph point");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeMidPoint) {
				jsxGraph.addElement(new JSXGraphMidPoint(geoProofSchemeElement.getID(),
						jsxGraph.getElementByID(((GeoProofSchemeMidPoint) geoProofSchemeElement).getPoint1().getID()),
						jsxGraph.getElementByID(((GeoProofSchemeMidPoint) geoProofSchemeElement).getPoint2().getID())));
				logger.info(
						"midpoint ID:" + geoProofSchemeElement.getID() + " has been converted to JSXGraph midpoint");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeIntersectionPoint) {
				jsxGraph.addElement(new JSXGraphIntersection(geoProofSchemeElement.getID(),
						jsxGraph.getElementByID(
								((GeoProofSchemeIntersectionPoint) geoProofSchemeElement).getLine1().getID()),
						jsxGraph.getElementByID(
								((GeoProofSchemeIntersectionPoint) geoProofSchemeElement).getLine2().getID())));
				logger.info("intersection_point ID:" + geoProofSchemeElement.getID()
						+ " has been converted to JSXGraph intersection");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeCircleSlider) {
				GeoProofSchemePCCircle tempGeoProofSchemePCCirle = null;
				for (GeoProofSchemeElement tempGeoProofSchemeElement : geoProofScheme.getGeoProofSchemeElements()) {
					if (tempGeoProofSchemeElement instanceof GeoProofSchemePCCircle) {
						if (((GeoProofSchemePCCircle) tempGeoProofSchemeElement).getCenterPoint().getID()
								.equals(((GeoProofSchemeCircleSlider) geoProofSchemeElement).getCenterPoint().getID())
								&& ((GeoProofSchemePCCircle) tempGeoProofSchemeElement).getThroughPoint().getID()
										.equals(((GeoProofSchemeCircleSlider) geoProofSchemeElement).getThroughPoint()
												.getID())) {
							tempGeoProofSchemePCCirle = (GeoProofSchemePCCircle) tempGeoProofSchemeElement;
							break;
						}
					}
				}
				jsxGraph.addElement(new JSXGraphCircleGlider(geoProofSchemeElement.getID(),
						(JSXGraphPCCircle) jsxGraph.getElementByID(tempGeoProofSchemePCCirle.getID()),
						((JSXGraphParameter) jsxGraph.getElementByID(
								((GeoProofSchemeCircleSlider) geoProofSchemeElement).getParameter().getID()))));
				logger.info(
						"circle_slider ID:" + geoProofSchemeElement.getID() + " has been converted to JSXGraph glider");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeLineSlider) {
				jsxGraph.addElement(new JSXGraphLineGlider(geoProofSchemeElement.getID(),
						jsxGraph.getElementByID(((GeoProofSchemeLineSlider) geoProofSchemeElement).getLine().getID()),
						(JSXGraphParameter) jsxGraph.getElementByID(
								((GeoProofSchemeLineSlider) geoProofSchemeElement).getParameter().getID())));
				logger.info(
						"line_slider ID:" + geoProofSchemeElement.getID() + " has been converted to JSXGraph glider");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeVarPoint) {
				jsxGraph.addElement(new JSXGraphVarPoint(geoProofSchemeElement.getID(),
						jsxGraph.getElementByID(((GeoProofSchemeVarPoint) geoProofSchemeElement).getPoint1().getID()),
						jsxGraph.getElementByID(((GeoProofSchemeVarPoint) geoProofSchemeElement).getPoint2().getID()),
						(JSXGraphParameter) jsxGraph.getElementByID(
								((GeoProofSchemeVarPoint) geoProofSchemeElement).getParameter().getID())));
				logger.info(
						"varpoint ID:" + geoProofSchemeElement.getID() + " has been converted to JSXGraph varpoint");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeFixedPoint) {
				jsxGraph.addElement(new JSXGraphFixedPoint(geoProofSchemeElement.getID(),
						jsxGraph.getElementByID(((GeoProofSchemeFixedPoint) geoProofSchemeElement).getPoint1().getID()),
						jsxGraph.getElementByID(((GeoProofSchemeFixedPoint) geoProofSchemeElement).getPoint2().getID()),
						((GeoProofSchemeFixedPoint) geoProofSchemeElement).getParameter()));
				logger.info("fixedpoint ID:" + geoProofSchemeElement.getID() + " has been converted to JSXGraph line");
			} else if (geoProofSchemeElement instanceof GeoProofSchemePPLine) {
				jsxGraph.addElement(new JSXGraphLine(geoProofSchemeElement.getID(),
						jsxGraph.getElementByID(((GeoProofSchemePPLine) geoProofSchemeElement).getPoint1().getID()),
						jsxGraph.getElementByID(((GeoProofSchemePPLine) geoProofSchemeElement).getPoint2().getID())));
				logger.info("pp_line ID:" + geoProofSchemeElement.getID() + " has been converted to JSXGraph line");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeParLine) {
				jsxGraph.addElement(new JSXGraphParallel(geoProofSchemeElement.getID(),
						jsxGraph.getElementByID(((GeoProofSchemeParLine) geoProofSchemeElement).getPoint().getID()),
						jsxGraph.getElementByID(((GeoProofSchemeParLine) geoProofSchemeElement).getLine().getID())));
				logger.info(
						"par_line ID:" + geoProofSchemeElement.getID() + " has been converted to JSXGraph parallel");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeOrthoLine) {
				jsxGraph.addElement(new JSXGraphPerpendicular(geoProofSchemeElement.getID(),
						jsxGraph.getElementByID(((GeoProofSchemeOrthoLine) geoProofSchemeElement).getPoint().getID()),
						jsxGraph.getElementByID(((GeoProofSchemeOrthoLine) geoProofSchemeElement).getLine().getID())));
				logger.info(
						"ortho_line ID:" + geoProofSchemeElement.getID() + " has been converted to JSXGraph perpendicular");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeAltitude) {
				GeoProofSchemePPLine tempGeoProofSchemePPLine = null;
				for (GeoProofSchemeElement tempGeoProofSchemeElement : geoProofScheme.getGeoProofSchemeElements()) {
					if (tempGeoProofSchemeElement instanceof GeoProofSchemePPLine) {
						if (((GeoProofSchemePPLine) tempGeoProofSchemeElement).getPoint1().getID()
								.equals(((GeoProofSchemeAltitude) geoProofSchemeElement).getPoint2().getID())
								&& ((GeoProofSchemePPLine) tempGeoProofSchemeElement).getPoint2().getID()
										.equals(((GeoProofSchemeAltitude) geoProofSchemeElement).getPoint3().getID())) {
							tempGeoProofSchemePPLine = (GeoProofSchemePPLine) tempGeoProofSchemeElement;
							break;
						}
					}
				}
				jsxGraph.addElement(new JSXGraphPerpendicular(geoProofSchemeElement.getID(),
						jsxGraph.getElementByID(((GeoProofSchemeAltitude) geoProofSchemeElement).getPoint1().getID()),
						jsxGraph.getElementByID(tempGeoProofSchemePPLine.getID())));
				logger.info(
						"altitude ID:" + geoProofSchemeElement.getID() + " has been converted to JSXGraph perpendicular");
			} else if (geoProofSchemeElement instanceof GeoProofSchemePBisector) {
				GeoProofSchemePPLine tempGeoProofSchemePPLine = null;
				for (GeoProofSchemeElement tempGeoProofSchemeElement : geoProofScheme.getGeoProofSchemeElements()) {
					if (tempGeoProofSchemeElement instanceof GeoProofSchemePPLine) {
						if (((GeoProofSchemePPLine) tempGeoProofSchemeElement).getPoint1().getID()
								.equals(((GeoProofSchemePBisector) geoProofSchemeElement).getPoint1().getID())
								&& ((GeoProofSchemePPLine) tempGeoProofSchemeElement).getPoint2().getID().equals(
										((GeoProofSchemePBisector) geoProofSchemeElement).getPoint2().getID())) {
							tempGeoProofSchemePPLine = (GeoProofSchemePPLine) tempGeoProofSchemeElement;
							break;
						}
					}
				}
				GeoProofSchemeMidPoint tempGeoProofSchemeMidPoint = null;
				for (GeoProofSchemeElement tempGeoProofSchemeElement : geoProofScheme.getGeoProofSchemeElements()) {
					if (tempGeoProofSchemeElement instanceof GeoProofSchemeMidPoint) {
						if (((GeoProofSchemeMidPoint) tempGeoProofSchemeElement).getPoint1().getID()
								.equals(((GeoProofSchemePBisector) geoProofSchemeElement).getPoint1().getID())
								&& ((GeoProofSchemeMidPoint) tempGeoProofSchemeElement).getPoint2().getID().equals(
										((GeoProofSchemePBisector) geoProofSchemeElement).getPoint2().getID())) {
							tempGeoProofSchemeMidPoint = (GeoProofSchemeMidPoint) tempGeoProofSchemeElement;
							break;
						}
					}
				}
				jsxGraph.addElement(new JSXGraphPerpendicular(geoProofSchemeElement.getID(),
						jsxGraph.getElementByID(tempGeoProofSchemeMidPoint.getID()),
						jsxGraph.getElementByID(tempGeoProofSchemePPLine.getID())));
				logger.info(
						"p_bisector ID:" + geoProofSchemeElement.getID() + " has been converted to JSXGraph perpendicular");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeMedian) {
				GeoProofSchemeMidPoint tempGeoProofSchemeMidPoint = null;
				for (GeoProofSchemeElement tempGeoProofSchemeElement : geoProofScheme.getGeoProofSchemeElements()) {
					if (tempGeoProofSchemeElement instanceof GeoProofSchemeMidPoint) {
						if (((GeoProofSchemeMidPoint) tempGeoProofSchemeElement).getPoint1().getID()
								.equals(((GeoProofSchemeMedian) geoProofSchemeElement).getPoint2().getID())
								&& ((GeoProofSchemeMidPoint) tempGeoProofSchemeElement).getPoint2().getID().equals(
										((GeoProofSchemeMedian) geoProofSchemeElement).getPoint3().getID())) {
							tempGeoProofSchemeMidPoint = (GeoProofSchemeMidPoint) tempGeoProofSchemeElement;
							break;
						}
					}
				}
				jsxGraph.addElement(new JSXGraphLine(geoProofSchemeElement.getID(),
						jsxGraph.getElementByID(((GeoProofSchemeMedian) geoProofSchemeElement).getPoint1().getID()),
						jsxGraph.getElementByID(tempGeoProofSchemeMidPoint.getID())));
				logger.info(
						"median ID:" + geoProofSchemeElement.getID() + " has been converted to JSXGraph line");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeP3Bisector) {
				jsxGraph.addElement(new JSXGraphP3Bisector(geoProofSchemeElement.getID(),
						jsxGraph.getElementByID(((GeoProofSchemeP3Bisector) geoProofSchemeElement).getPoint1().getID()),
						jsxGraph.getElementByID(((GeoProofSchemeP3Bisector) geoProofSchemeElement).getPoint2().getID()),
						jsxGraph.getElementByID(
								((GeoProofSchemeP3Bisector) geoProofSchemeElement).getPoint3().getID())));
				logger.info(
						"p3_bisector ID:" + geoProofSchemeElement.getID() + " has been converted to JSXGraph bisector");
			} else if (geoProofSchemeElement instanceof GeoProofSchemePCCircle) {
				jsxGraph.addElement(new JSXGraphPCCircle(geoProofSchemeElement.getID(),
						jsxGraph.getElementByID(
								((GeoProofSchemePCCircle) geoProofSchemeElement).getCenterPoint().getID()),
						jsxGraph.getElementByID(
								((GeoProofSchemePCCircle) geoProofSchemeElement).getThroughPoint().getID())));
				logger.info("pc_circle ID:" + geoProofSchemeElement.getID() + " has been converted to JSXGraph circle");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeP3Circle) {
				jsxGraph.addElement(new JSXGraphCircumCircle(geoProofSchemeElement.getID(),
						jsxGraph.getElementByID(((GeoProofSchemeP3Circle) geoProofSchemeElement).getPoint1().getID()),
						jsxGraph.getElementByID(((GeoProofSchemeP3Circle) geoProofSchemeElement).getPoint2().getID()),
						jsxGraph.getElementByID(((GeoProofSchemeP3Circle) geoProofSchemeElement).getPoint3().getID())));
				logger.info("p3_circle ID:" + geoProofSchemeElement.getID()
						+ " has been converted to JSXGraph circumcircle");
			}
		}
		logger.info("Conversion successfully completed");
		return jsxGraph;
	}
}
