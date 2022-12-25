# Issue 9240: applying full_simplify() to gamma functions causes an error

archive/issues_009240.json:
```json
{
    "body": "Assignee: tomc\n\nCC:  @kcrisman\n\nKeywords: gamma function, full_simplify, factorial\n\nApplying full_simplify() to the gamma function sometimes causes an error.  This example works:\n\n```\nsage: gamma(4/3).full_simplify()\n1/3*gamma(1/3)\n```\n\nbut this example does not:\n\n```\nsage: gamma(1/3).full_simplify()\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1254, 0))\n\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/Users/tomc/sage-4.4.1/<ipython console> in <module>()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.simplify_full (sage/symbolic/expression.cpp:21549)()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.simplify_factorial (sage/symbolic/expression.cpp:22240)()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4053)()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/interfaces/maxima.pyc in _symbolic_(self, R)\n   1810             sqrt(2)\n   1811         \"\"\"\n-> 1812         return R(self._sage_())\n   1813 \n   1814     def __complex__(self):\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/interfaces/maxima.pyc in _sage_(self)\n   1791         import sage.calculus.calculus as calculus\n   1792         return calculus.symbolic_expression_from_maxima_string(self.name(),\n-> 1793                 maxima=self.parent())\n   1794 \n   1795     def _symbolic_(self, R):\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/calculus/calculus.pyc in symbolic_expression_from_maxima_string(x, equals_sub, maxima)\n   1524         # evaluation of maxima code are assumed pre-simplified\n   1525         is_simplified = True\n-> 1526         return symbolic_expression_from_string(s, syms, accept_sequence=True)\n   1527     except SyntaxError:\n   1528         raise TypeError, \"unable to make sense of Maxima expression '%s' in Sage\"%s\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/calculus/calculus.pyc in symbolic_expression_from_string(s, syms, accept_sequence)\n   1692             global _augmented_syms\n   1693             _augmented_syms = syms\n-> 1694             return parse_func(s)\n   1695         finally:\n   1696             _augmented_syms = {}\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.parse_sequence (sage/misc/parser.c:3855)()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.parse_sequence (sage/misc/parser.c:3747)()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_sequence (sage/misc/parser.c:4376)()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_tuple (sage/misc/parser.c:5032)()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_eqn (sage/misc/parser.c:5145)()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_expr (sage/misc/parser.c:5465)()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_term (sage/misc/parser.c:5690)()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_factor (sage/misc/parser.c:6053)()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_power (sage/misc/parser.c:6264)()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/symbolic/function.so in sage.symbolic.function.GinacFunction.__call__ (sage/symbolic/function.cpp:6321)()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.factorial (sage/symbolic/expression.cpp:20595)()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/symbolic/pynac.so in sage.symbolic.pynac.py_factorial (sage/symbolic/pynac.cpp:9156)()\n\n/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/rings/arith.pyc in factorial(n, algorithm)\n    403     \"\"\"\n    404     if n < 0:\n--> 405         raise ValueError, \"factorial -- must be nonnegative\"\n    406     if algorithm == 'gmp':\n    407         return ZZ(n).factorial()\n\nValueError: factorial -- must be nonnegative\n```\n\nI am running Sage 4.4.1 on Mac OS X version 10.6 (Snow Leopard), built from source. But the second example also fails on Sage 4.3.5 on 64-bit Linux, built from source. Looking at the source code suggests that the second example will fail on all platforms.\n\nThe problem occurs because full_simplify() here runs the following commands in Maxima:\n\n```\n(%i1) minfactorial(factcomb(makefact(gamma(1/3))));\n                                       2\n(%o1)                               (- -)!\n                                       3\n```\n\nand then the Maxima interface converts this to Sage as factorial(-2/3).  This causes an error.  For Sage, factorial(x) is only defined if x is a non-negative integer, whereas for Maxima factorial(x) is equivalent to gamma(1+x) and so makes sense whenever x is not in {-1, -2, -3, ...}\n\nApply: trac_9240_full_simplify_gamma.patch, trac_9240-factorial_evaluation.patch\n\nIssue created by migration from https://trac.sagemath.org/ticket/9240\n\n",
    "closed_at": "2011-06-14T19:20:21Z",
    "created_at": "2010-06-15T03:24:18Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "applying full_simplify() to gamma functions causes an error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9240",
    "user": "https://trac.sagemath.org/admin/accounts/users/tomc"
}
```
Assignee: tomc

CC:  @kcrisman

Keywords: gamma function, full_simplify, factorial

Applying full_simplify() to the gamma function sometimes causes an error.  This example works:

```
sage: gamma(4/3).full_simplify()
1/3*gamma(1/3)
```

but this example does not:

```
sage: gamma(1/3).full_simplify()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1254, 0))

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/tomc/sage-4.4.1/<ipython console> in <module>()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.simplify_full (sage/symbolic/expression.cpp:21549)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.simplify_factorial (sage/symbolic/expression.cpp:22240)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6332)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4053)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/interfaces/maxima.pyc in _symbolic_(self, R)
   1810             sqrt(2)
   1811         """
-> 1812         return R(self._sage_())
   1813 
   1814     def __complex__(self):

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/interfaces/maxima.pyc in _sage_(self)
   1791         import sage.calculus.calculus as calculus
   1792         return calculus.symbolic_expression_from_maxima_string(self.name(),
-> 1793                 maxima=self.parent())
   1794 
   1795     def _symbolic_(self, R):

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/calculus/calculus.pyc in symbolic_expression_from_maxima_string(x, equals_sub, maxima)
   1524         # evaluation of maxima code are assumed pre-simplified
   1525         is_simplified = True
-> 1526         return symbolic_expression_from_string(s, syms, accept_sequence=True)
   1527     except SyntaxError:
   1528         raise TypeError, "unable to make sense of Maxima expression '%s' in Sage"%s

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/calculus/calculus.pyc in symbolic_expression_from_string(s, syms, accept_sequence)
   1692             global _augmented_syms
   1693             _augmented_syms = syms
-> 1694             return parse_func(s)
   1695         finally:
   1696             _augmented_syms = {}

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.parse_sequence (sage/misc/parser.c:3855)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.parse_sequence (sage/misc/parser.c:3747)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_sequence (sage/misc/parser.c:4376)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_tuple (sage/misc/parser.c:5032)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_eqn (sage/misc/parser.c:5145)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_expr (sage/misc/parser.c:5465)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_term (sage/misc/parser.c:5690)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_factor (sage/misc/parser.c:6053)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/misc/parser.so in sage.misc.parser.Parser.p_power (sage/misc/parser.c:6264)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/symbolic/function.so in sage.symbolic.function.GinacFunction.__call__ (sage/symbolic/function.cpp:6321)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.factorial (sage/symbolic/expression.cpp:20595)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/symbolic/pynac.so in sage.symbolic.pynac.py_factorial (sage/symbolic/pynac.cpp:9156)()

/Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/rings/arith.pyc in factorial(n, algorithm)
    403     """
    404     if n < 0:
