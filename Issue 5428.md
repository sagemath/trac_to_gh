# Issue 5428: Doctest failure in devel/sage/doc/en/bordeaux_2008/method_of_graphs.rst

archive/issues_005428.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  georgsweber @williamstein\n\nJohn Palmieri reported this first in sage-3.4.alpha. I is still here\nin rc0:\n\n\n\n```\nFile \"/home/jaap/downloads/sage-3.4.alpha0/devel/sage/doc/en/bordeaux_2008/method_of_graphs.rst\", line 25:\n    sage: t2 = ModularSymbols(389,sign=1).hecke_matrix(2); t2[0]\nExpected:\n    (3, 0, -1, 0, 0, -1, 1, 0, 0, 0, 1, -1, 0, 0, 1, 1, 0, 1,\n     -1, 1, -1, 1, 0, 0, -1, 0, 0, 0, 0, 0, 1, -1, -1)\nGot:\n    (3, 0, -1, 0, 0, -1, 1, 0, 0, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0, 1, -1, 1, -1, 1, 0, 0, 0, 0, 0, 0, 1, -1, -1)\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_0\n\n```\n\n\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/5428\n\n",
    "created_at": "2009-03-03T13:01:22Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "Doctest failure in devel/sage/doc/en/bordeaux_2008/method_of_graphs.rst",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5428",
    "user": "https://github.com/jaapspies"
}
```
Assignee: mabshoff

CC:  georgsweber @williamstein

John Palmieri reported this first in sage-3.4.alpha. I is still here
in rc0:



```
File "/home/jaap/downloads/sage-3.4.alpha0/devel/sage/doc/en/bordeaux_2008/method_of_graphs.rst", line 25:
    sage: t2 = ModularSymbols(389,sign=1).hecke_matrix(2); t2[0]
Expected:
    (3, 0, -1, 0, 0, -1, 1, 0, 0, 0, 1, -1, 0, 0, 1, 1, 0, 1,
     -1, 1, -1, 1, 0, 0, -1, 0, 0, 0, 0, 0, 1, -1, -1)
Got:
    (3, 0, -1, 0, 0, -1, 1, 0, 0, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0, 1, -1, 1, -1, 1, 0, 0, 0, 0, 0, 0, 1, -1, -1)
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_0

```



Jaap

Issue created by migration from https://trac.sagemath.org/ticket/5428





---

archive/issue_comments_041907.json:
```json
{
    "body": "In sage-3.3 we have:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.3, Release Date: 2009-02-21                         |\n| Type notebook() for the GUI, and license() for information.        |\nsage: t2 = ModularSymbols(389,sign=1).hecke_matrix(2); t2[0]\n (3, 0, -1, 0, 0, -1, 1, 0, 0, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0, 1, -1, 1, -1, 1, 0, 0, 0, 0, 0, 0, 1, -1, -1)\n\n\n```\n\n\nversus\n\n\n```\n(3, 0, -1, 0, 0, -1, 1, 0, 0, 0, 1, -1, 0, 0, 1, 1, 0, 1, -1, 1, -1, 1, 0, 0, -1, 0, 0, 0, 0, 0, 1, -1, -1)\n```\n\n\nin sage-3.4.xxx\n\n\nJaap",
    "created_at": "2009-03-03T13:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41907",
    "user": "https://github.com/jaapspies"
}
```

In sage-3.3 we have:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.3, Release Date: 2009-02-21                         |
| Type notebook() for the GUI, and license() for information.        |
sage: t2 = ModularSymbols(389,sign=1).hecke_matrix(2); t2[0]
 (3, 0, -1, 0, 0, -1, 1, 0, 0, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0, 1, -1, 1, -1, 1, 0, 0, 0, 0, 0, 0, 1, -1, -1)


```


versus


```
(3, 0, -1, 0, 0, -1, 1, 0, 0, 0, 1, -1, 0, 0, 1, 1, 0, 1, -1, 1, -1, 1, 0, 0, -1, 0, 0, 0, 0, 0, 1, -1, -1)
```


in sage-3.4.xxx


Jaap



---

