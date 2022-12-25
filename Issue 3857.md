# Issue 3857: BinaryQF_reduced_representatives in binry_qf.py produces extra unreduced forms

archive/issues_003857.json:
```json
{
    "body": "Assignee: @williamstein\n\nFor example \n\n```\nsage: BinaryQF_reduced_representatives(-63)\n\n[2*x^2 - x*y + 8*y^2,\n 4*x^2 - x*y + 4*y^2,\n x^2 + x*y + 16*y^2,\n 2*x^2 + x*y + 8*y^2,\n 4*x^2 + x*y + 4*y^2,\n 3*x^2 + 3*x*y + 6*y^2]\n```\n\n\nHowever, clearly:\n\n\n```\n4*x^2 - x*y + 4*y^2\n```\n\n\nisn't a reduced form.\nBinaryQF_reduced_representatives is incorrectly classifying some forms.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3857\n\n",
    "created_at": "2008-08-14T21:07:07Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "BinaryQF_reduced_representatives in binry_qf.py produces extra unreduced forms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3857",
    "user": "https://trac.sagemath.org/admin/accounts/users/choldsworth"
}
```
Assignee: @williamstein

For example 

```
sage: BinaryQF_reduced_representatives(-63)

[2*x^2 - x*y + 8*y^2,
 4*x^2 - x*y + 4*y^2,
 x^2 + x*y + 16*y^2,
 2*x^2 + x*y + 8*y^2,
 4*x^2 + x*y + 4*y^2,
 3*x^2 + 3*x*y + 6*y^2]
```


However, clearly:


```
4*x^2 - x*y + 4*y^2
```


isn't a reduced form.
BinaryQF_reduced_representatives is incorrectly classifying some forms.


Issue created by migration from https://trac.sagemath.org/ticket/3857





---

archive/issue_comments_027411.json:
```json
{
    "body": "Attachment [new_patch.patch](tarball://root/attachments/some-uuid/ticket3857/new_patch.patch) by choldsworth created at 2008-08-14 21:08:34",
    "created_at": "2008-08-14T21:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3857#issuecomment-27411",
    "user": "https://trac.sagemath.org/admin/accounts/users/choldsworth"
}
```

