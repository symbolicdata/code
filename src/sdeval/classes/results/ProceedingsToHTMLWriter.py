class ProceedingsToHTMLWriter(object):
    """
    This is a builder class that creates an html representing a given proceedings of a task.

    .. seealso:: :mod:`Proceedings <sdeval.classes.results.Proceedings>`
    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def createHTMLFromProceedings(self, proceedings):
        """
        Given an Proceedings instance, this procedure writes an
        html-String representing a Website of the following form::

          <Name of the Task>
          
          <Time Stamp when the running was started>
          
          Table
                             /CASs |                             |
          problem instances/       |  CAS 1                      |  CAS 2
          _________________________|_____________________________|________________________
          problem instance 1       |  Status of                  |   ...
                                   |  CAS1 on probleminstance 1  |
          _______________________________________________________|
          problem instance 2       |  Status of                  |  ...
                                   |  CAS1 on probleminstance 2  |
          _________________________|_____________________________|
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
" % (proceedings.getTask(),
     proceedings.getTimeStamp(),
     proceedings.getTask(),
     proceedings.getTimeStamp())
        #collect all cass and problem instances
        casList = map(lambda x: x[1],proceedings.getRUNNING()+proceedings.getWAITING()+proceedings.getERROR()+proceedings.getCOMPLETED())
        casList = list(set(casList))
        piList = map(lambda x: x[0],proceedings.getRUNNING()+proceedings.getWAITING()+proceedings.getERROR()+proceedings.getCOMPLETED())
        piList = list(set(piList))
        for c in casList:
            result += "\t\t<td>%s</td>\n" % c
        result += "\t</tr>\n"
        for p in piList:
            result +="\t<tr>\n\t\t<td>%s</td>\n" %p
            for c in casList:
                if [p,c] in proceedings.getRUNNING():
                    result += "\t\t<td bgcolor=yellow>RUNNING</td>\n"
                elif [p,c] in proceedings.getCOMPLETED():
                    result += "\t\t<td bgcolor=green>COMPLETED</td>\n"
                elif [p,c] in proceedings.getERROR():
                    result += "\t\t<td bgcolor=red>ERROR</td>\n"
                else:
                    result += "\t\t<td>WAITING</td>\n"
            result += "\t</tr>\n"
        result += "\
</table>\n\
</body>\n\
</html>"
        return result
