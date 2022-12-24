# Issue 6654: [with patch, needs review] new features in group algebra category

archive/issues_006654.json:
```json
{
    "body": "Assignee: mhansen\n\nKeywords: group algebra, center\n\nI added features in the category of group algebras (especially linked to the center).\n\nMoreover, the symmetric group algebra now is a parent of this category.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6654\n\n",
    "created_at": "2009-07-29T13:16:54Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] new features in group algebra category",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6654",
    "user": "vferay"
}
```
Assignee: mhansen

Keywords: group algebra, center

I added features in the category of group algebras (especially linked to the center).

Moreover, the symmetric group algebra now is a parent of this category.

Issue created by migration from https://trac.sagemath.org/ticket/6654





---

archive/issue_comments_054613.json:
```json
{
    "body": "This patch failed to pply for me:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nLoading Sage library. Current Mercurial branch is: gpalg\nsage: hg_sage.apply(\"/Users/davidjoyner/sagefiles/grotrac_6647_permutationgroup_improvement.patch\")\n/Users/davidjoyner/sagefiles/group_algebras_feature_central_vf.patch\n/Users/davidjoyner/sagefiles/groups\nsage: hg_sage.apply(\"/Users/davidjoyner/sagefiles/group_algebras_feature_central_vf.patch\")cd \"/Users/davidjoyner/sagefiles/sage-4.1.1.rc2/devel/sage\" && hg status\n/Users/davidjoyner/sagefiles/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.\n  x = os.popen3(s)\ncd \"/Users/davidjoyner/sagefiles/sage-4.1.1.rc2/devel/sage\" && hg status\ncd \"/Users/davidjoyner/sagefiles/sage-4.1.1.rc2/devel/sage\" && hg import   \"/Users/davidjoyner/sagefiles/group_algebras_feature_central_vf.patch\"\napplying /Users/davidjoyner/sagefiles/group_algebras_feature_central_vf.patch\nunable to find 'sage/categories/group_algebras.py' for patching\n3 out of 3 hunks FAILED -- saving rejects to file sage/categories/group_algebras.py.rej\nunable to find 'sage/categories/monoid_algebras.py' for patching\n1 out of 1 hunks FAILED -- saving rejects to file sage/categories/monoid_algebras.py.rej\npatching file sage/combinat/symmetric_group_algebra.py\nHunk #2 FAILED at 121\nHunk #3 FAILED at 131\nHunk #5 FAILED at 430\n3 out of 5 hunks FAILED -- saving rejects to file sage/combinat/symmetric_group_algebra.py.rej\nabort: patch failed to apply\n```\n\n| Sage Version 4.1.1.rc2, Release Date: 2009-08-06                   |\n| Type notebook() for the GUI, and license() for information.        |\nDO you know what the problem is?",
    "created_at": "2009-08-15T23:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6654#issuecomment-54613",
    "user": "wdj"
}
```

This patch failed to pply for me:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Loading Sage library. Current Mercurial branch is: gpalg
sage: hg_sage.apply("/Users/davidjoyner/sagefiles/grotrac_6647_permutationgroup_improvement.patch")
/Users/davidjoyner/sagefiles/group_algebras_feature_central_vf.patch
/Users/davidjoyner/sagefiles/groups
sage: hg_sage.apply("/Users/davidjoyner/sagefiles/group_algebras_feature_central_vf.patch")cd "/Users/davidjoyner/sagefiles/sage-4.1.1.rc2/devel/sage" && hg status
/Users/davidjoyner/sagefiles/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.
  x = os.popen3(s)
cd "/Users/davidjoyner/sagefiles/sage-4.1.1.rc2/devel/sage" && hg status
cd "/Users/davidjoyner/sagefiles/sage-4.1.1.rc2/devel/sage" && hg import   "/Users/davidjoyner/sagefiles/group_algebras_feature_central_vf.patch"
applying /Users/davidjoyner/sagefiles/group_algebras_feature_central_vf.patch
unable to find 'sage/categories/group_algebras.py' for patching
3 out of 3 hunks FAILED -- saving rejects to file sage/categories/group_algebras.py.rej
unable to find 'sage/categories/monoid_algebras.py' for patching
1 out of 1 hunks FAILED -- saving rejects to file sage/categories/monoid_algebras.py.rej
patching file sage/combinat/symmetric_group_algebra.py
Hunk #2 FAILED at 121
Hunk #3 FAILED at 131
Hunk #5 FAILED at 430
3 out of 5 hunks FAILED -- saving rejects to file sage/combinat/symmetric_group_algebra.py.rej
abort: patch failed to apply
```

