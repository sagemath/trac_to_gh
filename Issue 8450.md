# Issue 8450: contour_plot chokes on function which involves imaginary numbers

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-03-05 22:01:42

Assignee: was

CC:  mjo egourgoulhon @jungmath

This gives an error:


```
contour_plot(real_part(log(x+y*I+.001)), (x,-3,3),(y,-3,3),fill=False)
```


but this works:


```
a(x,y)=real(log(x+y*I+.001))
f=fast_callable(a,domain=CC)
contour_plot(f, (x,-3,3),(y,-3,3),fill=False)
```


and this works:


```
contour_plot(imag(log(x+y*I+.001)), (x,-3,3),(y,-3,3),fill=False)
```



---

Comment by jason created at 2010-04-26 11:59:23

#5572 will help solve this.


---

Comment by embray created at 2019-06-14 14:54:19

As the Sage-8.8 release milestone is pending, we should delete the sage-8.8 milestone for tickets that are not actively being worked on or that still require significant work to move forward.  If you feel that this ticket should be included in the next Sage release at the soonest please set its milestone to the next release milestone (sage-8.9).


---

Comment by mkoeppe created at 2021-07-22 00:57:56

Changing status from new to needs_info.


---

Comment by mjo created at 2021-07-23 15:13:24

Changing status from needs_info to needs_review.


---

Comment by mjo created at 2021-07-23 15:13:24

This is an "easy fix" but causes a cascade of other issues because removing `domain=float` turns a lot of things that used to be `Nan` into `TypeError`, `ValueError`, `ZeroDivisionError`, etc.

I'm still running a ptestlong on this, but everything under `sage/plot` now passes. Here are some thoughts:

1. Do we really want to support passing (for example) the integer zero as a function to be plotted? We have doctests that check things like `plot(ZZ(0), x, 0, 1)`. Supporting this requires special cases in the code, and IMO just perpetuates confusion about the difference between the integer 0 and the function const0.
2. We now have "try to evaluate this as a real number, and return NaN (or skip it) if we can't" code in at least five places. Should this be made consistent, or (better yet) factored out? I've made it so that the doctests pass, but in some places we catch only e.g. `TypeError`, while in others we check for a nice long list.
3. This needs a careful review, since it can change the appearance of plots. There was some other (now fixed) bug involved as you can see from the commit list, but for example, this fix accidentally broke `list_plot`.
4. I don't really like using try/except in fast loops. Is there a better way to fix the doctest failures that the first commit caused and that the later ones fix?


---

Comment by mkoeppe created at 2021-07-23 16:36:19

Replying to [comment:11 mjo]:
> 1. Do we really want to support passing (for example) the integer zero as a function to be plotted? We have doctests that check things like `plot(ZZ(0), x, 0, 1)`. Supporting this requires special cases in the code, and IMO just perpetuates confusion about the difference between the integer 0 and the function const0.

Allowing non-callables as input for `plot` is, I think, important to keep. Convenience for casual use is key. Given that `plot` takes variable names as part of its input, it's clear that there is some implicit construction of a symbolic or numerical function happening.


---

Comment by mkoeppe created at 2021-07-23 16:41:50

Replying to [comment:11 mjo]:
> This is an "easy fix" but causes a cascade of other issues because removing `domain=float` turns a lot of things that used to be `Nan` into `TypeError`, `ValueError`, `ZeroDivisionError`, etc.

Sorry, where do you remove `domain=float`?


---

Comment by mjo created at 2021-07-23 16:45:06

Replying to [comment:13 mkoeppe]:
> Replying to [comment:11 mjo]:
> > This is an "easy fix" but causes a cascade of other issues because removing `domain=float` turns a lot of things that used to be `Nan` into `TypeError`, `ValueError`, `ZeroDivisionError`, etc.
> 
> Sorry, where do you remove `domain=float`?

The first thing `fast_float()` tries is to use `fast_callable()` with `domain=float`:


```python
try:
    return fast_callable(f, vars=vars, domain=float,
                         expect_one_var=expect_one_var)
```


We're now using `fast_callable()` directly, and omit the `domain`.


---

Comment by mkoeppe created at 2021-07-23 16:59:44

Thanks.

I have not looked at the details, nor done any timing. But it seems to me that a better solution may be to try `domain=float` first, then `domain=complex` (or whatever is needed to make `fast_callable` use `interp_cdf`); and only in the end fall back to the general interpreter.

> 2. We now have "try to evaluate this as a real number, and return NaN (or skip it) if we can't" code in at least five places. Should this be made consistent, or (better yet) factored out? 

Yes, I guess there would be value in a version of the general interpreter that catches errors and replaces them by NaN returns


---

Comment by mkoeppe created at 2021-07-23 17:08:46

