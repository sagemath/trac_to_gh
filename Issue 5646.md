# Issue 5646: vectors over CDF allow a coercion from scalars

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-03-30 23:59:39

Assignee: was

CC:  robertwb mjo

Keywords: complex vector coercion

These are incompatible and I claim the first one is wrong!


```
sage: (CDF^2)(1)
(1.0, 1.0)
sage: (CC^2)(1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage/sage/functions/riemann_theta.py in <module>()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in __ca\
ll__(self, e, coerce, copy, check)
   4394         except AttributeError:
   4395             pass
-> 4396         return FreeModule_generic_field.__call__(self,e)
   4397
   4398 ###############################################################################

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/modules/free_module.pyc in __ca\
ll__(self, x, coerce, copy, check)
    813             except ArithmeticError:
    814                 raise ValueError, "element (= %s) is not in free module"%(x,)
--> 815         return self._element_class(self, x, coerce, copy)
    816
    817     def is_submodule(self, other):

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/modules/free_module_element.so \
in sage.modules.free_module_element.FreeModuleElement_generic_dense.__init__ (sage/modules/free_module_element.c:15739)()

TypeError: entries (=1) must be a list
```



---

Comment by robertwb created at 2009-03-31 00:04:06

I second that the first one is wrong, but this is not a coercion issue. 


```
sage: (CDF^2).has_coerce_map_from(CDF)
False
```



---

Attachment


---

Comment by mjo created at 2012-01-09 04:48:41

Changing status from new to needs_review.


---

Comment by mjo created at 2012-01-09 04:48:41

(I think this was left 'new' by mistake)

Why is an exception made for zero? Is it just convenience? We have `(CDF^2).zero()` which does the same thing as far as I can tell.


---

Comment by johanbosman created at 2012-03-18 17:21:43

Every vector space has a zero element, which is denoted by 0.  There are generally no elements in a vector space denoted by 1.


---

Comment by johanbosman created at 2012-03-18 17:21:43

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by jdemeyer created at 2012-03-28 10:03:25

Resolution: fixed
