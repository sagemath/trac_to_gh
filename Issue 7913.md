# Issue 7913: extraneous output after deprecation warning

archive/issues_007913.json:
```json
{
    "body": "Assignee: was\n\nCC:  mjo\n\nKeywords: deprecation\n\nIn the following:\n\n```\nsage: EllipticCurve(0)\n/home/john/sage-4.3.1.alpha1/local/bin/sage-ipython:1:\nDeprecationWarning: 'EllipticCurve(j)' is deprecated; use\n'EllipticCurve_from_j(j)' or 'EllipticCurve(j=j)' instead.\n #!/usr/bin/env python\nElliptic Curve defined by y^2 = x^3 + 1 over Rational Field\n```\n\nwhere is the line \"#!/usr/bin/env python\" coming from?\n\nIssue created by migration from https://trac.sagemath.org/ticket/7913\n\n",
    "created_at": "2010-01-12T20:28:38Z",
    "labels": [
        "user interface",
        "minor",
        "bug"
    ],
    "title": "extraneous output after deprecation warning",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7913",
    "user": "cremona"
}
```
Assignee: was

CC:  mjo

Keywords: deprecation

In the following:

```
sage: EllipticCurve(0)
/home/john/sage-4.3.1.alpha1/local/bin/sage-ipython:1:
DeprecationWarning: 'EllipticCurve(j)' is deprecated; use
'EllipticCurve_from_j(j)' or 'EllipticCurve(j=j)' instead.
 #!/usr/bin/env python
