# Issue 7913: Warnings raised in Cython show wrong source line

archive/issues_007913.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @orlitzky\n\nKeywords: deprecation\n\n```\nsage: 5.is_prime_power(flag=1)  # defined in sage/rings/integer.pyx\n/usr/local/src/sage-config/local/lib/python2.7/site-packages/IPython/core/interactiveshell.py:2881: DeprecationWarning: the 'flag' argument to is_prime_power() is no longer used\nSee http://trac.sagemath.org/16878 for details.\n  exec(code_obj, self.user_global_ns, self.user_ns)\nTrue\n```\n\nThe line `exec(code_obj, self.user_global_ns, self.user_ns)` is not very useful.\n\nThis is because Cython functions do not add a new stack level.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7913\n\n",
    "closed_at": "2017-07-13T07:54:31Z",
    "created_at": "2010-01-12T20:28:38Z",
    "labels": [
        "component: cython",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Warnings raised in Cython show wrong source line",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7913",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

CC:  @orlitzky

Keywords: deprecation

```
sage: 5.is_prime_power(flag=1)  # defined in sage/rings/integer.pyx
/usr/local/src/sage-config/local/lib/python2.7/site-packages/IPython/core/interactiveshell.py:2881: DeprecationWarning: the 'flag' argument to is_prime_power() is no longer used
See http://trac.sagemath.org/16878 for details.
  exec(code_obj, self.user_global_ns, self.user_ns)
True
```

The line `exec(code_obj, self.user_global_ns, self.user_ns)` is not very useful.

This is because Cython functions do not add a new stack level.

Issue created by migration from https://trac.sagemath.org/ticket/7913





---

archive/issue_comments_068723.json:
```json
{
    "body": "This looks like a stacklevel mismatch between python and cython code. Some other examples in pure python:\n\n```\nsage: numerical_sqrt(3)\n/home/mjo/src/sage-5.0.beta1/local/bin/sage-ipython:1: DeprecationWarning: numerical_sqrt is deprecated, use sqrt(x, prec=n) instead\n  #!/usr/bin/env python\nsqrt(3)\n```\n\n```\nsage: Polyhedron(vertices=[[0]]).union( Polyhedron(vertices=[[1]]) )\n/home/mjo/src/sage-5.0.beta1/local/bin/sage-ipython:1: DeprecationWarning: (Since Sage Version 4.4.4) The function union is replaced by convex_hull.\n  #!/usr/bin/env python\nA 1-dimensional polyhedron in QQ^1 defined as the convex hull of 2 vertices.\n```\n\nIf we pick something in a `*.pyx` file,\n\n```\nsage: p = m.copy()\n/home/mjo/src/sage-5.0.beta1/local/lib/python2.7/site-packages/IPython/iplib.py:2260: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)\n  exec code_obj in self.user_global_ns, self.user_ns\n```\n\n```\nsage: x.lgamma()\n/home/mjo/src/sage-5.0.beta1/local/lib/python2.7/site-packages/IPython/iplib.py:2260: DeprecationWarning: The lgamma() function is deprecated. Use log_gamma() instead.\n  exec code_obj in self.user_global_ns, self.user_ns\nlog_gamma(x)\n```\n\n\n(notice the iplib.py/sage-ipython difference). In a python file, the stacklevel of EllipticCurve seems to be correct while the one for e.g. lgamma() is off by one. Here's a test.py file:\n\n```\nfrom sage.all import *\n\nprint \"Calling EllipticCurve...\"\nEllipticCurve(ZZ(1))\n\nprint \"\\nCalling x.lgamma()\"\nvar('x').lgamma()\n```\n\nAnd running it:\n\n```\n$ sage test.py \nCalling EllipticCurve...\ntest.py:4: DeprecationWarning: 'EllipticCurve(j)' is deprecated; use 'EllipticCurve_from_j(j)' or 'EllipticCurve(j=j)' instead.\n  EllipticCurve(ZZ(1))\n\nCalling x.lgamma()\nsys:1: DeprecationWarning: The lgamma() function is deprecated. Use log_gamma() instead.\n```\n\nAdjusting the stacklevel fixes one, but breaks the other.",
    "created_at": "2012-01-23T00:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68723",
    "user": "https://github.com/orlitzky"
}
```

This looks like a stacklevel mismatch between python and cython code. Some other examples in pure python:

```
sage: numerical_sqrt(3)
/home/mjo/src/sage-5.0.beta1/local/bin/sage-ipython:1: DeprecationWarning: numerical_sqrt is deprecated, use sqrt(x, prec=n) instead
  #!/usr/bin/env python
