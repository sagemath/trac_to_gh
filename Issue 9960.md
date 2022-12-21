# Issue 9960: Allow assumptions on the dependent variable in desolve

Issue created by migration from Trac.

Original creator: robert.marik

Original creation time: 2010-09-21 19:29:55

Assignee: burcin

Sage should be able to solve ODE

```
x*diff(y,x)-x*sqrt(y^2+x^2)-y == 0
```

under assumptions 

```
x>0,y>0
```


Now 

```
y=function('y',x)
assume(y>0)
```

passes

```
assume(y(x)>0)
```

to Maxima. As a consequence, Maxima asks on sign of y. This should be fixed,



---

Comment by robert.marik created at 2010-09-21 19:35:21

The patch fixes the problem, but we use strings in new optional argument of desolve. Some better suggestions are wellcomed.


---

Attachment


---

Comment by robert.marik created at 2010-09-21 19:52:25

The patch depends on #9961 which runs all commands in one Maxima session.


---

Comment by robert.marik created at 2010-09-21 20:05:03

Oops, I mean #9835 :)
Replying to [comment:2 robert.marik]:
> The patch depends on #9961 which runs all commands in one Maxima session.


---

Comment by robert.marik created at 2010-09-21 20:05:03

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-09-21 20:17:17

I appreciate the sentiment and idea, but adding a keyword exposes us to backwards incompatibility if someone (me?) ever gets to making the assumption system better - at least, that's my gut reaction.  What do you think?


---

Attachment

apply only this patch


---

Comment by burcin created at 2010-09-21 21:06:46

I was just thinking the same thing about the extra option. If we go with that option, the documentation should state clearly that this is a temporary solution.

On the other hand, attachment:trac_9961-assume_function.patch might provide an alternative option. I don't have much time so I didn't run tests or anything. Feel free to finish it up if you think it makes sense.


---

Attachment

apply only this patch


---

Comment by burcin created at 2010-09-22 16:07:58

I uploaded a new patch attachment:trac_9961-assume_function.take2.patch. The previous version caused doctest failures like:


```
File "/home/burcin/sage/sage-4.5.2.rc0/devel/sage-s/sage/calculus/wester.py", line 386:
    sage: assume(real(x) > 0, real(y) > 0)
Exception raised:
    Traceback (most recent call last):
      File "/home/burcin/sage/sage-4.5.2.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[131]>", line 1, in <module>
        assume(real(x) > Integer(0), real(y) > Integer(0))###line 386:
    sage: assume(real(x) > 0, real(y) > 0)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/symbolic/assumptions.py", line 357, in assume
        x.assume()
      File "expression.pyx", line 1214, in sage.symbolic.expression.Expression.assume (sage/symbolic/expression.cpp:6320)
    ValueError: Assumption is redundant
```


or 


```
File "/home/burcin/sage/sage-4.5.2.rc0/devel/sage-s/sage/symbolic/expression.pyx", line 7691:
    sage: (a*q^k).sum(k, 0, oo)
Exception raised:
    Traceback (most recent call last):
      File "/home/burcin/sage/sage-4.5.2.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_170[21]>", line 1, in <module>
        (a*q**k).sum(k, Integer(0), oo)###line 7691:
    sage: (a*q^k).sum(k, 0, oo)
      File "expression.pyx", line 7717, in sage.symbolic.expression.Expression.sum (sage/symbolic/expression.cpp:30994)
        Mathematica, so even if the chosen backend can perform the summation the
      File "/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/calculus/calculus.py", line 503, in symbolic_sum
        result = maxima.simplify_sum(sum)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/interfaces/expect.py", line 1387, in __call__
        return self._parent.function_call(self._name, list(args), kwds)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/interfaces/expect.py", line 1322, in function_call
        return self.new(s)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/interfaces/expect.py", line 1097, in new
        return self(code)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/interfaces/expect.py", line 1032, in __call__
        return cls(self, x, name=name)
      File "/home/burcin/sage/sage-4.5.2.rc0/local/lib/python/site-packages/sage/interfaces/expect.py", line 1457, in __init__
        raise TypeError, x
    TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(abs(q)-1>0)' before integral or limit evaluation, for example):
    Is  abs(q)-1  positive, negative, or zero?
```


This patch restricts the special treatment to user defined functions.

This passes all the symbolics related doctests, I think it's ready for review.


---

Comment by robert.marik created at 2010-09-23 15:52:30

Looks good for me, all tests passes.

Apply only attachment:trac_9961-assume_function.take2.patch and apply it on the top of #9835 

I would give positive review, but probably kcrisman should also look on the patch.


---

Comment by kcrisman created at 2010-09-23 17:31:59

I don't have time to give testing this the TLC it deserves, so I think the two of you should decide if you approve of each other's contributions.    However, it probably would be nice if we checked in the patch whether #9961 was actually fixed, like it does in Robert's patch!  If you can think of any other way to doctest this it would be nice.  Does it slow anything up very much?


---

Comment by kcrisman created at 2010-09-23 17:31:59

Changing status from needs_review to needs_work.


---

Attachment

Burcin's patch with doctest. Apply only this patch.


---

Comment by robert.marik created at 2010-09-23 17:45:41

Changing status from needs_work to needs_review.


---

Comment by robert.marik created at 2010-09-23 17:45:41

Oops, I actually tested Burcin's patch with one doctest added. This new patch is 
attachment:trac_9961-assume_function.take3.patch

Agree that each closed ticket must be doctested. Hope, everything is O.K. now. Burcin, can you review my changes in your patch?


---

Comment by burcin created at 2010-09-23 21:32:45

Of course there should be a doctest for the issue reported. Thanks for catching that Karl-Dieter.

Robert, thank you for fixing my patch and adding the doctest.

I'm changing this to a positive review, in light of comment:7 from Robert Marik and comment:8 from Karl-Dieter Crisman.


---

Comment by burcin created at 2010-09-23 21:32:45

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-28 09:11:50

Resolution: fixed
