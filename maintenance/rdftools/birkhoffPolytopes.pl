##################################
#
# author: nareike
# createdAt: 2013-03-18
# lastUpdate: 2013-09-30, graebe

# purpose: extract BirkhoffPolytopes.ttl from
# http://polymake.org/polytopes/paffenholz/www/birkhoff.*

# remark: fixed name spaces. BirkhoffPolytopes for the knowledge base,
# Data/BirkhoffPolytope/ as prefix for the instances, sd: as name prefix for
# the predicates. -- HGG, 2013-09-30

use strict;
use warnings;
use Encode;
use LWP::Simple;
use HTML::Tree;

print getPreamble();

for(my $k=2; $k<=8; $k++) {
    my $content = get("http://polymake.org/polytopes/paffenholz/www/birkhoff." . $k . "D.html");
    $content = decode('UTF-8', $content);

    my $tree = HTML::Tree -> new();
    $tree -> parse($content);

    my @rows = $tree -> look_down(_tag => 'tr');

    shift @rows;
    shift @rows;
    shift @rows;

    my $NS = "http://symbolicdata.org/Data/BirkhoffPolytope/";
    my $NSP = "sd";
    my $j = 0;

    my @combtypes = ("pyr", "prod", "join", "wed", "pyrb");

    foreach my $item (@rows) {
        my @tds = $item -> look_down(_tag => 'td');
        $j++;
        
        my $out = '';

        #print $item -> as_HTML;
        
        for(my $i=0; $i <= $#tds; $i+=1) {
            my $val = $tds[$i];
            my $a = $val->as_text;
            chomp $a;
            $a =~ s/^\s*//g;
            $a =~ s/\s*$//g;
            
            if ($i == 0) {    
                $out .= "<$NS$a> a sd:BirkhoffPolytope ;\n";
                $out .= "    $NSP:hasDimension \"$k\" ;\n";
            }
            elsif ($i == 1) {
                $a =~ s!</*td>!!g;
                $a =~ s!<sub>(.*)</sub>!_{$1}!g;
                $out .= "    $NSP:hasDescription \"$a\" ;\n";
            }
            elsif ($i == 2) {            
                $out .= "    $NSP:hasNodes \"$a\"^^xsd:integer ;\n";
            }
            elsif ($i == 3) {                
                $out .= "    $NSP:hasVertices \"$a\"^^xsd:integer ;\n";
            }
            elsif ($i == 4) {
                $out .= "    $NSP:f-vector \"$a\" ;\n";
            }
            elsif ($i > 4 && $i < 10) {
                if (!($a eq "---")) {
                    $out .= "    $NSP:hasCombinatorialType $NSP:" . $combtypes[$i-5] . " ; \n";
                }
            }
            elsif ($i == 10) {                            
                $out .= "    $NSP:simpl \"$a\" ;\n";
            }
            elsif ($i == 11) {
                $out .= "    $NSP:hiCube \"$a\" ;\n";
            }
            elsif ($i == 12) {
                $a = $val->as_HTML;
                $a =~ /href="([^"]*)".*href="([^"]*)"/;
                $out .= "    $NSP:hasPolymakeFile <$1> ;\n";
                $out .= "    $NSP:hasEPSFile <$2> .\n";
            }
        }
        print $out , "\n";
        #print join(" | ", @data) , "\n";
    }
}

sub getPreamble {
    return <<'EOF';
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sd: <http://symbolicdata.org/Data/Model#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://symbolicdata.org/Data/BirkhoffPolytopes/>
    a owl:Ontology ;
    rdfs:comment "SD Birkhoff Polytopes" ;
    rdfs:label "SD Birkhoff Polytopes" .

sd:BirkhoffPolytope
    a owl:Class ;
    rdfs:label "Birkhoff Polytope" .    

EOF
}
