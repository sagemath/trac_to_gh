# Issue 9890: substitute goes too far: (5-e^x).substitute(x=log(x)) -> 5-log(x)

archive/issues_009890.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @RBKreckel\n\nKeywords: pynac\n\nReported by Kees on sage-support:\n\nhttp://groups.google.com/group/sage-support/t/bfa34b077dd31b73\n\n\n```\nRunning the following few lines:\n\neq=5-e^x\nprint \"1:\",eq.substitute(x=3*x)\nprint \"2:\",eq.substitute(x=log(x))\n\nyields the output (Sage 4.5.2 with Ubuntu):\n\n1: -e^(3*x) + 5\n2: -log(x) + 5\n```\n\n\nThis is also present in GiNaC:\n\n\n```\nginsh - GiNaC Interactive Shell (ginac V1.5.7)\n  __,  _______  Copyright (C) 1999-2010 Johannes Gutenberg University Mainz,\n (__) *       | Germany.  This is free software with ABSOLUTELY NO WARRANTY.\n  ._) i N a C | You are welcome to redistribute it under certain conditions.\n<-------------' For details type `warranty;'.\n\nType ?? for a list of help topics.\n> subs(5-exp(x),x==log(x));\n5-log(x)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9891\n\n",
    "created_at": "2010-09-10T19:53:23Z",
    "labels": [
        "component: symbolics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "substitute goes too far: (5-e^x).substitute(x=log(x)) -> 5-log(x)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9890",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

CC:  @RBKreckel

Keywords: pynac

Reported by Kees on sage-support:

http://groups.google.com/group/sage-support/t/bfa34b077dd31b73


```
Running the following few lines:

eq=5-e^x
print "1:",eq.substitute(x=3*x)
print "2:",eq.substitute(x=log(x))

yields the output (Sage 4.5.2 with Ubuntu):

1: -e^(3*x) + 5
2: -log(x) + 5
```


This is also present in GiNaC:


```
ginsh - GiNaC Interactive Shell (ginac V1.5.7)
  __,  _______  Copyright (C) 1999-2010 Johannes Gutenberg University Mainz,
 (__) *       | Germany.  This is free software with ABSOLUTELY NO WARRANTY.
  ._) i N a C | You are welcome to redistribute it under certain conditions.
<-------------' For details type `warranty;'.

Type ?? for a list of help topics.
> subs(5-exp(x),x==log(x));
5-log(x)
```



Issue created by migration from https://trac.sagemath.org/ticket/9891





---

archive/issue_comments_097867.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-09-19T14:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9890#issuecomment-97867",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_097868.json:
```json
{
    "body": "This was fixed in GiNaC by Richard Kreckel:\n\nhttp://www.ginac.de/pipermail/ginac-list/2010-September/001738.html\n\nI merged his changes to pynac, so it will be available in the next release.",
    "created_at": "2010-09-19T14:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9890#issuecomment-97868",
    "user": "https://github.com/burcin"
}
```

This was fixed in GiNaC by Richard Kreckel:

http://www.ginac.de/pipermail/ginac-list/2010-September/001738.html

I merged his changes to pynac, so it will be available in the next release.



---

archive/issue_comments_097869.json:
```json
{
    "body": "Attachment [trac_9891-substitute.patch](tarball://root/attachments/some-uuid/ticket9891/trac_9891-substitute.patch) by @burcin created at 2010-09-19 23:07:06\n\nadd doctest",
    "created_at": "2010-09-19T23:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9890#issuecomment-97869",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_9891-substitute.patch](tarball://root/attachments/some-uuid/ticket9891/trac_9891-substitute.patch) by @burcin created at 2010-09-19 23:07:06

add doctest



---

archive/issue_comments_097870.json:
```json
{
    "body": "Burcin, I'm still getting\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: (5-e^x).substitute(x=log(x))\n-log(x) + 5\n```\n\nWhich version of Pynac is this in?",
    "created_at": "2011-02-17T01:39:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9890#issuecomment-97870",
    "user": "https://github.com/kcrisman"
}
```

Burcin, I'm still getting

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: (5-e^x).substitute(x=log(x))
-log(x) + 5
```

Which version of Pynac is this in?



---

archive/issue_comments_097871.json:
```json
{
    "body": "For reference, here is a link to the upstream patch:\nhttp://www.ginac.de/ginac.git?p=ginac.git;a=commitdiff;h=90ad10b58d02365a407b2d84d8b93e50030feaa5",
    "created_at": "2011-02-17T07:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9890#issuecomment-97871",
    "user": "https://github.com/RBKreckel"
}
```

For reference, here is a link to the upstream patch:
http://www.ginac.de/ginac.git?p=ginac.git;a=commitdiff;h=90ad10b58d02365a407b2d84d8b93e50030feaa5



---

archive/issue_comments_097872.json:
```json
{
    "body": "I can confirm this is not in the latest version of Pynac in Sage or on its website (0.2.1), by looking at container.h.",
    "created_at": "2011-02-17T14:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9890#issuecomment-97872",
    "user": "https://github.com/kcrisman"
}
```

I can confirm this is not in the latest version of Pynac in Sage or on its website (0.2.1), by looking at container.h.



---

archive/issue_comments_097873.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-05-09T15:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9890#issuecomment-97873",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_097874.json:
```json
{
    "body": "New pynac package with the fix is at #11317.",
    "created_at": "2011-05-09T15:08:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9890#issuecomment-97874",
    "user": "https://github.com/burcin"
}
```

New pynac package with the fix is at #11317.



---

archive/issue_comments_097875.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-05-09T18:33:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9890#issuecomment-97875",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097876.json:
```json
{
    "body": "Okay, this is fine.\n\nBurcin, I have to say I feel a little odd saying that I'm reviewing Kreckel's work, when I'm really reviewing your merging his work and your doctest (though I looked at the actual patch, naturally).  Is there a different way to put the author in?  You are the author of the actual patch here, not the Ginac update; I don't think any other spkgs put upstream people who committed things in this way.",
    "created_at": "2011-05-09T18:33:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9890#issuecomment-97876",
    "user": "https://github.com/kcrisman"
}
```

Okay, this is fine.

Burcin, I have to say I feel a little odd saying that I'm reviewing Kreckel's work, when I'm really reviewing your merging his work and your doctest (though I looked at the actual patch, naturally).  Is there a different way to put the author in?  You are the author of the actual patch here, not the Ginac update; I don't think any other spkgs put upstream people who committed things in this way.



---

archive/issue_comments_097877.json:
```json
{
    "body": "Thanks for the review!\n\nReplying to [comment:7 kcrisman]:\n> Burcin, I have to say I feel a little odd saying that I'm reviewing Kreckel's work, when I'm really reviewing your merging his work and your doctest (though I looked at the actual patch, naturally).  Is there a different way to put the author in?  You are the author of the actual patch here, not the Ginac update; I don't think any other spkgs put upstream people who committed things in this way.\n\nI put Richard's name in the authors list since he should get the credit for fixing this in the Sage release notes. I think we should give more credit to upstream developers. Are you suggesting my name should be in the authors or the reviewers field? :)",
    "created_at": "2011-05-09T19:04:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9890#issuecomment-97877",
    "user": "https://github.com/burcin"
}
```

Thanks for the review!

Replying to [comment:7 kcrisman]:
> Burcin, I have to say I feel a little odd saying that I'm reviewing Kreckel's work, when I'm really reviewing your merging his work and your doctest (though I looked at the actual patch, naturally).  Is there a different way to put the author in?  You are the author of the actual patch here, not the Ginac update; I don't think any other spkgs put upstream people who committed things in this way.

I put Richard's name in the authors list since he should get the credit for fixing this in the Sage release notes. I think we should give more credit to upstream developers. Are you suggesting my name should be in the authors or the reviewers field? :)



---

archive/issue_comments_097878.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-27T12:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9890#issuecomment-97878",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
