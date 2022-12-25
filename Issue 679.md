# Issue 679: [with patch, positive review] print statistics about the number of failed doctests and exact nature of failures

archive/issues_000679.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nCurrently we print something like:\n\n```\nfailures:\n\n        sage -t  calculus/calculus.py\n        sage -t  functions/constants.py\n<SNIP>\n```\nIt would be nice if we get more precise failure reports, something like:\n\n```\nfailures:\n\n        sage -t  calculus/calculus.py: 1 out of 27 tests failed\n        sage -t  functions/constants.py: segfault\n        sage -t  server/notebook/twist.py: CTRL-C invoked\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/679\n\n",
    "closed_at": "2008-03-21T00:20:50Z",
    "created_at": "2007-09-17T05:46:44Z",
    "labels": [
        "component: doctest coverage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, positive review] print statistics about the number of failed doctests and exact nature of failures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/679",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @garyfurnish

Currently we print something like:

```
failures:

        sage -t  calculus/calculus.py
        sage -t  functions/constants.py
<SNIP>
```
It would be nice if we get more precise failure reports, something like:

```
failures:

        sage -t  calculus/calculus.py: 1 out of 27 tests failed
        sage -t  functions/constants.py: segfault
        sage -t  server/notebook/twist.py: CTRL-C invoked
```

Issue created by migration from https://trac.sagemath.org/ticket/679





---

archive/issue_events_001810.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-24T09:12:22Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "milestone": "sage-2.9.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/679#event-1810"
}
```



---

