# Issue 252: Make number fields work when polynomial not integral or not monic.

archive/issues_000252.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @katestange bouillaguet\n\nMake number fields work when polynomial not integral or not monic.\n\n```\nsage: R.<x> = QQ[]\nsage: L.<b> = NumberField(x^2-1/2)\nsage: L.discriminant()\nTraceback (most recent call last):\n...\ngen.PariError:  (8)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/252\n\n",
    "created_at": "2007-02-08T17:49:51Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Make number fields work when polynomial not integral or not monic.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/252",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @katestange bouillaguet

Make number fields work when polynomial not integral or not monic.

```
sage: R.<x> = QQ[]
sage: L.<b> = NumberField(x^2-1/2)
sage: L.discriminant()
Traceback (most recent call last):
...
gen.PariError:  (8)
```

Issue created by migration from https://trac.sagemath.org/ticket/252





---

archive/issue_comments_001102.json:
```json
{
    "body": "You may find sage.rings.algebraic_real.clear_denominators() useful here.  (If so, the function should probably be moved to a more sensible place, and perhaps renamed.)",
    "created_at": "2007-10-09T04:31:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1102",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

You may find sage.rings.algebraic_real.clear_denominators() useful here.  (If so, the function should probably be moved to a more sensible place, and perhaps renamed.)



---

archive/issue_comments_001103.json:
```json
{
    "body": "The example above works.  But other things don't:\n\n```\nsage: R.<x> = QQ[]\nsage: sage: L.<b> = NumberField(x^2-1/2)\nsage: sage: L.discriminant()\n8\nsage: L.ring_of_integers()\nboom\n```",
    "created_at": "2007-10-21T01:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1103",
    "user": "https://github.com/williamstein"
}
```

The example above works.  But other things don't:

```
sage: R.<x> = QQ[]
sage: sage: L.<b> = NumberField(x^2-1/2)
sage: sage: L.discriminant()
8
sage: L.ring_of_integers()
boom
```



---

archive/issue_events_000527.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-21T01:59:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/252#event-527"
}
```



---

archive/issue_comments_001104.json:
```json
{
    "body": "Notice that #4041 is a duplicate of this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T17:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1104",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Notice that #4041 is a duplicate of this ticket.

Cheers,

Michael



---

archive/issue_comments_001105.json:
```json
{
    "body": "Changing component from number theory to number fields.",
    "created_at": "2009-07-20T19:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1105",
    "user": "https://github.com/loefflerd"
}
```

Changing component from number theory to number fields.



---

archive/issue_comments_001106.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-07-20T19:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1106",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_001107.json:
```json
{
    "body": "Another example from #9408\n\n```\nsage: L.<a,b> = QQ[i].relativize(1) #Ok\nsage: L.<a,b> = QQ[i].relativize(1/2) #PariError\n```",
    "created_at": "2010-07-06T10:59:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1107",
    "user": "https://github.com/lftabera"
}
```

Another example from #9408

```
sage: L.<a,b> = QQ[i].relativize(1) #Ok
sage: L.<a,b> = QQ[i].relativize(1/2) #PariError
```



---

archive/issue_comments_001108.json:
```json
{
    "body": "At least the pari errors could be changed to \"not implemented\" messages in the meantime?  This is an error a new user may encounter.  It would help them to know immediately that the problem is all non-integral coefficients, so they can program around it, and to know that it is known to the developers.",
    "created_at": "2011-02-16T16:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1108",
    "user": "https://github.com/katestange"
}
```

At least the pari errors could be changed to "not implemented" messages in the meantime?  This is an error a new user may encounter.  It would help them to know immediately that the problem is all non-integral coefficients, so they can program around it, and to know that it is known to the developers.



---

archive/issue_comments_001109.json:
```json
{
    "body": "I agree that fixing this would be very nice, but also would require completely reworking the number field code.  I think it is feasible, but do we really want to put that much effort into this?",
    "created_at": "2011-10-09T11:03:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1109",
    "user": "https://github.com/jdemeyer"
}
```

I agree that fixing this would be very nice, but also would require completely reworking the number field code.  I think it is feasible, but do we really want to put that much effort into this?



---

archive/issue_comments_001110.json:
```json
{
    "body": "I, for myself would like to see this fixed. I would fix this myself if I had time...\n\nIn any case, current situation in Sage is not admissible. If we decide not to fix this then, should we allow to define number fields with nonintegral generators? This would also mean a lot of effort.",
    "created_at": "2011-10-09T12:35:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1110",
    "user": "https://github.com/lftabera"
}
```

I, for myself would like to see this fixed. I would fix this myself if I had time...

In any case, current situation in Sage is not admissible. If we decide not to fix this then, should we allow to define number fields with nonintegral generators? This would also mean a lot of effort.



---

archive/issue_comments_001111.json:
```json
{
    "body": "Replying to [comment:9 jdemeyer]:\n> I agree that fixing this would be very nice, but also would require \n> completely reworking the number field code.  I think it is feasible,\n> but do we really want to put that much effort into this?\n\n\nI don't know about \"we\", but it is a total no brainer that this has to get done eventually.   It is certainly easier than writing the number field code in the first place, which was hard, but not that hard.",
    "created_at": "2011-10-09T16:00:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1111",
    "user": "https://github.com/williamstein"
}
```

Replying to [comment:9 jdemeyer]:
> I agree that fixing this would be very nice, but also would require 
> completely reworking the number field code.  I think it is feasible,
> but do we really want to put that much effort into this?


I don't know about "we", but it is a total no brainer that this has to get done eventually.   It is certainly easier than writing the number field code in the first place, which was hard, but not that hard.



---

archive/issue_events_000528.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/Bouillaguet",
    "created_at": "2013-02-19T20:45:34Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/252#event-528"
}
```



