# Issue 6895: Detect discontinuities when plotting the ceil function

Issue created by migration from Trac.

Original creator: nbonifas

Original creation time: 2009-09-05 21:16:21

Assignee: was

The discontinuities in the ceil function are not detected.

Example: plot(lambda x: ceil(x), (-5,5), detect_poles='show') should not display vertical lines between the steps.


---

Comment by whuss created at 2009-09-07 10:35:01

_detect_poles_ is only meant for the case when the left/right side limits of the function are +/-Infinity.
It was never intended to detect other discontinuities.

But ticket #6878 implements something like this. It does not automatically detect the discontinuities but
lets you specify which points to exclude from the plot.

The following would have the effect you want:


```
sage: plot(ceil(x), (x, 1, 10), exclude = [1..10])
```



---

Comment by nbonifas created at 2009-09-07 13:09:49

I was thinking of implementing some kind of general automatic discontinuity detection, either numerical (when the numerical derivative of the function is locally above a threshold, consider this point to be a discontinuity) or via algebraic means, as in the Maple "discont" function.
