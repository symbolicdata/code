#!/usr/bin/env python
"""
Usage: {prog} [OPTION] FILE1 FILE2

Compare two XML files, ignoring element and attribute order.

Any extra options are passed to the `diff' command.

Copyright (c) 2017, Johannes H. Jensen.

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

* Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

* The names of the contributors may not be used to endorse or promote 
  products derived from this software without specific prior written
  permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
from __future__ import print_function, unicode_literals
import sys
import os
import io
import xml.etree.ElementTree as ET
from tempfile import NamedTemporaryFile
import subprocess

def attr_str(k, v):
    return "{}=\"{}\"".format(k,v)

def node_str(n):
    attrs = sorted(n.attrib.items())
    astr = " ".join(attr_str(k,v) for k,v in attrs)
    s = n.tag
    if astr:
        s += " " + astr
    return s

def node_key(n):
    return node_str(n)

def indent(s, level):
    return "  " * level + s

def write_sorted(stream, node, level=0):
    children = node.getchildren()
    text = (node.text or "").strip()
    tail = (node.tail or "").strip()

    if children or text:
        children.sort(key=node_key)

        stream.write(indent("<" + node_str(node) + ">\n", level))

        if text:
            stream.write(indent(text + "\n", level))

        for child in children:
            write_sorted(stream, child, level + 1)

        stream.write(indent("</" + node.tag + ">\n", level))
    else:
        stream.write(indent("<" + node_str(node) + "/>\n", level))

    if tail:
        stream.write(indent(tail + "\n", level))

if sys.version_info < (3, 0):
    # Python 2
    import codecs
    def unicode_writer(fp):
        return codecs.getwriter('utf-8')(fp)
else:
    # Python 3
    def unicode_writer(fp):
        return fp

def xmldiffs(file1, file2, diffargs=["-u"]):
    tree = ET.parse(file1)
    tmp1 = unicode_writer(NamedTemporaryFile('w'))
    write_sorted(tmp1, tree.getroot())
    tmp1.flush()

    tree = ET.parse(file2)
    tmp2 = unicode_writer(NamedTemporaryFile('w'))
    write_sorted(tmp2, tree.getroot())
    tmp2.flush()

    args = [ "colordiff" ]
    args += diffargs
    args += [ "--label", file1, "--label", file2 ]
    args += [ tmp1.name, tmp2.name ]

    try:
        subprocess.call(args)
    except OSError:
        args[0] = "diff"
        subprocess.call(args)

def print_usage(prog):
    print(__doc__.format(prog=prog).strip())

if __name__ == '__main__':
    args = sys.argv
    prog = os.path.basename(args.pop(0))

    if '-h' in args or '--help' in args:
        print_usage(prog)
        exit(0)

    if len(args) < 2:
        print_usage(prog)
        exit(1)

    file2 = args.pop(-1)
    file1 = args.pop(-1)
    diffargs = args if args else ["-u"]

    xmldiffs(file1, file2, diffargs)
