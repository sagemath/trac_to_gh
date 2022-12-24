# Issue 5731: Update NTL to 5.5 release (latest upstream)

archive/issues_005731.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  cremona\n\n2009.04.08: Changes between NTL 5.4.2 and 5.5 from http://www.shoup.net/ntl/doc/tour-changes.html\n\n* Added the ability to generate a shared library (with help from Tim Abbott). Details.\n* Fixed some standardization issues (with help from Tim Abbot): default location of installed documentation files now conforms to standards; use of EOF now conforms to standards.\nAdded a callback mechanism to NTL's error reporting function. See ErrorCallback in tools.txt.\n* Added support for the gf2x library for speeding up arithmetic in GF2X (with help from Emmanuel Thom\u00e9).\n  * In conjuction with the above, I also changed the GF2X so that it works better with very large polynomials: large blocks of memory are released, recursive HalfGCD algorithms are used for large polynomials.\n* Fixed a bug in void TraceMod(zz_p& x, const zz_pX& a, const zz_pXModulus& F) (reported by Luca De Feo).\n* Fixed a performance issue in various versions of SetCoeff (reported by Luca De Feo).\n* Fixed the declaration of mat_zz_p transpose(const mat_zz_p& a) (reported by Benoit Lacelle).\n\nSo we should be able to drop a couple custom patches.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5731\n\n",
    "created_at": "2009-04-10T08:11:36Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "Update NTL to 5.5 release (latest upstream)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5731",
    "user": "mabshoff"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/5731





---

archive/issue_comments_044774.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-10T08:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44774",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_044775.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-09-03T21:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44775",
    "user": "leif"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_044776.json:
```json
{
    "body": "Changing keywords from \"\" to \"upgrade\".",
    "created_at": "2010-09-03T21:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44776",
    "user": "leif"
}
```

Changing keywords from "" to "upgrade".



---

archive/issue_comments_044777.json:
```json
{
    "body": "Remove assignee mabshoff.",
    "created_at": "2010-09-03T21:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44777",
    "user": "leif"
}
```

Remove assignee mabshoff.



---

archive/issue_comments_044778.json:
```json
{
    "body": "Attachment [ntl-5.5.2.p1.spkg](tarball://root/attachments/some-uuid/ticket5731/ntl-5.5.2.p1.spkg) by mraum created at 2011-03-21 23:30:25\n\nThis works for me with all long tests.",
    "created_at": "2011-03-21T23:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44778",
    "user": "mraum"
}
```

