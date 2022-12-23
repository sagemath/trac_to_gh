# Issue 7913: extraneous output after deprecation warning

Issue created by migration from https://trac.sagemath.org/ticket/7913

Original creator: cremona

Original creation time: 2010-01-12 20:28:38

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


---

Comment by mjo created at 2012-01-23 00:51:07

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

Comment by mjo created at 2012-01-23 00:53:33

I bungled one of my examples up there. This,


```
sage: p = m.copy()
```


Should be preceded by,


```
sage: m = identity_matrix(1)
```



---

Comment by cremona created at 2016-10-27 15:31:59

Changing status from new to needs_review.


---

Comment by cremona created at 2016-10-27 15:31:59

Changing priority from minor to trivial.


---

Comment by cremona created at 2016-10-27 15:31:59

This is ancient and the problems have all gone away.  I tagged it as invalid / donfix.


---

Comment by pbruin created at 2016-10-27 18:16:14

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

Comment by jdemeyer created at 2017-03-22 10:24:48

Changing component from user interface to cython.


---

Comment by jdemeyer created at 2017-03-22 10:24:48

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2017-06-09 12:40:09

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2017-06-09 12:40:09

This is clearly a Cython upstream issue. There is no way to fix this within Sage.


---

Comment by jdemeyer created at 2017-06-09 12:43:33

See http://cython.readthedocs.io/en/latest/src/userguide/limitations.html#stack-frames


---

Comment by embray created at 2017-07-13 07:54:31

Resolution: wontfix


---

Comment by embray created at 2017-07-13 07:54:31

Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).
