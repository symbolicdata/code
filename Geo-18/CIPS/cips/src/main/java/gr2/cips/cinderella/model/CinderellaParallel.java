package gr2.cips.cinderella.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class CinderellaParallel extends CinderellaElement {
	CinderellaElement point;
	CinderellaElement lineOrSegment;

	public CinderellaParallel(String id, CinderellaElement lineOrSegment, CinderellaElement point) {
		this.setID(id);
		this.setLineOrSegment(lineOrSegment);
		this.setPoint(point);
	}

	public void setLineOrSegment(CinderellaElement lineOrSegment) {
		this.lineOrSegment = lineOrSegment;
	}

	public void setPoint(CinderellaElement point) {
		this.point = point;
	}

	public CinderellaElement getlineOrSegment() {
		return this.lineOrSegment;
	}

	public CinderellaElement getPoint() {
		return this.point;
	}

	public double getA() {
		return this.getlineOrSegment().getA();
	}

	public double getB() {
		return this.getlineOrSegment().getB();
	}

	public double getC() {
		return -(this.getPoint().getY() * this.getlineOrSegment().getB()
				+ this.getlineOrSegment().getA() * this.getPoint().getX());
	}

	@Override
	public String toString() {
		return "Point:(" + point.toString() + "), " + "Line:[" + lineOrSegment.toString() + "]";
	}
}
