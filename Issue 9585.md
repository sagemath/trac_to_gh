# Issue 9585: Interactive equation editor for the notebook

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-07-23 08:47:07

Assignee: jason, was

CC:  chapoton

We've have several requests and discussions ([on the mailing lists](http://groups.google.com/groups/search?q=equation+editor+group%3Asage-devel&btnG=Search&sitesearch=), etc.) for an interactive equation editor for Sage.

Some possibilities:

 * [D. Cervone's experimental editor](http://www.math.union.edu/~dpvc/talks/2006-12-08.IMA/editor.html) (but see [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/28c918d66a421573/3ed595b482b889b4#3ed595b482b889b4))


---

Comment by q10 created at 2010-07-23 20:21:09

Yes, I believe that an interactive equation editor will bring more non-programming math students to using SAGE, especially secondary school students, where programming is most likely not taught.


---

Comment by lftabera created at 2010-07-26 09:43:29

I have been told about the following page:

http://www.imathas.com/editordemo/demo.html

tinyMCE plugin to add a table of math symbols


---

Comment by jason created at 2010-08-12 04:41:18

Davide has told me that he's designed MathJax with an equation-editor application in mind, so it's probably going to be better to start with MathJax.  Especially since we will likely soon move to using MathJax instead of jsmath.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-08-19 12:33:40

Resolution: invalid
