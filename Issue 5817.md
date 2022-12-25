# Issue 5817: Update FLINT to 1.2.5 (latest upstream release)

archive/issues_005817.json:
```json
{
    "body": "Assignee: mabshoff\n\n```\nI've release FLINT 1.2.5. This fixes a serious error that existed in\nzn_poly-0.8. Unbeknownst to me, David Harvey had already fixed this\nissue in zn_poly-0.9 but I had not realised that had been released,\ndue to him changing institutions and me not updating my link to his\nwebpage in my frequently visited tabs list. FLINT now uses zn_poly-0.9\nby default for polynomial arithmetic over Z/nZ in zmod_poly.\n\nThere is still an issue with z_factor which fails to factor some\nnumbers very rarely (it prints a message to say it has failed). Tom\nBoothby is working on a fix, and this should also speed up the\nfactorisation function noticeably.\n\nBill. \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5817\n\n",
    "created_at": "2009-04-18T23:20:28Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "Update FLINT to 1.2.5 (latest upstream release)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5817",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

```
I've release FLINT 1.2.5. This fixes a serious error that existed in
zn_poly-0.8. Unbeknownst to me, David Harvey had already fixed this
issue in zn_poly-0.9 but I had not realised that had been released,
due to him changing institutions and me not updating my link to his
webpage in my frequently visited tabs list. FLINT now uses zn_poly-0.9
by default for polynomial arithmetic over Z/nZ in zmod_poly.

There is still an issue with z_factor which fails to factor some
numbers very rarely (it prints a message to say it has failed). Tom
Boothby is working on a fix, and this should also speed up the
factorisation function noticeably.

Bill. 
```

Issue created by migration from https://trac.sagemath.org/ticket/5817





---

archive/issue_comments_045625.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-18T23:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45625",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045626.json:
```json
{
    "body": "While I am at it: Please also add this fix to make the check target work on OSX, too:\n\n```\ndiff -r fc2eb24f71a2 spkg-check\n--- a/spkg-check        Thu Apr 09 00:29:11 2009 -0400\n+++ b/spkg-check        Mon Apr 20 00:04:56 2009 -0700\n@@ -17,6 +17,11 @@\n    FLINT_TUNE=\" -fPIC -funroll-loops  \"\n fi\n \n+if [ `uname` = \"Darwin\" -a \"$SAGE64\" = \"yes\" ]; then\n+   echo \"64 bit MacIntel\"\n+   FLINT_TUNE=\" -fPIC -m64 -funroll-loops\"\n+fi\n+\n export FLINT_TUNE\n \n FLINT_GMP_INCLUDE_DIR=\"$SAGE_LOCAL\"/include/\n```\n\nCheers,\n\nMichael",
    "created_at": "2009-04-20T07:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45626",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

While I am at it: Please also add this fix to make the check target work on OSX, too:

```
diff -r fc2eb24f71a2 spkg-check
--- a/spkg-check        Thu Apr 09 00:29:11 2009 -0400
+++ b/spkg-check        Mon Apr 20 00:04:56 2009 -0700
@@ -17,6 +17,11 @@
    FLINT_TUNE=" -fPIC -funroll-loops  "
 fi
 
+if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
+   echo "64 bit MacIntel"
+   FLINT_TUNE=" -fPIC -m64 -funroll-loops"
+fi
+
 export FLINT_TUNE
 
 FLINT_GMP_INCLUDE_DIR="$SAGE_LOCAL"/include/
```

Cheers,

Michael



---

archive/issue_events_013657.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-30T08:13:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5817#event-13657"
}
```



---

archive/issue_comments_045627.json:
```json
{
    "body": "The spkg is at \n\n  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.2/rc0/flint-1.2.5.spkg\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T08:13:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45627",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg is at 

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.2/rc0/flint-1.2.5.spkg

Cheers,

Michael



---

archive/issue_events_013658.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-30T08:29:16Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5817#event-13658"
}
```



---

archive/issue_events_013659.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-30T08:29:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "milestone": "sage-4.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5817#event-13659"
}
```



---

