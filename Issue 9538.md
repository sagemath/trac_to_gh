# Issue 9538: internal side effect in roots?

archive/issues_009538.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @nbruin\n\nKeywords: roots, side effect\n\nConsider the following with Sage 4.4.4:\n\n```\nsage: var('a6,a5,a4,x')\n(a6, a5, a4, x)\nsage: e=15*a6*x^2 + 5*a5*x + a4\nsage: e.roots(x)\n[(-1/30*(sqrt(-12*a4*a6 + 5*a5^2)*sqrt(5) + 5*a5)/a6, 1), (1/30*(sqrt(-12*a4*a6 + 5*a5^2)*sqrt(5) - 5*a5)/a6, 1)]\n```\n\nThis is fine. However:\n\n```\nsage: var('f6,f5,f4,x')\n(f6, f5, f4, x)\nsage: e=15*f6*x^2 + 5*f5*x + f4\nsage: e.roots(x)\n[(1/30*(-I*sqrt(35) - 5)/binomial(n, k), 1), (1/30*(I*sqrt(35) - 5)/binomial(n, k), 1)]\n```\n\nWTF???\n\nIssue created by migration from https://trac.sagemath.org/ticket/9538\n\n",
    "created_at": "2010-07-18T15:42:05Z",
    "labels": [
        "calculus",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "internal side effect in roots?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9538",
    "user": "@zimmermann6"
}
```
Assignee: @burcin

CC:  @nbruin

Keywords: roots, side effect

Consider the following with Sage 4.4.4:

```
sage: var('a6,a5,a4,x')
(a6, a5, a4, x)
sage: e=15*a6*x^2 + 5*a5*x + a4
sage: e.roots(x)
[(-1/30*(sqrt(-12*a4*a6 + 5*a5^2)*sqrt(5) + 5*a5)/a6, 1), (1/30*(sqrt(-12*a4*a6 + 5*a5^2)*sqrt(5) - 5*a5)/a6, 1)]
```

This is fine. However:

```
sage: var('f6,f5,f4,x')
(f6, f5, f4, x)
sage: e=15*f6*x^2 + 5*f5*x + f4
sage: e.roots(x)
[(1/30*(-I*sqrt(35) - 5)/binomial(n, k), 1), (1/30*(I*sqrt(35) - 5)/binomial(n, k), 1)]
```

WTF???

Issue created by migration from https://trac.sagemath.org/ticket/9538





---

archive/issue_comments_091898.json:
```json
{
    "body": "I'm pretty sure this is just #8734.",
    "created_at": "2010-07-18T17:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91898",
    "user": "@mwhansen"
}
```

I'm pretty sure this is just #8734.



---

archive/issue_comments_091899.json:
```json
{
    "body": "Replying to [comment:1 mhansen]:\n> I'm pretty sure this is just #8734.\n\nI tried the patch coming with #8734, but this does not resolve this issue.\n\nPaul",
    "created_at": "2010-07-18T17:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91899",
    "user": "@zimmermann6"
}
```

Replying to [comment:1 mhansen]:
> I'm pretty sure this is just #8734.

I tried the patch coming with #8734, but this does not resolve this issue.

Paul



---

archive/issue_comments_091900.json:
```json
{
    "body": "Replying to [comment:2 zimmerma]:\n> Replying to [comment:1 mhansen]:\n> > I'm pretty sure this is just #8734.\n> \n> I tried the patch coming with #8734, but this does not resolve this issue.\n\nCould you try this again?  After applying #8734 to 4.5.3.alpha0 (and ignoring the patch rejects), I get\n\n```python\nsage: var('f6,f5,f4,x')\n(f6, f5, f4, x)\nsage: e=15*f6*x^2 + 5*f5*x + f4\nsage: e.roots(x)\n[(-1/30*(sqrt(-12*f4*f6 + 5*f5^2)*sqrt(5) + 5*f5)/f6, 1), (1/30*(sqrt(-12*f4*f6 + 5*f5^2)*sqrt(5) - 5*f5)/f6, 1)]\n```\n",
    "created_at": "2010-08-12T22:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91900",
    "user": "@qed777"
}
```

Replying to [comment:2 zimmerma]:
> Replying to [comment:1 mhansen]:
> > I'm pretty sure this is just #8734.
> 
> I tried the patch coming with #8734, but this does not resolve this issue.

Could you try this again?  After applying #8734 to 4.5.3.alpha0 (and ignoring the patch rejects), I get

```python
sage: var('f6,f5,f4,x')
(f6, f5, f4, x)
sage: e=15*f6*x^2 + 5*f5*x + f4
sage: e.roots(x)
[(-1/30*(sqrt(-12*f4*f6 + 5*f5^2)*sqrt(5) + 5*f5)/f6, 1), (1/30*(sqrt(-12*f4*f6 + 5*f5^2)*sqrt(5) - 5*f5)/f6, 1)]
```




---

archive/issue_comments_091901.json:
```json
{
    "body": "The patch attached to #8734 indeed fixes this problem. However there are simpler solutions, and I'm not convinced that #8734 is necessary, given that #7377 could solve this in a much cleaner way. Also see the discussion linked from comment:3:ticket:8734:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/67f0a63d00b8d835/06557a921a582f87\n\nIn particular, Robert Dodier's suggestion to apply this patch to maxima:\n\n\n```\n--- share/contrib/Zeilberger/testZeilberger.mac 9 Feb 2007 22:32:34\n-0000       1.4\n+++ share/contrib/Zeilberger/testZeilberger.mac 15 Jan 2010 19:10:53\n-0000\n@@ -110,3 +110,8 @@\n\n FULL_TEST : append(GOSPER_TEST,EASY_TEST,\n                    HARD_TEST,EXTREME_TEST);\n+\n+kill (g1, g2, g3, g4, g5, g6, g7,\n+    f1, f2, f3, f4, f5, f6, f7, f8, f9, f10,\n+    h1, h2, h3, h4, h5, h6, h6b, h7, h8, h9, h10, h11, h12, h13,\n+    d1, d2); \n```\n\n\nI can confirm that adding these lines to `$SAGE_LOCAL/share/maxima/5.20.1/share/contrib/Zeilberger/testZeilberger.mac` solves this issue.\n\nPerhaps this patch is already in a more recent version of maxima?",
    "created_at": "2010-09-26T00:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91901",
    "user": "@burcin"
}
```

The patch attached to #8734 indeed fixes this problem. However there are simpler solutions, and I'm not convinced that #8734 is necessary, given that #7377 could solve this in a much cleaner way. Also see the discussion linked from comment:3:ticket:8734:

http://groups.google.com/group/sage-devel/browse_thread/thread/67f0a63d00b8d835/06557a921a582f87

In particular, Robert Dodier's suggestion to apply this patch to maxima:


```
--- share/contrib/Zeilberger/testZeilberger.mac 9 Feb 2007 22:32:34
-0000       1.4
+++ share/contrib/Zeilberger/testZeilberger.mac 15 Jan 2010 19:10:53
-0000
@@ -110,3 +110,8 @@

 FULL_TEST : append(GOSPER_TEST,EASY_TEST,
                    HARD_TEST,EXTREME_TEST);
