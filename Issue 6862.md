# Issue 6862: Mixing of different domains for symbolic variables

archive/issues_006862.json:
```json
{
    "body": "From suge-support\n\nOn Sep 1, 11:35 pm, Mani chandra <mchan...`@`iitk.ac.in> wrote:\n\n> Mani chandra wrote:\n\n```\nsage: x = a + I*b\nsage: real(x.conjugate().simplify())\nreal_part(a) + imag_part(b)\nsage: real(x.conjugate())\nreal_part(a) - imag_part(b)\n```\n\n\nThis seems to be happening because maxima(via simplify)\ntreats variables as real whereas pynac treats as \ncomplex.\n\n\n\n```\nsage: x.conjugate()\nconjugate(a) - I*conjugate(b)\n\nsage: x.conjugate().simplify()\na - I*b\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6862\n\n",
    "created_at": "2009-09-02T11:35:47Z",
    "labels": [
        "symbolics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.8",
    "title": "Mixing of different domains for symbolic variables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6862",
    "user": "@golam-m-hossain"
}
```
From suge-support

On Sep 1, 11:35 pm, Mani chandra <mchan...`@`iitk.ac.in> wrote:

> Mani chandra wrote:

```
sage: x = a + I*b
sage: real(x.conjugate().simplify())
real_part(a) + imag_part(b)
sage: real(x.conjugate())
real_part(a) - imag_part(b)
```


This seems to be happening because maxima(via simplify)
treats variables as real whereas pynac treats as 
complex.



```
sage: x.conjugate()
conjugate(a) - I*conjugate(b)

sage: x.conjugate().simplify()
a - I*b
```



Issue created by migration from https://trac.sagemath.org/ticket/6862





---

archive/issue_comments_056604.json:
```json
{
    "body": "See [http://groups.google.com/group/sage-devel/browse_thread/thread/e25e03c9dba88a93](http://groups.google.com/group/sage-devel/browse_thread/thread/e25e03c9dba88a93)\n\nAlso, based on the hint there from Robert Dodier, here is the eventual way a fix will have to occur, perhaps as outlined in the thread:\n\n```\nsage: assume(a,'complex')\nsage: x.conjugate().simplify()\n-I*b + conjugate(a)\n```\n",
    "created_at": "2009-09-04T18:04:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56604",
    "user": "@kcrisman"
}
```

See [http://groups.google.com/group/sage-devel/browse_thread/thread/e25e03c9dba88a93](http://groups.google.com/group/sage-devel/browse_thread/thread/e25e03c9dba88a93)

Also, based on the hint there from Robert Dodier, here is the eventual way a fix will have to occur, perhaps as outlined in the thread:

```
sage: assume(a,'complex')
sage: x.conjugate().simplify()
-I*b + conjugate(a)
```




---

archive/issue_comments_056605.json:
```json
{
    "body": "See also this closely related [ask.sagemath.org question](http://ask.sagemath.org/question/2287/bug-with-absolute-value-of-a-complex-variable), where the following example occurs.\n\n\n```\nsage: var('a')\na\nsage: b=a*a.conjugate()-a*a\nsage: b\n-a^2 + a*conjugate(a)\nsage: simplify(b)\n0\n```\n\n\nI think this is a little weird, though, since in Maxima\n\n```\n(%i1) domain:complex;\n(%o1)                               complex\n(%i2) -a^2+a*conjugate(a);\n(%o2)                                  0\n```\n\nand sadly, the Maxima manual says that all this is expected to do is\n\n```\nOption variable: domain\nDefault value: real\n\nWhen domain is set to complex, sqrt (x^2) will remain sqrt (x^2) instead of returning abs(x).\n```\n\n\nWilliam says in the thread above that\n\n```\nWhat we need is to queue up (put in some list somewhere) all\ndeclaration that could ever be needed, then whenever we do a Sage -->\ncalculus Maxima conversion, we would empty the queue if it is\nnonempty.  Also, if Maxima were to crash/get restarted (does that ever\nhappen anymore), we would need to  make sure all var's get set again.\nThis seems very do-able.\n```\n\nand perhaps that could be part of the initialization process of any variable - without actually calling Maxima at that time, of course!",
    "created_at": "2013-02-24T02:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56605",
    "user": "@kcrisman"
}
```

See also this closely related [ask.sagemath.org question](http://ask.sagemath.org/question/2287/bug-with-absolute-value-of-a-complex-variable), where the following example occurs.


```
sage: var('a')
a
sage: b=a*a.conjugate()-a*a
sage: b
-a^2 + a*conjugate(a)
sage: simplify(b)
0
```


I think this is a little weird, though, since in Maxima

```
(%i1) domain:complex;
(%o1)                               complex
(%i2) -a^2+a*conjugate(a);
(%o2)                                  0
```

and sadly, the Maxima manual says that all this is expected to do is

```
Option variable: domain
Default value: real

