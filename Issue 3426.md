# Issue 3426: bessel_K function is broken (with patch, needs review)

archive/issues_003426.json:
```json
{
    "body": "Assignee: bober\n\nCC:  burcin kcrisman benjaminfjones\n\nKeywords: bessel, bessel_K\n\nCurrently we have\n\n```\nsage: bessel_K(10 * I, 10)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/bober/sage-3.0.2/devel/sage-bober/sage/functions/<ipython console> in <module>()\n\n/home/bober/sage/local/lib/python2.5/site-packages/sage/functions/special.py in bessel_K(nu, z, algorithm, prec)\n    586         from sage.libs.pari.all import pari\n    587         RR,a = _setup(prec)\n--> 588         b = RR(pari(nu).besselk(z))\n    589         pari.set_real_precision(a)\n    590         return b\n\n/home/bober/sage-3.0.2/devel/sage-bober/sage/functions/real_mpfr.pyx in sage.rings.real_mpfr.RealField.__call__ (sage/rings/real_mpfr.c:3138)()\n\n/home/bober/sage-3.0.2/devel/sage-bober/sage/functions/real_mpfr.pyx in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:5905)()\n\nTypeError: Unable to convert x (='0.000000098241574381992468+0.E-161*I') to real number.\nsage: bessel_K(10 * I, 10)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/bober/sage-3.0.2/devel/sage-bober/sage/functions/<ipython console> in <module>()\n\n/home/bober/sage/local/lib/python2.5/site-packages/sage/functions/special.py in bessel_K(nu, z, algorithm, prec)\n    586         from sage.libs.pari.all import pari\n    587         RR,a = _setup(prec)\n--> 588         b = RR(pari(nu).besselk(z))\n    589         pari.set_real_precision(a)\n    590         return b\n\n/home/bober/sage-3.0.2/devel/sage-bober/sage/functions/real_mpfr.pyx in sage.rings.real_mpfr.RealField.__call__ (sage/rings/real_mpfr.c:3138)()\n\n/home/bober/sage-3.0.2/devel/sage-bober/sage/functions/real_mpfr.pyx in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:5905)()\n\nTypeError: Unable to convert x (='0.000000098241574381992468+0.E-161*I') to real number.\n```\n\n\nIn this case the result actually should be a real number, so we fix this by discarding the imaginary part of the result from pari. In other cases, however, the result is actually a complex number, and we shouldn't always be attempting to cast it to a real number (which the attached patch also fixes).\n\nIssue created by migration from https://trac.sagemath.org/ticket/3426\n\n",
    "created_at": "2008-06-14T22:10:12Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "title": "bessel_K function is broken (with patch, needs review)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3426",
    "user": "bober"
}
```
Assignee: bober

CC:  burcin kcrisman benjaminfjones

Keywords: bessel, bessel_K

Currently we have

```
sage: bessel_K(10 * I, 10)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/bober/sage-3.0.2/devel/sage-bober/sage/functions/<ipython console> in <module>()

/home/bober/sage/local/lib/python2.5/site-packages/sage/functions/special.py in bessel_K(nu, z, algorithm, prec)
    586         from sage.libs.pari.all import pari
    587         RR,a = _setup(prec)
--> 588         b = RR(pari(nu).besselk(z))
    589         pari.set_real_precision(a)
    590         return b

/home/bober/sage-3.0.2/devel/sage-bober/sage/functions/real_mpfr.pyx in sage.rings.real_mpfr.RealField.__call__ (sage/rings/real_mpfr.c:3138)()

/home/bober/sage-3.0.2/devel/sage-bober/sage/functions/real_mpfr.pyx in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:5905)()

TypeError: Unable to convert x (='0.000000098241574381992468+0.E-161*I') to real number.
sage: bessel_K(10 * I, 10)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/bober/sage-3.0.2/devel/sage-bober/sage/functions/<ipython console> in <module>()

/home/bober/sage/local/lib/python2.5/site-packages/sage/functions/special.py in bessel_K(nu, z, algorithm, prec)
    586         from sage.libs.pari.all import pari
    587         RR,a = _setup(prec)
--> 588         b = RR(pari(nu).besselk(z))
    589         pari.set_real_precision(a)
    590         return b

/home/bober/sage-3.0.2/devel/sage-bober/sage/functions/real_mpfr.pyx in sage.rings.real_mpfr.RealField.__call__ (sage/rings/real_mpfr.c:3138)()

/home/bober/sage-3.0.2/devel/sage-bober/sage/functions/real_mpfr.pyx in sage.rings.real_mpfr.RealNumber._set (sage/rings/real_mpfr.c:5905)()

TypeError: Unable to convert x (='0.000000098241574381992468+0.E-161*I') to real number.
```


