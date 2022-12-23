# Issue 1309: [graphs] generate trees

archive/issues_001309.json:
```json
{
    "body": "Assignee: rlm\n\nKeywords: graphs\n\nFrom Chris Godsil's wishlist (with final reply by Robert Miller):\n\n\n```\n> \n>>> A database of trees, or a generator for trees. I think it would be\n>>> reasonably\n>>> straightforward to generate rooted trees, and hence get trees. The\n>>> generators\n>>> would be more useful than the database. It is not impossible that\n>>> something\n>>> in the nauty package generates trees.\n> If you look into the code that graphs(7) calls, you will notice that\n> you can pass it any vertex-hereditary property, including being a\n> tree. So in some sense, this is already implemented. However, this\n> could be its own constructor, and more importantly, I know of a way to\n> optimize the generation of trees to go much faster than it would with\n> what I described above. Create a ticket, and assign it to me.\n> \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1309\n\n",
    "created_at": "2007-11-28T19:58:44Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "[graphs] generate trees",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1309",
    "user": "jason"
}
```
Assignee: rlm

Keywords: graphs

From Chris Godsil's wishlist (with final reply by Robert Miller):


```
> 
>>> A database of trees, or a generator for trees. I think it would be
>>> reasonably
>>> straightforward to generate rooted trees, and hence get trees. The
>>> generators
>>> would be more useful than the database. It is not impossible that
>>> something
>>> in the nauty package generates trees.
> If you look into the code that graphs(7) calls, you will notice that
> you can pass it any vertex-hereditary property, including being a
> tree. So in some sense, this is already implemented. However, this
> could be its own constructor, and more importantly, I know of a way to
> optimize the generation of trees to go much faster than it would with
> what I described above. Create a ticket, and assign it to me.
> 
```



Issue created by migration from https://trac.sagemath.org/ticket/1309





---

archive/issue_comments_008238.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-02T04:52:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1309#issuecomment-8238",
    "user": "rlm"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008239.json:
```json
{
    "body": "There are still significant bugs from the patch from\n\nhttp://trac.sagemath.org/sage_trac/ticket/1361\n\nthat I am working on now. I discovered them while implementing this ticket, so the fixes will be in the patch for this.",
    "created_at": "2007-12-02T21:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1309#issuecomment-8239",
    "user": "rlm"
}
```

There are still significant bugs from the patch from

http://trac.sagemath.org/sage_trac/ticket/1361

that I am working on now. I discovered them while implementing this ticket, so the fixes will be in the patch for this.



---

archive/issue_comments_008240.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-12-03T01:53:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1309#issuecomment-8240",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_008241.json:
```json
{
    "body": "Merged in 2.8.15.rc0.",
    "created_at": "2007-12-03T02:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1309#issuecomment-8241",
    "user": "mabshoff"
}
```

Merged in 2.8.15.rc0.



---

archive/issue_comments_008242.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-03T02:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1309",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1309#issuecomment-8242",
    "user": "mabshoff"
}
```

Resolution: fixed
