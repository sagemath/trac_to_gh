# Issue 3237: update ecm to 6.2

archive/issues_003237.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @zimmermann6\n\nPaul Zimmermann writes:\n\n```\nRelease notes:\n* New stage 2 for P-1 and P+1, described in Montgomery and Kruppa,\n  Improved Stage 2 to P+-1 Factoring Algorithms,\n  in A. J. van der Poorten and A. Stein (Eds.), ANTS-VIII 2008,\n  LNCS 5011, pp. 180-195.\n* Parallelization in the new P+-1 stage 2 (with --enable-openmp).\n* Optimizations to the NTT code by Jason S. Papadopoulos\n* Improved mulredc assembly code for Athlon64/Opteron\n* Improved modular reduction in the mpzmod range\n* Bugfix in P+1 stage 2 which caused incorrect initialisation if\n  Brent-Suyama polynomial had degree > 1 and i0 was negative (occurs\n  only with non-standard parameters)\n* Bugfix in generation of Lucas chains for P+1 and ECM, causing some\n  stage 1 primes close to 2^32 to be processed incorrectly on 32 bit\n  systems\n* Added build project for VC++ by Brian Gladman\n* File ecm.h changed from GPL to LGPL: the fact it was under GPL was an\n  unvoluntary mistake, which has the consequence that applications\n  linking with libecm for version < 6.2 should be under GPL too.\n* Fixed a regression introduced in 6.1.1: the default arithmetic (NTT)\n  for stage 2 was slower for large inputs. Now defaults to -no-ntt for\n  input numbers >30 machine words.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3237\n\n",
    "created_at": "2008-05-17T09:51:38Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "update ecm to 6.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3237",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @zimmermann6

Paul Zimmermann writes:

```
Release notes:
* New stage 2 for P-1 and P+1, described in Montgomery and Kruppa,
  Improved Stage 2 to P+-1 Factoring Algorithms,
  in A. J. van der Poorten and A. Stein (Eds.), ANTS-VIII 2008,
  LNCS 5011, pp. 180-195.
* Parallelization in the new P+-1 stage 2 (with --enable-openmp).
* Optimizations to the NTT code by Jason S. Papadopoulos
* Improved mulredc assembly code for Athlon64/Opteron
* Improved modular reduction in the mpzmod range
* Bugfix in P+1 stage 2 which caused incorrect initialisation if
  Brent-Suyama polynomial had degree > 1 and i0 was negative (occurs
  only with non-standard parameters)
* Bugfix in generation of Lucas chains for P+1 and ECM, causing some
  stage 1 primes close to 2^32 to be processed incorrectly on 32 bit
  systems
* Added build project for VC++ by Brian Gladman
* File ecm.h changed from GPL to LGPL: the fact it was under GPL was an
  unvoluntary mistake, which has the consequence that applications
  linking with libecm for version < 6.2 should be under GPL too.
* Fixed a regression introduced in 6.1.1: the default arithmetic (NTT)
  for stage 2 was slower for large inputs. Now defaults to -no-ntt for
  input numbers >30 machine words.
