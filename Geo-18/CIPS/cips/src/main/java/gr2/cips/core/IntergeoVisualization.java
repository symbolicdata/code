package gr2.cips.core;

import org.apache.log4j.Logger;

import gr2.cips.intergeo.Intergeo;
import gr2.cips.jsxgraph.JSXGraph;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class IntergeoVisualization {
	final static Logger logger = Logger.getLogger(IntergeoVisualization.class);
	private Intergeo intergeo;
	private String visualizationFilePath;

	public IntergeoVisualization(Intergeo intergeo, String visualizationFilePath) {
		setIntergeo(intergeo);
		this.visualizationFilePath = visualizationFilePath;
	}

	public void setIntergeo(Intergeo intergeo) {
		this.intergeo = intergeo;
	}

	public void setVisualizationFilePath(String visualizationFilePath) {
		this.visualizationFilePath = visualizationFilePath;
	}

	public Intergeo getIntergeo() {
		return this.intergeo;
	}

	public String getVisualizationFilePath() {
		return this.visualizationFilePath;
	}

	public void visualize() {
		Intergeo2JSXGraph intergeo2JSXGraph = new Intergeo2JSXGraph(intergeo);
		JSXGraph jsxGraph = intergeo2JSXGraph.convert();
		jsxGraph.exportVisualization(getVisualizationFilePath());
	}
}
