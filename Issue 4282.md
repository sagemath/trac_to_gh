# Issue 4282: [with patch, needs review] symbolic minpoly

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-10-14 14:18:11

Assignee: burcin

The current minpoly algorithm on symbolic objects is slow and often fails. This patch makes it work in many more cases, as well as implementing better conversion into QQbar. 




---

Attachment

It's still not super fast, but it's a lot better. Perhaps working with resultants directly could be faster (or improving QQbar's implementation, though I'm not sure how much is overhead vs. being a hard computational problem).


---

Comment by mhampton created at 2008-10-24 03:23:58

There's a problem that comes up testing this, which may be something the improved doctests are exposing rather than causing:


```
sage: sin(pi/7).minpoly()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/mh/sagestuff/sage-3.1.4/<ipython console> in <module>()

/Users/mh/sagestuff/sage-3.1.4/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in minpoly(self, *args, **kwds)
   1343         from sage.rings.all import QQbar
   1344         try:
-> 1345             return QQbar(self).minpoly()
   1346         except TypeError, ValueError:
   1347             return self.minpoly_numeric(*args, **kwds)

/Users/mh/sagestuff/sage-3.1.4/local/lib/python2.5/site-packages/sage/rings/qqbar.pyc in __call__(self, x)
    661             return AlgebraicNumber(x._descr)
    662         elif hasattr(x, '_algebraic_'):
--> 663             return x._algebraic_(QQbar)
    664         return AlgebraicNumber(x)
    665 

/Users/mh/sagestuff/sage-3.1.4/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in _algebraic_(self, field)
   6432                 res = mag * QQbar.zeta(rat_arg.denom())**rat_arg.numer()
   6433             elif func_name in ['sin', 'cos', 'tan']:
-> 6434                 exp_ia = exp(SR(-1).sqrt()*operand)._algebraic_(QQbar)
   6435                 if func_name == 'sin':
   6436                     res = (exp_ia - ~exp_ia)/(2*QQbar.zeta(4))

AttributeError: 'SymbolicConstant' object has no attribute 'sqrt'

```



---

Comment by robertwb created at 2008-11-03 21:47:52

