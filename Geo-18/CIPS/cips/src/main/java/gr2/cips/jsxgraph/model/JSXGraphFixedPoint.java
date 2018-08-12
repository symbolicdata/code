package gr2.cips.jsxgraph.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class JSXGraphFixedPoint extends JSXGraphElement {
	private JSXGraphElement point1;
	private JSXGraphElement point2;
	private double parameter;

	public JSXGraphFixedPoint(String id, JSXGraphElement point1, JSXGraphElement point2, double parameter) {
		this.setID(id);
		this.point1 = point1;
		this.point2 = point2;
		this.parameter = parameter;
	}

	public JSXGraphElement getPoint1() {
		return point1;
	}

	public void setPoint1(JSXGraphElement point1) {
		this.point1 = point1;
	}

	public JSXGraphElement getPoint2() {
		return point2;
	}

	public void setPoint2(JSXGraphElement point2) {
		this.point2 = point2;
	}

	public double getParameter() {
		return parameter;
	}

	public void setParameter(double parameter) {
		this.parameter = parameter;
	}

	public double getX() {
		double x1 = point1.getX();
		double x2 = point2.getX();
		double u = parameter;
		return (x1 + (x2 - x1) * u);
	}

	public double getY() {
		double y1 = point1.getY();
		double y2 = point2.getY();
		double u = parameter;
		return (y1 + (y2 - y1) * u);
	}

	public double getW() {
		return 1.0;
	}

	@Override
	public String toString() {
		return "Point1:(" + this.point1.toString() + "), Point2:(" + this.point1.toString() + "), Parameter:"
				+ this.parameter;
	}
}