Attachment [ntl-5.5.2.p1.spkg](tarball://root/attachments/some-uuid/ticket5731/ntl-5.5.2.p1.spkg) by mraum created at 2011-03-21 23:30:25

This works for me with all long tests.



---

archive/issue_comments_044779.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-03-21T23:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44779",
    "user": "mraum"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_044780.json:
```json
{
    "body": "two things. \n* trac is not a place to attach spkg. \n* why is it .p1? It should just be ntl-5.5.2.spkg\n\nOther than that I have no doubts that it works out of the box personally, and you save me from creating a spkg.",
    "created_at": "2011-03-22T01:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44780",
    "user": "fbissey"
}
```

two things. 
* trac is not a place to attach spkg. 
* why is it .p1? It should just be ntl-5.5.2.spkg

Other than that I have no doubts that it works out of the box personally, and you save me from creating a spkg.



---

archive/issue_comments_044781.json:
```json
{
    "body": "Installed fine for me on top of 4.7.alpha1, and all tests passed.  (ubuntu linux 64-bit).\n\nNote that since several other spkgs use NTL (for example, eclib), someone should check that they all build ok.  One way to do this would be to put the spkg into the next alpha and let the automatic testing system see what happens.",
    "created_at": "2011-03-22T23:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44781",
    "user": "cremona"
}
```

Installed fine for me on top of 4.7.alpha1, and all tests passed.  (ubuntu linux 64-bit).

Note that since several other spkgs use NTL (for example, eclib), someone should check that they all build ok.  One way to do this would be to put the spkg into the next alpha and let the automatic testing system see what happens.



---

archive/issue_comments_044782.json:
```json
{
    "body": "I have been using ntl-5.5.2 in sage-on-gentoo since\n\n```\n     Mon Nov  9 10:55:35 2009 >>> dev-libs/ntl-5.5.2\n       merge time: 10 minutes and 27 seconds.                                                                                       \n```\n\nthe following depend on ntl:\n* flint\n* singular\n* linbox\n* eclib\n* sage (through c_lib and several extensions so sage -ba is required)\n\nI have rebuild/updated all of those since 2009 so I don't expect any shocking results.",
    "created_at": "2011-03-23T00:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44782",
    "user": "fbissey"
}
```

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

archive/issue_comments_044783.json:
```json
{
    "body": "I am putting this for 4.7.1. Hopefully I'll find the time to give a proper review.",
    "created_at": "2011-05-02T00:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44783",
    "user": "fbissey"
}
```

I am putting this for 4.7.1. Hopefully I'll find the time to give a proper review.



---

archive/issue_comments_044784.json:
```json
{
    "body": "OK I had a closer look at the spkg. First of SPKG.txt hasn't been updated, the hg repo looks ok so I suppose you only changed the content of the src directory. This need a bit of work. I may elect to do the finishing bits if I have time this week.",
    "created_at": "2011-05-31T23:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44784",
    "user": "fbissey"
}
```

OK I had a closer look at the spkg. First of SPKG.txt hasn't been updated, the hg repo looks ok so I suppose you only changed the content of the src directory. This need a bit of work. I may elect to do the finishing bits if I have time this week.



---

archive/issue_comments_044785.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-05-31T23:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44785",
    "user": "fbissey"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_044786.json:
```json
{
    "body": "So I have looked more closely. You updated the patches and everything but didn't update the info in SPKG.txt. What I will do is update SPKG.txt with your details make a nice ntl-5.5.2.spkg and post it on google-code and I will put myself and John Cremona as reviewer.\n\nOnce that's done can you have a quick check and put it to positive review John?",
    "created_at": "2011-06-01T03:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44786",
    "user": "fbissey"
}
```

So I have looked more closely. You updated the patches and everything but didn't update the info in SPKG.txt. What I will do is update SPKG.txt with your details make a nice ntl-5.5.2.spkg and post it on google-code and I will put myself and John Cremona as reviewer.

Once that's done can you have a quick check and put it to positive review John?



---

archive/issue_comments_044787.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-06-01T04:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44787",
    "user": "fbissey"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_044788.json:
```json
{
    "body": "New spkg upload on google-code, link in updated description. Let's get a final sign off on this.",
    "created_at": "2011-06-01T04:01:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44788",
    "user": "fbissey"
}
```

New spkg upload on google-code, link in updated description. Let's get a final sign off on this.



---

archive/issue_comments_044789.json:
```json
{
    "body": "I am checking this now.\n\nJohn",
    "created_at": "2011-06-01T11:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44789",
    "user": "cremona"
}
```

I am checking this now.

John



---

archive/issue_comments_044790.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-01T12:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44790",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_044791.json:
```json
{
    "body": "Replying to [comment:14 cremona]:\n> I am checking this now.\n> \n> John\n\nI started with a fresh build of 4.7.1.alpha0 which passes all tests;  built the new spkg here (with SAGE_CHECK=yes\"); did \"sage -ba\" followed by \"sage -t -long\", and all tests pass.\n\nThe spkg itself is ok (though there's a typo \"numbery\" in the README, and William should probably not be the only spkg maintainer listed), so I am giving this a positive review and hop that it can go into the next alpha form 4.7.1.",
    "created_at": "2011-06-01T12:12:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44791",
    "user": "cremona"
}
```

Replying to [comment:14 cremona]:
> I am checking this now.
> 
> John

I started with a fresh build of 4.7.1.alpha0 which passes all tests;  built the new spkg here (with SAGE_CHECK=yes"); did "sage -ba" followed by "sage -t -long", and all tests pass.

The spkg itself is ok (though there's a typo "numbery" in the README, and William should probably not be the only spkg maintainer listed), so I am giving this a positive review and hop that it can go into the next alpha form 4.7.1.



---

archive/issue_comments_044792.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-06-10T08:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5731",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5731#issuecomment-44792",
    "user": "jdemeyer"
}
```

Resolution: fixed