When domain is set to complex, sqrt (x^2) will remain sqrt (x^2) instead of returning abs(x).
```


William says in the thread above that

```
What we need is to queue up (put in some list somewhere) all
declaration that could ever be needed, then whenever we do a Sage -->
calculus Maxima conversion, we would empty the queue if it is
nonempty.  Also, if Maxima were to crash/get restarted (does that ever
happen anymore), we would need to  make sure all var's get set again.
This seems very do-able.
```

and perhaps that could be part of the initialization process of any variable - without actually calling Maxima at that time, of course!



---

archive/issue_comments_056606.json:
```json
{
    "body": "#14628 is somewhat related, though this would not fix it, as far as I can tell.",
    "created_at": "2013-06-13T16:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56606",
    "user": "@kcrisman"
}
```

#14628 is somewhat related, though this would not fix it, as far as I can tell.



---

archive/issue_comments_056607.json:
```json
{
    "body": "Let's make sure to also test #11656, which was a dup, when (?!) we fix this:\n\n```\nvar('c', domain='complex')\nvar('x', domain='real')\nC = c * exp(-x^2)\nprint (C)\n    c*e^(-x^2)\n\nprint (C.imag())\n    e^(-x^2)*imag_part(c)\n\nprint (C.imag().simplify_full()) \n    0\n```\n",
    "created_at": "2013-06-13T16:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56607",
    "user": "@kcrisman"
}
```

Let's make sure to also test #11656, which was a dup, when (?!) we fix this:

```
var('c', domain='complex')
var('x', domain='real')
C = c * exp(-x^2)
print (C)
    c*e^(-x^2)

print (C.imag())
    e^(-x^2)*imag_part(c)

print (C.imag().simplify_full()) 
    0
