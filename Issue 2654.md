# Issue 2654: Cyclotomic polynomials -- suggested improvement

archive/issues_002654.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  rlb\n\nKeywords: cyclotomic polynomial\n\nThe current implementation of cyclotomic polynomials in sage/rings/polynomial/cyclotomic.pyx uses the Mobius inversion formula.\n\nI think it would be more efficient to use the recursion\n\n```\n\\Phi_{p*n}(X) = \\Phi_n(X^p) # if p|n\n              = \\Phi_n(X^p)/\\Phi_n(X) # else\n```\n\n(though probably not implemented recursively).  This would be simpler than what is currently done, and it would be worth implementing this to see if was really faster.\n\nSecondly, it would be easy to implement a function is_cyclotomic() using the algorithm of Smyth and Beukers.  This could just return True/False, or even n if the input is the n'th cyclotomic poly.  One application would be to improve the function multiplicative_order() for elements of number fields (and more general algebras), by checking if the minimal poly is cyclotomic.  There are a couple of TODOs in sage.rings.number_field.number_field_element which this would address (the algorithm there describes itself as \"very dumb\" and it is hard to disagree!).\n\nIssue created by migration from https://trac.sagemath.org/ticket/2654\n\n",
    "created_at": "2008-03-23T12:24:24Z",
    "labels": [
        "commutative algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Cyclotomic polynomials -- suggested improvement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2654",
    "user": "@JohnCremona"
}
```
Assignee: @malb

CC:  rlb

Keywords: cyclotomic polynomial

The current implementation of cyclotomic polynomials in sage/rings/polynomial/cyclotomic.pyx uses the Mobius inversion formula.

I think it would be more efficient to use the recursion

```
\Phi_{p*n}(X) = \Phi_n(X^p) # if p|n
              = \Phi_n(X^p)/\Phi_n(X) # else
```

(though probably not implemented recursively).  This would be simpler than what is currently done, and it would be worth implementing this to see if was really faster.

Secondly, it would be easy to implement a function is_cyclotomic() using the algorithm of Smyth and Beukers.  This could just return True/False, or even n if the input is the n'th cyclotomic poly.  One application would be to improve the function multiplicative_order() for elements of number fields (and more general algebras), by checking if the minimal poly is cyclotomic.  There are a couple of TODOs in sage.rings.number_field.number_field_element which this would address (the algorithm there describes itself as "very dumb" and it is hard to disagree!).

Issue created by migration from https://trac.sagemath.org/ticket/2654





---

archive/issue_comments_018241.json:
```json
{
    "body": "I think this proves it.  Here's my new implementation as a Sage function:\n\n```\ndef newcyc(n):\n    assert n>0\n    plist = n.prime_divisors()\n    X = PolynomialRing(ZZ,'X').gen()\n    f = X-1\n    m = n\n    for p in plist:\n    \tf = f(X**p)//f(X)\n\tm //= p\n    return f.subs(X**m)\n```\n\n\nNow newcyc(factorial(10)) takes 15s compared with cyclotomic_polynomial(factorial(10)) whihc takes 108s.  When you take into account the fact that the old function is written in cython while the new one is in sage, I think I have proved my point!  Moreover the code for the new function is very much simpler.",
    "created_at": "2008-03-23T12:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18241",
    "user": "@JohnCremona"
}
```

I think this proves it.  Here's my new implementation as a Sage function:

```
def newcyc(n):
    assert n>0
    plist = n.prime_divisors()
    X = PolynomialRing(ZZ,'X').gen()
    f = X-1
    m = n
    for p in plist:
    	f = f(X**p)//f(X)
	m //= p
    return f.subs(X**m)
