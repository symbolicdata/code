##################################################
#
# Author: graebe
# createdAt: 2013-09-11
# lastUpdate: 2013-09-11

# purpose: parse a GeoProofScheme to get generic GeoProver output
# usage: perl parseGeoProofs.pl (path_to)/GeoProofSchemes/*.xml

use XML::DOM;
use strict;

my $parser=new XML::DOM::Parser;
map parseGeoProofScheme($_), @ARGV;

## end main ##

sub parseGeoProofScheme {
  my $doc=$parser->parsefile(shift) or die;
  my $doc=$doc->getDocumentElement;
  my $out;
  my $v=fix(getTagValue($doc,"vars"));
  $out.="vars = List[$v];\n" if $v;
  $v=fix(getTagValue($doc,"parameters"));
  $out.="parameters = List[$v];\n" if $v;
  map { 
    $out.=getCommands($_); 
  } $doc->getElementsByTagName("Points",0) ;
  map {   
    $out.=getCommands($_);
  } $doc->getElementsByTagName("Assignments",0) ;
  map {   
    $out.="prop = ".getProperties($_);
  } $doc->getElementsByTagName("Properties",0) ;
  map {   
    $out.="con = ".getProperties($_);  
  } $doc->getElementsByTagName("Conclusions",0) ;
  
  print $out;
}

sub getCommands {
  my $doc=shift;
  my $out;
  for my $a ("Angle", "Circle", "Distance", "Line", "Point", "Scalar") { 
    map {
      my $id=$_->getAttribute("id");
      my $s=$_->toString();
      $s=~s/<[^>]*>\s*//gs;
      $s=~s/\s*<\/[^>]*>//gs;
      $out.="$id = $s ; \n";
    } $doc->getElementsByTagName($a,0) 
  }
  return $out;
}

sub getProperties {
  my $doc=shift;
  my @l;
  map {
    my $s=$_->toString();
    $s=~s/<[^>]*>\s*//gs;
    $s=~s/\s*<\/[^>]*>//gs;
    push(@l,$s);
  } $doc->getElementsByTagName("prop",0);
  my $out=join(", ",@l);
  return <<EOT;
List[$out] ;
EOT
}

## helpers ##

sub fix {
  local $_=shift;
  s|\s||gs;
  return $_;
}

sub getValues {
  my ($node,$tag)=@_;
  my $u;
  map {
    my $s=$_->toString();
    $s=~s/<[^>]*>\s*//gs;
    $s=~s/\s*<\/[^>]*>//gs;
    push(@$u,$s) if $s;
  } $node->getElementsByTagName($tag,0);
  return $u; # gibt nun einen ListPointer zurück
}

sub getTagValue {
  my ($node,$tag)=@_;
  my $u=getValues($node,$tag);
  return join(" ",@$u) if $u; 
}

__END__

Typical generic output looks as follows

vars = List[x0,x1,x2,x3,x4];
parameters = List[u1,u2,u3,u4];
$c_0 = Point[0, 0] ; 
$c_1 = Point[u1, 0] ; 
$c_2 = Point[x1, x2] ; 
$c_3 = Point[x3, x4] ; 
$c_5 = sqrdist[$c_1, $c_2] ; 
$c_6 = sqrdist[$c_2, $c_3] ; 
$c_7 = sqrdist[$c_0, $c_3] ; 
$c_8 = triangle_area[$c_0, $c_1, $c_2] ; 
$c_9 = triangle_area[$c_0, $c_2, $c_3] ; 
prop = List[is_concyclic[$c_0, $c_1, $c_2, $c_3]] ;

where 
  name[..] is a function call
  ; is the command termination symbol
  = is the assignment
  $c_(\d+) are the variable names
  vars, parameters, prop, con are predefined names

Hopefully this allows to map on syntaxes of other target CAS using a simple
text rewriting tool.
