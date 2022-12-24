# Issue 2114: get gf2x into Sage!

archive/issues_002114.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  zimmerma malb jpflori jdemeyer\n\nCheck out http://wwwmaths.anu.edu.au/~brent/gf2x.html\n\nIt's:\n* by very well respected people\n* GPL'd (v2 or later)\n* Small pure C code:\n\n```\ndhcp46-72:gf2x-0.1 was$ ls\nBestToom.c          README              ToomSpace.c         gen_bb_mul_code.c   mul-tc3w.c          mul2t.c             tune1               tuneup.c\nCOPYING             TC.h                cantor              mul-tc3.c           mul-tc4.c           mulfft-bit.c        tunefft.c\nHalfGCD.c           Toom.c              factor.c            mul-tc3u.c          mul.c               patch-wrt-ntl-5.3.1 tunetoom.c\ndhcp46-72:gf2x-0.1 was$ usage\n4\tBestToom.c\n4\tREADME\n4\tTC.h\n4\tToom.c\n4\tToomSpace.c\n4\tpatch-wrt-ntl-5.3.1\n4\ttune1\n4\ttuneup.c\n8\tgen_bb_mul_code.c\n8\tmul2t.c\n8\ttunefft.c\n12\tmul-tc3.c\n12\tmul-tc3u.c\n12\tmul-tc3w.c\n12\tmul-tc4.c\n12\ttunetoom.c\n16\tHalfGCD.c\n16\tmul.c\n20\tCOPYING\n28\tmulfft-bit.c\n40\tfactor.c\n132\tcantor\n368\ttotal\n```\n\n* and Paul Z. says: \n\n```\nfor your information, on http://wwwmaths.anu.edu.au/~brent/gf2x.html you will\nfind an implementation up to 5 times faster than NTL's GF2X (for degree 2^20).\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2114\n\n",
    "created_at": "2008-02-08T15:12:20Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "get gf2x into Sage!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2114",
    "user": "was"
}
```
Assignee: somebody

CC:  zimmerma malb jpflori jdemeyer

Check out http://wwwmaths.anu.edu.au/~brent/gf2x.html

It's:
* by very well respected people
* GPL'd (v2 or later)
* Small pure C code:

```
dhcp46-72:gf2x-0.1 was$ ls
BestToom.c          README              ToomSpace.c         gen_bb_mul_code.c   mul-tc3w.c          mul2t.c             tune1               tuneup.c
COPYING             TC.h                cantor              mul-tc3.c           mul-tc4.c           mulfft-bit.c        tunefft.c
HalfGCD.c           Toom.c              factor.c            mul-tc3u.c          mul.c               patch-wrt-ntl-5.3.1 tunetoom.c
dhcp46-72:gf2x-0.1 was$ usage
4	BestToom.c
4	README
4	TC.h
4	Toom.c
4	ToomSpace.c
4	patch-wrt-ntl-5.3.1
4	tune1
4	tuneup.c
8	gen_bb_mul_code.c
8	mul2t.c
8	tunefft.c
12	mul-tc3.c
12	mul-tc3u.c
12	mul-tc3w.c
12	mul-tc4.c
12	tunetoom.c
16	HalfGCD.c
16	mul.c
20	COPYING
28	mulfft-bit.c
40	factor.c
132	cantor
368	total
```

* and Paul Z. says: 

```
for your information, on http://wwwmaths.anu.edu.au/~brent/gf2x.html you will
find an implementation up to 5 times faster than NTL's GF2X (for degree 2^20).
```


Issue created by migration from https://trac.sagemath.org/ticket/2114





---

archive/issue_comments_013790.json:
```json
{
    "body": "\n```\nEmmanuel Thom\u00e9 to me, Paul, Pierrick\n\t\nshow details 2:53 PM (5 hours ago) [gf2x-20070214.tar.gz]\n\t\n\t\nReply\n\t\n\t\n\tfrom\tEmmanuel Thom\u00e9 <Emmanuel.Thome@normalesup.org>\nto\twstein@gmail.com,\ncc\tPaul Zimmermann <Paul.Zimmermann@loria.fr>,\nPierrick Gaudry <gaudry@lix.polytechnique.fr>,\ndate\tThu, Feb 14, 2008 at 2:53 PM\nsubject\tgf2x package\n\t\nhide details 2:53 PM (5 hours ago) [gf2x-20070214.tar.gz]\n\t\n\t\nReply\n\t\n\t\nOn Thu, Feb 14, 2008 at 06:12:34PM +0100, Paul Zimmermann wrote:\n> http://trac.sagemath.org/sage_trac/ticket/2114\n\nFor your information, you might find the attached version more\npackageable (it can live outside NTL, for instance). Yet, the build\nprocess is still tricky: Auto tuning and so on. Depending on your\npreferred practices for sage, your preferred option could be to\nstatically save the thresholds file per-machine.\n\nRegards,\n\nE.\n```\n\n\nThe \"attached version\" is here:\n   http://sage.math.washington.edu/home/was/tmp/gf2x-20070214.tar.gz",
    "created_at": "2008-02-15T04:42:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13790",
    "user": "was"
}
```


```
Emmanuel Thomé to me, Paul, Pierrick
	
show details 2:53 PM (5 hours ago) [gf2x-20070214.tar.gz]
	
	
Reply
	
	
	from	Emmanuel Thomé <Emmanuel.Thome@normalesup.org>
to	wstein@gmail.com,
cc	Paul Zimmermann <Paul.Zimmermann@loria.fr>,
Pierrick Gaudry <gaudry@lix.polytechnique.fr>,
date	Thu, Feb 14, 2008 at 2:53 PM
subject	gf2x package
	
hide details 2:53 PM (5 hours ago) [gf2x-20070214.tar.gz]
	
	
Reply
	
	
On Thu, Feb 14, 2008 at 06:12:34PM +0100, Paul Zimmermann wrote:
> http://trac.sagemath.org/sage_trac/ticket/2114

For your information, you might find the attached version more
packageable (it can live outside NTL, for instance). Yet, the build
process is still tricky: Auto tuning and so on. Depending on your
preferred practices for sage, your preferred option could be to
statically save the thresholds file per-machine.

Regards,

