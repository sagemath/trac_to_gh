# Issue 9003: Doctest failure on Mac PPC in free_module.py

archive/issues_009003.json:
```json
{
    "body": "Assignee: tbd\n\nOn Mac PPC G4 with 10.4:\n\n```\nsage -t  \"devel/sage/sage/modules/free_module.py\"           \n**********************************************************************\n    sage: V.base_extend(QQ)\nExpected:\n    Vector space of dimension 7 over Rational Field\nGot:\n    V\n**********************************************************************\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9003\n\n",
    "created_at": "2010-05-21T00:04:26Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "Doctest failure on Mac PPC in free_module.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9003",
    "user": "https://github.com/kcrisman"
}
```
Assignee: tbd

On Mac PPC G4 with 10.4:

```
sage -t  "devel/sage/sage/modules/free_module.py"           
**********************************************************************
    sage: V.base_extend(QQ)
Expected:
    Vector space of dimension 7 over Rational Field
Got:
    V
**********************************************************************
```



Issue created by migration from https://trac.sagemath.org/ticket/9003





---

archive/issue_comments_083119.json:
```json
{
    "body": "I have the same failure testing sage 4.4.2 (32-bit) on Mac OS X, 10.5.8, on a Mac Pro (Dual Quad Xeon).",
    "created_at": "2010-05-21T14:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83119",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```

I have the same failure testing sage 4.4.2 (32-bit) on Mac OS X, 10.5.8, on a Mac Pro (Dual Quad Xeon).



---

archive/issue_comments_083120.json:
```json
{
    "body": "The same occurs for Sage-4.4.2 on 32bit MacIntel OS X 10.4.\n\nOn that very system, Sage-4.4.2.rc0 did *not* show this error.",
    "created_at": "2010-05-21T16:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83120",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

The same occurs for Sage-4.4.2 on 32bit MacIntel OS X 10.4.

On that very system, Sage-4.4.2.rc0 did *not* show this error.



---

archive/issue_comments_083121.json:
```json
{
    "body": "So on 10.4 and 10.5, but not on OS X 10.6.  Very interesting.  I don't have time to look at this now, but will be happy to test.  Given that the changes from rc0 to final [http://groups.google.com/group/sage-release/msg/45369d3053275b58?](http://groups.google.com/group/sage-release/msg/45369d3053275b58?)  are all in documentation, this seems strange.",
    "created_at": "2010-05-21T16:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83121",
    "user": "https://github.com/kcrisman"
}
```

So on 10.4 and 10.5, but not on OS X 10.6.  Very interesting.  I don't have time to look at this now, but will be happy to test.  Given that the changes from rc0 to final [http://groups.google.com/group/sage-release/msg/45369d3053275b58?](http://groups.google.com/group/sage-release/msg/45369d3053275b58?)  are all in documentation, this seems strange.



---

archive/issue_comments_083122.json:
```json
{
    "body": "I **don't** get this failure with 32 bit 4.4 built from source on a  1.8 GHz PowerPC G5 running Mac OS X 10.5.8",
    "created_at": "2010-05-22T09:14:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83122",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

I **don't** get this failure with 32 bit 4.4 built from source on a  1.8 GHz PowerPC G5 running Mac OS X 10.5.8



---

archive/issue_comments_083123.json:
```json
{
    "body": "Guys, this problem is *by far* worse than I ever thought! I changed the lines 1124ff in question in \"modules/free_module.py\" to:\n\n```\n            sage: V = ZZ^7; V\n            Ambient free module of rank 7 over the principal ideal domain Integer Ring\n            sage: W = V.base_extend(QQ)\n            sage: W._repr_()\n            'Vector space of dimension 7 over Rational Field'\n            sage: W\n            Vector space of dimension 7 over Rational Field\n```\n\n\nand this is the one failing doctest I get when running \"sage -t -verbose \"devel/sage/sage/modules/free_module.py\"\":\n\n```\nTrying:\n    set_random_seed(0L)\nExpecting nothing\nok\nTrying:\n    change_warning_output(sys.stdout)\nExpecting nothing\nok\nTrying:\n    V = ZZ**Integer(7); V###line 1124:_sage_    >>> V = ZZ^7; V\nExpecting:\n    Ambient free module of rank 7 over the principal ideal domain Integer Ring\nok\nTrying:\n    W = V.base_extend(QQ)###line 1126:_sage_    >>> W = V.base_extend(QQ)\nExpecting nothing\nok\nTrying:\n    W._repr_()###line 1127:_sage_    >>> W._repr_()\nExpecting:\n    'Vector space of dimension 7 over Rational Field'\nok\nTrying:\n    W###line 1129:_sage_    >>> W\nExpecting:\n    Vector space of dimension 7 over Rational Field\n**********************************************************************\nFile \"/Users/Shared/sage/test/sage-4.4.2/devel/sage/sage/modules/free_module.py\", line 924, in __main__.example_23\nFailed example:\n    W###line 1129:_sage_    >>> W\nExpected:\n    Vector space of dimension 7 over Rational Field\nGot:\n    V\n```\n\nUnbelievable!\n\nThe problem seems to lie within the doctest framework ... does anybody has experience with that? I think I stumbled once upon a time over temporary files from doctests, does anyone remember where these are stored?",
    "created_at": "2010-05-22T20:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83123",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Guys, this problem is *by far* worse than I ever thought! I changed the lines 1124ff in question in "modules/free_module.py" to:

```
            sage: V = ZZ^7; V
            Ambient free module of rank 7 over the principal ideal domain Integer Ring
            sage: W = V.base_extend(QQ)
            sage: W._repr_()
            'Vector space of dimension 7 over Rational Field'
            sage: W
            Vector space of dimension 7 over Rational Field
```


and this is the one failing doctest I get when running "sage -t -verbose "devel/sage/sage/modules/free_module.py"":

```
Trying:
    set_random_seed(0L)
Expecting nothing
ok
Trying:
    change_warning_output(sys.stdout)
Expecting nothing
ok
Trying:
    V = ZZ**Integer(7); V###line 1124:_sage_    >>> V = ZZ^7; V
Expecting:
    Ambient free module of rank 7 over the principal ideal domain Integer Ring
ok
Trying:
    W = V.base_extend(QQ)###line 1126:_sage_    >>> W = V.base_extend(QQ)
Expecting nothing
ok
Trying:
    W._repr_()###line 1127:_sage_    >>> W._repr_()
Expecting:
    'Vector space of dimension 7 over Rational Field'
ok
Trying:
    W###line 1129:_sage_    >>> W
Expecting:
    Vector space of dimension 7 over Rational Field
**********************************************************************
File "/Users/Shared/sage/test/sage-4.4.2/devel/sage/sage/modules/free_module.py", line 924, in __main__.example_23
Failed example:
    W###line 1129:_sage_    >>> W
Expected:
    Vector space of dimension 7 over Rational Field
Got:
    V
```

Unbelievable!

The problem seems to lie within the doctest framework ... does anybody has experience with that? I think I stumbled once upon a time over temporary files from doctests, does anyone remember where these are stored?



---

archive/issue_comments_083124.json:
```json
{
    "body": "Oh, I should add that from within Sage (command line/interpreter), everything is OK ...",
    "created_at": "2010-05-22T20:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83124",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Oh, I should add that from within Sage (command line/interpreter), everything is OK ...



---

archive/issue_comments_083125.json:
```json
{
    "body": "My system is Mac Pro, Quad-core Intel Xeon 64bit, Snow Leopard. With Sage 4.4.2, I don't have this doctest failure. But strangely enough, if I apply a patch for other purpose, I have the doctest failure. It is reproducible. The patch mainly touches sage/rings/polynomial/term_order.py, and is now attached to the ticket #6922.",
    "created_at": "2010-05-25T15:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83125",
    "user": "https://github.com/kwankyu"
}
```

My system is Mac Pro, Quad-core Intel Xeon 64bit, Snow Leopard. With Sage 4.4.2, I don't have this doctest failure. But strangely enough, if I apply a patch for other purpose, I have the doctest failure. It is reproducible. The patch mainly touches sage/rings/polynomial/term_order.py, and is now attached to the ticket #6922.



---

archive/issue_comments_083126.json:
```json
{
    "body": "Thanks, klee, hopefully this will help us track it down.\n\nReplying to [comment:3 kcrisman]:\n> So on 10.4 and 10.5, but not on OS X 10.6.  Very interesting.  I don't have time to look at this now, but will be happy to test.  Given that the changes from rc0 to final [http://groups.google.com/group/sage-release/msg/45369d3053275b58?](http://groups.google.com/group/sage-release/msg/45369d3053275b58?)  are all in documentation, this seems strange.\n\nHere they are:\n\n```\n#8915: Mike Zabrocki: improve documentation on combinat.dyck_words [Reviewed by Minh Van Nguyen, S\u00e9bastien Labb\u00e9] \n#8919: William Laffin: documetation error in super_categories for Sets [Reviewed by Minh Van Nguyen] \n#8964: Jason Grout: Two small typos [Reviewed by Francis Clarke] \n#8979: Andr\u00e9-Patrick Bubel: spelling mistake in sage/gsl/ode.pyx [Reviewed by Minh Van Nguyen] \n#8990: Georg S. Weber: update MPIR 1.2.2 license information as requested by upstream [Reviewed by Minh Van Nguyen] \n#8991: Rob Beezer: Adjust developer walkthrough for two changes to mercurial queues syntax [Reviewed by Arthur Lubovsky] \n```\n\nI'll try to revert some of these and see if that helps track it down.",
    "created_at": "2010-05-25T15:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83126",
    "user": "https://github.com/kcrisman"
}
```

Thanks, klee, hopefully this will help us track it down.

Replying to [comment:3 kcrisman]:
> So on 10.4 and 10.5, but not on OS X 10.6.  Very interesting.  I don't have time to look at this now, but will be happy to test.  Given that the changes from rc0 to final [http://groups.google.com/group/sage-release/msg/45369d3053275b58?](http://groups.google.com/group/sage-release/msg/45369d3053275b58?)  are all in documentation, this seems strange.

Here they are:

```
#8915: Mike Zabrocki: improve documentation on combinat.dyck_words [Reviewed by Minh Van Nguyen, Sébastien Labbé] 
#8919: William Laffin: documetation error in super_categories for Sets [Reviewed by Minh Van Nguyen] 
#8964: Jason Grout: Two small typos [Reviewed by Francis Clarke] 
#8979: André-Patrick Bubel: spelling mistake in sage/gsl/ode.pyx [Reviewed by Minh Van Nguyen] 
#8990: Georg S. Weber: update MPIR 1.2.2 license information as requested by upstream [Reviewed by Minh Van Nguyen] 
#8991: Rob Beezer: Adjust developer walkthrough for two changes to mercurial queues syntax [Reviewed by Arthur Lubovsky] 
```

I'll try to revert some of these and see if that helps track it down.



---

archive/issue_comments_083127.json:
```json
{
    "body": "After much testing, I am pretty certain that the error is caused by revision 14321.  You may ask what that revision looks like.  \n\n```\nchangeset:   14321:1451c00a8d44\ntag:         tip\nuser:        Minh Van Nguyen <nguyenminh2@gmail.com>\ndate:        Wed May 19 00:55:29 2010 -0700\nsummary:     4.4.2\n\ndiff -r 26a4be28b4ef -r 1451c00a8d44 sage/version.py\n--- a/sage/version.py   Wed May 19 00:55:29 2010 -0700\n+++ b/sage/version.py   Wed May 19 00:55:29 2010 -0700\n@@ -1,2 +1,2 @@\n \"\"\"nodoctests\"\"\"\n-version='4.4.2.rc0'; date='2010-05-12'\n+version='4.4.2'; date='2010-05-19'\n\n```\n\nWHAT???\n\nBut on my OSX 10.4.11 PPC G4 at 1.25 GHz, that very last change to get to Sage 4.4.2 is what does it.   Combine that with klee's report, and I am totally baffled.  Is it possible that some weird cumulative change could cause a weird overflow or something along the lines of what GeorgSWeber is suggesting?",
    "created_at": "2010-05-26T02:57:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83127",
    "user": "https://github.com/kcrisman"
}
```

After much testing, I am pretty certain that the error is caused by revision 14321.  You may ask what that revision looks like.  

```
changeset:   14321:1451c00a8d44
tag:         tip
user:        Minh Van Nguyen <nguyenminh2@gmail.com>
date:        Wed May 19 00:55:29 2010 -0700
summary:     4.4.2

diff -r 26a4be28b4ef -r 1451c00a8d44 sage/version.py
--- a/sage/version.py   Wed May 19 00:55:29 2010 -0700
+++ b/sage/version.py   Wed May 19 00:55:29 2010 -0700
@@ -1,2 +1,2 @@
 """nodoctests"""
-version='4.4.2.rc0'; date='2010-05-12'
+version='4.4.2'; date='2010-05-19'

```

WHAT???

But on my OSX 10.4.11 PPC G4 at 1.25 GHz, that very last change to get to Sage 4.4.2 is what does it.   Combine that with klee's report, and I am totally baffled.  Is it possible that some weird cumulative change could cause a weird overflow or something along the lines of what GeorgSWeber is suggesting?



---

archive/issue_comments_083128.json:
```json
{
    "body": "I haven't been following this ticket (or the sage-release thread), but just a random idea to throw out there: is there any chance that one or more of those quote characters is actually in a different character set, or something else like that?",
    "created_at": "2010-05-26T06:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83128",
    "user": "https://github.com/craigcitro"
}
```

I haven't been following this ticket (or the sage-release thread), but just a random idea to throw out there: is there any chance that one or more of those quote characters is actually in a different character set, or something else like that?



---

archive/issue_comments_083129.json:
```json
{
    "body": "Replying to [comment:5 GeorgSWeber]:\n> The problem seems to lie within the doctest framework ... does anybody has experience with that? I think I stumbled once upon a time over temporary files from doctests, does anyone remember where these are stored?\n\nIn this case, it should be `~/.sage/tmp/.doctest_free_module.py`. It's only kept after failing tests, I believe.",
    "created_at": "2010-05-26T09:24:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83129",
    "user": "https://github.com/wjp"
}
```

Replying to [comment:5 GeorgSWeber]:
> The problem seems to lie within the doctest framework ... does anybody has experience with that? I think I stumbled once upon a time over temporary files from doctests, does anyone remember where these are stored?

In this case, it should be `~/.sage/tmp/.doctest_free_module.py`. It's only kept after failing tests, I believe.



---

archive/issue_comments_083130.json:
```json
{
    "body": "Replying to [comment:10 craigcitro]:\n> I haven't been following this ticket (or the sage-release thread), but just a random idea to throw out there: is there any chance that one or more of those quote characters is actually in a different character set, or something else like that? \n\n(At least) `version.py` does not contain any non-ASCII characters.",
    "created_at": "2010-05-26T12:16:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83130",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:10 craigcitro]:
> I haven't been following this ticket (or the sage-release thread), but just a random idea to throw out there: is there any chance that one or more of those quote characters is actually in a different character set, or something else like that? 

(At least) `version.py` does not contain any non-ASCII characters.



---

archive/issue_comments_083131.json:
```json
{
    "body": "To add to the confusion (or is this enlightening for somebody?), here is what happened when I revisited the issue, freshly firing up Sage-4.4.2:\n\n```\ngeorg-webers-computer:~ georgweber$ cd ../Shared/sage/sage-4.4.2\ngeorg-webers-computer:/Users/Shared/sage/sage-4.4.2 georgweber$ ./sage -t devel/sage/sage/modules/free_module.py\nsage -t  \"devel/sage/sage/modules/free_module.py\"           \n         [60.4 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 60.5 seconds\ngeorg-webers-computer:/Users/Shared/sage/sage-4.4.2 georgweber$ ./sage -t devel/sage/sage/modules/free_module.py\nsage -t  \"devel/sage/sage/modules/free_module.py\"           \n**********************************************************************\nFile \"/Users/Shared/sage/test/sage-4.4.2/devel/sage/sage/modules/free_module.py\", line 1129:\n    sage: W\nExpected:\n    Vector space of dimension 7 over Rational Field\nGot:\n    V\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_23\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/georgweber/.sage//tmp/.doctest_free_module.py\n         [34.7 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/modules/free_module.py\"\nTotal time for all tests: 34.7 seconds\n```\n\nSo the very first attempt was successful! However it took much time. I think this is due to the fact that quite some libraries have to be loaded to memory, which is not anymore the case for the subsequent tests (where the needed libraries are already present). After this first successful run, *all* directly following runs fail (I just tried a couple of times, only the first one is attached above). Note that I did let run the tests without doing any changes to code in between (you might notice that I had let run the doctest on file like I had changed it); I just used \"arrow up\" in the terminal to get the last command and re-issued it, immediately after the first one.\n\nSo if anybody is doing tests w.r.t. this issue, please keep in mind that the \"history\" does seem to matter, i.e. whether the system was just started up, or whether already test have been running!\n\nSince Kwankyu Lee reported above that he could \"get\" this issue on OS X 64bit (with Sage-4.4.2, after applying a seemingly totally unrelated patch to it) also, I altered the title line a bit.",
    "created_at": "2010-05-26T15:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83131",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

To add to the confusion (or is this enlightening for somebody?), here is what happened when I revisited the issue, freshly firing up Sage-4.4.2:

```
georg-webers-computer:~ georgweber$ cd ../Shared/sage/sage-4.4.2
georg-webers-computer:/Users/Shared/sage/sage-4.4.2 georgweber$ ./sage -t devel/sage/sage/modules/free_module.py
sage -t  "devel/sage/sage/modules/free_module.py"           
         [60.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 60.5 seconds
georg-webers-computer:/Users/Shared/sage/sage-4.4.2 georgweber$ ./sage -t devel/sage/sage/modules/free_module.py
sage -t  "devel/sage/sage/modules/free_module.py"           
**********************************************************************
File "/Users/Shared/sage/test/sage-4.4.2/devel/sage/sage/modules/free_module.py", line 1129:
    sage: W
Expected:
    Vector space of dimension 7 over Rational Field
Got:
    V
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_23
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/georgweber/.sage//tmp/.doctest_free_module.py
         [34.7 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/modules/free_module.py"
Total time for all tests: 34.7 seconds
```

So the very first attempt was successful! However it took much time. I think this is due to the fact that quite some libraries have to be loaded to memory, which is not anymore the case for the subsequent tests (where the needed libraries are already present). After this first successful run, *all* directly following runs fail (I just tried a couple of times, only the first one is attached above). Note that I did let run the tests without doing any changes to code in between (you might notice that I had let run the doctest on file like I had changed it); I just used "arrow up" in the terminal to get the last command and re-issued it, immediately after the first one.

So if anybody is doing tests w.r.t. this issue, please keep in mind that the "history" does seem to matter, i.e. whether the system was just started up, or whether already test have been running!

Since Kwankyu Lee reported above that he could "get" this issue on OS X 64bit (with Sage-4.4.2, after applying a seemingly totally unrelated patch to it) also, I altered the title line a bit.



---

archive/issue_comments_083132.json:
```json
{
    "body": "Karl-Dieter, I can confirm your finding. More precisely, on a fresh clone made in Sage-4.4.2, I did \"hg update -r 14320\", i.e. reverting only the last change in version.py. Then I did \"sage -b\", and (only) version.py got updated.\n\nAnd then, doctesting \"free_module.py\" succeeds (I tried it several times)!\n\nDouble-check: Doing \"hg update -r 14321\" (and then \"sage -b\", which touches only version.py), and after that --- doctesting \"free_module.py\" fails again (I also tested several times) ... \n\nBTW, thanks for the tip w.r.t. the \"dot\" doctest files --- I found it exactly there, under \"~/.sage/tmp/.doctest_free_module.py\". It looks totally innocent to me, however (the failing doctest is \"example_23\").",
    "created_at": "2010-05-26T15:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83132",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Karl-Dieter, I can confirm your finding. More precisely, on a fresh clone made in Sage-4.4.2, I did "hg update -r 14320", i.e. reverting only the last change in version.py. Then I did "sage -b", and (only) version.py got updated.

And then, doctesting "free_module.py" succeeds (I tried it several times)!

Double-check: Doing "hg update -r 14321" (and then "sage -b", which touches only version.py), and after that --- doctesting "free_module.py" fails again (I also tested several times) ... 

BTW, thanks for the tip w.r.t. the "dot" doctest files --- I found it exactly there, under "~/.sage/tmp/.doctest_free_module.py". It looks totally innocent to me, however (the failing doctest is "example_23").



---

archive/issue_comments_083133.json:
```json
{
    "body": "That is really bizarre... is it the change to version or to date in version.py that breaks it? Does it depend on the length of the date and/or version strings, or the content?",
    "created_at": "2010-05-26T15:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83133",
    "user": "https://github.com/wjp"
}
```

That is really bizarre... is it the change to version or to date in version.py that breaks it? Does it depend on the length of the date and/or version strings, or the content?



---

archive/issue_comments_083134.json:
```json
{
    "body": "Some more tapping around in the dark:\n\n```\n        EXAMPLES::\n        \n            sage: testname = ZZ^7\n            sage: testname.base_extend(QQ)\n            Vector space of dimension 7 over Rational Field\n```\n\ngives:\n\n```\n**********************************************************************\nFile \"/Users/Shared/sage/test/sage-4.4.2/devel/sage/sage/modules/free_module.py\", line 1125:\n    sage: testname.base_extend(QQ)\nExpected:\n    Vector space of dimension 7 over Rational Field\nGot:\n    V\n**********************************************************************\n```\n\nAmazing. Now try a bit \"Eau de Cologne\":\n\n```\n        EXAMPLES::\n        \n            sage: testname = ZZ^4711\n            sage: testname.base_extend(QQ)\n            Vector space of dimension 4711 over Rational Field\n```\n\nand this gives (repeatedly, several times):\n\n```\nsage -t  \"devel/sage/sage/modules/free_module.py\"           \n         [35.3 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 35.3 seconds\n```\n\nHmm, I've got to stop here for today, but the next thing one might check, is whether in (the doctest file of) free_module.py, somewhere there is *another* \"ZZ^7\" lurking with the name of \"V\", getting loaded/dumped or something like that ...",
    "created_at": "2010-05-26T16:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83134",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Some more tapping around in the dark:

```
        EXAMPLES::
        
            sage: testname = ZZ^7
            sage: testname.base_extend(QQ)
            Vector space of dimension 7 over Rational Field
```

gives:

```
**********************************************************************
File "/Users/Shared/sage/test/sage-4.4.2/devel/sage/sage/modules/free_module.py", line 1125:
    sage: testname.base_extend(QQ)
Expected:
    Vector space of dimension 7 over Rational Field
Got:
    V
**********************************************************************
```

Amazing. Now try a bit "Eau de Cologne":

```
        EXAMPLES::
        
            sage: testname = ZZ^4711
            sage: testname.base_extend(QQ)
            Vector space of dimension 4711 over Rational Field
```

and this gives (repeatedly, several times):

```
sage -t  "devel/sage/sage/modules/free_module.py"           
         [35.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 35.3 seconds
```

Hmm, I've got to stop here for today, but the next thing one might check, is whether in (the doctest file of) free_module.py, somewhere there is *another* "ZZ^7" lurking with the name of "V", getting loaded/dumped or something like that ...



---

archive/issue_comments_083135.json:
```json
{
    "body": "Ups, I meant to write \"ZZ to the power of seven\" ...",
    "created_at": "2010-05-26T16:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83135",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Ups, I meant to write "ZZ to the power of seven" ...



---

archive/issue_comments_083136.json:
```json
{
    "body": "And keep in mind this error seems to only occur on MacOS...",
    "created_at": "2010-05-26T16:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83136",
    "user": "https://github.com/nexttime"
}
```

And keep in mind this error seems to only occur on MacOS...



---

archive/issue_comments_083137.json:
```json
{
    "body": "Replying to [comment:16 GeorgSWeber]:\n>\n> Hmm, I've got to stop here for today, but the next thing one might check, is whether in (the doctest file of) free_module.py, somewhere there is *another* `\"ZZ^7\"` lurking with the name of \"V\", getting loaded/dumped or something like that ...\n\nThat sounds like a very good idea.\n\nElsewhere in the file is an example renaming `QQ^7` to V...",
    "created_at": "2010-05-26T16:19:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83137",
    "user": "https://github.com/wjp"
}
```

Replying to [comment:16 GeorgSWeber]:
>
> Hmm, I've got to stop here for today, but the next thing one might check, is whether in (the doctest file of) free_module.py, somewhere there is *another* `"ZZ^7"` lurking with the name of "V", getting loaded/dumped or something like that ...

That sounds like a very good idea.

Elsewhere in the file is an example renaming `QQ^7` to V...



---

archive/issue_comments_083138.json:
```json
{
    "body": "Ah, I should have worked on a different project, but just couldn't.\nCurrently, I know the following:\n\n* There is a line `V = QQ^7` elsewhere in the same doctest\n* Sage stores free modules of some rank over some ring only once, see free_module.py/factory.pyx\n* so if `testname = ZZ^7`, then `testname.base_extend(QQ)` will refer to the same object as V before (!), albeit there is some \"weakref\" magic I don't understand\n* in this factory.pyx and weakref magic, the version number of Sage plays some role unclear to me (but at least there is some hint to from where the difference comes)\n* if the Sage version reads '4.4.2', then this object above has during the evalution in the doctest an attribute \"`__custom_name`\" set to the string \"V\", so this is why \"V\" is printed (as is clear from \"sage_object.pyx\", see `__repr__()` there)\n* after the *only* change making the Sage version to be '4.4.2.rc0' (note that the item after the last dot is not a number ...), then this object during evaluation of the doctest does not have this attribute \"`__custom_name`\" (direct evaluation now gives an AttributeError)\n\nIMPORTANT NOTE: If one takes Sage-4.4.2.alpha0, and just alters in version.py the Sage version to read something with numbers only (e.g. \"4.4.2\"), then the bug becomes visible! So the problem must be in one of the patches in between Sage-4.4.1 and Sage-4.4.2.alpha0 --- and was only \"shadowed\" by the version number ending with a string (see factory.pyx lines 8 - 14 why this might be relevant --- I do not really know, why this hurts ... possibly garbage collection/weakref somehow acting differently, since the string \"alpha0\" (or \"rc0\") *is* being referenced?)",
    "created_at": "2010-05-26T21:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83138",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Ah, I should have worked on a different project, but just couldn't.
Currently, I know the following:

* There is a line `V = QQ^7` elsewhere in the same doctest
* Sage stores free modules of some rank over some ring only once, see free_module.py/factory.pyx
* so if `testname = ZZ^7`, then `testname.base_extend(QQ)` will refer to the same object as V before (!), albeit there is some "weakref" magic I don't understand
* in this factory.pyx and weakref magic, the version number of Sage plays some role unclear to me (but at least there is some hint to from where the difference comes)
* if the Sage version reads '4.4.2', then this object above has during the evalution in the doctest an attribute "`__custom_name`" set to the string "V", so this is why "V" is printed (as is clear from "sage_object.pyx", see `__repr__()` there)
* after the *only* change making the Sage version to be '4.4.2.rc0' (note that the item after the last dot is not a number ...), then this object during evaluation of the doctest does not have this attribute "`__custom_name`" (direct evaluation now gives an AttributeError)

IMPORTANT NOTE: If one takes Sage-4.4.2.alpha0, and just alters in version.py the Sage version to read something with numbers only (e.g. "4.4.2"), then the bug becomes visible! So the problem must be in one of the patches in between Sage-4.4.1 and Sage-4.4.2.alpha0 --- and was only "shadowed" by the version number ending with a string (see factory.pyx lines 8 - 14 why this might be relevant --- I do not really know, why this hurts ... possibly garbage collection/weakref somehow acting differently, since the string "alpha0" (or "rc0") *is* being referenced?)



---

archive/issue_comments_083139.json:
```json
{
    "body": "Well, I can tell you _some_ of what's going on, but I don't know the whole story. First, here's an easy band-aid that doesn't fix the problem, but covers it up: in the doctest block for `rename` (around line 4440), add an extra doctest that changes the name back to the appropriate thing.\n\nHere are some interesting facts:\n\n* the failure is coming from the code around line 4440, with the call to `V.rename('V')`. (Someone pointed this out above.) Sage knows that there's only one vector space over `QQ` of dimension 7, so it's keeping the same object around and returning it in both cases -- but it's been renamed in one case, so that shows up in the other one.\n* running `sage -t -verbose free_module.py` shows that even though the `rename` doctest comes later in the file than the `base_extend` one, it actually gets run before. This is because the generated functions get their doctests run in alphabetical order by name -- and `example_127` gets run before `example_23`. (Those are the numbers on my machine, anyway.) \n* this also hints as to why it has something to do  with the version: as Georg noted above, the version gets used as part of the key for objects handled by the factory code. \n* Deleting any whole doctest block above the `base_change` method seem to cover up the issue when running `sage -t`. \n* It doesn't always cover it up with `sage -t -verbose` -- there are cases where `sage -t` succeeds, but `sage -t -verbose` fails. That's really fishy.\n\nThat said, I **totally** can't explain the whole story. I'd love to take some time to debug this, but I just don't have time right now -- if it's still sitting in a week or so, I'll try and dig further. The first thing I'd try next is to print the version in the factory `__call__` method, see if we can spot where it's not the value we expect. I also have no idea why applying the patches from #6922 changes this. \n\nI can't wait for someone to get to the bottom of this. `;)`",
    "created_at": "2010-05-27T06:59:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83139",
    "user": "https://github.com/craigcitro"
}
```

Well, I can tell you _some_ of what's going on, but I don't know the whole story. First, here's an easy band-aid that doesn't fix the problem, but covers it up: in the doctest block for `rename` (around line 4440), add an extra doctest that changes the name back to the appropriate thing.

Here are some interesting facts:

* the failure is coming from the code around line 4440, with the call to `V.rename('V')`. (Someone pointed this out above.) Sage knows that there's only one vector space over `QQ` of dimension 7, so it's keeping the same object around and returning it in both cases -- but it's been renamed in one case, so that shows up in the other one.
* running `sage -t -verbose free_module.py` shows that even though the `rename` doctest comes later in the file than the `base_extend` one, it actually gets run before. This is because the generated functions get their doctests run in alphabetical order by name -- and `example_127` gets run before `example_23`. (Those are the numbers on my machine, anyway.) 
* this also hints as to why it has something to do  with the version: as Georg noted above, the version gets used as part of the key for objects handled by the factory code. 
* Deleting any whole doctest block above the `base_change` method seem to cover up the issue when running `sage -t`. 
* It doesn't always cover it up with `sage -t -verbose` -- there are cases where `sage -t` succeeds, but `sage -t -verbose` fails. That's really fishy.

That said, I **totally** can't explain the whole story. I'd love to take some time to debug this, but I just don't have time right now -- if it's still sitting in a week or so, I'll try and dig further. The first thing I'd try next is to print the version in the factory `__call__` method, see if we can spot where it's not the value we expect. I also have no idea why applying the patches from #6922 changes this. 

I can't wait for someone to get to the bottom of this. `;)`



---

archive/issue_comments_083140.json:
```json
{
    "body": "I can't really think of anything other than seemingly unrelated things affecting the garbage collector somehow... I think avoiding renaming an object used in a different doctest should be a safe solution. (Patch attached.)",
    "created_at": "2010-05-27T21:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83140",
    "user": "https://github.com/wjp"
}
```

I can't really think of anything other than seemingly unrelated things affecting the garbage collector somehow... I think avoiding renaming an object used in a different doctest should be a safe solution. (Patch attached.)



---

archive/issue_comments_083141.json:
```json
{
    "body": "Attachment [9003_rename_doctest.patch](tarball://root/attachments/some-uuid/ticket9003/9003_rename_doctest.patch) by @wjp created at 2010-05-27 21:56:49",
    "created_at": "2010-05-27T21:56:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83141",
    "user": "https://github.com/wjp"
}
```

Attachment [9003_rename_doctest.patch](tarball://root/attachments/some-uuid/ticket9003/9003_rename_doctest.patch) by @wjp created at 2010-05-27 21:56:49



---

archive/issue_comments_083142.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-27T21:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83142",
    "user": "https://github.com/wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083143.json:
```json
{
    "body": "Replying to [comment:22 wjp]:\n> I can't really think of anything other than seemingly unrelated things affecting the garbage collector somehow... I think avoiding renaming an object used in a different doctest should be a safe solution. (Patch attached.)\n\nDoes this solve the problem, or just its symptoms? ;-)\n\nI wonder if only the doctesting is affected...",
    "created_at": "2010-05-27T22:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83143",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:22 wjp]:
> I can't really think of anything other than seemingly unrelated things affecting the garbage collector somehow... I think avoiding renaming an object used in a different doctest should be a safe solution. (Patch attached.)

Does this solve the problem, or just its symptoms? ;-)

I wonder if only the doctesting is affected...



---

archive/issue_comments_083144.json:
```json
{
    "body": "If I understand it correctly, the only reason that it works on other systems is that the garbage collector deletes an object (`QQ^7`) between the two doctests. I think it would be safer not to depend on that.",
    "created_at": "2010-05-27T22:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83144",
    "user": "https://github.com/wjp"
}
```

If I understand it correctly, the only reason that it works on other systems is that the garbage collector deletes an object (`QQ^7`) between the two doctests. I think it would be safer not to depend on that.



---

archive/issue_comments_083145.json:
```json
{
    "body": "Replying to [comment:25 wjp]:\n> If I understand it correctly, the only reason that it works on other systems is that the garbage collector deletes an object (`QQ^7`) between the two doctests. I think it would be safer not to depend on that.\n\nActually, I don't know that it's the garbage collector:\n\n\n```\nsage: V = QQ^7\nsage: V.rename('foo')\nsage: V\nfoo\nsage: del V\nsage: import gc\nsage: gc.collect()\n54\nsage: QQ^7\nfoo\n```\n\n\nOf course, maybe I'm tricking myself because something else is holding onto a non-weakref that prevents the stored `V` from being collected?\n\nThat said, I think the answer to Leif's question above is \"yes and no.\" I think this *will* fix the issue for now, which is good. On the other hand, I think there still are weirdnesses lurking that should be investigated ... or at least explained to me if they're already understood. `;)`\n\nIt can't _just_ be the garbage collector -- the fact that the version strings were futzing with it means that it somehow has to intersect with weirdness related to pickling ... maybe because of the pickle jar? In any event, there's some weird behavior, and we should open a ticket to ferret out that weird behavior. Once that's open, I say positive review and merge Willem Jan's patch ...",
    "created_at": "2010-05-27T22:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83145",
    "user": "https://github.com/craigcitro"
}
```

Replying to [comment:25 wjp]:
> If I understand it correctly, the only reason that it works on other systems is that the garbage collector deletes an object (`QQ^7`) between the two doctests. I think it would be safer not to depend on that.

Actually, I don't know that it's the garbage collector:


```
sage: V = QQ^7
sage: V.rename('foo')
sage: V
foo
sage: del V
sage: import gc
sage: gc.collect()
54
sage: QQ^7
foo
```


Of course, maybe I'm tricking myself because something else is holding onto a non-weakref that prevents the stored `V` from being collected?

That said, I think the answer to Leif's question above is "yes and no." I think this *will* fix the issue for now, which is good. On the other hand, I think there still are weirdnesses lurking that should be investigated ... or at least explained to me if they're already understood. `;)`

It can't _just_ be the garbage collector -- the fact that the version strings were futzing with it means that it somehow has to intersect with weirdness related to pickling ... maybe because of the pickle jar? In any event, there's some weird behavior, and we should open a ticket to ferret out that weird behavior. Once that's open, I say positive review and merge Willem Jan's patch ...



---

archive/issue_comments_083146.json:
```json
{
    "body": "I think the ipython/sage output history might still be holding a ref there:\n\n\n```\nsage: V = QQ^7\nsage: V.rename('foo')\nsage: del V\nsage: import gc\nsage: gc.collect()\n60\nsage: QQ^7\nVector space of dimension 7 over Rational Field\nsage: V = QQ^7\nsage: V.rename('foo')\nsage: V\nfoo\nsage: import gc\nsage: gc.collect()\n9\nsage: QQ^7\nfoo\n```\n\n\n(I left out printing V the first time.)\n\n\nI don't understand the impact of the version either... It might just be affecting the GC algorithm in some subtle way due to different memory usage, but I realize that's next to impossible to verify.",
    "created_at": "2010-05-27T22:56:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83146",
    "user": "https://github.com/wjp"
}
```

I think the ipython/sage output history might still be holding a ref there:


```
sage: V = QQ^7
sage: V.rename('foo')
sage: del V
sage: import gc
sage: gc.collect()
60
sage: QQ^7
Vector space of dimension 7 over Rational Field
sage: V = QQ^7
sage: V.rename('foo')
sage: V
foo
sage: import gc
sage: gc.collect()
9
sage: QQ^7
foo
```


(I left out printing V the first time.)


I don't understand the impact of the version either... It might just be affecting the GC algorithm in some subtle way due to different memory usage, but I realize that's next to impossible to verify.



---

archive/issue_comments_083147.json:
```json
{
    "body": "Replying to [comment:27 wjp]:\n> I think the ipython/sage output history might still be holding a ref there:\n> \n\nThat's right, I think there's an IPython variable called `Out` -- but deleting the reference in there doesn't do it once it's been printed ... apparently something else is holding one, too. \n\nEven still, though, it's printed by the doctests -- so if whoever is holding on to it is part of Python and not just IPython, we'd still hit the same issue.",
    "created_at": "2010-05-27T23:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83147",
    "user": "https://github.com/craigcitro"
}
```

Replying to [comment:27 wjp]:
> I think the ipython/sage output history might still be holding a ref there:
> 

That's right, I think there's an IPython variable called `Out` -- but deleting the reference in there doesn't do it once it's been printed ... apparently something else is holding one, too. 

Even still, though, it's printed by the doctests -- so if whoever is holding on to it is part of Python and not just IPython, we'd still hit the same issue.



---

archive/issue_comments_083148.json:
```json
{
    "body": "What is the status of this - does it need review, or need work (the latter seems indicated by the last few comments)?",
    "created_at": "2010-06-14T13:58:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83148",
    "user": "https://github.com/kcrisman"
}
```

What is the status of this - does it need review, or need work (the latter seems indicated by the last few comments)?



---

archive/issue_comments_083149.json:
```json
{
    "body": "As far as I'm concerned it still needs review.\n\nRight now in one doctest `QQ^7` is renamed, and in another doctest we depend on `QQ^7` having its original name. I don't have any further ideas on how to exactly track down which aspect of the GC is responsible for the different behaviour on different systems, but at this point I have no reason to suspect a bug. Not depending on the GC behaviour at all by replacing one of the `QQ^7` by `QQ^37` as the patch I attached does still sounds like a good solution to me.",
    "created_at": "2010-06-14T14:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83149",
    "user": "https://github.com/wjp"
}
```

As far as I'm concerned it still needs review.

Right now in one doctest `QQ^7` is renamed, and in another doctest we depend on `QQ^7` having its original name. I don't have any further ideas on how to exactly track down which aspect of the GC is responsible for the different behaviour on different systems, but at this point I have no reason to suspect a bug. Not depending on the GC behaviour at all by replacing one of the `QQ^7` by `QQ^37` as the patch I attached does still sounds like a good solution to me.



---

archive/issue_comments_083150.json:
```json
{
    "body": "Attachment [trac_9003_rename_doctest_alternate.patch](tarball://root/attachments/some-uuid/ticket9003/trac_9003_rename_doctest_alternate.patch) by GeorgSWeber created at 2010-06-14 18:38:26\n\napply instead (or additionally, but the first patch is not needed anymore with this one)",
    "created_at": "2010-06-14T18:38:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83150",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [trac_9003_rename_doctest_alternate.patch](tarball://root/attachments/some-uuid/ticket9003/trac_9003_rename_doctest_alternate.patch) by GeorgSWeber created at 2010-06-14 18:38:26

apply instead (or additionally, but the first patch is not needed anymore with this one)



---

archive/issue_comments_083151.json:
```json
{
    "body": "I think we all agree that a workaround will do, since finding the \"real\" root cause is both too difficult, and not bringing an advantage w.r.t. making the Sage Library more bugfree (since the root cause is not located within Sage).\n\nBoth patches are workarounds. But I feel that the latter from me is a bit closer to the root cause. Actually, the \"rename\" feature is used a handful of times in the `free_module.py` file, and any of these occurences had (before the latter patch) the potential to cause the failure seen (or a very similar one).\n \nI tested that with the latter patch, the former is not needed anymore.",
    "created_at": "2010-06-14T18:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83151",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

I think we all agree that a workaround will do, since finding the "real" root cause is both too difficult, and not bringing an advantage w.r.t. making the Sage Library more bugfree (since the root cause is not located within Sage).

Both patches are workarounds. But I feel that the latter from me is a bit closer to the root cause. Actually, the "rename" feature is used a handful of times in the `free_module.py` file, and any of these occurences had (before the latter patch) the potential to cause the failure seen (or a very similar one).
 
I tested that with the latter patch, the former is not needed anymore.



---

archive/issue_comments_083152.json:
```json
{
    "body": "> Both patches are workarounds. But I feel that the latter from me is a bit closer to the root cause. Actually, the \"rename\" feature is used a handful of times in the `free_module.py` file, and any of these occurences had (before the latter patch) the potential to cause the failure seen (or a very similar one).\n\nThis seems reasonable.  I'll try to check this later tonight.",
    "created_at": "2010-08-05T20:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83152",
    "user": "https://github.com/kcrisman"
}
```

> Both patches are workarounds. But I feel that the latter from me is a bit closer to the root cause. Actually, the "rename" feature is used a handful of times in the `free_module.py` file, and any of these occurences had (before the latter patch) the potential to cause the failure seen (or a very similar one).

This seems reasonable.  I'll try to check this later tonight.



---

archive/issue_comments_083153.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-06T00:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83153",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083154.json:
```json
{
    "body": "I feel like I can give this positive review based on the patch and passing tests, but my machine this occurred on only has room for one Sage install at a time, and I now have 4.5.2.rc1 rather than 4.4.2, and this failure does not occur even before the patch.  What do you all think?  \n\nMaybe we would need to make this change in all such places, of which there are a fair number (esp. in `categories/modules_with_basis.py` and `modules/free_quadratic_module.py`; in `modular/abvar/abvar_ambient_jacobian.py` they clear the cache.\n\nIncidentally, `reset_name()` is not doctested, and neither are a couple of other things in `structure/sage_object.pyx` related to this.  I don't think it's worth opening a ticket, though, since we still need several thousand functions doctested ;)\n\nThe author/reviewer things I filled in are just my best approximation; if someone disagrees, they can add themselves.",
    "created_at": "2010-08-06T00:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83154",
    "user": "https://github.com/kcrisman"
}
```

I feel like I can give this positive review based on the patch and passing tests, but my machine this occurred on only has room for one Sage install at a time, and I now have 4.5.2.rc1 rather than 4.4.2, and this failure does not occur even before the patch.  What do you all think?  

Maybe we would need to make this change in all such places, of which there are a fair number (esp. in `categories/modules_with_basis.py` and `modules/free_quadratic_module.py`; in `modular/abvar/abvar_ambient_jacobian.py` they clear the cache.

Incidentally, `reset_name()` is not doctested, and neither are a couple of other things in `structure/sage_object.pyx` related to this.  I don't think it's worth opening a ticket, though, since we still need several thousand functions doctested ;)

The author/reviewer things I filled in are just my best approximation; if someone disagrees, they can add themselves.



---

archive/issue_comments_083155.json:
```json
{
    "body": "Should I merge *only* [attachment:trac_9003_rename_doctest_alternate.patch]?",
    "created_at": "2010-08-07T05:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83155",
    "user": "https://github.com/qed777"
}
```

Should I merge *only* [attachment:trac_9003_rename_doctest_alternate.patch]?



---

archive/issue_comments_083156.json:
```json
{
    "body": "Yes, only the alternate patch is fine.",
    "created_at": "2010-08-07T09:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83156",
    "user": "https://github.com/wjp"
}
```

Yes, only the alternate patch is fine.



---

archive/issue_events_009157.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-08-09T09:49:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9003#event-9157"
}
```



---

archive/issue_comments_083157.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9003",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9003#issuecomment-83157",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