```


Issue created by migration from https://trac.sagemath.org/ticket/3237





---

archive/issue_comments_022368.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-31T22:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3237#issuecomment-22368",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_022369.json:
```json
{
    "body": "A new patch release 6.2.1 out. To quote:\n\n```\nwe consider a patch release (6.2.1) to fix a few issues in 6.2:\n\n* the default B2 bound is way too small for the new P-1/P+1 algorithms\n* on some architectures, ecm-6.2 fails to compile due to undefined\n  udiv_qrnnd_preinv(). We will define LONGLONG_STANDALONE before including\n  longlong.h (this might slow down some architectures like HPPA, but we didn't\n  figure out a simple patch for now)\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-05-31T22:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3237#issuecomment-22369",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

A new patch release 6.2.1 out. To quote:

```
we consider a patch release (6.2.1) to fix a few issues in 6.2:

* the default B2 bound is way too small for the new P-1/P+1 algorithms
* on some architectures, ecm-6.2 fails to compile due to undefined
  udiv_qrnnd_preinv(). We will define LONGLONG_STANDALONE before including
  longlong.h (this might slow down some architectures like HPPA, but we didn't
  figure out a simple patch for now)
```


Cheers,

Michael



---

archive/issue_comments_022370.json:
```json
{
    "body": "Man, this ticket has gone stale, so I will hopefully fix it soon.\n\nAnyway: Paul, I have been seeing the following on occasion in Sage 3.x for a while:\n\n```\nsage -t -long devel/sage/sage/interfaces/ecm.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha2/devel/sage-main/sage/interfaces/ecm.py\", line 317:\n    sage: ecm.factor((2^197 + 1)/3)           # takes a long time\nExpected:\n    [197002597249, 1348959352853811313, 251951573867253012259144010843]\nGot:\n    [251951573867253012259144010843, 265748496095531068869578877937]\n**********************************************************************\n```\n\nWhat happens in that case was that ecm did not finish quickly, but spend a long, long time burning 100% CPU until I killed it via top for example. Then the above output was printed. Is this something I should be concerned about? Will the 6.2.1 release fix this? The problem happens on occasion, i.e. maybe a percent of the tries, but I have no exact numbers.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T00:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3237#issuecomment-22370",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Man, this ticket has gone stale, so I will hopefully fix it soon.

Anyway: Paul, I have been seeing the following on occasion in Sage 3.x for a while:

```
sage -t -long devel/sage/sage/interfaces/ecm.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha2/devel/sage-main/sage/interfaces/ecm.py", line 317:
    sage: ecm.factor((2^197 + 1)/3)           # takes a long time
Expected:
    [197002597249, 1348959352853811313, 251951573867253012259144010843]
Got:
    [251951573867253012259144010843, 265748496095531068869578877937]
**********************************************************************
```

What happens in that case was that ecm did not finish quickly, but spend a long, long time burning 100% CPU until I killed it via top for example. Then the above output was printed. Is this something I should be concerned about? Will the 6.2.1 release fix this? The problem happens on occasion, i.e. maybe a percent of the tries, but I have no exact numbers.

Cheers,

Michael



---

archive/issue_comments_022371.json:
```json
{
    "body": "What happens is that find factors is given as input the prime factor 251...843 (I don't know why).\nOf course ECM takes a long time to factor it! It seems some primality test is missing (or wrong):\n\n```\nenter find_factor, n= 6695575184412459481424842051421510843842512474094970147089\n1 B1= 2000\n[265748496095531068869578877937, 251951573867253012259144010843]\nenter find_factor, n= 251951573867253012259144010843 B1= 2399\n```\n",
    "created_at": "2008-11-27T08:03:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3237#issuecomment-22371",
    "user": "https://github.com/zimmermann6"
}
```

What happens is that find factors is given as input the prime factor 251...843 (I don't know why).
Of course ECM takes a long time to factor it! It seems some primality test is missing (or wrong):

```
enter find_factor, n= 6695575184412459481424842051421510843842512474094970147089
1 B1= 2000
[265748496095531068869578877937, 251951573867253012259144010843]
enter find_factor, n= 251951573867253012259144010843 B1= 2399
```




---

archive/issue_comments_022372.json:
```json
{
    "body": "Attachment [trac_3237.patch](tarball://root/attachments/some-uuid/ticket3237/trac_3237.patch) by mabshoff created at 2008-12-23 23:13:46\n\nThe spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.3/alpha0/ecm-6.2.1.spkg\n\nupdates to lates upstream. The growth of the spkg is caused by upstream and there is no obvious far to cut. The patch attached to this ticket makes the ecm extension depend on ecm.h, so the next -b will automatically rebuild the ecm extension after the upgrade.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-23T23:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3237#issuecomment-22372",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_3237.patch](tarball://root/attachments/some-uuid/ticket3237/trac_3237.patch) by mabshoff created at 2008-12-23 23:13:46

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.3/alpha0/ecm-6.2.1.spkg

updates to lates upstream. The growth of the spkg is caused by upstream and there is no obvious far to cut. The patch attached to this ticket makes the ecm extension depend on ecm.h, so the next -b will automatically rebuild the ecm extension after the upgrade.

Cheers,

Michael



---

archive/issue_comments_022373.json:
```json
{
    "body": "Builds and passes tests for me.\n\n+1",
    "created_at": "2008-12-23T23:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3237#issuecomment-22373",
    "user": "https://github.com/rlmill"
}
```

Builds and passes tests for me.

+1



---

archive/issue_comments_022374.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-23T23:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3237#issuecomment-22374",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.3.alpha0



---

archive/issue_events_003456.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-12-23T23:44:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3237",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3237#event-3456"
}
```



---

archive/issue_comments_022375.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-23T23:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3237",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3237#issuecomment-22375",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
