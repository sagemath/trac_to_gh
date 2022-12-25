# Issue 8253: search_src (etc.) bug

archive/issues_008253.json:
```json
{
    "body": "Assignee: tbd\n\nIn Sage 4.3.2:\n\n```\nsearch_src('is', 'prime', 'field', ignore_case=True)\nTraceback (most recent call last):\n...\nTypeError: search() takes at most 3 arguments (4 given)\n```\nThis is because of a bug in sage.misc.sagedoc: when calling re.search, flags like re.MULTILINE and re.IGNORECASE should be combined using bit-wise or, not by passing them as separate entries in a list.  The attached patch fixes this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8253\n\n",
    "created_at": "2010-02-12T22:22:10Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "search_src (etc.) bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8253",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: tbd

In Sage 4.3.2:

```
search_src('is', 'prime', 'field', ignore_case=True)
Traceback (most recent call last):
...
TypeError: search() takes at most 3 arguments (4 given)
```
This is because of a bug in sage.misc.sagedoc: when calling re.search, flags like re.MULTILINE and re.IGNORECASE should be combined using bit-wise or, not by passing them as separate entries in a list.  The attached patch fixes this.

Issue created by migration from https://trac.sagemath.org/ticket/8253





---

archive/issue_comments_072889.json:
```json
{
    "body": "Attachment [trac_8253-search.patch](tarball://root/attachments/some-uuid/ticket8253/trac_8253-search.patch) by @jhpalmieri created at 2010-02-12 22:22:52",
    "created_at": "2010-02-12T22:22:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8253#issuecomment-72889",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8253-search.patch](tarball://root/attachments/some-uuid/ticket8253/trac_8253-search.patch) by @jhpalmieri created at 2010-02-12 22:22:52



---

archive/issue_comments_072890.json:
```json
{
    "body": "I noticed another `*flags` nearby.  Should we make it `flags`?",
    "created_at": "2010-02-16T21:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8253#issuecomment-72890",
    "user": "https://github.com/qed777"
}
```

I noticed another `*flags` nearby.  Should we make it `flags`?



---

archive/issue_comments_072891.json:
```json
{
    "body": "Yes.  Here's a new patch, rebased against 4.3.3.alpha0.",
    "created_at": "2010-02-17T20:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8253#issuecomment-72891",
    "user": "https://github.com/jhpalmieri"
}
```

Yes.  Here's a new patch, rebased against 4.3.3.alpha0.



---

archive/issue_comments_072892.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-17T20:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8253#issuecomment-72892",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072893.json:
```json
{
    "body": "Attachment [trac_8253-search.v2.patch](tarball://root/attachments/some-uuid/ticket8253/trac_8253-search.v2.patch) by @jhpalmieri created at 2010-02-17 20:58:13",
    "created_at": "2010-02-17T20:58:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8253#issuecomment-72893",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8253-search.v2.patch](tarball://root/attachments/some-uuid/ticket8253/trac_8253-search.v2.patch) by @jhpalmieri created at 2010-02-17 20:58:13



---

archive/issue_comments_072894.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-18T02:00:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8253#issuecomment-72894",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072895.json:
```json
{
    "body": "Merged [trac_8253-search.v2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8253/trac_8253-search.v2.patch).",
    "created_at": "2010-02-18T22:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8253#issuecomment-72895",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_8253-search.v2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8253/trac_8253-search.v2.patch).



---

archive/issue_comments_072896.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-18T22:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8253",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8253#issuecomment-72896",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_019740.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-18T22:05:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8253",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8253#event-19740"
}
```
