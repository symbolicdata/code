package gr2.cips.cinderella;

import gr2.cips.cinderella.model.CinderellaAngularBisector;
import gr2.cips.cinderella.model.CinderellaCircleBy3;
import gr2.cips.cinderella.model.CinderellaCircleMP;
import gr2.cips.cinderella.model.CinderellaElement;
import gr2.cips.cinderella.model.CinderellaFreePoint;
import gr2.cips.cinderella.model.CinderellaJoin;
import gr2.cips.cinderella.model.CinderellaMeet;
import gr2.cips.cinderella.model.CinderellaMid;
import gr2.cips.cinderella.model.CinderellaOrthogonal;
import gr2.cips.cinderella.model.CinderellaParallel;
import gr2.cips.cinderella.model.CinderellaSegment;
import gr2.cips.cinderella.model.CinderellaThrough;
import net.lingala.zip4j.core.ZipFile;
import net.lingala.zip4j.exception.ZipException;
import org.apache.log4j.Logger;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class Cinderella {
	final static Logger logger = Logger.getLogger(Cinderella.class);
	public static final String TEMP_FOLDER = System.getProperty("java.io.tmpdir") + File.separator + "Cinderella.temp";
	public static final String EL_NAME_REGEX = "\\(\"[A-Za-z0-9]*\"\\)";
	private List<CinderellaElement> cinderellaElements;
	private String title;

	public Cinderella() {
		cinderellaElements = new ArrayList<CinderellaElement>();
	}

	public void setCinderellaElements(ArrayList<CinderellaElement> cinderellaElements) {
		this.cinderellaElements = cinderellaElements;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public List<CinderellaElement> getCinderellaElements() {
		return this.cinderellaElements;
	}

	public String getTitle() {
		return this.title;
	}

	public boolean loadFromFile(String cinderellaFilePath) throws IOException, ZipException {
		String dataLine;
		Path path = Paths.get(cinderellaFilePath);
		setTitle(path.getFileName().toString());

		if (!unzip(cinderellaFilePath))
			return false;

		try (BufferedReader bufferedReader = new BufferedReader(new FileReader(TEMP_FOLDER + File.separator + "private"
				+ File.separator + "de.cinderella" + File.separator + "construction.cdy"))) {
			while ((dataLine = bufferedReader.readLine()) != null) {
				if (dataLine.matches(".*:=FreePoint.*")) {
					CinderellaFreePoint cinderellaFreePoint = parseFreePoint(dataLine);
					if (cinderellaFreePoint != null) {
						addElement(cinderellaFreePoint);
						logger.info("Found FreePoint: ID:" + cinderellaFreePoint.getID() + ", "
								+ cinderellaFreePoint.toString());
					} else {
						logger.error("Error while parsing FreePoint: ID:" + parseElementName(dataLine));
						return false;
					}
				} else if (dataLine.matches(".*:=Meet.*")) {
					CinderellaMeet cinderellaMeet = parseMeet(dataLine);
					if (cinderellaMeet != null) {
						addElement(cinderellaMeet);
						logger.info("Found Meet: ID:" + cinderellaMeet.getID() + ", " + cinderellaMeet.toString());
					} else {
						logger.error("Error while parsing Meet: ID:" + parseElementName(dataLine));
						return false;
					}
				} else if (dataLine.matches(".*:=Mid.*")) {
					CinderellaMid cinderellaMid = parseMid(dataLine);
					if (cinderellaMid != null) {
						addElement(cinderellaMid);
						logger.info("Found Mid: ID:" + cinderellaMid.getID() + ", " + cinderellaMid.toString());
					} else {
						logger.error("Error while parsing Mid: ID:" + parseElementName(dataLine));
						return false;
					}
				} else if (dataLine.matches(".*:=Join.*")) {
					CinderellaJoin cinderellaJoin = parseJoin(dataLine);
					if (cinderellaJoin != null) {
						addElement(cinderellaJoin);
						logger.info("Found Join: ID:" + cinderellaJoin.getID() + ", " + cinderellaJoin.toString());
					} else {
						logger.error("Error while parsing Join: ID:" + parseElementName(dataLine));
						return false;
					}
				} else if (dataLine.matches(".*:=Segment.*")) {
					CinderellaSegment cinderellaSegment = parseSegment(dataLine);
					if (cinderellaSegment != null) {
						addElement(cinderellaSegment);
						logger.info(
								"Found Segment: ID:" + cinderellaSegment.getID() + ", " + cinderellaSegment.toString());
					} else {
						logger.error("Error while parsing Segment: ID:" + parseElementName(dataLine));
						return false;
					}
				} else if (dataLine.matches(".*:=Through.*")) {
					CinderellaThrough cinderellaThrough = parseThrough(dataLine);
					if (cinderellaThrough != null) {
						addElement(cinderellaThrough);
						logger.info(
								"Found Through: ID:" + cinderellaThrough.getID() + ", " + cinderellaThrough.toString());
					} else {
						logger.error("Error while parsing Through: ID:" + parseElementName(dataLine));
						return false;
					}
				} else if (dataLine.matches(".*:=Parallel.*")) {
					CinderellaParallel cinderellaParallel = parseParallel(dataLine);
					if (cinderellaParallel != null) {
						addElement(cinderellaParallel);
						logger.info("Found Parallel: ID:" + cinderellaParallel.getID() + ", "
								+ cinderellaParallel.toString());
					} else {
						logger.error("Error while parsing Parallel: ID:" + parseElementName(dataLine));
						return false;
					}
				} else if (dataLine.matches(".*:=Orthogonal.*")) {
					CinderellaOrthogonal cinderellaOrthogonal = parseOrthogonal(dataLine);
					if (cinderellaOrthogonal != null) {
						addElement(cinderellaOrthogonal);
						logger.info("Found Orthogonal: ID:" + cinderellaOrthogonal.getID() + ", "
								+ cinderellaOrthogonal.toString());
					} else {
						logger.error("Error while parsing Orthogonal: ID:" + parseElementName(dataLine));
						return false;
					}
				} else if (dataLine.matches(".*:=AngularBisector.*")) {
					CinderellaAngularBisector cinderellaAngularBisector = parseAngularBisector(dataLine);
					if (cinderellaAngularBisector != null) {
						addElement(cinderellaAngularBisector);
						logger.info("Found AngularBisector: ID:" + cinderellaAngularBisector.getID() + ", "
								+ cinderellaAngularBisector.toString());
					} else {
						logger.error("Error while parsing AngularBisector: ID:" + parseElementName(dataLine));
						return false;
					}
				} else if (dataLine.matches(".*:=CircleMP.*")) {
					CinderellaCircleMP cinderellaCircleMP = parseCircleMP(dataLine);
					if (cinderellaCircleMP != null) {
						addElement(cinderellaCircleMP);
						logger.info("Found CircleMP: ID:" + cinderellaCircleMP.getID() + ", "
								+ cinderellaCircleMP.toString());
					} else {
						logger.error("Error while parsing CircleMP: ID:" + parseElementName(dataLine));
						return false;
					}
				} else if (dataLine.matches(".*:=CircleBy3.*")) {
					CinderellaCircleBy3 cinderellaCircleBy3 = parseCircleBy3(dataLine);
					if (cinderellaCircleBy3 != null) {
						addElement(cinderellaCircleBy3);
						logger.info("Found CircleBy3: ID:" + cinderellaCircleBy3.getID() + ", "
								+ cinderellaCircleBy3.toString());
					} else {
						logger.error("Error while parsing CircleBy3: ID:" + parseElementName(dataLine));
						return false;
					}
				}
			}
			bufferedReader.close();
		} catch (Exception e) {
			e.printStackTrace();
			return false;
		}
		return true;
	}

	public CinderellaFreePoint parseFreePoint(String dataLine) {
		String elementName = parseElementName(dataLine);
		dataLine = dataLine.substring(elementName.length() + 17, dataLine.length() - 2);

		String[] pCoords = dataLine.split(",");
		double x = Double.parseDouble(pCoords[0].substring(0, pCoords[0].indexOf("+i")))
				/ Double.parseDouble(pCoords[2].substring(0, pCoords[2].indexOf("+i")));
		double y = Double.parseDouble(pCoords[1].substring(0, pCoords[1].indexOf("+i")))
				/ -Double.parseDouble(pCoords[2].substring(0, pCoords[2].indexOf("+i")));
		return new CinderellaFreePoint(elementName, x, y);
	}

	public CinderellaMid parseMid(String dataLine) {
		String elementName = parseElementName(dataLine);
		dataLine = dataLine.substring(elementName.length() + 10, dataLine.length() - 2);

		String[] points = dataLine.split(",");
		CinderellaElement p1 = getElementByID(points[0].substring(1, points[0].length() - 1));
		CinderellaElement p2 = getElementByID(points[1].substring(1, points[1].length() - 1));
		return new CinderellaMid(elementName, p1, p2);
	}

	public CinderellaMeet parseMeet(String dataLine) {
		String elementName = parseElementName(dataLine);
		dataLine = dataLine.substring(elementName.length() + 11, dataLine.length() - 2);

		String[] elements = dataLine.split(",");
		CinderellaElement line1 = getElementByID(elements[0].substring(1, elements[0].length() - 1));
		CinderellaElement line2 = getElementByID(elements[1].substring(1, elements[1].length() - 1));

		return new CinderellaMeet(elementName, line1, line2);
	}

	public CinderellaJoin parseJoin(String dataLine) {
		String elementName = parseElementName(dataLine);
		dataLine = dataLine.substring(elementName.length() + 11, dataLine.length() - 2);

		String[] points = dataLine.split(",");
		CinderellaElement p1 = getElementByID(points[0].substring(1, points[0].length() - 1));
		CinderellaElement p2 = getElementByID(points[1].substring(1, points[1].length() - 1));
		return new CinderellaJoin(elementName, p1, p2);
	}

	public CinderellaSegment parseSegment(String dataLine) {
		String elementName = parseElementName(dataLine);
		dataLine = dataLine.substring(elementName.length() + 14, dataLine.length() - 2);

		String[] points = dataLine.split(",");
		CinderellaElement p1 = getElementByID(points[0].substring(1, points[0].length() - 1));
		CinderellaElement p2 = getElementByID(points[1].substring(1, points[1].length() - 1));
		return new CinderellaSegment(elementName, p1, p2);
	}

	public CinderellaThrough parseThrough(String dataLine) {
		String elementName = parseElementName(dataLine);
		dataLine = dataLine.substring(elementName.length() + 14, dataLine.length() - 2);

		String[] points = dataLine.split(",");
		CinderellaFreePoint throughPoint = (CinderellaFreePoint) getElementByID(
				points[0].substring(1, points[0].length() - 1));

		double x = Double.parseDouble(points[1].substring(1, points[1].indexOf("+i"))) + throughPoint.getX();
		double y = -Double.parseDouble(points[2].substring(0, points[2].indexOf("+i"))) + throughPoint.getY();
		CinderellaFreePoint tempPoint = new CinderellaFreePoint(
				"tempPoint" + UUID.randomUUID().toString().replaceAll("-", ""), x, y);
		return new CinderellaThrough(elementName, throughPoint, tempPoint);
	}

	public CinderellaParallel parseParallel(String dataLine) {
		String elementName = parseElementName(dataLine);
		dataLine = dataLine.substring(elementName.length() + 15, dataLine.length() - 2);

		String[] elements = dataLine.split(",");
		CinderellaElement lineOrSegment = getElementByID(elements[0].substring(1, elements[0].length() - 1));
		CinderellaElement throughPoint = getElementByID(elements[1].substring(1, elements[1].length() - 1));
		return new CinderellaParallel(elementName, throughPoint, lineOrSegment);
	}

	public CinderellaOrthogonal parseOrthogonal(String dataLine) {
		String elementName = parseElementName(dataLine);
		dataLine = dataLine.substring(elementName.length() + 17, dataLine.length() - 2);

		String[] elements = dataLine.split(",");
		CinderellaElement lineOrSegment = getElementByID(elements[0].substring(1, elements[0].length() - 1));
		CinderellaFreePoint throughPoint = (CinderellaFreePoint) getElementByID(
				elements[1].substring(1, elements[1].length() - 1));

		return new CinderellaOrthogonal(elementName, throughPoint, lineOrSegment);
	}

	public CinderellaAngularBisector parseAngularBisector(String dataLine) {
		Pattern pattern = Pattern.compile("\\{\"[A-Za-z0-9]*\",");
		Matcher matcher = pattern.matcher(dataLine);
		String elementName = "";
		if (matcher.find()) {
			elementName = dataLine.substring(matcher.start() + 2, matcher.end() - 2);
		}
		dataLine = dataLine.substring(dataLine.indexOf("AngularBisector") + 25, dataLine.length() - 3);
		CinderellaElement cinderellaElement = getElementByID(dataLine);
		if (cinderellaElement.getClass().getSimpleName().equals("CinderellaMeet")) {
			return new CinderellaAngularBisector(elementName, (CinderellaMeet) cinderellaElement);
		}
		return null;
	}

	public CinderellaCircleMP parseCircleMP(String dataLine) {
		String elementName = parseElementName(dataLine);
		dataLine = dataLine.substring(elementName.length() + 15, dataLine.length() - 2);

		String[] points = dataLine.split(",");
		CinderellaElement p1 = getElementByID(points[0].substring(1, points[0].length() - 1));
		CinderellaElement p2 = getElementByID(points[1].substring(1, points[1].length() - 1));
		return new CinderellaCircleMP(elementName, p1, p2);
	}

	public CinderellaCircleBy3 parseCircleBy3(String dataLine) {
		String elementName = parseElementName(dataLine);
		dataLine = dataLine.substring(elementName.length() + 16, dataLine.length() - 2);

		String[] points = dataLine.split(",");
		CinderellaElement p1 = getElementByID(points[0].substring(1, points[0].length() - 1));
		CinderellaElement p2 = getElementByID(points[1].substring(1, points[1].length() - 1));
		CinderellaElement p3 = getElementByID(points[2].substring(1, points[2].length() - 1));

		return new CinderellaCircleBy3(elementName, p1, p2, p3);
	}

	public String parseElementName(String dataLine) {
		Pattern pattern = Pattern.compile(EL_NAME_REGEX);
		Matcher matcher = pattern.matcher(dataLine);
		if (matcher.find()) {
			return dataLine.substring(matcher.start() + 2, matcher.end() - 2);
		}
		return null;
	}

	public void addElement(CinderellaElement cinderellaElement) {
		this.cinderellaElements.add(cinderellaElement);
	}

	public CinderellaElement getElementByID(String id) {
		for (CinderellaElement cinderellaElement : cinderellaElements) {
			if (cinderellaElement.getID().equals(id)) {
				return cinderellaElement;
			}
		}
		return null;
	}

	private boolean unzip(String filePath) throws ZipException, IOException {
		try {
			ZipFile zipFile = new ZipFile(filePath);
			zipFile.extractAll(TEMP_FOLDER);
		} catch (Exception e) {
			e.printStackTrace();
			return false;
		}
		return true;
	}

	// private void unzip2(String filePath) throws IOException {
	// byte[] buffer = new byte[1024];
	// String outputFolder = TEMP_FOLDER;
	//
	// try {
	// File folder = new File(outputFolder);
	// if (!folder.exists()) {
	// folder.mkdir();
	// }
	//
	// ZipInputStream zis = new ZipInputStream(new FileInputStream(filePath));
	// ZipEntry ze = zis.getNextEntry();
	//
	// while (ze != null) {
	// String fileName = ze.getName();
	// if (ze.isDirectory()) {
	// ze = zis.getNextEntry();
	// continue;
	// }
	// fileName = new File(fileName).getName();
	// File newFile = new File(outputFolder + File.separator + fileName);
	//
	// new File(newFile.getParent()).mkdirs();
	//
	// FileOutputStream fos = new FileOutputStream(newFile);
	//
	// int len;
	// while ((len = zis.read(buffer)) > 0) {
	// fos.write(buffer, 0, len);
	// }
	//
	// fos.close();
	// ze = zis.getNextEntry();
	// }
	//
	// zis.closeEntry();
	// zis.close();
	//
	// } catch (IOException e) {
	// e.printStackTrace();
	// }
	// }
}
