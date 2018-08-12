package gr2.cips.geoproofscheme.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class GeoProofSchemeCircleSlider extends GeoProofSchemeElement {
	private GeoProofSchemeElement centerPoint;
	private GeoProofSchemeElement throughPoint;
	private GeoProofSchemeParameter parameter;

	public GeoProofSchemeCircleSlider(String id, GeoProofSchemeElement centerPoint, GeoProofSchemeElement throughPoint,
			GeoProofSchemeParameter parameter) {
		this.setID(id);
		this.setCenterPoint(centerPoint);
		this.setThroughPoint(throughPoint);
		this.parameter = parameter;
	}

	public void setCenterPoint(GeoProofSchemeElement centerPoint) {
		this.centerPoint = centerPoint;
	}

	public void setThroughPoint(GeoProofSchemeElement throughPoint) {
		this.throughPoint = throughPoint;
	}

	public void setParameter(GeoProofSchemeParameter parameter) {
		this.parameter = parameter;
	}

	public GeoProofSchemeElement getCenterPoint() {
		return this.centerPoint;
	}

	public GeoProofSchemeElement getThroughPoint() {
		return this.throughPoint;
	}

	public GeoProofSchemeParameter getParameter() {
		return parameter;
	}

	public double getX() {
		GeoProofSchemePCCircle tempPCCircle = new GeoProofSchemePCCircle(null, this.centerPoint, this.throughPoint);
		double a = tempPCCircle.getCenterPointX();
		double r = tempPCCircle.getRadius();
		double u = this.parameter.getValue();
		return a + r * Math.cos(u);
	}

	public double getY() {
		GeoProofSchemePCCircle tempPCCircle = new GeoProofSchemePCCircle(null, this.centerPoint, this.throughPoint);
		double b = tempPCCircle.getCenterPointY();
		double r = tempPCCircle.getRadius();
		double u = this.parameter.getValue();
		return b + r * Math.sin(u);
	}

	@Override
	public String toString() {
		return "CenterPoint:(" + this.centerPoint.toString() + "), ThroughPoint:(" + this.throughPoint.toString()
				+ "), Parameter:" + this.parameter;
	}
}
