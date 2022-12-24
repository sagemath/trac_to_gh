# Issue 9836: New PARI and new MPIR don't combine

archive/issues_009836.json:
```json
{
    "body": "Assignee: tbd\n\nCombining #9343 (new PARI) and #8664 (MPIR 2.1.1) gives Segmentation Faults.  This problem is not limited to Sage, it is either a bug in PARI or in MPIR.\n\nTest gp script: [http://sage.math.washington.edu/home/jdemeyer/pari-mpir-bug.gp](http://sage.math.washington.edu/home/jdemeyer/pari-mpir-bug.gp)\n\nSee also [http://wiki.sagemath.org/NewPARI](http://wiki.sagemath.org/NewPARI)\n\nIssue created by migration from https://trac.sagemath.org/ticket/9837\n\n",
    "created_at": "2010-08-29T14:00:49Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "New PARI and new MPIR don't combine",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9836",
    "user": "@jdemeyer"
}
```
Assignee: tbd

Combining #9343 (new PARI) and #8664 (MPIR 2.1.1) gives Segmentation Faults.  This problem is not limited to Sage, it is either a bug in PARI or in MPIR.

Test gp script: [http://sage.math.washington.edu/home/jdemeyer/pari-mpir-bug.gp](http://sage.math.washington.edu/home/jdemeyer/pari-mpir-bug.gp)

See also [http://wiki.sagemath.org/NewPARI](http://wiki.sagemath.org/NewPARI)

Issue created by migration from https://trac.sagemath.org/ticket/9837





---

archive/issue_comments_097065.json:
```json
{
    "body": "This line from the PARI source code (src/kernel/gmp/mp.c:952) says it all:\n\n\n```\n#if 1 /* use undocumented GMP interface */\n```\n\n\nChanging that to a zero solves the problem.",
    "created_at": "2010-08-29T14:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9836#issuecomment-97065",
    "user": "@jdemeyer"
}
```

This line from the PARI source code (src/kernel/gmp/mp.c:952) says it all:


```
#if 1 /* use undocumented GMP interface */
```


Changing that to a zero solves the problem.



---

archive/issue_comments_097066.json:
```json
{
    "body": "Replying to [comment:1 jdemeyer]:\n> This line from the PARI source code (src/kernel/gmp/mp.c:952) says it all:\n> \n\n```\n#if 1 /* use undocumented GMP interface */\n```\n\n> \n> Changing that to a zero solves the problem.\n\n:D Thanks, I didn't want to track this down further...\n\nFunny, because *GMP* (5.0.1) dropped other things not part of the *public* interface, which are still available in the newest MPIR.",
    "created_at": "2010-08-29T14:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9836#issuecomment-97066",
    "user": "@nexttime"
}
```

Replying to [comment:1 jdemeyer]:
> This line from the PARI source code (src/kernel/gmp/mp.c:952) says it all:
> 

```
#if 1 /* use undocumented GMP interface */
```

> 
> Changing that to a zero solves the problem.

:D Thanks, I didn't want to track this down further...

Funny, because *GMP* (5.0.1) dropped other things not part of the *public* interface, which are still available in the newest MPIR.



---

archive/issue_comments_097067.json:
```json
{
    "body": "P.S.: Yet another major single-character patch... ;-)",
    "created_at": "2010-08-29T14:22:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9836#issuecomment-97067",
    "user": "@nexttime"
}
```

P.S.: Yet another major single-character patch... ;-)



---

archive/issue_comments_097068.json:
```json
{
    "body": "Should we patch it to\n\n```\n#ifdef PARI_USE_GMP_INTERNALS\n```\n\nrather than\n\n```\n#if 0\n```\n\n?",
    "created_at": "2010-08-29T14:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9836#issuecomment-97068",
    "user": "@nexttime"
}
```

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

archive/issue_comments_097069.json:
```json
{
    "body": "It's actually an MPIR issue, I will report it to the MPIR people.  The following MPIR program gives a Segmentation Fault:\n\n\n```\n#include <mpir.h>\nint main()\n{\n    mpz_t Z, R;\n    mpz_init(Z);\n    mpz_init(R);\n    mpz_ui_pow_ui(Z, 10, 100000);\n    mpz_divexact(R, Z, Z);\n    return 0;\n}\n```\n",
    "created_at": "2010-08-29T15:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9836#issuecomment-97069",
    "user": "@jdemeyer"
}
```

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

archive/issue_comments_097070.json:
```json
{
    "body": "Cross-replying to [comment:ticket:9343:359 jdemeyer]:\n> Replying to [comment:ticket:9343:357 leif]:\n> >  * preparing a PARI 2.4.3.svn-12577.p5 spkg, with the fixes from #9722, and in addition disabling the use of GMP internals by PARI by default (with an *option* to make PARI use them)\n> \n> I'm assuming you refer to the \"GMP internals\" mentioned in #9837?\n\nYes. I intended to simply change the `#if 1` to `#ifdef PARI_USE_GMP_INTERNALS` in `mp.c`, which we already patch. (I've in fact already prepared and tested a `.svn-12577.p4.5` spkg with exactly that change; all long tests passed.)\n\nThen in case somebody wanted to enable PARI's use of \"whatever\" (see below), he could simply add `-DPARI_USE_GMP_INTERNALS` to `CFLAGS`, or we could do that if some (other) environment variable is set [to `yes`].\n\n> Note that these are actually **documented** GMP internals, so it's not as bad as it sounds.\n\nI haven't checked this. To me, it is rather irrelevant if they are *documented* or not, but rather whether they are part of the official / **public** interface to GMP. If those features PARI uses aren't, we should IMHO disable their use *by default*. So correct me if my assumption is false; I'll perhaps later take a closer look at what PARI considers \"undocumented\" (but not at the moment...). The odd thing is that the `#else` branch currently contains `TODO`s (though it seems functional at least for the purpose of Sage).\n\n> So I would prefer not to touch that code and leave PARI using documented GMP/MPIR internals as it is.\n\nSince we already patch `mp.c`, I think it doesn't hurt to add the above change to it.\n\nWe can then easily enable or disable the use in `spkg-install` and/or by setting environment variables, which may be valuable for testing, without changing the spkg at all.\n\nThe remaining question would be whether to *enable* or *disable* it by default. With *MPIR* the Sage standard package, I preferred the latter. \n\n> Also, on the who-is-doing-what part: I am not doing anything with this for the moment (I do plan to release a prealpha4 when leif's done with p5).\n\nI don't know if *\"with this\"* referred to the PARI *spkg*, the ticket (#9343), or PARI in general... ;-)\n\nI'll again ask at #9343 if anyone plans to add doctests or at least missing docstrings (to the Sage library part of PARI / #9343). I am not..., only perhaps going to fix the Sphinx warnings.",
    "created_at": "2010-08-31T01:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9836#issuecomment-97070",
    "user": "@nexttime"
}
```

Cross-replying to [comment:ticket:9343:359 jdemeyer]:
> Replying to [comment:ticket:9343:357 leif]:
> >  * preparing a PARI 2.4.3.svn-12577.p5 spkg, with the fixes from #9722, and in addition disabling the use of GMP internals by PARI by default (with an *option* to make PARI use them)
> 
> I'm assuming you refer to the "GMP internals" mentioned in #9837?

Yes. I intended to simply change the `#if 1` to `#ifdef PARI_USE_GMP_INTERNALS` in `mp.c`, which we already patch. (I've in fact already prepared and tested a `.svn-12577.p4.5` spkg with exactly that change; all long tests passed.)

Then in case somebody wanted to enable PARI's use of "whatever" (see below), he could simply add `-DPARI_USE_GMP_INTERNALS` to `CFLAGS`, or we could do that if some (other) environment variable is set [to `yes`].

> Note that these are actually **documented** GMP internals, so it's not as bad as it sounds.

I haven't checked this. To me, it is rather irrelevant if they are *documented* or not, but rather whether they are part of the official / **public** interface to GMP. If those features PARI uses aren't, we should IMHO disable their use *by default*. So correct me if my assumption is false; I'll perhaps later take a closer look at what PARI considers "undocumented" (but not at the moment...). The odd thing is that the `#else` branch currently contains `TODO`s (though it seems functional at least for the purpose of Sage).

> So I would prefer not to touch that code and leave PARI using documented GMP/MPIR internals as it is.

Since we already patch `mp.c`, I think it doesn't hurt to add the above change to it.

We can then easily enable or disable the use in `spkg-install` and/or by setting environment variables, which may be valuable for testing, without changing the spkg at all.

The remaining question would be whether to *enable* or *disable* it by default. With *MPIR* the Sage standard package, I preferred the latter. 

> Also, on the who-is-doing-what part: I am not doing anything with this for the moment (I do plan to release a prealpha4 when leif's done with p5).

I don't know if *"with this"* referred to the PARI *spkg*, the ticket (#9343), or PARI in general... ;-)

I'll again ask at #9343 if anyone plans to add doctests or at least missing docstrings (to the Sage library part of PARI / #9343). I am not..., only perhaps going to fix the Sphinx warnings.



---

archive/issue_comments_097071.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n> I'll again ask at #9343 if anyone plans to add doctests or at least missing docstrings (to the Sage library part of PARI / #9343). I am not..., only perhaps going to fix the Sphinx warnings.\n\nI believe the Sphinx warnings come from #9400 and I will fix these when I have time.",
    "created_at": "2010-08-31T06:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9836#issuecomment-97071",
    "user": "@jdemeyer"
}
```

Replying to [comment:8 leif]:
> I'll again ask at #9343 if anyone plans to add doctests or at least missing docstrings (to the Sage library part of PARI / #9343). I am not..., only perhaps going to fix the Sphinx warnings.

I believe the Sphinx warnings come from #9400 and I will fix these when I have time.



---

archive/issue_comments_097072.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n> I haven't checked this. To me, it is rather irrelevant if they are *documented* or not, but rather whether they are part of the official / **public** interface to GMP.\n\nThis is how the MPIR documentation phrases the internals used by PARI:\n> **This chapter is provided only for informational purposes and the various internals described**\n> **here may change in future MPIR releases. Applications expecting to be compatible with future**\n> **releases should use only the documented interfaces described in previous chapters.**\n\n> Since we already patch `mp.c`, I think it doesn't hurt to add the above change to it.\nWell, it depends because in this case, using the internals means a potentially significant speed gain.\n\n> > Also, on the who-is-doing-what part: I am not doing anything with this for the moment (I do plan to release a prealpha4 when leif's done with p5).\n> \n> I don't know if *\"with this\"* referred to the PARI *spkg*, the ticket (#9343), or PARI in general... ;-)\nThe only thing I'll do is release a new prealpha when PARI p5 is out and to fix the few remaining issues in #9400.",
    "created_at": "2010-08-31T06:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9836#issuecomment-97072",
    "user": "@jdemeyer"
}
```

Replying to [comment:8 leif]:
> I haven't checked this. To me, it is rather irrelevant if they are *documented* or not, but rather whether they are part of the official / **public** interface to GMP.

This is how the MPIR documentation phrases the internals used by PARI:
> **This chapter is provided only for informational purposes and the various internals described**
> **here may change in future MPIR releases. Applications expecting to be compatible with future**
> **releases should use only the documented interfaces described in previous chapters.**

> Since we already patch `mp.c`, I think it doesn't hurt to add the above change to it.
Well, it depends because in this case, using the internals means a potentially significant speed gain.

> > Also, on the who-is-doing-what part: I am not doing anything with this for the moment (I do plan to release a prealpha4 when leif's done with p5).
> 
> I don't know if *"with this"* referred to the PARI *spkg*, the ticket (#9343), or PARI in general... ;-)
The only thing I'll do is release a new prealpha when PARI p5 is out and to fix the few remaining issues in #9400.



---

archive/issue_comments_097073.json:
```json
{
    "body": "This got filed as \"reported upstream, little or no feedback\". How did it get reported originally, because I only received the report yesterday, and since then there are five or six replies on the MPIR devel list.\n\nAnyhow, just to update, it looks like we found the bug in MPIR. Just have to patch it now.\n\nWith regard to the \"undocumented interface\", if Pari currently builds against MPIR without missing symbol errors, then it is likely that it is relying on now documented symbols in both GMP and MPIR. The disclaimer is out-of-date. It has been removed in the GMP manual, but we have forgotten to remove it in the MPIR manual. I will make a note on the MPIR devel list to do so.\n\nIf there are missing symbol errors, then I guess it relied on undocumented functions in *GMP* but not in MPIR. That would be a different (but surprising) situation.",
    "created_at": "2010-09-04T13:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9836#issuecomment-97073",
    "user": "wbhart"
}
```

This got filed as "reported upstream, little or no feedback". How did it get reported originally, because I only received the report yesterday, and since then there are five or six replies on the MPIR devel list.

Anyhow, just to update, it looks like we found the bug in MPIR. Just have to patch it now.

With regard to the "undocumented interface", if Pari currently builds against MPIR without missing symbol errors, then it is likely that it is relying on now documented symbols in both GMP and MPIR. The disclaimer is out-of-date. It has been removed in the GMP manual, but we have forgotten to remove it in the MPIR manual. I will make a note on the MPIR devel list to do so.

If there are missing symbol errors, then I guess it relied on undocumented functions in *GMP* but not in MPIR. That would be a different (but surprising) situation.



---

archive/issue_comments_097074.json:
```json
{
    "body": "Just to save someone writing a response, this was originally reported to thempirteam email address, which because of technical problems was not being accessed. So, it was reported in the correct way, 6 days ago, and there would have indeed been little to no response over that time due to hardware issues. Sorry for the noise.",
    "created_at": "2010-09-04T15:22:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9836#issuecomment-97074",
    "user": "wbhart"
}
```

Just to save someone writing a response, this was originally reported to thempirteam email address, which because of technical problems was not being accessed. So, it was reported in the correct way, 6 days ago, and there would have indeed been little to no response over that time due to hardware issues. Sorry for the noise.



---

archive/issue_comments_097075.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-05T12:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9836#issuecomment-97075",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097076.json:
```json
{
    "body": "What does \"needs review\" mean? Confirming that PARI uses **documented** GMP features? Or that it's an *MPIR* bug?\n\nI'd say we (i.e. the release manager) can close this ticket as \"fixed\". #8664 should not be merged until there's MPIR 2.1.2 or alike with this bug fixed; I think we agreed on that.",
    "created_at": "2010-09-05T16:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9836#issuecomment-97076",
    "user": "@nexttime"
}
```

What does "needs review" mean? Confirming that PARI uses **documented** GMP features? Or that it's an *MPIR* bug?

I'd say we (i.e. the release manager) can close this ticket as "fixed". #8664 should not be merged until there's MPIR 2.1.2 or alike with this bug fixed; I think we agreed on that.



---

archive/issue_comments_097077.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-05T16:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9836#issuecomment-97077",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097078.json:
```json
{
    "body": "Positive review for the fact that it is an MPIR bug which has been fixed upstream.",
    "created_at": "2010-09-05T16:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9836#issuecomment-97078",
    "user": "@jdemeyer"
}
```

Positive review for the fact that it is an MPIR bug which has been fixed upstream.



---

archive/issue_comments_097079.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T11:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9836#issuecomment-97079",
    "user": "@qed777"
}
```

Resolution: fixed



---

archive/issue_comments_097080.json:
```json
{
    "body": "Feel free to edit the \"Author(s)\" and \"Reviewer(s)\" fields.",
    "created_at": "2010-09-15T11:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9836",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9836#issuecomment-97080",
    "user": "@qed777"
}
```

Feel free to edit the "Author(s)" and "Reviewer(s)" fields.
