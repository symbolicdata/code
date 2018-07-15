package gr2.cips.geoproofscheme.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class GeoProofSchemeIntersectionPoint extends GeoProofSchemeElement {
	private GeoProofSchemeElement line1;
	private GeoProofSchemeElement line2;

	public GeoProofSchemeIntersectionPoint(String id, GeoProofSchemeElement line1, GeoProofSchemeElement line2) {
		this.setID(id);
		this.setLine1(line1);
		this.setLine2(line2);
	}

	public void setLine1(GeoProofSchemeElement Line1) {
		this.line1 = Line1;
	}

	public void setLine2(GeoProofSchemeElement Line2) {
		this.line2 = Line2;
	}

	public GeoProofSchemeElement getLine1() {
		return this.line1;
	}

	public GeoProofSchemeElement getLine2() {
		return this.line2;
	}

	public double getX() {
		double a1 = this.getLine1().getA();
		double a2 = this.getLine2().getA();
		double b1 = this.getLine1().getB();
		double b2 = this.getLine2().getB();
		double c1 = this.getLine1().getC();
		double c2 = this.getLine2().getC();
		if (b1 == 0)
			return -c1 / a1;
		if (b2 == 0)
			return -c2 / a2;
		return ((-c2 / b2 + c1 / b1) / (-a1 / b1 + a2 / b2));
	}

	public double getY() {
		double a1 = this.getLine1().getA();
		double b1 = this.getLine1().getB();
		double c1 = this.getLine1().getC();
		return (-a1 / b1) * getX() - c1 / b1;
	}

	@Override
	public String toString() {
		return "Line1:[" + line1.toString() + "], " + "Line2:[" + line2.toString() + "]";
	}
}
