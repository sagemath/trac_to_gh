# Issue 9717: fix variable substitution in PolyBoRi

archive/issues_009717.json:
```json
{
    "body": "Assignee: malb\n\nCC:  polybori alexanderdreyer leif mpatel\n\nFor some inputs our[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) wrapper throws an error while upstream computes the example just fine. The reason we fail is that some rings don't match and thus coercion goes wrong. The problem was reported by Joan Daemen who also provided an example via private communication.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9717\n\n",
    "created_at": "2010-08-10T12:43:40Z",
    "labels": [
        "commutative algebra",
        "critical",
        "bug"
    ],
    "title": "fix variable substitution in PolyBoRi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9717",
    "user": "malb"
}
```
Assignee: malb

CC:  polybori alexanderdreyer leif mpatel

For some inputs our[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) wrapper throws an error while upstream computes the example just fine. The reason we fail is that some rings don't match and thus coercion goes wrong. The problem was reported by Joan Daemen who also provided an example via private communication.

Issue created by migration from https://trac.sagemath.org/ticket/9717





---

archive/issue_comments_094805.json:
```json
{
    "body": "Alexander Dreyer provided a fix for the issue. I've packaged this fix into an SPKG\n\n\u00a0http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p2.spkg\n\nI've also packaged his patch for Sage into a proper mercurial patch which I'll attach in a sec.",
    "created_at": "2010-08-10T12:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94805",
    "user": "malb"
}
```

Alexander Dreyer provided a fix for the issue. I've packaged this fix into an SPKG

 http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p2.spkg

I've also packaged his patch for Sage into a proper mercurial patch which I'll attach in a sec.



---

archive/issue_comments_094806.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-08-10T12:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94806",
    "user": "malb"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_094807.json:
```json
{
    "body": "The attached patch + SPKG fix the original problem, however I'm getting segfaults now:\n\n\n```\nProgram received signal SIGSEGV, Segmentation fault.\nlinalg_step_modified (polys=<value optimized out>, terms=<value optimized out>, \n    leads_from_strat=<value optimized out>, log=<value optimized out>, \n    optDrawMatrices=<value optimized out>, matrixPrefix=<value optimized out>)\n    at groebner/src/nf.cc:2270\n2270    groebner/src/nf.cc: No such file or directory.\n        in groebner/src/nf.cc\nCurrent language:  auto\nThe current source language is \"auto; currently c++\".\n(gdb) bt\n#0  linalg_step_modified (polys=<value optimized out>, terms=<value optimized out>, \n    leads_from_strat=<value optimized out>, log=<value optimized out>, \n    optDrawMatrices=<value optimized out>, matrixPrefix=<value optimized out>)\n    at groebner/src/nf.cc:2270\n#1  0x00007fffcf4f6c56 in polybori::groebner::GroebnerStrategy::faugereStepDense (\n    this=<value optimized out>, orig_system=<value optimized out>) at groebner/src/nf.cc:2386\n#2  0x00007fffcf3e2a0d in __pyx_pf_4sage_5rings_10polynomial_5pbori_16GroebnerStrategy_faugere_step_dense (__pyx_v_self=0x5997520, __pyx_v_v=0x12bf3500) at sage/rings/polynomial/pbori.cpp:31846\n#3  0x00007ffff7b11316 in call_function (f=0x418a900, throwflag=<value optimized out>)\n    at Python/ceval.c:3694\n\n```\n",
    "created_at": "2010-08-10T12:49:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94807",
    "user": "malb"
}
```

The attached patch + SPKG fix the original problem, however I'm getting segfaults now:


```
Program received signal SIGSEGV, Segmentation fault.
linalg_step_modified (polys=<value optimized out>, terms=<value optimized out>, 
    leads_from_strat=<value optimized out>, log=<value optimized out>, 
    optDrawMatrices=<value optimized out>, matrixPrefix=<value optimized out>)
    at groebner/src/nf.cc:2270
2270    groebner/src/nf.cc: No such file or directory.
        in groebner/src/nf.cc