--> 405         raise ValueError, "factorial -- must be nonnegative"
    406     if algorithm == 'gmp':
    407         return ZZ(n).factorial()

ValueError: factorial -- must be nonnegative
```

I am running Sage 4.4.1 on Mac OS X version 10.6 (Snow Leopard), built from source. But the second example also fails on Sage 4.3.5 on 64-bit Linux, built from source. Looking at the source code suggests that the second example will fail on all platforms.

The problem occurs because full_simplify() here runs the following commands in Maxima:

```
(%i1) minfactorial(factcomb(makefact(gamma(1/3))));
                                       2
(%o1)                               (- -)!
                                       3
```

and then the Maxima interface converts this to Sage as factorial(-2/3).  This causes an error.  For Sage, factorial(x) is only defined if x is a non-negative integer, whereas for Maxima factorial(x) is equivalent to gamma(1+x) and so makes sense whenever x is not in {-1, -2, -3, ...}

Apply: trac_9240_full_simplify_gamma.patch, trac_9240-factorial_evaluation.patch

Issue created by migration from https://trac.sagemath.org/ticket/9240





---

archive/issue_comments_086756.json:
```json
{
    "body": "Attachment [trac_9240_full_simplify_gamma.patch](tarball://root/attachments/some-uuid/ticket9240/trac_9240_full_simplify_gamma.patch) by tomc created at 2010-06-15 03:49:32\n\nbased on Sage 4.4.1",
    "created_at": "2010-06-15T03:49:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86756",
    "user": "https://trac.sagemath.org/admin/accounts/users/tomc"
}
```

Attachment [trac_9240_full_simplify_gamma.patch](tarball://root/attachments/some-uuid/ticket9240/trac_9240_full_simplify_gamma.patch) by tomc created at 2010-06-15 03:49:32

based on Sage 4.4.1



---

archive/issue_comments_086757.json:
```json
{
    "body": "The patch applies cleanly to 4.4.4.alpha0, fixes the problem and includes some nice tests. I would give this a positive review, except that I really don't know the Pynac integration code. \n\nOh, and you say \"For Sage, factorial(x) is only defined if x is a non-negative integer\", but (with a clean 4.4.4.alpha0), it's defined the same way as Maxima:\n\n```\nsage: factorial(5)\n120\nsage: factorial(1/2)\n1/2*sqrt(pi)\nsage: factorial(1/21)\ngamma(22/21)\n```",
    "created_at": "2010-06-15T05:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86757",
    "user": "https://github.com/dandrake"
}
```

The patch applies cleanly to 4.4.4.alpha0, fixes the problem and includes some nice tests. I would give this a positive review, except that I really don't know the Pynac integration code. 

Oh, and you say "For Sage, factorial(x) is only defined if x is a non-negative integer", but (with a clean 4.4.4.alpha0), it's defined the same way as Maxima:

```
sage: factorial(5)
120
sage: factorial(1/2)
1/2*sqrt(pi)
sage: factorial(1/21)
gamma(22/21)
```



---

archive/issue_comments_086758.json:
```json
{
    "body": "OK: I had misunderstood the docstring, which says:\n\n```\nsage: ? factorial\n\nString Form:    factorial\nNamespace:      Interactive\nFile:           /Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/functions/other.py\nDefinition:     factorial(self, *args, coerce=True, hold=False, dont_call_method_on_arg=False)\nDocstring:\n       Returns the factorial of n.\n    \n       INPUT:\n    \n       * ``n`` - an integer, or symbolic expression\n...\n```\n\nI suppose that non-integer numerical values (rational numbers, real numbers, etc) count as symbolic expressions here, as they can be canonically coerced into the symbolic ring.  But then there is definitely a bug in factorial(), because [in an unpatched version of Sage]:\n\n```\nsage: factorial(-1/2)\nERROR: An unexpected error occurred while tokenizing input\n...\nValueError: factorial -- must be nonnegative\n```\n\nThe patch fixes this.",
    "created_at": "2010-06-15T14:47:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86758",
    "user": "https://trac.sagemath.org/admin/accounts/users/tomc"
}
```

OK: I had misunderstood the docstring, which says:

```
sage: ? factorial

