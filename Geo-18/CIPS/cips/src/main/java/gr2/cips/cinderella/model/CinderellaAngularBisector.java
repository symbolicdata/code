package gr2.cips.cinderella.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class CinderellaAngularBisector extends CinderellaElement {
	private CinderellaMeet meet;

	public CinderellaAngularBisector(String id, CinderellaMeet meet) {
		this.setID(id);
		this.setMeet(meet);
	}

	public void setMeet(CinderellaMeet meet) {
		this.meet = meet;
	}

	public CinderellaMeet getMeet() {
		return this.meet;
	}
}
