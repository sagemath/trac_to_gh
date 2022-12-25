# Issue 3475: [with patch, needs review] setup.py was missing jquery.form.js, upgrade to latest version of jquery (1.2.6) and jquery.form

archive/issues_003475.json:
```json
{
    "body": "Assignee: @williamstein\n\njquery.form.js somehow got dropped from setup.py, which is needed for the web interface, it does *NOT* function correctly without the proper jquery plugin. \n\nThis patch also upgrades jquery, jquery.form to the latest version. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3475\n\n",
    "created_at": "2008-06-19T21:47:07Z",
    "labels": [
        "component: dsage",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, needs review] setup.py was missing jquery.form.js, upgrade to latest version of jquery (1.2.6) and jquery.form",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3475",
    "user": "https://github.com/yqiang"
}
```
Assignee: @williamstein

jquery.form.js somehow got dropped from setup.py, which is needed for the web interface, it does *NOT* function correctly without the proper jquery plugin. 

This patch also upgrades jquery, jquery.form to the latest version. 

Issue created by migration from https://trac.sagemath.org/ticket/3475





---

archive/issue_comments_024436.json:
```json
{
    "body": "Attachment [3475_dsage_js.patch](tarball://root/attachments/some-uuid/ticket3475/3475_dsage_js.patch) by @yqiang created at 2008-06-19 21:51:06\n\nrenamed patch file to include bug #",
    "created_at": "2008-06-19T21:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3475#issuecomment-24436",
    "user": "https://github.com/yqiang"
}
```

Attachment [3475_dsage_js.patch](tarball://root/attachments/some-uuid/ticket3475/3475_dsage_js.patch) by @yqiang created at 2008-06-19 21:51:06

renamed patch file to include bug #



---

archive/issue_comments_024437.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-06-20T04:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3475#issuecomment-24437",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_024438.json:
```json
{
    "body": "Yi,\n\ncan you split off the \"missing jquery.form.js from setup.py\" part from the jquery update? The copy part of the patch is trivial to review and will get into 3.0.4, I am not so sure about the jquery update since that should be done by somebody who works on the notebook and withb `@`interact for example.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-02T20:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3475#issuecomment-24438",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yi,

can you split off the "missing jquery.form.js from setup.py" part from the jquery update? The copy part of the patch is trivial to review and will get into 3.0.4, I am not so sure about the jquery update since that should be done by somebody who works on the notebook and withb `@`interact for example.

Cheers,

Michael



---

archive/issue_comments_024439.json:
```json
{
    "body": "Michael,\n\nThe jquery update is a non issue since AFAIK the notebook does not use the jquery version dsage uses. \n\nIt uses the one found here:\n\niapetus:~/Software/sage-3.0.3.rc0/data/extcode/notebook/javascript/jquery > \n\nMaybe in the future we can simply provide one version, but that is another issue. Let me know if this resolves your complaint.",
    "created_at": "2008-07-02T21:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3475#issuecomment-24439",
    "user": "https://github.com/yqiang"
}
```

Michael,

The jquery update is a non issue since AFAIK the notebook does not use the jquery version dsage uses. 

It uses the one found here:

iapetus:~/Software/sage-3.0.3.rc0/data/extcode/notebook/javascript/jquery > 

Maybe in the future we can simply provide one version, but that is another issue. Let me know if this resolves your complaint.



---

archive/issue_comments_024440.json:
```json
{
    "body": "I agree that there are two copies of jquery and we can upgrade DSage's copy without having any repercussions on the notebook one. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-03T05:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3475#issuecomment-24440",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I agree that there are two copies of jquery and we can upgrade DSage's copy without having any repercussions on the notebook one. Positive review.

Cheers,

Michael



---

archive/issue_comments_024441.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-03T05:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3475#issuecomment-24441",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024442.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-03T05:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3475#issuecomment-24442",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha2



---

archive/issue_events_003695.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-07-03T05:03:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3475",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3475#event-3695"
}
```