archive/issue_comments_041908.json:
```json
{
    "body": "I'm more than a bit baffled. I have looked twice now over the patches that went into Sage in between 3.3 and 3.4.alpha0, but still I have no idea why this change would possibly be caused by any of them.\n\nThe least unplausible one (for me) is the patch about NTL (#5340) --- but I would not really believe that until I see it, i.e. testing with removing/reapplying it. (And I'm currently busy with other things.)",
    "created_at": "2009-03-03T19:45:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41908",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

I'm more than a bit baffled. I have looked twice now over the patches that went into Sage in between 3.3 and 3.4.alpha0, but still I have no idea why this change would possibly be caused by any of them.

The least unplausible one (for me) is the patch about NTL (#5340) --- but I would not really believe that until I see it, i.e. testing with removing/reapplying it. (And I'm currently busy with other things.)



---

archive/issue_comments_041909.json:
```json
{
    "body": "Replying to [comment:3 GeorgSWeber]:\n\nHi Georg,\n\n> I'm more than a bit baffled. I have looked twice now over the patches that went into Sage in between 3.3 and 3.4.alpha0, but still I have no idea why this change would possibly be caused by any of them.\n\nThe issue exists in both 3.3 and 3.4.alpha0/rc0 - the Bordeaux document was written in October 2008 by William and never doctested until the ReST patches. \n\n> The least unplausible one (for me) is the patch about NTL (#5340) --- but I would not really believe that until I see it, i.e. testing with removing/reapplying it. (And I'm currently busy with other things.) \n\nThat patch isn't the cause. It would be interesting to see if it is a generic 32 vs. 64 bit problem or 32 bit linux specific.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-04T04:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41909",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:3 GeorgSWeber]:

Hi Georg,

> I'm more than a bit baffled. I have looked twice now over the patches that went into Sage in between 3.3 and 3.4.alpha0, but still I have no idea why this change would possibly be caused by any of them.

The issue exists in both 3.3 and 3.4.alpha0/rc0 - the Bordeaux document was written in October 2008 by William and never doctested until the ReST patches. 

