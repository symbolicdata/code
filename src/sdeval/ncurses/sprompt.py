class sprompt:
  """A simple single line input prompt for curses"""
  # TODO:
  # make it more efficient: use delchar to delete chars, etc.
  content="" # internal storage for user input
  prompts="" # will be shown as prompt symbol, before user input
  xoff=0 # x-position, where prompt begins (relative to win)
  yoff=0 # y-position, where prompt will be placed (relative to win)
  length=0 # maximum length to which display of prompt line is cut
  x=0 # cursor position
  win=None # curses window in which prompt shall be placed

  def get_content(self): return self.content

  def __init__(self, win, yoff, xoff, length=None, prompts="> "):
    self.prompts = prompts
    self.xoff = xoff
    self.yoff = yoff
    self.x = xoff + len(prompts)
    self.win = win
    if not length: self.length, winH = self.win.getmaxyx()
    else: self.length = length

  def print_prompts(self):
    self.win.addstr(self.yoff,self.xoff,self.prompts)

  def refresh(self): # TODO: untested
    print_prompts()
    winH,winW = win.getmaxyx()
    max_len_of_line = min( length, winW - xoff + 1 )
    if max_len_of_line < len(prompts) + len(content):
      max_len_input = max_len_of_line - len(prompts)
      win.addstr \
        (yoff,len(prompts)+xoff,content[-max_len_input:])
    else:
      win.addstr(yoff,len(prompts)+xoff,content)
    y,self.x = win.getyx()

  def appendch(self,c):
    winH,winW = self.win.getmaxyx()
    max_len_of_line = min( self.length, winW - self.xoff - 1 )
    max_len_display = len(self.prompts) + len(self.content);
    if max_len_display < max_len_of_line:
      self.win.addch(self.yoff,self.x,c)
      self.content = self.content + str(unichr(c))
      self.x += 1
    else:
      self.content = self.content + str(unichr(c))
      max_len_input = max_len_of_line - len(self.prompts)
      realxoff = len(self.prompts)+self.xoff
      self.win.addstr \
        ( self.yoff, realxoff, self.content[-max_len_input:])

  def delch_left(self):
    deleted_char = None
    if self.x > len(self.prompts) + self.xoff:
      winH,winW = self.win.getmaxyx()
      max_len_of_line = min( self.length, winW - self.xoff - 1 )
      max_len_display = len(self.prompts) + len(self.content);
      deleted_char = self.content[-1:]
      self.content = self.content[:-1]
      if max_len_display <= max_len_of_line:
        self.win.addch(self.yoff, self.x-1, ord(' '))
        self.win.move(self.yoff, self.x-1)
        self.x -= 1
      else:
        max_len_input = max_len_of_line - len(self.prompts)
        realxoff = len(self.prompts)+self.xoff
        self.win.addstr \
          ( self.yoff, realxoff, self.content[-max_len_input:])
    return deleted_char

  def get_lastch(self):
    return self.content[-1] if len(self.content) > 0 else None

  def get_last_word(self):
    return self.content.rsplit(" ", 1)[-1]

  def set_cursor(self): self.win.move(self.yoff, self.x)
