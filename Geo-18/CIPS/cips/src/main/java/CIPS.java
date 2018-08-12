import gr2.cips.cinderella.Cinderella;
import gr2.cips.core.Cinderella2Intergeo;
import gr2.cips.core.CinderellaVisualization;
import gr2.cips.core.GeoProofScheme2Intergeo;
import gr2.cips.core.GeoProofSchemeVisualization;
import gr2.cips.core.IntergeoVisualization;
import gr2.cips.geoproofscheme.GeoProofScheme;
import gr2.cips.intergeo.Intergeo;
import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;

import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.util.Arrays;

/**
 * @author Duong Trung Duong
 * @author <a href=
 *         "mailto:bss13ard@studserv.uni-leipzig.de">bss13ard@studserv.uni-leipzig.de</a>
 */
public class CIPS {
	public static void main(String argv[]) throws Exception {
		Options options = new Options();

		options.addOption(new Option("c2i", false, "cinderella to intergeo"));
		options.addOption(new Option("g2i", false, "geoproofscheme to intergeo"));
		options.addOption(new Option("vc", false, "cinderella visualisation with jsxgraph"));
		options.addOption(new Option("vi", false, "intergeo visualisation with jsxgraph"));
		options.addOption(new Option("vg", false, "geoproofscheme visualisation with jsxgraph"));

		Option oInput = new Option("i", "input", true, "input file path");
		oInput.setRequired(false);
		options.addOption(oInput);

		Option oParameter = new Option("p", "parameter", true, "default parameter file path");
		oParameter.setRequired(false);
		options.addOption(oParameter);

		Option oOutput = new Option("o", "output", true, "output file path");
		oOutput.setRequired(false);
		options.addOption(oOutput);

		Option oHelp = new Option("h", "help", false, "print this message");
		oHelp.setRequired(false);
		options.addOption(oHelp);

		CommandLineParser parser = new DefaultParser();
		HelpFormatter formatter = new HelpFormatter();
		CommandLine cmd;
		String helpString =
				"\njava -jar cips.jar <mode (optional)> <input file> <output file (optional)> -p [default parameter file]\n"
				+ "java -jar cips.jar -c2i <cinderella file path> <intergeo file path>\n"
				+ "java -jar cips.jar -g2i <geoproofscheme file> <intergeo file> -p [default parameter file]\n"
				+ "java -jar cips.jar -vc  <cinderella file> <visualization file>\n"
				+ "java -jar cips.jar -vi  <intergeo file> <visualization file>\n"
				+ "java -jar cips.jar -vg  <geoproofscheme file> <visualization file> -p [default parameter file]\n"
				+ "example:\n"
				+ "java -jar cips.jar -vg Gruppe-2/testdata/Chou.28_1.xml Gruppe-2/jsx_Chou.html\n\n";


		try {
			cmd = parser.parse(options, argv);
		} catch (ParseException e) {
			System.out.println(e.getMessage());
			formatter.printHelp(helpString, options);
			System.exit(1);
			return;
		}

		if (cmd.hasOption("help")) {
			formatter.printHelp(helpString, options);
			return;
		}

		boolean hasRun = false;
		try {
			if( cmd.hasOption("c2i")) {
				hasRun = c2iMode(cmd);
			}
			if (cmd.hasOption("g2i")) {
				hasRun |= g2iMode(cmd);
			}
			if (cmd.hasOption("vc")) {
				hasRun |= vcMode(cmd);
			}
			if (cmd.hasOption("vi")) {
				hasRun |= viMode(cmd);
			}
			if (cmd.hasOption("vg")) {
				hasRun |= vgMode(cmd);
			}

			if (!hasRun) {
				final String inputFileExtension = getInputFileExtension(cmd);
				switch (inputFileExtension) {
					case "cdy":
						hasRun = vcMode(cmd);
						hasRun |= c2iMode(cmd);
						break;
					case "xml":
						hasRun = vgMode(cmd);
						hasRun |= g2iMode(cmd);
						break;
					case "i2g":
						hasRun = viMode(cmd);
						break;
					default:
						break;
				}
			}
		} catch (IllegalArgumentException e) {

		}

		if (!hasRun) {
			formatter.printHelp(helpString, options);
		}
	}

