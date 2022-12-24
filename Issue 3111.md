# Issue 3111: sage's new baby-step giant step evidently needs additional polish

archive/issues_003111.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nPaste this code into a Sage session:\n\n```\nE = EllipticCurve('389a')\nfor p in prime_range(10000):\n    if p != 389:\n       try:\n           G = E.change_ring(GF(p)).abelian_group()\n       except Exception, msg:\n           print \"p = %s fails\"%p\n           print msg\n```\n\n\nThe output varies on run and computer.  Typical output looks like this:\n\n```\np = 7 fails\nNo solution in bsgs()\np = 1901 fails\n\np = 4273 fails\n\np = 5101 fails\n\np = 7177 fails\n\np = 7433 fails\n\np = 9013 fails\n\np = 9049 fails\n\np = 9749 fails\n```\n\n\nThe actual failures are assertion failures in the baby-step giant-step implementation.\n\n -- William\n\nIssue created by migration from https://trac.sagemath.org/ticket/3111\n\n",
    "created_at": "2008-05-06T16:07:05Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "sage's new baby-step giant step evidently needs additional polish",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3111",
    "user": "@williamstein"
}
```
Assignee: @JohnCremona

Paste this code into a Sage session:

```
E = EllipticCurve('389a')
for p in prime_range(10000):
    if p != 389:
       try:
           G = E.change_ring(GF(p)).abelian_group()
       except Exception, msg:
           print "p = %s fails"%p
           print msg
```


The output varies on run and computer.  Typical output looks like this:

```
p = 7 fails
No solution in bsgs()
p = 1901 fails

p = 4273 fails

p = 5101 fails

p = 7177 fails

p = 7433 fails

p = 9013 fails

p = 9049 fails

p = 9749 fails
```


The actual failures are assertion failures in the baby-step giant-step implementation.

 -- William

Issue created by migration from https://trac.sagemath.org/ticket/3111





---

archive/issue_comments_021502.json:
```json
{
    "body": "Under OS X (10.5.1 intel core2 duo with 2GB RAM)\nI also get a repeatable massive memory overflow that completely crashes Sage:\n\n```\nsage: E = EllipticCurve('389a')\nsage: for p in prime_range(10000):\n....:         if p != 389:\n....:            try:\n....:                G = E.change_ring(GF(p)).abelian_group()\n....:        except Exception, msg:\n....:                print \"p = %s fails\"%p\n....:            print msg\n....: \np = 7 fails\nNo solution in bsgs()\np = 523 fails\n\np = 2477 fails\n\np = 3001 fails\n\np = 3449 fails\n\n\nerror: no more memory\nSystem 5120k:5120k Appl 4637k/482k Malloc 4094k/1k Valloc 1024k/480k Pages 152/104 Regions 2:2\n\nhalt 14\nteragon-2:sage-3.0.1 was$ \n\n```\n\n\n\nRunning this under gdb yields nothing useful:\n\n\n```\n\nerror: no more memory\nSystem 5116k:5116k Appl 4629k/486k Malloc 4086k/5k Valloc 1024k/481k Pages 152/104 Regions 2:2\n\nhalt 14\n\nProgram exited with code 016.\n(gdb) bt\nNo stack.\n```\n",
    "created_at": "2008-05-06T16:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21502",
    "user": "@williamstein"
}
```

Under OS X (10.5.1 intel core2 duo with 2GB RAM)
I also get a repeatable massive memory overflow that completely crashes Sage:

```
sage: E = EllipticCurve('389a')
sage: for p in prime_range(10000):
....:         if p != 389:
....:            try:
....:                G = E.change_ring(GF(p)).abelian_group()
....:        except Exception, msg:
....:                print "p = %s fails"%p
....:            print msg
....: 
p = 7 fails
No solution in bsgs()
p = 523 fails

p = 2477 fails

p = 3001 fails

p = 3449 fails


error: no more memory
System 5120k:5120k Appl 4637k/482k Malloc 4094k/1k Valloc 1024k/480k Pages 152/104 Regions 2:2

halt 14
teragon-2:sage-3.0.1 was$ 

```



Running this under gdb yields nothing useful:


```

