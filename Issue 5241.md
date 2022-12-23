# Issue 5241: Matrix Group sometimes assumes base ring is a field

Issue created by migration from https://trac.sagemath.org/ticket/5241

Original creator: kcrisman

Original creation time: 2009-02-12 01:40:40

Assignee: joyner

CC:  joyner

From sage-support:


```
sage: M1 = matrix(ZZ,2,[[-1,0],[0,1]]) 
sage: M2 = matrix(ZZ,2,[[1,0],[0,-1]]) 
sage: M3 = matrix(ZZ,2,[[-1,0],[0,-1]]) 
sage: MG = MatrixGroup([M1, M2, M3]) 
sage: MG.order() 
    4 
sage: MG.list() 
    Traceback (click to the left for traceback) 
    ... 
    AttributeError: 'sage.rings.integer_ring.IntegerRing_class' object 
has 
    no attribute 'prime_subfield' 
```


The offending code is in groups/matrix_gps/matrix_group.py where the problem is in the list method of MatrixGroup.


```
429        F = self.field_of_definition()
430        n = F.degree()
431        p = F.characteristic()
432        a = F.prime_subfield().multiplicative_generator()
433        b = F.multiplicative_generator()
```


In the class definition of MatrixGroup, any base ring is allowed.  But at least this particular method (others?) assume that the base ring is in fact in a field.  

Since a and b above are definitely used later in list(), as this all calls GAP, someone with a good knowledge of GAP should address this - and look for other places it's assumed that the base ring is a field and at least catch that exception with a better error message.  



---

Comment by wdj created at 2009-02-17 02:53:46

to be applied to sage-3.3.alpha6


---

Attachment

This passes sage -t but sage -testall has lots of (unrelated I think) failures. It simply fixes the bug reported and adds the required docstring examples.


---

Comment by kcrisman created at 2009-03-06 15:45:00

Will this need rebase against 3.4?


---

Comment by kcrisman created at 2009-03-16 15:25:21

Against 3.4:

patching file sage/groups/matrix_gps/matrix_group.py
Hunk #1 FAILED at 410
1 out of 3 hunks FAILED -- saving rejects to file sage/groups/matrix_gps/matrix_group.py.rej
abort: patch failed to apply

The hunk that didn't apply was the documentation hunk, as it turns out, unsurprisingly.

So it does need a rebase.  Sorry it took a while to be able to check this; it's sometimes complicated for me to do these things in a timely fashion, particularly with the 3.4 upgrade this was the case.


---

Comment by AlexGhitza created at 2009-05-31 13:19:41

I have rebased the patch against 4.0 and tested it.  Looks good to me.

Apply only `trac_5241-rebased.patch`.


---

Attachment

rebased against 4.0


---

Comment by mhansen created at 2009-06-01 05:36:29

Merged in 4.0.1.alpha0.


---

Comment by mhansen created at 2009-06-01 05:36:29

Resolution: fixed
