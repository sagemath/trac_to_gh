# Issue 5675: notebook with address="" option should set the address to something useful

archive/issues_005675.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  acleone\n\n\n```\nOn Thu, 02 Apr 2009 at 11:53PM -0700, Ondrej Certik wrote:\n>\n> Hi,\n>\n[...]\n> sage: notebook(secure=False, address=\"\")\n> [...]\n>\n> and it starts firefox on the local machine with this address:\n>\n> http://[www.:8000.com]/?startup_token=41e2a34e89e40139333a8113e9be2a50\n>\n> which obviously fails. This also happens with sage 3.2.3 (I didn't try\n> other versions).\n\nThis has been around for a while; I haven't filed a ticket for it, since\nI just retype the URL.\n```\n\n\nIt used to be in the notebook that address=\"\" was an error.  Then when we switched to twisted, it suddenly meant \"listen on all interfaces\".  Now it's a common option to give.  \n\nThe two places I know of where the address is given are: (1) when popping up a web browser pointed at the notebook, and (2) when publishing a worksheet and it shows the URL where people can get the published version.\n\nIdeas:\n* If one gives address=\"\", everywhere else, set the address to the fully qualified domain name.  How to get that in Python?\n* If one gives address=\"\", simply never automatically pop up a viewer, and doesn't display the URL for published worksheets (since it is wrong).  If people want proper URL's they shouldn't be lazy with their address= option.\n* Make address=\"\" an error, and require the user to give a proper fully qualified name.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5675\n\n",
    "created_at": "2009-04-03T13:27:21Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook with address=\"\" option should set the address to something useful",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5675",
    "user": "was"
}
```
Assignee: boothby

CC:  acleone


```
On Thu, 02 Apr 2009 at 11:53PM -0700, Ondrej Certik wrote:
>
> Hi,
>
[...]
> sage: notebook(secure=False, address="")
> [...]
>
> and it starts firefox on the local machine with this address:
>
> http://[www.:8000.com]/?startup_token=41e2a34e89e40139333a8113e9be2a50
>
> which obviously fails. This also happens with sage 3.2.3 (I didn't try
> other versions).

