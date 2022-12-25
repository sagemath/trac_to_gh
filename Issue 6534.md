# Issue 6534: Jacobi sums are calculated in a ridiculously roundabout fashion

archive/issues_006534.json:
```json
{
    "body": "Assignee: @craigcitro\n\nKeywords: dirichlet characters\n\nWhy are we using a devious and roundabout algorithm to compute Jacobi sums using Gauss sums, which is actually many orders of magnitude slower than using the definition directly? I'm not joking here: for a pretty small prime, the obvious algorithm is more than 800 times as fast as the implementation we currently have.\n\n\n```\nsage: chi = DirichletGroup(67).0\nsage: psi = chi**3\nsage: time sum([chi(a)*psi(1-a) for a in Zmod(67)])\nCPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s\nWall time: 0.05 s\n-5*zeta66^19 - 3*zeta66^18 + 6*zeta66^17 + 11*zeta66^16 + 3*zeta66^15 - 3*zeta66^14 - 7*zeta66^13 - 2*zeta66^12 + 3*zeta66^11 + 4*zeta66^10 + 5*zeta66^9 + 5*zeta66^8 - 4*zeta66^7 - 8*zeta66^6 - 8*zeta66^5 + 4*zeta66^4+ 6*zeta66^3 + 6*zeta66^2 - 3*zeta66 - 8\nsage: time chi.jacobi_sum(psi)\nCPU times: user 25.59 s, sys: 0.06 s, total: 25.65 s\nWall time: 29.02 s\n-5*zeta4422^1273 - 3*zeta4422^1206 + 6*zeta4422^1139 + 11*zeta4422^1072 + 3*zeta4422^1005 - 3*zeta4422^938 -7*zeta4422^871 - 2*zeta4422^804 + 3*zeta4422^737 + 4*zeta4422^670 + 5*zeta4422^603 + 5*zeta4422^536 - 4*zeta4422^469 - 8*zeta4422^402 - 8*zeta4422^335 + 4*zeta4422^268 + 6*zeta4422^201 + 6*zeta4422^134 - 3*zeta4422^67- 8\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6534\n\n",
    "created_at": "2009-07-14T19:55:02Z",
    "labels": [
        "component: modular forms"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "Jacobi sums are calculated in a ridiculously roundabout fashion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6534",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @craigcitro

Keywords: dirichlet characters

Why are we using a devious and roundabout algorithm to compute Jacobi sums using Gauss sums, which is actually many orders of magnitude slower than using the definition directly? I'm not joking here: for a pretty small prime, the obvious algorithm is more than 800 times as fast as the implementation we currently have.


```
sage: chi = DirichletGroup(67).0
sage: psi = chi**3
sage: time sum([chi(a)*psi(1-a) for a in Zmod(67)])
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.05 s
-5*zeta66^19 - 3*zeta66^18 + 6*zeta66^17 + 11*zeta66^16 + 3*zeta66^15 - 3*zeta66^14 - 7*zeta66^13 - 2*zeta66^12 + 3*zeta66^11 + 4*zeta66^10 + 5*zeta66^9 + 5*zeta66^8 - 4*zeta66^7 - 8*zeta66^6 - 8*zeta66^5 + 4*zeta66^4+ 6*zeta66^3 + 6*zeta66^2 - 3*zeta66 - 8
sage: time chi.jacobi_sum(psi)
CPU times: user 25.59 s, sys: 0.06 s, total: 25.65 s
Wall time: 29.02 s
-5*zeta4422^1273 - 3*zeta4422^1206 + 6*zeta4422^1139 + 11*zeta4422^1072 + 3*zeta4422^1005 - 3*zeta4422^938 -7*zeta4422^871 - 2*zeta4422^804 + 3*zeta4422^737 + 4*zeta4422^670 + 5*zeta4422^603 + 5*zeta4422^536 - 4*zeta4422^469 - 8*zeta4422^402 - 8*zeta4422^335 + 4*zeta4422^268 + 6*zeta4422^201 + 6*zeta4422^134 - 3*zeta4422^67- 8
```


Issue created by migration from https://trac.sagemath.org/ticket/6534





---

archive/issue_comments_053171.json:
```json
{
    "body": "Attachment [trac_6534-jacobi_sums_faster-without_6393.patch](tarball://root/attachments/some-uuid/ticket6534/trac_6534-jacobi_sums_faster-without_6393.patch) by @loefflerd created at 2009-07-14 20:28:14",
    "created_at": "2009-07-14T20:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6534#issuecomment-53171",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_6534-jacobi_sums_faster-without_6393.patch](tarball://root/attachments/some-uuid/ticket6534/trac_6534-jacobi_sums_faster-without_6393.patch) by @loefflerd created at 2009-07-14 20:28:14



---

archive/issue_comments_053172.json:
```json
{
    "body": "Here are two patches. One is intended to be applied on top of the patch at #6393, and the other without it; both give identical results. (This is intended to future-proof this ticket in case #6393 gets merged before anyone gets around to reviewing this one.)\n\nWhile I was at it, I couldn't resist doing some streamlining to dirichlet.py by using the ``@`cached_method` decorator, and fixing a non-ReSTified docstring for Kloosterman sums.",
    "created_at": "2009-07-14T20:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6534#issuecomment-53172",
    "user": "https://github.com/loefflerd"
}
```

Here are two patches. One is intended to be applied on top of the patch at #6393, and the other without it; both give identical results. (This is intended to future-proof this ticket in case #6393 gets merged before anyone gets around to reviewing this one.)

While I was at it, I couldn't resist doing some streamlining to dirichlet.py by using the ``@`cached_method` decorator, and fixing a non-ReSTified docstring for Kloosterman sums.



---

archive/issue_comments_053173.json:
```json
{
    "body": "Attachment [trac_6534_fix.patch](tarball://root/attachments/some-uuid/ticket6534/trac_6534_fix.patch) by @loefflerd created at 2009-07-14 20:56:59\n\napply over exactly one of the above two patches",
    "created_at": "2009-07-14T20:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6534#issuecomment-53173",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_6534_fix.patch](tarball://root/attachments/some-uuid/ticket6534/trac_6534_fix.patch) by @loefflerd created at 2009-07-14 20:56:59

apply over exactly one of the above two patches



---

archive/issue_comments_053174.json:
```json
{
    "body": "The third patch above fixes some formatting slips in the documentation. I also added a definition of the Jacobi sum to the docstring, since there wasn't one before. This should apply fine over either of the previous two patches.",
    "created_at": "2009-07-14T20:58:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6534#issuecomment-53174",
    "user": "https://github.com/loefflerd"
}
```

The third patch above fixes some formatting slips in the documentation. I also added a definition of the Jacobi sum to the docstring, since there wasn't one before. This should apply fine over either of the previous two patches.



---

archive/issue_comments_053175.json:
```json
{
    "body": "I like this patch.  (I tested the version which goes on top of #6393 having applied that first).  The code is a lot simpler, and it is faster, and it is more general (it works for characters withe values in non-prime finite fields).  What more can one ask?\n\nAll files in sage/modular test ok.\n\nI must check out this cached_method trick, since it simplifies code a lot!",
    "created_at": "2009-07-18T16:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6534#issuecomment-53175",
    "user": "https://github.com/JohnCremona"
}
```

I like this patch.  (I tested the version which goes on top of #6393 having applied that first).  The code is a lot simpler, and it is faster, and it is more general (it works for characters withe values in non-prime finite fields).  What more can one ask?

All files in sage/modular test ok.

I must check out this cached_method trick, since it simplifies code a lot!



---

archive/issue_comments_053176.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-19T08:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6534#issuecomment-53176",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_006770.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-19T08:02:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6534",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6534#event-6770"
}
```



---

archive/issue_comments_053177.json:
```json
{
    "body": "Merged `trac_6534-jacobi_sums_faster-with_6393.patch` and `trac_6534_fix.patch`, since #6393 has already been merged.",
    "created_at": "2009-07-19T08:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6534#issuecomment-53177",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged `trac_6534-jacobi_sums_faster-with_6393.patch` and `trac_6534_fix.patch`, since #6393 has already been merged.
