# Issue 5205: [with patch, needs review] Set "# -*- coding: utf-8 -*-" encoding for sage/server/notebook/template.py

Issue created by migration from https://trac.sagemath.org/ticket/5205

Original creator: mabshoff

Original creation time: 2009-02-08 06:14:26

Assignee: mabshoff

CC:  jason malb

When building Sage 3.3.alpha6 every doctest passes. Move the tree, start Sage once so that all the pyc files are rewritten and then doctest and failures galore:

```
	sage -t -long devel/sage/sage/server/notebook/cell.py # 136 doctests failed
	sage -t -long devel/sage/sage/server/notebook/worksheet.py # 379 doctests failed
	sage -t -long devel/sage/sage/server/notebook/twist.py # 39 doctests failed
	sage -t -long devel/sage/sage/server/notebook/notebook.py # 127 doctests failed
	sage -t -long devel/sage/sage/server/notebook/avatars.py # 13 doctests failed
	sage -t -long devel/sage/sage/server/notebook/template.py # 10 doctests failed
```

This all boils down to

```
File "/scratch/mabshoff/sage-3.3.rc0/devel/sage-main/sage/server/notebook/worksheet.py", line 347:
    sage: nb = sage.server.notebook.notebook.Notebook(tmp_dir())
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.3.alpha6/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha6/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha6/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[2]>", line 1, in <module>
        nb = sage.server.notebook.notebook.Notebook(tmp_dir())###line 347:
    sage: nb = sage.server.notebook.notebook.Notebook(tmp_dir())
      File "/scratch/mabshoff/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py", line 94, in __init__
        import sage.server.notebook.twist
      File "/scratch/mabshoff/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 44, in <module>
        from sage.server.notebook.template import template
      File "/scratch/mabshoff/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/server/notebook/template.py", line 64
     SyntaxError: Non-ASCII character '\xc3' in file /scratch/mabshoff/sage-3.3.rc0/local/lib/python2.5/site-packages/sage/server/notebook/template.py on line 65, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details (template.py, line 64)
```

As I pointed out in #5176 we must declare the encoding, but then I tested the cloning of the repo and could not get it to fail. I am clueless why, but the patch fixes the issue for me. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-08 06:19:17

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-08 06:19:17

Well, I am clueless when testing for this failure I could not get it to go boom. The fix itself is obvious.

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2009-02-08 06:48:10

Looks good.


---

Comment by mabshoff created at 2009-02-08 07:42:03

Merged in Sage 3.3.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-08 07:42:03

Resolution: fixed
