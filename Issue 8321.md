# Issue 8321: numerical integration with arbitrary precision

archive/issues_008321.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  maldun fredrik.johansson kcrisman mariah bober eviatarbach mforets\n\nFrom the sage-devel:\n\n\n```\nOn Feb 20, 2010, at 12:40 PM, John H Palmieri wrote:\n...\n> I was curious about this, so I tried specifying the number of digits:\n>\n> sage: h = integral(sin(x)/x^2, (x, 1, pi/2)); h\n> integrate(sin(x)/x^2, x, 1, 1/2*pi)\n> sage: h.n()\n> 0.33944794097891573\n> sage: h.n(digits=14)\n> 0.33944794097891573\n> sage: h.n(digits=600)\n> 0.33944794097891573\n> sage: h.n(digits=600) == h.n(digits=14)\n> True\n> sage: h.n(prec=50) == h.n(prec=1000)\n> True\n>\n> Is there an inherit limit in Sage on the accuracy of numerical\n> integrals?  \n```\n\n\nThe `_evalf_` function defined on line 179 of `sage/symbolic/integration/integral.py` calls the gsl `numerical_integral()` function and ignores the precision.\n\nWe should raise a `NotImplementedError` for high precision, or find a way to do arbitrary precision numerical integration.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8321\n\n",
    "created_at": "2010-02-21T21:26:32Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "numerical integration with arbitrary precision",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8321",
    "user": "burcin"
}
```
Assignee: burcin

CC:  maldun fredrik.johansson kcrisman mariah bober eviatarbach mforets

From the sage-devel:


```
On Feb 20, 2010, at 12:40 PM, John H Palmieri wrote:
...
> I was curious about this, so I tried specifying the number of digits:
>
> sage: h = integral(sin(x)/x^2, (x, 1, pi/2)); h
> integrate(sin(x)/x^2, x, 1, 1/2*pi)
> sage: h.n()
> 0.33944794097891573
> sage: h.n(digits=14)
> 0.33944794097891573
> sage: h.n(digits=600)
> 0.33944794097891573
> sage: h.n(digits=600) == h.n(digits=14)
> True
> sage: h.n(prec=50) == h.n(prec=1000)
> True
>
> Is there an inherit limit in Sage on the accuracy of numerical
> integrals?  
```


The `_evalf_` function defined on line 179 of `sage/symbolic/integration/integral.py` calls the gsl `numerical_integral()` function and ignores the precision.

We should raise a `NotImplementedError` for high precision, or find a way to do arbitrary precision numerical integration.

Issue created by migration from https://trac.sagemath.org/ticket/8321





---

archive/issue_comments_073805.json:
```json
{
    "body": "Note that PARI/GP can do (arbitrary precision) numerical integration:\n\n```\nsage: %gp\ngp: \\p100\n   realprecision = 115 significant digits (100 digits displayed)\ngp: intnum(x=1,Pi/2,sin(x)/x^2)\n0.3394479409789156796919271718652186179944769882691752577491475103140509215988087842006743201412102786\n```\n\nI don't know why it does not work from Sage:\n\n```\nsage: gp.intnum(x=1,2,sin(x)/x^2)\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\nSyntaxError: non-keyword arg after keyword arg (<ipython console>, line 1)\n```\n",
    "created_at": "2010-02-24T09:07:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73805",
    "user": "zimmerma"
}
```

Note that PARI/GP can do (arbitrary precision) numerical integration:

```
sage: %gp
gp: \p100
   realprecision = 115 significant digits (100 digits displayed)
gp: intnum(x=1,Pi/2,sin(x)/x^2)
0.3394479409789156796919271718652186179944769882691752577491475103140509215988087842006743201412102786
```

I don't know why it does not work from Sage:

```
sage: gp.intnum(x=1,2,sin(x)/x^2)
------------------------------------------------------------
   File "<ipython console>", line 1
SyntaxError: non-keyword arg after keyword arg (<ipython console>, line 1)
```




---

archive/issue_comments_073806.json:
```json
{
    "body": "There is an example-doctest in the file `interfaces/maxima.py`, for the method `nintegral`.  It says:\n\n\n```\n        Note that GP also does numerical integration, and can do so to very\n        high precision very quickly::\n        \n            sage: gp('intnum(x=0,1,exp(-sqrt(x)))')            \n            0.5284822353142307136179049194             # 32-bit\n            0.52848223531423071361790491935415653021   # 64-bit\n            sage: _ = gp.set_precision(80)\n            sage: gp('intnum(x=0,1,exp(-sqrt(x)))')\n            0.52848223531423071361790491935415653021675547587292866196865279321015401702040079\n```\n",
    "created_at": "2010-02-25T11:12:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73806",
    "user": "AlexGhitza"
}
```

There is an example-doctest in the file `interfaces/maxima.py`, for the method `nintegral`.  It says:


```
        Note that GP also does numerical integration, and can do so to very
        high precision very quickly::
        
            sage: gp('intnum(x=0,1,exp(-sqrt(x)))')            
            0.5284822353142307136179049194             # 32-bit
            0.52848223531423071361790491935415653021   # 64-bit
            sage: _ = gp.set_precision(80)
            sage: gp('intnum(x=0,1,exp(-sqrt(x)))')
            0.52848223531423071361790491935415653021675547587292866196865279321015401702040079
```




---

archive/issue_comments_073807.json:
```json
{
    "body": "mpmath also supports it and can handle python functions.",
    "created_at": "2010-03-06T06:20:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73807",
    "user": "mhansen"
}
```

mpmath also supports it and can handle python functions.



---

archive/issue_comments_073808.json:
```json
{
    "body": "I think I have the solution for this trac with mpmath:\n\n\n```\ndef _evalf_(self, f, x, a, b, parent = None): \n        \"\"\"\n        Returns numerical approximation of the integral\n        \n        EXAMPLES::\n\n            sage: from sage.symbolic.integration.integral import definite_integral\n            sage: h = definite_integral(sin(x)/x^2, x, 1, 2); h\n            integrate(sin(x)/x^2, x, 1, 2)\n            sage: h.n() # indirect doctest\n            0.4723991772689525...\n\n        TESTS:\n\n        Check if #3863 is fixed::\n\n            sage: integrate(x^2.7 * e^(-2.4*x), x, 0, 3).n()\n            0.154572952320790\n\n        #Check if #8321 is fixed:\n\n            sage: d = definite_integral(sin(x)/x^2, x, 1, 2)\n            sage: d.n(77)\n            0.4723991772689525199904\n        \"\"\"\n        #from sage.gsl.integration import numerical_integral\n        # The gsl routine returns a tuple, which also contains the error.\n        # We only return the result.\n        #return numerical_integral(f, a, b)[0]\n\n        #Lets try mpmath instead:\n\n        import sage.libs.mpmath.all as mpmath\n\n        try:\n            precision = parent.prec()\n            mpmath.mp.prec = precision\n        except AttributeError:\n            precision = mpmath.mp.prec\n\n        mp_f = lambda z: \\\n               f(x = mpmath.mpmath_to_sage(z,precision))\n\n        return mpmath.call(mpmath.quad,mp_f,[a,b])\n```\n\n\nThe tests just run fine:\n\n```\nsage: sage: sage: from sage.symbolic.integration.integral import definite_integral\nsage: sage: h = definite_integral(sin(x)/x^2, x, 1, 2); h\nintegrate(sin(x)/x^2, x, 1, 2)\nsage: h.n()\n0.472399177268953\nsage: h.n(77)\n0.4723991772689525199904\nsage: h.n(100)\n0.47239917726895251999041133798\n```\n\n\ngreez maldun",
    "created_at": "2010-08-25T15:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73808",
    "user": "maldun"
}
```

I think I have the solution for this trac with mpmath:


```
def _evalf_(self, f, x, a, b, parent = None): 
        """
        Returns numerical approximation of the integral
        
        EXAMPLES::

            sage: from sage.symbolic.integration.integral import definite_integral
            sage: h = definite_integral(sin(x)/x^2, x, 1, 2); h
            integrate(sin(x)/x^2, x, 1, 2)
            sage: h.n() # indirect doctest
            0.4723991772689525...

        TESTS:

        Check if #3863 is fixed::

            sage: integrate(x^2.7 * e^(-2.4*x), x, 0, 3).n()
            0.154572952320790

        #Check if #8321 is fixed:

            sage: d = definite_integral(sin(x)/x^2, x, 1, 2)
            sage: d.n(77)
            0.4723991772689525199904
        """
        #from sage.gsl.integration import numerical_integral
        # The gsl routine returns a tuple, which also contains the error.
        # We only return the result.
        #return numerical_integral(f, a, b)[0]

        #Lets try mpmath instead:

        import sage.libs.mpmath.all as mpmath

        try:
            precision = parent.prec()
            mpmath.mp.prec = precision
        except AttributeError:
            precision = mpmath.mp.prec

        mp_f = lambda z: \
               f(x = mpmath.mpmath_to_sage(z,precision))

        return mpmath.call(mpmath.quad,mp_f,[a,b])
