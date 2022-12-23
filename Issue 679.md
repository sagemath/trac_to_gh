# Issue 679: print statistics about the number of failed doctests and exact nature of failures

archive/issues_000679.json:
```json
{
    "body": "Assignee: mhansen\n\nCurrently we print something like:\n\n```\nfailures:\n\n        sage -t  calculus/calculus.py\n        sage -t  functions/constants.py\n<SNIP>\n```\n\nIt would be nice if we get more precise failure reports, something like:\n\n```\nfailures:\n\n        sage -t  calculus/calculus.py: 1 out of 27 tests failed\n        sage -t  functions/constants.py: segfault\n        sage -t  server/notebook/twist.py: CTRL-C invoked\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/679\n\n",
    "created_at": "2007-09-17T05:46:44Z",
    "labels": [
        "doctest coverage",
        "major",
        "enhancement"
    ],
    "title": "print statistics about the number of failed doctests and exact nature of failures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/679",
    "user": "mabshoff"
}
```
Assignee: mhansen

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

archive/issue_comments_003518.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-20T11:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3518",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003519.json:
```json
{
    "body": "Changing assignee from mhansen to gfurnish.",
    "created_at": "2008-03-20T11:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3519",
    "user": "gfurnish"
}
```

Changing assignee from mhansen to gfurnish.



---

archive/issue_comments_003520.json:
```json
{
    "body": "This also fixes the segfault hang bug and the keyboard interrupt functionality of sage-ptest",
    "created_at": "2008-03-20T23:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3520",
    "user": "gfurnish"
}
```

This also fixes the segfault hang bug and the keyboard interrupt functionality of sage-ptest



---

archive/issue_comments_003521.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-20T23:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3521",
    "user": "gfurnish"
}
```

Attachment



---

archive/issue_comments_003522.json:
```json
{
    "body": "Patch looks good to me. Excellent work.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-21T00:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3522",
    "user": "mabshoff"
}
```

Patch looks good to me. Excellent work.

Cheers,

Michael



---

archive/issue_comments_003523.json:
```json
{
    "body": "Merged in Sage 2.11.alpha1",
    "created_at": "2008-03-21T00:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3523",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha1



---

archive/issue_comments_003524.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-21T00:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3524",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_003525.json:
```json
{
    "body": "After the patch some small trouble left:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-2.11.alpha1$ ./sage -tp 1 -long devel/sage/sage/plot/plot.py\nGlobal iterations: 1\nFile iterations: 1\nTeX files: 0\n\n----------------------------------------------------------------------\nsage -t -long devel/sage/sage/plot/plot.py\n**********************************************************************\nFile \"plot.py\", line 3506:\n    sage: plot(x^(1/3), (x,-1,1))\nExpected nothing\nGot:\n    WARNING: When plotting, failed to evaluate function at 100 points.\n    Last error message: 'negative number cannot be raised to a fractional power'\n    <BLANKLINE>\n**********************************************************************\n1 items had failures:\n   1 of  28 in __main__.example_111\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_plot.py\n\n         [71.8 s]\n\nThe following tests failed:\n\n        sage -t -long devel/sage/sage/plot/plot.py: 0 doctests failed\n----------------------------------------------------------------------\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-21T00:52:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3525",
    "user": "mabshoff"
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

archive/issue_comments_003526.json:
```json
{
    "body": "Attachment\n\nFix for plot.py bug",
    "created_at": "2008-03-21T00:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3526",
    "user": "gfurnish"
}
```

Attachment

Fix for plot.py bug



---

archive/issue_comments_003527.json:
```json
{
    "body": "Also merged trac_679n2.patch in Sage 2.11.alpha1",
    "created_at": "2008-03-21T01:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3527",
    "user": "mabshoff"
}
```

Also merged trac_679n2.patch in Sage 2.11.alpha1



---

archive/issue_comments_003528.json:
```json
{
    "body": "More trouble with pexpect exceptions:\n\n```\nsage -t -long devel/sage-main/sage/interfaces/rubik.py      **********************************************************************\nFile \"rubik.py\", line 243:\n    sage: DikSolver().solve(C.facets())\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[2]>\", line 1, in <module>\n        DikSolver().solve(C.facets())###line 243:\n    sage: DikSolver().solve(C.facets())\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/rubik.py\", line 253, in solve\n        child = pexpect.spawn(self.__cmd+\" -p\")\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/pexpect.py\", line 328, in __init__\n        raise ExceptionPexpect ('The command was not found or was not executable: %s.' % self.command)\n    ExceptionPexpect: The command was not found or was not executable: cube.\n**********************************************************************\nFile \"rubik.py\", line 246:\n    sage: DikSolver().solve(C.facets())\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[4]>\", line 1, in <module>\n        DikSolver().solve(C.facets())###line 246:\n    sage: DikSolver().solve(C.facets())\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/rubik.py\", line 253, in solve\n        child = pexpect.spawn(self.__cmd+\" -p\")\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/pexpect.py\", line 328, in __init__\n        raise ExceptionPexpect ('The command was not found or was not executable: %s.' % self.command)\n    ExceptionPexpect: The command was not found or was not executable: cube.\n**********************************************************************\nFile \"rubik.py\", line 249:\n    sage: DikSolver().solve(C.facets())\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[6]>\", line 1, in <module>\n        DikSolver().solve(C.facets())###line 249:\n    sage: DikSolver().solve(C.facets())\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/sage/interfaces/rubik.py\", line 253, in solve\n        child = pexpect.spawn(self.__cmd+\" -p\")\n      File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/site-packages/pexpect.py\", line 328, in __init__\n        raise ExceptionPexpect ('The command was not found or was not executable: %s.' % self.command)\n    ExceptionPexpect: The command was not found or was not executable: cube.\n**********************************************************************\n1 items had failures:\n   3 of   7 in __main__.example_5\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file .doctest_rubik.py\n         [59.8 s]\nexit code: 1024\n\n----------------------------------------------------------------------\nThe following tests failed:\n```\n",
    "created_at": "2008-03-21T12:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3528",
    "user": "mabshoff"
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

archive/issue_comments_003529.json:
```json
{
    "body": "Attachment\n\nThe patch trac_679-case-3.patch fixes the above issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-21T12:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/679",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/679#issuecomment-3529",
    "user": "mabshoff"
}
```

Attachment

The patch trac_679-case-3.patch fixes the above issue.

Cheers,

Michael
