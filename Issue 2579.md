# Issue 2579: Inconsistency in integer quotient

archive/issues_002579.json:
```json
{
    "body": "Assignee: somebody\n\nsage: a=-17\nsage: a//4\n-5\nsage: a.div(4)\n-4\nsage: a.mod(4)\n3\n\n\nI recommend we redefine\n\ndef div(self, other):\n    q,_ = self.quo_rem(other)\n    return q\n\nIssue created by migration from https://trac.sagemath.org/ticket/2579\n\n",
    "created_at": "2008-03-18T01:29:11Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "Inconsistency in integer quotient",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2579",
    "user": "rishi"
}
```
Assignee: somebody

sage: a=-17
sage: a//4
-5
sage: a.div(4)
-4
sage: a.mod(4)
3


I recommend we redefine

def div(self, other):
    q,_ = self.quo_rem(other)
    return q

Issue created by migration from https://trac.sagemath.org/ticket/2579





---

archive/issue_comments_017640.json:
```json
{
    "body": "sage: a=-17 \n\nsage: a//4 \n\n-5 \n\nsage: a.div(4)\n\n-4 \n\nsage: a.mod(4)\n\n3\n\nI recommend we redefine\n\ndef div(self, other):\n\n    q,_ = self.quo_rem(other) \n\n    return q",
    "created_at": "2008-03-18T01:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2579#issuecomment-17640",
    "user": "rishi"
}
```

sage: a=-17 

sage: a//4 

-5 

sage: a.div(4)

-4 

sage: a.mod(4)

3

I recommend we redefine

def div(self, other):

    q,_ = self.quo_rem(other) 

    return q



---

archive/issue_comments_017641.json:
```json
{
    "body": "If we want a.div(b) to be floor(a/b) (which I agree we probably do, if we want the method to exist at all), the correct fix is to change from mpz_tdiv_qr to mpz_fdiv_q.",
    "created_at": "2008-03-18T02:21:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2579#issuecomment-17641",
    "user": "cwitty"
}
```

If we want a.div(b) to be floor(a/b) (which I agree we probably do, if we want the method to exist at all), the correct fix is to change from mpz_tdiv_qr to mpz_fdiv_q.



---

archive/issue_comments_017642.json:
```json
{
    "body": "I think the basis logic should be as below. Since this will make the remainder always positive.\n\n\n```\nif mpz_sgn(_other.value) == 1:\n            mpz_fdiv_q(q.value, _self.value, _other.value)        \nelse:\n            mpz_cdiv_q(q.value, _self.value, _other.value)\n```\n",
    "created_at": "2008-03-18T03:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2579#issuecomment-17642",
    "user": "rishi"
}
```

I think the basis logic should be as below. Since this will make the remainder always positive.


```
if mpz_sgn(_other.value) == 1:
            mpz_fdiv_q(q.value, _self.value, _other.value)        
else:
            mpz_cdiv_q(q.value, _self.value, _other.value)
```




---

archive/issue_comments_017643.json:
```json
{
    "body": "Attachment [integerdiv.patch](tarball://root/attachments/some-uuid/ticket2579/integerdiv.patch) by rishi created at 2008-03-19 17:01:18",
    "created_at": "2008-03-19T17:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2579#issuecomment-17643",
    "user": "rishi"
}
```

Attachment [integerdiv.patch](tarball://root/attachments/some-uuid/ticket2579/integerdiv.patch) by rishi created at 2008-03-19 17:01:18



---

archive/issue_comments_017644.json:
```json
{
    "body": "I used quo_rem to redefine div. I would have essentially copied and pasted quo_rem otherwise.",
    "created_at": "2008-03-19T17:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2579#issuecomment-17644",
    "user": "rishi"
}
```

I used quo_rem to redefine div. I would have essentially copied and pasted quo_rem otherwise.



---

archive/issue_comments_017645.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-03-19T20:31:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2579#issuecomment-17645",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_017646.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-20T00:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2579#issuecomment-17646",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha0



---

archive/issue_comments_017647.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-20T00:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2579#issuecomment-17647",
    "user": "mabshoff"
}
```

Resolution: fixed