By the way, I just came across https://trac.sagemath.org/attachment/ticket/5572/improve_fast_callable.6.patch, which seems to have done a lot of what we're doing again now...


---

Comment by mjo created at 2021-07-23 17:31:04

Replying to [comment:15 mkoeppe]:
> Thanks.
> 
> I have not looked at the details, nor done any timing. But it seems to me that a better solution may be to try `domain=float` first, then `domain=complex` (or whatever is needed to make `fast_callable` use `interp_cdf`); and only in the end fall back to the general interpreter.

This is tough because there are so many plotting interfaces, and the fast-callables aren't created near the point of failure. In this case, `setup_for_eval_on_grid()` is preprocessing some of the plotting args and returning them to some other function that orchestrates the plotting. Then the failure occurs in _another_ function that actually computes the plot points. 

Some major refactoring would be needed to do this all more intelligently. (I think we would also need to generate some kind of custom exception to avoid wrapping ten layers of code in one big `except TypeError` block.)


---

Comment by mkoeppe created at 2021-07-23 17:35:16

Changing priority from major to minor.


---

Comment by mkoeppe created at 2021-07-23 17:35:16

OK, thanks for the explanation. Then I would suggest that we declare the issue of this ticket as "minor" and set it aside for later consideration.


---

Comment by mkoeppe created at 2021-07-23 17:35:16

Changing status from needs_review to needs_work.


---

Comment by git created at 2021-07-26 14:03:41

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by mjo created at 2021-07-26 14:25:51

Changing status from needs_work to needs_review.


---

Comment by mjo created at 2021-07-26 14:25:51

Replying to [comment:18 mkoeppe]:
> OK, thanks for the explanation. Then I would suggest that we declare the issue of this ticket as "minor" and set it aside for later consideration. 

I actually hold a grudge against this bug from back when I was generating plots programmatically and the random appearance of `0.000000000001*I` would kill the whole thing after an hour, so I haven't given up.

I tried a few more things, described in the first of the recent commit messages, and discovered problems with all of them. I did however eventually find a solution that is both unobtrusive and fast: wrap fast-callable evaluation in a class that can force the result to a specific output type. With ``domain=<something complex>`` and ``output=<something real>``, we return `NaN` unless the imaginary part is trivial, in which case we return the real part. In all other situations we simply try to coerce the output to the given type.

This allows us to plot over CDF but convert the result to float (possibly NaN) only on the way out, without having to hack that conversion logic into a hundred plotting functions. It's probably as fast as any solution could be; complex (two-float) operations necessarily take longer than plain float computations, but the difference is small in my non-rigorous tests, less than 10%.

An output wrapper is not used unless it's needed, so this doesn't affect any other uses of `fast_callable()` in the tree.


---

Comment by mkoeppe created at 2021-07-26 20:13:41

This looks like a fine approach. I won't have time before mid August to look at it in detail. Just a quick comment:

```
+        # This tolerance was not chosen for any particular reason.
+        if abs(ipart) < 1e-8:
+            return self._output(rpart)
+        else:
+            return self._output("nan")
```

Probably best to make these tolerances user-configurable (as an optional init argument of OutputWrapper and optional argument of `fast_callable`).


---

Comment by mjo created at 2021-07-26 23:24:05

Changing status from needs_review to needs_work.


---

Comment by mjo created at 2021-07-26 23:24:05

Replying to [comment:22 mkoeppe]:
> Probably best to make these tolerances user-configurable (as an optional init argument of OutputWrapper and optional argument of `fast_callable`).
> 

I'm glad you brought this up. I swept it under the rug when I had fifteen things on my internal problem stack, but it's a code smell: using a fixed tolerance isn't right, but adding the argument to `fast_callable()` and trying to explain how it will be used exposes too many implementation details.

I think I can simplify things even further.


---

Comment by git created at 2021-07-27 14:05:23

Branch pushed to git repo; I updated commit sha1. This was a forced push. Last 10 new commits:


---

Comment by mjo created at 2021-07-27 14:07:57

Much better now. There's no need to solve the output-conversion problem more generally; we need it only for plotting, and creating the wrapper under sage.plot.misc eliminates all of the problems with the previous iteration.


---

Comment by mjo created at 2021-07-27 14:07:57

Changing status from needs_work to needs_review.


---

Comment by git created at 2021-07-27 21:01:03

Branch pushed to git repo; I updated commit sha1. This was a forced push. Last 10 new commits:


---

Comment by mkoeppe created at 2021-08-15 02:53:25

This is looking nice. Similar to what I said in comment:22, I think the imaginary tolerance should be customizable on the level of the plot functions -- in the same way that options such as `detect_poles`, `adaptive_tolerance` are offered.


