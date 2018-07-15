package gr2.cips.intergeo.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class IntergeoPointOnLine extends IntergeoElement {
	private IntergeoElement line;
	private double x;
	private double y;
	private double w;

	public IntergeoPointOnLine(String id, IntergeoElement line, double x, double y, double w) {
		this.setID(id);
		this.line = line;
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

	public IntergeoElement getLine() {
		return line;
	}

	public void setLine(IntergeoElement line) {
		this.line = line;
	}

	public double getW() {
		return w;
	}

	public double getParameter() {
		double a = this.line.getA();
		double b = this.line.getB();
		double c = this.line.getC();
		double y = getY();
		if (a == 0 || b == 0) {
			return 0;
		}
		return (c - y * b) / a;
	}

	public void setW(double w) {
		this.w = w;
	}

	@Override
	public String toString() {
		return "X:" + this.x + ", Y:" + this.y + "Line:[" + line.toString() + "]";
	}
}
