# Issue 9476: Upgrade eclib to version 20100711

archive/issues_009476.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @williamstein @categorie\n\nKeywords: eclib modular symbols\n\nI have made several enhancements to eclib:\n\n1. Support for minus space modular symbols\n2. Some sparse linear algebra improvements\n\nThe new version is called eclib-20100711 since it is more than just a patch-level change.  New spkgs will be linked here shortly.\n\nThe interface in sage/libs/cremona has been updated accordingly in the patch (to appear shortly);  this depends on #9441\n\nIssue created by migration from https://trac.sagemath.org/ticket/9476\n\n",
    "created_at": "2010-07-11T20:36:54Z",
    "labels": [
        "component: packages: standard",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "Upgrade eclib to version 20100711",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9476",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: tbd

CC:  @williamstein @categorie

Keywords: eclib modular symbols

I have made several enhancements to eclib:

1. Support for minus space modular symbols
2. Some sparse linear algebra improvements

The new version is called eclib-20100711 since it is more than just a patch-level change.  New spkgs will be linked here shortly.

The interface in sage/libs/cremona has been updated accordingly in the patch (to appear shortly);  this depends on #9441

Issue created by migration from https://trac.sagemath.org/ticket/9476





---

archive/issue_comments_090807.json:
```json
{
    "body": "The new spkg is here: http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20100711.spkg",
    "created_at": "2010-07-11T21:23:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90807",
    "user": "https://github.com/JohnCremona"
}
```

The new spkg is here: http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20100711.spkg



---

archive/issue_comments_090808.json:
```json
{
    "body": "Attachment [trac_9476-eclib.patch](tarball://root/attachments/some-uuid/ticket9476/trac_9476-eclib.patch) by @JohnCremona created at 2010-07-11 21:25:10\n\nApplies after eclib-20100711.patch and trac_9441-atkin-lehner.patch",
    "created_at": "2010-07-11T21:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90808",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_9476-eclib.patch](tarball://root/attachments/some-uuid/ticket9476/trac_9476-eclib.patch) by @JohnCremona created at 2010-07-11 21:25:10

Applies after eclib-20100711.patch and trac_9441-atkin-lehner.patch



---

archive/issue_comments_090809.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-11T21:26:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90809",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090810.json:
```json
{
    "body": "I'm reviewing this and #9441 at the same time. So far it compiles just fine with sage-4.5 final, on Intel OS X 10.6.4, and I'm currently running tests. I'll also give it a try on geom.math, which has begun at the moment.",
    "created_at": "2010-07-17T10:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90810",
    "user": "https://github.com/rlmill"
}
```

I'm reviewing this and #9441 at the same time. So far it compiles just fine with sage-4.5 final, on Intel OS X 10.6.4, and I'm currently running tests. I'll also give it a try on geom.math, which has begun at the moment.



---

archive/issue_comments_090811.json:
```json
{
    "body": "Looks good on OS X. Same on geom.math.",
    "created_at": "2010-07-17T12:59:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90811",
    "user": "https://github.com/rlmill"
}
```

Looks good on OS X. Same on geom.math.



---

archive/issue_comments_090812.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-17T12:59:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90812",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090813.json:
```json
{
    "body": "Small reviewer patch coming up in a minute!",
    "created_at": "2010-07-17T13:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90813",
    "user": "https://github.com/rlmill"
}
```

Small reviewer patch coming up in a minute!



---

archive/issue_comments_090814.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-17T13:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90814",
    "user": "https://github.com/rlmill"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_090815.json:
```json
{
    "body": "Thanks!",
    "created_at": "2010-07-17T13:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90815",
    "user": "https://github.com/JohnCremona"
}
```

Thanks!



---

archive/issue_comments_090816.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-07-17T13:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90816",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_090817.json:
```json
{
    "body": "Hmm. I think this might have something to do with one of the things I saw on #9247.\n\nI'm attaching the reviewer patch, which causes the following:\n\n```\nsage -t  \"devel/sage-main/sage/schemes/elliptic_curves/ell_modular_symbols.py\"\n**********************************************************************\nFile \"/Users/rlmill/sage-4.5.eclib-test/devel/sage-main/sage/schemes/elliptic_curves/ell_modular_symbols.py\", line 429:\n    sage: M=sage.schemes.elliptic_curves.ell_modular_symbols.ModularSymbolECLIB(E,-1)\nExpected nothing\nGot:\n    Warning : Could not normalize the modular symbols, maybe all further results will be multiplied by -1, 2 or -2.\n**********************************************************************\nFile \"/Users/rlmill/sage-4.5.eclib-test/devel/sage-main/sage/schemes/elliptic_curves/ell_modular_symbols.py\", line 438:\n    sage: M=sage.schemes.elliptic_curves.ell_modular_symbols.ModularSymbolECLIB(E,-1)\nExpected nothing\nGot:\n    Warning : Could not normalize the modular symbols, maybe all further results will be multiplied by -1, 2 or -2.\n**********************************************************************\n```\n\nJohn,\n\nCan you give some info about what's going on here?",
    "created_at": "2010-07-17T13:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90817",
    "user": "https://github.com/rlmill"
}
```

Hmm. I think this might have something to do with one of the things I saw on #9247.

I'm attaching the reviewer patch, which causes the following:

```
sage -t  "devel/sage-main/sage/schemes/elliptic_curves/ell_modular_symbols.py"
**********************************************************************
File "/Users/rlmill/sage-4.5.eclib-test/devel/sage-main/sage/schemes/elliptic_curves/ell_modular_symbols.py", line 429:
    sage: M=sage.schemes.elliptic_curves.ell_modular_symbols.ModularSymbolECLIB(E,-1)
Expected nothing
Got:
    Warning : Could not normalize the modular symbols, maybe all further results will be multiplied by -1, 2 or -2.
**********************************************************************
File "/Users/rlmill/sage-4.5.eclib-test/devel/sage-main/sage/schemes/elliptic_curves/ell_modular_symbols.py", line 438:
    sage: M=sage.schemes.elliptic_curves.ell_modular_symbols.ModularSymbolECLIB(E,-1)
Expected nothing
Got:
    Warning : Could not normalize the modular symbols, maybe all further results will be multiplied by -1, 2 or -2.
**********************************************************************
```

John,

Can you give some info about what's going on here?



---

archive/issue_comments_090818.json:
```json
{
    "body": "I have added Chris W to the CC list since we'll need his input, as he wrote ell_modular_symbols.\n\nI agree that that file needs updating as a consequence of my upgrade;  but that can be done on a separate ticket?",
    "created_at": "2010-07-17T14:23:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90818",
    "user": "https://github.com/JohnCremona"
}
```

I have added Chris W to the CC list since we'll need his input, as he wrote ell_modular_symbols.

I agree that that file needs updating as a consequence of my upgrade;  but that can be done on a separate ticket?



---

archive/issue_comments_090819.json:
```json
{
    "body": "John,\n\nI thought that eclib was propagating that warning, but clearly it's coming from ell_modular_symbols.py. Have a look at the new ref patch, and let me know what you think.",
    "created_at": "2010-07-17T14:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90819",
    "user": "https://github.com/rlmill"
}
```

John,

I thought that eclib was propagating that warning, but clearly it's coming from ell_modular_symbols.py. Have a look at the new ref patch, and let me know what you think.



---

archive/issue_comments_090820.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-07-17T14:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90820",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_090821.json:
```json
{
    "body": "Attachment [trac_9476-remove-not-implemented-error.patch](tarball://root/attachments/some-uuid/ticket9476/trac_9476-remove-not-implemented-error.patch) by @rlmill created at 2010-07-17 14:31:49",
    "created_at": "2010-07-17T14:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90821",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_9476-remove-not-implemented-error.patch](tarball://root/attachments/some-uuid/ticket9476/trac_9476-remove-not-implemented-error.patch) by @rlmill created at 2010-07-17 14:31:49



---

archive/issue_comments_090822.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-21T13:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90822",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090823.json:
```json
{
    "body": "reviewer addendum looks good to me.",
    "created_at": "2010-07-21T13:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90823",
    "user": "https://github.com/williamstein"
}
```

reviewer addendum looks good to me.



---

archive/issue_comments_090824.json:
```json
{
    "body": "I'm having difficulty getting the new package:\n\n```\n$ wget http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20100711.spkg\n--19:50:47--  http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20100711.spkg\n           => `eclib-20100711.spkg'\nResolving www.warwick.ac.uk... 137.205.243.107\nConnecting to www.warwick.ac.uk|137.205.243.107|:80... connected.\nHTTP request sent, awaiting response... \n```\n\nCan someone check its availability and perhaps put a copy on the Sage cluster?\n\nAlso, should I apply both patches, too?",
    "created_at": "2010-08-07T02:54:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90824",
    "user": "https://github.com/qed777"
}
```

I'm having difficulty getting the new package:

```
$ wget http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20100711.spkg
--19:50:47--  http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20100711.spkg
           => `eclib-20100711.spkg'
Resolving www.warwick.ac.uk... 137.205.243.107
Connecting to www.warwick.ac.uk|137.205.243.107|:80... connected.
HTTP request sent, awaiting response... 
```

Can someone check its availability and perhaps put a copy on the Sage cluster?

Also, should I apply both patches, too?



---

archive/issue_comments_090825.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2010-08-07T02:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90825",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_090826.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-08-08T04:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90826",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_090827.json:
```json
{
    "body": "The package is available now.  I'll include both patches.",
    "created_at": "2010-08-08T04:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90827",
    "user": "https://github.com/qed777"
}
```

The package is available now.  I'll include both patches.



---

archive/issue_comments_090828.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-08T04:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90828",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_023489.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-09T09:49:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9476#event-23489"
}
```



---

archive/issue_comments_090829.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:49:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90829",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_090830.json:
```json
{
    "body": "Sorry not to have responded earlier but I was on holiday for a few days.  I think they were doing some network updating at U of Warwick, which could  explain why you could not get the file.  Glad it's fixed -- and thanks for the review.",
    "created_at": "2010-08-11T15:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90830",
    "user": "https://github.com/JohnCremona"
}
```

Sorry not to have responded earlier but I was on holiday for a few days.  I think they were doing some network updating at U of Warwick, which could  explain why you could not get the file.  Glad it's fixed -- and thanks for the review.
