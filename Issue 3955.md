# Issue 3955: make find_minimum_on_interval use _fast_float_

Issue created by migration from https://trac.sagemath.org/ticket/3955

Original creator: was

Original creation time: 2008-08-26 09:12:29

Assignee: tbd


```


On Tue, Aug 26, 2008 at 2:07 AM, Stan Schymanski <schymans@gmail.com> wrote:
>
> Dear William,
>
> On Aug 25, 6:48 pm, "William Stein" <wst...@gmail.com> wrote:
>
>> If you call _fast_float_ as illustrated below on your functions, find_* will
>> work, and also be much much faster:
>>
>> sage: find_maximum_on_interval((-x^2)._fast_float_(x),-1,1)
>> (-7.7037197775489434e-34, -2.77555756156e-17)
>> sage: find_minimum_on_interval((-x^2)._fast_float_(x),-1,1)
>> (-0.99999992595132459, -0.999999962976)
>>
>> find_* doesn't do this already since (1) _fast_float_ was written
>> after find_*, and (2) nobody has had the time to change find_*
>> to use _fast_float_.
>
> That's amazing, thank you! I didn't find any information about the
> _fast_float_. Can it be used for other purposes, too?

Yes.  It takes any polynomial or symbolic expression and turns
it into a very fast callable function that has input and output floats.
It should get used automatically by functions like find_min* but
we haven't pushed this through enough yet. 
```



---

Comment by was created at 2008-08-26 09:12:38

Changing component from algebra to calculus.


---

Comment by was created at 2008-08-26 09:12:38

Changing assignee from tbd to burcin.


---

Comment by jwmerrill created at 2008-09-02 02:30:34

fast_float doesn't look like a win here in 3.1.2.alpha2, at least not in the cases I tried


```
sage: timeit('find_minimum_on_interval(x*sin(x)^2,3,3.4)')
25 loops, best of 3: 24.5 ms per loop
sage: sage: timeit('find_minimum_on_interval((x*sin(x)^2)._fast_float_(x),3,3.4)')
5 loops, best of 3: 109 ms per loop

# not sure what goes wrong here
sage: find_maximum_on_interval(-x^2,-1,1)
Traceback (most recent call last):
...
TypeError: cannot coerce type '<class 'sage.calculus.equations.SymbolicEquation'>' into a SymbolicExpression.

sage: timeit('(-x^2).find_maximum_on_interval(-1,1)')
5 loops, best of 3: 22.4 ms per loop
sage: timeit('find_maximum_on_interval((-x^2)._fast_float_(x),-1,1)')
5 loops, best of 3: 61.5 ms per loop
```



---

Comment by jwmerrill created at 2008-09-02 02:37:49

I guess what is going on is that the time to compile the function to fast_float form swamps the time to find the minimum, at least in these cases.


```
sage: timeit('f = (-x^2)._fast_float_()')
5 loops, best of 3: 82.6 ms per loop
sage: timeit('find_maximum_on_interval(f,-1,1)')
625 loops, best of 3: 690 µs per loop
```



---

Comment by jwmerrill created at 2008-09-02 03:07:25

I notice that fast_float was sneaked into find_root in the first patch at #2703, which was nominally a doctest coverage patch.  It doesn't look like any kind of benchmarking was done there.


---

Comment by jwmerrill created at 2008-09-02 03:08:35

Oops, it was #2073.


---

Comment by jwmerrill created at 2008-09-02 06:26:15

See #3622 for a discussion of timings with fast_float.  Based on that discussion, this probably is worth doing.


---

Comment by aginiewicz created at 2012-06-09 09:53:42

It seems that both forms of find_minimum_on_interval use fast_float now (sage/symbolic/expression.pyx:8398 and sage/numerical/optimize.py:181) but only one form of find_maximum_on_interval does, i.e. the f.find_maximum_on_interval(a,b) (sage/symbolic/expression.pyx:8339). find_maximum_on_interval(f, a, b) does not.

I'm testing a patch for this and will be uploading it in a short while.


---

Comment by aginiewicz created at 2012-06-09 10:16:09

Changing status from new to needs_review.


---

Comment by novoselt created at 2012-06-10 07:49:45

I'll be happy to review this if it is rebased on top of #2607.

It would be great also if you approve my last changes on that ticket which were implementing your suggestion of dropping "_on_interval".


---

Comment by aginiewicz created at 2012-06-24 10:32:34

Due to number of inevitable changes in #2607 and fact, that's it is ready for review with reviewers comments fixed, I already rebased this patch on top of it and added it to dependencies. This patch also looks cleaner on top of it.


---

Comment by jdemeyer created at 2012-07-27 20:43:07

Please fill in your real name as Author.


---

Comment by aginiewicz created at 2012-07-27 20:58:04

Ah, forgot about that. Thanks for reminder, done now.


---

Attachment

rebased on v5.4


---

Comment by tkluck created at 2012-12-23 21:01:04

This should just be applied. I rebased it on 5.4.

Setting to positive-review.


---

Comment by tkluck created at 2012-12-23 21:01:04

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-12-23 21:04:22

Why the milestone change?


---

Comment by ppurka created at 2012-12-24 07:08:10

Is anyone working with very large numbers, or is there any doctest which checks for very large numbers? Because this patch might affect the result. See #13559.

Patchbot: apply trac3955-find_local_maximum-ff.2.patch


---

Comment by tkluck created at 2012-12-24 10:18:34

jdemeyer: sorry about the milestone change, I didn't realize 5.5 was already in the RC stage.

ppurka: if I understand it correctly, all the other `find_{min,max}imum_on_interval` functions have already been changed to use `fast_float`. So already from a consistency point of view, this one should be, too.

Of course, you still have a point. Especially since before, you could always manually pass a `fast_float` function if you needed the speedup, but now you cannot disable that feature if you need the precision.

Maybe there should be something like a safe version of fast float, that checks its results for `NaN` or `Inf` and if so, redoes the calculation with the original expression.

I think that this patch should still be applied for consistency. Maybe such a safe version of `fast_float` could be the solution to #13559?


---

Comment by ppurka created at 2012-12-24 17:57:26

Ok. If it is improving consistency, then let it be. The bug in #13559 is less about safety and more about allowing `fast_float` to work with higher precision. `@`kcrisman there asks whether it is possible to make `fast_float` not just behave like python float, but be able to handle even larger numbers.


---

Comment by jdemeyer created at 2012-12-27 11:42:17

In the future, make sure the "apply" instructions in the ticket description remain up-to-date.


---

Comment by jdemeyer created at 2012-12-29 19:32:12

Resolution: fixed
