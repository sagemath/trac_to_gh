# Issue 4337: modular forms -- compute action of Hecke operators on Gamma_1(N) modular forms

Issue created by migration from https://trac.sagemath.org/ticket/4337

Original creator: was

Original creation time: 2008-10-22 17:46:16

Assignee: craigcitro


```
sage: ModularForms(Gamma1(11),2).hecke_matrix(2)
boom!
```


and a genuine bug:

```
sage: ModularForms(GammaH(11, [2]),2).hecke_matrix(2)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
...
RuntimeError: maximum recursion depth exceeded in cmp
```



---

Attachment

patch against 3.4.2.final


---

Comment by davidloeffler created at 2009-05-05 16:49:20

Changing assignee from craigcitro to davidloeffler.


---

Comment by davidloeffler created at 2009-05-05 16:49:20

I believe I've fixed the Gamma1 bug; I've checked the algorithm by comparing the output with the obvious algorithm of summing over the character spaces for all characters of the given modulus, and it seems to agree (and it's a lot quicker). 

The GammaH one is more deep-rooted -- just about nothing works for spaces of GammaH forms, not even the basis() method. I've inserted a dummy routine that raises a NotImplementedError at an appropriate place, which is better than the current infinite loop. It will be easy to add computation of Hecke ops for modular forms for GammaH once we have them for the corresponding spaces of modular symbols.


---

Comment by davidloeffler created at 2009-05-05 16:49:20

Changing status from new to assigned.


---

Attachment


---

Comment by craigcitro created at 2009-05-08 06:58:03

This looks really good. Positive review! Here are my comments:

 * I'm really happy to see that this code is written! I'm very happy with how all the code works. This is actually functionality that Magma doesn't even have. Bravo, David!

 * I moved a few bits of code around, and did a few things to make the code run faster. On the (few) benchmarks I was running, I got a factor of 2 speedup for `_compute_hecke_matrix` on cuspidal subspaces, and about 1.5 on the Eisenstein part. (There's more post-processing to be done in the Eisenstein case.)

 * Unfortunately, this algorithm gets slow pretty fast. For instance, trying to compute the Hecke operators on something like `ModularForms(Gamma1(48),4)` is just hopeless in this case. We should try to talk about what else we could do that might scale a little better. But we *definitely* want this merged first!

David, I've added a few changes in my referee patch -- could you look over the changes and make sure you're okay with them? Most of it is just cleanup; the only change I'd really demand is renaming the variable you called `QQ`, since I think it's pretty confusing to have a local variable named `QQ`, even if it's going to be the global `QQ` 99% of the time.


---

Comment by davidloeffler created at 2009-05-08 09:56:35

Thanks for reviewing this. I'd actually never come across the python "for/else" syntax before; it's a neat trick, I'll have to remember it. I'm happy with the changes you propose.

Unfortunately, I've realised that there *is* a problem in my patch: in trying to prevent the infinite loop for GammaH, I've broken something else. The loop comes up because the default behaviour for the generic cuspidal submodule class is to get its q-expansions from its ambient space; and the generic ambient space class gets its q-expansions from its ambient modules.

Now, for *most* derived classes it's the cuspidal and eisenstein subs that have this overridden, but for the "ambient_R" class, it's the ambient space that overrides it. So my patch breaks calculation of q-expansion bases -- and consequently everything else -- for forms over a non-minimal base ring.

So here's a third patch, which fixes this and adds a doctest.

David


---

Comment by craigcitro created at 2009-05-08 10:01:19

I think something is wrong with the third patch? trac tells me it's 225 bytes, which seems unlikely. Can you re-upload it?


---

Attachment


---

Comment by davidloeffler created at 2009-05-08 10:08:38

Oops, I forgot to qrefresh before I exported. Here it is.


---

Comment by craigcitro created at 2009-05-08 10:12:21

Nice catch! I'm happy with the `_R`-related changes ... positive review! (I was apparently sloppy while reviewing and only worked over `QQ` ... I'm glad you were experimenting with quadratic imaginary fields!)


---

Comment by davidloeffler created at 2009-05-11 07:04:34

Looks like you weren't the only one that was sloppy: neither of us ran a full doctest cycle, so neither of us spotted the fact that this causes a doctest failure in William's Bordeaux lectures. One of those specifically states, with a doctest to prove it, that computing Hecke matrices for Gamma1(N) raises a `NotImplementedError`.


---

Attachment

apply over previous three


---

Comment by mabshoff created at 2009-05-11 07:47:10

Merged all four patches in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-11 07:47:10

Resolution: fixed
