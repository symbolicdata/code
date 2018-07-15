package gr2.cips.jsxgraph.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class JSXGraphCircumCircle extends JSXGraphElement {
	private JSXGraphElement point1;
	private JSXGraphElement point2;
	private JSXGraphElement point3;

	public JSXGraphCircumCircle(String id, JSXGraphElement point1, JSXGraphElement point2, JSXGraphElement point3) {
		this.setID(id);
		this.setPoint1(point1);
		this.setPoint2(point2);
		this.setPoint3(point3);
	}

	public void setPoint1(JSXGraphElement point1) {
		this.point1 = point1;
	}

	public void setPoint2(JSXGraphElement point2) {
		this.point2 = point2;
	}

	public void setPoint3(JSXGraphElement point3) {
		this.point3 = point3;
	}

	public JSXGraphElement getPoint1() {
		return this.point1;
	}

	public JSXGraphElement getPoint2() {
		return this.point2;
	}

	public JSXGraphElement getPoint3() {
		return this.point3;
	}

	public double getCenterPointX() {
		double x1 = this.point1.getX();
		double y1 = this.point1.getY();
		double x2 = this.point2.getX();
		double y2 = this.point2.getY();
		double x3 = this.point3.getX();
		double y3 = this.point3.getY();
		double A = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2;
		double D = (x1 * x1 + y1 * y1) * (y3 - y2) + (x2 * x2 + y2 * y2) * (y1 - y3) + (x3 * x3 + y3 * y3) * (y2 - y1);
		return -D / (2 * A);
	}

	public double getCenterPointY() {
		double x1 = this.point1.getX();
		double y1 = this.point1.getY();
		double x2 = this.point2.getX();
		double y2 = this.point2.getY();
		double x3 = this.point3.getX();
		double y3 = this.point3.getY();
		double A = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2;
		double E = (x1 * x1 + y1 * y1) * (x2 - x3) + (x2 * x2 + y2 * y2) * (x3 - x1) + (x3 * x3 + y3 * y3) * (x1 - x2);
		return -E / (2 * A);
	}

	public double getRadius() {
		double x1 = this.point1.getX();
		double y1 = this.point1.getY();
		double x2 = this.point2.getX();
		double y2 = this.point2.getY();
		double x3 = this.point3.getX();
		double y3 = this.point3.getY();
		double A = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2;
		double C = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2;
		double D = (x1 * x1 + y1 * y1) * (y3 - y2) + (x2 * x2 + y2 * y2) * (y1 - y3) + (x3 * x3 + y3 * y3) * (y2 - y1);
		double E = (x1 * x1 + y1 * y1) * (x2 - x3) + (x2 * x2 + y2 * y2) * (x3 - x1) + (x3 * x3 + y3 * y3) * (x1 - x2);
		double F = (x1 * x1 + y1 * y1) * (x3 * y2 - x2 * y3) + (x2 * x2 + y2 * y2) * (x1 * y3 - x3 * y1)
				+ (x3 * x3 + y3 * y3) * (x2 * y1 - x1 * y2);
		return Math.sqrt((D * D + E * E - 4 * A * F) / (4 * A * C));
	}

	public double[][] getQuadraticMatrix() {
		double[][] quadraticMatrix = new double[3][3];
		double x1 = this.point1.getX();
		double y1 = this.point1.getY();
		double x2 = this.point2.getX();
		double y2 = this.point2.getY();
		double x3 = this.point3.getX();
		double y3 = this.point3.getY();
		double A = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2;
		double C = x1 * (y2 - y3) - y1 * (x2 - x3) + x2 * y3 - x3 * y2;
		double D = (x1 * x1 + y1 * y1) * (y3 - y2) + (x2 * x2 + y2 * y2) * (y1 - y3) + (x3 * x3 + y3 * y3) * (y2 - y1);
		double E = (x1 * x1 + y1 * y1) * (x2 - x3) + (x2 * x2 + y2 * y2) * (x3 - x1) + (x3 * x3 + y3 * y3) * (x1 - x2);
		double F = (x1 * x1 + y1 * y1) * (x3 * y2 - x2 * y3) + (x2 * x2 + y2 * y2) * (x1 * y3 - x3 * y1)
				+ (x3 * x3 + y3 * y3) * (x2 * y1 - x1 * y2);
		quadraticMatrix[0][0] = A;
		quadraticMatrix[0][1] = 0;
		quadraticMatrix[0][2] = D / 2;
		quadraticMatrix[1][0] = 0;
		quadraticMatrix[1][1] = C;
		quadraticMatrix[1][2] = E / 2;
		quadraticMatrix[2][0] = D / 2;
		quadraticMatrix[2][1] = E / 2;
		quadraticMatrix[2][2] = F;
		return quadraticMatrix;
	}

	@Override
	public String toString() {
		return "Point1:(" + point1.toString() + "), Point2:(" + point2.toString() + "), Point3:(" + point3.toString()
				+ ")";
	}
}
