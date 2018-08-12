# Geo-18

This is code from a project conducted by a group of students at Leipzig
university in the summer term 2018.  The goal was to translate [SymbolicData
GeoProofSchemes](https://symbolicdata.github.io/Geo) to different Dynamic
Geometry Software, and to use [JSXGraph](http://jsxgraph.org/) to display the
results.

The project was part of a course "Geometry with Computer".  A [script of the
course](https://www.informatik.uni-leipzig.de/~graebe/skripte/geometrie18.pdf)
(in German) is available.

The students tested different approaches:

* Translate GeoProofSchemes to [GeoGebra code](http://geogebra.org/) and upload
  it with the JSXGraph GeoGebra loader.
  * Folder ggb2jsxGraph, file xml_transformer.js
  * Solution based on Javascript
  * Work done by Tobias Mann and Lisa Kießling
  
* Translate GeoProofSchemes to [Intergeo code](http://i2geo.net) and directly
  to JSXGraph code and upload it with the JSXGraph Intergeo loader.
  * Folder CIPS, solution based on Java and Maven
  * Provides different translation modes between
    [Cinderella](https://www.cinderella.de), GeoProofSchemes and Intergeo code
    and visualisation of all three kinds of code with JSXgraph
  * Work done by Kevin Marco Shrestha, Duong Trung Duong, Akber Sarchaddi and
    Johannes Michael

* Test display of Intergeo code with JSX graph
  * This group focused mainly better to understand the Intergeo format.
  * The Intergeo format was invented around 2011, is nowadays badly documented
    (`intergeo.xsd` as the main source of formal description could even not be
    located) and leaves the impression that it never was consolidated to a
    commonly agreed standard ready for use. See Intergeo/README.md
  * The folder Intergeo contains mainly material already compiled in the
    JSXGraph github repo (the JSXGraph group was one of the members of the
    Ingergeo consortium). 
  * Work done by Mirco Altenbernd, Max Braungardt and Hannes Thalheim
 