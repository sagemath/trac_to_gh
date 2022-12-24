# Issue 5377: weird output for trivial class group

archive/issues_005377.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: K.<a> = NumberField(x^2 + 1)\nsage: K.class_group()\nClass group of order 1 with structure  of Number Field in a with defining polynomial x^2 + 1\n```\n\n\nThere is something missing after \"structure\".\n\nThis is possibly related to #2574 (which is marked as fixed...)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5377\n\n",
    "created_at": "2009-02-26T00:53:26Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "weird output for trivial class group",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5377",
    "user": "dmharvey"
}
```
Assignee: @williamstein


```
sage: K.<a> = NumberField(x^2 + 1)
sage: K.class_group()
Class group of order 1 with structure  of Number Field in a with defining polynomial x^2 + 1
```


There is something missing after "structure".

This is possibly related to #2574 (which is marked as fixed...)


Issue created by migration from https://trac.sagemath.org/ticket/5377





---

archive/issue_comments_041406.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-21T08:08:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5377#issuecomment-41406",
    "user": "@loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_041407.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-21T08:08:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5377#issuecomment-41407",
    "user": "@loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_041408.json:
```json
{
    "body": "Seems to be fixed in sage-4.7.2.alpha3.",
    "created_at": "2011-10-09T10:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5377#issuecomment-41408",
    "user": "@jdemeyer"
}
```

Seems to be fixed in sage-4.7.2.alpha3.



---

archive/issue_comments_041409.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2011-10-09T10:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5377",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5377#issuecomment-41409",
    "user": "@jdemeyer"
}
```

Resolution: worksforme
