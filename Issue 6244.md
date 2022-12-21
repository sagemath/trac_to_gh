# Issue 6244: conjugate() in sage-4.0 is broken

Issue created by migration from Trac.

Original creator: gmhossain

Original creation time: 2009-06-08 01:40:44

CC:  ncalexan

Keywords: conjugate, pynac

1) pynac  .conjugate() method returns wrong answer:


```
f(x) = function('f',x)
f(x).conjugate()

f(conjugate(x))
```


Above is certainly not true. For example: f(x) = I + x implies
f(x).conjugate() = -I + conjugate(x) which is not equal to
f(conjugate(x))


2)  view() causes SIGSEGV crash


```
f(x) = function('f',x)
g(x) = f(x).conjugate()
view( g(x) )
boom!!
```




---

Comment by burcin created at 2009-06-13 22:28:08

I have a fix for (1) above, don't know about (2) yet. Same issue effects `.real_part()`, `.imag_part()`, etc. functions.


---

Comment by burcin created at 2009-06-13 22:28:08

Changing status from new to assigned.


---

Comment by burcin created at 2009-06-13 22:28:08

Set assignee to burcin.


---

Attachment


---

Comment by burcin created at 2009-06-14 21:05:33

This is fixed in the new pynac package here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.8.p0.spkg

Since the package also contains fixes for #6256 and #6211, the doctests should be run with those patches applied.

Besides adding doctests for the fix, the patch cleans up symbolic functions and adds correct conversions for asin, asinh, acos, acosh, and atan.


Nick, can you review this?


---

Comment by ncalexan created at 2009-06-14 21:40:18

Resolution: fixed


---

Comment by ncalexan created at 2009-06-14 21:40:18

Fine by me.
