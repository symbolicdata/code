package gr2.cips.jsxgraph.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class JSXGraphPCCircle extends JSXGraphElement {
	private JSXGraphElement centerPoint;
	private JSXGraphElement throughPoint;

	public JSXGraphPCCircle(String id, JSXGraphElement centerPoint, JSXGraphElement throughPoint) {
		this.setID(id);
		this.setCenterPoint(centerPoint);
		this.setThroughPoint(throughPoint);
	}

	public void setCenterPoint(JSXGraphElement centerPoint) {
		this.centerPoint = centerPoint;
	}

	public void setThroughPoint(JSXGraphElement throughPoint) {
		this.throughPoint = throughPoint;
	}

	public JSXGraphElement getCenterPoint() {
		return this.centerPoint;
	}

	public JSXGraphElement getThroughPoint() {
		return this.throughPoint;
	}

	public double getCenterPointX() {
		return getCenterPoint().getX();
	}

	public double getCenterPointY() {
		return getCenterPoint().getY();
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
