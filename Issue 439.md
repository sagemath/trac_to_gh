# Issue 439: Interace with remote programs allowing for as many hops as needed

archive/issues_000439.json:
```json
{
    "body": "Assignee: pdehaye\n\nsee\nhttp://groups.google.com/group/sage-support/browse_thread/thread/b7215f69359ff4c2\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/439\n\n",
    "created_at": "2007-08-18T18:02:27Z",
    "labels": [
        "interfaces",
        "minor",
        "enhancement"
    ],
    "title": "Interace with remote programs allowing for as many hops as needed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/439",
    "user": "pdehaye"
}
```
Assignee: pdehaye

see
http://groups.google.com/group/sage-support/browse_thread/thread/b7215f69359ff4c2


Issue created by migration from https://trac.sagemath.org/ticket/439





---

archive/issue_comments_002196.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-18T21:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/439#issuecomment-2196",
    "user": "pdehaye"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002197.json:
```json
{
    "body": "Attachment [5771.patch](tarball://root/attachments/some-uuid/ticket439/5771.patch) by pdehaye created at 2007-08-19 23:11:30\n\nJust posted a patch. Issues that still need to be resolved:\n* could do better when converting with _sage_() remote objects\n* the _remote_tmpfile is defaulted to \"/tmp\", I am not sure that's a good idea, and if we shouldn't just return an error if (server_tmpdir is None) and not (server is None)",
    "created_at": "2007-08-19T23:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/439#issuecomment-2197",
    "user": "pdehaye"
}
```

Attachment [5771.patch](tarball://root/attachments/some-uuid/ticket439/5771.patch) by pdehaye created at 2007-08-19 23:11:30

Just posted a patch. Issues that still need to be resolved:
* could do better when converting with _sage_() remote objects
* the _remote_tmpfile is defaulted to "/tmp", I am not sure that's a good idea, and if we shouldn't just return an error if (server_tmpdir is None) and not (server is None)



---

archive/issue_comments_002198.json:
```json
{
    "body": "also, removed expect.tmp as this was confusing:\nthere ought to be two different temporary files in expect.py. one would be _local_tmpfile and interact with sage/python and the other one _remote_tmpfile and interact with the remote CAS session. \nallowing for something named tmp in expect.py is confusing as people who program more interfaces don t tend to think of the distinction needed when doing things remotely, and end up using the same file for both (without scp'ing one to the other if is_remote())",
    "created_at": "2007-08-19T23:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/439#issuecomment-2198",
    "user": "pdehaye"
}
```

also, removed expect.tmp as this was confusing:
there ought to be two different temporary files in expect.py. one would be _local_tmpfile and interact with sage/python and the other one _remote_tmpfile and interact with the remote CAS session. 
allowing for something named tmp in expect.py is confusing as people who program more interfaces don t tend to think of the distinction needed when doing things remotely, and end up using the same file for both (without scp'ing one to the other if is_remote())



---

archive/issue_comments_002199.json:
```json
{
    "body": "Trac #160, which will be included before this, might need to be revisited.",
    "created_at": "2007-08-20T19:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/439#issuecomment-2199",
    "user": "pdehaye"
}
```

Trac #160, which will be included before this, might need to be revisited.



---

archive/issue_comments_002200.json:
```json
{
    "body": "Paul has implemented this, sent me a patch, and I've applied it.",
    "created_at": "2007-08-23T01:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/439#issuecomment-2200",
    "user": "was"
}
```

Paul has implemented this, sent me a patch, and I've applied it.



---

archive/issue_comments_002201.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-23T01:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/439",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/439#issuecomment-2201",
    "user": "was"
}
```

Resolution: fixed
