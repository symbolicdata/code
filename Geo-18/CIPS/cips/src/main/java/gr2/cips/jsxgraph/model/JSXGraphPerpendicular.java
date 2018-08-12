package gr2.cips.jsxgraph.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class JSXGraphPerpendicular extends JSXGraphElement {
	private JSXGraphElement point;
	private JSXGraphElement line;

	public JSXGraphPerpendicular(String id, JSXGraphElement point, JSXGraphElement line) {
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
