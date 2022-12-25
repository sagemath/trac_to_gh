# Issue 9905: Move the RPy package outside of the R package

archive/issues_009905.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @nexttime @kcrisman @vbraun @kini\n\nWe include the RPy spkg in the R spkg and install the former from the latter.  It would be less potentially confusing to move RPy outside of R but make it depend on R and any other prerequisites in `spkg/standard/deps`.\n\nRelated: #3086.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9906\n\n",
    "created_at": "2010-09-13T23:08:55Z",
    "labels": [
        "component: packages: standard",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.4",
    "title": "Move the RPy package outside of the R package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9905",
    "user": "https://github.com/qed777"
}
```
Assignee: tbd

CC:  @nexttime @kcrisman @vbraun @kini

We include the RPy spkg in the R spkg and install the former from the latter.  It would be less potentially confusing to move RPy outside of R but make it depend on R and any other prerequisites in `spkg/standard/deps`.

Related: #3086.

Issue created by migration from https://trac.sagemath.org/ticket/9906





---

archive/issue_comments_098305.json:
```json
{
    "body": "It would also allow independent updates and potentially improve compression.",
    "created_at": "2010-09-14T07:05:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98305",
    "user": "https://github.com/nexttime"
}
```

It would also allow independent updates and potentially improve compression.



---

archive/issue_comments_098306.json:
```json
{
    "body": "When touching the R package, one should also consider #9847 (i.e. R environment variables potentially disturbing the build).",
    "created_at": "2010-09-20T22:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98306",
    "user": "https://github.com/nexttime"
}
```

When touching the R package, one should also consider #9847 (i.e. R environment variables potentially disturbing the build).



---

archive/issue_comments_098307.json:
```json
{
    "body": "Changing priority from minor to critical.",
    "created_at": "2010-09-25T18:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98307",
    "user": "https://github.com/nexttime"
}
```

Changing priority from minor to critical.



---

archive/issue_comments_098308.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2010-09-25T18:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98308",
    "user": "https://github.com/nexttime"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_098309.json:
```json
{
    "body": "See [comment:ticket:9896:95 this comment] for another important reason.",
    "created_at": "2010-09-25T18:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98309",
    "user": "https://github.com/nexttime"
}
```

See [comment:ticket:9896:95 this comment] for another important reason.



---

archive/issue_comments_098310.json:
```json
{
    "body": "(Having Rpy in R's spkg is the culprit of [comment:ticket:8306:29 this build error].)",
    "created_at": "2010-09-25T18:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98310",
    "user": "https://github.com/nexttime"
}
```

(Having Rpy in R's spkg is the culprit of [comment:ticket:8306:29 this build error].)



---

archive/issue_comments_098311.json:
```json
{
    "body": "I've created a separate RPy 2.0.8.p1 spkg and an R 2.10.1.p5 (follow-up of p4 at #10016) spkg with the RPy spkg removed; both coming soon... (including updated `deps` and `spkg/install`)\n\nI also cleaned up both packages a little, and tried to address #9847, too.",
    "created_at": "2010-09-26T04:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98311",
    "user": "https://github.com/nexttime"
}
```

I've created a separate RPy 2.0.8.p1 spkg and an R 2.10.1.p5 (follow-up of p4 at #10016) spkg with the RPy spkg removed; both coming soon... (including updated `deps` and `spkg/install`)

I also cleaned up both packages a little, and tried to address #9847, too.



---

archive/issue_comments_098312.json:
```json
{
    "body": "Changing assignee from tbd to @nexttime.",
    "created_at": "2010-09-26T04:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98312",
    "user": "https://github.com/nexttime"
}
```

Changing assignee from tbd to @nexttime.



---

archive/issue_comments_098313.json:
```json
{
    "body": "Replying to [comment:5 leif]:\n> I've created a separate RPy 2.0.8.p1 spkg and an R 2.10.1.p5 (follow-up of p4 at #10016) spkg with the RPy spkg removed; both coming soon... \n\n\nHow soon is soon? \n\nIf you can make these available, it will help those that want to update the source code. \n\nDave",
    "created_at": "2010-10-01T13:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98313",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:5 leif]:
> I've created a separate RPy 2.0.8.p1 spkg and an R 2.10.1.p5 (follow-up of p4 at #10016) spkg with the RPy spkg removed; both coming soon... 


How soon is soon? 

If you can make these available, it will help those that want to update the source code. 

Dave



---

archive/issue_comments_098314.json:
```json
{
    "body": "Personal note:\n\n* Add patching `libR.pc` to `spkg-install`, making `rhome` and `rincludedir` relative to `$SAGE_ROOT`. (Currently no `prefix=...` definition.)",
    "created_at": "2010-11-03T01:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98314",
    "user": "https://github.com/nexttime"
}
```

Personal note:

* Add patching `libR.pc` to `spkg-install`, making `rhome` and `rincludedir` relative to `$SAGE_ROOT`. (Currently no `prefix=...` definition.)



---

archive/issue_comments_098315.json:
```json
{
    "body": "So... does this activity mean you will be posting something on e.g. spkg-upload? \n\n:)",
    "created_at": "2011-08-03T15:06:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98315",
    "user": "https://github.com/kcrisman"
}
```

So... does this activity mean you will be posting something on e.g. spkg-upload? 

