# Issue 6143: Upgrade tinyMCE to 3.2.4.1

archive/issues_006143.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @rlmill boothby tclemans @williamstein @robertwb mhampton\n\nAn spkg is up at http://sage.math.washington.edu/home/jason/tinyMCE-3.2.4.1.spkg\n\nThe new version has lots and lots of bugfixes, including lots of fixes for Safari.  It also has a greatly improved paste-from-word functionality.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6143\n\n",
    "created_at": "2009-05-28T04:56:22Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "Upgrade tinyMCE to 3.2.4.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6143",
    "user": "https://github.com/jasongrout"
}
```
Assignee: mabshoff

CC:  @rlmill boothby tclemans @williamstein @robertwb mhampton

An spkg is up at http://sage.math.washington.edu/home/jason/tinyMCE-3.2.4.1.spkg

The new version has lots and lots of bugfixes, including lots of fixes for Safari.  It also has a greatly improved paste-from-word functionality.

Issue created by migration from https://trac.sagemath.org/ticket/6143





---

archive/issue_comments_048948.json:
```json
{
    "body": "I downloaded the new package and installed it via `sage -i`.  TinyMCE seems to work for me just as it did previously, in Cr3, FF3.5, and O9 on Linux and Cr2, FF3.5, IE8, S4, and O9 on Windows XP.   However, I can't test the new spkg in any Mac OS browsers or with Word.  I did have success with the 'paste-from-Word' feature --- from OpenOffice.org Writer v3.0.1 on Linux.  In particular, I was able to \"paste,\" through the dialog, tables and variously-formatted text.\n\nThe package contents conform to the [guidelines](http://wiki.sagemath.org/SPKG_Audit).\n\nPending a confirmation that it works properly on Macs, particularly in Safari, I give the new spkg a positive review.\n\nFor what it's worth, the patch at #6459 still works for me after the upgrade.",
    "created_at": "2009-07-17T01:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6143#issuecomment-48948",
    "user": "https://github.com/qed777"
}
```

I downloaded the new package and installed it via `sage -i`.  TinyMCE seems to work for me just as it did previously, in Cr3, FF3.5, and O9 on Linux and Cr2, FF3.5, IE8, S4, and O9 on Windows XP.   However, I can't test the new spkg in any Mac OS browsers or with Word.  I did have success with the 'paste-from-Word' feature --- from OpenOffice.org Writer v3.0.1 on Linux.  In particular, I was able to "paste," through the dialog, tables and variously-formatted text.

The package contents conform to the [guidelines](http://wiki.sagemath.org/SPKG_Audit).

Pending a confirmation that it works properly on Macs, particularly in Safari, I give the new spkg a positive review.

For what it's worth, the patch at #6459 still works for me after the upgrade.



---

archive/issue_comments_048949.json:
```json
{
    "body": "I'm CCing people that I know have macs or have worked on the notebook.  Can someone please check this spkg out on a mac?",
    "created_at": "2009-07-18T23:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6143#issuecomment-48949",
    "user": "https://github.com/jasongrout"
}
```

I'm CCing people that I know have macs or have worked on the notebook.  Can someone please check this spkg out on a mac?



---

archive/issue_comments_048950.json:
```json
{
    "body": "CCing one more person that I know has a mac, in hopes that someone will review this ticket (i.e., apply the spkg and check to make sure tinymce works in Safari.)",
    "created_at": "2009-07-30T09:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6143#issuecomment-48950",
    "user": "https://github.com/jasongrout"
}
```

CCing one more person that I know has a mac, in hopes that someone will review this ticket (i.e., apply the spkg and check to make sure tinymce works in Safari.)



---

archive/issue_comments_048951.json:
```json
{
    "body": "Seems to work fine on my mac, with Safari and Firefox.  Based on the previous review I think I can change this to a positive review.",
    "created_at": "2009-07-30T14:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6143#issuecomment-48951",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Seems to work fine on my mac, with Safari and Firefox.  Based on the previous review I think I can change this to a positive review.



---

archive/issue_events_006392.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-08-03T02:19:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6143",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6143#event-6392"
}
```



---

archive/issue_comments_048952.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-03T02:19:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6143#issuecomment-48952",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
