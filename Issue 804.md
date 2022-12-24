# Issue 804: Matrix should not inherit from AlgebraElement

archive/issues_000804.json:
```json
{
    "body": "Assignee: was\n\nCC:  jason pbruin\n\nKeywords: AlgebraElement, Matrix\n\nPeople just don't want to fix it because you'll have to rebuild everything after editing element.pxd.\n\nIssue created by migration from https://trac.sagemath.org/ticket/804\n\n",
    "created_at": "2007-10-03T08:30:30Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.3",
    "title": "Matrix should not inherit from AlgebraElement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/804",
    "user": "roed"
}
```
Assignee: was

CC:  jason pbruin

Keywords: AlgebraElement, Matrix

People just don't want to fix it because you'll have to rebuild everything after editing element.pxd.

Issue created by migration from https://trac.sagemath.org/ticket/804





---

archive/issue_comments_004843.json:
```json
{
    "body": "Maybe now is a good time to do it?\n\nCheers,\n\nMichael",
    "created_at": "2007-12-04T14:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4843",
    "user": "mabshoff"
}
```

Maybe now is a good time to do it?

Cheers,

Michael



---

archive/issue_comments_004844.json:
```json
{
    "body": "What are the reasons for the change in organization?",
    "created_at": "2007-12-05T19:12:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4844",
    "user": "mhansen"
}
```

What are the reasons for the change in organization?



---

archive/issue_comments_004845.json:
```json
{
    "body": "Changing component from algebraic geometry to linear algebra.",
    "created_at": "2008-01-24T09:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4845",
    "user": "AlexGhitza"
}
```

Changing component from algebraic geometry to linear algebra.



---

archive/issue_comments_004846.json:
```json
{
    "body": "The reason for the change is that not all matrices are Algebra Elements.",
    "created_at": "2008-11-14T06:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4846",
    "user": "robertwb"
}
```

The reason for the change is that not all matrices are Algebra Elements.



---

archive/issue_comments_004847.json:
```json
{
    "body": "What should it inherit from instead?  This is a naive question, but perhaps someone with not much skill but much patience could fix this :)",
    "created_at": "2009-12-30T05:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4847",
    "user": "kcrisman"
}
```

What should it inherit from instead?  This is a naive question, but perhaps someone with not much skill but much patience could fix this :)



---

archive/issue_comments_004848.json:
```json
{
    "body": "ModuleElement",
    "created_at": "2009-12-30T08:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4848",
    "user": "robertwb"
}
```

ModuleElement



---

archive/issue_comments_004849.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-04-02T00:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4849",
    "user": "pbruin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_004850.json:
```json
{
    "body": "Given that this ticket has been open for more than seven years, it turned out to be surprisingly straightforward.  There is one small simplification: `Matrix` used to have two identical methods `_mul_()` and `__mul__()`, now it only needs `__mul__()`.  On the other hand, new (but very straightforward) `__pow__()` and `__div__()` methods were required.",
    "created_at": "2014-04-02T00:33:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4850",
    "user": "pbruin"
}
```

Given that this ticket has been open for more than seven years, it turned out to be surprisingly straightforward.  There is one small simplification: `Matrix` used to have two identical methods `_mul_()` and `__mul__()`, now it only needs `__mul__()`.  On the other hand, new (but very straightforward) `__pow__()` and `__div__()` methods were required.



---

archive/issue_comments_004851.json:
```json
{
    "body": "Wow, nice necromancy!  Dumb question - any other translations of tutorials have this bit which would need to be translated?",
    "created_at": "2014-04-02T02:34:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4851",
    "user": "kcrisman"
}
```

Wow, nice necromancy!  Dumb question - any other translations of tutorials have this bit which would need to be translated?



---

