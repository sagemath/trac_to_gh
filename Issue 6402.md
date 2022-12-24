# Issue 6402: Fix bugs + improve documentation for overconvergent modular forms

archive/issues_006402.json:
```json
{
    "body": "Assignee: craigcitro\n\nCC:  was\n\nThis patch fixes lots of bugs + adds a substantial amount of documentation and examples, based on my talk at Sage Days 16.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6402\n\n",
    "created_at": "2009-06-25T12:11:59Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Fix bugs + improve documentation for overconvergent modular forms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6402",
    "user": "davidloeffler"
}
```
Assignee: craigcitro

CC:  was

This patch fixes lots of bugs + adds a substantial amount of documentation and examples, based on my talk at Sage Days 16.

Issue created by migration from https://trac.sagemath.org/ticket/6402





---

archive/issue_comments_051417.json:
```json
{
    "body": "patch against 4.0.2",
    "created_at": "2009-06-25T12:13:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6402#issuecomment-51417",
    "user": "davidloeffler"
}
```

patch against 4.0.2



---

archive/issue_comments_051418.json:
```json
{
    "body": "Attachment [trac_6402-overconvergent_fixes.patch](tarball://root/attachments/some-uuid/ticket6402/trac_6402-overconvergent_fixes.patch) by davidloeffler created at 2009-06-25 12:15:35\n\nHere's a patch.",
    "created_at": "2009-06-25T12:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6402#issuecomment-51418",
    "user": "davidloeffler"
}
```

Attachment [trac_6402-overconvergent_fixes.patch](tarball://root/attachments/some-uuid/ticket6402/trac_6402-overconvergent_fixes.patch) by davidloeffler created at 2009-06-25 12:15:35

Here's a patch.



---

archive/issue_comments_051419.json:
```json
{
    "body": "Looks good, and the added documentation is really great.\n\nI'm attaching a tiny referee patch fixing a few typos, and if you are ok with it we can give this a positive review.\n\nThere is one small issue, which I leave up to you whether you want to fix it or not: in the method `valuation_plot`, you added an optional argument `rmax`, but the docstring says nothing about its role.",
    "created_at": "2009-08-19T09:44:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6402#issuecomment-51419",
    "user": "AlexGhitza"
}
```

Looks good, and the added documentation is really great.

I'm attaching a tiny referee patch fixing a few typos, and if you are ok with it we can give this a positive review.

There is one small issue, which I leave up to you whether you want to fix it or not: in the method `valuation_plot`, you added an optional argument `rmax`, but the docstring says nothing about its role.



---

archive/issue_comments_051420.json:
```json
{
    "body": "apply after the previous patch",
    "created_at": "2009-08-19T09:45:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6402#issuecomment-51420",
    "user": "AlexGhitza"
}
```

apply after the previous patch



---

archive/issue_comments_051421.json:
```json
{
    "body": "Attachment [trac_6402-referee.patch](tarball://root/attachments/some-uuid/ticket6402/trac_6402-referee.patch) by davidloeffler created at 2009-08-19 09:52:05\n\nFine by me.",
    "created_at": "2009-08-19T09:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6402#issuecomment-51421",
    "user": "davidloeffler"
}
```

Attachment [trac_6402-referee.patch](tarball://root/attachments/some-uuid/ticket6402/trac_6402-referee.patch) by davidloeffler created at 2009-08-19 09:52:05

Fine by me.



---

archive/issue_comments_051422.json:
```json
{
    "body": "reviewer patch: more typo fixes",
    "created_at": "2009-08-23T13:27:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6402#issuecomment-51422",
    "user": "mvngu"
}
```

reviewer patch: more typo fixes



---

archive/issue_comments_051423.json:
```json
{
    "body": "Attachment [trac_6402-typos.patch](tarball://root/attachments/some-uuid/ticket6402/trac_6402-typos.patch) by mvngu created at 2009-08-23 13:29:55\n\nThe reviewer patch `trac_6402-typos.patch` fixes some typos left over from the previous two patches. If that is OK, then the whole ticket can be merged.",
    "created_at": "2009-08-23T13:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6402#issuecomment-51423",
    "user": "mvngu"
}
```

Attachment [trac_6402-typos.patch](tarball://root/attachments/some-uuid/ticket6402/trac_6402-typos.patch) by mvngu created at 2009-08-23 13:29:55

The reviewer patch `trac_6402-typos.patch` fixes some typos left over from the previous two patches. If that is OK, then the whole ticket can be merged.



---

archive/issue_comments_051424.json:
```json
{
    "body": "I certainly have no problems with Minh's suggestions. Can I suggest we get this in soon, rather than fixing every conceivable micro-bug, since the initial patch fixes some rather major and embarassing bugs that render the whole module basically unusable?",
    "created_at": "2009-08-24T08:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6402#issuecomment-51424",
    "user": "davidloeffler"
}
```

I certainly have no problems with Minh's suggestions. Can I suggest we get this in soon, rather than fixing every conceivable micro-bug, since the initial patch fixes some rather major and embarassing bugs that render the whole module basically unusable?



---

archive/issue_comments_051425.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-24T12:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6402#issuecomment-51425",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_051426.json:
```json
{
    "body": "Merged all three patches in this order:\n\n1. `trac_6402-overconvergent_fixes.patch`\n2. `trac_6402-referee.patch`\n3. `trac_6402-typos.patch`",
    "created_at": "2009-08-24T12:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6402#issuecomment-51426",
    "user": "mvngu"
}
```

Merged all three patches in this order:

1. `trac_6402-overconvergent_fixes.patch`
2. `trac_6402-referee.patch`
3. `trac_6402-typos.patch`
