package gr2.cips.intergeo.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class IntergeoLinePerpendicularToLineThroughPoint extends IntergeoElement {
	private IntergeoElement point;
	private IntergeoElement line;

	public IntergeoLinePerpendicularToLineThroughPoint(String id, IntergeoElement point, IntergeoElement line) {
		this.setID(id);
		this.setPoint(point);
		this.setLine(line);
	}

	public void setPoint(IntergeoElement point) {
		this.point = point;
	}

	public IntergeoElement getPoint() {
		return this.point;
	}

	public void setLine(IntergeoElement line) {
		this.line = line;
	}

	public IntergeoElement getLine() {
		return this.line;
	}

	public double getA() {
		return this.getLine().getB();
	}

	public double getB() {
		return -this.getLine().getA();
	}

	public double getC() {
		return -(this.getPoint().getX() * this.getLine().getB() - this.getLine().getA() * this.getPoint().getY());
	}

	@Override
	public String toString() {
		return "Point:(" + point.toString() + "), " + "Line:[" + line.toString() + "]";
	}
}