```


The tests just run fine:

```
sage: sage: sage: from sage.symbolic.integration.integral import definite_integral
sage: sage: h = definite_integral(sin(x)/x^2, x, 1, 2); h
integrate(sin(x)/x^2, x, 1, 2)
sage: h.n()
0.472399177268953
sage: h.n(77)
0.4723991772689525199904
sage: h.n(100)
0.47239917726895251999041133798
```


greez maldun



---

archive/issue_comments_073809.json:
```json
{
    "body": "Changing assignee from burcin to maldun.",
    "created_at": "2010-08-25T15:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73809",
    "user": "maldun"
}
```

Changing assignee from burcin to maldun.



---

archive/issue_comments_073810.json:
```json
{
    "body": "Changing assignee from maldun to burcin.",
    "created_at": "2010-08-25T15:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73810",
    "user": "maldun"
}
```

Changing assignee from maldun to burcin.



---

archive/issue_comments_073811.json:
```json
{
    "body": "Numerical evaluation of symbolic integration with arbitrary precision with help of mpmath",
    "created_at": "2010-08-25T15:43:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73811",
    "user": "maldun"
}
```

Numerical evaluation of symbolic integration with arbitrary precision with help of mpmath



---

archive/issue_comments_073812.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-25T15:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73812",
    "user": "maldun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073813.json:
```json
{
    "body": "Attachment [trac_8321_numeric_int_mpmath.patch](tarball://root/attachments/some-uuid/ticket8321/trac_8321_numeric_int_mpmath.patch) by maldun created at 2010-08-25 15:43:57",
    "created_at": "2010-08-25T15:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73813",
    "user": "maldun"
}
```

Attachment [trac_8321_numeric_int_mpmath.patch](tarball://root/attachments/some-uuid/ticket8321/trac_8321_numeric_int_mpmath.patch) by maldun created at 2010-08-25 15:43:57



---

archive/issue_comments_073814.json:
```json
{
    "body": "Thanks, Maldun, this is a good addition to have.  I don't have time to review this immediately, but it would be helpful to know if you detected any errors, compared this with symbolic integrals and their evaluation, etc.  Basically, that the results from this really are as accurate as advertised.  \n\nAlso, you might as well leave the GSL stuff in as comments, as in the patch you posted above, or even as an optional argument, though that may not be compatible with `_evalf_` elsewhere...",
    "created_at": "2010-08-26T18:49:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73814",
    "user": "kcrisman"
}
```

Thanks, Maldun, this is a good addition to have.  I don't have time to review this immediately, but it would be helpful to know if you detected any errors, compared this with symbolic integrals and their evaluation, etc.  Basically, that the results from this really are as accurate as advertised.  

Also, you might as well leave the GSL stuff in as comments, as in the patch you posted above, or even as an optional argument, though that may not be compatible with `_evalf_` elsewhere...



---

archive/issue_comments_073815.json:
```json
{
    "body": "Does this work for double integrals?",
    "created_at": "2010-08-26T20:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73815",
    "user": "mhansen"
}
```

Does this work for double integrals?



---

archive/issue_comments_073816.json:
```json
{
    "body": "Replying to [comment:8 kcrisman]:\n> Thanks, Maldun, this is a good addition to have.  I don't have time to review this immediately, but it would be helpful to know if you detected any errors, compared this with symbolic integrals and their evaluation, etc.  Basically, that the results from this really are as accurate as advertised.  \n> \n> Also, you might as well leave the GSL stuff in as comments, as in the patch you posted above, or even as an optional argument, though that may not be compatible with `_evalf_` elsewhere... \n\nI will consider this, but hopefully it is not necessary, and mpmath will do the whole thing.\nIf I understood that right, burcin wants to change the numerical evaluation completly to mpmath, because it supports arbitrary prescision.\n\nI plyed arround a little, and I didn't find any differences between the other evaluation methods. In some cases it works even better (I had an example recently in ask sage, which motivated me to switch to this form ov _evalf_)",
    "created_at": "2010-08-27T15:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73816",
    "user": "maldun"
}
```

Replying to [comment:8 kcrisman]:
> Thanks, Maldun, this is a good addition to have.  I don't have time to review this immediately, but it would be helpful to know if you detected any errors, compared this with symbolic integrals and their evaluation, etc.  Basically, that the results from this really are as accurate as advertised.  
> 
> Also, you might as well leave the GSL stuff in as comments, as in the patch you posted above, or even as an optional argument, though that may not be compatible with `_evalf_` elsewhere... 

I will consider this, but hopefully it is not necessary, and mpmath will do the whole thing.
If I understood that right, burcin wants to change the numerical evaluation completly to mpmath, because it supports arbitrary prescision.

I plyed arround a little, and I didn't find any differences between the other evaluation methods. In some cases it works even better (I had an example recently in ask sage, which motivated me to switch to this form ov _evalf_)



---

archive/issue_comments_073817.json:
```json
{
    "body": "Replying to [comment:9 mhansen]:\n> Does this work for double integrals?\n\nmpmath does, this function doesn't, but the current version in sage didn't either, so it's no prob.\nIf we want to support double integrals, one had to change the base class.",
    "created_at": "2010-08-27T15:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73817",
    "user": "maldun"
}
```

Replying to [comment:9 mhansen]:
> Does this work for double integrals?

mpmath does, this function doesn't, but the current version in sage didn't either, so it's no prob.
If we want to support double integrals, one had to change the base class.



---

archive/issue_comments_073818.json:
```json
{
    "body": "Changing keywords from \"\" to \"numerics,integration\".",
    "created_at": "2010-08-28T11:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73818",
    "user": "burcin"
}
```

Changing keywords from "" to "numerics,integration".



---

archive/issue_comments_073819.json:
```json
{
    "body": "Thank you for the patch Stefan. This was much needed for quite a while now.\n\nReplying to [comment:10 maldun]:\n> Replying to [comment:8 kcrisman]:\n> > Thanks, Maldun, this is a good addition to have.  I don't have time to review this immediately, but it would be helpful to know if you detected any errors, compared this with symbolic integrals and their evaluation, etc.  Basically, that the results from this really are as accurate as advertised. \n\nI agree. I like how the patch looks overall. It would be good to see comparisons on\n* error margins\n* speed\n\nMaybe Fredrik can comment on this as well.\n\nUsing `fast_callable()` for `mp_f` could help improve the speed.\n\nDoes anyone know of good examples to add as tests for numerical integration?\n\n> > Also, you might as well leave the GSL stuff in as comments, as in the patch you posted above, or even as an optional argument, though that may not be compatible with `_evalf_` elsewhere... \n\nUnfortunately, ATM, the numerical evaluation framework for symbolic expressions doesn't support specifying different methods. This could (probably, I didn't check the code) be done by changing the interpretation of the python object we pass around to keep the algorithm parameter and the parent, instead of just the parent. Is this a desirable change? Shall we open a ticket for this?\n\n> I will consider this, but hopefully it is not necessary, and mpmath will do the whole thing.\n> If I understood that right, burcin wants to change the numerical evaluation completly to mpmath, because it supports arbitrary prescision.\n\nI guess this is based on a comment I made in the context of orthogonal polynomials and scipy vs. mpmath. Instead of a general policy, I'd like to consider each function separately. \n\nOverall, I'd lean toward using `mpfr` if it supports the given function. Otherwise, choosing between `pari`, `mpmath`, etc. can be difficult, since on many examples one implementation doesn't beat the other uniformly for different precision or domains.",
    "created_at": "2010-08-28T11:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73819",
    "user": "burcin"
}
```

Thank you for the patch Stefan. This was much needed for quite a while now.

Replying to [comment:10 maldun]:
> Replying to [comment:8 kcrisman]:
> > Thanks, Maldun, this is a good addition to have.  I don't have time to review this immediately, but it would be helpful to know if you detected any errors, compared this with symbolic integrals and their evaluation, etc.  Basically, that the results from this really are as accurate as advertised. 

I agree. I like how the patch looks overall. It would be good to see comparisons on
* error margins
* speed

Maybe Fredrik can comment on this as well.

Using `fast_callable()` for `mp_f` could help improve the speed.

Does anyone know of good examples to add as tests for numerical integration?

> > Also, you might as well leave the GSL stuff in as comments, as in the patch you posted above, or even as an optional argument, though that may not be compatible with `_evalf_` elsewhere... 

Unfortunately, ATM, the numerical evaluation framework for symbolic expressions doesn't support specifying different methods. This could (probably, I didn't check the code) be done by changing the interpretation of the python object we pass around to keep the algorithm parameter and the parent, instead of just the parent. Is this a desirable change? Shall we open a ticket for this?

> I will consider this, but hopefully it is not necessary, and mpmath will do the whole thing.
> If I understood that right, burcin wants to change the numerical evaluation completly to mpmath, because it supports arbitrary prescision.

I guess this is based on a comment I made in the context of orthogonal polynomials and scipy vs. mpmath. Instead of a general policy, I'd like to consider each function separately. 

Overall, I'd lean toward using `mpfr` if it supports the given function. Otherwise, choosing between `pari`, `mpmath`, etc. can be difficult, since on many examples one implementation doesn't beat the other uniformly for different precision or domains.



---

archive/issue_comments_073820.json:
```json
{
    "body": "Replying to [comment:12 burcin]:\n> Thank you for the patch Stefan. This was much needed for quite a while now.\n> \n> Replying to [comment:10 maldun]:\n> > Replying to [comment:8 kcrisman]:\n> > > Thanks, Maldun, this is a good addition to have.  I don't have time to review this immediately, but it would be helpful to know if you detected any errors, compared this with symbolic integrals and their evaluation, etc.  Basically, that the results from this really are as accurate as advertised. \n> \n> I agree. I like how the patch looks overall. It would be good to see comparisons on\n>  * error margins\n>  * speed\n> \n> Maybe Fredrik can comment on this as well.\n> \n> Using `fast_callable()` for `mp_f` could help improve the speed.\n> \nOk I will try this + do some tests in the near future!\n\n> Does anyone know of good examples to add as tests for numerical integration?\n>\nI think I should find some, since I did/do a lot of work with finite element, spectral methods,\nand boundary elements. I hope I can do this in the coming weeks.\n\n> > > Also, you might as well leave the GSL stuff in as comments, as in the patch you posted above, or even as an optional argument, though that may not be compatible with `_evalf_` elsewhere... \n> \n> Unfortunately, ATM, the numerical evaluation framework for symbolic expressions doesn't support specifying different methods. This could (probably, I didn't check the code) be done by changing the interpretation of the python object we pass around to keep the algorithm parameter and the parent, instead of just the parent. Is this a desirable change? Shall we open a ticket for this?\n> \nI personally would highly recommend this. Consider for example highly oscillating integrals like \n`\\int_0^pi f(x) sin(n*x) dx` for large `n`'s or the example from Runge:\nhttp://en.wikipedia.org/wiki/Runge%27s_phenomenon.\nI would also suggest to take SciPy into consideration to provide indiviual data points.\nOn Friday, I and a colleague of mine had a simple example of a piecewise function, that only ScipPy could do properly while mpmath failed, (even MATLAB had problems) because I handled individual data points (mpath also provides different quadrature rules).\nIf you would like I could work on this.\n\n> I guess this is based on a comment I made in the context of orthogonal polynomials and SciPy vs. mpmath. Instead of a general policy, I'd like to consider each function separately. \n> \n> Overall, I'd lean toward using `mpfr` if it supports the given function. Otherwise, choosing between `pari`, `mpmath`, etc. can be difficult, since on many examples one implementation doesn't beat the other uniformly for different precision or domains.\n\nThat's true. I think we should provide, like mentioned above, method parameters.\nBut I don't think we have to fear compability problems, because if I understood the documentation of \nmpmath correctly it only evals the function on a data grid, and returns the `\\sum weigth_i * data_i`.\n\ngreez maldun",
    "created_at": "2010-08-28T17:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73820",
    "user": "maldun"
}
```

Replying to [comment:12 burcin]:
> Thank you for the patch Stefan. This was much needed for quite a while now.
> 
> Replying to [comment:10 maldun]:
> > Replying to [comment:8 kcrisman]:
> > > Thanks, Maldun, this is a good addition to have.  I don't have time to review this immediately, but it would be helpful to know if you detected any errors, compared this with symbolic integrals and their evaluation, etc.  Basically, that the results from this really are as accurate as advertised. 
> 
> I agree. I like how the patch looks overall. It would be good to see comparisons on
>  * error margins
>  * speed
> 
> Maybe Fredrik can comment on this as well.
> 
> Using `fast_callable()` for `mp_f` could help improve the speed.
> 
Ok I will try this + do some tests in the near future!

> Does anyone know of good examples to add as tests for numerical integration?
>
I think I should find some, since I did/do a lot of work with finite element, spectral methods,
and boundary elements. I hope I can do this in the coming weeks.

> > > Also, you might as well leave the GSL stuff in as comments, as in the patch you posted above, or even as an optional argument, though that may not be compatible with `_evalf_` elsewhere... 
> 
> Unfortunately, ATM, the numerical evaluation framework for symbolic expressions doesn't support specifying different methods. This could (probably, I didn't check the code) be done by changing the interpretation of the python object we pass around to keep the algorithm parameter and the parent, instead of just the parent. Is this a desirable change? Shall we open a ticket for this?
> 
I personally would highly recommend this. Consider for example highly oscillating integrals like 
`\int_0^pi f(x) sin(n*x) dx` for large `n`'s or the example from Runge:
http://en.wikipedia.org/wiki/Runge%27s_phenomenon.
I would also suggest to take SciPy into consideration to provide indiviual data points.
On Friday, I and a colleague of mine had a simple example of a piecewise function, that only ScipPy could do properly while mpmath failed, (even MATLAB had problems) because I handled individual data points (mpath also provides different quadrature rules).
If you would like I could work on this.

> I guess this is based on a comment I made in the context of orthogonal polynomials and SciPy vs. mpmath. Instead of a general policy, I'd like to consider each function separately. 
> 
> Overall, I'd lean toward using `mpfr` if it supports the given function. Otherwise, choosing between `pari`, `mpmath`, etc. can be difficult, since on many examples one implementation doesn't beat the other uniformly for different precision or domains.

That's true. I think we should provide, like mentioned above, method parameters.
But I don't think we have to fear compability problems, because if I understood the documentation of 
mpmath correctly it only evals the function on a data grid, and returns the `\sum weigth_i * data_i`.

greez maldun



---

archive/issue_comments_073821.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-28T17:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73821",
    "user": "maldun"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_073822.json:
```json
{
    "body": "Replying to [comment:13 maldun]:\n> Replying to [comment:12 burcin]:\n> > > Replying to [comment:8 kcrisman]:\n\n> > > > Also, you might as well leave the GSL stuff in as comments, as in the patch you posted above, or even as an optional argument, though that may not be compatible with `_evalf_` elsewhere... \n> > \n> > Unfortunately, ATM, the numerical evaluation framework for symbolic expressions doesn't support specifying different methods. This could (probably, I didn't check the code) be done by changing the interpretation of the python object we pass around to keep the algorithm parameter and the parent, instead of just the parent. Is this a desirable change? Shall we open a ticket for this?\n> > \n> I personally would highly recommand this. Consider for example highly oscillating integrals like \n> \\int_0^pi f(x) sin(n*x) dx for large n's or the example from Runge:\n> http://en.wikipedia.org/wiki/Runge%27s_phenomenon.\n> I would also suggest to take scipy into consideration to provide indiviual data points.\n> On friday, I and a colleague of mine had a simple example of a piecewise function, that only scipy could do properly while mpmath failed, (even matlab had problems) because I handled individual data points.(mpath also provides different quadrature rules)\n> If you would like I could work on this    \n\nThat would be great. I suggest making that a new enhancement ticket though. Let's fix this bug first and use mpmath for numerical evaluation. \n\nWe should also open a new ticket for numerical integration of double integrals as Mike was asking in comment:9.",
    "created_at": "2010-08-28T18:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73822",
    "user": "burcin"
}
```

Replying to [comment:13 maldun]:
> Replying to [comment:12 burcin]:
> > > Replying to [comment:8 kcrisman]:

> > > > Also, you might as well leave the GSL stuff in as comments, as in the patch you posted above, or even as an optional argument, though that may not be compatible with `_evalf_` elsewhere... 
> > 
> > Unfortunately, ATM, the numerical evaluation framework for symbolic expressions doesn't support specifying different methods. This could (probably, I didn't check the code) be done by changing the interpretation of the python object we pass around to keep the algorithm parameter and the parent, instead of just the parent. Is this a desirable change? Shall we open a ticket for this?
> > 
> I personally would highly recommand this. Consider for example highly oscillating integrals like 
> \int_0^pi f(x) sin(n*x) dx for large n's or the example from Runge:
> http://en.wikipedia.org/wiki/Runge%27s_phenomenon.
> I would also suggest to take scipy into consideration to provide indiviual data points.
> On friday, I and a colleague of mine had a simple example of a piecewise function, that only scipy could do properly while mpmath failed, (even matlab had problems) because I handled individual data points.(mpath also provides different quadrature rules)
> If you would like I could work on this    

That would be great. I suggest making that a new enhancement ticket though. Let's fix this bug first and use mpmath for numerical evaluation. 

We should also open a new ticket for numerical integration of double integrals as Mike was asking in comment:9.



---

archive/issue_comments_073823.json:
```json
{
    "body": "> Does anyone know of good examples to add as tests for numerical integration? \n\non page 132 of http://cannelle.lateralis.org/sagebook-1.0.pdf you'll find 10 examples.\n\nPaul",
    "created_at": "2010-08-30T10:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73823",
    "user": "zimmerma"
}
```

> Does anyone know of good examples to add as tests for numerical integration? 

on page 132 of http://cannelle.lateralis.org/sagebook-1.0.pdf you'll find 10 examples.

Paul



---

archive/issue_comments_073824.json:
```json
{
    "body": "I suggest the following doctests for integral.py:\n\n\n```\n            #Testing Runge's example:\n            sage: f(x) = 1/(1+25*x^2)\n            sage: f\n            x |--> 1/(25*x^2 + 1)\n            sage: integrate(f(x),x,-1,1)\n            2/5*arctan(5)\n            sage: integrate(1/(1+10^10*x^2),x,0,1)\n            1/100000*arctan(100000)\n            sage: integrate(1/(1+10^10*x^2),x,0,1).n()\n            0.0000157078632679490\n\n            \n            #Highly oscillating integrals:\n            sage: integrate(exp(x)*sin(1000*x),x,0,pi/2)\n            -1000/1000001*e^(1/2*pi) + 1000/1000001\n            sage: integrate(exp(x)*sin(1000*x),x,0,pi/2).n()\n            -0.00381047357049178\n \n            sage: from sage.symbolic.integration.integral import definite_integral\n            sage: definite_integral(exp(10*x)*sin(10000*x), x, 0, 1)\n            1/10000010*e^10*sin(10000) - 100/1000001*e^10*cos(10000) + 100/1000001\n            sage: definite_integral(exp(10*x)*sin(10000*x), x, 0, 1).n()\n            2.09668650785505\n\n            #Different tests:\n            sage: integrate(sin(x^3)*x^2,x,0,10)\n            -1/3*cos(1000) + 1/3\n            sage: integrate(sin(x^3)*x^2,x,0,10).n()\n            0.145873641236432\n            \n            sage: integrate(sin(x)*exp(cos(x)), x, 0, pi)\n            -e^(-1) + e\n            sage: integrate(sin(x)*exp(cos(x)), x, 0, pi).n()\n            2.35040238728760\n            \n            sage: integrate(x*log(1+x),x,0,1)\n            1/4\n            sage: integrate(x*log(1+x),x,0,1).n()\n            0.250000000000000\n\"\"\"\n```\n\n\nFurther Ideas?",
    "created_at": "2010-09-16T22:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73824",
    "user": "maldun"
}
```

I suggest the following doctests for integral.py:


```
            #Testing Runge's example:
            sage: f(x) = 1/(1+25*x^2)
            sage: f
            x |--> 1/(25*x^2 + 1)
            sage: integrate(f(x),x,-1,1)
            2/5*arctan(5)
            sage: integrate(1/(1+10^10*x^2),x,0,1)
            1/100000*arctan(100000)
            sage: integrate(1/(1+10^10*x^2),x,0,1).n()
            0.0000157078632679490

            
            #Highly oscillating integrals:
            sage: integrate(exp(x)*sin(1000*x),x,0,pi/2)
            -1000/1000001*e^(1/2*pi) + 1000/1000001
            sage: integrate(exp(x)*sin(1000*x),x,0,pi/2).n()
            -0.00381047357049178
 
            sage: from sage.symbolic.integration.integral import definite_integral
            sage: definite_integral(exp(10*x)*sin(10000*x), x, 0, 1)
            1/10000010*e^10*sin(10000) - 100/1000001*e^10*cos(10000) + 100/1000001
            sage: definite_integral(exp(10*x)*sin(10000*x), x, 0, 1).n()
            2.09668650785505

            #Different tests:
            sage: integrate(sin(x^3)*x^2,x,0,10)
            -1/3*cos(1000) + 1/3
            sage: integrate(sin(x^3)*x^2,x,0,10).n()
            0.145873641236432
            
            sage: integrate(sin(x)*exp(cos(x)), x, 0, pi)
            -e^(-1) + e
            sage: integrate(sin(x)*exp(cos(x)), x, 0, pi).n()
            2.35040238728760
            
            sage: integrate(x*log(1+x),x,0,1)
            1/4
            sage: integrate(x*log(1+x),x,0,1).n()
            0.250000000000000
