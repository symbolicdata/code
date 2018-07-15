package gr2.cips.intergeo.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class IntergeoMidPointOfTwoPoints extends IntergeoElement {
	private IntergeoElement point1;
	private IntergeoElement point2;

	public IntergeoMidPointOfTwoPoints(String id, IntergeoElement point1, IntergeoElement point2) {
		this.setID(id);
		this.setPoint1(point1);
		this.setPoint2(point2);
	}

	public void setPoint1(IntergeoElement point1) {
		this.point1 = point1;
	}

	public void setPoint2(IntergeoElement point2) {
		this.point2 = point2;
	}

	public IntergeoElement getPoint1() {
		return this.point1;
	}

	public IntergeoElement getPoint2() {
		return this.point2;
	}

	public double getX() {
		return (getPoint1().getX() + getPoint2().getX()) / 2;
	}

	public double getY() {
		return (getPoint1().getY() + getPoint2().getY()) / 2;
	}

	public double getW() {
		return 1.0;
	}

	@Override
	public String toString() {
		return "Point1:(" + point1.toString() + "), Point2:(" + point2.toString() + ")";
	}
}