error: no more memory
System 5116k:5116k Appl 4629k/486k Malloc 4086k/5k Valloc 1024k/481k Pages 152/104 Regions 2:2

halt 14

Program exited with code 016.
(gdb) bt
No stack.
```




---

archive/issue_comments_021503.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2008-05-06T16:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21503",
    "user": "@williamstein"
}
```

Changing priority from major to critical.



---

archive/issue_comments_021504.json:
```json
{
    "body": "NOte -- the above is not a leak between calls of abelian_group.  It's that one single calculation is somehow using up all memory and crashing sage.",
    "created_at": "2008-05-06T16:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21504",
    "user": "@williamstein"
}
```

NOte -- the above is not a leak between calls of abelian_group.  It's that one single calculation is somehow using up all memory and crashing sage.



---

archive/issue_comments_021505.json:
```json
{
    "body": "With Sage 3.0.1 on sage.math this seems rather harmless:\n\n```\n  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND\n28670 mabshoff  20   0  455m 141m  21m S    0  0.2   0:35.02 sage-ipython\n29958 mabshoff  15   0 97.7m  24m 2060 S    0  0.0   0:03.67 python\n28715 mabshoff  16   0  634m  14m 2096 S    0  0.0   0:02.27 gp\n```\n\nIf for some dumb reason pari doubles the stack once more on OSX you are SOL. I tried on OSX 10.5 and I hit the same error. Now it sounds like a 64 bit OSX version of Sage would fix that issue, but .....\n\nCheers,\n\nMichael",
    "created_at": "2008-05-06T17:14:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21505",
    "user": "mabshoff"
}
```

With Sage 3.0.1 on sage.math this seems rather harmless:

```
  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
28670 mabshoff  20   0  455m 141m  21m S    0  0.2   0:35.02 sage-ipython
29958 mabshoff  15   0 97.7m  24m 2060 S    0  0.0   0:03.67 python
28715 mabshoff  16   0  634m  14m 2096 S    0  0.0   0:02.27 gp
```

If for some dumb reason pari doubles the stack once more on OSX you are SOL. I tried on OSX 10.5 and I hit the same error. Now it sounds like a 64 bit OSX version of Sage would fix that issue, but .....

Cheers,

Michael



---

archive/issue_comments_021506.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-06T21:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21506",
    "user": "@JohnCremona"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021507.json:
```json
{
    "body": "I found the bug which causes this.  It is not in any of the generic code at all, but in some lines I added quite late on in ell_finite_field.py to make one step (in code which happens relatively infrequently) \"more efficient\".  I'll post a patch on Wednesday.",
    "created_at": "2008-05-06T21:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21507",
    "user": "@JohnCremona"
}
```

I found the bug which causes this.  It is not in any of the generic code at all, but in some lines I added quite late on in ell_finite_field.py to make one step (in code which happens relatively infrequently) "more efficient".  I'll post a patch on Wednesday.



---

archive/issue_comments_021508.json:
```json
{
    "body": "Two bugs fixed:\n\n* A stupid rounding error in `ell_generic.Hasse_bounds()`   [NB the floor of 2*sqrt(q) is not 2*floor(sqrt(q))!]\n\n* A more subtle bug in the abelian_group() function for curves over finite fields, in a bit of code added late on for \"efficiency\".  We now still have the efficiency but without the bug (at least, not that one).  The code in the original post now runs fine;  I also ran it up to `10***5` and for `GF(p^k)` up to `10^3` for `k=2,3,4,5`.\n\nFor the future: I still have some more plans for ell_finite_field in cases where j is not in the prime field.  Then, at present the only way we have to compute the cardinality is via the group structure, but for the majority of cases it should be easier to compute the cardinality only using Mestre's trick.  However, Mestre's trick (as stated and proved by Schoof's second JNTB paper) is usually stated over prime fields, and over non-prime fields of square size there is one situation where Mestre's trick does not work (specifically when q is a square and the Frobenius is an integer and the group order (and structure) is either `(sqrt(q)-1)**2` or `(sqrt(q)+1)**2`.)  \n\nWhen I have worked out how best to detect that case there will be a new patch.  Until then, curves whose j is not in the prime field and which do not have cyclic groups run into the efficiency problem (fixed above but only when the cardinality is already known) where some rather large elliptic curve discrete logs may need to be computed.",
    "created_at": "2008-05-07T10:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21508",
    "user": "@JohnCremona"
}
```

