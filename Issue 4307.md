# Issue 4307: bad error message in SupersingularModule constructor

Issue created by migration from https://trac.sagemath.org/ticket/4307

Original creator: was

Original creation time: 2008-10-16 09:21:45

Assignee: craigcitro


```
sage: SupersingularModule(15)
Traceback (most recent call last):
...
ValueError: order of finite field must be a prime power
```


The error message should say something like:

```
NotImplementedError: supersingular module of non-prime level not yet implemented
```



---

Comment by was created at 2008-10-16 09:21:55

Changing priority from major to minor.


---

Comment by AlexGhitza created at 2008-10-18 04:13:25

Having looked at the code in ssmod.py, it seems to me that any nontrivial functionality is only implemented for level 1 at the moment.  Two things that I tried: dimension() and hecke_matrix().

The attached patch raises ValueErrors if the characteristic is not prime or if the level is not coprime to the characteristic, and a NotImplementedError if the level is > 1.

Extending the functionality in ssmod.py to general levels is right up my alley, so I'll look into doing it in the near future.  The code could also use more documentation and tests.


---

Comment by mabshoff created at 2008-10-20 16:37:35

Alex,

please add doctests that show the new behavior to the not yet existing class SupersingularModule(hecke.HeckeModule_free_module) docstring.

Cheers,

Michael


---

Attachment

Yes.  Done, and replaced the patch.


---

Comment by craigcitro created at 2008-10-22 04:18:41

Looks good.


---

Comment by mabshoff created at 2008-10-26 01:35:16

Merged in Sage 3.2.alpha1


---

Comment by mabshoff created at 2008-10-26 01:35:16

Resolution: fixed
