# Issue 9835: Linear Programming Thematic Tutorial

archive/issues_009835.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  minh rhinton\n\nHere it is ! The long-promised tutorial for LP. It is a translation of the french sagebook, and I hope I will be able to keep the two coordinated `:-)`\n\nThis patchremoved the old tutorial from the \"constructions\" document where it shouldn't have been put in the first place, and creates a new file in thematic_tutorials. It is up-to-date for the moment, though I hope to be able to work on some improvements with the CPLEX interface soon. It may only change te way CPLEX has to be installed, which would only require a minor edit later.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9836\n\n",
    "created_at": "2010-08-29T03:56:30Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Linear Programming Thematic Tutorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9835",
    "user": "ncohen"
}
```
Assignee: mvngu

CC:  minh rhinton

Here it is ! The long-promised tutorial for LP. It is a translation of the french sagebook, and I hope I will be able to keep the two coordinated `:-)`

This patchremoved the old tutorial from the "constructions" document where it shouldn't have been put in the first place, and creates a new file in thematic_tutorials. It is up-to-date for the moment, though I hope to be able to work on some improvements with the CPLEX interface soon. It may only change te way CPLEX has to be installed, which would only require a minor edit later.

Issue created by migration from https://trac.sagemath.org/ticket/9836





---

archive/issue_comments_097050.json:
```json
{
    "body": "Attachment [lp_flot1.png](tarball://root/attachments/some-uuid/ticket9836/lp_flot1.png) by ncohen created at 2010-08-29 03:57:32",
    "created_at": "2010-08-29T03:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9835#issuecomment-97050",
    "user": "ncohen"
}
```

Attachment [lp_flot1.png](tarball://root/attachments/some-uuid/ticket9836/lp_flot1.png) by ncohen created at 2010-08-29 03:57:32



---

archive/issue_comments_097051.json:
```json
{
    "body": "Attachment [lp_flot2.png](tarball://root/attachments/some-uuid/ticket9836/lp_flot2.png) by ncohen created at 2010-08-29 03:57:46",
    "created_at": "2010-08-29T03:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9835#issuecomment-97051",
    "user": "ncohen"
}
```

Attachment [lp_flot2.png](tarball://root/attachments/some-uuid/ticket9836/lp_flot2.png) by ncohen created at 2010-08-29 03:57:46



---

archive/issue_comments_097052.json:
```json
{
    "body": "The two pictures should be added to the `thematic_tutotials/` folder. This patch does not pass doctests for two reasons :\n\n* Sage forgets the definition of the variables between different code sections (if you have any idea about how to fix this `^^;`)\n\n* There is a random doctest which should fail every second run, but it is a bit hard to fix with all the previous errors\n\nSorry to send this patch like that. This may be the last time I can access internet before next week (and I incidentally skipped my second meal today to finish it `:-D`), so if somebody knows how to fix these.. Otherwise, I'll take care of it when I'm back `:-)`\n\nNathann",
    "created_at": "2010-08-29T04:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9835#issuecomment-97052",
    "user": "ncohen"
}
```

The two pictures should be added to the `thematic_tutotials/` folder. This patch does not pass doctests for two reasons :

* Sage forgets the definition of the variables between different code sections (if you have any idea about how to fix this `^^;`)

* There is a random doctest which should fail every second run, but it is a bit hard to fix with all the previous errors

Sorry to send this patch like that. This may be the last time I can access internet before next week (and I incidentally skipped my second meal today to finish it `:-D`), so if somebody knows how to fix these.. Otherwise, I'll take care of it when I'm back `:-)`

Nathann



---

archive/issue_comments_097053.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-08-29T04:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9835#issuecomment-97053",
    "user": "ncohen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_097054.json:
```json
{
    "body": "Updated thanks to wise advice `:-)`\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/415a5c9fb8939c41/3c6d911b4d2fd2b3?lnk=gst&q=sphinx+forgets#3c6d911b4d2fd2b3\n\nIt is now ready for review !\n\nNathann",
    "created_at": "2010-09-04T11:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9835#issuecomment-97054",
    "user": "ncohen"
}
```

Updated thanks to wise advice `:-)`

http://groups.google.com/group/sage-devel/browse_thread/thread/415a5c9fb8939c41/3c6d911b4d2fd2b3?lnk=gst&q=sphinx+forgets#3c6d911b4d2fd2b3

It is now ready for review !

Nathann



---

archive/issue_comments_097055.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-04T11:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9835#issuecomment-97055",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_097056.json:
```json
{
    "body": "Attachment [trac_9836-reviewer.patch](tarball://root/attachments/some-uuid/ticket9836/trac_9836-reviewer.patch) by mvngu created at 2010-09-11 08:18:56",
    "created_at": "2010-09-11T08:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9835#issuecomment-97056",
    "user": "mvngu"
}
```

Attachment [trac_9836-reviewer.patch](tarball://root/attachments/some-uuid/ticket9836/trac_9836-reviewer.patch) by mvngu created at 2010-09-11 08:18:56



---

archive/issue_comments_097057.json:
```json
{
    "body": "I'm happy with ncohen's tutorial. I have attached a reviewer patch to make it slightly better. Changes include:\n\n* Directly add the two images with `hg add`. This makes sure that the images are under revision control.\n* Where possible, cut off lines at about 75 characters.\n* Some consistency in how you space headings.\n* Some consistency in how you present Sage code.\n* Use 4 space indentation.\n* Numerous typo fixes.\n* Simplify some of the prose to suit a tutorial format.\n\nI need another pair of eyes to check my patch.",
    "created_at": "2010-09-11T08:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9835#issuecomment-97057",
    "user": "mvngu"
}
```

I'm happy with ncohen's tutorial. I have attached a reviewer patch to make it slightly better. Changes include:

* Directly add the two images with `hg add`. This makes sure that the images are under revision control.
* Where possible, cut off lines at about 75 characters.
* Some consistency in how you space headings.
* Some consistency in how you present Sage code.
* Use 4 space indentation.
* Numerous typo fixes.
* Simplify some of the prose to suit a tutorial format.

I need another pair of eyes to check my patch.



---

archive/issue_comments_097058.json:
```json
{
    "body": "Thank you for your patch Minh ! I noticed reviewing it that I had forgotten to rename a variable, ``\"poids\"``, which means \"weight\" in french `:-D`\n\nCould you check this small patch before changing this ticket's status ?\n\nThanks !\n\nNathann",
    "created_at": "2010-09-11T10:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9835#issuecomment-97058",
    "user": "ncohen"
}
```

Thank you for your patch Minh ! I noticed reviewing it that I had forgotten to rename a variable, ``"poids"``, which means "weight" in french `:-D`

Could you check this small patch before changing this ticket's status ?

Thanks !

Nathann



---

archive/issue_comments_097059.json:
```json
{
    "body": "Attachment [trac_9836 - renaming a variable.patch](tarball://root/attachments/some-uuid/ticket9836/trac_9836 - renaming a variable.patch) by ncohen created at 2010-09-11 10:49:02",
    "created_at": "2010-09-11T10:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9835#issuecomment-97059",
    "user": "ncohen"
}
```

Attachment [trac_9836 - renaming a variable.patch](tarball://root/attachments/some-uuid/ticket9836/trac_9836 - renaming a variable.patch) by ncohen created at 2010-09-11 10:49:02



---

archive/issue_comments_097060.json:
```json
{
    "body": "Good! Let's get it into the standard documentation.",
    "created_at": "2010-09-11T11:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9835#issuecomment-97060",
    "user": "mvngu"
}
```

Good! Let's get it into the standard documentation.



---

archive/issue_comments_097061.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-11T11:07:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9835#issuecomment-97061",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097062.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T11:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9835#issuecomment-97062",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_097063.json:
```json
{
    "body": "Attachment [trac_9836-manifest.patch](tarball://root/attachments/some-uuid/ticket9836/trac_9836-manifest.patch) by mpatel created at 2010-09-16 01:01:51\n\nAdd new .png files to `MANIFEST.in`",
    "created_at": "2010-09-16T01:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9835#issuecomment-97063",
    "user": "mpatel"
}
```

Attachment [trac_9836-manifest.patch](tarball://root/attachments/some-uuid/ticket9836/trac_9836-manifest.patch) by mpatel created at 2010-09-16 01:01:51

Add new .png files to `MANIFEST.in`



---

archive/issue_comments_097064.json:
```json
{
    "body": "I've attached a patch that fixes two Sphinx warnings:\n\n```\n/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage/doc/en/thematic_tutorials/linear_programming.rst:: WARNING: image file not readable: static/lp_flot1.png\n/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage/doc/en/thematic_tutorials/linear_programming.rst:: WARNING: image file not readable: static/lp_flot2.png\n```\n",
    "created_at": "2010-09-16T02:10:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9835#issuecomment-97064",
    "user": "mpatel"
}
```

I've attached a patch that fixes two Sphinx warnings:

```
/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage/doc/en/thematic_tutorials/linear_programming.rst:: WARNING: image file not readable: static/lp_flot1.png
/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage/doc/en/thematic_tutorials/linear_programming.rst:: WARNING: image file not readable: static/lp_flot2.png
```

