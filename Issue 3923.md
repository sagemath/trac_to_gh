# Issue 3923: [with patch, not ready for review] notebook -- convert existing templates to Jinja templates

archive/issues_003923.json:
```json
{
    "body": "Assignee: boothby\n\nRequires the Jinja Template Engine http://jinja.pocoo.org/2/\n\nIssue created by migration from https://trac.sagemath.org/ticket/3923\n\n",
    "created_at": "2008-08-22T00:11:17Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "[with patch, not ready for review] notebook -- convert existing templates to Jinja templates",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3923",
    "user": "TimothyClemans"
}
```
Assignee: boothby

Requires the Jinja Template Engine http://jinja.pocoo.org/2/

Issue created by migration from https://trac.sagemath.org/ticket/3923





---

archive/issue_comments_028064.json:
```json
{
    "body": "Attachment [sage-3923_1.patch](tarball://root/attachments/some-uuid/ticket3923/sage-3923_1.patch) by TimothyClemans created at 2008-08-22 00:16:46",
    "created_at": "2008-08-22T00:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3923#issuecomment-28064",
    "user": "TimothyClemans"
}
```

Attachment [sage-3923_1.patch](tarball://root/attachments/some-uuid/ticket3923/sage-3923_1.patch) by TimothyClemans created at 2008-08-22 00:16:46



---

archive/issue_comments_028065.json:
```json
{
    "body": "Attachment [extcode-3923_1.patch](tarball://root/attachments/some-uuid/ticket3923/extcode-3923_1.patch) by TimothyClemans created at 2008-08-23 17:25:29",
    "created_at": "2008-08-23T17:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3923#issuecomment-28065",
    "user": "TimothyClemans"
}
```

Attachment [extcode-3923_1.patch](tarball://root/attachments/some-uuid/ticket3923/extcode-3923_1.patch) by TimothyClemans created at 2008-08-23 17:25:29



---

archive/issue_comments_028066.json:
```json
{
    "body": "Attachment [sage-3923_2.patch](tarball://root/attachments/some-uuid/ticket3923/sage-3923_2.patch) by TimothyClemans created at 2008-08-23 17:26:03",
    "created_at": "2008-08-23T17:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3923#issuecomment-28066",
    "user": "TimothyClemans"
}
```

Attachment [sage-3923_2.patch](tarball://root/attachments/some-uuid/ticket3923/sage-3923_2.patch) by TimothyClemans created at 2008-08-23 17:26:03



---

archive/issue_comments_028067.json:
```json
{
    "body": "Attachment [sage-3923_3.patch](tarball://root/attachments/some-uuid/ticket3923/sage-3923_3.patch) by TimothyClemans created at 2008-08-23 17:53:41\n\nremoves old files",
    "created_at": "2008-08-23T17:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3923#issuecomment-28067",
    "user": "TimothyClemans"
}
```

Attachment [sage-3923_3.patch](tarball://root/attachments/some-uuid/ticket3923/sage-3923_3.patch) by TimothyClemans created at 2008-08-23 17:53:41

removes old files



---

archive/issue_comments_028068.json:
```json
{
    "body": "Attachment [extcode-3923_3.patch](tarball://root/attachments/some-uuid/ticket3923/extcode-3923_3.patch) by TimothyClemans created at 2008-08-23 17:54:06",
    "created_at": "2008-08-23T17:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3923#issuecomment-28068",
    "user": "TimothyClemans"
}
```

Attachment [extcode-3923_3.patch](tarball://root/attachments/some-uuid/ticket3923/extcode-3923_3.patch) by TimothyClemans created at 2008-08-23 17:54:06



---

archive/issue_comments_028069.json:
```json
{
    "body": "I think that this is not ready for review until Jinja is in Sage, if it ever gets into Sage.",
    "created_at": "2008-09-24T11:04:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3923#issuecomment-28069",
    "user": "malb"
}
```

I think that this is not ready for review until Jinja is in Sage, if it ever gets into Sage.



---

archive/issue_comments_028070.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n> I think that this is not ready for review until Jinja is in Sage, if it ever gets into Sage.\n\nJinja is required for the ReST transition of the documentation, so I am very bullish that it will get in. In total the ReST tool chain in 4 spkg weights in at 2MB compressed total and since it is a large improvement over the current situation with latex2html I think it will happen soon. Mike Hansen is pretty much ready to go here and it seems likely that those changes will be in 3.2.x if not 3.2 (assuming the spkgs get voted in obviously :))\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T11:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3923#issuecomment-28070",
    "user": "mabshoff"
}
```

Replying to [comment:2 malb]:
> I think that this is not ready for review until Jinja is in Sage, if it ever gets into Sage.

Jinja is required for the ReST transition of the documentation, so I am very bullish that it will get in. In total the ReST tool chain in 4 spkg weights in at 2MB compressed total and since it is a large improvement over the current situation with latex2html I think it will happen soon. Mike Hansen is pretty much ready to go here and it seems likely that those changes will be in 3.2.x if not 3.2 (assuming the spkgs get voted in obviously :))

Cheers,

Michael



---

archive/issue_comments_028071.json:
```json
{
    "body": "Replying to [comment:3 mabshoff]:\n> Jinja is required for the ReST transition of the documentation, so I am very bullish that it will get in. In total the ReST tool chain in 4 spkg weights in at 2MB compressed total and since it is a large improvement over the current situation with latex2html I think it will happen soon. Mike Hansen is pretty much ready to go here and it seems likely that those changes will be in 3.2.x if not 3.2 (assuming the spkgs get voted in obviously :))\n\nDon't get me wrong, I'm all in favor of Jinja getting in, but this still needs formal verification. Also, IIRC there is the issue of Jinja v1 (ReST) vs. v2 (this patch)?",
    "created_at": "2008-09-24T11:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3923#issuecomment-28071",
    "user": "malb"
}
```

Replying to [comment:3 mabshoff]:
> Jinja is required for the ReST transition of the documentation, so I am very bullish that it will get in. In total the ReST tool chain in 4 spkg weights in at 2MB compressed total and since it is a large improvement over the current situation with latex2html I think it will happen soon. Mike Hansen is pretty much ready to go here and it seems likely that those changes will be in 3.2.x if not 3.2 (assuming the spkgs get voted in obviously :))

Don't get me wrong, I'm all in favor of Jinja getting in, but this still needs formal verification. Also, IIRC there is the issue of Jinja v1 (ReST) vs. v2 (this patch)?



---

archive/issue_comments_028072.json:
```json
{
    "body": "Replying to [comment:4 malb]:\n\n> Don't get me wrong, I'm all in favor of Jinja getting in, but this still needs formal verification. Also, IIRC there is the issue of Jinja v1 (ReST) vs. v2 (this patch)?\n\nSure, I agree. Mike has figured out IIRC that both Jinja and ReST and this code plays well together with Jinja v2. Timothy should have actually checked with [sage-devel] formally before going off into the sunset and code up loads of features that the code in question would actually be merged. But this story is likely to have a happy end :). Hopefully everyone involved here will learn a lesson from this.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T11:29:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3923#issuecomment-28072",
    "user": "mabshoff"
}
```

Replying to [comment:4 malb]:

> Don't get me wrong, I'm all in favor of Jinja getting in, but this still needs formal verification. Also, IIRC there is the issue of Jinja v1 (ReST) vs. v2 (this patch)?

Sure, I agree. Mike has figured out IIRC that both Jinja and ReST and this code plays well together with Jinja v2. Timothy should have actually checked with [sage-devel] formally before going off into the sunset and code up loads of features that the code in question would actually be merged. But this story is likely to have a happy end :). Hopefully everyone involved here will learn a lesson from this.

Cheers,

Michael



---

archive/issue_comments_028073.json:
```json
{
    "body": "Changing assignee from boothby to mhansen.",
    "created_at": "2008-10-23T23:15:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3923#issuecomment-28073",
    "user": "mhansen"
}
```

Changing assignee from boothby to mhansen.



---

archive/issue_comments_028074.json:
```json
{
    "body": "Attachment [trac_3923.patch](tarball://root/attachments/some-uuid/ticket3923/trac_3923.patch) by mhansen created at 2008-10-23 23:15:22\n\nI rebased the patches against 3.2.alpha0, moved the templates from extcode to sage/server/notebook/templates/, and changed the imports to use Jinja1 instead of Jinja2.\n\nApply only trac_3923.patch.",
    "created_at": "2008-10-23T23:15:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3923#issuecomment-28074",
    "user": "mhansen"
}
```

Attachment [trac_3923.patch](tarball://root/attachments/some-uuid/ticket3923/trac_3923.patch) by mhansen created at 2008-10-23 23:15:22

I rebased the patches against 3.2.alpha0, moved the templates from extcode to sage/server/notebook/templates/, and changed the imports to use Jinja1 instead of Jinja2.

Apply only trac_3923.patch.



---

archive/issue_comments_028075.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-23T23:15:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3923#issuecomment-28075",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_028076.json:
```json
{
    "body": "Merged trac_3923.patch in Sage 3.2.alpha1",
    "created_at": "2008-10-25T22:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3923#issuecomment-28076",
    "user": "mabshoff"
}
```

Merged trac_3923.patch in Sage 3.2.alpha1



---

archive/issue_comments_028077.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-25T22:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3923",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3923#issuecomment-28077",
    "user": "mabshoff"
}
```

Resolution: fixed
