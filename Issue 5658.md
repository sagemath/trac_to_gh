# Issue 5658: Efficiency improvement in generic order_from_multiple()

archive/issues_005658.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @rhinton\n\nKeywords: generic group order\n\nRyan Hinton pointed out that for groups of prime order n every non-identity element has order n.  The current implementation of order_from_multiple() computes `g^n` twice when g is not the identity and n is prime.\n\nThe attached patch avoids this: for each prime p dividing the given multiple M of the order, we avoid the last multiplication/powering by p, so there is a saving whenever the p-exponent of the order is maximal.\n\nIn an example where the order is `2^1279-1` (a Mersenne prime) the times was reduced from 100ms to 70ms.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5658\n\n",
    "created_at": "2009-04-01T15:04:57Z",
    "labels": [
        "component: algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Efficiency improvement in generic order_from_multiple()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5658",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: tbd

CC:  @rhinton

Keywords: generic group order

Ryan Hinton pointed out that for groups of prime order n every non-identity element has order n.  The current implementation of order_from_multiple() computes `g^n` twice when g is not the identity and n is prime.

The attached patch avoids this: for each prime p dividing the given multiple M of the order, we avoid the last multiplication/powering by p, so there is a saving whenever the p-exponent of the order is maximal.

In an example where the order is `2^1279-1` (a Mersenne prime) the times was reduced from 100ms to 70ms.

Issue created by migration from https://trac.sagemath.org/ticket/5658





---

archive/issue_comments_044152.json:
```json
{
    "body": "Attachment [generic_order.patch](tarball://root/attachments/some-uuid/ticket5658/generic_order.patch) by @JohnCremona created at 2009-04-01 15:05:19\n\nbased on 3.4.1.alpha0",
    "created_at": "2009-04-01T15:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5658#issuecomment-44152",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [generic_order.patch](tarball://root/attachments/some-uuid/ticket5658/generic_order.patch) by @JohnCremona created at 2009-04-01 15:05:19

based on 3.4.1.alpha0



---

archive/issue_comments_044153.json:
```json
{
    "body": "Patch applies cleanly and passes doctests.  I don't understand what `val_unit` does, so I am unsure whether I'm qualified to give a positive review.",
    "created_at": "2009-04-01T15:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5658#issuecomment-44153",
    "user": "https://github.com/rhinton"
}
```

Patch applies cleanly and passes doctests.  I don't understand what `val_unit` does, so I am unsure whether I'm qualified to give a positive review.



---

archive/issue_comments_044154.json:
```json
{
    "body": "Thanks for the fast review.\n\nHere is what val_unit does.  Given a nonzero integer or rational n and a prime p, you can write n uniquely as `n = m*p^e` where m is not divisible by p (if rational, neither the numerator nor the denominator of m is divisible by p).   We call e the valuation of m at p  (which can be obtained on its own by n.valuation(p)) and m the \"unit\" part of n at p (which can be obtained on its own by n.prime_to_m_part(p)).  Using val_unit() gives these together which is more efficient as they are computed together.\n\nIt's an operation frequently needed in number theory!\n\nI added \"needs review\" which I forgot to do earlier.  If you are happy with val_unit() you can change that, or I can hit someone else to take a look.",
    "created_at": "2009-04-01T15:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5658#issuecomment-44154",
    "user": "https://github.com/JohnCremona"
}
```

Thanks for the fast review.

Here is what val_unit does.  Given a nonzero integer or rational n and a prime p, you can write n uniquely as `n = m*p^e` where m is not divisible by p (if rational, neither the numerator nor the denominator of m is divisible by p).   We call e the valuation of m at p  (which can be obtained on its own by n.valuation(p)) and m the "unit" part of n at p (which can be obtained on its own by n.prime_to_m_part(p)).  Using val_unit() gives these together which is more efficient as they are computed together.

It's an operation frequently needed in number theory!

I added "needs review" which I forgot to do earlier.  If you are happy with val_unit() you can change that, or I can hit someone else to take a look.



---

archive/issue_comments_044155.json:
```json
{
    "body": "Sounds good to me!",
    "created_at": "2009-04-01T16:19:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5658#issuecomment-44155",
    "user": "https://github.com/rhinton"
}
```

Sounds good to me!



---

archive/issue_comments_044156.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-02T00:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5658#issuecomment-44156",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc0.

Cheers,

Michael



---

archive/issue_events_005901.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-02T00:06:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5658",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5658#event-5901"
}
```



---

archive/issue_comments_044157.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-02T00:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5658#issuecomment-44157",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
