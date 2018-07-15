This directory contains Intergeo files from the JSXGraph collection together
with a JSXGraph display interface for such files.  Included is a copy of
JSXGraphCore, but all that should probably also work with references to
external JSXGraph sources.

# Intergeo structure

Since neither a *real* documentation on the Intergeo-Fromat nor an
`intergeo.xsd` was found, an overview of existing *types* and construction
tools (*constraints*) is given below. This overview was extracted from the
papers "The Intergeo File Format in Progress" and "iG2 Common File Format
Specification", see the directory "Papers".

## Dead Links

* [HTML Dokumentation](http://i2geo.net/xwiki/bin/view/I2GFormat/FileFormatSymbols)
* [SVN Activemath](http://svn.activemath.org/intergeo/Format/)

## Elements (Types)

See "iG2 Common File Format Specification", ch. 4.2, pp. 17-20.

* point (*point_coordinates*)
* line (*homogeneous_coordinates*)
* line_segment (*point_coordinates, point_coordinates [, point_coordinates]*)
* directed_line_segment (*point_coordinates, point_coordinates [, point_coordinates]*)
* ray (*point_coordinates, direction | point_coordinates [, point_coordinates]*)
* polygon (*list_of_vertices_coordinates*)
* vector (*point_coordinates*)
* conic (*matrix [, dualmatrix]*)
* circle (*matrix [, dualmatrix]*)
* ellipse (*matrix [, dualmatrix]*)
* parabola (*matrix [, dualmatrix]*)
* hyperbola (*matrix [, dualmatrix]*)
* locus (*void | a sef of points*)

## Families

* line_family = {line, ray, line_segment, direction_line_segment}
* circle_family = {circle, arc}
* conic_famitly = {circle, circle arc, conic, parabola, ellipse, hyperbola}
* element_family = {all elements}

## Auxiliary symbols

* point_coordinates (*homogeneous_coordinates | euclidean_coordinates | polar_coordinates*)
  * homogeneous_coordinates (*scalar, scalar, scalar*)
  * euclidean_coordinates (*scalar, scalar*)
  * polar_coordinates (*scalar, scalar*)
* direction (*scalar, scalar [, scalar]*)
* list_of_vertices_coordinates (*point\**)
* list_of_vertices (*point_reference\**)

## Constraints (construction tools)

See "iG2 Common File Format Specification", ch. 4.2, pp. 20-26.

* free_point
* free_line
* point_on_line
* point_on_line_segment
* point_on_circle
* line_through_point
* line_through_two_points
* line_angular_bisector_of_three_points
* line_angular_bisector_of_two_points
* line_segment_by_points
* directed_line_segment_by_points
* ray_from_point_and_vector
* ray_from_point_through_point
* line_parallel_to_line_through_point
* line_perpendicular_to_line_through_point
* point_intersection_of_two_lines
* midpoint_of_two_lines
* midpoint_of_line_segment
* endpoints_of_line_segment
* carry_line_of_line_segment
* starting_point_of_directed_line_segment
* end_point_of_directed_line_segment
* line_segment_of_directed_line_segment
* vector_of_ray
* starting_point_of_ray
* carrying_line_of_ray
* circle_by_center_and_radius
* circle_by_center_and_point
* circle_by_three_points
* intersection_points_of_two_circles
* other_intersection_point_of_two_circles
* intersectrions_points_of_circle_and_line
* other_intersection_points_of_circle_and_line
* intersection_points_of_two_conics
* intersection_points_of_conic_and_line
* other_intersection_points_of_conic_and_line
* circle_tangent_lines_by_point
* foci_of_conic
* center_of_circle
* locus_defined_by_point_on_line
* locus_defined_by_point_on_line_segment
* locus_defined_by_point_on_circle
* locus_defined_by_point_on_locus
* locus_defined_by_line_through_point
* symmetry_by_point
* symmetry_by_line
* symmetry_by_circle
* translate

## Display

See "iG2 Common File Format Specification", ch. 4.2, pp. 26ff.
