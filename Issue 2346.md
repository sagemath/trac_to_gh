# Issue 2346: Sage needs a simple api for interaction with other applications

archive/issues_002346.json:
```json
{
    "body": "Assignee: was\n\nMany people have shown interest in a simple API that could be used to interface with Sage. This would be useful for java applets, moodle plugins, and other applications to use Sage as a computational back end. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2346\n\n",
    "created_at": "2008-02-28T08:53:49Z",
    "labels": [
        "user interface",
        "major",
        "enhancement"
    ],
    "title": "Sage needs a simple api for interaction with other applications",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2346",
    "user": "robertwb"
}
```
Assignee: was

Many people have shown interest in a simple API that could be used to interface with Sage. This would be useful for java applets, moodle plugins, and other applications to use Sage as a computational back end. 

Issue created by migration from https://trac.sagemath.org/ticket/2346





---

archive/issue_comments_015710.json:
```json
{
    "body": "Attachment [simple-api.hg](tarball://root/attachments/some-uuid/ticket2346/simple-api.hg) by robertwb created at 2008-02-28 08:54:07",
    "created_at": "2008-02-28T08:54:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2346#issuecomment-15710",
    "user": "robertwb"
}
```

Attachment [simple-api.hg](tarball://root/attachments/some-uuid/ticket2346/simple-api.hg) by robertwb created at 2008-02-28 08:54:07



---

archive/issue_comments_015711.json:
```json
{
    "body": "The above bundle implements a simple api over http as described in http://groups.google.com/group/sage-edu/browse_thread/thread/f2935bb4ddb72dc5\n\nIt should be completely useable in its current form, though of course there is lots of room for improvement.",
    "created_at": "2008-02-28T08:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2346#issuecomment-15711",
    "user": "robertwb"
}
```

The above bundle implements a simple api over http as described in http://groups.google.com/group/sage-edu/browse_thread/thread/f2935bb4ddb72dc5

It should be completely useable in its current form, though of course there is lots of room for improvement.



---

archive/issue_comments_015712.json:
```json
{
    "body": "Changing assignee from was to robertwb.",
    "created_at": "2008-02-28T08:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2346#issuecomment-15712",
    "user": "robertwb"
}
```

Changing assignee from was to robertwb.



---

archive/issue_comments_015713.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-28T08:57:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2346#issuecomment-15713",
    "user": "robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015714.json:
```json
{
    "body": "A few comments:\n\n1) Other than an unknown parent message, this applies cleanly against 2.10.3.alpha0\n\n2) I can't get the server/simple/twisted.py tests to pass.  The following error causes all the problems:\n\n\n```\n IOError: [Errno url error] unknown url type: 'https'\n```\n\n\nOther than that, this patch looks excellent!",
    "created_at": "2008-02-28T09:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2346#issuecomment-15714",
    "user": "mhansen"
}
```

A few comments:

1) Other than an unknown parent message, this applies cleanly against 2.10.3.alpha0

2) I can't get the server/simple/twisted.py tests to pass.  The following error causes all the problems:


```
 IOError: [Errno url error] unknown url type: 'https'
```


Other than that, this patch looks excellent!



---

archive/issue_comments_015715.json:
```json
{
    "body": "the function wait_for_comp could probably make use of twisted.internet.task.LoopingCall versus basically scheduling your own callbacks. See the API documentation here:\n\nhttp://twistedmatrix.com/documents/current/api/twisted.internet.task.LoopingCall.html\n\nOther than that it looks good.",
    "created_at": "2008-02-28T16:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2346#issuecomment-15715",
    "user": "yi"
}
```

the function wait_for_comp could probably make use of twisted.internet.task.LoopingCall versus basically scheduling your own callbacks. See the API documentation here:

http://twistedmatrix.com/documents/current/api/twisted.internet.task.LoopingCall.html

Other than that it looks good.



---

archive/issue_comments_015716.json:
```json
{
    "body": "I'll look into the looping call thing more, but if it's what I think it is I'm not sure it satisfies all my needs. \n\nThe Errno url error is strange, does your urllib not support secure http connections?",
    "created_at": "2008-03-07T18:25:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2346#issuecomment-15716",
    "user": "robertwb"
}
```

