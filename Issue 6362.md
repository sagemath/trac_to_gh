# Issue 6362: [with spkg, needs review] Singular and GCC 4.4

archive/issues_006362.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @malb\n\nsingular is last package that don't compile with latest GCC 4.4 for me, it's because of use of strchr function, see GCC 4.4 [porting guide](http://gcc.gnu.org/gcc-4.4/porting_to.html) part \"Strict null-terminated sequence utilities\" - there is used\n\nchar* strchr(const char*, int)\n\nthat silently cast-away const, simple explicit cast to char* removes the error during compilation for me so it's trivial to fix. The strchr function in this form is used twice. \n\nI made spkg that's fixed, wasn't creating patches/spkg for Sage for some time so I ask for strict review even if it's trivial fix :) I tried to remember about everything with spkg creation but something could still slip. There is spkg: [http://giniu.ravenlord.ws/singular-3-1-0-2-20090620.spkg](http://giniu.ravenlord.ws/singular-3-1-0-2-20090620.spkg).\n\nIssue created by migration from https://trac.sagemath.org/ticket/6362\n\n",
    "created_at": "2009-06-20T08:22:16Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[with spkg, needs review] Singular and GCC 4.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6362",
    "user": "aginiewicz"
}
```
Assignee: tbd

CC:  @malb

singular is last package that don't compile with latest GCC 4.4 for me, it's because of use of strchr function, see GCC 4.4 [porting guide](http://gcc.gnu.org/gcc-4.4/porting_to.html) part "Strict null-terminated sequence utilities" - there is used

char* strchr(const char*, int)

that silently cast-away const, simple explicit cast to char* removes the error during compilation for me so it's trivial to fix. The strchr function in this form is used twice. 

I made spkg that's fixed, wasn't creating patches/spkg for Sage for some time so I ask for strict review even if it's trivial fix :) I tried to remember about everything with spkg creation but something could still slip. There is spkg: [http://giniu.ravenlord.ws/singular-3-1-0-2-20090620.spkg](http://giniu.ravenlord.ws/singular-3-1-0-2-20090620.spkg).

Issue created by migration from https://trac.sagemath.org/ticket/6362





---

archive/issue_comments_050877.json:
```json
{
    "body": "I'm adding Martin to the cc here, because I think he's going to be looking at the Singular spkg soon (for #6240).",
    "created_at": "2009-06-20T08:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50877",
    "user": "@craigcitro"
}
```

I'm adding Martin to the cc here, because I think he's going to be looking at the Singular spkg soon (for #6240).



---

archive/issue_comments_050878.json:
```json
{
    "body": "I sent an email to singular`@`mathematik.uni-kl.de about this ticket as well.",
    "created_at": "2009-06-20T10:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50878",
    "user": "@williamstein"
}
```

I sent an email to singular`@`mathematik.uni-kl.de about this ticket as well.



---

archive/issue_comments_050879.json:
```json
{
    "body": "The spkg allowed me to compile sage on my machine, and it appears to be working. What would constitute a strict test?",
    "created_at": "2009-06-21T22:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50879",
    "user": "@johnperry-math"
}
```

The spkg allowed me to compile sage on my machine, and it appears to be working. What would constitute a strict test?



---

archive/issue_comments_050880.json:
```json
{
    "body": "There is problem that one cannot provide testcase... i.e. the issue is during compile time, if the compiler allows used syntax, that is casting away const trough strchr function, it still generates code that's safe because in this code the pointer isn't used in any malicious way, so if it compiles - with or without patch - one cannot tell the difference, probably even looking at assembler code. But on other hand, GCC 4.4 don't allow implicit const cast-away trough string manipulation functions (which is good thing in my opinion) so it fails to build without patch.",
    "created_at": "2009-06-21T22:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50880",
    "user": "aginiewicz"
}
```

There is problem that one cannot provide testcase... i.e. the issue is during compile time, if the compiler allows used syntax, that is casting away const trough strchr function, it still generates code that's safe because in this code the pointer isn't used in any malicious way, so if it compiles - with or without patch - one cannot tell the difference, probably even looking at assembler code. But on other hand, GCC 4.4 don't allow implicit const cast-away trough string manipulation functions (which is good thing in my opinion) so it fails to build without patch.



---

archive/issue_comments_050881.json:
```json
{
    "body": "I told upstream about this bug and they replied:\n\n```\nThanks for the patch - we agree with it\nand have integrated it into Singular.\n -- Hans Schoenemann\n```\n\n\nThat's a positive review from the singular project director.",
    "created_at": "2009-06-23T13:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50881",
    "user": "@williamstein"
}
```

I told upstream about this bug and they replied:

```
Thanks for the patch - we agree with it
and have integrated it into Singular.
 -- Hans Schoenemann
