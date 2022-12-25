# Issue 2579: [with patch, positive review] Inconsistency in integer quotient

archive/issues_002579.json:
```json
{
    "body": "Assignee: somebody\n\n```\nsage: a=-17\nsage: a//4\n-5\nsage: a.div(4)\n-4\nsage: a.mod(4)\n3\n```\n\nI recommend we redefine\n\n```\ndef div(self, other):\n    q,_ = self.quo_rem(other)\n    return q\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2579\n\n",
    "closed_at": "2008-03-20T00:18:51Z",
    "created_at": "2008-03-18T01:29:11Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, positive review] Inconsistency in integer quotient",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2579",
    "user": "https://github.com/rishikesha"
}
```
Assignee: somebody

```
sage: a=-17
sage: a//4
-5
sage: a.div(4)
-4
sage: a.mod(4)
3
```

I recommend we redefine

```
def div(self, other):
    q,_ = self.quo_rem(other)
    return q
```

Issue created by migration from https://trac.sagemath.org/ticket/2579





---

archive/issue_comments_017602.json:
```json
{
    "body": "sage: a=-17 \n\nsage: a//4 \n\n-5 \n\nsage: a.div(4)\n\n-4 \n\nsage: a.mod(4)\n\n3\n\nI recommend we redefine\n\ndef div(self, other):\n\n    q,_ = self.quo_rem(other) \n\n    return q",
    "created_at": "2008-03-18T01:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2579#issuecomment-17602",
    "user": "https://github.com/rishikesha"
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

archive/issue_comments_017603.json:
```json
{
    "body": "If we want a.div(b) to be floor(a/b) (which I agree we probably do, if we want the method to exist at all), the correct fix is to change from mpz_tdiv_qr to mpz_fdiv_q.",
    "created_at": "2008-03-18T02:21:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2579#issuecomment-17603",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

If we want a.div(b) to be floor(a/b) (which I agree we probably do, if we want the method to exist at all), the correct fix is to change from mpz_tdiv_qr to mpz_fdiv_q.



---

archive/issue_comments_017604.json:
```json
{
    "body": "I think the basis logic should be as below. Since this will make the remainder always positive.\n\n```\nif mpz_sgn(_other.value) == 1:\n            mpz_fdiv_q(q.value, _self.value, _other.value)        \nelse:\n            mpz_cdiv_q(q.value, _self.value, _other.value)\n```",
    "created_at": "2008-03-18T03:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2579#issuecomment-17604",
    "user": "https://github.com/rishikesha"
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

archive/issue_comments_017605.json:
```json
{
    "body": "Attachment [integerdiv.patch](tarball://root/attachments/some-uuid/ticket2579/integerdiv.patch) by @rishikesha created at 2008-03-19 17:01:18",
    "created_at": "2008-03-19T17:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2579#issuecomment-17605",
    "user": "https://github.com/rishikesha"
}
```

Attachment [integerdiv.patch](tarball://root/attachments/some-uuid/ticket2579/integerdiv.patch) by @rishikesha created at 2008-03-19 17:01:18



---

archive/issue_comments_017606.json:
```json
{
    "body": "I used quo_rem to redefine div. I would have essentially copied and pasted quo_rem otherwise.",
    "created_at": "2008-03-19T17:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2579#issuecomment-17606",
    "user": "https://github.com/rishikesha"
}
```

I used quo_rem to redefine div. I would have essentially copied and pasted quo_rem otherwise.



---

archive/issue_comments_017607.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-03-19T20:31:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2579#issuecomment-17607",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_006031.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-20T00:18:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2579#event-6031"
}
```



---

archive/issue_comments_017608.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-20T00:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2579#issuecomment-17608",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha0



---

archive/issue_comments_017609.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-20T00:18:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2579#issuecomment-17609",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
