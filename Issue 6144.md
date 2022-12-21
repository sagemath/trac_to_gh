# Issue 6144: Pynac doesn't simplify exp(x)*exp(2*x) to exp(3*x)

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-05-28 05:27:18

CC:  was


```
sage: exp(x)*exp(2*x)
e^(2*x)*e^x
```



---

Comment by burcin created at 2009-05-28 10:34:48

GiNaC doesn't do this either:


```
> exp(x)*exp(2*x);
exp(2*x)*exp(x)
```


I'll try to play with the mul::eval method in pynac to do this. The main problem is doing it without compromising speed.

Cheers,

Burcin


---

Attachment


---

Attachment

New pynac package here fixes the exp simplification:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.8.spkg

Attached patches fix doctests, and change module_list.py to rebuild the sage/symbolic/* modules if the package is updated.

This package also contains a fix for #6163, so these tickets should be merged together.


---

Attachment


---

Comment by mhansen created at 2009-06-05 01:53:24

Burcin's changes look good to me.  There was one doctest failure that I fixed and put in trac_6144-review.patch


---

Comment by ncalexan created at 2009-06-05 01:59:21

All looks good to me!  I'm glad this is fixed, I updated the number field tests and was disappointed with the previous behaviour.


---

Comment by mhansen created at 2009-06-05 02:01:32

Resolution: fixed


---

Comment by mhansen created at 2009-06-05 02:01:32

Merged in 4.0.1.rc2.
