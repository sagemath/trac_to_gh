# Issue 2873: Customize JMOL menu

archive/issues_002873.json:
```json
{
    "body": "Assignee: was\n\nIt would be nice to shorten the menu quite a bit and pick the options that make sense to us.\n\nSee http://chemapps.stolaf.edu/jmol/docs/examples-11/new4.htm point 13 for how to do this.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2873\n\n",
    "created_at": "2008-04-10T22:42:45Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "Customize JMOL menu",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2873",
    "user": "jason"
}
```
Assignee: was

It would be nice to shorten the menu quite a bit and pick the options that make sense to us.

See http://chemapps.stolaf.edu/jmol/docs/examples-11/new4.htm point 13 for how to do this.



Issue created by migration from https://trac.sagemath.org/ticket/2873





---

archive/issue_comments_019733.json:
```json
{
    "body": "See also the very nice writeup at http://wiki.jmol.org:81/index.php/Custom_Menus",
    "created_at": "2009-02-13T21:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19733",
    "user": "jason"
}
```

See also the very nice writeup at http://wiki.jmol.org:81/index.php/Custom_Menus



---

archive/issue_comments_019734.json:
```json
{
    "body": "Whoever fixes this, please make sure that #1777 is taken care of (which can be fixed by this ticket, I believe).",
    "created_at": "2009-02-13T21:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19734",
    "user": "jason"
}
```

Whoever fixes this, please make sure that #1777 is taken care of (which can be fixed by this ticket, I believe).



---

archive/issue_comments_019735.json:
```json
{
    "body": "Attachment [jmol-custom-menu.patch](tarball://root/attachments/some-uuid/ticket2873/jmol-custom-menu.patch) by jason created at 2009-02-14 09:48:17",
    "created_at": "2009-02-14T09:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19735",
    "user": "jason"
}
```

Attachment [jmol-custom-menu.patch](tarball://root/attachments/some-uuid/ticket2873/jmol-custom-menu.patch) by jason created at 2009-02-14 09:48:17



---

archive/issue_comments_019736.json:
```json
{
    "body": "We need both a patch and a new spkg (which contains the custom menu file).  The spkg is up at http://sage.math.washington.edu/home/jason/jmol-11.6.16.spkg (I took the opportunity to update to the latest jmol stable version).",
    "created_at": "2009-02-14T09:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19736",
    "user": "jason"
}
```

We need both a patch and a new spkg (which contains the custom menu file).  The spkg is up at http://sage.math.washington.edu/home/jason/jmol-11.6.16.spkg (I took the opportunity to update to the latest jmol stable version).



---

archive/issue_comments_019737.json:
```json
{
    "body": "This patch and spkg take care of #1777 too.",
    "created_at": "2009-02-14T10:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19737",
    "user": "jason"
}
```

This patch and spkg take care of #1777 too.



---

archive/issue_comments_019738.json:
```json
{
    "body": "Changing assignee from was to jason.",
    "created_at": "2009-02-14T10:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19738",
    "user": "jason"
}
```

Changing assignee from was to jason.



---

archive/issue_comments_019739.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-14T10:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19739",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019740.json:
```json
{
    "body": "The spkg is **not** based in the latest jmol.spkg in tree and is missing fixes to spkg-install. Bad Jason :)\n\nTimothy: **always** check the repo and verify that it is based on the previous spkg.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T13:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19740",
    "user": "mabshoff"
}
```

The spkg is **not** based in the latest jmol.spkg in tree and is missing fixes to spkg-install. Bad Jason :)

Timothy: **always** check the repo and verify that it is based on the previous spkg.

Cheers,

Michael



---

archive/issue_comments_019741.json:
```json
{
    "body": "I will put up a new jmol spkg at #5271.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T14:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19741",
    "user": "mabshoff"
}
```

I will put up a new jmol spkg at #5271.

Cheers,

Michael



---

archive/issue_comments_019742.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-14T14:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19742",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019743.json:
```json
{
    "body": "Merged jmol-custom-menu.patch in Sage 3.3.rc1. \n\nNote that the spkg above was **not** merged, but the one at #5271.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T14:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2873",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2873#issuecomment-19743",
    "user": "mabshoff"
}
```

Merged jmol-custom-menu.patch in Sage 3.3.rc1. 

Note that the spkg above was **not** merged, but the one at #5271.

Cheers,

Michael
