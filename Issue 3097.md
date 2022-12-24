# Issue 3097: pbuild: make sure the files from setup.py's scripts section are copied

archive/issues_003097.json:
```json
{
    "body": "Assignee: mabshoff\n\nIf one uses pbuild to build the Sage library the files from the scripts section are not copied into $SAGE_ROOT/local/bin:\n\n```\n      scripts = ['sage/dsage/scripts/dsage_worker.py',\n                 'sage/dsage/scripts/dsage_setup.py',\n                 'spkg-debian-maybe',\n                ],\n```\n\nErgo DSage's doctest just hang at 0% CPU use.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3097\n\n",
    "created_at": "2008-05-03T15:18:09Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "pbuild: make sure the files from setup.py's scripts section are copied",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3097",
    "user": "mabshoff"
}
```
Assignee: mabshoff

If one uses pbuild to build the Sage library the files from the scripts section are not copied into $SAGE_ROOT/local/bin:

```
      scripts = ['sage/dsage/scripts/dsage_worker.py',
                 'sage/dsage/scripts/dsage_setup.py',
                 'spkg-debian-maybe',
                ],
```

Ergo DSage's doctest just hang at 0% CPU use.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3097





---

archive/issue_comments_021374.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-05-03T15:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3097#issuecomment-21374",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_021375.json:
```json
{
    "body": "Changing assignee from mabshoff to @garyfurnish.",
    "created_at": "2008-05-04T04:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3097#issuecomment-21375",
    "user": "mabshoff"
}
```

Changing assignee from mabshoff to @garyfurnish.



---

archive/issue_comments_021376.json:
```json
{
    "body": "Changing component from build to pbuild.",
    "created_at": "2008-05-04T04:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3097#issuecomment-21376",
    "user": "mabshoff"
}
```

Changing component from build to pbuild.



---

archive/issue_comments_021377.json:
```json
{
    "body": "Attachment [trac_3097.patch](tarball://root/attachments/some-uuid/ticket3097/trac_3097.patch) by @garyfurnish created at 2008-05-04 11:55:06",
    "created_at": "2008-05-04T11:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3097#issuecomment-21377",
    "user": "@garyfurnish"
}
```

Attachment [trac_3097.patch](tarball://root/attachments/some-uuid/ticket3097/trac_3097.patch) by @garyfurnish created at 2008-05-04 11:55:06



---

archive/issue_comments_021378.json:
```json
{
    "body": "Attachment [trac_3097_scripts.patch](tarball://root/attachments/some-uuid/ticket3097/trac_3097_scripts.patch) by @garyfurnish created at 2008-05-04 11:55:40",
    "created_at": "2008-05-04T11:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3097#issuecomment-21378",
    "user": "@garyfurnish"
}
```

Attachment [trac_3097_scripts.patch](tarball://root/attachments/some-uuid/ticket3097/trac_3097_scripts.patch) by @garyfurnish created at 2008-05-04 11:55:40



---

archive/issue_comments_021379.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-04T11:55:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3097#issuecomment-21379",
    "user": "@garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021380.json:
```json
{
    "body": "The patches will not work as is:\n\n* this patchset, especially the bit to setup.py will break slowbuild\n* the scripts repo will be broken once you -sdist\n* what happens on clone\n\nThis is as-is not going into 3.0.1 :(.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-04T13:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3097#issuecomment-21380",
    "user": "mabshoff"
}
```

The patches will not work as is:

* this patchset, especially the bit to setup.py will break slowbuild
* the scripts repo will be broken once you -sdist
* what happens on clone

This is as-is not going into 3.0.1 :(.

Cheers,

Michael



---

archive/issue_comments_021381.json:
```json
{
    "body": "1) The patchset should not break slowbuild (infact the change to slowbuild should fix it for the scripts repo).\n2) I don't understand why -sdist is going to break the scripts repo.  I added the files to the hg scripts repo, why will sdist break this?\n3) the dsage/web directory is a link to devel/sage/...... so it will keep pointing at the right target on clone.",
    "created_at": "2008-05-04T14:50:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3097#issuecomment-21381",
    "user": "@garyfurnish"
}
```

1) The patchset should not break slowbuild (infact the change to slowbuild should fix it for the scripts repo).
2) I don't understand why -sdist is going to break the scripts repo.  I added the files to the hg scripts repo, why will sdist break this?
3) the dsage/web directory is a link to devel/sage/...... so it will keep pointing at the right target on clone.



