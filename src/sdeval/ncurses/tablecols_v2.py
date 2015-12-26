class tablecols:
  """
  display a list of words aligned into the columns of a table
  """

  # TODO: setters for changing attributes
  # TODO: implement scroll for one page
  # TODO: show indicators if possible to scroll up or down

  llist = [] #list of lists of words to be aligned in tables
  win=None # curses window in which the display shall be printed
  xoff = 0 # x-position where display begins (relative to win)
  yoff = 0 # y-position where display begins (relative to win)
  width = 0 # width of display
  height = 0 # height of display
  sep = "  " # column seperators for displayed columns
  index = 0 # index of first line of the table displayed
  llines = None # (printable) list of lists of lines of the table

  def __init__ \
      ( self, win, llist=[], sep="  ", \
        xoff=0, yoff=0, width=0, height=0, index=0 ):
    self.win = win
    self.llist = llist
    self.sep = sep
    self.xoff = xoff; self.yoff = yoff
    if width == 0 or height == 0:
      winH,winW = win.getmaxyx()
      if width == 0: width = winW
      if height == 0: height = winH
    self.width = width; self.height = height

  """
  calculate sizes of columns such that the strings in words can
  be written column by column with these sizes (columns
  seperated by sep) into a table of a given width; might not be
  optimally implemented
  Warning: this does not always produce the optimal result !
  """
  @staticmethod
  def get_ordered_table(words, sep, width):
    if len(words) == 0: return []
    num_cols = 2 # optimizable: find a better heuristic of number
    all_fits = True # of columns to start with; but algorithm
    colsizes = [0] * num_cols # might get more complicated
    # idea for example: num_cols = width/average_word_length

    while all_fits: # try to find max num of columns
      num_rows = int(len(words)/num_cols)
      num_rows += 1 if len(words) % num_cols > 0 else 0 #round up
      old_colsizes = list(colsizes)
      colsizes = [0] * num_cols
      sep_lens = len(sep) * (num_cols-1)
      sum_colsizes = 0
      for i in range(num_cols):
        for j in range(num_rows):
          list_index = num_rows*i + j
          if list_index >= len(words): #all lines tested => break
            break #next i will be num_cols => breaks out of outer
          col_size_diff = len(words[list_index]) - colsizes[i]
          if col_size_diff > 0: # found a new longer string...
            colsizes[i] += col_size_diff # ...update colsizes...
            sum_colsizes += col_size_diff # ...and test if...
            all_fits = sum_colsizes + sep_lens < width
            if not all_fits: break # ...columns still fit in line
        if not all_fits: break # does not fit => take num_cols-1
      if all_fits: num_cols += 1 # fits, try to take one more col
      else: num_cols -= 1 # take num_cols-1, loop will end

    if num_cols == 1: # special case: tested first two columns
      lenws = map(len, words) # haven't had colsizes for just
      old_colsizes = [max(lenws)] # one column

    return old_colsizes # end of get_ordered_table

  """
  like get_ordered_table, but this time create the table and
  return a list of it's lines
  """
  @staticmethod
  def get_ordered_table_lines(words, sep, width):
    if len(words) == 0: return []
    colsizes = tablecols.get_ordered_table(words, sep, width)
    num_rows = int(len(words)/len(colsizes))
    num_rows += 1 if len(words) % len(colsizes) > 0 else 0
    lines = []
    for i in range(num_rows):
      line = [] # first create list of words for each line
      for j in range(len(colsizes)):
        wi = num_rows*j + i # calculate index of word in table
        if wi >= len(words): # happens if len(words) < rows*cols
          line.append( " ".ljust(colsizes[j]) )
        else: # create array of all words in table line
          line.append( words[wi].ljust(colsizes[j]) )
      lines.append(sep.join(line)) # join the words into the line
    return lines

  """
  like get_ordered_table_lines, but this time we have a list of
  lists (llist) and will create for each sublist a table; llines
  will be the join of these tables (with empty lines between each
  subtable)
  """
  def refresh_llines(self):
    self.llines = []
    for words in self.llist:
      lines = \
          tablecols.get_ordered_table_lines\
          (words,self.sep,self.width)
      self.llines.append( lines )

  """
  create and display the table of columns
  """
  def display_table(self):
    winH,winW = self.win.getmaxyx()
    width = min(self.width, winW - self.xoff)
    height = min(self.height, winH - self.yoff)

    # create table lines, if not yet done
    if not self.llines: self.refresh_llines()

    # lheight: minimum of heigth of display area and the sum of
    # all lines in llines plus an empty line between each list in
    # llines minus the index of the first element displayed
    lheight = \
        reduce(lambda x, y: x + len(y), self.llist, 0)
    lheight = \
        min(height, lheight+len(self.llist)+1 - self.index)

    # index of list in llist, the line determined by self.index
    # is contained in or directly after (empty line) ...
    llindex = 0
    nbefore = 0 # ... sum of lines in lists before this list ...
    for i in range(len(self.llist)):
      if self.index <= len(self.llist[i]) + nbefore:
        llindex = i; break
      else: nbefore += len(self.llist[i]) + 1 # +1 for empty line sep

    # ... index of line in the list, might be len(list), if
    # pointing to the empty seperator line after this list
    lindex = self.index - nbefore

    lnr = 0
    for lines in self.llines: # print all lines of table to window
      for line in lines:
        if lnr > lheight-1: return
        self.win.addstr(self.yoff + lnr, self.xoff, line)
        lnr += 1
      if lnr > lheight-1: return
      self.win.addstr( self.yoff+lnr, self.xoff, " "*(width-1) )
      lnr += 1
  # end of display_table

  """
  remove the last list of words and redraw the table(s)
  TODO: could be more efficient; we do not always have to redraw
  the whole screen
  TODO: does not consider index
  """
  def pop_n_redraw(self):
    winH,winW = self.win.getmaxyx()
    width = min(self.width, winW - self.xoff)
    height = min(self.height, winH - self.yoff)
    for i in range(height):
      self.win.addstr( self.yoff+i, self.xoff, " "*(width-1) )
    self.llines.pop()
    self.llist.pop()
    self.display_table()

  """
  redraw the table(s)
  TODO: could be more efficient; we do not always have to redraw
  the whole screen
  TODO: does not consider index
  """
  def redraw(self):
    winH,winW = self.win.getmaxyx()
    width = min(self.width, winW - self.xoff)
    height = min(self.height, winH - self.yoff)
    for i in range(height):
      self.win.addstr( self.yoff+i, self.xoff, " "*(width-1) )
    self.display_table()

  def has_words(self):
    for words in self.llist:
      if len(words) > 0: return True
    return False

  def get_merged_words(self):
    all_words = []
    for words in self.llist:
      all_words.extend(words)
    return all_words

  def get_numlines_of_table(self):
    if not self.llines: # if lines of table are not yet created...
      self.refresh_llines()
    numlines = 0
    for lines in self.llines:
      for line in lines:
        numlines += 1
    return numlines

  def append(self, words):
    self.llist.append(words)
    if not self.llines: self.refresh_llines()
    else:
      self.llines.append( tablecols.get_ordered_table_lines\
                             (words,self.sep,self.width)     )

  def __setitem__(self, index, words):
    self.llist[index] = words
    self.llines[index] =\
      tablecols.get_ordered_table_lines\
          (words,self.sep,self.width)

  def __getitem__(self, index): return self.llist[index]

  """
  The following member functions are not yet adapted to the
  multiline version
  """

  """
  scroll display one line up
  (display_table has to be called afterwards)
  """
  def scroll_up(self):
    if not self.lines: # if lines of table are not yet created...
      winH,winW = self.win.getmaxyx()
      width = min(self.width, winW - self.xoff)
      self.lines = \
          self.get_ordered_table_lines \
          (self.words, self.sep, width) # ...create them now
    if self.index > 0: self.index -= 1

  """
  scroll display one line down
  (display_table has to be called afterwards)
  """
  def scroll_down(self):
    if not self.lines: # if lines of table are not yet created...
      winH,winW = self.win.getmaxyx()
      width = min(self.width, winW - self.xoff)
      self.lines = \
          self.get_ordered_table_lines \
          (self.words, self.sep, width) # ...create them now
    if len(self.lines) - (self.index+1) > self.height:
      self.index += 1 # only increase if undisplayed lines exist

  def set_height(self, height): self.height = height;

  """
  will delete the created table, such that the next function
  using it has to recreate it
  """
  def refresh(self): self.lines = None
