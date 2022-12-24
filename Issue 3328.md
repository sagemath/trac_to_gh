# Issue 3328: minor fix rpy

archive/issues_003328.json:
```json
{
    "body": "Assignee: mabshoff\n\nA problem was reported to me a month or two ago and I was hit by it\nwhen I built sage-3.0.2 from scratch (rather than by sage -upgrade).\nrpy didn't build because RHOME was not defined. This may be required \nbecause I have not only sage version of R but also a system provided\nversion. After adding a line in rpy spkg-install pointing RHOME to \nSAGE_LOCAL/lib/R it did build without problem.\nHowever a test failed:\nsage -t  devel/sage/sage/stats/test.py                      **********************************************************************\nFile \"/home/francois/Work/SAGE/tmp/test.py\", line 5:\n    sage: import rpy\nException raised:\n    Traceback (most recent call last):\n      File \"/home/francois/Work/SAGE/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[1]>\", line 1, in <module>\n        import rpy###line 5:\n    sage: import rpy\n      File \"/home/francois/Work/SAGE/local/lib/python2.5/site-packages/rpy.py\", line 58, in <module>\n        RVERSION = rpy_tools.get_R_VERSION(RHOME)\n      File \"/home/francois/Work/SAGE/local/lib/python2.5/site-packages/rpy_tools.py\", line 99, in get_R_VERSION\n        \" `%s'.\\n\" % rexec )\n    RuntimeError: Couldn't execute the R interpreter `/usr/lib/R/bin/R'.\n\n================\nAs one can see sage's rpy was trying to use the system provided R rather\nthan sage's own. An extra line in sage-env  took care of that.\n2 small patch attached to cover this corner case. Note that the patches\nwon't make any difference to people not affected by this issue.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3328\n\n",
    "created_at": "2008-05-29T09:38:16Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "minor fix rpy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3328",
    "user": "fbissey"
}
```
Assignee: mabshoff

A problem was reported to me a month or two ago and I was hit by it
when I built sage-3.0.2 from scratch (rather than by sage -upgrade).
rpy didn't build because RHOME was not defined. This may be required 
because I have not only sage version of R but also a system provided
version. After adding a line in rpy spkg-install pointing RHOME to 
SAGE_LOCAL/lib/R it did build without problem.
However a test failed:
sage -t  devel/sage/sage/stats/test.py                      **********************************************************************
File "/home/francois/Work/SAGE/tmp/test.py", line 5:
    sage: import rpy
Exception raised:
    Traceback (most recent call last):
      File "/home/francois/Work/SAGE/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[1]>", line 1, in <module>
        import rpy###line 5:
    sage: import rpy
      File "/home/francois/Work/SAGE/local/lib/python2.5/site-packages/rpy.py", line 58, in <module>
        RVERSION = rpy_tools.get_R_VERSION(RHOME)
      File "/home/francois/Work/SAGE/local/lib/python2.5/site-packages/rpy_tools.py", line 99, in get_R_VERSION
        " `%s'.\n" % rexec )
    RuntimeError: Couldn't execute the R interpreter `/usr/lib/R/bin/R'.

================
As one can see sage's rpy was trying to use the system provided R rather
than sage's own. An extra line in sage-env  took care of that.
2 small patch attached to cover this corner case. Note that the patches
won't make any difference to people not affected by this issue.

Issue created by migration from https://trac.sagemath.org/ticket/3328





---

archive/issue_comments_023079.json:
```json
{
    "body": "Attachment [spkg-install.patch](tarball://root/attachments/some-uuid/ticket3328/spkg-install.patch) by fbissey created at 2008-05-29 09:38:48",
    "created_at": "2008-05-29T09:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3328#issuecomment-23079",
    "user": "fbissey"
}
```

Attachment [spkg-install.patch](tarball://root/attachments/some-uuid/ticket3328/spkg-install.patch) by fbissey created at 2008-05-29 09:38:48



---

archive/issue_comments_023080.json:
```json
{
    "body": "Attachment [sage-env.patch](tarball://root/attachments/some-uuid/ticket3328/sage-env.patch) by fbissey created at 2008-05-29 09:39:18",
    "created_at": "2008-05-29T09:39:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3328#issuecomment-23080",
    "user": "fbissey"
}
```

Attachment [sage-env.patch](tarball://root/attachments/some-uuid/ticket3328/sage-env.patch) by fbissey created at 2008-05-29 09:39:18



---

archive/issue_comments_023081.json:
```json
{
    "body": "Hi Francois,\n\nthanks for the patches, we already had a ticket for this issue at #3011, so I am closing that as a duplicate. Please make sure in the future that you add \"[with patch, needs review]\" line to the Summary field and also assign a default milestone so your patch isn't slipping through the cracks. I will review this patch shortly, but it looks good as is :)\n\nCheers,\n\nMichaek",
    "created_at": "2008-05-29T11:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3328#issuecomment-23081",
    "user": "mabshoff"
}
```

Hi Francois,

thanks for the patches, we already had a ticket for this issue at #3011, so I am closing that as a duplicate. Please make sure in the future that you add "[with patch, needs review]" line to the Summary field and also assign a default milestone so your patch isn't slipping through the cracks. I will review this patch shortly, but it looks good as is :)

Cheers,

Michaek



---

archive/issue_comments_023082.json:
```json
{
    "body": "Ok, both patches look good. A couple remarks:\n\n* please post proper mercurial patches. I committed the patches in your name, but it would make applying future patches easier\n* be precise, i.e. spkg-install is for the rpy.spkg - it tool me some time to figure that out. \n\nAn updated r.spkg containing all your fixes [and some more things by me like updated SPKG.txt] is available at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha1/r-2.6.1.p17.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-05-29T14:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3328#issuecomment-23082",
    "user": "mabshoff"
}
```

Ok, both patches look good. A couple remarks:

* please post proper mercurial patches. I committed the patches in your name, but it would make applying future patches easier
* be precise, i.e. spkg-install is for the rpy.spkg - it tool me some time to figure that out. 

An updated r.spkg containing all your fixes [and some more things by me like updated SPKG.txt] is available at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha1/r-2.6.1.p17.spkg

Cheers,

Michael



---

archive/issue_comments_023083.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha1",
    "created_at": "2008-05-29T14:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3328#issuecomment-23083",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha1



---

archive/issue_comments_023084.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-29T14:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3328#issuecomment-23084",
    "user": "mabshoff"
}
```

Resolution: fixed
