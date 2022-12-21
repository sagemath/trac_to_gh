# Issue 5755: error converting symbolic expression to polynomial

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-04-11 17:17:23

CC:  jason mhansen


```
sage: xx = var('xx')
sage: RDF['xx'](1.0*xx)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/12913/_Users_ncalexan_sage_3_4_rc0_devel_sage_main_sage_symbolic_test2_sage_3.py in <module>()

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3653)()

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:3627)()

/Users/ncalexan/sage-3.4.rc0/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in _polynomial_(self, R)
   2220                     not_found_v = False
   2221             if not_found_v:
-> 2222                 raise TypeError, "%s is not a variable of %s" %(v, R)
   2223         if len(sub) == 0:
   2224             try:

TypeError: xx is not a variable of Univariate Polynomial Ring in xx over Real Double Field
```



---

Comment by kcrisman created at 2009-09-29 18:56:50

This will probably be fixed by the final resolution of #7007.


---

Comment by kcrisman created at 2009-09-30 18:58:54

Since #7007 got positive review, here is the patch documenting the fix.


---

Attachment

Based on 4.1.2.alpha4, depends on #7007


---

Comment by mhansen created at 2009-10-01 03:11:27

Looks good to me.


---

Comment by mhansen created at 2009-10-15 07:12:29

Resolution: fixed
