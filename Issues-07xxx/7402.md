# Issue 7402: SageNB -- Use `pkg_resources` to locate `DATA` directory

archive/issues_007402.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @qed777\n\nKeywords: sagenb notebook\n\n[`pkg_resources`](http://peak.telecommunity.com/DevCenter/PkgResources) is the official way to access data directories in a `setuptools` package. Using `pkg_resources` to locate the `DATA` directory will allow us to use [`.pth` files](http://bob.pythonmac.org/archives/2005/02/06/using-pth-files-for-python-development/) for ease of development. For example:\n\n```\n$ pwd\n/home/timdumol/devel/sagenb-0.3.5/src\n$ dev_dir=`pwd`\n$ cd /opt/sage/local/lib/python2.6/site-packages/\n$ rm -r sagenb*\n$ cat \"$dev_dir\" > sagenb.pth\n```\n\nThus, there will no longer be a need to `sage -python setup.py install` after every change.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7402\n\n",
    "closed_at": "2009-12-08T05:33:36Z",
    "created_at": "2009-11-06T11:24:02Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "SageNB -- Use `pkg_resources` to locate `DATA` directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7402",
    "user": "https://github.com/TimDumol"
}
```
Assignee: boothby

CC:  @qed777

Keywords: sagenb notebook

[`pkg_resources`](http://peak.telecommunity.com/DevCenter/PkgResources) is the official way to access data directories in a `setuptools` package. Using `pkg_resources` to locate the `DATA` directory will allow us to use [`.pth` files](http://bob.pythonmac.org/archives/2005/02/06/using-pth-files-for-python-development/) for ease of development. For example:

```
$ pwd
/home/timdumol/devel/sagenb-0.3.5/src
$ dev_dir=`pwd`
$ cd /opt/sage/local/lib/python2.6/site-packages/
$ rm -r sagenb*
$ cat "$dev_dir" > sagenb.pth
```

Thus, there will no longer be a need to `sage -python setup.py install` after every change.

Issue created by migration from https://trac.sagemath.org/ticket/7402





---

archive/issue_comments_062165.json:
```json
{
    "body": "Uses `pkg_resources` to locate the DATA directory.",
    "created_at": "2009-11-06T11:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7402#issuecomment-62165",
    "user": "https://github.com/TimDumol"
}
```

Uses `pkg_resources` to locate the DATA directory.



---

archive/issue_comments_062166.json:
```json
{
    "body": "Attachment [trac_7402-pkg_resources.patch](tarball://root/attachments/some-uuid/ticket7402/trac_7402-pkg_resources.patch) by @TimDumol created at 2009-11-06 11:31:18\n\nThis patch should do it.\n\nAs a note, we won't even need to restart the server if all we edit are template files. A big plus in ease of development, IMHO.",
    "created_at": "2009-11-06T11:31:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7402#issuecomment-62166",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7402-pkg_resources.patch](tarball://root/attachments/some-uuid/ticket7402/trac_7402-pkg_resources.patch) by @TimDumol created at 2009-11-06 11:31:18

This patch should do it.

As a note, we won't even need to restart the server if all we edit are template files. A big plus in ease of development, IMHO.



---

archive/issue_comments_062167.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-06T11:31:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7402#issuecomment-62167",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062168.json:
```json
{
    "body": "Changing keywords from \"\" to \"sagenb notebook\".",
    "created_at": "2009-11-06T11:31:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7402#issuecomment-62168",
    "user": "https://github.com/TimDumol"
}
```

Changing keywords from "" to "sagenb notebook".



---

archive/issue_comments_062169.json:
```json
{
    "body": "This works for me.  In particular, the Se test suite is oblivious to the change.\n\nFor me, an existing `site-packages/sagenb` takes precedence over `sagenb.pth`.  Short of deleting the former, can we reverse this?  How about a flag (e.g, `--dev-mode` or `--in-source`) to `sage -python setup.py install` that toggles between \"standard\" and \"developer\" modes?",
    "created_at": "2009-11-13T23:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7402#issuecomment-62169",
    "user": "https://github.com/qed777"
}
```

This works for me.  In particular, the Se test suite is oblivious to the change.

For me, an existing `site-packages/sagenb` takes precedence over `sagenb.pth`.  Short of deleting the former, can we reverse this?  How about a flag (e.g, `--dev-mode` or `--in-source`) to `sage -python setup.py install` that toggles between "standard" and "developer" modes?



---

archive/issue_comments_062170.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-13T23:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7402#issuecomment-62170",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062171.json:
```json
{
    "body": "A Sphinx warning to keep in mind:\n\n```\ncopying static files... WARNING: static directory '/home/apps/sage/local/lib/python/site-packages/sagenb/data/jsmath/' does not exist\n```",
    "created_at": "2009-11-14T00:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7402#issuecomment-62171",
    "user": "https://github.com/qed777"
}
```

A Sphinx warning to keep in mind:

```
copying static files... WARNING: static directory '/home/apps/sage/local/lib/python/site-packages/sagenb/data/jsmath/' does not exist
```



---

archive/issue_comments_062172.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> A Sphinx warning to keep in mind:\n> \n> ```\n> copying static files... WARNING: static directory '/home/apps/sage/local/lib/python/site-packages/sagenb/data/jsmath/' does not exist\n> ```\n\nSince this is only used for development, I don't think there's much of a problem. It should be possible to fix by making Sphinx read the .pth file and look there, but I am inexperienced regarding that.\n\nRegards the --dev-mode thing, I just noticed that SageNB uses disttools, not setuptools, which is why the `sage -python setup.py develop` command does not exist. This is now #7467.",
    "created_at": "2009-11-15T05:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7402#issuecomment-62172",
    "user": "https://github.com/TimDumol"
}
```

Replying to [comment:3 mpatel]:
> A Sphinx warning to keep in mind:
> 
> ```
> copying static files... WARNING: static directory '/home/apps/sage/local/lib/python/site-packages/sagenb/data/jsmath/' does not exist
> ```

Since this is only used for development, I don't think there's much of a problem. It should be possible to fix by making Sphinx read the .pth file and look there, but I am inexperienced regarding that.

Regards the --dev-mode thing, I just noticed that SageNB uses disttools, not setuptools, which is why the `sage -python setup.py develop` command does not exist. This is now #7467.



---

archive/issue_events_017514.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-12-08T05:33:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7402",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7402#event-17514"
}
```



---

archive/issue_comments_062173.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-08T05:33:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7402#issuecomment-62173",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
