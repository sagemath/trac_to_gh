# Issue 5556: symbolic gamma function and symbolic log function are incoherent

archive/issues_005556.json:
```json
{
    "body": "CC:  @burcin @robertwb\n\nKeywords: symbolic gamma log function numerical approximation\n\nSo this is incredibly awful:\n\n\n```\nsage: gamma(RealField(100)(3/4))\n1.2254167024651776451290983034\nsage: gamma(3/4).n(100)\n1.2254167024651776429777783051\n```\n\n\n(for the record, the first one is correct)\n\nand this doesn't agree with that:\n\n\n```\nsage: log(2).n(100)\n0.69314718055994530941723212146\nsage: log(RealField(2))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/ncalexan/Devel/RiemannTheta/riemann_theta.py in <module>()\n\n/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in log(x, base)\n   9242             return x.log()\n   9243         except AttributeError: \n-> 9244             return ln(x)\n   9245     else:\n   9246         try:\n\n/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in ln(x)\n   9189         0.693147180559945\n   9190     \"\"\"\n-> 9191     return function_log(x)\n   9192 \n   9193 def log(x, base=None):\n\n/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in __call__(self, x, *args)\n   7542             return getattr(x, self._repr_())(*args)\n   7543         except AttributeError:\n-> 7544             return SymbolicComposition(self, SR(x))\n   7545 \n   7546     def _approx_(self, x):  # must *always* be called with a float x as input.\n\n/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in __call__(self, x)\n    504                 msg, s, pos = err.args\n    505                 raise TypeError, \"%s: %s !!! %s\" % (msg, s[:pos], s[pos:])\n--> 506         return self._coerce_impl(x)\n    507 \n    508     def _coerce_impl(self, x):\n\n/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in _coerce_impl(self, x)\n    566             return self(x._sage_())\n    567         else:\n--> 568             raise TypeError, \"cannot coerce type '%s' into a SymbolicExpression.\"%type(x)\n    569 \n    570     def _repr_(self):\n\nTypeError: cannot coerce type '<type 'sage.rings.real_mpfr.RealField'>' into a SymbolicExpression.\nsage: log(RealField(2))\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5556\n\n",
    "created_at": "2009-03-18T05:54:30Z",
    "labels": [
        "component: symbolics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "symbolic gamma function and symbolic log function are incoherent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5556",
    "user": "https://github.com/ncalexan"
}
```
CC:  @burcin @robertwb

Keywords: symbolic gamma log function numerical approximation

So this is incredibly awful:


```
sage: gamma(RealField(100)(3/4))
1.2254167024651776451290983034
sage: gamma(3/4).n(100)
1.2254167024651776429777783051
```


(for the record, the first one is correct)

and this doesn't agree with that:


```
sage: log(2).n(100)
0.69314718055994530941723212146
sage: log(RealField(2))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/Devel/RiemannTheta/riemann_theta.py in <module>()

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in log(x, base)
   9242             return x.log()
   9243         except AttributeError: 
