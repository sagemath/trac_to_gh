# Issue 3587: calculus -- implement symbolic summation

Issue created by migration from https://trac.sagemath.org/ticket/3587

Original creator: was

Original creation time: 2008-07-07 15:52:57

Assignee: gfurnish

CC:  burcin jason

Maxima has good symbolic summation and it would be easy to wrap in the calculus package.
We are constantly getting stuff like this:

```
02:53 < nagyv> ﻿hello! how can I represent a summation in sage? like sum_{x=1}^N x, I would like to take the limit as N goes to infinity
03:02 < nagyv> what the heck is this? maxima.sum(1/x, x, 1, 2*N) gives 2*N/x! why?
```


Probably the only reason that this hasn't been done yet is the calculus rewrite by gfurnish.
That is *not* a good enough reason, and don't worry, the work won't be lost.


---

Comment by gfurnish created at 2008-07-07 17:43:51

I would like to add a +1 to this proposal as I'm not planning on implementing symbolic summation anytime in the near (or far) future, so I would be really happy if someone would work on this.


---

Comment by mhansen created at 2008-11-11 01:43:08

"sum" is probably the most appropriate name for this, but we'd have to make sure that it behaves the same way as Python's sum.


---

Comment by whuss created at 2009-06-04 14:15:14

Changing status from new to assigned.


---

Comment by whuss created at 2009-06-04 14:15:14

The attached patch adds a summation command which wraps simplify_sum from maxima.


---

Comment by whuss created at 2009-06-04 14:15:14

Changing assignee from gfurnish to whuss.


---

Comment by burcin created at 2009-06-05 13:25:08

Many thanks for the patch, this was long overdue. A few comments after reading your patch:

Your patch replicates the way integrate/integral works perfectly. Though, as Mike wrote in comment:3, we should just call this `sum`. There is also a discussion about naming here:

http://groups.google.com/group/sage-devel/browse_thread/thread/bd4eb3b613c98030

I suggest putting a `sum()` function in `sage.misc.misc_c`, that calls python's `sum()` or your function based on the type/number of the arguments. Would you like to do this or should I?

Here are some suggested changes:

 * rename all instances of the method to `sum` or `symbolic_sum`
 * you should import your function before the doctests in `calculus.py` to make sure you call the right function
 * it would be good to add a comment to #6197 pointing to the comment you have in `calculus.py`
 * you could add your code for converting MMA output back to Sage to a `_sage_()` method in `sage.interfaces.mathematica.MathematicaElement`, see the `MagmaElement` class in `sage.interfaces.magma` for an example, similarly for Maple output
 * In the last lines of the docstring for `sage.symbolic.expression.Expression.summation`, choosen -> chosen


In the long term, I would like to see `integral` and `sum` constructs as subclasses of `sage.symbolic.function.SFunction`, instead of the current thin wrappers around maxima functionality. I will take a look at the feasibility of doing this over the weekend. I don't want to hold your patch back for this though.


---

Comment by whuss created at 2009-06-06 17:12:52

Replying to [comment:5 burcin]:
> Many thanks for the patch, this was long overdue. A few comments after reading your patch:
> 
> Your patch replicates the way integrate/integral works perfectly. Though, as Mike wrote in comment:3, we should just call this `sum`. There is also a discussion about naming here:
> 
> http://groups.google.com/group/sage-devel/browse_thread/thread/bd4eb3b613c98030
> 
> I suggest putting a `sum()` function in `sage.misc.misc_c`, that calls python's `sum()` or your function based on the type/number of the arguments. Would you like to do this or should I?

It would be great if you could do this.

> Here are some suggested changes:
> 
>  * rename all instances of the method to `sum` or `symbolic_sum`
>  * you should import your function before the doctests in `calculus.py` to make sure you call the right function
>  * it would be good to add a comment to #6197 pointing to the comment you have in `calculus.py`
>  * you could add your code for converting MMA output back to Sage to a `_sage_()` method in `sage.interfaces.mathematica.MathematicaElement`, see the `MagmaElement` class in `sage.interfaces.magma` for an example, similarly for Maple output
>  * In the last lines of the docstring for `sage.symbolic.expression.Expression.summation`, choosen -> chosen

I will take care of these.
 
> 
> In the long term, I would like to see `integral` and `sum` constructs as subclasses of `sage.symbolic.function.SFunction`, instead of the current thin wrappers around maxima functionality.

This is definitely necessary. Currently there is no way to interact with an unevaluated integral or sum.

> I will take a look at the feasibility of doing this over the weekend. I don't want to hold your patch back for this though.


---

Attachment

Replying to [comment:5 burcin]: 
> Here are some suggested changes:
> 
>  * rename all instances of the method to `sum` or `symbolic_sum`
>  * you should import your function before the doctests in `calculus.py` to make sure you call the right function
>  * it would be good to add a comment to #6197 pointing to the comment you have in `calculus.py`
>  * you could add your code for converting MMA output back to Sage to a `_sage_()` method in `sage.interfaces.mathematica.MathematicaElement`, see the `MagmaElement` class in `sage.interfaces.magma` for an example, similarly for Maple output
>  * In the last lines of the docstring for `sage.symbolic.expression.Expression.summation`, choosen -> chosen