Ah. That should be an easy fix... (must have fixed it in my branch elsewhere, perhaps in the process of #4276)


---

Attachment


---

Comment by robertwb created at 2008-11-13 23:12:53

I fixed the above bug.


---

Comment by was created at 2008-11-27 16:56:24

Referee report:

I applied the patch to sage-3.2.1.alpha2. 

1. A doctest fails in calculus.py:

```
sage -t  devel/sage/sage/calculus/calculus.py
**********************************************************************
File "/home/was/build/sage-3.2.1.alpha1/devel/sage-main/sage/calculus/calculus.py", line 1337:
    sage: sin(pi/7).minpoly()
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_43[5]>", line 1, in <module>
        sin(pi/Integer(7)).minpoly()###line 1337:
    sage: sin(pi/7).minpoly()
      File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 1345, in minpoly
        return QQbar(self).minpoly()
      File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/qqbar.py", line 663, in __call__
        return x._algebraic_(QQbar)
      File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 6471, in _algebraic_
        exp_ia = exp(SR(-1).sqrt()*operand)._algebraic_(QQbar)
      File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 6460, in _algebraic_
        rat_arg = (operand.imag()/(2*self.parent().pi()))._rational_()
    AttributeError: 'SymbolicExpressionRing_class' object has no attribute 'pi'
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_43
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/was/build/sage-3.2.1.alpha1/tmp/.doctest_calculus.py

         [114.8 s]

The following tests failed:

        sage -t  devel/sage/sage/calculus/calculus.py # 1 doctests failed
```


2. This sentence sounds like nonsense:

```
 	1335	        NOTE: Failure of this function does not prove self is 
 	1336	              not algebraic.  
```


3. There are now only three boring tests of symbolic minpoly. All the old interesting tests are now tests of minpoly_numeric.  I think all the minpoly_numeric tests should *also* be copied to the docstring for minpoly and tested using the new non-numerical algorithm.


---

Comment by robertwb created at 2008-12-03 01:21:41

On point (3), should I simply consolidate minpoly_numeric into minpoly, or is it better to keep these two functions separate?


---

Comment by was created at 2008-12-04 22:15:45

> On point (3), should I simply consolidate minpoly_numeric into minpoly, or is 
> it better to keep these two functions separate? 

I think there should be one function the users sees called "minpoly" and it has an algorithm flag.  

 sage: foo.minpoly(algorithm='numerical')
 sage: foo.minpoly()
 sage: foo.minpoly(algorithm='something else clever...')

William


---

Comment by robertwb created at 2008-12-07 09:11:21

Changing assignee from burcin to robertwb.


---

Comment by robertwb created at 2008-12-07 09:11:21

OK, I believe I've addressed all the points above, and I expanded the documentation a bit more too.


---

Comment by was created at 2008-12-07 19:09:32

There are several mistakes in English in the new documentation that you added:

 * "Note that simplification may be necessary to see the minimal polynomial is correct."  -- missing word "if"

 * " If these are known, the numerical algorithm will be faster when these are give them explicitly." -- HUH?

 * "use PARI's algdep to get a to get a candidate minpoly $f$." -- delete doubled "to get a".

 * "Otherwise raise an error." -- say which exception is raised

 * "Note that simplification may be necessary to see the minimal polynomial is correct." -- missing word "if".


---

Attachment

I made these changes and refreshed the patch. On your first (= last) point, I prefer the word "that" as there is no question of whether or not the result is correct, it just may not be obvious without the right simplification.


---

Comment by ncalexan created at 2008-12-09 19:46:01

I do not like that 'algebraic' and 'numerical' are not parallel constructions -- the parallel construction *WHICH APPEARS IN SOME OF THE DOCTESTS!* is 'algebraic' and 'numeric'.  I have attached a patch which fixes the doctests but doesn't change it to 'numeric'.  The patch does try to help the user -- instead of testing algorithm='numerical' it tests if algorithm starts with 'numeric'.

I like the results and the performance:

With patch:

```
sage: cos(pi/22).minpoly()
x^10 - 11/4*x^8 + 11/4*x^6 - 77/64*x^4 + 55/256*x^2 - 11/1024
sage: cos(pi/56).minpoly()
x^24 - 6*x^22 + 63/4*x^20 - 95/4*x^18 + 5813/256*x^16 - 917/64*x^14 + 3081/512*x^12 - 847/512*x^10 + 9323/32768*x^8 - 459/16384*x^6 + 175/131072*x^4 - 3/131072*x^2 + 1/16777216
```


Without patch:


```
sage: cos(pi/22).minpoly()
Traceback (most recent call last):
...
NotImplementedError: Could not prove minimal polynomial x^10 - 11/4*x^8 + 11/4*x^6 - 77/64*x^4 + 55/256*x^2 - 11/1024 (epsilon 3.14321532602626e-100)
sage: cos(pi/56).minpoly()
Traceback (most recent call last):
...
NotImplementedError: Could not prove minimal polynomial x^24 - 6*x^22 + 63/4*x^20 - 95/4*x^18 + 5813/256*x^16 - 917/64*x^14 + 3081/512*x^12 - 847/512*x^10 + 9323/32768*x^8 - 459/16384*x^6 + 175/131072*x^4 - 3/131072*x^2 + 1/16777216 (epsilon 2.29367823690213e-400)
```


With patch:

```
sage: %timeit sqrt(5).minpoly()
100 loops, best of 3: 14.3 ms per loop
sage: %timeit sqrt(sqrt(5)).minpoly()
10 loops, best of 3: 54 ms per loop
sage: %timeit sqrt(sqrt(5) + sqrt(2)).minpoly()
10 loops, best of 3: 115 ms per loop
```


Without patch:


```
sage: %timeit sqrt(5).minpoly()
10 loops, best of 3: 150 ms per loop
sage: %timeit sqrt(sqrt(5)).minpoly()
10 loops, best of 3: 174 ms per loop
sage: %timeit sqrt(sqrt(5) + sqrt(2)).minpoly()
10 loops, best of 3: 218 ms per loop
```



---

Attachment


---

Comment by robertwb created at 2008-12-09 20:00:57

Thanks. 

I heartily agree with your change of "numerical" -> "numeric" (that's what I had originally, can't remember what the reason was for changing it).


---

Comment by mabshoff created at 2008-12-10 07:56:49

Resolution: fixed


---

Comment by mabshoff created at 2008-12-10 07:56:49

Merged all four patches in Sage 3.2.2.alpha1


---

Comment by mabshoff created at 2008-12-10 08:13:25

Note that trac_4282_part2_sqrt-fix.patch went in with quite a bit of offset, so hopefully this is cause by other changes to calculus.py and not a merge snafu:

```
sage-3.2.2.alpha1/devel/sage$ hg import trac_4282_part2_sqrt-fix.patch
applying trac_4282_part2_sqrt-fix.patch
patching file sage/calculus/calculus.py
Hunk #2 succeeded at 8359 with fuzz 1 (offset 386 lines).
```

It builds and doctests pass, so I am confident hg did the right thing.

Cheers,

Michael
