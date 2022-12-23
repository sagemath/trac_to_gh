# Issue 5079: overly greedy RealNumber handling in preparser

Issue created by migration from https://trac.sagemath.org/ticket/5079

Original creator: boothby

Original creation time: 2009-01-23 22:29:27

Assignee: boothby

This is an amalgamation of #4806, #4459, and #1599.  The RealNumber wrapper is too greedy.


```
   1.exp() -> RealNumber(1.e)xp()
   1.rational_reconstruction() -> 1.ational_reconstruction()
   1.e+10 -> RealNumber(1.e)+10
   1._xgcd() -> RealNumber(1.)_xgcd()
```


One patch should do it all.


---

Attachment


---

Attachment


---

Attachment

Also takes care of #4501 and parsing numbers of the form 5L, and Py3 binary and octal numbers, as well as simplifying the preparser.


---

Comment by mhansen created at 2009-01-24 16:20:20

I think the preparsing code is a fair amount easier to follow after this.  Nice work!  I folded all three of the patches into trac_5079.patch for review purposes.

Note that this depends on #5078 being applied.


---

Comment by mabshoff created at 2009-01-24 17:03:55

This patch causes various test failures all seemingly of the type

```
mabshoff@geom:/scratch/mabshoff/sage-3.3.alpha2$ ./sage -t -long devel/sage/sage/server/notebook/twist.py
sage -t -long "devel/sage/sage/server/notebook/twist.py"    
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/server/notebook/twist.py", line 1459:
    sage: W = n.new_worksheet_with_title_from_text('Sage', owner='sage')
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.3.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_21[4]>", line 1, in <module>
        W = n.new_worksheet_with_title_from_text('Sage', owner='sage')###line 1459:
    sage: W = n.new_worksheet_with_title_from_text('Sage', owner='sage')
      File "/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py", line 930, in new_worksheet_with_title_from_text
        W = self.create_new_worksheet(name, owner)
      File "/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py", line 623, in create_new_worksheet
        auto_publish = False)
      File "/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 248, in __init__
        self.save_snapshot(owner)
      File "/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 1640, in save_snapshot
        E = self.edit_text()
      File "/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/server/notebook/worksheet.py", line 1823, in edit_text
        t = C.edit_text().strip()
      File "/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/server/notebook/cell.py", line 783, in edit_text
        s = self.plain_text(ncols, prompts, max_out)
      File "/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/server/notebook/cell.py", line 760, in plain_text
        out = self.output_text(ncols, raw=True, html=False, allow_interact=False)
      File "/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/server/notebook/cell.py", line 1240, in output_text
        is_interact = self.is_interactive_cell()
      File "/scratch/mabshoff/sage-3.3.alpha2/local/lib/python2.5/site-packages/sage/server/notebook/cell.py", line 917, in is_interactive_cell
        s, _ = strip_string_literals(self.input_text())
    ValueError: too many values to unpack
**********************************************************************
```

The failures are in 

```
	sage -t -long devel/sage/sage/server/notebook/cell.py # 85 doctests failed
	sage -t -long devel/sage/sage/server/notebook/worksheet.py # 289 doctests failed
	sage -t -long devel/sage/sage/server/notebook/twist.py # 3 doctests failed
	sage -t -long devel/sage/sage/server/notebook/notebook.py # 19 doctests failed
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 19:46:14

Note that Mike Hansen's patch which I deleted depends on #4405 to be applied. So Mike please repost that patch since I deleted it. Boothby is working on fixing the above issues and will post an incremental patch on top of the three here already.

Cheers,

Michael


---

Attachment

The above was caused by the notebook calling strip_string_literals and not properly handling the returns.  Accept the following as proof that everything in sage is calling it right:



```
sage: search_src('strip_string_literals')
misc/preparser.py:    -- Robert Bradshaw (2007-09-19): * strip_string_literals, containing_block 
misc/preparser.py:def strip_string_literals(code, state=None):
misc/preparser.py:        sage: from sage.misc.preparser import strip_string_literals
misc/preparser.py:        sage: s, literals, state = strip_string_literals(r'''['a', "b", 'c', "d\""]''')
misc/preparser.py:        sage: print strip_string_literals(r'-"\\\""-"\\"-')[0]
misc/preparser.py:        sage: s, literals, state = strip_string_literals("[a, '''b''', c, '']")
misc/preparser.py:        sage: s, literals, state = strip_string_literals("code '#' # ccc 't'"); s
misc/preparser.py:        sage: s, literals, state = strip_string_literals('s = "some'); s
misc/preparser.py:        sage: s, literals, state = strip_string_literals('thing" * 5', state); s
misc/preparser.py:        L, literals, quote_state = strip_string_literals(line, quote_state)
misc/preparser.py:        contents, literals, state = strip_string_literals(contents)
misc/preparser.py:    code, literals, state = strip_string_literals(code)
server/notebook/cell.py:from   sage.misc.preparser import strip_string_literals
server/notebook/cell.py:        s = strip_string_literals(self.input_text())[0]
```



---

Attachment

I added a patch which folds all of the above ones together.

+1 on Tom's changes.


---

Comment by mabshoff created at 2009-01-25 01:45:17

Merged trac_5079.patch in Sage 3.3.alpha2


---

Comment by mabshoff created at 2009-01-25 01:45:17

Resolution: fixed


---

Comment by robertwb created at 2009-02-15 09:00:25

Changing component from interfaces to user interface.