:)



---

archive/issue_comments_098316.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-05T10:21:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98316",
    "user": "https://github.com/nexttime"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_098317.json:
```json
{
    "body": "Replying to [comment:11 kcrisman]:\n> So... does this activity mean you will be posting something on e.g. spkg-upload? \n\n\nLooks like. Before the spkgs have their first anniversary...\n\nThere are (still) some things that could be done, e.g. using `patch` and patching the `pkg-config` file (`libR.pc`) from `spkg-install`.\n\nWe could also perhaps either recompress the contained recommended R packages (`.tar.gz`) with `bzip2` or decompress them to plain `tar` files, as we compress the whole spkg with `bzip2` anyway. Haven't yet tried that though.\n\nRPy (and perhaps R) should IMHO be upgraded on a follow-up ticket.",
    "created_at": "2011-08-05T10:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98317",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:11 kcrisman]:
> So... does this activity mean you will be posting something on e.g. spkg-upload? 


Looks like. Before the spkgs have their first anniversary...

There are (still) some things that could be done, e.g. using `patch` and patching the `pkg-config` file (`libR.pc`) from `spkg-install`.

We could also perhaps either recompress the contained recommended R packages (`.tar.gz`) with `bzip2` or decompress them to plain `tar` files, as we compress the whole spkg with `bzip2` anyway. Haven't yet tried that though.

RPy (and perhaps R) should IMHO be upgraded on a follow-up ticket.



---

archive/issue_comments_098318.json:
```json
{
    "body": "I see the hardcoding issues shouldn't be hard to fix; the current (more or less superfluous) patch to `R.sh.in` and the corresponding Python script do only half of the job, namely setting `R_HOME_DIR` to `$SAGE_LOCAL/lib/R/`, but not changing `R_SHARE_DIR`, `R_INCLUDE_DIR` and `R_DOC_DIR`.\n\nBut before I do so, I think the new spkgs should first be tested as they are.\n\nI'll then make a p6, either here or (preferably) on a follow-up ticket if no other issues arise with the p5.",
    "created_at": "2011-08-05T11:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98318",
    "user": "https://github.com/nexttime"
}
```

I see the hardcoding issues shouldn't be hard to fix; the current (more or less superfluous) patch to `R.sh.in` and the corresponding Python script do only half of the job, namely setting `R_HOME_DIR` to `$SAGE_LOCAL/lib/R/`, but not changing `R_SHARE_DIR`, `R_INCLUDE_DIR` and `R_DOC_DIR`.

But before I do so, I think the new spkgs should first be tested as they are.

I'll then make a p6, either here or (preferably) on a follow-up ticket if no other issues arise with the p5.



---

archive/issue_comments_098319.json:
```json
{
    "body": "Yes, a different ticket would be fine.    I didn't realize these spkgs were actually ready :)\n\nComments/questions:\n* The rpy2 patch looks fine, and those are nice additions (the sanity checks, I mean).  \n* Really excellent work clarifying things on the r patch, adding all those checks etc.  I wouldn't have thought of any of them, but they all make loads of sense, though probably won't affect a million users.  I'm probably the one responsible for the .DS* stuff - I always try to check, but sometimes one forgets.\n* Do we need to unset `R_PROFILE` completely, or can we save that in a temp variable, unset it, then reset it after the spkg installs?  (If not because it would mess up RPy, we would have to do that there too.)\n* Do we need an 'echo' regarding the comment about the `$MAKE check` so that if it does fail, people know what to do?\n* What happened to Dave's favorite `\"x$SAGE64\" = xyes` (you removed the 'x's)?\n* Any reason to include the old RPy installation in the `if false` block?  Presumably if one really wanted to, the HG is there - I can't imagine this being very interesting to anyone.\n\nNote I have not actually installed or tested this yet :)",
    "created_at": "2011-08-05T17:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98319",
    "user": "https://github.com/kcrisman"
}
```

Yes, a different ticket would be fine.    I didn't realize these spkgs were actually ready :)

Comments/questions:
* The rpy2 patch looks fine, and those are nice additions (the sanity checks, I mean).  
* Really excellent work clarifying things on the r patch, adding all those checks etc.  I wouldn't have thought of any of them, but they all make loads of sense, though probably won't affect a million users.  I'm probably the one responsible for the .DS* stuff - I always try to check, but sometimes one forgets.
* Do we need to unset `R_PROFILE` completely, or can we save that in a temp variable, unset it, then reset it after the spkg installs?  (If not because it would mess up RPy, we would have to do that there too.)
* Do we need an 'echo' regarding the comment about the `$MAKE check` so that if it does fail, people know what to do?
* What happened to Dave's favorite `"x$SAGE64" = xyes` (you removed the 'x's)?
* Any reason to include the old RPy installation in the `if false` block?  Presumably if one really wanted to, the HG is there - I can't imagine this being very interesting to anyone.

Note I have not actually installed or tested this yet :)



---

archive/issue_comments_098320.json:
```json
{
    "body": "*Sorry for the delay, no trac notifications...* >B-|\n\nReplying to [comment:15 kcrisman]:\n> Yes, a different ticket would be fine.\n\n\n#9668 if you don't object...\n\n\n\n> I didn't realize these spkgs were actually ready :)\n\n\nI didn't know either. ;-)\n\nMore or less just completed the Changelog entries.\n\n\n\n> Comments/questions: \n\n\n>  * Do we need to unset `R_PROFILE` completely, or can we save that in a temp variable, unset it, then reset it after the spkg installs?  (If not because it would mess up RPy, we would have to do that there too.)\n\n\nIt's not fully clear to me what you mean by that. Unsetting `R_PROFILE` there only lasts until we leave `spkg-install`, i.e., is only effective within `spkg-install` and everything that's called from it. (Same applies to `spkg-check`.)\n\nActually I apparently didn't think of unsetting (or forgot to unset) `R_PROFILE` also in *RPy's* `spkg-install`; I'm not sure if RPy could break otherwise, but doing so shouldn't hurt.\n\nIIRC there were also problems with `R_PROFILE` when *using* Sage's R, which would have to be addressed in e.g. `sage-env` and/or the Sage library, not [necessarily] the spkg itself.\n\n\n\n>  * Do we need an 'echo' regarding the comment about the `$MAKE check` so that if it does fail, people know what to do?\n\n\nWell, I was expecting testing this being part of the review process, so I just added a comment. I can of course also print an appropriate message in case the (parallel) test should fail, but perhaps in the p6 on another ticket. (Automatically rerunning the test suite sequentially would IMHO be a less good idea.)\n\n\n\n>  * What happened to Dave's favorite `\"x$SAGE64\" = xyes` (you removed the 'x's)?\n\n\nI get eye cancer from such, it's worse readable and hence error-prone. If `test \"\" = foo` would evaluate to `true` (on some supported systems) Sage would certainly break in many places, not just because *we* use that all around. *Quoting* is important.\n\n(The broken instance of `test` was btw. a shell built-in version [besides some *really very old* `test` implementations which were less robust w.r.t. invalid expressions], and we explicitly use `bash` anyway. Prepending characters to variable expansions can make sense in different contexts, and is sometimes used to save the quotes, though the latter is also quite ugly. Similar applies to *not* using `-o` and `-a`.)\n\nIf one wanted to go really safe, one would either explicitly use `bash`'s built-in version of `test` (`[This is the Trac macro *\"$SAGE64\" = yes * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#\"$SAGE64\" = yes -macro)`), use `case \"$SAGE64\" in yes) ...`, or perhaps\n\n```sh\n[ \"${SAGE64:-no}\" = yes ]\n```\nwhich is the equivalent of Python's\n\n```python\nos.environ.get(\"SAGE64\", \"no\") == \"yes\"\n```\n\n\n\n>  * Any reason to include the old RPy installation in the `if false` block?\n\n\nNot really.\n\n> Presumably if one really wanted to, the HG is there - I can't imagine this being very interesting to anyone.\n\n\nSure, though it is buried by lots of other changes in the same changeset. I intended to remove it later, temporarily kept it just for documentation purposes.\n\n\n\n> Note I have not actually installed or tested this yet :)\n\n\nHope you'll do so later. :)",
    "created_at": "2011-08-07T03:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98320",
    "user": "https://github.com/nexttime"
}
```

*Sorry for the delay, no trac notifications...* >B-|

Replying to [comment:15 kcrisman]:
> Yes, a different ticket would be fine.


#9668 if you don't object...



> I didn't realize these spkgs were actually ready :)


I didn't know either. ;-)

More or less just completed the Changelog entries.



> Comments/questions: 


>  * Do we need to unset `R_PROFILE` completely, or can we save that in a temp variable, unset it, then reset it after the spkg installs?  (If not because it would mess up RPy, we would have to do that there too.)


It's not fully clear to me what you mean by that. Unsetting `R_PROFILE` there only lasts until we leave `spkg-install`, i.e., is only effective within `spkg-install` and everything that's called from it. (Same applies to `spkg-check`.)

Actually I apparently didn't think of unsetting (or forgot to unset) `R_PROFILE` also in *RPy's* `spkg-install`; I'm not sure if RPy could break otherwise, but doing so shouldn't hurt.

IIRC there were also problems with `R_PROFILE` when *using* Sage's R, which would have to be addressed in e.g. `sage-env` and/or the Sage library, not [necessarily] the spkg itself.



>  * Do we need an 'echo' regarding the comment about the `$MAKE check` so that if it does fail, people know what to do?


Well, I was expecting testing this being part of the review process, so I just added a comment. I can of course also print an appropriate message in case the (parallel) test should fail, but perhaps in the p6 on another ticket. (Automatically rerunning the test suite sequentially would IMHO be a less good idea.)



>  * What happened to Dave's favorite `"x$SAGE64" = xyes` (you removed the 'x's)?


I get eye cancer from such, it's worse readable and hence error-prone. If `test "" = foo` would evaluate to `true` (on some supported systems) Sage would certainly break in many places, not just because *we* use that all around. *Quoting* is important.

(The broken instance of `test` was btw. a shell built-in version [besides some *really very old* `test` implementations which were less robust w.r.t. invalid expressions], and we explicitly use `bash` anyway. Prepending characters to variable expansions can make sense in different contexts, and is sometimes used to save the quotes, though the latter is also quite ugly. Similar applies to *not* using `-o` and `-a`.)

If one wanted to go really safe, one would either explicitly use `bash`'s built-in version of `test` (`[This is the Trac macro *"$SAGE64" = yes * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#"$SAGE64" = yes -macro)`), use `case "$SAGE64" in yes) ...`, or perhaps

```sh
[ "${SAGE64:-no}" = yes ]
```
which is the equivalent of Python's

```python
os.environ.get("SAGE64", "no") == "yes"
```



>  * Any reason to include the old RPy installation in the `if false` block?


Not really.

> Presumably if one really wanted to, the HG is there - I can't imagine this being very interesting to anyone.


Sure, though it is buried by lots of other changes in the same changeset. I intended to remove it later, temporarily kept it just for documentation purposes.



> Note I have not actually installed or tested this yet :)