	static boolean c2iMode(CommandLine cmd) throws Exception {
		Cinderella cinderella = new Cinderella();
		String cinderellaFilePath = getInput(cmd);
		String intergeoFilePath = getOutput(cmd, "i2g");

		if (!cinderella.loadFromFile(cinderellaFilePath))
			return false;

		Cinderella2Intergeo cinderella2Intergeo = new Cinderella2Intergeo(cinderella);
		Intergeo intergeo = cinderella2Intergeo.convert();
		intergeo.exportXML(intergeoFilePath);

		return true;
	}
	static boolean g2iMode(CommandLine cmd) throws Exception {
		GeoProofScheme geoProofScheme = new GeoProofScheme();
		String geoProofSchemeFilePath = getInput(cmd);
		String intergeoFilePath = getOutput(cmd, "i2g");
		String parametersFilePath = getParameterFile(cmd);

		if (parametersFilePath.isEmpty() || !geoProofScheme.loadFromFile(geoProofSchemeFilePath, parametersFilePath))
			return false;

		GeoProofScheme2Intergeo geoProofScheme2Intergeo = new GeoProofScheme2Intergeo(geoProofScheme);
		Intergeo intergeo = geoProofScheme2Intergeo.convert();
		intergeo.exportXML(intergeoFilePath);

		return true;
	}
	static boolean vcMode(CommandLine cmd) throws Exception {
		Cinderella cinderella = new Cinderella();
		String cinderellaFilePath = getInput(cmd);
		String visualizationFilePath = getOutput(cmd, "html");

		if (!cinderella.loadFromFile(cinderellaFilePath))
			return false;

		CinderellaVisualization cinderellaVisualization = new CinderellaVisualization(cinderella,
				visualizationFilePath);
		cinderellaVisualization.visualize();

		openBrowser(visualizationFilePath);

		return true;
	}
	static boolean viMode(CommandLine cmd) throws Exception {
		Intergeo intergeo = new Intergeo();
		String intergeoFilePath = getInput(cmd);
		String visualizationFilePath = getOutput(cmd, "html");

		if (!intergeo.loadFromFile(intergeoFilePath))
			return false;

		IntergeoVisualization intergeoVisualization = new IntergeoVisualization(intergeo, visualizationFilePath);
		intergeoVisualization.visualize();

		openBrowser(visualizationFilePath);

		return true;
	}
	static boolean vgMode(CommandLine cmd) throws Exception {
		GeoProofScheme geoProofScheme = new GeoProofScheme();
		String geoProofSchemeFilePath = getInput(cmd);
		String visualizationFilePath = getOutput(cmd, "html");
		String parametersFilePath = getParameterFile(cmd);

		if (parametersFilePath.isEmpty() || !geoProofScheme.loadFromFile(geoProofSchemeFilePath, parametersFilePath))
			return false;

		GeoProofSchemeVisualization geoProofSchemeVisualization = new GeoProofSchemeVisualization(geoProofScheme,
				visualizationFilePath);
		geoProofSchemeVisualization.visualize();

		openBrowser(visualizationFilePath);

		return true;
	}

	private static void openBrowser(final String visualizationFilePath) {
		File htmlFile = new File(visualizationFilePath);
		try {
			Desktop.getDesktop().browse(htmlFile.toURI());
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static String getInputFileExtension(CommandLine cmd) {
		final String input = getInput(cmd);
		final String[] inputFile = input.split("\\.");
		final String inputFileExtension = inputFile[inputFile.length - 1];

		return inputFileExtension;
	}
	private static String getInput(CommandLine cmd) {
		String input = cmd.getOptionValue("input");

		if (input == null || input.isEmpty()) {
			if (cmd.getArgs().length > 0) {
				return cmd.getArgs()[0];
			} else {
				throw new IllegalArgumentException();
			}
		}

		return input;
	}

	private static String getOutput(CommandLine cmd, String extension) {
		String output;
		if (cmd.getArgs().length > 1) {
			output = cmd.getArgs()[1];
		} else {
			output = cmd.getOptionValue("output");
		}
		if (output == null || output.isEmpty()) {
			output = generateOutputFilePath(cmd, extension);
		}
		return output;
	}

	private static String generateOutputFilePath(CommandLine cmd, String extension) {
		String input = getInput(cmd);
		final String[] inputPaths = input.split("/");
		final String[] inputFile = inputPaths[inputPaths.length - 1].split("\\.");
		final String newName = String.join(".", Arrays.copyOf(inputFile, inputFile.length-1));
		final String newPath = String.join("/", Arrays.copyOf(inputPaths, inputPaths.length-1));

		return newPath + "/" + newName + "." + extension;
	}

	private static String getParameterFile(CommandLine cmd) {
		final String parameter = cmd.getOptionValue("parameter");
		if (parameter == null || parameter.isEmpty()) {
			return generateOutputFilePath(cmd, "parameter");
		}
		return parameter;
	}
}