---

Comment by mjo created at 2021-08-19 13:37:00

Replying to [comment:27 mkoeppe]:
> This is looking nice. Similar to what I said in comment:22, I think the imaginary tolerance should be customizable on the level of the plot functions -- in the same way that options such as `detect_poles`, `adaptive_tolerance` are offered.

Those only work for the `plot()` function, and not for anything else that calls `setup_for_eval_on_grid()`. But once #32234 gets reviewed, I guess I wouldn't mind adding `imaginary_tolerance` to `plot.options`. In that case, we should probably go back later and try to make the options to the various plotting functions consistent (in another ticket).


---

Comment by mjo created at 2021-10-21 00:29:30

Here's a rebase and the `plot.options` interface. I still need to look closer at what's going on with `real_nth_root()` though; what's there is a hack.
----
New commits:


---

Comment by mjo created at 2021-10-21 00:29:30

Changing status from needs_review to needs_work.


---

Comment by git created at 2021-11-03 12:31:23

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by mjo created at 2021-11-03 12:39:13

Changing status from needs_work to needs_review.


---

Comment by mjo created at 2021-11-03 12:39:13

The `real_nth_root()` fix reveals a new issue that may arise in some cases: symbolic functions that are not prepared to receive "real" arguments of the form `x + 0*I`. But the fix is not so bad as you can see. And it should be rare, since most sage operations will try to coerce things to the expected domain (and no other doctests fail, of course). The "mod" operation in this cases is a bit special in that regard.


---

Comment by dimpase created at 2021-12-03 10:14:29

rebased branch, with one `""" -> r"""` change
----
New commits:


---

Comment by git created at 2021-12-03 10:33:52

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by dimpase created at 2021-12-03 10:35:46

Wanna test this more. The new branch works with 9.5.beta7


---

Comment by dimpase created at 2021-12-03 10:56:18

off to the bots


---

Comment by dimpase created at 2021-12-03 10:56:18

Changing status from needs_review to positive_review.


---

Comment by slelievre created at 2021-12-03 12:59:38

Don't patchbots usually give higher priority to
"needs review" than "positive review"?


---

Comment by dimpase created at 2021-12-03 13:06:55

Replying to [comment:37 slelievre]:
> Don't patchbots usually give higher priority to
> "needs review" than "positive review"?
I meant buildbots


---

Comment by slelievre created at 2021-12-03 23:53:21

I missed that part of the developer guide.


---

Comment by dimpase created at 2021-12-27 13:03:12

Changing priority from minor to critical.


---

Comment by vbraun created at 2022-01-04 22:54:33

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2022-01-04 22:54:33

On OSX:

```
**********************************************************************
File "src/sage/plot/plot.py", line 3943, in sage.plot.plot.?
Failed example:
    generate_plot_points(sin(x).function(x), (-pi, pi), randomize=False)
Expected:
    [(-3.141592653589793, -1.2246...e-16), (-2.748893571891069,
    -0.3826834323650899), (-2.356194490192345, -0.707106781186547...),
    (-2.1598449493429825, -0.831469612302545...), (-1.9634954084936207,
    -0.9238795325112867), (-1.7671458676442586, -0.9807852804032304),
    (-1.5707963267948966, -1.0), (-1.3744467859455345,
    -0.9807852804032304), (-1.1780972450961724, -0.9238795325112867),
    (-0.9817477042468103, -0.831469612302545...), (-0.7853981633974483,
    -0.707106781186547...), (-0.39269908169872414, -0.3826834323650898),
    (0.0, 0.0), (0.39269908169872414, 0.3826834323650898),
    (0.7853981633974483, 0.707106781186547...), (0.9817477042468103,
    0.831469612302545...), (1.1780972450961724, 0.9238795325112867),
    (1.3744467859455345, 0.9807852804032304), (1.5707963267948966, 1.0),
    (1.7671458676442586, 0.9807852804032304), (1.9634954084936207,
    0.9238795325112867), (2.1598449493429825, 0.831469612302545...),
    (2.356194490192345, 0.707106781186547...), (2.748893571891069,
    0.3826834323650899), (3.141592653589793, 1.2246...e-16)]
Got:
    [(-3.141592653589793, -1.2246467991473532e-16),
     (-2.748893571891069, -0.38268343236508984),
     (-2.356194490192345, -0.7071067811865476),
     (-2.1598449493429825, -0.8314696123025455),
     (-1.9634954084936207, -0.9238795325112867),
     (-1.7671458676442586, -0.9807852804032304),
     (-1.5707963267948966, -1.0),
     (-1.3744467859455345, -0.9807852804032304),
     (-1.1780972450961724, -0.9238795325112867),
     (-0.9817477042468103, -0.8314696123025451),
     (-0.7853981633974483, -0.7071067811865475),
     (-0.39269908169872414, -0.3826834323650898),
     (0.0, 0.0),
     (0.39269908169872414, 0.3826834323650898),
     (0.7853981633974483, 0.7071067811865475),
     (0.9817477042468103, 0.8314696123025451),
     (1.1780972450961724, 0.9238795325112867),
     (1.3744467859455345, 0.9807852804032304),
     (1.5707963267948966, 1.0),
     (1.7671458676442586, 0.9807852804032304),
     (1.9634954084936207, 0.9238795325112867),
     (2.1598449493429825, 0.8314696123025455),
     (2.356194490192345, 0.7071067811865476),
     (2.748893571891069, 0.38268343236508984),
     (3.141592653589793, 1.2246467991473532e-16)]
**********************************************************************
1 item had failures:
   1 of  44 in sage.plot.plot.?
    [464 tests, 1 failure, 64.40 s]
----------------------------------------------------------------------
sage -t --long --random-seed=70775727671966200967886888406969327388 src/sage/plot/plot.py  # 1 doctest failed
----------------------------------------------------------------------
```



