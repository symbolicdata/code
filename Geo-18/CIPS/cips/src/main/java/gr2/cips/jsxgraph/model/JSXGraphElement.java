package gr2.cips.jsxgraph.model;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public abstract class JSXGraphElement {
	public final static String INDEPENDENT_POINT_PROP = "strokecolor:'red',fillColor:'red'";
	public final static String DEPENDENT_POINT_PROP = "strokecolor:'green',fillColor:'green'";
	public final static String INDEPENDENT_LINE_PROP = "strokecolor:'blue',fillColor:'blue'";
	public final static String DEPENDENT_LINE_PROP = "strokecolor:'black',fillColor:'black'";

	private String id;
	private String properties;

	public JSXGraphElement() {

	}

	public JSXGraphElement(String id, String properties) {
		this.id = id;
		this.properties = properties;
	}

	public void setID(String id) {
		this.id = id;
	}

	public void setProperties(String properties) {
		this.properties = properties;
	}

	public String getID() {
		return this.id;
	}

	public String getProperties() {
		return this.properties;
	}

	public boolean isParameter() {
		return this instanceof JSXGraphParameter ? true : false;
	}

	public boolean isVariable() {
		return this instanceof JSXGraphVariable ? true : false;
	}

	public boolean isPoint() {
		return this instanceof JSXGraphPoint || this instanceof JSXGraphMidPoint || this instanceof JSXGraphIntersection
				|| this instanceof JSXGraphLineGlider || this instanceof JSXGraphCircleGlider
				|| this instanceof JSXGraphVarPoint || this instanceof JSXGraphFixedPoint ? true : false;
	}

	public boolean isLine() {
		return this instanceof JSXGraphLine || this instanceof JSXGraphParallel || this instanceof JSXGraphPerpendicular
				|| this instanceof JSXGraphP3Bisector ? true : false;
	}

	public boolean isCircle() {
		return this instanceof JSXGraphPCCircle || this instanceof JSXGraphCircumCircle ? true : false;
	}

	public double getValue() {
		return Double.NaN;
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
