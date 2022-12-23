# Issue 376: finite field homomorphisms don't work

Issue created by migration from https://trac.sagemath.org/ticket/376

Original creator: was

Original creation time: 2007-05-23 17:04:26

Assignee: somebody

The following should work and define a homomorphism.
I don't remember actually implementing finite field homomorphisms, so it's
no surprise they don't just magically work.  This is very useful though, so
it needs to get done. 

```
k = GF(73^2,'a')
f = k.modulus()
r = f.change_ring(k).roots()
k.hom([r[0][0]])
///
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/was/edu/2007/bsd/sage_notebook/worksheets/_scratch_/code/15.py", line 4, in <module>
    exec compile(ur'k.hom([r[Integer(0)][Integer(0)]])' + '\n', '', 'single')
  File "/home/was/edu/2007/bsd/", line 1, in <module>
    
  File "parent_gens.pyx", line 505, in parent_gens.ParentWithGens.hom
  File "/home/was/s/local/lib/python2.5/site-packages/sage/rings/homset.py", line 80, in __call__
    raise TypeError, "images do not define a valid homomorphism"
TypeError: images do not define a valid homomorphism
```



```
k.hom([r[1][0]])
///
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/was/edu/2007/bsd/sage_notebook/worksheets/_scratch_/code/16.py", line 4, in <module>
    exec compile(ur'k.hom([r[Integer(1)][Integer(0)]])' + '\n', '', 'single')
  File "/home/was/edu/2007/bsd/", line 1, in <module>
    
  File "parent_gens.pyx", line 505, in parent_gens.ParentWithGens.hom
  File "/home/was/s/local/lib/python2.5/site-packages/sage/rings/homset.py", line 80, in __call__
    raise TypeError, "images do not define a valid homomorphism"
TypeError: images do not define a valid homomorphism
```



---

Comment by craigcitro created at 2007-09-07 02:31:13

Changing assignee from somebody to craigcitro.


---

Comment by craigcitro created at 2007-09-07 02:31:13

I think this patch fixes this bug. Turns out that the whole morphism system depends on the field having a method called _is_valid_homomorphism_ ... sadly, the way errors are caught and handled, this isn't the easiest to track down.


---

Attachment


---

Comment by was created at 2007-09-07 02:51:26

Resolution: fixed