Two bugs fixed:

* A stupid rounding error in `ell_generic.Hasse_bounds()`   [NB the floor of 2*sqrt(q) is not 2*floor(sqrt(q))!]

* A more subtle bug in the abelian_group() function for curves over finite fields, in a bit of code added late on for "efficiency".  We now still have the efficiency but without the bug (at least, not that one).  The code in the original post now runs fine;  I also ran it up to `10***5` and for `GF(p^k)` up to `10^3` for `k=2,3,4,5`.

For the future: I still have some more plans for ell_finite_field in cases where j is not in the prime field.  Then, at present the only way we have to compute the cardinality is via the group structure, but for the majority of cases it should be easier to compute the cardinality only using Mestre's trick.  However, Mestre's trick (as stated and proved by Schoof's second JNTB paper) is usually stated over prime fields, and over non-prime fields of square size there is one situation where Mestre's trick does not work (specifically when q is a square and the Frobenius is an integer and the group order (and structure) is either `(sqrt(q)-1)**2` or `(sqrt(q)+1)**2`.)  

When I have worked out how best to detect that case there will be a new patch.  Until then, curves whose j is not in the prime field and which do not have cyclic groups run into the efficiency problem (fixed above but only when the cardinality is already known) where some rather large elliptic curve discrete logs may need to be computed.



---

archive/issue_comments_021509.json:
```json
{
    "body": "Hmm ... there doesn't seem to be a patch attached, despite the title saying \"with patch.\" :)",
    "created_at": "2008-05-08T21:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21509",
    "user": "@craigcitro"
}
```

Hmm ... there doesn't seem to be a patch attached, despite the title saying "with patch." :)



---

archive/issue_comments_021510.json:
```json
{
    "body": "Attachment [sage-3111.patch](tarball://root/attachments/some-uuid/ticket3111/sage-3111.patch) by @JohnCremona created at 2008-05-08 21:26:16\n\nSorry about that, it is there now.\n\nAnd as I looked at the patch after uploading it I saw that there are a couple of debugging print statements which need deleting, near the end (lines 1194/5) but I'll leave that until tomorrow.",
    "created_at": "2008-05-08T21:26:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21510",
    "user": "@JohnCremona"
}
```

Attachment [sage-3111.patch](tarball://root/attachments/some-uuid/ticket3111/sage-3111.patch) by @JohnCremona created at 2008-05-08 21:26:16

Sorry about that, it is there now.

And as I looked at the patch after uploading it I saw that there are a couple of debugging print statements which need deleting, near the end (lines 1194/5) but I'll leave that until tomorrow.



---

archive/issue_comments_021511.json:
```json
{
    "body": "Doctests pass in ell_generic.py and ell_finite_field. No more printed failues when running code in ticket description (they were there before I applied the paths), though I also run out of memory on mac 10.5 with 2 GB ram. If this is not expected behavior it should be reported as a separate ticket. Positive review pending removal of debugging print statements.",
    "created_at": "2008-05-12T10:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21511",
    "user": "broune"
}
```

Doctests pass in ell_generic.py and ell_finite_field. No more printed failues when running code in ticket description (they were there before I applied the paths), though I also run out of memory on mac 10.5 with 2 GB ram. If this is not expected behavior it should be reported as a separate ticket. Positive review pending removal of debugging print statements.



---

archive/issue_comments_021512.json:
```json
{
    "body": "I think that we should also add at least one doctest showing that this behavior is fixed.",
    "created_at": "2008-05-12T16:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21512",
    "user": "@craigcitro"
}
```

I think that we should also add at least one doctest showing that this behavior is fixed.



---

archive/issue_comments_021513.json:
```json
{
    "body": "Additional tp sage-3111.patch",
    "created_at": "2008-05-12T21:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21513",
    "user": "@JohnCremona"
}
```

Additional tp sage-3111.patch



---

archive/issue_comments_021514.json:
```json
{
    "body": "Attachment [sage-3111-extra.patch](tarball://root/attachments/some-uuid/ticket3111/sage-3111-extra.patch) by @JohnCremona created at 2008-05-12 21:29:57\n\nsage-3111-extra.patch does the following:\n\n* deleted two debuggin print lines\n* added doctest to show that the original post is fixed\n* passes all doctests in sage/schemes/elliptic_curves\n\nFor the doctest I check that it is OK for 10 random primes up to `10^4` rather than all of them since that takes about 18s to run.",
    "created_at": "2008-05-12T21:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21514",
    "user": "@JohnCremona"
}
```

Attachment [sage-3111-extra.patch](tarball://root/attachments/some-uuid/ticket3111/sage-3111-extra.patch) by @JohnCremona created at 2008-05-12 21:29:57

sage-3111-extra.patch does the following:

* deleted two debuggin print lines
* added doctest to show that the original post is fixed
* passes all doctests in sage/schemes/elliptic_curves

For the doctest I check that it is OK for 10 random primes up to `10^4` rather than all of them since that takes about 18s to run.



---

archive/issue_comments_021515.json:
```json
{
    "body": "I would prefer to use 10 specific primes, as using random primes gives unrepeatable results. Unless Sage does something like reset the random seed before each test?",
    "created_at": "2008-05-12T21:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21515",
    "user": "broune"
}
```

I would prefer to use 10 specific primes, as using random primes gives unrepeatable results. Unless Sage does something like reset the random seed before each test?



---

archive/issue_comments_021516.json:
```json
{
    "body": "Replying to [comment:10 cremona]:\n> sage-3111-extra.patch does the following:\n> \n>    * deleted two debuggin print lines\n>    * added doctest to show that the original post is fixed\n>    * passes all doctests in sage/schemes/elliptic_curves\n> \n> For the doctest I check that it is OK for 10 random primes up to `10^4` rather than all of them since that takes about 18s to run.\n\nHi John,\n\nyou could do two tests: \n* a quick one that is run per default \n* a long one marked with `#long` - 18 seconds is not a problem with long.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-12T21:41:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21516",
    "user": "mabshoff"
}
```

Replying to [comment:10 cremona]:
> sage-3111-extra.patch does the following:
> 
>    * deleted two debuggin print lines
>    * added doctest to show that the original post is fixed
>    * passes all doctests in sage/schemes/elliptic_curves
> 
> For the doctest I check that it is OK for 10 random primes up to `10^4` rather than all of them since that takes about 18s to run.

Hi John,

you could do two tests: 
* a quick one that is run per default 
* a long one marked with `#long` - 18 seconds is not a problem with long.

Cheers,

Michael



---

archive/issue_comments_021517.json:
```json
{
    "body": "Replying to [comment:11 broune]:\n> I would prefer to use 10 specific primes, as using random primes gives unrepeatable results. Unless Sage does something like reset the random seed before each test?\n\nSage now uses the same seed per default for randomness at the start of each doctest, so it is reproducible. Not all sources of randomness have that property yet, but for primes it should work. So no need to stick `#random` in the doctest string.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-12T21:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21517",
    "user": "mabshoff"
}
```

Replying to [comment:11 broune]:
> I would prefer to use 10 specific primes, as using random primes gives unrepeatable results. Unless Sage does something like reset the random seed before each test?

Sage now uses the same seed per default for randomness at the start of each doctest, so it is reproducible. Not all sources of randomness have that property yet, but for primes it should work. So no need to stick `#random` in the doctest string.

Cheers,

Michael



---

archive/issue_comments_021518.json:
```json
{
    "body": "Attachment [sage-3111-extra2.patch](tarball://root/attachments/some-uuid/ticket3111/sage-3111-extra2.patch) by @JohnCremona created at 2008-05-12 21:47:04\n\nApply after previous two",
    "created_at": "2008-05-12T21:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21518",
    "user": "@JohnCremona"
}
```

Attachment [sage-3111-extra2.patch](tarball://root/attachments/some-uuid/ticket3111/sage-3111-extra2.patch) by @JohnCremona created at 2008-05-12 21:47:04

Apply after previous two



---

archive/issue_comments_021519.json:
```json
{
    "body": "Michael,\n\nI have added an extra patch anyway -- my comment on it was killed by trac as you were editing at the same time )I thought trac would be cleverer than that!)\n\nJohn",
    "created_at": "2008-05-12T21:49:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21519",
    "user": "@JohnCremona"
}
```

Michael,

I have added an extra patch anyway -- my comment on it was killed by trac as you were editing at the same time )I thought trac would be cleverer than that!)

