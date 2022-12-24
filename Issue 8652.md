# Issue 8652: load uses "strip" on non-strings

archive/issues_008652.json:
```json
{
    "body": "Assignee: was\n\nCC:  leif\n\nI got this bug/traceback today by making a file grader.py and a file grader.sage (their content doesn't matter).  \n\n\n```\nsage: import grader\nsage: load grader.sage\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/Users/wstein/edu/2010/480/grading/<ipython console> in <module>()\n\n/Users/wstein/sage/build/sage/local/lib/python2.6/site-packages/sage/misc/preparser.pyc in load(filename, globals, attach)\n   1487             return\n   1488         \n-> 1489     filename = filename.strip()\n   1490     \n   1491     if filename.lower().startswith('http://'):\n\nAttributeError: 'module' object has no attribute 'strip'\nsage: \n```\n\n\nThe above bug is the fault of the rewrite *I* did of load and attach, so is my fault. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8652\n\n",
    "created_at": "2010-04-06T05:25:31Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "load uses \"strip\" on non-strings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8652",
    "user": "was"
}
```
Assignee: was

CC:  leif

I got this bug/traceback today by making a file grader.py and a file grader.sage (their content doesn't matter).  


```
sage: import grader
sage: load grader.sage
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/wstein/edu/2010/480/grading/<ipython console> in <module>()

/Users/wstein/sage/build/sage/local/lib/python2.6/site-packages/sage/misc/preparser.pyc in load(filename, globals, attach)
   1487             return
   1488         
-> 1489     filename = filename.strip()
   1490     
   1491     if filename.lower().startswith('http://'):

AttributeError: 'module' object has no attribute 'strip'
sage: 
```


The above bug is the fault of the rewrite *I* did of load and attach, so is my fault. 

Issue created by migration from https://trac.sagemath.org/ticket/8652





---

archive/issue_comments_078503.json:
```json
{
    "body": "Did I miss something?\n\nIf I create both files `foo.py` and `foo.sage`, then\n\n\n```\nsage: import foo\nI am foo.py\nsage: load foo.sage\nI am foo.sage\n```\n\n\ndoesn't give an error (in 4.3.5).",
    "created_at": "2010-04-07T17:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8652#issuecomment-78503",
    "user": "leif"
}
```

Did I miss something?

If I create both files `foo.py` and `foo.sage`, then


```
sage: import foo
I am foo.py
sage: load foo.sage
I am foo.sage
```


doesn't give an error (in 4.3.5).



---

archive/issue_comments_078504.json:
```json
{
    "body": "I'm using 4.3.4 and I see the same thing as leif -- worksforme. Perhaps the content of grader.py and grader.sage does matter?",
    "created_at": "2010-04-28T03:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8652#issuecomment-78504",
    "user": "ddrake"
}
```

I'm using 4.3.4 and I see the same thing as leif -- worksforme. Perhaps the content of grader.py and grader.sage does matter?



---

archive/issue_comments_078505.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd40.5\".",
    "created_at": "2012-05-28T22:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8652#issuecomment-78505",
    "user": "ddrake"
}
```

Changing keywords from "" to "sd40.5".



---

archive/issue_comments_078506.json:
```json
{
    "body": "This still works properly on 5.1.beta0. In two years no one has reported or reproduced this bug; I propose we close it.",
    "created_at": "2012-05-28T22:32:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8652#issuecomment-78506",
    "user": "ddrake"
}
```

This still works properly on 5.1.beta0. In two years no one has reported or reproduced this bug; I propose we close it.



---

archive/issue_comments_078507.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-03-15T18:47:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8652#issuecomment-78507",
    "user": "mmezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078508.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-15T18:47:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8652#issuecomment-78508",
    "user": "mmezzarobba"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078509.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2014-03-19T04:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8652#issuecomment-78509",
    "user": "vbraun"
}
```

Resolution: invalid