archive/issue_comments_004852.json:
```json
{
    "body": "Replying to [comment:12 kcrisman]:\n> any other translations of tutorials have this bit which would need to be translated?\nIt seems not; `grep RingElement src/doc/*/tutorial/*` only finds the English and French ones.",
    "created_at": "2014-04-02T09:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4852",
    "user": "pbruin"
}
```

Replying to [comment:12 kcrisman]:
> any other translations of tutorials have this bit which would need to be translated?
It seems not; `grep RingElement src/doc/*/tutorial/*` only finds the English and French ones.



---

archive/issue_comments_004853.json:
```json
{
    "body": "> > any other translations of tutorials have this bit which would need to be translated?\n> It seems not; `grep RingElement src/doc/*/tutorial/*` only finds the English and French ones.\nInteresting - apparently that must have been added after the other translations were made.",
    "created_at": "2014-04-02T13:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4853",
    "user": "kcrisman"
}
```

> > any other translations of tutorials have this bit which would need to be translated?
> It seems not; `grep RingElement src/doc/*/tutorial/*` only finds the English and French ones.
Interesting - apparently that must have been added after the other translations were made.



---

archive/issue_comments_004854.json:
```json
{
    "body": "Hi,\n\nAt first glance, I thought this ticket would help to build tropical matrices as discussed in #14507... but no, the \"base ring\" for tropical matrix is a [semiring](http://en.wikipedia.org/wiki/Semiring) and not a ring (no requirement of an additive inverse). Am I right?\n\nVincent",
    "created_at": "2014-05-05T07:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4854",
    "user": "vdelecroix"
}
```

Hi,

At first glance, I thought this ticket would help to build tropical matrices as discussed in #14507... but no, the "base ring" for tropical matrix is a [semiring](http://en.wikipedia.org/wiki/Semiring) and not a ring (no requirement of an additive inverse). Am I right?

Vincent



---

archive/issue_comments_004855.json:
```json
{
    "body": "Replying to [comment:15 vdelecroix]:\n> At first glance, I thought this ticket would help to build tropical matrices as discussed in #14507... but no, the \"base ring\" for tropical matrix is a [semiring](http://en.wikipedia.org/wiki/Semiring) and not a ring (no requirement of an additive inverse). Am I right?\nI think you are.  Everywhere in Sage, matrices and vectors are assumed to have coefficients in some base ring.  This would probably be much harder to change than the inheritance issue addressed in this ticket.  If enough people want tropical matrices, then it seems we need new classes `Matrix_semiring` and `Vector_semiring`, possibly inheriting from some `ModuleElement_semiring`...",
    "created_at": "2014-05-05T09:13:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4855",
    "user": "pbruin"
}
```

Replying to [comment:15 vdelecroix]:
> At first glance, I thought this ticket would help to build tropical matrices as discussed in #14507... but no, the "base ring" for tropical matrix is a [semiring](http://en.wikipedia.org/wiki/Semiring) and not a ring (no requirement of an additive inverse). Am I right?
I think you are.  Everywhere in Sage, matrices and vectors are assumed to have coefficients in some base ring.  This would probably be much harder to change than the inheritance issue addressed in this ticket.  If enough people want tropical matrices, then it seems we need new classes `Matrix_semiring` and `Vector_semiring`, possibly inheriting from some `ModuleElement_semiring`...



---

archive/issue_comments_004856.json:
```json
{
    "body": "\n```\nsage -t --long src/sage/structure/element.pyx  # 2 doctests failed\n```\n",
    "created_at": "2014-05-14T20:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4856",
    "user": "pbruin"
}
```


```
sage -t --long src/sage/structure/element.pyx  # 2 doctests failed
```




---

archive/issue_comments_004857.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-05-14T20:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4857",
    "user": "pbruin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_004858.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-14T21:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4858",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_004859.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-05-14T21:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4859",
    "user": "pbruin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_004860.json:
```json
{
    "body": "Looks good to me. I also think that tropical matrices should have their own classes.\n\nMy copy did not compile against 6.3.beta3 but was probably more an issue with the beta since it failed before attempting to build the sage library. With 6.3.beta5 it works like a charm.",
    "created_at": "2014-07-18T11:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4860",
    "user": "lftabera"
}
```

Looks good to me. I also think that tropical matrices should have their own classes.

My copy did not compile against 6.3.beta3 but was probably more an issue with the beta since it failed before attempting to build the sage library. With 6.3.beta5 it works like a charm.



---

archive/issue_comments_004861.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-07-18T11:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4861",
    "user": "lftabera"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_004862.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-07-19T04:57:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/804#issuecomment-4862",
    "user": "vbraun"
}
```

Resolution: fixed
