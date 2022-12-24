# Issue 3068: empty matrices: smith_form() throws a RuntimeError

archive/issues_003068.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: m = matrix([])\nsage: m.smith_form()\n<type 'exceptions.RuntimeError'>:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3068\n\n",
    "created_at": "2008-04-30T15:25:30Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "empty matrices: smith_form() throws a RuntimeError",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3068",
    "user": "dfdeshom"
}
```
Assignee: was


```
sage: m = matrix([])
sage: m.smith_form()
<type 'exceptions.RuntimeError'>:
```


Issue created by migration from https://trac.sagemath.org/ticket/3068





---

archive/issue_comments_021171.json:
```json
{
    "body": "This seems to be gone as of 3.1.1. Could someone close this?\n\n```\nsage: m = matrix([])\nsage: m.smith_form()\n ([], [], [])\n```\n",
    "created_at": "2008-08-27T18:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3068#issuecomment-21171",
    "user": "dfdeshom"
}
```

This seems to be gone as of 3.1.1. Could someone close this?

```
sage: m = matrix([])
sage: m.smith_form()
 ([], [], [])
```




---

archive/issue_comments_021172.json:
```json
{
    "body": "In 3.2.2.alpha0 this works fine as long as the matrix has 0 rows and 0 columns, but for 0 rows and a nonzero number of columns (or vice versa) we still get the error. This arises from the fact that Pari doesn't have the notion of a matrix with 0 rows and 1 column, so the matrix gets \"truncated\" (!) before being passed to Pari.\n\nI will fix this as part of #4681.",
    "created_at": "2008-12-08T18:03:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3068#issuecomment-21172",
    "user": "davidloeffler"
}
```

In 3.2.2.alpha0 this works fine as long as the matrix has 0 rows and 0 columns, but for 0 rows and a nonzero number of columns (or vice versa) we still get the error. This arises from the fact that Pari doesn't have the notion of a matrix with 0 rows and 1 column, so the matrix gets "truncated" (!) before being passed to Pari.

I will fix this as part of #4681.



---

archive/issue_comments_021173.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-08T18:03:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3068#issuecomment-21173",
    "user": "davidloeffler"
}
```

Resolution: fixed



---

archive/issue_comments_021174.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-12-08T18:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3068#issuecomment-21174",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_021175.json:
```json
{
    "body": "Hi David,\n\nusually the release manager does the closing of a ticket once the fix has been merged. Until then it stays open.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-08T18:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3068#issuecomment-21175",
    "user": "mabshoff"
}
```

Hi David,

usually the release manager does the closing of a ticket once the fix has been merged. Until then it stays open.

Cheers,

Michael



---

archive/issue_comments_021176.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-12-08T18:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3068#issuecomment-21176",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_021177.json:
```json
{
    "body": "I'm sorry for overstepping my authority. Anyway, the fix is now up at #4681.",
    "created_at": "2008-12-08T18:18:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3068#issuecomment-21177",
    "user": "davidloeffler"
}
```

I'm sorry for overstepping my authority. Anyway, the fix is now up at #4681.



---

archive/issue_comments_021178.json:
```json
{
    "body": "Replying to [comment:4 davidloeffler]:\n> I'm sorry for overstepping my authority. Anyway, the fix is now up at #4681.\n\nDon't worry about it because it is one of those unwritten rules :)\n\nCheers,\n\nMichael",
    "created_at": "2008-12-08T18:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3068#issuecomment-21178",
    "user": "mabshoff"
}
```

Replying to [comment:4 davidloeffler]:
> I'm sorry for overstepping my authority. Anyway, the fix is now up at #4681.

Don't worry about it because it is one of those unwritten rules :)

Cheers,

Michael



---

archive/issue_comments_021179.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-10T11:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3068#issuecomment-21179",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021180.json:
```json
{
    "body": "Fixed in Sage 3.2.2.alpha1 via #4681.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-10T11:27:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3068",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3068#issuecomment-21180",
    "user": "mabshoff"
}
```

Fixed in Sage 3.2.2.alpha1 via #4681.

Cheers,

Michael
