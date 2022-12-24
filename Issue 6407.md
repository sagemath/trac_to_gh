# Issue 6407: Multiplication-by-n method on elliptic curve formal groups should use the double-and-add algorithm

archive/issues_006407.json:
```json
{
    "body": "Assignee: hlaw\n\nKeywords: formal group elliptic curve\n\nCurrently `EllipticCurveFormalGroup.mult_by_n()` is implemented simply by applying the group law to itself *n* times (except when working over a field of characteristic zero, in which case a fast algorithm is used).  This linear algorithm should be replaced with the logarithmic double-and-add algorithm (i.e. the additive version of the standard square-and-multiply algorithm).\n\nIssue created by migration from https://trac.sagemath.org/ticket/6407\n\n",
    "created_at": "2009-06-25T14:39:58Z",
    "labels": [
        "performance",
        "minor",
        "enhancement"
    ],
    "title": "Multiplication-by-n method on elliptic curve formal groups should use the double-and-add algorithm",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6407",
    "user": "hlaw"
}
```
Assignee: hlaw

Keywords: formal group elliptic curve

Currently `EllipticCurveFormalGroup.mult_by_n()` is implemented simply by applying the group law to itself *n* times (except when working over a field of characteristic zero, in which case a fast algorithm is used).  This linear algorithm should be replaced with the logarithmic double-and-add algorithm (i.e. the additive version of the standard square-and-multiply algorithm).

Issue created by migration from https://trac.sagemath.org/ticket/6407





---

archive/issue_comments_051447.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-25T14:41:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6407#issuecomment-51447",
    "user": "hlaw"
}
```

Changing status from new to assigned.



---

archive/issue_comments_051448.json:
```json
{
    "body": "Attachment [trac_6407_added_double-and-add_algo_to_EllipticCurveFormalGroup.patch](tarball://root/attachments/some-uuid/ticket6407/trac_6407_added_double-and-add_algo_to_EllipticCurveFormalGroup.patch) by hlaw created at 2009-07-12 19:53:06",
    "created_at": "2009-07-12T19:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6407#issuecomment-51448",
    "user": "hlaw"
}
```

Attachment [trac_6407_added_double-and-add_algo_to_EllipticCurveFormalGroup.patch](tarball://root/attachments/some-uuid/ticket6407/trac_6407_added_double-and-add_algo_to_EllipticCurveFormalGroup.patch) by hlaw created at 2009-07-12 19:53:06



---

archive/issue_comments_051449.json:
```json
{
    "body": "Attachment [6407_part2.patch](tarball://root/attachments/some-uuid/ticket6407/6407_part2.patch) by boothby created at 2009-07-17 23:22:53",
    "created_at": "2009-07-17T23:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6407#issuecomment-51449",
    "user": "boothby"
}
```

Attachment [6407_part2.patch](tarball://root/attachments/some-uuid/ticket6407/6407_part2.patch) by boothby created at 2009-07-17 23:22:53



---

archive/issue_comments_051450.json:
```json
{
    "body": "hlaw's implementation of the double-and-add algorithm resulted in a wasted doubling at the end -- potentially expensive.  My part2 patch is a slight improvement.",
    "created_at": "2009-07-17T23:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6407#issuecomment-51450",
    "user": "boothby"
}
```

hlaw's implementation of the double-and-add algorithm resulted in a wasted doubling at the end -- potentially expensive.  My part2 patch is a slight improvement.



---

archive/issue_comments_051451.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-07-21T19:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6407#issuecomment-51451",
    "user": "rlm"
}
```

Looks good to me.



---

archive/issue_comments_051452.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T08:18:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6407",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6407#issuecomment-51452",
    "user": "mvngu"
}
```

Resolution: fixed