In this case the result actually should be a real number, so we fix this by discarding the imaginary part of the result from pari. In other cases, however, the result is actually a complex number, and we shouldn't always be attempting to cast it to a real number (which the attached patch also fixes).

Issue created by migration from https://trac.sagemath.org/ticket/3426





---

archive/issue_comments_024107.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-06-14T22:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24107",
    "user": "bober"
}
```

Attachment



---

archive/issue_comments_024108.json:
```json
{
    "body": "Changing component from misc to calculus.",
    "created_at": "2008-06-15T01:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24108",
    "user": "malb"
}
```

Changing component from misc to calculus.



---

archive/issue_comments_024109.json:
```json
{
    "body": "Changing assignee from bober to gfurnish.",
    "created_at": "2008-06-15T01:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24109",
    "user": "malb"
}
```

Changing assignee from bober to gfurnish.



---

archive/issue_comments_024110.json:
```json
{
    "body": "Changing keywords from \"bessel, bessel_K\" to \"bessel, bessel_K, editor_gfurnish\".",
    "created_at": "2008-06-15T22:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24110",
    "user": "craigcitro"
}
```

Changing keywords from "bessel, bessel_K" to "bessel, bessel_K, editor_gfurnish".



---

archive/issue_comments_024111.json:
```json
{
    "body": "Regarding bessel_K being real for real argument and real or imaginary order, see, e.g. the appendix to H. Then, Maass cusp forms for large eigenvalues, Math. Comp. Volume 74, Number 249, pp. 363 - 381: \"The K-Bessel function K_ir(x) is ... real for real arguments x and real or imaginary order ir.\"",
    "created_at": "2008-06-16T04:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24111",
    "user": "bober"
}
```

Regarding bessel_K being real for real argument and real or imaginary order, see, e.g. the appendix to H. Then, Maass cusp forms for large eigenvalues, Math. Comp. Volume 74, Number 249, pp. 363 - 381: "The K-Bessel function K_ir(x) is ... real for real arguments x and real or imaginary order ir."



---

archive/issue_comments_024112.json:
```json
{
    "body": "I can say that I agree that this is 100% correct.",
    "created_at": "2008-06-16T05:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24112",
    "user": "gregorybard"
}
```

I can say that I agree that this is 100% correct.



---

archive/issue_comments_024113.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2008-06-16T05:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24113",
    "user": "gfurnish"
}
```

Changing priority from minor to major.



---

archive/issue_comments_024114.json:
```json
{
    "body": "I think a solution of the following type would be better.\n\n\n```\n\ntry:\n        from sage.libs.pari.all import pari\n        RR,a = _setup(prec)\n        b = RR(pari(nu).besselk(z))\n        pari.set_real_precision\n\nexcept TypeError:\n        CC,a = _setup(prec)\n        b = CC(pari(nu).besselk(z))\n        pari.set_real_precision(a)\n```\n",
    "created_at": "2008-06-17T17:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24114",
    "user": "rishi"
}
```

I think a solution of the following type would be better.


```

try:
        from sage.libs.pari.all import pari
        RR,a = _setup(prec)
        b = RR(pari(nu).besselk(z))
        pari.set_real_precision

except TypeError:
        CC,a = _setup(prec)
        b = CC(pari(nu).besselk(z))
        pari.set_real_precision(a)
```




---

archive/issue_comments_024115.json:
```json
{
    "body": "Probably the  correct code would be\n {{{\n \n try:\n         from sage.libs.pari.all import pari\n         RR,a = _setup(prec)\n         b = RR(pari(nu).besselk(z))\n         pari.set_real_precision\n \n except TypeError:\n         CC,a = _setup_CC(prec)\n         b = CC(pari(nu).besselk(z))\n         pari.set_real_precision(a)\n }}}",
    "created_at": "2008-06-17T18:14:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24115",
    "user": "rishi"
}
```