I posted a new patch that takes care of these issues.

The second patch (sum.patch) renames summation to sum. This currently overwrites the python sum command.


---

Attachment


---

Comment by mhansen created at 2009-06-20 01:54:02

I updated sum.patch so that it's compatible with __builtin__.sum.

Burcin, can you look at this?


---

Comment by burcin created at 2009-06-23 21:39:21

I uploaded a new patch in attachment:trac_3587-maxima_simplify_sum.patch. This has both patches folded together, and renames `sum()` to `symbolic_sum()` in `sage/calculus/calculus.py` and `sage/misc/functional.py` eliminating the risk of people using the symbolic sum instead of sum in library code without realizing, and the need to import `__builtin__`.

I am OK with the patch, and ready to give it a positive review. However, there is a problem, maxima returns wrong results in certain cases:


```
sage: sum(binomial(n,k), k, 1, n)
2^n - 2
sage: sum(binomial(n,k), k, 2, n)
2^n - 2*n - 2
sage: r=sum(binomial(n,k), k, 2, n-2)
sage: r.simplify()
2^n - 1/6*n^3 - 11/6*n - 2
```


It seems that maxima doesn't handle definite sums with "non natural" bounds. I.e., in the examples above the bounds don't span the whole support of the expression, so one needs further processing to get the final result after calling Zeilberger's algorithm.

Indefinite sums seem to be fine. In this case, we could check the inputs, and raise a warning if we have a definite sum. I'll try to do this, but don't count on me since I already signed up for a lot this week.


---

Attachment


---

Comment by kcrisman created at 2009-08-28 20:33:47

I installed this, but it does not seem to work as advertised.  Namely, 

```
sage: var('n,k')
(k, n)
sage: sum(binomial(n,k),k,0,n)
simplify_sum(sum(binomial(n,k),k,0,n))
```

It does behave as desired if I go to Maxima and load(simplify_sum) etc., but that's not the same.  Somehow it's staying symbolic for some reason.  This is off of 4.1.1 on Mac OSX.5.

> I am OK with the patch, and ready to give it a positive review. However, there is a problem, maxima returns wrong results in certain cases:
> 
> {{{
> sage: sum(binomial(n,k), k, 1, n)
> 2^n - 2
> sage: sum(binomial(n,k), k, 2, n)
> 2^n - 2*n - 2
> sage: r=sum(binomial(n,k), k, 2, n-2)
> sage: r.simplify()
> 2^n - 1/6*n^3 - 11/6*n - 2
> }}}
> 
> It seems that maxima doesn't handle definite sums with "non natural" bounds. I.e., in the examples above the bounds don't span the whole support of the expression, so one needs further processing to get the final result after calling Zeilberger's algorithm.

