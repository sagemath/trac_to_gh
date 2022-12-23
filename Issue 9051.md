# Issue 9051: Fast function field arithmetic

Issue created by migration from https://trac.sagemath.org/ticket/9051

Original creator: robertwb

Original creation time: 2010-05-26 00:27:53

Assignee: AlexGhitza

CC:  minz

Followup to #7585, which also did many, many other things. 

Wrapping flint directly is much faster than the current implementation of Frac(GF(p)['t'])


---

Attachment


---

Attachment


---

Comment by robertwb created at 2010-05-27 07:30:02

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-05-27 07:30:02

Apply all three patches in order. 

Positive review to `9051-FpT_2.patch` (the third was somewhat a rebasing, referee, and fixing some stuff).


---

Comment by was created at 2010-05-28 22:58:31

Note:   9051-FpT_2.patch  is by David Roe.


---

Attachment


---

Comment by was created at 2010-07-08 11:58:21

flattened parts1-4 and rebased against sage-4.4.4


---

Attachment

I took sage-4.4.4 and applied trac_9051-flattened_and_rebased.patch.  Doctesting just rings/ fails very seriously after applying this patch:


```

sage -t devel/sage/sage/rings/

The following tests failed:

        sage -t  devel/sage-main/sage/rings/residue_field.pyx # 16 doctests failed
        sage -t  devel/sage-main/sage/rings/number_field/order.py # 3 doctests failed
        sage -t  devel/sage-main/sage/rings/number_field/number_field_element_quadratic.pyx # 2 doctests failed
        sage -t  devel/sage-main/sage/rings/arith.py # 1 doctests failed
        sage -t  devel/sage-main/sage/rings/ring.pyx # 5 doctests failed
        sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx # 2 doctests failed
        sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 7 doctests failed
        sage -t  devel/sage-main/sage/rings/integer_ring.pyx # 5 doctests failed
        sage -t  devel/sage-main/sage/rings/number_field/galois_group.py # 8 doctests failed
        sage -t  devel/sage-main/sage/rings/polynomial/polynomial_element.pyx # 7 doctests failed
        sage -t  devel/sage-main/sage/rings/misc.py # 1 doctests failed
        sage -t  devel/sage-main/sage/rings/number_field/number_field_base.pyx # 13 doctests failed
        sage -t  devel/sage-main/sage/rings/qqbar.py # 4 doctests failed
        sage -t  devel/sage-main/sage/rings/number_field/number_field_rel.py # 10 doctests failed
        sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py # 15 doctests failed
        sage -t  devel/sage-main/sage/rings/polynomial/polynomial_singular_interface.py # 1 doctests failed
        sage -t  devel/sage-main/sage/rings/number_field/number_field_element.pyx # 13 doctests failed
----------------------------------------------------------------------
Timings have been updated.
Total time for all tests: 64.0 seconds
```



---

Comment by was created at 2010-07-08 12:05:56

Changing status from needs_review to needs_work.


---

Comment by roed created at 2010-07-09 11:59:27

Fixes the broken doctests


---

Attachment


---

Comment by roed created at 2010-07-09 11:59:46

Changing status from needs_work to needs_review.


---

Comment by roed created at 2010-07-09 12:00:29

The most recent patch should be applied on top of the flattened and rebased patche.


---

Comment by was created at 2010-07-09 12:06:22

I'm running tests with both patches:

  http://sage.math.washington.edu/home/wstein/build/sage-4.4.4/devel/sage/9051.out


---

Comment by was created at 2010-07-09 12:08:30

Changing status from needs_review to needs_work.


---

Comment by was created at 2010-07-09 12:08:30

Stuff fails.  See above link.


---

Comment by was created at 2010-07-09 12:18:34


```
----------------------------------------------------------------------

The following tests failed:

        sage -t  devel/sage-main/sage/modular/abvar/homspace.py # 20 doctests failed
        sage -t  devel/sage-main/sage/modular/abvar/abvar.py # 32 doctests failed
        sage -t  devel/sage-main/sage/modular/modsym/space.py # 6 doctests failed
        sage -t  devel/sage-main/sage/modular/modsym/ambient.py # 2 doctests failed
        sage -t  devel/sage-main/sage/modular/modform/element.py # 2 doctests failed
        sage -t  devel/sage-main/sage/functions/piecewise.py # 6 doctests failed
        sage -t  devel/sage-main/sage/graphs/graph.py # 1 doctests failed
        sage -t  devel/sage-main/sage/modular/abvar/morphism.py # 3 doctests failed
        sage -t  devel/sage-main/sage/modular/abvar/abvar_ambient_jacobian.py # 3 doctests failed
        sage -t  devel/sage-main/sage/modular/abvar/homology.py # 19 doctests failed
        sage -t  devel/sage-main/sage/modular/abvar/abvar_newform.py # 12 doctests failed
        sage -t  devel/sage-main/sage/tests/startup.py # 1 doctests failed
        sage -t  devel/sage-main/sage/numerical/optimize.py # 2 doctests failed
        sage -t  devel/sage-main/sage/modular/abvar/constructor.py # 2 doctests failed
        sage -t  devel/sage-main/sage/schemes/hyperelliptic_curves/hypellfrob.pyx # 1 doctests failed
----------------------------------------------------------------------
Timings have been updated.
Total time for all tests: 355.5 seconds
                                                            
```