Current language:  auto
The current source language is "auto; currently c++".
(gdb) bt
#0  linalg_step_modified (polys=<value optimized out>, terms=<value optimized out>, 
    leads_from_strat=<value optimized out>, log=<value optimized out>, 
    optDrawMatrices=<value optimized out>, matrixPrefix=<value optimized out>)
    at groebner/src/nf.cc:2270
#1  0x00007fffcf4f6c56 in polybori::groebner::GroebnerStrategy::faugereStepDense (
    this=<value optimized out>, orig_system=<value optimized out>) at groebner/src/nf.cc:2386
#2  0x00007fffcf3e2a0d in __pyx_pf_4sage_5rings_10polynomial_5pbori_16GroebnerStrategy_faugere_step_dense (__pyx_v_self=0x5997520, __pyx_v_v=0x12bf3500) at sage/rings/polynomial/pbori.cpp:31846
#3  0x00007ffff7b11316 in call_function (f=0x418a900, throwflag=<value optimized out>)
    at Python/ceval.c:3694

```




---

archive/issue_comments_094808.json:
```json
{
    "body": "Ignore the SIGSEGV above, it is unrelated to this ticket but is caused by #9562.\u00a0\n\nAlexander, can you review my SPKG + patch, i.e. that it does what you intended? I give your changes a positive review so all that's needed is some check whether I produced the SPKG correctly etc.",
    "created_at": "2010-08-10T13:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94808",
    "user": "malb"
}
```

Ignore the SIGSEGV above, it is unrelated to this ticket but is caused by #9562. 

Alexander, can you review my SPKG + patch, i.e. that it does what you intended? I give your changes a positive review so all that's needed is some check whether I produced the SPKG correctly etc.



---

archive/issue_comments_094809.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-10T13:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94809",
    "user": "malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094810.json:
```json
{
    "body": "Use this SPKG instead (it is based on the latest PolyBoRi SPKG which the previous SPKG wasn't)\u00a0\n\n\u00a0http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p3.spkg",
    "created_at": "2010-08-10T15:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94810",
    "user": "malb"
}
```

Use this SPKG instead (it is based on the latest PolyBoRi SPKG which the previous SPKG wasn't) 

 http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p3.spkg



---

archive/issue_comments_094811.json:
```json
{
    "body": "There was some unrelated issue with the previous spkg (libm4ri was not found, because Sage's lib directory was not given to PolyBoRi)\nI updated the spkg accordingly:\nhttp://sage.math.washington.edu/home/dreyer/pb/polybori-0.6.4.p4.spkg",
    "created_at": "2010-08-10T21:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94811",
    "user": "AlexanderDreyer"
}
```

There was some unrelated issue with the previous spkg (libm4ri was not found, because Sage's lib directory was not given to PolyBoRi)
I updated the spkg accordingly:
http://sage.math.washington.edu/home/dreyer/pb/polybori-0.6.4.p4.spkg



---

archive/issue_comments_094812.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-11T12:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94812",
    "user": "leif"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_094813.json:
```json
{
    "body": "`SPKG.txt` has to be updated for p4.\n\nAlexander's patch looks reasonable, though libm4ri (and the GD library) were previously found (in the second attempt)... (The only issue I'm aware of is with updating from 4.5.2 on MacOS X 10.6, which Mitesh Patel couldn't reproduce either; see #9721.)\n\n(The change to p4 is of course unrelated to the original intent of this ticket; perhaps adapt its title, too.)",
    "created_at": "2010-08-11T12:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94813",
    "user": "leif"
}
```

`SPKG.txt` has to be updated for p4.

Alexander's patch looks reasonable, though libm4ri (and the GD library) were previously found (in the second attempt)... (The only issue I'm aware of is with updating from 4.5.2 on MacOS X 10.6, which Mitesh Patel couldn't reproduce either; see #9721.)

(The change to p4 is of course unrelated to the original intent of this ticket; perhaps adapt its title, too.)



---

archive/issue_comments_094814.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n\n> `SPKG.txt` has to be updated for p4.\n\nI have a new SPKG which does exactly that. I'll upload it later.\n\n> Alexander's patch looks reasonable, though libm4ri (and the GD library) were previously found (in the second attempt)... (The only issue I'm aware of is with updating from 4.5.2 on MacOS X 10.6, which Mitesh Patel couldn't reproduce either; see #9721.) (The change to p4 is of course unrelated to the original intent of this ticket; perhaps adapt its title, too.)",
    "created_at": "2010-08-11T13:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94814",
    "user": "malb"
}
```

