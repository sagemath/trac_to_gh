# Issue 7483: notebook: weird pointless line

archive/issues_007483.json:
```json
{
    "body": "Assignee: boothby\n\nIn worksheet.py (at the end of `start_next_comp(self)`) in sagenb we have these lines:\n\n```\n        self.__comp_is_running = True\n        'exec _support_.preparse(base64.b64decode(\"%s\"))'%base64.b64encode(input)\n        self.sage().execute(input, os.path.abspath(self.data_directory()))\n```\n\n\nThat 'exec ' line in the middle is just sitting there making a string that is just discareded!?!?\n\nIssue created by migration from https://trac.sagemath.org/ticket/7483\n\n",
    "created_at": "2009-11-17T22:28:15Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "notebook: weird pointless line",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7483",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

In worksheet.py (at the end of `start_next_comp(self)`) in sagenb we have these lines:

```
        self.__comp_is_running = True
        'exec _support_.preparse(base64.b64decode("%s"))'%base64.b64encode(input)
        self.sage().execute(input, os.path.abspath(self.data_directory()))
```


That 'exec ' line in the middle is just sitting there making a string that is just discareded!?!?

Issue created by migration from https://trac.sagemath.org/ticket/7483





---

archive/issue_comments_063062.json:
```json
{
    "body": "I think I meant\n\n```\ninput = 'exec _support_.preparse(base64.b64decode(\"%s\"))'%base64.b64encode(input)\n```\n\nand to get rid of preparsing input at all done by the server.  In fact, I know for a fact I implemented things that way so that this wouldn't be broken:\n\n```\nimplicit_multiplication(True)\n///\nTraceback (most recent call last):\n...\nNotImplementedError: Implicit multiplication not implemented for the notebook.\n```\n\n\nBut now it seems to be broken again. \n\nI can only conclude that a serious mismerge or mangling has occurred to the code I originally wrote, since I definitely had the above working in an earlier version of sagenb.  \n\nHence, this ticket.",
    "created_at": "2009-11-17T22:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63062",
    "user": "https://github.com/williamstein"
}
```

I think I meant

```
input = 'exec _support_.preparse(base64.b64decode("%s"))'%base64.b64encode(input)
```

and to get rid of preparsing input at all done by the server.  In fact, I know for a fact I implemented things that way so that this wouldn't be broken:

```
implicit_multiplication(True)
///
Traceback (most recent call last):
...
NotImplementedError: Implicit multiplication not implemented for the notebook.
```


But now it seems to be broken again. 

I can only conclude that a serious mismerge or mangling has occurred to the code I originally wrote, since I definitely had the above working in an earlier version of sagenb.  

Hence, this ticket.



---

archive/issue_comments_063063.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-11-17T23:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63063",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_063064.json:
```json
{
    "body": "apply to the sagenb spkg",
    "created_at": "2009-11-18T00:35:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63064",
    "user": "https://github.com/williamstein"
}
```

apply to the sagenb spkg



---

archive/issue_comments_063065.json:
```json
{
    "body": "Attachment [sagenb_7483.patch](tarball://root/attachments/some-uuid/ticket7483/sagenb_7483.patch) by @williamstein created at 2009-11-18 00:35:45\n\napply to the core sage library",
    "created_at": "2009-11-18T00:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63065",
    "user": "https://github.com/williamstein"
}
```

Attachment [sagenb_7483.patch](tarball://root/attachments/some-uuid/ticket7483/sagenb_7483.patch) by @williamstein created at 2009-11-18 00:35:45

apply to the core sage library



---

archive/issue_comments_063066.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-18T00:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63066",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063067.json:
```json
{
    "body": "Attachment [sagelib-7483.patch](tarball://root/attachments/some-uuid/ticket7483/sagelib-7483.patch) by @williamstein created at 2009-11-18 00:35:52",
    "created_at": "2009-11-18T00:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63067",
    "user": "https://github.com/williamstein"
}
```

Attachment [sagelib-7483.patch](tarball://root/attachments/some-uuid/ticket7483/sagelib-7483.patch) by @williamstein created at 2009-11-18 00:35:52



---

archive/issue_comments_063068.json:
```json
{
    "body": "So the attached patch moves all the preparsing from the notebook server to the worksheet process.   I had thought I had made this change long ago, but I definitely hadn't.  It's *extremely* important from a security/robustness/speed/flexibility point of view.  Why?  Because it means the possibly time consuming and definitely _dangerous_ preparsing work gets pushed off to the worksheet processes, which will often be running on some remote virtual machines.  That's what we want!\n\nThis patch also makes it so the following are now fully supported in the notebook.  Note that they both used to not work at all:\n\n* implicit_multiplication -- turning on and off implicit multiplication\n\n* preparser -- turning on and off the preparser",
    "created_at": "2009-11-18T00:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63068",
    "user": "https://github.com/williamstein"
}
```

So the attached patch moves all the preparsing from the notebook server to the worksheet process.   I had thought I had made this change long ago, but I definitely hadn't.  It's *extremely* important from a security/robustness/speed/flexibility point of view.  Why?  Because it means the possibly time consuming and definitely _dangerous_ preparsing work gets pushed off to the worksheet processes, which will often be running on some remote virtual machines.  That's what we want!

This patch also makes it so the following are now fully supported in the notebook.  Note that they both used to not work at all:

* implicit_multiplication -- turning on and off implicit multiplication

* preparser -- turning on and off the preparser



---

archive/issue_comments_063069.json:
```json
{
    "body": "I've put a new sagenb spkg with just this patch (and the one from 7483) here:\n\n   http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.3.p1.spkg",
    "created_at": "2009-11-18T03:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63069",
    "user": "https://github.com/williamstein"
}
```

I've put a new sagenb spkg with just this patch (and the one from 7483) here:

   http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.3.p1.spkg



---

archive/issue_comments_063070.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-18T06:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63070",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063071.json:
```json
{
    "body": "The Selenium test results are unchanged in FF3.5.5 on Linux.  \n\n`make ptest` on sage.math passes.",
    "created_at": "2009-11-18T06:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63071",
    "user": "https://github.com/qed777"
}
```

The Selenium test results are unchanged in FF3.5.5 on Linux.  

`make ptest` on sage.math passes.



---

archive/issue_comments_063072.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-11-18T07:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63072",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_063073.json:
```json
{
    "body": "It seems that `load` and `save` are now broken in the notebook.\n\nWere `attach` and `detach` already broken in the notebook?",
    "created_at": "2009-11-18T07:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63073",
    "user": "https://github.com/qed777"
}
```

It seems that `load` and `save` are now broken in the notebook.

Were `attach` and `detach` already broken in the notebook?



---

archive/issue_comments_063074.json:
```json
{
    "body": "> It seems that load and save are now broken in the notebook.\n> Were attach and detach already broken in the notebook?\n\nNo, this broke them.  I'll fix the problem now.",
    "created_at": "2009-11-22T00:04:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63074",
    "user": "https://github.com/williamstein"
}
```

> It seems that load and save are now broken in the notebook.
> Were attach and detach already broken in the notebook?

No, this broke them.  I'll fix the problem now.



---

archive/issue_comments_063075.json:
```json
{
    "body": "Clarification: load and save still work on .sage files, but don't work on .py. This is related to #4474.  But I'll fix it here now, hopefully.",
    "created_at": "2009-11-22T00:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63075",
    "user": "https://github.com/williamstein"
}
```

Clarification: load and save still work on .sage files, but don't work on .py. This is related to #4474.  But I'll fix it here now, hopefully.



---

archive/issue_comments_063076.json:
```json
{
    "body": "OK, I went a bit crazy and spent 8 hours completely rewriting and unifying and refactoring all the load/save/attach code.  This is at #7514.  With that, the above mentioned issued is gone.",
    "created_at": "2009-11-22T08:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63076",
    "user": "https://github.com/williamstein"
}
```

OK, I went a bit crazy and spent 8 hours completely rewriting and unifying and refactoring all the load/save/attach code.  This is at #7514.  With that, the above mentioned issued is gone.



---

archive/issue_comments_063077.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-22T08:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63077",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063078.json:
```json
{
    "body": "Positive review, once #7514 passes.\n\nShould we also move \"docbrowser\" generation to a worksheet process?",
    "created_at": "2009-12-10T03:50:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63078",
    "user": "https://github.com/qed777"
}
```

Positive review, once #7514 passes.

Should we also move "docbrowser" generation to a worksheet process?



---

archive/issue_comments_063079.json:
```json
{
    "body": "> Should we also move \"docbrowser\" generation to a worksheet process? \n\nDefinitely!  The more that is done by worksheet processes, the better -- for scalability, security, etc.  Every spec of work done by the server is a potential speed and security problem.  The more that can be offloaded to worksheets, the better.",
    "created_at": "2009-12-10T18:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63079",
    "user": "https://github.com/williamstein"
}
```

> Should we also move "docbrowser" generation to a worksheet process? 

Definitely!  The more that is done by worksheet processes, the better -- for scalability, security, etc.  Every spec of work done by the server is a potential speed and security problem.  The more that can be offloaded to worksheets, the better.



---

archive/issue_comments_063080.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-01T07:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63080",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063081.json:
```json
{
    "body": "I've merged the sagelib patch in 4.3.1.alpha0",
    "created_at": "2010-01-03T22:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63081",
    "user": "https://github.com/mwhansen"
}
```

I've merged the sagelib patch in 4.3.1.alpha0



---

archive/issue_comments_063082.json:
```json
{
    "body": "I've merged this into sagenb-0.4.8.",
    "created_at": "2010-01-04T06:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63082",
    "user": "https://github.com/williamstein"
}
```

I've merged this into sagenb-0.4.8.



---

archive/issue_comments_063083.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T06:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63083",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_007713.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2010-01-04T06:34:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7483#event-7713"
}
```
