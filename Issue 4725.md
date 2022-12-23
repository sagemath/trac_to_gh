# Issue 4725: bug in number field conjugate function

archive/issues_004725.json:
```json
{
    "body": "Assignee: was\n\nThis is totally wrong!\n\n```\nsage: K.<j,b> = QQ[sqrt(-1), sqrt(2)]\nsage: j.conjugate()\n0\n```\n\n\nMuch better would be either an error message (since the docs for conjugate say it isn't implemented except for cyclotomic and quadratic fields!) or an actual correct answer using a number field embedding.  But giving 0 is just crazy.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4725\n\n",
    "created_at": "2008-12-06T18:37:26Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "bug in number field conjugate function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4725",
    "user": "was"
}
```
Assignee: was

This is totally wrong!

```
sage: K.<j,b> = QQ[sqrt(-1), sqrt(2)]
sage: j.conjugate()
0
```


Much better would be either an error message (since the docs for conjugate say it isn't implemented except for cyclotomic and quadratic fields!) or an actual correct answer using a number field embedding.  But giving 0 is just crazy.

Issue created by migration from https://trac.sagemath.org/ticket/4725





---

archive/issue_comments_035670.json:
```json
{
    "body": "This is sorted out by a minor change to `conjugate` included in the patch\nwith #5842.  There is a doctest at line 1456 of the patched\n`number_field_element.pyx`",
    "created_at": "2009-04-21T08:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4725#issuecomment-35670",
    "user": "fwclarke"
}
```

This is sorted out by a minor change to `conjugate` included in the patch
with #5842.  There is a doctest at line 1456 of the patched
`number_field_element.pyx`



---

archive/issue_comments_035671.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-21T08:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4725#issuecomment-35671",
    "user": "davidloeffler"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_035672.json:
```json
{
    "body": "I can confirm that this is indeed fixed (although the fix has now drifted to line 1542).",
    "created_at": "2009-07-21T08:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4725#issuecomment-35672",
    "user": "davidloeffler"
}
```

I can confirm that this is indeed fixed (although the fix has now drifted to line 1542).



---

archive/issue_comments_035673.json:
```json
{
    "body": "Changing assignee from was to davidloeffler.",
    "created_at": "2009-07-21T08:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4725#issuecomment-35673",
    "user": "davidloeffler"
}
```

Changing assignee from was to davidloeffler.



---

archive/issue_comments_035674.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-22T16:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4725#issuecomment-35674",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_035675.json:
```json
{
    "body": "Fixed due to #5842.",
    "created_at": "2009-07-22T16:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4725",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4725#issuecomment-35675",
    "user": "mvngu"
}
```

Fixed due to #5842.
