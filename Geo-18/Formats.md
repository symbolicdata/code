# More about the formats used by the different DGS

## Cinderella

## GeoGebra format 

GeoGebra uses a zipped archive, consisting of some help files and an XML file.
The XML file contains the data from which the stored constructions can be
reconstructed.  The other files play a minor role.

A construction is embedded in a <construction> tag, that contains a list of
construction steps (in the meaning developed in the accompanying course)
encoded in the following way:

* Initial (free) points are described by a single <element> tag. 
* Each further element is described by two different XML entries:
  * A <command> tag describes the construction step itself
  * A <element> tag describes the display characteristica, including the
    initial coordinates of the element.

The XML format is described on the following page:
https://wiki.geogebra.org/en/Reference:XML

## Intergeo format

