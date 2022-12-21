# Issue 9756: Document SAGE_TUNE_pari in Sage installation guide.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-08-17 17:36:14

Assignee: mvngu

CC:  jhpalmieri jdemeyer cremona

If the variable `SAGE_TUNE_pari` is exported to "yes", Pari will go through a tuning process to optimize the code for a particular computer. This takes considerable time, so the default behavior is not to tune Pari. 

This is implemented in a Pari snapshot (see #9343), but it not documented.


---

Comment by leif created at 2010-08-17 18:42:33

If we support that at all, we should also emphasize that this is hardly tested and (at least currently) fails on some (or a lot of?) machines...


---

Comment by leif created at 2010-08-17 18:48:48

Btw, shouldn't it be documented in the Sage *Installation* Guide [as well]?


---

Comment by leif created at 2010-08-17 18:50:35

LOL, forget my last post. I should get some food and/or sleep... ;-)


---

Comment by jhpalmieri created at 2010-08-17 18:53:26

Replying to [comment:2 leif]:
> If we support that at all, we should also emphasize that this is hardly tested and (at least currently) fails on some (or a lot of?) machines...

Well, I was hoping that this would get straightened out by #9343.  I agree that if this doesn't work, then there is no point documenting it (and also the message printed by the pari spkg-install script should say that it's buggy).


---

Comment by drkirkby created at 2010-08-19 09:50:30

As noted on #9343, the problem with Pari tuning has been reported to the Pari developers. See http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1089


---

Comment by leif created at 2010-09-03 23:35:49

Replying to [comment:5 jhpalmieri]:
> [...] (and also the message printed by the pari spkg-install script should say that it's buggy).

It meanwhile does so.

I still prefer following the convention that [exported] environment variables should be all uppercase (i.e. `SAGE_TUNE_PARI`), and am currently supporting that (in addition) in a new PARI 2.4.3.svn-12577.p5 spkg.


---

Comment by drkirkby created at 2010-09-03 23:59:51

Replying to [comment:7 leif]:
> Replying to [comment:5 jhpalmieri]:
> > [...] (and also the message printed by the pari spkg-install script should say that it's buggy).
> 
> It meanwhile does so.
> 
> I still prefer following the convention that [exported] environment variables should be all uppercase (i.e. `SAGE_TUNE_PARI`), and am currently supporting that (in addition) in a new PARI 2.4.3.svn-12577.p5 spkg.

I think it was Peter Jeremey that proposed the lower case, and showed some code how one could get it inside an arbitrary package (say ATLAS) from the package name. (This was in relation to the number of threads ATLAS uses). 

I don't have a big problem with upper or lower case, though I think there's an argument for making the global ones that affect every package upper case, and appending lower case for those that only affect a single package. But it's hardly a big deal either way. 

Dave


---

Comment by leif created at 2010-09-04 00:16:55

Replying to [comment:8 drkirkby]:
> Replying to [comment:7 leif]:
> > I still prefer following the convention that [exported] environment variables should be all uppercase (i.e. `SAGE_TUNE_PARI`), and am currently supporting that (in addition) in a new PARI 2.4.3.svn-12577.p5 spkg.
> 
> I think it was Peter Jeremey that proposed the lower case, and showed some code how one could get it inside an arbitrary package (say ATLAS) from the package name.

Ever heard of `tr`? ;-)

> I don't have a big problem with upper or lower case, though I think there's an argument for making the global ones that affect every package upper case, and appending lower case for those that only affect a single package.

Doesn't make sense to me (unless we accept _both_ lower as well as uppercase, which IMHO isn't a good idea either).

> But it's hardly a big deal either way. 

It isn't, but we shouldn't produce too much confusion, neither to the developers nor to the users.
Keeping it all uppercase is in my opinion the (conformant and) least annoying choice.

Otherwise we'd also run into problems with "PARI" vs. "pari", "NTL" vs. "ntl", "PolyBoRi" vs. "POLYBORI" vs. "polybori" etc. I think.


---

Comment by leif created at 2010-09-04 02:56:30

I'd suggest supporting `SAGE_TUNE_ALL=yes`, too.

And perhaps `SAGE_TUNE="package1 package2 ..."` (with of course only the package's basename), perhaps also `SAGE_TUNE=all`, `SAGE_TUNE=default`, `SAGE_TUNE=no`, with some handling / "normalization" in `sage-spkg`, s.t. not every potential `spkg-install` has to deal with lots of different cases.

ATLAS will tune itself anyway; I'm currently not sure with NTL. GMP-ECM (and GMP) can, but not as easily (would require some script "hacking").

We should make sure self-tuning uses CPU time as the measure, not wall time.

----

Similar extensions to `SAGE_CHECK[_*]` may be desirable.


---

Comment by drkirkby created at 2010-09-04 06:45:22

Replying to [comment:10 leif]:
> I'd suggest supporting `SAGE_TUNE_ALL=yes`, too.
> 
> And perhaps `SAGE_TUNE="package1 package2 ..."` (with of course only the package's basename), perhaps also `SAGE_TUNE=all`, `SAGE_TUNE=default`, `SAGE_TUNE=no`, with some handling / "normalization" in `sage-spkg`, s.t. not every potential `spkg-install` has to deal with lots of different cases.
> 
> ATLAS will tune itself anyway; I'm currently not sure with NTL. GMP-ECM (and GMP) can, but not as easily (would require some script "hacking").
> 
> We should make sure self-tuning uses CPU time as the measure, not wall time.
> 
> ----
> 
> Similar extensions to `SAGE_CHECK[_*]` may be desirable.

There have been a number of complaints about the growing number of environment variables. They are not popular!

That said, I personally think these sort of things are desirable. For example, when I asked people to run the Python tests, there's not been a single person who reported they could get all the Python tests to pass. So running SAGE_CHECK will always fail. 

I personally think having those that are for specific packages end in lower case does make them more obvious. All packages are listed in lower case in Sage, so ATLAS is atlas, PolyBoRi is polybori etc. 

Dave


---

Comment by mkoeppe created at 2022-07-27 05:22:21

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2022-07-27 05:22:21

`SAGE_TUNE_PARI` is documented in the installation manual, and both `SAGE_TUNE_PARI` and `SAGE_TUNE_pari` are handled in `build/pkgs/pari/spkg-install.in`. So this ticket can be closed


---

Comment by jhpalmieri created at 2022-07-27 17:05:59

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2022-08-02 06:31:03

Resolution: invalid
