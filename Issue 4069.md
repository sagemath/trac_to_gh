# Issue 4069: support "application shortcut" in chrome and gears

archive/issues_004069.json:
```json
{
    "body": "Assignee: schilly\n\nSome additional lines in the html-header enable proper handling of the sage notebook as a \"desktop application\". There, all elements from the browser UI are removed and it looks like an application with a shortcut on the desktop or start menu. This is probably more widespread used once HTML 5 ideas are used in other browsers as well.\n\nI'll attach nice icons and a text to this ticket.\n\n[read more here `@`google chrome webmasters/section 15.](http://www.google.com/chrome/intl/en/webmasters-faq.html#tools) and the link to the gears desktop api\n\nIssue created by migration from https://trac.sagemath.org/ticket/4069\n\n",
    "created_at": "2008-09-06T14:47:46Z",
    "labels": [
        "notebook",
        "trivial",
        "bug"
    ],
    "title": "support \"application shortcut\" in chrome and gears",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4069",
    "user": "schilly"
}
```
Assignee: schilly

Some additional lines in the html-header enable proper handling of the sage notebook as a "desktop application". There, all elements from the browser UI are removed and it looks like an application with a shortcut on the desktop or start menu. This is probably more widespread used once HTML 5 ideas are used in other browsers as well.

I'll attach nice icons and a text to this ticket.

[read more here `@`google chrome webmasters/section 15.](http://www.google.com/chrome/intl/en/webmasters-faq.html#tools) and the link to the gears desktop api

Issue created by migration from https://trac.sagemath.org/ticket/4069





---

archive/issue_comments_029360.json:
```json
{
    "body": "Implements a \"Create Shortcut\" link that is displayed in in the \"list worksheets\" view that is displayed if the user has installed Google Gears.\n\nThe images included need to be places in the data/extcode/notebook/images folder and provide the application shortcut image requested by gears.",
    "created_at": "2008-10-31T19:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29360",
    "user": "ahupfer"
}
```

Implements a "Create Shortcut" link that is displayed in in the "list worksheets" view that is displayed if the user has installed Google Gears.

The images included need to be places in the data/extcode/notebook/images folder and provide the application shortcut image requested by gears.



---

archive/issue_comments_029361.json:
```json
{
    "body": "shortcut patch for extcode repository",
    "created_at": "2008-11-02T21:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29361",
    "user": "ahupfer"
}
```

shortcut patch for extcode repository



---

archive/issue_comments_029362.json:
```json
{
    "body": "Attachment\n\nshortcut patch for main repository",
    "created_at": "2008-11-02T21:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29362",
    "user": "ahupfer"
}
```

Attachment

shortcut patch for main repository



---

archive/issue_comments_029363.json:
```json
{
    "body": "Attachment\n\nThe images aren't in either of the patches. I think you have to do ` hg export --git `",
    "created_at": "2008-11-10T02:33:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29363",
    "user": "TimothyClemans"
}
```

Attachment

The images aren't in either of the patches. I think you have to do ` hg export --git `



---

archive/issue_comments_029364.json:
```json
{
    "body": "Depends on #3950",
    "created_at": "2008-11-10T03:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29364",
    "user": "TimothyClemans"
}
```

Depends on #3950



---

archive/issue_comments_029365.json:
```json
{
    "body": "Don't apply sage-4069_2.patch if #3950 not in. The first two patches work with the lastest sage-3.2. The last patch makes this work when #3950 is merged in.",
    "created_at": "2008-11-10T03:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29365",
    "user": "TimothyClemans"
}
```

Don't apply sage-4069_2.patch if #3950 not in. The first two patches work with the lastest sage-3.2. The last patch makes this work when #3950 is merged in.



---

archive/issue_comments_029366.json:
```json
{
    "body": "Mike,\n\nany news on the ticket reviews you promised to Timothy? I want to hold off on this merge until #3950 is in, so until then this lovely ticket will bitrot :(\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T12:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29366",
    "user": "mabshoff"
}
```

Mike,

any news on the ticket reviews you promised to Timothy? I want to hold off on this merge until #3950 is in, so until then this lovely ticket will bitrot :(

Cheers,

Michael



---

archive/issue_comments_029367.json:
```json
{
    "body": "Now that #3950 is in this one can go in, but we need a rebase:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage$ patch -p1 --dry-run < trac_4069_shortcut_sage.patch \npatching file sage/server/notebook/notebook.py\nHunk #2 FAILED at 1319.\nHunk #3 succeeded at 1324 (offset -44 lines).\n1 out of 3 hunks FAILED -- saving rejects to file sage/server/notebook/notebook.py.rej\n```\n\nOnce it is rebased it will go in.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-07T11:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29367",
    "user": "mabshoff"
}
```

Now that #3950 is in this one can go in, but we need a rebase:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage$ patch -p1 --dry-run < trac_4069_shortcut_sage.patch 
patching file sage/server/notebook/notebook.py
Hunk #2 FAILED at 1319.
Hunk #3 succeeded at 1324 (offset -44 lines).
1 out of 3 hunks FAILED -- saving rejects to file sage/server/notebook/notebook.py.rej
```

Once it is rebased it will go in.

Cheers,

Michael



---

archive/issue_comments_029368.json:
```json
{
    "body": "Attachment\n\nRebased",
    "created_at": "2008-12-22T18:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29368",
    "user": "TimothyClemans"
}
```

Attachment

Rebased



---

archive/issue_comments_029369.json:
```json
{
    "body": "Apply shortcut_extcode.patch and sage-4069_2.patch",
    "created_at": "2008-12-22T18:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29369",
    "user": "TimothyClemans"
}
```

Apply shortcut_extcode.patch and sage-4069_2.patch



---

archive/issue_comments_029370.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-23T21:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29370",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029371.json:
```json
{
    "body": "Merged shortcut_extcode.patch and sage-4069_2.patch in Sage 3.2.3.alpha0",
    "created_at": "2008-12-23T21:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29371",
    "user": "mabshoff"
}
```

Merged shortcut_extcode.patch and sage-4069_2.patch in Sage 3.2.3.alpha0
