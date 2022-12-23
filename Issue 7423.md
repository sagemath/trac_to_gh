# Issue 7423: plot3d can't handle log(0)

Issue created by migration from https://trac.sagemath.org/ticket/7423

Original creator: kcrisman

Original creation time: 2009-11-10 20:33:44

Assignee: was

In 4.2.1.alpha0:

```
sage: f(x,y)=ln(x)
sage: P=plot3d(f,(x,0,1),(y,0,1))
sage: P
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (16, 0))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<snip a lot>
ValueError: math domain error
```

Switch to (x,0.1,1), and all is well.  I am pretty sure the problem is that line 404 in plot/plot3d/parametric_surface.pyx doesn't have an exception handler for log(0) or other such nan type values:

```
sage: math.log(0)
<snip>
ValueError: math domain error
```

But in the plotting context, it's silly not to just ignore this; we check for things like this all the time:

```
sage: plot(log,0,1)
<works fine>
```

For now it would probably be enough to fix it for the z variable.  


---

Comment by jason created at 2010-11-04 14:22:36

This works for me in 4.6:


```
sage: f(x,y)=ln(x)
sage: P=plot3d(f,(x,0,1),(y,0,1))
sage: P
```



---

Comment by kcrisman created at 2010-11-04 18:59:00

You're right, but I am baffled as to why.   The command `./sage -hg log -p ./devel/sage/sage/plot/plot3d/parametric_surface.pyx` doesn't give me any indication anything of this type has changed recently.  

If this worked on both Linux and Mac, and some other edge cases worked like this, I'd be satisfied to close this ticket with a patch that documented said edge cases worked; we can always fix other things like this as they occur.


---

Comment by @DaveWitteMorris created at 2021-01-11 01:25:18

As pointed out in comment:1, this problem went away ten years ago. I also verified now on MacOS and `CoCalc`. The PR adds a doctest, so we can close this old ticket if the patchbots agree.
----
New commits:


---

Comment by @DaveWitteMorris created at 2021-01-11 01:25:18

Changing status from new to needs_review.


---

Comment by @DaveWitteMorris created at 2021-01-11 01:25:18

Changing priority from major to minor.


---

Comment by tscrim created at 2021-01-11 23:41:13

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2021-01-11 23:41:13

LGTM.


---

Comment by vbraun created at 2021-01-24 10:36:56

Resolution: fixed