"""
```


Further Ideas?



---

archive/issue_comments_073825.json:
```json
{
    "body": "> I suggest the following doctests for integral.py: [...]\n\nthose doctests are not in arbitrary precision (or do you suggest to take them as a basis\nfor arbitrary precision examples?).",
    "created_at": "2010-09-16T23:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73825",
    "user": "zimmerma"
}
```

> I suggest the following doctests for integral.py: [...]

those doctests are not in arbitrary precision (or do you suggest to take them as a basis
for arbitrary precision examples?).



---

archive/issue_comments_073826.json:
```json
{
    "body": "I had now a little time to think about it, and I suggest to add even more tests. \nI initially used this tests, because the analytical solution is known so they would form a good basis. \n\nBut yesterday I found out that if sage knows the analytical solution it just evaluate this, and I don't think this is the best way I gave it to discussion on sage devel: see http://groups.google.com/group/sage-devel/browse_thread/thread/886efb8ca8bdcff2\n\nWhy do I have this concern?\njust try this:\n\n```\nintegrate(sin(x^2),x,0,pi).n()\n```\n\n\nI will give more examples today or tomorrow.",
    "created_at": "2010-09-17T09:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73826",
    "user": "maldun"
}
```

I had now a little time to think about it, and I suggest to add even more tests. 
I initially used this tests, because the analytical solution is known so they would form a good basis. 

But yesterday I found out that if sage knows the analytical solution it just evaluate this, and I don't think this is the best way I gave it to discussion on sage devel: see http://groups.google.com/group/sage-devel/browse_thread/thread/886efb8ca8bdcff2

Why do I have this concern?
just try this:

```
integrate(sin(x^2),x,0,pi).n()
```


I will give more examples today or tomorrow.



---

archive/issue_comments_073827.json:
```json
{
    "body": "See also #7763.  We continue to get support requests because of the non-unified nature of our options.",
    "created_at": "2011-04-18T15:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73827",
    "user": "kcrisman"
}
```

See also #7763.  We continue to get support requests because of the non-unified nature of our options.



---

archive/issue_comments_073828.json:
```json
{
    "body": "#10550 should be closed as a duplicate of this ticket. The discussion there includes some examples that might be useful here.",
    "created_at": "2011-06-14T19:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73828",
    "user": "burcin"
}
```

#10550 should be closed as a duplicate of this ticket. The discussion there includes some examples that might be useful here.



---

archive/issue_comments_073829.json:
```json
{
    "body": "Here is another example from http://openopt.org/IP\n\n\n```\nsigma = 1e-4\nff = exp(-x**2/(2*sigma)) / sqrt(2*pi*sigma)\nbounds_x = (-20, 10)\n```\n",
    "created_at": "2011-06-29T13:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73829",
    "user": "burcin"
}
```

Here is another example from http://openopt.org/IP


```
sigma = 1e-4
ff = exp(-x**2/(2*sigma)) / sqrt(2*pi*sigma)
bounds_x = (-20, 10)
```




---

archive/issue_comments_073830.json:
```json
{
    "body": "Replying to [comment:24 burcin]:\n> Here is another example [...]\n\nBurcin, please can you be more specific, for example with a complete Sage command?\n\nPaul",
    "created_at": "2011-06-29T13:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73830",
    "user": "zimmerma"
}
```

Replying to [comment:24 burcin]:
> Here is another example [...]

Burcin, please can you be more specific, for example with a complete Sage command?

Paul



---

archive/issue_comments_073831.json:
```json
{
    "body": "I hadn't actually done the computation in Sage. I just wanted to note that web site here. :)\n\nWith the patch attached to this ticket:\n\n\n```\nsage: sigma = 1e-4\nsage: ff = exp(-x**2/(2*sigma)) / sqrt(2*pi*sigma)\nsage: from sage.symbolic.integration.integral import definite_integral\nsage: definite_integral(ff, x, -20, 10, hold=True)\nintegrate(70.7106781186548*e^(-5000.00000000000*x^2)/sqrt(pi), x, -20, 10)\nsage: definite_integral(ff, x, -20, 10, hold=True).n()\n5.38249970415053e-939\n```\n\n\nWithout the patch:\n\n\n```\nsage: definite_integral(ff, x, -20, 10, hold=True).n()\n2.1074458151264474e-45\n```\n\n\nWe get a better result if we allow maxima to evaluate the integral symbolically:\n\n\n```\nsage: definite_integral(ff, x, -20, 10).n()\n1.00000000000000\nsage: definite_integral(ff, x, -20, 10)\n0.353553390593*(sqrt(2)*sqrt(pi)*erf(500*sqrt(2)) + sqrt(2)*sqrt(pi)*erf(1000*sqrt(2)))/sqrt(pi)\n```\n\n\nThe web site I linked to in comment:24 links to this page, where i got the example from:\n\nhttp://trac.openopt.org/openopt/browser/PythonPackages/FuncDesigner/FuncDesigner/examples/integrate1.py\n\nHere is an excerpt from that file:\n\n\n```\n'''interalg result: 1.000006 (usually solution, obtained by interalg, has real residual 10-100-1000 times less\nthan required tolerance, because interalg works with \"most worst case\" that extremely rarely occurs.\nUnfortunately, real obtained residual cannot be revealed).\nNow let's ensure scipy.integrate quad fails to solve the problem and mere lies about obtained residual: '''\n```\n",
    "created_at": "2011-06-29T15:21:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73831",
    "user": "burcin"
}
```

I hadn't actually done the computation in Sage. I just wanted to note that web site here. :)

With the patch attached to this ticket:


```
sage: sigma = 1e-4
sage: ff = exp(-x**2/(2*sigma)) / sqrt(2*pi*sigma)
sage: from sage.symbolic.integration.integral import definite_integral
sage: definite_integral(ff, x, -20, 10, hold=True)
integrate(70.7106781186548*e^(-5000.00000000000*x^2)/sqrt(pi), x, -20, 10)
sage: definite_integral(ff, x, -20, 10, hold=True).n()
5.38249970415053e-939
```


Without the patch:


```
sage: definite_integral(ff, x, -20, 10, hold=True).n()
2.1074458151264474e-45
```


We get a better result if we allow maxima to evaluate the integral symbolically:


```
sage: definite_integral(ff, x, -20, 10).n()
1.00000000000000
sage: definite_integral(ff, x, -20, 10)
0.353553390593*(sqrt(2)*sqrt(pi)*erf(500*sqrt(2)) + sqrt(2)*sqrt(pi)*erf(1000*sqrt(2)))/sqrt(pi)
```


The web site I linked to in comment:24 links to this page, where i got the example from:

http://trac.openopt.org/openopt/browser/PythonPackages/FuncDesigner/FuncDesigner/examples/integrate1.py

Here is an excerpt from that file:


```
'''interalg result: 1.000006 (usually solution, obtained by interalg, has real residual 10-100-1000 times less
than required tolerance, because interalg works with "most worst case" that extremely rarely occurs.
Unfortunately, real obtained residual cannot be revealed).
Now let's ensure scipy.integrate quad fails to solve the problem and mere lies about obtained residual: '''
```




---

archive/issue_comments_073832.json:
```json
{
    "body": "Replying to [comment:26 burcin]:\n> I hadn't actually done the computation in Sage. I just wanted to note that web site here. :)\n> \n> With the patch attached to this ticket:\n> \n> {{{\n> sage: sigma = 1e-4\n> sage: ff = exp(-x**2/(2*sigma)) / sqrt(2*pi*sigma)\n> sage: from sage.symbolic.integration.integral import definite_integral\n> sage: definite_integral(ff, x, -20, 10, hold=True)\n> integrate(70.7106781186548*e<sup>(-5000.00000000000*x</sup>2)/sqrt(pi), x, -20, 10)\n> sage: definite_integral(ff, x, -20, 10, hold=True).n()\n> 5.38249970415053e-939\n> }}}\n> \n> Without the patch:\n> \n> {{{\n> sage: definite_integral(ff, x, -20, 10, hold=True).n()\n> 2.1074458151264474e-45\n> }}}\n> \n> We get a better result if we allow maxima to evaluate the integral symbolically:\n> \n> {{{\n> sage: definite_integral(ff, x, -20, 10).n()\n> 1.00000000000000\n> sage: definite_integral(ff, x, -20, 10)\n> 0.353553390593*(sqrt(2)*sqrt(pi)*erf(500*sqrt(2)) + sqrt(2)*sqrt(pi)*erf(1000*sqrt(2)))/sqrt(pi)\n> }}}\n> \n\nThis is indeed a great example!\n\nThis is again a grid problem and not a precision problem. If you make trapezoidal or gauss rule\non finer grids you get also better results. \n\n\n```\nsage: from numpy import *\nsage: from scipy.integrate import trapz\nsage: sigma = 1e-4\nsage: def ff(x): return exp(-x**2/(2*sigma))/sqrt(2*pi*sigma)\n....: \nsage: ffv = vectorize(ff)\nsage: x = arange(-20,10,1)\nsage: y = ffv(x)\nsage: trapz(y,x)\n39.894228040143268\nsage: x = arange(-20,10,0.5)\nsage: y = ffv(x)\nsage: trapz(y,x)\n19.947114020071634\nsage: x = arange(-20,10,0.05)\nsage: y = ffv(x)\nsage: trapz(y,x)\n1.9947262692023391\nsage: x = arange(-20,10,0.005)\nsage: y = ffv(x)\nsage: trapz(y,x)\n1.0\nfrom scipy.integrate import fixed_quad\nsage: fixed_quad(ff,-20,10,n=int(10))\n(0.0, None)\nsage: fixed_quad(ff,-20,10,n=int(100))\n(2.6290056634068843e-58, None)\nsage: fixed_quad(ff,-20,10,n=int(1000))\n(0.8616135058547989, None)\n\n```\n\n\n\nThe reason for this is simply that the function is\napproximately 1 in a small region arround zero and nearly zero elsewhere. Thats also the reason why maxima works so well here: The main part is included in the analytical solution.",
    "created_at": "2011-07-01T11:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73832",
    "user": "maldun"
}
```

Replying to [comment:26 burcin]:
> I hadn't actually done the computation in Sage. I just wanted to note that web site here. :)
> 
> With the patch attached to this ticket:
> 
> {{{
> sage: sigma = 1e-4
> sage: ff = exp(-x**2/(2*sigma)) / sqrt(2*pi*sigma)
> sage: from sage.symbolic.integration.integral import definite_integral
> sage: definite_integral(ff, x, -20, 10, hold=True)
> integrate(70.7106781186548*e<sup>(-5000.00000000000*x</sup>2)/sqrt(pi), x, -20, 10)
> sage: definite_integral(ff, x, -20, 10, hold=True).n()
> 5.38249970415053e-939
> }}}
> 
> Without the patch:
> 
> {{{
> sage: definite_integral(ff, x, -20, 10, hold=True).n()
> 2.1074458151264474e-45
> }}}
> 
> We get a better result if we allow maxima to evaluate the integral symbolically:
> 
> {{{
> sage: definite_integral(ff, x, -20, 10).n()
> 1.00000000000000
> sage: definite_integral(ff, x, -20, 10)
> 0.353553390593*(sqrt(2)*sqrt(pi)*erf(500*sqrt(2)) + sqrt(2)*sqrt(pi)*erf(1000*sqrt(2)))/sqrt(pi)
> }}}
> 

This is indeed a great example!

This is again a grid problem and not a precision problem. If you make trapezoidal or gauss rule
on finer grids you get also better results. 


```
sage: from numpy import *
sage: from scipy.integrate import trapz
sage: sigma = 1e-4
sage: def ff(x): return exp(-x**2/(2*sigma))/sqrt(2*pi*sigma)
....: 
sage: ffv = vectorize(ff)
sage: x = arange(-20,10,1)
sage: y = ffv(x)
sage: trapz(y,x)
39.894228040143268
sage: x = arange(-20,10,0.5)
sage: y = ffv(x)
sage: trapz(y,x)
19.947114020071634
sage: x = arange(-20,10,0.05)
sage: y = ffv(x)
sage: trapz(y,x)
1.9947262692023391
sage: x = arange(-20,10,0.005)
sage: y = ffv(x)
sage: trapz(y,x)
1.0
from scipy.integrate import fixed_quad
sage: fixed_quad(ff,-20,10,n=int(10))
(0.0, None)
sage: fixed_quad(ff,-20,10,n=int(100))
(2.6290056634068843e-58, None)
sage: fixed_quad(ff,-20,10,n=int(1000))
(0.8616135058547989, None)

```



The reason for this is simply that the function is
approximately 1 in a small region arround zero and nearly zero elsewhere. Thats also the reason why maxima works so well here: The main part is included in the analytical solution.



---

archive/issue_comments_073833.json:
```json
{
    "body": "This should really be finished and fixed.  Does anyone have any objection to something that does what Stefan implements (using mpmath) but then has lots of examples in numerical integration and `integrate` warning people not to trust floating-point, even with high precision, calculations?  Otherwise this ticket could get doomed by the \"must be perfect\" problem. \n\nAre there specific places where this patch is causing incorrect or worse behavior?  Burcin's example seems to be equally bad for both, and I disagree with maldun that we shouldn't return symbolic answers.  At some point you have to make a decision, and the definite integral should naturally be symbolic if at all possible.",
    "created_at": "2011-08-15T14:28:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73833",
    "user": "kcrisman"
}
```

This should really be finished and fixed.  Does anyone have any objection to something that does what Stefan implements (using mpmath) but then has lots of examples in numerical integration and `integrate` warning people not to trust floating-point, even with high precision, calculations?  Otherwise this ticket could get doomed by the "must be perfect" problem. 

Are there specific places where this patch is causing incorrect or worse behavior?  Burcin's example seems to be equally bad for both, and I disagree with maldun that we shouldn't return symbolic answers.  At some point you have to make a decision, and the definite integral should naturally be symbolic if at all possible.



---

archive/issue_comments_073834.json:
```json
{
    "body": "Replying to [comment:28 kcrisman]:\n> This should really be finished and fixed.  Does anyone have any objection to something that does what Stefan implements (using mpmath) but then has lots of examples in numerical integration and `integrate` warning people not to trust floating-point, even with high precision, calculations?  Otherwise this ticket could get doomed by the \"must be perfect\" problem.\n\nwe are still waiting for comparison figures for errors and timings (see comment [comment:12]).\nIn those comparisons, I'd like to have arbitrary precision examples (say 20, 50, 100, 200, 500\nand 1000 digits).\n\n> Are there specific places where this patch is causing incorrect or worse behavior?  Burcin's example seems to be equally bad for both, and I disagree with maldun that we shouldn't return symbolic answers.  At some point you have to make a decision, and the definite integral should naturally be symbolic if at all possible.\n\nof course `integrate(...)` will first give a symbolic result if any, then `integrate(...).n()` will evaluate numerically this symbolic value.\nWe should explain in the documentation of `integrate` how to avoid the symbolic evaluation\n(for example adding the `hold` option). Anyway this is a different issue than this ticket.\n\nPaul",
    "created_at": "2011-08-17T16:22:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73834",
    "user": "zimmerma"
}
```

Replying to [comment:28 kcrisman]:
> This should really be finished and fixed.  Does anyone have any objection to something that does what Stefan implements (using mpmath) but then has lots of examples in numerical integration and `integrate` warning people not to trust floating-point, even with high precision, calculations?  Otherwise this ticket could get doomed by the "must be perfect" problem.

we are still waiting for comparison figures for errors and timings (see comment [comment:12]).
In those comparisons, I'd like to have arbitrary precision examples (say 20, 50, 100, 200, 500
and 1000 digits).

> Are there specific places where this patch is causing incorrect or worse behavior?  Burcin's example seems to be equally bad for both, and I disagree with maldun that we shouldn't return symbolic answers.  At some point you have to make a decision, and the definite integral should naturally be symbolic if at all possible.

of course `integrate(...)` will first give a symbolic result if any, then `integrate(...).n()` will evaluate numerically this symbolic value.
We should explain in the documentation of `integrate` how to avoid the symbolic evaluation
(for example adding the `hold` option). Anyway this is a different issue than this ticket.

Paul



---

archive/issue_comments_073835.json:
```json
{
    "body": "rebase of previous patch to 4.7.1",
    "created_at": "2011-08-23T03:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73835",
    "user": "benjaminfjones"
}
```

rebase of previous patch to 4.7.1



---

archive/issue_comments_073836.json:
```json
{
    "body": "Attachment [trac_8321_rebase.patch](tarball://root/attachments/some-uuid/ticket8321/trac_8321_rebase.patch) by benjaminfjones created at 2011-08-23 03:52:05\n\nI'm working on adding numerical integration examples, in the meantime I've posted a rebase of the previously uploaded patch to sage-4.7.1.",
    "created_at": "2011-08-23T03:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73836",
    "user": "benjaminfjones"
}
```

Attachment [trac_8321_rebase.patch](tarball://root/attachments/some-uuid/ticket8321/trac_8321_rebase.patch) by benjaminfjones created at 2011-08-23 03:52:05

I'm working on adding numerical integration examples, in the meantime I've posted a rebase of the previously uploaded patch to sage-4.7.1.



---

archive/issue_comments_073837.json:
```json
{
    "body": "I wrote a small function to compare errors and timings of the GSL implementation (of `numerical_integral`) and the mpmath implementation provided by the patch. Here is the testing code:\n\n\n```python\ndef num_int_test(f, a, b):\n    \"\"\" Input: `f` should be a function of a single variable, [a, b] is a domain of integration \"\"\"\n    LJ = 25 # left justification\n    from sage.symbolic.integration.integral import definite_integral\n    exact_I = definite_integral(f, f.variables()[0], a, b)\n    print \"Exact \".ljust(LJ)     + \" = %s\" % exact_I\n    print \"Exact .n()\".ljust(LJ) + \" = %s\" % exact_I.n()\n    print \"GSL\".ljust(LJ)        + \" = %s\" % numerical_integral(f, a, b)[0]\n    print \"mpmath\".ljust(LJ)     + \" = %s\" % definite_integral(f, f.variables()[0], a, b, hold=True).n()\n    \n    num_I = definite_integral(f, f.variables()[0], a, b, hold=True)\n    for p in [53, 64, 100, 200, 500, 1000]:\n        s = \"mpmath (prec=%d)\" % p\n        print s.ljust(LJ) + \" = %s\" % num_I.n(p)\n        \n    print \"Timings at prec=53:\"\n    print \"    GSL: \",\n    timeit('numerical_integral(%s, %s, %s)' % (f, a, b))\n    print \"    mpmath: \", \n    timeit('definite_integral(%s, %s, %s, %s, hold=True).n()' % (f, f.variables()[0], a, b))\n```\n\n\nNow I took 3 examples from pg. 132 of the PDF suggested above at http://cannelle.lateralis.org/sagebook-1.0.pdf and tested them using `num_int_test`:\n\n\n```\n# applied patch http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8321/trac_8321_rebase.patch\nsage: x = var('x')\nsage: from sage.symbolic.integration.integral import definite_integral\n\n# f = e^(-x^2)*log(x) on [17, 42]\nsage: num_int_test(e^(-x^2)*log(x), 17, 42)\nExact                     = integrate(e^(-x^2)*log(x), x, 17, 42)\nExact .n()                = 2.59225286296247e-127\nGSL                       = 2.5657285007e-127\nmpmath                    = 2.59225286296247e-127\nmpmath (prec=53)          = 2.59225286296247e-127\nmpmath (prec=64)          = 2.59225286296226841e-127\nmpmath (prec=100)         = 2.5922528629622683570941971829e-127\nmpmath (prec=200)         = 2.5922528629622683570941971813123497913329093314031958452707e-127\nmpmath (prec=500)         = 2.56572850056105148291735639613047859001477095540203266250504462960653767523831161390072264481216550025343198689835357618681873598023026225266716067780e-127\nmpmath (prec=1000)        = 2.56572850056105148291735639613047859001477095540203266250504462960653767360416188079136395575326953119218247602307727367985551096000368640359367812179070686479198046287233104280204937504901221620134046153583613193738177820412122516350777255525035947116513676784199592200655526485894447669230515221776e-127\nTimings at prec=53:\n    GSL:  625 loops, best of 3: 971 \u00b5s per loop\n    mpmath:  25 loops, best of 3: 26.9 ms per loop\n\n# f = sqrt(1-x^2) on [0, 1]\nsage: num_int_test(sqrt(1-x^2), 0, 1)\nExact                     = 1/4*pi\nExact .n()                = 0.785398163397448\nGSL                       = 0.785398167726\nmpmath                    = 0.785398163397448\nmpmath (prec=53)          = 0.785398163397448\nmpmath (prec=64)          = 0.785398163397448310\nmpmath (prec=100)         = 0.78539816339744830961566084582\nmpmath (prec=200)         = 0.78539816339744830961566084581987572104929234984377645524374\nmpmath (prec=500)         = 0.785398163397448309615660845819875721049292349843776455243736148076954101571552249657008706335529266995537021628320576661773461152387645557931339852032\nmpmath (prec=1000)        = 0.785398163397448309615660845819875721049292349843776455243736148076954101571552249657008706335529266995537021628320576661773461152387645557931339852032120279362571025675484630276389911155737238732595491107202743916483361532118912058446695791317800477286412141730865087152613581662053348401815062285318\nTimings at prec=53:\n    GSL:  625 loops, best of 3: 652 \u00b5s per loop\n    mpmath:  25 loops, best of 3: 12 ms per loop\n\n# f = sin(sin(x)) on [0, 1]\nsage: num_int_test(sin(sin(x)), 0, 1)\nExact                     = integrate(sin(sin(x)), x, 0, 1)\nExact .n()                = 0.430606103120691\nGSL                       = 0.430606103121\nmpmath                    = 0.430606103120691\nmpmath (prec=53)          = 0.430606103120691\nmpmath (prec=64)          = 0.430606103120690605\nmpmath (prec=100)         = 0.43060610312069060491237735525\nmpmath (prec=200)         = 0.43060610312069060491237735524846578643360804182199746950463\nmpmath (prec=500)         = 0.430606103120690604912377355248465786433608041821997469504633350750892193636074792502000332212863495547968512886769444385260392350928954849458834511854\nmpmath (prec=1000)        = 0.430606103120690604912377355248465786433608041821997469504633350750892193636074792502000332212863495547968512886769444385260392350928954849458834511854394326788473583253436780737313870079328121429092122005425057044706514198162061316772646582265252772251628205725432156943890956907988745419355505731945\nTimings at prec=53:\n    GSL:  625 loops, best of 3: 134 \u00b5s per loop\n    mpmath:  25 loops, best of 3: 11.2 ms per loop\n```\n\n\nIn the second example, GSL's answer compared to the numerically evaluated exact symbolic answer is significantly off. The mpmath answer at default precision matches the  numerically evaluated exact symbolic answer perfectly.\n\nAs for the timings, as you can see GSL is *much* faster than the patch code using mpmath. I tried using `fast_callable` in the case where the domain precision is the same as RDF and that gives a big speedup, though still not as fast as GSL:\n\n\n```python\n    def _evalf( ... ):\n    ...\n    \n        try:\n            precision = parent.prec()\n            mpmath.mp.prec = precision\n            if precision == RDF.precision():\n                mp_f = fast_callable(f, vars=[x], domain=RDF)\n            else:\n                mp_f = lambda z: f(x = mpmath.mpmath_to_sage(z, precision))\n        except AttributeError:\n            mp_f = fast_callable(f, vars=[x], domain=RDF)\n        \n        return mpmath.call(mpmath.quad, mp_f, [a,b])\n```\n\n\nNew timings using `fast_callable`:\n\n\n```\n# Testing: added fast_callable to _evalf_\n# results: definite_integral( ... ) is around 5x faster when called at RDF precision\n\nsage: timeit('numerical_integral(e^(-x^2)*log(x), 17, 42)') # base case using GSL at float precision\n625 loops, best of 3: 959 \u00b5s per loop\nsage: timeit('definite_integral(e^(-x^2)*log(x), x, 17, 42, hold=True).n()') # using fast_callable\n125 loops, best of 3: 5.41 ms per loop\nsage: timeit('definite_integral(e^(-x^2)*log(x), x, 17, 42, hold=True).n(53)') # using fast_callable\n125 loops, best of 3: 5.41 ms per loop\nsage: timeit('definite_integral(e^(-x^2)*log(x), x, 17, 42, hold=True).n(54)') # *not* using fast_callable\n25 loops, best of 3: 28.1 ms per loop\nsage: timeit('definite_integral(e^(-x^2)*log(x), x, 17, 42, hold=True).n(64)') # *not* using fast_callable\n25 loops, best of 3: 26.3 ms per loop\nsage: timeit('definite_integral(e^(-x^2)*log(x), x, 17, 42, hold=True).n(100)') # *not* using fast_callable\n25 loops, best of 3: 32.2 ms per loop\n```\n",
    "created_at": "2011-08-23T06:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73837",
    "user": "benjaminfjones"
}
```

I wrote a small function to compare errors and timings of the GSL implementation (of `numerical_integral`) and the mpmath implementation provided by the patch. Here is the testing code:


```python
def num_int_test(f, a, b):
    """ Input: `f` should be a function of a single variable, [a, b] is a domain of integration """
    LJ = 25 # left justification
    from sage.symbolic.integration.integral import definite_integral
    exact_I = definite_integral(f, f.variables()[0], a, b)
    print "Exact ".ljust(LJ)     + " = %s" % exact_I
    print "Exact .n()".ljust(LJ) + " = %s" % exact_I.n()
    print "GSL".ljust(LJ)        + " = %s" % numerical_integral(f, a, b)[0]
    print "mpmath".ljust(LJ)     + " = %s" % definite_integral(f, f.variables()[0], a, b, hold=True).n()
    
    num_I = definite_integral(f, f.variables()[0], a, b, hold=True)
    for p in [53, 64, 100, 200, 500, 1000]:
        s = "mpmath (prec=%d)" % p
        print s.ljust(LJ) + " = %s" % num_I.n(p)
        
    print "Timings at prec=53:"
    print "    GSL: ",
    timeit('numerical_integral(%s, %s, %s)' % (f, a, b))
    print "    mpmath: ", 
    timeit('definite_integral(%s, %s, %s, %s, hold=True).n()' % (f, f.variables()[0], a, b))
```


Now I took 3 examples from pg. 132 of the PDF suggested above at http://cannelle.lateralis.org/sagebook-1.0.pdf and tested them using `num_int_test`:


```
# applied patch http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8321/trac_8321_rebase.patch
sage: x = var('x')
sage: from sage.symbolic.integration.integral import definite_integral

# f = e^(-x^2)*log(x) on [17, 42]
sage: num_int_test(e^(-x^2)*log(x), 17, 42)
Exact                     = integrate(e^(-x^2)*log(x), x, 17, 42)
Exact .n()                = 2.59225286296247e-127
GSL                       = 2.5657285007e-127
mpmath                    = 2.59225286296247e-127
mpmath (prec=53)          = 2.59225286296247e-127
mpmath (prec=64)          = 2.59225286296226841e-127
mpmath (prec=100)         = 2.5922528629622683570941971829e-127
mpmath (prec=200)         = 2.5922528629622683570941971813123497913329093314031958452707e-127
mpmath (prec=500)         = 2.56572850056105148291735639613047859001477095540203266250504462960653767523831161390072264481216550025343198689835357618681873598023026225266716067780e-127
mpmath (prec=1000)        = 2.56572850056105148291735639613047859001477095540203266250504462960653767360416188079136395575326953119218247602307727367985551096000368640359367812179070686479198046287233104280204937504901221620134046153583613193738177820412122516350777255525035947116513676784199592200655526485894447669230515221776e-127
Timings at prec=53:
    GSL:  625 loops, best of 3: 971 µs per loop
    mpmath:  25 loops, best of 3: 26.9 ms per loop

# f = sqrt(1-x^2) on [0, 1]
sage: num_int_test(sqrt(1-x^2), 0, 1)
Exact                     = 1/4*pi
Exact .n()                = 0.785398163397448
GSL                       = 0.785398167726
mpmath                    = 0.785398163397448
mpmath (prec=53)          = 0.785398163397448
mpmath (prec=64)          = 0.785398163397448310
mpmath (prec=100)         = 0.78539816339744830961566084582
mpmath (prec=200)         = 0.78539816339744830961566084581987572104929234984377645524374
mpmath (prec=500)         = 0.785398163397448309615660845819875721049292349843776455243736148076954101571552249657008706335529266995537021628320576661773461152387645557931339852032
mpmath (prec=1000)        = 0.785398163397448309615660845819875721049292349843776455243736148076954101571552249657008706335529266995537021628320576661773461152387645557931339852032120279362571025675484630276389911155737238732595491107202743916483361532118912058446695791317800477286412141730865087152613581662053348401815062285318
Timings at prec=53:
    GSL:  625 loops, best of 3: 652 µs per loop
    mpmath:  25 loops, best of 3: 12 ms per loop

# f = sin(sin(x)) on [0, 1]
sage: num_int_test(sin(sin(x)), 0, 1)
Exact                     = integrate(sin(sin(x)), x, 0, 1)
Exact .n()                = 0.430606103120691
GSL                       = 0.430606103121
mpmath                    = 0.430606103120691
mpmath (prec=53)          = 0.430606103120691
mpmath (prec=64)          = 0.430606103120690605
mpmath (prec=100)         = 0.43060610312069060491237735525
mpmath (prec=200)         = 0.43060610312069060491237735524846578643360804182199746950463
mpmath (prec=500)         = 0.430606103120690604912377355248465786433608041821997469504633350750892193636074792502000332212863495547968512886769444385260392350928954849458834511854
mpmath (prec=1000)        = 0.430606103120690604912377355248465786433608041821997469504633350750892193636074792502000332212863495547968512886769444385260392350928954849458834511854394326788473583253436780737313870079328121429092122005425057044706514198162061316772646582265252772251628205725432156943890956907988745419355505731945
Timings at prec=53:
    GSL:  625 loops, best of 3: 134 µs per loop
    mpmath:  25 loops, best of 3: 11.2 ms per loop
```


In the second example, GSL's answer compared to the numerically evaluated exact symbolic answer is significantly off. The mpmath answer at default precision matches the  numerically evaluated exact symbolic answer perfectly.

As for the timings, as you can see GSL is *much* faster than the patch code using mpmath. I tried using `fast_callable` in the case where the domain precision is the same as RDF and that gives a big speedup, though still not as fast as GSL:


```python
    def _evalf( ... ):
    ...
    
        try:
            precision = parent.prec()
            mpmath.mp.prec = precision
            if precision == RDF.precision():
                mp_f = fast_callable(f, vars=[x], domain=RDF)
            else:
                mp_f = lambda z: f(x = mpmath.mpmath_to_sage(z, precision))
        except AttributeError:
            mp_f = fast_callable(f, vars=[x], domain=RDF)
        
        return mpmath.call(mpmath.quad, mp_f, [a,b])
```


New timings using `fast_callable`:


```
# Testing: added fast_callable to _evalf_
# results: definite_integral( ... ) is around 5x faster when called at RDF precision

sage: timeit('numerical_integral(e^(-x^2)*log(x), 17, 42)') # base case using GSL at float precision
625 loops, best of 3: 959 µs per loop
sage: timeit('definite_integral(e^(-x^2)*log(x), x, 17, 42, hold=True).n()') # using fast_callable
125 loops, best of 3: 5.41 ms per loop
sage: timeit('definite_integral(e^(-x^2)*log(x), x, 17, 42, hold=True).n(53)') # using fast_callable
125 loops, best of 3: 5.41 ms per loop
sage: timeit('definite_integral(e^(-x^2)*log(x), x, 17, 42, hold=True).n(54)') # *not* using fast_callable
25 loops, best of 3: 28.1 ms per loop
sage: timeit('definite_integral(e^(-x^2)*log(x), x, 17, 42, hold=True).n(64)') # *not* using fast_callable
25 loops, best of 3: 26.3 ms per loop
sage: timeit('definite_integral(e^(-x^2)*log(x), x, 17, 42, hold=True).n(100)') # *not* using fast_callable
25 loops, best of 3: 32.2 ms per loop
```




---

archive/issue_comments_073838.json:
```json
{
    "body": "\n```\n# f = e^(-x^2)*log(x) on [17, 42]\nsage: num_int_test(e^(-x^2)*log(x), 17, 42)\nExact                     = integrate(e^(-x^2)*log(x), x, 17, 42)\nExact .n()                = 2.59225286296247e-127\nGSL                       = 2.5657285007e-127\nmpmath                    = 2.59225286296247e-127\n```\n\nGee, I don't like this at all.  So do you think this is a bug?  (And if so, in which program?)  GSL is pretty stable, though...\n\n```\n        try:\n            precision = parent.prec()\n            mpmath.mp.prec = precision\n            if precision == RDF.precision():\n                mp_f = fast_callable(f, vars=[x], domain=RDF)\n```\n\nWhat if we called GSL for precisely this use case, not `fast_callable`?  Also, what does Maxima (`.nintegrate()`) do?\n\nGood analysis!",
    "created_at": "2011-08-23T15:02:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73838",
    "user": "kcrisman"
}
```


```
# f = e^(-x^2)*log(x) on [17, 42]
sage: num_int_test(e^(-x^2)*log(x), 17, 42)
Exact                     = integrate(e^(-x^2)*log(x), x, 17, 42)
Exact .n()                = 2.59225286296247e-127
GSL                       = 2.5657285007e-127
mpmath                    = 2.59225286296247e-127
```

Gee, I don't like this at all.  So do you think this is a bug?  (And if so, in which program?)  GSL is pretty stable, though...

```
        try:
            precision = parent.prec()
            mpmath.mp.prec = precision
            if precision == RDF.precision():
                mp_f = fast_callable(f, vars=[x], domain=RDF)
```

What if we called GSL for precisely this use case, not `fast_callable`?  Also, what does Maxima (`.nintegrate()`) do?

Good analysis!



---

archive/issue_comments_073839.json:
```json
{
    "body": "Maybe GSL targets absolute rather than relative error? mpmath uses the absolute error (which is something of a bug), but gives an accurate relative value here more or less by accident.",
    "created_at": "2011-08-23T15:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73839",
    "user": "fredrik.johansson"
}
```

Maybe GSL targets absolute rather than relative error? mpmath uses the absolute error (which is something of a bug), but gives an accurate relative value here more or less by accident.



---

archive/issue_comments_073840.json:
```json
{
    "body": "Replying to [comment:32 kcrisman]:\n> Gee, I don't like this at all.  So do you think this is a bug?  (And if so, in which program?)  GSL is pretty stable, though...\n\nthe correct result is 2.56...e-127, i.e., GSL's result.\n\nPaul",
    "created_at": "2011-08-23T15:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73840",
    "user": "zimmerma"
}
```

Replying to [comment:32 kcrisman]:
> Gee, I don't like this at all.  So do you think this is a bug?  (And if so, in which program?)  GSL is pretty stable, though...

the correct result is 2.56...e-127, i.e., GSL's result.

Paul



---

archive/issue_comments_073841.json:
```json
{
    "body": "Replying to [comment:34 zimmerma]:\n> Replying to [comment:32 kcrisman]:\n> > Gee, I don't like this at all.  So do you think this is a bug?  (And if so, in which program?)  GSL is pretty stable, though...\n> \n> the correct result is 2.56...e-127, i.e., GSL's result.\n> \n> Paul\n\nOh, indeed it is. I was confused by the \"exact\" result. That makes more sense.",
    "created_at": "2011-08-23T15:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73841",
    "user": "fredrik.johansson"
}
```

Replying to [comment:34 zimmerma]:
> Replying to [comment:32 kcrisman]:
> > Gee, I don't like this at all.  So do you think this is a bug?  (And if so, in which program?)  GSL is pretty stable, though...
> 
> the correct result is 2.56...e-127, i.e., GSL's result.
> 
> Paul

Oh, indeed it is. I was confused by the "exact" result. That makes more sense.



---

archive/issue_comments_073842.json:
```json
{
    "body": "Obviously mpmath should support a relative tolerance out of the box, but there's a not-so-hackish workaround which Sage could use. The quadrature rules are implemented as classes, and can be subclassed:\n\n\n```\nfrom mpmath import *\nfrom mpmath.calculus.quadrature import TanhSinh, GaussLegendre\n\nclass RelativeErrorMixin(object):\n    def estimate_error(self, results, prec, epsilon):\n        mag = abs(results[-1])\n        if len(results) == 2:\n            return abs(results[0]-results[1]) / mag\n        try:\n            if results[-1] == results[-2] == results[-3]:\n                return self.ctx.zero\n            D1 = self.ctx.log(abs(results[-1]-results[-2])/mag, 10)\n            D2 = self.ctx.log(abs(results[-1]-results[-3])/mag, 10)\n            if D2 == 0:\n                D2 = self.ctx.inf\n            else:\n                D2 = self.ctx.one / D2\n        except ValueError:\n            return epsilon\n        D3 = -prec\n        D4 = min(0, max(D1**2 * D2, 2*D1, D3))\n        return self.ctx.mpf(10) ** int(D4)\n\nclass TanhSinhRel(RelativeErrorMixin, TanhSinh):\n    pass\n\nclass GaussLegendreRel(RelativeErrorMixin, GaussLegendre):\n    pass\n```\n\nWith this change:\n\n\n```\n>>> quad(lambda x: exp(-x**2)*log(x), [17,42], method=TanhSinhRel)\nmpf('2.5657285005610513e-127')\n>>> \n>>> quad(lambda x: exp(-x**2)*log(x), [17,42], method=GaussLegendreRel)\nmpf('2.5657285005610513e-127')\n```\n\nBTW, I think the class will be instantiated every time this way, so the __init__ method should be overwritten as well to create a singleton. Alternatively Sage could call the summation() method directly, which would remove some overhead.\n\nThe estimate_error method should be changed to something better and should be tested on many examples. The input \"results\" is a list of results generated at successive levels of refinement. The code above attempts to extrapolate the error estimate (in a rather convoluted way that should be fixed in mpmath :). One could be more conservative (and slower) by just comparing the two last results.",
    "created_at": "2011-08-23T15:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73842",
    "user": "fredrik.johansson"
}
```

Obviously mpmath should support a relative tolerance out of the box, but there's a not-so-hackish workaround which Sage could use. The quadrature rules are implemented as classes, and can be subclassed:


```
from mpmath import *
from mpmath.calculus.quadrature import TanhSinh, GaussLegendre

class RelativeErrorMixin(object):
    def estimate_error(self, results, prec, epsilon):
        mag = abs(results[-1])
        if len(results) == 2:
            return abs(results[0]-results[1]) / mag
        try:
            if results[-1] == results[-2] == results[-3]:
                return self.ctx.zero
            D1 = self.ctx.log(abs(results[-1]-results[-2])/mag, 10)
            D2 = self.ctx.log(abs(results[-1]-results[-3])/mag, 10)
            if D2 == 0:
                D2 = self.ctx.inf
            else:
                D2 = self.ctx.one / D2
        except ValueError:
            return epsilon
        D3 = -prec
        D4 = min(0, max(D1**2 * D2, 2*D1, D3))
        return self.ctx.mpf(10) ** int(D4)

class TanhSinhRel(RelativeErrorMixin, TanhSinh):
    pass

class GaussLegendreRel(RelativeErrorMixin, GaussLegendre):
    pass
```

With this change:


```
>>> quad(lambda x: exp(-x**2)*log(x), [17,42], method=TanhSinhRel)
mpf('2.5657285005610513e-127')
>>> 
>>> quad(lambda x: exp(-x**2)*log(x), [17,42], method=GaussLegendreRel)
mpf('2.5657285005610513e-127')
```

BTW, I think the class will be instantiated every time this way, so the __init__ method should be overwritten as well to create a singleton. Alternatively Sage could call the summation() method directly, which would remove some overhead.

The estimate_error method should be changed to something better and should be tested on many examples. The input "results" is a list of results generated at successive levels of refinement. The code above attempts to extrapolate the error estimate (in a rather convoluted way that should be fixed in mpmath :). One could be more conservative (and slower) by just comparing the two last results.



---

archive/issue_comments_073843.json:
```json
{
    "body": "Remove assignee burcin.",
    "created_at": "2011-08-23T15:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73843",
    "user": "fredrik.johansson"
}
```

Remove assignee burcin.



---

archive/issue_comments_073844.json:
```json
{
    "body": "I've run some more comparisons which include Burcin's relative error for mpmath's quad. Here are some results  for 6 test functions. The code that runs the tests is here:  https://gist.github.com/1166436\n\nIn the output below:\n- GSL means we call `numerical_integral`\n- mpmath means we call `mpmath.call(mpmath.quad, mp_f, [a, b])` for an appropriate function `mp_f`\n- mpmath_rel means we call `mpmath.call(mpmath.quad, mp_f, [a, b], method=GaussLegendreRel)` \n\nAll of the times are listed in seconds.\n\n\n```\n\nfunction: e^(-x^2)*log(x)  on  [17, 42]\nGSL:                      2.5657285007e-127                    time:  0.001216173172\nmpmath:                   2.59225286296247e-127                time:  0.0308299064636\nmpmath_rel (prec=64):     2.56572850056105156e-127             time:  0.7594602108\nmpmath_rel (prec=100):    2.5657285005610514829173563974e-127  time:  0.894016981125\n\nfunction: sqrt(-x^2 + 1)  on  [0, 1]\nGSL:                      0.785398167726                       time:  0.000615119934082\nmpmath:                   0.785398163397448                    time:  0.011482000351\nmpmath_rel (prec=64):     0.785398183809260289                 time:  0.50303196907\nmpmath_rel (prec=100):    0.78539818380926028913861331848      time:  0.57284116745\n\nfunction: sin(sin(x))  on  [0, 1]\nGSL:                      0.430606103121                       time:  0.00026798248291\nmpmath:                   0.430606103120691                    time:  0.0110800266266\nmpmath_rel (prec=64):     0.430606103120690605                 time:  0.00665020942688\nmpmath_rel (prec=100):    0.43060610312069060491237735525      time:  0.0202469825745\n\nfunction: max(sin(x), cos(x))  on  [0, pi]\nGSL:                      2.41421356237                        time:  0.012158870697\nmpmath:                   2.41413598800040                     time:  0.102693796158\nmpmath_rel (prec=64):     2.41424024561759656                  time:  0.514449834824\nmpmath_rel (prec=100):    2.4142402456175965601829446506       time:  0.583966970444\n\nfunction: e^cos(x)*sin(x)  on  [0, pi]\nGSL:                      2.35040238729                        time:  0.000401973724365\nmpmath:                   2.35040238728760                     time:  0.103391170502\nmpmath_rel (prec=64):     2.35040238728760291                  time:  0.0510699748993\nmpmath_rel (prec=100):    2.3504023872876029137647637012       time:  0.132436037064\n\nfunction: e^(-x^100)  on  [0, 1.1]\nGSL:                      0.994325851192                       time:  0.000550031661987\nmpmath:                   0.994325851192472                    time:  0.390738010406\nmpmath_rel (prec=64):     0.994325851192555258                 time:  0.75753903389\nmpmath_rel (prec=100):    0.99432585119255525754634686152      time:  0.875532865524\n```\n\n\nIt looks like mpmath is now just as accurate as GSL but the times are obviously a lot longer. I agree with `@`kcrisman 's suggestion for calling GSL when the precision is default (float or RDF or 53 bits?) and calling mpmath with relative errors when the precision is higher. Perhaps adding the mpmath relative errors should be on a different ticket which this one will depend on?",
    "created_at": "2011-08-23T20:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73844",
    "user": "benjaminfjones"
}
```

I've run some more comparisons which include Burcin's relative error for mpmath's quad. Here are some results  for 6 test functions. The code that runs the tests is here:  https://gist.github.com/1166436

In the output below:
- GSL means we call `numerical_integral`
- mpmath means we call `mpmath.call(mpmath.quad, mp_f, [a, b])` for an appropriate function `mp_f`
- mpmath_rel means we call `mpmath.call(mpmath.quad, mp_f, [a, b], method=GaussLegendreRel)` 

All of the times are listed in seconds.


```

function: e^(-x^2)*log(x)  on  [17, 42]
GSL:                      2.5657285007e-127                    time:  0.001216173172
mpmath:                   2.59225286296247e-127                time:  0.0308299064636
mpmath_rel (prec=64):     2.56572850056105156e-127             time:  0.7594602108
mpmath_rel (prec=100):    2.5657285005610514829173563974e-127  time:  0.894016981125

function: sqrt(-x^2 + 1)  on  [0, 1]
GSL:                      0.785398167726                       time:  0.000615119934082
mpmath:                   0.785398163397448                    time:  0.011482000351
mpmath_rel (prec=64):     0.785398183809260289                 time:  0.50303196907
mpmath_rel (prec=100):    0.78539818380926028913861331848      time:  0.57284116745

function: sin(sin(x))  on  [0, 1]
GSL:                      0.430606103121                       time:  0.00026798248291
mpmath:                   0.430606103120691                    time:  0.0110800266266
mpmath_rel (prec=64):     0.430606103120690605                 time:  0.00665020942688
mpmath_rel (prec=100):    0.43060610312069060491237735525      time:  0.0202469825745

function: max(sin(x), cos(x))  on  [0, pi]
GSL:                      2.41421356237                        time:  0.012158870697
mpmath:                   2.41413598800040                     time:  0.102693796158
mpmath_rel (prec=64):     2.41424024561759656                  time:  0.514449834824
mpmath_rel (prec=100):    2.4142402456175965601829446506       time:  0.583966970444

function: e^cos(x)*sin(x)  on  [0, pi]
GSL:                      2.35040238729                        time:  0.000401973724365
mpmath:                   2.35040238728760                     time:  0.103391170502
mpmath_rel (prec=64):     2.35040238728760291                  time:  0.0510699748993
mpmath_rel (prec=100):    2.3504023872876029137647637012       time:  0.132436037064

function: e^(-x^100)  on  [0, 1.1]
GSL:                      0.994325851192                       time:  0.000550031661987
mpmath:                   0.994325851192472                    time:  0.390738010406
mpmath_rel (prec=64):     0.994325851192555258                 time:  0.75753903389
mpmath_rel (prec=100):    0.99432585119255525754634686152      time:  0.875532865524
```


It looks like mpmath is now just as accurate as GSL but the times are obviously a lot longer. I agree with `@`kcrisman 's suggestion for calling GSL when the precision is default (float or RDF or 53 bits?) and calling mpmath with relative errors when the precision is higher. Perhaps adding the mpmath relative errors should be on a different ticket which this one will depend on?



---

archive/issue_comments_073845.json:
```json
{
    "body": "The singleton trick definitely needs to be implemented; it can save a factor 4x or more.\n\nThen there is the question of whether to use GaussLegendreRel or TanhSinhRel by default. Gauss-Legendre is somewhat faster for smooth integrands; Tanh-Sinh is much better for something like `sqrt(-x^2 + 1)` on `[0,1]` (note that the values with mpmath_rel above are wrong!) or almost anything on an infinite interval (this should be tested as well!). I would favor TanhSinhRel.\n\nAnyway, I agree that it would be sensible to use GSL by default.",
    "created_at": "2011-08-23T21:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73845",
    "user": "fredrik.johansson"
}
```

The singleton trick definitely needs to be implemented; it can save a factor 4x or more.

Then there is the question of whether to use GaussLegendreRel or TanhSinhRel by default. Gauss-Legendre is somewhat faster for smooth integrands; Tanh-Sinh is much better for something like `sqrt(-x^2 + 1)` on `[0,1]` (note that the values with mpmath_rel above are wrong!) or almost anything on an infinite interval (this should be tested as well!). I would favor TanhSinhRel.

Anyway, I agree that it would be sensible to use GSL by default.



---

archive/issue_comments_073846.json:
```json
{
    "body": "Replying to [comment:38 fredrik.johansson]:\n> The singleton trick definitely needs to be implemented; it can save a factor 4x or more.\n\nI understand what you are saying about the class being instantiated on every call. Can you explain what you mean by the \"singleton trick\"?\n\n> Then there is the question of whether to use GaussLegendreRel or TanhSinhRel by default. Gauss-Legendre is somewhat faster for smooth integrands; Tanh-Sinh is much better for something like `sqrt(-x^2 + 1)` on `[0,1]` (note that the values with mpmath_rel above are wrong!) or almost anything on an infinite interval (this should be tested as well!). I would favor TanhSinhRel.\n> \n> Anyway, I agree that it would be sensible to use GSL by default.\n\nFor `mp_f = sqrt(1-x**2)`, here is what TanhSinhRel gives in comparison with GaussLengendreRel and with absolute errors, as well as the approx. of the exact answer pi/4:\n\n\n```\nsage: mp_f = lambda z: f(x = mpmath.mpmath_to_sage(z, 53))\nsage: mpmath.call(mpmath.quad, mp_f, [a, b])\n0.785398163397448\nsage: mpmath.call(mpmath.quad, mp_f, [a, b], method=GaussLegendreRel)\n0.785398325435763\nsage: mpmath.call(mpmath.quad, mp_f, [a, b], method=TanhSinhRel)\n0.785398163397448\nsage: N(pi/4)\n0.785398163397448\n```\n\n\nps. somehow I read your second to last comment (about the relative error) and thought it was written by Burcin (hence my reference to his name in my reply). Sorry :)",
    "created_at": "2011-08-23T21:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73846",
    "user": "benjaminfjones"
}
```

Replying to [comment:38 fredrik.johansson]:
> The singleton trick definitely needs to be implemented; it can save a factor 4x or more.

I understand what you are saying about the class being instantiated on every call. Can you explain what you mean by the "singleton trick"?

> Then there is the question of whether to use GaussLegendreRel or TanhSinhRel by default. Gauss-Legendre is somewhat faster for smooth integrands; Tanh-Sinh is much better for something like `sqrt(-x^2 + 1)` on `[0,1]` (note that the values with mpmath_rel above are wrong!) or almost anything on an infinite interval (this should be tested as well!). I would favor TanhSinhRel.
> 
> Anyway, I agree that it would be sensible to use GSL by default.

For `mp_f = sqrt(1-x**2)`, here is what TanhSinhRel gives in comparison with GaussLengendreRel and with absolute errors, as well as the approx. of the exact answer pi/4:


```
sage: mp_f = lambda z: f(x = mpmath.mpmath_to_sage(z, 53))
sage: mpmath.call(mpmath.quad, mp_f, [a, b])
0.785398163397448
sage: mpmath.call(mpmath.quad, mp_f, [a, b], method=GaussLegendreRel)
0.785398325435763
sage: mpmath.call(mpmath.quad, mp_f, [a, b], method=TanhSinhRel)
0.785398163397448
sage: N(pi/4)
0.785398163397448
```


ps. somehow I read your second to last comment (about the relative error) and thought it was written by Burcin (hence my reference to his name in my reply). Sorry :)



---

archive/issue_comments_073847.json:
```json
{
    "body": "Replying to [comment:39 benjaminfjones]:\n> Replying to [comment:38 fredrik.johansson]:\n> > The singleton trick definitely needs to be implemented; it can save a factor 4x or more.\n> \n> I understand what you are saying about the class being instantiated on every call. Can you explain what you mean by the \"singleton trick\"?\n\nTo make a class singleton, add something like this (warning: untested):\n\n\n```\n    instance = None\n    def __new__(cls, *args, **kwargs):\n        if not cls.instance:\n            cls.instance = super(ThisClass, cls).__new__(cls, *args, **kwargs)\n        return cls.instance\n```\n",
    "created_at": "2011-08-23T21:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73847",
    "user": "fredrik.johansson"
}
```

Replying to [comment:39 benjaminfjones]:
> Replying to [comment:38 fredrik.johansson]:
> > The singleton trick definitely needs to be implemented; it can save a factor 4x or more.
> 
> I understand what you are saying about the class being instantiated on every call. Can you explain what you mean by the "singleton trick"?

To make a class singleton, add something like this (warning: untested):


```
    instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(ThisClass, cls).__new__(cls, *args, **kwargs)
        return cls.instance
```




---

archive/issue_comments_073848.json:
```json
{
    "body": "I tried making TanhSinhRel the default and including the singleton `__new__` code you gave. Here is the resulting class definition:\n\n\n```python\nclass TanhSinhRel(TanhSinh):\n    instance = None\n    def __new__(cls, *args, **kwds):\n        if not cls.instance:\n            cls.instance = super(TanhSinhRel, cls).__new__(cls, *args, **kwds)\n        return cls.instance\n        \n    def estimate_error(self, results, prec, epsilon):\n        mag = abs(results[-1])\n        if len(results) == 2:\n            return abs(results[0]-results[1]) / mag\n        try:\n            if results[-1] == results[-2] == results[-3]:\n                return self.ctx.zero\n            D1 = self.ctx.log(abs(results[-1]-results[-2])/mag, 10)\n            D2 = self.ctx.log(abs(results[-1]-results[-3])/mag, 10)\n            if D2 == 0:\n                D2 = self.ctx.inf\n            else:\n                D2 = self.ctx.one / D2\n        except ValueError:\n            return epsilon\n        D3 = -prec\n        D4 = min(0, max(D1**2 * D2, 2*D1, D3))\n        return self.ctx.mpf(10) ** int(D4)\n```\n\n\nI couldn't see a timing difference by adding that code to TanhSinhRel (but maybe this isn't the right place to add it?). Also, I get a deprecation warning about arguments passed to `__new__`\n\nHere are two tests in a row, one shows the deprecation warning, the second doesn't:\n\n```\nsage: num_int_test_v2(e**(-x**2)*log(x), 17, 42)\nGSL:                      2.5657285007e-127                    time:  0.0059130191803\nmpmath:                   2.59225286296247e-127                time:  0.0680160522461\n/Users/jonesbe/sage/latest/local/bin/sage-ipython:66: DeprecationWarning: object.__new__() takes no parameters\nmpmath_rel_tanh (prec=64): 2.56572850056105156e-127             time:  0.310777187347\nmpmath_rel_tanh (prec=100): 2.5657285005610514829173563973e-127  time:  0.541303157806\n```\n\n\nand again in the same session to check if timings have improved:\n\n```\nsage: num_int_test_v2(e**(-x**2)*log(x), 17, 42)\nGSL:                      2.5657285007e-127                    time:  0.00131511688232\nmpmath:                   2.59225286296247e-127                time:  0.0299959182739\nmpmath_rel_tanh (prec=64): 2.56572850056105156e-127             time:  0.211745023727\nmpmath_rel_tanh (prec=100): 2.5657285005610514829173563973e-127  time:  0.513824939728\n```\n\n\nThe timings do improve after the first call which includes `method=TanhSinhRel`, but not dramatically. Am I missing something?",
    "created_at": "2011-08-24T18:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73848",
    "user": "benjaminfjones"
}
```

I tried making TanhSinhRel the default and including the singleton `__new__` code you gave. Here is the resulting class definition:


```python
class TanhSinhRel(TanhSinh):
    instance = None
    def __new__(cls, *args, **kwds):
        if not cls.instance:
            cls.instance = super(TanhSinhRel, cls).__new__(cls, *args, **kwds)
        return cls.instance
        
    def estimate_error(self, results, prec, epsilon):
        mag = abs(results[-1])
        if len(results) == 2:
            return abs(results[0]-results[1]) / mag
        try:
            if results[-1] == results[-2] == results[-3]:
                return self.ctx.zero
            D1 = self.ctx.log(abs(results[-1]-results[-2])/mag, 10)
            D2 = self.ctx.log(abs(results[-1]-results[-3])/mag, 10)
            if D2 == 0:
                D2 = self.ctx.inf
            else:
                D2 = self.ctx.one / D2
        except ValueError:
            return epsilon
        D3 = -prec
        D4 = min(0, max(D1**2 * D2, 2*D1, D3))
        return self.ctx.mpf(10) ** int(D4)
```


I couldn't see a timing difference by adding that code to TanhSinhRel (but maybe this isn't the right place to add it?). Also, I get a deprecation warning about arguments passed to `__new__`

Here are two tests in a row, one shows the deprecation warning, the second doesn't:

```
sage: num_int_test_v2(e**(-x**2)*log(x), 17, 42)
GSL:                      2.5657285007e-127                    time:  0.0059130191803
mpmath:                   2.59225286296247e-127                time:  0.0680160522461
/Users/jonesbe/sage/latest/local/bin/sage-ipython:66: DeprecationWarning: object.__new__() takes no parameters
mpmath_rel_tanh (prec=64): 2.56572850056105156e-127             time:  0.310777187347
mpmath_rel_tanh (prec=100): 2.5657285005610514829173563973e-127  time:  0.541303157806
```


and again in the same session to check if timings have improved:

```
sage: num_int_test_v2(e**(-x**2)*log(x), 17, 42)
GSL:                      2.5657285007e-127                    time:  0.00131511688232
mpmath:                   2.59225286296247e-127                time:  0.0299959182739
mpmath_rel_tanh (prec=64): 2.56572850056105156e-127             time:  0.211745023727
mpmath_rel_tanh (prec=100): 2.5657285005610514829173563973e-127  time:  0.513824939728
```


The timings do improve after the first call which includes `method=TanhSinhRel`, but not dramatically. Am I missing something?



---

archive/issue_comments_073849.json:
```json
{
    "body": "Ugh, I should clearly have tested this feature properly in mpmath. The problem is that the `__init__` method clears the caches. This definitely needs to be changed in mpmath. Anyway, a workaround is to move the initialization to the `__new__` method, like this:\n\n\n```\n    def __new__(cls):\n        if not cls.instance:\n            cls.instance = object.__new__(cls)\n            cls.instance.standard_cache = {}\n            cls.instance.transformed_cache = {}\n            cls.instance.interval_count = {}\n        return cls.instance\n    def __init__(self, ctx):\n        self.ctx = ctx\n```\n\nThis ought to work. The speedup of doing this should be greater for GaussLegendre than for TanhSinh, since the node generation is more expensive for the former.\n\nSome further speedup would be possible by overriding the transform_nodes and sum_next methods so that Sage numbers are used most of the time. This way most of the calls to sage_to_mpmath and mpmath_to_sage could be avoided when an interval is reused.\n\ntransform_nodes would just have to be replaced by a simple wrapper function that takes the output (a list of pairs of numbers) from the transform_nodes method of the parent class and converts it to Sage numbers.\n\nsum_next computes the sum over `weight[i]*f(node[i])`. This is trivial and could just be changed to a simple loop to work optimally with Sage numbers. (Only the return value needs to be converted back to an mpmath number).\n\nThis should all just require a few lines of code. One just needs to be careful to get the precision right in the conversions, and to support both real and complex numbers. Unless someone else is extremely eager to implement this, I could look at this tomorrow.",
    "created_at": "2011-08-24T19:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73849",
    "user": "fredrik.johansson"
}
```

Ugh, I should clearly have tested this feature properly in mpmath. The problem is that the `__init__` method clears the caches. This definitely needs to be changed in mpmath. Anyway, a workaround is to move the initialization to the `__new__` method, like this:


```
    def __new__(cls):
        if not cls.instance:
            cls.instance = object.__new__(cls)
            cls.instance.standard_cache = {}
            cls.instance.transformed_cache = {}
            cls.instance.interval_count = {}
        return cls.instance
    def __init__(self, ctx):
        self.ctx = ctx
```

This ought to work. The speedup of doing this should be greater for GaussLegendre than for TanhSinh, since the node generation is more expensive for the former.

Some further speedup would be possible by overriding the transform_nodes and sum_next methods so that Sage numbers are used most of the time. This way most of the calls to sage_to_mpmath and mpmath_to_sage could be avoided when an interval is reused.

transform_nodes would just have to be replaced by a simple wrapper function that takes the output (a list of pairs of numbers) from the transform_nodes method of the parent class and converts it to Sage numbers.

sum_next computes the sum over `weight[i]*f(node[i])`. This is trivial and could just be changed to a simple loop to work optimally with Sage numbers. (Only the return value needs to be converted back to an mpmath number).

This should all just require a few lines of code. One just needs to be careful to get the precision right in the conversions, and to support both real and complex numbers. Unless someone else is extremely eager to implement this, I could look at this tomorrow.



---

archive/issue_comments_073850.json:
```json
{
    "body": "Sorry, make that\n\n\n```\n    def __new__(cls, ctx):\n        if not cls.instance:\n            cls.instance = object.__new__(cls)\n            cls.instance.ctx = ctx\n            cls.instance.standard_cache = {}\n            cls.instance.transformed_cache = {}\n            cls.instance.interval_count = {}\n        return cls.instance\n    def __init__(self, ctx):\n        pass\n```\n",
    "created_at": "2011-08-24T19:29:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73850",
    "user": "fredrik.johansson"
}
```

Sorry, make that


```
    def __new__(cls, ctx):
        if not cls.instance:
            cls.instance = object.__new__(cls)
            cls.instance.ctx = ctx
            cls.instance.standard_cache = {}
            cls.instance.transformed_cache = {}
            cls.instance.interval_count = {}
        return cls.instance
    def __init__(self, ctx):
        pass
```




---

archive/issue_comments_073851.json:
```json
{
    "body": "Changing keywords from \"numerics,integration\" to \"numerics,integration, sd32\".",
    "created_at": "2011-08-24T23:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73851",
    "user": "was"
}
```

Changing keywords from "numerics,integration" to "numerics,integration, sd32".



---

archive/issue_comments_073852.json:
```json
{
    "body": "OK, here's a version also avoiding type conversions:\n\n\n```\nfrom mpmath.calculus.quadrature import TanhSinh\nfrom mpmath import quad, mp\nfrom sage.libs.mpmath.all import call, sage_to_mpmath, mpmath_to_sage\n\nclass TanhSinhRel(TanhSinh):\n    instance = None\n\n    def __new__(cls, ctx):\n        if not cls.instance:\n            cls.instance = object.__new__(cls)\n            cls.instance.ctx = ctx\n            cls.instance.standard_cache = {}\n            cls.instance.transformed_cache = {}\n            cls.instance.interval_count = {}\n        return cls.instance\n\n    def estimate_error(self, results, prec, epsilon):\n        mag = abs(results[-1])\n        if len(results) == 2:\n            return abs(results[0]-results[1]) / mag\n        try:\n            if results[-1] == results[-2] == results[-3]:\n                return self.ctx.zero\n            D1 = self.ctx.log(abs(results[-1]-results[-2])/mag, 10)\n            D2 = self.ctx.log(abs(results[-1]-results[-3])/mag, 10)\n            if D2 == 0:\n                D2 = self.ctx.inf\n            else:\n                D2 = self.ctx.one / D2\n        except ValueError:\n            print factorial(1000000)\n            return epsilon\n        D3 = -prec\n        D4 = min(0, max(D1**2 * D2, 2*D1, D3))\n        return self.ctx.mpf(10) ** int(D4)\n\nclass TanhSinhRel2(TanhSinhRel):\n    instance = None\n\n    def __init__(self, ctx):\n        pass\n\n\nclass TanhSinhRel3(TanhSinhRel2):\n    instance = None\n\n    def transform_nodes(self, nodes, a, b, verbose=False):\n        nodes = TanhSinh.transform_nodes(self, nodes, a, b, verbose)\n        prec = self.ctx.prec\n        nodes = [(mpmath_to_sage(x, prec), mpmath_to_sage(w, prec)) for (x, w) in nodes]\n        return nodes\n\n    def sum_next(self, f, nodes, degree, prec, previous, verbose=False):\n        h = self.ctx.mpf(2)**(-degree)\n        if previous:\n            S = previous[-1]/(h*2)\n        else:\n            S = self.ctx.zero\n        s = 0\n        for (x, w) in nodes:\n            s += w * f(x)\n        return h * (S + sage_to_mpmath(s, prec))\n\ndef f(x):\n    return exp(-x**2) * log(x)\n\ndef g(x):\n    x = mpmath_to_sage(x, mp.prec)\n    y = exp(-x**2) * log(x)\n    return sage_to_mpmath(y, mp.prec)\n\nmp.prec = 100\n\ntimeit(\"mp.quad(g, [17, 42], method=TanhSinhRel)\")\ntimeit(\"mp.quad(g, [17, 42], method=TanhSinhRel2)\")\ntimeit(\"mp.quad(f, [17, 42], method=TanhSinhRel3)\")\n\nprint mp.quad(g, [17, 42], method=TanhSinhRel)\nprint mp.quad(g, [17, 42], method=TanhSinhRel2)\nprint mp.quad(f, [17, 42], method=TanhSinhRel3)\n```\n\nThis prints:\n\n\n```\n5 loops, best of 3: 82.1 ms per loop\n5 loops, best of 3: 72.5 ms per loop\n5 loops, best of 3: 38.2 ms per loop\n2.5657285005610514829173563961e-127\n2.5657285005610514829173563961e-127\n2.5657285005610514829173563961e-127\n```\n\nThe estimate_error method still needs some work, though...",
    "created_at": "2011-08-25T17:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73852",
    "user": "fredrik.johansson"
}
```

OK, here's a version also avoiding type conversions:


```
from mpmath.calculus.quadrature import TanhSinh
from mpmath import quad, mp
from sage.libs.mpmath.all import call, sage_to_mpmath, mpmath_to_sage

class TanhSinhRel(TanhSinh):
    instance = None

    def __new__(cls, ctx):
        if not cls.instance:
            cls.instance = object.__new__(cls)
            cls.instance.ctx = ctx
            cls.instance.standard_cache = {}
            cls.instance.transformed_cache = {}
            cls.instance.interval_count = {}
        return cls.instance

    def estimate_error(self, results, prec, epsilon):
        mag = abs(results[-1])
        if len(results) == 2:
            return abs(results[0]-results[1]) / mag
        try:
            if results[-1] == results[-2] == results[-3]:
                return self.ctx.zero
            D1 = self.ctx.log(abs(results[-1]-results[-2])/mag, 10)
            D2 = self.ctx.log(abs(results[-1]-results[-3])/mag, 10)
            if D2 == 0:
                D2 = self.ctx.inf
            else:
                D2 = self.ctx.one / D2
        except ValueError:
            print factorial(1000000)
            return epsilon
        D3 = -prec
        D4 = min(0, max(D1**2 * D2, 2*D1, D3))
        return self.ctx.mpf(10) ** int(D4)

class TanhSinhRel2(TanhSinhRel):
    instance = None

    def __init__(self, ctx):
        pass


class TanhSinhRel3(TanhSinhRel2):
    instance = None

    def transform_nodes(self, nodes, a, b, verbose=False):
        nodes = TanhSinh.transform_nodes(self, nodes, a, b, verbose)
        prec = self.ctx.prec
        nodes = [(mpmath_to_sage(x, prec), mpmath_to_sage(w, prec)) for (x, w) in nodes]
        return nodes

    def sum_next(self, f, nodes, degree, prec, previous, verbose=False):
        h = self.ctx.mpf(2)**(-degree)
        if previous:
            S = previous[-1]/(h*2)
        else:
            S = self.ctx.zero
        s = 0
        for (x, w) in nodes:
            s += w * f(x)
        return h * (S + sage_to_mpmath(s, prec))

def f(x):
    return exp(-x**2) * log(x)

def g(x):
    x = mpmath_to_sage(x, mp.prec)
    y = exp(-x**2) * log(x)
    return sage_to_mpmath(y, mp.prec)

mp.prec = 100

timeit("mp.quad(g, [17, 42], method=TanhSinhRel)")
timeit("mp.quad(g, [17, 42], method=TanhSinhRel2)")
timeit("mp.quad(f, [17, 42], method=TanhSinhRel3)")

print mp.quad(g, [17, 42], method=TanhSinhRel)
print mp.quad(g, [17, 42], method=TanhSinhRel2)
print mp.quad(f, [17, 42], method=TanhSinhRel3)
```

This prints:


```
5 loops, best of 3: 82.1 ms per loop
5 loops, best of 3: 72.5 ms per loop
5 loops, best of 3: 38.2 ms per loop
2.5657285005610514829173563961e-127
2.5657285005610514829173563961e-127
2.5657285005610514829173563961e-127
```

The estimate_error method still needs some work, though...



---

archive/issue_comments_073853.json:
```json
{
    "body": "It turns out that the current top-level function, numerical_integral, isn't even in the reference manual. See #11916. I don't think this is addressed here yet, though if it eventually is then that ticket would be closed as a dup.",
    "created_at": "2011-10-12T12:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73853",
    "user": "kcrisman"
}
```

It turns out that the current top-level function, numerical_integral, isn't even in the reference manual. See #11916. I don't think this is addressed here yet, though if it eventually is then that ticket would be closed as a dup.



---

archive/issue_comments_073854.json:
```json
{
    "body": "Just FYI - the Maxima list has a similar discussion going on right now, starting [here](http://www.math.utexas.edu/pipermail/maxima/2011/026230.html) in the archives.  We should continue to allow access to their methods as optional, of course :)",
    "created_at": "2011-10-13T13:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73854",
    "user": "kcrisman"
}
```

Just FYI - the Maxima list has a similar discussion going on right now, starting [here](http://www.math.utexas.edu/pipermail/maxima/2011/026230.html) in the archives.  We should continue to allow access to their methods as optional, of course :)



---

archive/issue_comments_073855.json:
```json
{
    "body": "Replying to [comment:47 kcrisman]:\n> Just FYI - the Maxima list has a similar discussion going on right now, starting [here](http://www.math.utexas.edu/pipermail/maxima/2011/026230.html) in the archives.  We should continue to allow access to their methods as optional, of course :)\nI especially like this quote.  I think it is a better way forward than trying to guess what the user needs - maybe just allowing many options is better.\n\n```\nIn my opinion, an interface simplifying the use of packages like QUADPACK\nshould not attempt to guess which method is more appropriate for a given\nproblem. This should be left to the user. Otherwise we are going to have an\n\"all-purpose\" Maxima function supposed to do everything, like Mathematica's\nfunction \"NIntegrate\", which, however, not only fails to do what is supposed\nto do in many cases, but also encourages the \"blind use\" of Numerical\nAnalysis. There is no \"perfect\" numerical method, able to solve any problem\nefficiently; this is true for any numerical problem, such as numerical\nquadrature, solution of initial or boundary value problems etc.\nTwo simple examples:\n(1) consider integrating a \"sawtooth\" function. Romberg integration, which\nis generally very fast and accurate for smooth functions would have a hard\ntime integrating a sawtooth function, while a simple trapezoidal method\nwould be much faster in that particular case.\n(2) Most people use \"natural\" cubic splines for interpolation, just because\nof their name I guess, or maybe because Computer Algebra Systems use natural\ncubic splines by default for interpolation. However, \"natural\" splines are\nnot natural at all, and should be used only if there is a reason to assume\nsecond derivative is zero at the end points of the interpolation interval.\nOtherwise, \"not-a-knot\" splines should be used instead.\n\nI doubt there is a way to make a function which automatically selects the\nbest method to solve a numerical problem. Mathematica tries that and the\nresult is disappointing. I am very suspicious about such attempts, and I\nbelieve none should trust them, no matter how sophisticated they are.\nEveryone who needs to use numerical methods should have a basic knowledge of\nwhat (s)he is doing, and should be able to pick the numerical method most\nappropriate method for a given problem.\n```\n",
    "created_at": "2011-10-14T15:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73855",
    "user": "kcrisman"
}
```

Replying to [comment:47 kcrisman]:
> Just FYI - the Maxima list has a similar discussion going on right now, starting [here](http://www.math.utexas.edu/pipermail/maxima/2011/026230.html) in the archives.  We should continue to allow access to their methods as optional, of course :)
I especially like this quote.  I think it is a better way forward than trying to guess what the user needs - maybe just allowing many options is better.

```
In my opinion, an interface simplifying the use of packages like QUADPACK
should not attempt to guess which method is more appropriate for a given
problem. This should be left to the user. Otherwise we are going to have an
"all-purpose" Maxima function supposed to do everything, like Mathematica's
function "NIntegrate", which, however, not only fails to do what is supposed
to do in many cases, but also encourages the "blind use" of Numerical
Analysis. There is no "perfect" numerical method, able to solve any problem
efficiently; this is true for any numerical problem, such as numerical
quadrature, solution of initial or boundary value problems etc.
Two simple examples:
(1) consider integrating a "sawtooth" function. Romberg integration, which
is generally very fast and accurate for smooth functions would have a hard
time integrating a sawtooth function, while a simple trapezoidal method
would be much faster in that particular case.
(2) Most people use "natural" cubic splines for interpolation, just because
of their name I guess, or maybe because Computer Algebra Systems use natural
cubic splines by default for interpolation. However, "natural" splines are
not natural at all, and should be used only if there is a reason to assume
second derivative is zero at the end points of the interpolation interval.
Otherwise, "not-a-knot" splines should be used instead.

I doubt there is a way to make a function which automatically selects the
best method to solve a numerical problem. Mathematica tries that and the
result is disappointing. I am very suspicious about such attempts, and I
believe none should trust them, no matter how sophisticated they are.
Everyone who needs to use numerical methods should have a basic knowledge of
what (s)he is doing, and should be able to pick the numerical method most
appropriate method for a given problem.
```




---

archive/issue_comments_073856.json:
```json
{
    "body": "Replying to [comment:1 zimmerma]:\n> I don't know why it does not work from Sage:\n> {{{\n> sage: gp.intnum(x=1,2,sin(x)/x^2)\n> ------------------------------------------------------------\n>    File \"<ipython console>\", line 1\n> SyntaxError: non-keyword arg after keyword arg (<ipython console>, line 1)\n> }}}\nIt does not work for two reasons:\n- `gp.intnum` does not accept python keyword arguments (it would be very painful and error prone to transform that to the appropriate string input to `gp`\n- formula transformation to gp is very limited:\n\n```\nsage: gp(sin(x)/x^2)\nx^-1 - 1/6*x + 1/120*x^3 - 1/5040*x^5 + 1/362880*x^7 - 1/39916800*x^9 + 1/6227020800*x^11 - 1/1307674368000*x^13 + O(x^15)\n```\n\nThe latter point seems the most fundamental to me. For arbitrary precision numerical integration, GP/PARI is probably our best bet, though, and it seems that the PARI C api should be quite usable, because the integrand gets passed as a black box function. From [PARI handbook](http://pari.math.u-bordeaux.fr/dochtml/html.stable/Sums,_products,_integrals_and_similar_functions.html), we get the signature:\n\n```\nintnum(void *E, GEN (*eval)(void*,GEN), GEN a,GEN b,GEN tab, long prec)\n```\n\nso as long as we can provide a way to evaluate our integrand (say) `f` at a value `x` with precision `prec`, we can wrap that up into a C function that takes a `GEN`, converts it to `x`, evaluates `f` there and converts the result to a `GEN` and passes it back. We could pass a pointer to that function in as `eval` and then everything should work.\n\nPari's high precision numerical integration is supposed to be of quite high quality.\n\nThis approach would be much easier than trying to symbolically translate any arbitrary Sage symbolic expression to GP (plus more general, because we would be able to use any python callable, provided we find a way to provide the desired precision)",
    "created_at": "2012-04-18T19:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73856",
    "user": "nbruin"
}
```

Replying to [comment:1 zimmerma]:
> I don't know why it does not work from Sage:
> {{{
> sage: gp.intnum(x=1,2,sin(x)/x^2)
> ------------------------------------------------------------
>    File "<ipython console>", line 1
> SyntaxError: non-keyword arg after keyword arg (<ipython console>, line 1)
> }}}
It does not work for two reasons:
- `gp.intnum` does not accept python keyword arguments (it would be very painful and error prone to transform that to the appropriate string input to `gp`
- formula transformation to gp is very limited:

```
sage: gp(sin(x)/x^2)
x^-1 - 1/6*x + 1/120*x^3 - 1/5040*x^5 + 1/362880*x^7 - 1/39916800*x^9 + 1/6227020800*x^11 - 1/1307674368000*x^13 + O(x^15)
```

The latter point seems the most fundamental to me. For arbitrary precision numerical integration, GP/PARI is probably our best bet, though, and it seems that the PARI C api should be quite usable, because the integrand gets passed as a black box function. From [PARI handbook](http://pari.math.u-bordeaux.fr/dochtml/html.stable/Sums,_products,_integrals_and_similar_functions.html), we get the signature:

```
intnum(void *E, GEN (*eval)(void*,GEN), GEN a,GEN b,GEN tab, long prec)
```

so as long as we can provide a way to evaluate our integrand (say) `f` at a value `x` with precision `prec`, we can wrap that up into a C function that takes a `GEN`, converts it to `x`, evaluates `f` there and converts the result to a `GEN` and passes it back. We could pass a pointer to that function in as `eval` and then everything should work.

Pari's high precision numerical integration is supposed to be of quite high quality.

This approach would be much easier than trying to symbolically translate any arbitrary Sage symbolic expression to GP (plus more general, because we would be able to use any python callable, provided we find a way to provide the desired precision)



---

archive/issue_comments_073857.json:
```json
{
    "body": "Sage 4.8 can now integrate the formula in this ticket, thus I propose to change it to:\n\n```\nsage: h = integral(sin(sin(x)), (x, 1, 2)); h\nintegrate(sin(sin(x)), x, 1, 2)\nsage: h.n()\n0.81644995512331231\nsage: h.n(digits=14)\n0.81644995512331231\nsage: h.n(digits=600)\n0.81644995512331231\nsage: h.n(digits=600) == h.n(digits=14)\nTrue\nsage: h.n(prec=50) == h.n(prec=1000)\nTrue\n```\n\nPaul",
    "created_at": "2012-04-19T12:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73857",
    "user": "zimmerma"
}
```

Sage 4.8 can now integrate the formula in this ticket, thus I propose to change it to:

```
sage: h = integral(sin(sin(x)), (x, 1, 2)); h
integrate(sin(sin(x)), x, 1, 2)
sage: h.n()
0.81644995512331231
sage: h.n(digits=14)
0.81644995512331231
sage: h.n(digits=600)
0.81644995512331231
sage: h.n(digits=600) == h.n(digits=14)
True
sage: h.n(prec=50) == h.n(prec=1000)
True
```

Paul



---

archive/issue_comments_073858.json:
```json
{
    "body": "Replying to [comment:51 zimmerma]:\n> Sage 4.8 can now integrate the formula in this ticket\nYou are right that for this ticket, the original example doesn't test generic numerical integration. The numerical approximation of the resulting expressions in gamma functions seems suspect, though:\n\n```\nsage: h = integral(sin(x)/x^2, (x, 1, pi/2));\nsage: H1=h.n(digits=20)\nsage: H2=h.n(digits=100)\nsage: delta=parent(H2)(H1)-H2\nsage: delta\n0\nsage: parent(delta)\nComplex Field with 336 bits of precision\nsage: H2.imag_part()\n5.421010862427522170037264004349708557128906250000000000000000000000000000000000000000000000000000000e-20\n```\n\nAlso note that the equality tests as stated in the examples are not direct evidence that something is going wrong:\n\n```\nsage: a=RealField(10)(1)\nsage: b=RealField(20)(1)+RealField(20)(2)^(-14)\nsage: a,b\n(1.0, 1.0001)\nsage: a == b\nTrue\n```\n\nI guess the numbers are coerced into the parent with least precision before being compared ...",
    "created_at": "2012-04-19T17:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73858",
    "user": "nbruin"
}
```

Replying to [comment:51 zimmerma]:
> Sage 4.8 can now integrate the formula in this ticket
You are right that for this ticket, the original example doesn't test generic numerical integration. The numerical approximation of the resulting expressions in gamma functions seems suspect, though:

```
sage: h = integral(sin(x)/x^2, (x, 1, pi/2));
sage: H1=h.n(digits=20)
sage: H2=h.n(digits=100)
sage: delta=parent(H2)(H1)-H2
sage: delta
0
sage: parent(delta)
Complex Field with 336 bits of precision
sage: H2.imag_part()
5.421010862427522170037264004349708557128906250000000000000000000000000000000000000000000000000000000e-20
```

Also note that the equality tests as stated in the examples are not direct evidence that something is going wrong:

```
sage: a=RealField(10)(1)
sage: b=RealField(20)(1)+RealField(20)(2)^(-14)
sage: a,b
(1.0, 1.0001)
sage: a == b
True
```

I guess the numbers are coerced into the parent with least precision before being compared ...



---

archive/issue_comments_073859.json:
```json
{
    "body": "is there current interest in adding the functionality of this ticket? \n\ni read through the benchmarks in this thread, but on the other hand i didn't understand what is the proposed way to plug this into sage. how about the following: does it make sense to have the numerical integration algorithms to be called via a new keyword argument in `numerical_integral` ? that would use the current default GSL, the one from PARI, and the one from mpmath.",
    "created_at": "2017-06-03T15:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73859",
    "user": "mforets"
}
```

is there current interest in adding the functionality of this ticket? 

i read through the benchmarks in this thread, but on the other hand i didn't understand what is the proposed way to plug this into sage. how about the following: does it make sense to have the numerical integration algorithms to be called via a new keyword argument in `numerical_integral` ? that would use the current default GSL, the one from PARI, and the one from mpmath.



---

archive/issue_comments_073860.json:
```json
{
    "body": "for reference one will find on https://members.loria.fr/PZimmermann/sagebook/english.html a translation into english of the book \"Calcul mathematique avec Sage\", which was also updated to Sage 7.6. Chapter 14 discusses numerical integration, in particular with arbitrary precision. (We have also added a section about multiple integrals.)",
    "created_at": "2017-06-06T12:12:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8321#issuecomment-73860",
    "user": "zimmerma"
}
```

for reference one will find on https://members.loria.fr/PZimmermann/sagebook/english.html a translation into english of the book "Calcul mathematique avec Sage", which was also updated to Sage 7.6. Chapter 14 discusses numerical integration, in particular with arbitrary precision. (We have also added a section about multiple integrals.)
