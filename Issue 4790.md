# Issue 4790: sage -t does not take into account the current directory

Issue created by migration from https://trac.sagemath.org/ticket/4790

Original creator: gfurnish

Original creation time: 2008-12-14 05:28:39

Assignee: mabshoff

This is a split of #3677.  
At the end of testing when reporting the results, sage -t does not take into account the current directory. It produces output like this: 

```
        sage -t  devel/sage-combinat/sage/combinat/root_system/root_lattice_realization.py
	sage -t  devel/sage-combinat/sage/combinat/root_system/root_space.py
	sage -t  devel/sage-combinat/sage/combinat/root_system/root_system.py
	sage -t  devel/sage-combinat/sage/combinat/root_system/weight_space.py
```


when it should be giving output like 


```
        sage -t  ambient_space.py
	sage -t  root_lattice_realization.py
	sage -t  root_space.py
	sage -t  root_system.py
	sage -t  weight_space.py
```



---

Comment by roed created at 2013-03-14 21:56:00

Changing status from new to needs_review.


---

Comment by roed created at 2013-03-14 21:56:00

This is resolved by #12415.


---

Comment by roed created at 2013-03-14 21:56:16

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-15 13:00:47

Resolution: duplicate
