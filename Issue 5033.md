# Issue 5033: matrix lift function bad in two ways

archive/issues_005033.json:
```json
{
    "body": "Assignee: was\n\nThere are two problem here:\n\n```\nsage: B = matrix(QQ, 2, [1..4])\nsage: B.lift()\n...\nAttributeError: 'RationalField' object has no attribute 'cover_ring'\nsage: B.lift?\n            EXAMPLES:\n...\n```\n          \n\n1. lift should first check if there is a cover_ring attribute.  If not, I think lift should just return self.\n\n2. The lift function is undocumented.  It just has examples but no description of what it is supposed to do.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5033\n\n",
    "created_at": "2009-01-20T06:03:40Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "matrix lift function bad in two ways",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5033",
    "user": "was"
}
```
Assignee: was

There are two problem here:

```
sage: B = matrix(QQ, 2, [1..4])
sage: B.lift()
...
AttributeError: 'RationalField' object has no attribute 'cover_ring'
sage: B.lift?
            EXAMPLES:
...
```
          

1. lift should first check if there is a cover_ring attribute.  If not, I think lift should just return self.

2. The lift function is undocumented.  It just has examples but no description of what it is supposed to do.

Issue created by migration from https://trac.sagemath.org/ticket/5033





---

archive/issue_comments_038329.json:
```json
{
    "body": "Attachment\n\nthis is against sage-3.3.alpha0",
    "created_at": "2009-01-20T06:35:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5033#issuecomment-38329",
    "user": "was"
}
```

Attachment

this is against sage-3.3.alpha0



---

archive/issue_comments_038330.json:
```json
{
    "body": "The patch fixes both issues mentioned in the ticket and the code is nice. Positive review.",
    "created_at": "2009-01-20T06:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5033#issuecomment-38330",
    "user": "ddrake"
}
```

The patch fixes both issues mentioned in the ticket and the code is nice. Positive review.



---

archive/issue_comments_038331.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T09:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5033#issuecomment-38331",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038332.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T09:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5033",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5033#issuecomment-38332",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1
