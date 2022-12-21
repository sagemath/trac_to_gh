# Issue 6665: Expanding the 'zero' symmetric function in variables crashes symmetrica

Issue created by migration from Trac.

Original creator: jbandlow

Original creation time: 2009-08-02 11:16:36

Assignee: mhansen

Keywords: symmetrica

Jerome Lefebvre reported:

```
Bizarre error reporting with symmetric functions;

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: H = SymmetricFunctionAlgebra(QQ, basis='homogeneous')
sage: f = H(0)
sage: print f
0
sage: g = f.expand(3, alphabet=['x_1','x_2','x_3'])
| Sage Version 4.1, Release Date: 2009-07-09                         |
| Type notebook() for the GUI, and license() for information.        |
This then gives me;

enter a to abort with core dump, g to go, f to supress
s to supress further error text, r to retry,  e to explain, else stop
ERROR: s_po_k: not POLYNOM?:


So I entered e (had to do it twice) to get;


enter a to abort with core dump, g to go, f to supress
s to supress further error text, r to retry,  e to explain, else stop
ERROR: s_po_k: not POLYNOM?: e

enter a to abort with core dump, g to go, f to supress
s to supress further error text, r to retry,  e to explain, else stop
ERROR: s_o_k:object == NULL?: e
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call
last)

/Users/jeromelefebvre/.sage/temp/Jerome.local/22022/
_Users_jeromelefebvre__sage_init_sage_0.py in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/sf/
homogeneous.pyc in expand(self, n, alphabet)
     95         """
     96         condition = lambda part: False
---> 97         return self._expand(condition, n, alphabet)
     98
     99

/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/sf/
sfa.pyc in _expand(self, condition, n, alphabet)
   1534         resPR = PolynomialRing(parent.base_ring(), n,
alphabet)
   1535         f = lambda part: resPR(0) if condition(part) else resPR
(e(part, n, alphabet))
-> 1536         return parent._apply_module_morphism(self, f)
   1537
   1538     def scalar(self, x):

/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/
free_module.pyc in _apply_module_morphism(self, x, f)
    973         res = 0
    974         for m, c in x._monomial_coefficients.iteritems():
--> 975             res += c*f(m)
    976         return res
    977

/Applications/sage/local/lib/python2.6/site-packages/sage/combinat/sf/
sfa.pyc in <lambda>(part)
   1533         e = eval('symmetrica.compute_' + str
(classical.translate[parent.basis_name()]).lower() + '_with_alphabet')
   1534         resPR = PolynomialRing(parent.base_ring(), n,
alphabet)
-> 1535         f = lambda part: resPR(0) if condition(part) else resPR
(e(part, n, alphabet))
   1536         return parent._apply_module_morphism(self, f)
   1537

/Applications/sage/local/lib/python2.6/site-packages/sage/libs/
symmetrica/symmetrica.so in
sage.libs.symmetrica.symmetrica.compute_homsym_with_alphabet_symmetrica
(sage/libs/symmetrica/symmetrica.c:15628)()

/Applications/sage/local/lib/python2.6/site-packages/sage/libs/
symmetrica/symmetrica.so in
sage.libs.symmetrica.symmetrica._py_polynom_alphabet (sage/libs/
symmetrica/symmetrica.c:4777)()

/Applications/sage/local/lib/python2.6/site-packages/sage/libs/
symmetrica/symmetrica.so in sage.libs.symmetrica.symmetrica._py (sage/
libs/symmetrica/symmetrica.c:2203)()

NotImplementedError: -6
sage:
```


This is related to #6487, and the fact that symmetrica typically segfaults with input it doesn't expect.


---

Attachment


---

Comment by jbandlow created at 2010-05-06 15:39:35

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-05-09 16:47:05

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-05-09 16:47:05

Applies fines, does it job, nothing to complain about... Thank youuuuu ! :-)

Nathann


---

Comment by mhansen created at 2010-06-05 22:00:38

Resolution: fixed
