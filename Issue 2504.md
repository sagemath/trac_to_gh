# Issue 2504: number field .units() method caches proof=False result and returns it for proof=True

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-03-13 03:14:46

Assignee: was

The following was reported by Luis Finotti on sage-support, here: http://groups.google.com/group/sage-support/browse_thread/thread/f01e8661743d36d4#

The following commands return an error:

```
   P.<x>=PolynomialRing(QQ)
   f=x^17+3
   K=NumberField(f,'a')
   K.units(proof=True) # default
```

because Sage is incapable of performing the computation with proof=True.
(The error ends with "not enough precomputed primes, need primelimit ~  (35)".)

If you then do

```
   K.units(proof=False)
```

you get an answer immediately; then repeating the original

```
   K.units(proof=True)
```

gives you the unproved answer again even though proof=True is specified.


---

Attachment

The attached patch fixes this and adds doctests illustrating the correct behavior.


---

Comment by ncalexan created at 2008-04-15 16:34:06

Wait -- if you ask for units with proof, the value is cached.  If you then ask for it without proof, shouldn't we return the cached value?  The code doesn't look like it does that.


---

Attachment

You are completely right.  I've replaced the patch and reorganized the code so it looks a bit cleaner.


---

Comment by ncalexan created at 2008-04-26 17:16:53

Looks good to me.


---

Comment by mabshoff created at 2008-04-26 21:58:58

Merged 2504-units_cache.2.patch in Sage 3.0.1.alpha1


---

Comment by mabshoff created at 2008-04-26 21:58:58

Resolution: fixed