+
+kill (g1, g2, g3, g4, g5, g6, g7,
+    f1, f2, f3, f4, f5, f6, f7, f8, f9, f10,
+    h1, h2, h3, h4, h5, h6, h6b, h7, h8, h9, h10, h11, h12, h13,
+    d1, d2); 
```


I can confirm that adding these lines to `$SAGE_LOCAL/share/maxima/5.20.1/share/contrib/Zeilberger/testZeilberger.mac` solves this issue.

Perhaps this patch is already in a more recent version of maxima?



---

archive/issue_comments_091902.json:
```json
{
    "body": "I confirm that with the #8734 patch applied to 4.5.3 (and ignoring the patch reject) it works\nfine.\n\nHowever I'm convinced by Burcin's argument. I am ready to review a patch based on this patch\napplied to Maxima.\n\nPaul",
    "created_at": "2010-09-26T08:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91902",
    "user": "@zimmermann6"
}
```

I confirm that with the #8734 patch applied to 4.5.3 (and ignoring the patch reject) it works
fine.

However I'm convinced by Burcin's argument. I am ready to review a patch based on this patch
applied to Maxima.

Paul



---

archive/issue_comments_091903.json:
```json
{
    "body": "Attachment [trac_9538-maxima_kill.patch](tarball://root/attachments/some-uuid/ticket9538/trac_9538-maxima_kill.patch) by @burcin created at 2010-09-26 15:58:09",
    "created_at": "2010-09-26T15:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91903",
    "user": "@burcin"
}
```

Attachment [trac_9538-maxima_kill.patch](tarball://root/attachments/some-uuid/ticket9538/trac_9538-maxima_kill.patch) by @burcin created at 2010-09-26 15:58:09



---

archive/issue_comments_091904.json:
```json
{
    "body": "Here is a maxima package that patches the file `share/contrib/Zeilberger/testZeilberger.mac` as suggested by Robert Dodier:\n\nhttp://sage.math.washington.edu/home/burcin/maxima-5.20.1.p1.spkg\n\nattachment:trac_9538-maxima_kill.patch adds a doctest to check the example given in the description.",
    "created_at": "2010-09-26T16:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91904",
    "user": "@burcin"
}
```

Here is a maxima package that patches the file `share/contrib/Zeilberger/testZeilberger.mac` as suggested by Robert Dodier:

http://sage.math.washington.edu/home/burcin/maxima-5.20.1.p1.spkg

attachment:trac_9538-maxima_kill.patch adds a doctest to check the example given in the description.



---

archive/issue_comments_091905.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-26T16:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91905",
    "user": "@burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091906.json:
```json
{
    "body": "I tried `sage -i /tmp/maxima-5.20.1.p1.spkg` but got:\n\n```\n...\n;;; OPTIMIZE levels: Safety=2, Space=0, Speed=3, Debug=2\n;;; End of Pass 1.\n;;; Note: Creating tag: \"_eclFGkv5HJdeKquW_9rDWPWz\" for #P\"binary-ecl/maxima-package.o\"\n;;; Internal error: Unable to find include directory\n;      - Binary file binary-ecl/maxima-package.fas is old or does not exist. \n;        Compile (and load) source file /usr/local/sage-4.5.3/sage/spkg/build/maxima-5.20.1.p1/src/src/maxima-package.lisp instead? y\n\n;      - Should I bother you if this happens again? y\n\n;      - Compiling source file\n;        \"/usr/local/sage-4.5.3/sage/spkg/build/maxima-5.20.1.p1/src/src/maxima-package.lisp\"\n;;; Compiling /usr/local/sage-4.5.3/sage/spkg/build/maxima-5.20.1.p1/src/src/maxima-package.lisp.\n;;; OPTIMIZE levels: Safety=2, Space=0, Speed=3, Debug=2\n;;; End of Pass 1.\n;;; Note: Creating tag: \"_eclFGkv5HJdeKquW_IVMWPWz\" for #P\"binary-ecl/maxima-package.o\"\n;;; Internal error: Unable to find include directory\n;      - Loading binary file \"binary-ecl/maxima-package.fas\" An error occurred during initialization:\nFilesystem error with pathname #P\"/usr/local/sage-4.5.3/sage/spkg/build/maxima-5.20.1.p1/src/src/binary-ecl/maxima-package.fas\".\nEither\n 1) the file does not exist, or\n 2) we are not allow to access the file, or\n 3) the pathname points to a broken symbolic link..\nmake[1]: *** [binary-ecl/maxima] Error 1\nmake[1]: Leaving directory `/usr/local/sage-4.5.3/sage/spkg/build/maxima-5.20.1.p1/src/src'\nmake: *** [all-recursive] Error 1\n***********************************************************\nFailed to make Maxima.\n***********************************************************\n```\n\nDid I something wrong? How to install the patched spkg?\n\nPaul",
    "created_at": "2010-09-26T16:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91906",
    "user": "@zimmermann6"
}
```

I tried `sage -i /tmp/maxima-5.20.1.p1.spkg` but got:

```
...
;;; OPTIMIZE levels: Safety=2, Space=0, Speed=3, Debug=2
;;; End of Pass 1.
;;; Note: Creating tag: "_eclFGkv5HJdeKquW_9rDWPWz" for #P"binary-ecl/maxima-package.o"
;;; Internal error: Unable to find include directory
;      - Binary file binary-ecl/maxima-package.fas is old or does not exist. 
;        Compile (and load) source file /usr/local/sage-4.5.3/sage/spkg/build/maxima-5.20.1.p1/src/src/maxima-package.lisp instead? y

