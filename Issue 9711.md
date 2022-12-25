# Issue 9711: sagenb notebook -- error when downloading worksheets in some cases involving non-ASCII characters

archive/issues_009711.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @ppurka @jasongrout @kini\n\nI hope this traceback from the serverlog on prep.sagenb.org will help me to debug and fix this:\n\n```\n\n2010-08-09 14:11:02-0700 [-] Exception rendering:\n2010-08-09 14:11:02-0700 [-] Unhandled Error\n        Traceback (most recent call last):          File \"/usr/local/sage-prep/local/lib/python/threading.py\", line 497, in __bootstrap\n            self.__bootstrap_inner()\n          File \"/usr/local/sage-prep/local/lib/python/threading.py\", line 525, in __bootstrap_inner            self.run()\n          File \"/usr/local/sage-prep/local/lib/python/threading.py\", line 477, in run\n            self.__target(*self.__args, **self.__kwargs)\n        --- <exception caught here> ---\n          File \"/usr/local/sage-prep/local/lib/python2.6/site-packages/twisted/python/threadpool.py\", line 210, in _worker\n            result = context.call(ctx, function, *args, **kwargs)\n          File \"/usr/local/sage-prep/local/lib/python2.6/site-packages/twisted/python/context.py\", line 59, in callWithContext\n            return self.currentContext().callWithContext(ctx, func, *args, **kw)\n          File \"/usr/local/sage-prep/local/lib/python2.6/site-packages/twisted/python/context.py\", line 37, in callWithContext\n            return func(*args,**kw)\n          File \"/usr/local/sage-prep/sagenb-0.8.p2/src/sagenb/sagenb/notebook/twist.py\", line 1448, in f\n            notebook.export_worksheet(worksheet.filename(), sws_filename)\n          File \"/usr/local/sage-prep/sagenb-0.8.p2/src/sagenb/sagenb/notebook/notebook.py\", line 983, in export_work\nsheet\n            S.export_worksheet(username, id_number, output_filename, title=title)\n          File \"/usr/local/sage-prep/sagenb-0.8.p2/src/sagenb/sagenb/storage/filesystem_storage.py\", line 362, in ex\nport_worksheet\n            open(worksheet_txt,'w').write(old_heading + open(worksheet_html).read())\n        exceptions.UnicodeDecodeError: 'ascii' codec can't decode byte 0xc2 in position 180: ordinal not in range(12\n8)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9711\n\n",
    "created_at": "2010-08-09T21:20:23Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sagenb notebook -- error when downloading worksheets in some cases involving non-ASCII characters",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9711",
    "user": "https://github.com/williamstein"
}
```
Assignee: jason, was

CC:  @ppurka @jasongrout @kini

I hope this traceback from the serverlog on prep.sagenb.org will help me to debug and fix this:

```

2010-08-09 14:11:02-0700 [-] Exception rendering:
2010-08-09 14:11:02-0700 [-] Unhandled Error
        Traceback (most recent call last):          File "/usr/local/sage-prep/local/lib/python/threading.py", line 497, in __bootstrap
            self.__bootstrap_inner()
          File "/usr/local/sage-prep/local/lib/python/threading.py", line 525, in __bootstrap_inner            self.run()
          File "/usr/local/sage-prep/local/lib/python/threading.py", line 477, in run
            self.__target(*self.__args, **self.__kwargs)
        --- <exception caught here> ---
          File "/usr/local/sage-prep/local/lib/python2.6/site-packages/twisted/python/threadpool.py", line 210, in _worker
            result = context.call(ctx, function, *args, **kwargs)
          File "/usr/local/sage-prep/local/lib/python2.6/site-packages/twisted/python/context.py", line 59, in callWithContext
            return self.currentContext().callWithContext(ctx, func, *args, **kw)
          File "/usr/local/sage-prep/local/lib/python2.6/site-packages/twisted/python/context.py", line 37, in callWithContext
            return func(*args,**kw)
          File "/usr/local/sage-prep/sagenb-0.8.p2/src/sagenb/sagenb/notebook/twist.py", line 1448, in f
            notebook.export_worksheet(worksheet.filename(), sws_filename)
          File "/usr/local/sage-prep/sagenb-0.8.p2/src/sagenb/sagenb/notebook/notebook.py", line 983, in export_work
sheet
            S.export_worksheet(username, id_number, output_filename, title=title)
          File "/usr/local/sage-prep/sagenb-0.8.p2/src/sagenb/sagenb/storage/filesystem_storage.py", line 362, in ex
port_worksheet
            open(worksheet_txt,'w').write(old_heading + open(worksheet_html).read())
        exceptions.UnicodeDecodeError: 'ascii' codec can't decode byte 0xc2 in position 180: ordinal not in range(12
8)
```


Issue created by migration from https://trac.sagemath.org/ticket/9711





---

