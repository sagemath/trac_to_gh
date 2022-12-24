# Issue 3358: Improve the building of eclib (shared/static objects) [with patch needs review]

archive/issues_003358.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  tabbott@mit.edu\n\nAfter sitting waiting for some answers on the last thread about this on debian-sage\nI decided to go ahead. This patch do not add versionning for debian as it seems\nto cause problem on other OS. It builds static objects (libraries and executables)\nwithout any pic flag and shared object with pic flag on linux. I respected the earlier\nsetting where the flag is set in spkg-install and it is set to nothing on OS X and\nCYGWIN although I think it should be set as well on this platform.\nI also move executables in a created bin directory for convenience (this directory\nis created by the Makefile).\nI cleaned the spkg-install to accommodate the changes and added a few fix that I\nthought necessary. -fPIC to -fpic, those are 2 slightly different flags, I don't\nthink I should go on the technical differences between them. I also cleaned\na conditional block were linux specific code would be executed on darwin - probably\nwithout harm but still.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3358\n\n",
    "created_at": "2008-06-03T23:57:53Z",
    "labels": [
        "build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Improve the building of eclib (shared/static objects) [with patch needs review]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3358",
    "user": "@kiwifb"
}
```
Assignee: mabshoff

CC:  tabbott@mit.edu

After sitting waiting for some answers on the last thread about this on debian-sage
I decided to go ahead. This patch do not add versionning for debian as it seems
to cause problem on other OS. It builds static objects (libraries and executables)
without any pic flag and shared object with pic flag on linux. I respected the earlier
setting where the flag is set in spkg-install and it is set to nothing on OS X and
CYGWIN although I think it should be set as well on this platform.
I also move executables in a created bin directory for convenience (this directory
is created by the Makefile).
I cleaned the spkg-install to accommodate the changes and added a few fix that I
thought necessary. -fPIC to -fpic, those are 2 slightly different flags, I don't
think I should go on the technical differences between them. I also cleaned
a conditional block were linux specific code would be executed on darwin - probably
without harm but still.

Issue created by migration from https://trac.sagemath.org/ticket/3358





---

archive/issue_comments_023364.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-06-15T22:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23364",
    "user": "@craigcitro"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_023365.json:
```json
{
    "body": "Please remember to put the \"[with patch, needs review]\" at the *beginning* of the summary.",
    "created_at": "2008-06-15T22:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23365",
    "user": "@craigcitro"
}
```

Please remember to put the "[with patch, needs review]" at the *beginning* of the summary.



---

archive/issue_comments_023366.json:
```json
{
    "body": "I do not like the \"-fPIC\" -> \"-fpic\" change, otherwise I am fine with the patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-20T04:02:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23366",
    "user": "mabshoff"
}
```

I do not like the "-fPIC" -> "-fpic" change, otherwise I am fine with the patch.

Cheers,

Michael



---

archive/issue_comments_023367.json:
```json
{
    "body": "Hi Michael,\n\nI didn't think you would take it anyway as it has\nGNU-ism like:\n(SO_LIBNAME): FPICFLAG= $(PICFLAG)\n\texport FPICFLAG\n\nI thought a bit more about -fPIC versus -fPIC and\nI guess in the interest of KISS we should probably\nstick to -fPIC as ppc and may be other may balk \notherwise.",
    "created_at": "2008-06-20T08:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23367",
    "user": "@kiwifb"
}
```

Hi Michael,

I didn't think you would take it anyway as it has
GNU-ism like:
(SO_LIBNAME): FPICFLAG= $(PICFLAG)
	export FPICFLAG

I thought a bit more about -fPIC versus -fPIC and
I guess in the interest of KISS we should probably
stick to -fPIC as ppc and may be other may balk 
otherwise.



---

archive/issue_comments_023368.json:
```json
{
    "body": "OK new patches to ungnu-ify the makefiles and build shared and static objects\nproperly and use the bin folder. Tested with bsd make and gnu make - didn't have \ntime for sun make, should work though. \nspkg-install also updated. everything is against eclib-20080310.p4",
    "created_at": "2008-07-07T01:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23368",
    "user": "@kiwifb"
}
```

OK new patches to ungnu-ify the makefiles and build shared and static objects
properly and use the bin folder. Tested with bsd make and gnu make - didn't have 
time for sun make, should work though. 
spkg-install also updated. everything is against eclib-20080310.p4



---

archive/issue_comments_023369.json:
```json
{
    "body": "updated the patches to 20080310.p5.",
    "created_at": "2008-07-08T22:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23369",
    "user": "@kiwifb"
}
```

updated the patches to 20080310.p5.



---

archive/issue_comments_023370.json:
```json
{
    "body": "I'm probably not the best person to review this but if there's anything I can do, please let me know.  John",
    "created_at": "2008-08-10T16:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23370",
    "user": "@JohnCremona"
}
```

I'm probably not the best person to review this but if there's anything I can do, please let me know.  John



---

archive/issue_comments_023371.json:
```json
{
    "body": "I think there are some issues with eclib-ungnu.patch:\n\n* the formal changes, i.e. the removal of the \".o\" from the makefiles should be independent of the other changes for reviewing purposes\n* some of the fixes will have the makefiles as is working with Sage, but if anyone attempted to compile eclib without explicitly setting env variables like NTL the compile will break or the build will not include features like pari support. I don't care which way we go here, but this is up to John since it is his code project.\n\nAs is the patch needs to be rebased slighly:\n\n```\n/eclib-20080310.p7/src$ patch -p1 --dry-run < eclib-ungnu.patch\\?format\\=raw \npatching file Makefile\nHunk #4 FAILED at 45.\n1 out of 4 hunks FAILED -- saving rejects to file Makefile.rej\npatching file Makefile.dynamic\npatching file g0n/Makefile\nHunk #2 succeeded at 25 with fuzz 2.\npatching file procs/Makefile\nHunk #2 FAILED at 23.\n1 out of 6 hunks FAILED -- saving rejects to file procs/Makefile.rej\npatching file qcurves/Makefile\npatching file qrank/Makefile\n```\n\n\nI am -1 on all the other three patches at this ticket. Some of those might be salvaged, i.e. from the spkg-install patches like the better installation, but the PIC->pic change is just plain wrong.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T22:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23371",
    "user": "mabshoff"
}
```

I think there are some issues with eclib-ungnu.patch:

* the formal changes, i.e. the removal of the ".o" from the makefiles should be independent of the other changes for reviewing purposes
* some of the fixes will have the makefiles as is working with Sage, but if anyone attempted to compile eclib without explicitly setting env variables like NTL the compile will break or the build will not include features like pari support. I don't care which way we go here, but this is up to John since it is his code project.

As is the patch needs to be rebased slighly:

```
/eclib-20080310.p7/src$ patch -p1 --dry-run < eclib-ungnu.patch\?format\=raw 
patching file Makefile
Hunk #4 FAILED at 45.
1 out of 4 hunks FAILED -- saving rejects to file Makefile.rej
patching file Makefile.dynamic
patching file g0n/Makefile
Hunk #2 succeeded at 25 with fuzz 2.
patching file procs/Makefile
Hunk #2 FAILED at 23.
1 out of 6 hunks FAILED -- saving rejects to file procs/Makefile.rej
patching file qcurves/Makefile
patching file qrank/Makefile
```


I am -1 on all the other three patches at this ticket. Some of those might be salvaged, i.e. from the spkg-install patches like the better installation, but the PIC->pic change is just plain wrong.

Cheers,

Michael



---

archive/issue_comments_023372.json:
```json
{
    "body": "Replying to [comment:9 mabshoff]:\n> I think there are some issues with eclib-ungnu.patch:\n> \n>  * the formal changes, i.e. the removal of the \".o\" from the makefiles should be independent of the other changes for reviewing purposes\n>  * some of the fixes will have the makefiles as is working with Sage, but if anyone attempted to compile eclib without explicitly setting env variables like NTL the compile will break or the build will not include features like pari support. I don't care which way we go here, but this is up to John since it is his code project.\n> \n> As is the patch needs to be rebased slighly:\n> {{{\n> /eclib-20080310.p7/src$ patch -p1 --dry-run < eclib-ungnu.patch\\?format\\=raw \n> patching file Makefile\n> Hunk #4 FAILED at 45.\n> 1 out of 4 hunks FAILED -- saving rejects to file Makefile.rej\n> patching file Makefile.dynamic\n> patching file g0n/Makefile\n> Hunk #2 succeeded at 25 with fuzz 2.\n> patching file procs/Makefile\n> Hunk #2 FAILED at 23.\n> 1 out of 6 hunks FAILED -- saving rejects to file procs/Makefile.rej\n> patching file qcurves/Makefile\n> patching file qrank/Makefile\n> }}}\n> \n> I am -1 on all the other three patches at this ticket. Some of those might be salvaged, i.e. from the spkg-install patches like the better installation, but the PIC->pic change is just plain wrong.\n> \n> Cheers,\n> \n> Michael \n\nI am happy to go along with whatever is best for Sage. I agree that one should be able to type \"make\" without setting environment variables manually.  John",
    "created_at": "2008-11-28T22:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23372",
    "user": "@JohnCremona"
}
```

Replying to [comment:9 mabshoff]:
> I think there are some issues with eclib-ungnu.patch:
> 
>  * the formal changes, i.e. the removal of the ".o" from the makefiles should be independent of the other changes for reviewing purposes
>  * some of the fixes will have the makefiles as is working with Sage, but if anyone attempted to compile eclib without explicitly setting env variables like NTL the compile will break or the build will not include features like pari support. I don't care which way we go here, but this is up to John since it is his code project.
> 
> As is the patch needs to be rebased slighly:
> {{{
> /eclib-20080310.p7/src$ patch -p1 --dry-run < eclib-ungnu.patch\?format\=raw 
> patching file Makefile
> Hunk #4 FAILED at 45.
> 1 out of 4 hunks FAILED -- saving rejects to file Makefile.rej
> patching file Makefile.dynamic
> patching file g0n/Makefile
> Hunk #2 succeeded at 25 with fuzz 2.
> patching file procs/Makefile
> Hunk #2 FAILED at 23.
> 1 out of 6 hunks FAILED -- saving rejects to file procs/Makefile.rej
> patching file qcurves/Makefile
> patching file qrank/Makefile
> }}}
> 
> I am -1 on all the other three patches at this ticket. Some of those might be salvaged, i.e. from the spkg-install patches like the better installation, but the PIC->pic change is just plain wrong.
> 
> Cheers,
> 
> Michael 

I am happy to go along with whatever is best for Sage. I agree that one should be able to type "make" without setting environment variables manually.  John



---

archive/issue_comments_023373.json:
```json
{
    "body": "Hi guys,\n\nI am a bit out of action at the moment but I should comment on what I\nhad done and why.\n\nReplying to [comment:9 mabshoff]:\n> I think there are some issues with eclib-ungnu.patch:\n> \n>  * the formal changes, i.e. the removal of the \".o\" from the makefiles should be independent of the other changes for reviewing purposes\n\nI reviewed my patch and the removal of the \".o\" and its inclusion in\n$(OBJ_SUF) and $(SOBJ_SUF) was needed to write a working \".SUFFIXES:\"\nold unix style rule and keep putting \"_n\" in the object. It can be simplified\nif we remove it. It is a remnant of the various building options that weren't\nused in sage but could be restored with a bit of creativity and some environment\nvariables.\n\n>  * some of the fixes will have the makefiles as is working with Sage, but if anyone attempted to compile eclib without explicitly setting env variables like NTL the compile will break or the build will not include features like pari support. I don't care which way we go here, but this is up to John since it is his code project.\n> \n\nThe behavior before and after the patch is currently the same if you\ndon't set any variables. It defaults to look for stuff in /usr/local .\nEither you do some autodetection or you pass variables. It probably \nshould be documented in a README.\n\n> As is the patch needs to be rebased slighly:\n> {{{\n> /eclib-20080310.p7/src$ patch -p1 --dry-run < eclib-ungnu.patch\\?format\\=raw \n> patching file Makefile\n> Hunk #4 FAILED at 45.\n> 1 out of 4 hunks FAILED -- saving rejects to file Makefile.rej\n> patching file Makefile.dynamic\n> patching file g0n/Makefile\n> Hunk #2 succeeded at 25 with fuzz 2.\n> patching file procs/Makefile\n> Hunk #2 FAILED at 23.\n> 1 out of 6 hunks FAILED -- saving rejects to file procs/Makefile.rej\n> patching file qcurves/Makefile\n> patching file qrank/Makefile\n> }}}\n> \n\nI'll have a look and rebase it if that's all it takes.\n\n> I am -1 on all the other three patches at this ticket. Some of those might be salvaged, i.e. from the spkg-install patches like the better installation, but the PIC->pic change is just plain wrong.\n> \n\nThe two first patches are really obsolete in many ways. And yes, after doing\nsome growing up I realise PIC->pic is wrong for something like sage. It is \ndebatable that it could be selected appropriately at the start of the building \nprocess but that wouldn't be KISS.\n\n> Cheers,\n> \n> Michael \n\nCheers,\nFrancois",
    "created_at": "2008-11-29T10:20:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23373",
    "user": "@kiwifb"
}
```

Hi guys,

I am a bit out of action at the moment but I should comment on what I
had done and why.

Replying to [comment:9 mabshoff]:
> I think there are some issues with eclib-ungnu.patch:
> 
>  * the formal changes, i.e. the removal of the ".o" from the makefiles should be independent of the other changes for reviewing purposes

I reviewed my patch and the removal of the ".o" and its inclusion in
$(OBJ_SUF) and $(SOBJ_SUF) was needed to write a working ".SUFFIXES:"
old unix style rule and keep putting "_n" in the object. It can be simplified
if we remove it. It is a remnant of the various building options that weren't
used in sage but could be restored with a bit of creativity and some environment
variables.

>  * some of the fixes will have the makefiles as is working with Sage, but if anyone attempted to compile eclib without explicitly setting env variables like NTL the compile will break or the build will not include features like pari support. I don't care which way we go here, but this is up to John since it is his code project.
> 

The behavior before and after the patch is currently the same if you
don't set any variables. It defaults to look for stuff in /usr/local .
Either you do some autodetection or you pass variables. It probably 
should be documented in a README.

> As is the patch needs to be rebased slighly:
> {{{
> /eclib-20080310.p7/src$ patch -p1 --dry-run < eclib-ungnu.patch\?format\=raw 
> patching file Makefile
> Hunk #4 FAILED at 45.
> 1 out of 4 hunks FAILED -- saving rejects to file Makefile.rej
> patching file Makefile.dynamic
> patching file g0n/Makefile
> Hunk #2 succeeded at 25 with fuzz 2.
> patching file procs/Makefile
> Hunk #2 FAILED at 23.
> 1 out of 6 hunks FAILED -- saving rejects to file procs/Makefile.rej
> patching file qcurves/Makefile
> patching file qrank/Makefile
> }}}
> 

I'll have a look and rebase it if that's all it takes.

> I am -1 on all the other three patches at this ticket. Some of those might be salvaged, i.e. from the spkg-install patches like the better installation, but the PIC->pic change is just plain wrong.
> 

The two first patches are really obsolete in many ways. And yes, after doing
some growing up I realise PIC->pic is wrong for something like sage. It is 
debatable that it could be selected appropriately at the start of the building 
process but that wouldn't be KISS.

> Cheers,
> 
> Michael 

Cheers,
Francois



---

archive/issue_comments_023374.json:
```json
{
    "body": "Attachment [spkg.patch](tarball://root/attachments/some-uuid/ticket3358/spkg.patch) by @kiwifb created at 2008-12-04 10:56:26\n\nnew patch for spkg.install + new patch file for environment variables",
    "created_at": "2008-12-04T10:56:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23374",
    "user": "@kiwifb"
}
```

Attachment [spkg.patch](tarball://root/attachments/some-uuid/ticket3358/spkg.patch) by @kiwifb created at 2008-12-04 10:56:26

new patch for spkg.install + new patch file for environment variables



---

archive/issue_comments_023375.json:
```json
{
    "body": "OK it took me a little bit more time than expected - because of life and going back to this uncovered several \"itches\". So in summary there are two patches.\neclib-ungnu.patch:\n*rebased on 20080310.p7\n*do away with multiple building options we only build with ntl - that simplifies the suffixes of object files.\n*created an install target\n*Got enough of sub-makefile including the top makefile just for environment variables,\ncreating a lot of noise about over-riding target and so on - splitting was the only option that I knew would result in something compatible with BSD make (and incidentally sun make: bonus!).\n\nspkg.patch:\n*rebased on 20080310.p7\n*updated spkg-install to reflect changes in makefiles and the setting of environment variables.\n*included a Makefile.env in the patch directory to put the environment variables correctly for sage.\n\ncheers,\nFrancois",
    "created_at": "2008-12-04T11:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23375",
    "user": "@kiwifb"
}
```

OK it took me a little bit more time than expected - because of life and going back to this uncovered several "itches". So in summary there are two patches.
eclib-ungnu.patch:
*rebased on 20080310.p7
*do away with multiple building options we only build with ntl - that simplifies the suffixes of object files.
*created an install target
*Got enough of sub-makefile including the top makefile just for environment variables,
creating a lot of noise about over-riding target and so on - splitting was the only option that I knew would result in something compatible with BSD make (and incidentally sun make: bonus!).

spkg.patch:
*rebased on 20080310.p7
*updated spkg-install to reflect changes in makefiles and the setting of environment variables.
*included a Makefile.env in the patch directory to put the environment variables correctly for sage.

cheers,
Francois



---

archive/issue_comments_023376.json:
```json
{
    "body": "Thanks Francois,\n\nI have deleted the old and no longer useful patches so that only the two current patches remain. I will review those patches in the near future to avoid bitrot again. \n\nCheers,\n\nMichael",
    "created_at": "2008-12-04T11:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23376",
    "user": "mabshoff"
}
```

Thanks Francois,

I have deleted the old and no longer useful patches so that only the two current patches remain. I will review those patches in the near future to avoid bitrot again. 

Cheers,

Michael



---

archive/issue_comments_023377.json:
```json
{
    "body": "Oh dear me just seen that in the need review message.\nI have to check if it needs a lot of rebasing as it was \nagainst p5. Then may be David Kirby should have a look.",
    "created_at": "2009-12-08T08:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23377",
    "user": "@kiwifb"
}
```

Oh dear me just seen that in the need review message.
I have to check if it needs a lot of rebasing as it was 
against p5. Then may be David Kirby should have a look.



---

archive/issue_comments_023378.json:
```json
{
    "body": "Found problems with qrank's binary and the tests.\nBack to need work. \nHopefully I will update this soonish.",
    "created_at": "2009-12-09T20:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23378",
    "user": "@kiwifb"
}
```

Found problems with qrank's binary and the tests.
Back to need work. 
Hopefully I will update this soonish.



---

archive/issue_comments_023379.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-09T20:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23379",
    "user": "@kiwifb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_023380.json:
```json
{
    "body": "This is obsolete, solved by the current eclib, we should close it.",
    "created_at": "2012-08-05T10:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23380",
    "user": "@kiwifb"
}
```

This is obsolete, solved by the current eclib, we should close it.



---

archive/issue_comments_023381.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-08-05T10:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23381",
    "user": "@kiwifb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_023382.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-08-05T10:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23382",
    "user": "@kiwifb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_023383.json:
```json
{
    "body": "Replying to [comment:16 fbissey]:\n> This is obsolete, solved by the current eclib, we should close it.\n\nAgreed.",
    "created_at": "2012-08-05T12:38:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23383",
    "user": "@JohnCremona"
}
```

Replying to [comment:16 fbissey]:
> This is obsolete, solved by the current eclib, we should close it.

Agreed.



---

archive/issue_comments_023384.json:
```json
{
    "body": "May I remind you to set the milestone to \"sage-duplicate/invalid/wontfix\" in such a case?",
    "created_at": "2012-08-06T13:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23384",
    "user": "@jdemeyer"
}
```

May I remind you to set the milestone to "sage-duplicate/invalid/wontfix" in such a case?



---

archive/issue_comments_023385.json:
```json
{
    "body": "Changing keywords from \"editor_mabshoff\" to \"\".",
    "created_at": "2012-08-06T13:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23385",
    "user": "@jdemeyer"
}
```

Changing keywords from "editor_mabshoff" to "".



---

archive/issue_comments_023386.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-08-06T13:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3358#issuecomment-23386",
    "user": "@jdemeyer"
}
```

Resolution: worksforme
