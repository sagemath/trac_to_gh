# Issue 9949: Change Brian package from experimental to optional

archive/issues_009949.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  kcrisman\n\nKeywords: brian brain simulator neuronal dynamics\n\nBrian, a simulator for spiking neural networks, has been recently accepted as an experimental package (see ticket [#9675](http://trac.sagemath.org/sage_trac/ticket/9675) and [Brian's webage](http://www.briansimulator.org/)). In this ticket, it has been suggested the possibility to change it to an optional package. However, at least it should be tested in some different platforms.\n\nCode can be downloaded by clicking [here](http://code.google.com/p/spkg-upload/downloads/detail?name=brian-1.2.1.p0.spkg&can=2&q=) or at Sage's experimental packages page: [http://www.sagemath.org/packages/experimental/](http://www.sagemath.org/packages/experimental/).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9950\n\n",
    "created_at": "2010-09-19T17:51:10Z",
    "labels": [
        "packages: optional",
        "minor",
        "enhancement"
    ],
    "title": "Change Brian package from experimental to optional",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9949",
    "user": "uri"
}
```
Assignee: tbd

CC:  kcrisman

Keywords: brian brain simulator neuronal dynamics

Brian, a simulator for spiking neural networks, has been recently accepted as an experimental package (see ticket [#9675](http://trac.sagemath.org/sage_trac/ticket/9675) and [Brian's webage](http://www.briansimulator.org/)). In this ticket, it has been suggested the possibility to change it to an optional package. However, at least it should be tested in some different platforms.

Code can be downloaded by clicking [here](http://code.google.com/p/spkg-upload/downloads/detail?name=brian-1.2.1.p0.spkg&can=2&q=) or at Sage's experimental packages page: [http://www.sagemath.org/packages/experimental/](http://www.sagemath.org/packages/experimental/).

Issue created by migration from https://trac.sagemath.org/ticket/9950





---

archive/issue_comments_099230.json:
```json
{
    "body": "Brian has built-in tests, but they need nose to run. Ticket [#9921](http://trac.sagemath.org/sage_trac/ticket/9921) is precisely about adding nose as an optional/standard package; I installed the package provided there and runned Brian's tests by writing:\n\n[[[\nsage: import brian\nsage: brian.test()\n]]]\n\nand all of them were passed. However, I didn't do an SPKG-TEST file because nose is not part of Sage yet.",
    "created_at": "2010-09-19T18:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9949#issuecomment-99230",
    "user": "uri"
}
```

Brian has built-in tests, but they need nose to run. Ticket [#9921](http://trac.sagemath.org/sage_trac/ticket/9921) is precisely about adding nose as an optional/standard package; I installed the package provided there and runned Brian's tests by writing:

[[[
sage: import brian
sage: brian.test()
]]]

and all of them were passed. However, I didn't do an SPKG-TEST file because nose is not part of Sage yet.



---

archive/issue_comments_099231.json:
```json
{
    "body": "Works fine on OS X 10.4 PPC!  \n\n116 tests, zero errors, zero failures.",
    "created_at": "2010-09-20T20:08:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9949#issuecomment-99231",
    "user": "kcrisman"
}
```

Works fine on OS X 10.4 PPC!  

116 tests, zero errors, zero failures.



---

archive/issue_comments_099232.json:
```json
{
    "body": "Same on OS X 10.6.",
    "created_at": "2010-09-20T20:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9949#issuecomment-99232",
    "user": "kcrisman"
}
```

Same on OS X 10.6.



---

archive/issue_comments_099233.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-26T20:14:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9949#issuecomment-99233",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_099234.json:
```json
{
    "body": "This should be accepted.  It still works fine, installs fine.  Granted, perhaps one can do this without an spkg, but why not have it?\n\nBy the way, Brian is now in version 1.3.1, but that is a different issue.",
    "created_at": "2012-05-26T20:14:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9949#issuecomment-99234",
    "user": "kcrisman"
}
```

This should be accepted.  It still works fine, installs fine.  Granted, perhaps one can do this without an spkg, but why not have it?

By the way, Brian is now in version 1.3.1, but that is a different issue.



---

archive/issue_comments_099235.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-26T20:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9949#issuecomment-99235",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_099236.json:
```json
{
    "body": "Also ok on sage.math.",
    "created_at": "2012-05-26T20:17:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9949#issuecomment-99236",
    "user": "kcrisman"
}
```

Also ok on sage.math.



---

archive/issue_comments_099237.json:
```json
{
    "body": "Changing keywords from \"brian brain simulator neuronal dynamics\" to \"brian brain simulator neuronal dynamics sd40.5\".",
    "created_at": "2012-05-26T20:17:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9949#issuecomment-99237",
    "user": "kcrisman"
}
```

Changing keywords from "brian brain simulator neuronal dynamics" to "brian brain simulator neuronal dynamics sd40.5".



---

archive/issue_comments_099238.json:
```json
{
    "body": "spkg moved to optional",
    "created_at": "2012-06-11T20:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9949#issuecomment-99238",
    "user": "schilly"
}
```

spkg moved to optional



---

archive/issue_comments_099239.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-06-12T08:15:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9949#issuecomment-99239",
    "user": "jdemeyer"
}
```

Resolution: fixed