This has been around for a while; I haven't filed a ticket for it, since
I just retype the URL.
```


It used to be in the notebook that address="" was an error.  Then when we switched to twisted, it suddenly meant "listen on all interfaces".  Now it's a common option to give.  

The two places I know of where the address is given are: (1) when popping up a web browser pointed at the notebook, and (2) when publishing a worksheet and it shows the URL where people can get the published version.

Ideas:
* If one gives address="", everywhere else, set the address to the fully qualified domain name.  How to get that in Python?
* If one gives address="", simply never automatically pop up a viewer, and doesn't display the URL for published worksheets (since it is wrong).  If people want proper URL's they shouldn't be lazy with their address= option.
* Make address="" an error, and require the user to give a proper fully qualified name.

Issue created by migration from https://trac.sagemath.org/ticket/5675





---

archive/issue_comments_044395.json:
```json
{
    "body": "This ticket subsumes #5263.",
    "created_at": "2009-08-10T09:35:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5675#issuecomment-44395",
    "user": "mpatel"
}
```

This ticket subsumes #5263.



---

archive/issue_comments_044396.json:
```json
{
    "body": "There is [socket.getfqdn](http://docs.python.org/library/socket.html#socket.getfqdn), but does it help?  On `boxen`:\n\n```python\nsage: import socket\nsage: socket.getfqdn()\n'localhost'\nsage: socket.gethostbyname_ex(socket.gethostname())\n('localhost', ['boxen', 'boxen'], ['127.0.0.1', '128.208.160.197'])\n```\n\nOn a local Linux machine, I get\n\n```python\nsage: import socket\nsage: socket.getfqdn()\n'localhost.localdomain'\nsage: socket.gethostbyname_ex(socket.gethostname())\n('localhost.localdomain', ['localhost', 'foo'], ['127.0.0.1'])\n```\n\nall of which happen to be in `/etc/hosts`.\n\nWhat if we just add an option `published_host=*` (or a variation) and insert it into URLs for published (and remote!) worksheets when `interface=*`?  We could print a warning or raise an error, if both are left empty.",
    "created_at": "2010-01-16T06:49:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5675#issuecomment-44396",
    "user": "mpatel"
}
```

There is [socket.getfqdn](http://docs.python.org/library/socket.html#socket.getfqdn), but does it help?  On `boxen`:

```python
sage: import socket
sage: socket.getfqdn()
'localhost'
sage: socket.gethostbyname_ex(socket.gethostname())
('localhost', ['boxen', 'boxen'], ['127.0.0.1', '128.208.160.197'])
```

On a local Linux machine, I get

```python
sage: import socket
sage: socket.getfqdn()
'localhost.localdomain'
sage: socket.gethostbyname_ex(socket.gethostname())
('localhost.localdomain', ['localhost', 'foo'], ['127.0.0.1'])
```

all of which happen to be in `/etc/hosts`.

What if we just add an option `published_host=*` (or a variation) and insert it into URLs for published (and remote!) worksheets when `interface=*`?  We could print a warning or raise an error, if both are left empty.



---

archive/issue_comments_044397.json:
```json
{
    "body": "Renaming this to a more appropriate title.",
    "created_at": "2010-01-19T06:24:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5675#issuecomment-44397",
    "user": "timdumol"
}
```

Renaming this to a more appropriate title.



---

archive/issue_comments_044398.json:
```json
{
    "body": "Attachment [trac_5675-address-launch.patch](tarball://root/attachments/some-uuid/ticket5675/trac_5675-address-launch.patch) by timdumol created at 2010-01-19 06:26:15\n\nThis sets the hostname to localhost if interface=\"\" when launching the page",
    "created_at": "2010-01-19T06:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5675#issuecomment-44398",
    "user": "timdumol"
}
```

Attachment [trac_5675-address-launch.patch](tarball://root/attachments/some-uuid/ticket5675/trac_5675-address-launch.patch) by timdumol created at 2010-01-19 06:26:15

This sets the hostname to localhost if interface="" when launching the page



---

archive/issue_comments_044399.json:
```json
{
    "body": "This fixes the issue described.",
    "created_at": "2010-01-19T06:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5675#issuecomment-44399",
    "user": "timdumol"
}
```

This fixes the issue described.



---

archive/issue_comments_044400.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T06:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5675#issuecomment-44400",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_044401.json:
```json
{
    "body": "LGTM.  See #5263.  This bug is only for a blank option passed to `sage -n interface=''`.",
    "created_at": "2010-01-19T23:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5675#issuecomment-44401",
    "user": "acleone"
}
```

LGTM.  See #5263.  This bug is only for a blank option passed to `sage -n interface=''`.



---

archive/issue_comments_044402.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T23:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5675#issuecomment-44402",
    "user": "acleone"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_044403.json:
```json
{
    "body": "I see a few cases:\n1. The user starts the server on his/her computer.  localhost works fine\n2. The user starts the server on a network computer via ssh, in which case the browser should probably auto-open to whatever address the user used to ssh into computer.  However we can't get this information, and last time I tried firefox doesn't open anyway (when starting the notebook in an ssh session).\n\nSee #5263 for the publish url bug.",
    "created_at": "2010-01-19T23:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5675#issuecomment-44403",
    "user": "acleone"
}
```

I see a few cases:
1. The user starts the server on his/her computer.  localhost works fine
2. The user starts the server on a network computer via ssh, in which case the browser should probably auto-open to whatever address the user used to ssh into computer.  However we can't get this information, and last time I tried firefox doesn't open anyway (when starting the notebook in an ssh session).

See #5263 for the publish url bug.



---

archive/issue_comments_044404.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-25T01:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5675#issuecomment-44404",
    "user": "mpatel"
}
```

Resolution: fixed
