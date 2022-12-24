# Issue 5387: [with patch, needs review] a few changes to the installation guide

archive/issues_005387.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nAt least one thing in the installation guide (a table) disappeared in the ReST conversion, and I've changed a few other things: how to build the documentation, a broken link, etc.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5387\n\n",
    "created_at": "2009-02-26T18:29:41Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch, needs review] a few changes to the installation guide",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5387",
    "user": "@jhpalmieri"
}
```
Assignee: @jhpalmieri

At least one thing in the installation guide (a table) disappeared in the ReST conversion, and I've changed a few other things: how to build the documentation, a broken link, etc.


Issue created by migration from https://trac.sagemath.org/ticket/5387





---

archive/issue_comments_041488.json:
```json
{
    "body": "Attachment [installation.patch](tarball://root/attachments/some-uuid/ticket5387/installation.patch) by @jhpalmieri created at 2009-02-26 18:29:49",
    "created_at": "2009-02-26T18:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41488",
    "user": "@jhpalmieri"
}
```

Attachment [installation.patch](tarball://root/attachments/some-uuid/ticket5387/installation.patch) by @jhpalmieri created at 2009-02-26 18:29:49



---

archive/issue_comments_041489.json:
```json
{
    "body": "By the way, for the list of software, I just copied it from the old installation guide; I didn't check it for accuracy or omissions.",
    "created_at": "2009-02-26T18:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41489",
    "user": "@jhpalmieri"
}
```

By the way, for the list of software, I just copied it from the old installation guide; I didn't check it for accuracy or omissions.



---

archive/issue_comments_041490.json:
```json
{
    "body": "Isn't the current list of software is on the wiki at\nhttp://wiki.sagemath.org/standard_packages_available_for_SAGE?\nThe list you have in the patch and that list from the wiki don't\nagree.",
    "created_at": "2009-02-26T21:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41490",
    "user": "@wdjoyner"
}
```

Isn't the current list of software is on the wiki at
http://wiki.sagemath.org/standard_packages_available_for_SAGE?
The list you have in the patch and that list from the wiki don't
agree.



---

archive/issue_comments_041491.json:
```json
{
    "body": "I think the current list is actually in [http://sagemath.org/packages/standard/](http://sagemath.org/packages/standard/) or $SAGE_ROOT/spkg/installed, and the list there doesn't match the one in the installation guide or the one on the wiki.\n\nAnyway, here's a patch (apply on top of the old one) with a new list.",
    "created_at": "2009-02-26T22:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41491",
    "user": "@jhpalmieri"
}
```

I think the current list is actually in [http://sagemath.org/packages/standard/](http://sagemath.org/packages/standard/) or $SAGE_ROOT/spkg/installed, and the list there doesn't match the one in the installation guide or the one on the wiki.

Anyway, here's a patch (apply on top of the old one) with a new list.



---

archive/issue_comments_041492.json:
```json
{
    "body": "apply on top of other patch",
    "created_at": "2009-02-26T22:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41492",
    "user": "@jhpalmieri"
}
```

apply on top of other patch



---

archive/issue_comments_041493.json:
```json
{
    "body": "Attachment [installation-part2.patch](tarball://root/attachments/some-uuid/ticket5387/installation-part2.patch) by @wdjoyner created at 2009-02-26 22:40:07\n\nApplies cleanly to sage-3.4.alpha0 using hg_sage.apply (*not* hg_doc). Compiles cleanly and without error.\n\nExcellent job - thanks for making this patch!",
    "created_at": "2009-02-26T22:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41493",
    "user": "@wdjoyner"
}
```

Attachment [installation-part2.patch](tarball://root/attachments/some-uuid/ticket5387/installation-part2.patch) by @wdjoyner created at 2009-02-26 22:40:07

Applies cleanly to sage-3.4.alpha0 using hg_sage.apply (*not* hg_doc). Compiles cleanly and without error.

Excellent job - thanks for making this patch!



---

archive/issue_comments_041494.json:
```json
{
    "body": "Merged both patches in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T16:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41494",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_comments_041495.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-28T16:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41495",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041496.json:
```json
{
    "body": "reviewer fixes for above patches",
    "created_at": "2009-03-01T04:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41496",
    "user": "mvngu"
}
```

reviewer fixes for above patches



---

archive/issue_comments_041497.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-03-01T04:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41497",
    "user": "mvngu"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_041498.json:
```json
{
    "body": "Changing keywords from \"\" to \"installation guide\".",
    "created_at": "2009-03-01T04:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41498",
    "user": "mvngu"
}
```

Changing keywords from "" to "installation guide".



---

archive/issue_comments_041499.json:
```json
{
    "body": "Attachment [trac_5387_reviewer-fixes.patch](tarball://root/attachments/some-uuid/ticket5387/trac_5387_reviewer-fixes.patch) by mvngu created at 2009-03-01 04:37:40\n\nThe patch **trac_5387_reviewer-fixes.patch** fixes some typos found in the patches by jhpalmieri.",
    "created_at": "2009-03-01T04:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41499",
    "user": "mvngu"
}
```

Attachment [trac_5387_reviewer-fixes.patch](tarball://root/attachments/some-uuid/ticket5387/trac_5387_reviewer-fixes.patch) by mvngu created at 2009-03-01 04:37:40

The patch **trac_5387_reviewer-fixes.patch** fixes some typos found in the patches by jhpalmieri.



---

archive/issue_comments_041500.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-03-01T04:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41500",
    "user": "mvngu"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_041501.json:
```json
{
    "body": "Do not reopen ticket that I have closed. Open a followup ticket - this is otherwise a giant mess.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T04:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41501",
    "user": "mabshoff"
}
```

Do not reopen ticket that I have closed. Open a followup ticket - this is otherwise a giant mess.

Cheers,

Michael



---

archive/issue_comments_041502.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-01T04:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41502",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041503.json:
```json
{
    "body": "To keep things simple: Merged trac_5387_reviewer-fixes.patch in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T04:45:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41503",
    "user": "mabshoff"
}
```

To keep things simple: Merged trac_5387_reviewer-fixes.patch in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_comments_041504.json:
```json
{
    "body": "Replying to [comment:8 mabshoff]:\n> To keep things simple: Merged trac_5387_reviewer-fixes.patch in Sage 3.4.rc0.\nSorry about this, Michael. I'll keep your advice in mind.",
    "created_at": "2009-03-01T04:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5387#issuecomment-41504",
    "user": "mvngu"
}
```

Replying to [comment:8 mabshoff]:
> To keep things simple: Merged trac_5387_reviewer-fixes.patch in Sage 3.4.rc0.
Sorry about this, Michael. I'll keep your advice in mind.
