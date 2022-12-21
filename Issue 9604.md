# Issue 9604: Tracker bug for toric varieties

Issue created by migration from Trac.

Original creator: vbraun

Original creation time: 2010-07-26 17:21:42

Assignee: AlexGhitza

CC:  novoselt

This bug tracks the current status of the toric varieties code and the interdependence of new patches. The prerequisites are Sage 4.5.2.alpha0 (which should be equivalent to the 4.5.2 release).

  * #9470: Switch toric varieties to enhanced fans
  * #9326: Add cohomology of toric varieties
  * #9502: Basis parent bug in FreeModule
  * #9504: Add support for toric sublattices
  * #9296: Add lattice computations for convex polyhedral cones
  * #9337: Toric divisors

We expect the above to be ready for inclusion in Sage 5.0.


---

Comment by mpatel created at 2010-08-07 06:01:24

Can I merge #9470 and #9326 now, or should I wait until every ticket has a positive review?


---

Comment by vbraun created at 2010-08-07 14:31:23

#9470 and #9326 are ready to be merged, but I thought that 4.5.2 is in feature freeze now?


---

Comment by mpatel created at 2010-08-07 19:26:38

Replying to [comment:3 vbraun]:
> #9470 and #9326 are ready to be merged, but I thought that 4.5.2 is in feature freeze now?

Indeed, we'll release 4.5.2 very soon.  I've been preparing a 4.5.3.alpha0.


---

Comment by vbraun created at 2010-08-23 21:44:55

updated patch


---

Attachment

I'll put bugs in front of toric divisors, since they have chances to be settled quickly.


---

Comment by novoselt created at 2010-08-30 05:58:21

I sneaked in yet another patch in front of toric divisors, in case it will be useful for Kaehler/Mori cones (maybe not due to dimension limitations), but so far it is independent of #9337 and can be shifted down.


---

Comment by vbraun created at 2010-09-27 17:18:32

Changing status from new to needs_work.


---

Comment by vbraun created at 2010-10-04 20:16:51

`trac_9664_add_toric_potter.patch` depends on `trac_9972_add_toric_lattice_morphisms.patch`. No logical dependency, but thats how the patch works out. I don't think order matters too much on that one, just wanted to get it right.


---

Comment by novoselt created at 2010-10-04 20:33:21

No more dependence ;-)


---

Comment by SimonKing created at 2010-12-22 13:35:09

Sorry for temporarily making #10513 a dependency. This ticket isn't ready, yet. Thus I reoved the dependency again.


---

Comment by novoselt created at 2010-12-22 16:12:23

Tried to make all dependencies and especially their absences more clear.

Volker, I am a little confused by comments on #8169 and #9918 - do they depend on/conflict with each other somehow?


---

Comment by vbraun created at 2010-12-22 16:23:24

#9918 uses the TOPCOM spkg (in #8169) if it is available, and falls back to its own implementation if not. So there is no dependency either way. Except that applying #8169 without #9918 would be meaningless as there would be nothing in the sage library to use TOPCOM.


---

Comment by novoselt created at 2010-12-22 16:27:15

So none of the patches of #8169 should be applied, it just provides an optional package, correct?


---

Comment by vbraun created at 2010-12-22 16:29:33

Yes, none of the patches in #8169 should be applied.


---

Comment by vbraun created at 2010-12-28 00:16:03

I've started to put my patch queue into a mercurial repository itself. See

https://bitbucket.org/vbraun/mq-for-sage-toric-varieties/src


---

Comment by novoselt created at 2011-03-03 02:44:28

Changing keywords from "" to "toric geometry".


---

Comment by novoselt created at 2017-01-02 22:54:29

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2017-01-02 22:54:29

With trac dependencies, long history here, and generally low toric activity I propose closing this ticket.


---

Comment by chapoton created at 2018-11-30 20:52:55

indeed. And there is still the "toric" keyword to gather these tickets


---

Comment by chapoton created at 2018-11-30 20:52:55

Changing status from needs_review to positive_review.


---

Comment by embray created at 2019-02-26 13:58:00

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.


---

Comment by embray created at 2019-02-26 13:58:00

Resolution: invalid
