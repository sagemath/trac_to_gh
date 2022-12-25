# Issue 7787: Use a javascript minifier instead of a packer for sagenb

archive/issues_007787.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @fchapoton\n\nA minifier is safer (less likely to cause errors), is faster (no need for client-side to unpack), and smaller (with gzip).\n\nGoogle has reimplemented Douglas Crockford's `jsmin.py` with a BSD License for its V8 engine. It is available here:\n\nhttp://code.google.com/p/v8/source/browse/branches/bleeding_edge/tools/jsmin.py\n\nIssue created by migration from https://trac.sagemath.org/ticket/7787\n\n",
    "created_at": "2009-12-29T10:20:28Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Use a javascript minifier instead of a packer for sagenb",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7787",
    "user": "https://github.com/TimDumol"
}
```
Assignee: @williamstein

CC:  @fchapoton

A minifier is safer (less likely to cause errors), is faster (no need for client-side to unpack), and smaller (with gzip).

Google has reimplemented Douglas Crockford's `jsmin.py` with a BSD License for its V8 engine. It is available here:

http://code.google.com/p/v8/source/browse/branches/bleeding_edge/tools/jsmin.py

Issue created by migration from https://trac.sagemath.org/ticket/7787





---

archive/issue_comments_067087.json:
```json
{
    "body": "Attachment [trac_7787-sagenb-js-minify.patch](tarball://root/attachments/some-uuid/ticket7787/trac_7787-sagenb-js-minify.patch) by @TimDumol created at 2009-12-29 10:34:02\n\nAdds Google's jsmin.py",
    "created_at": "2009-12-29T10:34:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67087",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7787-sagenb-js-minify.patch](tarball://root/attachments/some-uuid/ticket7787/trac_7787-sagenb-js-minify.patch) by @TimDumol created at 2009-12-29 10:34:02

Adds Google's jsmin.py



---

archive/issue_comments_067088.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-29T10:34:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67088",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067089.json:
```json
{
    "body": "Attachment [trac_7787-sagenb-js-minify.2.patch](tarball://root/attachments/some-uuid/ticket7787/trac_7787-sagenb-js-minify.2.patch) by @TimDumol created at 2009-12-29 10:37:45\n\nReplaces JavaScriptCompressor with JavaScriptMinifier",
    "created_at": "2009-12-29T10:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67089",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7787-sagenb-js-minify.2.patch](tarball://root/attachments/some-uuid/ticket7787/trac_7787-sagenb-js-minify.2.patch) by @TimDumol created at 2009-12-29 10:37:45

Replaces JavaScriptCompressor with JavaScriptMinifier



---

archive/issue_comments_067090.json:
```json
{
    "body": "Attachment [trac_7787-sagenb-js-minify.3.patch](tarball://root/attachments/some-uuid/ticket7787/trac_7787-sagenb-js-minify.3.patch) by @TimDumol created at 2009-12-29 10:40:53\n\nAdds Google's jsmin.py. Apply this patch alone.",
    "created_at": "2009-12-29T10:40:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67090",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7787-sagenb-js-minify.3.patch](tarball://root/attachments/some-uuid/ticket7787/trac_7787-sagenb-js-minify.3.patch) by @TimDumol created at 2009-12-29 10:40:53

Adds Google's jsmin.py. Apply this patch alone.



---

archive/issue_comments_067091.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-29T15:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67091",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067092.json:
```json
{
    "body": "Google's `jsmin.py` causes failures (\"//\" in a string deletes the rest of the line), and does not remove unneeded lines.",
    "created_at": "2009-12-29T15:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67092",
    "user": "https://github.com/TimDumol"
}
```

Google's `jsmin.py` causes failures ("//" in a string deletes the rest of the line), and does not remove unneeded lines.



---

archive/issue_events_018619.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7787#event-18619"
}
```



---

archive/issue_events_018620.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7787#event-18620"
}
```



---

archive/issue_events_018621.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7787#event-18621"
}
```



---

archive/issue_events_018622.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7787#event-18622"
}
```



---

archive/issue_events_018623.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7787#event-18623"
}
```



---

archive/issue_events_018624.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7787#event-18624"
}
```



---

archive/issue_events_018625.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7787#event-18625"
}
```



---

archive/issue_comments_067093.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67093",
    "user": "https://github.com/mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_events_018626.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-08-18T00:36:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7787#event-18626"
}
```



---

archive/issue_events_018627.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-08-18T00:36:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7787#event-18627"
}
```



---

archive/issue_comments_067094.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67094",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067095.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-19T08:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7787#issuecomment-67095",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_events_018628.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-08-19T08:53:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7787",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7787#event-18628"
}
```
