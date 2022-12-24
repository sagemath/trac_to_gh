# Issue 1954: sage/modules/free_module_element.pyx computing abs(vector(...))

archive/issues_001954.json:
```json
{
    "body": "Assignee: mhansen\n\n\n```\n\nHi,\n\nIt seems the __abs__ method for vectors is missing the part that is\nsupposed to square the components before they are added.\n\n[e.g. abs(vector([1..5])) should really be\nsqrt(1+4+9+16+25)=sqrt(55) ]\n\nThe code of the current version is included below.\n\n   def __abs__(self):\n       \"\"\"\n       Return the square root of the sum of the squares of the\nentries of this vector.\n\n       EXAMPLES:\n           sage: v = vector([1..5]); abs(v)\n           sqrt(15)\n           sage: v = vector(RDF, [1..5]); abs(v)\n           3.87298334621\n       \"\"\"\n       return sum(self.list()).sqrt()\n\nThe last line should be something like\n\n       return sum([x*x for x in self.list()]).sqrt()\n\n(not sure if that is the most efficient way).\n\n--Peter\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1954\n\n",
    "created_at": "2008-01-28T00:03:21Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "sage/modules/free_module_element.pyx computing abs(vector(...))",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1954",
    "user": "mhansen"
}
```
Assignee: mhansen


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


Issue created by migration from https://trac.sagemath.org/ticket/1954





---

archive/issue_comments_012442.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-28T00:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1954#issuecomment-12442",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_012443.json:
```json
{
    "body": "Attachment [1954.patch](tarball://root/attachments/some-uuid/ticket1954/1954.patch) by mhansen created at 2008-01-28 00:06:03",
    "created_at": "2008-01-28T00:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1954#issuecomment-12443",
    "user": "mhansen"
}
```

Attachment [1954.patch](tarball://root/attachments/some-uuid/ticket1954/1954.patch) by mhansen created at 2008-01-28 00:06:03



---

archive/issue_comments_012444.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-01-28T00:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1954#issuecomment-12444",
    "user": "mhansen"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_012445.json:
```json
{
    "body": "Looks good to me (I only ran doctests on that file, not on all files).\n\n(If anyone has time, would be good to try doing this without the `list` call, and also I expect `x*x` is generally faster than `x**2`.)",
    "created_at": "2008-01-28T01:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1954#issuecomment-12445",
    "user": "dmharvey"
}
```

Looks good to me (I only ran doctests on that file, not on all files).

(If anyone has time, would be good to try doing this without the `list` call, and also I expect `x*x` is generally faster than `x**2`.)



---

archive/issue_comments_012446.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-28T02:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1954#issuecomment-12446",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012447.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc2",
    "created_at": "2008-01-28T02:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1954",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1954#issuecomment-12447",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc2
