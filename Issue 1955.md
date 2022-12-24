# Issue 1955: bug in vector

archive/issues_001955.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\n\nHi,\n\nIt seems the __abs__ method for vectors is missing the part that is\nsupposed to square the components before they are added.\n\n[e.g. abs(vector([1..5])) should really be\nsqrt(1+4+9+16+25)=sqrt(55) ]\n\nThe code of the current version is included below.\n\n   def __abs__(self):\n       \"\"\"\n       Return the square root of the sum of the squares of the\nentries of this vector.\n\n       EXAMPLES:\n           sage: v = vector([1..5]); abs(v)\n           sqrt(15)\n           sage: v = vector(RDF, [1..5]); abs(v)\n           3.87298334621\n       \"\"\"\n       return sum(self.list()).sqrt()\n\nThe last line should be something like\n\n       return sum([x*x for x in self.list()]).sqrt()\n\n(not sure if that is the most efficient way).\n\n--Peter\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1955\n\n",
    "created_at": "2008-01-28T00:25:26Z",
    "labels": [
        "basic arithmetic",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in vector",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1955",
    "user": "@williamstein"
}
```
Assignee: somebody


```

Hi,

It seems the __abs__ method for vectors is missing the part that is
supposed to square the components before they are added.

[e.g. abs(vector([1..5])) should really be
sqrt(1+4+9+16+25)=sqrt(55) ]

The code of the current version is included below.

   def __abs__(self):
       """
       Return the square root of the sum of the squares of the
entries of this vector.

       EXAMPLES:
           sage: v = vector([1..5]); abs(v)
           sqrt(15)
           sage: v = vector(RDF, [1..5]); abs(v)
           3.87298334621
       """
       return sum(self.list()).sqrt()

The last line should be something like

       return sum([x*x for x in self.list()]).sqrt()

(not sure if that is the most efficient way).

--Peter
```


Issue created by migration from https://trac.sagemath.org/ticket/1955





---

archive/issue_comments_012448.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-01-28T00:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1955#issuecomment-12448",
    "user": "mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_012449.json:
```json
{
    "body": "This is a dupe of #1954, which already has a patch for review.",
    "created_at": "2008-01-28T00:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1955",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1955#issuecomment-12449",
    "user": "mabshoff"
}
```

This is a dupe of #1954, which already has a patch for review.
