package gr2.cips.geoproofscheme.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public abstract class GeoProofSchemeElement {
	private String id;

	public GeoProofSchemeElement() {

	}

	public void setID(String ID) {
		this.id = ID;
	}

	public String getID() {
		return id;
	}

	public boolean isParameter() {
		return this instanceof GeoProofSchemeParameter ? true : false;
	}

	public boolean isVariable() {
		return this instanceof GeoProofSchemeVariable ? true : false;
	}

	public boolean isPoint() {
		return this instanceof GeoProofSchemeFreePoint 
				|| this instanceof GeoProofSchemeMidPoint
				|| this instanceof GeoProofSchemeIntersectionPoint 
				|| this instanceof GeoProofSchemeCircleSlider
				|| this instanceof GeoProofSchemeLineSlider 
				|| this instanceof GeoProofSchemeVarPoint
				|| this instanceof GeoProofSchemeFixedPoint ? true : false;
	}

	public boolean isLine() {
		return this instanceof GeoProofSchemePPLine 
				|| this instanceof GeoProofSchemeParLine
				|| this instanceof GeoProofSchemeOrthoLine 
				|| this instanceof GeoProofSchemeP3Bisector
				|| this instanceof GeoProofSchemeMedian
				|| this instanceof GeoProofSchemeAltitude
				|| this instanceof GeoProofSchemePBisector ? true : false;
	}

	public boolean isCircle() {
		return this instanceof GeoProofSchemeP3Circle 
				|| this instanceof GeoProofSchemePCCircle ? true : false;
	}

	public double getValue() {
		return Double.NaN;
	}

	public double getX() {
		return Double.NaN;
	}

	public double getY() {
		return Double.NaN;
	}

	public double getA() {
		return Double.NaN;
	}

	public double getB() {
		return Double.NaN;
	}

	public double getC() {
		return Double.NaN;
	}

	public String toString() {
		return "";
	}
}