Hope you'll do so later. :)



---

archive/issue_comments_098321.json:
```json
{
    "body": "> > Yes, a different ticket would be fine.\n\n> #9668 if you don't object...\nNo, that is quite natural.\n> >  * Do we need to unset `R_PROFILE` completely, or can we save that in a temp variable, unset it, then reset it after the spkg installs?  (If not because it would mess up RPy, we would have to do that there too.)\n \n> It's not fully clear to me what you mean by that. Unsetting `R_PROFILE` there only lasts until we leave `spkg-install`, i.e., is only effective within `spkg-install` and everything that's called from it. (Same applies to `spkg-check`.)\nI didn't realize that.  \n> Actually I apparently didn't think of unsetting (or forgot to unset) `R_PROFILE` also in *RPy's* `spkg-install`; I'm not sure if RPy could break otherwise, but doing so shouldn't hurt.\n\nSo maybe that's a \"needs work\"?\n> IIRC there were also problems with `R_PROFILE` when *using* Sage's R, which would have to be addressed in e.g. `sage-env` and/or the Sage library, not [necessarily] the spkg itself.\n\nYes, that's a different ticket, and notoriously hard to track down at times.\n> >  * Do we need an 'echo' regarding the comment about the `$MAKE check` so that if it does fail, people know what to do?\n \n> \n> Well, I was expecting testing this being part of the review process, so I just added a comment. I can of course also print an appropriate message in case the (parallel) test should fail, but perhaps in the p6 on another ticket. (Automatically rerunning the test suite sequentially would IMHO be a less good idea.)\n\nOk.\n> >  * Any reason to include the old RPy installation in the `if false` block?\n \n> Not really.\n> > Presumably if one really wanted to, the HG is there - I can't imagine this being very interesting to anyone.\n\n> Sure, though it is buried by lots of other changes in the same changeset. I intended to remove it later, temporarily kept it just for documentation purposes.\nWell, either way that wouldn't hold up this ticket.\n> > Note I have not actually installed or tested this yet :)\n\n> Hope you'll do so later. :)\nBut not today :(",
    "created_at": "2011-08-08T14:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98321",
    "user": "https://github.com/kcrisman"
}
```

