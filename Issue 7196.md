# Issue 7196: SageNB: Reorganize the JS/Java/CSS/HTML "data" directory

archive/issues_007196.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  timdumol was\n\nReorganize `sagenb/data` around packages.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7196\n\n",
    "created_at": "2009-10-12T17:16:48Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "SageNB: Reorganize the JS/Java/CSS/HTML \"data\" directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7196",
    "user": "mpatel"
}
```
Assignee: boothby

CC:  timdumol was

Reorganize `sagenb/data` around packages.

Issue created by migration from https://trac.sagemath.org/ticket/7196





---

archive/issue_comments_059685.json:
```json
{
    "body": "Attachment [trac_7196-sagenb_data_reorg_part_A.patch](tarball://root/attachments/some-uuid/ticket7196/trac_7196-sagenb_data_reorg_part_A.patch) by mpatel created at 2009-10-12 17:38:06\n\nSageNB data/ reorg part A: Shuffle files and directories.  Apply this patch first.",
    "created_at": "2009-10-12T17:38:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7196#issuecomment-59685",
    "user": "mpatel"
}
```

Attachment [trac_7196-sagenb_data_reorg_part_A.patch](tarball://root/attachments/some-uuid/ticket7196/trac_7196-sagenb_data_reorg_part_A.patch) by mpatel created at 2009-10-12 17:38:06

SageNB data/ reorg part A: Shuffle files and directories.  Apply this patch first.



---

archive/issue_comments_059686.json:
```json
{
    "body": "SageNB data/ reorg part B: Fix broken paths. Apply this patch second.",
    "created_at": "2009-10-12T17:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7196#issuecomment-59686",
    "user": "mpatel"
}
```

SageNB data/ reorg part B: Fix broken paths. Apply this patch second.



---

archive/issue_comments_059687.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-12T17:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7196#issuecomment-59687",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059688.json:
```json
{
    "body": "Attachment [trac_7196-sagenb_data_reorg_part_B.patch](tarball://root/attachments/some-uuid/ticket7196/trac_7196-sagenb_data_reorg_part_B.patch) by mpatel created at 2009-10-12 17:40:49\n\nI made the change in two parts, since the shuffle slowed Mercurial significantly.",
    "created_at": "2009-10-12T17:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7196#issuecomment-59688",
    "user": "mpatel"
}
```

Attachment [trac_7196-sagenb_data_reorg_part_B.patch](tarball://root/attachments/some-uuid/ticket7196/trac_7196-sagenb_data_reorg_part_B.patch) by mpatel created at 2009-10-12 17:40:49

I made the change in two parts, since the shuffle slowed Mercurial significantly.



---

archive/issue_comments_059689.json:
```json
{
    "body": "You didn't mention it, but one must *MANUALLY* move data/java/jmol to data/jmol after applying this patch, since jmol isn't under revision control, and the path to jmol was changed in twist.py.",
    "created_at": "2009-10-15T01:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7196#issuecomment-59689",
    "user": "was"
}
```

You didn't mention it, but one must *MANUALLY* move data/java/jmol to data/jmol after applying this patch, since jmol isn't under revision control, and the path to jmol was changed in twist.py.



---

archive/issue_comments_059690.json:
```json
{
    "body": "positive review, and merged into sagenb-0.3.1, which has been posted here:\n\n http://sage.math.washington.edu/home/wstein/patches/sagenb/",
    "created_at": "2009-10-15T01:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7196#issuecomment-59690",
    "user": "was"
}
```

positive review, and merged into sagenb-0.3.1, which has been posted here:

 http://sage.math.washington.edu/home/wstein/patches/sagenb/



---

archive/issue_comments_059691.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T01:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7196#issuecomment-59691",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_059692.json:
```json
{
    "body": "Attachment [trac_7196-manifest.patch](tarball://root/attachments/some-uuid/ticket7196/trac_7196-manifest.patch) by mpatel created at 2009-10-19 14:52:03\n\nUpdate MANIFEST.in.",
    "created_at": "2009-10-19T14:52:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7196#issuecomment-59692",
    "user": "mpatel"
}
```

Attachment [trac_7196-manifest.patch](tarball://root/attachments/some-uuid/ticket7196/trac_7196-manifest.patch) by mpatel created at 2009-10-19 14:52:03

Update MANIFEST.in.