;      - Should I bother you if this happens again? y

;      - Compiling source file
;        "/usr/local/sage-4.5.3/sage/spkg/build/maxima-5.20.1.p1/src/src/maxima-package.lisp"
;;; Compiling /usr/local/sage-4.5.3/sage/spkg/build/maxima-5.20.1.p1/src/src/maxima-package.lisp.
;;; OPTIMIZE levels: Safety=2, Space=0, Speed=3, Debug=2
;;; End of Pass 1.
;;; Note: Creating tag: "_eclFGkv5HJdeKquW_IVMWPWz" for #P"binary-ecl/maxima-package.o"
;;; Internal error: Unable to find include directory
;      - Loading binary file "binary-ecl/maxima-package.fas" An error occurred during initialization:
Filesystem error with pathname #P"/usr/local/sage-4.5.3/sage/spkg/build/maxima-5.20.1.p1/src/src/binary-ecl/maxima-package.fas".
Either
 1) the file does not exist, or
 2) we are not allow to access the file, or
 3) the pathname points to a broken symbolic link..
make[1]: *** [binary-ecl/maxima] Error 1
make[1]: Leaving directory `/usr/local/sage-4.5.3/sage/spkg/build/maxima-5.20.1.p1/src/src'
make: *** [all-recursive] Error 1
***********************************************************
Failed to make Maxima.
***********************************************************
```

