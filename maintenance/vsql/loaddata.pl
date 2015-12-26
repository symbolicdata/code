##################################
#
# author: graebe
# createdAt: 2013-08-24
# lastModified: 2013-09-15

# purpose: load data into the local Virtuoso store
# usage: perl loaddata.pl | isql-vt 1111 dba <YourSecretPassword>

# The environment variable SD should point to the root dir of the symbolicdata
# repo clone. Note that isql-vt does not follow symlinks, hence set 
#   export SD=/local/home/symbolicdata/... 
# on symbolicdata.org 

die "Environment variable SD not set" unless $ENV{'SD'};

my $RDFData="$ENV{'SD'}/data/RDFData";
# print cleardata();
print loaddata();

## end main ## 

sub cleardata {
  return <<EOT;
sparql clear graph <http://symbolicdata.org/Data/Annotations/> ;
sparql clear graph <http://symbolicdata.org/Data/Bibliography/> ;
sparql clear graph <http://symbolicdata.org/Data/FanoPolytopes/> ;
sparql clear graph <http://symbolicdata.org/Data/FreeAlgebras/> ;
sparql clear graph <http://symbolicdata.org/Data/GAlgebras/> ;
sparql clear graph <http://symbolicdata.org/Data/GeoCode/> ;
sparql clear graph <http://symbolicdata.org/Data/GeoProofSchemes/> ;
sparql clear graph <http://symbolicdata.org/Data/GeometryProblems/> ;
sparql clear graph <http://symbolicdata.org/Data/People/> ;
sparql clear graph <http://symbolicdata.org/Data/PolynomialSystems/> ;
sparql clear graph <http://symbolicdata.org/Data/Systems/> ;
sparql clear graph <http://symbolicdata.org/Data/TestSets/> ;
EOT
}

sub loaddata {
  my $out;
  $out.=createLoadCommand("Annotations","Annotations.ttl");
  $out.=createLoadCommand("Bibliography","Bibliography.ttl");
  $out.=createLoadCommand("FanoPolytopes","FanoPolytopes.ttl");
  $out.=createLoadCommand("FreeAlgebras","FreeAlgebras.ttl");
  $out.=createLoadCommand("GAlgebras","GAlgebras.ttl");
  $out.=createLoadCommand("GeoCode","GeoCode.ttl");
  $out.=createLoadCommand("GeoProofSchemes","GeoProofSchemes.ttl");
  $out.=createLoadCommand("GeometryProblems","GeometryProblems.ttl");
  $out.=createLoadCommand("People","People.ttl");
  $out.=createLoadCommand("PolynomialSystems","PolynomialSystems.ttl");
  $out.=createLoadCommand("Systems","Systems.ttl");
  $out.=createLoadCommand("TestSets","TestSets.ttl");
  return $out;
}

sub createLoadCommand {
  my ($graph,$file)=@_;
  return<<EOT;
sparql create silent graph <http://symbolicdata.org/Data/$graph/> ; 
DB.DBA.TTLP_MT (file_to_string_output('$RDFData/$file'),'http://symbolicdata.org/Data/$graph/'); 
EOT
}


__END__

