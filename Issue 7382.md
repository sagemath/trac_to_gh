# Issue 7382: MonskyWashnitzer segfault

archive/issues_007382.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  @jbalakrishnan minz jpflori\n\nSo I don't actually *need* matrix_of_frobenius_hyperelliptic of a curve over an extension field, but I inadvertently passed it in during a computation and caused a segfault. It would be nice for this to work (coercion?), since the curve is defined over QQ anyway.\n\n\n```\nsage: R.<x> = QQ['x']\nsage: H = HyperellipticCurve(x^3-10*x+9)\nsage: K = Qp(3,5)\nsage: J.<a> = K.extension(x^30-3)\nsage: HJ = H.change_ring(J)\nsage: import sage.schemes.elliptic_curves.monsky_washnitzer as mw\nsage: M_frob, forms = mw.matrix_of_frobenius_hyperelliptic(HJ)\n\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7382\n\n",
    "created_at": "2009-11-03T17:59:21Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "MonskyWashnitzer segfault",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7382",
    "user": "https://github.com/jbalakrishnan"
}
```
Assignee: @robertwb

CC:  @jbalakrishnan minz jpflori

So I don't actually *need* matrix_of_frobenius_hyperelliptic of a curve over an extension field, but I inadvertently passed it in during a computation and caused a segfault. It would be nice for this to work (coercion?), since the curve is defined over QQ anyway.


```
sage: R.<x> = QQ['x']
sage: H = HyperellipticCurve(x^3-10*x+9)
sage: K = Qp(3,5)
sage: J.<a> = K.extension(x^30-3)
sage: HJ = H.change_ring(J)
sage: import sage.schemes.elliptic_curves.monsky_washnitzer as mw
sage: M_frob, forms = mw.matrix_of_frobenius_hyperelliptic(HJ)


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```


Issue created by migration from https://trac.sagemath.org/ticket/7382





---

archive/issue_comments_061981.json:
```json
{
    "body": "Changing component from number theory to algebraic geometry.",
    "created_at": "2014-12-12T11:39:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7382#issuecomment-61981",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from number theory to algebraic geometry.



---

archive/issue_comments_061982.json:
```json
{
    "body": "I cannot recreate this error anymore. (most likely it has been fixed indirectly)\n\nJen, could you double check?\n\nThanks!",
    "created_at": "2018-04-25T17:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7382#issuecomment-61982",
    "user": "https://github.com/edgarcosta"
}
```

I cannot recreate this error anymore. (most likely it has been fixed indirectly)

Jen, could you double check?

Thanks!



---

archive/issue_comments_061983.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-04-26T09:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7382#issuecomment-61983",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061984.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-05-01T12:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7382#issuecomment-61984",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061985.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7382#issuecomment-61985",
    "user": "https://github.com/videlec"
}
```

Resolution: wontfix



---

archive/issue_comments_061986.json:
```json
{
    "body": "closing positively reviewed duplicates",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7382#issuecomment-61986",
    "user": "https://github.com/videlec"
}
```

closing positively reviewed duplicates
