# Issue 7331: Conditions for non-split multiplicative reduction in p_primary_bound of Tate-Shafarevich groups

archive/issues_007331.json:
```json
{
    "body": "Assignee: @loefflerd\n\nCC:  @williamstein @rlmill\n\nKeywords: sha, tate-shafarevich group,  primary bound\n\n`p_primary_bound` fails on the following rank 0 curve with non-split multiplicative reduction.\n\n\n```\nE = EllipticCurve('270b')\nE.sha().p_primary_bound(5)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7331\n\n",
    "created_at": "2009-10-28T09:56:17Z",
    "labels": [
        "component: elliptic curves",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Conditions for non-split multiplicative reduction in p_primary_bound of Tate-Shafarevich groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7331",
    "user": "https://github.com/categorie"
}
```
Assignee: @loefflerd

CC:  @williamstein @rlmill

Keywords: sha, tate-shafarevich group,  primary bound

`p_primary_bound` fails on the following rank 0 curve with non-split multiplicative reduction.


```
E = EllipticCurve('270b')
E.sha().p_primary_bound(5)
```


Issue created by migration from https://trac.sagemath.org/ticket/7331





---

archive/issue_comments_061188.json:
```json
{
    "body": "exported against sage 4.2.alpha1",
    "created_at": "2009-10-28T13:00:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7331#issuecomment-61188",
    "user": "https://github.com/categorie"
}
```

exported against sage 4.2.alpha1



---

archive/issue_comments_061189.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-28T13:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7331#issuecomment-61189",
    "user": "https://github.com/categorie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061190.json:
```json
{
    "body": "Attachment [trac_7331.patch](tarball://root/attachments/some-uuid/ticket7331/trac_7331.patch) by @categorie created at 2009-10-28 13:02:44\n\nThis patch allows now for non-split multiplicative reduction and for p=3 when the rank is 0. (As we do not need p-adic heights in this case)",
    "created_at": "2009-10-28T13:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7331#issuecomment-61190",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_7331.patch](tarball://root/attachments/some-uuid/ticket7331/trac_7331.patch) by @categorie created at 2009-10-28 13:02:44

This patch allows now for non-split multiplicative reduction and for p=3 when the rank is 0. (As we do not need p-adic heights in this case)



---

archive/issue_comments_061191.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-28T16:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7331#issuecomment-61191",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_061192.json:
```json
{
    "body": "For `p=3`, an error is getting triggered in computation of the p-adic regulator:\n\n\n```\nsage: E = EllipticCurve('148a')\nsage: E.is_surjective(3)\n(True, None)\nsage: E.has_additive_reduction(3)\nFalse\nsage: E.has_nonsplit_multiplicative_reduction(3)\nFalse\nsage: E.is_good(3)\nTrue\nsage: E.is_ordinary(3)\nTrue\nsage: E.sha().p_primary_bound(3)\nBOOM\n```\n\n\nI have a feeling that this just means that the documentation needs to include the rank 0 condition when `p=3`:\n\n\n```\nE.rank()\n1\n```\n",
    "created_at": "2009-10-28T16:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7331#issuecomment-61192",
    "user": "https://github.com/rlmill"
}
```

For `p=3`, an error is getting triggered in computation of the p-adic regulator:


```
sage: E = EllipticCurve('148a')
sage: E.is_surjective(3)
(True, None)
sage: E.has_additive_reduction(3)
False
sage: E.has_nonsplit_multiplicative_reduction(3)
False
sage: E.is_good(3)
True
sage: E.is_ordinary(3)
True
sage: E.sha().p_primary_bound(3)
BOOM
```


I have a feeling that this just means that the documentation needs to include the rank 0 condition when `p=3`:


```
E.rank()
1
```




---

archive/issue_comments_061193.json:
```json
{
    "body": "This one is a different failure:\n\n```\nsage: E = EllipticCurve('336c')\nsage: E.rank()\n0\nsage: E.is_surjective(3)\n(True, None)\nsage: E.has_additive_reduction(3)\nFalse\nsage: E.has_nonsplit_multiplicative_reduction(3)\nFalse\nsage: E.is_good(3)\nFalse\nsage: E.is_ordinary(3)\nTrue\nsage: E.has_split_multiplicative_reduction(3)\nTrue\nsage: E.sha().p_primary_bound(3)\nTraceback (most recent call last):\n/space/rlm/sage-4.2.alpha0-x86_64-Linux/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/sha_tate.pyc in p_primary_bound(self, p)\n    588             if not su :\n    589                 raise ValueError, \"The mod-p Galois representation is not surjective. Current knowledge about Euler systems does not provide an upper bound in this case. Try an_padic for a conjectural bound.\"\n--> 590             shan = self.an_padic(p,prec = 0,use_twists=True)\n    591             if shan == 0:\n    592                 raise RuntimeError, \"There is a bug in an_padic.\"\n\n/space/rlm/sage-4.2.alpha0-x86_64-Linux/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/sha_tate.pyc in an_padic(self, p, prec, use_twists)\n    450             not_yet_enough_prec = True\n    451             while not_yet_enough_prec:\n--> 452                 lps = lp.series(n,quadratic_twist=D,prec=r+1)\n    453                 lstar = lps[r]\n    454                 if (lstar != 0) or (prec != 0):\n\n/space/rlm/sage-4.2.alpha0-x86_64-Linux/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/padic_lseries.pyc in series(self, n, quadratic_twist, prec)\n    762                 for ell in prime_divisors(D):\n    763                     if valuation(self._E.conductor(),ell) > valuation(D,ell) :\n--> 764                         raise ValueError, \"can not twist a curve of conductor (=%s) by the quadratic twist (=%s).\"%(self._E.conductor(),D)\n    765\n    766\n\nValueError: can not twist a curve of conductor (=168) by the quadratic twist (=-4).\n```\n",
    "created_at": "2009-10-28T16:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7331#issuecomment-61193",
    "user": "https://github.com/rlmill"
}
```

This one is a different failure:

```
sage: E = EllipticCurve('336c')
sage: E.rank()
0
sage: E.is_surjective(3)
(True, None)
sage: E.has_additive_reduction(3)
False
sage: E.has_nonsplit_multiplicative_reduction(3)
False
sage: E.is_good(3)
False
sage: E.is_ordinary(3)
True
sage: E.has_split_multiplicative_reduction(3)
True
sage: E.sha().p_primary_bound(3)
Traceback (most recent call last):
/space/rlm/sage-4.2.alpha0-x86_64-Linux/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/sha_tate.pyc in p_primary_bound(self, p)
    588             if not su :
    589                 raise ValueError, "The mod-p Galois representation is not surjective. Current knowledge about Euler systems does not provide an upper bound in this case. Try an_padic for a conjectural bound."