Elliptic Curve defined by y^2 = x^3 + 1 over Rational Field
```

where is the line "#!/usr/bin/env python" coming from?

Issue created by migration from https://trac.sagemath.org/ticket/7913





---

archive/issue_comments_068842.json:
```json
{
    "body": "This looks like a stacklevel mismatch between python and cython code. Some other examples in pure python:\n\n\n```\nsage: numerical_sqrt(3)\n/home/mjo/src/sage-5.0.beta1/local/bin/sage-ipython:1: DeprecationWarning: numerical_sqrt is deprecated, use sqrt(x, prec=n) instead\n  #!/usr/bin/env python\nsqrt(3)\n```\n\n\n\n```\nsage: Polyhedron(vertices=[[0]]).union( Polyhedron(vertices=[[1]]) )\n/home/mjo/src/sage-5.0.beta1/local/bin/sage-ipython:1: DeprecationWarning: (Since Sage Version 4.4.4) The function union is replaced by convex_hull.\n  #!/usr/bin/env python\nA 1-dimensional polyhedron in QQ^1 defined as the convex hull of 2 vertices.\n```\n\n\nIf we pick something in a `*.pyx` file,\n\n\n```\nsage: p = m.copy()\n/home/mjo/src/sage-5.0.beta1/local/lib/python2.7/site-packages/IPython/iplib.py:2260: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)\n  exec code_obj in self.user_global_ns, self.user_ns\n```\n\n\n\n```\nsage: x.lgamma()\n/home/mjo/src/sage-5.0.beta1/local/lib/python2.7/site-packages/IPython/iplib.py:2260: DeprecationWarning: The lgamma() function is deprecated. Use log_gamma() instead.\n  exec code_obj in self.user_global_ns, self.user_ns\nlog_gamma(x)\n```\n\n\n\n(notice the iplib.py/sage-ipython difference). In a python file, the stacklevel of EllipticCurve seems to be correct while the one for e.g. lgamma() is off by one. Here's a test.py file:\n\n\n```\nfrom sage.all import *\n\nprint \"Calling EllipticCurve...\"\nEllipticCurve(ZZ(1))\n\nprint \"\\nCalling x.lgamma()\"\nvar('x').lgamma()\n```\n\n\nAnd running it:\n\n\n```\n$ sage test.py \nCalling EllipticCurve...\ntest.py:4: DeprecationWarning: 'EllipticCurve(j)' is deprecated; use 'EllipticCurve_from_j(j)' or 'EllipticCurve(j=j)' instead.\n  EllipticCurve(ZZ(1))\n\nCalling x.lgamma()\nsys:1: DeprecationWarning: The lgamma() function is deprecated. Use log_gamma() instead.\n```\n\n\nAdjusting the stacklevel fixes one, but breaks the other.",
    "created_at": "2012-01-23T00:51:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68842",
    "user": "mjo"
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

archive/issue_comments_068843.json:
```json
{
    "body": "I bungled one of my examples up there. This,\n\n\n```\nsage: p = m.copy()\n```\n\n\nShould be preceded by,\n\n\n```\nsage: m = identity_matrix(1)\n```\n",
    "created_at": "2012-01-23T00:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68843",
    "user": "mjo"
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

archive/issue_comments_068844.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-10-27T15:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68844",
    "user": "cremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068845.json:
```json
{
    "body": "Changing priority from minor to trivial.",
    "created_at": "2016-10-27T15:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68845",
    "user": "cremona"
}
```

Changing priority from minor to trivial.



---

archive/issue_comments_068846.json:
```json
{
    "body": "This is ancient and the problems have all gone away.  I tagged it as invalid / donfix.",
    "created_at": "2016-10-27T15:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68846",
    "user": "cremona"
}
```

This is ancient and the problems have all gone away.  I tagged it as invalid / donfix.



---

archive/issue_comments_068847.json:
```json
{
    "body": "I'm not sure if the output is now correct for Cython code:\n\n```\nsage: 5.is_prime_power(flag=1)  # defined in sage/rings/integer.pyx\n/home/peter/src/sage/local/lib/python2.7/site-packages/IPython/core/interactiveshell.py:2885: DeprecationWarning: the 'flag' argument to is_prime_power() is no longer used\nSee http://trac.sagemath.org/16878 for details.\n  exec(code_obj, self.user_global_ns, self.user_ns)\nTrue\n```\n\nThe source line starting with `exec` is not very informative.  For Python code we get a more useful source line:\n\n```\nsage: FiniteField(9, impl='pari_mod')\n/home/peter/src/sage/local/lib/python2.7/site-packages/sage/rings/finite_rings/finite_field_constructor.py:650: DeprecationWarning: The \"pari_mod\" finite field implementation is deprecated\nSee http://trac.sagemath.org/17297 for details.\n  K = FiniteField_ext_pari(order, name, modulus)\nFinite Field in z2 of size 3^2\n```\n\nMaybe it isn't worth trying to fix this, though.",
    "created_at": "2016-10-27T18:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68847",
    "user": "pbruin"
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

archive/issue_comments_068848.json:
```json
{
    "body": "Changing component from user interface to cython.",
    "created_at": "2017-03-22T10:24:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68848",
    "user": "jdemeyer"
}
```

Changing component from user interface to cython.



---

archive/issue_comments_068849.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-03-22T10:24:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68849",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068850.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2017-06-09T12:40:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68850",
    "user": "jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_068851.json:
```json
{
    "body": "This is clearly a Cython upstream issue. There is no way to fix this within Sage.",
    "created_at": "2017-06-09T12:40:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68851",
    "user": "jdemeyer"
}
```

This is clearly a Cython upstream issue. There is no way to fix this within Sage.



---

archive/issue_comments_068852.json:
```json
{
    "body": "See http://cython.readthedocs.io/en/latest/src/userguide/limitations.html#stack-frames",
    "created_at": "2017-06-09T12:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68852",
    "user": "jdemeyer"
}
```

See http://cython.readthedocs.io/en/latest/src/userguide/limitations.html#stack-frames



---

archive/issue_comments_068853.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2017-07-13T07:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68853",
    "user": "embray"
}
```

Resolution: wontfix



---

archive/issue_comments_068854.json:
```json
{
    "body": "Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).",
    "created_at": "2017-07-13T07:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7913#issuecomment-68854",
    "user": "embray"
}
```

Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).
