# Issue 6251: LogoutResource in sage/server/simple/twist.py doesn't really log you out

archive/issues_006251.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @robertwb\n\nKeywords: simple server logout\n\nI'm using the simple server, and it seems like the logout command doesn't really log you out. From a regular Python (2.6) session:\n\n```\n>>> import urllib\n>>> def get_url(url): h = urllib.urlopen(url); data = h.read(); h.close(); return data \n... \n>>> print(get_url('http://localhost:8000/simple/login?username=admin&password=xxx'))\n{\n\"session\": \"515f64ef06471627e1d4a903ee921899\"\n}\n___S_A_G_E___\n\n>>> sess = \"515f64ef06471627e1d4a903ee921899\"\n>>> print(get_url('http://localhost:8000/simple/compute?session={0}&code=2*2'.format(sess)))\n{\n\"status\": \"done\",\n\"files\": [],\n\"cell_id\": 1\n}\n___S_A_G_E___\n\n4\n\n>>> print(get_url('http://localhost:8000/simple/logout?session={0}'.format(sess)))\n{\n\"session\": \"515f64ef06471627e1d4a903ee921899\"\n}\n___S_A_G_E___\n\n```\n\nBut you can still issue compute commands and have them evaluated. In the same Python session:\n\n```\n>>> print(get_url('http://localhost:8000/simple/compute?session={0}&code=3*3'.format(sess)))\n{\n\"status\": \"done\",\n\"files\": [],\n\"cell_id\": 3\n}\n___S_A_G_E___\n\n9\n\n```\nIn the LogoutResource class of twist.py, I see that we quit the worksheet and remove all the cells, but it's retaining some state -- note above that after we logout, the next compute command uses  cell 3. You never explicitly remove \"session\" from the sessions dictionary; is that something that should be done?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6251\n\n",
    "created_at": "2009-06-09T01:20:04Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "LogoutResource in sage/server/simple/twist.py doesn't really log you out",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6251",
    "user": "https://github.com/dandrake"
}
```
Assignee: boothby

CC:  @robertwb

Keywords: simple server logout

I'm using the simple server, and it seems like the logout command doesn't really log you out. From a regular Python (2.6) session:

```
>>> import urllib
>>> def get_url(url): h = urllib.urlopen(url); data = h.read(); h.close(); return data 
... 
>>> print(get_url('http://localhost:8000/simple/login?username=admin&password=xxx'))
{
"session": "515f64ef06471627e1d4a903ee921899"
}
___S_A_G_E___

>>> sess = "515f64ef06471627e1d4a903ee921899"
>>> print(get_url('http://localhost:8000/simple/compute?session={0}&code=2*2'.format(sess)))
{
"status": "done",
"files": [],
"cell_id": 1
}
___S_A_G_E___

4

>>> print(get_url('http://localhost:8000/simple/logout?session={0}'.format(sess)))
{
"session": "515f64ef06471627e1d4a903ee921899"
}
___S_A_G_E___

```

But you can still issue compute commands and have them evaluated. In the same Python session:

```
>>> print(get_url('http://localhost:8000/simple/compute?session={0}&code=3*3'.format(sess)))
{
"status": "done",
"files": [],
"cell_id": 3
}
___S_A_G_E___

9

