# Issue 40: preparser issues

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 23:31:32

Assignee: somebody

{{{To: "Kyle Schalm" <kschalm`@`math.utexas.edu>, sage-devel`@`lists.sourceforge.net
Subject: Re: [SAGEdev] long string parsing bug in 1.3.2.2

The SAGE pre-parser currently works on single lines only -- it doesn't
take into account multi-line blocks.  This is more a
not-implemented-error than a bug.  Many thanks for sending this email
though, since it's an excellent test case:
mm.sage:
---------------------
"""
load with
 
sage: load "/Users/kyle/Documents/math/scripts/mm.sage"
"""
---------------------
}}}


---

Comment by was created at 2007-01-12 21:57:59

I can't find this mm.sage example any more.  Moreover, the preparser does work
on multiple lines, so won't fix until get a proper bug report.


---

Comment by was created at 2007-01-12 21:57:59

Resolution: wontfix


---

Comment by was created at 2007-01-21 04:51:33

Changing component from basic arithmetic to user interface.


---

Comment by was created at 2007-01-21 04:51:33

I found that loading files with triple quoted multiline strings would break.
Now fixed:


```
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1169354692 28800
# Node ID 9b38891949ca0db4e3df5592611a741f8b58568d
# Parent  19cc21de721be8ea5985cf1319582e1ab7dc2820
Finally fixed multiline preparser issue for command line.

diff -r 19cc21de721b -r 9b38891949ca sage/misc/interpreter.py
--- a/sage/misc/interpreter.py  Fri Jan 19 22:49:10 2007 -0800
+++ b/sage/misc/interpreter.py  Sat Jan 20 20:44:52 2007 -0800
`@``@` -248,7 +248,7 `@``@` def do_prefilter_paste(line, continuatio
                     ipmagic(L)
                 L = ''
             else:
-                L = preparser_ipython.preparse_ipython(L)
+                L = preparser_ipython.preparse_ipython(L, not continuation)
             __IPYTHON__.input_hist.append(L)
             __IPYTHON__.push(L)
         log.offset += 1
`@``@` -343,7 +343,7 `@``@` def do_prefilter_paste(line, continuatio
         else:
             raise ImportError, "Attaching of '%s' not implemented (load .py, .spyx, and .sage files)"%name
     if len(line) > 0:
-        line = preparser_ipython.preparse_ipython(line)
+        line = preparser_ipython.preparse_ipython(line, not continuation)
     return line
 
 def load_sagex(name):
```

