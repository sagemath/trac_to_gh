# Issue 3526: notebook -- change favicon to the new one seen at the new sagemath.org web site

archive/issues_003526.json:
```json
{
    "body": "Assignee: boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3526\n\n",
    "created_at": "2008-06-28T09:01:55Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "notebook -- change favicon to the new one seen at the new sagemath.org web site",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3526",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: boothby



Issue created by migration from https://trac.sagemath.org/ticket/3526





---

archive/issue_comments_024822.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_wstein\".",
    "created_at": "2008-06-28T09:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3526#issuecomment-24822",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing keywords from "" to "editor_wstein".



---

archive/issue_comments_024823.json:
```json
{
    "body": "Changing assignee from boothby to TimothyClemans.",
    "created_at": "2008-06-28T09:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3526#issuecomment-24823",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing assignee from boothby to TimothyClemans.



---

archive/issue_comments_024824.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-28T09:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3526#issuecomment-24824",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024825.json:
```json
{
    "body": "Changing priority from major to trivial.",
    "created_at": "2008-06-28T09:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3526#issuecomment-24825",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing priority from major to trivial.



---

archive/issue_comments_024826.json:
```json
{
    "body": "This patch is basically empty since favicon.ico is binary and not in the patch:\n\n```\ncat trac_3526_extcode-3526.patch \n# HG changeset patch\n# User Timothy Clemans <timothy.clemans@gmail.com>\n# Date 1214643704 25200\n# Node ID c6d839efcf8a7730a04e74399930ffab23651a5f\n# Parent  c3d96fbf0f19bf8b2c0c1c5188943ba54829f947\n#3526\n\ndiff -r c3d96fbf0f19 -r c6d839efcf8a notebook/images/favicon.ico\nBinary file notebook/images/favicon.ico has changed\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T02:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3526#issuecomment-24826",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch is basically empty since favicon.ico is binary and not in the patch:

```
cat trac_3526_extcode-3526.patch 
# HG changeset patch
# User Timothy Clemans <timothy.clemans@gmail.com>
# Date 1214643704 25200
# Node ID c6d839efcf8a7730a04e74399930ffab23651a5f
# Parent  c3d96fbf0f19bf8b2c0c1c5188943ba54829f947
#3526

diff -r c3d96fbf0f19 -r c6d839efcf8a notebook/images/favicon.ico
Binary file notebook/images/favicon.ico has changed
```


Cheers,

Michael



---

archive/issue_comments_024827.json:
```json
{
    "body": "From http://developer.mozilla.org/en/docs/Mercurial_FAQ#How_can_I_diff_and_patch_files.3F:\n\n* If you are changing binary files or renaming files you may want to use git style patches with hg diff -g to retain that sort of information in the patch.\n* If you have a git style patch with renames and/or binary changes you can use hg import --no-commit to apply the patch to your tree or use hg qimport to import the patch to mq. \n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T02:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3526#issuecomment-24827",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

From http://developer.mozilla.org/en/docs/Mercurial_FAQ#How_can_I_diff_and_patch_files.3F:

* If you are changing binary files or renaming files you may want to use git style patches with hg diff -g to retain that sort of information in the patch.
* If you have a git style patch with renames and/or binary changes you can use hg import --no-commit to apply the patch to your tree or use hg qimport to import the patch to mq. 

Cheers,

Michael



---

archive/issue_comments_024828.json:
```json
{
    "body": "Attachment [favicon.ico](tarball://root/attachments/some-uuid/ticket3526/favicon.ico) by TimothyClemans created at 2008-07-06 02:30:34",
    "created_at": "2008-07-06T02:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3526#issuecomment-24828",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [favicon.ico](tarball://root/attachments/some-uuid/ticket3526/favicon.ico) by TimothyClemans created at 2008-07-06 02:30:34



---

archive/issue_comments_024829.json:
```json
{
    "body": "Attachment [extcode-3526.2.patch](tarball://root/attachments/some-uuid/ticket3526/extcode-3526.2.patch) by mabshoff created at 2008-07-06 02:38:30\n\nPatch looks good to me, positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T02:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3526#issuecomment-24829",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [extcode-3526.2.patch](tarball://root/attachments/some-uuid/ticket3526/extcode-3526.2.patch) by mabshoff created at 2008-07-06 02:38:30

Patch looks good to me, positive review.

Cheers,

Michael



---

archive/issue_comments_024830.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-06T02:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3526#issuecomment-24830",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003745.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-07-06T02:38:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3526",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3526#event-3745"
}
```



---

archive/issue_comments_024831.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-06T02:38:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3526",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3526#issuecomment-24831",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha2