Probably the  correct code would be
 {{{
 
 try:
         from sage.libs.pari.all import pari
         RR,a = _setup(prec)
         b = RR(pari(nu).besselk(z))
         pari.set_real_precision
 
 except TypeError:
         CC,a = _setup_CC(prec)
         b = CC(pari(nu).besselk(z))
         pari.set_real_precision(a)
 }}}



---

archive/issue_comments_024116.json:
```json
{
    "body": "Since Rishi commented on this it might be a good idea to discuss his comments.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-23T09:36:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24116",
    "user": "mabshoff"
}
```

Since Rishi commented on this it might be a good idea to discuss his comments.

Cheers,

Michael



---

archive/issue_comments_024117.json:
```json
{
    "body": "The try code does not in my opinion work.  The issue here is correcting numerical instabilities, which attempting to coerce into RR will not do.  Positive review still.",
    "created_at": "2008-06-23T15:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24117",
    "user": "gfurnish"
}
```

The try code does not in my opinion work.  The issue here is correcting numerical instabilities, which attempting to coerce into RR will not do.  Positive review still.



---

archive/issue_comments_024118.json:
```json
{
    "body": "I am pretty confident that the try code works. Consider the following gp output. The current patch will try to coerce this to RR. If pari is right then this input after applying the patch will give a TypeError. \n\n```\n? besselk(2,-1.121)\n%1 = 1.234141459629829380224386595 - 0.5472316582663064541169798027*I\n```\n\n\nWe probably eliminate the double evaluation of bessel function using pari which my current suggestion does.",
    "created_at": "2008-06-23T18:50:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24118",
    "user": "rishi"
}
```

I am pretty confident that the try code works. Consider the following gp output. The current patch will try to coerce this to RR. If pari is right then this input after applying the patch will give a TypeError. 

```
? besselk(2,-1.121)
%1 = 1.234141459629829380224386595 - 0.5472316582663064541169798027*I
```


We probably eliminate the double evaluation of bessel function using pari which my current suggestion does.



---

archive/issue_comments_024119.json:
```json
{
    "body": "I don't understand what double evaluation of the bessel function you are talking about.  Furthermore the entire point is that Pari can give wrong answers in some cases because of numerical cases.  Therefore we want to manually correct the numerical noise.  Trying to coerce into RR instead of clearing it completely misses the point.",
    "created_at": "2008-06-23T18:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24119",
    "user": "gfurnish"
}
```

I don't understand what double evaluation of the bessel function you are talking about.  Furthermore the entire point is that Pari can give wrong answers in some cases because of numerical cases.  Therefore we want to manually correct the numerical noise.  Trying to coerce into RR instead of clearing it completely misses the point.



---

archive/issue_comments_024120.json:
```json
{
    "body": "I refuse to believe such a large numerical instabilities. In fact maple gives the same answer as pari. I will investigate further and figure out. You cannot Willy nilly ignore the imaginary part.",
    "created_at": "2008-06-23T19:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24120",
    "user": "rishi"
}
```

I refuse to believe such a large numerical instabilities. In fact maple gives the same answer as pari. I will investigate further and figure out. You cannot Willy nilly ignore the imaginary part.



---

archive/issue_comments_024121.json:
```json
{
    "body": "And Mathematica does the same as pari. \n\nI suggested the try: except: statement because it does not require deep understanding of Bessel's K function and probably in the end we might end up with this solution.",
    "created_at": "2008-06-23T19:39:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24121",
    "user": "rishi"
}
```

And Mathematica does the same as pari. 

I suggested the try: except: statement because it does not require deep understanding of Bessel's K function and probably in the end we might end up with this solution.



---

archive/issue_comments_024122.json:
```json
{
    "body": "The try except statement does not significantly help the original complaint.  Either the identity is true or we should give the patch a negative review and close it as invalid.",
    "created_at": "2008-06-23T20:47:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24122",
    "user": "gfurnish"
}
```

The try except statement does not significantly help the original complaint.  Either the identity is true or we should give the patch a negative review and close it as invalid.



---

archive/issue_comments_024123.json:
```json
{
    "body": "\n```\nbesselk(nu,x,{flag = 0})\n\nK-Bessel function of index nu (which can be complex) and argument x. Only real and positive arguments x are allowed in the present version 2.3.3. If flag is equal to 1, uses another implementation of this function which is faster when x >> 1.\n\nThe library syntax is kbessel(nu,x,prec) and kbessel2(nu,x,prec) respectively.\n```\n\nTherefore pari gives incorrect answers for your negative x.  Perhaps this is another bug and we should merge this ticket and open another one for adding some error checking to besselk?",
    "created_at": "2008-06-23T20:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24123",
    "user": "gfurnish"
}
```


