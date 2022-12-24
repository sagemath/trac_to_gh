# Issue 7390: Generate a HTML report for SageNB tests

archive/issues_007390.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein @TimDumol\n\nIt would be useful to have a HTML report summarizing the results of Sage Notebook tests, including the output and traceback, if any, of each test.\n\nWe can begin with the notebook's functional test suites (cf. #7343), but we could add doctests, eventually.  And with a backend server, we might select, run, and monitor tests remotely.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7390\n\n",
    "created_at": "2009-11-04T20:31:29Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Generate a HTML report for SageNB tests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7390",
    "user": "@qed777"
}
```
Assignee: boothby

CC:  @williamstein @TimDumol

It would be useful to have a HTML report summarizing the results of Sage Notebook tests, including the output and traceback, if any, of each test.

We can begin with the notebook's functional test suites (cf. #7343), but we could add doctests, eventually.  And with a backend server, we might select, run, and monitor tests remotely.

Issue created by migration from https://trac.sagemath.org/ticket/7390





---

archive/issue_comments_062149.json:
```json
{
    "body": "Attachment [trac_7390-sagenb_test_report_A.patch](tarball://root/attachments/some-uuid/ticket7390/trac_7390-sagenb_test_report_A.patch) by @qed777 created at 2009-11-06 14:32:18\n\nHTML test report.  Part A.  Apply to sagenb repo.",
    "created_at": "2009-11-06T14:32:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62149",
    "user": "@qed777"
}
```

Attachment [trac_7390-sagenb_test_report_A.patch](tarball://root/attachments/some-uuid/ticket7390/trac_7390-sagenb_test_report_A.patch) by @qed777 created at 2009-11-06 14:32:18

HTML test report.  Part A.  Apply to sagenb repo.



---

archive/issue_comments_062150.json:
```json
{
    "body": "Attachment [trac_7390-sagenb_test_report_B.patch](tarball://root/attachments/some-uuid/ticket7390/trac_7390-sagenb_test_report_B.patch) by @qed777 created at 2009-11-06 14:36:48\n\nHTML test report.  Part B.  Apply to sagenb repo after part A.",
    "created_at": "2009-11-06T14:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62150",
    "user": "@qed777"
}
```

Attachment [trac_7390-sagenb_test_report_B.patch](tarball://root/attachments/some-uuid/ticket7390/trac_7390-sagenb_test_report_B.patch) by @qed777 created at 2009-11-06 14:36:48

HTML test report.  Part B.  Apply to sagenb repo after part A.



---

archive/issue_comments_062151.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-06T14:59:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62151",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062152.json:
```json
{
    "body": "Note: The patches depend on #7343.  Please apply parts A *and* B, in order.  To test the test report generator, try\n\n```python\nsage: from sagenb.testing.run_tests import run_and_report; run_and_report()\n```\n\nThis should run the notebook's Selenium test suite, generate and write a self-contained `report.html`, and open the report in `SAGE_BROWSER`.\n\nRemarks:\n\n* Part A adds [HTMLTestRunner](http://tungwaiyip.info/software/HTMLTestRunner.html).\n* Part B makes significant changes to `HTMLTestRunner.py` and sets up the test runner for sagenb.\n* The runner captures all output, e.g., we can display information from passing tests, too.\n\nTo do, but not necessarily in this ticket:\n\n* Stabilize the results table's column widths, especially when toggling tracebacks.\n* Support multiple results tables.\n* Use the runner to display doctest results.\n* Use a backend server to select, run, and monitor live tests.",
    "created_at": "2009-11-06T14:59:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62152",
    "user": "@qed777"
}
```

Note: The patches depend on #7343.  Please apply parts A *and* B, in order.  To test the test report generator, try

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

archive/issue_comments_062153.json:
```json
{
    "body": "Mistake: `run_and_report`'s docstring should say `open_viewer` defaults to `True`.",
    "created_at": "2009-11-08T09:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62153",
    "user": "@qed777"
}
```

Mistake: `run_and_report`'s docstring should say `open_viewer` defaults to `True`.



---

archive/issue_comments_062154.json:
```json
{
    "body": "Doctesting *may* be straightforward.  Given `foo.py`, `sage-doctest` preparses its triple-quoted blocks and writes them as docstrings of `example_*` functions in `.doctest_foo.py`.  This file calls on itself a subclass of `doctest.DocTestRunner`.  Since Python's [doctest](http://docs.python.org/library/doctest.html) module can also generate [unittests](http://docs.python.org/library/unittest.html), we can \"replace\" the end of `.doctest_foo.py` with, e.g.,\n\n```\nif __name__ ==  '__main__':\n    from sagenb.testing.run_tests import run_and_report\n    import doctest\n    run_and_report(doctest.DocTestSuite())\n    sys.exit(0)\n```\n\nAlthough the test names `example_*` are not informative, `sage -python .doctest_foo_mod.py` runs the tests and makes a report!",
    "created_at": "2009-11-08T10:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62154",
    "user": "@qed777"
}
```

Doctesting *may* be straightforward.  Given `foo.py`, `sage-doctest` preparses its triple-quoted blocks and writes them as docstrings of `example_*` functions in `.doctest_foo.py`.  This file calls on itself a subclass of `doctest.DocTestRunner`.  Since Python's [doctest](http://docs.python.org/library/doctest.html) module can also generate [unittests](http://docs.python.org/library/unittest.html), we can "replace" the end of `.doctest_foo.py` with, e.g.,

```
if __name__ ==  '__main__':
    from sagenb.testing.run_tests import run_and_report
    import doctest
    run_and_report(doctest.DocTestSuite())
    sys.exit(0)
