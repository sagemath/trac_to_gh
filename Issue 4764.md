# Issue 4764: Error in computing compliment of modular symbol space

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-12-12 01:50:28

Assignee: craigcitro


```
sage: f = EllipticCurve('128a').modular_symbol_space()
sage: f.complement()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/robert/.sage/sage_notebook/worksheets/admin/110/code/7.py", line 7, in <module>
    f.complement()
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
  File "/Users/robert/sage/sage-3.1.3/local/lib/python2.5/site-packages/sage/modular/hecke/submodule.py", line 202, in complement
    raise RuntimeError, "Computation of complementary space failed (cut down to rank %s, but should have cut down to rank %s)."%(V.rank(), self.rank())
RuntimeError: Computation of complementary space failed (cut down to rank 18, but should have cut down to rank 1).
```


Note that the error is wrong, as 


```
sage: ModularSymbols(128, sign=1)
          	

Modular Symbols space of dimension 18 for Gamma_0(128) of weight 2 with sign 1 over Rational Field
```


however, it should have cut the rank down to 17.


---

Comment by craigcitro created at 2008-12-12 02:10:15

This seems to be the same error as #1127 ...

I'm curious whether my (still unfinished) patch from #2535 might help. I don't know that I ever checked ...


---

Comment by robertwb created at 2008-12-12 02:16:41

You're right, it is exactly #1127. I searched before making a ticket, but I guess I didn't go far enough back in time. Hopefully you've already fixed it :). 

I'm closing this as a dupe.


---

Comment by robertwb created at 2008-12-12 02:16:41

Resolution: duplicate
