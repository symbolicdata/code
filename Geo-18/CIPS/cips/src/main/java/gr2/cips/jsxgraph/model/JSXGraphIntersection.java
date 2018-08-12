package gr2.cips.jsxgraph.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class JSXGraphIntersection extends JSXGraphElement {
	private JSXGraphElement element1;
	private JSXGraphElement element2;

	public JSXGraphIntersection(String id, JSXGraphElement element1, JSXGraphElement element2) {
		this.setID(id);
		this.setElement1(element1);
		this.setElement2(element2);
	}

	public void setElement1(JSXGraphElement Element1) {
		this.element1 = Element1;
	}

	public void setElement2(JSXGraphElement Element2) {
		this.element2 = Element2;
	}

	public JSXGraphElement getElement1() {
		return this.element1;
	}

	public JSXGraphElement getElement2() {
		return this.element2;
	}

	public double getX() {
		double a1 = this.getElement1().getA();
		double a2 = this.getElement2().getA();
		double b1 = this.getElement1().getB();
		double b2 = this.getElement2().getB();
		double c1 = this.getElement1().getC();
		double c2 = this.getElement2().getC();
		if (b1 == 0)
			return -c1 / a1;
		if (b2 == 0)
			return -c2 / a2;
		return ((-c2 / b2 + c1 / b1) / (-a1 / b1 + a2 / b2));
	}

	public double getY() {
		double a1 = this.getElement1().getA();
		double b1 = this.getElement1().getB();
		double c1 = this.getElement1().getC();
		return (-a1 / b1) * getX() - c1 / b1;		
	}

	@Override
	public String toString() {
		return "Element1:[" + element1.toString() + "], " + "Element2:[" + element2.toString() + "]";
	}
}
