# Issue 8098: solve_mod is horribly broken

archive/issues_008098.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  polybori @malb @robertwb\n\nI was just grading papers in my class and one student (Andrew Ohana) pointed out in his solution that Sage's solve_mod is massively broken.  For example:\n\n```\nsage: var('x')\nsage: solve_mod([x^2==1], 9)\n[]         # WTF?\n```\n\nand:\n\n```\nsage: solve_mod([x^2==1], 8)\n[(1,), (3,), (4,), (5,), (7,)]\n```\n\n\nEtc. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8098\n\n",
    "created_at": "2010-01-27T23:13:42Z",
    "labels": [
        "basic arithmetic",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "solve_mod is horribly broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8098",
    "user": "@williamstein"
}
```
Assignee: @aghitza

CC:  polybori @malb @robertwb

I was just grading papers in my class and one student (Andrew Ohana) pointed out in his solution that Sage's solve_mod is massively broken.  For example:

```
sage: var('x')
sage: solve_mod([x^2==1], 9)
[]         # WTF?
```

and:

```
sage: solve_mod([x^2==1], 8)
[(1,), (3,), (4,), (5,), (7,)]
```


Etc. 

Issue created by migration from https://trac.sagemath.org/ticket/8098





---

archive/issue_comments_071047.json:
```json
{
    "body": "I tried to chase down the bug but it seems the rabbit hole goes deeper (all the way to multivariate singular polynomial evaluation). \n\n\n```\nsage: P.<x,y> = Zmod(3^2)[]\nsage: f=P(x*x)\nsage: f(3,0)\n1\n\nsage: P.<x,y> = Zmod(10)[]\nsage: f=P(x*y)\nsage: f(2,5)\n1\n```\n\n\nI think the problem is in the __call__ method in http://sagenb.org/src/libs/singular/polynomial.pyx/ but its all Cython land there, so I can't do much. In any case seems that Singular is fine, and something gets lost in the translation.\n\n\n```\n> ring R= (integer,9),(x,y),dp;\n> poly f=x2;\n> subst(f,x,3,y,0);\n0\n```\n",
    "created_at": "2010-02-01T06:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71047",
    "user": "rkirov"
}
```

I tried to chase down the bug but it seems the rabbit hole goes deeper (all the way to multivariate singular polynomial evaluation). 


```
sage: P.<x,y> = Zmod(3^2)[]
sage: f=P(x*x)
sage: f(3,0)
1

sage: P.<x,y> = Zmod(10)[]
sage: f=P(x*y)
sage: f(2,5)
1
```


I think the problem is in the __call__ method in http://sagenb.org/src/libs/singular/polynomial.pyx/ but its all Cython land there, so I can't do much. In any case seems that Singular is fine, and something gets lost in the translation.


```
> ring R= (integer,9),(x,y),dp;
> poly f=x2;
> subst(f,x,3,y,0);
0
```




---

archive/issue_comments_071048.json:
```json
{
    "body": "We need a Singular expert to comment on this.\n\nNote that the function we call is `fast_map()` and it returns `1` as the generator of the ideal in this case.",
    "created_at": "2010-02-01T18:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71048",
    "user": "@burcin"
}
```

We need a Singular expert to comment on this.

Note that the function we call is `fast_map()` and it returns `1` as the generator of the ideal in this case.



---

archive/issue_comments_071049.json:
```json
{
    "body": "The Singular map works fine in my somewhat ancient Singular version here...\n\n```\n> poly f=x2;\n> subst(f,x,3,y,0);\n0\n> map m=R,3,0;\n> m(f);\n0\n\n```\n\n\nDoes this fail with newer versions?",
    "created_at": "2010-02-02T08:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71049",
    "user": "PolyBoRi"
}
```

The Singular map works fine in my somewhat ancient Singular version here...

```
> poly f=x2;
> subst(f,x,3,y,0);
0
> map m=R,3,0;
> m(f);
0

