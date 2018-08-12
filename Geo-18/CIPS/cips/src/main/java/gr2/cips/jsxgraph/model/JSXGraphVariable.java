package gr2.cips.jsxgraph.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class JSXGraphVariable extends JSXGraphElement {
	private double value;

	public JSXGraphVariable(String id, double value) {
		this.setID(id);
		this.setValue(value);
	}

	public void setValue(double value) {
		this.value = value;
	}

	public double getValue() {
		return this.value;
	}

	@Override
	public String toString() {
		return Double.toString(getValue());
	}
}
