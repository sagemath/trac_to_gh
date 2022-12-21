# Issue 4923: convert sage.plot.* docstrings to Sphinx

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-01-01 22:55:12

Assignee: tba




---

Attachment


---

Comment by jhpalmieri created at 2009-01-07 22:20:30

I don't have the time or energy to review this fully right now, but I noticed one small issue: in line 61 in plot.py, "Type {?} after each primitive", change "{?}" to "?"


---

Attachment


---

Comment by jhpalmieri created at 2009-02-21 23:33:29

Looks good except for the following mostly minor changes:

plot.py, line 990: change 'suming' to 'summing'  (not your fault, an old typo)

line 1141: I think EXAMPLES is indented too far: check the page [http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/sage/plot/plot.html#sage.plot.plot.Graphics.show](http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/reference/sage/plot/plot.html#sage.plot.plot.Graphics.show)

line 1827: `'-' (dashed)` should say `'--' (dashed)`

line 2559: a dash "--" in some text got turned into a hyphen "-"

line 2913: change "increase" to "increases" (the subject of the sentence is "lowering", which is singular) (not your fault)


---

Comment by mabshoff created at 2009-02-24 19:09:28

Resolution: fixed


---

Comment by mabshoff created at 2009-02-24 19:09:28

Merged in Sage 3.4.alpha0.

Mike: please open a ticket for the review problems.

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-02-26 15:24:45

See #5376.


---

Comment by mabshoff created at 2009-02-26 16:19:06

Thanks John.

Cheers,

Michael