sqrt(3)
```

```
sage: Polyhedron(vertices=[[0]]).union( Polyhedron(vertices=[[1]]) )
/home/mjo/src/sage-5.0.beta1/local/bin/sage-ipython:1: DeprecationWarning: (Since Sage Version 4.4.4) The function union is replaced by convex_hull.
  #!/usr/bin/env python
A 1-dimensional polyhedron in QQ^1 defined as the convex hull of 2 vertices.
```

If we pick something in a `*.pyx` file,

```
sage: p = m.copy()
/home/mjo/src/sage-5.0.beta1/local/lib/python2.7/site-packages/IPython/iplib.py:2260: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)
  exec code_obj in self.user_global_ns, self.user_ns
```

```
sage: x.lgamma()
/home/mjo/src/sage-5.0.beta1/local/lib/python2.7/site-packages/IPython/iplib.py:2260: DeprecationWarning: The lgamma() function is deprecated. Use log_gamma() instead.
  exec code_obj in self.user_global_ns, self.user_ns
log_gamma(x)
```


(notice the iplib.py/sage-ipython difference). In a python file, the stacklevel of EllipticCurve seems to be correct while the one for e.g. lgamma() is off by one. Here's a test.py file:

```
from sage.all import *

print "Calling EllipticCurve..."
EllipticCurve(ZZ(1))

print "\nCalling x.lgamma()"
var('x').lgamma()
```

And running it:

```
$ sage test.py 
Calling EllipticCurve...
test.py:4: DeprecationWarning: 'EllipticCurve(j)' is deprecated; use 'EllipticCurve_from_j(j)' or 'EllipticCurve(j=j)' instead.
  EllipticCurve(ZZ(1))

Calling x.lgamma()
sys:1: DeprecationWarning: The lgamma() function is deprecated. Use log_gamma() instead.
```

Adjusting the stacklevel fixes one, but breaks the other.



---

archive/issue_comments_068724.json:
```json
{
    "body": "I bungled one of my examples up there. This,\n\n```\nsage: p = m.copy()\n```\n\nShould be preceded by,\n\n```\nsage: m = identity_matrix(1)\n```",
    "created_at": "2012-01-23T00:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68724",
    "user": "https://github.com/orlitzky"
}
```

I bungled one of my examples up there. This,

```
sage: p = m.copy()
```

Should be preceded by,

```
sage: m = identity_matrix(1)
```



---

archive/issue_events_018938.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7913#event-18938"
}
```



---

archive/issue_events_018939.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7913#event-18939"
}
```



---

archive/issue_events_018940.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7913#event-18940"
}
```



---

archive/issue_events_018941.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7913#event-18941"
}
```



---

archive/issue_events_018942.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7913#event-18942"
}
```



---

archive/issue_events_018943.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7913#event-18943"
}
```



---

archive/issue_events_018944.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7913#event-18944"
}
```



---

archive/issue_comments_068725.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-10-27T15:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68725",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068726.json:
```json
{
    "body": "Changing priority from minor to trivial.",
    "created_at": "2016-10-27T15:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68726",
    "user": "https://github.com/JohnCremona"
}
```

Changing priority from minor to trivial.



---

archive/issue_comments_068727.json:
```json
{
    "body": "This is ancient and the problems have all gone away.  I tagged it as invalid / donfix.",
    "created_at": "2016-10-27T15:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68727",
    "user": "https://github.com/JohnCremona"
}
```

This is ancient and the problems have all gone away.  I tagged it as invalid / donfix.



---

archive/issue_events_018945.json:
```json
{
    "actor": "https://github.com/JohnCremona",
    "created_at": "2016-10-27T15:31:59Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7913#event-18945"
}
```



---

archive/issue_events_018946.json:
```json
{
    "actor": "https://github.com/JohnCremona",
    "created_at": "2016-10-27T15:31:59Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7913#event-18946"
}
```



