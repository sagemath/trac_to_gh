# Issue 2740: Downloading and uploading folders of worksheets

archive/issues_002740.json:
```json
{
    "body": "Assignee: boothby\n\nTo ease migration between, for example, vmware images, it would be nice to be able to download and upload entire folders of worksheets, instead of just one at a time.  Or even beyond that, download/upload everything related to your notebook account.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2740\n\n",
    "created_at": "2008-03-31T15:54:01Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "Downloading and uploading folders of worksheets",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2740",
    "user": "jason"
}
```
Assignee: boothby

To ease migration between, for example, vmware images, it would be nice to be able to download and upload entire folders of worksheets, instead of just one at a time.  Or even beyond that, download/upload everything related to your notebook account.

Issue created by migration from https://trac.sagemath.org/ticket/2740





---

archive/issue_comments_018838.json:
```json
{
    "body": "we already have the checkboxes, so maybe just another menu option that would take the checked worksheets and make a zip of all the corresponding sws files.  Just a zip of all the sws files should do; maybe call it a snb for a sage note book?  The upload code then just double checks for sws files when it unzips and imports each one.",
    "created_at": "2008-11-14T05:04:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2740#issuecomment-18838",
    "user": "jason"
}
```

we already have the checkboxes, so maybe just another menu option that would take the checked worksheets and make a zip of all the corresponding sws files.  Just a zip of all the sws files should do; maybe call it a snb for a sage note book?  The upload code then just double checks for sws files when it unzips and imports each one.



---

archive/issue_comments_018839.json:
```json
{
    "body": "Attachment [2740-download-all.patch](tarball://root/attachments/some-uuid/ticket2740/2740-download-all.patch) by robertwb created at 2009-04-14 12:47:59\n\nThis should be fixed to be non-blocking, possibly even with feedback (as it might be slow).",
    "created_at": "2009-04-14T12:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2740#issuecomment-18839",
    "user": "robertwb"
}
```

Attachment [2740-download-all.patch](tarball://root/attachments/some-uuid/ticket2740/2740-download-all.patch) by robertwb created at 2009-04-14 12:47:59

This should be fixed to be non-blocking, possibly even with feedback (as it might be slow).



---

archive/issue_comments_018840.json:
```json
{
    "body": "Attachment [2740-download-checked.patch](tarball://root/attachments/some-uuid/ticket2740/2740-download-checked.patch) by robertwb created at 2009-04-14 13:35:44\n\nallows downloading of checked worksheets only",
    "created_at": "2009-04-14T13:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2740#issuecomment-18840",
    "user": "robertwb"
}
```

Attachment [2740-download-checked.patch](tarball://root/attachments/some-uuid/ticket2740/2740-download-checked.patch) by robertwb created at 2009-04-14 13:35:44

allows downloading of checked worksheets only



---

archive/issue_comments_018841.json:
```json
{
    "body": "REFEREE REPORT:\n\nI love this!\n\n1. I think this should go in even without the non-blocking option.   It can be an option in the notebook command to turn this on, with it off by default.   Then on public servers people keep it off, but for their own servers (the vast majority), it is on.\n\n2. The upload screen says: \"Upload worksheet (an sws or txt file) to the Sage Notebook\".  It should also say that one can upload a zip archive.\n\n3. It would be nice if the filename of the sws could be included in the worksheet name, optionally.  My students always seem to name their sws filename right, but often forgot to actually rename their worksheets.  This causes me a *massive* amount of work to track down.",
    "created_at": "2009-04-20T02:11:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2740#issuecomment-18841",
    "user": "was"
}
```

REFEREE REPORT:

I love this!

1. I think this should go in even without the non-blocking option.   It can be an option in the notebook command to turn this on, with it off by default.   Then on public servers people keep it off, but for their own servers (the vast majority), it is on.

2. The upload screen says: "Upload worksheet (an sws or txt file) to the Sage Notebook".  It should also say that one can upload a zip archive.

3. It would be nice if the filename of the sws could be included in the worksheet name, optionally.  My students always seem to name their sws filename right, but often forgot to actually rename their worksheets.  This causes me a *massive* amount of work to track down.



---

archive/issue_comments_018842.json:
```json
{
    "body": "I'm changing this to a positive review, because 1-3 above are just minor nitpicks, and can all easily be fixed/polished later.",
    "created_at": "2009-04-28T23:35:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2740#issuecomment-18842",
    "user": "was"
}
```

I'm changing this to a positive review, because 1-3 above are just minor nitpicks, and can all easily be fixed/polished later.



---

archive/issue_comments_018843.json:
```json
{
    "body": "Merged both patches in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T07:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2740#issuecomment-18843",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_018844.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-30T07:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2740",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2740#issuecomment-18844",
    "user": "mabshoff"
}
```

Resolution: fixed
