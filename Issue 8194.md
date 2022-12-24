# Issue 8194: SageNB 0.8.x

archive/issues_008194.json:
```json
{
    "body": "Assignee: was\n\nCC:  acleone jhpalmieri robert.marik\n\nThe trial spkg at\n\n* \n\nHas the queue\n\nIssue created by migration from https://trac.sagemath.org/ticket/8194\n\n",
    "created_at": "2010-02-05T15:58:45Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "SageNB 0.8.x",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8194",
    "user": "mpatel"
}
```
Assignee: was

CC:  acleone jhpalmieri robert.marik

The trial spkg at

* 

Has the queue

Issue created by migration from https://trac.sagemath.org/ticket/8194





---

archive/issue_comments_072265.json:
```json
{
    "body": "Feel free to ignore a patch (or all of them!).  This is an experiment.",
    "created_at": "2010-02-05T16:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8194#issuecomment-72265",
    "user": "mpatel"
}
```

Feel free to ignore a patch (or all of them!).  This is an experiment.



---

archive/issue_comments_072266.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-10T18:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8194#issuecomment-72266",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072267.json:
```json
{
    "body": "Testing on Sage 4.3.2 I get error\n\n\n```\nsage -t  \"local/lib/python2.6/site-packages/sagenb-0.7.5-py2.6.egg/sagenb/misc/sageinspect.py\"\n**********************************************************************\nFile \"/opt/sage-4.3.2/local/lib/python2.6/site-packages/sagenb-0.7.5-py2.6.egg/sagenb/misc/sageinspect.py\", line 75:\n    sage: sage_getdoc(Foo)\nExpected:\n    'docstring\\n'\nGot:\n    'docstring'\n**********************************************************************\nFile \"/opt/sage-4.3.2/local/lib/python2.6/site-packages/sagenb-0.7.5-py2.6.egg/sagenb/misc/sageinspect.py\", line 459:\n    sage: sage_getdoc(identity_matrix)[5:39]\nExpected:\n    'turn the n x n identity matrix ove'\nGot:\n    'Return the `n x n` identity matrix'\n**********************************************************************\n2 items had failures:\n   1 of  29 in __main__.example_0\n   1 of   4 in __main__.example_8\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/marik/.sage//tmp/.doctest_sageinspect.py\n\n```\n\nOr should be tested on Sage 4.3.3 alpha 0?",
    "created_at": "2010-02-12T18:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8194#issuecomment-72267",
    "user": "robert.marik"
}
```

Testing on Sage 4.3.2 I get error


```
sage -t  "local/lib/python2.6/site-packages/sagenb-0.7.5-py2.6.egg/sagenb/misc/sageinspect.py"
**********************************************************************
File "/opt/sage-4.3.2/local/lib/python2.6/site-packages/sagenb-0.7.5-py2.6.egg/sagenb/misc/sageinspect.py", line 75:
    sage: sage_getdoc(Foo)
Expected:
    'docstring\n'
Got:
    'docstring'
**********************************************************************
File "/opt/sage-4.3.2/local/lib/python2.6/site-packages/sagenb-0.7.5-py2.6.egg/sagenb/misc/sageinspect.py", line 459:
    sage: sage_getdoc(identity_matrix)[5:39]
Expected:
    'turn the n x n identity matrix ove'
Got:
    'Return the `n x n` identity matrix'
**********************************************************************
2 items had failures:
   1 of  29 in __main__.example_0
   1 of   4 in __main__.example_8
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/marik/.sage//tmp/.doctest_sageinspect.py

```

Or should be tested on Sage 4.3.3 alpha 0?



---

archive/issue_comments_072268.json:
```json
{
    "body": "Thanks for reporting this.  To test with 4.3.2, please apply #8161's latest sage repository patch.  I should have added a note to the description, which I've done now.  I apologize.",
    "created_at": "2010-02-13T18:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8194#issuecomment-72268",
    "user": "mpatel"
}
```

Thanks for reporting this.  To test with 4.3.2, please apply #8161's latest sage repository patch.  I should have added a note to the description, which I've done now.  I apologize.



---

archive/issue_comments_072269.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-13T18:46:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8194#issuecomment-72269",
    "user": "robert.marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072270.json:
```json
{
    "body": "Seems to work fine for me, hanks. Positive review.",
    "created_at": "2010-02-13T18:46:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8194#issuecomment-72270",
    "user": "robert.marik"
}
```

Seems to work fine for me, hanks. Positive review.



---

archive/issue_comments_072271.json:
```json
{
    "body": "It seems okay compared to 0.7.4, but it sure would be nice to fix #8231...",
    "created_at": "2010-02-13T19:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8194#issuecomment-72271",
    "user": "jhpalmieri"
}
```

It seems okay compared to 0.7.4, but it sure would be nice to fix #8231...



---

archive/issue_comments_072272.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-14T03:39:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8194#issuecomment-72272",
    "user": "mpatel"
}
```

Resolution: fixed