Attachment [new_patch.patch](tarball://root/attachments/some-uuid/ticket3857/new_patch.patch) by choldsworth created at 2008-08-14 21:08:34



---

archive/issue_comments_027412.json:
```json
{
    "body": "The patch applies cleanly to 3.1.1 and doctests pass.\n\nHowever, there are some things I really do not like about this implementation:\n\n1. `self.reduce()` computes (if necessary) caches and returns the reduced form equivalent to self.  I would expect it to change self into the reduced form, and have a different function self.reduced_form() to do what this function does.\n\n2. The function `is_reduced()` actually reduces self and tests if the result is the same as self.  This is potentially very expensive!  To test `is_reduced()` you should just test that the usual inequalities are satisfied.\n\n3. The function `BinaryQF_reduced_representatives(D)` -- where the bug was -- proceeds in a way very different to what I have always done, with the outer loop being over b.  For a start you should only loop over b's of the same parity as D, not over all b's and then compute and test if `b^2-D` is a multiple of 4.  Then, this method requires factoring all those values of `(b^2-D)/4` to get possible a's -- another expensive and quite unnecessary set of computations.  Finally, the list is not sorted as I think it should be.\n\nI would like to rewrite this function, but the current patch can be applied and a new ticket opened if anyone agrees with me.",
    "created_at": "2008-08-23T17:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3857#issuecomment-27412",
    "user": "https://github.com/JohnCremona"
}
```

The patch applies cleanly to 3.1.1 and doctests pass.

However, there are some things I really do not like about this implementation:

1. `self.reduce()` computes (if necessary) caches and returns the reduced form equivalent to self.  I would expect it to change self into the reduced form, and have a different function self.reduced_form() to do what this function does.

2. The function `is_reduced()` actually reduces self and tests if the result is the same as self.  This is potentially very expensive!  To test `is_reduced()` you should just test that the usual inequalities are satisfied.

3. The function `BinaryQF_reduced_representatives(D)` -- where the bug was -- proceeds in a way very different to what I have always done, with the outer loop being over b.  For a start you should only loop over b's of the same parity as D, not over all b's and then compute and test if `b^2-D` is a multiple of 4.  Then, this method requires factoring all those values of `(b^2-D)/4` to get possible a's -- another expensive and quite unnecessary set of computations.  Finally, the list is not sorted as I think it should be.

I would like to rewrite this function, but the current patch can be applied and a new ticket opened if anyone agrees with me.



---

archive/issue_comments_027413.json:
```json
{
    "body": "Patch implementing a superior BinaryQF_reduced_representatives method.",
    "created_at": "2008-08-25T00:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3857#issuecomment-27413",
    "user": "https://trac.sagemath.org/admin/accounts/users/choldsworth"
}
```

Patch implementing a superior BinaryQF_reduced_representatives method.



---

archive/issue_comments_027414.json:
```json
{
    "body": "Attachment [3857.patch](tarball://root/attachments/some-uuid/ticket3857/3857.patch) by choldsworth created at 2008-08-25 00:41:40\n\nI have submitted a new patch (superseding my first patch), re-implementing the BinaryQF_reduced_representatives method, and addressing your point 3.\n\nI agree the other points need fixing but feel they should have their own ticket, or at least separate patches.\n\nHere are some timings from the new method.\n\nOld code:\n\n```\nsage: timeit(\"BinaryQF_reduced_representatives(-4004)\")\n5 loops, best of 3: 29.6 s per loop\n```\n\n\nNew code:\n\n```\nsage: timeit(\"BinaryQF_reduced_representatives(-4004)\")\n5 loops, best of 3: 38.9 ms per loop\n```\n",
    "created_at": "2008-08-25T00:41:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3857#issuecomment-27414",
    "user": "https://trac.sagemath.org/admin/accounts/users/choldsworth"
}
```

Attachment [3857.patch](tarball://root/attachments/some-uuid/ticket3857/3857.patch) by choldsworth created at 2008-08-25 00:41:40

I have submitted a new patch (superseding my first patch), re-implementing the BinaryQF_reduced_representatives method, and addressing your point 3.

I agree the other points need fixing but feel they should have their own ticket, or at least separate patches.

Here are some timings from the new method.

Old code:

```
sage: timeit("BinaryQF_reduced_representatives(-4004)")
5 loops, best of 3: 29.6 s per loop
```


New code:

```
sage: timeit("BinaryQF_reduced_representatives(-4004)")
5 loops, best of 3: 38.9 ms per loop
```




---

archive/issue_comments_027415.json:
```json
{
    "body": "Apply after the previous patch (ignore the first one)",
    "created_at": "2008-08-25T10:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3857#issuecomment-27415",
    "user": "https://github.com/JohnCremona"
}
```

Apply after the previous patch (ignore the first one)



---

archive/issue_comments_027416.json:
```json
{
    "body": "Attachment [sage-trac3857.patch](tarball://root/attachments/some-uuid/ticket3857/sage-trac3857.patch) by @JohnCremona created at 2008-08-25 10:34:23\n\nThat is some speedup!  When I tested the same myself I noticed that during the (long) test of the old code the machine was running lisp, meaning that something was happening using maxima, which it should not.  But that is now in the past.\n\nI have simplified the code a bit more, using xsrange() for the a and b loops, and letting b only loop from 0 (or 1) to a, adding in the form with -b if needed.  This gives another speedup factor of about 2.\n\nThis should now have a new independent review -- as far as I am concerned it is ok!  \n\nI'll now review the other patches you made in response to my first two points.",
    "created_at": "2008-08-25T10:34:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3857#issuecomment-27416",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [sage-trac3857.patch](tarball://root/attachments/some-uuid/ticket3857/sage-trac3857.patch) by @JohnCremona created at 2008-08-25 10:34:23

That is some speedup!  When I tested the same myself I noticed that during the (long) test of the old code the machine was running lisp, meaning that something was happening using maxima, which it should not.  But that is now in the past.

I have simplified the code a bit more, using xsrange() for the a and b loops, and letting b only loop from 0 (or 1) to a, adding in the form with -b if needed.  This gives another speedup factor of about 2.

This should now have a new independent review -- as far as I am concerned it is ok!  

I'll now review the other patches you made in response to my first two points.



---

archive/issue_comments_027417.json:
```json
{
    "body": "Attachment [3857-nils-1.patch](tarball://root/attachments/some-uuid/ticket3857/3857-nils-1.patch) by NilsSkoruppa created at 2008-09-06 14:39:50\n\nApply after the previous two patches (ignore the first one)",
    "created_at": "2008-09-06T14:39:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3857#issuecomment-27417",
    "user": "https://trac.sagemath.org/admin/accounts/users/NilsSkoruppa"
}
```

Attachment [3857-nils-1.patch](tarball://root/attachments/some-uuid/ticket3857/3857-nils-1.patch) by NilsSkoruppa created at 2008-09-06 14:39:50

Apply after the previous two patches (ignore the first one)



---

archive/issue_comments_027418.json:
```json
{
    "body": "Changing assignee from @williamstein to NilsSkoruppa.",
    "created_at": "2008-09-06T15:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3857#issuecomment-27418",
    "user": "https://trac.sagemath.org/admin/accounts/users/NilsSkoruppa"
}
```

Changing assignee from @williamstein to NilsSkoruppa.



---

archive/issue_comments_027419.json:
```json
{
    "body": "The last patch seemed to be OK. However, I noticed that the bounds for the search region for reduced forms was not optimal. I inserted the optimal bounds and modified the loop logic accordingly, and I gained a speedup of a factor around 10.\n\nBefore:\n\n```\nsage: timeit( 'BinaryQF_reduced_representatives(-998995)')\n5 loops, best of 3: 5.52 s per loop\n```\n\n\nAfter:\n\n```\nsage: timeit( 'BinaryQF_reduced_representatives(-998995)')\n5 loops, best of 3: 547 ms per loop\n```\n\n\nDoctest runs successfully and I tested 1000 discriminants with 6 digits each, compared to the corresponding results produced by the last patch and compared number of produced forms with Hurwitz class numbers in gp. I think its OK now. Ready for being reviewed.",
    "created_at": "2008-09-06T15:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3857#issuecomment-27419",
    "user": "https://trac.sagemath.org/admin/accounts/users/NilsSkoruppa"
}
```

The last patch seemed to be OK. However, I noticed that the bounds for the search region for reduced forms was not optimal. I inserted the optimal bounds and modified the loop logic accordingly, and I gained a speedup of a factor around 10.

Before:

```
sage: timeit( 'BinaryQF_reduced_representatives(-998995)')
5 loops, best of 3: 5.52 s per loop
```


After:

```
sage: timeit( 'BinaryQF_reduced_representatives(-998995)')
5 loops, best of 3: 547 ms per loop
```


Doctest runs successfully and I tested 1000 discriminants with 6 digits each, compared to the corresponding results produced by the last patch and compared number of produced forms with Hurwitz class numbers in gp. I think its OK now. Ready for being reviewed.



---

archive/issue_comments_027420.json:
```json
{
    "body": "Thanks for the review and great improvement (improved lower bound for b).\n\nI applied all three patches (that is, all but the first attached to this ticket) to 3.1.2.alpha4 successfully, and all doctests in sage.quadraticforms pass.  Nils's testing vs. gp was a very good idea, so I think we can be confident of this.\n\nI vote for this to be adopted, and hope the editor will not feel the need to get in a new reviewer (so far, each reviewer has vastly improved the previous code, but I don't think we can hope for that to happen again!)",
    "created_at": "2008-09-06T15:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3857#issuecomment-27420",
    "user": "https://github.com/JohnCremona"
}
```

Thanks for the review and great improvement (improved lower bound for b).

I applied all three patches (that is, all but the first attached to this ticket) to 3.1.2.alpha4 successfully, and all doctests in sage.quadraticforms pass.  Nils's testing vs. gp was a very good idea, so I think we can be confident of this.

I vote for this to be adopted, and hope the editor will not feel the need to get in a new reviewer (so far, each reviewer has vastly improved the previous code, but I don't think we can hope for that to happen again!)



---

archive/issue_comments_027421.json:
```json
{
    "body": "Changing assignee from NilsSkoruppa to choldsworth.",
    "created_at": "2008-09-06T19:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3857#issuecomment-27421",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from NilsSkoruppa to choldsworth.



---

archive/issue_events_004080.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-06T23:50:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3857",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3857#event-4080"
}
```



---

archive/issue_comments_027422.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-06T23:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3857#issuecomment-27422",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027423.json:
```json
{
    "body": "Merged 3857.patch, sage-trac3857.patch and 3857-nils-1.patch in Sage 3.1.2.rc0",
    "created_at": "2008-09-06T23:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3857",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3857#issuecomment-27423",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 3857.patch, sage-trac3857.patch and 3857-nils-1.patch in Sage 3.1.2.rc0
