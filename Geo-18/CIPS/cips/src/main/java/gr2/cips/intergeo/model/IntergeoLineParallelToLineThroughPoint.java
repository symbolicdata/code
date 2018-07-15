package gr2.cips.intergeo.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class IntergeoLineParallelToLineThroughPoint extends IntergeoElement {
	private IntergeoElement point;
	private IntergeoElement line;

	public IntergeoLineParallelToLineThroughPoint(String id, IntergeoElement point, IntergeoElement line) {
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