```


Does this fail with newer versions?



---

archive/issue_comments_071050.json:
```json
{
    "body": "I have version 3-1-0 and Singular returns the same output as you (which is correct). I think the problem is in Sage.",
    "created_at": "2010-02-02T08:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71050",
    "user": "rkirov"
}
```

I have version 3-1-0 and Singular returns the same output as you (which is correct). I think the problem is in Sage.



---

archive/issue_comments_071051.json:
```json
{
    "body": "There's a discussion on this matter on [libsingular-devel], cf. http://groups.google.com/group/libsingular-devel/browse_thread/thread/bd0aa6c4d7b6ecc3\n\nThis still doesn't explain why subst works but I guess it uses a different code path.",
    "created_at": "2010-02-04T11:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71051",
    "user": "@malb"
}
```

There's a discussion on this matter on [libsingular-devel], cf. http://groups.google.com/group/libsingular-devel/browse_thread/thread/bd0aa6c4d7b6ecc3

This still doesn't explain why subst works but I guess it uses a different code path.



---

archive/issue_comments_071052.json:
```json
{
    "body": "completely independent implementation.\n\nCheers,\nMichael",
    "created_at": "2010-02-04T12:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71052",
    "user": "PolyBoRi"
}
```

completely independent implementation.

Cheers,
Michael



---

archive/issue_comments_071053.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-09T18:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71053",
    "user": "@malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071054.json:
```json
{
    "body": "Attachment [trac_8098.patch](tarball://root/attachments/some-uuid/ticket8098/trac_8098.patch) by @malb created at 2010-02-09 18:50:54\n\nSorry for the delay.",
    "created_at": "2010-02-09T18:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71054",
    "user": "@malb"
}
```

Attachment [trac_8098.patch](tarball://root/attachments/some-uuid/ticket8098/trac_8098.patch) by @malb created at 2010-02-09 18:50:54

Sorry for the delay.



---

archive/issue_comments_071055.json:
```json
{
    "body": "The attached patch will cause a SEGFAULT which is due to a bug in Singular (I believe). The bug is not caused by my patch but just uncovered (well, if my analysis on [libsingular-devel] is correct)",
    "created_at": "2010-02-09T20:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71055",
    "user": "@malb"
}
```

The attached patch will cause a SEGFAULT which is due to a bug in Singular (I believe). The bug is not caused by my patch but just uncovered (well, if my analysis on [libsingular-devel] is correct)



---

archive/issue_comments_071056.json:
```json
{
    "body": "Ticket depends on #8228",
    "created_at": "2010-02-10T13:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71056",
    "user": "@malb"
}
```

Ticket depends on #8228



---

archive/issue_comments_071057.json:
```json
{
    "body": "Anyone?",
    "created_at": "2010-03-03T12:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71057",
    "user": "@malb"
}
```

Anyone?



---

archive/issue_comments_071058.json:
```json
{
    "body": "I tried the doctests, but unfortunately one more test is Segfaulting wrt #7773:\n\n```\n[zimmerma@coing sage]$ sage -t -verbose rings/polynomial/multi_polynomial_libsingular.pyx\n...\nTrying:\n    f(Integer(0),Integer(0),Integer(0))###line 1725:_sage_    >>> f(0,0,0)\nExpecting:\n    0\n\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\nSince this is precisely linked to the modified file, I give a negative review.",
    "created_at": "2010-03-14T15:27:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71058",
    "user": "@zimmermann6"
}
```

I tried the doctests, but unfortunately one more test is Segfaulting wrt #7773:

```
[zimmerma@coing sage]$ sage -t -verbose rings/polynomial/multi_polynomial_libsingular.pyx
...
Trying:
    f(Integer(0),Integer(0),Integer(0))###line 1725:_sage_    >>> f(0,0,0)
Expecting:
    0


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```

Since this is precisely linked to the modified file, I give a negative review.



---

archive/issue_comments_071059.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-14T15:27:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71059",
    "user": "@zimmermann6"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071060.json:
```json
{
    "body": "Paul, which combination of SPKGs and patches did you apply?",
    "created_at": "2010-03-14T15:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71060",
    "user": "@malb"
}
```

Paul, which combination of SPKGs and patches did you apply?



---

archive/issue_comments_071061.json:
```json
{
    "body": "Michael,\n\n> Paul, which combination of SPKGs and patches did you apply? \n\njust a clone of 4.3.3 + your patch. I just reproduced it on a different computer.\n\nPaul",
    "created_at": "2010-03-15T10:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71061",
    "user": "@zimmermann6"
}
```

Michael,

> Paul, which combination of SPKGs and patches did you apply? 

just a clone of 4.3.3 + your patch. I just reproduced it on a different computer.

Paul



---

archive/issue_comments_071062.json:
```json
{
    "body": "Paul, this ticket depends on an update of Singular (cf. #8228 and #8059)\n\nCheers,\nMartin",
    "created_at": "2010-03-15T11:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71062",
    "user": "@malb"
}
```

Paul, this ticket depends on an update of Singular (cf. #8228 and #8059)

Cheers,
Martin



---

archive/issue_comments_071063.json:
```json
{
    "body": "With 4.6.1.rc1 I get:\n\n```python\nsage: var('x')\nx\nsage: solve_mod([x^2==1], 9)\n[(1,), (8,)]\nsage: solve_mod([x^2==1], 8)\n[(1,), (3,), (5,), (7,)]\n```\n\n\nThus, I believe this bug is fixed.",
    "created_at": "2011-01-14T15:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71063",
    "user": "@malb"
}
```

With 4.6.1.rc1 I get:

```python
sage: var('x')
x
sage: solve_mod([x^2==1], 9)
[(1,), (8,)]
sage: solve_mod([x^2==1], 8)
[(1,), (3,), (5,), (7,)]
```


Thus, I believe this bug is fixed.



---

archive/issue_comments_071064.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-14T15:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8098#issuecomment-71064",
    "user": "@malb"
}
```

Resolution: fixed
