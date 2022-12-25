# Issue 4132: complex arithmetic passes via pari

archive/issues_004132.json:
```json
{
    "body": "Assignee: somebody\n\nPassing through pari for every simple operation is probably unnecessary and slow...\n\nIssue created by migration from https://trac.sagemath.org/ticket/4132\n\n",
    "created_at": "2008-09-16T04:58:32Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "complex arithmetic passes via pari",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4132",
    "user": "https://github.com/robertwb"
}
```
Assignee: somebody

Passing through pari for every simple operation is probably unnecessary and slow...

Issue created by migration from https://trac.sagemath.org/ticket/4132





---

archive/issue_comments_029902.json:
```json
{
    "body": "Clarification: By \"every simple operation\" robertwb does not mean \"arithmetic operations\", which don't use PARI at all.  He means special functions like, exp, sin, Riemann zeta, etc. \n\nRobert, what do you propose to use instead of pari for these?  In some cases you can implement things building on what is in mpfr...",
    "created_at": "2008-09-16T17:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29902",
    "user": "https://github.com/williamstein"
}
```

Clarification: By "every simple operation" robertwb does not mean "arithmetic operations", which don't use PARI at all.  He means special functions like, exp, sin, Riemann zeta, etc. 

Robert, what do you propose to use instead of pari for these?  In some cases you can implement things building on what is in mpfr...



---

archive/issue_comments_029903.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-09-16T17:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29903",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_029904.json:
```json
{
    "body": "Yes, thanks for the clarification. I meant for many of them one could implement them directly against mpfr. For example:\n\n\n```\n\ninclude \"sage/rings/mpfr.pxi\"\nfrom sage.rings.complex_number cimport ComplexNumber\n\ndef my_exp(ComplexNumber self):\n    cdef ComplexNumber z = self._new()\n    cdef mpfr_t r\n    mpfr_init2(r, self._prec)\n    mpfr_exp(r, self.__re, GMP_RNDN)\n    mpfr_cos(z.__re, self.__im, GMP_RNDN)\n    mpfr_mul(z.__re, z.__re, r, GMP_RNDN)\n    mpfr_sin(z.__im, self.__im, GMP_RNDN)\n    mpfr_mul(z.__im, z.__im, r, GMP_RNDN)\n    mpfr_clear(r)\n    return z\n```\n\n\nThen\n\n\n```\nsage: a = CC.pi() + CC.0/3\nsage: my_exp(a) == a.exp()\nTrue\nsage: timeit(\"a.exp()\")\n625 loops, best of 3: 514 \u00b5s per loop\nsage: timeit(\"my_exp(a)\")\n625 loops, best of 3: 16.1 \u00b5s per loop\nsage: 514/16.1\n31.9254658385093\n```\n\n\nThis could be low-hanging fruit for a new developer.",
    "created_at": "2008-09-16T18:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29904",
    "user": "https://github.com/robertwb"
}
```

Yes, thanks for the clarification. I meant for many of them one could implement them directly against mpfr. For example:


```

include "sage/rings/mpfr.pxi"
from sage.rings.complex_number cimport ComplexNumber

def my_exp(ComplexNumber self):
    cdef ComplexNumber z = self._new()
    cdef mpfr_t r
    mpfr_init2(r, self._prec)
    mpfr_exp(r, self.__re, GMP_RNDN)
    mpfr_cos(z.__re, self.__im, GMP_RNDN)
    mpfr_mul(z.__re, z.__re, r, GMP_RNDN)
    mpfr_sin(z.__im, self.__im, GMP_RNDN)
    mpfr_mul(z.__im, z.__im, r, GMP_RNDN)
    mpfr_clear(r)
    return z
