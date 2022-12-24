# Issue 9476: Upgrade eclib to version 20100711

archive/issues_009476.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @williamstein @categorie\n\nKeywords: eclib modular symbols\n\nI have made several enhancements to eclib:\n\n1. Support for minus space modular symbols\n2. Some sparse linear algebra improvements\n\nThe new version is called eclib-20100711 since it is more than just a patch-level change.  New spkgs will be linked here shortly.\n\nThe interface in sage/libs/cremona has been updated accordingly in the patch (to appear shortly);  this depends on #9441\n\nIssue created by migration from https://trac.sagemath.org/ticket/9476\n\n",
    "created_at": "2010-07-11T20:36:54Z",
    "labels": [
        "packages: standard",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "Upgrade eclib to version 20100711",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9476",
    "user": "@JohnCremona"
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

archive/issue_comments_090959.json:
```json
{
    "body": "The new spkg is here: http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20100711.spkg",
    "created_at": "2010-07-11T21:23:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90959",
    "user": "@JohnCremona"
}
```

The new spkg is here: http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20100711.spkg



---

archive/issue_comments_090960.json:
```json
{
    "body": "Attachment [trac_9476-eclib.patch](tarball://root/attachments/some-uuid/ticket9476/trac_9476-eclib.patch) by @JohnCremona created at 2010-07-11 21:25:10\n\nApplies after eclib-20100711.patch and trac_9441-atkin-lehner.patch",
    "created_at": "2010-07-11T21:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90960",
    "user": "@JohnCremona"
}
```

Attachment [trac_9476-eclib.patch](tarball://root/attachments/some-uuid/ticket9476/trac_9476-eclib.patch) by @JohnCremona created at 2010-07-11 21:25:10

Applies after eclib-20100711.patch and trac_9441-atkin-lehner.patch



---

archive/issue_comments_090961.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-11T21:26:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90961",
    "user": "@JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090962.json:
```json
{
    "body": "I'm reviewing this and #9441 at the same time. So far it compiles just fine with sage-4.5 final, on Intel OS X 10.6.4, and I'm currently running tests. I'll also give it a try on geom.math, which has begun at the moment.",
    "created_at": "2010-07-17T10:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90962",
    "user": "@rlmill"
}
```

I'm reviewing this and #9441 at the same time. So far it compiles just fine with sage-4.5 final, on Intel OS X 10.6.4, and I'm currently running tests. I'll also give it a try on geom.math, which has begun at the moment.



---

archive/issue_comments_090963.json:
```json
{
    "body": "Looks good on OS X. Same on geom.math.",
    "created_at": "2010-07-17T12:59:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90963",
    "user": "@rlmill"
}
```

Looks good on OS X. Same on geom.math.



---

archive/issue_comments_090964.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-17T12:59:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90964",
    "user": "@rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090965.json:
```json
{
    "body": "Small reviewer patch coming up in a minute!",
    "created_at": "2010-07-17T13:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90965",
    "user": "@rlmill"
}
```

Small reviewer patch coming up in a minute!



---

archive/issue_comments_090966.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-17T13:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90966",
    "user": "@rlmill"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_090967.json:
```json
{
    "body": "Thanks!",
    "created_at": "2010-07-17T13:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90967",
    "user": "@JohnCremona"
}
```

Thanks!



---

archive/issue_comments_090968.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-07-17T13:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90968",
    "user": "@rlmill"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_090969.json:
```json
{
    "body": "Hmm. I think this might have something to do with one of the things I saw on #9247.\n\nI'm attaching the reviewer patch, which causes the following:\n\n\n```\nsage -t  \"devel/sage-main/sage/schemes/elliptic_curves/ell_modular_symbols.py\"\n**********************************************************************\nFile \"/Users/rlmill/sage-4.5.eclib-test/devel/sage-main/sage/schemes/elliptic_curves/ell_modular_symbols.py\", line 429:\n    sage: M=sage.schemes.elliptic_curves.ell_modular_symbols.ModularSymbolECLIB(E,-1)\nExpected nothing\nGot:\n    Warning : Could not normalize the modular symbols, maybe all further results will be multiplied by -1, 2 or -2.\n**********************************************************************\nFile \"/Users/rlmill/sage-4.5.eclib-test/devel/sage-main/sage/schemes/elliptic_curves/ell_modular_symbols.py\", line 438:\n    sage: M=sage.schemes.elliptic_curves.ell_modular_symbols.ModularSymbolECLIB(E,-1)\nExpected nothing\nGot:\n    Warning : Could not normalize the modular symbols, maybe all further results will be multiplied by -1, 2 or -2.\n**********************************************************************\n```\n\n\nJohn,\n\nCan you give some info about what's going on here?",
    "created_at": "2010-07-17T13:28:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90969",
    "user": "@rlmill"
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

archive/issue_comments_090970.json:
```json
{
    "body": "I have added Chris W to the CC list since we'll need his input, as he wrote ell_modular_symbols.\n\nI agree that that file needs updating as a consequence of my upgrade;  but that can be done on a separate ticket?",
    "created_at": "2010-07-17T14:23:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90970",
    "user": "@JohnCremona"
}
```

I have added Chris W to the CC list since we'll need his input, as he wrote ell_modular_symbols.

I agree that that file needs updating as a consequence of my upgrade;  but that can be done on a separate ticket?



---

archive/issue_comments_090971.json:
```json
{
    "body": "John,\n\nI thought that eclib was propagating that warning, but clearly it's coming from ell_modular_symbols.py. Have a look at the new ref patch, and let me know what you think.",
    "created_at": "2010-07-17T14:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90971",
    "user": "@rlmill"
}
```

John,

I thought that eclib was propagating that warning, but clearly it's coming from ell_modular_symbols.py. Have a look at the new ref patch, and let me know what you think.



---

archive/issue_comments_090972.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-07-17T14:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90972",
    "user": "@rlmill"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_090973.json:
```json
{
    "body": "Attachment [trac_9476-remove-not-implemented-error.patch](tarball://root/attachments/some-uuid/ticket9476/trac_9476-remove-not-implemented-error.patch) by @rlmill created at 2010-07-17 14:31:49",
    "created_at": "2010-07-17T14:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90973",
    "user": "@rlmill"
}
```

Attachment [trac_9476-remove-not-implemented-error.patch](tarball://root/attachments/some-uuid/ticket9476/trac_9476-remove-not-implemented-error.patch) by @rlmill created at 2010-07-17 14:31:49



---

archive/issue_comments_090974.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-21T13:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90974",
    "user": "@williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090975.json:
```json
{
    "body": "reviewer addendum looks good to me.",
    "created_at": "2010-07-21T13:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90975",
    "user": "@williamstein"
}
```

reviewer addendum looks good to me.



---

archive/issue_comments_090976.json:
```json
{
    "body": "I'm having difficulty getting the new package:\n\n```\n$ wget http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20100711.spkg\n--19:50:47--  http://www.warwick.ac.uk/staff/J.E.Cremona/eclib-20100711.spkg\n           => `eclib-20100711.spkg'\nResolving www.warwick.ac.uk... 137.205.243.107\nConnecting to www.warwick.ac.uk|137.205.243.107|:80... connected.\nHTTP request sent, awaiting response... \n```\n\n\nCan someone check its availability and perhaps put a copy on the Sage cluster?\n\nAlso, should I apply both patches, too?",
    "created_at": "2010-08-07T02:54:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90976",
    "user": "@qed777"
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

archive/issue_comments_090977.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2010-08-07T02:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90977",
    "user": "@qed777"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_090978.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-08-08T04:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90978",
    "user": "@qed777"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_090979.json:
```json
{
    "body": "The package is available now.  I'll include both patches.",
    "created_at": "2010-08-08T04:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90979",
    "user": "@qed777"
}
```

The package is available now.  I'll include both patches.



---

archive/issue_comments_090980.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-08T04:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90980",
    "user": "@qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090981.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:49:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90981",
    "user": "@qed777"
}
```

Resolution: fixed



---

archive/issue_comments_090982.json:
```json
{
    "body": "Sorry not to have responded earlier but I was on holiday for a few days.  I think they were doing some network updating at U of Warwick, which could  explain why you could not get the file.  Glad it's fixed -- and thanks for the review.",
    "created_at": "2010-08-11T15:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9476",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9476#issuecomment-90982",
    "user": "@JohnCremona"
}
```

Sorry not to have responded earlier but I was on holiday for a few days.  I think they were doing some network updating at U of Warwick, which could  explain why you could not get the file.  Glad it's fixed -- and thanks for the review.
