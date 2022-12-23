# Issue 2264: Sage 2.10.2.rc0: numerical noise doctest failure in rings/real_rqdf.pyx

archive/issues_002264.json:
```json
{
    "body": "Assignee: failure\n\nCraig Citro reported:\n\n```\n**********************************************************************\nFile \"real_rqdf.pyx\", line 32:\n    sage: RQDF(a)\nExpected:\n    0.868588963806503655302257837833210164588794011607333132228907565\nGot:\n    0.868588963806503655302257837833210164588794011607333132228907566\n********************************************************************** \n```\n\nThe above failure corresponds to:\n\n```\nMixing of symbolic an quad double elements:\n    sage: a = RQDF(2) / log(10); a\n    2.00000000000000/log(10)\n    sage: parent(a)\n    Symbolic Ring\n    sage: RQDF(a)\n    0.868588963806503655302257837833210164588794011607333132228907565\n```\n\nSo in this case it isn't so much a failure of an RQDF element (which should always print the same), but a numerical inconsistency from coercion the result into the quad double ring, i.e. coercion to the ring with lower precision. If the fix is to add \"...\" here we should comment on the fact that coercion causes the numerical noise and that RQDF is not at fault for that.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2264\n\n",
    "created_at": "2008-02-22T19:19:06Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "Sage 2.10.2.rc0: numerical noise doctest failure in rings/real_rqdf.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2264",
    "user": "mabshoff"
}
```
Assignee: failure

Craig Citro reported:

```
**********************************************************************
File "real_rqdf.pyx", line 32:
    sage: RQDF(a)
Expected:
    0.868588963806503655302257837833210164588794011607333132228907565
Got:
    0.868588963806503655302257837833210164588794011607333132228907566
********************************************************************** 
```

The above failure corresponds to:

```
Mixing of symbolic an quad double elements:
    sage: a = RQDF(2) / log(10); a
    2.00000000000000/log(10)
    sage: parent(a)
    Symbolic Ring
    sage: RQDF(a)
    0.868588963806503655302257837833210164588794011607333132228907565
```

So in this case it isn't so much a failure of an RQDF element (which should always print the same), but a numerical inconsistency from coercion the result into the quad double ring, i.e. coercion to the ring with lower precision. If the fix is to add "..." here we should comment on the fact that coercion causes the numerical noise and that RQDF is not at fault for that.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2264





---

archive/issue_comments_014998.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-02-22T19:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2264#issuecomment-14998",
    "user": "mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_014999.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-22T19:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2264#issuecomment-14999",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015000.json:
```json
{
    "body": ">  precision. If the fix is to add \"...\" here we should comment on the fact\n> that coercion causes the numerical noise and that RQDF is not at fault for\n> that.\n\nI agree.",
    "created_at": "2008-02-22T21:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2264#issuecomment-15000",
    "user": "was"
}
```

>  precision. If the fix is to add "..." here we should comment on the fact
> that coercion causes the numerical noise and that RQDF is not at fault for
> that.

I agree.



---

archive/issue_comments_015001.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-22T21:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2264#issuecomment-15001",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_015002.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-22T22:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2264#issuecomment-15002",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015003.json:
```json
{
    "body": "Merged in Sage 2.10.2.final",
    "created_at": "2008-02-22T22:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2264#issuecomment-15003",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.final
