# Issue 6045: [with patch, needs review] Computation of Heegner points

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-05-15 09:59:52

Assignee: was

CC:  was

Adds Heegner point method to elliptic curves over Q. Also cleans up the modular parametrization code.

This ticket is almost certainly related: #4849


---

Comment by robertwb created at 2009-05-16 03:11:29

I just looked at this and realized I can't just lift_x, I need to pick the right one. That should be easy given I have it embedded into C.


---

Comment by robertwb created at 2009-06-06 06:30:41

Fixed the lifting issue, ready for review.


---

Comment by ncalexan created at 2009-06-06 20:26:24

This code isn't ready for primetime, even with the lifting issue fixed, because increasing the precision until algdep succeeds is a recipe for disaster.  Maybe a bound on the number of precision increases?


---

Comment by robertwb created at 2009-06-06 23:05:06

There is a bound on how often it increases precision--in fact it's even one of the parameters (max_prec).


---

Comment by ncalexan created at 2009-06-06 23:13:23

Sorry, totally asleep at the wheel.  This looks good to me, but I'm not expert in the genus 1 case.  Maybe was can be the final word?


---

Comment by cremona created at 2009-06-14 17:32:35

I'm intending to try this and review it since I have implemented similar in C++ and in gp.


---

Comment by cremona created at 2009-06-14 17:58:06

REVIEW:  I applied this to 4.0.1, but got some doctest failures:

```
sage -t  "devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py"
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 5248:
    sage: E._heegner_best_tau(-7)
Expected:
    (sqrt(7)*I - 17)/74
Got:
    1/74*sqrt(-7) - 17/74
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 5250:
    sage: EllipticCurve('389a')._heegner_best_tau(-11)
Expected:
    (sqrt(11)*I - 355)/778
Got:
    1/778*sqrt(-11) - 355/778
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 5291:
    sage: P = E.heegner_point(-40); P
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_115[5]>", line 1, in <module>
        P = E.heegner_point(-Integer(40)); P###line 5291:
    sage: P = E.heegner_point(-40); P
      File "/home/john/sage-4.0.1/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 5335, in heegner_point
        raise ValueError, "Not enough precision (%s) to get heegner point exactly, try passing a larger max_prec." % (prec)
    ValueError: Not enough precision (2000) to get heegner point exactly, try passing a larger max_prec.
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 5301:
    sage: f = algdep(P[0], 5); f
Expected:
    x^5 + 2*x^4 + x^3 - x^2 - x - 1
Got:
    x^5 - x^4 + x^3 + x^2 - 2*x + 1
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 6825:
    sage: phi(CC.0)
Expected:
    (-2.04158222510587 + 3.21664059900000e-29*I : -0.500000000000000 + 0.0906126752327350*I : 1.00000000000000)
Got:
    (287826.309565255 : -1.54417490329940e8 : 1.00000000000000)
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 3114:
    sage: X,Y=E.modular_parametrization()
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_70[3]>", line 1, in <module>
        X,Y=E.modular_parametrization()###line 3114:
    sage: X,Y=E.modular_parametrization()
    TypeError: iteration over non-sequence
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 3115:
    sage: X
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_70[4]>", line 1, in <module>
        X###line 3115:
    sage: X
    NameError: name 'X' is not defined
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 3117:
    sage: Y
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_70[5]>", line 1, in <module>
        Y###line 3117:
    sage: Y
    NameError: name 'Y' is not defined
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 3122:
    sage: q = X.parent().gen()
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_70[6]>", line 1, in <module>
        q = X.parent().gen()###line 3122:
    sage: q = X.parent().gen()
    NameError: name 'X' is not defined
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 3123:
    sage: E.defining_polynomial()(X,Y,1) + O(q^11) == 0
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_70[7]>", line 1, in <module>
        E.defining_polynomial()(X,Y,Integer(1)) + O(q**Integer(11)) == Integer(0)###line 3123:
    sage: E.defining_polynomial()(X,Y,1) + O(q^11) == 0
    NameError: name 'X' is not defined
**********************************************************************
File "/home/john/sage-4.0.1/devel/sage-tests/sage/schemes/elliptic_curves/ell_rational_field.py", line 3133:
    sage: f/q == (X.derivative()/(2*Y+a1*X+a3))
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-4.0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_70[11]>", line 1, in <module>
        f/q == (X.derivative()/(Integer(2)*Y+a1*X+a3))###line 3133:
    sage: f/q == (X.derivative()/(2*Y+a1*X+a3))
    NameError: name 'X' is not defined
**********************************************************************
4 items had failures:
   2 of   5 in __main__.example_114
   2 of  11 in __main__.example_115
   1 of   5 in __main__.example_137
   6 of  12 in __main__.example_70
***Test Failed*** 11 failures.
For whitespace errors, see the file /home/john/sage-4.0.1/tmp/.doctest_ell_rational_field.py
	 [85.3 s]
exit code: 1024
```


