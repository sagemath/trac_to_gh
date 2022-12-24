# Issue 3646: Implement paren matching

archive/issues_003646.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein tclemans yiqiang\n\nPeople have been complaining about a lack of paren matching in the notebook.  Do something.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3646\n\n",
    "created_at": "2008-07-11T22:15:08Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "Implement paren matching",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3646",
    "user": "boothby"
}
```
Assignee: boothby

CC:  @williamstein tclemans yiqiang

People have been complaining about a lack of paren matching in the notebook.  Do something.

Issue created by migration from https://trac.sagemath.org/ticket/3646





---

archive/issue_comments_025775.json:
```json
{
    "body": "On my intel mac: works for me in Safari, and works in Firefox but noisily: it beeps whenever I hit ctrl-0 (whether it matches a parenthesis or not).",
    "created_at": "2008-07-18T20:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25775",
    "user": "@jhpalmieri"
}
```

On my intel mac: works for me in Safari, and works in Firefox but noisily: it beeps whenever I hit ctrl-0 (whether it matches a parenthesis or not).



---

archive/issue_comments_025776.json:
```json
{
    "body": "Attachment [3646-paren-matching-all.patch](tarball://root/attachments/some-uuid/ticket3646/3646-paren-matching-all.patch) by boothby created at 2008-07-29 17:22:55\n\nI just discovered quilt!  4 patches all rolled into one.",
    "created_at": "2008-07-29T17:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25776",
    "user": "boothby"
}
```

Attachment [3646-paren-matching-all.patch](tarball://root/attachments/some-uuid/ticket3646/3646-paren-matching-all.patch) by boothby created at 2008-07-29 17:22:55

I just discovered quilt!  4 patches all rolled into one.



---

archive/issue_comments_025777.json:
```json
{
    "body": "Oh, and this patch addresses jhpalmieri's issue.",
    "created_at": "2008-07-29T17:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25777",
    "user": "boothby"
}
```

Oh, and this patch addresses jhpalmieri's issue.



---

archive/issue_comments_025778.json:
```json
{
    "body": "REVIEW:\n\n* Looks very good but does *not* address jhpalmieri's issue successfully.  I can replicate the bing, which is OK, but pressing ctrl-] does not get recognized at all.  I'm using a macbookpro.",
    "created_at": "2008-07-29T17:33:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25778",
    "user": "@williamstein"
}
```

REVIEW:

* Looks very good but does *not* address jhpalmieri's issue successfully.  I can replicate the bing, which is OK, but pressing ctrl-] does not get recognized at all.  I'm using a macbookpro.



---

archive/issue_comments_025779.json:
```json
{
    "body": "Attachment [3646-paren-matching-all.2.patch](tarball://root/attachments/some-uuid/ticket3646/3646-paren-matching-all.2.patch) by boothby created at 2009-06-16 20:22:56\n\nrebased against #6307",
    "created_at": "2009-06-16T20:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25779",
    "user": "boothby"
}
```

Attachment [3646-paren-matching-all.2.patch](tarball://root/attachments/some-uuid/ticket3646/3646-paren-matching-all.2.patch) by boothby created at 2009-06-16 20:22:56

rebased against #6307



---

archive/issue_comments_025780.json:
```json
{
    "body": "Attachment [3646-silent.patch](tarball://root/attachments/some-uuid/ticket3646/3646-silent.patch) by boothby created at 2009-06-16 20:23:16",
    "created_at": "2009-06-16T20:23:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25780",
    "user": "boothby"
}
```

Attachment [3646-silent.patch](tarball://root/attachments/some-uuid/ticket3646/3646-silent.patch) by boothby created at 2009-06-16 20:23:16



---

archive/issue_comments_025781.json:
```json
{
    "body": "Ok, this really solves jhpalmieri's issue.  This time, I tested it on a mac with firefox!  I removed the ctrl-] keycode.",
    "created_at": "2009-06-16T20:24:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25781",
    "user": "boothby"
}
```

Ok, this really solves jhpalmieri's issue.  This time, I tested it on a mac with firefox!  I removed the ctrl-] keycode.



---

archive/issue_comments_025782.json:
```json
{
    "body": "If I create a cell with\n\n```\n3+2)\n```\n\nput the cursor at the end and hit ctrl-0, the parenthesis gets replaced with \"undefined\".  Is this the intended behavior?  It doesn't seem ideal to me; maybe ctrl-0 should do nothing in this situation?\n\n(Otherwise, it works well for me.)",
    "created_at": "2009-06-20T00:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25782",
    "user": "@jhpalmieri"
}
```

If I create a cell with

```
3+2)
```

put the cursor at the end and hit ctrl-0, the parenthesis gets replaced with "undefined".  Is this the intended behavior?  It doesn't seem ideal to me; maybe ctrl-0 should do nothing in this situation?

(Otherwise, it works well for me.)



---

archive/issue_comments_025783.json:
```json
{
    "body": "replaces all previous",
    "created_at": "2009-09-22T05:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25783",
    "user": "boothby"
}
```

replaces all previous



---

archive/issue_comments_025784.json:
```json
{
    "body": "Attachment [3646-paren-matching.patch](tarball://root/attachments/some-uuid/ticket3646/3646-paren-matching.patch) by boothby created at 2009-09-22 05:15:25",
    "created_at": "2009-09-22T05:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25784",
    "user": "boothby"
}
```

Attachment [3646-paren-matching.patch](tarball://root/attachments/some-uuid/ticket3646/3646-paren-matching.patch) by boothby created at 2009-09-22 05:15:25



---

archive/issue_comments_025785.json:
```json
{
    "body": "This looks good to me.",
    "created_at": "2009-09-22T18:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25785",
    "user": "@jhpalmieri"
}
```

This looks good to me.



---

archive/issue_comments_025786.json:
```json
{
    "body": "Oops, sorry, I forgot: the patch doesn't apply cleanly for me against 4.1.2.alpha2.  I'm attaching a rebased patch, but all credit should still go to boothby.",
    "created_at": "2009-09-22T18:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25786",
    "user": "@jhpalmieri"
}
```

Oops, sorry, I forgot: the patch doesn't apply cleanly for me against 4.1.2.alpha2.  I'm attaching a rebased patch, but all credit should still go to boothby.



---

archive/issue_comments_025787.json:
```json
{
    "body": "replaces all previous patches",
    "created_at": "2009-09-22T18:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25787",
    "user": "@jhpalmieri"
}
```

replaces all previous patches



---

archive/issue_comments_025788.json:
```json
{
    "body": "Attachment [trac_3646-rebased.patch](tarball://root/attachments/some-uuid/ticket3646/trac_3646-rebased.patch) by mvngu created at 2009-09-24 07:24:45\n\nreplaces all previous patches + boothby's name as author",
    "created_at": "2009-09-24T07:24:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25788",
    "user": "mvngu"
}
```

Attachment [trac_3646-rebased.patch](tarball://root/attachments/some-uuid/ticket3646/trac_3646-rebased.patch) by mvngu created at 2009-09-24 07:24:45

replaces all previous patches + boothby's name as author



---

archive/issue_comments_025789.json:
```json
{
    "body": "Attachment [trac_3646-rebased-v2.patch](tarball://root/attachments/some-uuid/ticket3646/trac_3646-rebased-v2.patch) by mvngu created at 2009-09-24 07:26:43\n\nThe patch `trac_3646-rebased-v2.patch` is the same as `trac_3646-rebased.patch`. The only difference is that v2 has the author name set to Tom Boothby.",
    "created_at": "2009-09-24T07:26:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25789",
    "user": "mvngu"
}
```

Attachment [trac_3646-rebased-v2.patch](tarball://root/attachments/some-uuid/ticket3646/trac_3646-rebased-v2.patch) by mvngu created at 2009-09-24 07:26:43

The patch `trac_3646-rebased-v2.patch` is the same as `trac_3646-rebased.patch`. The only difference is that v2 has the author name set to Tom Boothby.



---

archive/issue_comments_025790.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-24T07:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25790",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_025791.json:
```json
{
    "body": "Merged `trac_3646-rebased-v2.patch`.",
    "created_at": "2009-09-24T07:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25791",
    "user": "mvngu"
}
```

Merged `trac_3646-rebased-v2.patch`.



---

archive/issue_comments_025792.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25792",
    "user": "mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.



---

archive/issue_comments_025793.json:
```json
{
    "body": "Rebase v. #7196.  Apply only this patch.",
    "created_at": "2009-10-15T18:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25793",
    "user": "@qed777"
}
```

Rebase v. #7196.  Apply only this patch.



---

archive/issue_comments_025794.json:
```json
{
    "body": "Attachment [trac_3646-sagenb_paren_match.patch](tarball://root/attachments/some-uuid/ticket3646/trac_3646-sagenb_paren_match.patch) by @qed777 created at 2009-10-15 18:50:41\n\n[attachment:trac_3646-sagenb_paren_match.patch Patch] rebased against SageNB's #7196.",
    "created_at": "2009-10-15T18:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25794",
    "user": "@qed777"
}
```

Attachment [trac_3646-sagenb_paren_match.patch](tarball://root/attachments/some-uuid/ticket3646/trac_3646-sagenb_paren_match.patch) by @qed777 created at 2009-10-15 18:50:41

[attachment:trac_3646-sagenb_paren_match.patch Patch] rebased against SageNB's #7196.



---

archive/issue_comments_025795.json:
```json
{
    "body": "Merged into sagenb (for the sage-4.2 release cycle).",
    "created_at": "2009-10-17T05:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3646",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3646#issuecomment-25795",
    "user": "@williamstein"
}
```

Merged into sagenb (for the sage-4.2 release cycle).
