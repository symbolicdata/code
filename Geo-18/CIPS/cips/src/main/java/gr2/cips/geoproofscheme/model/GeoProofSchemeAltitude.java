package gr2.cips.geoproofscheme.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class GeoProofSchemeAltitude extends GeoProofSchemeElement {
	private GeoProofSchemeElement point1;
	private GeoProofSchemeElement point2;
	private GeoProofSchemeElement point3;

	public GeoProofSchemeAltitude(String id, GeoProofSchemeElement point1, GeoProofSchemeElement point2,
			GeoProofSchemeElement point3) {
		this.setID(id);
		this.setPoint1(point1);
		this.setPoint2(point2);
		this.setPoint3(point3);
	}

	public void setPoint1(GeoProofSchemeElement point1) {
		this.point1 = point1;
	}

	public void setPoint2(GeoProofSchemeElement point2) {
		this.point2 = point2;
	}

	public void setPoint3(GeoProofSchemeElement point3) {
		this.point3 = point3;
	}

	public GeoProofSchemeElement getPoint1() {
		return this.point1;
	}

	public GeoProofSchemeElement getPoint2() {
		return this.point2;
	}

	public GeoProofSchemeElement getPoint3() {
		return this.point3;
	}

	public double getA() {
		GeoProofSchemePPLine geoProofSchemePPLine = new GeoProofSchemePPLine(null, point2, point3);
		return geoProofSchemePPLine.getB();
	}

	public double getB() {
		GeoProofSchemePPLine geoProofSchemePPLine = new GeoProofSchemePPLine(null, point2, point3);
		return -geoProofSchemePPLine.getA();
	}

	public double getC() {
		GeoProofSchemePPLine geoProofSchemePPLine = new GeoProofSchemePPLine(null, point2, point3);
		return -(point1.getX() * geoProofSchemePPLine.getB() - geoProofSchemePPLine.getA() * point1.getY());
	}

	@Override
	public String toString() {
		return "Point1:(" + point1.toString() + "), Point2:(" + point2.toString() + "), Point3:(" + point3.toString()
				+ ")";
	}
}