String Form:    factorial
Namespace:      Interactive
File:           /Users/tomc/sage-4.4.1/local/lib/python2.6/site-packages/sage/functions/other.py
Definition:     factorial(self, *args, coerce=True, hold=False, dont_call_method_on_arg=False)
Docstring:
       Returns the factorial of n.
    
       INPUT:
    
       * ``n`` - an integer, or symbolic expression
...
```

I suppose that non-integer numerical values (rational numbers, real numbers, etc) count as symbolic expressions here, as they can be canonically coerced into the symbolic ring.  But then there is definitely a bug in factorial(), because [in an unpatched version of Sage]:

```
sage: factorial(-1/2)
ERROR: An unexpected error occurred while tokenizing input
...
ValueError: factorial -- must be nonnegative
```

The patch fixes this.



---

archive/issue_comments_086759.json:
```json
{
    "body": "Replying to [comment:2 tomc]:\n> OK: I had misunderstood the docstring, \n\n\nWell, of course you misunderstood the docstring, since it's wrong, or at least misleading. I've opened #9248 to fix the docstring for factorial().",
    "created_at": "2010-06-16T01:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86759",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:2 tomc]:
> OK: I had misunderstood the docstring, 


Well, of course you misunderstood the docstring, since it's wrong, or at least misleading. I've opened #9248 to fix the docstring for factorial().



---

archive/issue_comments_086760.json:
```json
{
    "body": "See also [this thread](http://trac.sagemath.org/sage_trac/ticket/9240), where it came up again.",
    "created_at": "2010-12-02T02:26:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86760",
    "user": "https://github.com/kcrisman"
}
```

