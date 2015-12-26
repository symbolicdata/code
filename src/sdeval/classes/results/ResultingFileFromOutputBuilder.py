from ResultingFile import ResultingFile
import re

class ResultingFileFromOutputBuilder(object):
    """
    A builder of ResultingFile intances given output files of the
    computer algebra systems with time outputs.

    .. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
    """

    def build(self, pInstance, cas, outp):
        """
        The main function in this builder class. It creates an
        instance from the given output file.

        :param   pInstance: The name of the problem instance that was used as input.
        :type    pInstance: string
        :param         cas: The name of the computer algebra system that was used to perform the calculations
        :type          cas: string
        :param        outp: The output of the computer algebra system and the timings in the end
        :type         outp: string
        :raises    IOError: If something was wrong with the output file (for example no timings), this Error is raised.
        :returns: An Instance of ResultingFile, containing the output of the CAS and the timings
        :rtype: ResultingFile
        """
        m = re.search(r"(real){1}\s+[0-9]*\.?[0-9]*\s*(user){1}\s+[0-9]*\.?[0-9]*\s*(sys){1}\s+[0-9]*\.?[0-9]*",outp)
        if not m:
            raise IOError("The output file did not contain timings. It shall come with user, sys and real with additional time measures at the end.")
        timeString = m.group(0)
        realTime = re.search(r"(real){1}\s+[0-9]*\.?[0-9]*",timeString).group(0)
        userTime = re.search(r"(user){1}\s+[0-9]*\.?[0-9]*",timeString).group(0)
        sysTime  = re.search(r"(sys){1}\s+[0-9]*\.?[0-9]*",timeString).group(0)
        timeDict = {"real":realTime.strip("real").strip(),
                    "user":userTime.strip("user").strip(),
                    "sys":sysTime.strip("sys").strip()}
        return ResultingFile(pInstance, cas, outp.replace(timeString,"").strip(),timeDict)
