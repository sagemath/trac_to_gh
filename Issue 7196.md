# Issue 7196: SageNB: Reorganize the JS/Java/CSS/HTML "data" directory

archive/issues_007196.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @TimDumol @williamstein\n\nReorganize `sagenb/data` around packages.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7196\n\n",
    "created_at": "2009-10-12T17:16:48Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "SageNB: Reorganize the JS/Java/CSS/HTML \"data\" directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7196",
    "user": "https://github.com/qed777"
}
```
Assignee: boothby

CC:  @TimDumol @williamstein

Reorganize `sagenb/data` around packages.

Issue created by migration from https://trac.sagemath.org/ticket/7196





---

archive/issue_comments_059573.json:
```json
{
    "body": "Attachment [trac_7196-sagenb_data_reorg_part_A.patch](tarball://root/attachments/some-uuid/ticket7196/trac_7196-sagenb_data_reorg_part_A.patch) by @qed777 created at 2009-10-12 17:38:06\n\nSageNB data/ reorg part A: Shuffle files and directories.  Apply this patch first.",
    "created_at": "2009-10-12T17:38:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7196#issuecomment-59573",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7196-sagenb_data_reorg_part_A.patch](tarball://root/attachments/some-uuid/ticket7196/trac_7196-sagenb_data_reorg_part_A.patch) by @qed777 created at 2009-10-12 17:38:06

SageNB data/ reorg part A: Shuffle files and directories.  Apply this patch first.



---

archive/issue_comments_059574.json:
```json
{
    "body": "SageNB data/ reorg part B: Fix broken paths. Apply this patch second.",
    "created_at": "2009-10-12T17:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7196#issuecomment-59574",
    "user": "https://github.com/qed777"
}
```

SageNB data/ reorg part B: Fix broken paths. Apply this patch second.



---

archive/issue_comments_059575.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-12T17:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7196#issuecomment-59575",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059576.json:
```json
{
    "body": "Attachment [trac_7196-sagenb_data_reorg_part_B.patch](tarball://root/attachments/some-uuid/ticket7196/trac_7196-sagenb_data_reorg_part_B.patch) by @qed777 created at 2009-10-12 17:40:49\n\nI made the change in two parts, since the shuffle slowed Mercurial significantly.",
    "created_at": "2009-10-12T17:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7196#issuecomment-59576",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7196-sagenb_data_reorg_part_B.patch](tarball://root/attachments/some-uuid/ticket7196/trac_7196-sagenb_data_reorg_part_B.patch) by @qed777 created at 2009-10-12 17:40:49

I made the change in two parts, since the shuffle slowed Mercurial significantly.



---

archive/issue_comments_059577.json:
```json
{
    "body": "You didn't mention it, but one must *MANUALLY* move data/java/jmol to data/jmol after applying this patch, since jmol isn't under revision control, and the path to jmol was changed in twist.py.",
    "created_at": "2009-10-15T01:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7196#issuecomment-59577",
    "user": "https://github.com/williamstein"
}
```

You didn't mention it, but one must *MANUALLY* move data/java/jmol to data/jmol after applying this patch, since jmol isn't under revision control, and the path to jmol was changed in twist.py.



---

archive/issue_comments_059578.json:
```json
{
    "body": "positive review, and merged into sagenb-0.3.1, which has been posted here:\n\n http://sage.math.washington.edu/home/wstein/patches/sagenb/",
    "created_at": "2009-10-15T01:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7196#issuecomment-59578",
    "user": "https://github.com/williamstein"
}
```

positive review, and merged into sagenb-0.3.1, which has been posted here:

 http://sage.math.washington.edu/home/wstein/patches/sagenb/



---

archive/issue_comments_059579.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T01:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7196#issuecomment-59579",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_007415.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2009-10-15T01:24:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7196#event-7415"
}
```



---

archive/issue_comments_059580.json:
```json
{
    "body": "Attachment [trac_7196-manifest.patch](tarball://root/attachments/some-uuid/ticket7196/trac_7196-manifest.patch) by @qed777 created at 2009-10-19 14:52:03\n\nUpdate MANIFEST.in.",
    "created_at": "2009-10-19T14:52:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7196#issuecomment-59580",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7196-manifest.patch](tarball://root/attachments/some-uuid/ticket7196/trac_7196-manifest.patch) by @qed777 created at 2009-10-19 14:52:03

Update MANIFEST.in.
