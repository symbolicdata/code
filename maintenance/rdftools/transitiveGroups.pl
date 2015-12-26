##################################
#
# author: nareike
# createdAt: 2013-03-18
# lastUpdate: 2013-09-30, graebe

# purpose: extract TransitiveGroups.ttl from
# http://galoisdb.math.uni-paderborn.de

# remark: This script can be run as-is, but it will take a very long time
# (probably over an hour) because all data has to be downloaded the first time.
# The second run will be significantly(!) faster (maybe 5 minutes) because
# offline copies will be made. The downloaded data was not included here.

# remark: fixed name spaces. TransitiveGroups for the knowledge base,
# Data/TransitiveGroup as prefix for the instances, sd: as name prefix for the
# predicates. -- HGG, 2013-09-30

use strict;
use warnings;
use Encode;
use LWP::Simple;
use HTML::Tree;
use Term::ReadKey;

my $NS = "http://symbolicdata.org/Data/TransitiveGroup/";
my $NSP = "sd";

print getPreamble();

# all: 2 .. 19

for(my $k=2; $k<=19; $k++) {
    #my $content = get('http://galoisdb.math.uni-paderborn.de/groups?deg='.$k);
    #$content = decode('UTF-8', $content);
    print STDERR "Processing degree $k, ";
    my $content = fetchHTML($k);

    my $tree = HTML::Tree -> new();
    $tree -> parse($content);

    my @rows = $tree -> look_down(_tag => 'tr');

    shift @rows;
    shift @rows;

    my $groupcount = $#rows + 1;
    my $current = 0;
    my $j = 0;

    print STDERR "($groupcount groups found)\n";

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
                $current++;
                print STDERR "... group $a ($current of $groupcount), " if ($i == 0);
                $out .= "<$NS" . "Gr" . "$a> a $NSP:TransitiveGroup ;\n";
                $out .= "    $NSP:hasURL <http://galoisdb.math.uni-paderborn.de/groups/view?deg=$k&num=$j> ;\n";
                $out .= parseGroupPage($k, $j);
            }
            elsif ($i == 1) {
                $a =~ s!</*td>!!g;
                $a =~ s!<sub>(.*)</sub>!_{$1}!g;
                $out .= "    $NSP:hasName \"$a\" ;\n";
            }
            elsif ($i == 2) {            
                $out .= "    $NSP:hasOrder \"$a\"^^xsd:integer ;\n";
            }
            elsif ($i == 3) {
                $val->as_HTML =~ /value="(.*)"/;
                $a = $1;
                $out .= "    $NSP:hasOrderFactorization \"$a\" ;\n";
            }
            elsif ($i == 4) {
                $out .= "    $NSP:OrderOfCenter \"$a\"^^xsd:integer ;\n";
            }        
            elsif ($i == 5) {            
                my @props = split(m/,\s*/, $a);
                @props = map {$NSP . ":" . taggerize($_)} @props;
                $a = join(", ", @props);
                $out .= "    $NSP:hasProperty $a ;\n";
            }
            elsif ($i == 6) {
                $out .= "    $NSP:numberOfFieldsInDatabase \"$a\" .\n";
            }
        }
        print $out , "\n";
        #print join(" | ", @data) , "\n";
        if (ReadKey(-1)) {
            print STDERR "\n\n==> Keyboard interrupt!\n\n";
            exit 0;
        }
    }
    $tree -> delete;
}

sub taggerize {
    shift;
    s/\s([a-z])/\U$1/g;
    return "$_";
}

# needs degree and optially a number as parameters
# 
# looks for a local copy first
#
# returns a string with the HTML

sub fetchHTML {
    # check directory structure
    my $dir = "sdtg/";
    my $url;
    my $file;
    my $content;

    unless(-d $dir) {
        mkdir $dir or die;
    }

    if ($#_ == 0) {        
        my $deg = shift;
        $url = 'http://galoisdb.math.uni-paderborn.de/groups?deg='.$deg;
        $file = $dir."deg$deg.xml";
    }
    elsif ($#_ == 1) {
        my $deg = shift;
        my $num = shift; 
        $dir.="deg$deg/";
        $file.= $dir."g$num.xml";
        $url = "http://galoisdb.math.uni-paderborn.de/groups/view?deg=$deg&num=$num";
        unless(-d $dir) {
            mkdir $dir or die;
        }
    }

    if (-e $file) {        
        print STDERR "reading from disk\n";
        open FILE, '<', $file;
        local $/;
        $content = <FILE>;
    }
    else {        
        print STDERR "fetching from the web, making local backup\n";
        open FILE, ">$file";
        $content = get($url);
        print FILE encode('UTF-8', $content);
        close FILE;
    }
    $content = decode('UTF-8', $content);
    return $content
}

sub parseGroupPage {            
    my $deg = shift;
    my $num = shift;
    my $content = fetchHTML($deg, $num);

    my $out = '';

    # extract generators
    my $generators = ($content =~ m!(>Generators.*<h3>)!s)[0];
    my @matches = ($generators =~ m!<li>(.*?)</li>!sg);

    if ($#matches > -1) {
        foreach my $item (@matches) {
            $item =~ s/^[\n\s]*//g;
            $item =~ s/[\n\s]*$//g;
            $out.="    $NSP:hasGenerator " . '"' . $item . '"' . " ;\n";
        }
    }

    # extract wreath product
    my $products = ($content =~ m!(Wreath.*?</p>.*?</p>)!s)[0];
    if ($products) {    
        foreach my $product (split ",", $products) {
            $product =~ m!<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>!;
            $out.="    $NSP:isWreathProductOf ( <$NS"."Gr"."$1> <$NS"."Gr"."$2> ) ; \n";
        }
    }
    
    # extract quotient of wreath product
    $products = ($content =~ m!(Quotient of wreath.*?</p>.*?</p>)!s)[0];
    if ($products) {    
        foreach my $product (split ",", $products) {
            $product =~ m!<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>!;
            $out.="    $NSP:isQuotientOfWreathProductOf ( <$NS"."Gr"."$1> <$NS"."Gr"."$2> ) ; \n";
        }
    }

    # extract direct product
    $products = ($content =~ m!(Direct product.*?</p>.*?</p>)!s)[0];
    if ($products) {    
        foreach my $product (split ",", $products) {
            $product =~ m!<a.*?>(.*?)</a>.*?<a.*?>(.*?)</a>!;
            $out.="    $NSP:isDirectProductOf ( <$NS"."Gr"."$1> <$NS"."Gr"."$2> ) ; \n";
        }
    }
    return $out;
}

sub getPreamble {
    return <<'EOF';
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sd: <http://symbolicdata.org/Data/Model#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://symbolicdata.org/Data/TransitiveGroups/>
    a owl:Ontology ;
    rdfs:comment "SD Transitive Groups" ;
    rdfs:label "SD Transitive Groups" .

sd:TransitiveGroup
    a owl:Class ;
    rdfs:label "Transitive Group" .
    
EOF
}
