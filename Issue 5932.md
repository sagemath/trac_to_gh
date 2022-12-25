# Issue 5932: graphs.RandomRegular(3,10) often returns a graph on 0 vertices

archive/issues_005932.json:
```json
{
    "body": "Assignee: @rlmill\n\nThe docstring for graphs.RandomRegular says\n\n```\nReturns a random d-regular graph on n vertices, or returns False on\nfailure.\n```\n\n\nHowever, try calling it a few times with input 3,10 and with probability about 25% you'll get back an empty graph!:\n\n```\nsage: graphs.RandomRegular(3,10)\nGraph on 0 vertices\n\nsage: [len(graphs.RandomRegular(3,10)) for _ in range(1000)].count(0)\n232\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5932\n\n",
    "created_at": "2009-04-29T05:21:23Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "graphs.RandomRegular(3,10) often returns a graph on 0 vertices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5932",
    "user": "https://github.com/williamstein"
}
```
Assignee: @rlmill

The docstring for graphs.RandomRegular says

```
Returns a random d-regular graph on n vertices, or returns False on
failure.
```


However, try calling it a few times with input 3,10 and with probability about 25% you'll get back an empty graph!:

```
sage: graphs.RandomRegular(3,10)
Graph on 0 vertices

sage: [len(graphs.RandomRegular(3,10)) for _ in range(1000)].count(0)
232
```



Issue created by migration from https://trac.sagemath.org/ticket/5932





---

archive/issue_comments_046824.json:
```json
{
    "body": "This is a bug in NetworkX. Their docstring says:\n\n\n```\nDefinition:     networkx.random_regular_graph(d, n, seed=None)\nSource:\ndef random_regular_graph(d, n, seed=None):\n    \"\"\"Return a random regular graph of n nodes each with degree d, G_{n,d}.\n    Return False if unsuccessful.\n```\n",
    "created_at": "2009-04-29T16:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5932#issuecomment-46824",
    "user": "https://github.com/rlmill"
}
```

This is a bug in NetworkX. Their docstring says:


```
Definition:     networkx.random_regular_graph(d, n, seed=None)
Source:
def random_regular_graph(d, n, seed=None):
    """Return a random regular graph of n nodes each with degree d, G_{n,d}.
    Return False if unsuccessful.
```




---

archive/issue_comments_046825.json:
```json
{
    "body": "Attachment [trac_5932.patch](tarball://root/attachments/some-uuid/ticket5932/trac_5932.patch) by @rlmill created at 2009-07-16 22:05:49",
    "created_at": "2009-07-16T22:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5932#issuecomment-46825",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_5932.patch](tarball://root/attachments/some-uuid/ticket5932/trac_5932.patch) by @rlmill created at 2009-07-16 22:05:49



---

archive/issue_comments_046826.json:
```json
{
    "body": "The fix looks correct, the file passes doctests, and everything looks great!",
    "created_at": "2009-07-18T23:35:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5932#issuecomment-46826",
    "user": "https://github.com/jasongrout"
}
```

The fix looks correct, the file passes doctests, and everything looks great!



---

archive/issue_comments_046827.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-19T12:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5932#issuecomment-46827",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_006186.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-19T12:02:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5932",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5932#event-6186"
}
```
