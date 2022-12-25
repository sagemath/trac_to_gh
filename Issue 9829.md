# Issue 9829: SageNB: Bad Request. Maximum length of 102400 bytes exceeded.

archive/issues_009829.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  schymans @jhpalmieri\n\nReported by Stan Schymanski on [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/c814c8cf7bc7dd87):\n\n```\nWhen trying to change the code of a worksheet in a text editor (using\nthe edit button in the worksheet), I get the following error message\nwhenever I want to save changes:\n\nBad Request\nMaximum length of 102400 bytes exceeded.\n\nDoes anyone have an idea what could cause this and how this can be\ncircumvented?\n```\nDidier Deshommes replied:\n\n```\nMy guess is that the web server has a limit on the size of a POST\nrequest and that you have reached it. Typically this is 1024kb. The\nsolution is to increase this limit. I'm not sure how to do that for a \nwsgi application (which I assume sage is). \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9830\n\n",
    "created_at": "2010-08-28T07:44:03Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "SageNB: Bad Request. Maximum length of 102400 bytes exceeded.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9829",
    "user": "https://github.com/qed777"
}
```
Assignee: jason, was

CC:  schymans @jhpalmieri

Reported by Stan Schymanski on [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/c814c8cf7bc7dd87):

```
When trying to change the code of a worksheet in a text editor (using
the edit button in the worksheet), I get the following error message
whenever I want to save changes:

Bad Request
Maximum length of 102400 bytes exceeded.

Does anyone have an idea what could cause this and how this can be
circumvented?
```
Didier Deshommes replied:

```
My guess is that the web server has a limit on the size of a POST
request and that you have reached it. Typically this is 1024kb. The
solution is to increase this limit. I'm not sure how to do that for a 
wsgi application (which I assume sage is). 
```

Issue created by migration from https://trac.sagemath.org/ticket/9830





---

archive/issue_comments_096841.json:
```json
{
    "body": "We can fix this by adjusting `twisted.web2.resource.PostableResource.maxMem` near the top of `sagenb.notebook.twist`.\n\nFor now, if you have write access to your Sage distribution, you can do this yourself by putting, e.g.,\n\n```python\nresource.PostableResource.maxMem = 1000 * 1024\n```\njust after\n\n```python\nfrom twisted.web2 import server, http, resource, channel\n```\nnear the top of \n\n```\nSAGE_ROOT/local/lib/python2.6/site-packages/sagenb-*-py2.6.egg/sagenb/notebook/twist.py\n```\nand restarting the notebook server.\n\nHere's the beginning of the class definition:\n\n```python\nclass PostableResource(Resource):\n    \"\"\"\n    A L{Resource} capable of handling the POST request method.\n\n    @cvar maxMem: maximum memory used during the parsing of the data.\n    @type maxMem: C{int}\n    @cvar maxFields: maximum number of form fields allowed.\n    @type maxFields: C{int}\n    @cvar maxSize: maximum size of the whole post allowed.\n    @type maxSize: C{int}\n    \"\"\"\n    maxMem = 100 * 1024\n    maxFields = 1024\n    maxSize = 10 * 1024 * 1024\n\n    def http_POST(self, request):\n[...]\n```",
    "created_at": "2010-08-28T07:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9829#issuecomment-96841",
    "user": "https://github.com/qed777"
}
```

We can fix this by adjusting `twisted.web2.resource.PostableResource.maxMem` near the top of `sagenb.notebook.twist`.

For now, if you have write access to your Sage distribution, you can do this yourself by putting, e.g.,

```python
resource.PostableResource.maxMem = 1000 * 1024
```
just after

```python
from twisted.web2 import server, http, resource, channel
```
near the top of 

```
SAGE_ROOT/local/lib/python2.6/site-packages/sagenb-*-py2.6.egg/sagenb/notebook/twist.py
```
and restarting the notebook server.

Here's the beginning of the class definition:

```python
class PostableResource(Resource):
    """
    A L{Resource} capable of handling the POST request method.

    @cvar maxMem: maximum memory used during the parsing of the data.
    @type maxMem: C{int}
    @cvar maxFields: maximum number of form fields allowed.
    @type maxFields: C{int}
    @cvar maxSize: maximum size of the whole post allowed.
    @type maxSize: C{int}
    """
    maxMem = 100 * 1024
    maxFields = 1024
    maxSize = 10 * 1024 * 1024

    def http_POST(self, request):
[...]
```



---

archive/issue_comments_096842.json:
```json
{
    "body": "The work-around does not seem to work any more as of 4.6.2.",
    "created_at": "2011-05-19T18:17:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9829#issuecomment-96842",
    "user": "https://trac.sagemath.org/admin/accounts/users/schymans"
}
```

The work-around does not seem to work any more as of 4.6.2.



---

archive/issue_events_024748.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-03-28T10:02:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9829",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9829#event-24748"
}
```



---

archive/issue_comments_096843.json:
```json
{
    "body": "old ticket about deprecated sagenb. Can we close ?",
    "created_at": "2020-03-28T10:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9829#issuecomment-96843",
    "user": "https://github.com/fchapoton"
}
```

old ticket about deprecated sagenb. Can we close ?



---

archive/issue_comments_096844.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-03-28T10:02:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9829#issuecomment-96844",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096845.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-03-28T16:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9829#issuecomment-96845",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096846.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-28T17:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9829",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9829#issuecomment-96846",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_events_024749.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-03-28T17:11:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9829",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9829#event-24749"
}
```
