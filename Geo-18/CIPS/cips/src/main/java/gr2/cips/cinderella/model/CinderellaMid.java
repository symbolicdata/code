package gr2.cips.cinderella.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class CinderellaMid extends CinderellaElement {
	CinderellaElement point1;
	CinderellaElement point2;

	public CinderellaMid(String id, CinderellaElement point1, CinderellaElement point2) {
		this.setID(id);
		this.setPoint1(point1);
		this.setPoint2(point2);
	}

	public void setPoint1(CinderellaElement point1) {
		this.point1 = point1;
	}

	public void setPoint2(CinderellaElement point2) {
		this.point2 = point2;
	}

	public CinderellaElement getPoint1() {
		return this.point1;
	}

	public CinderellaElement getPoint2() {
		return this.point2;
	}

	public double getX() {
		return (getPoint1().getX() + getPoint2().getX()) / 2;
	}

	public double getY() {
		return (getPoint1().getY() + getPoint2().getY()) / 2;
	}

	@Override
	public String toString() {
		return "Point1:(" + point1.toString() + "), Point2:(" + point2.toString() + ")";
	}
}