```


That's a positive review from the singular project director.



---

archive/issue_comments_050882.json:
```json
{
    "body": "Hmm... so this is positive review for patch, or we wait for upstream to fix it to not create too many patches?",
    "created_at": "2009-06-25T17:44:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50882",
    "user": "aginiewicz"
}
```

Hmm... so this is positive review for patch, or we wait for upstream to fix it to not create too many patches?



---

archive/issue_comments_050883.json:
```json
{
    "body": "We should patch it, but the next Singular SPKG needs a couple of other fixes applied (and updated to 3-1-0-4) this is I guess why it is taking so long.\n\nMy current attempt is here:\n\n  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090611.spkg\n\nIt needs a fix applied where the ring variables print without a space. Do you want to merge your patch with that SPKG?\n\nMartin",
    "created_at": "2009-06-25T17:57:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50883",
    "user": "@malb"
}
```

We should patch it, but the next Singular SPKG needs a couple of other fixes applied (and updated to 3-1-0-4) this is I guess why it is taking so long.

My current attempt is here:

  http://sage.math.washington.edu/home/malb/spkgs/singular-3-1-0-4-20090611.spkg

It needs a fix applied where the ring variables print without a space. Do you want to merge your patch with that SPKG?

Martin



---

archive/issue_comments_050884.json:
```json
{
    "body": "Sure, I will try to merge tomorrow in my local copy",
    "created_at": "2009-06-25T20:14:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50884",
    "user": "aginiewicz"
}
```

Sure, I will try to merge tomorrow in my local copy



---

archive/issue_comments_050885.json:
```json
{
    "body": "Hmm... so fix for #6360 is no longer needed with 3-1-0-4? I ask because I noticed in your spkg fix for it is erased from mercurial history, i.e. the change by Craig from 19'th?",
    "created_at": "2009-06-26T18:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50885",
    "user": "aginiewicz"
}
```

Hmm... so fix for #6360 is no longer needed with 3-1-0-4? I ask because I noticed in your spkg fix for it is erased from mercurial history, i.e. the change by Craig from 19'th?



---

archive/issue_comments_050886.json:
```json
{
    "body": "Good catch. It is still needed I just forgot to apply it!",
    "created_at": "2009-06-26T18:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50886",
    "user": "@malb"
}
```

Good catch. It is still needed I just forgot to apply it!



---

archive/issue_comments_050887.json:
```json
{
    "body": "Will you provide new version with this change (rebased on top of #6360?) or should I merge both to that gcc one? Sorry if this should be obvious, long break still have it's effects",
    "created_at": "2009-06-26T20:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50887",
    "user": "aginiewicz"
}
```

Will you provide new version with this change (rebased on top of #6360?) or should I merge both to that gcc one? Sorry if this should be obvious, long break still have it's effects



---

archive/issue_comments_050888.json:
```json
{
    "body": "Sorry, I was not very clear. It would be nice if you could re-merge it as I am in the middle of another project. If you can't get around to do it, I'll do it eventually.",
    "created_at": "2009-06-26T23:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50888",
    "user": "@malb"
}
```

Sorry, I was not very clear. It would be nice if you could re-merge it as I am in the middle of another project. If you can't get around to do it, I'll do it eventually.



---

archive/issue_comments_050889.json:
```json
{
    "body": "No problem, I will take care of it then",
    "created_at": "2009-06-27T07:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50889",
    "user": "aginiewicz"
}
```

No problem, I will take care of it then



---

archive/issue_comments_050890.json:
```json
{
    "body": "I merged the changes with Martins version (rebased actually) - there is spkg - http://giniu.ravenlord.ws/singular-3-1-0-4-20090620.spkg",
    "created_at": "2009-06-27T08:44:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50890",
    "user": "aginiewicz"
}
```

I merged the changes with Martins version (rebased actually) - there is spkg - http://giniu.ravenlord.ws/singular-3-1-0-4-20090620.spkg



---

archive/issue_comments_050891.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-07-01T11:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50891",
    "user": "@williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_050892.json:
```json
{
    "body": "I checked the changes (after some tutoring from was and jhpalmieri) against the default package included with 4.0.2, released 18 Jun and against the source included with the spkg.\n\nIs there an error in line 725 of patches/mpr_complex.cc? The original source file src/kernel/mpr_complex.cc contains\n\n```\n          sprintf(out,\"%s\",currRing->parameter[0]);\n```\n\nbut the patch contains\n\n```\n          sprintf(out,currRing->parameter[0]);\n```\n\nWhat happened to the \"%s\"? I thought that was required.\n\nEverything else looks fine.",
    "created_at": "2009-07-03T05:44:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50892",
    "user": "@johnperry-math"
}
```

I checked the changes (after some tutoring from was and jhpalmieri) against the default package included with 4.0.2, released 18 Jun and against the source included with the spkg.

Is there an error in line 725 of patches/mpr_complex.cc? The original source file src/kernel/mpr_complex.cc contains

```
          sprintf(out,"%s",currRing->parameter[0]);
