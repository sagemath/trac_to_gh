# Issue 8076: upgrade GAP to version 4.4.12

archive/issues_008076.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: gap\n\nPlease test [http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg](http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg), in particular on \"exotic\" platforms:  (Itanium Linux), Solaris(?).\nSo far tests are OK on Linux x86, x86_64, ia64 and\nPPC/Intel MacOSX 10.5/10.6.\nIt incorporates a long-awaited upstream GAP patches for Itanium.\n\nIt can be combined with \n[http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg](http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg) (see also trac ticket #8229)and\n[http://boxen.math.washington.edu/home/dima/packages/database_gap-4.4.12.spkg](http://boxen.math.washington.edu/home/dima/packages/database_gap-4.4.12.spkg)\n\n(please ignore the patch in this ticket, it is obsolete and not needed)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8076\n\n",
    "closed_at": "2010-02-17T20:49:35Z",
    "created_at": "2010-01-26T11:54:24Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "upgrade GAP to version 4.4.12",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8076",
    "user": "https://github.com/dimpase"
}
```
Assignee: tbd

Keywords: gap

Please test [http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg](http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg), in particular on "exotic" platforms:  (Itanium Linux), Solaris(?).
So far tests are OK on Linux x86, x86_64, ia64 and
PPC/Intel MacOSX 10.5/10.6.
It incorporates a long-awaited upstream GAP patches for Itanium.

It can be combined with 
[http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg](http://boxen.math.washington.edu/home/dima/packages/gap_packages-4.4.12_2.spkg) (see also trac ticket #8229)and
[http://boxen.math.washington.edu/home/dima/packages/database_gap-4.4.12.spkg](http://boxen.math.washington.edu/home/dima/packages/database_gap-4.4.12.spkg)

(please ignore the patch in this ticket, it is obsolete and not needed)


Issue created by migration from https://trac.sagemath.org/ticket/8076





---

archive/issue_comments_070638.json:
```json
{
    "body": "It builds fine, and Gap seems to work.   The major workspaces issue seems gone.    Bravo!  Thanks to Steve Linton and dimpase!\n\nThe repo needs to have its changed checked in:\n\n```\nwstein@iras:~/screen/iras/sage-4.3.1/gap-4.4.12.p2> ../sage -hg status\nM .hgignore\nM SPKG.txt\n? patches/saveload.patch\nwstein@iras:~/screen/iras/sage-4.3.1/gap-4.4.12.p2>\n```\n\nThis needs an `hg ci`.\n\nThe changes to the spkg look fine.  I'm guess I'm OK with the comment \"(not using the usual patches/* procedure, as this is an upstream patch.)\", though I would personally never do things that way -- to me src/ should be pristine.    \n\nI give this a positive review, subject to the other doctests in the core Sage library being fixed to reflect the new package update, e.g., things like\n\n```\nwstein@iras:~/screen/iras/sage-4.3.1> ./sage -t devel/sage/sage/interfaces/gap.py \nsage -t  \"devel/sage/sage/interfaces/gap.py\"                                      \n**********************************************************************\nFile \"/home/wstein/screen/iras/sage-4.3.1/devel/sage/sage/interfaces/gap.py\", line 821:\n    sage: gap.version()\nExpected:\n    '4.4.10'\nGot:\n    '4.4.12'\n```\n\n\n\n -- William",
    "created_at": "2010-01-26T16:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70638",
    "user": "https://github.com/williamstein"
}
```

It builds fine, and Gap seems to work.   The major workspaces issue seems gone.    Bravo!  Thanks to Steve Linton and dimpase!

The repo needs to have its changed checked in:

```
wstein@iras:~/screen/iras/sage-4.3.1/gap-4.4.12.p2> ../sage -hg status
M .hgignore
M SPKG.txt
? patches/saveload.patch
wstein@iras:~/screen/iras/sage-4.3.1/gap-4.4.12.p2>
```

This needs an `hg ci`.

The changes to the spkg look fine.  I'm guess I'm OK with the comment "(not using the usual patches/* procedure, as this is an upstream patch.)", though I would personally never do things that way -- to me src/ should be pristine.    

I give this a positive review, subject to the other doctests in the core Sage library being fixed to reflect the new package update, e.g., things like

```
wstein@iras:~/screen/iras/sage-4.3.1> ./sage -t devel/sage/sage/interfaces/gap.py 
sage -t  "devel/sage/sage/interfaces/gap.py"                                      
**********************************************************************
File "/home/wstein/screen/iras/sage-4.3.1/devel/sage/sage/interfaces/gap.py", line 821:
    sage: gap.version()
