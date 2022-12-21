# Issue 1237: E.torsion_order() fails on curves with big coefficients !!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-21 17:25:16

Assignee: was

On Nov 20, 2007 1:40 PM, Paul Zimmermann  wrote:
>        William,
> 
> sage told me to report you, thus I do:
[... see below]

For the particular curve you're considering mwrank (via sage's rank command)
can compute the rank -- which is what you want -- in 0.5 seconds, so maybe
you can use .rank() instead?

{{{id=24|
e = EllipticCurve([0, 33076156654533652066609946884, 0,
347897536144342179642120321790729023127716119338758604800,
114112815436927429551902303280680424778815462104985764887003237028585178\
1352816640000])
}}}

{{{id=27|
time e.rank()
///
1
CPU time: 0.00 s,  Wall time: 0.46 s
}}}

That said, the fact that  e.torsion_order() fails is certainly a bug:

{{{id=29|
e.torsion_order()
///
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/was/sage_notebook/worksheets/admin/23/code/91.py", line 4, in <module>
...
    self.__torsion_subgroup = rational_torsion.EllipticCurveTorsionSubgroup(self, flag)
  File "/Users/was/s/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/rational_torsion.py", line 56, in __init__
    self.__E.__pari_double_prec()
AttributeError: 'EllipticCurve_rational_field' object has no attribute '_EllipticCurveTorsionSubgroup__pari_double_prec'
}}}



```

> sage: d = 919681/88529281
> sage: _ = magma.eval('K := Rationals()')
> sage: _ = magma.eval('P<x,y,z>:=ProjectiveSpace(K,2)')
> sage: def rank(d):
> ....:        s='f := (x^2+y^2)*z^2-z^4-('
> ....:    s=''.join([s, repr(d), ')*x^2*y^2;'])
> ....:    magma.eval(s)
> ....:    magma.eval('C:=Curve(P,f);')
> ....:    E = magma('EllipticCurve(C,C![0,1,1])')
> ....:    l = E.aInvariants()
> ....:    EE = EllipticCurve(map(Integer,l))
> ....:    return EE.simon_two_descent()[0]
> ....:
> sage: rank(d)
> ---------------------------------------------------------------------------
> <type 'exceptions.AttributeError'>        Traceback (most recent call last)
> 
> /home/zimmerma/<ipython console> in <module>()
> 
> /home/zimmerma/<ipython console> in rank(d)
> 
> /usr/local/sage-2.8.12/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in simon_two_descent(self, verbose, lim1, lim3, limtriv, maxprob, limbigprime)
>     858             (8, 8)
>     859         """
> --> 860         if self.torsion_order() % 2 == 0:
>     861             raise ArithmeticError, "curve must not have rational 2-torsion\nThe *only* reason for this is that I haven't finished implementing the wrapper\nin this case.  It wouldn't be too difficult.\nPerhaps you could do it?!  Email me (wstein`@`gmail.com)."
>     862         F = self.integral_weierstrass_model()
> 
> /usr/local/sage-2.8.12/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in torsion_order(self)
>    1743             return self.__torsion_order
>    1744         except AttributeError:
> -> 1745             self.__torsion_order = self.torsion_subgroup().order()
>    1746             return self.__torsion_order
>    1747
> 
> /usr/local/sage-2.8.12/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py in torsion_subgroup(self, flag)
>    1781             return self.__torsion_subgroup
>    1782         except AttributeError:
> -> 1783             self.__torsion_subgroup = rational_torsion.EllipticCurveTorsionSubgroup(self, flag)
>    1784             return self.__torsion_subgroup
>    1785
> 
> /usr/local/sage-2.8.12/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/rational_torsion.py in __init__(self, E, flag)
>      54                 G = self.__E.pari_curve().elltors(flag)
>      55             except RuntimeError:
> ---> 56                 self.__E.__pari_double_prec()
>      57         if G is None:
>      58             raise RuntimeError, "Could not compute torsion subgroup"
> 
> <type 'exceptions.AttributeError'>: 'EllipticCurve_rational_field' object has no attribute '_EllipticCurveTorsionSubgroup__pari_double_prec'
> 
> Paul
> 
```



-- 
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org



---

Comment by roed created at 2007-11-21 22:13:39

Fix


---

Comment by roed created at 2007-11-21 22:14:39

Changing assignee from was to roed.


---

Comment by roed created at 2007-11-21 22:14:39

Changing status from new to assigned.


---

Attachment


---

Attachment

this touches up a bunch of the docs.


---

Comment by was created at 2007-12-15 11:40:32

I give this a positive review.


---

Comment by mabshoff created at 2007-12-15 11:51:36

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 11:51:36

Merged in 2.9.rc0.
