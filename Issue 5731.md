# Issue 5731: Update NTL to 5.5 release (latest upstream)

Issue created by migration from https://trac.sagemath.org/ticket/5731

Original creator: mabshoff

Original creation time: 2009-04-10 08:11:36

Assignee: mabshoff

CC:  cremona

2009.04.08: Changes between NTL 5.4.2 and 5.5 from http://www.shoup.net/ntl/doc/tour-changes.html

 * Added the ability to generate a shared library (with help from Tim Abbott). Details.
 * Fixed some standardization issues (with help from Tim Abbot): default location of installed documentation files now conforms to standards; use of EOF now conforms to standards.
Added a callback mechanism to NTL's error reporting function. See ErrorCallback in tools.txt.
 * Added support for the gf2x library for speeding up arithmetic in GF2X (with help from Emmanuel Thomé).
  * In conjuction with the above, I also changed the GF2X so that it works better with very large polynomials: large blocks of memory are released, recursive HalfGCD algorithms are used for large polynomials.
 * Fixed a bug in void TraceMod(zz_p& x, const zz_pX& a, const zz_pXModulus& F) (reported by Luca De Feo).
 * Fixed a performance issue in various versions of SetCoeff (reported by Luca De Feo).
 * Fixed the declaration of mat_zz_p transpose(const mat_zz_p& a) (reported by Benoit Lacelle).

So we should be able to drop a couple custom patches.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-10 08:12:43

Changing status from new to assigned.


---

Comment by leif created at 2010-09-03 21:45:33

Changing type from defect to enhancement.


---

Comment by leif created at 2010-09-03 21:45:33

Changing keywords from "" to "upgrade".


---

Comment by leif created at 2010-09-03 21:45:33

Remove assignee mabshoff.


---

Attachment

This works for me with all long tests.


---

Comment by mraum created at 2011-03-21 23:30:25

Changing status from new to needs_review.


---

Comment by fbissey created at 2011-03-22 01:27:54

two things. 
 * trac is not a place to attach spkg. 
 * why is it .p1? It should just be ntl-5.5.2.spkg

Other than that I have no doubts that it works out of the box personally, and you save me from creating a spkg.


---

Comment by cremona created at 2011-03-22 23:33:15

Installed fine for me on top of 4.7.alpha1, and all tests passed.  (ubuntu linux 64-bit).

Note that since several other spkgs use NTL (for example, eclib), someone should check that they all build ok.  One way to do this would be to put the spkg into the next alpha and let the automatic testing system see what happens.


---

Comment by fbissey created at 2011-03-23 00:32:30

I have been using ntl-5.5.2 in sage-on-gentoo since

```
     Mon Nov  9 10:55:35 2009 >>> dev-libs/ntl-5.5.2
       merge time: 10 minutes and 27 seconds.                                                                                       
```

the following depend on ntl:
 * flint
 * singular
 * linbox
 * eclib
 * sage (through c_lib and several extensions so sage -ba is required)

I have rebuild/updated all of those since 2009 so I don't expect any shocking results.


---

Comment by fbissey created at 2011-05-02 00:00:15

I am putting this for 4.7.1. Hopefully I'll find the time to give a proper review.


---

Comment by fbissey created at 2011-05-31 23:06:27

OK I had a closer look at the spkg. First of SPKG.txt hasn't been updated, the hg repo looks ok so I suppose you only changed the content of the src directory. This need a bit of work. I may elect to do the finishing bits if I have time this week.


---

Comment by fbissey created at 2011-05-31 23:06:27

Changing status from needs_review to needs_work.


---

Comment by fbissey created at 2011-06-01 03:36:21

So I have looked more closely. You updated the patches and everything but didn't update the info in SPKG.txt. What I will do is update SPKG.txt with your details make a nice ntl-5.5.2.spkg and post it on google-code and I will put myself and John Cremona as reviewer.

Once that's done can you have a quick check and put it to positive review John?


---

Comment by fbissey created at 2011-06-01 04:01:35

Changing status from needs_work to needs_review.


---

Comment by fbissey created at 2011-06-01 04:01:35

New spkg upload on google-code, link in updated description. Let's get a final sign off on this.


---

Comment by cremona created at 2011-06-01 11:29:33

I am checking this now.

John


---

Comment by cremona created at 2011-06-01 12:12:49

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2011-06-01 12:12:49

Replying to [comment:14 cremona]:
> I am checking this now.
> 
> John

I started with a fresh build of 4.7.1.alpha0 which passes all tests;  built the new spkg here (with SAGE_CHECK=yes"); did "sage -ba" followed by "sage -t -long", and all tests pass.

The spkg itself is ok (though there's a typo "numbery" in the README, and William should probably not be the only spkg maintainer listed), so I am giving this a positive review and hop that it can go into the next alpha form 4.7.1.


---

Comment by jdemeyer created at 2011-06-10 08:52:40

Resolution: fixed
