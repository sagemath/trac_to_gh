# Issue 7628: Error on account creation still creates (half of) an account

archive/issues_007628.json:
```json
{
    "body": "Assignee: was\n\nI went to the settings page and checked yes to allowing new registrations and requiring an email address.  I then created an account with username asdf and password asdf.  It returned an error (bad password; contains the username).  I logged out anyway and logged back in as admin.  Then I clicked on Settings, and got the following error:\n\n\n\n```\n\n\n2009-12-08 13:34:06-0600 [HTTPChannel,3,127.0.0.1] Exception rendering:\n2009-12-08 13:34:06-0600 [HTTPChannel,3,127.0.0.1] Unhandled Error\n   Traceback (most recent call last):\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 186, in addCallbacks\n       self._runCallbacks()\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n       self.result = callback(self.result, *args, **kw)\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 289, in _continue\n       self.unpause()\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 285, in unpause\n       self._runCallbacks()\n   --- <exception caught here> ---\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py\", line 328, in _runCallbacks\n       self.result = callback(self.result, *args, **kw)\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/web2/server.py\", line 296, in <lambda>\n       d.addCallback(lambda res, req: res.renderHTTP(req), self)\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 85, in renderHTTP\n       return method(request)\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 202, in http_GET\n       return super(Resource, self).http_GET(request)\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py\", line 128, in http_GET\n       return self.render(request)\n     File \"/home/jason/sage/local/lib/python2.6/site-packages/sagenb/notebook/twist.py\", line 962, in render\n       template_dict['email_address'] = 'None' if not notebook.user(self.username)._User__email else notebook.user(self.username)._User__email\n   exceptions.AttributeError: 'User' object has no attribute '_User__email' \n\nIssue created by migration from https://trac.sagemath.org/ticket/7628\n\n",
    "created_at": "2009-12-08T19:56:28Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Error on account creation still creates (half of) an account",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7628",
    "user": "jason"
}
```
Assignee: was

I went to the settings page and checked yes to allowing new registrations and requiring an email address.  I then created an account with username asdf and password asdf.  It returned an error (bad password; contains the username).  I logged out anyway and logged back in as admin.  Then I clicked on Settings, and got the following error:



```


2009-12-08 13:34:06-0600 [HTTPChannel,3,127.0.0.1] Exception rendering:
2009-12-08 13:34:06-0600 [HTTPChannel,3,127.0.0.1] Unhandled Error
   Traceback (most recent call last):
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 186, in addCallbacks
       self._runCallbacks()
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
       self.result = callback(self.result, *args, **kw)
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 289, in _continue
       self.unpause()
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 285, in unpause
       self._runCallbacks()
   --- <exception caught here> ---
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/internet/defer.py", line 328, in _runCallbacks
       self.result = callback(self.result, *args, **kw)
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/web2/server.py", line 296, in <lambda>
       d.addCallback(lambda res, req: res.renderHTTP(req), self)
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 85, in renderHTTP
       return method(request)
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 202, in http_GET
       return super(Resource, self).http_GET(request)
     File "/home/jason/sage/local/lib/python2.6/site-packages/twisted/web2/resource.py", line 128, in http_GET
       return self.render(request)
     File "/home/jason/sage/local/lib/python2.6/site-packages/sagenb/notebook/twist.py", line 962, in render
       template_dict['email_address'] = 'None' if not notebook.user(self.username)._User__email else notebook.user(self.username)._User__email
   exceptions.AttributeError: 'User' object has no attribute '_User__email' 

Issue created by migration from https://trac.sagemath.org/ticket/7628





---

archive/issue_comments_065172.json:
```json
{
    "body": "Just prevents the error.  Depends on #7625.  sagenb repo.",
    "created_at": "2009-12-09T01:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7628#issuecomment-65172",
    "user": "mpatel"
}
```

Just prevents the error.  Depends on #7625.  sagenb repo.



---

archive/issue_comments_065173.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-09T01:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7628#issuecomment-65173",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065174.json:
```json
{
    "body": "Attachment [trac_7628-user_settings_page_error.patch](tarball://root/attachments/some-uuid/ticket7628/trac_7628-user_settings_page_error.patch) by mpatel created at 2009-12-09 01:09:29\n\nThe patch should prevent the error.  It does not activate the email system.\n\nIn the future, we could auto-generate the user settings page, with drop-down menus for key-bindings, a la the notebook settings page.  From `todo.txt`:\n\n```\n[ ] move is_valid_username (etc.) out of twist.py, which is definitely *not* where it belongs\n```\n\nHow about a `validate.py`, with functions for other fields, too?",
    "created_at": "2009-12-09T01:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7628#issuecomment-65174",
    "user": "mpatel"
}
```

Attachment [trac_7628-user_settings_page_error.patch](tarball://root/attachments/some-uuid/ticket7628/trac_7628-user_settings_page_error.patch) by mpatel created at 2009-12-09 01:09:29

The patch should prevent the error.  It does not activate the email system.

In the future, we could auto-generate the user settings page, with drop-down menus for key-bindings, a la the notebook settings page.  From `todo.txt`:

```
[ ] move is_valid_username (etc.) out of twist.py, which is definitely *not* where it belongs
```

How about a `validate.py`, with functions for other fields, too?



---

archive/issue_comments_065175.json:
```json
{
    "body": "Looks good. Thanks.",
    "created_at": "2009-12-09T03:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7628#issuecomment-65175",
    "user": "was"
}
```

Looks good. Thanks.



---

archive/issue_comments_065176.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-09T03:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7628#issuecomment-65176",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065177.json:
```json
{
    "body": "Merged into 0.4.7 (which isn't released yet).",
    "created_at": "2009-12-09T06:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7628#issuecomment-65177",
    "user": "was"
}
```

Merged into 0.4.7 (which isn't released yet).



---

archive/issue_comments_065178.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T06:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7628",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7628#issuecomment-65178",
    "user": "was"
}
```

Resolution: fixed