-> 9244             return ln(x)
   9245     else:
   9246         try:

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in ln(x)
   9189         0.693147180559945
   9190     """
-> 9191     return function_log(x)
   9192 
   9193 def log(x, base=None):

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in __call__(self, x, *args)
   7542             return getattr(x, self._repr_())(*args)
   7543         except AttributeError:
-> 7544             return SymbolicComposition(self, SR(x))
   7545 
   7546     def _approx_(self, x):  # must *always* be called with a float x as input.

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in __call__(self, x)
    504                 msg, s, pos = err.args
    505                 raise TypeError, "%s: %s !!! %s" % (msg, s[:pos], s[pos:])
--> 506         return self._coerce_impl(x)
    507 
    508     def _coerce_impl(self, x):

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in _coerce_impl(self, x)
    566             return self(x._sage_())
    567         else:
--> 568             raise TypeError, "cannot coerce type '%s' into a SymbolicExpression."%type(x)
    569 
    570     def _repr_(self):

TypeError: cannot coerce type '<type 'sage.rings.real_mpfr.RealField'>' into a SymbolicExpression.
sage: log(RealField(2))
```


Issue created by migration from https://trac.sagemath.org/ticket/5556





---

archive/issue_comments_043148.json:
```json
{
    "body": "I just realized I goofed, I meant:\n\n\n```\nsage: log(2).n(100)\n0.69314718055994530941723212146\nsage: log(RealField(100)(2))\n0.69314718055994530941723212146\n```\n\n\nwhich works as expected.  But the symbolic gamma function is still wrong, and egregiously wrong at that!",
    "created_at": "2009-03-18T05:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5556#issuecomment-43148",
    "user": "https://github.com/ncalexan"
}
```

I just realized I goofed, I meant:


```
sage: log(2).n(100)
0.69314718055994530941723212146
sage: log(RealField(100)(2))
0.69314718055994530941723212146
```


which works as expected.  But the symbolic gamma function is still wrong, and egregiously wrong at that!



---

archive/issue_comments_043149.json:
```json
{
    "body": "The problem is that gamma(3/4) is automatically evaluated to precision 53, and then doing n(100) has only meaningless effect.  I don't know what happened between the original filing of this ticket and the Pynac update, but now Pynac automatically evaluates these.  See [http://groups.google.com/group/sage-devel/browse_thread/thread/f43fa9c900d06efd](http://groups.google.com/group/sage-devel/browse_thread/thread/f43fa9c900d06efd)",
    "created_at": "2009-09-29T16:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5556#issuecomment-43149",
    "user": "https://github.com/kcrisman"
}
```

The problem is that gamma(3/4) is automatically evaluated to precision 53, and then doing n(100) has only meaningless effect.  I don't know what happened between the original filing of this ticket and the Pynac update, but now Pynac automatically evaluates these.  See [http://groups.google.com/group/sage-devel/browse_thread/thread/f43fa9c900d06efd](http://groups.google.com/group/sage-devel/browse_thread/thread/f43fa9c900d06efd)



---

archive/issue_comments_043150.json:
```json
{
    "body": "Actually, belay that.  There are a few such functions out there.  E.g., \n\n```\nsage: sin(SR(3/4))\nsin(3/4)\nsage: sin(3/4)\nsin(3/4)\nsage: gamma(SR(3/4))\ngamma(3/4)\nsage: gamma(3/4)\n1.22541670246518\nsage: zeta(SR(3/4))\nzeta(3/4)\nsage: zeta(3/4)\n-3.44128538694522\n```\n\nSo the problem lies in gamma itself (and friends).  Most likely fix at this point is adding a prec keyword, as in sqrt.",
    "created_at": "2009-09-30T14:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5556#issuecomment-43150",
    "user": "https://github.com/kcrisman"
}
```

Actually, belay that.  There are a few such functions out there.  E.g., 

```
sage: sin(SR(3/4))
sin(3/4)
sage: sin(3/4)
sin(3/4)
sage: gamma(SR(3/4))
gamma(3/4)
sage: gamma(3/4)
1.22541670246518
sage: zeta(SR(3/4))
zeta(3/4)
sage: zeta(3/4)
-3.44128538694522
```

So the problem lies in gamma itself (and friends).  Most likely fix at this point is adding a prec keyword, as in sqrt.



---

archive/issue_comments_043151.json:
```json
{
    "body": "This should fix all such things, with the change that rationals now default to symbolic output.  The sage-devel discussion above didn't seem to think this was a problem, so hopefully it won't be, as one can still use prec or .n() to get exact values when the input isn't a multiple of 1/2.\n\nNote that this patch also fixes a NASTY hang error with negative integer CDF input into gamma.",
    "created_at": "2009-09-30T17:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5556#issuecomment-43151",
    "user": "https://github.com/kcrisman"
}
```

This should fix all such things, with the change that rationals now default to symbolic output.  The sage-devel discussion above didn't seem to think this was a problem, so hopefully it won't be, as one can still use prec or .n() to get exact values when the input isn't a multiple of 1/2.

Note that this patch also fixes a NASTY hang error with negative integer CDF input into gamma.



---

archive/issue_comments_043152.json:
```json
{
    "body": "Attachment [trac_5556-gamma-fix.patch](tarball://root/attachments/some-uuid/ticket5556/trac_5556-gamma-fix.patch) by @kcrisman created at 2009-09-30 17:00:51\n\nBased on 4.1.2.alpha4",
    "created_at": "2009-09-30T17:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5556#issuecomment-43152",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_5556-gamma-fix.patch](tarball://root/attachments/some-uuid/ticket5556/trac_5556-gamma-fix.patch) by @kcrisman created at 2009-09-30 17:00:51

Based on 4.1.2.alpha4



---

archive/issue_comments_043153.json:
```json
{
    "body": "Attachment [trac_5556-reviewer.patch](tarball://root/attachments/some-uuid/ticket5556/trac_5556-reviewer.patch) by @mwhansen created at 2009-10-05 06:00:15",
    "created_at": "2009-10-05T06:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5556#issuecomment-43153",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5556-reviewer.patch](tarball://root/attachments/some-uuid/ticket5556/trac_5556-reviewer.patch) by @mwhansen created at 2009-10-05 06:00:15



---

archive/issue_comments_043154.json:
```json
{
    "body": "Looks good to me.  \n\nI added a small little patch which cleans up the docstrings a little bit.  kcrisman, can you just go over them?",
    "created_at": "2009-10-05T06:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5556#issuecomment-43154",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  

I added a small little patch which cleans up the docstrings a little bit.  kcrisman, can you just go over them?



---

archive/issue_comments_043155.json:
```json
{
    "body": "Yup, those are all good changes.  I never know exactly how many characters are okay for the width of docstrings; it varies wildly by file, so I go short to be safe.  Also good eye with the n-1.",
    "created_at": "2009-10-05T13:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5556#issuecomment-43155",
    "user": "https://github.com/kcrisman"
}
```

Yup, those are all good changes.  I never know exactly how many characters are okay for the width of docstrings; it varies wildly by file, so I go short to be safe.  Also good eye with the n-1.



---

archive/issue_comments_043156.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T05:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5556#issuecomment-43156",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
