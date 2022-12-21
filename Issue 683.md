# Issue 683: bug in "latex?" in the notebook

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-17 21:52:21

Assignee: boothby


```
     --  The response to `latex?' seems to be out of date.

            %latex
            The equation y^2 = x^3 + x defines an elliptic curve.
            We have 2006 = SAGE{factor(2006)}.

    I thought it was a great credit to SAGE that when I edited the sample input
    in what seemed the obvious way, enclosing the math in $$ and changing SAGE
    to \sage, that it worked as expected.

```





Ah, you've found a bug.  What happens is that all SAGE documentation
is de-texed before displaying in the notebook (in plain text format).  Unfortunately
this detexing makes the documentation for latex appear completely
wrong!  

The solution is probably to come up with a notation to tell SAGE not
to do the detexing. 


---

Attachment


---

Comment by ncalexan created at 2007-11-04 07:33:09

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

Comment by mabshoff created at 2007-11-06 21:35:43

applied to 2.8.12.rc0


---

Comment by mabshoff created at 2007-11-06 21:35:43

Resolution: fixed
