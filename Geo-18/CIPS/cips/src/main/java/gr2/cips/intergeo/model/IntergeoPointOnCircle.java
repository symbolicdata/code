package gr2.cips.intergeo.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class IntergeoPointOnCircle extends IntergeoElement {
	private IntergeoElement circle;
	private double x;
	private double y;
	private double w;

	public IntergeoPointOnCircle(String id, IntergeoElement circle, double x, double y, double w) {
		this.setID(id);
		this.circle = circle;
		this.x = x;
		this.y = y;
		this.w = w;
	}

	public double getX() {
		return x;
	}

	public void setX(double x) {
		this.x = x;
	}

	public double getY() {
		return y;
	}

	public void setY(double y) {
		this.y = y;
	}

	public IntergeoElement getCircle() {
		return circle;
	}

	public void setCircle(IntergeoElement circle) {
		this.circle = circle;
	}

	public double getW() {
		return w;
	}

	public void setW(double w) {
		this.w = w;
	}

	public double getParameter() {
		IntergeoCircleByCenterAndPoint tempCircle = (IntergeoCircleByCenterAndPoint) this.circle;
		double b = tempCircle.getCenterPointY();
		double r = tempCircle.getRadius();
		double y = getY();
		return Math.asin((y - b) / r);
	}

	@Override
	public String toString() {
		return "X:" + this.x + ", Y:" + this.y + "Circle:[" + circle.toString() + "]";
	}
}