---

archive/issue_events_000529.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/Bouillaguet",
    "created_at": "2013-02-19T20:45:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "milestone": "sage-5.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/252#event-529"
}
```



---

archive/issue_comments_001112.json:
```json
{
    "body": "I just ran into this issue",
    "created_at": "2013-02-19T20:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1112",
    "user": "https://trac.sagemath.org/admin/accounts/users/Bouillaguet"
}
```

I just ran into this issue



---

archive/issue_events_000530.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:34:36Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "milestone": "sage-5.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/252#event-530"
}
```



---

archive/issue_events_000531.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:34:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/252#event-531"
}
```



---

archive/issue_events_000532.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/252#event-532"
}
```



---

archive/issue_events_000533.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/252#event-533"
}
```



---

archive/issue_events_000534.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/252#event-534"
}
```



---

archive/issue_events_000535.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/252#event-535"
}
```



---

archive/issue_events_000536.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/252#event-536"
}
```



---

archive/issue_events_000537.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/252#event-537"
}
```



---

archive/issue_comments_001113.json:
```json
{
    "body": "In SageMath 6.7.beta1:\n\n```\nsage: R.<x> = QQ[]\nsage: L.<b> = NumberField(x^2-1/2)\nsage: L.discriminant()\n8\nsage: L.ring_of_integers()\nMaximal Order in Number Field in b with defining polynomial x^2 - 1/2\n```\nHowever, there are still problems; see e.g. #18243.  We should make use of the fact that when one feeds a non-monic or non-integral polynomial `f` to PARI's `nfinit()`, it returns a pair `[nf, c]` where `nf` is an number field isomorphic to **Q**[*x*]/(*f*) and defined by a monic integral polynomial, and `c` is a root of `f` in `nf`.",
    "created_at": "2015-04-17T22:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1113",
    "user": "https://github.com/pjbruin"
}
```

In SageMath 6.7.beta1:

```
sage: R.<x> = QQ[]
sage: L.<b> = NumberField(x^2-1/2)
sage: L.discriminant()
8
sage: L.ring_of_integers()
Maximal Order in Number Field in b with defining polynomial x^2 - 1/2
```
However, there are still problems; see e.g. #18243.  We should make use of the fact that when one feeds a non-monic or non-integral polynomial `f` to PARI's `nfinit()`, it returns a pair `[nf, c]` where `nf` is an number field isomorphic to **Q**[*x*]/(*f*) and defined by a monic integral polynomial, and `c` is a root of `f` in `nf`.



---

archive/issue_comments_001114.json:
```json
{
    "body": "This branch is work in progress; it does not solve #18243 yet, and there are probably other places where it should be checked that non-integral and/or non-monic polynomials are supported.",
    "created_at": "2015-06-19T20:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1114",
    "user": "https://github.com/pjbruin"
}
```

This branch is work in progress; it does not solve #18243 yet, and there are probably other places where it should be checked that non-integral and/or non-monic polynomials are supported.



---

archive/issue_comments_001115.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-06-22T20:40:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1115",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_001116.json:
```json
{
    "body": "The examples in #14164 and #18243 now work.  This is mostly finished, but it needs more doctests to show that number fields defined by non-monic and non-integral polynomials are supported.",
    "created_at": "2015-06-22T20:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1116",
    "user": "https://github.com/pjbruin"
}
```

The examples in #14164 and #18243 now work.  This is mostly finished, but it needs more doctests to show that number fields defined by non-monic and non-integral polynomials are supported.



---

archive/issue_comments_001117.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-06-24T10:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1117",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_001118.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-06-24T10:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1118",
    "user": "https://github.com/pjbruin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_001119.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-07-03T09:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1119",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_001120.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-07-22T11:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1120",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_001121.json:
```json
{
    "body": "The above version fixes `composite_fields()` to correctly solve #14164 and #18243.",
    "created_at": "2015-07-22T11:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1121",
    "user": "https://github.com/pjbruin"
}
```

The above version fixes `composite_fields()` to correctly solve #14164 and #18243.



---

archive/issue_comments_001122.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-08-21T07:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1122",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_001123.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-08-22T22:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1123",
    "user": "https://trac.sagemath.org/admin/accounts/users/kartikv"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_001124.json:
```json
{
    "body": "Something weird seems to be going on with factoring. This is \"normal\" behavior for a number field.\n\n```\nsage: F.<a> = NumberField(x^3+x+1)\nsage: F(2).factor()\n2\nsage: F(3).factor()\n(a^2 + a + 2) * (-a + 1)\nsage: (a^2 + a + 2).factor()\na^2 + a + 2\nsage: F.factor(3)\n(Fractional ideal (a^2 + a + 2)) * (Fractional ideal (-a + 1))\nsage: (-a+1).factor()\n-a + 1\n```\n\nThis is not.\n\n```\nsage: F.<a> = NumberField(2*x^3+x+1)\nsage: F(2).factor()\n(-47*a^2 + 21*a - 93/2) * (-1/2*a^2 + 1/2*a)^2 * (1/2*a^2 + 1/2*a)\nsage: F.factor(2)\n(Fractional ideal (-1/2*a^2 + 1/2*a))^2 * (Fractional ideal (1/2*a^2 + 1/2*a))\nsage: (-47*a^2 + 21*a - 93/2).norm()\n-8192\nsage: (-47*a^2 + 21*a - 93/2).factor()\n(3718815975/16384*a^2 - 1336872061/16384*a + 7884913157/32768) * (-1/2*a^2 + 1/2*a)^14 * (1/2*a^2 + 1/2*a)^-1\nsage: (1/2*a^2 + 1/2*a).factor()\n(13/512*a^2 - 11/512*a - 7/256) * (-1/2*a^2 + 1/2*a)^-4\n```\n\nSomehow, it's not controlling primes over the leading coefficient properly...",
    "created_at": "2015-08-22T22:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1124",
    "user": "https://trac.sagemath.org/admin/accounts/users/kartikv"
}
```

Something weird seems to be going on with factoring. This is "normal" behavior for a number field.

```
sage: F.<a> = NumberField(x^3+x+1)
sage: F(2).factor()
2
sage: F(3).factor()
(a^2 + a + 2) * (-a + 1)
sage: (a^2 + a + 2).factor()
a^2 + a + 2
sage: F.factor(3)
(Fractional ideal (a^2 + a + 2)) * (Fractional ideal (-a + 1))
sage: (-a+1).factor()
-a + 1
```

This is not.

```
sage: F.<a> = NumberField(2*x^3+x+1)
sage: F(2).factor()
(-47*a^2 + 21*a - 93/2) * (-1/2*a^2 + 1/2*a)^2 * (1/2*a^2 + 1/2*a)
sage: F.factor(2)
(Fractional ideal (-1/2*a^2 + 1/2*a))^2 * (Fractional ideal (1/2*a^2 + 1/2*a))
sage: (-47*a^2 + 21*a - 93/2).norm()
-8192
sage: (-47*a^2 + 21*a - 93/2).factor()
(3718815975/16384*a^2 - 1336872061/16384*a + 7884913157/32768) * (-1/2*a^2 + 1/2*a)^14 * (1/2*a^2 + 1/2*a)^-1
sage: (1/2*a^2 + 1/2*a).factor()
(13/512*a^2 - 11/512*a - 7/256) * (-1/2*a^2 + 1/2*a)^-4
```

Somehow, it's not controlling primes over the leading coefficient properly...



---

archive/issue_comments_001125.json:
```json
{
    "body": "The underlying problem seems to be converting PARI ideals in Hilbert normal form to Sage ideals:\n\n```\nsage: F.<a> = NumberField(2*x^3+x+1)\nsage: Fp = F.pari_nf()\nsage: I = F.ideal(2)\nsage: Ip = I.pari_hnf()\nsage: fact = Fp.idealfactor(Ip)\nsage: Jp = fact[0, 0]\nsage: Fp.idealnorm(Jp)\n2\nsage: J = F.ideal(Jp)\nsage: J.norm()\n1/2             # should be 2, like Fp.idealnorm(Jp)\n```",
    "created_at": "2015-08-24T13:29:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1125",
    "user": "https://github.com/pjbruin"
}
```

The underlying problem seems to be converting PARI ideals in Hilbert normal form to Sage ideals:

```
sage: F.<a> = NumberField(2*x^3+x+1)
sage: Fp = F.pari_nf()
sage: I = F.ideal(2)
sage: Ip = I.pari_hnf()
sage: fact = Fp.idealfactor(Ip)
sage: Jp = fact[0, 0]
sage: Fp.idealnorm(Jp)
2
sage: J = F.ideal(Jp)
sage: J.norm()
1/2             # should be 2, like Fp.idealnorm(Jp)
```



---

archive/issue_comments_001126.json:
```json
{
    "body": "Actually the bug is in the conversion from PARI elements expressed on the integral basis:\n\n```\nsage: F.<a> = NumberField(2*x^3+x+1)\nsage: b = F.random_element()\nsage: F(F.pari_nf().nfalgtobasis(b)) == b\nFalse  # should be True\n```\nI'm working on a patch.",
    "created_at": "2015-08-24T16:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1126",
    "user": "https://github.com/pjbruin"
}
```

Actually the bug is in the conversion from PARI elements expressed on the integral basis:

```
sage: F.<a> = NumberField(2*x^3+x+1)
sage: b = F.random_element()
sage: F(F.pari_nf().nfalgtobasis(b)) == b
False  # should be True
```
I'm working on a patch.



---

archive/issue_comments_001127.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-08-24T17:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1127",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_001128.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-08-24T17:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1128",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_001129.json:
```json
{
    "body": "Positive review. I think there should probably be an example in the docstring to NumberField that demonstrates/tests this functionality (since it has been missing for so long), but otherwise ready to submit. You're welcome to use my example or any of yours from deeper in the number field code.",
    "created_at": "2015-08-24T17:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1129",
    "user": "https://trac.sagemath.org/admin/accounts/users/kartikv"
}
```

Positive review. I think there should probably be an example in the docstring to NumberField that demonstrates/tests this functionality (since it has been missing for so long), but otherwise ready to submit. You're welcome to use my example or any of yours from deeper in the number field code.



---

archive/issue_comments_001130.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-08-24T17:53:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1130",
    "user": "https://trac.sagemath.org/admin/accounts/users/kartikv"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_001131.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-08-25T11:38:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1131",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_001132.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-08-25T11:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1132",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_001133.json:
```json
{
    "body": "Replying to [comment:33 kartikv]:\n> Positive review. I think there should probably be an example in the docstring to NumberField that demonstrates/tests this functionality (since it has been missing for so long), but otherwise ready to submit. You're welcome to use my example or any of yours from deeper in the number field code.\n\nThanks for your comments.  If you approve of the new examples you can set this to positive review (and remember to fill in your [real] name as reviewer).",
    "created_at": "2015-08-25T11:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1133",
    "user": "https://github.com/pjbruin"
}
```

Replying to [comment:33 kartikv]:
> Positive review. I think there should probably be an example in the docstring to NumberField that demonstrates/tests this functionality (since it has been missing for so long), but otherwise ready to submit. You're welcome to use my example or any of yours from deeper in the number field code.

Thanks for your comments.  If you approve of the new examples you can set this to positive review (and remember to fill in your [real] name as reviewer).



---

archive/issue_comments_001134.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-08-25T11:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1134",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_001135.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-08-25T13:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1135",
    "user": "https://trac.sagemath.org/admin/accounts/users/kartikv"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_001136.json:
```json
{
    "body": "Perfect.",
    "created_at": "2015-08-25T13:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1136",
    "user": "https://trac.sagemath.org/admin/accounts/users/kartikv"
}
```

Perfect.



---

archive/issue_events_000538.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-08-26T03:00:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/252#event-538"
}
```



---

archive/issue_comments_001137.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-08-26T03:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/252#issuecomment-1137",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