--> 590             shan = self.an_padic(p,prec = 0,use_twists=True)
    591             if shan == 0:
    592                 raise RuntimeError, "There is a bug in an_padic."

/space/rlm/sage-4.2.alpha0-x86_64-Linux/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/sha_tate.pyc in an_padic(self, p, prec, use_twists)
    450             not_yet_enough_prec = True
    451             while not_yet_enough_prec:
--> 452                 lps = lp.series(n,quadratic_twist=D,prec=r+1)
    453                 lstar = lps[r]
    454                 if (lstar != 0) or (prec != 0):

/space/rlm/sage-4.2.alpha0-x86_64-Linux/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/padic_lseries.pyc in series(self, n, quadratic_twist, prec)
    762                 for ell in prime_divisors(D):
    763                     if valuation(self._E.conductor(),ell) > valuation(D,ell) :
--> 764                         raise ValueError, "can not twist a curve of conductor (=%s) by the quadratic twist (=%s)."%(self._E.conductor(),D)
    765
    766

ValueError: can not twist a curve of conductor (=168) by the quadratic twist (=-4).
```




---

archive/issue_comments_061194.json:
```json
{
    "body": "I agree that I should change the documentation about p=3 => rank 0. I prefer not to catch them at the start of `p_primary_bound` since in principle it should work. The only issue is that Kedlaya's algorithm is not implemented in sage for p=3. \n\nBut I can not reproduce your second issue. This should have been solved by #6455, merge in 4.2.alpha1.",
    "created_at": "2009-10-28T18:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7331#issuecomment-61194",
    "user": "https://github.com/categorie"
}
```

I agree that I should change the documentation about p=3 => rank 0. I prefer not to catch them at the start of `p_primary_bound` since in principle it should work. The only issue is that Kedlaya's algorithm is not implemented in sage for p=3. 

But I can not reproduce your second issue. This should have been solved by #6455, merge in 4.2.alpha1.



---

archive/issue_comments_061195.json:
```json
{
    "body": "Attachment [trac_7331_2.patch](tarball://root/attachments/some-uuid/ticket7331/trac_7331_2.patch) by @categorie created at 2009-10-28 18:50:28\n\nto be applied after teh first patch",
    "created_at": "2009-10-28T18:50:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7331#issuecomment-61195",
    "user": "https://github.com/categorie"
}
```

Attachment [trac_7331_2.patch](tarball://root/attachments/some-uuid/ticket7331/trac_7331_2.patch) by @categorie created at 2009-10-28 18:50:28

to be applied after teh first patch



---

archive/issue_comments_061196.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-30T17:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7331#issuecomment-61196",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061197.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-30T17:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7331#issuecomment-61197",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007553.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-31T16:27:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7331",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7331#event-7553"
}
```



---

archive/issue_comments_061198.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T16:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7331#issuecomment-61198",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