```

Although the test names `example_*` are not informative, `sage -python .doctest_foo_mod.py` runs the tests and makes a report!



---

archive/issue_comments_062155.json:
```json
{
    "body": "HTML test report. Part B **Version 2**. Apply to sagenb repo after part A.",
    "created_at": "2009-11-10T06:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62155",
    "user": "@qed777"
}
```

HTML test report. Part B **Version 2**. Apply to sagenb repo after part A.



---

archive/issue_comments_062156.json:
```json
{
    "body": "Attachment [trac_7390-sagenb_test_report_B_v2.patch](tarball://root/attachments/some-uuid/ticket7390/trac_7390-sagenb_test_report_B_v2.patch) by @qed777 created at 2009-11-10 07:01:41\n\nVersion 2 (of part B):\n\n* Solves the table width problem for Cr3, FF3.5, IE8, O10, S4 on Windows XP and Cr4, FF3.5, O10 on Linux.\n* Works around a jQuery / IE8 toggle bug.\n* Fixes `run_and_report`'s docstring.",
    "created_at": "2009-11-10T07:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62156",
    "user": "@qed777"
}
```

Attachment [trac_7390-sagenb_test_report_B_v2.patch](tarball://root/attachments/some-uuid/ticket7390/trac_7390-sagenb_test_report_B_v2.patch) by @qed777 created at 2009-11-10 07:01:41

Version 2 (of part B):

* Solves the table width problem for Cr3, FF3.5, IE8, O10, S4 on Windows XP and Cr4, FF3.5, O10 on Linux.
* Works around a jQuery / IE8 toggle bug.
* Fixes `run_and_report`'s docstring.



---

archive/issue_comments_062157.json:
```json
{
    "body": "Feel free to suggest improvements to the form and function of the report!",
    "created_at": "2009-11-12T02:20:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62157",
    "user": "@qed777"
}
```

Feel free to suggest improvements to the form and function of the report!



---

archive/issue_comments_062158.json:
```json
{
    "body": "There's sample report at\n\n* http://sage.math.washington.edu/home/mpatel/trac/7390/report.html",
    "created_at": "2009-11-12T02:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62158",
    "user": "@qed777"
}
```

There's sample report at

* http://sage.math.washington.edu/home/mpatel/trac/7390/report.html



---

archive/issue_comments_062159.json:
```json
{
    "body": "Replying to [comment:7 mpatel]:\n> There's sample report at\n> \n>  * http://sage.math.washington.edu/home/mpatel/trac/7390/report.html\n\nIf you don't mind, I can try restyling the tests. The colors are a bit jarring, in my opinion.",
    "created_at": "2009-11-15T07:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62159",
    "user": "@TimDumol"
}
```

Replying to [comment:7 mpatel]:
> There's sample report at
> 
>  * http://sage.math.washington.edu/home/mpatel/trac/7390/report.html

If you don't mind, I can try restyling the tests. The colors are a bit jarring, in my opinion.



---

archive/issue_comments_062160.json:
```json
{
    "body": "Feel free.",
    "created_at": "2009-11-15T07:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62160",
    "user": "@qed777"
}
```

Feel free.



---

archive/issue_comments_062161.json:
```json
{
    "body": "Attachment [trac_7390-sagenb_test_report_referee.patch](tarball://root/attachments/some-uuid/ticket7390/trac_7390-sagenb_test_report_referee.patch) by @TimDumol created at 2009-11-15 08:50:08\n\nRemoves unicode characters from the documentation. Restyles color scheme to a lighter layout.",
    "created_at": "2009-11-15T08:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62161",
    "user": "@TimDumol"
}
```

Attachment [trac_7390-sagenb_test_report_referee.patch](tarball://root/attachments/some-uuid/ticket7390/trac_7390-sagenb_test_report_referee.patch) by @TimDumol created at 2009-11-15 08:50:08

Removes unicode characters from the documentation. Restyles color scheme to a lighter layout.



---

archive/issue_comments_062162.json:
```json
{
    "body": "This patch removes unicode characters from the documentation that would otherwise require magic comments (feel free to do so instead). The color scheme has been inverted to a lighter layout, with colors taken from the color palette on [Wikipedia](http://en.wikipedia.org/wiki/List_of_colors).\n\nThings look great. The only thing I might want added are timings for each individual test, but that can go in another patch. Positive review. All that's needed now is for someone to review the referee patch.",
    "created_at": "2009-11-15T08:54:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62162",
    "user": "@TimDumol"
}
```

This patch removes unicode characters from the documentation that would otherwise require magic comments (feel free to do so instead). The color scheme has been inverted to a lighter layout, with colors taken from the color palette on [Wikipedia](http://en.wikipedia.org/wiki/List_of_colors).

Things look great. The only thing I might want added are timings for each individual test, but that can go in another patch. Positive review. All that's needed now is for someone to review the referee patch.



---

archive/issue_comments_062163.json:
```json
{
    "body": "Attachment [trac_7390-sagenb_test_report_referee_v2.patch](tarball://root/attachments/some-uuid/ticket7390/trac_7390-sagenb_test_report_referee_v2.patch) by @qed777 created at 2009-11-15 09:11:28\n\nUpdate TODO list.  **Version 2** of referee patch.",
    "created_at": "2009-11-15T09:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62163",
    "user": "@qed777"
}
```

Attachment [trac_7390-sagenb_test_report_referee_v2.patch](tarball://root/attachments/some-uuid/ticket7390/trac_7390-sagenb_test_report_referee_v2.patch) by @qed777 created at 2009-11-15 09:11:28

Update TODO list.  **Version 2** of referee patch.



---

archive/issue_comments_062164.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-15T09:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62164",
    "user": "@qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062165.json:
```json
{
    "body": "Looks good to me.  I'll change this status to \"positive review.\"",
    "created_at": "2009-11-15T09:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62165",
    "user": "@qed777"
}
```

Looks good to me.  I'll change this status to "positive review."



---

archive/issue_comments_062166.json:
```json
{
    "body": "merged into sagenb for sage-4.3",
    "created_at": "2009-12-08T07:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62166",
    "user": "@williamstein"
}
```

merged into sagenb for sage-4.3



---

archive/issue_comments_062167.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-08T07:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7390#issuecomment-62167",
    "user": "@williamstein"
}
```

Resolution: fixed
