# Issue 7437: the optional gnuplotpy-1.7.p3 spkg doesn't build at all since with switched to python-2.6

archive/issues_007437.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nTraceback (most recent call last):\n  File \"setup.py\", line 17, in <module>\n    from __init__ import __version__\n  File \"/home/sage/sage/spkg/build/gnuplotpy-1.7.p3/src/__init__.py\", line 167, in <module>\n    from PlotItems import PlotItem, Func, File, Data, GridData\n  File \"/home/sage/sage/spkg/build/gnuplotpy-1.7.p3/src/PlotItems.py\", line 88\n    'with' : lambda self, with: self.set_string_option(\n                             ^\nSyntaxError: invalid syntax\nError installing gnuplotpy.\n\nreal    0m0.159s\nuser    0m0.024s\nsys     0m0.124s\nsage: An error occurred while installing gnuplotpy-1.7.p3\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7437\n\n",
    "created_at": "2009-11-12T05:04:19Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "the optional gnuplotpy-1.7.p3 spkg doesn't build at all since with switched to python-2.6",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7437",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd


```
Traceback (most recent call last):
  File "setup.py", line 17, in <module>
    from __init__ import __version__
  File "/home/sage/sage/spkg/build/gnuplotpy-1.7.p3/src/__init__.py", line 167, in <module>
    from PlotItems import PlotItem, Func, File, Data, GridData
  File "/home/sage/sage/spkg/build/gnuplotpy-1.7.p3/src/PlotItems.py", line 88
    'with' : lambda self, with: self.set_string_option(
                             ^
SyntaxError: invalid syntax
Error installing gnuplotpy.

real    0m0.159s
user    0m0.024s
sys     0m0.124s
sage: An error occurred while installing gnuplotpy-1.7.p3
```


Issue created by migration from https://trac.sagemath.org/ticket/7437





---

archive/issue_comments_062468.json:
```json
{
    "body": "\n```\nmhansen:\nThere is a new upstream release for that.\n[9:07pm] mhansen:\nI'm not sure if it fixes that issue though.\nmhansen:\nYep, it should (looking at SVN).\n```\n",
    "created_at": "2009-11-12T05:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7437#issuecomment-62468",
    "user": "https://github.com/williamstein"
}
```


```
mhansen:
There is a new upstream release for that.
[9:07pm] mhansen:
I'm not sure if it fixes that issue though.
mhansen:
Yep, it should (looking at SVN).
```




---

archive/issue_events_017619.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7437",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7437#event-17619"
}
```



---

archive/issue_events_017620.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7437",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7437#event-17620"
}
```



---

archive/issue_events_017621.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7437",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7437#event-17621"
}
```



---

archive/issue_events_017622.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7437",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7437#event-17622"
}
```



---

archive/issue_events_017623.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7437",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7437#event-17623"
}
```



---

archive/issue_events_017624.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7437",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7437#event-17624"
}
```



---

archive/issue_events_017625.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7437",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7437#event-17625"
}
```



---

archive/issue_comments_062469.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-13T22:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7437#issuecomment-62469",
    "user": "https://github.com/a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_events_017626.json:
```json
{
    "actor": "https://github.com/a-andre",
    "created_at": "2014-08-13T22:28:38Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7437",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7437#event-17626"
}
```



---

archive/issue_events_017627.json:
```json
{
    "actor": "https://github.com/a-andre",
    "created_at": "2014-08-13T22:28:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7437",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7437#event-17627"
}
```



---

archive/issue_comments_062470.json:
```json
{
    "body": "Works for me with Python 2.7.8 and current optional gnuplotpy-1.8 (on linux).",
    "created_at": "2014-08-13T22:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7437#issuecomment-62470",
    "user": "https://github.com/a-andre"
}
```

Works for me with Python 2.7.8 and current optional gnuplotpy-1.8 (on linux).



---

archive/issue_comments_062471.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2014-10-25T21:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7437#issuecomment-62471",
    "user": "https://github.com/vbraun"
}
```

Resolution: worksforme



---

archive/issue_events_017628.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-10-25T21:44:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7437",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7437#event-17628"
}
```