---

Attachment

Fixes more doctests


---

Comment by roed created at 2010-07-09 12:30:31

Thanks; I was going to run tests while sleeping, but this worked better.  I think I have them all now, but I haven't run tests after the fix: I'm doing it on my laptop, so it'll take a while.


---

Comment by roed created at 2010-07-09 12:30:31

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-07-09 14:34:03

Here it goes again:

   http://sage.math.washington.edu/home/wstein/build/sage-4.4.4/devel/sage/9051-try2.out


---

Comment by roed created at 2010-07-09 22:02:23

Looks like all tests pass; do you want to review it?


---

Comment by was created at 2010-07-10 05:11:07

Wow, that's excellent that everything finally passes.  Yes, I hope to have time to review it soon.


---

Attachment

I did a benchmark on sage.math, comparing this code to Magma:

SAGE with your patch:

```
sage: R.<T> = GF(71)[]; K.<T> = FractionField(R); a=(T^3+T-1)*(T^2-2); b=(3*T^5-T+7)*(T^2-2)
sage: timeit('a/b+b/a')
625 loops, best of 3: 26.3 µs per loop
sage: time v=[a/b+b/a for i in range(10^5)]
CPU times: user 2.94 s, sys: 0.02 s, total: 2.96 s
Wall time: 2.96 s
sage: time v=[a*b for i in range(10^5)]
CPU times: user 0.54 s, sys: 0.02 s, total: 0.56 s
Wall time: 0.56 s
sage: time v=[(1/a)*(1/b) for i in range(10^5)]
CPU times: user 1.80 s, sys: 0.00 s, total: 1.80 s
Wall time: 1.80 s
```


Before the patch, the same benchmark is massively slower, so this patch is a very big improvement:

```
sage: sage: R.<T> = GF(71)[]; K.<T> = FractionField(R); a=(T^3+T-1)*(T^2-2); b=(3*T^5-T+7)*(T^2-2)
sage: sage: timeit('a/b+b/a')
625 loops, best of 3: 776 µs per loop
```



In Magma:

```
sage: R.<T> = GF(71)[]; K.<T> = FractionField(R); a=(T^3+T-1)*(T^2-2); b=(3*T^5-T+7)*(T^2-2)
sage: aa=magma(a); bb=magma(b)
sage: magma.eval('a:=%s;b:=%s;'%(aa.name(),bb.name()))
sage: magma.eval('time v := [a/b+b/a : i in [1..10^5]];')
'Time: 0.800'
sage: magma.eval('time v := [a*b : i in [1..10^5]];')
'Time: 0.320'
sage: magma.eval('time v := [(1/a) * (1/b) : i in [1..10^5]];')
'Time: 0.830'
```


Something surprising is that working in your rational function field is much faster than working with polynomials!

```
sage: R.<T> = GF(71)[];  a=(T^3+T-1)*(T^2-2); b=(3*T^5-T+7)*(T^2-2)
sage: time v=[a*b for i in range(10^5)]
CPU times: user 2.02 s, sys: 0.00 s, total: 2.02 s
Wall time: 2.02 s
```



---

Comment by was created at 2010-07-15 15:49:31

Before the patch... 79 seconds instead of the new 2.9 seconds:

```

sage: sage: time v=[a/b+b/a for i in range(10^5)]
CPU times: user 78.91 s, sys: 0.15 s, total: 79.06 s
Wall time: 79.05 s
```



---

Attachment

apply this after the "everything flattened" patch directly above.


---

Comment by was created at 2010-07-15 17:36:28

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2010-07-16 02:10:08

Reviewer patch looks good to me. My only comment is that it would be nice to have a faster not-equals comparison, but that's not worth holding this up.


---

Comment by mpatel created at 2010-07-20 09:28:45

I've merged only

 * [attachment:trac_9051-everything_flattened.patch]
 * [attachment:trac_9051-referee-1.patch]

in 4.5.2.alpha0.  Please correct the Author(s) and Reviewer(s) fields, if I'm wrong.


---

Comment by mpatel created at 2010-07-20 09:28:45

Resolution: fixed


---

Comment by jdemeyer created at 2013-01-18 08:10:25

I assume that it's a mistake that the function

```
def fraction_field(self):
```

was added _twice_ in `sage/rings/polynomial/polynomial_ring.py`


---

Comment by jdemeyer created at 2013-01-19 11:22:23

Please review #13971 to correct this duplicate method.
