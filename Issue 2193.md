# Issue 2193: doctest framework should check for keywords only in comments

archive/issues_002193.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @ncalexan\n\nChecking for keywords on the whole line causes unexpected behavior while testing. The test framework should only check for the keywords in the comments.\n\nThis thread is also relevant:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/c63998dbd4ee6a27/fc6643a2a871bf34#fc6643a2a871bf34\n\nIssue created by migration from https://trac.sagemath.org/ticket/2193\n\n",
    "created_at": "2008-02-17T14:19:35Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "doctest framework should check for keywords only in comments",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2193",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

CC:  @ncalexan

Checking for keywords on the whole line causes unexpected behavior while testing. The test framework should only check for the keywords in the comments.

This thread is also relevant:

http://groups.google.com/group/sage-devel/browse_thread/thread/c63998dbd4ee6a27/fc6643a2a871bf34#fc6643a2a871bf34

Issue created by migration from https://trac.sagemath.org/ticket/2193





---

archive/issue_comments_014365.json:
```json
{
    "body": "make sage-doctest search for keywords in comments",
    "created_at": "2008-02-17T16:30:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2193#issuecomment-14365",
    "user": "https://github.com/burcin"
}
```

make sage-doctest search for keywords in comments



---

archive/issue_comments_014366.json:
```json
{
    "body": "Attachment [2193-doctest_keywords_in_comments.patch](tarball://root/attachments/some-uuid/ticket2193/2193-doctest_keywords_in_comments.patch) by @burcin created at 2008-02-17 16:31:09\n\nadd random keyword to tests in doc-main",
    "created_at": "2008-02-17T16:31:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2193#issuecomment-14366",
    "user": "https://github.com/burcin"
}
```

Attachment [2193-doctest_keywords_in_comments.patch](tarball://root/attachments/some-uuid/ticket2193/2193-doctest_keywords_in_comments.patch) by @burcin created at 2008-02-17 16:31:09

add random keyword to tests in doc-main



---

archive/issue_comments_014367.json:
```json
{
    "body": "Attachment [2193-doc_add_random.patch](tarball://root/attachments/some-uuid/ticket2193/2193-doc_add_random.patch) by @burcin created at 2008-02-17 16:31:42\n\nadd random keyword to comments",
    "created_at": "2008-02-17T16:31:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2193#issuecomment-14367",
    "user": "https://github.com/burcin"
}
```

Attachment [2193-doc_add_random.patch](tarball://root/attachments/some-uuid/ticket2193/2193-doc_add_random.patch) by @burcin created at 2008-02-17 16:31:42

add random keyword to comments



---

archive/issue_comments_014368.json:
```json
{
    "body": "Attachment [2193-add_random_keyword.patch](tarball://root/attachments/some-uuid/ticket2193/2193-add_random_keyword.patch) by @burcin created at 2008-02-17 16:37:41\n\nattachment:2193-doctest_keywords_in_comments.patch changes the `sage-doctest` script to search for keywords only in comments. It also changes the way random keyword is handled to match wstein's suggestions in the sage-devel thread mentioned above.\n\nattachment:2193-doc_add_random.patch and attachment:2193-add_random_keyword.patch add the random keyword to comments for tests which relied on the old behavior in the documentation, and the sage library respectively.",
    "created_at": "2008-02-17T16:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2193#issuecomment-14368",
    "user": "https://github.com/burcin"
}
```

Attachment [2193-add_random_keyword.patch](tarball://root/attachments/some-uuid/ticket2193/2193-add_random_keyword.patch) by @burcin created at 2008-02-17 16:37:41

attachment:2193-doctest_keywords_in_comments.patch changes the `sage-doctest` script to search for keywords only in comments. It also changes the way random keyword is handled to match wstein's suggestions in the sage-devel thread mentioned above.

attachment:2193-doc_add_random.patch and attachment:2193-add_random_keyword.patch add the random keyword to comments for tests which relied on the old behavior in the documentation, and the sage library respectively.



---

archive/issue_comments_014369.json:
```json
{
    "body": "Looks fine to me.  I say apply.",
    "created_at": "2008-02-18T19:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2193#issuecomment-14369",
    "user": "https://github.com/ncalexan"
}
```

Looks fine to me.  I say apply.



---

archive/issue_comments_014370.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-18T19:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2193#issuecomment-14370",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002359.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-18T19:37:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2193",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2193#event-2359"
}
```



---

archive/issue_comments_014371.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-18T19:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2193#issuecomment-14371",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha1