Replying to [comment:8 leif]:

> `SPKG.txt` has to be updated for p4.

I have a new SPKG which does exactly that. I'll upload it later.

> Alexander's patch looks reasonable, though libm4ri (and the GD library) were previously found (in the second attempt)... (The only issue I'm aware of is with updating from 4.5.2 on MacOS X 10.6, which Mitesh Patel couldn't reproduce either; see #9721.) (The change to p4 is of course unrelated to the original intent of this ticket; perhaps adapt its title, too.)



---

archive/issue_comments_094815.json:
```json
{
    "body": "The new SPKG is here\n\n\u00a0http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p4.spkg\n\nI just added an entry to SPKG.txt",
    "created_at": "2010-08-11T13:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94815",
    "user": "malb"
}
```

The new SPKG is here

 http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p4.spkg

I just added an entry to SPKG.txt



---

archive/issue_comments_094816.json:
```json
{
    "body": "PolyBoRi makes assumptions about M4RI which are not met with the newest upstream release (#9475). Thus, we should fix this here asap since the new M4RI is about to go in.",
    "created_at": "2010-08-11T18:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94816",
    "user": "malb"
}
```

PolyBoRi makes assumptions about M4RI which are not met with the newest upstream release (#9475). Thus, we should fix this here asap since the new M4RI is about to go in.



---

archive/issue_comments_094817.json:
```json
{
    "body": "I've replaced the SPKG here\u00a0\n\n\u00a0 \u00a0http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p4.spkg\n\nand the new SPKG fixes the SIGSEGV and all doctests pass.\n\nThese fixes are:\n\n\u00a0http://bitbucket.org/brickenstein/polybori/changeset/6ef7402d935b\n\n\u00a0http://bitbucket.org/brickenstein/polybori/changeset/b692c8181e94",
    "created_at": "2010-08-12T18:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94817",
    "user": "malb"
}
```

I've replaced the SPKG here 

   http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p4.spkg

and the new SPKG fixes the SIGSEGV and all doctests pass.

These fixes are:

 http://bitbucket.org/brickenstein/polybori/changeset/6ef7402d935b

 http://bitbucket.org/brickenstein/polybori/changeset/b692c8181e94



---

archive/issue_comments_094818.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-12T18:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94818",
    "user": "malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094819.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-13T02:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94819",
    "user": "leif"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_094820.json:
```json
{
    "body": "`Work issues` field ( = *\"Update `SPKG.txt`\"*) still (or again) valid... ;-)\n\n(Perhaps also add this ticket number, and mention the PolyBoRi upstream fixes there.)",
    "created_at": "2010-08-13T02:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94820",
    "user": "leif"
}
```

`Work issues` field ( = *"Update `SPKG.txt`"*) still (or again) valid... ;-)

(Perhaps also add this ticket number, and mention the PolyBoRi upstream fixes there.)



---

archive/issue_comments_094821.json:
```json
{
    "body": "Updated accordingly.",
    "created_at": "2010-08-13T08:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94821",
    "user": "malb"
}
```

Updated accordingly.



---

archive/issue_comments_094822.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-13T08:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94822",
    "user": "malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094823.json:
```json
{
    "body": "Meanwhile, I took a look at the surrounding code also. (Just to ensure, that the patches also do the right thing in other contexts.) It's a good patch and it may fix even more issues. So I give a positive review from the mathematical point of view. (If I'm allowed to do so.) For the technical viewpoint: I'm waiting now for `sage -testall` to finish.",
    "created_at": "2010-08-13T09:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94823",
    "user": "AlexanderDreyer"
}
```

Meanwhile, I took a look at the surrounding code also. (Just to ensure, that the patches also do the right thing in other contexts.) It's a good patch and it may fix even more issues. So I give a positive review from the mathematical point of view. (If I'm allowed to do so.) For the technical viewpoint: I'm waiting now for `sage -testall` to finish.



