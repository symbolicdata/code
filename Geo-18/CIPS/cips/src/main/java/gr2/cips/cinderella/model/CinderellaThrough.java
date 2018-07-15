package gr2.cips.cinderella.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class CinderellaThrough extends CinderellaElement {
	private CinderellaFreePoint throughPoint;
	private CinderellaFreePoint tempPoint;

	public CinderellaThrough(String id, CinderellaFreePoint throughPoint, CinderellaFreePoint tempPoint) {
		this.setID(id);
		this.setThroughPoint(throughPoint);
		this.setTempPoint(tempPoint);
	}

	public void setThroughPoint(CinderellaFreePoint throughPoint) {
		this.throughPoint = throughPoint;
	}

	public void setTempPoint(CinderellaFreePoint tempPoint) {
		this.tempPoint = tempPoint;
	}

	public CinderellaFreePoint getThroughPoint() {
		return this.throughPoint;
	}

	public CinderellaFreePoint getTempPoint() {
		return this.tempPoint;
	}
}
