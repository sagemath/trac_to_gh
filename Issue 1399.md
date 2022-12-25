# Issue 1399: Problems with arithmetic

archive/issues_001399.json:
```json
{
    "body": "Assignee: somebody\n\nThere are some operations which are either unimplemented or give (what I would consider to be) wrong answers:\n\nN=-7\n\nN.is_prime()\n>>false\n\nI believe that this should give the answer \"true\".\n\nAlso, if one tries\n`ZZ.ideal(N).is_prime()`\n\none gets a NotImplementedError.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1399\n\n",
    "created_at": "2007-12-04T22:49:22Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Problems with arithmetic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1399",
    "user": "https://trac.sagemath.org/admin/accounts/users/ljpk"
}
```
Assignee: somebody

There are some operations which are either unimplemented or give (what I would consider to be) wrong answers:

N=-7

N.is_prime()
>>false

I believe that this should give the answer "true".

Also, if one tries
`ZZ.ideal(N).is_prime()`

one gets a NotImplementedError.

Issue created by migration from https://trac.sagemath.org/ticket/1399





---

archive/issue_events_003611.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-04T23:23:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1399#event-3611"
}
```



---

archive/issue_comments_008988.json:
```json
{
    "body": "Apply this patch after #1398 .",
    "created_at": "2007-12-06T04:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1399#issuecomment-8988",
    "user": "https://github.com/mwhansen"
}
```

Apply this patch after #1398 .



---

archive/issue_comments_008989.json:
```json
{
    "body": "Changing assignee from somebody to @mwhansen.",
    "created_at": "2007-12-06T04:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1399#issuecomment-8989",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from somebody to @mwhansen.



---

archive/issue_comments_008990.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-06T04:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1399#issuecomment-8990",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008991.json:
```json
{
    "body": "Attachment [1399.patch](tarball://root/attachments/some-uuid/ticket1399/1399.patch) by @mwhansen created at 2007-12-06 04:47:17",
    "created_at": "2007-12-06T04:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1399#issuecomment-8991",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1399.patch](tarball://root/attachments/some-uuid/ticket1399/1399.patch) by @mwhansen created at 2007-12-06 04:47:17



---

archive/issue_comments_008992.json:
```json
{
    "body": "NO!!!!!!\n\nThe change to ideal.py is fine, but making is_prime(-7) return True is *wrong*.\n\nJustification:\n\n```\nsage: gp.eval('isprime(-7)')\n'0'\nsage: prime_range(-10,10)\n[2, 3, 5, 7]\n```\n\nand in Wikipedia it says:\n \n\"In mathematics, a prime number (or a prime) is a natural number which has exactly two distinct natural number divisors: 1 and itself.\"\n\nand more importantly it says the same thing in my elementary number theory book.\n\nSo NO.\n\nHowever, the change to ideal.py is fine.",
    "created_at": "2007-12-13T23:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1399#issuecomment-8992",
    "user": "https://github.com/williamstein"
}
```

NO!!!!!!

The change to ideal.py is fine, but making is_prime(-7) return True is *wrong*.

Justification:

```
sage: gp.eval('isprime(-7)')
'0'
sage: prime_range(-10,10)
[2, 3, 5, 7]
```

and in Wikipedia it says:
 
"In mathematics, a prime number (or a prime) is a natural number which has exactly two distinct natural number divisors: 1 and itself."

and more importantly it says the same thing in my elementary number theory book.

So NO.

However, the change to ideal.py is fine.



---

archive/issue_comments_008993.json:
```json
{
    "body": "Oh, I should add that  Magma defines -7 to be Prime\n\n\n```\nsage: magma.eval('IsPrime(-7)')\n'true'\n```\n",
    "created_at": "2007-12-13T23:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1399#issuecomment-8993",
    "user": "https://github.com/williamstein"
}
```

Oh, I should add that  Magma defines -7 to be Prime


```
sage: magma.eval('IsPrime(-7)')
'true'
```




---

archive/issue_comments_008994.json:
```json
{
    "body": "Note:\n\n```\nsage: I = ZZ.ideal(-7)\nsage: I.gens()\n(-7,)\n```\n\nIf the change to integer.pyx isn't accepted, then the change to ideal.py needs to account for -1.",
    "created_at": "2007-12-13T23:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1399#issuecomment-8994",
    "user": "https://github.com/rlmill"
}
```

Note:

```
sage: I = ZZ.ideal(-7)
sage: I.gens()
(-7,)
```

If the change to integer.pyx isn't accepted, then the change to ideal.py needs to account for -1.



---

archive/issue_events_003612.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-12-16T00:07:17Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1399#event-3612"
}
```



---

archive/issue_events_003613.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-12-16T00:07:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1399#event-3613"
}
```



---

archive/issue_comments_008995.json:
```json
{
    "body": "Attachment [1399new.patch](tarball://root/attachments/some-uuid/ticket1399/1399new.patch) by @JohnCremona created at 2008-02-16 18:33:04\n\nRevised patch by John Cremona",
    "created_at": "2008-02-16T18:33:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1399#issuecomment-8995",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [1399new.patch](tarball://root/attachments/some-uuid/ticket1399/1399new.patch) by @JohnCremona created at 2008-02-16 18:33:04

Revised patch by John Cremona



---

archive/issue_comments_008996.json:
```json
{
    "body": "Replacement patch handles these issues as follows:\n\n* for Integers the method is_prime() only returns True for _positive_ primes, as agreed.\n* Integers have a new method is_irreducible() which is True for +p and -p where p is prime\n* the is_prime() method for ideals in a PID is almost as in mhansen's patch, but it tests if the generator is_irreducible() rather than is_prime().  So not only does it work properly for integer ideals, it also now works for ideals in polynomial rings (in one variable) over a field -- see doctests.\n* All relevant doctests have been updated\n* I changed IntegerModRing(n) to work for negative n (it just uses -n instead) which makes sense to me.",
    "created_at": "2008-02-16T18:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1399#issuecomment-8996",
    "user": "https://github.com/JohnCremona"
}
```

Replacement patch handles these issues as follows:

* for Integers the method is_prime() only returns True for _positive_ primes, as agreed.
* Integers have a new method is_irreducible() which is True for +p and -p where p is prime
* the is_prime() method for ideals in a PID is almost as in mhansen's patch, but it tests if the generator is_irreducible() rather than is_prime().  So not only does it work properly for integer ideals, it also now works for ideals in polynomial rings (in one variable) over a field -- see doctests.
* All relevant doctests have been updated
* I changed IntegerModRing(n) to work for negative n (it just uses -n instead) which makes sense to me.



---

archive/issue_comments_008997.json:
```json
{
    "body": "to be applied after 1399new.patch",
    "created_at": "2008-02-16T18:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1399#issuecomment-8997",
    "user": "https://github.com/JohnCremona"
}
```

to be applied after 1399new.patch



---

archive/issue_comments_008998.json:
```json
{
    "body": "Attachment [1399newextra.patch](tarball://root/attachments/some-uuid/ticket1399/1399newextra.patch) by @JohnCremona created at 2008-02-16 18:54:20\n\nSmall addendum to previous:  I forgot to return True for the zero ideal (which is prime in a PID!)\nBoth patches 1399new.patch and 1399newextra.patch shold be applied.",
    "created_at": "2008-02-16T18:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1399#issuecomment-8998",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [1399newextra.patch](tarball://root/attachments/some-uuid/ticket1399/1399newextra.patch) by @JohnCremona created at 2008-02-16 18:54:20

Small addendum to previous:  I forgot to return True for the zero ideal (which is prime in a PID!)
Both patches 1399new.patch and 1399newextra.patch shold be applied.



---

archive/issue_comments_008999.json:
```json
{
    "body": "Very nice. Code looks good to me, all doctests pass after applying 1399new.patch and 1399newextra.patch to 2.10.1.",
    "created_at": "2008-02-23T13:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1399#issuecomment-8999",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Very nice. Code looks good to me, all doctests pass after applying 1399new.patch and 1399newextra.patch to 2.10.1.



---

archive/issue_comments_009000.json:
```json
{
    "body": "Attachment [sage-1399-3_of_3.patch](tarball://root/attachments/some-uuid/ticket1399/sage-1399-3_of_3.patch) by @williamstein created at 2008-02-24 21:07:52",
    "created_at": "2008-02-24T21:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1399#issuecomment-9000",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-1399-3_of_3.patch](tarball://root/attachments/some-uuid/ticket1399/sage-1399-3_of_3.patch) by @williamstein created at 2008-02-24 21:07:52



---

archive/issue_comments_009001.json:
```json
{
    "body": "Apply the last three patches in order.",
    "created_at": "2008-02-24T21:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1399#issuecomment-9001",
    "user": "https://github.com/williamstein"
}
```

Apply the last three patches in order.



---

archive/issue_events_003614.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-24T21:19:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1399#event-3614"
}
```



---

archive/issue_comments_009002.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-24T21:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1399#issuecomment-9002",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009003.json:
```json
{
    "body": "Merged 1399new.patch, 1399newextra.patch and sage-1399-3_of_3.patch in Sage 2.10.3.alpha0",
    "created_at": "2008-02-24T21:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1399#issuecomment-9003",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 1399new.patch, 1399newextra.patch and sage-1399-3_of_3.patch in Sage 2.10.3.alpha0
