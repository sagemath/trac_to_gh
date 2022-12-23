# Issue 995: Generalize polynomial .roots() method by adding optional ring= parameter for result ring

archive/issues_000995.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\n<wstein> Better might be to improve the roots function so that it can take \n an optional ring as input.\n e.g.,\n    f = x^3 + 1 (over QQ say), then\n f.roots(ComplexField(200))\n would give the roots in that field.\n What do you think?\n<cwitty> I like it.\n I like it a lot.\n f.roots(RealField(200)), f.roots(AA), f.roots(RealIntervalField(200)) ...\n<wstein> Yep.\n And it could be intelligent, but when it doesn't know what to do just \n return f.change_ring(R).roots(...)\n But in many cases it could use that f is defined over a better ring\n than R, e.g., QQ, to find the roots\n to lots of precision.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/995\n\n",
    "created_at": "2007-10-25T06:21:10Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "Generalize polynomial .roots() method by adding optional ring= parameter for result ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/995",
    "user": "cwitty"
}
```
Assignee: cwitty


```
<wstein> Better might be to improve the roots function so that it can take 
 an optional ring as input.
 e.g.,
    f = x^3 + 1 (over QQ say), then
 f.roots(ComplexField(200))
 would give the roots in that field.
 What do you think?
<cwitty> I like it.
 I like it a lot.
 f.roots(RealField(200)), f.roots(AA), f.roots(RealIntervalField(200)) ...
<wstein> Yep.
 And it could be intelligent, but when it doesn't know what to do just 
 return f.change_ring(R).roots(...)
 But in many cases it could use that f is defined over a better ring
 than R, e.g., QQ, to find the roots
 to lots of precision.
```


Issue created by migration from https://trac.sagemath.org/ticket/995





---

archive/issue_comments_006061.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-11-04T03:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/995#issuecomment-6061",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_006062.json:
```json
{
    "body": "This adds a ring= argument for the univariate polynomial .roots() method, so that you can find the complex roots of a polynomial given over QQ (along with many other possibilities).  Along with that change, we change the default root-finding algorithm for polynomials over RR and CC to numpy instead of Pari; this is vastly faster, but occasionally slightly less accurate, and does not give exactly the same answers on different architectures.\n\nThese patches depend on the patch from #1096; without it, some of the doctests will fail.\n\nThese patches pass -testall on my 32-bit and 64-bit x86 Linux boxes, but have not been tested on other platforms; it's possible that the floating-point answers will vary more than allowed by the doctests.",
    "created_at": "2007-11-04T04:01:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/995#issuecomment-6062",
    "user": "cwitty"
}
```

This adds a ring= argument for the univariate polynomial .roots() method, so that you can find the complex roots of a polynomial given over QQ (along with many other possibilities).  Along with that change, we change the default root-finding algorithm for polynomials over RR and CC to numpy instead of Pari; this is vastly faster, but occasionally slightly less accurate, and does not give exactly the same answers on different architectures.

These patches depend on the patch from #1096; without it, some of the doctests will fail.

These patches pass -testall on my 32-bit and 64-bit x86 Linux boxes, but have not been tested on other platforms; it's possible that the floating-point answers will vary more than allowed by the doctests.



---

archive/issue_comments_006063.json:
```json
{
    "body": "It works great in almost all cases, but\n\n\n```\nsage: R.<x> = ZZ[]\nsage: f = 2*x-3\nsage: f.roots(ZZ)\n[(3/2, 1)]\n```\n\n\nPerhaps this is due to the default behavior of roots() over Z, not the new code (which is really nice).",
    "created_at": "2007-11-04T04:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/995#issuecomment-6063",
    "user": "robertwb"
}
```

It works great in almost all cases, but


```
sage: R.<x> = ZZ[]
sage: f = 2*x-3
sage: f.roots(ZZ)
[(3/2, 1)]
```


Perhaps this is due to the default behavior of roots() over Z, not the new code (which is really nice).



---

archive/issue_comments_006064.json:
```json
{
    "body": "The bug Robert found here is now #1100.  (It's not caused by this patch.)",
    "created_at": "2007-11-04T04:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/995#issuecomment-6064",
    "user": "cwitty"
}
```

The bug Robert found here is now #1100.  (It's not caused by this patch.)



---

archive/issue_comments_006065.json:
```json
{
    "body": "applied to 2.8.12.rc0",
    "created_at": "2007-11-06T21:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/995#issuecomment-6065",
    "user": "mabshoff"
}
```

applied to 2.8.12.rc0



---

archive/issue_comments_006066.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T21:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/995",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/995#issuecomment-6066",
    "user": "mabshoff"
}
```

Resolution: fixed
