# Issue 2466: 2.10.3: doctest failure in const.tex

archive/issues_002466.json:
```json
{
    "body": "Assignee: failure\n\n\n```\nsage -t -long devel/doc-main/const/const.tex\n**********************************************************************\nFile \"const.py\", line 1544:\n    : A.eigenspaces() #random output\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_47[5]>\", line 1, in <module>\n        print \"ignore this\";  A.eigenspaces() #random output###line 1544:\n    : A.eigenspaces() #random output\n      File \"matrix2.pyx\", line 2198, in sage.matrix.matrix2.Matrix.eigenspaces\n    NotImplementedError: won't use generic algorithm for inexact base rings, pass the option even_if_inexact=True if you really want this.\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2466\n\n",
    "created_at": "2008-03-11T01:47:54Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "2.10.3: doctest failure in const.tex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2466",
    "user": "mabshoff"
}
```
Assignee: failure


```
sage -t -long devel/doc-main/const/const.tex
**********************************************************************
File "const.py", line 1544:
    : A.eigenspaces() #random output
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-2.10.3.rc4/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_47[5]>", line 1, in <module>
        print "ignore this";  A.eigenspaces() #random output###line 1544:
    : A.eigenspaces() #random output
      File "matrix2.pyx", line 2198, in sage.matrix.matrix2.Matrix.eigenspaces
    NotImplementedError: won't use generic algorithm for inexact base rings, pass the option even_if_inexact=True if you really want this.
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/2466





---

archive/issue_comments_016711.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-11T02:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2466#issuecomment-16711",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_016712.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-11T02:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2466#issuecomment-16712",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_016713.json:
```json
{
    "body": "Patch looks good to me. Positive review.",
    "created_at": "2008-03-11T02:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2466#issuecomment-16713",
    "user": "mabshoff"
}
```

Patch looks good to me. Positive review.



---

archive/issue_comments_016714.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc5",
    "created_at": "2008-03-11T02:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2466",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2466#issuecomment-16714",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc5
