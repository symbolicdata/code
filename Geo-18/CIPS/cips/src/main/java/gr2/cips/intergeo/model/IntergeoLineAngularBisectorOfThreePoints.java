package gr2.cips.intergeo.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class IntergeoLineAngularBisectorOfThreePoints extends IntergeoElement {
	private IntergeoElement point1;
	private IntergeoElement point2;
	private IntergeoElement point3;

	public IntergeoLineAngularBisectorOfThreePoints(String id, IntergeoElement point1, IntergeoElement point2,
			IntergeoElement point3) {
		this.setID(id);
		this.setPoint1(point1);
		this.setPoint2(point2);
		this.setPoint3(point3);
	}

	public void setPoint1(IntergeoElement point1) {
		this.point1 = point1;
	}

	public void setPoint2(IntergeoElement point2) {
		this.point2 = point2;
	}

	public void setPoint3(IntergeoElement point3) {
		this.point3 = point3;
	}

	public IntergeoElement getPoint1() {
		return this.point1;
	}

	public IntergeoElement getPoint2() {
		return this.point2;
	}

	public IntergeoElement getPoint3() {
		return this.point3;
	}

	public double getA() {
		IntergeoLineThroughTwoPoints p1p2 = new IntergeoLineThroughTwoPoints(null, point1, point2);
		IntergeoLineThroughTwoPoints p2p3 = new IntergeoLineThroughTwoPoints(null, point2, point3);
		double a1 = p1p2.getA();
		double b1 = p1p2.getB();
		double a2 = p2p3.getA();
		double b2 = p2p3.getB();
		return a1 * Math.sqrt(a2 * a2 + b2 * b2) - a2 * Math.sqrt(a1 * a1 + b1 * b1);
	}

	public double getB() {
		IntergeoLineThroughTwoPoints p1p2 = new IntergeoLineThroughTwoPoints(null, point1, point2);
		IntergeoLineThroughTwoPoints p2p3 = new IntergeoLineThroughTwoPoints(null, point2, point3);
		double a1 = p1p2.getA();
		double b1 = p1p2.getB();
		double a2 = p2p3.getA();
		double b2 = p2p3.getB();
		return b1 * Math.sqrt(a2 * a2 + b2 * b2) - b2 * Math.sqrt(a1 * a1 + b1 * b1);
	}

	public double getC() {
		IntergeoLineThroughTwoPoints p1p2 = new IntergeoLineThroughTwoPoints(null, point1, point2);
		IntergeoLineThroughTwoPoints p2p3 = new IntergeoLineThroughTwoPoints(null, point2, point3);
		double a1 = p1p2.getA();
		double b1 = p1p2.getB();
		double c1 = -p1p2.getC();
		double a2 = p2p3.getA();
		double b2 = p2p3.getB();
		double c2 = -p2p3.getC();
		return -(c1 * Math.sqrt(a2 * a2 + b2 * b2) - c2 * Math.sqrt(a1 * a1 + b1 * b1));
	}

	@Override
	public String toString() {
		return "Point1:(" + point1.toString() + "), Point2:(" + point2.toString() + "), Point3:(" + point3.toString()
				+ ")";
	}
}