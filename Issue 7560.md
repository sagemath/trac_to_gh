# Issue 7560: len(t_span) > 2 case creates len(t_span) -  1 solutions

Issue created by migration from Trac.

Original creator: adavid

Original creation time: 2009-11-30 16:46:19

Assignee: jkantor

CC:  rnelsonchem@gmail.com

Keywords: t_span

From: Ryan


```
Hello all,

I've just started using Sage, and I'm currently trying to use the
ode_solver class to solve some simple differential equations. I was
having some problems setting up my own program based on this class
until I realized that the number of points in the solution does not
match the number of points requested by the t_span variable. For
example, when I run this script:
_________
#!/usr/bin/env sage-python
from sage.all import ode_solver

def f(t, y):
   return [y[1], -y[0]]
T = ode_solver()
T.function=f
T.y_0=[1, 1]
T.ode_solve(t_span=[0, 10], num_points=100)
print len(T.solution)
T.ode_solve(t_span=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print len(T.solution)
_________

I get returned values of 101 and 10, where I would expect 100 and 11.

I don't know about the first case, but for the second case, the
solution for the last value (10) is missing. I was able to circumvent
this problem by appending a dummy variable to the end of t_span, but
I'm wondering if this is the expected behavior. Is there something
about the solution that I'm missing? I am currently using Sage 4.2.1
that I built from source in a Gentoo Linux distro.
```



---

Comment by medlock created at 2010-10-16 02:58:41

Changing status from new to needs_review.


---

Comment by medlock created at 2010-10-16 02:58:41

Changing keywords from "t_span" to "ode_solver, ode_solve, t_span".


---

Attachment

There are two separate issues here, one of which is clearly a bug:

1. There's an off-by-one in the code for handling the case where t_span specifies all the time points for the solution (len(t_span) > 2).  I put together a patch for this above.  The upper limit of the loop was changed from n-1 to n and the setting of t_end was moved to the beginning of the loop.  I also changed t_span to self.t_span in two spots.

2. num_points specifies the number of points *after* the initial point, so there are num_points + 1 total.  This is not clear one way or the other.  I tend to like the current version, so that, e.g. t_span = [0, 1], num_points = 10, gives points at 0, 0.1, 0.2, ..., 0.9, 1 instead of 0, 0.11111, 0.22222, ..., 0.88888, 1.


---

Comment by jdemeyer created at 2012-07-27 20:42:56

Please fill in your real name as Author.


---

Comment by medlock created at 2012-07-27 23:03:21

Replying to [comment:2 jdemeyer]:
> Please fill in your real name as Author.

I'm not sure what exactly you're asking for.  My real name is Jan Medlock.  It's already in the patch.


---

Comment by tkluck created at 2012-12-23 21:29:53

Changing status from needs_review to needs_work.


---

Comment by tkluck created at 2012-12-23 21:29:53

I tested this and it seems to work well.

I agree with what you say about the documentation being a bit unclear about the interpretation of `num_points`. I also agree that it is nicest to interpret it as the number of intervals. Maybe you can update the documentation in you patch? I'll give it a positive review after that.


---

Comment by medlock created at 2013-01-05 23:04:48

Replying to [comment:6 tkluck]:
> I tested this and it seems to work well.
> 
> I agree with what you say about the documentation being a bit unclear about the interpretation of `num_points`. I also agree that it is nicest to interpret it as the number of intervals. Maybe you can update the documentation in you patch? I'll give it a positive review after that.

tkluck, I updated the patch with clarification of the documentation.  I'd appreciate if you would have a look.


---

Comment by tkluck created at 2013-01-06 17:48:28

This is a very clear explanation in the doctext, thanks.

This part is not entirely right, though:

```
    * If ``t_span`` is a tuple with more than 2 values, then (...)

    * If ``t_span`` is a tuple with just 2 time values, then (...) the user must also specify
      ``num_points``.
```


In the code, the distinction is made based on whether `num_points` is specified, and not based on the length of `t_span`. That's a good thing. (remember how your matlab code always breaks when you pass 1x1 matrices to your generic code for NxN matrices.)

