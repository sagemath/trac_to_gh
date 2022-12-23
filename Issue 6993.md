# Issue 6993: [with package, needs review] update pynac to 0.1.9

Issue created by migration from https://trac.sagemath.org/ticket/6993

Original creator: burcin

Original creation time: 2009-09-22 19:18:06

Assignee: burcin

CC:  was mhansen ncalexan

New pynac package available at:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.9.spkg

Changes to pynac can also be viewed by going here:

http://pynac.sagemath.org/hg/rev/beb49aa3cebf

and clicking the link for "children" to see the other patches.






---

Attachment

This package includes corresponding changes for the tickets:

 * #6948 powers of exp are over simplified
 * #6902 log(x) is typeset as \ln x
 * #6851 hashes for derivatives of symbolic functions still collide
 * #6524 Ratio of two symbolic expressions involving derivative does not simplify
 * #6992 rename lngamma to log gamma

The patch attached to this ticket is just an enhancement. It is the first step to cleaning up the interface for symbolic functions. Pynac now evaluates symbolic functions on non-exact input again. This eliminates the need for a separate `__call__` method in `sage.symbolic.function.PrimitiveFunction`.


---

Comment by burcin created at 2009-09-22 19:26:03

Changing status from new to assigned.


---

Comment by kcrisman created at 2009-09-23 02:40:25

There are a lot of other doctest failures caused by this package than the ones fixed above.  It is possible that some are spurious because I missed something in the tickets listed above, but I will post them here for now.
 Ones not covered elsewhere I describe.
	sage -t  "devel/sage/sage/calculus/calculus.py"
	sage -t  "devel/sage/sage/calculus/desolvers.py"
	sage -t  "devel/sage/sage/calculus/functional.py"
	sage -t  "devel/sage/sage/calculus/functions.py"
	sage -t  "devel/sage/sage/functions/log.py"
	sage -t  "devel/sage/sage/calculus/tests.py"
All of these are just order switches and should be trivial to fix.

	sage -t  "devel/sage/sage/calculus/wester.py"

```
    sage: print RealField(150)(a)
Expected:
    2.6253741264076874399999999999925007259719820e17
Got:
    2.6253741264076874399999999999925007259719819e17
*********************************************************************	
    sage: taylor(log(x)^a*exp(-b*x), x, 1, 3)
Expected:
    -1/48*(x - 1)^3*((6*b + 5)*(x - 1)^a*a^2 + (x - 1)^a*a^3 + 8*(x - 1)^a*b^3 + 2*(6*b^2 + 5*b + 3)*(x - 1)^a*a)*e^(-b) + 1/24*(x - 1)^2*((12*b + 5)*(x - 1)^a*a + 3*(x - 1)^a*a^2 + 12*(x - 1)^a*b^2)*e^(-b) - 1/2*(x - 1)*((x - 1)^a*a + 2*(x - 1)^a*b)*e^(-b) + (x - 1)^a*e^(-b)
Got:
    -1/48*(x - 1)^3*((6*b + 5)*(x - 1)^a*a^2 + (x - 1)^a*a^3 + 8*(x - 1)^a*b^3 + 2*(6*b^2 + 5*b + 3)*(x - 1)^a*a)/e^b + 1/24*(x - 1)^2*((12*b + 5)*(x - 1)^a*a + 3*(x - 1)^a*a^2 + 12*(x - 1)^a*b^2)/e^b - 1/2*(x - 1)*((x - 1)^a*a + 2*(x - 1)^a*b)/e^b + (x - 1)^a/e^b
*********************************************************************
```

	sage -t  "devel/sage/sage/symbolic/expression.pyx"
	sage -t  "devel/sage/sage/symbolic/expression_conversions.py"
Both of these have a problem with QQbar(e^(pi*I/3)).  This is definitely an algebraic number, so hopefully it's covered elsewhere.  Specifically,

```
ges/sage/symbolic/expression_conversions.pyc in composition(self, ex, operator)
    729             if rat_arg == 0:
    730                 # here we will either try and simplify, or return
--> 731                 raise ValueError, "Unable to represent as an algebraic number."
    732             real = operand.real()
    733             if real:

ValueError: Unable to represent as an algebraic number.
```

	sage -t  "devel/sage/sage/symbolic/relation.py"
This is:

```
   sage: eq._maxima_init_()
Expected:
    '(x)^(3/5) >= ((%pi)^(2))+(exp(0+%i*1))'
Got:
    '(x)^(3/5) >= ((%pi)^(2))+((exp(1))^(0+%i*1))'
******
   sage: solve(f==0,x)
Expected:
    [x == (-a)^(1/5)*e^(2/5*I*pi), x == (-a)^(1/5)*e^(4/5*I*pi), x == (-a)^(1/5)*e^(-4/5*I*pi), x == (-a)^(1/5)*e^(-2/5*I*pi), x == (-a)^(1/5)]
Got:
    [x == e^(2/5*I*pi)*(-a)^(1/5), x == e^(4/5*I*pi)*(-a)^(1/5), x == e^(-4/5*I*pi)*(-a)^(1/5), x == e^(-2/5*I*pi)*(-a)^(1/5), x == (-a)^(1/5)]
**********************************************************************
```



---

Comment by kcrisman created at 2009-09-23 20:58:53

I think you should have been more explicit about how to test this - it wasn't clear that all the patches were necessary to avoid doctest issues.  I checked and I think they must all have been related to powers of exp.

Anyway, relevant tests pass, the "children" were easy to follow, so the only thing (possibly) hindering positive review is the parenthesis issue in #6948.


---

Comment by burcin created at 2009-09-24 06:35:13

New package here: 

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.9.p0.spkg

Includes printing fixes for #6948.


---

Comment by kcrisman created at 2009-09-24 13:35:02

Positive review!  Great.  My only complaint is that Pynac is not on the Sage revision control system, so it's both difficult to look at (hence, thanks for the link to the changesets) and difficult to fix symbolic issues in Sage that really "should" live in Pynac.

To release manager: apply .p0 package first, then the tickets listed above in reverse numerical order, with #6948 ticket applying first the regular patch, then the print patch.  I think that should be the correct order, and should lead to no new doctest failures.  (In actual fact, I think that only the patch on this ticket needs to be applied before the others, but that's the order that worked for me.)


---

Comment by mvngu created at 2009-09-25 22:43:09

Merged `pynac-0.1.9.p0.spkg` in the standard packages repository. Merged `trac_6993-revert_evalf.patch` in the Sage library.


---

Comment by mvngu created at 2009-09-25 22:43:09

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:37:37

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