E.
```


The "attached version" is here:
   http://sage.math.washington.edu/home/was/tmp/gf2x-20070214.tar.gz



---

archive/issue_comments_013791.json:
```json
{
    "body": "A new version (0.3.1) is available from http://wwwmaths.anu.edu.au/~brent/gf2x.html.",
    "created_at": "2008-10-18T11:43:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13791",
    "user": "zimmerma"
}
```

A new version (0.3.1) is available from http://wwwmaths.anu.edu.au/~brent/gf2x.html.



---

archive/issue_comments_013792.json:
```json
{
    "body": "GF2X has now its own development page: http://gf2x.gforge.inria.fr/.\nIt should be easier to incorporate into Sage now, but maybe it would be better\nto include it through NTL, since since NTL 5.5, NTL can be configured to use GF2X as\nauxiliary package. In such a way, Sage will benefit from GF2X for all computations with NTL.",
    "created_at": "2009-11-27T10:13:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13792",
    "user": "zimmerma"
}
```

GF2X has now its own development page: http://gf2x.gforge.inria.fr/.
It should be easier to incorporate into Sage now, but maybe it would be better
to include it through NTL, since since NTL 5.5, NTL can be configured to use GF2X as
auxiliary package. In such a way, Sage will benefit from GF2X for all computations with NTL.



---

archive/issue_comments_013793.json:
```json
{
    "body": "Note that since ntl-5.5, NTL can now be configured to use GF2X instead of its own routines.\nThis is probably the easiest way to get GF2X into Sage.",
    "created_at": "2010-02-25T09:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13793",
    "user": "zimmerma"
}
```

Note that since ntl-5.5, NTL can now be configured to use GF2X instead of its own routines.
This is probably the easiest way to get GF2X into Sage.



---

archive/issue_comments_013794.json:
```json
{
    "body": "Paul, I'm finally packaging this, only planning to build NTL on top of it, no \"native\" interface.\nIs tuning still highly recommended? Because it really takes a long time.\nI was thinking of providing an option (GF2X_TUNE=yes/no, any better idea?) to enable/disable it, not sure what the default should be.\nThe README suggests it would be yes by default.",
    "created_at": "2013-06-04T14:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13794",
    "user": "jpflori"
}
```

Paul, I'm finally packaging this, only planning to build NTL on top of it, no "native" interface.
Is tuning still highly recommended? Because it really takes a long time.
I was thinking of providing an option (GF2X_TUNE=yes/no, any better idea?) to enable/disable it, not sure what the default should be.
The README suggests it would be yes by default.



---

archive/issue_comments_013795.json:
```json
{
    "body": "Changing keywords from \"\" to \"spkg gf2x\".",
    "created_at": "2013-06-04T15:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13795",
    "user": "jpflori"
}
```

Changing keywords from "" to "spkg gf2x".



---

archive/issue_comments_013796.json:
```json
{
    "body": "Upped spkgs, with the GF2X_TUNE option off by default (took one hour on a quite recent Xeon (with only one thread, but I did not test whether tuning gets parallelized)).\nSet it to yes to perform tuning.\n\nI did not check this actually speeds up NTL, anyone wanting to benchmark the new NTL spkg against the old one please go ahead.\n\nAs NTL is a standard spkg, not sure what the way to go is.\nJeroen please decide what to do.",
    "created_at": "2013-06-04T15:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13796",
    "user": "jpflori"
}
```

Upped spkgs, with the GF2X_TUNE option off by default (took one hour on a quite recent Xeon (with only one thread, but I did not test whether tuning gets parallelized)).
Set it to yes to perform tuning.

I did not check this actually speeds up NTL, anyone wanting to benchmark the new NTL spkg against the old one please go ahead.

As NTL is a standard spkg, not sure what the way to go is.
Jeroen please decide what to do.



---

archive/issue_comments_013797.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-06-04T15:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13797",
    "user": "jpflori"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_013798.json:
```json
{
    "body": "Spkg diff, for review only.",
    "created_at": "2013-06-04T15:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13798",
    "user": "jpflori"
}
```

Spkg diff, for review only.



---

archive/issue_comments_013799.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2013-06-04T20:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13799",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_013800.json:
```json
{
    "body": "Attachment [ntl-5.5.2.p1.diff](tarball://root/attachments/some-uuid/ticket2114/ntl-5.5.2.p1.diff) by jdemeyer created at 2013-06-04 20:08:31\n\nReplying to [comment:8 jpflori]:\n> Jeroen please decide what to do.\nWhy should I?  *You* should decide if you want this:\na. as standard package (which requires a discussion on `sage-devel` and changes to `spkg/standard/deps`)\nb. as optional package (but then NTL needs to work both with and without `gf2x`)\nc. not at all",
    "created_at": "2013-06-04T20:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13800",
    "user": "jdemeyer"
}
```

Attachment [ntl-5.5.2.p1.diff](tarball://root/attachments/some-uuid/ticket2114/ntl-5.5.2.p1.diff) by jdemeyer created at 2013-06-04 20:08:31

Replying to [comment:8 jpflori]:
> Jeroen please decide what to do.
Why should I?  *You* should decide if you want this:
a. as standard package (which requires a discussion on `sage-devel` and changes to `spkg/standard/deps`)
b. as optional package (but then NTL needs to work both with and without `gf2x`)
c. not at all



---

archive/issue_comments_013801.json:
```json
{
    "body": "I say we want this as a standard package and would prefer to avoid an optional stage (just imagine we patch ntl inbetween.\nBut I thought we needed optional before standard for all packages, so in this case this would be complicated.\nSo I'll post on sage-devel.",
    "created_at": "2013-06-04T22:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13801",
    "user": "jpflori"
}
```

I say we want this as a standard package and would prefer to avoid an optional stage (just imagine we patch ntl inbetween.
But I thought we needed optional before standard for all packages, so in this case this would be complicated.
So I'll post on sage-devel.



---

archive/issue_comments_013802.json:
```json
{
    "body": "So does it actually speed up things, considering that we disable tuning? If not then forget about it. If yes then I'd be happy to see it included.",
    "created_at": "2013-06-04T23:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13802",
    "user": "vbraun"
}
```

So does it actually speed up things, considering that we disable tuning? If not then forget about it. If yes then I'd be happy to see it included.



---

archive/issue_comments_013803.json:
```json
{
    "body": "Just for hint, my experience playing with FLINT, using gf2x for GF(2) polynomials instead of the basic implementation inside FLINT using long gave an incredible speedup.\nAnd from the maybe 4 years ago comments in the ticket description, it should also seepdup NTL.\nI just don't have the time or the motivation to benchmark products of GF(2**n) elements (once you don't use Givaro) right now to prove it is beneficial.",
    "created_at": "2013-06-04T23:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13803",
    "user": "jpflori"
}
```

Just for hint, my experience playing with FLINT, using gf2x for GF(2) polynomials instead of the basic implementation inside FLINT using long gave an incredible speedup.
And from the maybe 4 years ago comments in the ticket description, it should also seepdup NTL.
I just don't have the time or the motivation to benchmark products of GF(2**n) elements (once you don't use Givaro) right now to prove it is beneficial.



---

archive/issue_comments_013804.json:
```json
{
    "body": "Replying to [comment:7 jpflori]:\n> Paul, I'm finally packaging this, only planning to build NTL on top of it, no \"native\" interface.\n> Is tuning still highly recommended? Because it really takes a long time.\n> I was thinking of providing an option (GF2X_TUNE=yes/no, any better idea?) to enable/disable it, not sure what the default should be.\n> The README suggests it would be yes by default.\n\nJean-Pierre,\n\nmake tune-lowlevel is still highly recommended, since it will choose the best routine up to 9 words.\nIt takes a little more than one minute on my 4-year-old laptop (including recompiling the library).\n\nThen you can do say `make tune-toom TOOM_TUNING_LIMIT=100` to choose the best algorithm up to say\n100 words (i.e., degree < 6400 on a 64-bit computer). It should take a few minutes only.\n\nPaul",
    "created_at": "2013-06-05T08:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13804",
    "user": "zimmerma"
}
```

Replying to [comment:7 jpflori]:
> Paul, I'm finally packaging this, only planning to build NTL on top of it, no "native" interface.
> Is tuning still highly recommended? Because it really takes a long time.
> I was thinking of providing an option (GF2X_TUNE=yes/no, any better idea?) to enable/disable it, not sure what the default should be.
> The README suggests it would be yes by default.

Jean-Pierre,

make tune-lowlevel is still highly recommended, since it will choose the best routine up to 9 words.
It takes a little more than one minute on my 4-year-old laptop (including recompiling the library).

Then you can do say `make tune-toom TOOM_TUNING_LIMIT=100` to choose the best algorithm up to say
100 words (i.e., degree < 6400 on a 64-bit computer). It should take a few minutes only.

Paul



---

archive/issue_comments_013805.json:
```json
{
    "body": "Ok, I'll do that.\nThanks for the suggestion.",
    "created_at": "2013-06-05T09:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13805",
    "user": "jpflori"
}
```

Ok, I'll do that.
Thanks for the suggestion.



---

archive/issue_comments_013806.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2013-06-05T09:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13806",
    "user": "jpflori"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_013807.json:
```json
{
    "body": "Replying to [comment:12 jpflori]:\n> Just for hint, my experience playing with FLINT, using gf2x for GF(2) polynomials instead of the basic implementation inside FLINT using long gave an incredible speedup.\n> And from the maybe 4 years ago comments in the ticket description, it should also seepdup NTL.\n> I just don't have the time or the motivation to benchmark products of GF(2**n) elements (once you don't use Givaro) right now to prove it is beneficial.\nOn my pc, multiplying two random elements of GF(2**10000) goes from 103us in Sage 5.9 with old NTL to 21.4us in 5.10.rc0 with NTL+gf2x.",
    "created_at": "2013-06-05T09:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13807",
    "user": "jpflori"
}
```

Replying to [comment:12 jpflori]:
> Just for hint, my experience playing with FLINT, using gf2x for GF(2) polynomials instead of the basic implementation inside FLINT using long gave an incredible speedup.
> And from the maybe 4 years ago comments in the ticket description, it should also seepdup NTL.
> I just don't have the time or the motivation to benchmark products of GF(2**n) elements (once you don't use Givaro) right now to prove it is beneficial.
On my pc, multiplying two random elements of GF(2**10000) goes from 103us in Sage 5.9 with old NTL to 21.4us in 5.10.rc0 with NTL+gf2x.



---

archive/issue_comments_013808.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-06-05T09:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13808",
    "user": "jpflori"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_013809.json:
```json
{
    "body": "New spkg up and diff updated.\nPleas ignore the broken tuning.diff I posted.",
    "created_at": "2013-06-05T09:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13809",
    "user": "jpflori"
}
```

New spkg up and diff updated.
Pleas ignore the broken tuning.diff I posted.



---

archive/issue_comments_013810.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-05T09:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13810",
    "user": "jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_013811.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-06-05T09:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13811",
    "user": "jpflori"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_013812.json:
```json
{
    "body": "Wrong spelling...",
    "created_at": "2013-06-05T09:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13812",
    "user": "jpflori"
}
```

Wrong spelling...



---

archive/issue_comments_013813.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-05T09:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13813",
    "user": "jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_013814.json:
```json
{
    "body": "Should be ok now.",
    "created_at": "2013-06-05T09:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13814",
    "user": "jpflori"
}
```

Should be ok now.



---

archive/issue_comments_013815.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-06-05T10:35:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13815",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_013816.json:
```json
{
    "body": "This needs a patch to `spkg/standard/deps` and `spkg/install`.",
    "created_at": "2013-06-05T10:35:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13816",
    "user": "jdemeyer"
}
```

This needs a patch to `spkg/standard/deps` and `spkg/install`.



---

archive/issue_comments_013817.json:
```json
{
    "body": "while trying gf2x-1.1 on my laptop, I hit a bug due to the fact that the tuning gave\n`GF2X_MUL_TOOM4_ALWAYS_THRESHOLD=16`, whereas a value at least 30 is required.\nThe following patch will avoid this problem (or detect it earlier). It is against the development version but should be easily adapted to 1.1:\n\n```\n--- toom.c      (revision 148)\n+++ toom.c      (working copy)\n@@ -1,6 +1,6 @@\n /* This file is part of the gf2x library.\n \n-   Copyright 2007, 2008, 2009\n+   Copyright 2007, 2008, 2009, 2013\n    Richard Brent, Pierrick Gaudry, Emmanuel Thome', Paul Zimmermann\n \n    This program is free software; you can redistribute it and/or modify it\n@@ -53,6 +53,9 @@\n     if (n < GF2X_MUL_TOOMW_THRESHOLD)\n        return GF2X_SELECT_KARA;                // KarMul\n \n+#if GF2X_MUL_TOOM4_ALWAYS_THRESHOLD < 30\n+#error \"GF2X_MUL_TOOM4_ALWAYS_THRESHOLD must be >= 30\"\n+#endif\n     if (n >= GF2X_MUL_TOOM4_ALWAYS_THRESHOLD)\n        return GF2X_SELECT_TC4;         // Toom4Mul\n```\n",
    "created_at": "2013-06-05T12:11:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13817",
    "user": "zimmerma"
}
```

while trying gf2x-1.1 on my laptop, I hit a bug due to the fact that the tuning gave
`GF2X_MUL_TOOM4_ALWAYS_THRESHOLD=16`, whereas a value at least 30 is required.
The following patch will avoid this problem (or detect it earlier). It is against the development version but should be easily adapted to 1.1:

```
--- toom.c      (revision 148)
+++ toom.c      (working copy)
@@ -1,6 +1,6 @@
 /* This file is part of the gf2x library.
 
-   Copyright 2007, 2008, 2009
+   Copyright 2007, 2008, 2009, 2013
    Richard Brent, Pierrick Gaudry, Emmanuel Thome', Paul Zimmermann
 
    This program is free software; you can redistribute it and/or modify it
@@ -53,6 +53,9 @@
     if (n < GF2X_MUL_TOOMW_THRESHOLD)
        return GF2X_SELECT_KARA;                // KarMul
 
+#if GF2X_MUL_TOOM4_ALWAYS_THRESHOLD < 30
+#error "GF2X_MUL_TOOM4_ALWAYS_THRESHOLD must be >= 30"
+#endif
     if (n >= GF2X_MUL_TOOM4_ALWAYS_THRESHOLD)
        return GF2X_SELECT_TC4;         // Toom4Mul
```




---

archive/issue_comments_013818.json:
```json
{
    "body": "oh, I understand what happened now. I did `make tune-toom TOOM_TUNING_LIMIT=16` which sets automatically `GF2X_MUL_TOOM4_ALWAYS_THRESHOLD` to 16. When running `make tune-toom TOOM_TUNING_LIMIT=nnn`, one should always have nnn at least 30.\n\nPaul",
    "created_at": "2013-06-05T12:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13818",
    "user": "zimmerma"
}
```

oh, I understand what happened now. I did `make tune-toom TOOM_TUNING_LIMIT=16` which sets automatically `GF2X_MUL_TOOM4_ALWAYS_THRESHOLD` to 16. When running `make tune-toom TOOM_TUNING_LIMIT=nnn`, one should always have nnn at least 30.

Paul



---

archive/issue_comments_013819.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-05T12:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13819",
    "user": "jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_013820.json:
```json
{
    "body": "I've used 100 as a limit so it should be ok.",
    "created_at": "2013-06-05T12:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13820",
    "user": "jpflori"
}
```

I've used 100 as a limit so it should be ok.



---

archive/issue_comments_013821.json:
```json
{
    "body": "Waaaaah!  Just created (or rather finished) an NTL 5.5.2.p1 spkg (fixing hardcoded `make`) at #14692... 8-/",
    "created_at": "2013-06-05T21:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13821",
    "user": "leif"
}
```

Waaaaah!  Just created (or rather finished) an NTL 5.5.2.p1 spkg (fixing hardcoded `make`) at #14692... 8-/



---

archive/issue_comments_013822.json:
```json
{
    "body": "Replying to [comment:25 leif]:\n> Waaaaah!  Just created (or rather finished) an NTL 5.5.2.p1 spkg (fixing hardcoded `make`) at #14692... 8-/\n\nOk, I've rebased *your* `.p1` on mine:\n\nhttp://boxen.math.washington.edu/home/leif/Sage/spkgs/ntl-5.5.2.p2.spkg\n\n\n```diff\ndiff --git a/.hgtags b/.hgtags\n--- a/.hgtags\n+++ b/.hgtags\n@@ -1,3 +1,4 @@\n 73d22601a79e226c590bb93cc842391e9e8f8d11 ntl-5.5.2\n 5cf2d2f43b4d9cf1fc3cf8e9bb54efc58ccf2b4f ntl-5.5.2.p0\n c7af41e56a64bdef778ee579beda9d54943105fe ntl-5.5.2.p1\n+4984ca9298a7310c9378ca8cd391dc8a1ba85d9f ntl-5.5.2.p2\ndiff --git a/SPKG.txt b/SPKG.txt\n--- a/SPKG.txt\n+++ b/SPKG.txt\n@@ -18,6 +18,7 @@\n \n == Dependencies ==\n  * gmp\n+ * gf2x\n \n == Special Update/Build Instructions ==\n  * We need to modfiy new.h to accomodate Singular\n@@ -34,6 +35,9 @@\n \n == Changelog ==\n \n+=== ntl-5.5.2.p2 (Jean-Pierre Flori, June 5th 2013) ===\n+ * #2114: Build NTL with gf2x support.\n+\n === ntl-5.5.2.p1 (Leif Leonhardy, June 5th 2013) ===\n  * #14692: Patch upstream to use `$(MAKE)` (instead of `make`) in the generated\n    Makefile (and in two scripts called from the Makefile which in turn invoke\ndiff --git a/spkg-install b/spkg-install\n--- a/spkg-install\n+++ b/spkg-install\n@@ -86,7 +86,7 @@\n         CC=\"$CC\" CFLAGS=\"$CFLAGS $SHAREDFLAGS\" \\\n         CXX=\"$CXX\" CXXFLAGS=\"$CXXFLAGS $SHAREDFLAGS\" \\\n         LDFLAGS=\"$LDFLAGS\" LIBTOOL_LINK_FLAGS=\"$LIBTOOL_LINK_FLAGS\" \\\n-        NTL_GMP_LIP=on NTL_STD_CXX=on \\\n+        NTL_GMP_LIP=on NTL_GF2X_LIB=on NTL_STD_CXX=on \\\n         LIBTOOL=../../libtool/libtool\n \n     if [ $? -ne 0 ]; then\n```\n",
    "created_at": "2013-06-05T21:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13822",
    "user": "leif"
}
```

Replying to [comment:25 leif]:
> Waaaaah!  Just created (or rather finished) an NTL 5.5.2.p1 spkg (fixing hardcoded `make`) at #14692... 8-/

Ok, I've rebased *your* `.p1` on mine:

http://boxen.math.washington.edu/home/leif/Sage/spkgs/ntl-5.5.2.p2.spkg


```diff
diff --git a/.hgtags b/.hgtags
--- a/.hgtags
+++ b/.hgtags
@@ -1,3 +1,4 @@
 73d22601a79e226c590bb93cc842391e9e8f8d11 ntl-5.5.2
 5cf2d2f43b4d9cf1fc3cf8e9bb54efc58ccf2b4f ntl-5.5.2.p0
 c7af41e56a64bdef778ee579beda9d54943105fe ntl-5.5.2.p1
+4984ca9298a7310c9378ca8cd391dc8a1ba85d9f ntl-5.5.2.p2
diff --git a/SPKG.txt b/SPKG.txt
--- a/SPKG.txt
+++ b/SPKG.txt
@@ -18,6 +18,7 @@
 
 == Dependencies ==
  * gmp
+ * gf2x
 
 == Special Update/Build Instructions ==
  * We need to modfiy new.h to accomodate Singular
@@ -34,6 +35,9 @@
 
 == Changelog ==
 
+=== ntl-5.5.2.p2 (Jean-Pierre Flori, June 5th 2013) ===
+ * #2114: Build NTL with gf2x support.
+
 === ntl-5.5.2.p1 (Leif Leonhardy, June 5th 2013) ===
  * #14692: Patch upstream to use `$(MAKE)` (instead of `make`) in the generated
    Makefile (and in two scripts called from the Makefile which in turn invoke
diff --git a/spkg-install b/spkg-install
--- a/spkg-install
+++ b/spkg-install
@@ -86,7 +86,7 @@
         CC="$CC" CFLAGS="$CFLAGS $SHAREDFLAGS" \
         CXX="$CXX" CXXFLAGS="$CXXFLAGS $SHAREDFLAGS" \
         LDFLAGS="$LDFLAGS" LIBTOOL_LINK_FLAGS="$LIBTOOL_LINK_FLAGS" \
-        NTL_GMP_LIP=on NTL_STD_CXX=on \
+        NTL_GMP_LIP=on NTL_GF2X_LIB=on NTL_STD_CXX=on \
         LIBTOOL=../../libtool/libtool
 
     if [ $? -ne 0 ]; then
```




---

archive/issue_comments_013823.json:
```json
{
    "body": "W.r.t. gf2x:\n\nThe following doesn't work (`-O0` never takes effect):\n\n```sh\n\nif [ \"$SAGE64\" = \"yes\" ]; then\n    echo \"Building a 64-bit version of gf2x.\"\n    ABI=\"64\"; export ABI\n    CFLAGS=\"-O2 -g -m64 $CFLAGS\"; export CFLAGS\nelse\n    CFLAGS=\"-O2 -g $CFLAGS\"; export CFLAGS\nfi\n\nif [ \"$SAGE_DEBUG\" = \"yes\" ]; then\n    echo \"Building a debug version of gf2x.\"\n    CFLAGS=\"-O0 -g $CFLAGS\"; export CFLAGS\nfi\n```\n\n\n`$SAGE_LOCAL` should be quoted in the `rm` commands in `spkg-install`.",
    "created_at": "2013-06-05T22:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13823",
    "user": "leif"
}
```

W.r.t. gf2x:

The following doesn't work (`-O0` never takes effect):

```sh

if [ "$SAGE64" = "yes" ]; then
    echo "Building a 64-bit version of gf2x."
    ABI="64"; export ABI
    CFLAGS="-O2 -g -m64 $CFLAGS"; export CFLAGS
else
    CFLAGS="-O2 -g $CFLAGS"; export CFLAGS
fi

if [ "$SAGE_DEBUG" = "yes" ]; then
    echo "Building a debug version of gf2x."
    CFLAGS="-O0 -g $CFLAGS"; export CFLAGS
fi
```


`$SAGE_LOCAL` should be quoted in the `rm` commands in `spkg-install`.



---

archive/issue_comments_013824.json:
```json
{
    "body": "Minor thing:  \"Patching gf2x.\" gets printed even when no patch gets applied.",
    "created_at": "2013-06-05T22:05:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13824",
    "user": "leif"
}
```

Minor thing:  "Patching gf2x." gets printed even when no patch gets applied.



---

archive/issue_comments_013825.json:
```json
{
    "body": "P.S.:  For other spkgs, we (currently) use `SAGE_TUNE_<package name>[={yes,no}]` (where `<package name>` can be both upper or lower case).  And the new variable should probably get documented in `devel/sage/doc/en/installation/source.rst` (section \"Environment variables\").\n\n`GF2X_TUNE=full` really takes ages, and uses **a lot** of memory (so far up to 2 GB resident / 2.5 GB virtual).",
    "created_at": "2013-06-06T01:06:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13825",
    "user": "leif"
}
```

P.S.:  For other spkgs, we (currently) use `SAGE_TUNE_<package name>[={yes,no}]` (where `<package name>` can be both upper or lower case).  And the new variable should probably get documented in `devel/sage/doc/en/installation/source.rst` (section "Environment variables").

`GF2X_TUNE=full` really takes ages, and uses **a lot** of memory (so far up to 2 GB resident / 2.5 GB virtual).



---

archive/issue_comments_013826.json:
```json
{
    "body": "\n```\ngf2x.c: In function 'gf2x_mul_pool_init':\ngf2x.c:82:24: warning: argument to 'sizeof' in 'memset' call is the same expression as the destination; did you mean to dereference it? [-Wsizeof-pointer-memaccess]\n     memset(p, 0, sizeof(p));\n                        ^\n```\n\n\n? :-)",
    "created_at": "2013-06-06T04:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13826",
    "user": "leif"
}
```


```
gf2x.c: In function 'gf2x_mul_pool_init':
gf2x.c:82:24: warning: argument to 'sizeof' in 'memset' call is the same expression as the destination; did you mean to dereference it? [-Wsizeof-pointer-memaccess]
     memset(p, 0, sizeof(p));
                        ^
```


? :-)



---

archive/issue_comments_013827.json:
```json
{
    "body": "Replying to [comment:31 leif]:\n> {{{\n> gf2x.c: In function 'gf2x_mul_pool_init':\n> gf2x.c:82:24: warning: argument to 'sizeof' in 'memset' call is the same expression as the destination; did you mean to dereference it? [-Wsizeof-pointer-memaccess]\n>      memset(p, 0, sizeof(p));\n>                         ^\n> }}}\n\nHarmless, but warning could be avoided by using `sizeof(gf2x_mul_pool_t)` or `sizeof(p[0])` instead in\n\n```c\nvoid gf2x_mul_pool_init(gf2x_mul_pool_t p)\n{\n    memset(p, 0, sizeof(p));\n}\n```\n",
    "created_at": "2013-06-06T04:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13827",
    "user": "leif"
}
```

Replying to [comment:31 leif]:
> {{{
> gf2x.c: In function 'gf2x_mul_pool_init':
> gf2x.c:82:24: warning: argument to 'sizeof' in 'memset' call is the same expression as the destination; did you mean to dereference it? [-Wsizeof-pointer-memaccess]
>      memset(p, 0, sizeof(p));
>                         ^
> }}}

Harmless, but warning could be avoided by using `sizeof(gf2x_mul_pool_t)` or `sizeof(p[0])` instead in

```c
void gf2x_mul_pool_init(gf2x_mul_pool_t p)
{
    memset(p, 0, sizeof(p));
}
```




---

archive/issue_comments_013828.json:
```json
{
    "body": "Otherwise (i.e., modulo mentioned issues) looks ok (and apparently works; Linux x86 and x86_64, GCC 4.4.3 / 4.7.2 / 4.8.0, with `SAGE_CHECK=yes`, *some* doctests run).\n\n\n\n\nBuilding with `GF2X_TUNE=full` finally took more than four and a half hours, admittedly on a not-so-fast (but otherwise almost idle, dual-core) machine...",
    "created_at": "2013-06-06T04:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13828",
    "user": "leif"
}
```

Otherwise (i.e., modulo mentioned issues) looks ok (and apparently works; Linux x86 and x86_64, GCC 4.4.3 / 4.7.2 / 4.8.0, with `SAGE_CHECK=yes`, *some* doctests run).




Building with `GF2X_TUNE=full` finally took more than four and a half hours, admittedly on a not-so-fast (but otherwise almost idle, dual-core) machine...



---

archive/issue_comments_013829.json:
```json
{
    "body": "I've fixed the warning reported in comment [comment:31] upstream, thanks.\n\nPaul",
    "created_at": "2013-06-06T06:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13829",
    "user": "zimmerma"
}
```

I've fixed the warning reported in comment [comment:31] upstream, thanks.

Paul



---

archive/issue_comments_013830.json:
```json
{
    "body": "Thanks leif, I'll take all these sensible remarks into account.",
    "created_at": "2013-06-06T09:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13830",
    "user": "jpflori"
}
```

Thanks leif, I'll take all these sensible remarks into account.



---

archive/issue_comments_013831.json:
```json
{
    "body": "Also `$SAGE_ROOT/COPYING.txt` should be updated (keeping in mind #12447).",
    "created_at": "2013-06-06T09:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13831",
    "user": "jdemeyer"
}
```

Also `$SAGE_ROOT/COPYING.txt` should be updated (keeping in mind #12447).



---

archive/issue_comments_013832.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-06-06T09:20:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13832",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_013833.json:
```json
{
    "body": "I've not found doc for the other tune variables in the doc, so I'll postpone adding the doc until we've listed all that has to be documented.\n\nI'm aware that we always print the patching message, it saves a few lines of script...",
    "created_at": "2013-06-06T09:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13833",
    "user": "jpflori"
}
```

I've not found doc for the other tune variables in the doc, so I'll postpone adding the doc until we've listed all that has to be documented.

I'm aware that we always print the patching message, it saves a few lines of script...



---

archive/issue_comments_013834.json:
```json
{
    "body": "Attachment [trac_2114-gf2x.patch](tarball://root/attachments/some-uuid/ticket2114/trac_2114-gf2x.patch) by jpflori created at 2013-06-06 09:52:26",
    "created_at": "2013-06-06T09:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13834",
    "user": "jpflori"
}
```

Attachment [trac_2114-gf2x.patch](tarball://root/attachments/some-uuid/ticket2114/trac_2114-gf2x.patch) by jpflori created at 2013-06-06 09:52:26



---

archive/issue_comments_013835.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-06T09:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13835",
    "user": "jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_013836.json:
```json
{
    "body": "If you prefer, I can include Paul's patch so that we will actually be patching gf2x.",
    "created_at": "2013-06-06T09:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13836",
    "user": "jpflori"
}
```

If you prefer, I can include Paul's patch so that we will actually be patching gf2x.



---

archive/issue_comments_013837.json:
```json
{
    "body": "my patch (from comment [comment:22]) is not needed if you do `tune-toom TOOM_TUNING_LIMIT=nnn` with nnn at least 30.\n\nPaul",
    "created_at": "2013-06-06T09:58:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13837",
    "user": "zimmerma"
}
```

my patch (from comment [comment:22]) is not needed if you do `tune-toom TOOM_TUNING_LIMIT=nnn` with nnn at least 30.

Paul



---

archive/issue_comments_013838.json:
```json
{
    "body": "I meant leif's patch in fact, the one from comment http://trac.sagemath.org/sage_trac/ticket/2114#comment:32 suppressing a warning.",
    "created_at": "2013-06-06T10:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13838",
    "user": "jpflori"
}
```

I meant leif's patch in fact, the one from comment http://trac.sagemath.org/sage_trac/ticket/2114#comment:32 suppressing a warning.



---

archive/issue_comments_013839.json:
```json
{
    "body": "ok, here is the change I did upstream:\n\n```\n--- gf2x.c\t(revision 150)\n+++ gf2x.c\t(working copy)\n@@ -79,7 +79,7 @@\n \n void gf2x_mul_pool_init(gf2x_mul_pool_t p)\n {\n-    memset(p, 0, sizeof(p));\n+    memset(p, 0, sizeof(gf2x_mul_pool_t));\n }\n \n void gf2x_mul_pool_clear(gf2x_mul_pool_t p)\n```\n\nPaul",
    "created_at": "2013-06-06T10:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13839",
    "user": "zimmerma"
}
```

ok, here is the change I did upstream:

```
--- gf2x.c	(revision 150)
+++ gf2x.c	(working copy)
@@ -79,7 +79,7 @@
 
 void gf2x_mul_pool_init(gf2x_mul_pool_t p)
 {
-    memset(p, 0, sizeof(p));
+    memset(p, 0, sizeof(gf2x_mul_pool_t));
 }
 
 void gf2x_mul_pool_clear(gf2x_mul_pool_t p)
```

Paul



---

archive/issue_comments_013840.json:
```json
{
    "body": "Thanks Paul.\nIf leif rants, I'll include it.\n\nBut IMHO we can wait for the gf2x 1.2 release to get this warning suppressed.\nI think that getting gf2x in Sage quickly is a more important matter.",
    "created_at": "2013-06-06T10:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13840",
    "user": "jpflori"
}
```

Thanks Paul.
If leif rants, I'll include it.

But IMHO we can wait for the gf2x 1.2 release to get this warning suppressed.
I think that getting gf2x in Sage quickly is a more important matter.



---

archive/issue_comments_013841.json:
```json
{
    "body": "Replying to [comment:45 jpflori]:\n> Thanks Paul.\n> If leif rants, I'll include it.\n\nThe \"rant\" addressed upstream, and (as expected) reached it... ;-)\n\nI don't care whether you include a patch here.",
    "created_at": "2013-06-06T14:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13841",
    "user": "leif"
}
```

Replying to [comment:45 jpflori]:
> Thanks Paul.
> If leif rants, I'll include it.

The "rant" addressed upstream, and (as expected) reached it... ;-)

I don't care whether you include a patch here.



---

archive/issue_comments_013842.json:
```json
{
    "body": "P.S.:  There are other warnings where the return value of `fgets()` (IIRC) gets discarded / ignored, in tuning-related code.  (But in those cases it's IMHO more obvious to the user that the warnings can safely be ignored.)",
    "created_at": "2013-06-06T14:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13842",
    "user": "leif"
}
```

P.S.:  There are other warnings where the return value of `fgets()` (IIRC) gets discarded / ignored, in tuning-related code.  (But in those cases it's IMHO more obvious to the user that the warnings can safely be ignored.)



---

archive/issue_comments_013843.json:
```json
{
    "body": "Replying to [comment:39 jpflori]:\n> I've not found doc for the other tune variables in the doc, so I'll postpone adding the doc until we've listed all that has to be documented.\n\nHmmm...  If you at least create a meta-ticket to record what has to be documented...\n\n\n\n\n> I'm aware that we always print the patching message, it saves a few lines of script...\n\nI'm using either `ls ../patches/*.patch >/dev/null 2>&1 && ...`, or simply *\"Applying patches to upstream (if any) ...\"*",
    "created_at": "2013-06-06T14:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13843",
    "user": "leif"
}
```

Replying to [comment:39 jpflori]:
> I've not found doc for the other tune variables in the doc, so I'll postpone adding the doc until we've listed all that has to be documented.

Hmmm...  If you at least create a meta-ticket to record what has to be documented...




> I'm aware that we always print the patching message, it saves a few lines of script...

I'm using either `ls ../patches/*.patch >/dev/null 2>&1 && ...`, or simply *"Applying patches to upstream (if any) ..."*



---

archive/issue_comments_013844.json:
```json
{
    "body": "Btw., `ptestlong` passed with Sage 5.10.rc0 on Linux x86_64.",
    "created_at": "2013-06-06T14:57:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13844",
    "user": "leif"
}
```

Btw., `ptestlong` passed with Sage 5.10.rc0 on Linux x86_64.



---

archive/issue_comments_013845.json:
```json
{
    "body": "Replying to [comment:48 leif]:\n> Replying to [comment:39 jpflori]:\n> > I've not found doc for the other tune variables in the doc, so I'll postpone adding the doc until we've listed all that has to be documented.\n> \n> Hmmm...  If you at least create a meta-ticket to record what has to be documented...\nDone, see #14698 (you're cc'ed there anyway).\n> \n> \n\n> \n> > I'm aware that we always print the patching message, it saves a few lines of script...\n> \n> I'm using either `ls ../patches/*.patch >/dev/null 2>&1 && ...`, or simply *\"Applying patches to upstream (if any) ...\"*\nOk, it's true it's simple enough, I'll change that.",
    "created_at": "2013-06-06T15:02:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13845",
    "user": "jpflori"
}
```

Replying to [comment:48 leif]:
> Replying to [comment:39 jpflori]:
> > I've not found doc for the other tune variables in the doc, so I'll postpone adding the doc until we've listed all that has to be documented.
> 
> Hmmm...  If you at least create a meta-ticket to record what has to be documented...
Done, see #14698 (you're cc'ed there anyway).
> 
> 

> 
> > I'm aware that we always print the patching message, it saves a few lines of script...
> 
> I'm using either `ls ../patches/*.patch >/dev/null 2>&1 && ...`, or simply *"Applying patches to upstream (if any) ..."*
Ok, it's true it's simple enough, I'll change that.



---

archive/issue_comments_013846.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-06-06T15:02:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13846",
    "user": "jpflori"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_013847.json:
```json
{
    "body": "Done.\n\nNow the NTL spkg should be rebased when #14692 is done.",
    "created_at": "2013-06-06T15:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13847",
    "user": "jpflori"
}
```

Done.

Now the NTL spkg should be rebased when #14692 is done.



---

archive/issue_comments_013848.json:
```json
{
    "body": "Or the converse.",
    "created_at": "2013-06-06T15:11:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13848",
    "user": "jpflori"
}
```

Or the converse.



---

archive/issue_comments_013849.json:
```json
{
    "body": "As #14692 needs more work, let's base it on top of this ticket rather than the other way around.",
    "created_at": "2013-06-06T15:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13849",
    "user": "jpflori"
}
```

As #14692 needs more work, let's base it on top of this ticket rather than the other way around.



---

archive/issue_comments_013850.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-06T15:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13850",
    "user": "jpflori"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_013851.json:
```json
{
    "body": "Replying to [comment:47 leif]:\n> P.S.:  There are other warnings where the return value of `fgets()` (IIRC) gets discarded / ignored, in tuning-related code.  (But in those cases it's IMHO more obvious to the user that the warnings can safely be ignored.) \n\nLeif, thanks, I've fixed a few upstream. It is always nice to get feedback when a package is used in Sage!\n\nPaul",
    "created_at": "2013-06-06T17:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13851",
    "user": "zimmerma"
}
```

Replying to [comment:47 leif]:
> P.S.:  There are other warnings where the return value of `fgets()` (IIRC) gets discarded / ignored, in tuning-related code.  (But in those cases it's IMHO more obvious to the user that the warnings can safely be ignored.) 

Leif, thanks, I've fixed a few upstream. It is always nice to get feedback when a package is used in Sage!

Paul



---

archive/issue_comments_013852.json:
```json
{
    "body": "I made a few small changes to `gf2x` to make `spkg-install` more like most other standard packages. I also re-downloaded the upstream source, as timestamps got messed up somehow.",
    "created_at": "2013-06-08T11:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13852",
    "user": "jdemeyer"
}
```

I made a few small changes to `gf2x` to make `spkg-install` more like most other standard packages. I also re-downloaded the upstream source, as timestamps got messed up somehow.



---

archive/issue_comments_013853.json:
```json
{
    "body": "For NTL, I added the `hg tag`.",
    "created_at": "2013-06-08T11:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13853",
    "user": "jdemeyer"
}
```

For NTL, I added the `hg tag`.



---

archive/issue_comments_013854.json:
```json
{
    "body": "Changing component from basic arithmetic to packages: standard.",
    "created_at": "2013-06-08T11:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13854",
    "user": "jdemeyer"
}
```

Changing component from basic arithmetic to packages: standard.



---

archive/issue_comments_013855.json:
```json
{
    "body": "Replying to [comment:57 jdemeyer]:\n> I made a few small changes to `gf2x` to make `spkg-install` more like most other standard packages. I also re-downloaded the upstream source, as timestamps got messed up somehow.\n\nYou didn't fix \"gf2x is a C/C+ software package\" though... ;-)\n\nCould you attach a diff of **your** changes?\n\nI don't want to re-review everything.  Retesting is odd enough.",
    "created_at": "2013-06-08T11:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13855",
    "user": "leif"
}
```

Replying to [comment:57 jdemeyer]:
> I made a few small changes to `gf2x` to make `spkg-install` more like most other standard packages. I also re-downloaded the upstream source, as timestamps got messed up somehow.

You didn't fix "gf2x is a C/C+ software package" though... ;-)

Could you attach a diff of **your** changes?

I don't want to re-review everything.  Retesting is odd enough.



---

archive/issue_comments_013856.json:
```json
{
    "body": "Spkg diff, for review only.",
    "created_at": "2013-06-08T11:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13856",
    "user": "jdemeyer"
}
```

Spkg diff, for review only.



---

archive/issue_comments_013857.json:
```json
{
    "body": "Attachment [gf2x-1.1.diff](tarball://root/attachments/some-uuid/ticket2114/gf2x-1.1.diff) by jdemeyer created at 2013-06-08 11:28:40",
    "created_at": "2013-06-08T11:28:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13857",
    "user": "jdemeyer"
}
```

Attachment [gf2x-1.1.diff](tarball://root/attachments/some-uuid/ticket2114/gf2x-1.1.diff) by jdemeyer created at 2013-06-08 11:28:40



---

archive/issue_comments_013858.json:
```json
{
    "body": "Attachment [gf2x-1.1-jdemeyer.diff](tarball://root/attachments/some-uuid/ticket2114/gf2x-1.1-jdemeyer.diff) by jdemeyer created at 2013-06-08 11:29:22\n\nReplying to [comment:61 leif]:\n> You didn't fix \"gf2x is a C/C+ software package\" though... ;-)\nFixed now.\n\n> Could you attach a diff of **your** changes?\n[attachment:gf2x-1.1-jdemeyer.diff]",
    "created_at": "2013-06-08T11:29:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13858",
    "user": "jdemeyer"
}
```

Attachment [gf2x-1.1-jdemeyer.diff](tarball://root/attachments/some-uuid/ticket2114/gf2x-1.1-jdemeyer.diff) by jdemeyer created at 2013-06-08 11:29:22

Replying to [comment:61 leif]:
> You didn't fix "gf2x is a C/C+ software package" though... ;-)
Fixed now.

> Could you attach a diff of **your** changes?
[attachment:gf2x-1.1-jdemeyer.diff]



---

archive/issue_comments_013859.json:
```json
{
    "body": "Replying to [comment:62 jdemeyer]:\n> Replying to [comment:61 leif]:\n> > You didn't fix \"gf2x is a C/C+ software package\" though... ;-)\n> Fixed now.\n> \n> > Could you attach a diff of **your** changes?\n> [attachment:gf2x-1.1-jdemeyer.diff]\n\nI would have dropped the \"C++\"; if gf2x was (partially) implemented in C++, we'd have to set / change `CXXFLAGS` as well.\n\nI'd probably also use `$CFLAG64` instead of hardcoding `-m64`.",
    "created_at": "2013-06-08T12:04:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13859",
    "user": "leif"
}
```

Replying to [comment:62 jdemeyer]:
> Replying to [comment:61 leif]:
> > You didn't fix "gf2x is a C/C+ software package" though... ;-)
> Fixed now.
> 
> > Could you attach a diff of **your** changes?
> [attachment:gf2x-1.1-jdemeyer.diff]

I would have dropped the "C++"; if gf2x was (partially) implemented in C++, we'd have to set / change `CXXFLAGS` as well.

I'd probably also use `$CFLAG64` instead of hardcoding `-m64`.



---

archive/issue_comments_013860.json:
```json
{
    "body": "Did I mention it also builds with `clang`? ;-)",
    "created_at": "2013-06-08T12:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13860",
    "user": "leif"
}
```

Did I mention it also builds with `clang`? ;-)



---

archive/issue_comments_013861.json:
```json
{
    "body": "Replying to [comment:63 leif]:\n> I would have dropped the \"C++\"\nThe text was taken verbatim from [upstream](http://gf2x.gforge.inria.fr/).",
    "created_at": "2013-06-08T12:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13861",
    "user": "jdemeyer"
}
```

Replying to [comment:63 leif]:
> I would have dropped the "C++"
The text was taken verbatim from [upstream](http://gf2x.gforge.inria.fr/).



---

archive/issue_comments_013862.json:
```json
{
    "body": "Replying to [comment:65 jdemeyer]:\n> Replying to [comment:63 leif]:\n> > I would have dropped the \"C++\"\n> The text was taken verbatim from [upstream](http://gf2x.gforge.inria.fr/).\n\nI think it's covered by the GPL as well.",
    "created_at": "2013-06-08T12:13:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13862",
    "user": "leif"
}
```

Replying to [comment:65 jdemeyer]:
> Replying to [comment:63 leif]:
> > I would have dropped the "C++"
> The text was taken verbatim from [upstream](http://gf2x.gforge.inria.fr/).

I think it's covered by the GPL as well.



---

archive/issue_comments_013863.json:
```json
{
    "body": "the C++ part of gf2x is only in the \"apps\" subdirectory, which contains binaries to be linked with NTL\n(we had to use C++ here since NTL is under C++) to check for primitive trinomials. I guess Sage does not use that part, thus indeed only C code is used within Sage.\n\nPaul",
    "created_at": "2013-06-08T12:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13863",
    "user": "zimmerma"
}
```

the C++ part of gf2x is only in the "apps" subdirectory, which contains binaries to be linked with NTL
(we had to use C++ here since NTL is under C++) to check for primitive trinomials. I guess Sage does not use that part, thus indeed only C code is used within Sage.

Paul



---

archive/issue_comments_013864.json:
```json
{
    "body": "Replying to [comment:67 zimmerma]:\n> the C++ part of gf2x is only in the \"apps\" subdirectory, which contains binaries to be linked with NTL\n> (we had to use C++ here since NTL is under C++) to check for primitive trinomials.\n> \n\n> \n> I guess Sage does not use that part, thus indeed only C code is used within Sage.\n\nWe can't build those apps (at least not immediately), since we decided to let NTL depend on gf2x.",
    "created_at": "2013-06-08T13:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13864",
    "user": "leif"
}
```

Replying to [comment:67 zimmerma]:
> the C++ part of gf2x is only in the "apps" subdirectory, which contains binaries to be linked with NTL
> (we had to use C++ here since NTL is under C++) to check for primitive trinomials.
> 

> 
> I guess Sage does not use that part, thus indeed only C code is used within Sage.

We can't build those apps (at least not immediately), since we decided to let NTL depend on gf2x.



---

archive/issue_comments_013865.json:
```json
{
    "body": "Positive review to everything except my changes ([attachment:gf2x-1.1-jdemeyer.diff]).",
    "created_at": "2013-06-08T18:53:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13865",
    "user": "jdemeyer"
}
```

Positive review to everything except my changes ([attachment:gf2x-1.1-jdemeyer.diff]).



---

archive/issue_comments_013866.json:
```json
{
    "body": "I'm ok with them.",
    "created_at": "2013-06-08T18:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13866",
    "user": "jpflori"
}
```

I'm ok with them.



---

archive/issue_comments_013867.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-08T18:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13867",
    "user": "jpflori"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_013868.json:
```json
{
    "body": "FWIW, I was going to give the previous spkgs positive review right when Jeroen started to change both, so I don't insist on fixing the hardcoded `-m64`.",
    "created_at": "2013-06-08T19:02:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13868",
    "user": "leif"
}
```

FWIW, I was going to give the previous spkgs positive review right when Jeroen started to change both, so I don't insist on fixing the hardcoded `-m64`.



---

archive/issue_comments_013869.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-06-10T08:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2114",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2114#issuecomment-13869",
    "user": "jdemeyer"
}
```

Resolution: fixed