John



---

archive/issue_comments_021520.json:
```json
{
    "body": "If you still want the long test (all primes to 10000) I can add it tomorrow -- my bedtime now.",
    "created_at": "2008-05-12T21:51:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21520",
    "user": "@JohnCremona"
}
```

If you still want the long test (all primes to 10000) I can add it tomorrow -- my bedtime now.



---

archive/issue_comments_021521.json:
```json
{
    "body": "Sorry about the misinformation on random - it is good that Sage handles this nicely.\n\nRunnning the doctest code for the 10 primes with an unpatched Sage does not trigger the bug after I tried it a few times on my machine. Ten primes just does not seem to be enough to hit the bug with high probability. It would be better to find some primes that always trigger the bug. I get different numbers failing on each run, except that 7 seems to show up every time. So it would be nice to check p=7 every time in the doctest, in addition to the random tests.",
    "created_at": "2008-05-12T21:51:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21521",
    "user": "broune"
}
```

Sorry about the misinformation on random - it is good that Sage handles this nicely.

Runnning the doctest code for the 10 primes with an unpatched Sage does not trigger the bug after I tried it a few times on my machine. Ten primes just does not seem to be enough to hit the bug with high probability. It would be better to find some primes that always trigger the bug. I get different numbers failing on each run, except that 7 seems to show up every time. So it would be nice to check p=7 every time in the doctest, in addition to the random tests.



