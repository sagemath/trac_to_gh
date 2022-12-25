# Issue 8541: modular forms / linear algebra issue -- subspace not invariant

archive/issues_008541.json:
```json
{
    "body": "Assignee: @craigcitro\n\n\n```\nsage: CuspForms(DirichletGroup(5).0,5).0\nsage: f[15]\nBoom!\n```\n \n\nThis was reported by Paul Nelson, a grad student at Caltech.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8541\n\n",
    "created_at": "2010-03-15T05:20:37Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "modular forms / linear algebra issue -- subspace not invariant",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8541",
    "user": "https://github.com/williamstein"
}
```
Assignee: @craigcitro


```
sage: CuspForms(DirichletGroup(5).0,5).0
sage: f[15]
Boom!
```
 

This was reported by Paul Nelson, a grad student at Caltech.

Issue created by migration from https://trac.sagemath.org/ticket/8541





---

archive/issue_comments_077082.json:
```json
{
    "body": "Changing assignee from @craigcitro to jason, was.",
    "created_at": "2010-04-08T18:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8541#issuecomment-77082",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @craigcitro to jason, was.



---

archive/issue_comments_077083.json:
```json
{
    "body": "The problem is in the multimodular algorithm that's used for computing matrix multiplication over cyclotomic fields:\n\n\n```\nsage: K.<zeta4> = CyclotomicField(4)\nsage: m = matrix(K, 1, 1, [186])\nsage: n = matrix(K, 1, 2, [1, -6/125*zeta4 - 117/125])\nsage: m * n\n[                 -23087/125 -1116/125*zeta4 - 21762/125]\n```\n\n\nAccording to the output of verbose, it works modulo a single prime (split in K), in this case 46337; and the result is indeed correct modulo this prime. But that's not enough, clearly. I'm very suspicious about the method `sage.matrix.matrix_cyclo_dense.Matrix_cyclo_dense.height()`. It returns the maximum absolute value of any entry (in any complex embedding), so n has height 1. Shouldn't it return the maximum absolute value of the numerator or denominator of any element, as with the corresponding method for dense rational matrices? (What does this even mean when K doesn't have class number 1?)",
    "created_at": "2010-04-08T18:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8541#issuecomment-77083",
    "user": "https://github.com/loefflerd"
}
```

The problem is in the multimodular algorithm that's used for computing matrix multiplication over cyclotomic fields:


```
sage: K.<zeta4> = CyclotomicField(4)
sage: m = matrix(K, 1, 1, [186])
sage: n = matrix(K, 1, 2, [1, -6/125*zeta4 - 117/125])
sage: m * n
[                 -23087/125 -1116/125*zeta4 - 21762/125]
```


According to the output of verbose, it works modulo a single prime (split in K), in this case 46337; and the result is indeed correct modulo this prime. But that's not enough, clearly. I'm very suspicious about the method `sage.matrix.matrix_cyclo_dense.Matrix_cyclo_dense.height()`. It returns the maximum absolute value of any entry (in any complex embedding), so n has height 1. Shouldn't it return the maximum absolute value of the numerator or denominator of any element, as with the corresponding method for dense rational matrices? (What does this even mean when K doesn't have class number 1?)



---

archive/issue_comments_077084.json:
```json
{
    "body": "Changing component from modular forms to linear algebra.",
    "created_at": "2010-04-08T18:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8541#issuecomment-77084",
    "user": "https://github.com/loefflerd"
}
```

Changing component from modular forms to linear algebra.



---

archive/issue_comments_077085.json:
```json
{
    "body": "Hold it, my suspicion was wrong: the height method only gets called after clearing denominators, and the problem is still there if we use the integral matrix `n = matrix(K, [125, -6*zeta4 - 117])`. So maybe the problem is here:\n\n```\n        # conservative but correct estimate\n        bound = A.height() * B.height() * self._ncols\n```\n\nPerhaps this estimate is wrong in this degenerate case?",
    "created_at": "2010-04-08T18:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8541#issuecomment-77085",
    "user": "https://github.com/loefflerd"
}
```

Hold it, my suspicion was wrong: the height method only gets called after clearing denominators, and the problem is still there if we use the integral matrix `n = matrix(K, [125, -6*zeta4 - 117])`. So maybe the problem is here:

```
        # conservative but correct estimate
        bound = A.height() * B.height() * self._ncols
```

Perhaps this estimate is wrong in this degenerate case?



---

archive/issue_comments_077086.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-04-09T11:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8541#issuecomment-77086",
    "user": "https://github.com/loefflerd"
}
```

Changing priority from major to critical.



---

archive/issue_comments_077087.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2010-04-09T21:18:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8541#issuecomment-77087",
    "user": "https://github.com/loefflerd"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_077088.json:
```json
{
    "body": "This seems to be a duplicate of #8666, which already has a positive review.",
    "created_at": "2010-04-11T12:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8541#issuecomment-77088",
    "user": "https://github.com/burcin"
}
```

This seems to be a duplicate of #8666, which already has a positive review.



---

archive/issue_comments_077089.json:
```json
{
    "body": "Changing priority from blocker to minor.",
    "created_at": "2010-04-11T20:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8541#issuecomment-77089",
    "user": "https://github.com/loefflerd"
}
```

Changing priority from blocker to minor.



---

archive/issue_comments_077090.json:
```json
{
    "body": "Arguably, the correct statement is that #8666 is a duplicate of this :-).\n\nJust to be safe, it might be worth adding a doctest to the modular forms code to show that the computation that triggered the problem in the original bug report does now work -- I will write a mini-patch tomorrow morning. When that is reviewed and merged then we can close this ticket, but in any case the ticket \"priority\" flag can safely be reduced.",
    "created_at": "2010-04-11T20:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8541#issuecomment-77090",
    "user": "https://github.com/loefflerd"
}
```

Arguably, the correct statement is that #8666 is a duplicate of this :-).

Just to be safe, it might be worth adding a doctest to the modular forms code to show that the computation that triggered the problem in the original bug report does now work -- I will write a mini-patch tomorrow morning. When that is reviewed and merged then we can close this ticket, but in any case the ticket "priority" flag can safely be reduced.



---

archive/issue_comments_077091.json:
```json
{
    "body": "apply after #8666",
    "created_at": "2010-04-12T13:56:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8541#issuecomment-77091",
    "user": "https://github.com/loefflerd"
}
```

apply after #8666



---

archive/issue_comments_077092.json:
```json
{
    "body": "Attachment [trac_8541.patch](tarball://root/attachments/some-uuid/ticket8541/trac_8541.patch) by @loefflerd created at 2010-04-12 13:57:32\n\nAs promised, here's a doctest.",
    "created_at": "2010-04-12T13:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8541#issuecomment-77092",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_8541.patch](tarball://root/attachments/some-uuid/ticket8541/trac_8541.patch) by @loefflerd created at 2010-04-12 13:57:32

As promised, here's a doctest.



---

archive/issue_comments_077093.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-12T13:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8541#issuecomment-77093",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077094.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-14T23:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8541#issuecomment-77094",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008722.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-04-16T18:42:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8541",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8541#event-8722"
}
```



---

archive/issue_comments_077095.json:
```json
{
    "body": "Merged \"trac_8541.patch\" in 4.4.alpha0.",
    "created_at": "2010-04-16T18:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8541#issuecomment-77095",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8541.patch" in 4.4.alpha0.



---

archive/issue_comments_077096.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8541",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8541#issuecomment-77096",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