See also [this thread](http://trac.sagemath.org/sage_trac/ticket/9240), where it came up again.



---

archive/issue_events_022750.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2011-05-10T19:13:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "milestone": "sage-4.7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9240#event-22750"
}
```



---

archive/issue_comments_086761.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-05-10T19:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86761",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086762.json:
```json
{
    "body": "I suppose this needs review.",
    "created_at": "2011-05-10T19:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86762",
    "user": "https://github.com/burcin"
}
```

I suppose this needs review.



---

archive/issue_comments_086763.json:
```json
{
    "body": "For some reason, the patchbot isn't applying this patch, but it does apply cleanly and pass doctests in 4.7.rc1. (On 64-bit Ubuntu 10.10)\n\nLooking at it again, I might recommend that in the TESTS, the first few examples be moved, since they already work and aren't testing to see if the problem in this ticket has been fixed. Only the `full_simplify()` tests are, strictly speaking, relevant to this ticket.",
    "created_at": "2011-05-11T00:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86763",
    "user": "https://github.com/dandrake"
}
```

For some reason, the patchbot isn't applying this patch, but it does apply cleanly and pass doctests in 4.7.rc1. (On 64-bit Ubuntu 10.10)

Looking at it again, I might recommend that in the TESTS, the first few examples be moved, since they already work and aren't testing to see if the problem in this ticket has been fixed. Only the `full_simplify()` tests are, strictly speaking, relevant to this ticket.



---

archive/issue_comments_086764.json:
```json
{
    "body": "That's a good point, Dan.  It's not bad to add them, but they should be added to the doc for gamma.  A friendly reviewer patch from ddrake would probably be sufficient for this :)",
    "created_at": "2011-05-11T00:29:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86764",
    "user": "https://github.com/kcrisman"
}
```

That's a good point, Dan.  It's not bad to add them, but they should be added to the doc for gamma.  A friendly reviewer patch from ddrake would probably be sufficient for this :)



---

archive/issue_comments_086765.json:
```json
{
    "body": "apply after trac_9240_full_simplify_gamma.patch",
    "created_at": "2011-05-24T19:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86765",
    "user": "https://github.com/burcin"
}
```

apply after trac_9240_full_simplify_gamma.patch



---

archive/issue_comments_086766.json:
```json
{
    "body": "Attachment [trac_9240-factorial_evaluation.patch](tarball://root/attachments/some-uuid/ticket9240/trac_9240-factorial_evaluation.patch) by @burcin created at 2011-05-24 19:20:03\n\nattachment:trac_9240-factorial_evaluation.patch adds further doctests and fixes for the evaluation of factorials. It should be applied after attachment:trac_9240_full_simplify_gamma.patch.\n\nMy changes depend on a small patch to pynac, where I somehow used && instead of bitwise and. This patch can be obtained from: \n\nhttps://bitbucket.org/burcin/pynac-patches/src/c3c5b3b8b1eb/bitwise.patch\n\nThis ticket now depends on a new pynac release, which should be coming soon.",
    "created_at": "2011-05-24T19:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86766",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_9240-factorial_evaluation.patch](tarball://root/attachments/some-uuid/ticket9240/trac_9240-factorial_evaluation.patch) by @burcin created at 2011-05-24 19:20:03

attachment:trac_9240-factorial_evaluation.patch adds further doctests and fixes for the evaluation of factorials. It should be applied after attachment:trac_9240_full_simplify_gamma.patch.

My changes depend on a small patch to pynac, where I somehow used && instead of bitwise and. This patch can be obtained from: 

https://bitbucket.org/burcin/pynac-patches/src/c3c5b3b8b1eb/bitwise.patch

This ticket now depends on a new pynac release, which should be coming soon.



---

archive/issue_comments_086767.json:
```json
{
    "body": "Pynac package with the changes required by attachment:trac_9240-factorial_evaluation.patch is at #11415.",
    "created_at": "2011-05-31T15:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86767",
    "user": "https://github.com/burcin"
}
```

Pynac package with the changes required by attachment:trac_9240-factorial_evaluation.patch is at #11415.



---

archive/issue_comments_086768.json:
```json
{
    "body": "Can you explain why the change from && to & was necessary?  I don't know much CPP.   Would there be a difference between bitwise 'and' and 'and' when the outputs are boolean?  Or maybe they are not boolean.  \n\nThanks!",
    "created_at": "2011-06-08T22:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86768",
    "user": "https://github.com/kcrisman"
}
```

Can you explain why the change from && to & was necessary?  I don't know much CPP.   Would there be a difference between bitwise 'and' and 'and' when the outputs are boolean?  Or maybe they are not boolean.  

Thanks!



---

archive/issue_comments_086769.json:
```json
{
    "body": "Well I am not sure because I don't know the code well. But python_func is an unsigned and used to be a boolean according to comment in the code.\nWhat I think happens here is the code tries to match a precise type of python_func.\n0 is just a c++ function but different from 0 it is a python construct and it can take different value depending on the construct. So if I am not mistaken it is bitwise because we are trying to match the construct code. This can be seen in the follwing snippet from function.cpp\n\n```\nfunction_options& function_options::eval_func(PyObject* e)\n{\n        python_func |= eval_python_f;\n        eval_f = eval_funcp(e);\n        return *this;\n}\nfunction_options& function_options::evalf_func(PyObject* ef)\n{\n        python_func |= evalf_python_f;\n        evalf_f = evalf_funcp(ef);\n        return *this;\n}\nfunction_options& function_options::conjugate_func(PyObject* c)\n{\n        python_func |= conjugate_python_f;\n        conjugate_f = conjugate_funcp(c);\n        return *this;\n}\nfunction_options& function_options::real_part_func(PyObject* c)\n{\n        python_func |= real_part_python_f;\n        real_part_f = real_part_funcp(c);\n        return *this;\n}\nfunction_options& function_options::imag_part_func(PyObject* c)\n{\n        python_func |= imag_part_python_f;\n        imag_part_f = imag_part_funcp(c);\n        return *this;\n}\n\nfunction_options& function_options::derivative_func(PyObject* d)\n{\n        python_func |= derivative_python_f;\n        derivative_f = derivative_funcp(d);\n        return *this;\n}\nfunction_options& function_options::power_func(PyObject* d)\n{\n        python_func |= power_python_f;\n        power_f = power_funcp(d);\n        return *this;\n}\nfunction_options& function_options::series_func(PyObject* s)\n{\n        python_func |= series_python_f;\n        series_f = series_funcp(s);\n        return *this;\n}\n```\nNotice how they match the bitwise comparison later in the patched code?",
    "created_at": "2011-06-09T01:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86769",
    "user": "https://github.com/kiwifb"
}
```

Well I am not sure because I don't know the code well. But python_func is an unsigned and used to be a boolean according to comment in the code.
What I think happens here is the code tries to match a precise type of python_func.
0 is just a c++ function but different from 0 it is a python construct and it can take different value depending on the construct. So if I am not mistaken it is bitwise because we are trying to match the construct code. This can be seen in the follwing snippet from function.cpp

```
function_options& function_options::eval_func(PyObject* e)
{
        python_func |= eval_python_f;
        eval_f = eval_funcp(e);
        return *this;
}
function_options& function_options::evalf_func(PyObject* ef)
{
        python_func |= evalf_python_f;
        evalf_f = evalf_funcp(ef);
        return *this;
}
function_options& function_options::conjugate_func(PyObject* c)
{
        python_func |= conjugate_python_f;
        conjugate_f = conjugate_funcp(c);
        return *this;
}
function_options& function_options::real_part_func(PyObject* c)
{
        python_func |= real_part_python_f;
        real_part_f = real_part_funcp(c);
        return *this;
}
function_options& function_options::imag_part_func(PyObject* c)
{
        python_func |= imag_part_python_f;
        imag_part_f = imag_part_funcp(c);
        return *this;
}

function_options& function_options::derivative_func(PyObject* d)
{
        python_func |= derivative_python_f;
        derivative_f = derivative_funcp(d);
        return *this;
}
function_options& function_options::power_func(PyObject* d)
{
        python_func |= power_python_f;
        power_f = power_funcp(d);
        return *this;
}
function_options& function_options::series_func(PyObject* s)
{
        python_func |= series_python_f;
        series_f = series_funcp(s);
        return *this;
}
```
Notice how they match the bitwise comparison later in the patched code?



---

archive/issue_comments_086770.json:
```json
{
    "body": "Thanks, I think that helps a *little*.  I also found\n\n```\n    cdef _register_function(self):\n        # We don't need to add anything to GiNaC's function registry\n        # However, if any custom methods were provided in the python class,\n        # we should set the properties of the function_options object\n        # corresponding to this function\n        cdef GFunctionOpt opt = g_registered_functions().index(self._serial)\n\n        if hasattr(self, '_eval_'):\n            opt.eval_func(self)\n\n```\nwhich I knew about before.  \n\nI am going to have to write down **exactly** how all this works at Sage Days 31, because I do not want to be rediscovering this from scratch every time like I am now.\n\n---\n\nI have some more questions, presumably for Burcin.   I don't think they are big deals, but I don't feel comfortable giving positive review without knowing them.  Someone else who knows more might!\n\n* why the change from the 'billions of digits' error message to the symbolic answer?  This seems like a big change - someone might rely on that type of entry failing in number theory.  Note that the multifactorial still has the 'billions of digits' error message, incidentally.\n* what would the problem be if Ginac got symbolic answers back, if it didn't have anything for those before?  (Not criticizing, just not understanding.  I don't have a problem with them being numeric for ints and floats and longs.)\n* Why did you remove `opt.set_python_func() `?  I assume this has something to do with fbissey's comment.\n* Does `        return None ` just mean that Ginac will not try to evaluate things like `factorial(sqrt(2))` internally?\n\n---\n\nStatus:\n* Positive review on Tom's patch, from Dan Drake.\n* The log gamma stuff is fine.\n* Apparently Francois is happy with the && to & switch.  This is beyond me, though I don't see any problems with it.\n* The actual changes to and new factorial and gamma functions are fine.\n* Need answer to questions, or someone else to review those pieces in lieu of that.\n* Finally, the big question - WHY this change?  I can't find a single doctest that tells me what broke with Tom's patch but without Burcin's patch.  I feel there must be some very subtle Maxima output that could have come out incorrect, but I cannot find it.  All these doctests should have worked before (or were cdef functions so they couldn't be doctested).",
    "created_at": "2011-06-09T01:39:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86770",
    "user": "https://github.com/kcrisman"
}
```

Thanks, I think that helps a *little*.  I also found

```
    cdef _register_function(self):
        # We don't need to add anything to GiNaC's function registry
        # However, if any custom methods were provided in the python class,
        # we should set the properties of the function_options object
        # corresponding to this function
        cdef GFunctionOpt opt = g_registered_functions().index(self._serial)

        if hasattr(self, '_eval_'):
            opt.eval_func(self)

