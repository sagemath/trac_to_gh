# Issue 9836: New PARI and new MPIR don't combine

Issue created by migration from Trac.

Original creator: jdemeyer

Original creation time: 2010-08-29 14:00:49

Assignee: tbd

Combining #9343 (new PARI) and #8664 (MPIR 2.1.1) gives Segmentation Faults.  This problem is not limited to Sage, it is either a bug in PARI or in MPIR.

Test gp script: [http://sage.math.washington.edu/home/jdemeyer/pari-mpir-bug.gp](http://sage.math.washington.edu/home/jdemeyer/pari-mpir-bug.gp)

See also [http://wiki.sagemath.org/NewPARI](http://wiki.sagemath.org/NewPARI)


---

Comment by jdemeyer created at 2010-08-29 14:11:46

This line from the PARI source code (src/kernel/gmp/mp.c:952) says it all:


```
#if 1 /* use undocumented GMP interface */
```


Changing that to a zero solves the problem.


---

Comment by leif created at 2010-08-29 14:20:20

Replying to [comment:1 jdemeyer]:
> This line from the PARI source code (src/kernel/gmp/mp.c:952) says it all:
> 

```
#if 1 /* use undocumented GMP interface */
```

> 
> Changing that to a zero solves the problem.

:D Thanks, I didn't want to track this down further...

Funny, because _GMP_ (5.0.1) dropped other things not part of the _public_ interface, which are still available in the newest MPIR.


---

Comment by leif created at 2010-08-29 14:22:35

P.S.: Yet another major single-character patch... ;-)


---

Comment by leif created at 2010-08-29 14:40:48

Should we patch it to

```
#ifdef PARI_USE_GMP_INTERNALS
```

rather than

```
#if 0
```

?


---

Comment by jdemeyer created at 2010-08-29 15:24:04

It's actually an MPIR issue, I will report it to the MPIR people.  The following MPIR program gives a Segmentation Fault:


```
#include <mpir.h>
int main()
{
    mpz_t Z, R;
    mpz_init(Z);
    mpz_init(R);
    mpz_ui_pow_ui(Z, 10, 100000);
    mpz_divexact(R, Z, Z);
    return 0;
}
```



---

Comment by leif created at 2010-08-31 01:46:13

Cross-replying to [comment:ticket:9343:359 jdemeyer]:
> Replying to [comment:ticket:9343:357 leif]:
> >  * preparing a PARI 2.4.3.svn-12577.p5 spkg, with the fixes from #9722, and in addition disabling the use of GMP internals by PARI by default (with an _option_ to make PARI use them)
> 
> I'm assuming you refer to the "GMP internals" mentioned in #9837?

Yes. I intended to simply change the `#if 1` to `#ifdef PARI_USE_GMP_INTERNALS` in `mp.c`, which we already patch. (I've in fact already prepared and tested a `.svn-12577.p4.5` spkg with exactly that change; all long tests passed.)

Then in case somebody wanted to enable PARI's use of "whatever" (see below), he could simply add `-DPARI_USE_GMP_INTERNALS` to `CFLAGS`, or we could do that if some (other) environment variable is set [to `yes`].

> Note that these are actually *documented* GMP internals, so it's not as bad as it sounds.

I haven't checked this. To me, it is rather irrelevant if they are _documented_ or not, but rather whether they are part of the official / *public* interface to GMP. If those features PARI uses aren't, we should IMHO disable their use _by default_. So correct me if my assumption is false; I'll perhaps later take a closer look at what PARI considers "undocumented" (but not at the moment...). The odd thing is that the `#else` branch currently contains `TODO`s (though it seems functional at least for the purpose of Sage).

> So I would prefer not to touch that code and leave PARI using documented GMP/MPIR internals as it is.

Since we already patch `mp.c`, I think it doesn't hurt to add the above change to it.

We can then easily enable or disable the use in `spkg-install` and/or by setting environment variables, which may be valuable for testing, without changing the spkg at all.

The remaining question would be whether to _enable_ or _disable_ it by default. With _MPIR_ the Sage standard package, I preferred the latter. 

> Also, on the who-is-doing-what part: I am not doing anything with this for the moment (I do plan to release a prealpha4 when leif's done with p5).

I don't know if _"with this"_ referred to the PARI _spkg_, the ticket (#9343), or PARI in general... ;-)

I'll again ask at #9343 if anyone plans to add doctests or at least missing docstrings (to the Sage library part of PARI / #9343). I am not..., only perhaps going to fix the Sphinx warnings.


---

Comment by jdemeyer created at 2010-08-31 06:20:40

Replying to [comment:8 leif]:
> I'll again ask at #9343 if anyone plans to add doctests or at least missing docstrings (to the Sage library part of PARI / #9343). I am not..., only perhaps going to fix the Sphinx warnings.

I believe the Sphinx warnings come from #9400 and I will fix these when I have time.


---

Comment by jdemeyer created at 2010-08-31 06:27:25

Replying to [comment:8 leif]:
> I haven't checked this. To me, it is rather irrelevant if they are _documented_ or not, but rather whether they are part of the official / *public* interface to GMP.

This is how the MPIR documentation phrases the internals used by PARI:
> *This chapter is provided only for informational purposes and the various internals described*
> *here may change in future MPIR releases. Applications expecting to be compatible with future*
> *releases should use only the documented interfaces described in previous chapters.*

> Since we already patch `mp.c`, I think it doesn't hurt to add the above change to it.
Well, it depends because in this case, using the internals means a potentially significant speed gain.

> > Also, on the who-is-doing-what part: I am not doing anything with this for the moment (I do plan to release a prealpha4 when leif's done with p5).
> 
> I don't know if _"with this"_ referred to the PARI _spkg_, the ticket (#9343), or PARI in general... ;-)
The only thing I'll do is release a new prealpha when PARI p5 is out and to fix the few remaining issues in #9400.


---

Comment by wbhart created at 2010-09-04 13:05:42

This got filed as "reported upstream, little or no feedback". How did it get reported originally, because I only received the report yesterday, and since then there are five or six replies on the MPIR devel list.

Anyhow, just to update, it looks like we found the bug in MPIR. Just have to patch it now.

With regard to the "undocumented interface", if Pari currently builds against MPIR without missing symbol errors, then it is likely that it is relying on now documented symbols in both GMP and MPIR. The disclaimer is out-of-date. It has been removed in the GMP manual, but we have forgotten to remove it in the MPIR manual. I will make a note on the MPIR devel list to do so.

If there are missing symbol errors, then I guess it relied on undocumented functions in *GMP* but not in MPIR. That would be a different (but surprising) situation.


---

Comment by wbhart created at 2010-09-04 15:22:42

Just to save someone writing a response, this was originally reported to thempirteam email address, which because of technical problems was not being accessed. So, it was reported in the correct way, 6 days ago, and there would have indeed been little to no response over that time due to hardware issues. Sorry for the noise.


---

Comment by jdemeyer created at 2010-09-05 12:19:05

Changing status from new to needs_review.


---

Comment by leif created at 2010-09-05 16:14:33

What does "needs review" mean? Confirming that PARI uses *documented* GMP features? Or that it's an _MPIR_ bug?

I'd say we (i.e. the release manager) can close this ticket as "fixed". #8664 should not be merged until there's MPIR 2.1.2 or alike with this bug fixed; I think we agreed on that.


---

Comment by jdemeyer created at 2010-09-05 16:21:24

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-09-05 16:21:24

Positive review for the fact that it is an MPIR bug which has been fixed upstream.


---

Comment by mpatel created at 2010-09-15 11:53:55

Resolution: fixed


---

Comment by mpatel created at 2010-09-15 11:53:55

Feel free to edit the "Author(s)" and "Reviewer(s)" fields.
