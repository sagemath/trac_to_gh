# Issue 7614: change plot to use fast_callable

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-06 22:30:12

Assignee: was


```


On Sun, Dec 6, 2009 at 4:51 PM, Michel <vdbergh`@`gmail.com> wrote:
> Thanks for the reply. But no. The problem is not due to the fact that
> the function has a singularity. Indeed.
>
> plot(20*log(abs((1+I*x)^4),10),(x,0,3))
>
> fails with the same error which is incomprehensible to me.
>
> On the other hand turning the expression into a lambda function made
> it possible to plot it. Thanks for this practical advice.
>
> I wish someone could explain this rationally to me.
>
> 20*log(abs((1+I*x)^4),10)
>
> seems to be a perfectly fine symbolic expression so IMHO it should be
> possible to plot it.

This is a bug.  There absolutely no reason that plotting should give the error
   "float() argument must be a string or a number".
We could give an error about not being able to evaluate the function at certain
points.  However, the above error is not OK.    The error in fact is not in plotting
but in making a fast_float compiled version of the expression:

sage: s = 20*log(abs((1+I*x)^4),10)
sage: fast_float(s,x)
Traceback (most recent call last):
...
TypeError: float() argument must be a string or a number

In fact, SAge *should* be using fast_callable, not fast_float.  This works just fine if you force it manually:

s = 20*log(abs((1+I*x)^4),10)
plot(fast_callable(s,vars=[x]), (x,0,3))
[This is the Trac macro *nice picture as output* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#nice picture as output-macro)

Many, many thanks for your bug report.  It is bug reports from users like you that really helps Sage to be a first-rate mathematical software system. 

  }}}


---

Comment by mvngu created at 2009-12-07 00:17:52

From this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/19de9e09ff948cbc) thread:

```
On Sun, Dec 6, 2009 at 4:51 PM, Michel <vdbergh`@`gmail.com> wrote:
> Thanks for the reply. But no. The problem is not due to the fact that
> the function has a singularity. Indeed.
>
> plot(20*log(abs((1+I*x)^4),10),(x,0,3))
>
> fails with the same error which is incomprehensible to me.
>
> On the other hand turning the expression into a lambda function made
> it possible to plot it. Thanks for this practical advice.
>
> I wish someone could explain this rationally to me.
>
> 20*log(abs((1+I*x)^4),10)
>
> seems to be a perfectly fine symbolic expression so IMHO it should be
> possible to plot it.

This is a bug.  There absolutely no reason that plotting should give the error
   "float() argument must be a string or a number".
We could give an error about not being able to evaluate the function at certain
points.  However, the above error is not OK.    The error in fact is not in plotting
but in making a fast_float compiled version of the expression:

sage: s = 20*log(abs((1+I*x)^4),10)
sage: fast_float(s,x)
Traceback (most recent call last):
...
TypeError: float() argument must be a string or a number

In fact, SAge *should* be using fast_callable, not fast_float.  This works
just fine if you force it manually:

s = 20*log(abs((1+I*x)^4),10)
plot(fast_callable(s,vars=[x]), (x,0,3))
[This is the Trac macro *nice picture as output* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#nice picture as output-macro)

Many, many thanks for your bug report.  It is bug reports from users like
you that really helps Sage to be a first-rate mathematical software system.
```



---

Comment by jason created at 2009-12-07 11:42:39

Some of the things at #5572 need to be fixed (like constant functions) before this switch.  Right now, fast_float handles things like constant functions, but fast_callable does not.


---

Comment by was created at 2009-12-09 15:48:07

Replying to [comment:3 jason]:
> Some of the things at #5572 need to be fixed (like constant functions) before this switch.  Right now, fast_float handles things like constant functions, but fast_callable does not.

1. fast_float is just as bad as fast_callable, IMHO, since fast_float fails to handle many things too.  

2. Nobody is working on fast_callable, as far as I know, since Carl Witty is no longer working on Sage. 

3. The specific problem under consideration could nicely by solved with a simple try/except:

```
try: 
    fast_float(...)
except:
    fast_callable(...)
```



---

Attachment


---

Comment by was created at 2009-12-09 16:13:28

Changing status from new to needs_review.


---

Comment by jason created at 2009-12-09 17:29:40

Changing status from needs_review to positive_review.


---

Comment by jason created at 2009-12-09 17:29:40

passes doctests, fixes the problem above.


---

Comment by mhansen created at 2009-12-14 16:36:15

Resolution: fixed