archive/issue_comments_003505.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-20T11:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3505",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003506.json:
```json
{
    "body": "Changing assignee from @mwhansen to @garyfurnish.",
    "created_at": "2008-03-20T11:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3506",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from @mwhansen to @garyfurnish.



---

archive/issue_comments_003507.json:
```json
{
    "body": "This also fixes the segfault hang bug and the keyboard interrupt functionality of sage-ptest",
    "created_at": "2008-03-20T23:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3507",
    "user": "https://github.com/garyfurnish"
}
```

This also fixes the segfault hang bug and the keyboard interrupt functionality of sage-ptest



---

archive/issue_events_001811.json:
```json
{
    "actor": "https://github.com/garyfurnish",
    "created_at": "2008-03-20T23:02:02Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "milestone": "sage-2.9.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/679#event-1811"
}
```



---

archive/issue_events_001812.json:
```json
{
    "actor": "https://github.com/garyfurnish",
    "created_at": "2008-03-20T23:02:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/679#event-1812"
}
```



---

archive/issue_comments_003508.json:
```json
{
    "body": "Attachment [trac_679.patch](tarball://root/attachments/some-uuid/ticket679/trac_679.patch) by @garyfurnish created at 2008-03-20 23:05:48",
    "created_at": "2008-03-20T23:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3508",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_679.patch](tarball://root/attachments/some-uuid/ticket679/trac_679.patch) by @garyfurnish created at 2008-03-20 23:05:48



---

archive/issue_comments_003509.json:
```json
{
    "body": "Patch looks good to me. Excellent work.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-21T00:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3509",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. Excellent work.

Cheers,

Michael



---

archive/issue_comments_003510.json:
```json
{
    "body": "Merged in Sage 2.11.alpha1",
    "created_at": "2008-03-21T00:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3510",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha1



---

archive/issue_events_001813.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-21T00:20:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/679#event-1813"
}
```



---

archive/issue_comments_003511.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-21T00:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3511",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_003512.json:
```json
{
    "body": "After the patch some small trouble left:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha1$ ./sage -tp 1 -long devel/sage/sage/plot/plot.py\nGlobal iterations: 1\nFile iterations: 1\nTeX files: 0\n\n----------------------------------------------------------------------\nsage -t -long devel/sage/sage/plot/plot.py\n**********************************************************************\nFile \"plot.py\", line 3506:\n    sage: plot(x^(1/3), (x,-1,1))\nExpected nothing\nGot:\n    WARNING: When plotting, failed to evaluate function at 100 points.\n    Last error message: 'negative number cannot be raised to a fractional power'\n    <BLANKLINE>\n**********************************************************************\n1 items had failures:\n   1 of  28 in __main__.example_111\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_plot.py\n\n         [71.8 s]\n\nThe following tests failed:\n\n        sage -t -long devel/sage/sage/plot/plot.py: 0 doctests failed\n----------------------------------------------------------------------\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-03-21T00:52:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3512",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

After the patch some small trouble left:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha1$ ./sage -tp 1 -long devel/sage/sage/plot/plot.py
Global iterations: 1
File iterations: 1
TeX files: 0

----------------------------------------------------------------------
sage -t -long devel/sage/sage/plot/plot.py
**********************************************************************
File "plot.py", line 3506:
    sage: plot(x^(1/3), (x,-1,1))
Expected nothing
Got:
    WARNING: When plotting, failed to evaluate function at 100 points.
    Last error message: 'negative number cannot be raised to a fractional power'
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of  28 in __main__.example_111
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_plot.py

         [71.8 s]

The following tests failed:

        sage -t -long devel/sage/sage/plot/plot.py: 0 doctests failed
----------------------------------------------------------------------
```

Cheers,

Michael



---

archive/issue_comments_003513.json:
```json
{
    "body": "Attachment [trac_679n2.patch](tarball://root/attachments/some-uuid/ticket679/trac_679n2.patch) by @garyfurnish created at 2008-03-21 00:55:11\n\nFix for plot.py bug",
    "created_at": "2008-03-21T00:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3513",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_679n2.patch](tarball://root/attachments/some-uuid/ticket679/trac_679n2.patch) by @garyfurnish created at 2008-03-21 00:55:11

Fix for plot.py bug



---

archive/issue_comments_003514.json:
```json
{
    "body": "Also merged trac_679n2.patch in Sage 2.11.alpha1",
    "created_at": "2008-03-21T01:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3514",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Also merged trac_679n2.patch in Sage 2.11.alpha1



---

archive/issue_comments_003515.json:
```json
{
    "body": "More trouble with pexpect exceptions:\n\n```\nsage -t -long devel/sage-main/sage/interfaces/rubik.py      **********************************************************************\nFile \"rubik.py\", line 243:\n    sage: DikSolver().solve(C.facets())\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[2]>\", line 1, in <module>\n        DikSolver().solve(C.facets())###line 243:\n    sage: DikSolver().solve(C.facets())\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/rubik.py\", line 253, in solve\n        child = pexpect.spawn(self.__cmd+\" -p\")\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/pexpect.py\", line 328, in __init__\n        raise ExceptionPexpect ('The command was not found or was not executable: %s.' % self.command)\n    ExceptionPexpect: The command was not found or was not executable: cube.\n**********************************************************************\nFile \"rubik.py\", line 246:\n    sage: DikSolver().solve(C.facets())\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[4]>\", line 1, in <module>\n        DikSolver().solve(C.facets())###line 246:\n    sage: DikSolver().solve(C.facets())\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/rubik.py\", line 253, in solve\n        child = pexpect.spawn(self.__cmd+\" -p\")\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/pexpect.py\", line 328, in __init__\n        raise ExceptionPexpect ('The command was not found or was not executable: %s.' % self.command)\n    ExceptionPexpect: The command was not found or was not executable: cube.\n**********************************************************************\nFile \"rubik.py\", line 249:\n    sage: DikSolver().solve(C.facets())\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[6]>\", line 1, in <module>\n        DikSolver().solve(C.facets())###line 249:\n    sage: DikSolver().solve(C.facets())\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/rubik.py\", line 253, in solve\n        child = pexpect.spawn(self.__cmd+\" -p\")\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/pexpect.py\", line 328, in __init__\n        raise ExceptionPexpect ('The command was not found or was not executable: %s.' % self.command)\n    ExceptionPexpect: The command was not found or was not executable: cube.\n**********************************************************************\n1 items had failures:\n   3 of   7 in __main__.example_5\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file .doctest_rubik.py\n         [59.8 s]\nexit code: 1024\n\n----------------------------------------------------------------------\nThe following tests failed:\n```",
    "created_at": "2008-03-21T12:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3515",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

More trouble with pexpect exceptions:

```
sage -t -long devel/sage-main/sage/interfaces/rubik.py      **********************************************************************
File "rubik.py", line 243:
    sage: DikSolver().solve(C.facets())
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[2]>", line 1, in <module>
        DikSolver().solve(C.facets())###line 243:
    sage: DikSolver().solve(C.facets())
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/rubik.py", line 253, in solve
        child = pexpect.spawn(self.__cmd+" -p")
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/pexpect.py", line 328, in __init__
        raise ExceptionPexpect ('The command was not found or was not executable: %s.' % self.command)
    ExceptionPexpect: The command was not found or was not executable: cube.
**********************************************************************
File "rubik.py", line 246:
    sage: DikSolver().solve(C.facets())
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[4]>", line 1, in <module>
        DikSolver().solve(C.facets())###line 246:
    sage: DikSolver().solve(C.facets())
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/rubik.py", line 253, in solve
        child = pexpect.spawn(self.__cmd+" -p")
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/pexpect.py", line 328, in __init__
        raise ExceptionPexpect ('The command was not found or was not executable: %s.' % self.command)
    ExceptionPexpect: The command was not found or was not executable: cube.
**********************************************************************
File "rubik.py", line 249:
    sage: DikSolver().solve(C.facets())
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[6]>", line 1, in <module>
        DikSolver().solve(C.facets())###line 249:
    sage: DikSolver().solve(C.facets())
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/rubik.py", line 253, in solve
        child = pexpect.spawn(self.__cmd+" -p")
      File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/pexpect.py", line 328, in __init__
        raise ExceptionPexpect ('The command was not found or was not executable: %s.' % self.command)
    ExceptionPexpect: The command was not found or was not executable: cube.
**********************************************************************
1 items had failures:
   3 of   7 in __main__.example_5
***Test Failed*** 3 failures.
For whitespace errors, see the file .doctest_rubik.py
         [59.8 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:
```



---

archive/issue_comments_003516.json:
```json
{
    "body": "Attachment [trac_679-case-3.patch](tarball://root/attachments/some-uuid/ticket679/trac_679-case-3.patch) by mabshoff created at 2008-03-21 12:34:21\n\nThe patch trac_679-case-3.patch fixes the above issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-21T12:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3516",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_679-case-3.patch](tarball://root/attachments/some-uuid/ticket679/trac_679-case-3.patch) by mabshoff created at 2008-03-21 12:34:21

The patch trac_679-case-3.patch fixes the above issue.

Cheers,

Michael
