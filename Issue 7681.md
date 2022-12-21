# Issue 7681: R pexpect interface seems to keep data around

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-12-14 19:43:23

Assignee: tbd

CC:  schilly

Keywords: pexpect, interface, R

For instance:

```
sage: r.length([1,2,3,4])
[1] 4
sage: r.vector('c(1,2,3,4,3)')
[1] 4
sage: r.length([1,2,3,4])
[1] 4
sage: r.vector('c(1,2,3,4,3)')
[1] 4
sage: r.vector('c(1,2,3,4,3)')
[1] 2
sage: r.vector('c(1,2,3,4,3)')
[1] 1 2 3 4 3
sage: r.vector('c(1,2,3,4,3)')
[1] 1 2 3 4 3
sage: r.vector('c(1,2,3,4,3)')
Error: object 'sage49' not found
```

Somehow the R interface is keeping stuff from previous calls and returning it, and then at some point choking.   Incidentally, in the above session, after trying many other R commands this way and always getting similar errors, all of a sudden 

```
[1] 1 2 3 4 3
```

showed up - as the answer to something else!  Where it had been hiding, I can only guess.


---

Comment by schilly created at 2009-12-14 20:00:55

This interface to R (which is entirely different from the rpy2 python module) is rather hard to do and still needs work. I think the problem is that "vector" in R does something differently than you imagine. I.e. an error happens which isn't shown and the pexpect interface is confused.


```
sage: x = r.c(1,2,3)
sage: r.as_vector(x)
[1] 1 2 3
sage: r.is_vector(r.as_vector(x))
[1] TRUE
```


works for me.

Here what really happens in R:


```
> length(c(1,2,3,4))
[1] 4
> vector(c(1,2,3,4,3))
Error in vector(c(1, 2, 3, 4, 3)) : 
  vector: cannot make a vector of mode '1'.
> as.vector(c(1,2,3,4,3))
[1] 1 2 3 4 3
```



---

Comment by kcrisman created at 2009-12-14 20:20:53

Okay, now I understand this example.  But clearly the error should be shown, correct?  The current behavior is bizarre, and in general this sort of thing happens a lot when trying to use it.

Should we not use the R interface and use rpy2 instead?  But it looks rather more difficult to use, upon a quick perusal of the documentation.


---

Comment by kcrisman created at 2009-12-14 20:30:56

And here's just something randomly annoying:

```
sage: r([1,1/2,1/2])
[1] 1.0 0.5 0.5
sage: r([0,sqrt(3)/2,sqrt(3)/2])
Error: object 'sage10' not found
```

Even though R knows what sqrt(3) is natively:

```
> sqrt(3)/2
[1] 0.8660254
```

I'm not saying this is really related to the summary of the ticket, but it's not unrelated, either.


---

Comment by schilly created at 2009-12-14 20:38:05

yes of course, wrong error handling + hickup is bad. these examples might be useful to track down the bug.

[http://rpy.sourceforge.net/rpy2/doc/html/rpy_classic.html](http://rpy.sourceforge.net/rpy2/doc/html/rpy_classic.html) might be helpful when using rpy, though...


---

Comment by kcrisman created at 2010-04-20 13:32:28

Changing summary to be more accurate - hopefully fixing this will fix the issues reported.


---

Comment by kcrisman created at 2010-04-30 16:03:11

Okay, the problem is that instead of handling errors, we are ignoring them:

```
        # don't abort on errors, just raise them! 
        # necessary for non-interactive execution
        self.eval('options(error = expression(NULL))') 
```

But see [here](http://stat.ethz.ch/R-manual/R-patched/library/base/html/stop.html) - it turns out that this is R's way of just totally ignoring them, not just 'raising' them.  This should be fixed.


---

Comment by kcrisman created at 2010-04-30 16:03:25

Changing component from packages to interfaces.


---

Comment by kcrisman created at 2010-04-30 16:03:25

Changing assignee from tbd to was.


---

Comment by kcrisman created at 2012-05-21 13:15:00

Changing keywords from "pexpect, interface, R" to "pexpect, interface, R, r-project".
