# Issue 7390: Generate a HTML report for SageNB tests

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-11-04 20:31:29

Assignee: boothby

CC:  was timdumol

It would be useful to have a HTML report summarizing the results of Sage Notebook tests, including the output and traceback, if any, of each test.

We can begin with the notebook's functional test suites (cf. #7343), but we could add doctests, eventually.  And with a backend server, we might select, run, and monitor tests remotely.


---

Attachment

HTML test report.  Part A.  Apply to sagenb repo.


---

Attachment

HTML test report.  Part B.  Apply to sagenb repo after part A.


---

Comment by mpatel created at 2009-11-06 14:59:09

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-11-06 14:59:09

Note: The patches depend on #7343.  Please apply parts A _and_ B, in order.  To test the test report generator, try

```python
sage: from sagenb.testing.run_tests import run_and_report; run_and_report()
```

This should run the notebook's Selenium test suite, generate and write a self-contained `report.html`, and open the report in `SAGE_BROWSER`.

Remarks:

 * Part A adds [HTMLTestRunner](http://tungwaiyip.info/software/HTMLTestRunner.html).
 * Part B makes significant changes to `HTMLTestRunner.py` and sets up the test runner for sagenb.
 * The runner captures all output, e.g., we can display information from passing tests, too.

To do, but not necessarily in this ticket:

  * Stabilize the results table's column widths, especially when toggling tracebacks.
  * Support multiple results tables.
  * Use the runner to display doctest results.
  * Use a backend server to select, run, and monitor live tests.


---

Comment by mpatel created at 2009-11-08 09:39:46

Mistake: `run_and_report`'s docstring should say `open_viewer` defaults to `True`.


---

Comment by mpatel created at 2009-11-08 10:33:05

Doctesting _may_ be straightforward.  Given `foo.py`, `sage-doctest` preparses its triple-quoted blocks and writes them as docstrings of `example_*` functions in `.doctest_foo.py`.  This file calls on itself a subclass of `doctest.DocTestRunner`.  Since Python's [doctest](http://docs.python.org/library/doctest.html) module can also generate [unittests](http://docs.python.org/library/unittest.html), we can "replace" the end of `.doctest_foo.py` with, e.g.,

```
if __name__ ==  '__main__':
    from sagenb.testing.run_tests import run_and_report
    import doctest
    run_and_report(doctest.DocTestSuite())
    sys.exit(0)
```

Although the test names `example_*` are not informative, `sage -python .doctest_foo_mod.py` runs the tests and makes a report!


---

Comment by mpatel created at 2009-11-10 06:54:01

HTML test report. Part B *Version 2*. Apply to sagenb repo after part A.


---

Attachment

Version 2 (of part B):

 * Solves the table width problem for Cr3, FF3.5, IE8, O10, S4 on Windows XP and Cr4, FF3.5, O10 on Linux.
 * Works around a jQuery / IE8 toggle bug.
 * Fixes `run_and_report`'s docstring.


---

Comment by mpatel created at 2009-11-12 02:20:00

Feel free to suggest improvements to the form and function of the report!


---

Comment by mpatel created at 2009-11-12 02:29:48

There's sample report at

 * http://sage.math.washington.edu/home/mpatel/trac/7390/report.html


---

Comment by timdumol created at 2009-11-15 07:38:48

Replying to [comment:7 mpatel]:
> There's sample report at
> 
>  * http://sage.math.washington.edu/home/mpatel/trac/7390/report.html

If you don't mind, I can try restyling the tests. The colors are a bit jarring, in my opinion.


---

Comment by mpatel created at 2009-11-15 07:53:23

Feel free.


---

Attachment

Removes unicode characters from the documentation. Restyles color scheme to a lighter layout.


---

Comment by timdumol created at 2009-11-15 08:54:22

This patch removes unicode characters from the documentation that would otherwise require magic comments (feel free to do so instead). The color scheme has been inverted to a lighter layout, with colors taken from the color palette on [Wikipedia](http://en.wikipedia.org/wiki/List_of_colors).

Things look great. The only thing I might want added are timings for each individual test, but that can go in another patch. Positive review. All that's needed now is for someone to review the referee patch.


---

Attachment

Update TODO list.  *Version 2* of referee patch.


---

Comment by mpatel created at 2009-11-15 09:12:34

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2009-11-15 09:12:34

Looks good to me.  I'll change this status to "positive review."


---

Comment by was created at 2009-12-08 07:31:11

merged into sagenb for sage-4.3


---

Comment by was created at 2009-12-08 07:31:11

Resolution: fixed