---

archive/issue_comments_094824.json:
```json
{
    "body": "Passed `ptestlong` with Sage 4.5.3.alpha0 and `libm4ri-20100701.p1` from #9475 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4).\n\nSo I can give \"positive review\" from the technical side. ;-)",
    "created_at": "2010-08-13T09:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94824",
    "user": "leif"
}
```

Passed `ptestlong` with Sage 4.5.3.alpha0 and `libm4ri-20100701.p1` from #9475 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4).

So I can give "positive review" from the technical side. ;-)



---

archive/issue_comments_094825.json:
```json
{
    "body": "The updated `SPKG.txt` is ok, too. (And the upstream fixes also look reasonable btw.)",
    "created_at": "2010-08-13T10:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94825",
    "user": "leif"
}
```

The updated `SPKG.txt` is ok, too. (And the upstream fixes also look reasonable btw.)



---

archive/issue_comments_094826.json:
```json
{
    "body": "Replying to [comment:18 leif]:\n> The updated `SPKG.txt` is ok, too.\n\n... except for the date(s), but I'll assume the intention was to avoid naming Friday 13th and accept it. ;-)",
    "created_at": "2010-08-13T10:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94826",
    "user": "leif"
}
```

Replying to [comment:18 leif]:
> The updated `SPKG.txt` is ok, too.

... except for the date(s), but I'll assume the intention was to avoid naming Friday 13th and accept it. ;-)



---

archive/issue_comments_094827.json:
```json
{
    "body": "So we have a positive review then?",
    "created_at": "2010-08-13T11:59:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94827",
    "user": "malb"
}
```

So we have a positive review then?



---

archive/issue_comments_094828.json:
```json
{
    "body": "Replying to [comment:20 malb]:\n> So we have a positive review then?\n\nOnce Alexander's `testall` has finished, I think yes. :)\n\nI'll perhaps test later on a 64-bit platform, although I don't expect any issues.",
    "created_at": "2010-08-13T12:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94828",
    "user": "leif"
}
```

Replying to [comment:20 malb]:
> So we have a positive review then?

Once Alexander's `testall` has finished, I think yes. :)

I'll perhaps test later on a 64-bit platform, although I don't expect any issues.



---

archive/issue_comments_094829.json:
```json
{
    "body": "Replying to [comment:21 leif]:\n> I'll perhaps test later on a 64-bit platform, although I don't expect any issues.\n\nPassed all long tests in `sage/matrix`; currently running `make testlong`, but this will take some time since the system is already fully loaded... (Ubuntu 9.04 x86_64, Core2, gcc 4.3.3)",
    "created_at": "2010-08-13T12:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94829",
    "user": "leif"
}
```

Replying to [comment:21 leif]:
> I'll perhaps test later on a 64-bit platform, although I don't expect any issues.

Passed all long tests in `sage/matrix`; currently running `make testlong`, but this will take some time since the system is already fully loaded... (Ubuntu 9.04 x86_64, Core2, gcc 4.3.3)



---

archive/issue_comments_094830.json:
```json
{
    "body": "> Once Alexander's `testall` has finished, I think yes. :)\nThey have successfully finished (SuSE 11.1 64 Bits). So we have the positive review now",
    "created_at": "2010-08-13T14:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94830",
    "user": "AlexanderDreyer"
}
```

> Once Alexander's `testall` has finished, I think yes. :)
They have successfully finished (SuSE 11.1 64 Bits). So we have the positive review now



---

archive/issue_comments_094831.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-13T14:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94831",
    "user": "AlexanderDreyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094832.json:
```json
{
    "body": "## Note to the release managers\n\nI think this should (only) be merged together with #9475, but I'm not *that* sure.",
    "created_at": "2010-08-13T14:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94832",
    "user": "leif"
}
```

## Note to the release managers

I think this should (only) be merged together with #9475, but I'm not *that* sure.



---

