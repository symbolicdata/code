package gr2.cips.cinderella.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class CinderellaFreePoint extends CinderellaElement {
	private double x;
	private double y;

	public CinderellaFreePoint(String id, double x, double y) {
		this.setID(id);
		this.setX(x);
		this.setY(y);
	}

	public void setX(double x) {
		this.x = x;
	}

	public void setY(double y) {
		this.y = y;
	}

	public double getX() {
		return this.x;
	}

	public double getY() {
		return this.y;
	}

	@Override
	public String toString() {
		return "X:" + getX() + ", Y:" + getY();
	}
}
