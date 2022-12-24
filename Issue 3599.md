# Issue 3599: Longer slider and labels on sliders

archive/issues_003599.json:
```json
{
    "body": "Assignee: itolkov\n\nSlider update:\n\n* Sliders are now version 3, which is similar to current version 1, but longer\n\n* Label to the right of slider containing the current slider value (string representation), which is updated dynamically\n\n* User can hide label with \"display_value=False\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/3599\n\n",
    "created_at": "2008-07-08T00:28:26Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "title": "Longer slider and labels on sliders",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3599",
    "user": "itolkov"
}
```
Assignee: itolkov

Slider update:

* Sliders are now version 3, which is similar to current version 1, but longer

* Label to the right of slider containing the current slider value (string representation), which is updated dynamically

* User can hide label with "display_value=False".

Issue created by migration from https://trac.sagemath.org/ticket/3599





---

archive/issue_comments_025424.json:
```json
{
    "body": "Attachment [trac3599_extcode_1.patch](tarball://root/attachments/some-uuid/ticket3599/trac3599_extcode_1.patch) by itolkov created at 2008-07-08 00:30:01",
    "created_at": "2008-07-08T00:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3599#issuecomment-25424",
    "user": "itolkov"
}
```

Attachment [trac3599_extcode_1.patch](tarball://root/attachments/some-uuid/ticket3599/trac3599_extcode_1.patch) by itolkov created at 2008-07-08 00:30:01



---

archive/issue_comments_025425.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2008-07-18T00:05:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3599#issuecomment-25425",
    "user": "itolkov"
}
```

Changing priority from minor to major.



---

archive/issue_comments_025426.json:
```json
{
    "body": "Where does the png file go?",
    "created_at": "2008-07-21T22:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3599#issuecomment-25426",
    "user": "jason"
}
```

Where does the png file go?



---

archive/issue_comments_025427.json:
```json
{
    "body": "Answering my question, it goes in:\n\n$SAGE_ROOT/data/extcode/notebook/javascript/jqueryui/themes/flora/i/slider-bg-3.png\n\nThis patch seems to do what it claims and looks like reasonable code, looks nice, and doctests pass in sage/server/notebook/*.py\n\n+1",
    "created_at": "2008-07-21T22:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3599#issuecomment-25427",
    "user": "jason"
}
```

Answering my question, it goes in:

$SAGE_ROOT/data/extcode/notebook/javascript/jqueryui/themes/flora/i/slider-bg-3.png

This patch seems to do what it claims and looks like reasonable code, looks nice, and doctests pass in sage/server/notebook/*.py

+1



---

archive/issue_comments_025428.json:
```json
{
    "body": "the image of the slider",
    "created_at": "2008-07-29T18:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3599#issuecomment-25428",
    "user": "was"
}
```

the image of the slider



---

archive/issue_comments_025429.json:
```json
{
    "body": "Attachment [trac3599_extcode_2.patch](tarball://root/attachments/some-uuid/ticket3599/trac3599_extcode_2.patch) by was created at 2008-07-29 18:38:37\n\nI replaced the png by a proper patch.",
    "created_at": "2008-07-29T18:38:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3599#issuecomment-25429",
    "user": "was"
}
```

Attachment [trac3599_extcode_2.patch](tarball://root/attachments/some-uuid/ticket3599/trac3599_extcode_2.patch) by was created at 2008-07-29 18:38:37

I replaced the png by a proper patch.



---

archive/issue_comments_025430.json:
```json
{
    "body": "I give this another positive review, by the way.  Very good.",
    "created_at": "2008-07-29T18:41:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3599#issuecomment-25430",
    "user": "was"
}
```

I give this another positive review, by the way.  Very good.



---

archive/issue_comments_025431.json:
```json
{
    "body": "Merged trac3599_sage_1.patch and trac3599_extcode_1.patch in Sage 3.1.alpha0. trac3599_extcode_2.patch is empty. You need to add a git style patch or reattach the png.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-31T01:19:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3599#issuecomment-25431",
    "user": "mabshoff"
}
```

Merged trac3599_sage_1.patch and trac3599_extcode_1.patch in Sage 3.1.alpha0. trac3599_extcode_2.patch is empty. You need to add a git style patch or reattach the png.

Cheers,

Michael



---

archive/issue_comments_025432.json:
```json
{
    "body": "Attachment [slider-bg-3.png](tarball://root/attachments/some-uuid/ticket3599/slider-bg-3.png) by itolkov created at 2008-07-31 17:55:17\n\nHere's the png again.",
    "created_at": "2008-07-31T17:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3599#issuecomment-25432",
    "user": "itolkov"
}
```

Attachment [slider-bg-3.png](tarball://root/attachments/some-uuid/ticket3599/slider-bg-3.png) by itolkov created at 2008-07-31 17:55:17

Here's the png again.



---

archive/issue_comments_025433.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-31T21:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3599#issuecomment-25433",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025434.json:
```json
{
    "body": "Merged slider-bg-3.png in Sage 3.1.alpha0. Thanks Igor for the png. In the future please export a git style patch in case binaries are involved.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-31T21:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3599#issuecomment-25434",
    "user": "mabshoff"
}
```

Merged slider-bg-3.png in Sage 3.1.alpha0. Thanks Igor for the png. In the future please export a git style patch in case binaries are involved.

Cheers,

Michael
