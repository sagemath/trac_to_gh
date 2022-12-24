# Issue 3046: version option returning clone branch name

archive/issues_003046.json:
```json
{
    "body": "Assignee: was\n\nThe attached patch adds to version an option which returns the version and the branch clone name.\nNew behavior:\nsage: version()\nreturns exactly the same thing it did before no change.\nsage: version(True) # or replace \"True\" by anything except \"0\" or \"False\"\nreturns \n(Version, Branch name)\nFor example,\n\n```\nsage: version(1)\n\n('SAGE Version 3.0, Release Date: 2008-04-22',\n 'Mercurial clone branch: version')\n```\n\nin a Mercurial clone branch created using \"sage -clone version\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/3046\n\n",
    "created_at": "2008-04-27T20:19:58Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "version option returning clone branch name",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3046",
    "user": "wdj"
}
```
Assignee: was

The attached patch adds to version an option which returns the version and the branch clone name.
New behavior:
sage: version()
returns exactly the same thing it did before no change.
sage: version(True) # or replace "True" by anything except "0" or "False"
returns 
(Version, Branch name)
For example,

```
sage: version(1)

('SAGE Version 3.0, Release Date: 2008-04-22',
 'Mercurial clone branch: version')
```

in a Mercurial clone branch created using "sage -clone version".

Issue created by migration from https://trac.sagemath.org/ticket/3046





---

archive/issue_comments_020973.json:
```json
{
    "body": "Attachment [9607.patch](tarball://root/attachments/some-uuid/ticket3046/9607.patch) by wdj created at 2008-04-27 20:20:13",
    "created_at": "2008-04-27T20:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3046#issuecomment-20973",
    "user": "wdj"
}
```

Attachment [9607.patch](tarball://root/attachments/some-uuid/ticket3046/9607.patch) by wdj created at 2008-04-27 20:20:13



---

archive/issue_comments_020974.json:
```json
{
    "body": "Patch looks good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-11T11:08:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3046#issuecomment-20974",
    "user": "mabshoff"
}
```

Patch looks good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_020975.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T11:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3046#issuecomment-20975",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020976.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-11T11:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3046#issuecomment-20976",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_comments_020977.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-05-19T06:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3046#issuecomment-20977",
    "user": "was"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_020978.json:
```json
{
    "body": "Very negative review because the patch adds this line:\n\n```\n\tr\"\"\"nodoctest \n```\n",
    "created_at": "2008-05-19T06:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3046#issuecomment-20978",
    "user": "was"
}
```

Very negative review because the patch adds this line:

```
	r"""nodoctest 
```




---

archive/issue_comments_020979.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-05-19T06:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3046#issuecomment-20979",
    "user": "was"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_020980.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-19T06:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3046#issuecomment-20980",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020981.json:
```json
{
    "body": "I fixed this in the repo by removing \"nodoctest\". Doctests do pass now.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-19T06:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3046#issuecomment-20981",
    "user": "mabshoff"
}
```

I fixed this in the repo by removing "nodoctest". Doctests do pass now.

Cheers,

Michael



---

archive/issue_comments_020982.json:
```json
{
    "body": "this patch removes 'nodoctest' and make the doctests actually pass - my bad for the sloppy review",
    "created_at": "2008-05-19T06:32:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3046#issuecomment-20982",
    "user": "mabshoff"
}
```

this patch removes 'nodoctest' and make the doctests actually pass - my bad for the sloppy review
