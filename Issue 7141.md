# Issue 7141: `math_parse` parses $'s in <script> tags

Issue created by migration from https://trac.sagemath.org/ticket/7141

Original creator: timdumol

Original creation time: 2009-10-06 15:02:03

Assignee: boothby

Keywords: sagenb notebook jQuery

`sagenb.notebook.jsmath.math_parse` (and the source, `sage.misc.html.math_parse`) parse $'s in <script> tags, which breaks jQuery code.


---

Attachment

Fixes math_parse in sagenb.notebook.jsmath to skip <script> tags. Apply to sagenb repo.


---

Comment by was created at 2009-10-07 04:48:53

Very nice!

And I've applied it and pushed it to the official sagenb branch.


---

Comment by was created at 2009-10-07 04:48:53

Resolution: fixed
