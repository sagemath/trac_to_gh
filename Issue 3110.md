# Issue 3110: [with patch, needs review] rare pbuild dependency bug

archive/issues_003110.json:
```json
{
    "body": "Assignee: gfurnish\n\nKeywords: pbuild\n\nThis patch corrects a bug in pbuild dependency checking that does not correctly register the pxd file dependency for a pyx file if no other files cimport the file (rare).\n\nIssue created by migration from https://trac.sagemath.org/ticket/3110\n\n",
    "created_at": "2008-05-06T04:33:11Z",
    "labels": [
        "pbuild",
        "blocker",
        "bug"
    ],
    "title": "[with patch, needs review] rare pbuild dependency bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3110",
    "user": "gfurnish"
}
```
Assignee: gfurnish

Keywords: pbuild

This patch corrects a bug in pbuild dependency checking that does not correctly register the pxd file dependency for a pyx file if no other files cimport the file (rare).

Issue created by migration from https://trac.sagemath.org/ticket/3110





---

archive/issue_comments_021496.json:
```json
{
    "body": "Attachment [trac_extcode_3110.patch](tarball://root/attachments/some-uuid/ticket3110/trac_extcode_3110.patch) by gfurnish created at 2008-05-06 04:34:54",
    "created_at": "2008-05-06T04:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3110#issuecomment-21496",
    "user": "gfurnish"
}
```

Attachment [trac_extcode_3110.patch](tarball://root/attachments/some-uuid/ticket3110/trac_extcode_3110.patch) by gfurnish created at 2008-05-06 04:34:54



---

archive/issue_comments_021497.json:
```json
{
    "body": "This patch also modifies -ba to clean the build directory.",
    "created_at": "2008-05-06T04:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3110#issuecomment-21497",
    "user": "gfurnish"
}
```

This patch also modifies -ba to clean the build directory.



---

archive/issue_comments_021498.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-06T04:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3110#issuecomment-21498",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021499.json:
```json
{
    "body": "Path looks good to me. One thing: This patch also contains unrelated changes [besides the clean option] which are uncontroversial. I would suggest that you also add some release number that you increment on changes so we do not end up having to poke around for the exact version of pbuild when we need to debug some problem remotely.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-06T20:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3110#issuecomment-21499",
    "user": "mabshoff"
}
```

Path looks good to me. One thing: This patch also contains unrelated changes [besides the clean option] which are uncontroversial. I would suggest that you also add some release number that you increment on changes so we do not end up having to poke around for the exact version of pbuild when we need to debug some problem remotely.

Cheers,

Michael



---

archive/issue_comments_021500.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-06T20:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3110#issuecomment-21500",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_comments_021501.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-06T20:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3110",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3110#issuecomment-21501",
    "user": "mabshoff"
}
```

Resolution: fixed