```

but the patch contains

```
          sprintf(out,currRing->parameter[0]);
```

What happened to the "%s"? I thought that was required.

Everything else looks fine.



---

archive/issue_comments_050893.json:
```json
{
    "body": "... it must have slipped by, i.e. it was probably change upstream that I didn't noticed when merge of mine and Martins packages. I will take care of it right now.",
    "created_at": "2009-07-03T12:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50893",
    "user": "aginiewicz"
}
```

... it must have slipped by, i.e. it was probably change upstream that I didn't noticed when merge of mine and Martins packages. I will take care of it right now.



---

archive/issue_comments_050894.json:
```json
{
    "body": "Ok, fixed it. New spkg is at http://giniu.ravenlord.ws/singular-3-1-0-4-20090703.spkg",
    "created_at": "2009-07-03T13:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50894",
    "user": "aginiewicz"
}
```

Ok, fixed it. New spkg is at http://giniu.ravenlord.ws/singular-3-1-0-4-20090703.spkg



---

archive/issue_comments_050895.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-07-03T15:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50895",
    "user": "@johnperry-math"
}
```

Looks good to me.



---

archive/issue_comments_050896.json:
```json
{
    "body": "Fixed description in ticked to make sure which one is latest, as with Johns review link to spkg got reverted to not latest version.",
    "created_at": "2009-07-03T15:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50896",
    "user": "aginiewicz"
}
```

Fixed description in ticked to make sure which one is latest, as with Johns review link to spkg got reverted to not latest version.



---

archive/issue_comments_050897.json:
```json
{
    "body": "The spkg causes several doctest failures when built on sage-4.1.alpha3:\n\n```\n        sage -t -long devel/sage/sage/rings/quotient_ring.py # 1 doctests failed\n        sage -t -long devel/sage/sage/rings/quotient_ring_element.py # 1 doctests failed\n        sage -t -long devel/sage/sage/rings/polynomial/term_order.py # 1 doctests failed\n        sage -t -long devel/sage/sage/rings/polynomial/polynomial_singular_interface.py # 6 doctests failed\n        sage -t -long devel/sage/sage/rings/polynomial/pbori.pyx # 1 doctests failed\n        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 11 doctests failed\n        sage -t -long devel/sage/sage/interfaces/singular.py # 10 doctests failed\n```\n\n\nThese all seem to be just from the way Singular is printing things, e.g.:\n\n```\n**********************************************************************\nFile \"/space/rlm/sage-4.1.alpha3/devel/sage-main/sage/interfaces/singular.py\", line 975:\n    sage: singular.current_ring()\nExpected:\n    //   characteristic : 127\n    //   number of vars : 3\n    //        block   1 : ordering rp\n    //                  : names    x y z\n    //        block   2 : ordering C\nGot:\n    //   characteristic : 127\n    //   number of vars : 3\n    //        block   1 : ordering rp\n    //                  : names    xyz\n    //        block   2 : ordering C\n**********************************************************************\n```\n\n\nI assume this is nothing major. If someone wants to post a patch, I will gladly finish the review.",
    "created_at": "2009-07-03T16:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50897",
    "user": "@rlmill"
}
```

The spkg causes several doctest failures when built on sage-4.1.alpha3:

```
        sage -t -long devel/sage/sage/rings/quotient_ring.py # 1 doctests failed
        sage -t -long devel/sage/sage/rings/quotient_ring_element.py # 1 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/term_order.py # 1 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/polynomial_singular_interface.py # 6 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/pbori.pyx # 1 doctests failed
        sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 11 doctests failed
        sage -t -long devel/sage/sage/interfaces/singular.py # 10 doctests failed
