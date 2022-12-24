# Issue 5506: symbolic vectors class

archive/issues_005506.json:
```json
{
    "body": "Assignee: was\n\nCC:  eviatarbach\n\nWe really should make symbolic vectors a subclass of the generic free modules.  That way we can have a .args() function, a variables function, and a few other functions that make sense for symbolic vectors, but maybe not for arbitrary vectors.\n\nWe can also make them callable, so vector-valued functions work.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5506\n\n",
    "created_at": "2009-03-12T23:07:38Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "symbolic vectors class",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5506",
    "user": "jason"
}
```
Assignee: was

CC:  eviatarbach

We really should make symbolic vectors a subclass of the generic free modules.  That way we can have a .args() function, a variables function, and a few other functions that make sense for symbolic vectors, but maybe not for arbitrary vectors.

We can also make them callable, so vector-valued functions work.

Issue created by migration from https://trac.sagemath.org/ticket/5506





---

archive/issue_comments_042761.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T05:57:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5506#issuecomment-42761",
    "user": "jason"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_042762.json:
```json
{
    "body": "#8947 is a start on this.  We could add to that an args() function, a variables function, etc.",
    "created_at": "2010-05-11T18:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5506#issuecomment-42762",
    "user": "jason"
}
```

#8947 is a start on this.  We could add to that an args() function, a variables function, etc.



---

archive/issue_comments_042763.json:
```json
{
    "body": "See #3021 for more things we could add to the class.",
    "created_at": "2010-05-11T18:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5506",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5506#issuecomment-42763",
    "user": "jason"
}
```

See #3021 for more things we could add to the class.
