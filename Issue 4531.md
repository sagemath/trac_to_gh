# Issue 4531: Sage 3.2.rc1: automorphism_group() doctest failure on 32 bit in sage/combinat/species/library.py

Issue created by migration from https://trac.sagemath.org/ticket/4531

Original creator: mabshoff

Original creation time: 2008-11-15 20:13:32

Assignee: mhansen


```
sage -t  devel/sage/sage/combinat/species/library.py 
********************************************************************** 
File "/home/john/sage-3.2.rc1/devel/sage/sage/combinat/species/library.py", 
line 86: 
    sage: a.automorphism_group() 
Expected: 
    Permutation Group with generators [(), ()] 
Got: 
    Permutation Group with generators [()] 
********************************************************************** 
```



---

Comment by GeorgSWeber created at 2008-11-16 10:43:00

That seems to be a problem of how Sage displays/prints permutation groups. Internally, everything seems fine. I just produced such a group and I get:

```
sage: B = species.BinaryTreeSpecies()
sage: a = B.structures([1,2,3,4,5]).random_element(); a
(1*5)*((2*3)*4)
sage: grp = a.automorphism_group()
sage: grp
Permutation Group with generators [(), ()]
sage: grp.list()
[()]
```

The latter two lines are pretty inconsistent.


---

Comment by mabshoff created at 2008-11-16 10:44:49

Mike Hansen mentioned in IRC that this is the expected output and will post a patch to fix this in the morning.

Cheers,

Michael


---

Comment by GeorgSWeber created at 2008-11-16 10:46:46

OK. Thanks for this info!


---

Comment by was created at 2008-11-18 07:16:38

I am fixing this by changing permutation groups to make their gens be canonicalized by default (meaning they are sorted and duplicates are removed).  This is *much* more in the spirit of Sage.  There is still the option to have the generators be exactly what is input (duplicates and all).


---

Comment by was created at 2008-11-18 07:16:38

Changing assignee from mhansen to was.


---

Attachment


---

Attachment


---

Attachment

trivial followup


---

Comment by mabshoff created at 2008-11-18 19:40:27

mhansen gave this patch a positive review assuming the doctests pass. Since they do I am changing the subject.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-18 19:40:44

Resolution: fixed


---

Comment by mabshoff created at 2008-11-18 19:40:44

Merged all three patches in Sage 3.2.rc2