```


Now newcyc(factorial(10)) takes 15s compared with cyclotomic_polynomial(factorial(10)) whihc takes 108s.  When you take into account the fact that the old function is written in cython while the new one is in sage, I think I have proved my point!  Moreover the code for the new function is very much simpler.



---

archive/issue_comments_018242.json:
```json
{
    "body": "This is due to some (very!) poor conversion code, not due to the algorithm itself. \n\n\n```\nsage: import sage.rings.polynomial.cyclotomic as c\nsage: n = factorial(10)\nsage: time f = newcyc(n)\nCPU time: 12.40 s,  Wall time: 12.53 s\nsage: time L = c.cyclotomic_coeffs(n)\nCPU time: 0.12 s,  Wall time: 0.13 s\n```\n",
    "created_at": "2008-03-31T20:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18242",
    "user": "@robertwb"
}
```

This is due to some (very!) poor conversion code, not due to the algorithm itself. 


```
sage: import sage.rings.polynomial.cyclotomic as c
sage: n = factorial(10)
sage: time f = newcyc(n)
CPU time: 12.40 s,  Wall time: 12.53 s
sage: time L = c.cyclotomic_coeffs(n)
CPU time: 0.12 s,  Wall time: 0.13 s
```




---

archive/issue_comments_018243.json:
```json
{
    "body": "In that case I'll leave this alone and wait for you to provide a suitable patch!",
    "created_at": "2008-03-31T21:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18243",
    "user": "@JohnCremona"
}
```

In that case I'll leave this alone and wait for you to provide a suitable patch!



---

archive/issue_comments_018244.json:
```json
{
    "body": "Attachment [2654-cyclo.patch](tarball://root/attachments/some-uuid/ticket2654/2654-cyclo.patch) by @robertwb created at 2008-04-01 00:13:21",
    "created_at": "2008-04-01T00:13:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18244",
    "user": "@robertwb"
}
```

Attachment [2654-cyclo.patch](tarball://root/attachments/some-uuid/ticket2654/2654-cyclo.patch) by @robertwb created at 2008-04-01 00:13:21



---

archive/issue_comments_018245.json:
```json
{
    "body": "With timings like that, I couldn't resist\n\n\n```\nsage: time f = cyclotomic_polynomial(factorial(10))\nCPU times: user 0.09 s, sys: 0.03 s, total: 0.12 s\nWall time: 0.13\nsage: time f = cyclotomic_polynomial(10^5)\nCPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s\nWall time: 0.01\nsage: time f = cyclotomic_polynomial(10^6)\nCPU times: user 0.01 s, sys: 0.01 s, total: 0.02 s\nWall time: 0.02\nsage: time f = cyclotomic_polynomial(10^7)\nCPU times: user 0.14 s, sys: 0.07 s, total: 0.22 s\nWall time: 0.23\n```\n\n\nImplementing an `is_cyclotomic` function is also a good idea, but probably a separate ticket.",
    "created_at": "2008-04-01T00:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18245",
    "user": "@robertwb"
}
```

With timings like that, I couldn't resist


```
sage: time f = cyclotomic_polynomial(factorial(10))
CPU times: user 0.09 s, sys: 0.03 s, total: 0.12 s
Wall time: 0.13
sage: time f = cyclotomic_polynomial(10^5)
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01
sage: time f = cyclotomic_polynomial(10^6)
CPU times: user 0.01 s, sys: 0.01 s, total: 0.02 s
Wall time: 0.02
sage: time f = cyclotomic_polynomial(10^7)
CPU times: user 0.14 s, sys: 0.07 s, total: 0.22 s
Wall time: 0.23
```


Implementing an `is_cyclotomic` function is also a good idea, but probably a separate ticket.



---

archive/issue_comments_018246.json:
```json
{
    "body": "REFEREE REPORT:\n\nIt builds fine.  It works fine, but gives the wrong (?) answer for n=1. \n\n\n```\nsage: cyclotomic_polynomial(1)\n-x + 1\nsage: gp('polcyclo(1)')\nx - 1\nsage: magma('CyclotomicPolynomial(1)')\n$.1 - 1\n```\n\n\nI also got it to Segfault.  Heh heh:\n\n\n```\nsage: time f = cyclotomic_polynomial(2^30)\nsage.bin(3624) malloc: *** error for object 0x6b089e0: incorrect checksum for freed object - object was probably modified after being freed.\n*** set a breakpoint in malloc_error_break to debug\nsage.bin(3624) malloc: *** error for object 0x6b0cb90: incorrect checksum for freed object - object was probably modified after being freed.\n*** set a breakpoint in malloc_error_break to debug\n\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\n```\n\n\nFix the above 2, and it's a positive review.",
    "created_at": "2008-04-01T04:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18246",
    "user": "@williamstein"
}
```

REFEREE REPORT:

It builds fine.  It works fine, but gives the wrong (?) answer for n=1. 


```
sage: cyclotomic_polynomial(1)
-x + 1
sage: gp('polcyclo(1)')
x - 1
sage: magma('CyclotomicPolynomial(1)')
$.1 - 1
```


I also got it to Segfault.  Heh heh:


```
sage: time f = cyclotomic_polynomial(2^30)
sage.bin(3624) malloc: *** error for object 0x6b089e0: incorrect checksum for freed object - object was probably modified after being freed.
*** set a breakpoint in malloc_error_break to debug
sage.bin(3624) malloc: *** error for object 0x6b0cb90: incorrect checksum for freed object - object was probably modified after being freed.
*** set a breakpoint in malloc_error_break to debug


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------

