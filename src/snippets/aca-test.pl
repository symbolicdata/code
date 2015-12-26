##################################
#
# author: graebe
# createdAt: 2006-03-03
# lastUpdate: 2013-08-25

# purpose: Demonstration how a benchmark could be set up. Works for examples
# given directly by an INTPS XMLResource.

# remark: obsolete in SymbolicData v.3, since degree list and lengths list
# depend on the base ring of the polynomials. These result are valid only for
# the flat ideals associated with the polynomial systems.

use strict;
use XML::DOM; # A convenient perl DOM Parser package 

# The environment variable SD should point to the root directory of the git
# cloned repo.

die unless defined $ENV{'SD'};

#### start main: create benchmark output for a special system.

my $parser=new XML::DOM::Parser;
my $xmldir="$ENV{'SD'}/data/XMLResources/IntPS";
my $zeroDimensionalExamples=
    ["Sym1_211", "Katsura_4", "Sym1_311", "Cyclic_5", "Sym1_321", 
     "Katsura_5"]; 

print createOutputforMuPAD($zeroDimensionalExamples);

# === end main ===

sub createOutputforMuPAD {
    my $listOfExamples=shift;
    my $theExamples=join(",\n",map(getExample($_), @$listOfExamples));
    my $out=<<EOT;
// Startup
read("aca-test.mu"):

// make a list of all examples to be processed
theExamples:=[$theExamples]:

// Run the examples using a specially defined run function
// within the CAS that encapsulates all data and produces all
// output information.

map(theExamples, myBenchmarkFunction);

quit;
EOT
}

sub createOutputforMaple {
    my $listOfExamples=shift;
    my $theExamples=join(",\n",map(getExample($_), @$listOfExamples));
    my $out=<<EOT;
read("aca-test.mpl");
theExamples:=[$theExamples];
map(myBenchmarkFunction, theExamples);
quit;
EOT
}

sub getExample {
    my $name=shift;
    my $doc=$parser->parsefile("$xmldir/$name.xml") or die;
    my $vars=join(",",getTagValue($doc,"vars"));
    my $polys=join(",\n",getPolys($doc));
    return <<EOT;
[theExample = "$name",
 theVars=[$vars],
 thePolys=[
$polys
       ]]
EOT
}

sub getPolys {
    my ($doc)=@_;
    my @l;
    map { push(@l, getValue($_));} $doc->getElementsByTagName("poly");  
    return @l;
}

sub getTagValue {
    my ($doc,$tag)=@_;
    map { return getValue($_);} $doc->getElementsByTagName($tag);  
}

sub getValue {
    my $node=shift;
    local $_=$node->toString(1);
    s/^\s*<[^>]*?>\s*//s;
    s/\s*<\/[^>]*?>\s*$//s;
    return $_;
}