This is on a 32-bit machine -- possibly the problem?

Note -- I'm planning to implement a better weierstrass function, calling the pari library.  In fact I already did that, got stuck on precision problems, then deleted that branch by mistake so it is back to square one.

Also, for recognising the points, what I have always done is compute all the conjugates (not quite all, I do one from each complex conjugate pair) and then add them up (on C mod the lattice) before applying Weierstrass.  I have never tried to recognise the points as points defined over the Hilbert class field.


---

Comment by robertwb created at 2009-06-17 06:19:28

Some of these are due to new symbolics printing differently, others may be due to different choices of root (it was developed on Sage < 4.0). I'll rebase and see what's up.


---

Attachment

OK, I fixed the patch. As well as the symbolics printing changes, I had moved some doctests around and got some of them associated with the wrong output. Based on 4.0.2, ready to be looked at again.


---

Comment by cremona created at 2009-06-23 20:04:50

Robert, can I suggest that we first get #6386 approved (e.g. by you reviewing it) as then your step of going from z mod period lattice to E(CC) can be done much better than your explicit use of pari/gp?  (I do use pari behind the scene of course).  I think that might be better than reviewing this now and then patching it again later.  john


---

Comment by robertwb created at 2009-06-25 03:42:15

That's a clever way of getting someone to review your work :). Actually, I was planning on looking at your elliptic exponential function anyways, so I'll go review that (and modify this to use it, under the very safe assumption that it's good).


---

Comment by cremona created at 2009-06-25 08:40:42

Replying to [comment:13 robertwb]:
> That's a clever way of getting someone to review your work :). Actually, I was planning on looking at your elliptic exponential function anyways, so I'll go review that (and modify this to use it, under the very safe assumption that it's good). 

I hoped you would not mind.  It was seeing that code in your patch which spurred me to get mine working properly.  It seems that for some of these wrapped functions (particularly the pari ones), there are two distinct layers:  the basic wrapper (here in gen.pyx), use of which directly requires careful study of the pari manual;  and a proper Sage function, well documented and *not* requiring any knowledge of the deeper library.


---

Comment by robertwb created at 2009-06-26 04:47:44

Depends on #6386.


---

Comment by robertwb created at 2009-06-26 06:12:39

apply on top of previous


---

Attachment

NB this requires #6386.  Applies fine to 4.1.alpha2 + the four patches there.  Tests in ell_rational_field pass.

Modular param: type "and and" in a comment.

Heegner:  typo "give" -> "given" in 2 or 3 places in docstrings.  Why
do you reverse the order of summation of a_n/n?  Can you sum the
series using an iterator for the an instead of forming the whole list?

 _heegner_forms_list: (this only depends on N and D so could perhaps be
 factored out of the class to a stand-alone function).

More seriously, this function is *wrong*!  (Though in a way which does
not matter for the use which is made of it here so far.)  The point is
this:  To get a complete set of forms you need to choose *one* sqrt of
D mod 4*N and use the same b for all the forms.  Otherwise the points
you get are not Galois conjugate.  [Changing b to another sqrt amounts
to applying to the point in the upper half plane one of the
Atkin-Lehner involutions.  This has two effects: firstly, it may
change the sign of the integral (depending on the A-L eigenvalue;
secondly, it maps \infty to another cusp, hence adds a torsion point
to the Heegner point.  So instead of getting come conjugate point P
you get either P+T or -P+T with T torsion.  The reason that this does
not make the rest of the code wrong here is that you only actually use
one of the forms (the one with smallest a to get best accuracy) and
then use algdep.  But we should have code that could in principal
deliver a set of Galois conjugate points.

To get around this:  try all the sqrt of D mod 4*N;  for each, try to
find a complete set of forms with that same b.  If that fails, either
look at another b, or choose a different lift of b from Z/2N to Z
(since larger b's will give more possible forms).  I implemented this
in gp ages ago, so I have gp code which does this!

Future work: one useful application of Heegner points is to find
rational points on curves of rank 1.   I have been doing this
successfully for years, and in 2005 work of Delaunay and Watkins made
it vastly more efficient.  That excellent efficient version found its
way into Magma (thanks for Mark) and it would be good to get something
as good in Sage.  The idea is to compute all the complex z (mod period
lattice L) for a complete set of forms, then take the trace by adding
those up (as complex numbers) before mapping to the curve, at which
point you only need to recognise the coordinates as rational numbers.
You can use the action of complex conjugation on the forms to halve
the number of evaluations (and in each pair can choose the smallest
a).  The Delaunay-Watkins improvement allows to use even smaller a,
and I can explain further if asked!

Lastly:  I tried 873b1 and D=-11, which works fine, though the point constructed has height 14.785 but the heegner_point_height function returns double that.  This might need a different ticket.


---

Comment by was created at 2009-06-28 21:43:29

> Lastly: I tried 873b1 and D=-11, which works fine, though the point constructed 
> has height 14.785 but the heegner_point_height function returns double that. 
> This might need a different ticket. 

Heegner points are naturally defined over K, and the height over K is *double* the height over Q.   In general, if P in E(Q) and L is a number field, then `[L:Q]*h_Q(P) = h_L(P)`


---

Comment by cremona created at 2009-06-28 21:50:58

Replying to [comment:17 was]:
> > Lastly: I tried 873b1 and D=-11, which works fine, though the point constructed 
> > has height 14.785 but the heegner_point_height function returns double that. 
> > This might need a different ticket. 
> 
> Heegner points are naturally defined over K, and the height over K is *double* the height over Q.   In general, if P in E(Q) and L is a number field, then `[L:Q]*h_Q(P) = h_L(P)`

OK, I stand corrected!   I'm just used to computing rational Heegner points (via the trace) so that had not occurred to me.


---

Comment by robertwb created at 2009-06-29 16:32:19

Thanks for the feedback--I'll take a look at `_heegner_forms_list`. 

We're interested in computing Heegner points for rank >= 2 elliptic curves, and of course by the Gross-Zagier theorem their traces down to Q are always torsion. However, I agree it would be useful to have a "trace" option to trace it down (via summation in the lattice) as well.


---

Attachment


---

Comment by robertwb created at 2009-07-01 08:50:03

Replying to [comment:16 cremona]:

> Modular param: type "and and" in a comment.

Not sure what you meant by this...

> Why do you reverse the order of summation of a_n/n?  

Because there's less rounding error by starting with the tail. 


```
sage: E = EllipticCurve('37a')
sage: tau = E._heegner_best_tau(-7, prec=100)
sage: r1 = sum([an/(m+1)*tau**(m+1) for m, an in enumerate(E.anlist(100))])
sage: r2 = sum(reversed([an/(m+1)*tau**(m+1) for m, an in enumerate(E.anlist(100))]))
sage: tau500 = E._heegner_best_tau(-7, prec=500)
sage: r = sum([an/(m+1)*tau500**(m+1) for m, an in enumerate(E.anlist(100))])
sage: (r1-r)
9.8607613152626475676466070660e-32 - 3.6977854932234928378674776498e-32*I
sage: (r2-r)
2.4651903288156618919116517665e-32*I
```


Not that that's really much of a difference... 

> Can you sum the series using an iterator for the an instead of forming the whole list?

There's not a way to get the `a_n` as an iterator rather than a list. FYI, I do plan on optimizing this part a lot more. 

> 
>  _heegner_forms_list: (this only depends on N and D so could perhaps be
>  factored out of the class to a stand-alone function).

Perhaps, although I couldn't think of a better place to put it (one advantage of having it there is it's defined close to where it's used). 

> More seriously, this function is *wrong*!  

I was thinking of this as the `H_N^D` rather than the `H_N^D(\beta)` from Mark Watkins "Some Remarks on Heegner Point Computations," though I see that it may not have been a complete set. 

I not make it take the chosen square root as a parameter, and it returns all the forms associated to that square root. I'm actually not using this function right now (as I only want a single surd to recover the Heegner point over the Hilbert Class Field) but it will be valuable when implementing computation of the Heegner point traced down to Q (which we should definitely have n optimized version of in Sage).


---

Comment by cremona created at 2009-07-03 11:54:16

Final review:  Sorry about the first one, I meant to say that in the comment now in line 7026 "the the" should be "the".

One small thing I found:

```
sage: E=EllipticCurve([1,0,0,-1,0]) 
sage: [E.heegner_point(D) for D in E.heegner_discriminants_list(3)]
...
/home/jec/sage-4.1.alpha3/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in _heegner_best_tau(self, D, prec)
   5353         N = self.conductor()
   5354         b = ZZ(Integers(4*N)(D).sqrt(extend=False) % (2*N))
-> 5355         return (-b + D.sqrt(prec=prec)) / (2*N)
   5356
   5357     def heegner_point(self, D, prec=None, max_prec=2000):

AttributeError: 'int' object has no attribute 'sqrt'
```


The function  _heegner_best_tau() needs to coerce D into ZZ before calling D.sqrt().  I think some other functions might do well to make D into a ZZ as well.

Otherwise I am happy.


---

Attachment

Apply all four patches.


---

Comment by cremona created at 2009-07-09 11:53:50

This looks ok now.  I applied it to 4.1.alpha3 + patches from #6386.  Tests pass.  Assuming that it's still ok with rc0 this can go in now.


---

Comment by mvngu created at 2009-07-16 10:10:08

I'm getting numerical noise when running all doctests:

```
sage -t -long devel/sage-exp/sage/schemes/elliptic_curves/ell_rational_field.py
/scratch/mvngu/release/sage-4.1.1/local/lib/python/site-packages/sage/misc/misc.py:1901: DeprecationWarning: functions overriding warnings.showwarning() must support the 'line' argument
  warn(message, DeprecationWarning, stacklevel=3)
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-exp/sage/schemes/elliptic_curves/ell_rational_field.py", line 6989:
    sage: phi((sqrt(7)*I - 17)/74, 53)
Expected:
    (-3.37746093871080e-16 - 2.21824021705058e-16*I : 3.33066907387547e-16 + 2.21719344273286e-16*I : 1.00000000000000)
Got:
    (-3.37704345632016e-16 - 2.21996076934245e-16*I : 3.33066907387547e-16 + 2.22044604925031e-16*I : 1.00000000000000)
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_141
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_ell_rational_field.py
	 [257.8 s]

<SNIP>

----------------------------------------------------------------------

The following tests failed:

	sage -t -long devel/sage-exp/sage/schemes/elliptic_curves/ell_rational_field.py # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 504.7 seconds
```



---

Attachment

Noise issue fixed.


---

Comment by mvngu created at 2009-07-20 15:48:26

Resolution: fixed


---

Comment by mvngu created at 2009-07-20 15:52:58

Ticket #4849 has been closed as a duplicate of this ticket.
