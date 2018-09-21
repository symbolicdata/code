import os
import sys
import classes.xmldiffs as xmldiffs

args = sys.argv

cas1 = "Singular" # default value
cas2 = cas1
if len(args) - 1 >= 4:
    cas1 = args[3]
    cas2 = args[4]
resultFiles1 = os.path.join(args[1], "resultFiles")
resultFiles2 = os.path.join(args[2], "resultFiles")

problemInstances1 = next(os.walk(resultFiles1))[1]
problemInstances2 = next(os.walk(resultFiles2))[1]
diff = list(set(problemInstances1).symmetric_difference(set(problemInstances2)))
print("Not matched: " + str(diff))
for problemInstance1 in problemInstances1:
    for problemInstance2 in problemInstances2:
        if problemInstance1 == problemInstance2:
            solutionPath1 = os.path.join(resultFiles1, problemInstance1, cas1)
            solutionPath2 = os.path.join(resultFiles2, problemInstance2, cas2)
            if "solutionInXML.xml" in next(os.walk(solutionPath1))[2]:
                if "solutionInXML.xml" in next(os.walk(solutionPath2))[2]:
                    solutionXML1 = os.path.join(solutionPath1, "solutionInXML.xml")
                    solutionXML2 = os.path.join(solutionPath2, "solutionInXML.xml")
                    xmldiffs.xmldiffs(solutionXML1, solutionXML2)