```
which I knew about before.  

I am going to have to write down **exactly** how all this works at Sage Days 31, because I do not want to be rediscovering this from scratch every time like I am now.

---

I have some more questions, presumably for Burcin.   I don't think they are big deals, but I don't feel comfortable giving positive review without knowing them.  Someone else who knows more might!

* why the change from the 'billions of digits' error message to the symbolic answer?  This seems like a big change - someone might rely on that type of entry failing in number theory.  Note that the multifactorial still has the 'billions of digits' error message, incidentally.
* what would the problem be if Ginac got symbolic answers back, if it didn't have anything for those before?  (Not criticizing, just not understanding.  I don't have a problem with them being numeric for ints and floats and longs.)
* Why did you remove `opt.set_python_func() `?  I assume this has something to do with fbissey's comment.
* Does `        return None ` just mean that Ginac will not try to evaluate things like `factorial(sqrt(2))` internally?

---

Status:
* Positive review on Tom's patch, from Dan Drake.
* The log gamma stuff is fine.
* Apparently Francois is happy with the && to & switch.  This is beyond me, though I don't see any problems with it.
* The actual changes to and new factorial and gamma functions are fine.
* Need answer to questions, or someone else to review those pieces in lieu of that.
* Finally, the big question - WHY this change?  I can't find a single doctest that tells me what broke with Tom's patch but without Burcin's patch.  I feel there must be some very subtle Maxima output that could have come out incorrect, but I cannot find it.  All these doctests should have worked before (or were cdef functions so they couldn't be doctested).



---

archive/issue_comments_086771.json:
```json
{
    "body": "Replying to [comment:12 kcrisman]:\n> Thanks, I think that helps a *little*.  I also found\n> \n> ```\n>     cdef _register_function(self):\n>         # We don't need to add anything to GiNaC's function registry\n>         # However, if any custom methods were provided in the python class,\n>         # we should set the properties of the function_options object\n>         # corresponding to this function\n>         cdef GFunctionOpt opt = g_registered_functions().index(self._serial)\n> \n>         if hasattr(self, '_eval_'):\n>             opt.eval_func(self)\n> \n> ```\n> which I knew about before.  \n\n\nFrancois is right. The `python_func` variable is a bitset, indexed by the values here:\n\nhttps://bitbucket.org/burcin/pynac/src/687b580c8c7c/ginac/function.h#cl-240\n\nIf the corresponding bit is on, then we call a python function.\n\nWhen I first implemented this, defining custom evaluation etc. methods in Python was an all or nothing matter. Then I realized that overriding some of these methods and using the others defined in C++ made sense. I switched to the bitset at that point. As the change with `&` and `&&` shows, that switch wasn't very successful.\n \n> I am going to have to write down **exactly** how all this works at Sage Days 31, because I do not want to be rediscovering this from scratch every time like I am now.\n\n\nMaybe we can add some documentation to the reference manual about the general design of symbolics and in particular how the functions work.\n\n---\n> \n> I have some more questions, presumably for Burcin.   I don't think they are big deals, but I don't feel comfortable giving positive review without knowing them.  Someone else who knows more might!\n> \n> * why the change from the 'billions of digits' error message to the symbolic answer?  This seems like a big change - someone might rely on that type of entry failing in number theory.  Note that the multifactorial still has the 'billions of digits' error message, incidentally.\n\n\nThe number theory people should use the functions from `sage.rings.arith`. In general, it's a bad idea to use the symbolics functions in library code unless you know what you're doing.\n\nSuppose you have the expression `factorial(big_number+1)/factorial(big_number)`. This would simplify to `big_number`. Telling people that they can't possibly work with numbers that big defeats the purpose of *symbolic computation*.\n\n>  * what would the problem be if Ginac got symbolic answers back, if it didn't have anything for those before?  (Not criticizing, just not understanding.  I don't have a problem with them being numeric for ints and floats and longs.)\n\n\nWe get problems like #9913. I was being cautious.\n\n>  * Why did you remove `opt.set_python_func() `?  I assume this has something to do with fbissey's comment.\n>  * Does `        return None ` just mean that Ginac will not try to evaluate things like `factorial(sqrt(2))` internally?\n\n\nYes. It's quite likely that this is not documented anywhere. :)\n\n---\n> \n> Status:\n> * Positive review on Tom's patch, from Dan Drake.\n> * The log gamma stuff is fine.\n> * Apparently Francois is happy with the && to & switch.  This is beyond me, though I don't see any problems with it.\n> * The actual changes to and new factorial and gamma functions are fine.\n> * Need answer to questions, or someone else to review those pieces in lieu of that.\n> * Finally, the big question - WHY this change?  I can't find a single doctest that tells me what broke with Tom's patch but without Burcin's patch.  I feel there must be some very subtle Maxima output that could have come out incorrect, but I cannot find it.  All these doctests should have worked before (or were cdef functions so they couldn't be doctested).\n\n\nTom's patch was great, it fixed the problem at hand. But when I first looked at it, I thought it needed more tests. Sitting down to write the tests, I found all kinds of problems, like the bitwise `&` issue and the big factorials raising an error. So I fixed those as well. Perhaps it was a mistake to tag these changes on this ticket, but here we are now.",
    "created_at": "2011-06-09T10:50:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86771",
    "user": "https://github.com/burcin"
}
```

Replying to [comment:12 kcrisman]:
> Thanks, I think that helps a *little*.  I also found
> 
> ```
>     cdef _register_function(self):
>         # We don't need to add anything to GiNaC's function registry
>         # However, if any custom methods were provided in the python class,
>         # we should set the properties of the function_options object
>         # corresponding to this function
>         cdef GFunctionOpt opt = g_registered_functions().index(self._serial)
> 
>         if hasattr(self, '_eval_'):
>             opt.eval_func(self)
> 
> ```
> which I knew about before.  


Francois is right. The `python_func` variable is a bitset, indexed by the values here:

https://bitbucket.org/burcin/pynac/src/687b580c8c7c/ginac/function.h#cl-240

If the corresponding bit is on, then we call a python function.

When I first implemented this, defining custom evaluation etc. methods in Python was an all or nothing matter. Then I realized that overriding some of these methods and using the others defined in C++ made sense. I switched to the bitset at that point. As the change with `&` and `&&` shows, that switch wasn't very successful.
 
> I am going to have to write down **exactly** how all this works at Sage Days 31, because I do not want to be rediscovering this from scratch every time like I am now.


Maybe we can add some documentation to the reference manual about the general design of symbolics and in particular how the functions work.

---
> 
> I have some more questions, presumably for Burcin.   I don't think they are big deals, but I don't feel comfortable giving positive review without knowing them.  Someone else who knows more might!
> 
> * why the change from the 'billions of digits' error message to the symbolic answer?  This seems like a big change - someone might rely on that type of entry failing in number theory.  Note that the multifactorial still has the 'billions of digits' error message, incidentally.


The number theory people should use the functions from `sage.rings.arith`. In general, it's a bad idea to use the symbolics functions in library code unless you know what you're doing.

Suppose you have the expression `factorial(big_number+1)/factorial(big_number)`. This would simplify to `big_number`. Telling people that they can't possibly work with numbers that big defeats the purpose of *symbolic computation*.

>  * what would the problem be if Ginac got symbolic answers back, if it didn't have anything for those before?  (Not criticizing, just not understanding.  I don't have a problem with them being numeric for ints and floats and longs.)


We get problems like #9913. I was being cautious.

>  * Why did you remove `opt.set_python_func() `?  I assume this has something to do with fbissey's comment.
>  * Does `        return None ` just mean that Ginac will not try to evaluate things like `factorial(sqrt(2))` internally?


Yes. It's quite likely that this is not documented anywhere. :)

---
> 
> Status:
> * Positive review on Tom's patch, from Dan Drake.
> * The log gamma stuff is fine.
> * Apparently Francois is happy with the && to & switch.  This is beyond me, though I don't see any problems with it.
> * The actual changes to and new factorial and gamma functions are fine.
> * Need answer to questions, or someone else to review those pieces in lieu of that.
> * Finally, the big question - WHY this change?  I can't find a single doctest that tells me what broke with Tom's patch but without Burcin's patch.  I feel there must be some very subtle Maxima output that could have come out incorrect, but I cannot find it.  All these doctests should have worked before (or were cdef functions so they couldn't be doctested).


Tom's patch was great, it fixed the problem at hand. But when I first looked at it, I thought it needed more tests. Sitting down to write the tests, I found all kinds of problems, like the bitwise `&` issue and the big factorials raising an error. So I fixed those as well. Perhaps it was a mistake to tag these changes on this ticket, but here we are now.



---

archive/issue_comments_086772.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-09T12:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86772",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086773.json:
```json
{
    "body": "> Francois is right. The `python_func` variable is a bitset, indexed by the values here:\n> \n> https://bitbucket.org/burcin/pynac/src/687b580c8c7c/ginac/function.h#cl-240\n> \n> If the corresponding bit is on, then we call a python function.\n\n\nOkay, I finally understand what is going on here.  I couldn't implement it myself, but it's just a [really space-saving way](http://www.cplusplus.com/reference/stl/bitset/) to keep track of booleans like this.  So it's just the way we tell Ginac that a custom `_eval_` method or whatever has been defined.  Good.\n\n> > I am going to have to write down **exactly** how all this works at Sage Days 31, because I do not want to be rediscovering this from scratch every time like I am now.\n\n> \n> Maybe we can add some documentation to the reference manual about the general design of symbolics and in particular how the functions work.\n\n\nAbsolutely - witness for instance #11143 where a new-ish developer has been stymied by this, though hopefully I was able to explain at least some of it to him.\n\n> The number theory people should use the functions from `sage.rings.arith`. In general, it's a bad idea to use the symbolics functions in library code unless you know what you're doing.\n\n\nYes, I agree, but sometimes the order of imports makes it hard to know which one is top-level.\n \n> Suppose you have the expression `factorial(big_number+1)/factorial(big_number)`. This would simplify to `big_number`. Telling people that they can't possibly work with numbers that big defeats the purpose of *symbolic computation*.\n\n\nGood point!\n\n> Yes. It's quite likely that this is not documented anywhere. :)\n  \nA good project as well.\n> >  * Finally, the big question - WHY this change?  I can't find a single doctest that tells me what broke with Tom's patch but \n \nSo you are saying this was just an overhaul, but there is no specific error we know of that the rest fixed, it was just needed.  \n\nGood enough for me!  Positive review.  Long doctests finished passing late last night :)",
    "created_at": "2011-06-09T12:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86773",
    "user": "https://github.com/kcrisman"
}
```

> Francois is right. The `python_func` variable is a bitset, indexed by the values here:
> 
> https://bitbucket.org/burcin/pynac/src/687b580c8c7c/ginac/function.h#cl-240
> 
> If the corresponding bit is on, then we call a python function.


Okay, I finally understand what is going on here.  I couldn't implement it myself, but it's just a [really space-saving way](http://www.cplusplus.com/reference/stl/bitset/) to keep track of booleans like this.  So it's just the way we tell Ginac that a custom `_eval_` method or whatever has been defined.  Good.

> > I am going to have to write down **exactly** how all this works at Sage Days 31, because I do not want to be rediscovering this from scratch every time like I am now.

> 
> Maybe we can add some documentation to the reference manual about the general design of symbolics and in particular how the functions work.


Absolutely - witness for instance #11143 where a new-ish developer has been stymied by this, though hopefully I was able to explain at least some of it to him.

> The number theory people should use the functions from `sage.rings.arith`. In general, it's a bad idea to use the symbolics functions in library code unless you know what you're doing.


Yes, I agree, but sometimes the order of imports makes it hard to know which one is top-level.
 
> Suppose you have the expression `factorial(big_number+1)/factorial(big_number)`. This would simplify to `big_number`. Telling people that they can't possibly work with numbers that big defeats the purpose of *symbolic computation*.


Good point!

> Yes. It's quite likely that this is not documented anywhere. :)
  
A good project as well.
> >  * Finally, the big question - WHY this change?  I can't find a single doctest that tells me what broke with Tom's patch but 
 
So you are saying this was just an overhaul, but there is no specific error we know of that the rest fixed, it was just needed.  

Good enough for me!  Positive review.  Long doctests finished passing late last night :)



---

archive/issue_comments_086774.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-06-14T19:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9240#issuecomment-86774",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_022751.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-06-14T19:20:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9240",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9240#event-22751"
}
```