```


Then


```
sage: a = CC.pi() + CC.0/3
sage: my_exp(a) == a.exp()
True
sage: timeit("a.exp()")
625 loops, best of 3: 514 µs per loop
sage: timeit("my_exp(a)")
625 loops, best of 3: 16.1 µs per loop
sage: 514/16.1
31.9254658385093
```


This could be low-hanging fruit for a new developer.



---

archive/issue_comments_029905.json:
```json
{
    "body": "Changing assignee from somebody to @aghitza.",
    "created_at": "2008-09-25T22:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29905",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from somebody to @aghitza.



---

archive/issue_comments_029906.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-25T22:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29906",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_029907.json:
```json
{
    "body": "The attached patch does the following:\n\n* based on Robert's example, gets rid of Pari calls in cos, cosh, sin, sinh, tan, tanh, exp, sqrt, nth_root, !__pow!__\n* adds csc() and sec()\n* adds a !__nonzero!__() method to speed up is_zero()\n* fixes doctests that were affected by these changes\n\nThe patch is currently based on 3.1.3.alpha1, and I'm putting it out as such so that it can be reviewed.  I am aware of some interaction with patches that were merged in alpha2, so I will rebase it once alpha2 is out.",
    "created_at": "2008-09-28T09:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29907",
    "user": "https://github.com/aghitza"
}
```

The attached patch does the following:

* based on Robert's example, gets rid of Pari calls in cos, cosh, sin, sinh, tan, tanh, exp, sqrt, nth_root, !__pow!__
* adds csc() and sec()
* adds a !__nonzero!__() method to speed up is_zero()
* fixes doctests that were affected by these changes

The patch is currently based on 3.1.3.alpha1, and I'm putting it out as such so that it can be reviewed.  I am aware of some interaction with patches that were merged in alpha2, so I will rebase it once alpha2 is out.



---

archive/issue_comments_029908.json:
```json
{
    "body": "Thanks. For the most part it looks good. Here's some suggestions though: \n\n   * Sqrt(x) for negative x should be pure imaginary, even if a special case is needed. \n   * Calling `a.__invert__()` manually is a Python call, use `~a` instead. \n   * There seems to be a regression of accuracy in some of these examples. And some give totally different answers! Ideally, none of the doctests should have to change--and if any of them do there should be an explanation as to why the new answer is the correct one (if there are ones your not sure on, feel free to ask). \n   * some benchmarking would be good, especially for some of the more complicated ones like tan, or even sqrt. You *should* be faster, but it's best to be safe.",
    "created_at": "2008-09-28T10:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29908",
    "user": "https://github.com/robertwb"
}
```

Thanks. For the most part it looks good. Here's some suggestions though: 

   * Sqrt(x) for negative x should be pure imaginary, even if a special case is needed. 
   * Calling `a.__invert__()` manually is a Python call, use `~a` instead. 
   * There seems to be a regression of accuracy in some of these examples. And some give totally different answers! Ideally, none of the doctests should have to change--and if any of them do there should be an explanation as to why the new answer is the correct one (if there are ones your not sure on, feel free to ask). 
   * some benchmarking would be good, especially for some of the more complicated ones like tan, or even sqrt. You *should* be faster, but it's best to be safe.



---

archive/issue_comments_029909.json:
```json
{
    "body": "Attachment [trac4132-speedup-complex-functions.patch](tarball://root/attachments/some-uuid/ticket4132/trac4132-speedup-complex-functions.patch) by @aghitza created at 2008-09-29 02:26:18\n\nI have replaced the old patch with one that addresses the first two points made above.  I had actually done benchmarks while writing the code, and they're now listed further down in this comment.\n\nAs for the point on accuracy: I guess the issue is elliptic_logarithm, which was somewhat broken before this patch and is still broken now (see #4214); this has nothing to do with this ticket, though.\n\nTimings after/before the patch (z was chosen randomly):\n\n\n```\nsage: z = CC(0.588296734970724 - 0.918562568630843*I)\nsage: z\n0.588296734970724 - 0.918562568630843*I\nsage: timeit(\"z.is_zero()\")                          \n625 loops, best of 3: 901 ns per loop    # was 11.7 \u00b5s\nsage: timeit(\"z^(2/3)\")\n625 loops, best of 3: 80 \u00b5s per loop     # was 110 \u00b5s\nsage: timeit(\"z.csch()\")\n625 loops, best of 3: 18.2 \u00b5s per loop   # was 70.4 \u00b5s\nsage: timeit(\"z.sech()\")\n625 loops, best of 3: 18.3 \u00b5s per loop   # was 70.2 \u00b5s\nsage: timeit(\"z.cotan()\")\n625 loops, best of 3: 24.6 \u00b5s per loop   # was 52.5 \u00b5s\nsage: timeit(\"z.cos()\")  \n625 loops, best of 3: 21.9 \u00b5s per loop   # was 50.2 \u00b5s\nsage: timeit(\"z.cosh()\")\n625 loops, best of 3: 16.9 \u00b5s per loop   # was 50.9 \u00b5s\nsage: timeit(\"z.sin()\") \n625 loops, best of 3: 22.1 \u00b5s per loop   # was 50.2 \u00b5s\nsage: timeit(\"z.sinh()\")\n625 loops, best of 3: 17.2 \u00b5s per loop   # was 51.3 \u00b5s\nsage: timeit(\"z.tan()\") \n625 loops, best of 3: 22.9 \u00b5s per loop   # was 52.8 \u00b5s\nsage: timeit(\"z.tanh()\")\n625 loops, best of 3: 17.8 \u00b5s per loop   # was 51.8 \u00b5s\nsage: timeit(\"z.argument()\")\n625 loops, best of 3: 26.4 \u00b5s per loop   # was 36.3 \u00b5s\nsage: timeit(\"z.exp()\")     \n625 loops, best of 3: 10.8 \u00b5s per loop   # was 49.2 \u00b5s\nsage: timeit(\"z.sqrt()\")\n625 loops, best of 3: 34.4 \u00b5s per loop   # was 44.1 \u00b5s\nsage: timeit(\"z.nth_root(20)\")\n625 loops, best of 3: 56 \u00b5s per loop     # was 94.1 \u00b5s\nsage: timeit(\"z.nth_root(20, all=True)\")             \n625 loops, best of 3: 232 \u00b5s per loop    # was 537 \u00b5s\n```\n",
    "created_at": "2008-09-29T02:26:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29909",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac4132-speedup-complex-functions.patch](tarball://root/attachments/some-uuid/ticket4132/trac4132-speedup-complex-functions.patch) by @aghitza created at 2008-09-29 02:26:18

I have replaced the old patch with one that addresses the first two points made above.  I had actually done benchmarks while writing the code, and they're now listed further down in this comment.

As for the point on accuracy: I guess the issue is elliptic_logarithm, which was somewhat broken before this patch and is still broken now (see #4214); this has nothing to do with this ticket, though.

Timings after/before the patch (z was chosen randomly):


```
sage: z = CC(0.588296734970724 - 0.918562568630843*I)
sage: z
0.588296734970724 - 0.918562568630843*I
sage: timeit("z.is_zero()")                          
625 loops, best of 3: 901 ns per loop    # was 11.7 µs
sage: timeit("z^(2/3)")
625 loops, best of 3: 80 µs per loop     # was 110 µs
sage: timeit("z.csch()")
625 loops, best of 3: 18.2 µs per loop   # was 70.4 µs
sage: timeit("z.sech()")
625 loops, best of 3: 18.3 µs per loop   # was 70.2 µs
sage: timeit("z.cotan()")
625 loops, best of 3: 24.6 µs per loop   # was 52.5 µs
sage: timeit("z.cos()")  
625 loops, best of 3: 21.9 µs per loop   # was 50.2 µs
sage: timeit("z.cosh()")
625 loops, best of 3: 16.9 µs per loop   # was 50.9 µs
sage: timeit("z.sin()") 
625 loops, best of 3: 22.1 µs per loop   # was 50.2 µs
sage: timeit("z.sinh()")
625 loops, best of 3: 17.2 µs per loop   # was 51.3 µs
sage: timeit("z.tan()") 
625 loops, best of 3: 22.9 µs per loop   # was 52.8 µs
sage: timeit("z.tanh()")
625 loops, best of 3: 17.8 µs per loop   # was 51.8 µs
sage: timeit("z.argument()")
625 loops, best of 3: 26.4 µs per loop   # was 36.3 µs
sage: timeit("z.exp()")     
625 loops, best of 3: 10.8 µs per loop   # was 49.2 µs
sage: timeit("z.sqrt()")
625 loops, best of 3: 34.4 µs per loop   # was 44.1 µs
sage: timeit("z.nth_root(20)")
625 loops, best of 3: 56 µs per loop     # was 94.1 µs
sage: timeit("z.nth_root(20, all=True)")             
625 loops, best of 3: 232 µs per loop    # was 537 µs
```




---

archive/issue_comments_029910.json:
```json
{
    "body": "Nice work. You've probably noticed by now that the trig operations are expensive, so you could possibly shave 25% of some of the calls where you compute both sinh and cosh by using the identity\n\n    cosh(x) = sqrt(1+sinh(x)).\n\nOn the note of expensive trig, might I suggest a faster sqrt \n\n\n```\ndef new_sqrt(ComplexNumber self, all=False):\n    cdef ComplexNumber z = self._new()\n    if mpfr_zero_p(self.__im):\n        if mpfr_sgn(self.__re) >= 0:\n            mpfr_set_ui(z.__im, 0, rnd)\n            mpfr_sqrt(z.__re, self.__re, rnd)\n        else:\n            mpfr_set_ui(z.__re, 0, rnd)\n            mpfr_neg(z.__im, self.__re, rnd)\n            mpfr_sqrt(z.__im, z.__im, rnd)\n        if all:\n            return [z, -z] if z else [z]\n        else:\n            return z\n    # z = x + yi = (a+bi)^2\n    # expand, substitute, solve (note that a is nonzero)\n    # a^2 = (x + sqrt(x^2+y^2))/2\n    cdef mpfr_t a2\n    mpfr_init2(a2, self._prec)\n    mpfr_hypot(a2, self.__re, self.__im, rnd)\n    mpfr_add(a2, a2, self.__re, rnd)\n    mpfr_mul_2si(a2, a2, -1, rnd)\n    # a = sqrt(a2)\n    mpfr_sqrt(z.__re, a2, rnd)\n    # b = y/(2a)\n    mpfr_div(z.__im, self.__im, z.__re, rnd)\n    mpfr_mul_2si(z.__im, z.__im, -1, rnd)\n    mpfr_clear(a2)\n    if all:\n        return [z, -z]\n    else:\n        return z\n```\n\n\nwhich should run in 3 or 4 \u00b5s with 53 bits, and an even more significant improvement further out. \n\nThis patch is very good, exactly what I wanted when I wrote the ticket, so thanks. The only thing that *needs* to change for a positive review is I noticed in several case you write `long(n)` when you want an unsigned long. What this does is create a python int, call the python type \"long\" on it to get a python long, then extract that as a c long. In summary, just write `n` to get a C [unsigned] long just as you would in C. (This is a common confusion with Cython, as the C long and python long are totally different things.)",
    "created_at": "2008-09-29T18:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29910",
    "user": "https://github.com/robertwb"
}
```

Nice work. You've probably noticed by now that the trig operations are expensive, so you could possibly shave 25% of some of the calls where you compute both sinh and cosh by using the identity

    cosh(x) = sqrt(1+sinh(x)).

On the note of expensive trig, might I suggest a faster sqrt 


```
def new_sqrt(ComplexNumber self, all=False):
    cdef ComplexNumber z = self._new()
    if mpfr_zero_p(self.__im):
        if mpfr_sgn(self.__re) >= 0:
            mpfr_set_ui(z.__im, 0, rnd)
            mpfr_sqrt(z.__re, self.__re, rnd)
        else:
            mpfr_set_ui(z.__re, 0, rnd)
            mpfr_neg(z.__im, self.__re, rnd)
            mpfr_sqrt(z.__im, z.__im, rnd)
        if all:
            return [z, -z] if z else [z]
        else:
            return z
    # z = x + yi = (a+bi)^2
    # expand, substitute, solve (note that a is nonzero)
    # a^2 = (x + sqrt(x^2+y^2))/2
    cdef mpfr_t a2
    mpfr_init2(a2, self._prec)
    mpfr_hypot(a2, self.__re, self.__im, rnd)
    mpfr_add(a2, a2, self.__re, rnd)
    mpfr_mul_2si(a2, a2, -1, rnd)
    # a = sqrt(a2)
    mpfr_sqrt(z.__re, a2, rnd)
    # b = y/(2a)
    mpfr_div(z.__im, self.__im, z.__re, rnd)
    mpfr_mul_2si(z.__im, z.__im, -1, rnd)
    mpfr_clear(a2)
    if all:
        return [z, -z]
    else:
        return z
```


which should run in 3 or 4 µs with 53 bits, and an even more significant improvement further out. 

This patch is very good, exactly what I wanted when I wrote the ticket, so thanks. The only thing that *needs* to change for a positive review is I noticed in several case you write `long(n)` when you want an unsigned long. What this does is create a python int, call the python type "long" on it to get a python long, then extract that as a c long. In summary, just write `n` to get a C [unsigned] long just as you would in C. (This is a common confusion with Cython, as the C long and python long are totally different things.)



---

archive/issue_comments_029911.json:
```json
{
    "body": "On the sinh/cosh comment, I should note that this is what mpfr_sin_cos does, though in that case more care needs to be taken to make sure enough precision is obtained.",
    "created_at": "2008-09-29T18:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29911",
    "user": "https://github.com/robertwb"
}
```

On the sinh/cosh comment, I should note that this is what mpfr_sin_cos does, though in that case more care needs to be taken to make sure enough precision is obtained.



---

archive/issue_comments_029912.json:
```json
{
    "body": "I keep replying to myself, but I realized while I was sitting in class today that my sqrt function has numerical instability near the branch cut. I've got a fix, perhaps I should post it as a new patch on top of the one you posted.",
    "created_at": "2008-09-30T00:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29912",
    "user": "https://github.com/robertwb"
}
```

I keep replying to myself, but I realized while I was sitting in class today that my sqrt function has numerical instability near the branch cut. I've got a fix, perhaps I should post it as a new patch on top of the one you posted.



---

archive/issue_comments_029913.json:
```json
{
    "body": "apply after the first patch",
    "created_at": "2008-09-30T04:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29913",
    "user": "https://github.com/aghitza"
}
```

apply after the first patch



---

archive/issue_comments_029914.json:
```json
{
    "body": "Attachment [trac4132-speedup-complex-functions-more.patch](tarball://root/attachments/some-uuid/ticket4132/trac4132-speedup-complex-functions-more.patch) by @aghitza created at 2008-09-30 04:19:02\n\nHi Robert,\n\nThanks for looking at this so carefully!  I have uploaded an additional patch that gets rid of the long's and avoids computing cosh's as you suggested.  This does indeed speed things by about 1/4.  Having seen your other comment, can I leave it to you to make sqrt fast?  I tried the code you posted above and it is really fast, but I didn't look into stability questions.\n\nOn a related note, I emailed Paul Zimmermann to ask if MPFR could get a function mpfr_sinh_cosh() sometime in the future.  Then I stumbled upon his library MPC (see http://www.multiprecision.org/mpc/ ).  Should we start thinking about using this as the backbone for arbitrary precision complex numbers, the same way we use MPFR for real numbers?",
    "created_at": "2008-09-30T04:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29914",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac4132-speedup-complex-functions-more.patch](tarball://root/attachments/some-uuid/ticket4132/trac4132-speedup-complex-functions-more.patch) by @aghitza created at 2008-09-30 04:19:02

Hi Robert,

Thanks for looking at this so carefully!  I have uploaded an additional patch that gets rid of the long's and avoids computing cosh's as you suggested.  This does indeed speed things by about 1/4.  Having seen your other comment, can I leave it to you to make sqrt fast?  I tried the code you posted above and it is really fast, but I didn't look into stability questions.

On a related note, I emailed Paul Zimmermann to ask if MPFR could get a function mpfr_sinh_cosh() sometime in the future.  Then I stumbled upon his library MPC (see http://www.multiprecision.org/mpc/ ).  Should we start thinking about using this as the backbone for arbitrary precision complex numbers, the same way we use MPFR for real numbers?



---

archive/issue_comments_029915.json:
```json
{
    "body": "I would suggest we move sqrt to another ticket and merge the code (assuming the changes Alex made are satisfactory to Robert) in 3.1.3.alphaX now. No point in letting this patch potentially bitrot :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-30T12:02:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29915",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I would suggest we move sqrt to another ticket and merge the code (assuming the changes Alex made are satisfactory to Robert) in 3.1.3.alphaX now. No point in letting this patch potentially bitrot :)

Cheers,

Michael



---

archive/issue_comments_029916.json:
```json
{
    "body": "Yes, for sure lests get this in. \n\nFollow-up sqrt ticket at #4225. As for MPC, I'd never heard of it. Certainly something to keep our eyes on.",
    "created_at": "2008-09-30T20:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29916",
    "user": "https://github.com/robertwb"
}
```

Yes, for sure lests get this in. 

Follow-up sqrt ticket at #4225. As for MPC, I'd never heard of it. Certainly something to keep our eyes on.



---

archive/issue_comments_029917.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-30T23:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29917",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha2



---

archive/issue_comments_029918.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-30T23:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4132",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4132#issuecomment-29918",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
