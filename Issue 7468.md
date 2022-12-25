# Issue 7468: SageNB - Include `zope.testbrowser` and its dependencies in the SageNB package

archive/issues_007468.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @qed777\n\nThis package will be used for future testing. Adding another package to a package was also done with the Trac package.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7468\n\n",
    "created_at": "2009-11-15T07:26:48Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "SageNB - Include `zope.testbrowser` and its dependencies in the SageNB package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7468",
    "user": "https://github.com/TimDumol"
}
```
Assignee: boothby

CC:  @qed777

This package will be used for future testing. Adding another package to a package was also done with the Trac package.

Issue created by migration from https://trac.sagemath.org/ticket/7468





---

archive/issue_comments_062785.json:
```json
{
    "body": "Adds `zope.testbrowser` to the package's dependencies and makes `spkg-dist` automatically download the dependencies. Depends on #7467",
    "created_at": "2009-11-15T07:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7468#issuecomment-62785",
    "user": "https://github.com/TimDumol"
}
```

Adds `zope.testbrowser` to the package's dependencies and makes `spkg-dist` automatically download the dependencies. Depends on #7467



---

archive/issue_comments_062786.json:
```json
{
    "body": "Attachment [trac_7468-zope.testbrowser.patch](tarball://root/attachments/some-uuid/ticket7468/trac_7468-zope.testbrowser.patch) by @TimDumol created at 2009-11-15 07:31:10\n\nThis should do the trick.",
    "created_at": "2009-11-15T07:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7468#issuecomment-62786",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7468-zope.testbrowser.patch](tarball://root/attachments/some-uuid/ticket7468/trac_7468-zope.testbrowser.patch) by @TimDumol created at 2009-11-15 07:31:10

This should do the trick.



---

archive/issue_comments_062787.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-15T07:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7468#issuecomment-62787",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062788.json:
```json
{
    "body": "Is zope.testbrowser (or does it appear to be) sufficiently powerful to implement a [nearly] complete Sage Remote Access API (cf. [comment:24:ticket:7343 this comment] at #7343)?  \n\nProgrammatic possibilities: login/out; create, archive, delete, rename, share, up/download, publish worksheets; add/remove data files.",
    "created_at": "2009-11-26T14:30:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7468#issuecomment-62788",
    "user": "https://github.com/qed777"
}
```

Is zope.testbrowser (or does it appear to be) sufficiently powerful to implement a [nearly] complete Sage Remote Access API (cf. [comment:24:ticket:7343 this comment] at #7343)?  

Programmatic possibilities: login/out; create, archive, delete, rename, share, up/download, publish worksheets; add/remove data files.



---

archive/issue_comments_062789.json:
```json
{
    "body": "This patch is *totally unacceptable* as is.  The problem is this:\n\n(1) Turn off your internet connection, then\n\n(2) Try doing \"sage -python setup.py install\", and you get\n\n```\n...\nReading http://pypi.python.org/simple/zope.testbrowser/\nDownload error: [Errno 8] nodename nor servname provided, or not known -- Some packages may not be found!\nReading http://pypi.python.org/simple/zope.testbrowser/\nDownload error: [Errno 8] nodename nor servname provided, or not known -- Some packages may not be found!\nCouldn't find index page for 'zope.testbrowser' (maybe misspelled?)\nScanning index of all packages (this may take a while)\nReading http://pypi.python.org/simple/\nDownload error: [Errno 8] nodename nor servname provided, or not known -- Some packages may not be found!\nNo local packages or download links found for zope.testbrowser>=3.7.0a1\nerror: Could not find suitable distribution for Requirement.parse('zope.testbrowser>=3.7.0a1')\n```\n\nNow imagine that you're building Sage from source on an airplane, or while camping, or working at a job which for security reasons doesn't allow outside network connections.\n\nOptions:\n\n(1) Get zope.testbrowser included as a standard sage package. \n\n(2) Make the dependency on zope.testbrowser optional.  \n\n -- william",
    "created_at": "2009-12-08T21:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7468#issuecomment-62789",
    "user": "https://github.com/williamstein"
}
```

This patch is *totally unacceptable* as is.  The problem is this:

(1) Turn off your internet connection, then

(2) Try doing "sage -python setup.py install", and you get

```
...
Reading http://pypi.python.org/simple/zope.testbrowser/
Download error: [Errno 8] nodename nor servname provided, or not known -- Some packages may not be found!
Reading http://pypi.python.org/simple/zope.testbrowser/
Download error: [Errno 8] nodename nor servname provided, or not known -- Some packages may not be found!
Couldn't find index page for 'zope.testbrowser' (maybe misspelled?)
Scanning index of all packages (this may take a while)
Reading http://pypi.python.org/simple/
Download error: [Errno 8] nodename nor servname provided, or not known -- Some packages may not be found!
No local packages or download links found for zope.testbrowser>=3.7.0a1
error: Could not find suitable distribution for Requirement.parse('zope.testbrowser>=3.7.0a1')
```

Now imagine that you're building Sage from source on an airplane, or while camping, or working at a job which for security reasons doesn't allow outside network connections.

Options:

(1) Get zope.testbrowser included as a standard sage package. 

(2) Make the dependency on zope.testbrowser optional.  

 -- william



---

archive/issue_comments_062790.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-08T21:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7468#issuecomment-62790",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_062791.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-09T11:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7468#issuecomment-62791",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062792.json:
```json
{
    "body": "I have edited the `spkg-dist` file, which I believe is used for creating the sagenb spkg, in this patch to automatically download zope.testbrowser and its dependencies, and include it in the spkg. Thus, installing through `sage -i sagenb` or `spkg-install` should not require internet access. Inclusion of package dependencies is also done in the Twisted package (zope.interface) and in the Trac package (Genshi).\n\nPlease correct me if I am mistaken, though.",
    "created_at": "2009-12-09T11:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7468#issuecomment-62792",
    "user": "https://github.com/TimDumol"
}
```

I have edited the `spkg-dist` file, which I believe is used for creating the sagenb spkg, in this patch to automatically download zope.testbrowser and its dependencies, and include it in the spkg. Thus, installing through `sage -i sagenb` or `spkg-install` should not require internet access. Inclusion of package dependencies is also done in the Twisted package (zope.interface) and in the Trac package (Genshi).

Please correct me if I am mistaken, though.



---

archive/issue_comments_062793.json:
```json
{
    "body": "> Please correct me if I am mistaken, though. \n\n\nNo, that should be fine, and is probably a good idea.     Can you post your edited spkg-dist file?",
    "created_at": "2009-12-09T14:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7468#issuecomment-62793",
    "user": "https://github.com/williamstein"
}
```

> Please correct me if I am mistaken, though. 


No, that should be fine, and is probably a good idea.     Can you post your edited spkg-dist file?



---

archive/issue_comments_062794.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-09T14:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7468#issuecomment-62794",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062795.json:
```json
{
    "body": "Oops, I stupidly missed that you had already done that 3 weeks ago!  Thanks for teaching me setuptools. :-)  This indeed looks fine.",
    "created_at": "2009-12-09T14:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7468#issuecomment-62795",
    "user": "https://github.com/williamstein"
}
```

Oops, I stupidly missed that you had already done that 3 weeks ago!  Thanks for teaching me setuptools. :-)  This indeed looks fine.



---

archive/issue_comments_062796.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-04T06:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7468#issuecomment-62796",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_017699.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-01-04T06:59:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7468",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7468#event-17699"
}
```



---

archive/issue_comments_062797.json:
```json
{
    "body": "Merged into sagenb-0.4.8.",
    "created_at": "2010-01-04T06:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7468#issuecomment-62797",
    "user": "https://github.com/williamstein"
}
```

Merged into sagenb-0.4.8.
