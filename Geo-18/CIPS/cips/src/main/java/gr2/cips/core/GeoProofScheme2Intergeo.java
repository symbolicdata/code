package gr2.cips.core;

import gr2.cips.geoproofscheme.GeoProofScheme;
import gr2.cips.geoproofscheme.model.GeoProofSchemeCircleSlider;
import gr2.cips.geoproofscheme.model.GeoProofSchemeElement;
import gr2.cips.geoproofscheme.model.GeoProofSchemeFreePoint;
import gr2.cips.geoproofscheme.model.GeoProofSchemeIntersectionPoint;
import gr2.cips.geoproofscheme.model.GeoProofSchemeLineSlider;
import gr2.cips.geoproofscheme.model.GeoProofSchemeMidPoint;
import gr2.cips.geoproofscheme.model.GeoProofSchemeOrthoLine;
import gr2.cips.geoproofscheme.model.GeoProofSchemeP3Bisector;
import gr2.cips.geoproofscheme.model.GeoProofSchemeP3Circle;
import gr2.cips.geoproofscheme.model.GeoProofSchemePCCircle;
import gr2.cips.geoproofscheme.model.GeoProofSchemePPLine;
import gr2.cips.geoproofscheme.model.GeoProofSchemeParLine;
import gr2.cips.geoproofscheme.model.GeoProofSchemeParameter;
import gr2.cips.geoproofscheme.model.GeoProofSchemeVarPoint;
import gr2.cips.intergeo.Intergeo;
import gr2.cips.intergeo.model.IntergeoCircleByCenterAndPoint;
import gr2.cips.intergeo.model.IntergeoCircleByThreePoints;
import gr2.cips.intergeo.model.IntergeoFreePoint;
import gr2.cips.intergeo.model.IntergeoLineAngularBisectorOfThreePoints;
import gr2.cips.intergeo.model.IntergeoLineParallelToLineThroughPoint;
import gr2.cips.intergeo.model.IntergeoLinePerpendicularToLineThroughPoint;
import gr2.cips.intergeo.model.IntergeoLineThroughTwoPoints;
import gr2.cips.intergeo.model.IntergeoMidPointOfTwoPoints;
import gr2.cips.intergeo.model.IntergeoPointIntersectionOfTwoLines;
import gr2.cips.intergeo.model.IntergeoPointOnCircle;
import gr2.cips.intergeo.model.IntergeoPointOnLine;
import org.apache.log4j.Logger;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class GeoProofScheme2Intergeo {
	final static Logger logger = Logger.getLogger(GeoProofScheme2Intergeo.class);
	private GeoProofScheme geoProofScheme;

	public GeoProofScheme2Intergeo() {

	}

	public GeoProofScheme2Intergeo(GeoProofScheme geoProofScheme) {
		this.geoProofScheme = geoProofScheme;
	}

	public void setGeoProofScheme(GeoProofScheme geoProofScheme) {
		this.geoProofScheme = geoProofScheme;
	}

	public GeoProofScheme getGeoProofScheme() {
		return this.geoProofScheme;
	}

	public Intergeo convert() {
		Intergeo intergeo = new Intergeo();
		for (GeoProofSchemeElement geoProofSchemeElement : geoProofScheme.getGeoProofSchemeElements()) {
			if (geoProofSchemeElement instanceof GeoProofSchemeFreePoint) {
				intergeo.addElement(new IntergeoFreePoint(geoProofSchemeElement.getID(), geoProofSchemeElement.getX(),
						geoProofSchemeElement.getY(), 1.0));
				logger.info("point ID:" + geoProofSchemeElement.getID() + " has been converted");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeMidPoint) {
				intergeo.addElement(new IntergeoMidPointOfTwoPoints(geoProofSchemeElement.getID(),
						intergeo.getElementByID(((GeoProofSchemeMidPoint) geoProofSchemeElement).getPoint1().getID()),
						intergeo.getElementByID(((GeoProofSchemeMidPoint) geoProofSchemeElement).getPoint2().getID())));
				logger.info("midpoint ID:" + geoProofSchemeElement.getID() + " has been converted");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeIntersectionPoint) {
				intergeo.addElement(new IntergeoPointIntersectionOfTwoLines(geoProofSchemeElement.getID(),
						intergeo.getElementByID(
								((GeoProofSchemeIntersectionPoint) geoProofSchemeElement).getLine1().getID()),
						intergeo.getElementByID(
								((GeoProofSchemeIntersectionPoint) geoProofSchemeElement).getLine2().getID())));
				logger.info("intersection_point ID:" + geoProofSchemeElement.getID() + " has been converted");
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
				intergeo.addElement(new IntergeoPointOnCircle(geoProofSchemeElement.getID(),
						intergeo.getElementByID(tempGeoProofSchemePCCirle.getID()), geoProofSchemeElement.getX(),
						geoProofSchemeElement.getY(), 1.0));
				logger.info("circle_slider ID:" + geoProofSchemeElement.getID() + " has been converted");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeLineSlider) {
				intergeo.addElement(new IntergeoPointOnLine(geoProofSchemeElement.getID(),
						intergeo.getElementByID(((GeoProofSchemeLineSlider) geoProofSchemeElement).getLine().getID()),
						geoProofSchemeElement.getX(), geoProofSchemeElement.getY(), 1.0));
				logger.info("line_slider ID:" + geoProofSchemeElement.getID() + " has been converted");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeVarPoint) {
				intergeo.addElement(new IntergeoLineThroughTwoPoints(geoProofSchemeElement.getID(),
						intergeo.getElementByID(((GeoProofSchemeVarPoint) geoProofSchemeElement).getPoint1().getID()),
						intergeo.getElementByID(((GeoProofSchemeVarPoint) geoProofSchemeElement).getPoint2().getID())));
				logger.info("varpoint ID:" + geoProofSchemeElement.getID() + " has been converted");
			} else if (geoProofSchemeElement instanceof GeoProofSchemePPLine) {
				intergeo.addElement(new IntergeoLineThroughTwoPoints(geoProofSchemeElement.getID(),
						intergeo.getElementByID(((GeoProofSchemePPLine) geoProofSchemeElement).getPoint1().getID()),
						intergeo.getElementByID(((GeoProofSchemePPLine) geoProofSchemeElement).getPoint2().getID())));
				logger.info("pp_line ID:" + geoProofSchemeElement.getID() + " has been converted");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeParLine) {
				intergeo.addElement(new IntergeoLineParallelToLineThroughPoint(geoProofSchemeElement.getID(),
						intergeo.getElementByID(((GeoProofSchemeParLine) geoProofSchemeElement).getPoint().getID()),
						intergeo.getElementByID(((GeoProofSchemeParLine) geoProofSchemeElement).getLine().getID())));
				logger.info("par_line ID:" + geoProofSchemeElement.getID() + " has been converted");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeOrthoLine) {
				intergeo.addElement(new IntergeoLinePerpendicularToLineThroughPoint(geoProofSchemeElement.getID(),
						intergeo.getElementByID(((GeoProofSchemeOrthoLine) geoProofSchemeElement).getPoint().getID()),
						intergeo.getElementByID(((GeoProofSchemeOrthoLine) geoProofSchemeElement).getLine().getID())));
				logger.info("ortho_line ID:" + geoProofSchemeElement.getID() + " has been converted");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeP3Bisector) {
				intergeo.addElement(new IntergeoLineAngularBisectorOfThreePoints(geoProofSchemeElement.getID(),
						intergeo.getElementByID(((GeoProofSchemeP3Bisector) geoProofSchemeElement).getPoint1().getID()),
						intergeo.getElementByID(((GeoProofSchemeP3Bisector) geoProofSchemeElement).getPoint2().getID()),
						intergeo.getElementByID(
								((GeoProofSchemeP3Bisector) geoProofSchemeElement).getPoint3().getID())));
				logger.info("p3_bisector ID:" + geoProofSchemeElement.getID() + " has been converted");
			} else if (geoProofSchemeElement instanceof GeoProofSchemePCCircle) {
				intergeo.addElement(new IntergeoCircleByCenterAndPoint(geoProofSchemeElement.getID(),
						intergeo.getElementByID(
								((GeoProofSchemePCCircle) geoProofSchemeElement).getCenterPoint().getID()),
						intergeo.getElementByID(
								((GeoProofSchemePCCircle) geoProofSchemeElement).getThroughPoint().getID())));
				logger.info("pc_circle ID:" + geoProofSchemeElement.getID() + " has been converted");
			} else if (geoProofSchemeElement instanceof GeoProofSchemeP3Circle) {
				intergeo.addElement(new IntergeoCircleByThreePoints(geoProofSchemeElement.getID(),
						intergeo.getElementByID(((GeoProofSchemeP3Circle) geoProofSchemeElement).getPoint1().getID()),
						intergeo.getElementByID(((GeoProofSchemeP3Circle) geoProofSchemeElement).getPoint2().getID()),
						intergeo.getElementByID(((GeoProofSchemeP3Circle) geoProofSchemeElement).getPoint3().getID())));
				logger.info("p3_circle ID:" + geoProofSchemeElement.getID() + " has been converted");
			} else if (!(geoProofSchemeElement instanceof GeoProofSchemeParameter)) {
				logger.error("Error while converting element ID:" + geoProofSchemeElement.getID());
				logger.error("Not yet implemented: " + geoProofSchemeElement.getClass().getSimpleName());
				return null;
			}
		}
		logger.info("Conversion successfully completed");
		return intergeo;
	}
}