archive/issue_comments_094833.json:
```json
{
    "body": "As expected, also passed `testlong` with Sage 4.5.3.alpha0 and #9475 on Ubuntu 9.04 x86_64 (Core2, gcc 4.3.3, native code, O2).",
    "created_at": "2010-08-13T16:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94833",
    "user": "leif"
}
```

As expected, also passed `testlong` with Sage 4.5.3.alpha0 and #9475 on Ubuntu 9.04 x86_64 (Core2, gcc 4.3.3, native code, O2).



---

archive/issue_comments_094834.json:
```json
{
    "body": "Ooops, I just noticed the [attached patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9717/polybori-0.6.4.p2.patch) is to the *Sage library* (I assumed it is an *spkg* patch). So I did **not** apply that patch in any of the tests I made, which despite that all passed...\n\nMartin, is that patch now obsolete or do we just not test an example which would fail without it? Or is it platform-specific?\n\n(Btw, the patch's commit message lacks a ticket number; also, a back-reference/comment in the code wouldn't be bad.)\n\nPerhaps you could add Joan Daemen's example to the ticket.",
    "created_at": "2010-08-13T17:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94834",
    "user": "leif"
}
```

Ooops, I just noticed the [attached patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9717/polybori-0.6.4.p2.patch) is to the *Sage library* (I assumed it is an *spkg* patch). So I did **not** apply that patch in any of the tests I made, which despite that all passed...

Martin, is that patch now obsolete or do we just not test an example which would fail without it? Or is it platform-specific?

(Btw, the patch's commit message lacks a ticket number; also, a back-reference/comment in the code wouldn't be bad.)

Perhaps you could add Joan Daemen's example to the ticket.



---

archive/issue_comments_094835.json:
```json
{
    "body": "Replying to [comment:26 leif]:\n\n> Ooops, I just noticed the [attached patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9717/polybori-0.6.4.p2.patch) is to the *Sage library* (I assumed it is an *spkg* patch). So I did **not** apply that patch in any of the tests I made, which despite that all passed... Martin, is that patch now obsolete or do we just not test an example which would fail without it?\n\nThe patch is necessary, Sage will SIGSEGV in some cases otherwise. I'll try to update the patch with an example.\n\n> Or is it platform-specific? (Btw, the patch's commit message lacks a ticket number; also, a back-reference/comment in the code wouldn't be bad.)\n\nI'll add the ticket number.\n\n> Perhaps you could add Joan Daemen's example to the ticket.\n\nThe problem is a bit bigger and I have no permission to publish it, sorry.",
    "created_at": "2010-08-14T12:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94835",
    "user": "malb"
}
```

Replying to [comment:26 leif]:

> Ooops, I just noticed the [attached patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9717/polybori-0.6.4.p2.patch) is to the *Sage library* (I assumed it is an *spkg* patch). So I did **not** apply that patch in any of the tests I made, which despite that all passed... Martin, is that patch now obsolete or do we just not test an example which would fail without it?

The patch is necessary, Sage will SIGSEGV in some cases otherwise. I'll try to update the patch with an example.

> Or is it platform-specific? (Btw, the patch's commit message lacks a ticket number; also, a back-reference/comment in the code wouldn't be bad.)

I'll add the ticket number.

> Perhaps you could add Joan Daemen's example to the ticket.

The problem is a bit bigger and I have no permission to publish it, sorry.



---

archive/issue_comments_094836.json:
```json
{
    "body": "I've updated the patch with an example and this ticket's number.",
    "created_at": "2010-08-14T12:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94836",
    "user": "malb"
}
```

I've updated the patch with an example and this ticket's number.



---

archive/issue_comments_094837.json:
```json
{
    "body": "Replying to [comment:28 malb]:\n> I've updated the patch with an example and this ticket's number.\n\nOk, I'll rerun some of the tests later. Currently all machines busy with new PARI testing... ;-)\n\n(I don't see the ticket number in the patched code though.)",
    "created_at": "2010-08-14T12:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94837",
    "user": "leif"
}
```

Replying to [comment:28 malb]:
> I've updated the patch with an example and this ticket's number.

Ok, I'll rerun some of the tests later. Currently all machines busy with new PARI testing... ;-)

