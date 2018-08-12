package gr2.cips.cinderella.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class CinderellaCircleMP extends CinderellaElement {
	private CinderellaElement centerPoint;
	private CinderellaElement throughPoint;

	public CinderellaCircleMP(String id, CinderellaElement centerPoint, CinderellaElement throughPoint) {
		this.setID(id);
		this.setCenterPoint(centerPoint);
		this.setThroughPoint(throughPoint);
	}

	public void setCenterPoint(CinderellaElement centerPoint) {
		this.centerPoint = centerPoint;
	}

	public void setThroughPoint(CinderellaElement throughPoint) {
		this.throughPoint = throughPoint;
	}

	public CinderellaElement getCenterPoint() {
		return this.centerPoint;
	}

	public CinderellaElement getThroughPoint() {
		return this.throughPoint;
	}

	public double getRadius() {
		double xC = this.centerPoint.getX();
		double yC = this.centerPoint.getY();
		double xT = this.throughPoint.getX();
		double yT = this.throughPoint.getY();
		return Math.sqrt((xT - xC) * (xT - xC) + (yT - yC) * (yT - yC));
	}

	public double[][] getQuadraticMatrix() {
		double[][] quadraticMatrix = new double[3][3];
		quadraticMatrix[0][0] = 1;
		quadraticMatrix[0][1] = 0;
		quadraticMatrix[0][2] = (2 * this.centerPoint.getX() / 2);
		quadraticMatrix[1][0] = 0;
		quadraticMatrix[1][1] = 1;
		quadraticMatrix[1][2] = (2 * this.centerPoint.getY() / 2);
		quadraticMatrix[2][0] = (2 * this.centerPoint.getX() / 2);
		quadraticMatrix[2][1] = (2 * this.centerPoint.getY() / 2);
		quadraticMatrix[2][2] = this.centerPoint.getX() * this.centerPoint.getX()
				+ this.centerPoint.getY() * this.centerPoint.getY() - getRadius() * getRadius();
		return quadraticMatrix;
	}

	@Override
	public String toString() {
		return "Point1:(" + centerPoint.toString() + "), Point2:(" + throughPoint.toString() + ")";
	}
}