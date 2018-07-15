package gr2.cips.geoproofscheme.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class GeoProofSchemePBisector extends GeoProofSchemeElement {
	private GeoProofSchemeElement point1;
	private GeoProofSchemeElement point2;

	public GeoProofSchemePBisector(String id, GeoProofSchemeElement point1, GeoProofSchemeElement point2) {
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
		GeoProofSchemePPLine geoProofSchemePPLine = new GeoProofSchemePPLine(null, point1, point2);
		return geoProofSchemePPLine.getB();
	}

	public double getB() {
		GeoProofSchemePPLine geoProofSchemePPLine = new GeoProofSchemePPLine(null, point1, point2);
		return -geoProofSchemePPLine.getA();
	}

	public double getC() {
		GeoProofSchemePPLine geoProofSchemePPLine = new GeoProofSchemePPLine(null, point1, point2);
		GeoProofSchemeMidPoint geoProofSchemeMidPoint = new GeoProofSchemeMidPoint(null, point1,point2);
		return -(geoProofSchemeMidPoint.getX() * geoProofSchemePPLine.getB() - geoProofSchemePPLine.getA() * geoProofSchemeMidPoint.getY());
	}

	@Override
	public String toString() {
		return "Point1:(" + point1.toString() + "), Point2:(" + point2.toString() + ")";
	}
}
