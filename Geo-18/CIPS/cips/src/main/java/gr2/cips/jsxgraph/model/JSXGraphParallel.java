package gr2.cips.jsxgraph.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class JSXGraphParallel extends JSXGraphElement {
	private JSXGraphElement point;
	private JSXGraphElement line;

	public JSXGraphParallel(String id, JSXGraphElement point, JSXGraphElement line) {
		this.setID(id);
		this.setPoint(point);
		this.setLine(line);
	}

	public void setPoint(JSXGraphElement point) {
		this.point = point;
	}

	public JSXGraphElement getPoint() {
		return this.point;
	}

	public void setLine(JSXGraphElement line) {
		this.line = line;
	}

	public JSXGraphElement getLine() {
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
