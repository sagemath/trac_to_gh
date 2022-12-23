# Issue 7856: update matplotlib hack for OS X

archive/issues_007856.json:
```json
{
    "body": "Assignee: tbd\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7856\n\n",
    "created_at": "2010-01-06T15:01:56Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "title": "update matplotlib hack for OS X",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7856",
    "user": "was"
}
```
Assignee: tbd



Issue created by migration from https://trac.sagemath.org/ticket/7856





---

archive/issue_comments_068067.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-06T15:02:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7856#issuecomment-68067",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068068.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-06T15:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7856#issuecomment-68068",
    "user": "was"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068069.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-06T15:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7856#issuecomment-68069",
    "user": "was"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068070.json:
```json
{
    "body": "http://wstein.org/home/wstein/patches/matplotlib-0.99.1.p3.spkg",
    "created_at": "2010-01-06T15:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7856#issuecomment-68070",
    "user": "was"
}
```

http://wstein.org/home/wstein/patches/matplotlib-0.99.1.p3.spkg



---

archive/issue_comments_068071.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-06T16:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7856#issuecomment-68071",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_068072.json:
```json
{
    "body": "A few quick comments: SPGK.txt needs to be updated.  Also, is the hack appropriate for OS X running 10.5 (since it now just checks for \"DARWIN\", not the version number)?  I don't have access to a machine to test that.\n\nFinally, if SAGE64 is set and we're on DARWIN, is it worth making some of the other changes in [http://blog.hyperjeff.net/?p=160](http://blog.hyperjeff.net/?p=160)?  For example, in src/make.osx, changing \n\n```\nCFLAGS=\"-arch i386 -arch ppc -I${PREFIX}/include -I${PREFIX}/include/freetype2 -isysroot /Developer/SDKs/MacOSX10.4u.sdk\"\nLDFLAGS=\"-arch i386 -arch ppc -L${PREFIX}/lib -syslibroot,/Developer/SDKs/MacOSX10.4u.sdk\"\n```\n\nso that \"-arch ppc\" gets changed to \"-arch x86_64\"?  (That web page also suggests adding \"FFLAGS\", and making a few other changes.  We can defer these until later, also.)",
    "created_at": "2010-01-06T16:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7856#issuecomment-68072",
    "user": "jhpalmieri"
}
```

A few quick comments: SPGK.txt needs to be updated.  Also, is the hack appropriate for OS X running 10.5 (since it now just checks for "DARWIN", not the version number)?  I don't have access to a machine to test that.

Finally, if SAGE64 is set and we're on DARWIN, is it worth making some of the other changes in [http://blog.hyperjeff.net/?p=160](http://blog.hyperjeff.net/?p=160)?  For example, in src/make.osx, changing 

```
CFLAGS="-arch i386 -arch ppc -I${PREFIX}/include -I${PREFIX}/include/freetype2 -isysroot /Developer/SDKs/MacOSX10.4u.sdk"
LDFLAGS="-arch i386 -arch ppc -L${PREFIX}/lib -syslibroot,/Developer/SDKs/MacOSX10.4u.sdk"
```

so that "-arch ppc" gets changed to "-arch x86_64"?  (That web page also suggests adding "FFLAGS", and making a few other changes.  We can defer these until later, also.)



---

archive/issue_comments_068073.json:
```json
{
    "body": "Oh, also, the file patches/osx10.6hack~ should be deleted.",
    "created_at": "2010-01-06T16:02:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7856#issuecomment-68073",
    "user": "jhpalmieri"
}
```

Oh, also, the file patches/osx10.6hack~ should be deleted.



---

archive/issue_comments_068074.json:
```json
{
    "body": "As far as actual testing goes, on my OS X 10.6 machines:\n\n- before the patch, if I delete the files in ~/.matplotlib, then `sage: plot(sin)` causes a crash.\n\n- after the patch, if I delete the files in ~/.matplotlib, then `sage: plot(sin)` works fine.\n\n- this is completely reproducible: if I force installation of the old matplotlib spkg, then the crashes come back, and then if I force installation of the new one, the crashes go away.\n\nSo positive review, modulo the comments made above.\n\nDo we need to test on an OS X 10.5 machine?",
    "created_at": "2010-01-06T18:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7856#issuecomment-68074",
    "user": "jhpalmieri"
}
```

As far as actual testing goes, on my OS X 10.6 machines:

- before the patch, if I delete the files in ~/.matplotlib, then `sage: plot(sin)` causes a crash.

- after the patch, if I delete the files in ~/.matplotlib, then `sage: plot(sin)` works fine.

- this is completely reproducible: if I force installation of the old matplotlib spkg, then the crashes come back, and then if I force installation of the new one, the crashes go away.

So positive review, modulo the comments made above.

Do we need to test on an OS X 10.5 machine?



---

archive/issue_comments_068075.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-06T23:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7856#issuecomment-68075",
    "user": "was"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_068076.json:
```json
{
    "body": "> A few quick comments: SPGK.txt needs to be updated. Also, is the hack \n> appropriate for OS X running 10.5 (since it now just checks for \"DARWIN\", \n> not the version number)?\n\nIt runs patches/osx10.6hack on any OS X, but *only* actually applies the hack on 10.6.  It immediately exits patches/osx10.6hack on other than 10.6. \n\nI've updated the spkg, and also now tested it on 10.5 and it works fine (as before).  So, can you change it to positive review?",
    "created_at": "2010-01-06T23:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7856#issuecomment-68076",
    "user": "was"
}
```

> A few quick comments: SPGK.txt needs to be updated. Also, is the hack 
> appropriate for OS X running 10.5 (since it now just checks for "DARWIN", 
> not the version number)?

It runs patches/osx10.6hack on any OS X, but *only* actually applies the hack on 10.6.  It immediately exits patches/osx10.6hack on other than 10.6. 

I've updated the spkg, and also now tested it on 10.5 and it works fine (as before).  So, can you change it to positive review?



---

archive/issue_comments_068077.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-06T23:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7856#issuecomment-68077",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068078.json:
```json
{
    "body": "Please see [http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04165.html](http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04165.html) and [http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04166.html](http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04166.html) for something which looks relevant - namely, DPY_ARRAYAUNIQUE_SYMBOL is, in fact, a typo for DPY_ARRAY_UNIQUE_SYMBOL.  I don't know if this would fix things for us, but at any rate the 'horrible hack' uses precisely this (incorrect) variable, so we should at least fix both the source and the hack to use the correct one.",
    "created_at": "2010-01-08T01:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7856#issuecomment-68078",
    "user": "kcrisman"
}
```

Please see [http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04165.html](http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04165.html) and [http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04166.html](http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04166.html) for something which looks relevant - namely, DPY_ARRAYAUNIQUE_SYMBOL is, in fact, a typo for DPY_ARRAY_UNIQUE_SYMBOL.  I don't know if this would fix things for us, but at any rate the 'horrible hack' uses precisely this (incorrect) variable, so we should at least fix both the source and the hack to use the correct one.



---

archive/issue_comments_068079.json:
```json
{
    "body": "Replying to [comment:11 kcrisman]:\n> Please see [http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04165.html](http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04165.html) and [http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04166.html](http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04166.html) for something which looks relevant - namely, DPY_ARRAYAUNIQUE_SYMBOL is, in fact, a typo for DPY_ARRAY_UNIQUE_SYMBOL.  I don't know if this would fix things for us, but at any rate the 'horrible hack' uses precisely this (incorrect) variable, so we should at least fix both the source and the hack to use the correct one.\n\nI tried just the patches mentioned above, not the \"horrible hack\", but it didn't work: the hack was needed to avoid crashes.",
    "created_at": "2010-01-08T06:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7856#issuecomment-68079",
    "user": "jhpalmieri"
}
```

Replying to [comment:11 kcrisman]:
> Please see [http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04165.html](http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04165.html) and [http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04166.html](http://www.mail-archive.com/matplotlib-checkins`@`lists.sourceforge.net/msg04166.html) for something which looks relevant - namely, DPY_ARRAYAUNIQUE_SYMBOL is, in fact, a typo for DPY_ARRAY_UNIQUE_SYMBOL.  I don't know if this would fix things for us, but at any rate the 'horrible hack' uses precisely this (incorrect) variable, so we should at least fix both the source and the hack to use the correct one.

I tried just the patches mentioned above, not the "horrible hack", but it didn't work: the hack was needed to avoid crashes.



---

archive/issue_comments_068080.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T06:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7856",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7856#issuecomment-68080",
    "user": "rlm"
}
```

Resolution: fixed
