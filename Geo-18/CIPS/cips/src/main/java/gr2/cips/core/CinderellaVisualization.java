package gr2.cips.core;

import org.apache.log4j.Logger;

import gr2.cips.cinderella.Cinderella;
import gr2.cips.jsxgraph.JSXGraph;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class CinderellaVisualization {
	final static Logger logger = Logger.getLogger(CinderellaVisualization.class);
	private Cinderella cinderella;
	private String visualizationFilePath;

	public CinderellaVisualization(Cinderella cinderella, String visualizationFilePath) {
		setCinderella(cinderella);
		this.visualizationFilePath = visualizationFilePath;
	}

	public void setCinderella(Cinderella cinderella) {
		this.cinderella = cinderella;
	}

	public void setVisualizationFilePath(String visualizationFilePath) {
		this.visualizationFilePath = visualizationFilePath;
	}

	public Cinderella getCinderella() {
		return this.cinderella;
	}

	public String getVisualizationFilePath() {
		return this.visualizationFilePath;
	}

	public void visualize() {
		Cinderella2JSXGraph cinderella2JSXGraph = new Cinderella2JSXGraph(cinderella);
		JSXGraph jsxGraph = cinderella2JSXGraph.convert();
		jsxGraph.exportVisualization(getVisualizationFilePath());
	}
}