> > Yes, a different ticket would be fine.

> #9668 if you don't object...
No, that is quite natural.
> >  * Do we need to unset `R_PROFILE` completely, or can we save that in a temp variable, unset it, then reset it after the spkg installs?  (If not because it would mess up RPy, we would have to do that there too.)
 
> It's not fully clear to me what you mean by that. Unsetting `R_PROFILE` there only lasts until we leave `spkg-install`, i.e., is only effective within `spkg-install` and everything that's called from it. (Same applies to `spkg-check`.)
I didn't realize that.  
> Actually I apparently didn't think of unsetting (or forgot to unset) `R_PROFILE` also in *RPy's* `spkg-install`; I'm not sure if RPy could break otherwise, but doing so shouldn't hurt.

So maybe that's a "needs work"?
> IIRC there were also problems with `R_PROFILE` when *using* Sage's R, which would have to be addressed in e.g. `sage-env` and/or the Sage library, not [necessarily] the spkg itself.

Yes, that's a different ticket, and notoriously hard to track down at times.
> >  * Do we need an 'echo' regarding the comment about the `$MAKE check` so that if it does fail, people know what to do?
 
> 
> Well, I was expecting testing this being part of the review process, so I just added a comment. I can of course also print an appropriate message in case the (parallel) test should fail, but perhaps in the p6 on another ticket. (Automatically rerunning the test suite sequentially would IMHO be a less good idea.)

Ok.
> >  * Any reason to include the old RPy installation in the `if false` block?
 
> Not really.
> > Presumably if one really wanted to, the HG is there - I can't imagine this being very interesting to anyone.

> Sure, though it is buried by lots of other changes in the same changeset. I intended to remove it later, temporarily kept it just for documentation purposes.
Well, either way that wouldn't hold up this ticket.
> > Note I have not actually installed or tested this yet :)

