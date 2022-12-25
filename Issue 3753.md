# Issue 3753: notebook -- change the default for nb.save('...')

archive/issues_003753.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein @mwhansen\n\n```\n\n\nHi,\n\nI also noticed there is a problem with \"nb.save()\". It assumes that\nthe current directory is \".sage\". So it saves the notebook object in a\nwrong place if you are not in \".sage\". I think this is a bug.\n\n\nKwankyu\n\n\t\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3753\n\n",
    "closed_at": "2009-11-19T23:30:27Z",
    "created_at": "2008-08-01T01:34:06Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook -- change the default for nb.save('...')",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3753",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

CC:  @williamstein @mwhansen

```


Hi,

I also noticed there is a problem with "nb.save()". It assumes that
the current directory is ".sage". So it saves the notebook object in a
wrong place if you are not in ".sage". I think this is a bug.


Kwankyu

	
```

Issue created by migration from https://trac.sagemath.org/ticket/3753





---

archive/issue_comments_026610.json:
```json
{
    "body": "I can't seem to confirm that this is the case. I added the method filename to the Notebook class and here's what I get:\n\n```\nnb = load('test/nb.sobj')\nsage: nb.filename()\n'test/nb.sobj'\n```\n\nLooking at the source code for Notebook.save() it appears to me that save() relies on self.__filename.",
    "created_at": "2008-08-03T17:56:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3753#issuecomment-26610",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I can't seem to confirm that this is the case. I added the method filename to the Notebook class and here's what I get:

```
nb = load('test/nb.sobj')
sage: nb.filename()
'test/nb.sobj'
```

Looking at the source code for Notebook.save() it appears to me that save() relies on self.__filename.



---

archive/issue_comments_026611.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3753#issuecomment-26611",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_026612.json:
```json
{
    "body": "This does not seem to be a problem anymore, especially noting the change to the Datastore backend. Can someone check this and close it if it is so?",
    "created_at": "2009-11-19T20:14:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3753#issuecomment-26612",
    "user": "https://github.com/TimDumol"
}
```

This does not seem to be a problem anymore, especially noting the change to the Datastore backend. Can someone check this and close it if it is so?



---

archive/issue_events_008603.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-11-19T23:30:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3753",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3753#event-8603"
}
```



---

archive/issue_comments_026613.json:
```json
{
    "body": "I agree timdumol -- there's no reason to save nb anymore so who cares what it does.",
    "created_at": "2009-11-19T23:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3753#issuecomment-26613",
    "user": "https://github.com/williamstein"
}
```

I agree timdumol -- there's no reason to save nb anymore so who cares what it does.



---

archive/issue_comments_026614.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2009-11-19T23:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3753",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3753#issuecomment-26614",
    "user": "https://github.com/williamstein"
}
```

Resolution: wontfix



---

archive/issue_events_008604.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-12-08T23:50:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3753",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3753#event-8604"
}
```
