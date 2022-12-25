# Issue 5633: [with patch, needs review] add pix to the documentation

archive/issues_005633.json:
```json
{
    "body": "Assignee: tba\n\nThe documentation has been missing a few pictures, and this patch restores them.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5633\n\n",
    "created_at": "2009-03-29T16:08:57Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] add pix to the documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5633",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: tba

The documentation has been missing a few pictures, and this patch restores them.

Issue created by migration from https://trac.sagemath.org/ticket/5633





---

archive/issue_comments_043910.json:
```json
{
    "body": "Changing assignee from tba to @jhpalmieri.",
    "created_at": "2009-03-29T16:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5633#issuecomment-43910",
    "user": "https://github.com/jhpalmieri"
}
```

Changing assignee from tba to @jhpalmieri.



---

archive/issue_comments_043911.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-29T16:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5633#issuecomment-43911",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_043912.json:
```json
{
    "body": "To summarize: these files are added:\n\nsage/doc/en/a_tour_of_sage/eigen_plot.png\nsage/doc/en/a_tour_of_sage/sin_plot.png\nsage/doc/en/bordeaux_2008/birch.png\nsage/doc/en/bordeaux_2008/modpcurve.png\n\nYou can test this by viewing the documentation (html or pdf version) as is, then apply the patch, rebuild, and view the new documentation.  The pictures should appear in the second version.",
    "created_at": "2009-03-29T23:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5633#issuecomment-43912",
    "user": "https://github.com/jhpalmieri"
}
```

To summarize: these files are added:

sage/doc/en/a_tour_of_sage/eigen_plot.png
sage/doc/en/a_tour_of_sage/sin_plot.png
sage/doc/en/bordeaux_2008/birch.png
sage/doc/en/bordeaux_2008/modpcurve.png

You can test this by viewing the documentation (html or pdf version) as is, then apply the patch, rebuild, and view the new documentation.  The pictures should appear in the second version.



---

archive/issue_comments_043913.json:
```json
{
    "body": "This patch will need to be accomplished by a patch that adds those file to MANIFEST.in. Otherwise the repo will be broken for a fresh build.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T00:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5633#issuecomment-43913",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch will need to be accomplished by a patch that adds those file to MANIFEST.in. Otherwise the repo will be broken for a fresh build.

Cheers,

Michael



---

archive/issue_comments_043914.json:
```json
{
    "body": "I've added a line adding all .png files in the doc directory; is that okay?",
    "created_at": "2009-04-06T03:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5633#issuecomment-43914",
    "user": "https://github.com/jhpalmieri"
}
```

I've added a line adding all .png files in the doc directory; is that okay?



---

archive/issue_comments_043915.json:
```json
{
    "body": "(Oops -- if this patch is too big, delete it: the link in the summary points to the new patch.)",
    "created_at": "2009-04-06T03:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5633#issuecomment-43915",
    "user": "https://github.com/jhpalmieri"
}
```

(Oops -- if this patch is too big, delete it: the link in the summary points to the new patch.)



---

archive/issue_comments_043916.json:
```json
{
    "body": "The patch is fine, it isn't too large and we just don't want spkgs attached here.\n\nI am not happy with the MANIFEST.in changes since if one does build the documentation using pngs instead of jsmath you end up with a boatload of crap in the spkg. You should add the four files explicitly to MANIFEST.in - this is the only true and optimal patch IMHO.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T04:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5633#issuecomment-43916",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch is fine, it isn't too large and we just don't want spkgs attached here.

I am not happy with the MANIFEST.in changes since if one does build the documentation using pngs instead of jsmath you end up with a boatload of crap in the spkg. You should add the four files explicitly to MANIFEST.in - this is the only true and optimal patch IMHO.

Cheers,

Michael



---

archive/issue_comments_043917.json:
```json
{
    "body": "Okay.  Note that this means that if someone decides to add pictures to the tutorial, for example (people requested this a long time ago for the plotting section), then they'll have to add those individually, too. It might get to be a little tedious after a while...",
    "created_at": "2009-04-06T05:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5633#issuecomment-43917",
    "user": "https://github.com/jhpalmieri"
}
```

Okay.  Note that this means that if someone decides to add pictures to the tutorial, for example (people requested this a long time ago for the plotting section), then they'll have to add those individually, too. It might get to be a little tedious after a while...



---

archive/issue_comments_043918.json:
```json
{
    "body": "Attachment [pic.patch](tarball://root/attachments/some-uuid/ticket5633/pic.patch) by @jhpalmieri created at 2009-04-06 05:12:55",
    "created_at": "2009-04-06T05:12:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5633#issuecomment-43918",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [pic.patch](tarball://root/attachments/some-uuid/ticket5633/pic.patch) by @jhpalmieri created at 2009-04-06 05:12:55



---

archive/issue_comments_043919.json:
```json
{
    "body": "Replying to [comment:8 jhpalmieri]:\n> Okay.  Note that this means that if someone decides to add pictures to the tutorial, for example (people requested this a long time ago for the plotting section), then they'll have to add those individually, too. It might get to be a little tedious after a while...\n\nWell, you can recursively include png images below a certain directory for example, but I will catch any issue with pics being added to the documentation, but not in MANIFEST.in. I will review this patch shortly.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T05:22:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5633#issuecomment-43919",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:8 jhpalmieri]:
> Okay.  Note that this means that if someone decides to add pictures to the tutorial, for example (people requested this a long time ago for the plotting section), then they'll have to add those individually, too. It might get to be a little tedious after a while...

Well, you can recursively include png images below a certain directory for example, but I will catch any issue with pics being added to the documentation, but not in MANIFEST.in. I will review this patch shortly.

Cheers,

Michael



---

archive/issue_comments_043920.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T05:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5633#issuecomment-43920",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_043921.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-06T05:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5633#issuecomment-43921",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043922.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T05:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5633#issuecomment-43922",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc1.

Cheers,

Michael