```


These all seem to be just from the way Singular is printing things, e.g.:

```
**********************************************************************
File "/space/rlm/sage-4.1.alpha3/devel/sage-main/sage/interfaces/singular.py", line 975:
    sage: singular.current_ring()
Expected:
    //   characteristic : 127
    //   number of vars : 3
    //        block   1 : ordering rp
    //                  : names    x y z
    //        block   2 : ordering C
Got:
    //   characteristic : 127
    //   number of vars : 3
    //        block   1 : ordering rp
    //                  : names    xyz
    //        block   2 : ordering C
**********************************************************************
```


I assume this is nothing major. If someone wants to post a patch, I will gladly finish the review.



---

archive/issue_comments_050898.json:
```json
{
    "body": "Hmm... this must be what Martin was talking about with his spkg in [comment 7](http://trac.sagemath.org/sage_trac/ticket/6362#comment:7) above... will look into it right now",
    "created_at": "2009-07-03T16:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50898",
    "user": "aginiewicz"
}
```

Hmm... this must be what Martin was talking about with his spkg in [comment 7](http://trac.sagemath.org/sage_trac/ticket/6362#comment:7) above... will look into it right now



---

archive/issue_comments_050899.json:
```json
{
    "body": "Ok, I found that upstream changed in kernel/ring.cc:370 the \"Print(\"%s \",r->names[i]);\" into \"PrintS(r->names[i]);\", I reverted the change and now building/testing. Will post fixed spkg just as it finishes",
    "created_at": "2009-07-03T17:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50899",
    "user": "aginiewicz"
}
```

Ok, I found that upstream changed in kernel/ring.cc:370 the "Print("%s ",r->names[i]);" into "PrintS(r->names[i]);", I reverted the change and now building/testing. Will post fixed spkg just as it finishes



---

archive/issue_comments_050900.json:
```json
{
    "body": "Fixed, thanks for report. I replaced the file at http://giniu.ravenlord.ws/singular-3-1-0-4-20090703.spkg with new version.",
    "created_at": "2009-07-03T17:31:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50900",
    "user": "aginiewicz"
}
```

Fixed, thanks for report. I replaced the file at http://giniu.ravenlord.ws/singular-3-1-0-4-20090703.spkg with new version.



---

archive/issue_comments_050901.json:
```json
{
    "body": "Wouldn't it make more sense to not change things upstream, and just fix the doctests?",
    "created_at": "2009-07-03T17:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50901",
    "user": "@rlmill"
}
```

Wouldn't it make more sense to not change things upstream, and just fix the doctests?



---

archive/issue_comments_050902.json:
```json
{
    "body": "I guess the change looks like it wasn't intended, they massively changed Print(\"%s\", ...) (without space after %s) and Print(...) into PrintS(...), printing variable names without spaces or any other means of separation between them doesn't seem like something anyone wants...\n\nalso, what about:\n\n```\nS = singular.ring('real', '(xx,yy)', 'lp')\n```\n\nvs\n\n```\nR = singular.ring('real', '(x,xyy)', 'lp')\n```\n\nthat looks same when variables are printed without separation?",
    "created_at": "2009-07-03T17:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50902",
    "user": "aginiewicz"
}
```

I guess the change looks like it wasn't intended, they massively changed Print("%s", ...) (without space after %s) and Print(...) into PrintS(...), printing variable names without spaces or any other means of separation between them doesn't seem like something anyone wants...

also, what about:

```
S = singular.ring('real', '(xx,yy)', 'lp')
```

vs

```
R = singular.ring('real', '(x,xyy)', 'lp')
```

that looks same when variables are printed without separation?



---

archive/issue_comments_050903.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-03T18:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50903",
    "user": "@rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_050904.json:
```json
{
    "body": "Replying to [comment:26 aginiewicz]:\n> I guess the change looks like it wasn't intended\n\nIndeed, I talked to upstream about it and they consider this a bug (which they fixed in CVS).",
    "created_at": "2009-07-04T13:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50904",
    "user": "@malb"
}
```

Replying to [comment:26 aginiewicz]:
> I guess the change looks like it wasn't intended

Indeed, I talked to upstream about it and they consider this a bug (which they fixed in CVS).



---

archive/issue_comments_050905.json:
```json
{
    "body": "As contained in Sage-4.1.rc0, singular-3-1-0-4-20090703.spkg does not even build on OS X, neither 10.4 nor 10.5. Changing the line 201 in /src/factory/GNUmakefile.in:\n\n```\nfactoryobj :=   $(factorysrc:%.cc=%.o) $(factorysrc:%.y=%.o)\n```\n\ninto the following two lines:\n\n```\nfactoryobj :=   $(factorysrc:%.cc=%.o)\nfactoryobj :=   $(factoryobj:%.y=%.o)\n```\n\nmade the resulting Singular spkg build on OS X 10.4. But after installing it into Sage-4.1.rc0, Sage doesn't even start, it fails with:\n\n```\nImportError: dlopen(/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so, 2): Symbol not found: ___eprintf\n  Referenced from: /Users/Shared/sage/sage-4.1.rc0/local/lib//libsingular.dylib\n  Expected in: dynamic lookup\n```\n\nThis might be due to the fact that I had dropped in the 3.1.0.2 Singular spkg before, so I am re-running the build from the start. (I doubt that it'll help, but let's see.)\n\nFor the record, skipping through the install logs, I spotted another error (this time \"copy'n'paste\") in the Singular 3.1.0.4 build scripts. In /src/libfac/Makefile.in, the two identical lines 157/158 read:\n\n```\n\t-$(RANLIB) ${libdir}/libsingfac_g.a\n\t-$(RANLIB) ${libdir}/libsingfac_g.a\n```\n\nand it is obvious from the surrounding lines, that the line 158 should end with \"..._p.a\" instead of \"..._g.a\".\n\n`@`Martin:\nWould you please report the findings so far upstream?",
    "created_at": "2009-07-06T19:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50905",
    "user": "GeorgSWeber"
}
```

As contained in Sage-4.1.rc0, singular-3-1-0-4-20090703.spkg does not even build on OS X, neither 10.4 nor 10.5. Changing the line 201 in /src/factory/GNUmakefile.in:

```
factoryobj :=   $(factorysrc:%.cc=%.o) $(factorysrc:%.y=%.o)
```

into the following two lines:

```
factoryobj :=   $(factorysrc:%.cc=%.o)
factoryobj :=   $(factoryobj:%.y=%.o)
```

made the resulting Singular spkg build on OS X 10.4. But after installing it into Sage-4.1.rc0, Sage doesn't even start, it fails with:

```
ImportError: dlopen(/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so, 2): Symbol not found: ___eprintf
  Referenced from: /Users/Shared/sage/sage-4.1.rc0/local/lib//libsingular.dylib
  Expected in: dynamic lookup