---

archive/issue_comments_021382.json:
```json
{
    "body": "I haven't been able to test this set of patches yet but from speaking with gfurnish on IRC it seems to be the right way to go to resolve the pbuild issue. I'll try these patches out and provide feedback then.",
    "created_at": "2008-05-07T00:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3097#issuecomment-21382",
    "user": "@yqiang"
}
```

I haven't been able to test this set of patches yet but from speaking with gfurnish on IRC it seems to be the right way to go to resolve the pbuild issue. I'll try these patches out and provide feedback then.



---

archive/issue_comments_021383.json:
```json
{
    "body": "Attachment [trac_3097-hgignore.patch](tarball://root/attachments/some-uuid/ticket3097/trac_3097-hgignore.patch) by mabshoff created at 2008-05-23 02:37:23",
    "created_at": "2008-05-23T02:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3097#issuecomment-21383",
    "user": "mabshoff"
}
```

Attachment [trac_3097-hgignore.patch](tarball://root/attachments/some-uuid/ticket3097/trac_3097-hgignore.patch) by mabshoff created at 2008-05-23 02:37:23



---

archive/issue_comments_021384.json:
```json
{
    "body": "Attachment [trac_3097_extcode.patch](tarball://root/attachments/some-uuid/ticket3097/trac_3097_extcode.patch) by mabshoff created at 2008-05-23 02:48:46\n\nthis  is a slightly updated version of the original patch by Gary",
    "created_at": "2008-05-23T02:48:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3097#issuecomment-21384",
    "user": "mabshoff"
}
```

Attachment [trac_3097_extcode.patch](tarball://root/attachments/some-uuid/ticket3097/trac_3097_extcode.patch) by mabshoff created at 2008-05-23 02:48:46

this  is a slightly updated version of the original patch by Gary



---

archive/issue_comments_021385.json:
```json
{
    "body": "Attachment [trac_3097-sdist-fix-part2.patch](tarball://root/attachments/some-uuid/ticket3097/trac_3097-sdist-fix-part2.patch) by mabshoff created at 2008-05-23 05:38:03\n\noops - this ought to fix the issue",
    "created_at": "2008-05-23T05:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3097#issuecomment-21385",
    "user": "mabshoff"
}
```

Attachment [trac_3097-sdist-fix-part2.patch](tarball://root/attachments/some-uuid/ticket3097/trac_3097-sdist-fix-part2.patch) by mabshoff created at 2008-05-23 05:38:03

oops - this ought to fix the issue



---

archive/issue_comments_021386.json:
```json
{
    "body": "Ok, now the `-sdist` issue is resolved. I did an sdist followed by a full rebuild and a testall. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-23T06:23:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3097#issuecomment-21386",
    "user": "mabshoff"
}
```

Ok, now the `-sdist` issue is resolved. I did an sdist followed by a full rebuild and a testall. Positive review.

Cheers,

Michael



---

archive/issue_comments_021387.json:
```json
{
    "body": "Merged all six patches in Sage 3.0.2.rc0",
    "created_at": "2008-05-23T06:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3097#issuecomment-21387",
    "user": "mabshoff"
}
```

Merged all six patches in Sage 3.0.2.rc0



---

archive/issue_comments_021388.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-23T06:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3097#issuecomment-21388",
    "user": "mabshoff"
}
```

Resolution: fixed
