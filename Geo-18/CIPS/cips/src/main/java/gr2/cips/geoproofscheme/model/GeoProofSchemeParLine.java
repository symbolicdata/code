package gr2.cips.geoproofscheme.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class GeoProofSchemeParLine extends GeoProofSchemeElement {
	private GeoProofSchemeElement point;
	private GeoProofSchemeElement line;

	public GeoProofSchemeParLine(String id, GeoProofSchemeElement point, GeoProofSchemeElement line) {
		this.setID(id);
		this.setPoint(point);
		this.setLine(line);
	}

	public void setPoint(GeoProofSchemeElement point) {
		this.point = point;
	}

	public GeoProofSchemeElement getPoint() {
		return this.point;
	}

	public void setLine(GeoProofSchemeElement line) {
		this.line = line;
	}

	public GeoProofSchemeElement getLine() {
		return this.line;
	}

	public double getA() {
		return this.getLine().getA();
	}

	public double getB() {
		return this.getLine().getB();
	}

	public double getC() {
		return -(this.getPoint().getY() * this.getLine().getB() + this.getLine().getA() * this.getPoint().getX());
	}

	@Override
	public String toString() {
		return "Point:(" + point.toString() + "), " + "Line:[" + line.toString() + "]";
	}
}