```

This might be due to the fact that I had dropped in the 3.1.0.2 Singular spkg before, so I am re-running the build from the start. (I doubt that it'll help, but let's see.)

For the record, skipping through the install logs, I spotted another error (this time "copy'n'paste") in the Singular 3.1.0.4 build scripts. In /src/libfac/Makefile.in, the two identical lines 157/158 read:

```
	-$(RANLIB) ${libdir}/libsingfac_g.a
	-$(RANLIB) ${libdir}/libsingfac_g.a
```

and it is obvious from the surrounding lines, that the line 158 should end with "..._p.a" instead of "..._g.a".

`@`Martin:
Would you please report the findings so far upstream?



---

archive/issue_comments_050906.json:
```json
{
    "body": "Replying to [comment:29 GeorgSWeber]:\n> As contained in Sage-4.1.rc0, singular-3-1-0-4-20090703.spkg does not even build on OS X, neither 10.4 nor 10.5. Changing the line 201 in /src/factory/GNUmakefile.in:\n> {{{\n> factoryobj :=   $(factorysrc:%.cc=%.o) $(factorysrc:%.y=%.o)\n> }}}\n> into the following two lines:\n> {{{\n> factoryobj :=   $(factorysrc:%.cc=%.o)\n> factoryobj :=   $(factoryobj:%.y=%.o)\n> }}}\n> made the resulting Singular spkg build on OS X 10.4. But after installing it into Sage-4.1.rc0, Sage doesn't even start, it fails with:\n> {{{\n> ImportError: dlopen(/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so, 2): Symbol not found: ___eprintf\n>   Referenced from: /Users/Shared/sage/sage-4.1.rc0/local/lib//libsingular.dylib\n>   Expected in: dynamic lookup\n> }}}\n> This might be due to the fact that I had dropped in the 3.1.0.2 Singular spkg before, so I am re-running the build from the start. (I doubt that it'll help, but let's see.)\n> \n> For the record, skipping through the install logs, I spotted another error (this time \"copy'n'paste\") in the Singular 3.1.0.4 build scripts. In /src/libfac/Makefile.in, the two identical lines 157/158 read:\n> {{{\n> \t-$(RANLIB) ${libdir}/libsingfac_g.a\n> \t-$(RANLIB) ${libdir}/libsingfac_g.a\n> }}}\n> and it is obvious from the surrounding lines, that the line 158 should end with \"..._p.a\" instead of \"..._g.a\".\n> \n> `@`Martin:\n> Would you please report the findings so far upstream?\n\nOh, that's something already... but anyway, if I can suggest something, maybe [#6470](http://trac.sagemath.org/sage_trac/ticket/6470) would be better for continuation of this (closed) ticket? It will be better exposed that way I think",
    "created_at": "2009-07-06T19:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50906",
    "user": "aginiewicz"
}
```

Replying to [comment:29 GeorgSWeber]:
> As contained in Sage-4.1.rc0, singular-3-1-0-4-20090703.spkg does not even build on OS X, neither 10.4 nor 10.5. Changing the line 201 in /src/factory/GNUmakefile.in:
> {{{
> factoryobj :=   $(factorysrc:%.cc=%.o) $(factorysrc:%.y=%.o)
> }}}
> into the following two lines:
> {{{
> factoryobj :=   $(factorysrc:%.cc=%.o)
> factoryobj :=   $(factoryobj:%.y=%.o)
> }}}
> made the resulting Singular spkg build on OS X 10.4. But after installing it into Sage-4.1.rc0, Sage doesn't even start, it fails with:
> {{{
> ImportError: dlopen(/Users/Shared/sage/sage-4.1.rc0/local/lib/python2.6/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so, 2): Symbol not found: ___eprintf
>   Referenced from: /Users/Shared/sage/sage-4.1.rc0/local/lib//libsingular.dylib
>   Expected in: dynamic lookup
> }}}
> This might be due to the fact that I had dropped in the 3.1.0.2 Singular spkg before, so I am re-running the build from the start. (I doubt that it'll help, but let's see.)
> 
> For the record, skipping through the install logs, I spotted another error (this time "copy'n'paste") in the Singular 3.1.0.4 build scripts. In /src/libfac/Makefile.in, the two identical lines 157/158 read:
> {{{
> 	-$(RANLIB) ${libdir}/libsingfac_g.a
> 	-$(RANLIB) ${libdir}/libsingfac_g.a
> }}}
> and it is obvious from the surrounding lines, that the line 158 should end with "..._p.a" instead of "..._g.a".
> 
> `@`Martin:
> Would you please report the findings so far upstream?

Oh, that's something already... but anyway, if I can suggest something, maybe [#6470](http://trac.sagemath.org/sage_trac/ticket/6470) would be better for continuation of this (closed) ticket? It will be better exposed that way I think



---

archive/issue_comments_050907.json:
```json
{
    "body": "Yes, let's continue at #6470. Thanks for pointing out to me the new ticket!\n\nCheers,\ngsw",
    "created_at": "2009-07-06T20:11:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6362",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6362#issuecomment-50907",
    "user": "GeorgSWeber"
}
```

Yes, let's continue at #6470. Thanks for pointing out to me the new ticket!

Cheers,
gsw