```
In the LogoutResource class of twist.py, I see that we quit the worksheet and remove all the cells, but it's retaining some state -- note above that after we logout, the next compute command uses  cell 3. You never explicitly remove "session" from the sessions dictionary; is that something that should be done?


Issue created by migration from https://trac.sagemath.org/ticket/6251





---

archive/issue_comments_049825.json:
```json
{
    "body": "I should add a bit about why I'm concerned about this: I'm working on some SageTeX stuff that uses the simple server, and I had run maybe 20 tests and the server now had 20 running worksheets and was consuming tons of memory. I want to make sure that when you issue a logout command, the worksheet and session really are disposed of, so that we don't unncessarily use memory and resources.",
    "created_at": "2009-06-09T01:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6251#issuecomment-49825",
    "user": "https://github.com/dandrake"
}
```

I should add a bit about why I'm concerned about this: I'm working on some SageTeX stuff that uses the simple server, and I had run maybe 20 tests and the server now had 20 running worksheets and was consuming tons of memory. I want to make sure that when you issue a logout command, the worksheet and session really are disposed of, so that we don't unncessarily use memory and resources.



---

archive/issue_comments_049826.json:
```json
{
    "body": "Yes, this should be fixed. It's a security issue as well. I'm surprised the session is still good!",
    "created_at": "2009-06-09T04:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6251#issuecomment-49826",
    "user": "https://github.com/robertwb"
}
```

Yes, this should be fixed. It's a security issue as well. I'm surprised the session is still good!



---

archive/issue_comments_049827.json:
```json
{
    "body": "Attachment [trac_6251.patch](tarball://root/attachments/some-uuid/ticket6251/trac_6251.patch) by @dandrake created at 2009-06-09 07:23:46",
    "created_at": "2009-06-09T07:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6251#issuecomment-49827",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_6251.patch](tarball://root/attachments/some-uuid/ticket6251/trac_6251.patch) by @dandrake created at 2009-06-09 07:23:46



---

archive/issue_comments_049828.json:
```json
{
    "body": "I've attached one attempt at some kind of solution. I noticed that the SessionObject never gets deleted, so I thought I would just remove it from the \"sessions\" dictionary. This does make the session unavailable from the simple server, but I thought it might not properly get rid of the worksheet...but it seems like it does. Perhaps when the SessionObject gets deleted from the sessions dictionary, the worksheet and so on all get garbage collected?\n\nThe GC theory seems a bit plausible, especially since I noticed the line `sessions['test'] = session` in the file, which seems like some leftover debugging cruft...I deleted that line and things seem to work better, since now there isn't a spurious second reference to the session object.\n\nHere's a question: in the simple server, we create a worksheet, and to get rid of it, we simply delete its directory. Is that sufficient? My thinking is that it is, since we aren't creating the worksheet within the notebook, so there's no other record of the worksheet's existence; hence deleting the files removes all traces of the worksheet on disk. Is this correct?\n\nI've tested this some, and it seems to solve my problems. Please check this over!",
    "created_at": "2009-06-09T07:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6251#issuecomment-49828",
    "user": "https://github.com/dandrake"
}
```

I've attached one attempt at some kind of solution. I noticed that the SessionObject never gets deleted, so I thought I would just remove it from the "sessions" dictionary. This does make the session unavailable from the simple server, but I thought it might not properly get rid of the worksheet...but it seems like it does. Perhaps when the SessionObject gets deleted from the sessions dictionary, the worksheet and so on all get garbage collected?

The GC theory seems a bit plausible, especially since I noticed the line `sessions['test'] = session` in the file, which seems like some leftover debugging cruft...I deleted that line and things seem to work better, since now there isn't a spurious second reference to the session object.

Here's a question: in the simple server, we create a worksheet, and to get rid of it, we simply delete its directory. Is that sufficient? My thinking is that it is, since we aren't creating the worksheet within the notebook, so there's no other record of the worksheet's existence; hence deleting the files removes all traces of the worksheet on disk. Is this correct?

I've tested this some, and it seems to solve my problems. Please check this over!



---

archive/issue_comments_049829.json:
```json
{
    "body": "Actually, if you log into the notebook you will see these transient worksheets get created (or at least did at one point). Everything lives in the directory, but there may be pointers to it from elsewhere. I think when the notebook restarts it does more extensive cleanup though.",
    "created_at": "2009-06-09T08:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6251#issuecomment-49829",
    "user": "https://github.com/robertwb"
}
```

Actually, if you log into the notebook you will see these transient worksheets get created (or at least did at one point). Everything lives in the directory, but there may be pointers to it from elsewhere. I think when the notebook restarts it does more extensive cleanup though.



---

archive/issue_comments_049830.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> Actually, if you log into the notebook you will see these transient worksheets get created (or at least did at one point). Everything lives in the directory, but there may be pointers to it from elsewhere. I think when the notebook restarts it does more extensive cleanup though. \n\n\nI don't see the transient worksheets in the usual web notebook, and if load `nb.sobj` after running some sessions, I don't see any worksheets there (but I might have missed something). I've tested this on my own machine, sage.math, and bsd.math.\n\nThe \"further-stuff\" patch removes the nodoctest, since the file does pass doctests. It also adds the server to the reference manual and improves the documentation a bit. It doesn't have anything to do with fixing the issue in this ticket, but while we're there, we might as well fix some things up.",
    "created_at": "2009-06-09T09:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6251#issuecomment-49830",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:4 robertwb]:
> Actually, if you log into the notebook you will see these transient worksheets get created (or at least did at one point). Everything lives in the directory, but there may be pointers to it from elsewhere. I think when the notebook restarts it does more extensive cleanup though. 


I don't see the transient worksheets in the usual web notebook, and if load `nb.sobj` after running some sessions, I don't see any worksheets there (but I might have missed something). I've tested this on my own machine, sage.math, and bsd.math.

The "further-stuff" patch removes the nodoctest, since the file does pass doctests. It also adds the server to the reference manual and improves the documentation a bit. It doesn't have anything to do with fixing the issue in this ticket, but while we're there, we might as well fix some things up.



---

archive/issue_comments_049831.json:
```json
{
    "body": "Changing assignee from boothby to @dandrake.",
    "created_at": "2009-06-09T09:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6251#issuecomment-49831",
    "user": "https://github.com/dandrake"
}
```

Changing assignee from boothby to @dandrake.



---

archive/issue_comments_049832.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-09T09:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6251#issuecomment-49832",
    "user": "https://github.com/dandrake"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049833.json:
```json
{
    "body": "robertwb, can you review this? If this patch is good, I'd like to see it get into Sage very soon, so I can more publicly release my remote-sagetex script.",
    "created_at": "2009-06-15T07:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6251#issuecomment-49833",
    "user": "https://github.com/dandrake"
}
```

robertwb, can you review this? If this patch is good, I'd like to see it get into Sage very soon, so I can more publicly release my remote-sagetex script.



---

archive/issue_comments_049834.json:
```json
{
    "body": "One quick comment: in \"trac_6251-further-stuff.patch\", you don't need to add the file \"twist.rst\": it is autogenerated (as it says) -- it is created automatically because of the line you added to \"doc/en/reference/notebook.rst\".",
    "created_at": "2009-07-20T02:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6251#issuecomment-49834",
    "user": "https://github.com/jhpalmieri"
}
```

One quick comment: in "trac_6251-further-stuff.patch", you don't need to add the file "twist.rst": it is autogenerated (as it says) -- it is created automatically because of the line you added to "doc/en/reference/notebook.rst".



---

archive/issue_comments_049835.json:
```json
{
    "body": "Replying to [comment:7 jhpalmieri]:\n> One quick comment: in \"trac_6251-further-stuff.patch\", you don't need to add the file \"twist.rst\": it is autogenerated (as it says) -- it is created automatically because of the line you added to \"doc/en/reference/notebook.rst\".\n\n\nOkay, thanks. I still don't really know what I'm doing with the documentation system. I'll get an updated version of this patch up.",
    "created_at": "2009-07-20T05:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6251#issuecomment-49835",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:7 jhpalmieri]:
> One quick comment: in "trac_6251-further-stuff.patch", you don't need to add the file "twist.rst": it is autogenerated (as it says) -- it is created automatically because of the line you added to "doc/en/reference/notebook.rst".


Okay, thanks. I still don't really know what I'm doing with the documentation system. I'll get an updated version of this patch up.



---

archive/issue_comments_049836.json:
```json
{
    "body": "Positive review subject to removing twist.rst from the patch.",
    "created_at": "2009-07-26T02:19:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6251#issuecomment-49836",
    "user": "https://github.com/williamstein"
}
```

Positive review subject to removing twist.rst from the patch.



---

archive/issue_comments_049837.json:
```json
{
    "body": "Attachment [trac_6251-further-stuff.patch](tarball://root/attachments/some-uuid/ticket6251/trac_6251-further-stuff.patch) by @dandrake created at 2009-07-26 05:36:15",
    "created_at": "2009-07-26T05:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6251#issuecomment-49837",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_6251-further-stuff.patch](tarball://root/attachments/some-uuid/ticket6251/trac_6251-further-stuff.patch) by @dandrake created at 2009-07-26 05:36:15



---

archive/issue_comments_049838.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-29T12:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6251#issuecomment-49838",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_049839.json:
```json
{
    "body": "Merged both patches.",
    "created_at": "2009-07-29T12:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6251",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6251#issuecomment-49839",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged both patches.



---

archive/issue_events_014645.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-29T12:11:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6251",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6251#event-14645"
}
```
