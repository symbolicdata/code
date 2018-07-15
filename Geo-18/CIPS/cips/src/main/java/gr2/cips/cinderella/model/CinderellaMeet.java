package gr2.cips.cinderella.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class CinderellaMeet extends CinderellaElement {
	private CinderellaElement lineOrSegment1;
	private CinderellaElement lineOrSegment2;

	public CinderellaMeet(String id, CinderellaElement lineOrSegment1, CinderellaElement lineOrSegment2) {
		this.setID(id);
		this.setLineOrSegment1(lineOrSegment1);
		this.setLineOrSegment2(lineOrSegment2);
	}

	public void setLineOrSegment1(CinderellaElement lineOrSegment1) {
		this.lineOrSegment1 = lineOrSegment1;
	}

	public void setLineOrSegment2(CinderellaElement lineOrSegment2) {
		this.lineOrSegment2 = lineOrSegment2;
	}

	public CinderellaElement getLineOrSegment1() {
		return this.lineOrSegment1;
	}

	public CinderellaElement getLineOrSegment2() {
		return this.lineOrSegment2;
	}

	public double getX() {
		double a1 = this.getLineOrSegment1().getA();
		double b1 = this.getLineOrSegment1().getB();
		double c1 = this.getLineOrSegment1().getC();
		return (-c1 - b1 * this.getY()) / a1;
	}

	public double getY() {
		double a1 = this.getLineOrSegment1().getA();
		double a2 = this.getLineOrSegment2().getA();
		double b1 = this.getLineOrSegment1().getB();
		double b2 = this.getLineOrSegment2().getB();
		double c1 = this.getLineOrSegment1().getC();
		double c2 = this.getLineOrSegment2().getC();
		return ((a2 * c1) / a1 - c2) / (b2 - (a2 * b1) / a1);
	}

	@Override
	public String toString() {
		return "Line1:[" + lineOrSegment1.toString() + "], " + "Line2:[" + lineOrSegment2.toString() + "]";
	}
}
