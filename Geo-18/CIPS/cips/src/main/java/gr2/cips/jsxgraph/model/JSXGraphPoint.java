package gr2.cips.jsxgraph.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class JSXGraphPoint extends JSXGraphElement {
	private JSXGraphElement xElement;
	private JSXGraphElement yElement;
	private JSXGraphElement wElement;

	public JSXGraphPoint(String id, JSXGraphElement xElement, JSXGraphElement yElement, JSXGraphElement wElement) {
		this.setID(id);
		this.setXElement(xElement);
		this.setYElement(yElement);
		this.setWElement(wElement);
	}

	public JSXGraphElement getXElement() {
		return xElement;
	}

	public void setXElement(JSXGraphElement xElement) {
		this.xElement = xElement;
	}

	public JSXGraphElement getYElement() {
		return yElement;
	}

	public void setYElement(JSXGraphElement yElement) {
		this.yElement = yElement;
	}

	public JSXGraphElement getWElement() {
		return wElement;
	}

	public void setWElement(JSXGraphElement wElement) {
		this.wElement = wElement;
	}

	public double getX() {
		return this.xElement.getValue();
	}

	public double getY() {
		return this.yElement.getValue();
	}

	public double getW() {
		return this.wElement.getValue();
	}

	@Override
	public String toString() {
		return "X:" + getX() + ", Y:" + getY();
	}
}
