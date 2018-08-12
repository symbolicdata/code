package gr2.cips.geoproofscheme.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class GeoProofSchemePPLine extends GeoProofSchemeElement {
	private GeoProofSchemeElement point1;
	private GeoProofSchemeElement point2;

	public GeoProofSchemePPLine(String id, GeoProofSchemeElement point1, GeoProofSchemeElement point2) {
		this.setID(id);
		this.setPoint1(point1);
		this.setPoint2(point2);
	}

	public void setPoint1(GeoProofSchemeElement point1) {
		this.point1 = point1;
	}

	public void setPoint2(GeoProofSchemeElement point2) {
		this.point2 = point2;
	}

	public GeoProofSchemeElement getPoint1() {
		return this.point1;
	}

	public GeoProofSchemeElement getPoint2() {
		return this.point2;
	}

	public double getA() {
		return this.getPoint2().getY() - this.getPoint1().getY();
	}

	public double getB() {
		return this.getPoint1().getX() - this.getPoint2().getX();
	}

	public double getC() {
		return this.getPoint2().getX() * this.getPoint1().getY() - this.getPoint1().getX() * this.getPoint2().getY();
	}

	@Override
	public String toString() {
		return "Point1:(" + point1.toString() + "), Point2:(" + point2.toString() + ")";
	}
}
