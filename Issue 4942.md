# Issue 4942: find_root() is broken when interval borders cannot be evaluated

Issue created by migration from https://trac.sagemath.org/ticket/4942

Original creator: mabshoff

Original creation time: 2009-01-05 20:32:08

Assignee: jkantor

CC:  kcrisman

Reported in http://groups.google.com/group/sage-support/browse_thread/thread/40da8039090c3e8a


```
Hi, I'm trying out SAGE for the first time, so I entered what you 
suggested (see above). 
Now, from the plot, it there seems to be no other roots between 0 and 2 
so I entered 
sage: find_root(x^2*log(x,2)-1,0, 2) 
and got the root = 0.0 
what am I missing here? 
TIA, 
AJG 
```

But note the following:

```
sage: find_root(1/(x-1)+1,0, 2) 
0.0 
sage: find_root(1/(x-1)+1,0.00001, 2) 
1.0000000000011564 
```


Cheers,

Michael


---

Comment by mhansen created at 2009-01-30 23:27:11

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-30 23:27:11

Changing assignee from jkantor to mhansen.


---

Comment by mabshoff created at 2009-02-08 06:41:17

This is a critical bug and ought to be fixed in 3.3.

Note that #3870 might be a dupe of this bug.

Cheers,

Michael


---

Comment by mhansen created at 2009-02-08 23:59:48

It seems this is a problem with Scipy:


```
In [16]: def f(x):         
   ....:     return 1.0/(x-1.0)+1.0
   ....: 

In [17]: import scipy.optimize

In [18]: scipy.optimize.brentq(f, 0, 2)
Out[18]: 0.0

In [19]: f(0.001)
Out[19]: -0.0010010010010010895

In [20]: f(2)
Out[20]: 2.0

In [21]: scipy.optimize.brentq(f, 0.001, 2)                                                   
Out[21]: 1.0000000000007283

In [22]: f(1.0000000000007283)
Out[22]: 1373048666882.2488
```



---

Comment by cwitty created at 2009-02-15 03:15:54

There are at least a couple of issues here.  First, brentq is a variant of a bisection-based solver; if you use any bisection-based solver to find a zero of 1/(x-1) between 0 and 2, it will narrow down and return something very close to 1.  So if we don't like that, we should use a different solver (or at least try to check the output; for instance, a simple check that f(x) is "small" would detect this particular problem).

Second, find_root tries to verify that the function evaluates to different signs at the endpoints of the interval (as required by brentq); but it doesn't check the function evaluation results for NaN.  In the original test case, fast_float(f)(0) gives NaN.


---

Comment by mabshoff created at 2009-03-01 02:30:48

Better luck in 3.4.1. Unfortunately this either requires testing of the result of scipy or some deeper surgery in Scipy.

Cheers,

Michael


---

Comment by was created at 2009-06-15 23:23:28

Changing priority from blocker to critical.


---

Comment by was created at 2009-06-15 23:23:28

If we've released for months and months without fixing this, it doesn't make sense to keep it as a blocker.


---

Comment by assaferan created at 2018-09-04 11:23:24

Changing status from new to needs_review.


---

Comment by assaferan created at 2018-09-04 11:23:24

Hi, added two small validity checks:
1. If one of the endpoints is evaluated to NaN we seek a nearby point in the interval which can be evaluated.
2. If the value of the function at the root found is "large", raise an error that we could not find it.
----
New commits:


---

Comment by assaferan created at 2018-09-06 09:21:55

Changing status from needs_review to needs_work.


---

Comment by tscrim created at 2018-09-06 22:32:32

I am not sure 1 is necessarily the best solution to this because what if you get a function that always evaluates to NaN as you increase/decrease the endpoints? For instance

```
sage: f(x) = 0.0 / max(0, x)
```

will be NaN for infinitely many values. So your current test means this runs forever:

```
sage: find_root(f, -1, 0)
```

(before it simply gave a wrong value).

Also, I think for 2 you should raise a `NotImplementedError` as I think that more accurately reflects the situation.


---

Comment by git created at 2018-09-07 10:11:49

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2018-09-07 12:01:17

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by assaferan created at 2018-09-07 13:20:40

Fixed the bugs and changed behaviour in both cases, as suggested by tscrim


---

Comment by assaferan created at 2018-09-07 13:20:40

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2018-09-07 23:24:14

Thanks. Looks better now. A few more little things:

- `ticket 4942` -> `:trac:`4942`` in the documentation.
- Could you add the test from comment:17.
- This change:
  {{{#!diff
        Traceback (most recent call last):
-           ...
+       ...
        NotImplementedError: Brent's method failed to find a zero for f on the interval
  }}}
- Instead of using `...` for imprecision, it would be better to use `# abs tol` (or a `# rel tol`).
- `if` statements do not need outer parentheses in Python, so remove them from `if (full_output):` and the outermost pair from the other `if` statement 4 lines down.


---

Comment by git created at 2018-09-10 08:39:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2018-09-17 06:28:47

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2018-09-17 06:28:47

Thank you. LGTM.


---

Comment by vbraun created at 2018-09-19 08:09:26

Resolution: fixed
