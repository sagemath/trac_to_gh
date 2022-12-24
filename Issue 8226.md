# Issue 8226: Elementary divisors for non PIDs

archive/issues_008226.json:
```json
{
    "body": "Assignee: @loefflerd\n\nKeywords: elementary divisors\n\nOver maximal orders O in number fields K the elementary divisors provide a complete system of invariants for in matrices GL_n(K). Here the elementary divisors are the ideals e_i = d_i / d_{i-1} where d_i are the determinantal divisors. This patch provides the possibility to compute these elementary divisors.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8226\n\n",
    "created_at": "2010-02-10T08:48:32Z",
    "labels": [
        "number fields",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Elementary divisors for non PIDs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8226",
    "user": "mraum"
}
```
Assignee: @loefflerd

Keywords: elementary divisors

Over maximal orders O in number fields K the elementary divisors provide a complete system of invariants for in matrices GL_n(K). Here the elementary divisors are the ideals e_i = d_i / d_{i-1} where d_i are the determinantal divisors. This patch provides the possibility to compute these elementary divisors.

Issue created by migration from https://trac.sagemath.org/ticket/8226





---

archive/issue_comments_072635.json:
```json
{
    "body": "Attachment [trac-8226-elementary_divisors.patch](tarball://root/attachments/some-uuid/ticket8226/trac-8226-elementary_divisors.patch) by mraum created at 2010-02-10 08:49:46",
    "created_at": "2010-02-10T08:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8226#issuecomment-72635",
    "user": "mraum"
}
```

Attachment [trac-8226-elementary_divisors.patch](tarball://root/attachments/some-uuid/ticket8226/trac-8226-elementary_divisors.patch) by mraum created at 2010-02-10 08:49:46



---

archive/issue_comments_072636.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-10T08:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8226#issuecomment-72636",
    "user": "mraum"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072637.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-21T14:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8226#issuecomment-72637",
    "user": "@JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_072638.json:
```json
{
    "body": "There looks like a typo on line 6293.",
    "created_at": "2010-02-21T14:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8226#issuecomment-72638",
    "user": "@JohnCremona"
}
```

There looks like a typo on line 6293.



---

archive/issue_comments_072639.json:
```json
{
    "body": "Replying to [comment:2 cremona]:\n> There looks like a typo on line 6293.\n\nAcutally no. The statement \"raise\" raises the last exception one has cached and this is exactly what I want. If the SMNF can't be obtainted by means of the algorithm implemented at the moment - and this is indicated by an ArithmeticError - I check whether I can do it diffently. If not the original ArithmeticError with its trac back is the most useful error message.\nDo you think diffently about this?\n\nThe best would be to check whether a ring is a PID or not. Then decide on the algorithm to use. But this isn't even implemented for ZZ, so no chance to do it.",
    "created_at": "2010-02-21T14:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8226#issuecomment-72639",
    "user": "mraum"
}
```

Replying to [comment:2 cremona]:
> There looks like a typo on line 6293.

Acutally no. The statement "raise" raises the last exception one has cached and this is exactly what I want. If the SMNF can't be obtainted by means of the algorithm implemented at the moment - and this is indicated by an ArithmeticError - I check whether I can do it diffently. If not the original ArithmeticError with its trac back is the most useful error message.
Do you think diffently about this?

The best would be to check whether a ring is a PID or not. Then decide on the algorithm to use. But this isn't even implemented for ZZ, so no chance to do it.



---

archive/issue_comments_072640.json:
```json
{
    "body": "I think mraum's point is a fair one: re-raising the original error will generally be more helpful than raising a new one (e.g. it might give an explicit example of a non-principal ideal in the base ring). \n\nBut I don't like the idea that `smith_form` will sometimes return elements and sometimes ideals. I totally agree that we should have the functionality to compute these elementary divisor ideals, but it should be a separate function, with `smith_form` raising an error when the elementary divisors aren't principal. Also, Pari has a fast algorithm for this problem, so we should use that rather than devising our own; see #4742.",
    "created_at": "2010-06-29T11:34:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8226#issuecomment-72640",
    "user": "@loefflerd"
}
```

I think mraum's point is a fair one: re-raising the original error will generally be more helpful than raising a new one (e.g. it might give an explicit example of a non-principal ideal in the base ring). 

But I don't like the idea that `smith_form` will sometimes return elements and sometimes ideals. I totally agree that we should have the functionality to compute these elementary divisor ideals, but it should be a separate function, with `smith_form` raising an error when the elementary divisors aren't principal. Also, Pari has a fast algorithm for this problem, so we should use that rather than devising our own; see #4742.
