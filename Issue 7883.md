# Issue 7883: Added some functionality to ideals

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-01-09 20:07:10

Assignee: malb

CC:  roed

Added some functionality to ideals (is_maximal works more often now, and there's a new ideal class for univariate polynomial rings).  Changed the logic on what class is chosen for ideals so that it's easier to override with _ideal_class_.


---

Comment by robertwb created at 2010-01-09 20:11:52

Changing status from new to needs_work.


---

Attachment

There's a lot of useful looking code in here, but it's unclear what exactly it does or it's intended to fix. Some more explanations would be nice, and the new behavior should be doctested. Especially for most of the changes in `sage/rings/ideal.py`

What is the parameter in _ideal_class_ supposed to mean? (Then why is it 0 by default?) 

Depends on #7881?


---

Attachment

Rebased against 4.3.3; may need 8218, 8332, 7880, but probably not.


---

Comment by roed created at 2010-02-23 15:05:22

I haven't made the changes Robert suggested, but I wanted to get an updated patch up since other finite field functionality depends on this.


---

Comment by roed created at 2010-02-23 17:39:01

Part of a series:

```
8218 -> 8332 -> 7880 -> 7883 -> 8333 -> 8334 -> 8335
```

I tried to make each of these mostly self contained, with doctests passing after every ticket, but I didn't entirely succeed.  If you're reviewing one of these tickets, applying later tickets will hopefully fix doctest failures that you're seeing.


---

Comment by davidloeffler created at 2010-03-17 22:11:04

Tried this under 4.3.4.rc0 with 8218, 8332, 7880 applied. It applies fine but seven doctests fail. Moreover, I second Robert's criticism: it's not clear what all this new code is actually for. (The fact that other finite-field stuff depends on this doesn't change that.) Can we have a new patch with some more docstrings etc?


---

Attachment

Addresses referee comments


---

Comment by roed created at 2010-09-19 13:19:43

Changing status from needs_work to needs_review.


---

Comment by roed created at 2010-09-19 13:19:43

Apply:


```
7883_ideals.patch
7883_fixes.patch
```


Probably will not pass doctests unless you also apply the patches on #8333 and #8334.


---

Comment by davidloeffler created at 2010-09-23 15:31:16

Apply only this patch


---

Attachment

I've uploaded a patch above which consists of 
- the two patches mentioned in roed's previous comment 
- the hunk from `7585_12_1_fixes.2.patch` (at #8334) that concerns `sage/rings/ring.pyx`
- a tiny fix to remove the code in `ideal_1poly_field` that calls `residue_field`, since the residue fields code isn't going in until a subsequent patch.

I have checked that this applies cleanly to 4.6.alpha1 and passes long doctests.


---

Comment by davidloeffler created at 2010-09-23 15:36:30

Changing keywords from "" to "ideals".


---

Comment by davidloeffler created at 2010-09-23 15:36:30

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-28 10:55:25

Resolution: fixed