I would also be tempted to change the name of the parameter `num_points` to `num_intervals`, raising a `DeprecationWarning` for `num_points`. How do you feel about that?


---

Comment by medlock created at 2013-01-06 19:54:38

Replying to [comment:8 tkluck]:
> This is a very clear explanation in the doctext, thanks.
> 
> This part is not entirely right, though:
> {{{
>     * If ``t_span`` is a tuple with more than 2 values, then (...)
> 
>     * If ``t_span`` is a tuple with just 2 time values, then (...) the user must also specify
>       ``num_points``.
> }}}
> 
> In the code, the distinction is made based on whether `num_points` is specified, and not based on the length of `t_span`. That's a good thing. (remember how your matlab code always breaks when you pass 1x1 matrices to your generic code for NxN matrices.)

I'm not sure I understand what you're saying.  I believe what I've written is exactly correct.  The code in question is:

```
if len(self.t_span)==2 and num_points!=False:
    # Solve at num_points time steps.

elif len(self.t_span) > 2:
     # Solve using t_span as the times.
```

http://trac.sagemath.org/sage_trac/browser/sage/gsl/ode.pyx#L495
&
http://trac.sagemath.org/sage_trac/browser/sage/gsl/ode.pyx#L538

I agree that it is not ideal: the second condition should be `len(self.t_span) >= 2` and there should be an `else` clause to catch mis-specified `self.t_span`.  As for what to do if `len(self.t_span) > 2` and `num_points` is defined, I think the best thing to do is to use the values in `self.t_span` and ignore `num_points`.  I will put together a patch with this addition.

> I would also be tempted to change the name of the parameter `num_points` to `num_intervals`, raising a `DeprecationWarning` for `num_points`. How do you feel about that?

I personally find points more natural than intervals in this setting, even though intervals don't have the +1 issue.


---

Comment by tkluck created at 2013-01-06 22:27:57

> I'm not sure I understand what you're saying. I believe what I've written is exactly correct. 

I'm sorry, you're right. I think the `elif` condition needs to be changed to `>= 2` as you suggest, even though I realize it's technically a different issue. If we don't, this will really bite people. 

> As for what to do if len(self.t_span) > 2 and num_points is defined, I think the best thing to do is to use the values in self.t_span and ignore num_points.

I agree.

> I personally find points more natural than intervals in this setting,

I'll trust your judgment since I haven't actually used this.


---

Comment by tkluck created at 2013-01-07 03:55:50

Actually, why restrict to `len(t_span) >= 2` at all? I think we should just:

 * return only the initial condition as a list with one element if `len(t_span) == 1`;
 * return an empty list `[]` if we get `t_span == []`.

For example, this can be useful if someone wants to find solutions on the intersection of two sets. Then s/he does not have to treat an empty intersection as a special case.


---

Attachment

Updated patch (v3).


---

Comment by medlock created at 2013-01-07 04:52:45

Replying to [comment:11 tkluck]:
> Actually, why restrict to `len(t_span) >= 2` at all? I think we should just:
> 
>  * return only the initial condition as a list with one element if `len(t_span) == 1`;
>  * return an empty list `[]` if we get `t_span == []`.
> 
> For example, this can be useful if someone wants to find solutions on the intersection of two sets. Then s/he does not have to treat an empty intersection as a special case.

Patch updated.

Thanks for your comments.  I implemented `len(t_span) == 2` and `num_points` not specified.  I also implemented `len(t_span) == 1` because it was very easy.

I did not implement `len(t_span) == 0` because it would have required a separate `if-then` branch.  My further reasoning was that the initial condition `y_0` is required, so `t_span[0]` is also required, although I do see your point about how one could end up with `t_span` being empty.

I have a big rewriting of this file in the works: I hope you'll be able to have a look.


---

Comment by tkluck created at 2013-01-09 21:47:03

I have no more comments. Positive review!


---

Comment by tkluck created at 2013-01-09 21:47:03

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2013-01-12 08:51:37

Resolution: fixed
