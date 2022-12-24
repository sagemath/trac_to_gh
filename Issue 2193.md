# Issue 2193: doctest framework should check for keywords only in comments

archive/issues_002193.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  ncalexan\n\nChecking for keywords on the whole line causes unexpected behavior while testing. The test framework should only check for the keywords in the comments.\n\nThis thread is also relevant:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/c63998dbd4ee6a27/fc6643a2a871bf34#fc6643a2a871bf34\n\nIssue created by migration from https://trac.sagemath.org/ticket/2193\n\n",
    "created_at": "2008-02-17T14:19:35Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "doctest framework should check for keywords only in comments",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2193",
    "user": "burcin"
}
```
Assignee: burcin

CC:  ncalexan

Checking for keywords on the whole line causes unexpected behavior while testing. The test framework should only check for the keywords in the comments.

This thread is also relevant:

http://groups.google.com/group/sage-devel/browse_thread/thread/c63998dbd4ee6a27/fc6643a2a871bf34#fc6643a2a871bf34

Issue created by migration from https://trac.sagemath.org/ticket/2193





---

archive/issue_comments_014396.json:
```json
{
    "body": "make sage-doctest search for keywords in comments",
    "created_at": "2008-02-17T16:30:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2193#issuecomment-14396",
    "user": "burcin"
}
```

make sage-doctest search for keywords in comments



---

archive/issue_comments_014397.json:
```json
{
    "body": "Attachment [2193-doctest_keywords_in_comments.patch](tarball://root/attachments/some-uuid/ticket2193/2193-doctest_keywords_in_comments.patch) by burcin created at 2008-02-17 16:31:09\n\nadd random keyword to tests in doc-main",
    "created_at": "2008-02-17T16:31:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2193#issuecomment-14397",
    "user": "burcin"
}
```

Attachment [2193-doctest_keywords_in_comments.patch](tarball://root/attachments/some-uuid/ticket2193/2193-doctest_keywords_in_comments.patch) by burcin created at 2008-02-17 16:31:09

add random keyword to tests in doc-main



---

archive/issue_comments_014398.json:
```json
{
    "body": "Attachment [2193-doc_add_random.patch](tarball://root/attachments/some-uuid/ticket2193/2193-doc_add_random.patch) by burcin created at 2008-02-17 16:31:42\n\nadd random keyword to comments",
    "created_at": "2008-02-17T16:31:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2193#issuecomment-14398",
    "user": "burcin"
}
```

Attachment [2193-doc_add_random.patch](tarball://root/attachments/some-uuid/ticket2193/2193-doc_add_random.patch) by burcin created at 2008-02-17 16:31:42

add random keyword to comments



---

archive/issue_comments_014399.json:
```json
{
    "body": "Attachment [2193-add_random_keyword.patch](tarball://root/attachments/some-uuid/ticket2193/2193-add_random_keyword.patch) by burcin created at 2008-02-17 16:37:41\n\nattachment:2193-doctest_keywords_in_comments.patch changes the `sage-doctest` script to search for keywords only in comments. It also changes the way random keyword is handled to match wstein's suggestions in the sage-devel thread mentioned above.\n\nattachment:2193-doc_add_random.patch and attachment:2193-add_random_keyword.patch add the random keyword to comments for tests which relied on the old behavior in the documentation, and the sage library respectively.",
    "created_at": "2008-02-17T16:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2193#issuecomment-14399",
    "user": "burcin"
}
```

Attachment [2193-add_random_keyword.patch](tarball://root/attachments/some-uuid/ticket2193/2193-add_random_keyword.patch) by burcin created at 2008-02-17 16:37:41

attachment:2193-doctest_keywords_in_comments.patch changes the `sage-doctest` script to search for keywords only in comments. It also changes the way random keyword is handled to match wstein's suggestions in the sage-devel thread mentioned above.

attachment:2193-doc_add_random.patch and attachment:2193-add_random_keyword.patch add the random keyword to comments for tests which relied on the old behavior in the documentation, and the sage library respectively.



---

archive/issue_comments_014400.json:
```json
{
    "body": "Looks fine to me.  I say apply.",
    "created_at": "2008-02-18T19:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2193#issuecomment-14400",
    "user": "ncalexan"
}
```

Looks fine to me.  I say apply.



---

archive/issue_comments_014401.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-18T19:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2193#issuecomment-14401",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014402.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-18T19:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2193#issuecomment-14402",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha1
