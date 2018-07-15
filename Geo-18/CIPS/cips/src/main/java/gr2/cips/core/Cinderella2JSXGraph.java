package gr2.cips.core;

import gr2.cips.cinderella.Cinderella;
import gr2.cips.cinderella.model.CinderellaCircleBy3;
import gr2.cips.cinderella.model.CinderellaCircleMP;
import gr2.cips.cinderella.model.CinderellaElement;
import gr2.cips.cinderella.model.CinderellaFreePoint;
import gr2.cips.cinderella.model.CinderellaJoin;
import gr2.cips.cinderella.model.CinderellaMeet;
import gr2.cips.cinderella.model.CinderellaMid;
import gr2.cips.cinderella.model.CinderellaOrthogonal;
import gr2.cips.cinderella.model.CinderellaParallel;
import gr2.cips.jsxgraph.JSXGraph;
import gr2.cips.jsxgraph.model.JSXGraphCircumCircle;
import gr2.cips.jsxgraph.model.JSXGraphIntersection;
import gr2.cips.jsxgraph.model.JSXGraphLine;
import gr2.cips.jsxgraph.model.JSXGraphMidPoint;
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
public class Cinderella2JSXGraph {
	final static Logger logger = Logger.getLogger(Cinderella2JSXGraph.class);
	private Cinderella cinderella;

	public Cinderella2JSXGraph() {

	}

	public Cinderella2JSXGraph(Cinderella cinderella) {
		this.cinderella = cinderella;
	}

	public void setCinderella(Cinderella cinderella) {
		this.cinderella = cinderella;
	}

	public Cinderella getCinderella() {
		return this.cinderella;
	}

	public JSXGraph convert() {
		JSXGraph jsxGraph = new JSXGraph();

		if (getCinderella().getTitle() != null) {
			jsxGraph.setTitle(getCinderella().getTitle());
		}

		for (CinderellaElement cinderellaElement : cinderella.getCinderellaElements()) {
			if (cinderellaElement instanceof CinderellaFreePoint) {
				JSXGraphParameter xParameter = (JSXGraphParameter) jsxGraph
						.getElementByID(JSXGraphParameter.CONST_IDENTITY + cinderellaElement.getX());
				JSXGraphParameter yParameter = (JSXGraphParameter) jsxGraph
						.getElementByID(JSXGraphParameter.CONST_IDENTITY + cinderellaElement.getY());
				if (xParameter == null) {
					xParameter = new JSXGraphParameter(JSXGraphParameter.CONST_IDENTITY + cinderellaElement.getX(),
							cinderellaElement.getX());
					jsxGraph.addElement(xParameter);
				}
				if (yParameter == null) {
					yParameter = new JSXGraphParameter(JSXGraphParameter.CONST_IDENTITY + cinderellaElement.getY(),
							cinderellaElement.getY());
					jsxGraph.addElement(yParameter);
				}
				jsxGraph.addElement(new JSXGraphPoint(cinderellaElement.getID(), xParameter, yParameter,
						jsxGraph.getElementByID(JSXGraphParameter.CONST_IDENTITY + String.valueOf(1.0))));
				logger.info("FreePoint ID:" + cinderellaElement.getID() + " has been converted to JSXGraph point");
			} else if (cinderellaElement instanceof CinderellaMid) {
				jsxGraph.addElement(new JSXGraphMidPoint(cinderellaElement.getID(),
						jsxGraph.getElementByID(((CinderellaMid) cinderellaElement).getPoint1().getID()),
						jsxGraph.getElementByID(((CinderellaMid) cinderellaElement).getPoint2().getID())));
				logger.info("Mid ID:" + cinderellaElement.getID() + " has been converted to JSXGraph midpoint");
			} else if (cinderellaElement instanceof CinderellaMeet) {
				jsxGraph.addElement(new JSXGraphIntersection(cinderellaElement.getID(),
						jsxGraph.getElementByID(((CinderellaMeet) cinderellaElement).getLineOrSegment1().getID()),
						jsxGraph.getElementByID(((CinderellaMeet) cinderellaElement).getLineOrSegment2().getID())));
				logger.info("Meet ID:" + cinderellaElement.getID() + " has been converted to JSXGraph intersection");
			} else if (cinderellaElement instanceof CinderellaJoin) {
				jsxGraph.addElement(new JSXGraphLine(cinderellaElement.getID(),
						jsxGraph.getElementByID(((CinderellaJoin) cinderellaElement).getPoint1().getID()),
						jsxGraph.getElementByID(((CinderellaJoin) cinderellaElement).getPoint2().getID())));
				logger.info("Join ID:" + cinderellaElement.getID() + " has been converted to JSXGraph line");
			} else if (cinderellaElement instanceof CinderellaParallel) {
				jsxGraph.addElement(new JSXGraphParallel(cinderellaElement.getID(),
						jsxGraph.getElementByID(((CinderellaParallel) cinderellaElement).getPoint().getID()),
						jsxGraph.getElementByID(((CinderellaParallel) cinderellaElement).getlineOrSegment().getID())));
				logger.info("Parallel ID:" + cinderellaElement.getID() + " has been converted to JSXGraph parallel");
			} else if (cinderellaElement instanceof CinderellaOrthogonal) {
				jsxGraph.addElement(new JSXGraphPerpendicular(cinderellaElement.getID(),
						jsxGraph.getElementByID(((CinderellaOrthogonal) cinderellaElement).getThroughPoint().getID()),
						jsxGraph.getElementByID(
								((CinderellaOrthogonal) cinderellaElement).getOrthogonalLineOrSegment().getID())));
				logger.info(
						"Orthogonal ID:" + cinderellaElement.getID() + " has been converted to JSXGraph perpendicular");
			} else if (cinderellaElement instanceof CinderellaCircleMP) {
				jsxGraph.addElement(new JSXGraphPCCircle(cinderellaElement.getID(),
						jsxGraph.getElementByID(((CinderellaCircleMP) cinderellaElement).getCenterPoint().getID()),
						jsxGraph.getElementByID(((CinderellaCircleMP) cinderellaElement).getThroughPoint().getID())));
				logger.info("CircleMP ID:" + cinderellaElement.getID() + " has been converted to JSXGraph circle");
			} else if (cinderellaElement instanceof CinderellaCircleBy3) {
				jsxGraph.addElement(new JSXGraphCircumCircle(cinderellaElement.getID(),
						jsxGraph.getElementByID(((CinderellaCircleBy3) cinderellaElement).getPoint1().getID()),
						jsxGraph.getElementByID(((CinderellaCircleBy3) cinderellaElement).getPoint2().getID()),
						jsxGraph.getElementByID(((CinderellaCircleBy3) cinderellaElement).getPoint3().getID())));
				logger.info(
						"CircleBy3 ID:" + cinderellaElement.getID() + " has been converted to JSXGraph circumcircle");
			}
		}
		logger.info("Conversion successfully completed");
		return jsxGraph;
	}
}
