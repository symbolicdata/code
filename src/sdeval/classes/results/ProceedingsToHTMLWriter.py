from Proceedings import Proceedings

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
          _________________________|_____________________________|
          problem instance 2       |  Status of                  |  ...
                                   |  CAS1 on probleminstance 2  |
          _________________________|_____________________________|
          ...


        If the given parameter was not an instance of Proceedings, this function will return None.

        The style of the HTML file in general is specified in the file ``proceedints_css.css``, which is included
        in the result folder.
        
        :param     proceedings: The Proceedings-instance that we want to convert to HTML
        :type      proceedings: Proceedings
        :returns : The HTML representation of proceedings
        :rtype   : string
        """
        if not isinstance(proceedings, Proceedings):
            return None
        if proceedings == None:
            return None
        result = "\
<html>\n\
<head>\n\
\t<title>%s run at %s</title>\n\
\t<link rel=\"stylesheet\" type=\"text/css\" href=\"proceedings_css.css\">\n\
</head>\n\
<body>\n\
<h1> Task: %s </h1>\n\
<h2> Run at time: %s </h2>\n\
<br><br>\n\
<table id=\"mainTable\">\n\
\t<tr>\n\
\t\t<td id=\"piAndCAS\"> Problem Instance/Computer Algebra System</td>\n\
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
            result += "\t\t<td id=\"casName\">%s</td>\n" % c
        result += "\t</tr>\n"
        for p in piList:
            result +="\t<tr>\n\t\t<td id=\"piName\">%s</td>\n" %p
            for c in casList:
                if [p,c] in proceedings.getRUNNING():
                    result += "\t\t<td id=\"runningCalc\">RUNNING</td>\n"
                elif [p,c] in proceedings.getCOMPLETED():
                    result += "\t\t<td id=\"completedCalc\">COMPLETED</td>\n"
                elif [p,c] in proceedings.getERROR():
                    result += "\t\t<td id=\"erroneousCalc\">ERROR</td>\n"
                else:
                    result += "\t\t<td id=\"waitingCalc\">WAITING</td>\n"
            result += "\t</tr>\n"
        result += "\
</table>\n\
</body>\n\
</html>"
        return result