```
besselk(nu,x,{flag = 0})

K-Bessel function of index nu (which can be complex) and argument x. Only real and positive arguments x are allowed in the present version 2.3.3. If flag is equal to 1, uses another implementation of this function which is faster when x >> 1.

The library syntax is kbessel(nu,x,prec) and kbessel2(nu,x,prec) respectively.
```

Therefore pari gives incorrect answers for your negative x.  Perhaps this is another bug and we should merge this ticket and open another one for adding some error checking to besselk?



---

archive/issue_comments_024124.json:
```json
{
    "body": "The complaint is valid. In fact the current version is lot more broken that the patched version. The current version does not take any complex argument. The patched version only fails on negative real axis.",
    "created_at": "2008-06-23T21:22:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24124",
    "user": "rishi"
}
```

The complaint is valid. In fact the current version is lot more broken that the patched version. The current version does not take any complex argument. The patched version only fails on negative real axis.



---

archive/issue_comments_024125.json:
```json
{
    "body": "Ok lets patch this then and open a new ticket for the negative real axis case.",
    "created_at": "2008-06-23T21:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24125",
    "user": "gfurnish"
}
```

Ok lets patch this then and open a new ticket for the negative real axis case.



---

archive/issue_comments_024126.json:
```json
{
    "body": "I think \n\n```\nif (real(nu) == 0 or imag(nu) == 0) and (imag(z) == 0)\n```\n\n\nshould become\n\n```\nif (real(nu) == 0 or imag(nu) == 0) and (imag(z) == 0 and real(z) > 0)\n```\n",
    "created_at": "2008-06-23T22:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24126",
    "user": "rishi"
}
```

I think 

```
if (real(nu) == 0 or imag(nu) == 0) and (imag(z) == 0)
```


should become

```
if (real(nu) == 0 or imag(nu) == 0) and (imag(z) == 0 and real(z) > 0)
```




---

archive/issue_comments_024127.json:
```json
{
    "body": "Following the philosophy that wrong answers are worse than errors, this patch should not go in as is. Probably the code in Rishi's most recent comment is all that is needed for a fix, as long as we're not missing something else. I can't fix this at exactly this moment, but the fix should be trivial. Anyway, even though I posted the original patch, I have to give this a -1.",
    "created_at": "2008-06-24T17:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24127",
    "user": "bober"
}
```

Following the philosophy that wrong answers are worse than errors, this patch should not go in as is. Probably the code in Rishi's most recent comment is all that is needed for a fix, as long as we're not missing something else. I can't fix this at exactly this moment, but the fix should be trivial. Anyway, even though I posted the original patch, I have to give this a -1.



---

archive/issue_comments_024128.json:
```json
{
    "body": "rishi's code does not prevent brokenness at all (in fact it is 100% equivalent to attempting to trying to return RR(answer, prec).  The patch as is makes the answer \"more correct,\" and then we can go back and write code (that makes use of this patch) to make it 100% correct.  Alternatively, if someone wants to make a new patch that checks for real(z)>=0 in all cases and throws an error otherwise, I would give that a positive review.  However, the modification of real(z)>0 is not sufficient to ensure correctness.",
    "created_at": "2008-06-24T17:48:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24128",
    "user": "gfurnish"
}
```

rishi's code does not prevent brokenness at all (in fact it is 100% equivalent to attempting to trying to return RR(answer, prec).  The patch as is makes the answer "more correct," and then we can go back and write code (that makes use of this patch) to make it 100% correct.  Alternatively, if someone wants to make a new patch that checks for real(z)>=0 in all cases and throws an error otherwise, I would give that a positive review.  However, the modification of real(z)>0 is not sufficient to ensure correctness.



---

archive/issue_comments_024129.json:
```json
{
    "body": "This ticket has been sitting around for a while without any movement. Change the title so that the reports pick up this ticket correctly.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-01T02:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24129",
    "user": "mabshoff"
}
```

This ticket has been sitting around for a while without any movement. Change the title so that the reports pick up this ticket correctly.

Cheers,

Michael



---