Did I something wrong? How to install the patched spkg?

Paul



---

archive/issue_comments_091907.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-09-26T16:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91907",
    "user": "@zimmermann6"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_091908.json:
```json
{
    "body": "patch for maxima spkg",
    "created_at": "2010-09-26T20:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91908",
    "user": "@burcin"
}
```

patch for maxima spkg



---

archive/issue_comments_091909.json:
```json
{
    "body": "Attachment [maxima_package.patch](tarball://root/attachments/some-uuid/ticket9538/maxima_package.patch) by @burcin created at 2010-09-26 20:25:38\n\nReplying to [comment:7 zimmerma]:\n> Did I something wrong? How to install the patched spkg?\n\nI don't have any experience with the maxima spkg. I just applied the patch in attachment:maxima_package.patch. It works here, but just complains about not being able to build `maxima.fasb`:\n\n\n```\ncp: cannot stat `maxima.fasb': No such file or directory\n```\n\n\nPerhaps someone more knowledgeable can help out. Building maxima as a library is #8645.",
    "created_at": "2010-09-26T20:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91909",
    "user": "@burcin"
}
```

Attachment [maxima_package.patch](tarball://root/attachments/some-uuid/ticket9538/maxima_package.patch) by @burcin created at 2010-09-26 20:25:38

Replying to [comment:7 zimmerma]:
> Did I something wrong? How to install the patched spkg?

I don't have any experience with the maxima spkg. I just applied the patch in attachment:maxima_package.patch. It works here, but just complains about not being able to build `maxima.fasb`:


```
cp: cannot stat `maxima.fasb': No such file or directory
```


Perhaps someone more knowledgeable can help out. Building maxima as a library is #8645.



---

archive/issue_comments_091910.json:
```json
{
    "body": "maybe we should wait that #8645 is fixed and merged within Sage to review that ticket.\n\nPaul",
    "created_at": "2010-09-27T09:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91910",
    "user": "@zimmermann6"
}
```

maybe we should wait that #8645 is fixed and merged within Sage to review that ticket.

Paul



---

archive/issue_comments_091911.json:
```json
{
    "body": "Adding\n\n```\nkill (g1, g2, g3, g4, g5, g6, g7,\n    f1, f2, f3, f4, f5, f6, f7, f8, f9, f10,\n    h1, h2, h3, h4, h5, h6, h6b, h7, h8, h9, h10, h11, h12, h13,\n    d1, d2);\n```\n\ndirectly to the bottom of \n\n `SAGE_ROOT/local/share/maxima/5.20.1/share/contrib/Zeilberger/testZeilberger.mac`\n\nwithout installing http://sage.math.washington.edu/home/burcin/maxima-5.20.1.p1.spkg fixes the problem in the description.",
    "created_at": "2010-09-30T23:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91911",
    "user": "@qed777"
}
```

Adding

```
kill (g1, g2, g3, g4, g5, g6, g7,
    f1, f2, f3, f4, f5, f6, f7, f8, f9, f10,
    h1, h2, h3, h4, h5, h6, h6b, h7, h8, h9, h10, h11, h12, h13,
    d1, d2);
```

directly to the bottom of 

 `SAGE_ROOT/local/share/maxima/5.20.1/share/contrib/Zeilberger/testZeilberger.mac`

without installing http://sage.math.washington.edu/home/burcin/maxima-5.20.1.p1.spkg fixes the problem in the description.



---