---

archive/issue_comments_021522.json:
```json
{
    "body": "Attachment [sage-3111-extra3.patch](tarball://root/attachments/some-uuid/ticket3111/sage-3111-extra3.patch) by @JohnCremona created at 2008-05-13 08:18:56\n\napply after all previous",
    "created_at": "2008-05-13T08:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21522",
    "user": "@JohnCremona"
}
```

Attachment [sage-3111-extra3.patch](tarball://root/attachments/some-uuid/ticket3111/sage-3111-extra3.patch) by @JohnCremona created at 2008-05-13 08:18:56

apply after all previous



---

archive/issue_comments_021523.json:
```json
{
    "body": "Yet another patch sage-3111-extra3.patch now tests the original full code for primes to 10000 but this longer test is marked #long as it takes around 20s.\n\nApologies for the succession of small cumulative patches, Michael:  I only trust myself to do `hg_sage.export(\"tip\")`.",
    "created_at": "2008-05-13T08:22:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21523",
    "user": "@JohnCremona"
}
```

Yet another patch sage-3111-extra3.patch now tests the original full code for primes to 10000 but this longer test is marked #long as it takes around 20s.

Apologies for the succession of small cumulative patches, Michael:  I only trust myself to do `hg_sage.export("tip")`.



---

archive/issue_comments_021524.json:
```json
{
    "body": "The phrase \"needs minimal further review\" resulted in this one not being listed by trac as a \"needs review\" ticket so I have changed that and hope that someone can oblige.  The extra patches do what was wanted by the orginal reviewer.",
    "created_at": "2008-05-14T21:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21524",
    "user": "@JohnCremona"
}
```

The phrase "needs minimal further review" resulted in this one not being listed by trac as a "needs review" ticket so I have changed that and hope that someone can oblige.  The extra patches do what was wanted by the orginal reviewer.



---

archive/issue_comments_021525.json:
```json
{
    "body": "This looks good. (I don't know how this slipped under the radar as long as it did.)",
    "created_at": "2008-06-02T07:59:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21525",
    "user": "@craigcitro"
}
```

This looks good. (I don't know how this slipped under the radar as long as it did.)



---

archive/issue_comments_021526.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-04T18:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21526",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021527.json:
```json
{
    "body": "Finally! Merged all four patches in Sage 3.0.3.alpha1",
    "created_at": "2008-06-04T18:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3111#issuecomment-21527",
    "user": "mabshoff"
}
```

Finally! Merged all four patches in Sage 3.0.3.alpha1
