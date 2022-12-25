# Issue 4441: [with patch, needs review] fixes to the doc repo

archive/issues_004441.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nSplitted away from #4370 as the reviewer requested.\nThe patch is identical and was just renamed.\nFrom #4370:\n  After applying the patch to devel/doc, you have to do there once:\n\n  chmod a+x needed_additions_Sage-3.2.alpha2_doc-repository\n\n  ./needed_additions_Sage-3.2.alpha2_doc-repository\n\n  (Writing that script was faster than trying to explain what to do with words.)\n\nI was tempted to give this ticket the priority \"blocker\" :-)\n\nNow seriously, this should be taken in ASAP for two reasons.\nFirstly, it removes the build of two obsolete chapters of no-more-existing modules in the documentation (sage.modular.abvar.torsion_point, sage.modular.abvar.hecke_operator), whose contents are currently doubled (the contents being currently also in sage.modular.abvar.finite_subgroup resp. sage.modular.abvar.morphism).\nSecondly, and much more importantly, it puts the doc repo in a clean state, in order to start with the ReST integration.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4441\n\n",
    "created_at": "2008-11-04T21:15:17Z",
    "labels": [
        "component: documentation",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, needs review] fixes to the doc repo",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4441",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```
Assignee: GeorgSWeber

Splitted away from #4370 as the reviewer requested.
The patch is identical and was just renamed.
From #4370:
  After applying the patch to devel/doc, you have to do there once:

  chmod a+x needed_additions_Sage-3.2.alpha2_doc-repository

  ./needed_additions_Sage-3.2.alpha2_doc-repository

  (Writing that script was faster than trying to explain what to do with words.)

I was tempted to give this ticket the priority "blocker" :-)

Now seriously, this should be taken in ASAP for two reasons.
Firstly, it removes the build of two obsolete chapters of no-more-existing modules in the documentation (sage.modular.abvar.torsion_point, sage.modular.abvar.hecke_operator), whose contents are currently doubled (the contents being currently also in sage.modular.abvar.finite_subgroup resp. sage.modular.abvar.morphism).
Secondly, and much more importantly, it puts the doc repo in a clean state, in order to start with the ReST integration.

Issue created by migration from https://trac.sagemath.org/ticket/4441





---

archive/issue_comments_032596.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-04T21:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4441#issuecomment-32596",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032597.json:
```json
{
    "body": "I wanted 4370-sage_library.patch - the attached patch also need to change since the ReST transformation will start with a clean repo, i.e. we will nuke the old repo. The bit from the patch that removes the old and no longer existing input files should go in.\n\nAnd by the way: my doc repo does not need any fixes:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha3/devel/doc$ hg status\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha3/devel/doc$ hg verify\nchecking changesets\nchecking manifests\ncrosschecking files in changesets and manifests\nchecking files\n149 files, 683 changesets, 964 total revisions\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha3/devel/doc$\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-11-04T21:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4441#issuecomment-32597",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I wanted 4370-sage_library.patch - the attached patch also need to change since the ReST transformation will start with a clean repo, i.e. we will nuke the old repo. The bit from the patch that removes the old and no longer existing input files should go in.

And by the way: my doc repo does not need any fixes:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha3/devel/doc$ hg status
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha3/devel/doc$ hg verify
checking changesets
checking manifests
crosschecking files in changesets and manifests
checking files
149 files, 683 changesets, 964 total revisions
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha3/devel/doc$
```


Cheers,

Michael



---

archive/issue_comments_032598.json:
```json
{
    "body": "Ok, I see the congroup fixes are now at #4442. So you can ignore that part of the comment.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-04T21:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4441#issuecomment-32598",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, I see the congroup fixes are now at #4442. So you can ignore that part of the comment.

Cheers,

Michael



---

archive/issue_comments_032599.json:
```json
{
    "body": "Hi, after the patch:\n\n```\nsusanne-webers-computer:~/Public/sage/sage-3.2.alpha2/devel/doc georgweber$ hg verify\nchecking changesets\nchecking manifests\ncrosschecking files in changesets and manifests\nchecking files\n185 files, 683 changesets, 999 total revisions\n```\n\nThat's 185 files now, and not only 149!\n\nThe main focus is to add essential files to the repo for the first time (!), but only those that are needed/important to be complete after doing a \"hg clone\".\n\nIMHO, the wording \"fixing the doc repo\" is appropriate if even the basic \"Makefile\" and \"Makefile.deps\" files are missing entirely from a spkg hg repository. Although formally the repo isn't broken, it is not of much use in this incomplete state.\n\nThe many, many other files not in the doc hg repo, but currently delivered with the doc spkg, should definitely \"jump over the blade\" in the ReST transition. But those 36 (=185-149) files addressed in the patch should not. (Another dozen or so of these 36 files could be disposed of easily, too, but that would require changes in the Makefile).\n\nPlease consider the patch as-is again, thanks!",
    "created_at": "2008-11-04T22:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4441#issuecomment-32599",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Hi, after the patch:

```
susanne-webers-computer:~/Public/sage/sage-3.2.alpha2/devel/doc georgweber$ hg verify
checking changesets
checking manifests
crosschecking files in changesets and manifests
checking files
185 files, 683 changesets, 999 total revisions
```

That's 185 files now, and not only 149!

The main focus is to add essential files to the repo for the first time (!), but only those that are needed/important to be complete after doing a "hg clone".

IMHO, the wording "fixing the doc repo" is appropriate if even the basic "Makefile" and "Makefile.deps" files are missing entirely from a spkg hg repository. Although formally the repo isn't broken, it is not of much use in this incomplete state.

The many, many other files not in the doc hg repo, but currently delivered with the doc spkg, should definitely "jump over the blade" in the ReST transition. But those 36 (=185-149) files addressed in the patch should not. (Another dozen or so of these 36 files could be disposed of easily, too, but that would require changes in the Makefile).

Please consider the patch as-is again, thanks!



---

archive/issue_comments_032600.json:
```json
{
    "body": "Nope, I see no point adding those files to the repo since they will be deleted anyway. Adding those files will onlu needlessly increase the size.\n\nWhen one runs -sdist there are files that are copied over into the new spkg that are not in the hg repo, so *if* we were to merge such a patch it would not add the files to the repo. Since we are waiting for ReST anyway the patch will not go into 3.2.\n\nPlease post a patch removing the two stale files from ref/modabvar.tex - negative review on the script.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-04T22:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4441#issuecomment-32600",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nope, I see no point adding those files to the repo since they will be deleted anyway. Adding those files will onlu needlessly increase the size.

When one runs -sdist there are files that are copied over into the new spkg that are not in the hg repo, so *if* we were to merge such a patch it would not add the files to the repo. Since we are waiting for ReST anyway the patch will not go into 3.2.

Please post a patch removing the two stale files from ref/modabvar.tex - negative review on the script.

Cheers,

Michael



---

archive/issue_comments_032601.json:
```json
{
    "body": "apply only this one",
    "created_at": "2008-11-05T06:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4441#issuecomment-32601",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

apply only this one



---

archive/issue_comments_032602.json:
```json
{
    "body": "Attachment [4441-modabvar.patch](tarball://root/attachments/some-uuid/ticket4441/4441-modabvar.patch) by GeorgSWeber created at 2008-11-05 07:02:14\n\nHi Michael, thanks for your patience.\n\nI'm still the newbie in the learning phase. Obviously, the current sage documentation repo does not miss files, but contains too many. It probably would have been sufficient in the past if only certain tex files would have been in there, like prog.tex.\n\n>Please post a patch removing the two stale files from ref/modabvar.tex \nHere you go.",
    "created_at": "2008-11-05T07:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4441#issuecomment-32602",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [4441-modabvar.patch](tarball://root/attachments/some-uuid/ticket4441/4441-modabvar.patch) by GeorgSWeber created at 2008-11-05 07:02:14

Hi Michael, thanks for your patience.

I'm still the newbie in the learning phase. Obviously, the current sage documentation repo does not miss files, but contains too many. It probably would have been sufficient in the past if only certain tex files would have been in there, like prog.tex.

>Please post a patch removing the two stale files from ref/modabvar.tex 
Here you go.



---

archive/issue_comments_032603.json:
```json
{
    "body": "Changing priority from critical to minor.",
    "created_at": "2008-11-05T07:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4441#issuecomment-32603",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing priority from critical to minor.



---

archive/issue_comments_032604.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-05T20:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4441#issuecomment-32604",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_032605.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-05T20:24:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4441#issuecomment-32605",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_010033.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-05T20:24:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4441",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4441#event-10033"
}
```



---

archive/issue_comments_032606.json:
```json
{
    "body": "Merged in Sage 3.2.alpha3",
    "created_at": "2008-11-05T20:24:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4441#issuecomment-32606",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha3
