import os
import sys
import classes.xmldiffs as xmldiffs
import argparse
import re

PURPLE_COLOR = '\033[95m'
BOLD_COLOR = '\033[1m'
UNDERLINE_COLOR = '\033[4m'
WARNING_COLOR = '\033[93m'
HEADER_COLOR = PURPLE_COLOR + BOLD_COLOR + UNDERLINE_COLOR
END_COLOR = '\033[0m'

parser = argparse.ArgumentParser(description='Compare two result folders among CASs')
parser.add_argument('-f','--result-folder', metavar='result folder', required=True, help='The first result folder. If it is the results folder, the latest result folder will be choosen.')
parser.add_argument('-f2','--result-folder2', metavar='result folder', help='The second result folder (if not set, the first result folder is compared to it self). If it is the results folder, the latest result folder will be choosen.')
parser.add_argument('-c', '--cas', dest='cas', metavar='CAS', nargs='+', help='Compare the result folders among CASs. If not specified, all CASs are compared.')
parser.add_argument('-c1', '--cas1', dest='cas1', metavar='CAS', nargs='+', help='Compare the first result folder among CASs, overwrites other values.')
parser.add_argument('-c2', '--cas2', dest='cas2', metavar='CAS', nargs='+', help='Compare the second result folder among CASs, overwrites other values.')
parser.add_argument('-n', '--dry-run', action="store_true", help='Just print which files would be compared.')
args = parser.parse_args()

casArg1 = args.cas1
casArg2 = args.cas2
if casArg1 == None:
    casArg1 = args.cas
if casArg2 == None:
    casArg2 = args.cas

resultFolder1 = args.result_folder
resultFolder2 = args.result_folder2
if resultFolder2 == None:
    resultFolder2 = resultFolder1

if "resultFiles" not in next(os.walk(resultFolder1))[1]:
    resultFolderRegEx = re.compile('\d+_\d+_\d+_\d+_\d+_\d+')
    resultFolder1 = os.path.join(resultFolder1, sorted([dirname for dirname in next(os.walk(resultFolder1))[1] if resultFolderRegEx.match(dirname)])[-1])
if "resultFiles" not in next(os.walk(resultFolder2))[1]:
    resultFolderRegEx = re.compile('\d+_\d+_\d+_\d+_\d+_\d+')
    resultFolder2 = os.path.join(resultFolder2, sorted([dirname for dirname in next(os.walk(resultFolder2))[1] if resultFolderRegEx.match(dirname)])[-1])

print(resultFolder1)
print(resultFolder2)

resultFiles1 = os.path.join(resultFolder1, "resultFiles")
resultFiles2 = os.path.join(resultFolder2, "resultFiles")

problemInstances1 = next(os.walk(resultFiles1))[1]
problemInstances2 = next(os.walk(resultFiles2))[1]
diff = list(set(problemInstances1).symmetric_difference(set(problemInstances2)))
if len(diff) > 0:
    print(WARNING_COLOR + "Not matched: " + str(diff) + END_COLOR)
for problemInstance1 in problemInstances1:
    for problemInstance2 in problemInstances2:
        if problemInstance1 == problemInstance2:

            problemInstancePath1 = os.path.join(resultFiles1, problemInstance1)
            problemInstancePath2 = os.path.join(resultFiles2, problemInstance2)

            makediff = False
            if casArg1 == None:
                casList1 = next(os.walk(problemInstancePath1))[1]
                makediff = True
            else:
                casList1 = list(casArg1) # make a copy
            if casArg2 == None:
                casList2 = next(os.walk(problemInstancePath2))[1]
                makediff = True
            else:
                casList2 = list(casArg2) # make a copy
            if makediff: # if one of the two lists were not specified by the user
                diff = list(set(casList1).symmetric_difference(set(casList2)))
                if len(diff) > 0:
                    print(WARNING_COLOR + "Not matched CASs for " + problemInstance1 + ": " + str(diff) + END_COLOR)

            printedHeader = False
            for cas1 in casList1:
                for cas2 in casList2:
                    if resultFolder1 == resultFolder2 and cas1 == cas2:
                        continue

                    solutionPath1 = os.path.join(problemInstancePath1, cas1)
                    solutionPath2 = os.path.join(problemInstancePath2, cas2)

                    solutionFileName = "solutionInXML.xml"
                    solutionFiles1 = next(os.walk(solutionPath1))[2]
                    solutionFiles2 = next(os.walk(solutionPath2))[2]

                    if solutionFileName not in solutionFiles1:
                        print(WARNING_COLOR + cas1 + " solution missing for " + problemInstance1 + " in " + resultFolder1 + END_COLOR)
                        break
                    if solutionFileName not in solutionFiles2:
                        print(WARNING_COLOR + cas2 + " solution missing for " + problemInstance2 + " in " + resultFolder2 + END_COLOR)
                        casList2.remove(cas2)
                        continue

                    solutionXML1 = os.path.join(solutionPath1, solutionFileName)
                    solutionXML2 = os.path.join(solutionPath2, solutionFileName)
                    if args.dry_run:
                        print("Would compare " + solutionXML1 + " and " + solutionXML2)
                    else:
                        diff = xmldiffs.xmldiffs(solutionXML1, solutionXML2)
                        if len(diff) > 0:
                            if not printedHeader:
                                print(HEADER_COLOR + "Problem Instance: " + problemInstance1 + END_COLOR + "\n")
                                printedHeader = True
                            print(diff)
