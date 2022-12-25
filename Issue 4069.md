# Issue 4069: support "application shortcut" in chrome and gears

archive/issues_004069.json:
```json
{
    "body": "Assignee: @haraldschilly\n\nSome additional lines in the html-header enable proper handling of the sage notebook as a \"desktop application\". There, all elements from the browser UI are removed and it looks like an application with a shortcut on the desktop or start menu. This is probably more widespread used once HTML 5 ideas are used in other browsers as well.\n\nI'll attach nice icons and a text to this ticket.\n\n[read more here `@`google chrome webmasters/section 15.](http://www.google.com/chrome/intl/en/webmasters-faq.html#tools) and the link to the gears desktop api\n\nIssue created by migration from https://trac.sagemath.org/ticket/4069\n\n",
    "created_at": "2008-09-06T14:47:46Z",
    "labels": [
        "component: notebook",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "support \"application shortcut\" in chrome and gears",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4069",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: @haraldschilly

Some additional lines in the html-header enable proper handling of the sage notebook as a "desktop application". There, all elements from the browser UI are removed and it looks like an application with a shortcut on the desktop or start menu. This is probably more widespread used once HTML 5 ideas are used in other browsers as well.

I'll attach nice icons and a text to this ticket.

[read more here `@`google chrome webmasters/section 15.](http://www.google.com/chrome/intl/en/webmasters-faq.html#tools) and the link to the gears desktop api

Issue created by migration from https://trac.sagemath.org/ticket/4069





---

archive/issue_comments_029301.json:
```json
{
    "body": "Implements a \"Create Shortcut\" link that is displayed in in the \"list worksheets\" view that is displayed if the user has installed Google Gears.\n\nThe images included need to be places in the data/extcode/notebook/images folder and provide the application shortcut image requested by gears.",
    "created_at": "2008-10-31T19:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29301",
    "user": "https://trac.sagemath.org/admin/accounts/users/ahupfer"
}
```

Implements a "Create Shortcut" link that is displayed in in the "list worksheets" view that is displayed if the user has installed Google Gears.

The images included need to be places in the data/extcode/notebook/images folder and provide the application shortcut image requested by gears.



---

archive/issue_comments_029302.json:
```json
{
    "body": "shortcut patch for extcode repository",
    "created_at": "2008-11-02T21:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29302",
    "user": "https://trac.sagemath.org/admin/accounts/users/ahupfer"
}
```

shortcut patch for extcode repository



---

archive/issue_comments_029303.json:
```json
{
    "body": "Attachment [shortcut_extcode.patch](tarball://root/attachments/some-uuid/ticket4069/shortcut_extcode.patch) by ahupfer created at 2008-11-02 21:23:42\n\nshortcut patch for main repository",
    "created_at": "2008-11-02T21:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29303",
    "user": "https://trac.sagemath.org/admin/accounts/users/ahupfer"
}
```

Attachment [shortcut_extcode.patch](tarball://root/attachments/some-uuid/ticket4069/shortcut_extcode.patch) by ahupfer created at 2008-11-02 21:23:42

shortcut patch for main repository



---

archive/issue_comments_029304.json:
```json
{
    "body": "Attachment [shortcut_sage.patch](tarball://root/attachments/some-uuid/ticket4069/shortcut_sage.patch) by TimothyClemans created at 2008-11-10 02:33:41\n\nThe images aren't in either of the patches. I think you have to do ` hg export --git `",
    "created_at": "2008-11-10T02:33:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29304",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [shortcut_sage.patch](tarball://root/attachments/some-uuid/ticket4069/shortcut_sage.patch) by TimothyClemans created at 2008-11-10 02:33:41

The images aren't in either of the patches. I think you have to do ` hg export --git `



---

archive/issue_comments_029305.json:
```json
{
    "body": "Depends on #3950",
    "created_at": "2008-11-10T03:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29305",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Depends on #3950



---

archive/issue_comments_029306.json:
```json
{
    "body": "Don't apply sage-4069_2.patch if #3950 not in. The first two patches work with the lastest sage-3.2. The last patch makes this work when #3950 is merged in.",
    "created_at": "2008-11-10T03:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29306",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Don't apply sage-4069_2.patch if #3950 not in. The first two patches work with the lastest sage-3.2. The last patch makes this work when #3950 is merged in.



---

archive/issue_comments_029307.json:
```json
{
    "body": "Mike,\n\nany news on the ticket reviews you promised to Timothy? I want to hold off on this merge until #3950 is in, so until then this lovely ticket will bitrot :(\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T12:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29307",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mike,

any news on the ticket reviews you promised to Timothy? I want to hold off on this merge until #3950 is in, so until then this lovely ticket will bitrot :(

Cheers,

Michael



---

archive/issue_comments_029308.json:
```json
{
    "body": "Now that #3950 is in this one can go in, but we need a rebase:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha1/devel/sage$ patch -p1 --dry-run < trac_4069_shortcut_sage.patch \npatching file sage/server/notebook/notebook.py\nHunk #2 FAILED at 1319.\nHunk #3 succeeded at 1324 (offset -44 lines).\n1 out of 3 hunks FAILED -- saving rejects to file sage/server/notebook/notebook.py.rej\n```\nOnce it is rebased it will go in.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-07T11:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29308",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_comments_029309.json:
```json
{
    "body": "Attachment [sage-4069_2.patch](tarball://root/attachments/some-uuid/ticket4069/sage-4069_2.patch) by TimothyClemans created at 2008-12-22 18:35:48\n\nRebased",
    "created_at": "2008-12-22T18:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29309",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-4069_2.patch](tarball://root/attachments/some-uuid/ticket4069/sage-4069_2.patch) by TimothyClemans created at 2008-12-22 18:35:48

Rebased



---

archive/issue_comments_029310.json:
```json
{
    "body": "Apply shortcut_extcode.patch and sage-4069_2.patch",
    "created_at": "2008-12-22T18:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29310",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Apply shortcut_extcode.patch and sage-4069_2.patch



---

archive/issue_comments_029311.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-23T21:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29311",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009287.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-23T21:03:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4069#event-9287"
}
```



---

archive/issue_comments_029312.json:
```json
{
    "body": "Merged shortcut_extcode.patch and sage-4069_2.patch in Sage 3.2.3.alpha0",
    "created_at": "2008-12-23T21:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4069#issuecomment-29312",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged shortcut_extcode.patch and sage-4069_2.patch in Sage 3.2.3.alpha0



---

archive/issue_events_009288.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-23T21:03:07Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4069",
    "milestone": "sage-3.2.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4069#event-9288"
}
```
