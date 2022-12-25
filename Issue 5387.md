# Issue 5387: [with patch, needs review] a few changes to the installation guide

archive/issues_005387.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nAt least one thing in the installation guide (a table) disappeared in the ReST conversion, and I've changed a few other things: how to build the documentation, a broken link, etc.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5387\n\n",
    "created_at": "2009-02-26T18:29:41Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch, needs review] a few changes to the installation guide",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5387",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

At least one thing in the installation guide (a table) disappeared in the ReST conversion, and I've changed a few other things: how to build the documentation, a broken link, etc.


Issue created by migration from https://trac.sagemath.org/ticket/5387





---

archive/issue_comments_041406.json:
```json
{
    "body": "Attachment [installation.patch](tarball://root/attachments/some-uuid/ticket5387/installation.patch) by @jhpalmieri created at 2009-02-26 18:29:49",
    "created_at": "2009-02-26T18:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41406",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [installation.patch](tarball://root/attachments/some-uuid/ticket5387/installation.patch) by @jhpalmieri created at 2009-02-26 18:29:49



---

archive/issue_comments_041407.json:
```json
{
    "body": "By the way, for the list of software, I just copied it from the old installation guide; I didn't check it for accuracy or omissions.",
    "created_at": "2009-02-26T18:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41407",
    "user": "https://github.com/jhpalmieri"
}
```

By the way, for the list of software, I just copied it from the old installation guide; I didn't check it for accuracy or omissions.



---

archive/issue_comments_041408.json:
```json
{
    "body": "Isn't the current list of software is on the wiki at\nhttp://wiki.sagemath.org/standard_packages_available_for_SAGE?\nThe list you have in the patch and that list from the wiki don't\nagree.",
    "created_at": "2009-02-26T21:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41408",
    "user": "https://github.com/wdjoyner"
}
```

Isn't the current list of software is on the wiki at
http://wiki.sagemath.org/standard_packages_available_for_SAGE?
The list you have in the patch and that list from the wiki don't
agree.



---

archive/issue_comments_041409.json:
```json
{
    "body": "I think the current list is actually in [http://sagemath.org/packages/standard/](http://sagemath.org/packages/standard/) or $SAGE_ROOT/spkg/installed, and the list there doesn't match the one in the installation guide or the one on the wiki.\n\nAnyway, here's a patch (apply on top of the old one) with a new list.",
    "created_at": "2009-02-26T22:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41409",
    "user": "https://github.com/jhpalmieri"
}
```

I think the current list is actually in [http://sagemath.org/packages/standard/](http://sagemath.org/packages/standard/) or $SAGE_ROOT/spkg/installed, and the list there doesn't match the one in the installation guide or the one on the wiki.

Anyway, here's a patch (apply on top of the old one) with a new list.



---

archive/issue_comments_041410.json:
```json
{
    "body": "apply on top of other patch",
    "created_at": "2009-02-26T22:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41410",
    "user": "https://github.com/jhpalmieri"
}
```

apply on top of other patch



---

archive/issue_comments_041411.json:
```json
{
    "body": "Attachment [installation-part2.patch](tarball://root/attachments/some-uuid/ticket5387/installation-part2.patch) by @wdjoyner created at 2009-02-26 22:40:07\n\nApplies cleanly to sage-3.4.alpha0 using hg_sage.apply (*not* hg_doc). Compiles cleanly and without error.\n\nExcellent job - thanks for making this patch!",
    "created_at": "2009-02-26T22:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41411",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [installation-part2.patch](tarball://root/attachments/some-uuid/ticket5387/installation-part2.patch) by @wdjoyner created at 2009-02-26 22:40:07

Applies cleanly to sage-3.4.alpha0 using hg_sage.apply (*not* hg_doc). Compiles cleanly and without error.

Excellent job - thanks for making this patch!



---

archive/issue_events_005642.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-28T16:27:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5387#event-5642"
}
```



---

archive/issue_comments_041412.json:
```json
{
    "body": "Merged both patches in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T16:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41412",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_comments_041413.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-28T16:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41413",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041414.json:
```json
{
    "body": "reviewer fixes for above patches",
    "created_at": "2009-03-01T04:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41414",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

reviewer fixes for above patches



---

archive/issue_comments_041415.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-03-01T04:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41415",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from closed to reopened.



---

archive/issue_events_005643.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-03-01T04:37:40Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5387#event-5643"
}
```



---

archive/issue_comments_041416.json:
```json
{
    "body": "Changing keywords from \"\" to \"installation guide\".",
    "created_at": "2009-03-01T04:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41416",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing keywords from "" to "installation guide".



---

archive/issue_comments_041417.json:
```json
{
    "body": "Attachment [trac_5387_reviewer-fixes.patch](tarball://root/attachments/some-uuid/ticket5387/trac_5387_reviewer-fixes.patch) by mvngu created at 2009-03-01 04:37:40\n\nThe patch **trac_5387_reviewer-fixes.patch** fixes some typos found in the patches by jhpalmieri.",
    "created_at": "2009-03-01T04:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41417",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_5387_reviewer-fixes.patch](tarball://root/attachments/some-uuid/ticket5387/trac_5387_reviewer-fixes.patch) by mvngu created at 2009-03-01 04:37:40

The patch **trac_5387_reviewer-fixes.patch** fixes some typos found in the patches by jhpalmieri.



---

archive/issue_comments_041418.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-03-01T04:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41418",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_041419.json:
```json
{
    "body": "Do not reopen ticket that I have closed. Open a followup ticket - this is otherwise a giant mess.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T04:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41419",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Do not reopen ticket that I have closed. Open a followup ticket - this is otherwise a giant mess.

Cheers,

Michael



---

archive/issue_comments_041420.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-01T04:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41420",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005644.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-03-01T04:41:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5387#event-5644"
}
```



---

archive/issue_comments_041421.json:
```json
{
    "body": "To keep things simple: Merged trac_5387_reviewer-fixes.patch in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T04:45:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41421",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

To keep things simple: Merged trac_5387_reviewer-fixes.patch in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_comments_041422.json:
```json
{
    "body": "Replying to [comment:8 mabshoff]:\n> To keep things simple: Merged trac_5387_reviewer-fixes.patch in Sage 3.4.rc0.\nSorry about this, Michael. I'll keep your advice in mind.",
    "created_at": "2009-03-01T04:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41422",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:8 mabshoff]:
> To keep things simple: Merged trac_5387_reviewer-fixes.patch in Sage 3.4.rc0.
Sorry about this, Michael. I'll keep your advice in mind.