archive/issue_comments_045628.json:
```json
{
    "body": "Ok, this spkg needs a patch to module_list.py due to header changes for zn_poly.h. Bumping it to 4.0.\n\nCheers,\n\nMcihael",
    "created_at": "2009-04-30T08:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45628",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, this spkg needs a patch to module_list.py due to header changes for zn_poly.h. Bumping it to 4.0.

Cheers,

Mcihael



---

archive/issue_comments_045629.json:
```json
{
    "body": "Fixed the issue with headers, but monsky still has a small problem:\n\n```\nsage -t -long devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.2.alpha0/devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py\", line 1562:\n    sage: B.det()                                               # long time\nExpected:\n    11 + 484*t^2 + 451*t^3 + O(t^4)\nGot:\n    245 + 240*t + 724*t^2 + 808*t^3 + O(t^4)\n**********************************************************************\n```\n\nThe spkg is now at http://sage.math.washington.edu/home/mabshoff/spkgs/flint-1.2.5.spkg\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T08:58:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45629",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed the issue with headers, but monsky still has a small problem:

```
sage -t -long devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py
**********************************************************************
File "/scratch/mabshoff/sage-3.4.2.alpha0/devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1562:
    sage: B.det()                                               # long time
Expected:
    11 + 484*t^2 + 451*t^3 + O(t^4)
Got:
    245 + 240*t + 724*t^2 + 808*t^3 + O(t^4)
**********************************************************************
```

The spkg is now at http://sage.math.washington.edu/home/mabshoff/spkgs/flint-1.2.5.spkg

Cheers,

Michael



---

archive/issue_comments_045630.json:
```json
{
    "body": "FYI: Turning off znpoly in FLINT makes the doctest pass.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T07:26:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45630",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

FYI: Turning off znpoly in FLINT makes the doctest pass.

Cheers,

Michael



---

archive/issue_comments_045631.json:
```json
{
    "body": "I couldn't build the spkg on linux/opteron. I tried vanilla sage 3.4.2 with spkg/standard/flint-1.2.4.p2.spkg replaced by flint-1.2.5.spkg, building from scratch. It breaks at\n\n```\nfmpz.c:40:29: error: zn_poly/zn_poly.h: No such file or directory\n```\n\nwhile building FLINT. Am I doing this incorrectly, or is there some problem with the spkg?",
    "created_at": "2009-05-28T15:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45631",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I couldn't build the spkg on linux/opteron. I tried vanilla sage 3.4.2 with spkg/standard/flint-1.2.4.p2.spkg replaced by flint-1.2.5.spkg, building from scratch. It breaks at

```
fmpz.c:40:29: error: zn_poly/zn_poly.h: No such file or directory
```

while building FLINT. Am I doing this incorrectly, or is there some problem with the spkg?



---

archive/issue_comments_045632.json:
```json
{
    "body": "Ok, for some reason fmpz.c has\n\n#include \"zn_poly/zn_poly.h\"\n\nwhereas all the other files have\n\n#include \"zn_poly/src/zn_poly.h\"\n\nWhen I change fmpz.c to the latter, the spkg builds.",
    "created_at": "2009-05-28T16:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45632",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Ok, for some reason fmpz.c has

#include "zn_poly/zn_poly.h"

whereas all the other files have

#include "zn_poly/src/zn_poly.h"

When I change fmpz.c to the latter, the spkg builds.



---

archive/issue_comments_045633.json:
```json
{
    "body": "After fixing the build problem above, I can replicate mabshoff's doctest failure.\n\nHowever, if one tries the computation directly, it gives the correct answer:\n\n```\nsage: S.<t> = PowerSeriesRing(Integers(1331), default_prec=4)\nsage: B = Matrix([[1144 + 264*t + 841*t^2 + 1025*t^3 + O(t^4), 176 + 1052*t + 216*t^2 + 523*t^3 + O(t^4)], [847 + 668*t + 81*t^2 + 424*t^3 + O(t^4), 185 + 341*t + 171*t^2 + 642*t^3 + O(t^4)]])sage: B.det()11 + 484*t^2 + 451*t^3 + O(t^4)\n```\n\nStill investigating...",
    "created_at": "2009-05-29T15:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45633",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

After fixing the build problem above, I can replicate mabshoff's doctest failure.

However, if one tries the computation directly, it gives the correct answer:

```
sage: S.<t> = PowerSeriesRing(Integers(1331), default_prec=4)
sage: B = Matrix([[1144 + 264*t + 841*t^2 + 1025*t^3 + O(t^4), 176 + 1052*t + 216*t^2 + 523*t^3 + O(t^4)], [847 + 668*t + 81*t^2 + 424*t^3 + O(t^4), 185 + 341*t + 171*t^2 + 642*t^3 + O(t^4)]])sage: B.det()11 + 484*t^2 + 451*t^3 + O(t^4)
```

Still investigating...



---

archive/issue_comments_045634.json:
```json
{
    "body": "Here is a simpler failure case:\n\n```\nsage: S.<t> = PolynomialRing(Integers(14641))\nsage: f = 1 + 9581*t\nsage: g = 1 + 4334*t\nsage: R = PolynomialRing(Integers(1331), \"t\")\nsage: ff = f.change_ring(R)\nsage: gg = g.change_ring(R)\nsage: ff\n264*t + 1\nsage: gg\n341*t + 1\nsage: ff * gg\n925*t^2 + 605*t + 1\nsage: (264 * 341) % 1331\n847\n```\n\nSo the `t^2` coefficient is wrong.",
    "created_at": "2009-05-29T15:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45634",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Here is a simpler failure case:

```
sage: S.<t> = PolynomialRing(Integers(14641))
sage: f = 1 + 9581*t
sage: g = 1 + 4334*t
sage: R = PolynomialRing(Integers(1331), "t")
sage: ff = f.change_ring(R)
sage: gg = g.change_ring(R)
sage: ff
264*t + 1
sage: gg
341*t + 1
sage: ff * gg
925*t^2 + 605*t + 1
sage: (264 * 341) % 1331
847
```

So the `t^2` coefficient is wrong.



---

archive/issue_comments_045635.json:
```json
{
    "body": "The output of `change_ring` (in the previous example) is not of type `Polynomial_zmod_flint` as it should be, it ends up being `Polynomial_generic_dense`. The multiplication ff * gg is actually calling the generic karatsuba code in the Sage library, it's not calling FLINT or `zn_poly` as far as I can tell. Each input to `do_karatsuba()` is a list containing a single polynomial, instead of a list of coefficients.\n\nProbably making `change_ring` return the correct type of object will fix all this mess. I don't think it has anything to do with FLINT or `zn_poly`. Maybe it's a coercion problem.",
    "created_at": "2009-05-29T16:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45635",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

The output of `change_ring` (in the previous example) is not of type `Polynomial_zmod_flint` as it should be, it ends up being `Polynomial_generic_dense`. The multiplication ff * gg is actually calling the generic karatsuba code in the Sage library, it's not calling FLINT or `zn_poly` as far as I can tell. Each input to `do_karatsuba()` is a list containing a single polynomial, instead of a list of coefficients.

Probably making `change_ring` return the correct type of object will fix all this mess. I don't think it has anything to do with FLINT or `zn_poly`. Maybe it's a coercion problem.



---

archive/issue_comments_045636.json:
```json
{
    "body": "Sorry, I'm an idiot. That code snippet above is using `change_ring` incorrectly. Here is a better example:\n\n```\nsage: S.<t> = PolynomialRing(Integers(14641))\nsage: f = 1 + 9581*t\nsage: g = 1 + 4334*t\nsage: R = Integers(1331)\nsage: ff = f.change_ring(R)\nsage: gg = g.change_ring(R)\nsage: ff\n264*t + 1\nsage: gg\n341*t + 1\nsage: ff * gg\n925*t^2 + 605*t + 1\nsage: (264 * 341) % 1331\n847\n```\n\nBoth ff and gg now have the correct type, but the answer is still wrong. Still investigating...",
    "created_at": "2009-05-29T16:28:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45636",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Sorry, I'm an idiot. That code snippet above is using `change_ring` incorrectly. Here is a better example:

```
sage: S.<t> = PolynomialRing(Integers(14641))
sage: f = 1 + 9581*t
sage: g = 1 + 4334*t
sage: R = Integers(1331)
sage: ff = f.change_ring(R)
sage: gg = g.change_ring(R)
sage: ff
264*t + 1
sage: gg
341*t + 1
sage: ff * gg
925*t^2 + 605*t + 1
sage: (264 * 341) % 1331
847
```

Both ff and gg now have the correct type, but the answer is still wrong. Still investigating...



---

archive/issue_comments_045637.json:
```json
{
    "body": "Somewhere some coefficients are not being reduced properly:\n\n```\nsage: R.<x> = PolynomialRing(Integers(121))\nsage: S.<y> = PolynomialRing(Integers(11))\nsage: S(50*x)\n6*y\nsage: R(S(50*x))\n50*x     # !!!!!!\n```\n\nThis happens for both the flint-1.2.4.p2 and flint-1.2.5 spkgs.",
    "created_at": "2009-05-29T19:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45637",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Somewhere some coefficients are not being reduced properly:

```
sage: R.<x> = PolynomialRing(Integers(121))
sage: S.<y> = PolynomialRing(Integers(11))
sage: S(50*x)
6*y
sage: R(S(50*x))
50*x     # !!!!!!
```

This happens for both the flint-1.2.4.p2 and flint-1.2.5 spkgs.



---

archive/issue_comments_045638.json:
```json
{
    "body": "I have made a more specific ticket at #6168.",
    "created_at": "2009-05-31T05:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45638",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I have made a more specific ticket at #6168.



---

archive/issue_comments_045639.json:
```json
{
    "body": "I applied the ticket at #6168 against 4.0, and then built the spkg (on sage.math). It now passes all doctests in sage/schemes and sage/rings. Positive review.",
    "created_at": "2009-06-02T01:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45639",
    "user": "https://github.com/kedlaya"
}
```

I applied the ticket at #6168 against 4.0, and then built the spkg (on sage.math). It now passes all doctests in sage/schemes and sage/rings. Positive review.



---

archive/issue_comments_045640.json:
```json
{
    "body": "Merged flint-1.2.5.spkg in 4.0.1.rc0.  Note that testing is enabled.  I'll make a ticket to disable it for the final release.",
    "created_at": "2009-06-03T20:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45640",
    "user": "https://github.com/mwhansen"
}
```

Merged flint-1.2.5.spkg in 4.0.1.rc0.  Note that testing is enabled.  I'll make a ticket to disable it for the final release.



---

archive/issue_events_013660.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-03T20:23:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5817#event-13660"
}
```



---

archive/issue_comments_045641.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-03T20:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5817",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5817#issuecomment-45641",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
