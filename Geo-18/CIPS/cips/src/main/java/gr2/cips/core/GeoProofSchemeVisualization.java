package gr2.cips.core;

import org.apache.log4j.Logger;

import gr2.cips.geoproofscheme.GeoProofScheme;
import gr2.cips.jsxgraph.JSXGraph;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class GeoProofSchemeVisualization {
	final static Logger logger = Logger.getLogger(GeoProofSchemeVisualization.class);
	private GeoProofScheme geoProofScheme;
	private String visualizationFilePath;

	public GeoProofSchemeVisualization(GeoProofScheme geoProofScheme, String visualizationFilePath) {
		setGeoProofScheme(geoProofScheme);
		this.visualizationFilePath = visualizationFilePath;
	}

	public void setGeoProofScheme(GeoProofScheme geoProofScheme) {
		this.geoProofScheme = geoProofScheme;
	}

	public void setVisualizationFilePath(String visualizationFilePath) {
		this.visualizationFilePath = visualizationFilePath;
	}

	public GeoProofScheme getGeoProofScheme() {
		return this.geoProofScheme;
	}

	public String getVisualizationFilePath() {
		return this.visualizationFilePath;
	}

	public void visualize() {
		GeoProofScheme2JSXGraph geoProofScheme2JSXGraph = new GeoProofScheme2JSXGraph(geoProofScheme);
		JSXGraph jsxGraph = geoProofScheme2JSXGraph.convert();
		jsxGraph.exportVisualization(getVisualizationFilePath());
	}
}
