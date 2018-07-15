package gr2.cips.jsxgraph.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class JSXGraphCircleGlider extends JSXGraphElement {
	private JSXGraphElement circle;
	private JSXGraphParameter parameter;

	public JSXGraphCircleGlider(String id, JSXGraphElement circle, JSXGraphParameter parameter) {
		this.setID(id);
		this.circle = circle;
		this.parameter = parameter;
	}

	public JSXGraphElement getCircle() {
		return circle;
	}

	public void setCircle(JSXGraphElement circle) {
		this.circle = circle;
	}

	public JSXGraphParameter getParameter() {
		return parameter;
	}

	public void setParameter(JSXGraphParameter parameter) {
		this.parameter = parameter;
	}

	public double getX() {
		JSXGraphPCCircle tempPCCircle = (JSXGraphPCCircle) circle;
		double a = tempPCCircle.getCenterPointX();
		double r = tempPCCircle.getRadius();
		double u = this.parameter.getValue();
		return a + r * Math.cos(u);
	}

	public double getY() {
		JSXGraphPCCircle tempPCCircle = (JSXGraphPCCircle) circle;
		double b = tempPCCircle.getCenterPointY();
		double r = tempPCCircle.getRadius();
		double u = this.parameter.getValue();
		return b + r * Math.sin(u);
	}

	@Override
	public String toString() {
		return "Circle:" + circle.toString() + ", " + "Parameter:" + this.parameter.toString();
	}
}
