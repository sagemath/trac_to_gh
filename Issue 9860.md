# Issue 9860: Improving the Graph Theory table of contents

archive/issues_009860.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @rlmill mvngu\n\nThe table of contents of the Graph Theory module is a bit hard to parse at the moment [1]. The file graph.py is even entitled \"Graph Theory\" itself, which must have remained from before this file was split into three, and the depth of 2 does not really help.\n\nThis patch is a possible way to clean it and make it.... readable ! I don't expect this patch to be merged as it is, as you probably have a different view of how it should be.. `:-)`\n\nNathann\n\n[1] http://www.sagemath.org/doc/reference/graphs.html\n\nIssue created by migration from https://trac.sagemath.org/ticket/9861\n\n",
    "created_at": "2010-09-06T17:34:24Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Improving the Graph Theory table of contents",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9860",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: mvngu

CC:  @rlmill mvngu

The table of contents of the Graph Theory module is a bit hard to parse at the moment [1]. The file graph.py is even entitled "Graph Theory" itself, which must have remained from before this file was split into three, and the depth of 2 does not really help.

This patch is a possible way to clean it and make it.... readable ! I don't expect this patch to be merged as it is, as you probably have a different view of how it should be.. `:-)`

Nathann

[1] http://www.sagemath.org/doc/reference/graphs.html

Issue created by migration from https://trac.sagemath.org/ticket/9861





---

archive/issue_comments_097197.json:
```json
{
    "body": "Attachment [trac_9861.patch](tarball://root/attachments/some-uuid/ticket9861/trac_9861.patch) by @nathanncohen created at 2010-09-06 17:35:26",
    "created_at": "2010-09-06T17:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9860#issuecomment-97197",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9861.patch](tarball://root/attachments/some-uuid/ticket9861/trac_9861.patch) by @nathanncohen created at 2010-09-06 17:35:26



---

archive/issue_comments_097198.json:
```json
{
    "body": "Attachment [trac_9861-reviewer.patch](tarball://root/attachments/some-uuid/ticket9861/trac_9861-reviewer.patch) by mvngu created at 2010-09-07 09:19:29",
    "created_at": "2010-09-07T09:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9860#issuecomment-97198",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_9861-reviewer.patch](tarball://root/attachments/some-uuid/ticket9861/trac_9861-reviewer.patch) by mvngu created at 2010-09-07 09:19:29



---

archive/issue_comments_097199.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-07T09:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9860#issuecomment-97199",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097200.json:
```json
{
    "body": "I got these warnings after applying ncohen's patch to Sage 4.5.3.rc0:\n\n\n```\n/dev/shm/mvngu/sage-4.5.3/devel/sage/doc/en/reference/graphs.rst:36: (WARNING/2)\n Title underline too short.\n\nLibraries of algorithms\n--------------------\n/dev/shm/mvngu/sage-4.5.3/devel/sage/doc/en/reference/graphs.rst:36: (WARNING/2)\n Title underline too short.\n\nLibraries of algorithms\n--------------------\n```\n\n\nThese are fixed in my reviewer patch. The reviewer patch also adds some consistency to how module headings are named, and consistency on how to space headings in the index file graph.rst. Capitalized titles are more difficult to read than a title only whose first letter is capitalized. I have avoided capitalized titles. \n\n\n\nI like ncohen's re-organized table of content for graph theory. Now it's just a matter of someone checking my reviewer patch. If it gets a positive review, then the whole ticket is good to go.",
    "created_at": "2010-09-07T09:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9860#issuecomment-97200",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I got these warnings after applying ncohen's patch to Sage 4.5.3.rc0:


```
/dev/shm/mvngu/sage-4.5.3/devel/sage/doc/en/reference/graphs.rst:36: (WARNING/2)
 Title underline too short.

Libraries of algorithms
--------------------
/dev/shm/mvngu/sage-4.5.3/devel/sage/doc/en/reference/graphs.rst:36: (WARNING/2)
 Title underline too short.

Libraries of algorithms
--------------------
```


These are fixed in my reviewer patch. The reviewer patch also adds some consistency to how module headings are named, and consistency on how to space headings in the index file graph.rst. Capitalized titles are more difficult to read than a title only whose first letter is capitalized. I have avoided capitalized titles. 



I like ncohen's re-organized table of content for graph theory. Now it's just a matter of someone checking my reviewer patch. If it gets a positive review, then the whole ticket is good to go.



---

archive/issue_comments_097201.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-07T10:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9860#issuecomment-97201",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097202.json:
```json
{
    "body": "Great ! Thank you again for your help ! `:-)`\n\nNathann",
    "created_at": "2010-09-07T10:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9860#issuecomment-97202",
    "user": "https://github.com/nathanncohen"
}
```

Great ! Thank you again for your help ! `:-)`

Nathann



---

archive/issue_comments_097203.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T11:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9860",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9860#issuecomment-97203",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_009990.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T11:38:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9860",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9860#event-9990"
}
```
