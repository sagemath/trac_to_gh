# Issue 3461: write a construction for permutation groups so that the coercion system can find a common parent

archive/issues_003461.json:
```json
{
    "body": "Assignee: joyner\n\nThis happens in the coercion branch:\n\n\n```\nsage: P1 = PermutationGroup([[(1,2)]]); P1\nPermutation Group with generators [(1,2)]\nsage: P2 = PermutationGroup([[(1,3)]]); P2\nPermutation Group with generators [(1,3)]\nsage: p1 = P1.gen(); p2 = P2.gen()\nsage: p1*p2\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/opt/sage-3.0.3.rc0/devel/sage-main/sage/combinat/matrices/<ipython console> in <module>()\n\n/opt/sage-3.0.3.rc0/devel/sage-main/sage/combinat/matrices/element.pyx in sage.structure.element.MonoidElement.__mul__ (sage/structure/element.c:7517)()\n\nTypeError: unsupported operand parent(s) for '*': 'Permutation Group with generators [(1,2)]' and 'Permutation Group with generators [(1,3)]'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3461\n\n",
    "created_at": "2008-06-18T09:05:16Z",
    "labels": [
        "component: group theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "write a construction for permutation groups so that the coercion system can find a common parent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3461",
    "user": "https://github.com/mwhansen"
}
```
Assignee: joyner

This happens in the coercion branch:


```
sage: P1 = PermutationGroup([[(1,2)]]); P1
Permutation Group with generators [(1,2)]
sage: P2 = PermutationGroup([[(1,3)]]); P2
Permutation Group with generators [(1,3)]
sage: p1 = P1.gen(); p2 = P2.gen()
sage: p1*p2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/opt/sage-3.0.3.rc0/devel/sage-main/sage/combinat/matrices/<ipython console> in <module>()

/opt/sage-3.0.3.rc0/devel/sage-main/sage/combinat/matrices/element.pyx in sage.structure.element.MonoidElement.__mul__ (sage/structure/element.c:7517)()

TypeError: unsupported operand parent(s) for '*': 'Permutation Group with generators [(1,2)]' and 'Permutation Group with generators [(1,3)]'
```


Issue created by migration from https://trac.sagemath.org/ticket/3461





---

archive/issue_comments_024363.json:
```json
{
    "body": "Attachment [trac_3461.patch](tarball://root/attachments/some-uuid/ticket3461/trac_3461.patch) by @mwhansen created at 2010-01-17 03:24:37",
    "created_at": "2010-01-17T03:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3461#issuecomment-24363",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3461.patch](tarball://root/attachments/some-uuid/ticket3461/trac_3461.patch) by @mwhansen created at 2010-01-17 03:24:37



---

archive/issue_comments_024364.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T03:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3461#issuecomment-24364",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_024365.json:
```json
{
    "body": "Attachment [trac_3461_new.patch](tarball://root/attachments/some-uuid/ticket3461/trac_3461_new.patch) by @loefflerd created at 2010-05-17 10:03:34\n\nreplaces previous patch",
    "created_at": "2010-05-17T10:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3461#issuecomment-24365",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_3461_new.patch](tarball://root/attachments/some-uuid/ticket3461/trac_3461_new.patch) by @loefflerd created at 2010-05-17 10:03:34

replaces previous patch



---

archive/issue_comments_024366.json:
```json
{
    "body": "The original patch suffered from a particularly evil piece of bitrotting: since the patch was written, some change somewhere has meant that the trivial permutation now has truth value True, not False, which meant that the pushout code would never terminate -- it would keep on returning bigger and bigger towers of (empty) construction functors! \n\nThe new patch I've just uploaded gets around this by using the `is_one` method, instead of a plain truth value test. It passes doctests under 4.4.1. Anyone willing to sign off on my tiny changes, and maybe we can get this into Sage 5.0?",
    "created_at": "2010-05-17T10:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3461#issuecomment-24366",
    "user": "https://github.com/loefflerd"
}
```

The original patch suffered from a particularly evil piece of bitrotting: since the patch was written, some change somewhere has meant that the trivial permutation now has truth value True, not False, which meant that the pushout code would never terminate -- it would keep on returning bigger and bigger towers of (empty) construction functors! 

The new patch I've just uploaded gets around this by using the `is_one` method, instead of a plain truth value test. It passes doctests under 4.4.1. Anyone willing to sign off on my tiny changes, and maybe we can get this into Sage 5.0?



---

archive/issue_comments_024367.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-17T17:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3461#issuecomment-24367",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_024368.json:
```json
{
    "body": "Looks good to me.  Thanks David!",
    "created_at": "2010-05-17T17:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3461#issuecomment-24368",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  Thanks David!



---

archive/issue_comments_024369.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T01:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3461#issuecomment-24369",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