---

Comment by slelievre created at 2022-01-05 04:59:50

How about adding `# abs tol 1e-16` or using
the following output for the doctest:

```
    [(-3.141592653589793, -1.2246...e-16),
     (-2.748893571891069, -0.382683432365089...),
     (-2.356194490192345, -0.707106781186547...),
     (-2.1598449493429825, -0.831469612302545...),
     (-1.9634954084936207, -0.9238795325112867),
     (-1.7671458676442586, -0.9807852804032304),
     (-1.5707963267948966, -1.0),
     (-1.3744467859455345, -0.9807852804032304),
     (-1.1780972450961724, -0.9238795325112867),
     (-0.9817477042468103, -0.831469612302545...),
     (-0.7853981633974483, -0.707106781186547...),
     (-0.39269908169872414, -0.3826834323650898),
     (0.0, 0.0),
     (0.39269908169872414, 0.3826834323650898),
     (0.7853981633974483, 0.707106781186547...),
     (0.9817477042468103, 0.831469612302545...),
     (1.1780972450961724, 0.9238795325112867),
     (1.3744467859455345, 0.9807852804032304),
     (1.5707963267948966, 1.0),
     (1.7671458676442586, 0.9807852804032304),
     (1.9634954084936207, 0.9238795325112867),
     (2.1598449493429825, 0.831469612302545...),
     (2.356194490192345, 0.707106781186547...),
     (2.748893571891069, 0.382683432365089...),
     (3.141592653589793, 1.2246...e-16)]
```



---

Comment by slelievre created at 2022-01-05 05:08:44

Also, the blank line after an example or test block
is not needed if it ends a docstring.


---

Comment by mjo created at 2022-01-05 15:31:11

I've reworked that doctest to check something useful (and added `abs tol`) instead of a specific blob of digits.
----
New commits:


---

Comment by mjo created at 2022-01-05 15:31:11

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2022-01-06 11:43:28

Changing status from needs_review to positive_review.


---

Comment by dimpase created at 2022-01-06 11:43:28

lgtm


---

Comment by slelievre created at 2022-01-08 06:08:00

Class `FastCallablePlotWrapper`, method `__call__`,
test block needs double-colon:


```diff
-        Evaluation never fails and always returns a ``float``:
+        Evaluation never fails and always returns a ``float``::
```


It might also be worth checking why all patchbots
report pyflakes errors.


---

Comment by git created at 2022-01-08 13:25:54

Changing status from positive_review to needs_review.


---

Comment by git created at 2022-01-08 13:25:54

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:


---

Comment by mjo created at 2022-01-08 13:27:16

Thanks, setting back to positive review as the last commit is trivial.

I looked at the pyflakes failures, but the logs all say that everything is OK.


---

Comment by mjo created at 2022-01-08 13:27:16

Changing status from needs_review to positive_review.


---

Comment by git created at 2022-01-08 15:07:33

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:


---

Comment by git created at 2022-01-08 15:07:33

Changing status from positive_review to needs_review.


---

Comment by mjo created at 2022-01-08 15:08:09

Changing status from needs_review to positive_review.


---

Comment by mjo created at 2022-01-08 15:08:09

Also deleted a `set_random_seed()` call from a doctest that we don't need to add any more.


---

Comment by slelievre created at 2022-01-30 15:39:13

Setting milestone to 9.6 now that 9.5 is out.


---

Comment by vbraun created at 2022-01-31 23:32:07

Resolution: fixed


---

Comment by kcrisman created at 2022-02-18 12:52:32

Thanks for this fix, it will be very helpful!
