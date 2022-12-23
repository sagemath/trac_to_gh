# Issue 6319: optional doctest failure -- mistake in constructions guide wrt maxima interface

archive/issues_006319.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  awebb\n\nThis was clearly *never* tested, since eval always returns a string (it can't return nothing). \n\n\n```\nsage -t -long --optional devel/sage/doc/en/constructions/plotting.rst\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/plotting.rst\", line 211:\n    sage: maxima.eval('plotdf(x+y,[trajectory_at,2,-0.1]); ') #optional\nExpected nothing\nGot:\n    '1'\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_11\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6319\n\n",
    "created_at": "2009-06-16T14:47:30Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "title": "optional doctest failure -- mistake in constructions guide wrt maxima interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6319",
    "user": "was"
}
```
Assignee: tbd

CC:  awebb

This was clearly *never* tested, since eval always returns a string (it can't return nothing). 


```
sage -t -long --optional devel/sage/doc/en/constructions/plotting.rst
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/constructions/plotting.rst", line 211:
    sage: maxima.eval('plotdf(x+y,[trajectory_at,2,-0.1]); ') #optional
Expected nothing
Got:
    '1'
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_11
```




Issue created by migration from https://trac.sagemath.org/ticket/6319





---

archive/issue_comments_050437.json:
```json
{
    "body": "applies to 4.0.2.rc1",
    "created_at": "2009-06-16T23:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6319#issuecomment-50437",
    "user": "wdj"
}
```

applies to 4.0.2.rc1



---

archive/issue_comments_050438.json:
```json
{
    "body": "Attachment\n\nPasses sage -tp 1 SAGE_ROOT/devel/sage/doc/en/constructions/. Also the builds sage -docbuild  constructions html (resp., pdf) went fine.",
    "created_at": "2009-06-16T23:26:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6319#issuecomment-50438",
    "user": "wdj"
}
```

Attachment

Passes sage -tp 1 SAGE_ROOT/devel/sage/doc/en/constructions/. Also the builds sage -docbuild  constructions html (resp., pdf) went fine.



---

archive/issue_comments_050439.json:
```json
{
    "body": "I still get an error with sage -t -long --optional devel/sage/doc/en/constructions/plotting.rst, although it is with a return value of '0' instead of '1'. It passes sage -tp 1 SAGE_ROOT/devel/sage/doc/en/constructions/ for me as well. \n\nThe odd thing is that if I try the test from the sage command line I don't get the string returned i.e. the test passes.  Or is it fine if 'sage -t' fails but the documentation is correct for what happens when you actually run it?\n\nAdam",
    "created_at": "2009-07-16T06:31:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6319#issuecomment-50439",
    "user": "awebb"
}
```

I still get an error with sage -t -long --optional devel/sage/doc/en/constructions/plotting.rst, although it is with a return value of '0' instead of '1'. It passes sage -tp 1 SAGE_ROOT/devel/sage/doc/en/constructions/ for me as well. 

The odd thing is that if I try the test from the sage command line I don't get the string returned i.e. the test passes.  Or is it fine if 'sage -t' fails but the documentation is correct for what happens when you actually run it?

Adam
