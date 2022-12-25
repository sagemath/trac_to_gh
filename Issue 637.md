# Issue 637: notebook improvement --

archive/issues_000637.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\n> 1) It would be nice if one could upload directly the text of a\n>    worksheet to SAGE and have it automatically evaluated as an\n>    uploaded worksheet.\n\nI like this suggestion.  It has always been on my (perhaps only mental)\ntodo list. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/637\n\n",
    "created_at": "2007-09-11T04:39:49Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "notebook improvement --",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/637",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby


```
> 1) It would be nice if one could upload directly the text of a
>    worksheet to SAGE and have it automatically evaluated as an
>    uploaded worksheet.

I like this suggestion.  It has always been on my (perhaps only mental)
todo list. 
```


Issue created by migration from https://trac.sagemath.org/ticket/637





---

archive/issue_comments_003270.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2007-09-11T04:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/637#issuecomment-3270",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to minor.



---

archive/issue_comments_003271.json:
```json
{
    "body": "\n```\n21:39 < boothby> wstein -- can we close #637?\n21:40 < wstein> no.\n21:40 < wstein> I don't think so.\n21:40 < wstein> The idea was supposed to be that you could make a wiki\n21:40 < wstein> marked up .txt file, with {{{'s\n21:40 < wstein> and upload it.\n21:40 < wstein> And get a worksheet.\n```\n",
    "created_at": "2008-03-17T04:43:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/637#issuecomment-3271",
    "user": "https://github.com/williamstein"
}
```


```
21:39 < boothby> wstein -- can we close #637?
21:40 < wstein> no.
21:40 < wstein> I don't think so.
21:40 < wstein> The idea was supposed to be that you could make a wiki
21:40 < wstein> marked up .txt file, with {{{'s
21:40 < wstein> and upload it.
21:40 < wstein> And get a worksheet.
```




---

archive/issue_comments_003272.json:
```json
{
    "body": "\n```\n19:55 < tclemans> for the upload a plain text worksheet ticket: would it just\n                  work to create an empty worksheet and then call edit_save\n                  with the plain text?\n19:55 < wstein-3121> tclemans -- yep.\n19:55 < wstein-3121> That's exactly right.\n```\n",
    "created_at": "2008-05-11T02:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/637#issuecomment-3272",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```


```
19:55 < tclemans> for the upload a plain text worksheet ticket: would it just
                  work to create an empty worksheet and then call edit_save
                  with the plain text?
19:55 < wstein-3121> tclemans -- yep.
19:55 < wstein-3121> That's exactly right.
```




---

archive/issue_comments_003273.json:
```json
{
    "body": "Attachment [sage-637.patch](tarball://root/attachments/some-uuid/ticket637/sage-637.patch) by @williamstein created at 2008-05-11 05:03:26",
    "created_at": "2008-05-11T05:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/637#issuecomment-3273",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-637.patch](tarball://root/attachments/some-uuid/ticket637/sage-637.patch) by @williamstein created at 2008-05-11 05:03:26



---

archive/issue_comments_003274.json:
```json
{
    "body": "The attached patch:\n\n1. Implements uploading .txt files (plain text worksheets).\n2. Adds lots of related documentation, docstrings, doctests, etc., and clean up some related code.",
    "created_at": "2008-05-11T05:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/637#issuecomment-3274",
    "user": "https://github.com/williamstein"
}
```

The attached patch:

1. Implements uploading .txt files (plain text worksheets).
2. Adds lots of related documentation, docstrings, doctests, etc., and clean up some related code.



---

archive/issue_comments_003275.json:
```json
{
    "body": "I can't seem to apply the patch.\n\n\n```\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/637/sage-637.patch?format=raw')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/637/sage-637.patch?format=raw\nLoading: [..]\ncd \"/home/tclemans/sage-3.0/devel/sage\" && hg status\ncd \"/home/tclemans/sage-3.0/devel/sage\" && hg status\ncd \"/home/tclemans/sage-3.0/devel/sage\" && hg import   \"/home/tclemans/.sage/temp/sage/27583/tmp_0.patch\"\napplying /home/tclemans/.sage/temp/sage/27583/tmp_0.patch\npatching file sage/server/notebook/notebook.py\nHunk #1 FAILED at 148\n1 out of 4 hunks FAILED -- saving rejects to file sage/server/notebook/notebook.py.rej\nabort: patch failed to apply\nsage: version()\n'SAGE Version 3.0.1, Release Date: 2008-05-05'\n```\n",
    "created_at": "2008-05-11T14:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/637#issuecomment-3275",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I can't seem to apply the patch.


```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/637/sage-637.patch?format=raw')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/637/sage-637.patch?format=raw
Loading: [..]
cd "/home/tclemans/sage-3.0/devel/sage" && hg status
cd "/home/tclemans/sage-3.0/devel/sage" && hg status
cd "/home/tclemans/sage-3.0/devel/sage" && hg import   "/home/tclemans/.sage/temp/sage/27583/tmp_0.patch"
applying /home/tclemans/.sage/temp/sage/27583/tmp_0.patch
patching file sage/server/notebook/notebook.py
Hunk #1 FAILED at 148
1 out of 4 hunks FAILED -- saving rejects to file sage/server/notebook/notebook.py.rej
abort: patch failed to apply
sage: version()
'SAGE Version 3.0.1, Release Date: 2008-05-05'
```




---

archive/issue_comments_003276.json:
```json
{
    "body": "This is likely a dependency issue. William can provide a dependency tree for the 15+ notebook patches he did during Bug Day 12.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-11T14:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/637#issuecomment-3276",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is likely a dependency issue. William can provide a dependency tree for the 15+ notebook patches he did during Bug Day 12.

Cheers,

Michael



---

archive/issue_comments_003277.json:
```json
{
    "body": "I applied the patches in the following order and had no problems:\n\n```\n1733\n1864\n2359\n2636\n2884\n2992\n3024\n3053\n637\n```\n",
    "created_at": "2008-05-12T06:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/637#issuecomment-3277",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

I applied the patches in the following order and had no problems:

```
1733
1864
2359
2636
2884
2992
3024
3053
637
```




---

archive/issue_comments_003278.json:
```json
{
    "body": "Works, except when I tried to upload a rather old (from SD3) worksheet:\n\n\n```\n2008-05-11 22:47:55-0700 [-] cd \"/home/boothby/.sage/temp/eight/32244/dir_1\"; tar -jxf \"/home/boothby/.sage/temp/eight/32244/dir_0/pippenger.sws\"\n2008-05-11 22:47:55-0700 [-] Exception rendering:\n2008-05-11 22:47:55-0700 [-] Unhandled Error\n        Traceback (most recent call last):\n          File \"/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 609, in gotResult\n            _deferGenerator(g, deferred)\n          File \"/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 586, in _deferGenerator\n            deferred.callback(result)\n          File \"/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 242, in callback\n            self._startRunCallbacks(result)\n          File \"/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 307, in _startRunCallbacks\n            self._runCallbacks()\n        --- <exception caught here> ---\n          File \"/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 323, in _runCallbacks\n            self.result = callback(self.result, *args, **kw)\n          File \"/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/web2/resource.py\", line 230, in <lambda>\n            ).addCallback(lambda res: self.render(request))\n          File \"/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/twist.py\", line 326, in render\n            W = notebook.import_worksheet(filename, self.username)\n          File \"/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py\", line 800, in import_worksheet\n            return self._import_worksheet_sws(filename, owner)\n          File \"/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py\", line 882, in _import_worksheet_sws\n            worksheet_txt = open(text_filename).read()\n        exceptions.IOError: [Errno 2] No such file or directory: '/home/boothby/.sage/temp/eight/32244/dir_1/pippenger/worksheet.txt'\n```\n\n\nIt would be nice be able to recover this.  It isn't a problem (for me) to do this manually, and this is probably irrelevant to this ticket.",
    "created_at": "2008-05-12T06:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/637#issuecomment-3278",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Works, except when I tried to upload a rather old (from SD3) worksheet:


```
2008-05-11 22:47:55-0700 [-] cd "/home/boothby/.sage/temp/eight/32244/dir_1"; tar -jxf "/home/boothby/.sage/temp/eight/32244/dir_0/pippenger.sws"
2008-05-11 22:47:55-0700 [-] Exception rendering:
2008-05-11 22:47:55-0700 [-] Unhandled Error
        Traceback (most recent call last):
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 609, in gotResult
            _deferGenerator(g, deferred)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 586, in _deferGenerator
            deferred.callback(result)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 242, in callback
            self._startRunCallbacks(result)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 307, in _startRunCallbacks
            self._runCallbacks()
        --- <exception caught here> ---
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 323, in _runCallbacks
            self.result = callback(self.result, *args, **kw)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 230, in <lambda>
            ).addCallback(lambda res: self.render(request))
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 326, in render
            W = notebook.import_worksheet(filename, self.username)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py", line 800, in import_worksheet
            return self._import_worksheet_sws(filename, owner)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py", line 882, in _import_worksheet_sws
            worksheet_txt = open(text_filename).read()
        exceptions.IOError: [Errno 2] No such file or directory: '/home/boothby/.sage/temp/eight/32244/dir_1/pippenger/worksheet.txt'
```


It would be nice be able to recover this.  It isn't a problem (for me) to do this manually, and this is probably irrelevant to this ticket.



---

archive/issue_comments_003279.json:
```json
{
    "body": "Accidentally pasted this url to the description, not my comment:\n\n\nhttp://sage.math.washington.edu/home/boothby/pippenger.sws",
    "created_at": "2008-05-12T06:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/637#issuecomment-3279",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Accidentally pasted this url to the description, not my comment:


http://sage.math.washington.edu/home/boothby/pippenger.sws



---

archive/issue_comments_003280.json:
```json
{
    "body": "Attachment [sage-637-part2.patch](tarball://root/attachments/some-uuid/ticket637/sage-637-part2.patch) by @williamstein created at 2008-05-15 01:12:27",
    "created_at": "2008-05-15T01:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/637#issuecomment-3280",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-637-part2.patch](tarball://root/attachments/some-uuid/ticket637/sage-637-part2.patch) by @williamstein created at 2008-05-15 01:12:27



---

archive/issue_comments_003281.json:
```json
{
    "body": "This occurs whenever I try to upload from a URL:\n\n\n```\n2008-05-14 18:28:20-0700 [-] Unhandled Error\n        Traceback (most recent call last):\n          File \"/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 609, in gotResult\n            _deferGenerator(g, deferred)\n          File \"/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 586, in _deferGenerator\n            deferred.callback(result)\n          File \"/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 242, in callback\n            self._startRunCallbacks(result)\n          File \"/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 307, in _startRunCallbacks\n            self._runCallbacks()\n        --- <exception caught here> ---\n          File \"/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py\", line 323, in _runCallbacks\n            self.result = callback(self.result, *args, **kw)\n          File \"/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/web2/resource.py\", line 230, in <lambda>\n            ).addCallback(lambda res: self.render(request))\n          File \"/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/twist.py\", line 333, in render\n            os.unlink(filename)\n        exceptions.UnboundLocalError: local variable 'filename' referenced before assignment\n```\n",
    "created_at": "2008-05-15T02:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/637#issuecomment-3281",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

This occurs whenever I try to upload from a URL:


```
2008-05-14 18:28:20-0700 [-] Unhandled Error
        Traceback (most recent call last):
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 609, in gotResult
            _deferGenerator(g, deferred)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 586, in _deferGenerator
            deferred.callback(result)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 242, in callback
            self._startRunCallbacks(result)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 307, in _startRunCallbacks
            self._runCallbacks()
        --- <exception caught here> ---
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/internet/defer.py", line 323, in _runCallbacks
            self.result = callback(self.result, *args, **kw)
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/twisted/web2/resource.py", line 230, in <lambda>
            ).addCallback(lambda res: self.render(request))
          File "/home/boothby/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/server/notebook/twist.py", line 333, in render
            os.unlink(filename)
        exceptions.UnboundLocalError: local variable 'filename' referenced before assignment
```




---

archive/issue_comments_003282.json:
```json
{
    "body": "Attachment [sage-637-part3.patch](tarball://root/attachments/some-uuid/ticket637/sage-637-part3.patch) by @williamstein created at 2008-05-15 02:16:05",
    "created_at": "2008-05-15T02:16:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/637#issuecomment-3282",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-637-part3.patch](tarball://root/attachments/some-uuid/ticket637/sage-637-part3.patch) by @williamstein created at 2008-05-15 02:16:05



---

archive/issue_comments_003283.json:
```json
{
    "body": "works!",
    "created_at": "2008-05-15T03:17:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/637#issuecomment-3283",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

works!



---

archive/issue_comments_003284.json:
```json
{
    "body": "Merged all three patches in Sage 3.0.2.alpha1",
    "created_at": "2008-05-17T18:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/637#issuecomment-3284",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged all three patches in Sage 3.0.2.alpha1



---

archive/issue_events_000699.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-05-17T18:36:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/637#event-699"
}
```



---

archive/issue_comments_003285.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-17T18:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/637",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/637#issuecomment-3285",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