```




---

archive/issue_comments_056608.json:
```json
{
    "body": "see also #14305\n\nPaul",
    "created_at": "2013-08-29T07:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56608",
    "user": "@zimmermann6"
}
```

see also #14305

Paul



---

archive/issue_comments_056609.json:
```json
{
    "body": "Changing priority from critical to major.",
    "created_at": "2020-10-08T12:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56609",
    "user": "@kcrisman"
}
```

Changing priority from critical to major.



---

archive/issue_comments_056610.json:
```json
{
    "body": "See https://groups.google.com/forum/#!topic/sage-devel/U1dsVFP-2PA",
    "created_at": "2020-10-08T12:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56610",
    "user": "@kcrisman"
}
```

See https://groups.google.com/forum/#!topic/sage-devel/U1dsVFP-2PA



---

archive/issue_comments_056611.json:
```json
{
    "body": "The result reported in the description is correct :\n\n\n```\nsage: var(\"a, b\")\n(a, b)\nsage: c=a+I*b\nsage: c.real()\n-imag_part(b) + real_part(a)\nsage: c.conjugate()\nconjugate(a) - I*conjugate(b)\nsage: c.conjugate().real()\n-imag_part(b) + real_part(a)\n```\n\n\n//unless `a` and `b` are **known** to be real}}}//. If so :\n\n```\nsage: assume(a, b, \"real\")\nsage: c.real()\na\nsage: c.conjugate()\na - I*b\nsage: c.conjugate().real()\na\n```\n\n\nwhich is also correct.\n\n==> marking as invalid and requesting review in order to get this bug closed...",
    "created_at": "2021-03-13T13:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56611",
    "user": "@EmmanuelCharpentier"
}
```

The result reported in the description is correct :


```
sage: var("a, b")
(a, b)
sage: c=a+I*b
sage: c.real()
-imag_part(b) + real_part(a)
sage: c.conjugate()
conjugate(a) - I*conjugate(b)
sage: c.conjugate().real()
-imag_part(b) + real_part(a)
```


//unless `a` and `b` are **known** to be real}}}//. If so :

```
sage: assume(a, b, "real")
sage: c.real()
a
sage: c.conjugate()
a - I*b
sage: c.conjugate().real()
a
```


which is also correct.

==> marking as invalid and requesting review in order to get this bug closed...



---

archive/issue_comments_056612.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-03-13T13:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56612",
    "user": "@EmmanuelCharpentier"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_056613.json:
```json
{
    "body": "The problem is Maxima, not Sage. (Or rather, the fact that we don't have a good way to make sure that Maxima variables are complex by default, or didn't at the time.)\n\n```\nsage: real(x.conjugate().simplify())\nreal_part(a) + imag_part(b)\n```\n",
    "created_at": "2021-03-13T22:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56613",
    "user": "@kcrisman"
}
```

The problem is Maxima, not Sage. (Or rather, the fact that we don't have a good way to make sure that Maxima variables are complex by default, or didn't at the time.)

```
sage: real(x.conjugate().simplify())
real_part(a) + imag_part(b)
```




---

archive/issue_comments_056614.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2021-03-13T22:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56614",
    "user": "@kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_056615.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2021-03-13T22:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56615",
    "user": "@kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056616.json:
```json
{
    "body": "Replying to [comment:8 kcrisman]:\n> The problem is Maxima, not Sage. (Or rather, the fact that we don't have a good way to make sure that Maxima variables are complex by default, or didn't at the time.)\n> {{{\n> sage: real(x.conjugate().simplify())\n> real_part(a) + imag_part(b)\n> }}}\n\nUnless `a` and `b` are known to be real, this is the correct result. When this assumption is verifiable, Sage also gives the expected result (see comment 7)...\n\nBTW, at least the \"Computational mathematics with SageMath\" book states that SR variables behave, by default, as complex variables, but, IIRC, no formal assertion is made in the documentation about this. AFAICT, we use a\"domain:complex\" assertion in our uses of Maxima.\n\nSo what should be the behavior you expect ? OIn fact, I'm having troubleperceivng the point of this ticket...\n\n==> re-asking review ; possibly after discussion on `sage-devel` if we can't agree...",
    "created_at": "2021-03-13T22:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56616",
    "user": "@EmmanuelCharpentier"
}
```

Replying to [comment:8 kcrisman]:
> The problem is Maxima, not Sage. (Or rather, the fact that we don't have a good way to make sure that Maxima variables are complex by default, or didn't at the time.)
> {{{
> sage: real(x.conjugate().simplify())
> real_part(a) + imag_part(b)
> }}}

Unless `a` and `b` are known to be real, this is the correct result. When this assumption is verifiable, Sage also gives the expected result (see comment 7)...

BTW, at least the "Computational mathematics with SageMath" book states that SR variables behave, by default, as complex variables, but, IIRC, no formal assertion is made in the documentation about this. AFAICT, we use a"domain:complex" assertion in our uses of Maxima.

So what should be the behavior you expect ? OIn fact, I'm having troubleperceivng the point of this ticket...

==> re-asking review ; possibly after discussion on `sage-devel` if we can't agree...



---

archive/issue_comments_056617.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-03-13T22:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56617",
    "user": "@EmmanuelCharpentier"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056618.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2021-03-14T02:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56618",
    "user": "@kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056619.json:
```json
{
    "body": "> > {{{\n> > sage: real(x.conjugate().simplify())\n> > real_part(a) + imag_part(b)\n> > }}}\n\nI thought you said this one was correct:\n\n```\nsage: c.conjugate().real()\n-imag_part(b) + real_part(a)\n```\n\nSo you can see that the Maxima (`.simplify()`) and Sage result are different, unless I'm even more confused.  \n\n> BTW, at least the \"Computational mathematics with SageMath\" book states that SR variables behave, by default, as complex variables, but, IIRC, no formal assertion is made in the documentation about this. AFAICT, we use a\"domain:complex\" assertion in our uses of Maxima.\n\nThe problem is that `domain:complex` doesn't make the Maxima variables complex, it just doesn't simplify square roots (see the linked sage-devel thread in comment:1).    We do use complex variables for `SR` but those live in Pynac.  However, since `.simplify()` is a Sage method (it just sends to Maxima and back), we don't want that giving wrong behavior.\n\nAnyway, perhaps we need a third party to adjudicate; I did try to suss out the right behavior after your comment:7 but I have been known to make sign errors in my life :-)  But I hope I clarified the exact status in this comment.\n\n```\nvar(\"a, b\")\nc=a+I*b\nprint(c.conjugate().real())\nprint((c.conjugate().simplify()).real())\n```\n\n[gives](https://sagecell.sagemath.org/?z=eJwrSyzSUErUUUhS0uTlSrZN1PbUSuLlUk7WK0pNzNHQBDOT8_OyStMTS1JB_IKizLwSDRRBqFq4JJpscWZuQU5mWiVQBUwlAOCYI5M=&lang=sage&interacts=eJyLjgUAARUAuQ==)\n\n```\n-imag_part(b) + real_part(a)\nimag_part(b) + real_part(a)\n```\n\nand I don't think those can both be correct.",
    "created_at": "2021-03-14T02:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56619",
    "user": "@kcrisman"
}
```

> > {{{
> > sage: real(x.conjugate().simplify())
> > real_part(a) + imag_part(b)
> > }}}

I thought you said this one was correct:

```
sage: c.conjugate().real()
-imag_part(b) + real_part(a)
```

So you can see that the Maxima (`.simplify()`) and Sage result are different, unless I'm even more confused.  

> BTW, at least the "Computational mathematics with SageMath" book states that SR variables behave, by default, as complex variables, but, IIRC, no formal assertion is made in the documentation about this. AFAICT, we use a"domain:complex" assertion in our uses of Maxima.

The problem is that `domain:complex` doesn't make the Maxima variables complex, it just doesn't simplify square roots (see the linked sage-devel thread in comment:1).    We do use complex variables for `SR` but those live in Pynac.  However, since `.simplify()` is a Sage method (it just sends to Maxima and back), we don't want that giving wrong behavior.

Anyway, perhaps we need a third party to adjudicate; I did try to suss out the right behavior after your comment:7 but I have been known to make sign errors in my life :-)  But I hope I clarified the exact status in this comment.

```
var("a, b")
c=a+I*b
print(c.conjugate().real())
print((c.conjugate().simplify()).real())
```

[gives](https://sagecell.sagemath.org/?z=eJwrSyzSUErUUUhS0uTlSrZN1PbUSuLlUk7WK0pNzNHQBDOT8_OyStMTS1JB_IKizLwSDRRBqFq4JJpscWZuQU5mWiVQBUwlAOCYI5M=&lang=sage&interacts=eJyLjgUAARUAuQ==)

```
-imag_part(b) + real_part(a)
imag_part(b) + real_part(a)
```

and I don't think those can both be correct.



---

archive/issue_comments_056620.json:
```json
{
    "body": "Replying to [comment:10 kcrisman]:\n> Anyway, perhaps we need a third party to adjudicate; I did try to suss out the right behavior after your comment:7 but I have been known to make sign errors in my life :-)  But I hope I clarified the exact status in this comment.\n> {{{\n> var(\"a, b\")\n> c=a+I*b\n> print(c.conjugate().real())\n> print((c.conjugate().simplify()).real())\n> }}}\n> [gives](https://sagecell.sagemath.org/?z=eJwrSyzSUErUUUhS0uTlSrZN1PbUSuLlUk7WK0pNzNHQBDOT8_OyStMTS1JB_IKizLwSDRRBqFq4JJpscWZuQU5mWiVQBUwlAOCYI5M=&lang=sage&interacts=eJyLjgUAARUAuQ==)\n> {{{\n> -imag_part(b) + real_part(a)\n> imag_part(b) + real_part(a)\n> }}}\n> and I don't think those can both be correct.\n\nIndeed; I'd say that the problem diagnosed in the ticket is spot on. I also don't know what the best solution is. Note that the two results are both correct if `imag_part(b)==0`, which is what maxima assumes (and we inherit those assumptions by the implementation of `simplify`).\n\nA minimal solution would be to document (in simplify and/or in real_part, imag_part, and conjugate) that for `simplify`, symbolic variables are assumed to be real, so that `conjugate(x).simplify()==real_part(x).simplify()==x` and `imag_part(x).simplify()==0`.",
    "created_at": "2021-03-14T20:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56620",
    "user": "@nbruin"
}
```

Replying to [comment:10 kcrisman]:
> Anyway, perhaps we need a third party to adjudicate; I did try to suss out the right behavior after your comment:7 but I have been known to make sign errors in my life :-)  But I hope I clarified the exact status in this comment.
> {{{
> var("a, b")
> c=a+I*b
> print(c.conjugate().real())
> print((c.conjugate().simplify()).real())
> }}}
> [gives](https://sagecell.sagemath.org/?z=eJwrSyzSUErUUUhS0uTlSrZN1PbUSuLlUk7WK0pNzNHQBDOT8_OyStMTS1JB_IKizLwSDRRBqFq4JJpscWZuQU5mWiVQBUwlAOCYI5M=&lang=sage&interacts=eJyLjgUAARUAuQ==)
> {{{
> -imag_part(b) + real_part(a)
> imag_part(b) + real_part(a)
> }}}
> and I don't think those can both be correct.

Indeed; I'd say that the problem diagnosed in the ticket is spot on. I also don't know what the best solution is. Note that the two results are both correct if `imag_part(b)==0`, which is what maxima assumes (and we inherit those assumptions by the implementation of `simplify`).

A minimal solution would be to document (in simplify and/or in real_part, imag_part, and conjugate) that for `simplify`, symbolic variables are assumed to be real, so that `conjugate(x).simplify()==real_part(x).simplify()==x` and `imag_part(x).simplify()==0`.



---

archive/issue_comments_056621.json:
```json
{
    "body": "Replying to [comment:11 nbruin]:\n\n[ Snip... ]\n\n> Indeed; I'd say that the problem diagnosed in the ticket is spot on. \n\nIndeed...\n\n> I also don't know what the best solution is. Note that the two results are both correct if `imag_part(b)==0`, which is what maxima assumes (and we inherit those assumptions by the implementation of `simplify`).\n> \n> A minimal solution would be to document (in simplify and/or in real_part, imag_part, and conjugate) that for `simplify`, symbolic variables are assumed to be real, so that `conjugate(x).simplify()==real_part(x).simplify()==x` and `imag_part(x).simplify()==0`.\n\nAt the (accepted) risk of lampooning the British Commons : No, no, no, no, no, no, no, no. \n\n\nAnd no...\n\nThis assumption is a way too large limitation of Sage's algebraic abilities. And can't be enforced by checks...\n\nFinding the source of the problem is necessary. It might help to show that the problem is alleviated by //renaming// the variables :\n\n\n```\nsage: %cpaste\nPasting code; enter '--' alone on the line to stop or use Ctrl-D.\n:var('a,b')\n:c=a+I*b\n:L=c.operands()\n:aL=[maxima.gensym().sage() for u in L]\n:D=dict(zip(L,aL))\n:DI=dict(zip(aL,L))\n:print(c.conjugate().real())\n:print(c.conjugate().simplify().real())\n:print(c.subs(D).conjugate().real().subs(DI))\n:print(c.subs(D).conjugate().simplify().real().subs(DI))\n:--\n(a, b)\n-imag_part(b) + real_part(a)\nimag_part(b) + real_part(a)\n-imag_part(b) + real_part(a)\n-imag_part(b) + real_part(a)\n```\n\n\nHowever :\n\n```\nsage: print(c.conjugate().subs(D).simplify().real().subs(DI))\nimag_part(b) + real_part(a)\n```\n\n\n\nThis behaviour let us think that somehow, `simplify` doesn't account for the \"complexity\"of `(-I*b\")`. Another hint in this direction :\n\n\n```\nsage: with assuming(a,b,\"real\"):c.conjugate().simplify().real()\na\nsage: with assuming(a,b,\"complex\"):c.conjugate().simplify().real()\n-imag_part(b) + real_part(a)\n```\n\nwhich is correct.\n\n\nThis suggests a direction for debugging the  source (which is probably in `pynac` territory, i. e. put of my reach...) and a possible workaround : bracket calls to Maxima's `simplify` with an explicit assumption of complexity for all variables not declared otherwise... This is problematic, however, since `simplify` just converts its argument to Maxima and back. Following the relevant code isn't exactly easy...\n\nHowever, the real problem is probably not in Maxima itself :\n\n```\n(%i1) display2d:false;\n\n(%o1) false\n(%i2) domain:complex;\n\n(%o2) complex\n(%i3) c:a+%i*b;\n\n(%o3) %i*b+a\n(%i4) realpart(conjugate(c));\n\n(%o4) a\n(%i5) realpart(ratsimp(conjugate(c)));\n\n(%o5) a\n```\n\n\nNotwithstanding the `domain` setting, Maxima acts as if `a` and `b` were real.\n\n\n```\n(%i6) declare(a, complex, b, complex);\n\n(%o6) done\n(%i7) realpart(conjugate(c));\n\n(%o7) 'realpart(a)-'imagpart(b)\n(%i8) realpart(ratsimp(conjugate(c)));\n\n(%o8) 'realpart(a)-'imagpart(b)\n```\n\n\nMaxima's `ratsimp` does not create the same problem as Sage`s `simplify`.\n\nHTH,",
    "created_at": "2021-03-14T22:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56621",
    "user": "@EmmanuelCharpentier"
}
```

Replying to [comment:11 nbruin]:

[ Snip... ]

> Indeed; I'd say that the problem diagnosed in the ticket is spot on. 

Indeed...

> I also don't know what the best solution is. Note that the two results are both correct if `imag_part(b)==0`, which is what maxima assumes (and we inherit those assumptions by the implementation of `simplify`).
> 
> A minimal solution would be to document (in simplify and/or in real_part, imag_part, and conjugate) that for `simplify`, symbolic variables are assumed to be real, so that `conjugate(x).simplify()==real_part(x).simplify()==x` and `imag_part(x).simplify()==0`.

At the (accepted) risk of lampooning the British Commons : No, no, no, no, no, no, no, no. 


And no...

This assumption is a way too large limitation of Sage's algebraic abilities. And can't be enforced by checks...

Finding the source of the problem is necessary. It might help to show that the problem is alleviated by //renaming// the variables :


```
sage: %cpaste
Pasting code; enter '--' alone on the line to stop or use Ctrl-D.
:var('a,b')
:c=a+I*b
:L=c.operands()
:aL=[maxima.gensym().sage() for u in L]
:D=dict(zip(L,aL))
:DI=dict(zip(aL,L))
:print(c.conjugate().real())
:print(c.conjugate().simplify().real())
:print(c.subs(D).conjugate().real().subs(DI))
:print(c.subs(D).conjugate().simplify().real().subs(DI))
:--
(a, b)
-imag_part(b) + real_part(a)
imag_part(b) + real_part(a)
-imag_part(b) + real_part(a)
-imag_part(b) + real_part(a)
```


However :

```
sage: print(c.conjugate().subs(D).simplify().real().subs(DI))
imag_part(b) + real_part(a)
```



This behaviour let us think that somehow, `simplify` doesn't account for the "complexity"of `(-I*b")`. Another hint in this direction :


```
sage: with assuming(a,b,"real"):c.conjugate().simplify().real()
a
sage: with assuming(a,b,"complex"):c.conjugate().simplify().real()
-imag_part(b) + real_part(a)
```

which is correct.


This suggests a direction for debugging the  source (which is probably in `pynac` territory, i. e. put of my reach...) and a possible workaround : bracket calls to Maxima's `simplify` with an explicit assumption of complexity for all variables not declared otherwise... This is problematic, however, since `simplify` just converts its argument to Maxima and back. Following the relevant code isn't exactly easy...

However, the real problem is probably not in Maxima itself :

```
(%i1) display2d:false;

(%o1) false
(%i2) domain:complex;

(%o2) complex
(%i3) c:a+%i*b;

(%o3) %i*b+a
(%i4) realpart(conjugate(c));

(%o4) a
(%i5) realpart(ratsimp(conjugate(c)));

(%o5) a
```


Notwithstanding the `domain` setting, Maxima acts as if `a` and `b` were real.


```
(%i6) declare(a, complex, b, complex);

(%o6) done
(%i7) realpart(conjugate(c));

(%o7) 'realpart(a)-'imagpart(b)
(%i8) realpart(ratsimp(conjugate(c)));

(%o8) 'realpart(a)-'imagpart(b)
```


Maxima's `ratsimp` does not create the same problem as Sage`s `simplify`.

HTH,



---

archive/issue_comments_056622.json:
```json
{
    "body": "Replying to [comment:12 charpent]:\n> This behaviour let us think that somehow, `simplify` doesn't account for the \"complexity\"of `(-I*b\")`. Another hint in this direction :\n> \n> {{{\n> sage: with assuming(a,b,\"real\"):c.conjugate().simplify().real()\n> a\n> sage: with assuming(a,b,\"complex\"):c.conjugate().simplify().real()\n> -imag_part(b) + real_part(a)\n> }}}\n> which is correct.\n\nNice find! That is consistent with \"maxima by default assumes variables are real-valued as far as conjugate, real_part, imag_part as concerned\", so there's a mismatch between sage/pynac and maxima what the default assumptions about variables is, and indeed the appropriate work-around is to sync up those assumptions to match (one way or the other).\n\nI'm not so sure if we should bracket each simplify call with an `assume`. I think it's the responsibility of the interface to translate `x` into a symbol in the other system with the right properties. So I think that `maxima_calculus(x)` should basically already insert the assumption on the maxima side, unless `x` is assumed to be `real`: mismatching defaults on the maxima side just mean we cannot rely on the default behaviour there and we need to enforce the desired behaviour appropriately.\n\nI'd also be fine with changing the assumption that variables are by default real unless declared otherwise. If we want to change our default assumption about variables, we may need to change pynac. Otherwise, I think it's a matter of changing the maxima interface (mainly the maxima_calculus one).",
    "created_at": "2021-03-14T22:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56622",
    "user": "@nbruin"
}
```

Replying to [comment:12 charpent]:
> This behaviour let us think that somehow, `simplify` doesn't account for the "complexity"of `(-I*b")`. Another hint in this direction :
> 
> {{{
> sage: with assuming(a,b,"real"):c.conjugate().simplify().real()
> a
> sage: with assuming(a,b,"complex"):c.conjugate().simplify().real()
> -imag_part(b) + real_part(a)
> }}}
> which is correct.

Nice find! That is consistent with "maxima by default assumes variables are real-valued as far as conjugate, real_part, imag_part as concerned", so there's a mismatch between sage/pynac and maxima what the default assumptions about variables is, and indeed the appropriate work-around is to sync up those assumptions to match (one way or the other).

I'm not so sure if we should bracket each simplify call with an `assume`. I think it's the responsibility of the interface to translate `x` into a symbol in the other system with the right properties. So I think that `maxima_calculus(x)` should basically already insert the assumption on the maxima side, unless `x` is assumed to be `real`: mismatching defaults on the maxima side just mean we cannot rely on the default behaviour there and we need to enforce the desired behaviour appropriately.

I'd also be fine with changing the assumption that variables are by default real unless declared otherwise. If we want to change our default assumption about variables, we may need to change pynac. Otherwise, I think it's a matter of changing the maxima interface (mainly the maxima_calculus one).



---

archive/issue_comments_056623.json:
```json
{
    "body": "> Nice find! That is consistent with \"maxima by default assumes variables are real-valued as far as conjugate, real_part, imag_part as concerned\", \nCorrect.  As I mention above, `domain:complex` is useful but doesn't affect much beyond `sqrt`.  And I doubt Maxima will be changing that.\n\n> I'm not so sure if we should bracket each simplify call with an `assume`. I think it's the responsibility of the interface to translate `x` into a symbol in the other system with the right properties. So I think that `maxima_calculus(x)` should basically already insert the assumption on the maxima side, unless `x` is assumed to be `real`: mismatching defaults on the maxima side just mean we cannot rely on the default behaviour there and we need to enforce the desired behaviour appropriately.\n\nYes, we should be sending the correct thing to Maxima.  The problem is that it might be hard to parse out every symbol and make sure it has all the right extra assumptions, or at least in the past that seems to have led into a rat's nest.  We do prepend `sage_var` or something like that to each Sage variable in Maxima, so at least in theory it should be possible, but one wouldn't want to overwrite previous assumptions, so a lot of testing would be involved.  It would be really nice, of course!\n\n> \n> I'd also be fine with changing the assumption that variables are by default real unless declared otherwise. If we want to change our default assumption about variables, we may need to change pynac. \n\nI think that changing all variables to real by default probably would be a bad move in many ways.  (I don't think you're suggesting that, but the way you phrased it sounds like that.)",
    "created_at": "2021-03-15T01:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56623",
    "user": "@kcrisman"
}
```

> Nice find! That is consistent with "maxima by default assumes variables are real-valued as far as conjugate, real_part, imag_part as concerned", 
Correct.  As I mention above, `domain:complex` is useful but doesn't affect much beyond `sqrt`.  And I doubt Maxima will be changing that.

> I'm not so sure if we should bracket each simplify call with an `assume`. I think it's the responsibility of the interface to translate `x` into a symbol in the other system with the right properties. So I think that `maxima_calculus(x)` should basically already insert the assumption on the maxima side, unless `x` is assumed to be `real`: mismatching defaults on the maxima side just mean we cannot rely on the default behaviour there and we need to enforce the desired behaviour appropriately.

Yes, we should be sending the correct thing to Maxima.  The problem is that it might be hard to parse out every symbol and make sure it has all the right extra assumptions, or at least in the past that seems to have led into a rat's nest.  We do prepend `sage_var` or something like that to each Sage variable in Maxima, so at least in theory it should be possible, but one wouldn't want to overwrite previous assumptions, so a lot of testing would be involved.  It would be really nice, of course!

> 
> I'd also be fine with changing the assumption that variables are by default real unless declared otherwise. If we want to change our default assumption about variables, we may need to change pynac. 

I think that changing all variables to real by default probably would be a bad move in many ways.  (I don't think you're suggesting that, but the way you phrased it sounds like that.)



---

archive/issue_comments_056624.json:
```json
{
    "body": "The `Maxima` problem has been [reported](https://sourceforge.net/p/maxima/bugs/3747/) upstream.",
    "created_at": "2021-03-15T10:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56624",
    "user": "@EmmanuelCharpentier"
}
```

The `Maxima` problem has been [reported](https://sourceforge.net/p/maxima/bugs/3747/) upstream.



---

archive/issue_comments_056625.json:
```json
{
    "body": "Changing priority from minor to critical.",
    "created_at": "2021-03-15T10:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56625",
    "user": "@EmmanuelCharpentier"
}
```

Changing priority from minor to critical.



---

archive/issue_comments_056626.json:
```json
{
    "body": "Priority set to `critical` because this bug silenty leads to mathematically incorrect results.",
    "created_at": "2021-03-15T10:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56626",
    "user": "@EmmanuelCharpentier"
}
```

Priority set to `critical` because this bug silenty leads to mathematically incorrect results.



---

archive/issue_comments_056627.json:
```json
{
    "body": "Replying to [comment:14 kcrisman]:\n\n> Yes, we should be sending the correct thing to Maxima.  The problem is that it might be hard to parse out every symbol and make sure it has all the right extra assumptions, or at least in the past that seems to have led into a rat's nest.  We do prepend `sage_var` or something like that to each Sage variable in Maxima, so at least in theory it should be possible, but one wouldn't want to overwrite previous assumptions, so a lot of testing would be involved.  It would be really nice, of course!\n\nThat should actually be dead-easy. This is not about sending strings over that need to be parsed for variables; this is about sending expressions over. They are already parsed. Especially if you do that in the way that maxima_lib works, the symbol needs to be created on the maxima side. If we assume our variables to be complex by default, then that assumption should be inserted at that time. If assumptions change, we just need to do whatever dance we do already to change them on the maxima side as well.\n\nThe main problem I expect is that inserting the assumption will probably lead to other side-effects we didn't anticipate. That's why I figured documenting the current \"simplify\" behaviour is the easier way out (but I wouldn't trust non-trivial SR computations for publication-quality work anyway).",
    "created_at": "2021-03-15T17:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56627",
    "user": "@nbruin"
}
```

Replying to [comment:14 kcrisman]:

> Yes, we should be sending the correct thing to Maxima.  The problem is that it might be hard to parse out every symbol and make sure it has all the right extra assumptions, or at least in the past that seems to have led into a rat's nest.  We do prepend `sage_var` or something like that to each Sage variable in Maxima, so at least in theory it should be possible, but one wouldn't want to overwrite previous assumptions, so a lot of testing would be involved.  It would be really nice, of course!

That should actually be dead-easy. This is not about sending strings over that need to be parsed for variables; this is about sending expressions over. They are already parsed. Especially if you do that in the way that maxima_lib works, the symbol needs to be created on the maxima side. If we assume our variables to be complex by default, then that assumption should be inserted at that time. If assumptions change, we just need to do whatever dance we do already to change them on the maxima side as well.

The main problem I expect is that inserting the assumption will probably lead to other side-effects we didn't anticipate. That's why I figured documenting the current "simplify" behaviour is the easier way out (but I wouldn't trust non-trivial SR computations for publication-quality work anyway).



---

archive/issue_comments_056628.json:
```json
{
    "body": "> That should actually be dead-easy. This is not about sending strings over that need to be parsed for variables; this is about sending expressions over. They are already parsed. Especially if you do that in the way that maxima_lib works, the symbol needs to be created on the maxima side. If we assume our variables to be complex by default, then that assumption should be inserted at that time. If assumptions change, we just need to do whatever dance we do already to change them on the maxima side as well.\n> \n\nGood.  And I certainly only care about the `maxima_lib` case.\n\n> The main problem I expect is that inserting the assumption will probably lead to other side-effects we didn't anticipate. That's why I figured documenting the current \"simplify\" behaviour is the easier way out (but I wouldn't trust non-trivial SR computations for publication-quality work anyway).\n\nTrue.  \n\n> The Maxima problem has been \u200breported upstream.\n\nI expect they will say this is user error or won't implement, since the documentation makes it pretty clear that `domain:complex` doesn't do much, and presumably (though by implication only) shouldn't be expected to do much else.",
    "created_at": "2021-03-15T17:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56628",
    "user": "@kcrisman"
}
```

> That should actually be dead-easy. This is not about sending strings over that need to be parsed for variables; this is about sending expressions over. They are already parsed. Especially if you do that in the way that maxima_lib works, the symbol needs to be created on the maxima side. If we assume our variables to be complex by default, then that assumption should be inserted at that time. If assumptions change, we just need to do whatever dance we do already to change them on the maxima side as well.
> 

Good.  And I certainly only care about the `maxima_lib` case.

> The main problem I expect is that inserting the assumption will probably lead to other side-effects we didn't anticipate. That's why I figured documenting the current "simplify" behaviour is the easier way out (but I wouldn't trust non-trivial SR computations for publication-quality work anyway).

True.  

> The Maxima problem has been ​reported upstream.

I expect they will say this is user error or won't implement, since the documentation makes it pretty clear that `domain:complex` doesn't do much, and presumably (though by implication only) shouldn't be expected to do much else.



---

archive/issue_comments_056629.json:
```json
{
    "body": "According to [Stavros Macrakis](https://sourceforge.net/p/maxima/bugs/3747/#fe49),`domain` is supposed to have an effect only for power operations (and is not expected to have an effect on `realpart`). He reclassified the issue as a documentation issue (wrongly, IMHO, but nothing can be done...).\n\nWe should therefore fox it at Sage's level...",
    "created_at": "2021-03-21T08:56:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56629",
    "user": "@EmmanuelCharpentier"
}
```

According to [Stavros Macrakis](https://sourceforge.net/p/maxima/bugs/3747/#fe49),`domain` is supposed to have an effect only for power operations (and is not expected to have an effect on `realpart`). He reclassified the issue as a documentation issue (wrongly, IMHO, but nothing can be done...).

We should therefore fox it at Sage's level...



---

archive/issue_comments_056630.json:
```json
{
    "body": "Related ticket: #30793.",
    "created_at": "2021-03-28T22:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56630",
    "user": "@DaveWitteMorris"
}
```

Related ticket: #30793.



---

archive/issue_comments_056631.json:
```json
{
    "body": "Moving to 9.4, as 9.3 has been released.",
    "created_at": "2021-05-10T17:42:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6862",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6862#issuecomment-56631",
    "user": "@mkoeppe"
}
```

Moving to 9.4, as 9.3 has been released.
