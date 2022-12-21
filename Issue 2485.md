# Issue 2485: Complete docstrings and doctests for schemes/elliptic_curves

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-03-12 09:25:54

Assignee: cremona

CC:  ncalexan

Keywords: elliptic curves

Following Doc Days 2 on 2008-03-09 I am working on making the docstrings and tests for schemes/elliptic_curves as complete as I can.  A patch based on 2.10.3 will be posted here in time for 2.10.4, I hope.



---

Comment by ncalexan created at 2008-03-13 07:54:39

Hi John,

I assume you're CCed on this.  I am actively using the hyperelliptic curve code and have lots of things to fix/upgrade.  Some of my work will touch schemes/elliptic_curves and I don't want to step on your toes.  I'm CCed on this; when your patch is done I'll gladly referee it.

Nick


---

Comment by cremona created at 2008-03-13 09:32:20

Thanks Nick, that will be very helpful.  It's unlikely that we will conflict.  There is almost nothing I am planning to do except add to docstrings.  John


---

Attachment


---

Comment by cremona created at 2008-03-14 17:57:15

Changing status from new to assigned.


---

Comment by cremona created at 2008-03-14 17:57:15

The attached patch adds many docstrings to the following files (based on 2.10.3):

   * M sage/schemes/elliptic_curves/ell_finite_field.py
   * M sage/schemes/elliptic_curves/ell_generic.py
   * M sage/schemes/elliptic_curves/ell_modular_symbols.py
   * M sage/schemes/elliptic_curves/ell_number_field.py
   * M sage/schemes/elliptic_curves/ell_padic.py
   * M sage/schemes/elliptic_curves/ell_padic_field.py
   * M sage/schemes/elliptic_curves/ell_point.py
   * M sage/schemes/elliptic_curves/ell_rational_field.py
   * M sage/schemes/elliptic_curves/ell_tate_curve.py
   * M sage/schemes/elliptic_curves/gp_cremona.py
   * M sage/schemes/elliptic_curves/gp_simon.py

In addition there are a very few changes other than docstrings.
   * Some internal and local functions have had _ prepended to their names to explain why they may not have doctests
   * The output type of `modular_parametrization()` in ell_rational_field.py has been changed from a list of pari types to a list of Sage Laurent Series in the variable q
   * In addition to has_cm for elliptic curves over QQ, there is now a function cm_discriminant().  These two functions refer to a new global (to ell_rational_field.py) dict structure called CMJ.

I hope all this will be found useful!  There is still more to do in this directory:

Overall weighted coverage score:  66.1%

but a lot of that is explained by monsky_washnitzer.py: 23% (25 of 107) whci someone else will do, I hope.


---

Comment by ncalexan created at 2008-03-14 18:43:03

I think this patch should be applied, because it is mostly good, but it's not perfect.  I've noted a few nits below, only one of which (the KeyError) should be addressed before application.

Thanks for your effort, John!

This is probably not your bug, John, but it doesn't look right.


```
606	        EXAMPLES: 
607	            sage: E=EllipticCurve(GF(5),[1,1]) 
608	            sage: E._homset_class(GF(5^10,'a'),GF(5)) 
609	            Abelian group of points on Finite Field in a of size 5^10
```


Also, I really worry about double underscore functions at all -- I say replace with single underscore; then doctesting isn't so strange.


```
 	632	            sage: E=EllipticCurve(QQ,[1,1]) 
 	633	            sage: E._EllipticCurve_generic__is_over_RationalField() 
 	634	            True 
```


This comment looks outdated, and should be removed:

```
 	521	        def _pval(x):   # cannot be used for x=0 
 	522	            """ 
 	523	            Local function returning the valuation of x at P 
 	524	            """ 
522	525	            if x==0: return Infinity 
```


I think things like

```
1809	2264	    def label(self): 
1810	2265	        r""" 
1811	2266	        Exactly the same as the \code{cremona_label()} command. 
 	2267	 
 	2268	        EXAMPLES: 
 	2269	            sage: E=EllipticCurve('389a1') 
 	2270	            sage: E.label() 
 	2271	            '389a1' 
 	2272	 
1812	2273	        """ 
1813	2274	        return self.cremona_label() 
```


should be replaced with `label = cremona_label`.

This is not very helpful -- I would prefer, "A ValueError is raised..."

```
        2390	        An error is raised if the curve does not have CM (see the 
 	2391	        function has_cm()) 
```

and change the code to raise ValueError; it seems more appropriate than KeyError.


---

Attachment

Apply after 8866.patch


---

Comment by cremona created at 2008-03-14 19:52:38

Thanks a lot for the fast review, Nick.

   * I left the _homset_class test as it was.  That was one where I had a hard time working out what the function did and what was the point of it.  I still do not know.

   * Doctesting double-underscore functions is indeed very hard.  For things like __init__() the test does not mention __init__() and "sage -t" complains.  For ones like `_EllipticCurve_generic__is_over_RationalField()` (where in the code the function is simply `__is_over_RationalField()` there's no way the user will ever get to use them, and putting in tests will hardly help developers.

  * I fixed the others as you suggested, including changing the KeyError to ValueError -- it's just that the error is first raised as a KeyError (the value of j is not a key in the dict CMJ), but the user need not know that.


---

Comment by AlexGhitza created at 2008-03-15 18:57:28

Both patches apply cleanly against 2.10.3, and all doctests pass in sage/schemes/elliptic_curves/

The second patch appears to fix the issues brought up by the first reviewer, so I say "thumbs up".


---

Comment by mabshoff created at 2008-03-15 19:27:00

Resolution: fixed


---

Comment by mabshoff created at 2008-03-15 19:27:00

Merged both patches in Sage 2.10.4.rc0
