# Issue 7459: sage virtualbox -- install imagemagick

archive/issues_007459.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  kcrisman\n\nWhen we make the virtualbox sage image for sage-4.2.1, do the following:\n\n\n```\nThe easiest way is :\n\n1) Within VirtualBox, use the integrated web navigator SeaMonkey to go\nat :\n\nhttp://www.murga-linux.com/puppy/viewtopic.php?t=45981\n\n2) download the two packages :\nImageMagick-6.5.6-10.pet\nImageMagick_DEV-6.5.6-10.pet\n\nand in dialog, choose : open with petget\n\n3) installation is automatic.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7459\n\n",
    "created_at": "2009-11-14T17:56:37Z",
    "labels": [
        "distribution",
        "major",
        "enhancement"
    ],
    "title": "sage virtualbox -- install imagemagick",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7459",
    "user": "was"
}
```
Assignee: tbd

CC:  kcrisman

When we make the virtualbox sage image for sage-4.2.1, do the following:


```
The easiest way is :

1) Within VirtualBox, use the integrated web navigator SeaMonkey to go
at :

http://www.murga-linux.com/puppy/viewtopic.php?t=45981

2) download the two packages :
ImageMagick-6.5.6-10.pet
ImageMagick_DEV-6.5.6-10.pet

and in dialog, choose : open with petget

3) installation is automatic.
```


Issue created by migration from https://trac.sagemath.org/ticket/7459





---

archive/issue_comments_062831.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-02T12:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7459#issuecomment-62831",
    "user": "vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062832.json:
```json
{
    "body": "The current virtual machine contains ImageMagick and I just tested that creating of an animated gif works as expected. Also, for future reference note that you don't need ImageMagick-dev since we just call the executable.\n\nTicket can be closed.",
    "created_at": "2012-06-02T12:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7459#issuecomment-62832",
    "user": "vbraun"
}
```

The current virtual machine contains ImageMagick and I just tested that creating of an animated gif works as expected. Also, for future reference note that you don't need ImageMagick-dev since we just call the executable.

Ticket can be closed.



---

archive/issue_comments_062833.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-02T12:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7459#issuecomment-62833",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062834.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-06-02T13:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7459#issuecomment-62834",
    "user": "jdemeyer"
}
```

Resolution: worksforme