archive/issue_comments_091912.json:
```json
{
    "body": "Replying to [comment:7 zimmerma]:\n> I tried `sage -i /tmp/maxima-5.20.1.p1.spkg` but got: \n\n> [...]\n\n> Did I something wrong? How to install the patched spkg?\n\nI have the same problem with the forthcoming 4.6.alpha2, **if** I've renamed `SAGE_ROOT` since that copy of Sage was first compiled (and another installation with the previous name does not exist).  In this case, even reinstalling the included Maxima, with\n\n `./sage -f spkg/standard/maxima-5.20.1.p0.spkg`\n\ntriggers the behavior.  Paul, did you happen to move or rename your Sage root directory?  Does  Burcin's p1 package install successfully and fix the roots problem with a Sage that has not been moved?",
    "created_at": "2010-09-30T23:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91912",
    "user": "@qed777"
}
```

Replying to [comment:7 zimmerma]:
> I tried `sage -i /tmp/maxima-5.20.1.p1.spkg` but got: 

> [...]

> Did I something wrong? How to install the patched spkg?

I have the same problem with the forthcoming 4.6.alpha2, **if** I've renamed `SAGE_ROOT` since that copy of Sage was first compiled (and another installation with the previous name does not exist).  In this case, even reinstalling the included Maxima, with

 `./sage -f spkg/standard/maxima-5.20.1.p0.spkg`

triggers the behavior.  Paul, did you happen to move or rename your Sage root directory?  Does  Burcin's p1 package install successfully and fix the roots problem with a Sage that has not been moved?



---

archive/issue_comments_091913.json:
```json
{
    "body": "Nils, do you have any thoughts about the problem in [comment:7 comment 7ff]?",
    "created_at": "2010-09-30T23:32:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91913",
    "user": "@qed777"
}
```

Nils, do you have any thoughts about the problem in [comment:7 comment 7ff]?



---

archive/issue_comments_091914.json:
```json
{
    "body": "> Paul, did you happen to move or rename your Sage root directory?\n\nno, I did all my experiments in /tmp/sage-4.6.alpha1, where I built sage-4.6.alpha1 from source.\nI have no `SAGE_ROOT` environment variable.\n\nPaul",
    "created_at": "2010-10-01T06:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91914",
    "user": "@zimmermann6"
}
```

> Paul, did you happen to move or rename your Sage root directory?

no, I did all my experiments in /tmp/sage-4.6.alpha1, where I built sage-4.6.alpha1 from source.
I have no `SAGE_ROOT` environment variable.

Paul



---

archive/issue_comments_091915.json:
```json
{
    "body": "Burcin, do you agree that we try Mitesh's solution from comment 10, which avoids installing a new\nMaxima spkg? If so, if someone can provide a patch, I will review it.\n\nPaul",
    "created_at": "2010-10-01T06:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91915",
    "user": "@zimmermann6"
}
```

Burcin, do you agree that we try Mitesh's solution from comment 10, which avoids installing a new
Maxima spkg? If so, if someone can provide a patch, I will review it.

Paul



---

archive/issue_comments_091916.json:
```json
{
    "body": "Replying to [comment:14 zimmerma]:\n> Burcin, do you agree that we try Mitesh's solution from comment 10, which avoids installing a new\n> Maxima spkg? If so, if someone can provide a patch, I will review it.\n\nExcept for `SAGE_LOCAL/bin`, the files under `SAGE_LOCAL` are not under version control.  I was mainly trying to check whether Robert's fix works with an already installed Maxima in Sage.\n\nSo far, it seems the build problem is orthogonal to the problem in the description.",
    "created_at": "2010-10-01T07:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91916",
    "user": "@qed777"
}
```

Replying to [comment:14 zimmerma]:
> Burcin, do you agree that we try Mitesh's solution from comment 10, which avoids installing a new
> Maxima spkg? If so, if someone can provide a patch, I will review it.

Except for `SAGE_LOCAL/bin`, the files under `SAGE_LOCAL` are not under version control.  I was mainly trying to check whether Robert's fix works with an already installed Maxima in Sage.

So far, it seems the build problem is orthogonal to the problem in the description.



---

archive/issue_comments_091917.json:
```json
{
    "body": "> So far, it seems the build problem is orthogonal to the problem in the description. \n\nagreed, but how can we proceed in practice so that I can review this ticket?\n\nPaul",
    "created_at": "2010-10-01T07:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91917",
    "user": "@zimmermann6"
}
```

> So far, it seems the build problem is orthogonal to the problem in the description. 

agreed, but how can we proceed in practice so that I can review this ticket?

Paul



---

archive/issue_comments_091918.json:
```json
{
    "body": "apply only this patch -- forget about the package :)",
    "created_at": "2010-10-01T15:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91918",
    "user": "@burcin"
}
```

