class ResultedTimingsToHTMLWriter(object):
    """
    This is a builder class that creates an html representing a given ResultedTimings instance of a task.

    .. seealso:: :mod:`ResultedTimings <sdeval.classes.results.ResultedTimings>`
    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def createHTMLFromResultedTimings(self, rt):
        """
        Given an ResultedTimings instance, this procedure writes an
        html-String representing a Website of the following form::

          <Name of the Task>
          
          <Time Stamp when the running was started>
          
          Table
                             /CASs |                             |
          problem instances/       |  CAS 1                      |  CAS 2
          _________________________|_____________________________|________________________
          problem instance 1       |  Either status of           |   ...
                                   |  CAS1 on probleminstance 1  |
                                   |  or used time               |
          _________________________|_____________________________|________________________
          problem instance 2       |  Either status of           |  ...
                                   |  CAS1 on probleminstance 2  |
                                   |  or used time               |
          _________________________|_____________________________|________________________
          ...
        """
        result = "\
<html>\n\
<head>\n\
\t<title>%s run at %s</title>\n\
</head>\n\
<body>\n\
<h1> Task: %s </h1>\n\
<h2> Run at time: %s </h2>\n\
<br><br>\n\
<table border=1>\n\
\t<tr>\n\
\t\t<td> Problem Instance/Computer Algebra System</td>\n\
" % (rt.getTask(),
     rt.getTimeStamp(),
     rt.getTask(),
     rt.getTimeStamp())
        #collect all cass and problem instances
        casList = map(lambda x: x[1],rt.getRUNNING()+rt.getWAITING()+rt.getERROR()+rt.getCOMPLETED())
        casList = list(set(casList))
        piList = map(lambda x: x[0],rt.getRUNNING()+rt.getWAITING()+rt.getERROR()+rt.getCOMPLETED())
        piList = list(set(piList))
        for c in casList:
            result += "\t\t<td>%s</td>\n" % c
        result += "\t</tr>\n"
        for p in piList:
            result +="\t<tr>\n\t\t<td>%s</td>\n" %p
            for c in casList:
                if [p,c] in map(lambda x: x[:2],rt.getRUNNING()):
                    result += "\t\t<td bgcolor=yellow>RUNNING</td>\n"
                elif [p,c] in map(lambda x: x[:2],rt.getCOMPLETED()):
                    result += "\t\t<td bgcolor=green>%s</td>\n" % ";".join(str(k)+":"+str(rt.getResultingFileDict()[str([p,c])][k]) for k in rt.getResultingFileDict()[str([p,c])])
                elif [p,c] in map(lambda x: x[:2],rt.getERROR()):
                    result += "\t\t<td bgcolor=red>%</td>\n" % ";".join(str(k)+":"+str(rt.getResultingFileDict()[str([p,c])][k]) for k in rt.getResultingFileDict()[str([p,c])])
                else:
                    result += "\t\t<td>WAITING</td>\n"
            result += "\t</tr>\n"
        result += "\
</table>\n\
</body>\n\
</html>"
        return result
