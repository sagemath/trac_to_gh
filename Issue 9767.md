# Issue 9767: Fix PolyBoRi's broken dynamic libraries

archive/issues_009767.json:
```json
{
    "body": "Assignee: @alexanderdreyer\n\nCC:  polybori @malb @wjp mvngu\n\nIn #8830 wqe worked around PolyBoRi's broken dynamic libraries by removing them after build, hence using the static ones instead. The problem was caused by improper handling of a global variable which was fixed for upcoming PolyBoRi 0.7.\n\nThe package at http://sage.math.washington.edu/home/dreyer/pb/polybori-0.6.4.p5.spkg backports this fix and reintroduces the dynamic libraries. The spkg is based on #9717 and assumes its sage-library patch to be applied. It installs, runs and passed testall on boxen.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9768\n\n",
    "created_at": "2010-08-19T20:17:16Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Fix PolyBoRi's broken dynamic libraries",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9767",
    "user": "https://github.com/alexanderdreyer"
}
```
Assignee: @alexanderdreyer

CC:  polybori @malb @wjp mvngu

In #8830 wqe worked around PolyBoRi's broken dynamic libraries by removing them after build, hence using the static ones instead. The problem was caused by improper handling of a global variable which was fixed for upcoming PolyBoRi 0.7.

The package at http://sage.math.washington.edu/home/dreyer/pb/polybori-0.6.4.p5.spkg backports this fix and reintroduces the dynamic libraries. The spkg is based on #9717 and assumes its sage-library patch to be applied. It installs, runs and passed testall on boxen.

Issue created by migration from https://trac.sagemath.org/ticket/9768





---

archive/issue_comments_095551.json:
```json
{
    "body": "Attachment [polybori-0.6.4.p5.spkg.patch](tarball://root/attachments/some-uuid/ticket9768/polybori-0.6.4.p5.spkg.patch) by @alexanderdreyer created at 2010-08-19 20:25:51\n\nDiffs of the new package",
    "created_at": "2010-08-19T20:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9767#issuecomment-95551",
    "user": "https://github.com/alexanderdreyer"
}
```

Attachment [polybori-0.6.4.p5.spkg.patch](tarball://root/attachments/some-uuid/ticket9768/polybori-0.6.4.p5.spkg.patch) by @alexanderdreyer created at 2010-08-19 20:25:51

Diffs of the new package



---

archive/issue_comments_095552.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-19T20:27:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9767#issuecomment-95552",
    "user": "https://github.com/alexanderdreyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095553.json:
```json
{
    "body": "The SPKG looks good, I'm running installation + doctests on a few platforms right now, so far that also looks good.\n\nA somewhat related issue (feel free to ignore): It seems scons doesn't touch for example polybori.h if that didn't change. It would thus be nice to touch this file at the end of spkg-install to inform the Sage build system that it needs to rebuild the extensions. If you agree I can provide a patch.",
    "created_at": "2010-08-20T13:33:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9767#issuecomment-95553",
    "user": "https://github.com/malb"
}
```

The SPKG looks good, I'm running installation + doctests on a few platforms right now, so far that also looks good.

A somewhat related issue (feel free to ignore): It seems scons doesn't touch for example polybori.h if that didn't change. It would thus be nice to touch this file at the end of spkg-install to inform the Sage build system that it needs to rebuild the extensions. If you agree I can provide a patch.



---

archive/issue_comments_095554.json:
```json
{
    "body": "I built this SPKG and ran long doctests on bsd.math, sage.math and t2.math. They all worked fine, thus I'm giving this a positive review.",
    "created_at": "2010-08-22T15:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9767#issuecomment-95554",
    "user": "https://github.com/malb"
}
```

I built this SPKG and ran long doctests on bsd.math, sage.math and t2.math. They all worked fine, thus I'm giving this a positive review.



---

archive/issue_comments_095555.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-22T15:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9767#issuecomment-95555",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095556.json:
```json
{
    "body": "> A somewhat related issue (feel free to ignore): It seems scons doesn't touch for example polybori.h if that didn't change. It would thus be nice to touch this file at the end of spkg-install to inform the Sage build system that it needs to rebuild the extensions. If you agree I can provide a patch.\n\nFeel free to provide such a patch (even tough it's a little bit against the philosopy that a build system should take care of the remaining dependencies automatically).",
    "created_at": "2010-08-22T21:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9767#issuecomment-95556",
    "user": "https://github.com/alexanderdreyer"
}
```

> A somewhat related issue (feel free to ignore): It seems scons doesn't touch for example polybori.h if that didn't change. It would thus be nice to touch this file at the end of spkg-install to inform the Sage build system that it needs to rebuild the extensions. If you agree I can provide a patch.

Feel free to provide such a patch (even tough it's a little bit against the philosopy that a build system should take care of the remaining dependencies automatically).



---

archive/issue_comments_095557.json:
```json
{
    "body": "Changing component from algebra to packages.",
    "created_at": "2010-09-15T10:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9767#issuecomment-95557",
    "user": "https://github.com/qed777"
}
```

Changing component from algebra to packages.



---

archive/issue_comments_095558.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-16T00:53:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9767#issuecomment-95558",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_009897.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-16T00:53:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9767",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9767#event-9897"
}
```



---

archive/issue_comments_095559.json:
```json
{
    "body": "I have not merged the p5 package.  Instead, I've merged #9872's p6 package, which [comment:ticket:9872:17 includes the changes made here].",
    "created_at": "2010-09-16T00:53:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9767#issuecomment-95559",
    "user": "https://github.com/qed777"
}
```

I have not merged the p5 package.  Instead, I've merged #9872's p6 package, which [comment:ticket:9872:17 includes the changes made here].
