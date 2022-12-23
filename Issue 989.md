# Issue 989: Stripping $ from documentation

Issue created by migration from https://trac.sagemath.org/ticket/989

Original creator: nbruin

Original creation time: 2007-10-25 01:14:24

Assignee: tba


```
sage: edit?
```

presently yields

```
 ...
          sage: import sage.misc.edit_module as m
          sage: m.set_edit_template("vi -c {line} {file}")
 ...
```

whereas the last line should read

```
         sage: m.set_edit_template("vi -c ${line} ${file}")
```

i.e., $ gets stripped from EXAMPLE text where it should not.


---

Comment by cwitty created at 2007-10-27 18:38:52

$ signs are stripped from docstrings in sage/misc/sagedoc.py, as part of an effort to convert LaTeX math markup to plain text.

Perhaps the right fix is to notice doctests, and disable these modifications for that part of the docstring.


---

Attachment

Changelog for the patch:

683,989: add 'nodetex' directive to docstrings: doesn't strip (la)tex code from docstrings.

The first line of a docstring is parsed as a comma-separated list of
directives (no whitespace in directives!).  For example:


```
r"""nodetex,notyetimplemented
...
"""
```


If 'nodetex' is one of the directives, then no (la)tex code is stripped from
the docstring.  The model was the 'nodoctest' directive already found at the
top of a file.


---

Comment by mabshoff created at 2007-11-06 21:35:27

applied to 2.8.12.rc0


---

Comment by mabshoff created at 2007-11-06 21:35:27

Resolution: fixed
