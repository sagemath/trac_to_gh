# Issue 7704: bug in sparse matrix det

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-16 08:13:27

Assignee: was

CC:  spancratz


```
sage: matrix(ZZ,4,sparse=True).det()
...
TypeError: charpoly() takes at most 1 positional argument (2 given)
```



---

Attachment


---

Comment by was created at 2009-12-16 08:34:24

Changing status from new to needs_review.


---

Comment by spancratz created at 2009-12-19 01:08:52

Very minor cosmetic change to the method


---

Attachment

The patch looks fine, and ``make test`` on my installation of SAGE 4.2.1 returns only one unrelated error, which I include for completeness:


```
sage -t  "devel/sage/sage/plot/plot3d/tachyon.py"
```



```
File "/scratch/pancratz/sage-4.2.1/devel/sage/sage/plot/plot3d/tachyon.py", line 297:
    sage: os.system('rm ' + tempname)
Expected:
    0
Got:
    256
```


I have attached an additional patch which removes one unused local variable.

Sebastian


---

Comment by was created at 2009-12-29 08:34:33

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 21:32:11

Resolution: fixed