archive/issue_comments_024130.json:
```json
{
    "body": "I note that Alex added himself to the CC for this.   Whatever is done for this issue absolutely must take into account the work done for #4096, so at the least I suggest that the author of this patch looks at that one and reworks this.  Anything relying on Sage/pari precision questions is likely to be useless otherwise.",
    "created_at": "2008-09-23T11:45:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24130",
    "user": "cremona"
}
```

I note that Alex added himself to the CC for this.   Whatever is done for this issue absolutely must take into account the work done for #4096, so at the least I suggest that the author of this patch looks at that one and reworks this.  Anything relying on Sage/pari precision questions is likely to be useless otherwise.



---

archive/issue_comments_024131.json:
```json
{
    "body": "I looked up the definition and properties of the Bessel functions in\nseveral references (Section 7.2 of the \"Bateman Manuscript Project\",\nfor instance).\n\nI uploaded a brand new patch that implements the behavior described\nthere, namely returning a real number if the result is theoretically\nknown to be real, and a complex number otherwise.  I added doctests\nthat document this behavior, and checked all of them against\nMathematica.  I did this for all three Bessel functions that are\nimplemented in special.py using Pari, namely J, K, and I.  I also put in a workaround for a silly Pari buglet that\ncomplains about negative integer values of nu.\n\nIn the process I uncovered a couple of unrelated issues with\nspecial.py and Bessel functions, for which I'll open separate tickets.\n\nThe patch is made against 3.1.3.alpha2.",
    "created_at": "2008-10-01T09:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24131",
    "user": "AlexGhitza"
}
```

I looked up the definition and properties of the Bessel functions in
several references (Section 7.2 of the "Bateman Manuscript Project",
for instance).

I uploaded a brand new patch that implements the behavior described
there, namely returning a real number if the result is theoretically
known to be real, and a complex number otherwise.  I added doctests
that document this behavior, and checked all of them against
Mathematica.  I did this for all three Bessel functions that are
implemented in special.py using Pari, namely J, K, and I.  I also put in a workaround for a silly Pari buglet that
complains about negative integer values of nu.

In the process I uncovered a couple of unrelated issues with
special.py and Bessel functions, for which I'll open separate tickets.

The patch is made against 3.1.3.alpha2.



---

archive/issue_comments_024132.json:
```json
{
    "body": "Uh oh:\n\n\n```\nsage: bessel_J(0,0)\n---------------------------------------------------------------------------\nPariError                                 Traceback (most recent call last)\n\n/home/drake/.sage/temp/klee/32521/_home_drake__sage_init_sage_0.py in <module>()\n----> 1 \n      2 \n      3 \n      4 \n      5 \n\n/opt/sage-3.1.3.alpha2/local/lib/python2.5/site-packages/sage/functions/special.pyc in bessel_J(nu, z, algorithm, prec)\n    570             z = C(z)\n    571             K = C\n--> 572         pari_bes = pari(nu).besselj(z, precision=prec)\n    573         if K is R:\n    574             return fudge*K(pari_bes.real())\n\n/opt/sage-3.1.3.alpha2/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:34414)()\n   7865 \n   7866 \n-> 7867 \n   7868 \n   7869 \n\nPariError:  (8)\n```\n\n\nDoing `bessel_J(0, 0)` in 3.1.2 works fine. I get similar errors with this patch for other Bessel functions, too.",
    "created_at": "2008-10-10T00:40:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24132",
    "user": "ddrake"
}
```

Uh oh:


```
sage: bessel_J(0,0)
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)

/home/drake/.sage/temp/klee/32521/_home_drake__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/opt/sage-3.1.3.alpha2/local/lib/python2.5/site-packages/sage/functions/special.pyc in bessel_J(nu, z, algorithm, prec)
    570             z = C(z)
    571             K = C
--> 572         pari_bes = pari(nu).besselj(z, precision=prec)
    573         if K is R:
    574             return fudge*K(pari_bes.real())

/opt/sage-3.1.3.alpha2/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:34414)()
   7865 
   7866 
-> 7867 
   7868 
   7869 

PariError:  (8)
```


Doing `bessel_J(0, 0)` in 3.1.2 works fine. I get similar errors with this patch for other Bessel functions, too.



---

archive/issue_comments_024133.json:
```json
{
    "body": "Thanks for catching this.  It actually comes from a bug in Pari:\n\n\n```\n? besselj(0, 0)\n%1 = 1.000000000000000000000000000\n? besselj(0.E-19, 0)\n  *** besselj: gpow: 0 to a non positive exponent.\n```\n\n\nI've reported it upstream, but I will post  a patch with a workaround while we wait.",
    "created_at": "2008-10-10T01:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24133",
    "user": "AlexGhitza"
}
```

