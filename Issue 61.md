# Issue 61: hanke -- disturbing matrix constructor issue involving rows versus columns

archive/issues_000061.json:
```json
{
    "body": "Assignee: somebody\n\nHi William,\n \nI just found a disturbing trait about Matrix constructions, and was\nwondering if you could include a rows/columns flag to address it.\n \n\nWhen a matrix is constructed from tuples, it assumes that you want to\nuse these numbers as *rows*, regardless of whether the tuples are\nappropriately sized.  Since there is no way of deciding which is meant\nfor square matrices, it seems reasonable to add an extra (mandatory)\nflag to the constructor for a list of tuples to ask which is meant.\n \n\n\nI hope your semster is going well.   See you,\n \n\t\t\t\t\t\t-Jon (Hanke)\n\t\t\t\t\t\t \n\n```\n--------------------------------------------------------------------\n \nsage: M2 = MatrixSpace(ZZ,2,4)(range(8)); M2\n[0 1 2 3]\n[4 5 6 7]\n \nsage: M2.columns()\n [(0, 4), (1, 5), (2, 6), (3, 7)]\n \nsage: MatrixSpace(ZZ,2,4)(M2.columns())\n[0 4 1 5]\n[2 6 3 7]\n \nsage: M2 == MatrixSpace(ZZ,2,4)(M2.columns())\n False\n \nsage: M2 == MatrixSpace(ZZ,2,4)(M2.rows())\n True\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/61\n\n",
    "created_at": "2006-09-14T22:26:29Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "title": "hanke -- disturbing matrix constructor issue involving rows versus columns",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/61",
    "user": "was"
}
```
Assignee: somebody

Hi William,
 
I just found a disturbing trait about Matrix constructions, and was
wondering if you could include a rows/columns flag to address it.
 

When a matrix is constructed from tuples, it assumes that you want to
use these numbers as *rows*, regardless of whether the tuples are
appropriately sized.  Since there is no way of deciding which is meant
for square matrices, it seems reasonable to add an extra (mandatory)
flag to the constructor for a list of tuples to ask which is meant.
 


I hope your semster is going well.   See you,
 
						-Jon (Hanke)
						 

```
--------------------------------------------------------------------
 
sage: M2 = MatrixSpace(ZZ,2,4)(range(8)); M2
[0 1 2 3]
[4 5 6 7]
 
sage: M2.columns()
 [(0, 4), (1, 5), (2, 6), (3, 7)]
 
sage: MatrixSpace(ZZ,2,4)(M2.columns())
[0 4 1 5]
[2 6 3 7]
 
sage: M2 == MatrixSpace(ZZ,2,4)(M2.columns())
 False
 
sage: M2 == MatrixSpace(ZZ,2,4)(M2.rows())
 True
```


Issue created by migration from https://trac.sagemath.org/ticket/61





---

archive/issue_comments_000322.json:
```json
{
    "body": "This is still a problem with Sage 2.8.2. The 2.8.3 release might cut it a little close because there are still a large number of tickets left (to be fixed in roughly 1 day).\n\nCheers,\n\nMichael",
    "created_at": "2007-08-23T11:11:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/61",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/61#issuecomment-322",
    "user": "mabshoff"
}
```

This is still a problem with Sage 2.8.2. The 2.8.3 release might cut it a little close because there are still a large number of tickets left (to be fixed in roughly 1 day).

Cheers,

Michael



---

archive/issue_comments_000323.json:
```json
{
    "body": "Changing assignee from somebody to mhansen.",
    "created_at": "2007-09-21T05:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/61",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/61#issuecomment-323",
    "user": "mhansen"
}
```

Changing assignee from somebody to mhansen.



---

archive/issue_comments_000324.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-03T18:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/61",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/61#issuecomment-324",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_000325.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-11-03T19:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/61",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/61#issuecomment-325",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_000326.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T23:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/61",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/61#issuecomment-326",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000327.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-11-03T23:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/61",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/61#issuecomment-327",
    "user": "was"
}
```

Attachment
