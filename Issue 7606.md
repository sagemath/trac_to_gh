# Issue 7606: images not picked up when making source releases of Sage 4.3.alpha0 and 4.3.alpha1

archive/issues_007606.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @nathanncohen\n\nFrom this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/11f432ca0302189e) thread (see also [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/af1fa373245166a7)):\n\n```\n> 10. sage: hg_sage.status()\n>     Getting status of modified or unknown files:\n>     cd \"/home/SimonKing/sandbox/sage-4.3.alpha0/devel/sage\" && hg\n> status\n>     ! doc/fr/a_tour_of_sage/eigen_plot.png\n>     ! doc/fr/a_tour_of_sage/sin_plot.png\n\n> Aha! There is a problem with the docs, right? Are these files missing?\n\nYou get those two lines with the exclamation marks because the file\nMANIFEST.in in Sage 4.3.alpha0 isn't configured to pick up those two\nimage files. When ticket #7190 (French translation: A Tour of Sage)\n[1] was merged in Sage 4.3.alpha0, the file\ndevel/sage-main/MANIFEST.in wasn't also changed to take into account\nthe new image files, so these are not picked up when releasing the\nalpha0 tarball. A result is that one would not see the image files in\ndevel/sage-main/doc/fr/a_tour_of_sage. You can fix the missing files\nproblem as follows:\n\n[mvngu@sage sage-4.3.alpha0-7473-sphinx]$ cd devel/sage-main/\n[mvngu@sage sage-main]$ hg st\n! doc/fr/a_tour_of_sage/eigen_plot.png\n! doc/fr/a_tour_of_sage/sin_plot.png\n[mvngu@sage sage-main]$ hg revert -a\nreverting doc/fr/a_tour_of_sage/eigen_plot.png\nreverting doc/fr/a_tour_of_sage/sin_plot.png\n[mvngu@sage sage-main]$ hg st\n<no output>\n```\n\nThis missing files problem is due to #7190.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7606\n\n",
    "created_at": "2009-12-05T11:41:53Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "images not picked up when making source releases of Sage 4.3.alpha0 and 4.3.alpha1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7606",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

CC:  @nathanncohen

From this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/11f432ca0302189e) thread (see also [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/af1fa373245166a7)):

```
> 10. sage: hg_sage.status()
>     Getting status of modified or unknown files:
>     cd "/home/SimonKing/sandbox/sage-4.3.alpha0/devel/sage" && hg
> status
>     ! doc/fr/a_tour_of_sage/eigen_plot.png
>     ! doc/fr/a_tour_of_sage/sin_plot.png

> Aha! There is a problem with the docs, right? Are these files missing?

You get those two lines with the exclamation marks because the file
MANIFEST.in in Sage 4.3.alpha0 isn't configured to pick up those two
image files. When ticket #7190 (French translation: A Tour of Sage)
[1] was merged in Sage 4.3.alpha0, the file
devel/sage-main/MANIFEST.in wasn't also changed to take into account
the new image files, so these are not picked up when releasing the
alpha0 tarball. A result is that one would not see the image files in
devel/sage-main/doc/fr/a_tour_of_sage. You can fix the missing files
problem as follows:

[mvngu@sage sage-4.3.alpha0-7473-sphinx]$ cd devel/sage-main/
[mvngu@sage sage-main]$ hg st
! doc/fr/a_tour_of_sage/eigen_plot.png
! doc/fr/a_tour_of_sage/sin_plot.png
[mvngu@sage sage-main]$ hg revert -a
reverting doc/fr/a_tour_of_sage/eigen_plot.png
reverting doc/fr/a_tour_of_sage/sin_plot.png
[mvngu@sage sage-main]$ hg st
<no output>
```

This missing files problem is due to #7190.

Issue created by migration from https://trac.sagemath.org/ticket/7606





---

archive/issue_comments_064773.json:
```json
{
    "body": "Attachment [trac_7606-manifest.patch](tarball://root/attachments/some-uuid/ticket7606/trac_7606-manifest.patch) by mvngu created at 2009-12-05 12:37:25\n\nbased on Sage 4.3.alpha1",
    "created_at": "2009-12-05T12:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7606#issuecomment-64773",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7606-manifest.patch](tarball://root/attachments/some-uuid/ticket7606/trac_7606-manifest.patch) by mvngu created at 2009-12-05 12:37:25

based on Sage 4.3.alpha1



---

archive/issue_comments_064774.json:
```json
{
    "body": "Here are some steps to fix the problem with missing image files. On a freshly compiled Sage 4.3.alpha1 or a newly unpacked binary of that version, do a Mercurial revert to recover the deleted images:\n\n```\n[mvngu@sage sage-4.3.alpha1-7606-images]$ cd devel/sage-main/\n[mvngu@sage sage-main]$ hg st\n! doc/fr/a_tour_of_sage/eigen_plot.png\n! doc/fr/a_tour_of_sage/sin_plot.png\n[mvngu@sage sage-main]$ hg revert -a\nreverting doc/fr/a_tour_of_sage/eigen_plot.png\nreverting doc/fr/a_tour_of_sage/sin_plot.png\n[mvngu@sage sage-main]$ hg st\n<no output>\n```\n\nNext, apply the patch `trac_7606-manifest.patch`, which configures MANIFEST.in to pick up those two image files when making a source release. Afterwards, making a source tarball with \"./sage -sdist <version-number>\" should also pick up the two image files.",
    "created_at": "2009-12-05T12:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7606#issuecomment-64774",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Here are some steps to fix the problem with missing image files. On a freshly compiled Sage 4.3.alpha1 or a newly unpacked binary of that version, do a Mercurial revert to recover the deleted images:

```
[mvngu@sage sage-4.3.alpha1-7606-images]$ cd devel/sage-main/
[mvngu@sage sage-main]$ hg st
! doc/fr/a_tour_of_sage/eigen_plot.png
! doc/fr/a_tour_of_sage/sin_plot.png
[mvngu@sage sage-main]$ hg revert -a
reverting doc/fr/a_tour_of_sage/eigen_plot.png
reverting doc/fr/a_tour_of_sage/sin_plot.png
[mvngu@sage sage-main]$ hg st
<no output>
```

Next, apply the patch `trac_7606-manifest.patch`, which configures MANIFEST.in to pick up those two image files when making a source release. Afterwards, making a source tarball with "./sage -sdist <version-number>" should also pick up the two image files.



---

archive/issue_comments_064775.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-05T12:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7606#issuecomment-64775",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064776.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-12-06T06:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7606#issuecomment-64776",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_064777.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-06T06:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7606#issuecomment-64777",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