(I don't see the ticket number in the patched code though.)



---

archive/issue_comments_094838.json:
```json
{
    "body": "\n```\n#9717 fixing parent ring in substitute_variable() (fix due to Alexander Dreyer)\n```\n\nThat's the commit message, is that alright?",
    "created_at": "2010-08-14T12:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94838",
    "user": "malb"
}
```


```
#9717 fixing parent ring in substitute_variable() (fix due to Alexander Dreyer)
```

That's the commit message, is that alright?



---

archive/issue_comments_094839.json:
```json
{
    "body": "And an attachment comment would be nice... (\"Sage library patch - ...\")\n\nI HATE TRAC! [concurrent \"editing\" grrrrr...]\n\n----\n\nI meant putting the ticket number also into a comment **in the code**; you don't see the commit messages when looking just at source files. E.g.\n\n```\n        ... # fixes #9717\n```\n\nor in the `TESTS::` section:\n\n```\n    Substitution is (now) also allowed with different rings (cf. #9717)::\n```\n\nSomething like that.",
    "created_at": "2010-08-14T13:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94839",
    "user": "leif"
}
```

And an attachment comment would be nice... ("Sage library patch - ...")

I HATE TRAC! [concurrent "editing" grrrrr...]

----

I meant putting the ticket number also into a comment **in the code**; you don't see the commit messages when looking just at source files. E.g.

```
        ... # fixes #9717
```

or in the `TESTS::` section:

```
    Substitution is (now) also allowed with different rings (cf. #9717)::
```

Something like that.



---

archive/issue_comments_094840.json:
```json
{
    "body": "I'm not too convinced by that. This was a serious bug which just wasn't reported to far. I don't want to clutter the code with track ticket numbers. When reading the code it is relatively simple to see (I'd say) that the new code is correct, thus I'd say it doesn't need a ticket to explain why it is there. Also, the new example isn't just a test, it shows a real use case.",
    "created_at": "2010-08-14T13:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94840",
    "user": "malb"
}
```

I'm not too convinced by that. This was a serious bug which just wasn't reported to far. I don't want to clutter the code with track ticket numbers. When reading the code it is relatively simple to see (I'd say) that the new code is correct, thus I'd say it doesn't need a ticket to explain why it is there. Also, the new example isn't just a test, it shows a real use case.



---

archive/issue_comments_094841.json:
```json
{
    "body": "Sage library patch fixing an issue with substitute_variable()",
    "created_at": "2010-08-14T13:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94841",
    "user": "malb"
}
```

Sage library patch fixing an issue with substitute_variable()



---

archive/issue_comments_094842.json:
```json
{
    "body": "Attachment [polybori-0.6.4.p2.patch](tarball://root/attachments/some-uuid/ticket9717/polybori-0.6.4.p2.patch) by leif created at 2010-08-14 14:48:44",
    "created_at": "2010-08-14T14:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94842",
    "user": "leif"
}
```

Attachment [polybori-0.6.4.p2.patch](tarball://root/attachments/some-uuid/ticket9717/polybori-0.6.4.p2.patch) by leif created at 2010-08-14 14:48:44



---

archive/issue_comments_094843.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-15T08:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94843",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_094844.json:
```json
{
    "body": "How does one run PolyBoRi's test suite?  I'm curious about whether we can add an `spkg-check` file (at a new ticket).",
    "created_at": "2010-08-17T07:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94844",
    "user": "mpatel"
}
```

How does one run PolyBoRi's test suite?  I'm curious about whether we can add an `spkg-check` file (at a new ticket).



---

archive/issue_comments_094845.json:
```json
{
    "body": "The testsuite, which is included in PolyBoRi is not up to date, we use another suite for developing internally. On the one hand, it is lange, on the other, some examples are not freely available. We'll try to deliver a suitable subset of the examples in the future.",
    "created_at": "2010-08-17T08:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94845",
    "user": "AlexanderDreyer"
}
```

The testsuite, which is included in PolyBoRi is not up to date, we use another suite for developing internally. On the one hand, it is lange, on the other, some examples are not freely available. We'll try to deliver a suitable subset of the examples in the future.
