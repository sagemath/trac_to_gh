# Issue 3539: bug in DirichletGroup -- bad code

Issue created by migration from https://trac.sagemath.org/ticket/3539

Original creator: was

Original creation time: 2008-07-01 00:55:36

Assignee: craigcitro


```
Dear SAGE community,

I am trying to compute characters for some finite fields.

With "small" fields, everything is fine:
 sage:   K=CyclotomicField(10);
 sage:   p=10151;
 sage:   Character=DirichletGroup(p,K);
 sage:   Khi=Character.0;
 sage:   Khi(7)
 zeta10

However, with slightly larger fields:
 sage:   K=CyclotomicField(10);
 sage:   p=100151;
 sage:   Character=DirichletGroup(p,K);
 sage:   Khi=Character.0;
 sage:   Khi(7)
 ---------------------------------------------------------------------------
 AttributeError                            Traceback (most recent call
 last)

 /users/cacao/bissogae/<ipython console> in <module>()

 /localdisk/tmp/sage-3.0.3/local/lib/python2.5/site-packages/sage/modular/dirichlet.py
 in __call__(self, m)

 /localdisk/tmp/sage-3.0.3/local/lib/python2.5/site-packages/sage/modular/dirichlet.py
 in values(self)

 AttributeError: 'sage.rings.integer_mod.IntegerMod_int64' object has no
 attribute 'ivalue'

Is there something I am missing?

Thanks,
 --Gaetan
```



---

Comment by wjp created at 2008-07-06 01:27:11

This is because `IntegerMod_int.ivalue` is cdef'ed public but `IntegerMod_int64.ivalue` isn't. The attached patch makes replaces the use of `ivalue` by the `__int___()` method. Timings are somewhat variable, but seem to suggest this makes the `values()` function about 2% slower for the p=10151,100151 cases reported.


---

Attachment


---

Comment by craigcitro created at 2008-07-06 20:51:08

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-07-06 20:51:08

I'm adding a new patch, that is intended as a replacement of the old one. Rob Bradshaw suggseted that directly indexing with the integer mod n would actually be faster than using `n.ivalue` anyway -- on my machine, at least, they're nearly identical, with using `n` directly edging slightly ahead. This patch also includes a doctest to catch this in the future.


---

Attachment


---

Comment by craigcitro created at 2008-07-06 21:00:48

I forgot to mention this on the ticket -- credit should also go to wjp and robertwb.


---

Comment by mabshoff created at 2008-07-07 01:39:44

Merged trac-3539-new-patch.patch in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-07 01:39:44

Resolution: fixed