> The least unplausible one (for me) is the patch about NTL (#5340) --- but I would not really believe that until I see it, i.e. testing with removing/reapplying it. (And I'm currently busy with other things.) 

That patch isn't the cause. It would be interesting to see if it is a generic 32 vs. 64 bit problem or 32 bit linux specific.

Cheers,

Michael



---

archive/issue_comments_041910.json:
```json
{
    "body": "Thanks Michael,\n\ngiven that information seems to make the patch trivial. William and Craig did some optimization in calculating the underlying P1List for modular symbols (trac #3502 I strongly guess), now using some caching of xgcd's and such.\n\nFrom what I remember in the code, this hardly could be a 32bit/64bit issue anyway.\n\nSo the patch attached just is the \"new\" correct answer.",
    "created_at": "2009-03-04T20:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41910",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Thanks Michael,

given that information seems to make the patch trivial. William and Craig did some optimization in calculating the underlying P1List for modular symbols (trac #3502 I strongly guess), now using some caching of xgcd's and such.

From what I remember in the code, this hardly could be a 32bit/64bit issue anyway.

So the patch attached just is the "new" correct answer.



---

archive/issue_comments_041911.json:
```json
{
    "body": "Hmmm,\n\nI was too fast and just now re-read the description from Jaap, where he explicitly posted a Sage 3.3 session with the \"other\" answer.",
    "created_at": "2009-03-04T20:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41911",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Hmmm,

I was too fast and just now re-read the description from Jaap, where he explicitly posted a Sage 3.3 session with the "other" answer.



---

archive/issue_comments_041912.json:
```json
{
    "body": "OK,\n\nto add more confusion: I re-re-read what Jaap posted above and looked again at the doctest failure with vanilla 3.4.rc0:\n\n* the Bordeaux October talk shows answer \"A\"\n* my computation with Sage 3.4.rc0 shows answer \"B\"\n* Jaap's computation with Sage 3.3 shows answer \"B\"\n* my own computation with Sage 3.3 shows answer \"B\"\n* the patch attached implements the new answer \"B\"\n\nSo it seems that only Jaap's description did mislead me, and the patch is good.",
    "created_at": "2009-03-04T20:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41912",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

OK,

to add more confusion: I re-re-read what Jaap posted above and looked again at the doctest failure with vanilla 3.4.rc0:

* the Bordeaux October talk shows answer "A"
* my computation with Sage 3.4.rc0 shows answer "B"
* Jaap's computation with Sage 3.3 shows answer "B"
* my own computation with Sage 3.3 shows answer "B"
* the patch attached implements the new answer "B"

So it seems that only Jaap's description did mislead me, and the patch is good.



---

archive/issue_comments_041913.json:
```json
{
    "body": "I don't think the patch will do:\n\nOn sage.math, 64 bits:\n\n```\njsp@sage:/scratch/jsp/sage-3.4.alpha0$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: t2 = ModularSymbols(389,sign=1).hecke_matrix(2); t2[0]\n(3, 0, -1, 0, 0, -1, 1, 0, 0, 0, 1, -1, 0, 0, 1, 1, 0, 1, -1, 1, -1, 1, 0, 0, -1, 0, 0, 0, 0, 0, 1, -1, -1)\n| Sage Version 3.4.rc0, Release Date: 2009-03-02                     |\n| Type notebook() for the GUI, and license() for information.        |\n```\n\n\nOn Fedora 9, 32 bits:\n\n\n```\n[jaap@paix sage-3.4.alpha0]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 3.4.rc0, Release Date: 2009-03-02                     |\n| Type notebook() for the GUI, and license() for information.        |\nsage: t2 = ModularSymbols(389,sign=1).hecke_matrix(2); t2[0]\n (3, 0, -1, 0, 0, -1, 1, 0, 0, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0, 1, -1, 1, -1, 1, 0, 0, 0, 0, 0, 0, 1, -1, -1)\n\n```\n\n\n\nCan't explain the different output.\n\nJaap",
    "created_at": "2009-03-04T20:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41913",
    "user": "https://github.com/jaapspies"
}
```

I don't think the patch will do:

On sage.math, 64 bits:

```
jsp@sage:/scratch/jsp/sage-3.4.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: t2 = ModularSymbols(389,sign=1).hecke_matrix(2); t2[0]
(3, 0, -1, 0, 0, -1, 1, 0, 0, 0, 1, -1, 0, 0, 1, 1, 0, 1, -1, 1, -1, 1, 0, 0, -1, 0, 0, 0, 0, 0, 1, -1, -1)
| Sage Version 3.4.rc0, Release Date: 2009-03-02                     |
| Type notebook() for the GUI, and license() for information.        |
```


On Fedora 9, 32 bits:


```
[jaap@paix sage-3.4.alpha0]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.4.rc0, Release Date: 2009-03-02                     |
| Type notebook() for the GUI, and license() for information.        |
sage: t2 = ModularSymbols(389,sign=1).hecke_matrix(2); t2[0]
 (3, 0, -1, 0, 0, -1, 1, 0, 0, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0, 1, -1, 1, -1, 1, 0, 0, 0, 0, 0, 0, 1, -1, -1)

```



Can't explain the different output.

Jaap



---

archive/issue_comments_041914.json:
```json
{
    "body": "Hi Jaap,\n\nI just re-re-re-read the posts on sage-devel --- there Rob Beezer reported *not* to have this doctest failure on his 64-bit box, but to see it on his 32bit box.\n\nAnd yes, sigh, I just did the calculation, too, on sage.math (it's 64bit --- or 256bit :-)) and you are right. I'll redo the patch in a minute, on the assumption it is 32 bit versus 64 bit.",
    "created_at": "2009-03-04T20:50:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41914",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Hi Jaap,

I just re-re-re-read the posts on sage-devel --- there Rob Beezer reported *not* to have this doctest failure on his 64-bit box, but to see it on his 32bit box.

And yes, sigh, I just did the calculation, too, on sage.math (it's 64bit --- or 256bit :-)) and you are right. I'll redo the patch in a minute, on the assumption it is 32 bit versus 64 bit.



---

archive/issue_comments_041915.json:
```json
{
    "body": "Attachment [trac_5428.patch](tarball://root/attachments/some-uuid/ticket5428/trac_5428.patch) by GeorgSWeber created at 2009-03-04 21:05:44\n\ntested against 3.4.rc0 on 32-bit (OS X)",
    "created_at": "2009-03-04T21:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41915",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [trac_5428.patch](tarball://root/attachments/some-uuid/ticket5428/trac_5428.patch) by GeorgSWeber created at 2009-03-04 21:05:44

tested against 3.4.rc0 on 32-bit (OS X)



---

archive/issue_comments_041916.json:
```json
{
    "body": "I doubt this is the fix. AFAIK no other modular form doctest has 32 vs. 64 bit specific result, so this fix might not address the root cause.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-04T21:09:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41916",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I doubt this is the fix. AFAIK no other modular form doctest has 32 vs. 64 bit specific result, so this fix might not address the root cause.

Cheers,

Michael



---

archive/issue_comments_041917.json:
```json
{
    "body": "Matter-of-factly, the following:\n\n```\nModularSymbols(389,sign=1).basis()\n```\n\ngives different output on 32 bit OS X versus 64 bit sage.math. It seems to be consistent w.r.t. architecture , though.\n\nThe modular symbols code is old, and definitely should have more examples and doctests. Especially the above one should be added, if only to show clearly that an architecture dependency is there. The doctests that are there do focus on the important stuff, not on how the modular symbols bases are enumerated, or the explicit matrices of Hecke operators. (But e.g. on characteristic polynomials of the Hecke operators and their factorization instead --- which are *not* architecture dependent, as I just did check!) It would be interesting if the Cremona EC-lib modular symbol implementation (also in Sage) yields the same architecture dependency.\n\nI admit I don't know yet where the architecture dependency actually creeps in.\n\nBut I believe what I see, and do think the (current) patch does its job.",
    "created_at": "2009-03-04T21:38:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41917",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Matter-of-factly, the following:

```
ModularSymbols(389,sign=1).basis()
```

gives different output on 32 bit OS X versus 64 bit sage.math. It seems to be consistent w.r.t. architecture , though.

The modular symbols code is old, and definitely should have more examples and doctests. Especially the above one should be added, if only to show clearly that an architecture dependency is there. The doctests that are there do focus on the important stuff, not on how the modular symbols bases are enumerated, or the explicit matrices of Hecke operators. (But e.g. on characteristic polynomials of the Hecke operators and their factorization instead --- which are *not* architecture dependent, as I just did check!) It would be interesting if the Cremona EC-lib modular symbol implementation (also in Sage) yields the same architecture dependency.

I admit I don't know yet where the architecture dependency actually creeps in.

But I believe what I see, and do think the (current) patch does its job.



---

archive/issue_comments_041918.json:
```json
{
    "body": "Hooray,\n\nI just checked that the documentation still builds fine (it does). I think this is the first time I did this after submitting a patch. I do love the new ReST documentation!\n\n(But cloning did not copy over all the html files and such docbuild output, so there is potential left for further polishing.)",
    "created_at": "2009-03-04T21:50:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41918",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Hooray,

I just checked that the documentation still builds fine (it does). I think this is the first time I did this after submitting a patch. I do love the new ReST documentation!

(But cloning did not copy over all the html files and such docbuild output, so there is potential left for further polishing.)



---

archive/issue_comments_041919.json:
```json
{
    "body": "I tracked down some architecture-dependence in sage.modular when I was working on randstate.pyx (trying to remove \"# random\"), but then I never got around to submitting the patch.  Perhaps this is the problem?\n\nUntested, very old, possibly no-longer-applies patch chunk:\n\n```\n--- a/sage/modular/modsym/relation_matrix.py\tSat Mar 29 12:28:22 2008 -0700\n+++ b/sage/modular/modsym/relation_matrix.py\tSun Mar 30 07:09:50 2008 -0700\n@@ -391,7 +391,8 @@ def sparse_2term_quotient(rels, n, F):\n     ZERO = F(0)\n     coef = [ONE for i in xrange(n)] \n     related_to_me = [[] for i in xrange(n)]\n-    for v0, v1 in rels:\n+    # Sort rels so that we get the same answer on 32-bit and 64-bit platforms.\n+    for v0, v1 in sorted(rels):\n         c0 = coef[v0[0]] * F(v0[1])\n         c1 = coef[v1[0]] * F(v1[1])\n         # Mod out by the relation \n```\n\n\nIterating through a set uses an order that depends on the `__hash__`, and `__hash__` values are different between 32-bit and 64-bit platforms.  I think I remember that sorting rels fixed that.  (I don't know what the performance implications are, but probably not much; sorting is pretty fast.)",
    "created_at": "2009-03-04T23:55:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41919",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I tracked down some architecture-dependence in sage.modular when I was working on randstate.pyx (trying to remove "# random"), but then I never got around to submitting the patch.  Perhaps this is the problem?

Untested, very old, possibly no-longer-applies patch chunk:

```
--- a/sage/modular/modsym/relation_matrix.py	Sat Mar 29 12:28:22 2008 -0700
+++ b/sage/modular/modsym/relation_matrix.py	Sun Mar 30 07:09:50 2008 -0700
@@ -391,7 +391,8 @@ def sparse_2term_quotient(rels, n, F):
     ZERO = F(0)
     coef = [ONE for i in xrange(n)] 
     related_to_me = [[] for i in xrange(n)]
-    for v0, v1 in rels:
+    # Sort rels so that we get the same answer on 32-bit and 64-bit platforms.
+    for v0, v1 in sorted(rels):
         c0 = coef[v0[0]] * F(v0[1])
         c1 = coef[v1[0]] * F(v1[1])
         # Mod out by the relation 
```


Iterating through a set uses an order that depends on the `__hash__`, and `__hash__` values are different between 32-bit and 64-bit platforms.  I think I remember that sorting rels fixed that.  (I don't know what the performance implications are, but probably not much; sorting is pretty fast.)



---

archive/issue_comments_041920.json:
```json
{
    "body": "Replying to [comment:13 cwitty]:\n> I tracked down some architecture-dependence in sage.modular when I was working on randstate.pyx (trying to remove \"# random\"), but then I never got around to submitting the patch.  Perhaps this is the problem?\n> \n> Untested, very old, possibly no-longer-applies patch chunk:\n\nApplying this \"patch\" introduced a ton of test failures all over the place.\n\nJaap",
    "created_at": "2009-03-05T18:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41920",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:13 cwitty]:
> I tracked down some architecture-dependence in sage.modular when I was working on randstate.pyx (trying to remove "# random"), but then I never got around to submitting the patch.  Perhaps this is the problem?
> 
> Untested, very old, possibly no-longer-applies patch chunk:

Applying this "patch" introduced a ton of test failures all over the place.

Jaap



---

archive/issue_comments_041921.json:
```json
{
    "body": "I don't see any way that this change could break the algorithm, so I'm guessing that these test failures are changing from one mathematically-correct answer to another mathematically-correct answer.  (But this should definitely be checked by somebody who understands the mathematics.)\n\nI'm adding wstein to the CC list on the theory that he may have written the original code.  (The code is present in the very first revision that got checked in to mercurial, so version history doesn't say who wrote it.)",
    "created_at": "2009-03-05T18:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41921",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I don't see any way that this change could break the algorithm, so I'm guessing that these test failures are changing from one mathematically-correct answer to another mathematically-correct answer.  (But this should definitely be checked by somebody who understands the mathematics.)

I'm adding wstein to the CC list on the theory that he may have written the original code.  (The code is present in the very first revision that got checked in to mercurial, so version history doesn't say who wrote it.)



---

archive/issue_comments_041922.json:
```json
{
    "body": "Replying to [comment:15 cwitty]:\n> I don't see any way that this change could break the algorithm, so I'm guessing that these test failures are changing from one mathematically-correct answer to another mathematically-correct answer.  (But this should definitely be checked by somebody who understands the mathematics.)\n> \n> I'm adding wstein to the CC list on the theory that he may have written the original code.  (The code is present in the very first revision that got checked in to mercurial, so version history doesn't say who wrote it.)\n\n\nI saw some weird results in here:\n\n\n\n```\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  \"devel/sage/doc/en/constructions/modular_forms.rst\"\n\tsage -t  \"devel/sage/doc/en/bordeaux_2008/method_of_graphs.rst\"\n\tsage -t  \"devel/sage/doc/en/bordeaux_2008/birds_other.rst\"\n\tsage -t  \"devel/sage/sage/modular/cusps.py\"\n\tsage -t  \"devel/sage/sage/modular/modsym/space.py\"\n\tsage -t  \"devel/sage/sage/modular/modsym/heilbronn.pyx\"\n\tsage -t  \"devel/sage/sage/modular/modsym/boundary.py\"\n\tsage -t  \"devel/sage/sage/modular/modsym/ambient.py\"\n\tsage -t  \"devel/sage/sage/modular/modsym/hecke_operator.py\"\n\tsage -t  \"devel/sage/sage/modular/modform/numerical.py\"\n\tsage -t  \"devel/sage/sage/modular/hecke/ambient_module.py\"\n\tsage -t  \"devel/sage/sage/modular/hecke/module.py\"\n\tsage -t  \"devel/sage/sage/modular/abvar/abvar.py\"\n\tsage -t  \"devel/sage/sage/modular/abvar/homology.py\"\n\tsage -t  \"devel/sage/sage/modular/abvar/cuspidal_subgroup.py\"\n\tsage -t  \"devel/sage/sage/modular/abvar/finite_subgroup.py\"\n\tsage -t  \"devel/sage/sage/matrix/matrix_integer_dense.pyx\"\n\tsage -t  \"devel/sage/sage/matrix/matrix2.pyx\"\n\tsage -t  \"devel/sage/sage/schemes/elliptic_curves/padic_lseries.py\"\n\tsage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py\"\n\tsage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\"\nTotal time for all tests: 2885.1 seconds\nPlease see /scratch/jsp/sage-3.4.alpha0/tmp/test.log for the complete log from this test.\njsp@sage:/scratch/jsp/sage-3.4.alpha0$ \n```\n\n\n\nJaap",
    "created_at": "2009-03-05T19:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41922",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:15 cwitty]:
> I don't see any way that this change could break the algorithm, so I'm guessing that these test failures are changing from one mathematically-correct answer to another mathematically-correct answer.  (But this should definitely be checked by somebody who understands the mathematics.)
> 
> I'm adding wstein to the CC list on the theory that he may have written the original code.  (The code is present in the very first revision that got checked in to mercurial, so version history doesn't say who wrote it.)


I saw some weird results in here:



```
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage/doc/en/constructions/modular_forms.rst"
	sage -t  "devel/sage/doc/en/bordeaux_2008/method_of_graphs.rst"
	sage -t  "devel/sage/doc/en/bordeaux_2008/birds_other.rst"
	sage -t  "devel/sage/sage/modular/cusps.py"
	sage -t  "devel/sage/sage/modular/modsym/space.py"
	sage -t  "devel/sage/sage/modular/modsym/heilbronn.pyx"
	sage -t  "devel/sage/sage/modular/modsym/boundary.py"
	sage -t  "devel/sage/sage/modular/modsym/ambient.py"
	sage -t  "devel/sage/sage/modular/modsym/hecke_operator.py"
	sage -t  "devel/sage/sage/modular/modform/numerical.py"
	sage -t  "devel/sage/sage/modular/hecke/ambient_module.py"
	sage -t  "devel/sage/sage/modular/hecke/module.py"
	sage -t  "devel/sage/sage/modular/abvar/abvar.py"
	sage -t  "devel/sage/sage/modular/abvar/homology.py"
	sage -t  "devel/sage/sage/modular/abvar/cuspidal_subgroup.py"
	sage -t  "devel/sage/sage/modular/abvar/finite_subgroup.py"
	sage -t  "devel/sage/sage/matrix/matrix_integer_dense.pyx"
	sage -t  "devel/sage/sage/matrix/matrix2.pyx"
	sage -t  "devel/sage/sage/schemes/elliptic_curves/padic_lseries.py"
	sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py"
	sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
Total time for all tests: 2885.1 seconds
Please see /scratch/jsp/sage-3.4.alpha0/tmp/test.log for the complete log from this test.
jsp@sage:/scratch/jsp/sage-3.4.alpha0$ 
```



Jaap



---

archive/issue_comments_041923.json:
```json
{
    "body": "Oops, I had the wrong TRAC username when I tried to CC william...",
    "created_at": "2009-03-06T01:51:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41923",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Oops, I had the wrong TRAC username when I tried to CC william...



---

archive/issue_comments_041924.json:
```json
{
    "body": "> I'm adding wstein to the CC list on the theory that he may \n> have written the original code. \n\nI did write the code.  A big +1 to sorted(rels), even though that will mean changing lots of doctests.   That's definitely the right fix. \n\nI tried the change and ran doctests and the many failures are all consistent with making a specific change of basis like sorted rels would do.   So this is the right fix, but requires a lot of work to update all the doctests.  Somebody let me know when a patch is up so I can referee it :-)",
    "created_at": "2009-03-06T16:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41924",
    "user": "https://github.com/williamstein"
}
```

> I'm adding wstein to the CC list on the theory that he may 
> have written the original code. 

I did write the code.  A big +1 to sorted(rels), even though that will mean changing lots of doctests.   That's definitely the right fix. 

I tried the change and ran doctests and the many failures are all consistent with making a specific change of basis like sorted rels would do.   So this is the right fix, but requires a lot of work to update all the doctests.  Somebody let me know when a patch is up so I can referee it :-)



---

archive/issue_comments_041925.json:
```json
{
    "body": "Mmmh, using \"sorted(rels)\" instead of \"rels\" certainly points in the right direction. \n\nBut IMHO, the fix(es) should not be done inside \"sparse_2term_quotient(rels, n, F)\", where the first argument \"rels\" is processed, but way before in the calling functions.\n\nMore precisely, the function \"modS_relations(syms)\" should not do \"return rels\" but should do \"return sorted(rels)\", and in the function \"relation_matrix_wtk_g0(...)\" we should do \"rels = sorted(rels.update(modI_relations(syms, sign)))\", and possibly there are one or two other places more like this.\n\nBut could we not postpone this to a point release 3.4.x, and open another ticket for that?!? (The Bordeaux ReST file would have to be touched a second time, but that's trivial.)",
    "created_at": "2009-03-07T10:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41925",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Mmmh, using "sorted(rels)" instead of "rels" certainly points in the right direction. 

But IMHO, the fix(es) should not be done inside "sparse_2term_quotient(rels, n, F)", where the first argument "rels" is processed, but way before in the calling functions.

More precisely, the function "modS_relations(syms)" should not do "return rels" but should do "return sorted(rels)", and in the function "relation_matrix_wtk_g0(...)" we should do "rels = sorted(rels.update(modI_relations(syms, sign)))", and possibly there are one or two other places more like this.

But could we not postpone this to a point release 3.4.x, and open another ticket for that?!? (The Bordeaux ReST file would have to be touched a second time, but that's trivial.)



---

archive/issue_comments_041926.json:
```json
{
    "body": "Replying to [comment:19 GeorgSWeber]:\n\nHi Georg,\n\n> But could we not postpone this to a point release 3.4.x, and open another ticket for that?!? (The Bordeaux ReST file would have to be touched a second time, but that's trivial.)\n\nI talked to William about this: positive review for the workaround patch, please open another ticket for the above fixes so it will be sorted out later.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-08T06:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41926",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:19 GeorgSWeber]:

Hi Georg,

> But could we not postpone this to a point release 3.4.x, and open another ticket for that?!? (The Bordeaux ReST file would have to be touched a second time, but that's trivial.)

I talked to William about this: positive review for the workaround patch, please open another ticket for the above fixes so it will be sorted out later.

Cheers,

Michael



---

archive/issue_comments_041927.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-08T07:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41927",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005681.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-03-08T07:12:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5428#event-5681"
}
```



---

archive/issue_comments_041928.json:
```json
{
    "body": "Merged in Sage 3.4.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-08T07:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41928",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.rc1.

Cheers,

Michael



---

archive/issue_comments_041929.json:
```json
{
    "body": "The follow-up ticket is #5456.",
    "created_at": "2009-03-08T10:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5428#issuecomment-41929",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

The follow-up ticket is #5456.
