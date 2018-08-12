package gr2.cips.geoproofscheme;

import gr2.cips.geoproofscheme.model.GeoProofSchemeAltitude;
import gr2.cips.geoproofscheme.model.GeoProofSchemeCircleSlider;
import gr2.cips.geoproofscheme.model.GeoProofSchemeElement;
import gr2.cips.geoproofscheme.model.GeoProofSchemeFixedPoint;
import gr2.cips.geoproofscheme.model.GeoProofSchemeFreePoint;
import gr2.cips.geoproofscheme.model.GeoProofSchemeIntersectionPoint;
import gr2.cips.geoproofscheme.model.GeoProofSchemeLineSlider;
import gr2.cips.geoproofscheme.model.GeoProofSchemeMedian;
import gr2.cips.geoproofscheme.model.GeoProofSchemeMidPoint;
import gr2.cips.geoproofscheme.model.GeoProofSchemeOrthoLine;
import gr2.cips.geoproofscheme.model.GeoProofSchemeP3Bisector;
import gr2.cips.geoproofscheme.model.GeoProofSchemeP3Circle;
import gr2.cips.geoproofscheme.model.GeoProofSchemePBisector;
import gr2.cips.geoproofscheme.model.GeoProofSchemePCCircle;
import gr2.cips.geoproofscheme.model.GeoProofSchemePPLine;
import gr2.cips.geoproofscheme.model.GeoProofSchemeParLine;
import gr2.cips.geoproofscheme.model.GeoProofSchemeParameter;
import gr2.cips.geoproofscheme.model.GeoProofSchemeVarPoint;
import org.apache.commons.io.FileUtils;
import org.apache.commons.lang3.math.NumberUtils;
import org.apache.log4j.Logger;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Random;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class GeoProofScheme {
	final static Logger logger = Logger.getLogger(GeoProofScheme.class);
	private List<GeoProofSchemeElement> geoProofSchemeElements;
	private String title;

	public GeoProofScheme() {
		geoProofSchemeElements = new ArrayList<GeoProofSchemeElement>();
	}

	public void setGeoProofSchemeElements(List<GeoProofSchemeElement> geoProofSchemeElements) {
		this.geoProofSchemeElements = geoProofSchemeElements;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public List<GeoProofSchemeElement> getGeoProofSchemeElements() {
		return this.geoProofSchemeElements;
	}

	public String getTitle() {
		return this.title;
	}

	public boolean loadFromFile(String geoProofSchemeFilePath, String parameterFilePath) {
		try {
			File geoProofSchemeFile = new File(geoProofSchemeFilePath);
			DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
			DocumentBuilder documentBuilder = documentBuilderFactory.newDocumentBuilder();
			Document document = documentBuilder.parse(geoProofSchemeFile);

			document.getDocumentElement().normalize();

			if (document.getElementsByTagName("prooftype").getLength() == 1) {
				if (!document.getElementsByTagName("prooftype").item(0).getChildNodes().item(0).getNodeValue().trim()
						.toLowerCase().equals("constructive")) {
					logger.error("Only support constructive-prooftype.");
					return false;
				}
			}

			if (document.getElementsByTagName("Title").getLength() == 1) {
				final String[] inputPaths = geoProofSchemeFilePath.split("/");
				final String[] inputFile = inputPaths[inputPaths.length - 1].split("\\.");
				final String newName = String.join(".", Arrays.copyOf(inputFile, inputFile.length-1));
				setTitle(newName);
			}

			if (document.getElementsByTagName("parameters").getLength() == 1) {
				List<String> parameterIDs = Arrays.asList(document.getElementsByTagName("parameters").item(0)
						.getChildNodes().item(0).getNodeValue().split(","));
				if (!isParameterMatching(parameterIDs, parameterFilePath)) {
					generateAndSaveParameters(parameterIDs, parameterFilePath);
					if (isParameterMatching(parameterIDs, parameterFilePath)) {
						parseParameters(parameterIDs, parameterFilePath);
					} else {
						logger.error("Parameters do not match");
						return false;
					}
				} else {
					parseParameters(parameterIDs, parameterFilePath);
				}
			}

			if (document.getElementsByTagName("Points").getLength() == 1) {
				NodeList pointsChildNodes = document.getElementsByTagName("Points").item(0).getChildNodes();
				for (int i = 0; i < pointsChildNodes.getLength(); i++) {
					if (pointsChildNodes.item(i).getNodeType() == Node.ELEMENT_NODE) {
						String id = pointsChildNodes.item(i).getAttributes().getNamedItem("id").getNodeValue();
						String rawData = pointsChildNodes.item(i).getFirstChild().getNodeValue();
						GeoProofSchemeFreePoint geoProofSchemeFreePoint = parseFreePoint(id, rawData);
						if (geoProofSchemeFreePoint != null) {
							addElement(geoProofSchemeFreePoint);
							logger.info("Found point: ID:" + geoProofSchemeFreePoint.getID() + ", "
									+ geoProofSchemeFreePoint.toString());
						} else {
							return false;
						}
					}
				}
			}

			if (document.getElementsByTagName("Assignments").getLength() == 1) {
				NodeList assignmentChildNodes = document.getElementsByTagName("Assignments").item(0).getChildNodes();
				for (int i = 0; i < assignmentChildNodes.getLength(); i++) {
					if (assignmentChildNodes.item(i).getNodeType() == Node.ELEMENT_NODE) {
						String id = assignmentChildNodes.item(i).getAttributes().getNamedItem("id").getNodeValue();
						String rawData = assignmentChildNodes.item(i).getFirstChild().getNodeValue();

						if (rawData.matches(".*midpoint.*")) {
							GeoProofSchemeMidPoint geoProofSchemeMidPoint = parseMidPoint(id, rawData);
							if (geoProofSchemeMidPoint != null) {
								addElement(geoProofSchemeMidPoint);
								logger.info("Found midpoint: ID:" + geoProofSchemeMidPoint.getID() + ", "
										+ geoProofSchemeMidPoint.toString());
							} else {
								return false;
							}
						} else if (rawData.matches(".*intersection_point.*")) {
							GeoProofSchemeIntersectionPoint geoProofSchemeIntersectionPoint = parseIntersectionPoint(id,
									rawData);
							if (geoProofSchemeIntersectionPoint != null) {
								addElement(geoProofSchemeIntersectionPoint);
								logger.info("Found intersection_point: ID:" + geoProofSchemeIntersectionPoint.getID()
										+ ", " + geoProofSchemeIntersectionPoint.toString());
							} else {
								return false;
							}
						} else if (rawData.matches(".*circle_slider.*")) {
							GeoProofSchemeCircleSlider geoProofSchemeCircleSlider = parseCircleSlider(id, rawData);
							if (geoProofSchemeCircleSlider != null) {
								addElement(geoProofSchemeCircleSlider);
								logger.info("Found circle_slider: ID:" + geoProofSchemeCircleSlider.getID() + ", "
										+ geoProofSchemeCircleSlider.toString());
							} else {
								return false;
							}
						} else if (rawData.matches(".*line_slider.*")) {
							GeoProofSchemeLineSlider geoProofSchemeLineSlider = parseLineSlider(id, rawData);
							if (geoProofSchemeLineSlider != null) {
								addElement(geoProofSchemeLineSlider);
								logger.info("Found line_slider: ID:" + geoProofSchemeLineSlider.getID() + ", "
										+ geoProofSchemeLineSlider.toString());
							} else {
								return false;
							}
						} else if (rawData.matches(".*varpoint.*")) {
							GeoProofSchemeVarPoint geoProofSchemeVarPoint = parseVarPoint(id, rawData);
							if (geoProofSchemeVarPoint != null) {
								addElement(geoProofSchemeVarPoint);
								logger.info("Found varpoint: ID:" + geoProofSchemeVarPoint.getID() + ", "
										+ geoProofSchemeVarPoint.toString());
							} else {
								return false;
							}
						} else if (rawData.matches(".*fixedpoint.*")) {
							GeoProofSchemeFixedPoint geoProofSchemeFixedPoint = parseFixedPoint(id, rawData);
							if (geoProofSchemeFixedPoint != null) {
								addElement(geoProofSchemeFixedPoint);
								logger.info("Found fixedpoint: ID:" + geoProofSchemeFixedPoint.getID() + ", "
										+ geoProofSchemeFixedPoint.toString());
							} else {
								return false;
							}
						} else if (rawData.matches(".*pp_line.*")) {
							GeoProofSchemePPLine geoProofSchemePPLine = parsePPLine(id, rawData);
							if (geoProofSchemePPLine != null) {
								addElement(geoProofSchemePPLine);
								logger.info("Found pp_line: ID:" + geoProofSchemePPLine.getID() + ", "
										+ geoProofSchemePPLine.toString());
							} else {
								return false;
							}
						} else if (rawData.matches(".*par_line.*")) {
							GeoProofSchemeParLine geoProofSchemeParLine = parseParLine(id, rawData);
							if (geoProofSchemeParLine != null) {
								addElement(geoProofSchemeParLine);
								logger.info("Found par_line: ID:" + geoProofSchemeParLine.getID() + ", "
										+ geoProofSchemeParLine.toString());
							} else {
								return false;
							}
						} else if (rawData.matches(".*ortho_line.*")) {
							GeoProofSchemeOrthoLine geoProofSchemeOrthoLine = parseOrthoLine(id, rawData);
							if (geoProofSchemeOrthoLine != null) {
								addElement(geoProofSchemeOrthoLine);
								logger.info("Found ortho_line: ID:" + geoProofSchemeOrthoLine.getID() + ", "
										+ geoProofSchemeOrthoLine.toString());
							} else {
								return false;
							}
						} else if (rawData.matches(".*altitude.*")) {
							GeoProofSchemeAltitude geoProofSchemeAltitude = parseAltitude(id, rawData);
							if (geoProofSchemeAltitude != null) {
								addElement(geoProofSchemeAltitude);
								logger.info("Found altitude: ID:" + geoProofSchemeAltitude.getID() + ", "
										+ geoProofSchemeAltitude.toString());
							} else {
								return false;
							}
						} else if (rawData.matches(".*p_bisector.*")) {
							GeoProofSchemePBisector geoProofSchemePBisector = parsePBisector(id, rawData);
							if (geoProofSchemePBisector != null) {
								addElement(geoProofSchemePBisector);
								logger.info("Found p_bisector: ID:" + geoProofSchemePBisector.getID() + ", "
										+ geoProofSchemePBisector.toString());
							} else {
								return false;
							}
						} else if (rawData.matches(".*median.*")) {
							GeoProofSchemeMedian geoProofSchemeMedian = parseMedian(id, rawData);
							if (geoProofSchemeMedian != null) {
								addElement(geoProofSchemeMedian);
								logger.info("Found median: ID:" + geoProofSchemeMedian.getID() + ", "
										+ geoProofSchemeMedian.toString());
							} else {
								return false;
							}
						} else if (rawData.matches(".*p3_bisector.*")) {
							GeoProofSchemeP3Bisector geoProofSchemeP3Bisector = parseP3Bisector(id, rawData);
							if (geoProofSchemeP3Bisector != null) {
								addElement(geoProofSchemeP3Bisector);
								logger.info("Found p3_bisector: ID:" + geoProofSchemeP3Bisector.getID() + ", "
										+ geoProofSchemeP3Bisector.toString());
							} else {
								return false;
							}
						} else if (rawData.matches(".*p3_circle.*")) {
							GeoProofSchemeP3Circle geoProofSchemeP3Circle = parseP3Circle(id, rawData);
							if (geoProofSchemeP3Circle != null) {
								addElement(geoProofSchemeP3Circle);
								logger.info("Found p3_circle: ID:" + geoProofSchemeP3Circle.getID() + ", "
										+ geoProofSchemeP3Circle.toString());
							} else {
								return false;
							}
						} else if (rawData.matches(".*pc_circle.*")) {
							GeoProofSchemePCCircle geoProofSchemePCCircle = parsePCCircle(id, rawData);
							if (geoProofSchemePCCircle != null) {
								addElement(geoProofSchemePCCircle);
								logger.info("Found pc_circle: ID:" + geoProofSchemePCCircle.getID() + ", "
										+ geoProofSchemePCCircle.toString());
							} else {
								return false;
							}
						} else {
							logger.error("Error while parsing element ID:" + id);
							logger.error("Not yet implemented: " + rawData);
							return false;
						}
					}
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
			return false;
		}
		return true;
	}

	public void parseParameters(List<String> parameterIDs, String parameterFilePath) {
		Map<String, Double> parametersFromFile = new HashMap<String, Double>();
		try (BufferedReader bufferedReader = new BufferedReader(new FileReader(parameterFilePath))) {
			String tempString;
			while ((tempString = bufferedReader.readLine()) != null) {
				parametersFromFile.put(tempString.split("\t")[0], NumberUtils.toDouble(tempString.split("\t")[1]));
			}
		} catch (Exception e) {
			e.printStackTrace();
		}

		for (String parameterID : parameterIDs) {
			GeoProofSchemeParameter geoProofSchemeParameter = new GeoProofSchemeParameter(parameterID,
					parametersFromFile.get(parameterID));
			addElement(geoProofSchemeParameter);
			logger.info("Found parameter: ID:" + geoProofSchemeParameter.getID() + ", Value:"
					+ geoProofSchemeParameter.getValue());
		}
	}

	private void generateAndSaveParameters(final List<String> parameterIDs, final String parameterFilePath) {
		Random random = new Random();
		StringBuilder parameters = new StringBuilder();
		for (String parameterID : parameterIDs) {
			double RANDOM_VALUE = random.nextDouble()*10;
			RANDOM_VALUE = BigDecimal.valueOf(RANDOM_VALUE).setScale(2, RoundingMode.HALF_UP).doubleValue();
			parameters.append(parameterID).append("\t").append(RANDOM_VALUE).append("\n");
		}
		try {
			FileUtils.writeStringToFile(new File(parameterFilePath), parameters.toString());
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public GeoProofSchemeFreePoint parseFreePoint(String id, String rawData) {
		String rawX = rawData.substring(6, rawData.length() - 1).split(",")[0].trim();
		String rawY = rawData.substring(6, rawData.length() - 1).split(",")[1].trim();
		GeoProofSchemeParameter xParameter;
		GeoProofSchemeParameter yParameter;

		if (NumberUtils.isCreatable(rawX)) {
			String xID = GeoProofSchemeParameter.CONST_IDENTITY + String.valueOf(rawX);
			xParameter = (GeoProofSchemeParameter) getElementByID(xID);
			if (xParameter == null) {
				xParameter = new GeoProofSchemeParameter(GeoProofSchemeParameter.CONST_IDENTITY + String.valueOf(rawX),
						NumberUtils.toDouble(rawX));
				addElement(xParameter);
			}
		} else {
			xParameter = (GeoProofSchemeParameter) getElementByID(rawX);
			if (xParameter == null) {
				logger.error("Error while parsing FreePoint: ID:" + id);
				return null;
			}
		}

		if (NumberUtils.isCreatable(rawY)) {
			String yID = GeoProofSchemeParameter.CONST_IDENTITY + String.valueOf(rawY);
			yParameter = (GeoProofSchemeParameter) getElementByID(yID);
			if (yParameter == null) {
				yParameter = new GeoProofSchemeParameter(GeoProofSchemeParameter.CONST_IDENTITY + String.valueOf(rawY),
						NumberUtils.toDouble(rawY));
				addElement(yParameter);
			}
		} else {
			yParameter = (GeoProofSchemeParameter) getElementByID(rawY);
			if (yParameter == null) {
				logger.error("Error while parsing FreePoint: ID:" + id);
				return null;
			}
		}
		return new GeoProofSchemeFreePoint(id, xParameter, yParameter);
	}

	public GeoProofSchemeMidPoint parseMidPoint(String id, String rawData) {
		String point1ID = rawData.substring(9, rawData.length() - 1).split(",")[0].trim();
		String point2ID = rawData.substring(9, rawData.length() - 1).split(",")[1].trim();
		GeoProofSchemeElement point1 = getElementByID(point1ID);
		GeoProofSchemeElement point2 = getElementByID(point2ID);
		if (point1 == null || point2 == null) {
			logger.error("Error while parsing midpoint: ID:" + id);
			return null;
		} else {
			if (!point1.isPoint() || !point2.isPoint()) {
				logger.error("Error while parsing midpoint: ID:" + id);
				return null;
			} else {
				return new GeoProofSchemeMidPoint(id, point1, point2);
			}
		}
	}

	public GeoProofSchemeIntersectionPoint parseIntersectionPoint(String id, String rawData) {
		String line1ID = rawData.substring(19, rawData.length() - 1).split(",")[0].trim();
		String line2ID = rawData.substring(19, rawData.length() - 1).split(",")[1].trim();
		GeoProofSchemeElement line1 = getElementByID(line1ID);
		GeoProofSchemeElement line2 = getElementByID(line2ID);
		if (line1 == null || line2 == null) {
			logger.error("Error while parsing intersection_point: ID:" + id);
			return null;
		} else {
			if (!line1.isLine() || !line2.isLine()) {
				logger.error("Error while parsing intersection_point: ID:" + id);
				return null;
			} else {
				return new GeoProofSchemeIntersectionPoint(id, line1, line2);
			}
		}
	}

	public GeoProofSchemeCircleSlider parseCircleSlider(String id, String rawData) {
		String centerPointID = rawData.substring(14, rawData.length() - 1).split(",")[0].trim();
		String throughPointID = rawData.substring(14, rawData.length() - 1).split(",")[1].trim();
		String rawParameter = rawData.substring(14, rawData.length() - 1).split(",")[2].trim();

		GeoProofSchemeElement centerPoint = getElementByID(centerPointID);
		GeoProofSchemeElement throughPoint = getElementByID(throughPointID);
		GeoProofSchemeParameter parameter;

		if (centerPoint == null || throughPoint == null) {
			logger.error("Error while parsing circle_slider: ID:" + id);
			return null;
		} else if (!centerPoint.isPoint() || !throughPoint.isPoint()) {
			logger.error("Error while parsing circle_slider: ID:" + id);
			return null;
		}

		if (NumberUtils.isCreatable(rawParameter)) {
			String xID = GeoProofSchemeParameter.CONST_IDENTITY + String.valueOf(rawParameter);
			parameter = (GeoProofSchemeParameter) getElementByID(xID);
			if (parameter == null) {
				parameter = new GeoProofSchemeParameter(
						GeoProofSchemeParameter.CONST_IDENTITY + String.valueOf(rawParameter),
						NumberUtils.toDouble(rawParameter));
				addElement(parameter);
			}
		} else {
			parameter = (GeoProofSchemeParameter) getElementByID(rawParameter);
			if (parameter == null) {
				logger.error("Error while parsing circle_slider: ID:" + id);
				return null;
			}
		}

		GeoProofSchemePCCircle tempPCCirle = null;
		for (GeoProofSchemeElement geoProofSchemeElement : geoProofSchemeElements) {
			if (geoProofSchemeElement instanceof GeoProofSchemePCCircle) {
				if (((GeoProofSchemePCCircle) geoProofSchemeElement).getCenterPoint().getID()
						.equals(centerPoint.getID())
						&& ((GeoProofSchemePCCircle) geoProofSchemeElement).getThroughPoint().getID()
								.equals(throughPoint.getID())) {
					tempPCCirle = (GeoProofSchemePCCircle) geoProofSchemeElement;
					break;
				} else {
					tempPCCirle = null;
				}
			}
		}
		if (tempPCCirle == null) {
			tempPCCirle = new GeoProofSchemePCCircle("cir" + centerPoint.getID() + throughPoint.getID(), centerPoint,
					throughPoint);
			addElement(tempPCCirle);
		}
		return new GeoProofSchemeCircleSlider(id, centerPoint, throughPoint, parameter);
	}

	public GeoProofSchemeLineSlider parseLineSlider(String id, String rawData) {
		String lineID = rawData.substring(12, rawData.length() - 1).split(",")[0].trim();
		String rawParameter = rawData.substring(12, rawData.length() - 1).split(",")[1].trim();

		GeoProofSchemeElement line = getElementByID(lineID);
		GeoProofSchemeParameter parameter;

		if (line == null) {
			logger.error("Error while parsing line_slider: ID:" + id);
			return null;
		} else if (!line.isLine()) {
			logger.error("Error while parsing line_slider: ID:" + id);
			return null;
		}
		if (NumberUtils.isCreatable(rawParameter)) {
			String xID = GeoProofSchemeParameter.CONST_IDENTITY + String.valueOf(rawParameter);
			parameter = (GeoProofSchemeParameter) getElementByID(xID);
			if (parameter == null) {
				parameter = new GeoProofSchemeParameter(
						GeoProofSchemeParameter.CONST_IDENTITY + String.valueOf(rawParameter),
						NumberUtils.toDouble(rawParameter));
				addElement(parameter);
			}
		} else {
			parameter = (GeoProofSchemeParameter) getElementByID(rawParameter);
			if (parameter == null) {
				logger.error("Error while parsing line_slider: ID:" + id);
				return null;
			}
		}
		return new GeoProofSchemeLineSlider(id, line, parameter);
	}

	public GeoProofSchemeVarPoint parseVarPoint(String id, String rawData) {
		String point1ID = rawData.substring(9, rawData.length() - 1).split(",")[0].trim();
		String point2ID = rawData.substring(9, rawData.length() - 1).split(",")[1].trim();
		String parameterID = rawData.substring(12, rawData.length() - 1).split(",")[2].trim();

		GeoProofSchemeElement point1 = getElementByID(point1ID);
		GeoProofSchemeElement point2 = getElementByID(point2ID);
		GeoProofSchemeElement parameter = getElementByID(parameterID);

		if (point1 == null || point2 == null || parameter == null) {
			logger.error("Error while parsing line_slider: ID:" + id);
			return null;
		} else if (!point1.isPoint() || !point2.isPoint() || !parameter.isParameter()) {
			logger.error("Error while parsing line_slider: ID:" + id);
			return null;
		}
		/*
		 * GeoProofSchemePPLine tempPPLine = null; for (GeoProofSchemeElement
		 * geoProofSchemeElement : geoProofSchemeElements) { if (geoProofSchemeElement
		 * instanceof GeoProofSchemePPLine) { if (((GeoProofSchemePPLine)
		 * geoProofSchemeElement).getPoint1().getID().equals(point1.getID()) &&
		 * ((GeoProofSchemePPLine)
		 * geoProofSchemeElement).getPoint2().getID().equals(point2.getID())) {
		 * tempPPLine = (GeoProofSchemePPLine) geoProofSchemeElement; break; } else {
		 * tempPPLine = null; } } }
		 * 
		 * if (tempPPLine == null) { tempPPLine = new
		 * GeoProofSchemePPLine(point1.getID() + point2.getID(), point1, point2);
		 * addElement(tempPPLine); }
		 */
		return new GeoProofSchemeVarPoint(id, point1, point2, (GeoProofSchemeParameter) parameter);
	}

	public GeoProofSchemeFixedPoint parseFixedPoint(String id, String rawData) {
		String point1ID = rawData.substring(11, rawData.length() - 1).split(",")[0].trim();
		String point2ID = rawData.substring(11, rawData.length() - 1).split(",")[1].trim();
		String rawParameter = rawData.substring(12, rawData.length() - 1).split(",")[2].trim();

		GeoProofSchemeElement point1 = getElementByID(point1ID);
		GeoProofSchemeElement point2 = getElementByID(point2ID);

		if (point1 == null || point2 == null || !NumberUtils.isCreatable(rawParameter)) {
			logger.error("Error while parsing fixedpoint: ID:" + id);
			return null;
		} else if (!point1.isPoint() || !point2.isPoint()) {
			logger.error("Error while parsing fixedpoint: ID:" + id);
			return null;
		}
		return new GeoProofSchemeFixedPoint(id, point1, point2, NumberUtils.toDouble(rawParameter));
	}

	public GeoProofSchemePPLine parsePPLine(String id, String rawData) {
		String point1ID = rawData.substring(8, rawData.length() - 1).split(",")[0].trim();
		String point2ID = rawData.substring(8, rawData.length() - 1).split(",")[1].trim();
		GeoProofSchemeElement point1 = getElementByID(point1ID);
		GeoProofSchemeElement point2 = getElementByID(point2ID);
		if (point1 == null || point2 == null) {
			logger.error("Error while parsing pp_line: ID:" + id);
			return null;
		} else {
			if (!point1.isPoint() || !point2.isPoint()) {
				logger.error("Error while parsing pp_line: ID:" + id);
				return null;
			} else {
				return new GeoProofSchemePPLine(id, point1, point2);
			}
		}
	}

	public GeoProofSchemeParLine parseParLine(String id, String rawData) {
		String pointID = rawData.substring(9, rawData.length() - 1).split(",")[0].trim();
		String lineID = rawData.substring(9, rawData.length() - 1).split(",")[1].trim();
		GeoProofSchemeElement point = getElementByID(pointID);
		GeoProofSchemeElement line = getElementByID(lineID);
		if (point == null || line == null) {
			logger.error("Error while parsing par_line: ID:" + id);
			return null;
		} else {
			if (!point.isPoint() || !line.isLine()) {
				logger.error("Error while parsing par_line: ID:" + id);
				return null;
			} else {
				return new GeoProofSchemeParLine(id, point, line);
			}
		}
	}

	public GeoProofSchemeOrthoLine parseOrthoLine(String id, String rawData) {
		String pointID = rawData.substring(11, rawData.length() - 1).split(",")[0].trim();
		String lineID = rawData.substring(11, rawData.length() - 1).split(",")[1].trim();
		GeoProofSchemeElement point = getElementByID(pointID);
		GeoProofSchemeElement line = getElementByID(lineID);
		if (point == null || line == null) {
			logger.error("Error while parsing ortho_line: ID:" + id);
			return null;
		} else {
			if (!point.isPoint() || !line.isLine()) {
				logger.error("Error while parsing ortho_line: ID:" + id);
				return null;
			} else {
				return new GeoProofSchemeOrthoLine(id, point, line);
			}
		}
	}

	public GeoProofSchemeAltitude parseAltitude(String id, String rawData) {
		String point1ID = rawData.substring(9, rawData.length() - 1).split(",")[0].trim();
		String point2ID = rawData.substring(9, rawData.length() - 1).split(",")[1].trim();
		String point3ID = rawData.substring(9, rawData.length() - 1).split(",")[2].trim();
		GeoProofSchemeElement point1 = getElementByID(point1ID);
		GeoProofSchemeElement point2 = getElementByID(point2ID);
		GeoProofSchemeElement point3 = getElementByID(point3ID);

		if (point1 == null || point2 == null || point3 == null) {
			logger.error("Error while parsing altitude: ID:" + id);
			return null;
		} else {
			if (!point1.isPoint() || !point2.isPoint() || !point3.isPoint()) {
				logger.error("Error while altitude: ID:" + id);
				return null;
			} else {
				GeoProofSchemePPLine tempGeoProofSchemePPLine = null;
				for (GeoProofSchemeElement geoProofSchemeElement : geoProofSchemeElements) {
					if (geoProofSchemeElement instanceof GeoProofSchemePPLine) {
						if (((GeoProofSchemePPLine) geoProofSchemeElement).getPoint1().getID().equals(point2.getID())
								&& ((GeoProofSchemePPLine) geoProofSchemeElement).getPoint2().getID()
										.equals(point3.getID())) {
							tempGeoProofSchemePPLine = (GeoProofSchemePPLine) geoProofSchemeElement;
							break;
						} else {
							tempGeoProofSchemePPLine = null;
						}
					}
				}

				if (tempGeoProofSchemePPLine == null) {
					tempGeoProofSchemePPLine = new GeoProofSchemePPLine("pp" + point2.getID() + point3.getID(),
							point2, point3);
					addElement(tempGeoProofSchemePPLine);
				}
				return new GeoProofSchemeAltitude(id, point1, point2, point3);
			}
		}
	}

	public GeoProofSchemePBisector parsePBisector(String id, String rawData) {
		String point1ID = rawData.substring(11, rawData.length() - 1).split(",")[0].trim();
		String point2ID = rawData.substring(11, rawData.length() - 1).split(",")[1].trim();
		GeoProofSchemeElement point1 = getElementByID(point1ID);
		GeoProofSchemeElement point2 = getElementByID(point2ID);

		if (point1 == null || point2 == null) {
			logger.error("Error while parsing altitude: ID:" + id);
			return null;
		} else {
			if (!point1.isPoint() || !point2.isPoint()) {
				logger.error("Error while altitude: ID:" + id);
				return null;
			} else {
				GeoProofSchemePPLine tempGeoProofSchemePPLine = null;
				for (GeoProofSchemeElement geoProofSchemeElement : geoProofSchemeElements) {
					if (geoProofSchemeElement instanceof GeoProofSchemePPLine) {
						if (((GeoProofSchemePPLine) geoProofSchemeElement).getPoint1().getID().equals(point1.getID())
								&& ((GeoProofSchemePPLine) geoProofSchemeElement).getPoint2().getID()
										.equals(point2.getID())) {
							tempGeoProofSchemePPLine = (GeoProofSchemePPLine) geoProofSchemeElement;
							break;
						} else {
							tempGeoProofSchemePPLine = null;
						}
					}
				}

				if (tempGeoProofSchemePPLine == null) {
					tempGeoProofSchemePPLine = new GeoProofSchemePPLine("pp" + point1.getID() + point2.getID(), point1,
							point2);
					addElement(tempGeoProofSchemePPLine);
				}

				GeoProofSchemeMidPoint tempGeoProofSchemeMidPoint = null;
				for (GeoProofSchemeElement geoProofSchemeElement : geoProofSchemeElements) {
					if (geoProofSchemeElement instanceof GeoProofSchemeMidPoint) {
						if (((GeoProofSchemeMidPoint) geoProofSchemeElement).getPoint1().getID().equals(point1.getID())
								&& ((GeoProofSchemeMidPoint) geoProofSchemeElement).getPoint2().getID()
										.equals(point2.getID())) {
							tempGeoProofSchemeMidPoint = (GeoProofSchemeMidPoint) geoProofSchemeElement;
							break;
						} else {
							tempGeoProofSchemeMidPoint = null;
						}
					}
				}

				if (tempGeoProofSchemeMidPoint == null) {
					tempGeoProofSchemeMidPoint = new GeoProofSchemeMidPoint("mid" + point1.getID() + point2.getID(),
							point1, point2);
					addElement(tempGeoProofSchemeMidPoint);
				}
				return new GeoProofSchemePBisector(id, point1, point2);
			}
		}
	}

	public GeoProofSchemeMedian parseMedian(String id, String rawData) {
		String point1ID = rawData.substring(7, rawData.length() - 1).split(",")[0].trim();
		String point2ID = rawData.substring(7, rawData.length() - 1).split(",")[1].trim();
		String point3ID = rawData.substring(7, rawData.length() - 1).split(",")[2].trim();
		GeoProofSchemeElement point1 = getElementByID(point1ID);
		GeoProofSchemeElement point2 = getElementByID(point2ID);
		GeoProofSchemeElement point3 = getElementByID(point3ID);

		if (point1 == null || point2 == null || point3 == null) {
			logger.error("Error while parsing altitude: ID:" + id);
			return null;
		} else {
			if (!point1.isPoint() || !point2.isPoint() || !point3.isPoint()) {
				logger.error("Error while altitude: ID:" + id);
				return null;
			} else {
				GeoProofSchemePPLine tempGeoProofSchemePPLine = null;
				for (GeoProofSchemeElement geoProofSchemeElement : geoProofSchemeElements) {
					if (geoProofSchemeElement instanceof GeoProofSchemePPLine) {
						if (((GeoProofSchemePPLine) geoProofSchemeElement).getPoint1().getID().equals(point2.getID())
								&& ((GeoProofSchemePPLine) geoProofSchemeElement).getPoint2().getID()
										.equals(point3.getID())) {
							tempGeoProofSchemePPLine = (GeoProofSchemePPLine) geoProofSchemeElement;
							break;
						} else {
							tempGeoProofSchemePPLine = null;
						}
					}
				}

				if (tempGeoProofSchemePPLine == null) {
					tempGeoProofSchemePPLine = new GeoProofSchemePPLine("pp" + point2.getID() + point3.getID(), point2,
							point3);
					addElement(tempGeoProofSchemePPLine);
				}

				GeoProofSchemeMidPoint tempGeoProofSchemeMidPoint = null;
				for (GeoProofSchemeElement geoProofSchemeElement : geoProofSchemeElements) {
					if (geoProofSchemeElement instanceof GeoProofSchemeMidPoint) {
						if (((GeoProofSchemeMidPoint) geoProofSchemeElement).getPoint1().getID().equals(point2.getID())
								&& ((GeoProofSchemeMidPoint) geoProofSchemeElement).getPoint2().getID()
										.equals(point3.getID())) {
							tempGeoProofSchemeMidPoint = (GeoProofSchemeMidPoint) geoProofSchemeElement;
							break;
						} else {
							tempGeoProofSchemeMidPoint = null;
						}
					}
				}

				if (tempGeoProofSchemeMidPoint == null) {
					tempGeoProofSchemeMidPoint = new GeoProofSchemeMidPoint("mid" + point2.getID() + point3.getID(),
							point2, point3);
					addElement(tempGeoProofSchemeMidPoint);
				}
				return new GeoProofSchemeMedian(id, point1, point2, point3);
			}
		}
	}

	public GeoProofSchemeP3Bisector parseP3Bisector(String id, String rawData) {
		String point1ID = rawData.substring(12, rawData.length() - 1).split(",")[0].trim();
		String point2ID = rawData.substring(12, rawData.length() - 1).split(",")[1].trim();
		String point3ID = rawData.substring(12, rawData.length() - 1).split(",")[2].trim();
		GeoProofSchemeElement point1 = getElementByID(point1ID);
		GeoProofSchemeElement point2 = getElementByID(point2ID);
		GeoProofSchemeElement point3 = getElementByID(point3ID);
		if (point1 == null || point2 == null || point3 == null) {
			logger.error("Error while parsing p3_bisector: ID:" + id);
			return null;
		} else {
			if (!point1.isPoint() || !point2.isPoint() || !point3.isPoint()) {
				logger.error("Error while parsing p3_bisector: ID:" + id);
				return null;
			} else {
				GeoProofSchemePPLine tempGeoProofSchemePPLine = null;
				for (GeoProofSchemeElement geoProofSchemeElement : geoProofSchemeElements) {
					if (geoProofSchemeElement instanceof GeoProofSchemePPLine) {
						if (((GeoProofSchemePPLine) geoProofSchemeElement).getPoint1().getID().equals(point2.getID())
								&& ((GeoProofSchemePPLine) geoProofSchemeElement).getPoint2().getID()
										.equals(point3.getID())) {
							tempGeoProofSchemePPLine = (GeoProofSchemePPLine) geoProofSchemeElement;
							break;
						} else {
							tempGeoProofSchemePPLine = null;
						}
					}
				}

				if (tempGeoProofSchemePPLine == null) {
					tempGeoProofSchemePPLine = new GeoProofSchemePPLine("pp" + point2.getID() + point3.getID(), point2,
							point3);
					addElement(tempGeoProofSchemePPLine);
				}
				return new GeoProofSchemeP3Bisector(id, point1, point2, point3);
			}
		}
	}

	public GeoProofSchemeP3Circle parseP3Circle(String id, String rawData) {
		String point1ID = rawData.substring(10, rawData.length() - 1).split(",")[0].trim();
		String point2ID = rawData.substring(10, rawData.length() - 1).split(",")[1].trim();
		String point3ID = rawData.substring(10, rawData.length() - 1).split(",")[2].trim();
		GeoProofSchemeElement point1 = getElementByID(point1ID);
		GeoProofSchemeElement point2 = getElementByID(point2ID);
		GeoProofSchemeElement point3 = getElementByID(point3ID);
		if (point1 == null || point2 == null || point3 == null) {
			logger.error("Error while parsing p3_circle: ID:" + id);
			return null;
		} else {
			if (!point1.isPoint() || !point2.isPoint() || !point3.isPoint()) {
				logger.error("Error while parsing p3_circle: ID:" + id);
				return null;
			} else {
				return new GeoProofSchemeP3Circle(id, point1, point2, point3);
			}
		}
	}

	public GeoProofSchemePCCircle parsePCCircle(String id, String rawData) {
		String point1ID = rawData.substring(10, rawData.length() - 1).split(",")[0].trim();
		String point2ID = rawData.substring(10, rawData.length() - 1).split(",")[1].trim();
		GeoProofSchemeElement point1 = getElementByID(point1ID);
		GeoProofSchemeElement point2 = getElementByID(point2ID);
		if (point1 == null || point2 == null) {
			logger.error("Error while parsing pc_circle: ID:" + id);
			return null;
		} else {
			if (!point1.isPoint() || !point2.isPoint()) {
				logger.error("Error while parsing pc_circle: ID:" + id);
				return null;
			} else {
				return new GeoProofSchemePCCircle(id, point1, point2);
			}
		}
	}

	public boolean isParameterMatching(List<String> parameterIDs, String parameterFilePath) {
		List<String> parametersFromFile = new ArrayList<String>();
		try (BufferedReader bufferedReader = new BufferedReader(new FileReader(parameterFilePath))) {
			String tempString;
			while ((tempString = bufferedReader.readLine()) != null) {
				parametersFromFile.add(tempString.split("\t")[0]);
			}
		} catch (Exception e) {
			logger.error("Missing parameter file:" + parameterFilePath);
			return false;
		}
		return new HashSet<>(parameterIDs).equals(new HashSet<>(parametersFromFile));
	}

	public void addElement(GeoProofSchemeElement geoProofSchemeElement) {
		this.geoProofSchemeElements.add(geoProofSchemeElement);
	}

	public GeoProofSchemeElement getElementByID(String id) {
		for (GeoProofSchemeElement geoProofSchemeElement : geoProofSchemeElements) {
			if (geoProofSchemeElement.getID().equals(id)) {
				return geoProofSchemeElement;
			}
		}
		return null;
	}
}