Expected:
    '4.4.10'
Got:
    '4.4.12'
```



 -- William



---

archive/issue_comments_070639.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-26T16:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70639",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070640.json:
```json
{
    "body": "Attachment [13702.patch](tarball://root/attachments/some-uuid/ticket8076/13702.patch) by @dimpase created at 2010-01-27 03:32:51\n\nchanging GAP version to 4.4.12",
    "created_at": "2010-01-27T03:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70640",
    "user": "https://github.com/dimpase"
}
```

Attachment [13702.patch](tarball://root/attachments/some-uuid/ticket8076/13702.patch) by @dimpase created at 2010-01-27 03:32:51

changing GAP version to 4.4.12



---

archive/issue_comments_070641.json:
```json
{
    "body": "attached a patch to bump up version in interfaces/gap.py\n\nupdated the gap-4.4.12 spkg at the URL above to fix the repo issue (hopefully) \n\nPlease check these. Thanks!",
    "created_at": "2010-01-27T03:38:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70641",
    "user": "https://github.com/dimpase"
}
```

attached a patch to bump up version in interfaces/gap.py

updated the gap-4.4.12 spkg at the URL above to fix the repo issue (hopefully) 

Please check these. Thanks!



---

archive/issue_comments_070642.json:
```json
{
    "body": "Is there a patch that also fixes all the ordering issues that were discussed (the conjugacy classes, etc)?",
    "created_at": "2010-01-27T11:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70642",
    "user": "https://github.com/wdjoyner"
}
```

Is there a patch that also fixes all the ordering issues that were discussed (the conjugacy classes, etc)?



---

archive/issue_comments_070643.json:
```json
{
    "body": "working on the latter. \nWill use TESTS:: instead of EXAMPLES::, and whenever necessary, mark EXAMPLES:: as \"not tested\"",
    "created_at": "2010-01-31T06:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70643",
    "user": "https://github.com/dimpase"
}
```

working on the latter. 
Will use TESTS:: instead of EXAMPLES::, and whenever necessary, mark EXAMPLES:: as "not tested"



---

archive/issue_comments_070644.json:
```json
{
    "body": "Ticket #6348 is a duplicate of this.",
    "created_at": "2010-02-02T07:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70644",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Ticket #6348 is a duplicate of this.



---

archive/issue_comments_070645.json:
```json
{
    "body": "Replying to [comment:6 mvngu]:\n> Ticket #6348 is a duplicate of this.\n\nit could be, but this is a new version of the spkg's in question, that\nin particular incorporated a new patch by Steve Linton and fixed the stopper problem (crashes on Linux ia64 that occured with\nprevious spkg vesrions)\n\nI am about to open up a new trac ticket with a grand patch fixing the doctrings\naffected.",
    "created_at": "2010-02-02T09:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70645",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:6 mvngu]:
> Ticket #6348 is a duplicate of this.

it could be, but this is a new version of the spkg's in question, that
in particular incorporated a new patch by Steve Linton and fixed the stopper problem (crashes on Linux ia64 that occured with
previous spkg vesrions)

I am about to open up a new trac ticket with a grand patch fixing the doctrings
affected.



---

archive/issue_comments_070646.json:
```json
{
    "body": "Replying to [comment:4 wdj]:\n> Is there a patch that also fixes all the ordering issues that were discussed (the conjugacy classes, etc)?\n\n\nplease see trac ticket\n\n#8150\n\nfor this patch (at least it fixes all the -t -long sage/groups/ docstring problems)",
    "created_at": "2010-02-02T09:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70646",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:4 wdj]:
> Is there a patch that also fixes all the ordering issues that were discussed (the conjugacy classes, etc)?


please see trac ticket

#8150

for this patch (at least it fixes all the -t -long sage/groups/ docstring problems)



---

archive/issue_comments_070647.json:
```json
{
    "body": "Replying to [comment:4 wdj]:\n> Is there a patch that also fixes all the ordering issues that were discussed (the conjugacy classes, etc)?\n\n\nas #8150 is done, could you please review this ticket, too, too, to have it all set, formally speaking? Thanks!",
    "created_at": "2010-02-05T16:30:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70647",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:4 wdj]:
> Is there a patch that also fixes all the ordering issues that were discussed (the conjugacy classes, etc)?


as #8150 is done, could you please review this ticket, too, too, to have it all set, formally speaking? Thanks!



---

archive/issue_comments_070648.json:
```json
{
    "body": "Tested on a mac 10.6.2 and ubuntu 9.10. \n\nPositive review from me too (see also William Stein's review above).",
    "created_at": "2010-02-13T00:39:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70648",
    "user": "https://github.com/wdjoyner"
}
```

Tested on a mac 10.6.2 and ubuntu 9.10. 

Positive review from me too (see also William Stein's review above).



---

archive/issue_comments_070649.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-13T00:39:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70649",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070650.json:
```json
{
    "body": "Something is wrong with the package [gap-4.4.12.p2.spkg](http://www1.spms.ntu.edu.sg/~dima/tmp/gap-4.4.12.p2.spkg). First, all changes are not checked in:\n\n```\n[mvngu@sage gap-4.4.12.p2]$ hg st\nM .hgignore\nM SPKG.txt\n```\nSecond, the directory `patches/` must be under revision control, so the file `.hgignore` must not contain the line `patches/`:\n\n```\n[mvngu@sage gap-4.4.12.p2]$ cat .hgignore \nsrc/\npatches/\n```\nThird, I can't check anything in:\n\n```\n[mvngu@sage gap-4.4.12.p2]$ hg ci\n<enter-commit-message>\nabort: data/.hgignore.i@bc8f0f49e4a4: no node!\n```\nAm I using the correct version of the spkg to be updated?",
    "created_at": "2010-02-13T06:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70650",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Something is wrong with the package [gap-4.4.12.p2.spkg](http://www1.spms.ntu.edu.sg/~dima/tmp/gap-4.4.12.p2.spkg). First, all changes are not checked in:

```
[mvngu@sage gap-4.4.12.p2]$ hg st
M .hgignore
M SPKG.txt
```
Second, the directory `patches/` must be under revision control, so the file `.hgignore` must not contain the line `patches/`:

```
[mvngu@sage gap-4.4.12.p2]$ cat .hgignore 
src/
patches/
```
Third, I can't check anything in:

```
[mvngu@sage gap-4.4.12.p2]$ hg ci
<enter-commit-message>
abort: data/.hgignore.i@bc8f0f49e4a4: no node!
```
Am I using the correct version of the spkg to be updated?



---

archive/issue_comments_070651.json:
```json
{
    "body": "Replying to [comment:12 mvngu]:\n\nThe question is which version is \"right\". Gap 4.4.12 was never a part of Sage,\nso perhaps the proper package name is\ngap-4.4.12.spkg ?\n\nIf yes, can I just wipe out .hg directory there and re-initialise hg ?\n\nIt's better to use the files located at\nhttp://boxen.math.washington.edu/home/dima/packages/\nrather than at http://www1.spms.ntu.edu.sg/~dima/tmp/\n(the connection is not always stable, etc. http://boxen.math.washington.edu/home/dima/packages/\ncontains copies of spkg's on http://www1.spms.ntu.edu.sg/~dima/tmp/)\n\n\n> Something is wrong with the package [gap-4.4.12.p2.spkg](http://www1.spms.ntu.edu.sg/~dima/tmp/gap-4.4.12.p2.spkg). First, all changes are not checked in:\n> \n> ```\n> [mvngu@sage gap-4.4.12.p2]$ hg st\n> M .hgignore\n> M SPKG.txt\n> ```\n> Second, the directory `patches/` must be under revision control, so the file `.hgignore` must not contain the line `patches/`:\n> \n> ```\n> [mvngu@sage gap-4.4.12.p2]$ cat .hgignore \n> src/\n> patches/\n> ```\n> Third, I can't check anything in:\n> \n> ```\n> [mvngu@sage gap-4.4.12.p2]$ hg ci\n> <enter-commit-message>\n> abort: data/.hgignore.i@bc8f0f49e4a4: no node!\n> ```\n> Am I using the correct version of the spkg to be updated?",
    "created_at": "2010-02-13T14:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70651",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:12 mvngu]:

The question is which version is "right". Gap 4.4.12 was never a part of Sage,
so perhaps the proper package name is
gap-4.4.12.spkg ?

If yes, can I just wipe out .hg directory there and re-initialise hg ?

It's better to use the files located at
http://boxen.math.washington.edu/home/dima/packages/
rather than at http://www1.spms.ntu.edu.sg/~dima/tmp/
(the connection is not always stable, etc. http://boxen.math.washington.edu/home/dima/packages/
contains copies of spkg's on http://www1.spms.ntu.edu.sg/~dima/tmp/)


> Something is wrong with the package [gap-4.4.12.p2.spkg](http://www1.spms.ntu.edu.sg/~dima/tmp/gap-4.4.12.p2.spkg). First, all changes are not checked in:
> 
> ```
> [mvngu@sage gap-4.4.12.p2]$ hg st
> M .hgignore
> M SPKG.txt
> ```
> Second, the directory `patches/` must be under revision control, so the file `.hgignore` must not contain the line `patches/`:
> 
> ```
> [mvngu@sage gap-4.4.12.p2]$ cat .hgignore 
> src/
> patches/
> ```
> Third, I can't check anything in:
> 
> ```
> [mvngu@sage gap-4.4.12.p2]$ hg ci
> <enter-commit-message>
> abort: data/.hgignore.i@bc8f0f49e4a4: no node!
> ```
> Am I using the correct version of the spkg to be updated?



---

archive/issue_comments_070652.json:
```json
{
    "body": "Replying to [comment:12 mvngu]:\n\nI have fixed the hg issues and uploaded the revised version to\n[http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg](http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg)\n\napparently, editing .hgignore at the wrong time wreaks havoc in .hg...\n\n> Something is wrong with the package [gap-4.4.12.p2.spkg](http://www1.spms.ntu.edu.sg/~dima/tmp/gap-4.4.12.p2.spkg). First, all changes are not checked in:\n> \n> ```\n> [mvngu@sage gap-4.4.12.p2]$ hg st\n> M .hgignore\n> M SPKG.txt\n> ```\n> Second, the directory `patches/` must be under revision control, so the file `.hgignore` must not contain the line `patches/`:\n> \n> ```\n> [mvngu@sage gap-4.4.12.p2]$ cat .hgignore \n> src/\n> patches/\n> ```\n> Third, I can't check anything in:\n> \n> ```\n> [mvngu@sage gap-4.4.12.p2]$ hg ci\n> <enter-commit-message>\n> abort: data/.hgignore.i@bc8f0f49e4a4: no node!\n> ```\n> Am I using the correct version of the spkg to be updated?",
    "created_at": "2010-02-14T07:14:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70652",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:12 mvngu]:

I have fixed the hg issues and uploaded the revised version to
[http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg](http://boxen.math.washington.edu/home/dima/packages/gap-4.4.12.p2.spkg)

apparently, editing .hgignore at the wrong time wreaks havoc in .hg...

> Something is wrong with the package [gap-4.4.12.p2.spkg](http://www1.spms.ntu.edu.sg/~dima/tmp/gap-4.4.12.p2.spkg). First, all changes are not checked in:
> 
> ```
> [mvngu@sage gap-4.4.12.p2]$ hg st
> M .hgignore
> M SPKG.txt
> ```
> Second, the directory `patches/` must be under revision control, so the file `.hgignore` must not contain the line `patches/`:
> 
> ```
> [mvngu@sage gap-4.4.12.p2]$ cat .hgignore 
> src/
> patches/
> ```
> Third, I can't check anything in:
> 
> ```
> [mvngu@sage gap-4.4.12.p2]$ hg ci
> <enter-commit-message>
> abort: data/.hgignore.i@bc8f0f49e4a4: no node!
> ```
> Am I using the correct version of the spkg to be updated?



---

archive/issue_comments_070653.json:
```json
{
    "body": "If all you did was change the hg-related files then I don't think this needs retesting. If this is wrong, please correct me.",
    "created_at": "2010-02-14T12:19:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70653",
    "user": "https://github.com/wdjoyner"
}
```

If all you did was change the hg-related files then I don't think this needs retesting. If this is wrong, please correct me.



---

archive/issue_comments_070654.json:
```json
{
    "body": "Replying to [comment:16 wdj]:\n> If all you did was change the hg-related files then I don't think this needs retesting. If this is wrong, please correct me.\n\n\nThat's correct, I just changed the hg-related files, and updated the trac ticket descriptions. \n\nI changed URLs there, so now they point to the files on boxen in my\naccount there, rather than to anything else. But this is just administration, the code did not change. I imagine there would be more testing done when they go into a Sage pre-release, and you have already tested the updated gap_packages spkg.\n(and certainly I did some testing of the updated gap spkg-file)",
    "created_at": "2010-02-14T13:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70654",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:16 wdj]:
> If all you did was change the hg-related files then I don't think this needs retesting. If this is wrong, please correct me.


That's correct, I just changed the hg-related files, and updated the trac ticket descriptions. 

I changed URLs there, so now they point to the files on boxen in my
account there, rather than to anything else. But this is just administration, the code did not change. I imagine there would be more testing done when they go into a Sage pre-release, and you have already tested the updated gap_packages spkg.
(and certainly I did some testing of the updated gap spkg-file)



---

archive/issue_comments_070655.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-15T04:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70655",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_070656.json:
```json
{
    "body": "Here are some issues with the latest updated spkg:\n\n* It wiped out the entire commit history of all versions of the GAP spkg prior to 4.4.12.\n* The changelog `SPKG.txt` does not conform to the requirements as documented in the [Developer's Guide](http://www.sagemath.org/doc/developer/producing_spkgs.html#the-file-spkg-txt).",
    "created_at": "2010-02-15T04:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70656",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Here are some issues with the latest updated spkg:

* It wiped out the entire commit history of all versions of the GAP spkg prior to 4.4.12.
* The changelog `SPKG.txt` does not conform to the requirements as documented in the [Developer's Guide](http://www.sagemath.org/doc/developer/producing_spkgs.html#the-file-spkg-txt).



---

archive/issue_comments_070657.json:
```json
{
    "body": "What happened to `gap-4.4.12.spkg`, `gap-4.4.12.p0.spkg`, and `gap-4.4.12.p1.spkg`?",
    "created_at": "2010-02-15T04:45:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70657",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

What happened to `gap-4.4.12.spkg`, `gap-4.4.12.p0.spkg`, and `gap-4.4.12.p1.spkg`?



---

archive/issue_comments_070658.json:
```json
{
    "body": "Replying to [comment:19 mvngu]:\n> What happened to `gap-4.4.12.spkg`, `gap-4.4.12.p0.spkg`, and `gap-4.4.12.p1.spkg`?\n\n\nI picked up the package made by wdj and did a bit of fixing.\nNone of p0, p1 ever made it to Sage.\nThat's why I ask whether we should really be calling it p2, and not just \ngap-4.4.12.spkg",
    "created_at": "2010-02-15T04:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70658",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:19 mvngu]:
> What happened to `gap-4.4.12.spkg`, `gap-4.4.12.p0.spkg`, and `gap-4.4.12.p1.spkg`?


I picked up the package made by wdj and did a bit of fixing.
None of p0, p1 ever made it to Sage.
That's why I ask whether we should really be calling it p2, and not just 
gap-4.4.12.spkg



---

archive/issue_comments_070659.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-15T05:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70659",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070660.json:
```json
{
    "body": "Replying to [comment:18 mvngu]:\n> Here are some issues with the latest updated spkg:\n> \n> * It wiped out the entire commit history of all versions of the GAP spkg prior to 4.4.12.\n\n\nWell, the .hg/ broke down, as you have noticed.\nSo I wiped it out. \nNow I copied .hg/ from gap-4.4.10.p13.spkg\nand merged the changes there. Please check the updated spkg file.\n\n>  * The changelog `SPKG.txt` does not conform to the requirements as documented in the [Developer's Guide](http://www.sagemath.org/doc/developer/producing_spkgs.html#the-file-spkg-txt).\n\n\nFixed. Please check the updated spkg file.",
    "created_at": "2010-02-15T05:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70660",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:18 mvngu]:
> Here are some issues with the latest updated spkg:
> 
> * It wiped out the entire commit history of all versions of the GAP spkg prior to 4.4.12.


Well, the .hg/ broke down, as you have noticed.
So I wiped it out. 
Now I copied .hg/ from gap-4.4.10.p13.spkg
and merged the changes there. Please check the updated spkg file.

>  * The changelog `SPKG.txt` does not conform to the requirements as documented in the [Developer's Guide](http://www.sagemath.org/doc/developer/producing_spkgs.html#the-file-spkg-txt).


Fixed. Please check the updated spkg file.



---

archive/issue_comments_070661.json:
```json
{
    "body": "If you have not changed the code and only the hg stuff, then I think I can leave the review to Minh, who knows mercurial much better than I do. If you changed the code so that the package needs testing, please let me know.",
    "created_at": "2010-02-15T12:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70661",
    "user": "https://github.com/wdjoyner"
}
```

If you have not changed the code and only the hg stuff, then I think I can leave the review to Minh, who knows mercurial much better than I do. If you changed the code so that the package needs testing, please let me know.



---

archive/issue_comments_070662.json:
```json
{
    "body": "Replying to [comment:22 wdj]:\n> If you have not changed the code and only the hg stuff, then I think I can leave the review to Minh, who knows mercurial much better than I do. If you changed the code so that the package needs testing, please let me know.\n\n\nI changed $CP to cp, $RM to rm, etc., in spkg-install.\nThat was all, as far as code goes. The rest was hg stuff and documentation.",
    "created_at": "2010-02-15T12:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70662",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:22 wdj]:
> If you have not changed the code and only the hg stuff, then I think I can leave the review to Minh, who knows mercurial much better than I do. If you changed the code so that the package needs testing, please let me know.


I changed $CP to cp, $RM to rm, etc., in spkg-install.
That was all, as far as code goes. The rest was hg stuff and documentation.



---

archive/issue_comments_070663.json:
```json
{
    "body": "This seems to apply fine and pass the same tests as before. at least on a mac 10.6.2. Again, I guess I leave this to Minh to give a positive review.",
    "created_at": "2010-02-15T20:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70663",
    "user": "https://github.com/wdjoyner"
}
```

This seems to apply fine and pass the same tests as before. at least on a mac 10.6.2. Again, I guess I leave this to Minh to give a positive review.



---

archive/issue_comments_070664.json:
```json
{
    "body": "I assume that I don't need to apply [13702.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8076/13702.patch) since it's already covered by #8150.",
    "created_at": "2010-02-17T06:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70664",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I assume that I don't need to apply [13702.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8076/13702.patch) since it's already covered by #8150.



---

archive/issue_comments_070665.json:
```json
{
    "body": "Replying to [comment:25 mvngu]:\n> I assume that I don't need to apply [13702.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8076/13702.patch) since it's already covered by #8150.\n\n\nthat's correct.",
    "created_at": "2010-02-17T06:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70665",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:25 mvngu]:
> I assume that I don't need to apply [13702.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8076/13702.patch) since it's already covered by #8150.


that's correct.



---

archive/issue_comments_070666.json:
```json
{
    "body": "Someone reading the changelog of the GAP spkg would come across this snippet:\n\n```\n### gap-4.4.12.p2 (Dima Pasechnik, 2010-1-25)\n\n * Added .hgignore.\n *  Applied Steve Linton's Itanium patch to GAP_ROOT/src/saveload.c\n   (not using the usual patches/* procedure, as this is\n   an upstream patch.)\n *  Removed a stray binary file \"patch\" at the top level.\n *  Replaced $LN, $MKDIR, etc as done in gap-4.4.10.p13 (see below)\n\n### gap-4.4.12.p0 (David Joyner, 2009-6-17)\n\nUpgraded to gap-4.4.12. Removed guava compilation. From the source\nGAP tarball, removed tomlib, small, prim, trans.\n```\nand wonder what happened to `gap-4.4.12.p1`. The updated spkg is OK by me, but I have changed its name to `gap-4.4.12.p1` and its changelog now reads:\n\n```\n### gap-4.4.12.p1 (Dima Pasechnik, 2010-1-25)\n * See ticket #8076 for full details.\n * Added .hgignore.\n * Applied Steve Linton's Itanium patch to GAP_ROOT/src/saveload.c\n   (not using the usual patches/* procedure, as this is\n   an upstream patch.)\n *  Removed a stray binary file \"patch\" at the top level.\n *  Replaced $LN, $MKDIR, etc as done in gap-4.4.10.p13 (see below)\n\n### gap-4.4.12.p0 (David Joyner, 2009-6-17)\n * Upgraded to gap-4.4.12. Removed guava compilation. From the source\n   GAP tarball, removed tomlib, small, prim, trans.\n```\nRemember to reference the ticket number, both in the commit message and in the changelog. The updated spkg with the above name and changelog changes is up at\n\nhttp://sage.math.washington.edu/home/mvngu/spkg/standard/gap/gap-4.4.12.p1.spkg",
    "created_at": "2010-02-17T15:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70666",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Someone reading the changelog of the GAP spkg would come across this snippet:

```
### gap-4.4.12.p2 (Dima Pasechnik, 2010-1-25)

 * Added .hgignore.
 *  Applied Steve Linton's Itanium patch to GAP_ROOT/src/saveload.c
   (not using the usual patches/* procedure, as this is
   an upstream patch.)
 *  Removed a stray binary file "patch" at the top level.
 *  Replaced $LN, $MKDIR, etc as done in gap-4.4.10.p13 (see below)

### gap-4.4.12.p0 (David Joyner, 2009-6-17)

Upgraded to gap-4.4.12. Removed guava compilation. From the source
GAP tarball, removed tomlib, small, prim, trans.
```
and wonder what happened to `gap-4.4.12.p1`. The updated spkg is OK by me, but I have changed its name to `gap-4.4.12.p1` and its changelog now reads:

```
### gap-4.4.12.p1 (Dima Pasechnik, 2010-1-25)
 * See ticket #8076 for full details.
 * Added .hgignore.
 * Applied Steve Linton's Itanium patch to GAP_ROOT/src/saveload.c
   (not using the usual patches/* procedure, as this is
   an upstream patch.)
 *  Removed a stray binary file "patch" at the top level.
 *  Replaced $LN, $MKDIR, etc as done in gap-4.4.10.p13 (see below)

### gap-4.4.12.p0 (David Joyner, 2009-6-17)
 * Upgraded to gap-4.4.12. Removed guava compilation. From the source
   GAP tarball, removed tomlib, small, prim, trans.
```
Remember to reference the ticket number, both in the commit message and in the changelog. The updated spkg with the above name and changelog changes is up at

http://sage.math.washington.edu/home/mvngu/spkg/standard/gap/gap-4.4.12.p1.spkg



---

archive/issue_comments_070667.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-17T15:13:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70667",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070668.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-17T20:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70668",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_070669.json:
```json
{
    "body": "Merged [gap-4.4.12.p1.spkg](http://sage.math.washington.edu/home/mvngu/spkg/standard/gap/gap-4.4.12.p1.spkg) in the standard spkg repository.",
    "created_at": "2010-02-17T20:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8076#issuecomment-70669",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [gap-4.4.12.p1.spkg](http://sage.math.washington.edu/home/mvngu/spkg/standard/gap/gap-4.4.12.p1.spkg) in the standard spkg repository.



---

archive/issue_events_019343.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-17T20:49:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8076",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8076#event-19343"
}
```
