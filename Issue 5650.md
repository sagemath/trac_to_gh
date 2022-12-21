# Issue 5650: speed up gamma_inc

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-03-31 17:02:35

Keywords: gamma_inc log performance speed

The following is from code for evaluating Riemann theta functions on sage.math:


```
sage: %prun siegel_theta(tau3p, 1/10*vector([1/2 + I, 2/3*I, 1.222*I]))
         137700 function calls (136832 primitive calls) in 2.221 CPU seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
       23    1.668    0.073    1.674    0.073 {method 'gamma_inc' of 'sage.rings.complex_number.ComplexNumber' objects}
    791/1    0.153    0.000    0.380    0.380 riemann_theta.py:313(find_integer_points)
     1601    0.066    0.000    0.066    0.000 {method 'sin' of 'sage.rings.real_mpfr.RealNumber' objects}
     5706    0.056    0.000    0.077    0.000 free_module.py:742(__call__)
        1    0.029    0.029    0.137    0.137 riemann_theta.py:51(finite_sum_without_derivatives)
     1602    0.026    0.000    0.026    0.000 {method 'exp' of 'sage.rings.real_mpfr.RealNumber' objects}
```


The `finite_sum_without_derivatives` is the main loop, which calls sin, cos, and exp each iteration.  But the dominant part is computing an initial error approximation, which computes `gamma_inc` to very high precision a bunch of times, optimizing a parameter.  That takes longer than everything else!  Could a party interested in special functions please speed this up?


---

Comment by fredrik.johansson created at 2009-04-02 08:39:48

How high precision and for what values of the arguments is this?


---

Comment by kcrisman created at 2012-06-01 18:36:44

Changing status from new to needs_info.


---

Comment by kcrisman created at 2012-06-01 18:36:44

> How high precision and for what values of the arguments is this?

Yeah, this is really vague, and the code involved is custom and not in Sage at this time.  It would be helpful to know if #7748, which changed the approximation to mpmath, helped here.  Until such time as we get more details, 'needs info'.


---

Comment by jdemeyer created at 2014-10-11 19:29:08

Changing status from needs_info to positive_review.


---

Comment by jdemeyer created at 2014-10-11 19:29:08

No answer, close as "invalid".


---

Comment by vbraun created at 2014-10-13 15:47:34

Resolution: invalid