Thanks for catching this.  It actually comes from a bug in Pari:


```
? besselj(0, 0)
%1 = 1.000000000000000000000000000
? besselj(0.E-19, 0)
  *** besselj: gpow: 0 to a non positive exponent.
```


I've reported it upstream, but I will post  a patch with a workaround while we wait.



---

archive/issue_comments_024134.json:
```json
{
    "body": "apply instead of the previous patch",
    "created_at": "2008-10-10T12:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24134",
    "user": "AlexGhitza"
}
```

apply instead of the previous patch



---

archive/issue_comments_024135.json:
```json
{
    "body": "Attachment\n\nOK, I've replaced my patch with one that fixes the issue reported by Dan.",
    "created_at": "2008-10-10T12:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24135",
    "user": "AlexGhitza"
}
```

Attachment

OK, I've replaced my patch with one that fixes the issue reported by Dan.



---

archive/issue_comments_024136.json:
```json
{
    "body": "Now `bessel_J(0,0)` works but I'm seeing other problems. I'm concentrating here on the \"K\" functions since that's what this ticket is about. This is all with the current patch applied to 3.1.4.\n\n* `bessel_K(0, -1)` doesn't work at all; it just soaks up all the CPU and doesn't return. The correct answer is about `0.421024438240708 - 3.97746326050642*I`.\n\n* `bessel_K(-1*I - 1, 0)` gives an uninformative Pari error; the function isn't defined there. Mathematica says \"ComplexInfinity\"; can we give a better error message? Even just \"function not defined at 0\" would be fine.\n\n* `bessel_K(-1, -1)` says it can't convert `-0.601907230197235-1.77549968921218*I` to a real   number, which I agree with. :)  It looks like Pari has the right answer but we're trying to convert it to a real when we shouldn't be.\n\n* `bessel_K(0, -1 - I)` says \"incorrect type\", but Mathematica and Maple evaluate it just fine.",
    "created_at": "2008-10-20T05:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24136",
    "user": "ddrake"
}
```

Now `bessel_J(0,0)` works but I'm seeing other problems. I'm concentrating here on the "K" functions since that's what this ticket is about. This is all with the current patch applied to 3.1.4.

* `bessel_K(0, -1)` doesn't work at all; it just soaks up all the CPU and doesn't return. The correct answer is about `0.421024438240708 - 3.97746326050642*I`.

* `bessel_K(-1*I - 1, 0)` gives an uninformative Pari error; the function isn't defined there. Mathematica says "ComplexInfinity"; can we give a better error message? Even just "function not defined at 0" would be fine.

* `bessel_K(-1, -1)` says it can't convert `-0.601907230197235-1.77549968921218*I` to a real   number, which I agree with. :)  It looks like Pari has the right answer but we're trying to convert it to a real when we shouldn't be.

* `bessel_K(0, -1 - I)` says "incorrect type", but Mathematica and Maple evaluate it just fine.



---

archive/issue_comments_024137.json:
```json
{
    "body": "See #4626, which at least fixes the `bessel_J` problem.",
    "created_at": "2009-01-22T18:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24137",
    "user": "rlm"
}
```

See #4626, which at least fixes the `bessel_J` problem.



---

archive/issue_comments_024138.json:
```json
{
    "body": "This ticket is a huge mess :)\n\nI now think that we should just use mpmath to evaluate Bessel functions, see\n\nhttp://mpmath.googlecode.com/svn/trunk/doc/build/functions/bessel.html\n\nFor the examples that Dan gave:\n\n\n```\nsage: from mpmath import *\nsage: mp.dps = 25; mp.pretty = True\nsage: besselk(0, -1)\n(0.4210244382407083333356274 - 3.97746326050642263725661j)\nsage: besselk(-1*I - 1, 0)\n+inf\nsage: besselk(-1, -1)\n(-0.60190723019723457473754 - 1.775499689212180946878577j)\nsage: besselk(0, -1-I)\n(-1.479697108749625193260947 + 2.588306443392007370808151j)\n```\n",
    "created_at": "2010-01-20T07:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24138",
    "user": "AlexGhitza"
}
```

This ticket is a huge mess :)

I now think that we should just use mpmath to evaluate Bessel functions, see