apply only this patch -- forget about the package :)



---

archive/issue_comments_091919.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-10-01T16:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91919",
    "user": "@burcin"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_091920.json:
```json
{
    "body": "Attachment [trac_9538-maxima_kill.take2.patch](tarball://root/attachments/some-uuid/ticket9538/trac_9538-maxima_kill.take2.patch) by @burcin created at 2010-10-01 16:04:37\n\nI uploaded an alternate patch, attachment:trac_9538-maxima_kill.take2.patch. This issues the `kill` command Robert Dodier recommended when initializing maxima. There is no need for any changes to the maxima package.",
    "created_at": "2010-10-01T16:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91920",
    "user": "@burcin"
}
```

Attachment [trac_9538-maxima_kill.take2.patch](tarball://root/attachments/some-uuid/ticket9538/trac_9538-maxima_kill.take2.patch) by @burcin created at 2010-10-01 16:04:37

I uploaded an alternate patch, attachment:trac_9538-maxima_kill.take2.patch. This issues the `kill` command Robert Dodier recommended when initializing maxima. There is no need for any changes to the maxima package.



---

archive/issue_comments_091921.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-03T10:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91921",
    "user": "@zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091922.json:
```json
{
    "body": "ok for the last patch, which fixes the problem, and all tests pass (tested with Sage 4.4.4).\n\nPaul\n\nPS: a minor remark, is there a mechanism to update the calculus.py patch once the problem is\nfixed upstream?",
    "created_at": "2010-10-03T10:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91922",
    "user": "@zimmermann6"
}
```

ok for the last patch, which fixes the problem, and all tests pass (tested with Sage 4.4.4).

Paul

PS: a minor remark, is there a mechanism to update the calculus.py patch once the problem is
fixed upstream?



---

archive/issue_comments_091923.json:
```json
{
    "body": "Thank you for the review.\n\nReplying to [comment:18 zimmerma]:\n> PS: a minor remark, is there a mechanism to update the calculus.py patch once the problem is\n> fixed upstream?\n\nIf it is fixed upstream, this doctest should fail:\n\n\n```\nsage: maxima = Maxima(init_code = ['load(simplify_sum)']) \nsage: maxima('f1') \nbinomial(n,k) \n```\n\n\nThen we can remove the line with the `kill` command.",
    "created_at": "2010-10-03T10:58:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91923",
    "user": "@burcin"
}
```

Thank you for the review.

Replying to [comment:18 zimmerma]:
> PS: a minor remark, is there a mechanism to update the calculus.py patch once the problem is
> fixed upstream?

If it is fixed upstream, this doctest should fail:


```
sage: maxima = Maxima(init_code = ['load(simplify_sum)']) 
sage: maxima('f1') 
binomial(n,k) 
```


Then we can remove the line with the `kill` command.



---

archive/issue_comments_091924.json:
```json
{
    "body": "> If it is fixed upstream, this doctest should fail: [...]\n\nexcellent!\n\nPaul",
    "created_at": "2010-10-03T11:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91924",
    "user": "@zimmermann6"
}
```

> If it is fixed upstream, this doctest should fail: [...]

excellent!

Paul



---

archive/issue_comments_091925.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-04T02:48:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91925",
    "user": "@qed777"
}
```

Resolution: fixed



---

archive/issue_comments_091926.json:
```json
{
    "body": "For the record, this fails with maxima-5.22.1:\n\n```\nFile \"/home/vbraun/opt/sage-4.6.rc0/devel/sage-main/sage/calculus/calculus.py\", line 368:\n    sage: maxima('f1')\nExpected:\n    binomial(n,k)\nGot:\n    f1\n```\n\nNone of the patches from `maxima_package.patch` are in the updated maxima-5.22.1 package. See #10187 for the updated spgk. I take it that this is the expected behaviour and no further patches to maxima are necessary.",
    "created_at": "2010-10-29T15:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9538",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9538#issuecomment-91926",
    "user": "@vbraun"
}
```

For the record, this fails with maxima-5.22.1:

```
File "/home/vbraun/opt/sage-4.6.rc0/devel/sage-main/sage/calculus/calculus.py", line 368:
    sage: maxima('f1')
Expected:
    binomial(n,k)
Got:
    f1
```

None of the patches from `maxima_package.patch` are in the updated maxima-5.22.1 package. See #10187 for the updated spgk. I take it that this is the expected behaviour and no further patches to maxima are necessary.
