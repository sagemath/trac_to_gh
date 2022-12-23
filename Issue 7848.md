# Issue 7848: Fix misleading stuff about HTML cells on sagenb

Issue created by migration from https://trac.sagemath.org/ticket/7848

Original creator: kcrisman

Original creation time: 2010-01-05 04:12:35

Assignee: was

CC:  timdumol

From sage-support:

```
The directive given in the help doesn't work: 
Shift click between cells to create a new HTML cell. Double click on 
existing HTML to edit it. 
Use $...$ and $$...$$ to include typeset math in the HTML block. 
```

There is no mention of the horizontal blue line.


---

Comment by mpatel created at 2010-01-05 05:37:54

Should we move the contents of `tutorial.py` to an HTML file?


---

Comment by timdumol created at 2010-01-05 12:56:13

I believe that some of it can be put into the documentation, under "The Notebook Interface", which is a bit lacking.


---

Attachment

Changes the tutorial help verbage regarding text (HTML) cells.  Also replaces all the <b> tags in the tutorial with <strong>


---

Comment by acleone created at 2010-01-19 07:23:31

Changing status from new to needs_review.


---

Comment by acleone created at 2010-01-19 07:23:31

trac_7848-misleading_HTML_cells.patch: changes verbage to:

```
Insert New Text Cell

Move the mouse between cells until a blue bar appears.
<strong>Shift-click</strong> on the blue bar to create a new text cell.
Double click on existing text to edit it.
Use $...$ and $$...$$ to include typeset math in the text block.
```



---

Comment by timdumol created at 2010-01-19 08:54:25

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-19 08:54:25

LGTM.


---

Comment by mpatel created at 2010-01-25 00:59:47

Resolution: fixed
