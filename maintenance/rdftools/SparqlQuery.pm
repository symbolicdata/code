##################################
#
# author: graebe
# createdAt: 2014-03-05
# lastUpdate: 2014-03-05

# purpose: Query connector to a local resp. the remote SPARQL endpoint at
# symbolicdata.org.

package SparqlQuery;

use URI::Escape;
use LWP::UserAgent;
use XML::DOM;
use strict;

my $parser=new XML::DOM::Parser;
my $ua = LWP::UserAgent->new;

# ------- Parse ResultSet functions -------

sub localQuery {
  return query(shift,"http://localhost:8890/sparql"); 
}

sub remoteQuery {
  return query(shift,"http://symbolicdata.org:8890/sparql"); 
}

sub query {
  my ($query,$sep)=@_;
  # print $query;
  my $url = "$sep?query=".uri_escape($query); 
  # print $url;
  my $req = HTTP::Request->new(GET => $url);
  my $res = $ua->request($req);
  if ($res->is_success) { return $res->content; } 
  else { print $res->status_line, "\n"; die; }
}

sub printResultSet { # for test purposes only
  my $u=shift;
  map printResult($_), (@$u);
}

sub printResult { # private to printResultSet
  my $h=shift;
  my $out="---------------\n";
  map {
    $out.="\t$_ -> $h->{$_}\n";
  } (sort keys %$h);
  print $out;
}

sub parseResult {
  my $in=shift();
  # print $in;
  my $doc=$parser->parse($in);
  # print $doc->toString();
  my $u;
  for my $a ($doc->getElementsByTagName("results")) {
    map push(@$u, getResult($_)), $a->getElementsByTagName("result");
  }
  # printResultSet($u);
  return $u; # Returns a Pointer to a list of HashPointers
}

sub getResult { # private to parseResult
  my $node=shift;
  my $h;
  map {
    my $id=$_->getAttribute("name");
    my $uri=getValue($_,"uri");
    my $literal=getValue($_,"literal");
    $h->{$id}=adjustURI($uri) if $uri;
    $h->{$id}=$literal if $literal;
  } $node->getElementsByTagName("binding");
  return $h;
}

sub adjustURI { # private to parseResult
  local $_=shift;
#  s|http://zak.ontowiki.de/Inspirata/[^/]*/||g;
#  s|.*\#||g;
  return $_;
}

sub getValue {
  my ($node,$tag)=@_;
  map {
    my $s=$_->toString(); 
    $s=~s/<[^>]*>\s*//gs;
    $s=~s/\s*<\/[^>]*>//gs;
    return $s;
  } $node->getElementsByTagName($tag,0);
}

1;