> Hope you'll do so later. :)
But not today :(



---

archive/issue_comments_098322.json:
```json
{
    "body": "Replying to [comment:17 kcrisman]:\n> > > Yes, a different ticket would be fine.\n\n> > #9668 if you don't object...\n> No, that is quite natural.\n\n\nOk.\n\n\n\n\n> > Actually I apparently didn't think of unsetting (or forgot to unset) `R_PROFILE` also in *RPy's* `spkg-install`; I'm not sure if RPy could break otherwise, but doing so shouldn't hurt.\n\n> So maybe that's a \"needs work\"?\n\n`R_PROFILE` doesn't appear in any of RPy's source files, so I don't think so. (I perhaps checked that last year, but forgot about it. :D )",
    "created_at": "2011-08-09T05:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98322",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:17 kcrisman]:
> > > Yes, a different ticket would be fine.

> > #9668 if you don't object...
> No, that is quite natural.


Ok.




> > Actually I apparently didn't think of unsetting (or forgot to unset) `R_PROFILE` also in *RPy's* `spkg-install`; I'm not sure if RPy could break otherwise, but doing so shouldn't hurt.

> So maybe that's a "needs work"?

`R_PROFILE` doesn't appear in any of RPy's source files, so I don't think so. (I perhaps checked that last year, but forgot about it. :D )



---

archive/issue_comments_098323.json:
```json
{
    "body": "Just a note to self/any other reviewer of what would have to be tested.\n* Upgrading rpy2 by itself.\n* Upgrading r by itself.\n* Then upgrading rpy2 after having upgraded r.\n* And test R and rpy2 after each step.\n* Test with and without `R_PROFILE` set.\n* Test with and without `SAGE_CHECK` set.\n* Test with `SAGE_CHECK` yes with and without parallel make.\n* Test on (at least) Linux and Mac.\n* Test with and without spaces in the path.\nRemind me why this is needed again?  :-)",
    "created_at": "2011-08-10T21:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98323",
    "user": "https://github.com/kcrisman"
}
```

Just a note to self/any other reviewer of what would have to be tested.
* Upgrading rpy2 by itself.
* Upgrading r by itself.
* Then upgrading rpy2 after having upgraded r.
* And test R and rpy2 after each step.
* Test with and without `R_PROFILE` set.
* Test with and without `SAGE_CHECK` set.
* Test with `SAGE_CHECK` yes with and without parallel make.
* Test on (at least) Linux and Mac.
* Test with and without spaces in the path.
Remind me why this is needed again?  :-)



---

archive/issue_comments_098324.json:
```json
{
    "body": "Here is another somewhat related ticket - #10967.   I don't think that is fixed, at least not in the same way, by this p5.",
    "created_at": "2011-08-19T13:48:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98324",
    "user": "https://github.com/kcrisman"
}
```

Here is another somewhat related ticket - #10967.   I don't think that is fixed, at least not in the same way, by this p5.



---

archive/issue_comments_098325.json:
```json
{
    "body": "Replying to [comment:20 kcrisman]:\n> Here is another somewhat related ticket - #10967.   I don't think that is fixed, at least not in the same way, by this p5.\n\n\nFor the record: #10967 will be addressed at #9668, by an R 2.10.1.p6 spkg there, so I've made the former ticket depend on the latter, and changed its milestone to *\"duplicate/invalid/won't fix\"*.",
    "created_at": "2011-08-21T00:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98325",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:20 kcrisman]:
> Here is another somewhat related ticket - #10967.   I don't think that is fixed, at least not in the same way, by this p5.


For the record: #10967 will be addressed at #9668, by an R 2.10.1.p6 spkg there, so I've made the former ticket depend on the latter, and changed its milestone to *"duplicate/invalid/won't fix"*.



---

archive/issue_comments_098326.json:
```json
{
    "body": "Ping.\n\nI think we should merge this before it further rottens; I'll not be able to finish #9668 in the next days (and right now don't know when I'll do that), but it's not a dependency anyway, just a further improvement...",
    "created_at": "2011-10-09T15:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98326",
    "user": "https://github.com/nexttime"
}
```

Ping.

I think we should merge this before it further rottens; I'll not be able to finish #9668 in the next days (and right now don't know when I'll do that), but it's not a dependency anyway, just a further improvement...



---

archive/issue_comments_098327.json:
```json
{
    "body": "Sorry, I just won't have time to do that laundry list of testing in the near future.  (As you may have noticed from my relative lack of activity elsewhere.)   And there isn't really anything breaking because of this weirdness, thankfully... My apologies :(",
    "created_at": "2011-10-10T02:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98327",
    "user": "https://github.com/kcrisman"
}
```

Sorry, I just won't have time to do that laundry list of testing in the near future.  (As you may have noticed from my relative lack of activity elsewhere.)   And there isn't really anything breaking because of this weirdness, thankfully... My apologies :(



---

archive/issue_comments_098328.json:
```json
{
    "body": "Wow.  I just upgraded my rpy2 spkg to 2.2.4, and was tempted to work on upgrading R to 2.14.  But then I saw this ticket.  I don't have time either right now to do the extensive testing this ticket appears to need (according to comments above), and it feels like this work should go in before upgrading to 2.14, etc.",
    "created_at": "2011-11-15T05:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98328",
    "user": "https://github.com/jasongrout"
}
```

Wow.  I just upgraded my rpy2 spkg to 2.2.4, and was tempted to work on upgrading R to 2.14.  But then I saw this ticket.  I don't have time either right now to do the extensive testing this ticket appears to need (according to comments above), and it feels like this work should go in before upgrading to 2.14, etc.



---

archive/issue_comments_098329.json:
```json
{
    "body": "Changing keywords from \"\" to \"r-project\".",
    "created_at": "2011-11-20T01:17:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98329",
    "user": "https://github.com/kcrisman"
}
```

Changing keywords from "" to "r-project".



---

archive/issue_comments_098330.json:
```json
{
    "body": "Replying to [comment:25 jason]:\n> Wow.  I just upgraded my rpy2 spkg to 2.2.4, and was tempted to work on upgrading R to 2.14.  But then I saw this ticket.  I don't have time either right now to do the extensive testing this ticket appears to need (according to comments above), and it feels like this work should go in before upgrading to 2.14, etc.\n\n\nRegarding this, see #12057.",
    "created_at": "2011-11-20T01:18:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98330",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:25 jason]:
> Wow.  I just upgraded my rpy2 spkg to 2.2.4, and was tempted to work on upgrading R to 2.14.  But then I saw this ticket.  I don't have time either right now to do the extensive testing this ticket appears to need (according to comments above), and it feels like this work should go in before upgrading to 2.14, etc.


Regarding this, see #12057.



---

archive/issue_comments_098331.json:
```json
{
    "body": "Replying to [comment:25 jason]:\n> Wow.  I just upgraded my rpy2 spkg to 2.2.4, and was tempted to work on upgrading R to 2.14.  But then I saw this ticket.  I don't have time either right now to do the extensive testing this ticket appears to need (according to comments above), and it feels like this work should go in before upgrading to 2.14, etc.\n\n\nWell, this didn't happen.  R will be upgraded to version 2.14 in #12057 which will normally be merged in sage-4.8.alpha4.  So, this ticket needs to be rebased...",
    "created_at": "2011-12-09T10:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98331",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:25 jason]:
> Wow.  I just upgraded my rpy2 spkg to 2.2.4, and was tempted to work on upgrading R to 2.14.  But then I saw this ticket.  I don't have time either right now to do the extensive testing this ticket appears to need (according to comments above), and it feels like this work should go in before upgrading to 2.14, etc.


Well, this didn't happen.  R will be upgraded to version 2.14 in #12057 which will normally be merged in sage-4.8.alpha4.  So, this ticket needs to be rebased...



---

archive/issue_comments_098332.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-12-09T10:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98332",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_098333.json:
```json
{
    "body": "Replying to [comment:25 jason]:\n> I don't have time either right now to do the extensive testing this ticket appears to need (according to comments above)\n\nTesting is easy, I wouldn't mind doing that.",
    "created_at": "2011-12-09T11:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98333",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:25 jason]:
> I don't have time either right now to do the extensive testing this ticket appears to need (according to comments above)

Testing is easy, I wouldn't mind doing that.



---

archive/issue_comments_098334.json:
```json
{
    "body": "> > I don't have time either right now to do the extensive testing this ticket appears to need (according to comments above)\n\n> Testing is easy, I wouldn't mind doing that.\nI had the same problem, because it would require a lot of manual stuff, but if you can use the buildbot to test a rebased version of this that would be fantastic.",
    "created_at": "2011-12-09T14:55:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98334",
    "user": "https://github.com/kcrisman"
}
```

> > I don't have time either right now to do the extensive testing this ticket appears to need (according to comments above)

> Testing is easy, I wouldn't mind doing that.
I had the same problem, because it would require a lot of manual stuff, but if you can use the buildbot to test a rebased version of this that would be fantastic.



---

archive/issue_comments_098335.json:
```json
{
    "body": "Apparently we also should take care of some references to sage-env or something which are soon to disappear - see #11073, in particular [comment:73:ticket:11073 this comment].",
    "created_at": "2012-01-17T14:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98335",
    "user": "https://github.com/kcrisman"
}
```

Apparently we also should take care of some references to sage-env or something which are soon to disappear - see #11073, in particular [comment:73:ticket:11073 this comment].



---

archive/issue_comments_098336.json:
```json
{
    "body": "Argh!",
    "created_at": "2012-03-21T13:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98336",
    "user": "https://github.com/nexttime"
}
```

Argh!



---

archive/issue_comments_098337.json:
```json
{
    "body": "Apply to SAGE_ROOT. Activates RPY in spkg/install and spkg/standard/deps",
    "created_at": "2012-09-04T12:04:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98337",
    "user": "https://github.com/jdemeyer"
}
```

Apply to SAGE_ROOT. Activates RPY in spkg/install and spkg/standard/deps



---

archive/issue_comments_098338.json:
```json
{
    "body": "Attachment [trac_9906-Activate_separate_RPy_spkg.root-repo.patch](tarball://root/attachments/some-uuid/ticket9906/trac_9906-Activate_separate_RPy_spkg.root-repo.patch) by @jdemeyer created at 2012-09-04 12:06:03\n\nWhy should `R` depend on `PYTHON`?  The old `spkg/standard/deps` claims \"Note that even with a separate RPy spkg (#9906), Sage's R will still depend on \"Python, but I see no reason for this.  So I removed the explicit PYTHON dependency.  But it still indirectly depends on PYTHON via PYTHON->ATLAS->R.",
    "created_at": "2012-09-04T12:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98338",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [trac_9906-Activate_separate_RPy_spkg.root-repo.patch](tarball://root/attachments/some-uuid/ticket9906/trac_9906-Activate_separate_RPy_spkg.root-repo.patch) by @jdemeyer created at 2012-09-04 12:06:03

Why should `R` depend on `PYTHON`?  The old `spkg/standard/deps` claims "Note that even with a separate RPy spkg (#9906), Sage's R will still depend on "Python, but I see no reason for this.  So I removed the explicit PYTHON dependency.  But it still indirectly depends on PYTHON via PYTHON->ATLAS->R.



---

archive/issue_events_024962.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-09-04T12:08:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "milestone": "sage-5.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9905#event-24962"
}
```



---

archive/issue_comments_098339.json:
```json
{
    "body": "Changing keywords from \"r-project\" to \"r-project spkg\".",
    "created_at": "2012-09-04T12:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98339",
    "user": "https://github.com/jdemeyer"
}
```

Changing keywords from "r-project" to "r-project spkg".



---

archive/issue_comments_098340.json:
```json
{
    "body": "Attachment [r-2.14.0.p5.diff](tarball://root/attachments/some-uuid/ticket9906/r-2.14.0.p5.diff) by @jdemeyer created at 2012-09-04 12:09:29\n\nDiff for the R spkg. For reference / review only.",
    "created_at": "2012-09-04T12:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98340",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [r-2.14.0.p5.diff](tarball://root/attachments/some-uuid/ticket9906/r-2.14.0.p5.diff) by @jdemeyer created at 2012-09-04 12:09:29

Diff for the R spkg. For reference / review only.



---

archive/issue_comments_098341.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-09-04T13:36:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98341",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_098342.json:
```json
{
    "body": "There is also some general cleanup that could happen; for example:\n\n```diff\ndiff --git a/spkg-install b/spkg-install\n--- a/spkg-install\n+++ b/spkg-install\n@@ -67,15 +67,6 @@ if [ \"$UNAME\" = \"SunOS\" ]; then\n     SUN_FLAGS=\"--without-ICU\"; export SUN_FLAGS\n fi\n \n-# let's remove old install, even the wrongly installed ones\n-rm -rf \"$SAGE_LOCAL\"/lib/r\n-rm -rf \"$SAGE_LOCAL\"/lib/R\n-rm -rf \"$SAGE_LOCAL\"/lib64/R\n-rm -rf \"$SAGE_LOCAL\"/lib64/r\n-# and let's also nuke some leftovers on SAGE_LOCAL/lib\n-rm -rf \"$SAGE_LOCAL\"/lib/libRblas.so \"$SAGE_LOCAL\"/lib/libRlapack.so \"$SAGE_LOCAL\"/lib/libR.so\n-rm -rf \"$SAGE_LOCAL\"/lib/libRblas.dylib \"$SAGE_LOCAL\"/lib/libRlapack.dylib \"$SAGE_LOCAL\"/lib/libR.dylib\n-\n cd src\n \n # Apply patches.  See SPKG.txt for information about what each patch\n@@ -131,6 +122,15 @@ if [ $? -ne 0 ]; then\n     exit 1\n fi\n \n+# Before installing, remove old install, even the wrongly installed ones.\n+rm -rf \"$SAGE_LOCAL\"/lib/r\n+rm -rf \"$SAGE_LOCAL\"/lib/R\n+rm -rf \"$SAGE_LOCAL\"/lib64/R\n+rm -rf \"$SAGE_LOCAL\"/lib64/r\n+# and let's also nuke some leftovers on SAGE_LOCAL/lib\n+rm -rf \"$SAGE_LOCAL\"/lib/libRblas.so \"$SAGE_LOCAL\"/lib/libRlapack.so \"$SAGE_LOCAL\"/lib/libR.so\n+rm -rf \"$SAGE_LOCAL\"/lib/libRblas.dylib \"$SAGE_LOCAL\"/lib/libRlapack.dylib \"$SAGE_LOCAL\"/lib/libR.dylib\n+\n # Disable parallel make install, which is supposedly broken\n $MAKE -j1 vignettes  # Needed for help system\n $MAKE -j1 install\n@@ -168,7 +168,7 @@ if [ $? -ne 0 ] || [ ! -f \"$SAGE_ROOT\"/s\n fi\n \n if [ \"$UNAME\" = \"Darwin\" ]; then\n-    echo \"Copying fake java and javac compiler on OSX\"\n+    echo \"Removing fake java and javac compiler on OSX.\"\n     rm -f \"$SAGE_LOCAL\"/bin/java\n     rm -f \"$SAGE_LOCAL\"/bin/javac\n fi\n```\nShould this happen on another ticket?",
    "created_at": "2012-09-04T19:39:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98342",
    "user": "https://github.com/jhpalmieri"
}
```

There is also some general cleanup that could happen; for example:

```diff
diff --git a/spkg-install b/spkg-install
--- a/spkg-install
+++ b/spkg-install
@@ -67,15 +67,6 @@ if [ "$UNAME" = "SunOS" ]; then
     SUN_FLAGS="--without-ICU"; export SUN_FLAGS
 fi
 
-# let's remove old install, even the wrongly installed ones
-rm -rf "$SAGE_LOCAL"/lib/r
-rm -rf "$SAGE_LOCAL"/lib/R
-rm -rf "$SAGE_LOCAL"/lib64/R
-rm -rf "$SAGE_LOCAL"/lib64/r
-# and let's also nuke some leftovers on SAGE_LOCAL/lib
-rm -rf "$SAGE_LOCAL"/lib/libRblas.so "$SAGE_LOCAL"/lib/libRlapack.so "$SAGE_LOCAL"/lib/libR.so
-rm -rf "$SAGE_LOCAL"/lib/libRblas.dylib "$SAGE_LOCAL"/lib/libRlapack.dylib "$SAGE_LOCAL"/lib/libR.dylib
-
 cd src
 
 # Apply patches.  See SPKG.txt for information about what each patch
@@ -131,6 +122,15 @@ if [ $? -ne 0 ]; then
     exit 1
 fi
 
+# Before installing, remove old install, even the wrongly installed ones.
+rm -rf "$SAGE_LOCAL"/lib/r
+rm -rf "$SAGE_LOCAL"/lib/R
+rm -rf "$SAGE_LOCAL"/lib64/R
+rm -rf "$SAGE_LOCAL"/lib64/r
+# and let's also nuke some leftovers on SAGE_LOCAL/lib
+rm -rf "$SAGE_LOCAL"/lib/libRblas.so "$SAGE_LOCAL"/lib/libRlapack.so "$SAGE_LOCAL"/lib/libR.so
+rm -rf "$SAGE_LOCAL"/lib/libRblas.dylib "$SAGE_LOCAL"/lib/libRlapack.dylib "$SAGE_LOCAL"/lib/libR.dylib
+
 # Disable parallel make install, which is supposedly broken
 $MAKE -j1 vignettes  # Needed for help system
 $MAKE -j1 install
@@ -168,7 +168,7 @@ if [ $? -ne 0 ] || [ ! -f "$SAGE_ROOT"/s
 fi
 
 if [ "$UNAME" = "Darwin" ]; then
-    echo "Copying fake java and javac compiler on OSX"
+    echo "Removing fake java and javac compiler on OSX."
     rm -f "$SAGE_LOCAL"/bin/java
     rm -f "$SAGE_LOCAL"/bin/javac
 fi
```
Should this happen on another ticket?



---

archive/issue_comments_098343.json:
```json
{
    "body": "Replying to [comment:44 jhpalmieri]:\n> Should this happen on another ticket?\n\nYes please.  I specifically didn't do any kind of cleanup just to ensure this would finally be merged.",
    "created_at": "2012-09-04T19:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98343",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:44 jhpalmieri]:
> Should this happen on another ticket?

Yes please.  I specifically didn't do any kind of cleanup just to ensure this would finally be merged.



---

archive/issue_comments_098344.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-09-04T20:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98344",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_098345.json:
```json
{
    "body": "rpy2 needs a version bump, otherwise it won't be downloaded when upgrading.",
    "created_at": "2012-09-04T20:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98345",
    "user": "https://github.com/jdemeyer"
}
```

rpy2 needs a version bump, otherwise it won't be downloaded when upgrading.



---

archive/issue_comments_098346.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-09-04T20:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98346",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_098347.json:
```json
{
    "body": "Attachment [rpy2-2.0.8.p0.diff](tarball://root/attachments/some-uuid/ticket9906/rpy2-2.0.8.p0.diff) by @jdemeyer created at 2012-09-04 20:26:08\n\nDiff for the rpy2 spkg (w.r.t. to the one in the current R spkg). For reference / review only.",
    "created_at": "2012-09-04T20:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98347",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [rpy2-2.0.8.p0.diff](tarball://root/attachments/some-uuid/ticket9906/rpy2-2.0.8.p0.diff) by @jdemeyer created at 2012-09-04 20:26:08

Diff for the rpy2 spkg (w.r.t. to the one in the current R spkg). For reference / review only.



---

archive/issue_comments_098348.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-09-05T04:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98348",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_098349.json:
```json
{
    "body": "Looks good to me. Builds and passes tests, and works when upgrading.",
    "created_at": "2012-09-05T04:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98349",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me. Builds and passes tests, and works when upgrading.



---

archive/issue_events_024963.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-09-06T05:23:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9905#event-24963"
}
```



---

archive/issue_comments_098350.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-09-06T05:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98350",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_098351.json:
```json
{
    "body": "> > Should this happen on another ticket?\n\n> Yes please.  I specifically didn't do any kind of cleanup just to ensure this would finally be merged.\nYou can cc: me on this new ticket too when you make it.",
    "created_at": "2012-09-06T19:19:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98351",
    "user": "https://github.com/kcrisman"
}
```

> > Should this happen on another ticket?

> Yes please.  I specifically didn't do any kind of cleanup just to ensure this would finally be merged.
You can cc: me on this new ticket too when you make it.



---

archive/issue_comments_098352.json:
```json
{
    "body": "Replying to [comment:50 kcrisman]:\n> You can cc: me on this new ticket too when you make it.\n\nTo be honest, this is not something I feel like working on, so I'm going to make that ticket.",
    "created_at": "2012-09-07T09:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98352",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:50 kcrisman]:
> You can cc: me on this new ticket too when you make it.

To be honest, this is not something I feel like working on, so I'm going to make that ticket.



---

archive/issue_comments_098353.json:
```json
{
    "body": "Okay, I'm making the follow-up anyway: #13443.",
    "created_at": "2012-09-10T14:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9905#issuecomment-98353",
    "user": "https://github.com/jdemeyer"
}
```

Okay, I'm making the follow-up anyway: #13443.