http://mpmath.googlecode.com/svn/trunk/doc/build/functions/bessel.html

For the examples that Dan gave:


```
sage: from mpmath import *
sage: mp.dps = 25; mp.pretty = True
sage: besselk(0, -1)
(0.4210244382407083333356274 - 3.97746326050642263725661j)
sage: besselk(-1*I - 1, 0)
+inf
sage: besselk(-1, -1)
(-0.60190723019723457473754 - 1.775499689212180946878577j)
sage: besselk(0, -1-I)
(-1.479697108749625193260947 + 2.588306443392007370808151j)
```




---

archive/issue_comments_024139.json:
```json
{
    "body": "Changing keywords from \"bessel, bessel_K, editor_gfurnish\" to \"bessel, bessel_K\".",
    "created_at": "2010-01-20T07:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24139",
    "user": "AlexGhitza"
}
```

Changing keywords from "bessel, bessel_K, editor_gfurnish" to "bessel, bessel_K".



---

archive/issue_comments_024140.json:
```json
{
    "body": "From my quick experiments with the issues Bober was dealing with a year ago, I see that do not arise if we use mpmath, even when I set the precision to 5000.\n\nI agree with Alex Ghitza.\n\n\nI should say that the bessels functions for non integer indices have always bothered me. I believe computing will involve a log, and how do you consistently choose a branch.",
    "created_at": "2010-01-20T21:04:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24140",
    "user": "rishi"
}
```

From my quick experiments with the issues Bober was dealing with a year ago, I see that do not arise if we use mpmath, even when I set the precision to 5000.

I agree with Alex Ghitza.


I should say that the bessels functions for non integer indices have always bothered me. I believe computing will involve a log, and how do you consistently choose a branch.



---

archive/issue_comments_024141.json:
```json
{
    "body": "I also agree with Alex -- both in that this ticket is a mess, and that we should just use mpmath. I'll see if I can work up a patch (although anyone else who wants to should feel free to do it).",
    "created_at": "2010-01-21T00:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24141",
    "user": "ddrake"
}
```

I also agree with Alex -- both in that this ticket is a mess, and that we should just use mpmath. I'll see if I can work up a patch (although anyone else who wants to should feel free to do it).



---

archive/issue_comments_024142.json:
```json
{
    "body": "With some experiments, I saw that the branch of the log taken is the negative real axis. We should mention this in the documentation when it is implemented. I believe ddrake is working up a patch.",
    "created_at": "2010-01-22T18:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24142",
    "user": "rishi"
}
```

With some experiments, I saw that the branch of the log taken is the negative real axis. We should mention this in the documentation when it is implemented. I believe ddrake is working up a patch.



---

archive/issue_comments_024143.json:
```json
{
    "body": "Here are some more problems with bessel_K: http://groups.google.com/group/sage-support/browse_thread/thread/84e5cd4fb1381ad5\n\nIn resolving this ticket, we should make sure to have doctests related to those problems!",
    "created_at": "2010-02-18T09:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24143",
    "user": "ddrake"
}
```

Here are some more problems with bessel_K: http://groups.google.com/group/sage-support/browse_thread/thread/84e5cd4fb1381ad5

In resolving this ticket, we should make sure to have doctests related to those problems!



---

archive/issue_comments_024144.json:
```json
{
    "body": "This would most likely be fixed by #4102.",
    "created_at": "2013-01-03T15:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24144",
    "user": "kcrisman"
}
```

This would most likely be fixed by #4102.



---

archive/issue_comments_024145.json:
```json
{
    "body": "Yes, it will be fixed by #4102. I'll make a note to add a related doctest to that effect.",
    "created_at": "2013-01-03T23:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24145",
    "user": "benjaminfjones"
}
```

Yes, it will be fixed by #4102. I'll make a note to add a related doctest to that effect.



---

archive/issue_comments_024146.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-02-08T17:34:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24146",
    "user": "kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_024147.json:
```json
{
    "body": "Everything here is now in a doctest in #4102, including the stuff in the thread from three (!) years ago.",
    "created_at": "2013-02-08T17:34:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24147",
    "user": "kcrisman"
}
```

Everything here is now in a doctest in #4102, including the stuff in the thread from three (!) years ago.



---

archive/issue_comments_024148.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-02-17T20:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3426",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3426#issuecomment-24148",
    "user": "jdemeyer"
}
```

Resolution: duplicate
