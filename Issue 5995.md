# Issue 5995: Membership testing for modular forms subspaces is hopeless

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2009-05-06 10:01:31

Assignee: craigcitro

CC:  craigcitro

This is pretty poor, IMHO:

```
sage: M = ModularForms(17, 4)
sage: S = M.cuspidal_submodule()
sage: M.0 == S.0
True
sage: M.0 in S
False
```


As far as I can tell at a glance this is happening because `S.__call__(x)` tests whether or not the parent of x has a canonical inclusion map to S; it should probably be testing whether the parent of x has a canonical inclusion map to the *ambient space* of S.

Once the above is fixed we should also have a method `is_cuspidal()` for modular forms objects, which would be secretly just `self in self.parent().cuspidal_submodule()`. A corresponding `is_eisenstein()` would be good, too.


---

Comment by davidloeffler created at 2009-05-12 08:49:51

apply after #4357 and #5736


---

Attachment

Here's a patch, which adds ` is_cuspidal`, `is_eisenstein`, `is_new` and `is_old`, and corrects a funny glitch whereby elliptic curve newforms consistently claimed not to be cuspidal :-) I wrote the patch and ran tests with this and everything else (including the not-yet-fully-refereed #5968) installed simultaneously, but it should at least apply as long as you have the patches at #4357 and #5736 installed.


---

Comment by cremona created at 2009-05-30 16:06:50

Looks good to me.  Patch applies fine to 4.0 and tests in sage/modular/{modform,hecke} pass.


---

Comment by mhansen created at 2009-06-01 06:16:22

Merged in 4.0.1.alpha0.


---

Comment by mhansen created at 2009-06-01 06:16:22

Resolution: fixed
