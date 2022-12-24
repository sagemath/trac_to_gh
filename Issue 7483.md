# Issue 7483: notebook: weird pointless line

archive/issues_007483.json:
```json
{
    "body": "Assignee: boothby\n\nIn worksheet.py (at the end of `start_next_comp(self)`) in sagenb we have these lines:\n\n```\n        self.__comp_is_running = True\n        'exec _support_.preparse(base64.b64decode(\"%s\"))'%base64.b64encode(input)\n        self.sage().execute(input, os.path.abspath(self.data_directory()))\n```\n\n\nThat 'exec ' line in the middle is just sitting there making a string that is just discareded!?!?\n\nIssue created by migration from https://trac.sagemath.org/ticket/7483\n\n",
    "created_at": "2009-11-17T22:28:15Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook: weird pointless line",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7483",
    "user": "was"
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

archive/issue_comments_063177.json:
```json
{
    "body": "I think I meant\n\n```\ninput = 'exec _support_.preparse(base64.b64decode(\"%s\"))'%base64.b64encode(input)\n```\n\nand to get rid of preparsing input at all done by the server.  In fact, I know for a fact I implemented things that way so that this wouldn't be broken:\n\n```\nimplicit_multiplication(True)\n///\nTraceback (most recent call last):\n...\nNotImplementedError: Implicit multiplication not implemented for the notebook.\n```\n\n\nBut now it seems to be broken again. \n\nI can only conclude that a serious mismerge or mangling has occurred to the code I originally wrote, since I definitely had the above working in an earlier version of sagenb.  \n\nHence, this ticket.",
    "created_at": "2009-11-17T22:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63177",
    "user": "was"
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

archive/issue_comments_063178.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-11-17T23:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63178",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_063179.json:
```json
{
    "body": "apply to the sagenb spkg",
    "created_at": "2009-11-18T00:35:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63179",
    "user": "was"
}
```

apply to the sagenb spkg



---

archive/issue_comments_063180.json:
```json
{
    "body": "Attachment [sagenb_7483.patch](tarball://root/attachments/some-uuid/ticket7483/sagenb_7483.patch) by was created at 2009-11-18 00:35:45\n\napply to the core sage library",
    "created_at": "2009-11-18T00:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63180",
    "user": "was"
}
```

Attachment [sagenb_7483.patch](tarball://root/attachments/some-uuid/ticket7483/sagenb_7483.patch) by was created at 2009-11-18 00:35:45

apply to the core sage library



---

archive/issue_comments_063181.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-18T00:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63181",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063182.json:
```json
{
    "body": "Attachment [sagelib-7483.patch](tarball://root/attachments/some-uuid/ticket7483/sagelib-7483.patch) by was created at 2009-11-18 00:35:52",
    "created_at": "2009-11-18T00:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63182",
    "user": "was"
}
```

Attachment [sagelib-7483.patch](tarball://root/attachments/some-uuid/ticket7483/sagelib-7483.patch) by was created at 2009-11-18 00:35:52



---

archive/issue_comments_063183.json:
```json
{
    "body": "So the attached patch moves all the preparsing from the notebook server to the worksheet process.   I had thought I had made this change long ago, but I definitely hadn't.  It's *extremely* important from a security/robustness/speed/flexibility point of view.  Why?  Because it means the possibly time consuming and definitely _dangerous_ preparsing work gets pushed off to the worksheet processes, which will often be running on some remote virtual machines.  That's what we want!\n\nThis patch also makes it so the following are now fully supported in the notebook.  Note that they both used to not work at all:\n\n* implicit_multiplication -- turning on and off implicit multiplication\n\n* preparser -- turning on and off the preparser",
    "created_at": "2009-11-18T00:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63183",
    "user": "was"
}
```

So the attached patch moves all the preparsing from the notebook server to the worksheet process.   I had thought I had made this change long ago, but I definitely hadn't.  It's *extremely* important from a security/robustness/speed/flexibility point of view.  Why?  Because it means the possibly time consuming and definitely _dangerous_ preparsing work gets pushed off to the worksheet processes, which will often be running on some remote virtual machines.  That's what we want!

This patch also makes it so the following are now fully supported in the notebook.  Note that they both used to not work at all:

* implicit_multiplication -- turning on and off implicit multiplication

* preparser -- turning on and off the preparser



---

archive/issue_comments_063184.json:
```json
{
    "body": "I've put a new sagenb spkg with just this patch (and the one from 7483) here:\n\n   http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.3.p1.spkg",
    "created_at": "2009-11-18T03:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63184",
    "user": "was"
}
```

I've put a new sagenb spkg with just this patch (and the one from 7483) here:

   http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.3.p1.spkg



---

archive/issue_comments_063185.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-18T06:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63185",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063186.json:
```json
{
    "body": "The Selenium test results are unchanged in FF3.5.5 on Linux.  \n\n`make ptest` on sage.math passes.",
    "created_at": "2009-11-18T06:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63186",
    "user": "mpatel"
}
```

The Selenium test results are unchanged in FF3.5.5 on Linux.  

`make ptest` on sage.math passes.



---

archive/issue_comments_063187.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-11-18T07:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63187",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_063188.json:
```json
{
    "body": "It seems that `load` and `save` are now broken in the notebook.\n\nWere `attach` and `detach` already broken in the notebook?",
    "created_at": "2009-11-18T07:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63188",
    "user": "mpatel"
}
```

It seems that `load` and `save` are now broken in the notebook.

Were `attach` and `detach` already broken in the notebook?



---

archive/issue_comments_063189.json:
```json
{
    "body": "> It seems that load and save are now broken in the notebook.\n> Were attach and detach already broken in the notebook?\n\nNo, this broke them.  I'll fix the problem now.",
    "created_at": "2009-11-22T00:04:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63189",
    "user": "was"
}
```

> It seems that load and save are now broken in the notebook.
> Were attach and detach already broken in the notebook?

No, this broke them.  I'll fix the problem now.



---

archive/issue_comments_063190.json:
```json
{
    "body": "Clarification: load and save still work on .sage files, but don't work on .py. This is related to #4474.  But I'll fix it here now, hopefully.",
    "created_at": "2009-11-22T00:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63190",
    "user": "was"
}
```

Clarification: load and save still work on .sage files, but don't work on .py. This is related to #4474.  But I'll fix it here now, hopefully.



---

archive/issue_comments_063191.json:
```json
{
    "body": "OK, I went a bit crazy and spent 8 hours completely rewriting and unifying and refactoring all the load/save/attach code.  This is at #7514.  With that, the above mentioned issued is gone.",
    "created_at": "2009-11-22T08:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63191",
    "user": "was"
}
```

OK, I went a bit crazy and spent 8 hours completely rewriting and unifying and refactoring all the load/save/attach code.  This is at #7514.  With that, the above mentioned issued is gone.



---

archive/issue_comments_063192.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-22T08:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63192",
    "user": "was"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063193.json:
```json
{
    "body": "Positive review, once #7514 passes.\n\nShould we also move \"docbrowser\" generation to a worksheet process?",
    "created_at": "2009-12-10T03:50:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63193",
    "user": "mpatel"
}
```

Positive review, once #7514 passes.

Should we also move "docbrowser" generation to a worksheet process?



---

archive/issue_comments_063194.json:
```json
{
    "body": "> Should we also move \"docbrowser\" generation to a worksheet process? \n\nDefinitely!  The more that is done by worksheet processes, the better -- for scalability, security, etc.  Every spec of work done by the server is a potential speed and security problem.  The more that can be offloaded to worksheets, the better.",
    "created_at": "2009-12-10T18:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63194",
    "user": "was"
}
```

> Should we also move "docbrowser" generation to a worksheet process? 

Definitely!  The more that is done by worksheet processes, the better -- for scalability, security, etc.  Every spec of work done by the server is a potential speed and security problem.  The more that can be offloaded to worksheets, the better.



---

archive/issue_comments_063195.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-01T07:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63195",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063196.json:
```json
{
    "body": "I've merged the sagelib patch in 4.3.1.alpha0",
    "created_at": "2010-01-03T22:31:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63196",
    "user": "mhansen"
}
```

I've merged the sagelib patch in 4.3.1.alpha0



---

archive/issue_comments_063197.json:
```json
{
    "body": "I've merged this into sagenb-0.4.8.",
    "created_at": "2010-01-04T06:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63197",
    "user": "was"
}
```

I've merged this into sagenb-0.4.8.



---

archive/issue_comments_063198.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T06:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7483#issuecomment-63198",
    "user": "was"
}
```

Resolution: fixed