---

archive/issue_comments_068728.json:
```json
{
    "body": "I'm not sure if the output is now correct for Cython code:\n\n```\nsage: 5.is_prime_power(flag=1)  # defined in sage/rings/integer.pyx\n/home/peter/src/sage/local/lib/python2.7/site-packages/IPython/core/interactiveshell.py:2885: DeprecationWarning: the 'flag' argument to is_prime_power() is no longer used\nSee http://trac.sagemath.org/16878 for details.\n  exec(code_obj, self.user_global_ns, self.user_ns)\nTrue\n```\nThe source line starting with `exec` is not very informative.  For Python code we get a more useful source line:\n\n```\nsage: FiniteField(9, impl='pari_mod')\n/home/peter/src/sage/local/lib/python2.7/site-packages/sage/rings/finite_rings/finite_field_constructor.py:650: DeprecationWarning: The \"pari_mod\" finite field implementation is deprecated\nSee http://trac.sagemath.org/17297 for details.\n  K = FiniteField_ext_pari(order, name, modulus)\nFinite Field in z2 of size 3^2\n```\nMaybe it isn't worth trying to fix this, though.",
    "created_at": "2016-10-27T18:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68728",
    "user": "https://github.com/pjbruin"
}
```

I'm not sure if the output is now correct for Cython code:

```
sage: 5.is_prime_power(flag=1)  # defined in sage/rings/integer.pyx
/home/peter/src/sage/local/lib/python2.7/site-packages/IPython/core/interactiveshell.py:2885: DeprecationWarning: the 'flag' argument to is_prime_power() is no longer used
See http://trac.sagemath.org/16878 for details.
  exec(code_obj, self.user_global_ns, self.user_ns)
True
```
The source line starting with `exec` is not very informative.  For Python code we get a more useful source line:

```
sage: FiniteField(9, impl='pari_mod')
/home/peter/src/sage/local/lib/python2.7/site-packages/sage/rings/finite_rings/finite_field_constructor.py:650: DeprecationWarning: The "pari_mod" finite field implementation is deprecated
See http://trac.sagemath.org/17297 for details.
  K = FiniteField_ext_pari(order, name, modulus)
Finite Field in z2 of size 3^2
```
Maybe it isn't worth trying to fix this, though.



---

archive/issue_comments_068729.json:
```json
{
    "body": "Changing component from user interface to cython.",
    "created_at": "2017-03-22T10:24:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68729",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from user interface to cython.



---

archive/issue_events_018947.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-03-22T10:24:48Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7913#event-18947"
}
```



---

archive/issue_events_018948.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-03-22T10:24:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "milestone": "sage-8.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7913#event-18948"
}
```



---

archive/issue_comments_068730.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-03-22T10:24:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68730",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068731.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2017-06-09T12:40:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68731",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_068732.json:
```json
{
    "body": "This is clearly a Cython upstream issue. There is no way to fix this within Sage.",
    "created_at": "2017-06-09T12:40:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68732",
    "user": "https://github.com/jdemeyer"
}
```

This is clearly a Cython upstream issue. There is no way to fix this within Sage.



---

archive/issue_events_018949.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-06-09T12:40:09Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "milestone": "sage-8.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7913#event-18949"
}
```



---

archive/issue_events_018950.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-06-09T12:40:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7913#event-18950"
}
```



---

archive/issue_comments_068733.json:
```json
{
    "body": "See http://cython.readthedocs.io/en/latest/src/userguide/limitations.html#stack-frames",
    "created_at": "2017-06-09T12:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68733",
    "user": "https://github.com/jdemeyer"
}
```

See http://cython.readthedocs.io/en/latest/src/userguide/limitations.html#stack-frames



---

archive/issue_comments_068734.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2017-07-13T07:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68734",
    "user": "https://github.com/embray"
}
```

Resolution: wontfix



---

archive/issue_comments_068735.json:
```json
{
    "body": "Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).",
    "created_at": "2017-07-13T07:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68735",
    "user": "https://github.com/embray"
}
```

Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).



---

archive/issue_events_018951.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2017-07-13T07:54:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7913#event-18951"
}
```
