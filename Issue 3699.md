# Issue 3699: rewrite free_module.py to use basis matrices everywhere

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-07-21 21:39:05

Assignee: tbd

You should only do this on top of patch #3514.


---

Comment by cwitty created at 2008-08-02 14:12:48

I'm not sure exactly what you mean here, but if it would involve computing the basis_matrix for all `FreeModules` (even in the `FreeModule_ambient` case, where currently the basis_matrix is only computed lazily when requested) I think it's a bad idea unless the following can be vastly sped up:

```
sage: %time K = FreeModule(ZZ, 2000)
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: %time _ = K.basis_matrix()
CPU times: user 191.08 s, sys: 19.63 s, total: 210.71 s
Wall time: 210.69 s
```



---

Comment by was created at 2008-08-03 17:27:55

> I'm not sure exactly what you mean here, but if it would involve computing the 
> basis_matrix for all FreeModules (even in the FreeModule_ambient case, where
> currently the basis_matrix is only computed lazily when requested) I think 
> it's a bad idea unless the following can be vastly sped up:

It would *only* involve computing the basis matrix for proper *submodules*, where
currently exactly equivalent (namely a list of basis vectors) but vastly 
harder to work with data is computed and carried around. 

By the way, regarding your example, that is just creating the 2000x2000 identity
matrix, which can be sped up, see:

```
sage: time a = identity_matrix(ZZ,2000)
CPU times: user 0.27 s, sys: 0.05 s, total: 0.32 s
```


A cheap easy patch that vastly speeds up sage would be one that optimizes the
basis_matrix function for ambient free modules to just call the identity matrix
command :-).


---

Attachment

Patch attached which does what I think was intended.  Based on 3.4, all tests in sage/modules should pass.


---

Comment by cremona created at 2009-05-30 15:47:13

This still applies fine to 4.0 and is still in need of a review -- should be very quick!  All doctests in sage/modules pass.


---

Comment by AlexGhitza created at 2009-06-02 08:56:17

Looks good to me.


---

Comment by mhansen created at 2009-06-03 18:29:24

Resolution: fixed


---

Comment by mhansen created at 2009-06-03 18:29:24

Merged in 4.0.1.rc0.
