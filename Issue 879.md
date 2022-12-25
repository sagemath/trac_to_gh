# Issue 879: "sage -testall" should summarize all failures at the end of the run

archive/issues_000879.json:
```json
{
    "body": "Assignee: failure\n\nCC:  @garyfurnish @orlitzky\n\n\"sage -testall\" has at least three parts (DSage unit tests, documentation doctests, library doctests).  If some documentation doctests fail, you have to know to look in the middle of the -testall output to notice; the end of the output may well say that all tests passed (meaning all library doctests).\n\nIssue created by migration from https://trac.sagemath.org/ticket/879\n\n",
    "created_at": "2007-10-13T19:05:33Z",
    "labels": [
        "component: doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "\"sage -testall\" should summarize all failures at the end of the run",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/879",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: failure

CC:  @garyfurnish @orlitzky

"sage -testall" has at least three parts (DSage unit tests, documentation doctests, library doctests).  If some documentation doctests fail, you have to know to look in the middle of the -testall output to notice; the end of the output may well say that all tests passed (meaning all library doctests).

Issue created by migration from https://trac.sagemath.org/ticket/879





---

archive/issue_comments_005424.json:
```json
{
    "body": "The desired behaviour is what actually happens now, so this ticket can surely be closed.",
    "created_at": "2008-09-04T15:21:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/879#issuecomment-5424",
    "user": "https://github.com/JohnCremona"
}
```

The desired behaviour is what actually happens now, so this ticket can surely be closed.



---

archive/issue_comments_005425.json:
```json
{
    "body": "This is actually not solved yet in the regular sage-test, but in sage-ptest. We need to merge the two implementations or alternatively move the features to sage-test to close this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T17:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/879#issuecomment-5425",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is actually not solved yet in the regular sage-test, but in sage-ptest. We need to merge the two implementations or alternatively move the features to sage-test to close this ticket.

Cheers,

Michael



---

archive/issue_comments_005426.json:
```json
{
    "body": "FYI",
    "created_at": "2008-12-05T05:19:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/879#issuecomment-5426",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

FYI



---

archive/issue_comments_005427.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:23:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/879#issuecomment-5427",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_005428.json:
```json
{
    "body": "I think this ticket can be closed since it works now.",
    "created_at": "2011-08-23T21:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/879#issuecomment-5428",
    "user": "https://github.com/koffie"
}
```

I think this ticket can be closed since it works now.



---

archive/issue_comments_005429.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-23T21:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/879#issuecomment-5429",
    "user": "https://github.com/koffie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_005430.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-01T02:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/879#issuecomment-5430",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_005431.json:
```json
{
    "body": "Agreed, it's working now. I broke a test in the tutorial and some others in the main library are failing because of an upgraded Maxima spkg. They all get shown in the summary at the end:\n\n\n```\n$ sage -testall\n\n...\n\nThe following tests failed:\n\n\n\tsage -t  -force_lib \"devel/sage/doc/en/tutorial/tour_functions.rst\"\n\tsage -t  -force_lib \"devel/sage/sage/symbolic/expression.pyx\"\n\tsage -t  -force_lib \"devel/sage/sage/symbolic/integration/integral.py\"\n\tsage -t  -force_lib \"devel/sage/sage/interfaces/maxima_abstract.py\"\n\tsage -t  -force_lib \"devel/sage/sage/tests/cmdline.py\"\nTotal time for all tests: 6717.0 seconds\nPlease see /home/mjo/.sage//tmp/test.log for the complete log from this test.\n```\n",
    "created_at": "2011-12-01T02:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/879#issuecomment-5431",
    "user": "https://github.com/orlitzky"
}
```

Agreed, it's working now. I broke a test in the tutorial and some others in the main library are failing because of an upgraded Maxima spkg. They all get shown in the summary at the end:


```
$ sage -testall

...

The following tests failed:


	sage -t  -force_lib "devel/sage/doc/en/tutorial/tour_functions.rst"
	sage -t  -force_lib "devel/sage/sage/symbolic/expression.pyx"
	sage -t  -force_lib "devel/sage/sage/symbolic/integration/integral.py"
	sage -t  -force_lib "devel/sage/sage/interfaces/maxima_abstract.py"
	sage -t  -force_lib "devel/sage/sage/tests/cmdline.py"
Total time for all tests: 6717.0 seconds
Please see /home/mjo/.sage//tmp/test.log for the complete log from this test.
```




---

archive/issue_comments_005432.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2011-12-09T10:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/879",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/879#issuecomment-5432",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_events_000993.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-12-09T10:25:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/879",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/879#event-993"
}
```
