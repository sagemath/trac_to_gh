# Issue 3123: blacklist "gcc version 4.1.0 (SUSE Linux)"

archive/issues_003123.json:
```json
{
    "body": "Assignee: mabshoff\n\ngcc version 4.1.0 (SUSE Linux) from OpenSuSE 10.1 is know broken and will fail to file Sage with\n\n```\nsage/modules/real_double_vector.c: In function \u2018__pyx_pf_4sage_7modules_18real_double_vector_28RealDoubleVectorSpaceElement_\n__init__\u2019:\nsage/modules/real_double_vector.c:2012: internal compiler error: in merge_alias_info, at tree-ssa-copy.c:235\nPlease submit a full bug report,\nwith preprocessed source if appropriate.\nSee <URL:http://www.suse.de/feedback> for instructions.\nerror: command 'gcc' failed with exit status 1\n```\n\nBlacklist it.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3123\n\n",
    "created_at": "2008-05-07T14:27:31Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "blacklist \"gcc version 4.1.0 (SUSE Linux)\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3123",
    "user": "mabshoff"
}
```
Assignee: mabshoff

gcc version 4.1.0 (SUSE Linux) from OpenSuSE 10.1 is know broken and will fail to file Sage with

```
sage/modules/real_double_vector.c: In function ‘__pyx_pf_4sage_7modules_18real_double_vector_28RealDoubleVectorSpaceElement_
__init__’:
sage/modules/real_double_vector.c:2012: internal compiler error: in merge_alias_info, at tree-ssa-copy.c:235
Please submit a full bug report,
with preprocessed source if appropriate.
See <URL:http://www.suse.de/feedback> for instructions.
error: command 'gcc' failed with exit status 1
```

Blacklist it.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3123





---

archive/issue_comments_021641.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-07T14:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3123#issuecomment-21641",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021642.json:
```json
{
    "body": "Changing priority from blocker to major.",
    "created_at": "2009-06-15T23:19:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3123#issuecomment-21642",
    "user": "was"
}
```

Changing priority from blocker to major.



---

archive/issue_comments_021643.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-05-19T13:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3123#issuecomment-21643",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_021644.json:
```json
{
    "body": "Fixed by the GCC spkg.",
    "created_at": "2013-05-19T13:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3123#issuecomment-21644",
    "user": "jdemeyer"
}
```

Fixed by the GCC spkg.



---

archive/issue_comments_021645.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-19T13:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3123#issuecomment-21645",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_021646.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-05-21T07:23:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3123",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3123#issuecomment-21646",
    "user": "jdemeyer"
}
```

Resolution: invalid
