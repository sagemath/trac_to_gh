# Issue 4910: convert sage.functions.* docstrings to Sphinx

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-01-01 22:50:50

Assignee: tba




---

Attachment


---

Attachment

I've found some minor problem in the patch:


```
-  Each *Legendre polynomial* `P_n(x)` is an $n$-th degree polynomial. 
```

Should be

```
-  Each *Legendre polynomial* `P_n(x)` is an `n`-th degree polynomial. 
```


And a little bit lower:

```
 The *Legendre function of the second kind* $Q_n(x)$ is another 
```

Should be

```
 The *Legendre function of the second kind* `Q_n(x)` is another 
```


A whole section

```
Implemented methods: 
  9 latex outout 
  10 __call__ 
[...]
  39 extend_by_zero_to 
  40 unextend 
```

seems to have vanished.


---

Comment by hivert created at 2009-02-24 15:36:33

I've manually edited the patch to fixes the two "$" vs "`" problems. The corrected patch should follow. 

The section implemented methods is removed on purpose (it is redundent with the code). Otherwise it seems Ok.

As for combinat, my rereading was a fast rereading. In particular, There are a lot of formulas that needs time to be checked carfully.


---

Attachment

New patch with hand fix.


---

Comment by mhansen created at 2009-02-24 18:07:32

Changing assignee from tba to mhansen.


---

Comment by mhansen created at 2009-02-24 18:07:32

I put these changes in the fixes.patch in #5330.


---

Comment by mhansen created at 2009-02-24 18:07:32

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-24 18:14:08

Resolution: fixed


---

Comment by mabshoff created at 2009-02-24 18:14:08

Merged sage.functions-final-fixed.patch in Sage 3.4.alpha0.

Cheers,

Michael