I'll look into the looping call thing more, but if it's what I think it is I'm not sure it satisfies all my needs. 

The Errno url error is strange, does your urllib not support secure http connections?



---

archive/issue_comments_015717.json:
```json
{
    "body": "Attachment [2346-loops.patch](tarball://root/attachments/some-uuid/ticket2346/2346-loops.patch) by robertwb created at 2008-03-07 19:59:13\n\nI've re-implemented the waiting using LoopingCall, and also reduced the amount of time it spends blocking waiting for Sage input. \n\nI'm not sure what to do about the https error--we don't want to doctest with http as that would be a potential security vulnerability. \n\nmhansen: what system are you getting that error on. Is it the Sage python?",
    "created_at": "2008-03-07T19:59:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2346#issuecomment-15717",
    "user": "robertwb"
}
```

Attachment [2346-loops.patch](tarball://root/attachments/some-uuid/ticket2346/2346-loops.patch) by robertwb created at 2008-03-07 19:59:13

I've re-implemented the waiting using LoopingCall, and also reduced the amount of time it spends blocking waiting for Sage input. 

I'm not sure what to do about the https error--we don't want to doctest with http as that would be a potential security vulnerability. 

mhansen: what system are you getting that error on. Is it the Sage python?



---

archive/issue_comments_015718.json:
```json
{
    "body": "Perhaps we can use http://twistedmatrix.com/documents/current/api/twisted.web.client.html\n\n(Need to do the same gnu-tls vs. OpenSSL trick as for the notebook.)",
    "created_at": "2008-03-30T00:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2346#issuecomment-15718",
    "user": "robertwb"
}
```

Perhaps we can use http://twistedmatrix.com/documents/current/api/twisted.web.client.html

(Need to do the same gnu-tls vs. OpenSSL trick as for the notebook.)



---

archive/issue_comments_015719.json:
```json
{
    "body": "Attachment [2346-gnutls.patch](tarball://root/attachments/some-uuid/ticket2346/2346-gnutls.patch) by robertwb created at 2008-04-06 04:42:03",
    "created_at": "2008-04-06T04:42:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2346#issuecomment-15719",
    "user": "robertwb"
}
```

Attachment [2346-gnutls.patch](tarball://root/attachments/some-uuid/ticket2346/2346-gnutls.patch) by robertwb created at 2008-04-06 04:42:03



---

archive/issue_comments_015720.json:
```json
{
    "body": "Using twisted.web.client with the reactor and all is a major pain to do interactively (e.g. for doctests), but I was able to get it to fall back to gnutls if socket.ssl (from openssl) is not available.",
    "created_at": "2008-04-06T04:43:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2346#issuecomment-15720",
    "user": "robertwb"
}
```

Using twisted.web.client with the reactor and all is a major pain to do interactively (e.g. for doctests), but I was able to get it to fall back to gnutls if socket.ssl (from openssl) is not available.



---

archive/issue_comments_015721.json:
```json
{
    "body": "Attachment [2346-early-ssl-import.patch](tarball://root/attachments/some-uuid/ticket2346/2346-early-ssl-import.patch) by robertwb created at 2008-04-06 05:21:20",
    "created_at": "2008-04-06T05:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2346#issuecomment-15721",
    "user": "robertwb"
}
```

Attachment [2346-early-ssl-import.patch](tarball://root/attachments/some-uuid/ticket2346/2346-early-ssl-import.patch) by robertwb created at 2008-04-06 05:21:20



---

archive/issue_comments_015722.json:
```json
{
    "body": "Everything works for me.  Apply the bundle and all three patches.",
    "created_at": "2008-04-06T05:30:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2346#issuecomment-15722",
    "user": "mhansen"
}
```

Everything works for me.  Apply the bundle and all three patches.



---

archive/issue_comments_015723.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T06:05:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2346#issuecomment-15723",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015724.json:
```json
{
    "body": "Merged the bundle as well as the three patches in Sage 3.0.alpha2",
    "created_at": "2008-04-06T06:05:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2346#issuecomment-15724",
    "user": "mabshoff"
}
```

Merged the bundle as well as the three patches in Sage 3.0.alpha2
