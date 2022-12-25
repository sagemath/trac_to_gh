# Issue 9717: fix variable substitution in PolyBoRi

archive/issues_009717.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  polybori alexanderdreyer @nexttime @qed777\n\nFor some inputs our[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) wrapper throws an error while upstream computes the example just fine. The reason we fail is that some rings don't match and thus coercion goes wrong. The problem was reported by Joan Daemen who also provided an example via private communication.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9717\n\n",
    "created_at": "2010-08-10T12:43:40Z",
    "labels": [
        "component: commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "fix variable substitution in PolyBoRi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9717",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  polybori alexanderdreyer @nexttime @qed777

For some inputs our[This is the Trac macro *PolyBoRi* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#PolyBoRi-macro) wrapper throws an error while upstream computes the example just fine. The reason we fail is that some rings don't match and thus coercion goes wrong. The problem was reported by Joan Daemen who also provided an example via private communication.

Issue created by migration from https://trac.sagemath.org/ticket/9717





---

archive/issue_comments_094647.json:
```json
{
    "body": "Alexander Dreyer provided a fix for the issue. I've packaged this fix into an SPKG\n\n\u00a0http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p2.spkg\n\nI've also packaged his patch for Sage into a proper mercurial patch which I'll attach in a sec.",
    "created_at": "2010-08-10T12:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94647",
    "user": "https://github.com/malb"
}
```

Alexander Dreyer provided a fix for the issue. I've packaged this fix into an SPKG

 http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p2.spkg

I've also packaged his patch for Sage into a proper mercurial patch which I'll attach in a sec.



---

archive/issue_comments_094648.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-08-10T12:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94648",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_094649.json:
```json
{
    "body": "The attached patch + SPKG fix the original problem, however I'm getting segfaults now:\n\n```\nProgram received signal SIGSEGV, Segmentation fault.\nlinalg_step_modified (polys=<value optimized out>, terms=<value optimized out>, \n    leads_from_strat=<value optimized out>, log=<value optimized out>, \n    optDrawMatrices=<value optimized out>, matrixPrefix=<value optimized out>)\n    at groebner/src/nf.cc:2270\n2270    groebner/src/nf.cc: No such file or directory.\n        in groebner/src/nf.cc\nCurrent language:  auto\nThe current source language is \"auto; currently c++\".\n(gdb) bt\n#0  linalg_step_modified (polys=<value optimized out>, terms=<value optimized out>, \n    leads_from_strat=<value optimized out>, log=<value optimized out>, \n    optDrawMatrices=<value optimized out>, matrixPrefix=<value optimized out>)\n    at groebner/src/nf.cc:2270\n#1  0x00007fffcf4f6c56 in polybori::groebner::GroebnerStrategy::faugereStepDense (\n    this=<value optimized out>, orig_system=<value optimized out>) at groebner/src/nf.cc:2386\n#2  0x00007fffcf3e2a0d in __pyx_pf_4sage_5rings_10polynomial_5pbori_16GroebnerStrategy_faugere_step_dense (__pyx_v_self=0x5997520, __pyx_v_v=0x12bf3500) at sage/rings/polynomial/pbori.cpp:31846\n#3  0x00007ffff7b11316 in call_function (f=0x418a900, throwflag=<value optimized out>)\n    at Python/ceval.c:3694\n\n```",
    "created_at": "2010-08-10T12:49:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94649",
    "user": "https://github.com/malb"
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

archive/issue_comments_094650.json:
```json
{
    "body": "Ignore the SIGSEGV above, it is unrelated to this ticket but is caused by #9562.\u00a0\n\nAlexander, can you review my SPKG + patch, i.e. that it does what you intended? I give your changes a positive review so all that's needed is some check whether I produced the SPKG correctly etc.",
    "created_at": "2010-08-10T13:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94650",
    "user": "https://github.com/malb"
}
```

Ignore the SIGSEGV above, it is unrelated to this ticket but is caused by #9562. 

Alexander, can you review my SPKG + patch, i.e. that it does what you intended? I give your changes a positive review so all that's needed is some check whether I produced the SPKG correctly etc.



---

archive/issue_comments_094651.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-10T13:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94651",
    "user": "https://github.com/malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094652.json:
```json
{
    "body": "Use this SPKG instead (it is based on the latest PolyBoRi SPKG which the previous SPKG wasn't)\u00a0\n\n\u00a0http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p3.spkg",
    "created_at": "2010-08-10T15:08:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94652",
    "user": "https://github.com/malb"
}
```

Use this SPKG instead (it is based on the latest PolyBoRi SPKG which the previous SPKG wasn't) 

 http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p3.spkg



---

archive/issue_comments_094653.json:
```json
{
    "body": "There was some unrelated issue with the previous spkg (libm4ri was not found, because Sage's lib directory was not given to PolyBoRi)\nI updated the spkg accordingly:\nhttp://sage.math.washington.edu/home/dreyer/pb/polybori-0.6.4.p4.spkg",
    "created_at": "2010-08-10T21:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94653",
    "user": "https://github.com/alexanderdreyer"
}
```

There was some unrelated issue with the previous spkg (libm4ri was not found, because Sage's lib directory was not given to PolyBoRi)
I updated the spkg accordingly:
http://sage.math.washington.edu/home/dreyer/pb/polybori-0.6.4.p4.spkg



---

archive/issue_comments_094654.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-11T12:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94654",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_094655.json:
```json
{
    "body": "`SPKG.txt` has to be updated for p4.\n\nAlexander's patch looks reasonable, though libm4ri (and the GD library) were previously found (in the second attempt)... (The only issue I'm aware of is with updating from 4.5.2 on MacOS X 10.6, which Mitesh Patel couldn't reproduce either; see #9721.)\n\n(The change to p4 is of course unrelated to the original intent of this ticket; perhaps adapt its title, too.)",
    "created_at": "2010-08-11T12:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94655",
    "user": "https://github.com/nexttime"
}
```

`SPKG.txt` has to be updated for p4.

Alexander's patch looks reasonable, though libm4ri (and the GD library) were previously found (in the second attempt)... (The only issue I'm aware of is with updating from 4.5.2 on MacOS X 10.6, which Mitesh Patel couldn't reproduce either; see #9721.)

(The change to p4 is of course unrelated to the original intent of this ticket; perhaps adapt its title, too.)



---

archive/issue_comments_094656.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n\n> `SPKG.txt` has to be updated for p4.\n\n\nI have a new SPKG which does exactly that. I'll upload it later.\n\n> Alexander's patch looks reasonable, though libm4ri (and the GD library) were previously found (in the second attempt)... (The only issue I'm aware of is with updating from 4.5.2 on MacOS X 10.6, which Mitesh Patel couldn't reproduce either; see #9721.) (The change to p4 is of course unrelated to the original intent of this ticket; perhaps adapt its title, too.)",
    "created_at": "2010-08-11T13:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94656",
    "user": "https://github.com/malb"
}
```

Replying to [comment:8 leif]:

> `SPKG.txt` has to be updated for p4.


I have a new SPKG which does exactly that. I'll upload it later.

> Alexander's patch looks reasonable, though libm4ri (and the GD library) were previously found (in the second attempt)... (The only issue I'm aware of is with updating from 4.5.2 on MacOS X 10.6, which Mitesh Patel couldn't reproduce either; see #9721.) (The change to p4 is of course unrelated to the original intent of this ticket; perhaps adapt its title, too.)



---

archive/issue_comments_094657.json:
```json
{
    "body": "The new SPKG is here\n\n\u00a0http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p4.spkg\n\nI just added an entry to SPKG.txt",
    "created_at": "2010-08-11T13:30:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94657",
    "user": "https://github.com/malb"
}
```

The new SPKG is here

 http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p4.spkg

I just added an entry to SPKG.txt



---

archive/issue_comments_094658.json:
```json
{
    "body": "PolyBoRi makes assumptions about M4RI which are not met with the newest upstream release (#9475). Thus, we should fix this here asap since the new M4RI is about to go in.",
    "created_at": "2010-08-11T18:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94658",
    "user": "https://github.com/malb"
}
```

PolyBoRi makes assumptions about M4RI which are not met with the newest upstream release (#9475). Thus, we should fix this here asap since the new M4RI is about to go in.



---

archive/issue_comments_094659.json:
```json
{
    "body": "I've replaced the SPKG here\u00a0\n\n\u00a0 \u00a0http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p4.spkg\n\nand the new SPKG fixes the SIGSEGV and all doctests pass.\n\nThese fixes are:\n\n\u00a0http://bitbucket.org/brickenstein/polybori/changeset/6ef7402d935b\n\n\u00a0http://bitbucket.org/brickenstein/polybori/changeset/b692c8181e94",
    "created_at": "2010-08-12T18:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94659",
    "user": "https://github.com/malb"
}
```

I've replaced the SPKG here 

   http://sage.math.washington.edu/home/malb/spkgs/polybori-0.6.4.p4.spkg

and the new SPKG fixes the SIGSEGV and all doctests pass.

These fixes are:

 http://bitbucket.org/brickenstein/polybori/changeset/6ef7402d935b

 http://bitbucket.org/brickenstein/polybori/changeset/b692c8181e94



---

archive/issue_comments_094660.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-12T18:48:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94660",
    "user": "https://github.com/malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094661.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-13T02:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94661",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_094662.json:
```json
{
    "body": "`Work issues` field ( = *\"Update `SPKG.txt`\"*) still (or again) valid... ;-)\n\n(Perhaps also add this ticket number, and mention the PolyBoRi upstream fixes there.)",
    "created_at": "2010-08-13T02:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94662",
    "user": "https://github.com/nexttime"
}
```

`Work issues` field ( = *"Update `SPKG.txt`"*) still (or again) valid... ;-)

(Perhaps also add this ticket number, and mention the PolyBoRi upstream fixes there.)



---

archive/issue_comments_094663.json:
```json
{
    "body": "Updated accordingly.",
    "created_at": "2010-08-13T08:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94663",
    "user": "https://github.com/malb"
}
```

Updated accordingly.



---

archive/issue_comments_094664.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-13T08:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94664",
    "user": "https://github.com/malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094665.json:
```json
{
    "body": "Meanwhile, I took a look at the surrounding code also. (Just to ensure, that the patches also do the right thing in other contexts.) It's a good patch and it may fix even more issues. So I give a positive review from the mathematical point of view. (If I'm allowed to do so.) For the technical viewpoint: I'm waiting now for `sage -testall` to finish.",
    "created_at": "2010-08-13T09:02:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94665",
    "user": "https://github.com/alexanderdreyer"
}
```

Meanwhile, I took a look at the surrounding code also. (Just to ensure, that the patches also do the right thing in other contexts.) It's a good patch and it may fix even more issues. So I give a positive review from the mathematical point of view. (If I'm allowed to do so.) For the technical viewpoint: I'm waiting now for `sage -testall` to finish.



---

archive/issue_comments_094666.json:
```json
{
    "body": "Passed `ptestlong` with Sage 4.5.3.alpha0 and `libm4ri-20100701.p1` from #9475 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4).\n\nSo I can give \"positive review\" from the technical side. ;-)",
    "created_at": "2010-08-13T09:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94666",
    "user": "https://github.com/nexttime"
}
```

Passed `ptestlong` with Sage 4.5.3.alpha0 and `libm4ri-20100701.p1` from #9475 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4).

So I can give "positive review" from the technical side. ;-)



---

archive/issue_comments_094667.json:
```json
{
    "body": "The updated `SPKG.txt` is ok, too. (And the upstream fixes also look reasonable btw.)",
    "created_at": "2010-08-13T10:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94667",
    "user": "https://github.com/nexttime"
}
```

The updated `SPKG.txt` is ok, too. (And the upstream fixes also look reasonable btw.)



---

archive/issue_comments_094668.json:
```json
{
    "body": "Replying to [comment:18 leif]:\n> The updated `SPKG.txt` is ok, too.\n\n\n... except for the date(s), but I'll assume the intention was to avoid naming Friday 13th and accept it. ;-)",
    "created_at": "2010-08-13T10:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94668",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:18 leif]:
> The updated `SPKG.txt` is ok, too.


... except for the date(s), but I'll assume the intention was to avoid naming Friday 13th and accept it. ;-)



---

archive/issue_comments_094669.json:
```json
{
    "body": "So we have a positive review then?",
    "created_at": "2010-08-13T11:59:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94669",
    "user": "https://github.com/malb"
}
```

So we have a positive review then?



---

archive/issue_comments_094670.json:
```json
{
    "body": "Replying to [comment:20 malb]:\n> So we have a positive review then?\n\n\nOnce Alexander's `testall` has finished, I think yes. :)\n\nI'll perhaps test later on a 64-bit platform, although I don't expect any issues.",
    "created_at": "2010-08-13T12:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94670",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:20 malb]:
> So we have a positive review then?


Once Alexander's `testall` has finished, I think yes. :)

I'll perhaps test later on a 64-bit platform, although I don't expect any issues.



---

archive/issue_comments_094671.json:
```json
{
    "body": "Replying to [comment:21 leif]:\n> I'll perhaps test later on a 64-bit platform, although I don't expect any issues.\n\n\nPassed all long tests in `sage/matrix`; currently running `make testlong`, but this will take some time since the system is already fully loaded... (Ubuntu 9.04 x86_64, Core2, gcc 4.3.3)",
    "created_at": "2010-08-13T12:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94671",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:21 leif]:
> I'll perhaps test later on a 64-bit platform, although I don't expect any issues.


Passed all long tests in `sage/matrix`; currently running `make testlong`, but this will take some time since the system is already fully loaded... (Ubuntu 9.04 x86_64, Core2, gcc 4.3.3)



---

archive/issue_comments_094672.json:
```json
{
    "body": "> Once Alexander's `testall` has finished, I think yes. :)\n\nThey have successfully finished (SuSE 11.1 64 Bits). So we have the positive review now",
    "created_at": "2010-08-13T14:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94672",
    "user": "https://github.com/alexanderdreyer"
}
```

> Once Alexander's `testall` has finished, I think yes. :)

They have successfully finished (SuSE 11.1 64 Bits). So we have the positive review now



---

archive/issue_comments_094673.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-13T14:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94673",
    "user": "https://github.com/alexanderdreyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094674.json:
```json
{
    "body": "## Note to the release managers\n\nI think this should (only) be merged together with #9475, but I'm not *that* sure.",
    "created_at": "2010-08-13T14:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94674",
    "user": "https://github.com/nexttime"
}
```

## Note to the release managers

I think this should (only) be merged together with #9475, but I'm not *that* sure.



---

archive/issue_comments_094675.json:
```json
{
    "body": "As expected, also passed `testlong` with Sage 4.5.3.alpha0 and #9475 on Ubuntu 9.04 x86_64 (Core2, gcc 4.3.3, native code, O2).",
    "created_at": "2010-08-13T16:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94675",
    "user": "https://github.com/nexttime"
}
```

As expected, also passed `testlong` with Sage 4.5.3.alpha0 and #9475 on Ubuntu 9.04 x86_64 (Core2, gcc 4.3.3, native code, O2).



---

archive/issue_comments_094676.json:
```json
{
    "body": "Ooops, I just noticed the [attached patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9717/polybori-0.6.4.p2.patch) is to the *Sage library* (I assumed it is an *spkg* patch). So I did **not** apply that patch in any of the tests I made, which despite that all passed...\n\nMartin, is that patch now obsolete or do we just not test an example which would fail without it? Or is it platform-specific?\n\n(Btw, the patch's commit message lacks a ticket number; also, a back-reference/comment in the code wouldn't be bad.)\n\nPerhaps you could add Joan Daemen's example to the ticket.",
    "created_at": "2010-08-13T17:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94676",
    "user": "https://github.com/nexttime"
}
```

Ooops, I just noticed the [attached patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9717/polybori-0.6.4.p2.patch) is to the *Sage library* (I assumed it is an *spkg* patch). So I did **not** apply that patch in any of the tests I made, which despite that all passed...

Martin, is that patch now obsolete or do we just not test an example which would fail without it? Or is it platform-specific?

(Btw, the patch's commit message lacks a ticket number; also, a back-reference/comment in the code wouldn't be bad.)

Perhaps you could add Joan Daemen's example to the ticket.



---

archive/issue_comments_094677.json:
```json
{
    "body": "Replying to [comment:26 leif]:\n\n> Ooops, I just noticed the [attached patch](http://trac.sagemath.org/sage_trac/attachment/ticket/9717/polybori-0.6.4.p2.patch) is to the *Sage library* (I assumed it is an *spkg* patch). So I did **not** apply that patch in any of the tests I made, which despite that all passed... Martin, is that patch now obsolete or do we just not test an example which would fail without it?\n\n\nThe patch is necessary, Sage will SIGSEGV in some cases otherwise. I'll try to update the patch with an example.\n\n> Or is it platform-specific? (Btw, the patch's commit message lacks a ticket number; also, a back-reference/comment in the code wouldn't be bad.)\n\n\nI'll add the ticket number.\n\n> Perhaps you could add Joan Daemen's example to the ticket.\n\n\nThe problem is a bit bigger and I have no permission to publish it, sorry.",
    "created_at": "2010-08-14T12:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94677",
    "user": "https://github.com/malb"
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

archive/issue_comments_094678.json:
```json
{
    "body": "I've updated the patch with an example and this ticket's number.",
    "created_at": "2010-08-14T12:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94678",
    "user": "https://github.com/malb"
}
```

I've updated the patch with an example and this ticket's number.



---

archive/issue_comments_094679.json:
```json
{
    "body": "Replying to [comment:28 malb]:\n> I've updated the patch with an example and this ticket's number.\n\n\nOk, I'll rerun some of the tests later. Currently all machines busy with new PARI testing... ;-)\n\n(I don't see the ticket number in the patched code though.)",
    "created_at": "2010-08-14T12:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94679",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:28 malb]:
> I've updated the patch with an example and this ticket's number.


Ok, I'll rerun some of the tests later. Currently all machines busy with new PARI testing... ;-)

(I don't see the ticket number in the patched code though.)



---

archive/issue_comments_094680.json:
```json
{
    "body": "```\n#9717 fixing parent ring in substitute_variable() (fix due to Alexander Dreyer)\n```\nThat's the commit message, is that alright?",
    "created_at": "2010-08-14T12:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94680",
    "user": "https://github.com/malb"
}
```

```
#9717 fixing parent ring in substitute_variable() (fix due to Alexander Dreyer)
```
That's the commit message, is that alright?



---

archive/issue_comments_094681.json:
```json
{
    "body": "And an attachment comment would be nice... (\"Sage library patch - ...\")\n\nI HATE TRAC! [concurrent \"editing\" grrrrr...]\n\n---\n\nI meant putting the ticket number also into a comment **in the code**; you don't see the commit messages when looking just at source files. E.g.\n\n```\n        ... # fixes #9717\n```\nor in the `TESTS::` section:\n\n```\n    Substitution is (now) also allowed with different rings (cf. #9717)::\n```\nSomething like that.",
    "created_at": "2010-08-14T13:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94681",
    "user": "https://github.com/nexttime"
}
```

And an attachment comment would be nice... ("Sage library patch - ...")

I HATE TRAC! [concurrent "editing" grrrrr...]

---

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

archive/issue_comments_094682.json:
```json
{
    "body": "I'm not too convinced by that. This was a serious bug which just wasn't reported to far. I don't want to clutter the code with track ticket numbers. When reading the code it is relatively simple to see (I'd say) that the new code is correct, thus I'd say it doesn't need a ticket to explain why it is there. Also, the new example isn't just a test, it shows a real use case.",
    "created_at": "2010-08-14T13:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94682",
    "user": "https://github.com/malb"
}
```

I'm not too convinced by that. This was a serious bug which just wasn't reported to far. I don't want to clutter the code with track ticket numbers. When reading the code it is relatively simple to see (I'd say) that the new code is correct, thus I'd say it doesn't need a ticket to explain why it is there. Also, the new example isn't just a test, it shows a real use case.



---

archive/issue_comments_094683.json:
```json
{
    "body": "Sage library patch fixing an issue with substitute_variable()",
    "created_at": "2010-08-14T13:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94683",
    "user": "https://github.com/malb"
}
```

Sage library patch fixing an issue with substitute_variable()



---

archive/issue_comments_094684.json:
```json
{
    "body": "Attachment [polybori-0.6.4.p2.patch](tarball://root/attachments/some-uuid/ticket9717/polybori-0.6.4.p2.patch) by @nexttime created at 2010-08-14 14:48:44",
    "created_at": "2010-08-14T14:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94684",
    "user": "https://github.com/nexttime"
}
```

Attachment [polybori-0.6.4.p2.patch](tarball://root/attachments/some-uuid/ticket9717/polybori-0.6.4.p2.patch) by @nexttime created at 2010-08-14 14:48:44



---

archive/issue_comments_094685.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-15T08:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94685",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_024309.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-15T08:03:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9717#event-24309"
}
```



---

archive/issue_comments_094686.json:
```json
{
    "body": "How does one run PolyBoRi's test suite?  I'm curious about whether we can add an `spkg-check` file (at a new ticket).",
    "created_at": "2010-08-17T07:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94686",
    "user": "https://github.com/qed777"
}
```

How does one run PolyBoRi's test suite?  I'm curious about whether we can add an `spkg-check` file (at a new ticket).



---

archive/issue_comments_094687.json:
```json
{
    "body": "The testsuite, which is included in PolyBoRi is not up to date, we use another suite for developing internally. On the one hand, it is lange, on the other, some examples are not freely available. We'll try to deliver a suitable subset of the examples in the future.",
    "created_at": "2010-08-17T08:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9717",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9717#issuecomment-94687",
    "user": "https://github.com/alexanderdreyer"
}
```

The testsuite, which is included in PolyBoRi is not up to date, we use another suite for developing internally. On the one hand, it is lange, on the other, some examples are not freely available. We'll try to deliver a suitable subset of the examples in the future.
