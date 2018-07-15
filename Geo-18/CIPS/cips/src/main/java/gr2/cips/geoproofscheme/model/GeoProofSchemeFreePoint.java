package gr2.cips.geoproofscheme.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class GeoProofSchemeFreePoint extends GeoProofSchemeElement {
	private GeoProofSchemeParameter xParameter;
	private GeoProofSchemeParameter yParameter;

	public GeoProofSchemeFreePoint(String id, GeoProofSchemeParameter xParameter, GeoProofSchemeParameter yParameter) {
		this.setID(id);
		this.setXParameter(xParameter);
		this.setYParameter(yParameter);
	}

	public GeoProofSchemeParameter getXParameter() {
		return xParameter;
	}

	public void setXParameter(GeoProofSchemeParameter xParameter) {
		this.xParameter = xParameter;
	}

	public GeoProofSchemeParameter getYParameter() {
		return yParameter;
	}

	public void setYParameter(GeoProofSchemeParameter yParameter) {
		this.yParameter = yParameter;
	}

	public double getX() {
		return this.xParameter.getValue();
	}

	public double getY() {
		return this.yParameter.getValue();
	}

	@Override
	public String toString() {
		return "X:" + getX() + ", Y:" + getY();
	}
}
