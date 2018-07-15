package gr2.cips.jsxgraph.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class JSXGraphParameter extends JSXGraphElement {
	public final static String CONST_IDENTITY = Math.abs("CONSTANT".hashCode()) + "CONSTANT";
	private double value;

	public JSXGraphParameter(String id, double value) {
		this.setID(id);
		this.setValue(value);
	}

	public void setValue(double value) {
		this.value = value;
	}

	public double getValue() {
		return this.value;
	}

	public boolean isConstant() {
		if (this.getID().contains(CONST_IDENTITY)) {
			return true;
		}
		return false;
	}

	@Override
	public String toString() {
		return Double.toString(getValue());
	}
}
