# Issue 241: mod bug

archive/issues_000241.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nHi William,\n \nI don't consider this correct:\n \nsage: x = -8\nsage: x.mod(3)\n-2\nsage: x = 8\nsage: x.mod(3)\n2\n \nIf the convention where to return a value in (-n/2,n/2] rather than \n[0,n) then this could be justified.  But the output should depend \nonly on x in Z/3Z, not on the representative.\n \nIt is also called in a rather convoluted way -- by creating an \nideal then calling reduce on the ideal, then extracting the principal \ngenerator for the ideal.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/241\n\n",
    "created_at": "2007-02-03T19:13:09Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "mod bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/241",
    "user": "was"
}
```
Assignee: somebody


```
Hi William,
 
I don't consider this correct:
 
sage: x = -8
sage: x.mod(3)
-2
sage: x = 8
sage: x.mod(3)
2
 
If the convention where to return a value in (-n/2,n/2] rather than 
[0,n) then this could be justified.  But the output should depend 
only on x in Z/3Z, not on the representative.
 
It is also called in a rather convoluted way -- by creating an 
ideal then calling reduce on the ideal, then extracting the principal 
generator for the ideal.
```


Issue created by migration from https://trac.sagemath.org/ticket/241





---

archive/issue_comments_001074.json:
```json
{
    "body": "Seems to be fixed in 2.4",
    "created_at": "2007-04-13T03:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/241#issuecomment-1074",
    "user": "roed"
}
```

Seems to be fixed in 2.4



---

archive/issue_comments_001075.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2007-04-13T03:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/241#issuecomment-1075",
    "user": "roed"
}
```

Resolution: worksforme
