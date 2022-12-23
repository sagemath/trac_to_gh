# Issue 2959: bug in DirichletGroup over a finite base ring

Issue created by migration from https://trac.sagemath.org/ticket/2959

Original creator: wdj

Original creation time: 2008-04-19 21:32:13

Assignee: was


```

sage: G = DirichletGroup(21)
sage: chi = G.0; chi
[-1, 1]
sage: chi.values()
[0, 1, -1, 0, 1, -1, 0, 0, -1, 0, 1, -1, 0, 1, 0, 0, 1, -1, 0, 1, -1]
```


So far, so good (similar code is in the tutorial: http://www.sagemath.org/doc/html/tut/node15.html). Now use a different base ring:


```
sage: G = DirichletGroup(21, GF(37))
sage: chi = G.0; chi
[36, 1]
sage: chi.values()
---------------------------------------------------------------------------
<type 'exceptions.IndexError'>            Traceback (most recent call last)

/mnt/drive_hda1/sagefiles/sage-3.0.alpha5/<ipython console> in <module>()

/mnt/drive_hda1/sagefiles/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/modular/dirichlet.py
in values(self)
  1056             ########################
  1057             # record character value on n
-> 1058             result_list[n.ivalue] = R_values[value.ivalue]
  1059             # iterate:
  1060             #   increase the exponent vector by 1,

<type 'exceptions.IndexError'>: list index out of range
```




---

Comment by craigcitro created at 2008-04-19 23:54:27

Changing assignee from was to craigcitro.


---

Comment by craigcitro created at 2008-04-19 23:54:27

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-04-19 23:54:27

Yep, this was a mistake on my part. The attached patch fixes it, adds a few doctests to check the various possibilities (i.e. when the zeta_order of the base_ring is a proper divisor of, is equal to, and is strictly divisible by the modulus for the DirichletGroup).


---

Attachment


---

Comment by was created at 2008-04-20 00:13:07

Looks good; works.


---

Comment by mabshoff created at 2008-04-20 00:36:59

Merges in Sage 3.0.rc0


---

Comment by mabshoff created at 2008-04-20 00:36:59

Resolution: fixed
