# Issue 9327: Bugs in the Simple Sage Server API of sagenb

archive/issues_009327.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @robertwb @jasongrout\n\nKeywords: simple twist\n\nI found (and fixed) the following bugs in the file local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/simple/twist.py:\n\n* When trying to login via the Simple Sage Server API using the sagenb.notebook.notebook_object module the following error came up:\n....\n/sagenb-0.8-py2.6.egg/sagenb/simple/twist.py, line 206, in render\n   U = notebook_twist.notebook.user(username)\nexceptions.AttributeError: 'NoneType' object has no attribute 'user'\n--------------------------------------------------------------------\nThe problem is: The sagenb twist.py module still imports the (old and unmaintained) sage.server modules instead of the new sagenb files. It is quite logical that there is a NoneType error because there is no server started that relies on the (imported) old files.\nIf the two imports from sage.server in twist.py are replaced with the sagenb modules at least the login via Simple Sage Server API works quite fine.\n\n* When login works there is another bug: On line 286 in the twist.py file where it says \"return http.Response(...\" the stream variable has to be converted into a string (twisted somehow seems to have problems with unicode characters because IByteStream(stream) which is called in http.Response() fails with a TypeError if stream is of type 'unicode').\n\nIssue created by migration from https://trac.sagemath.org/ticket/9327\n\n",
    "created_at": "2010-06-24T12:22:29Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Bugs in the Simple Sage Server API of sagenb",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9327",
    "user": "https://trac.sagemath.org/admin/accounts/users/dpoetzsch"
}
```
Assignee: jason, was

CC:  @robertwb @jasongrout

Keywords: simple twist

I found (and fixed) the following bugs in the file local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/simple/twist.py:

* When trying to login via the Simple Sage Server API using the sagenb.notebook.notebook_object module the following error came up:
....
/sagenb-0.8-py2.6.egg/sagenb/simple/twist.py, line 206, in render
   U = notebook_twist.notebook.user(username)
exceptions.AttributeError: 'NoneType' object has no attribute 'user'
--------------------------------------------------------------------
The problem is: The sagenb twist.py module still imports the (old and unmaintained) sage.server modules instead of the new sagenb files. It is quite logical that there is a NoneType error because there is no server started that relies on the (imported) old files.
If the two imports from sage.server in twist.py are replaced with the sagenb modules at least the login via Simple Sage Server API works quite fine.

* When login works there is another bug: On line 286 in the twist.py file where it says "return http.Response(..." the stream variable has to be converted into a string (twisted somehow seems to have problems with unicode characters because IByteStream(stream) which is called in http.Response() fails with a TypeError if stream is of type 'unicode').

Issue created by migration from https://trac.sagemath.org/ticket/9327





---

archive/issue_comments_087841.json:
```json
{
    "body": "Could you post patches or new versions of the affected files?  After your fixes, does the simple API seem to work?\n\nThe simple API is important for the remote sagetex feature to work.",
    "created_at": "2010-06-27T03:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9327#issuecomment-87841",
    "user": "https://github.com/jasongrout"
}
```

Could you post patches or new versions of the affected files?  After your fixes, does the simple API seem to work?

The simple API is important for the remote sagetex feature to work.



---

archive/issue_comments_087842.json:
```json
{
    "body": "For my purposes the simple API seems to work after applying my fixes (this is logging in, computing stuff, logging out).",
    "created_at": "2010-06-28T08:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9327#issuecomment-87842",
    "user": "https://trac.sagemath.org/admin/accounts/users/dpoetzsch"
}
```

For my purposes the simple API seems to work after applying my fixes (this is logging in, computing stuff, logging out).



---

archive/issue_comments_087843.json:
```json
{
    "body": "Attachment [simple_api.patch](tarball://root/attachments/some-uuid/ticket9327/simple_api.patch) by dpoetzsch created at 2010-06-28 08:32:03\n\nThe bugfixes mentioned above as a patch file",
    "created_at": "2010-06-28T08:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9327#issuecomment-87843",
    "user": "https://trac.sagemath.org/admin/accounts/users/dpoetzsch"
}
```

Attachment [simple_api.patch](tarball://root/attachments/some-uuid/ticket9327/simple_api.patch) by dpoetzsch created at 2010-06-28 08:32:03

The bugfixes mentioned above as a patch file



---

archive/issue_comments_087844.json:
```json
{
    "body": "The new file including the fixes",
    "created_at": "2010-06-28T08:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9327#issuecomment-87844",
    "user": "https://trac.sagemath.org/admin/accounts/users/dpoetzsch"
}
```

The new file including the fixes



---

archive/issue_comments_087845.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-06T11:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9327#issuecomment-87845",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087846.json:
```json
{
    "body": "Attachment [twist.py](tarball://root/attachments/some-uuid/ticket9327/twist.py) by @rlmill created at 2010-07-06 11:53:53",
    "created_at": "2010-07-06T11:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9327#issuecomment-87846",
    "user": "https://github.com/rlmill"
}
```

Attachment [twist.py](tarball://root/attachments/some-uuid/ticket9327/twist.py) by @rlmill created at 2010-07-06 11:53:53



---

archive/issue_comments_087847.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-28T19:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9327#issuecomment-87847",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087848.json:
```json
{
    "body": "This seems to work great!  Remote Sagetex works, for example.\n\nAnother ticket would be deleting the verbose output in the server logs anytime something is executed.",
    "created_at": "2010-09-28T19:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9327#issuecomment-87848",
    "user": "https://github.com/jasongrout"
}
```

This seems to work great!  Remote Sagetex works, for example.

Another ticket would be deleting the verbose output in the server logs anytime something is executed.



---

archive/issue_events_009482.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-10-04T01:34:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9327",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9327#event-9482"
}
```



---

archive/issue_comments_087849.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-04T01:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9327#issuecomment-87849",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_087850.json:
```json
{
    "body": "David, could you add yourself to [the account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?",
    "created_at": "2010-10-08T22:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9327",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9327#issuecomment-87850",
    "user": "https://github.com/qed777"
}
```

David, could you add yourself to [the account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?
