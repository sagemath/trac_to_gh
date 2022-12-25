# Issue 1584: calculus.py doctest failure on Fermat

archive/issues_001584.json:
```json
{
    "body": "Assignee: @williamstein\n\nFERMAT -- OSX 10.4 PowerPC\n\n\n```\nsage -t  devel/sage-main/sage/calculus/calculus.py\n**********************************************************************\nFile \"calculus.py\", line 2005:\n    sage: f = f.nintegral(x,0,1,1e-14)\nExpected:\n    Traceback (most recent call last):\n    ...\n    ValueError: Maxima (via quadpack) cannot compute the integral to\nthat precision\nGot:\n    Traceback (most recent call last):\n      File \"/Users/was/build/sage-2.9.1.alpha2/local/lib/python2.5/doctest.py\",\nline 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_40[1]>\", line 1, in <module>\n        f = f.nintegral(x,Integer(0),Integer(1),RealNumber('1e-14'))###line\n2005:\n    sage: f = f.nintegral(x,0,1,1e-14)\n      File \"/Users/was/build/sage-2.9.1.alpha2/local/lib/python2.5/site-packages/sage/calculus/calculus.py\",\nline 2068, in nintegral\n        raise TypeError, err\n    TypeError: Error executing code in Maxima\n    CODE:\n        sage356 : quad_qags(sage6,sage6,sage352,sage353,sage354,sage355)$\n    Maxima ERROR:\n        ^M\n    Maxima encountered a Lisp error:^M\n    ^M\n     ^M\n    WRITE-CHAR on #<CLOSED OUTPUT BUFFERED FILE-STREAM CHARACTER\n#P\"/dev/fd/1\"> is illegal^M\n    ^M\n    Automatically continuing.^M\n    To reenable the Lisp debugger set *debugger-hook* to nil.^M\n    <BLANKLINE>\n**********************************************************************\n1 items had failures:\n   1 of  14 in __main__.example_40\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_calculus.py\n         [61.0 s]\n```\n\n----- This is related to Mike Hansen's precision detection patch -- it\ndoesn't work right on\nOSX PPC, evidently. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1584\n\n",
    "created_at": "2007-12-21T20:38:26Z",
    "labels": [
        "component: calculus",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "calculus.py doctest failure on Fermat",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1584",
    "user": "https://github.com/rlmill"
}
```
Assignee: @williamstein

FERMAT -- OSX 10.4 PowerPC


```
sage -t  devel/sage-main/sage/calculus/calculus.py
**********************************************************************
File "calculus.py", line 2005:
    sage: f = f.nintegral(x,0,1,1e-14)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: Maxima (via quadpack) cannot compute the integral to
that precision
Got:
    Traceback (most recent call last):
      File "/Users/was/build/sage-2.9.1.alpha2/local/lib/python2.5/doctest.py",
line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_40[1]>", line 1, in <module>
        f = f.nintegral(x,Integer(0),Integer(1),RealNumber('1e-14'))###line
2005:
    sage: f = f.nintegral(x,0,1,1e-14)
      File "/Users/was/build/sage-2.9.1.alpha2/local/lib/python2.5/site-packages/sage/calculus/calculus.py",
line 2068, in nintegral
        raise TypeError, err
    TypeError: Error executing code in Maxima
    CODE:
        sage356 : quad_qags(sage6,sage6,sage352,sage353,sage354,sage355)$
    Maxima ERROR:
        ^M
    Maxima encountered a Lisp error:^M
    ^M
     ^M
    WRITE-CHAR on #<CLOSED OUTPUT BUFFERED FILE-STREAM CHARACTER
#P"/dev/fd/1"> is illegal^M
    ^M
    Automatically continuing.^M
    To reenable the Lisp debugger set *debugger-hook* to nil.^M
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of  14 in __main__.example_40
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_calculus.py
         [61.0 s]
```

----- This is related to Mike Hansen's precision detection patch -- it
doesn't work right on
OSX PPC, evidently. 

Issue created by migration from https://trac.sagemath.org/ticket/1584





---

archive/issue_comments_010059.json:
```json
{
    "body": "Attachment [maxima-error2.9.1.alpha2.patch](tarball://root/attachments/some-uuid/ticket1584/maxima-error2.9.1.alpha2.patch) by @williamstein created at 2007-12-21 21:59:46\n\n+1",
    "created_at": "2007-12-21T21:59:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1584#issuecomment-10059",
    "user": "https://github.com/williamstein"
}
```

Attachment [maxima-error2.9.1.alpha2.patch](tarball://root/attachments/some-uuid/ticket1584/maxima-error2.9.1.alpha2.patch) by @williamstein created at 2007-12-21 21:59:46

+1



---

archive/issue_events_001740.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2007-12-21T22:09:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1584",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1584#event-1740"
}
```



---

archive/issue_comments_010060.json:
```json
{
    "body": "merged in 2.9.1 alpha3",
    "created_at": "2007-12-21T22:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1584#issuecomment-10060",
    "user": "https://github.com/rlmill"
}
```

merged in 2.9.1 alpha3



---

archive/issue_comments_010061.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-21T22:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1584",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1584#issuecomment-10061",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
