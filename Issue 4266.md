# Issue 4266: overflow error in SR approx

Issue created by migration from https://trac.sagemath.org/ticket/4266

Original creator: robertwb

Original creation time: 2008-10-11 14:06:33

Assignee: burcin


```
sage: round(sqrt(Integer('1'*500)))
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/misc/functional.py", line 865, in round
    except AttributeError: return RealDoubleElement(__builtin__.round(x, 0))
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 6164, in __float__
    return float(f._approx_(float(g)))
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 7941, in _approx_
    return math.sqrt(x)
OverflowError: math range error
```


Approx should fall back to mpfr if float fails. 


---

Comment by robertwb created at 2008-10-30 22:02:22

This is related to #188...


---

Attachment

I assume there is good reason that "always return an RDF" is enforced. SR elements should probably implement round() themselves.


---

Comment by mhansen created at 2008-11-21 17:24:58

Actually, I don't know of a good reason that "always return as RDF" is enforced.  It seems like floor, round, and ceiling should return Integers where possible.  There is a trac ticket by Nick Alexander that does this for some objects.


---

Comment by was created at 2008-11-27 17:46:35

REFEREE REPORT:

The attached patch fixes the reported problem.

I agree that changing round, etc., to not return RDF's makes perfect sense, but I think that should be an entirely new trac ticket. 

I doctested only the calculus tree after applying this patch, and all was good.


---

Comment by mabshoff created at 2008-11-28 07:32:47

Resolution: fixed


---

Comment by mabshoff created at 2008-11-28 07:32:47

Merged in Sage 3.2.1.rc0
