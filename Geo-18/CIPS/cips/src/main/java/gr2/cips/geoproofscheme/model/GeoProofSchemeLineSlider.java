package gr2.cips.geoproofscheme.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class GeoProofSchemeLineSlider extends GeoProofSchemeElement {
	private GeoProofSchemeElement line;
	private GeoProofSchemeParameter parameter;

	public GeoProofSchemeLineSlider(String id, GeoProofSchemeElement line, GeoProofSchemeParameter parameter) {
		this.setID(id);
		this.line = line;
		this.parameter = parameter;
	}

	public GeoProofSchemeElement getLine() {
		return line;
	}

	public void setLine(GeoProofSchemeElement line) {
		this.line = line;
	}

	public GeoProofSchemeElement getParameter() {
		return parameter;
	}

	public void setParameter(GeoProofSchemeParameter parameter) {
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
			return this.parameter.getValue();
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
		return "Line:(" + this.line.toString() + "), Parameter:" + this.parameter.toString();
	}
}
