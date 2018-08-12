package gr2.cips.cinderella.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public abstract class CinderellaElement {
	private String id;

	public CinderellaElement() {

	}

	public CinderellaElement(String id) {
		this.id = id;
	}

	public void setID(String id) {
		this.id = id;
	}

	public String getID() {
		return id;
	}

	public double getX() {
		return Double.NaN;
	}

	public double getY() {
		return Double.NaN;
	}

	public double getA() {
		return Double.NaN;
	}

	public double getB() {
		return Double.NaN;
	}

	public double getC() {
		return Double.NaN;
	}

	public String toString() {
		return null;
	}
}
