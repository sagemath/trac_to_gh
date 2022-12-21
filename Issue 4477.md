# Issue 4477: [with patch; needs review] Allow exp() function for PowerSeriesRing element to compute with valid non-zero constant term

Issue created by migration from Trac.

Original creator: sengupta

Original creation time: 2008-11-09 07:44:08

Assignee: somebody

CC:  dmharvey

The patch posted against this ticket enhances the exp() function for PowerSeriesRing elements and allows it to compute with valid non-zero constant terms in the power series.

Previously: f.exp() would return an error "Constant term must be zero" if f[0] != 0

With the patch: f.exp() checks if f[0].exp() is at all defined and in the case it is defined, whether f[0].exp() belongs to the base ring of f. If both the conditions are satisfied, f.exp() is returned.


---

Attachment


---

Comment by sengupta created at 2008-11-09 08:05:12

Changing status from new to assigned.


---

Comment by sengupta created at 2008-11-09 08:05:12

Changing assignee from somebody to sengupta.


---

Comment by sengupta created at 2008-11-09 08:05:12

Hi David ... I have just posted the patch to the exp() code ... Please take a look ... It will be great if I can have it checked ... Thank you ...


---

Comment by dmharvey created at 2008-11-10 22:22:05

I will review this in the next few days.


---

Comment by dmharvey created at 2008-11-13 03:53:03

Code is basically good. Still running doctests. A few comments:

 * Indenting on "Check for non-zero constant term" line is wrong. Please fix.

 * Shouldn't have "fixes \#4477" (what will that mean in two years)

 * please refactor so that self.derivative().solve_linear_de(prec) is not called in two different places

 * "if C.parent()!=self.base_ring()" should use "is not" instead of "!=" (much more efficient)

 * possibly should use "if not self[0].is_zero()" instead of "if self[0]". I can't remember why, but maybe is_zero actually does something useful (I vaguely remember it might have something to do with testing zero-ness in inexact rings)

 * the error message "exponential of the input does not belong to the ring" should be more useful to the user. Perhaps "exponential of the constant term does not lie in the coefficient ring. Consider coercing to an appropriate larger ring", or if you're feeling ambitious, invoke the coercion machinery to automagically find that larger ring (but don't ask me how to do that, I have no idea)

 * I think that error message is also misleading in the case that the constant term doesn't have an exp method defined. Perhaps raise a different error in that case, e.g. "cannot exponentiate series; exp of constant term is not defined".

 * The last doctest is misleading. The power series ring is defined over QQ, but the doctest *implicitly* creates a power series over RR and then exponentiates that. To demonstrate the different situation clearly, the doctest should explicitly create the power series ring over RR.


---

Comment by mabshoff created at 2008-11-13 03:57:17

Replying to [comment:4 dmharvey]:

>  * Shouldn't have "fixes \#4477" (what will that mean in two years)

I disagree. Any doctest marked that way should never be changed since it fixes a specific bug and hence refers to the trac ticket. Tests like that should probably be moved to a TESTS section in the long term, but we can deal with that later.

Cheers,

Michael


---

Comment by was created at 2008-11-13 14:37:51

I agree with Michael on the value of "Shouldn't have "fixes \#4477" (what will that mean in two years)", assuming we never loose all of trac :-)  I prefer writing "Trac ticket \#4477" to clue people a little more about the meaning of it though, in any docstring.


---

Comment by dmharvey created at 2008-11-13 15:01:57

ok, fair enough. At some point it starts getting kind of cluttered though, and can distract from the "documentation" purpose of the docstring. I agree with moving it out to a TESTS section at some point.


---

Attachment


---

Comment by dmharvey created at 2008-12-05 03:39:50

Second attempt, to address my previous concerns. Apply both patches.


---

Comment by robertwb created at 2008-12-09 19:54:47

Is this expected? 


```
sage: R.<x> = ZZ[[]]
sage: x.exp()
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "power_series_ring_element.pyx", line 1383, in sage.rings.power_series_ring_element.PowerSeries.exp (sage/rings/power_series_ring_element.c:9850)
  File "power_series_ring_element.pyx", line 1305, in sage.rings.power_series_ring_element.PowerSeries.solve_linear_de (sage/rings/power_series_ring_element.c:9707)
  File "power_series_ring_element.pyx", line 1648, in sage.rings.power_series_ring_element._solve_linear_de (sage/rings/power_series_ring_element.c:11103)
  File "power_series_ring_element.pyx", line 1648, in sage.rings.power_series_ring_element._solve_linear_de (sage/rings/power_series_ring_element.c:11103)
  File "power_series_ring_element.pyx", line 1650, in sage.rings.power_series_ring_element._solve_linear_de (sage/rings/power_series_ring_element.c:11124)
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 252, in __call__
    return C(self, x, check, is_gen, construct=construct)
  File "polynomial_integer_dense_flint.pyx", line 224, in sage.rings.polynomial.polynomial_integer_dense_flint.Polynomial_integer_dense_flint.__init__ (sage/rings/polynomial/polynomial_integer_dense_flint.cpp:4981)
  File "parent.pyx", line 293, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3828)
  File "parent.pyx", line 284, in sage.structure.parent.__call__ (sage/structure/parent.c:3712)
  File "rational.pyx", line 2288, in sage.rings.rational.Q_to_Z._call_ (sage/rings/rational.c:14682)
TypeError: no conversion of this rational to integer
```


The sqrt function automatically passes to the rationals. 

```
sage: (1+x).sqrt()
1 + 1/2*x - 1/8*x^2 + 1/16*x^3 - 5/128*x^4 + 7/256*x^5 - 21/1024*x^6 + 33/2048*x^7 - 429/32768*x^8 + 715/65536*x^9 - 2431/262144*x^10 + 4199/524288*x^11 - 29393/4194304*x^12 + 52003/8388608*x^13 - 185725/33554432*x^14 + 334305/67108864*x^15 - 9694845/2147483648*x^16 + 17678835/4294967296*x^17 - 64822395/17179869184*x^18 + 119409675/34359738368*x^19 + O(x^20)
```



---

Comment by dmharvey created at 2008-12-09 23:27:58

I suppose it's reasonable to expect it automatically passes to the quotient field where possible, but unless someone wants to fix that right now, it should probably go onto another ticket.

(While we're here, shouldn't the sqrt function pass to the localisation away from the prime 2? Why all the way to Q? (Just kidding --- I know the answer :-)))


---

Comment by robertwb created at 2008-12-10 00:13:30

I've created #4748. Other than that it works great (and the issue above didn't work before either). 

- Robert


---

Comment by mabshoff created at 2008-12-10 07:54:39

Resolution: fixed


---

Comment by mabshoff created at 2008-12-10 07:54:39

Merged trac_4477.patch and trac_4477-2.patch in Sage 3.2.2.alpha1