archive/issue_comments_094486.json:
```json
{
    "body": "Attachment [trac_9711-unicode-worksheets.patch](tarball://root/attachments/some-uuid/ticket9711/trac_9711-unicode-worksheets.patch) by @TimDumol created at 2010-08-19 12:57:35\n\nWraps the arguments of the write call in an encoded_str() call.",
    "created_at": "2010-08-19T12:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9711#issuecomment-94486",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_9711-unicode-worksheets.patch](tarball://root/attachments/some-uuid/ticket9711/trac_9711-unicode-worksheets.patch) by @TimDumol created at 2010-08-19 12:57:35

Wraps the arguments of the write call in an encoded_str() call.



---

archive/issue_comments_094487.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-19T12:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9711#issuecomment-94487",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094488.json:
```json
{
    "body": "I have been unable to replicate the issue, even with rather exotic unicode characters (in the title and the body), but this should fix any possible problems (hopefully).",
    "created_at": "2010-08-19T12:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9711#issuecomment-94488",
    "user": "https://github.com/TimDumol"
}
```

I have been unable to replicate the issue, even with rather exotic unicode characters (in the title and the body), but this should fix any possible problems (hopefully).



---

archive/issue_comments_094489.json:
```json
{
    "body": "Please fill in your real name as Author.",
    "created_at": "2012-07-27T20:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9711#issuecomment-94489",
    "user": "https://github.com/jdemeyer"
}
```

Please fill in your real name as Author.



---

archive/issue_comments_094490.json:
```json
{
    "body": "I think this should be closed. Codec related issues should be long gone, especially with the internationalization changes that have occurred since this.",
    "created_at": "2012-07-28T04:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9711#issuecomment-94490",
    "user": "https://github.com/TimDumol"
}
```

I think this should be closed. Codec related issues should be long gone, especially with the internationalization changes that have occurred since this.



---

archive/issue_comments_094491.json:
```json
{
    "body": "If this is still valid, [the relevant code](https://github.com/sagemath/sagenb/blob/master/sagenb/storage/filesystem_storage.py#L462) has changed slightly, so this wouldn't apply.  Also, we should probably create a pull request.\n\nOr, as Tim suggests, if not, we could indeed close this.  It's unfortunate William didn't attach a sample sws :(  I'd go with Tim, though I think that we should have at least one current sagenb guru also confirm his statement.",
    "created_at": "2013-06-11T16:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9711#issuecomment-94491",
    "user": "https://github.com/kcrisman"
}
```

If this is still valid, [the relevant code](https://github.com/sagemath/sagenb/blob/master/sagenb/storage/filesystem_storage.py#L462) has changed slightly, so this wouldn't apply.  Also, we should probably create a pull request.

Or, as Tim suggests, if not, we could indeed close this.  It's unfortunate William didn't attach a sample sws :(  I'd go with Tim, though I think that we should have at least one current sagenb guru also confirm his statement.



---

archive/issue_events_024289.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2013-06-11T16:52:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9711",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9711#event-24289"
}
```



---

archive/issue_comments_094492.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2013-06-11T16:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9711#issuecomment-94492",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_094493.json:
```json
{
    "body": "I know I fixed a lot of issues involving errors like this last year.",
    "created_at": "2013-06-11T16:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9711#issuecomment-94493",
    "user": "https://github.com/jasongrout"
}
```

I know I fixed a lot of issues involving errors like this last year.



---

archive/issue_comments_094494.json:
```json
{
    "body": "This is now\n[SageNB issue 410: Downloading worksheets can fail with non-ASCII characters](https://github.com/sagemath/sagenb/issues/410)",
    "created_at": "2016-08-30T13:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9711#issuecomment-94494",
    "user": "https://github.com/slel"
}
```

This is now
[SageNB issue 410: Downloading worksheets can fail with non-ASCII characters](https://github.com/sagemath/sagenb/issues/410)



---

archive/issue_comments_094495.json:
```json
{
    "body": "Attachment [testdoc3.sws](tarball://root/attachments/some-uuid/ticket9711/testdoc3.sws) by @fchapoton created at 2017-07-25 07:30:52",
    "created_at": "2017-07-25T07:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9711#issuecomment-94495",
    "user": "https://github.com/fchapoton"
}
```

Attachment [testdoc3.sws](tarball://root/attachments/some-uuid/ticket9711/testdoc3.sws) by @fchapoton created at 2017-07-25 07:30:52



---

archive/issue_comments_094496.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2018-08-14T17:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9711#issuecomment-94496",
    "user": "https://github.com/embray"
}
```

Resolution: worksforme



---

archive/issue_events_024290.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2018-08-14T17:16:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9711",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9711#event-24290"
}
```



---

archive/issue_comments_094497.json:
```json
{
    "body": "Appears to be fixed in SageNB; see the upstream issue.",
    "created_at": "2018-08-14T17:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9711#issuecomment-94497",
    "user": "https://github.com/embray"
}
```

Appears to be fixed in SageNB; see the upstream issue.
