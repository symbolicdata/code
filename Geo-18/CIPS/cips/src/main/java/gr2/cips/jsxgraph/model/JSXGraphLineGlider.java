package gr2.cips.jsxgraph.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class JSXGraphLineGlider extends JSXGraphElement {
	private JSXGraphElement line;
	private JSXGraphParameter parameter;

	public JSXGraphLineGlider(String id, JSXGraphElement line, JSXGraphParameter parameter) {
		this.setID(id);
		this.line = line;
		this.parameter = parameter;
	}

	public JSXGraphElement getLine() {
		return line;
	}

	public void setLine(JSXGraphElement line) {
		this.line = line;
	}

	public JSXGraphParameter getParameter() {
		return parameter;
	}

	public void setParameter(JSXGraphParameter parameter) {
		this.parameter = parameter;
	}

	public double getX() {
		double a = this.line.getA();
		double b = this.line.getB();
		double c = this.line.getC();
		if (a == 0) {
			return this.parameter.getValue();
		} else if (b == 0) {
			return -c / a;
		} else {
			return 1.0;
		}
	}

	public double getY() {
		double a = this.line.getA();
		double b = this.line.getB();
		double c = this.line.getC();
		if (a == 0) {
			return -c / b;
		} else if (b == 0) {
			return this.parameter.getValue();
		} else {
			return -(a * this.parameter.getValue() - c) / b;
		}
	}

	@Override
	public String toString() {
		return "Line:" + line.toString() + ", " + "Parameter:" + this.parameter.toString();
	}
}