| Sage Version 4.1.1.rc2, Release Date: 2009-08-06                   |
| Type notebook() for the GUI, and license() for information.        |
DO you know what the problem is?



---

archive/issue_comments_054614.json:
```json
{
    "body": "This patch must be applied after Nicolas Thi\u00e9ry's patches on categories (I do not know which one exactly). So please do not use import to test it but apply it with qpush.",
    "created_at": "2009-09-10T10:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6654#issuecomment-54614",
    "user": "vferay"
}
```

This patch must be applied after Nicolas Thiéry's patches on categories (I do not know which one exactly). So please do not use import to test it but apply it with qpush.



---

archive/issue_comments_054615.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-13T14:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6654#issuecomment-54615",
    "user": "vferay"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_054616.json:
```json
{
    "body": "Apply [attachment:group_algebras_feature_central_vf.patch.new_version]",
    "created_at": "2012-08-29T10:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6654#issuecomment-54616",
    "user": "chapoton"
}
```

Apply [attachment:group_algebras_feature_central_vf.patch.new_version]



---

archive/issue_comments_054617.json:
```json
{
    "body": "apply only group_algebras_feature_central_vf.v2.patch",
    "created_at": "2012-09-08T07:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6654#issuecomment-54617",
    "user": "chapoton"
}
```

apply only group_algebras_feature_central_vf.v2.patch



---

archive/issue_comments_054618.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-09-08T07:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6654#issuecomment-54618",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054619.json:
```json
{
    "body": "apply only group_algebras_feature_central_vf.v2.patch",
    "created_at": "2012-09-08T09:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6654#issuecomment-54619",
    "user": "chapoton"
}
```

apply only group_algebras_feature_central_vf.v2.patch



---

archive/issue_comments_054620.json:
```json
{
    "body": "clean up of doc",
    "created_at": "2012-09-08T12:00:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6654#issuecomment-54620",
    "user": "chapoton"
}
```

clean up of doc



---

archive/issue_comments_054621.json:
```json
{
    "body": "Attachment [group_algebras_feature_central_vf.v2.patch](tarball://root/attachments/some-uuid/ticket6654/group_algebras_feature_central_vf.v2.patch) by chapoton created at 2012-09-08 12:00:24\n\napply only group_algebras_feature_central_vf.v2.patch",
    "created_at": "2012-09-08T12:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6654#issuecomment-54621",
    "user": "chapoton"
}
```

Attachment [group_algebras_feature_central_vf.v2.patch](tarball://root/attachments/some-uuid/ticket6654/group_algebras_feature_central_vf.v2.patch) by chapoton created at 2012-09-08 12:00:24

apply only group_algebras_feature_central_vf.v2.patch



---

archive/issue_comments_054622.json:
```json
{
    "body": "Given that the bot is happy, and that I have done my best to check the doc, I give a positive review.",
    "created_at": "2012-09-09T18:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6654#issuecomment-54622",
    "user": "chapoton"
}
```

Given that the bot is happy, and that I have done my best to check the doc, I give a positive review.



---

archive/issue_comments_054623.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-09-09T18:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6654#issuecomment-54623",
    "user": "chapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054624.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-09-11T07:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6654",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6654#issuecomment-54624",
    "user": "jdemeyer"
}
```

Resolution: fixed
