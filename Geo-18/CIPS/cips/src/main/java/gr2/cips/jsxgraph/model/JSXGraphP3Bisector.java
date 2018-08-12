package gr2.cips.jsxgraph.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class JSXGraphP3Bisector extends JSXGraphElement {
	private JSXGraphElement point1;
	private JSXGraphElement point2;
	private JSXGraphElement point3;

	public JSXGraphP3Bisector(String id, JSXGraphElement point1, JSXGraphElement point2, JSXGraphElement point3) {
		this.setID(id);
		this.setPoint1(point1);
		this.setPoint2(point2);
		this.setPoint3(point3);
	}

	public void setPoint1(JSXGraphElement point1) {
		this.point1 = point1;
	}

	public void setPoint2(JSXGraphElement point2) {
		this.point2 = point2;
	}

	public void setPoint3(JSXGraphElement point3) {
		this.point3 = point3;
	}

	public JSXGraphElement getPoint1() {
		return this.point1;
	}

	public JSXGraphElement getPoint2() {
		return this.point2;
	}

	public JSXGraphElement getPoint3() {
		return this.point3;
	}

	public double getA() {
		JSXGraphLine p1p2 = new JSXGraphLine(null, point1, point2);
		JSXGraphLine p2p3 = new JSXGraphLine(null, point2, point3);
		double a1 = p1p2.getA();
		double b1 = p1p2.getB();
		double a2 = p2p3.getA();
		double b2 = p2p3.getB();
		return a1 * Math.sqrt(a2 * a2 + b2 * b2) - a2 * Math.sqrt(a1 * a1 + b1 * b1);
	}

	public double getB() {
		JSXGraphLine p1p2 = new JSXGraphLine(null, point1, point2);
		JSXGraphLine p2p3 = new JSXGraphLine(null, point2, point3);
		double a1 = p1p2.getA();
		double b1 = p1p2.getB();
		double a2 = p2p3.getA();
		double b2 = p2p3.getB();
		return b1 * Math.sqrt(a2 * a2 + b2 * b2) - b2 * Math.sqrt(a1 * a1 + b1 * b1);
	}

	public double getC() {
		JSXGraphLine p1p2 = new JSXGraphLine(null, point1, point2);
		JSXGraphLine p2p3 = new JSXGraphLine(null, point2, point3);
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
