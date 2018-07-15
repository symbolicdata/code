package gr2.cips.geoproofscheme.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class GeoProofSchemeVarPoint extends GeoProofSchemeElement {
	private GeoProofSchemeElement point1;
	private GeoProofSchemeElement point2;
	private GeoProofSchemeParameter parameter;

	public GeoProofSchemeVarPoint(String id, GeoProofSchemeElement point1, GeoProofSchemeElement point2,
			GeoProofSchemeParameter parameter) {
		this.setID(id);
		this.point1 = point1;
		this.point2 = point2;
		this.parameter = parameter;
	}
	
	public GeoProofSchemeElement getPoint1() {
		return point1;
	}

	public void setPoint1(GeoProofSchemeElement point1) {
		this.point1 = point1;
	}

	public GeoProofSchemeElement getPoint2() {
		return point2;
	}

	public void setPoint2(GeoProofSchemeElement point2) {
		this.point2 = point2;
	}

	public GeoProofSchemeParameter getParameter() {
		return parameter;
	}

	public void setParameter(GeoProofSchemeParameter parameter) {
		this.parameter = parameter;
	}
	
	public double getX() {
		double x1=point1.getX();
		double x2=point2.getX();
		double u=parameter.getValue();
		return (x1+(x2-x1)*u);
	}

	public double getY() {
		double y1=point1.getY();
		double y2=point2.getY();
		double u=parameter.getValue();
		return (y1+(y2-y1)*u);
	}

	@Override
	public String toString() {
		return "Point1:(" + this.point1.toString() + "), Point2:(" + this.point1.toString() + "), Parameter:" + this.parameter.toString();
	}
}
