# Issue 5250: But in multiplicative_generator function for Z/NZ

archive/issues_005250.json:
```json
{
    "body": "Assignee: @williamstein\n\nNotice that (ZZ/162ZZ)^* *is* cyclic:\n\n```\nsage: R = Integers(162)\nsage: R(5).multiplicative_order()\n54\nsage: euler_phi(162)\n54\n```\n\nHowever, Sage gets this totally wrong:\n\n```\nsage: R.multiplicative_generator()\nTraceback (most recent call last):\n...\nValueError: multiplicative group of this ring is not cyclic\n```\n\nThis bug came up for me today while doing some research.  I'm glad I didn't believe Sage :-). \n\nIssue created by migration from https://trac.sagemath.org/ticket/5250\n\n",
    "created_at": "2009-02-12T23:41:54Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "But in multiplicative_generator function for Z/NZ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5250",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Notice that (ZZ/162ZZ)^* *is* cyclic:

```
sage: R = Integers(162)
sage: R(5).multiplicative_order()
54
sage: euler_phi(162)
54
```

However, Sage gets this totally wrong:

```
sage: R.multiplicative_generator()
Traceback (most recent call last):
...
ValueError: multiplicative group of this ring is not cyclic
```

This bug came up for me today while doing some research.  I'm glad I didn't believe Sage :-). 

Issue created by migration from https://trac.sagemath.org/ticket/5250





---

archive/issue_comments_040189.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-06T14:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40189",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040190.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-05-06T14:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40190",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_040191.json:
```json
{
    "body": "This comes up whenever n is twice a power of an odd prime. In these cases, `multiplicative_group_is_cyclic` would wrongly return False, `multiplicative_generator` would throw an error and `unit_gens` would return a list of length 2 one of whose elements is 1.\n\nThe attached patch fixes this. It also streamlines the code a bit by using the is_prime_power function; this is more readable, and in theory should be quicker than factorisation. At the moment it is actually a tiny fraction slower, but this is a consequence of an awkward workaround for a Pari bug (see #4777) and it will presumably be fixed in the future.",
    "created_at": "2009-05-06T14:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40191",
    "user": "https://github.com/loefflerd"
}
```

This comes up whenever n is twice a power of an odd prime. In these cases, `multiplicative_group_is_cyclic` would wrongly return False, `multiplicative_generator` would throw an error and `unit_gens` would return a list of length 2 one of whose elements is 1.

The attached patch fixes this. It also streamlines the code a bit by using the is_prime_power function; this is more readable, and in theory should be quicker than factorisation. At the moment it is actually a tiny fraction slower, but this is a consequence of an awkward workaround for a Pari bug (see #4777) and it will presumably be fixed in the future.



---

archive/issue_comments_040192.json:
```json
{
    "body": "Oops, just realised that this breaks one or two doctests (because various functions expect the list of unit gens to contain 1's).",
    "created_at": "2009-05-06T14:40:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40192",
    "user": "https://github.com/loefflerd"
}
```

Oops, just realised that this breaks one or two doctests (because various functions expect the list of unit gens to contain 1's).



---

archive/issue_comments_040193.json:
```json
{
    "body": "Attachment [trac_5250.patch](tarball://root/attachments/some-uuid/ticket5250/trac_5250.patch) by @loefflerd created at 2009-05-07 15:48:46\n\npatch against 3.4.2.final",
    "created_at": "2009-05-07T15:48:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40193",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5250.patch](tarball://root/attachments/some-uuid/ticket5250/trac_5250.patch) by @loefflerd created at 2009-05-07 15:48:46

patch against 3.4.2.final



---

archive/issue_comments_040194.json:
```json
{
    "body": "Here's a patch that fixes the (relatively easy) bug in multiplicative_generator and the (much deeper) bug in multiplicative_subgroups. The latter is written in such a way that it should be very easy to transplant into was's new framework for Abelian groups based on 5882.",
    "created_at": "2009-05-07T15:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40194",
    "user": "https://github.com/loefflerd"
}
```

Here's a patch that fixes the (relatively easy) bug in multiplicative_generator and the (much deeper) bug in multiplicative_subgroups. The latter is written in such a way that it should be very easy to transplant into was's new framework for Abelian groups based on 5882.



---

archive/issue_comments_040195.json:
```json
{
    "body": "A valiant job: if I come against something which depends on adding functionality to abelian groups I just give up, but you did it.  (In my ideal world every finite abelian group would internally be stored and work with elementary divisors, which would make the code simpler.  Never mind).\n\nExpecting to review this over the weekend.",
    "created_at": "2009-05-08T19:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40195",
    "user": "https://github.com/JohnCremona"
}
```

A valiant job: if I come against something which depends on adding functionality to abelian groups I just give up, but you did it.  (In my ideal world every finite abelian group would internally be stored and work with elementary divisors, which would make the code simpler.  Never mind).

Expecting to review this over the weekend.



---

archive/issue_comments_040196.json:
```json
{
    "body": "Positive review.  The code looks ok to me, applies to 3.4.2 and tests pass (I tested abelian_groups and all modular).\n\nNo doubt the subgroups function in abelian groups will be superseded one day (after #5882) but that's no reason to stop this.  And both the original bugs are fixed.",
    "created_at": "2009-05-09T17:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40196",
    "user": "https://github.com/JohnCremona"
}
```

Positive review.  The code looks ok to me, applies to 3.4.2 and tests pass (I tested abelian_groups and all modular).

No doubt the subgroups function in abelian groups will be superseded one day (after #5882) but that's no reason to stop this.  And both the original bugs are fixed.



---

archive/issue_comments_040197.json:
```json
{
    "body": "Michael: don't merge this one quite yet -- it breaks one of the new doctests I added as part of #4357, so if you apply both patches you will get a doctest failure in sage/modular/modform/ambient_eps.py. I will do yet another patch to sort this out.",
    "created_at": "2009-05-10T20:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40197",
    "user": "https://github.com/loefflerd"
}
```

Michael: don't merge this one quite yet -- it breaks one of the new doctests I added as part of #4357, so if you apply both patches you will get a doctest failure in sage/modular/modform/ambient_eps.py. I will do yet another patch to sort this out.



---

archive/issue_comments_040198.json:
```json
{
    "body": "Attachment [trac_5250_doctest_fix.patch](tarball://root/attachments/some-uuid/ticket5250/trac_5250_doctest_fix.patch) by @loefflerd created at 2009-05-10 21:40:02\n\nfix doctest from #4357 which this breaks",
    "created_at": "2009-05-10T21:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40198",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5250_doctest_fix.patch](tarball://root/attachments/some-uuid/ticket5250/trac_5250_doctest_fix.patch) by @loefflerd created at 2009-05-10 21:40:02

fix doctest from #4357 which this breaks



---

archive/issue_comments_040199.json:
```json
{
    "body": "Right, that should fix it. (I'm trying to ensure that the tickets of mine for which I have patches up right now apply without conflicts if they are all applied *in order of ticket number*.)",
    "created_at": "2009-05-10T21:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40199",
    "user": "https://github.com/loefflerd"
}
```

Right, that should fix it. (I'm trying to ensure that the tickets of mine for which I have patches up right now apply without conflicts if they are all applied *in order of ticket number*.)



---

archive/issue_comments_040200.json:
```json
{
    "body": "I am observing one more doctest failure in ambient.py with -long:\n\n```\nsage -t -long \"devel/sage/sage/modular/modsym/ambient.py\"   \n**********************************************************************\nFile \"/scratch/mabshoff/sage-4.0.alpha0/devel/sage/sage/modular/modsym/ambient.py\", line 1104:\n    sage: M.factorization()                    # long time (about 8 seconds)\nExpected:\n    (Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 7 and level 38, weight 2, character [1, zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) *\n    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [1, zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) *\n    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [1, zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) *\n    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [1, zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2)\nGot:\n    (Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) * \n    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) * \n    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) * \n    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2)\n**********************************************************************\n```\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T09:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40200",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am observing one more doctest failure in ambient.py with -long:

```
sage -t -long "devel/sage/sage/modular/modsym/ambient.py"   
**********************************************************************
File "/scratch/mabshoff/sage-4.0.alpha0/devel/sage/sage/modular/modsym/ambient.py", line 1104:
    sage: M.factorization()                    # long time (about 8 seconds)
Expected:
    (Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 7 and level 38, weight 2, character [1, zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) *
    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [1, zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) *
    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [1, zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) *
    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [1, zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2)
Got:
    (Modular Symbols subspace of dimension 1 of Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) * 
    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) * 
    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2) * 
    (Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 7 and level 38, weight 2, character [zeta3], sign 1, over Cyclotomic Field of order 3 and degree 2)
**********************************************************************
```

Cheers,

Michael



---

archive/issue_comments_040201.json:
```json
{
    "body": "Ah, I didn't do the long doctests. It is harmless. Patch coming in a couple of seconds.",
    "created_at": "2009-05-11T09:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40201",
    "user": "https://github.com/loefflerd"
}
```

Ah, I didn't do the long doctests. It is harmless. Patch coming in a couple of seconds.



---

archive/issue_comments_040202.json:
```json
{
    "body": "Attachment [trac_5250_doctest_fix_2.patch](tarball://root/attachments/some-uuid/ticket5250/trac_5250_doctest_fix_2.patch) by @loefflerd created at 2009-05-11 09:23:05\n\nfix borken -long doctest in modsym/ambient.py",
    "created_at": "2009-05-11T09:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40202",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5250_doctest_fix_2.patch](tarball://root/attachments/some-uuid/ticket5250/trac_5250_doctest_fix_2.patch) by @loefflerd created at 2009-05-11 09:23:05

fix borken -long doctest in modsym/ambient.py



---

archive/issue_comments_040203.json:
```json
{
    "body": "Here it is.",
    "created_at": "2009-05-11T09:25:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40203",
    "user": "https://github.com/loefflerd"
}
```

Here it is.



---

archive/issue_comments_040204.json:
```json
{
    "body": "Just as a double-check, I'll be another voice to say the last two doctest patches look good. (The old code had 1 as one of the multiplicative generators of `Z/38` ... pretty funny.)",
    "created_at": "2009-05-11T09:27:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40204",
    "user": "https://github.com/craigcitro"
}
```

Just as a double-check, I'll be another voice to say the last two doctest patches look good. (The old code had 1 as one of the multiplicative generators of `Z/38` ... pretty funny.)



---

archive/issue_comments_040205.json:
```json
{
    "body": "Replying to [comment:11 craigcitro]:\n> Just as a double-check, I'll be another voice to say the last two doctest patches look good. (The old code had 1 as one of the multiplicative generators of `Z/38` ... pretty funny.)\n\n\nI agree that the new output looks good (and the old one very bad for the reasons stated).",
    "created_at": "2009-05-11T09:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40205",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:11 craigcitro]:
> Just as a double-check, I'll be another voice to say the last two doctest patches look good. (The old code had 1 as one of the multiplicative generators of `Z/38` ... pretty funny.)


I agree that the new output looks good (and the old one very bad for the reasons stated).



---

archive/issue_comments_040206.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T09:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40206",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040207.json:
```json
{
    "body": "Merged all three patches in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T09:31:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5250#issuecomment-40207",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_events_012195.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-11T09:31:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5250",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5250#event-12195"
}
```