Looks like this problem is fixed in Maxima 5.19 (at least they work properly in 5.19.1), so this is another good reason to get that in Sage soon (there was an experimental spkg posted at [http://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.0/maxima-5.19.0.spkg](http://sage.math.washington.edu/home/kirkby/Solaris-fixes/maxima-5.19.0/maxima-5.19.0.spkg) at one point).  Incidentally, apparently it never got to as heavy a hitter as Zeilberger, but I'm not sure where the problem was.


---

Comment by whuss created at 2009-08-31 11:23:28

Replying to [comment:10 kcrisman]:
> I installed this, but it does not seem to work as advertised.  Namely, 
> {{{
> sage: var('n,k')
> (k, n)
> sage: sum(binomial(n,k),k,0,n)
> simplify_sum(sum(binomial(n,k),k,0,n))
> }}}
> It does behave as desired if I go to Maxima and load(simplify_sum) etc., but that's not the same.  Somehow it's staying symbolic for some reason.  This is off of 4.1.1 on Mac OSX.5.

It works for me on sage-4.1.1 on Linux. I don't have a Mac to check.


---

Comment by kcrisman created at 2009-09-02 18:53:56

The fix for my problem is to change

```
maxima = Maxima(init_code = ['display2d:false; domain: complex; keepfloat: true; load(topoly_solver); load(simplify_sum)'],
                script_subdirectory=None)
```

by

```
maxima = Maxima(init_code = ['display2d:false', 'domain: complex', 'keepfloat: true', 'load(topoly_solver)', 'load(simplify_sum)'],
                script_subdirectory=None)
```

the need for which perhaps does depend on the operating system.   Can someone check that this doesn't break Linux?


---

Comment by kcrisman created at 2009-09-02 19:30:44

The latest .spkg in #6699 (and hence in 4.1.2.alpha0) should fix the problems Burcin mentions, and seems to handle all the sums properly.

```
sage: sum(binomial(n,k), k, 1, n)
2^n - 2
sage: sum(binomial(n,k), k, 2, n)
2^n - 2*n - 2
```

are now

```
sage: var('k,n')
(k, n)
sage: sum(binomial(n,k),k,0,n)
2^n
sage: sum(binomial(n,k),k,1,n)
2^n - 1
sage: sum(binomial(n,k),k,2,n)
2^n - n - 1
```

So perhaps a new patch based on 4.1.2.alpha0 is in order, but then the review should be quite straightforward, with the fix above.


---

Comment by kcrisman created at 2009-09-02 20:24:51

This should fix all the outstanding issues. It is built off of 4.1.1, with #6564 and (then) #6699 applied, then this patch.  Several additional doctests/fixes to them are included beyond the previous patch, in addition to the Maxima init fix.  Should definitely be tested on Linux to make sure the fix for OSX didn't break Linux!


---

Comment by jason created at 2009-09-02 22:20:35

I browsed through the patch---is it still easy to access the (fast) native python sum command, or will we have to import that into the namespace?  In other words, was the suggestion given above about calling the python sum vs. this new sum depending on the arguments implemented?  If not, I see a serious, far-reaching problem with backwards compatibility...


---

Comment by kcrisman created at 2009-09-03 00:20:23

Well, the following was identical with and without the patch:

```
sage: l = range(10^6)
sage: time sum(l)
CPU times: user 0.15 s, sys: 0.00 s, total: 0.15 s
Wall time: 0.15 s
499999500000L
```

And the same with summing m = 5*l, both 0.79 s, and summing n = 100*m, both about 80 s.  And sum(l,3) returns the correct answer (without the L).  Also, earlier mhansen seems to indicate that it's still okay - I don't know exactly where in the code that happens, though.  Hope this helps.


---

Comment by was created at 2009-09-13 01:15:20

Fix this one broken doctest and this gets a positive review from me:

```python
wstein@sage:~/build/sage-4.1.2.alpha1$ ./sage -t devel/sage/sage/misc/functional.py 
sage -t  "devel/sage/sage/misc/functional.py"               
**********************************************************************
File "/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/misc/functional.py", line 442:
    sage: sum(k * binomial(n, k), k, 1, n)
Expected:
    1/2*2^n*n
Got:
    n*2^(n - 1)
**********************************************************************
File "/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage/sage/misc/functional.py", line 480:
    sage: sum(a*q^k, k, 0, oo)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: Sum is divergent.
Got:
    -a/(q - 1)
**********************************************************************
1 items had failures:
   2 of  20 in __main__.example_25
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-4.1.2.alpha1/tmp/.doctest_functional.py
         [8.3 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/misc/functional.py"
Total time for all tests: 8.3 seconds
wstein@sage:~/build/sage-4.1.2.alpha1$ 
```


The above is just the result of changes in Maxima going from 5.16 to 5.19 in sage-4.1.2.

  -- William


---

Comment by mpatel created at 2009-09-13 01:55:24

This is nice!

Just a small note: Sphinx warns about the indentation of the new `note::` block in `expression.pyx`:

```
/home/apps/sage/devel/sage/doc/en/reference/sage/symbolic/expression.rst:: (ERROR/3) Content block expected for the "note" directive; none found.
```



---

Comment by whuss created at 2009-09-14 14:09:48

fixes the doctest errors reported by William


---

Attachment

Okay, I fixed those tests; there were identical ones elsewhere I did fix but functional.py escaped me.  I also think I fixed the note issue.  

Since #6197 is merged I also used the correct algorithm=maxima behavior.  I don't have Maple so I didn't feel comfortable changing the Maple behavior, but it would be easy to open a new ticket for that if the appropriate algorithm worked, which it certainly seems like it should post-#6197.

I'm going to assume that the builtin sum is indeed okay - great!


---

Comment by kcrisman created at 2009-09-14 14:12:16

Use only the 5-19-1 patch.


---

Attachment

removes the workaround for binomials. Depends on #6197


---

Comment by whuss created at 2009-09-14 14:19:50

Looks like I have been a little too late.

I have checked that algorithm=maple also works without the workaround for #6197.
I think it is save to remove it.


---

Comment by kcrisman created at 2009-09-14 15:28:10

Great, I'll do that as well.


---

Comment by was created at 2009-09-22 14:26:42

I get *tons* of doctest failures when I apply this patch, say to sage-4.1.2.alpha1:

```
The following tests failed:

        sage -t  devel/sage/sage/misc/functional.py # 5 doctests failed
        sage -t  devel/sage/sage/calculus/calculus.py # 10 doctests failed
        sage -t  devel/sage/sage/symbolic/expression.pyx # 9 doctests failed
```


See http://sage.math.washington.edu/home/wstein/build/sage-4.1.2.alpha1/test_3587.out


---

Comment by kcrisman created at 2009-09-22 14:33:50

Did you do #6197?


---

Comment by kcrisman created at 2009-09-24 14:02:11

This patch in fact applies cleanly to 4.1.2.alpha2, and none of the files above have doctest failures with it.  Please review.


---

Comment by kcrisman created at 2009-11-17 20:12:39

Based on 4.2.1, apply only this patch


---

Attachment

Please someone (beyond myself and the author) review this!  It would be perfect for the big 4.3 release coming up!


---

Comment by mhansen created at 2009-11-29 14:27:30

Resolution: fixed


---

Comment by mhansen created at 2009-11-29 14:30:47

Positive review from me (by the way).