```


Fix the above 2, and it's a positive review.



---

archive/issue_comments_018247.json:
```json
{
    "body": "Attachment [2654-cyclo-fixes.patch](tarball://root/attachments/some-uuid/ticket2654/2654-cyclo-fixes.patch) by @robertwb created at 2008-04-01 05:14:23\n\nFixes area attached.",
    "created_at": "2008-04-01T05:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18247",
    "user": "@robertwb"
}
```

Attachment [2654-cyclo-fixes.patch](tarball://root/attachments/some-uuid/ticket2654/2654-cyclo-fixes.patch) by @robertwb created at 2008-04-01 05:14:23

Fixes area attached.



---

archive/issue_comments_018248.json:
```json
{
    "body": "I really have no horses in this race.",
    "created_at": "2008-04-01T12:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18248",
    "user": "@malb"
}
```

I really have no horses in this race.



---

archive/issue_comments_018249.json:
```json
{
    "body": "Changing assignee from @malb to @robertwb.",
    "created_at": "2008-04-01T12:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18249",
    "user": "@malb"
}
```

Changing assignee from @malb to @robertwb.



---

archive/issue_comments_018250.json:
```json
{
    "body": "So far so good:\n\n```\nsage: cyclotomic_polynomial(1)\nx - 1\nsage: cyclotomic_polynomial(2^45)\n---------------------------------------------------------------------------\n<type 'exceptions.MemoryError'>           Traceback (most recent call last)\n\n/scratch/mabshoff/release-cycle/sage-3.0.alpha0/<ipython console> in <module>()\n\n/scratch/mabshoff/release-cycle/sage-3.0.alpha0/local/lib/python2.5/site-packages/sage/misc/functional.py in cyclotomic_polynomial(n, var)\n    199     \"\"\"\n    200     return sage.rings.all.PolynomialRing(\\\n--> 201                   sage.rings.all.ZZ, name=var).cyclotomic_polynomial(n)\n    202\n    203 def decomposition(x):\n\n/scratch/mabshoff/release-cycle/sage-3.0.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in cyclotomic_polynomial(self, n)\n    594             return self.gen() - 1\n    595         else:\n--> 596             return self(cyclotomic.cyclotomic_coeffs(n), check=True)\n    597\n    598     def gen(self, n=0):\n\n/scratch/mabshoff/release-cycle/sage-3.0.alpha0/cyclotomic.pyx in sage.rings.polynomial.cyclotomic.cyclotomic_coeffs()\n\n<type 'exceptions.MemoryError'>: Not enough memory to calculate cyclotomic polynomial of 35184372088832\n```\n\n\nI tried `cyclotomic_polynomial(2^30)` on sage.math, but killed it when it started to consume more than 16GB of RAM. So can somebody please check on as 32 bit platform?\n\nBut: it causes doctest trouble for me:\n\n```\nsage -t -long devel/sage/sage/rings/polynomial/polynomial_ring.py: 1 doctests failed\nsage -t -long devel/sage/sage/rings/polynomial/cyclotomic.pyx: 1 doctests failed\nsage -t -long devel/sage/sage/combinat/sf/hall_littlewood.py: 16 doctests failed\nsage -t -long devel/sage/sage/combinat/schubert_polynomial.py: 4 doctests failed\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-04-01T12:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18250",
    "user": "mabshoff"
}
```

So far so good:

```
sage: cyclotomic_polynomial(1)
x - 1
sage: cyclotomic_polynomial(2^45)
---------------------------------------------------------------------------
<type 'exceptions.MemoryError'>           Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.0.alpha0/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.0.alpha0/local/lib/python2.5/site-packages/sage/misc/functional.py in cyclotomic_polynomial(n, var)
    199     """
    200     return sage.rings.all.PolynomialRing(\
--> 201                   sage.rings.all.ZZ, name=var).cyclotomic_polynomial(n)
    202
    203 def decomposition(x):

/scratch/mabshoff/release-cycle/sage-3.0.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py in cyclotomic_polynomial(self, n)
    594             return self.gen() - 1
    595         else:
--> 596             return self(cyclotomic.cyclotomic_coeffs(n), check=True)
    597
    598     def gen(self, n=0):

/scratch/mabshoff/release-cycle/sage-3.0.alpha0/cyclotomic.pyx in sage.rings.polynomial.cyclotomic.cyclotomic_coeffs()

<type 'exceptions.MemoryError'>: Not enough memory to calculate cyclotomic polynomial of 35184372088832
```


I tried `cyclotomic_polynomial(2^30)` on sage.math, but killed it when it started to consume more than 16GB of RAM. So can somebody please check on as 32 bit platform?

But: it causes doctest trouble for me:

```
sage -t -long devel/sage/sage/rings/polynomial/polynomial_ring.py: 1 doctests failed
sage -t -long devel/sage/sage/rings/polynomial/cyclotomic.pyx: 1 doctests failed
sage -t -long devel/sage/sage/combinat/sf/hall_littlewood.py: 16 doctests failed
sage -t -long devel/sage/sage/combinat/schubert_polynomial.py: 4 doctests failed
```


Cheers,

Michael



---

archive/issue_comments_018251.json:
```json
{
    "body": "These examples (powers of two) show very clearly what I was talking about.  The `2^n'th` cyclotomic polynomial is `x<sup>(2</sup>(n-1))+1` which is obtained by taking x+1 and replacing x by `x<sup>(2</sup>(n-1))`.  This should be trivial for sparse polys, and one would expect a fatal explosion for dense polys.\n\nI'll try it on my 32 bit machine now.",
    "created_at": "2008-04-01T12:58:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18251",
    "user": "@JohnCremona"
}
```

These examples (powers of two) show very clearly what I was talking about.  The `2^n'th` cyclotomic polynomial is `x<sup>(2</sup>(n-1))+1` which is obtained by taking x+1 and replacing x by `x<sup>(2</sup>(n-1))`.  This should be trivial for sparse polys, and one would expect a fatal explosion for dense polys.

I'll try it on my 32 bit machine now.



---

archive/issue_comments_018252.json:
```json
{
    "body": "This is on a 32-bit machine (Linux fermat 2.6.22-14-generic #1 SMP Tue Feb 12 07:42:25 UTC 2008 i686 GNU/Linux)\n\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: cyclo\nsage: time f=cyclotomic_polynomial(2^26)\nCPU times: user 0.70 s, sys: 0.54 s, total: 1.24 s\nWall time: 1.24\nsage: time f=cyclotomic_polynomial(2^27)\nexcessive length in vector::SetLength\n/home/jec/sage-2.11/local/bin/sage-sage: line 214: 30105 Aborted                 (core dumped) sage-ipython \"$@\" -c \"$SAGE_STARTUP_COMMAND;\"\n```\n\n| SAGE Version 2.11, Release Date: 2008-03-30                        |\n| Type notebook() for the GUI, and license() for information.        |\nBy the way, there's a huge time penalty in displaying the results of (say) `cyclotomic_polynomial(2^26)`, after the wall time is displayed and before the poly itself is (which is why in the above clip I assigned the result to a variable instead of outputting it).  I supect that the output takes time O(degree) instead of O(number-of-terms).  If that is true, can it be fixed?",
    "created_at": "2008-04-01T15:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18252",
    "user": "@JohnCremona"
}
```

This is on a 32-bit machine (Linux fermat 2.6.22-14-generic #1 SMP Tue Feb 12 07:42:25 UTC 2008 i686 GNU/Linux)



```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: cyclo
sage: time f=cyclotomic_polynomial(2^26)
CPU times: user 0.70 s, sys: 0.54 s, total: 1.24 s
Wall time: 1.24
sage: time f=cyclotomic_polynomial(2^27)
excessive length in vector::SetLength
/home/jec/sage-2.11/local/bin/sage-sage: line 214: 30105 Aborted                 (core dumped) sage-ipython "$@" -c "$SAGE_STARTUP_COMMAND;"
```

| SAGE Version 2.11, Release Date: 2008-03-30                        |
| Type notebook() for the GUI, and license() for information.        |
By the way, there's a huge time penalty in displaying the results of (say) `cyclotomic_polynomial(2^26)`, after the wall time is displayed and before the poly itself is (which is why in the above clip I assigned the result to a variable instead of outputting it).  I supect that the output takes time O(degree) instead of O(number-of-terms).  If that is true, can it be fixed?



---

archive/issue_comments_018253.json:
```json
{
    "body": "The SetLength crash is an NTL issue (NTL has a limit on how large polynomials can be, one can duplicate the error trying to make x<sup>{(2</sup>30)} directly by doing\n\n\n```\nsage: ZZ['x']({2^30: 1})\noverflow in SetCoeff\n/Users/robert/sage/current/local/bin/sage-sage: line 222: 13929 Abort trap              sage-ipython \"$@\" -c \"$SAGE_STARTUP_COMMAND;\"\n```\n\n\nI'll make it throw an error instead of crashing in this case. Does anyone know what the NTL limit is for polynomial degrees? \n\nPrinting taking a long time is a more involved problem, but the real issue here is that we don't have sparse univariate polynomials. \n\nI'll look at the doctests too, it's strange 'cause I didn't change anything that should have affected combinat.",
    "created_at": "2008-04-01T20:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18253",
    "user": "@robertwb"
}
```

The SetLength crash is an NTL issue (NTL has a limit on how large polynomials can be, one can duplicate the error trying to make x<sup>{(2</sup>30)} directly by doing


```
sage: ZZ['x']({2^30: 1})
overflow in SetCoeff
/Users/robert/sage/current/local/bin/sage-sage: line 222: 13929 Abort trap              sage-ipython "$@" -c "$SAGE_STARTUP_COMMAND;"
```


I'll make it throw an error instead of crashing in this case. Does anyone know what the NTL limit is for polynomial degrees? 

Printing taking a long time is a more involved problem, but the real issue here is that we don't have sparse univariate polynomials. 

I'll look at the doctests too, it's strange 'cause I didn't change anything that should have affected combinat.



---

archive/issue_comments_018254.json:
```json
{
    "body": "Replying to [comment:14 robertwb]:\n> The SetLength crash is an NTL issue (NTL has a limit on how large polynomials can be, one can duplicate the error trying to make x<sup>{(2</sup>30)} directly by doing\n> \n> {{{\n> sage: ZZ['x']({2^30: 1})\n> overflow in SetCoeff\n> /Users/robert/sage/current/local/bin/sage-sage: line 222: 13929 Abort trap              sage-ipython \"$`@`\" -c \"$SAGE_STARTUP_COMMAND;\"\n> }}}\n> \n> I'll make it throw an error instead of crashing in this case. Does anyone know what the NTL limit is for polynomial degrees? \n> \n\nNo such limit is mentioned at http://www.shoup.net/ntl/doc/ZZX.txt\n\n> Printing taking a long time is a more involved problem, but the real issue here is that we don't have sparse univariate polynomials. \n> \n> I'll look at the doctests too, it's strange 'cause I didn't change anything that should have affected combinat.",
    "created_at": "2008-04-01T21:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18254",
    "user": "@JohnCremona"
}
```

Replying to [comment:14 robertwb]:
> The SetLength crash is an NTL issue (NTL has a limit on how large polynomials can be, one can duplicate the error trying to make x<sup>{(2</sup>30)} directly by doing
> 
> {{{
> sage: ZZ['x']({2^30: 1})
> overflow in SetCoeff
> /Users/robert/sage/current/local/bin/sage-sage: line 222: 13929 Abort trap              sage-ipython "$`@`" -c "$SAGE_STARTUP_COMMAND;"
> }}}
> 
> I'll make it throw an error instead of crashing in this case. Does anyone know what the NTL limit is for polynomial degrees? 
> 

No such limit is mentioned at http://www.shoup.net/ntl/doc/ZZX.txt

> Printing taking a long time is a more involved problem, but the real issue here is that we don't have sparse univariate polynomials. 
> 
> I'll look at the doctests too, it's strange 'cause I didn't change anything that should have affected combinat.



---

archive/issue_comments_018255.json:
```json
{
    "body": "Attachment [2654-cyclo-printing.patch](tarball://root/attachments/some-uuid/ticket2654/2654-cyclo-printing.patch) by @robertwb created at 2008-04-02 19:54:50",
    "created_at": "2008-04-02T19:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18255",
    "user": "@robertwb"
}
```

Attachment [2654-cyclo-printing.patch](tarball://root/attachments/some-uuid/ticket2654/2654-cyclo-printing.patch) by @robertwb created at 2008-04-02 19:54:50



---

archive/issue_comments_018256.json:
```json
{
    "body": "Attachment [2654-cyclo-doctest-fixes.patch](tarball://root/attachments/some-uuid/ticket2654/2654-cyclo-doctest-fixes.patch) by @robertwb created at 2008-04-02 19:58:29\n\nI implemented fast printing for `ZZ[x]`, but the generic case could be done better in some cases and I didn't touch that. \n\nAs for the limit, it's buried in ntl/include/ctools.h. \n\n\n```\n#define NTL_OVFBND (1L << (NTL_BITS_PER_LONG-4))\n```\n\n\nwhich is now checked for (rather than inducing a crash). Also, the failing doctests are fixed.",
    "created_at": "2008-04-02T19:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18256",
    "user": "@robertwb"
}
```

Attachment [2654-cyclo-doctest-fixes.patch](tarball://root/attachments/some-uuid/ticket2654/2654-cyclo-doctest-fixes.patch) by @robertwb created at 2008-04-02 19:58:29

I implemented fast printing for `ZZ[x]`, but the generic case could be done better in some cases and I didn't touch that. 

As for the limit, it's buried in ntl/include/ctools.h. 


```
#define NTL_OVFBND (1L << (NTL_BITS_PER_LONG-4))
```


which is now checked for (rather than inducing a crash). Also, the failing doctests are fixed.



---

archive/issue_comments_018257.json:
```json
{
    "body": "I have succesfully applied the last two patches and tested them, and am very happy with this now.\nAll four patches are needed!",
    "created_at": "2008-04-02T21:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18257",
    "user": "@JohnCremona"
}
```

I have succesfully applied the last two patches and tested them, and am very happy with this now.
All four patches are needed!



---

archive/issue_comments_018258.json:
```json
{
    "body": "I am seeing one doctest failure with all four patches applied on sage.math:\n\n```\nsage-3.0.alpha1$ ./sage -t -long devel/sage/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx\nsage -t -long devel/sage/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.alpha1/tmp/polynomial_integer_dense_ntl.py\", line 131:\n    sage: ZZ['x']({2^3: 1})\nExpected:\n    x^8\n    Traceback (most recent call last):\n    ...\n    OverflowError: Dense NTL integer polynomials have a maximum degree of 268435455\nGot:\n    x^8\n**********************************************************************\n```\n\n\nI would assume this is a 32bit vs. 64bit issue. Man, it is time for FLINT to take over Z[x].\n\nCheers,\n\nMichael",
    "created_at": "2008-04-04T13:00:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18258",
    "user": "mabshoff"
}
```

I am seeing one doctest failure with all four patches applied on sage.math:

```
sage-3.0.alpha1$ ./sage -t -long devel/sage/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx
sage -t -long devel/sage/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha1/tmp/polynomial_integer_dense_ntl.py", line 131:
    sage: ZZ['x']({2^3: 1})
Expected:
    x^8
    Traceback (most recent call last):
    ...
    OverflowError: Dense NTL integer polynomials have a maximum degree of 268435455
Got:
    x^8
**********************************************************************
```


I would assume this is a 32bit vs. 64bit issue. Man, it is time for FLINT to take over Z[x].

Cheers,

Michael



---

archive/issue_comments_018259.json:
```json
{
    "body": "Attachment [2654-cyclo-64bit.patch](tarball://root/attachments/some-uuid/ticket2654/2654-cyclo-64bit.patch) by @robertwb created at 2008-04-04 18:23:19",
    "created_at": "2008-04-04T18:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18259",
    "user": "@robertwb"
}
```

Attachment [2654-cyclo-64bit.patch](tarball://root/attachments/some-uuid/ticket2654/2654-cyclo-64bit.patch) by @robertwb created at 2008-04-04 18:23:19



---

archive/issue_comments_018260.json:
```json
{
    "body": "Yes, I didn't have a 64 bit tests in the doctest, so the docstring got mangled. I posted a patch to address this issue.",
    "created_at": "2008-04-04T18:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18260",
    "user": "@robertwb"
}
```

Yes, I didn't have a 64 bit tests in the doctest, so the docstring got mangled. I posted a patch to address this issue.



---

archive/issue_comments_018261.json:
```json
{
    "body": "Yep. That fixes the issue for me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-04T18:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18261",
    "user": "mabshoff"
}
```

Yep. That fixes the issue for me. Positive review.

Cheers,

Michael



---

archive/issue_comments_018262.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-04T19:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18262",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha1



---

archive/issue_comments_018263.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T19:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2654#issuecomment-18263",
    "user": "mabshoff"
}
```

Resolution: fixed
