##################################
#
# author: graebe
# createdAt: 2014-03-05
# lastUpdate: 2014-03-05

# purpose: Prototypical demonstration how a SPARQL query can be set up using
# the Perl connector SparqlQuery.pm.

use SparqlQuery;
use strict;

my $query = <<EOT;
PREFIX ical: <http://www.w3.org/2002/12/cal/ical#> 
PREFIX sd: <http://symbolicdata.org/Data/Model#> 
select ?a ?l ?d ?begin
from <http://symbolicdata.org/Data/Tagungsankuendigungen/>
where {
?a a sd:Event  .
?a rdfs:label ?l  .
optional { ?a ical:dtstart ?begin . }
?a ical:description ?d .
}
EOT

my $u=SparqlQuery::remoteQuery($query);
my $res=SparqlQuery::parseResult($u);
SparqlQuery::printResultSet($res);

#print TurtleEnvelope($out);

## end main ##

sub createEntry {
  my $s=shift;
  local $_=$s;
  s|_\d+$||;
  return <<EOT;
<http://symbolicdata.org/Data/GeoProofScheme/$s> 
sd:relatedGeometryProblem <http://symbolicdata.org/Data/GeometryProblem/$_> . 
EOT
}



sub TurtleEnvelope {
  my $out=shift;

  return <<EOT
\@prefix owl: <http://www.w3.org/2002/07/owl#> .
\@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
\@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
\@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
\@prefix foaf: <http://xmlns.com/foaf/0.1/> .
\@prefix sd: <http://symbolicdata.org/Data/Model#> .

$out
EOT
}
