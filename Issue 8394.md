# Issue 8394: plot/plot3d/tri_plot.py is at 0% coverage: get it to 100%

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2010-02-28 14:48:33

Assignee: was

CC:  wcauchois boothby

Keywords: doctests, coverage, plotting

The adaptive refinement code in tri_plot.py has almost no docstrings or tests.  However, there are a lot of helpful comments in the code, and the file is not very long, so it should be pretty easy to bring this up to 100% coverage.


---

Comment by mhampton created at 2010-04-25 21:35:12

adds basic doctests to tri_plot.py


---

Attachment


---

Comment by mhampton created at 2010-04-25 21:38:05

Changing status from new to needs_review.


---

Comment by mhampton created at 2010-04-25 21:39:30

The patch formally gets coverage of tri_plot.py from 0 to 100%.  Since I still don't completely understand this module, the tests and descriptions could be better but this is an improvement.


---

Attachment

The documentation is OK by me. I have just one trivial patch to add, which requires another pair of eyes other than mine. So if that reviewer patch gets a positive review, the whole ticket is good to go.



When the module `plot/plot3d/tri_plot.py` is added to the reference manual, building the reference manual with that newly added module would result in some warnings. But fixing that is another ticket.


---

Comment by boothby created at 2010-04-28 16:51:41

Looks great!  Thank you!


---

Comment by boothby created at 2010-04-28 16:51:41

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-29 05:28:31

Resolution: fixed
