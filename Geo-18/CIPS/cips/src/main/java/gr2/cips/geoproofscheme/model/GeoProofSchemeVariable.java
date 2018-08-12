package gr2.cips.geoproofscheme.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class GeoProofSchemeVariable extends GeoProofSchemeElement {
	private double value;

	public GeoProofSchemeVariable(String id, double value) {
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
