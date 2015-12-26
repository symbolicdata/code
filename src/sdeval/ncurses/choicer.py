#.. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
# TODO: Notice Copyright
import re

class choicer:
  """
  calculate choices from a list determined by a line of user input
  """

  # this is a list of pairs: first pair is copied from the
  # choices list given at initialization; second pair is a copy
  # of that choice with all characters from the ...
  pchoices = [] #  ... ignore variable string removed
  sep = "" # seperator at which user's input string will be split
  ignore = "" # see description of __init__

  """
  ignore all characters from ignore string (d.i. if user types
  them in or not is not important for an item of choices,
  containing those characters, to be selected)
  """
  def __init__(self, choices, sep=" ", ignore=""):
    self.pchoices = []
    for choice in choices:
      ichoice = choice.translate( None, ignore )
      self.pchoices.append([choice, ichoice])
    self.sep = sep

  """
  calculate choices determined by user input; user input will be
  split into words by sep; every item in choice, which contains
  one of the words of the user input, will be added to the users
  selection; matching is done incasesensitive; could be more
  effective, since most often it is not necessary to search again
  for all users choices (e.g. if only one character changes)
  """
  def get_user_choices_additive(self, user_input_string):
    uinput = filter( None, user_input_string.split(self.sep) )
    user_choices = []
    for pchoice in self.pchoices:
      found = False
      for up in uinput:
        for choice in pchoice: # look input matches in pchoice
          upl = up.split("*")
          ms = 0 # where to start searching for a match
          found = True
          j = len(upl)-1
          for i in range(len(upl)-1):
            if upl[i] != '': j = i; break
          upl = upl[j:] # remove empty strings at front of upl
          for u in upl:
            if not u: continue # * at end or **
            match = re.search(u,choice[ms:],re.IGNORECASE)
            if not match: found = False; break
            else: ms += match.end(0)
          if found: user_choices.append(pchoice[0]); break
          if found: return temp
        if found: break # is a match: stop looping through input
    return user_choices

  def get_pchoices(self): return self.pchoices;
