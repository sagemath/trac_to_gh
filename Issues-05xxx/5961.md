# Issue 5961: Document potential interference issues with ~/.pydistutils.cfg

archive/issues_005961.json:
```json
{
    "body": "Assignee: tba\n\nSee https://groups.google.com/group/sage-devel/browse_thread/thread/2cee11b068180497\n\n```\nDear Sage developers,\n\nI tried to build Sage-3.4 on my intel macbook (Mac OS X 10.4.11).  I\nhave Xcode 2.5 installed and gcc-4.0.1. I downloaded the sage-3.4.tar,\nuntarred it and ran make. I have macports installed so changed the PATH\nto remove anything from /opt.  I also renamed /opt to something else in\none attempt but both failed with the same error:\n\n-------------\n[...]\nSleeping for three seconds before testing python\nTraceback (most recent call last):\n   File \"<string>\", line 1, in <module>\n   File \"/Users/prabhu/src/build/sage-3.4/local/lib/python2.5/md5.py\",\nline 6, in <module>\n     from hashlib import md5\n   File\n\"/Users/prabhu/src/build/sage-3.4/local/lib/python2.5/hashlib.py\", line\n133, in <module>\n     md5 = __get_builtin_constructor('md5')\n   File\n\"/Users/prabhu/src/build/sage-3.4/local/lib/python2.5/hashlib.py\", line\n60, in __get_builtin_constructor\n     import _md5\nImportError: No module named _md5\nmd5 module failed to import\n[...]\nsage: An error occurred while installing python-2.5.2.p9\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /Users/prabhu/src/build/sage-3.4/install.log.  Describe your\ncomputer, operating system, etc.\n\n-----------------\n\nSearching the lists for this gave me this:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/e2fcb3...\n\nwhich isn't very helpful.\n\nAfter spending a little while figuring out what is wrong I realize that\nI've done something a little non-standard that broke things.  I have\na default ~/.pydistutils.cfg which reads like so:\n\n[install]\ninstall_lib = ~/Library/Python/$py_version_short/site-packages\ninstall_scripts = ~/usr/bin\n\nI completely forgot about this and my install logs indicated a large\nnumber of files being installed in the `install_lib` directory. So\nmoving this .pydistutils.cfg out of the way helped resolve the problem\nand the build went well.\n\nI think this should be documented somewhere so others don't fall into\nthe same trap.  Thanks.\n\ncheers,\nprabhu \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5961\n\n",
    "closed_at": "2015-01-13T01:14:12Z",
    "created_at": "2009-05-02T06:39:51Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Document potential interference issues with ~/.pydistutils.cfg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5961",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: tba

See https://groups.google.com/group/sage-devel/browse_thread/thread/2cee11b068180497

```
Dear Sage developers,

I tried to build Sage-3.4 on my intel macbook (Mac OS X 10.4.11).  I
have Xcode 2.5 installed and gcc-4.0.1. I downloaded the sage-3.4.tar,
untarred it and ran make. I have macports installed so changed the PATH
to remove anything from /opt.  I also renamed /opt to something else in
one attempt but both failed with the same error:

-------------
[...]
Sleeping for three seconds before testing python
Traceback (most recent call last):
   File "<string>", line 1, in <module>
   File "/Users/prabhu/src/build/sage-3.4/local/lib/python2.5/md5.py",
line 6, in <module>
     from hashlib import md5
   File
"/Users/prabhu/src/build/sage-3.4/local/lib/python2.5/hashlib.py", line
133, in <module>
     md5 = __get_builtin_constructor('md5')
   File
"/Users/prabhu/src/build/sage-3.4/local/lib/python2.5/hashlib.py", line
60, in __get_builtin_constructor
     import _md5
ImportError: No module named _md5
md5 module failed to import
[...]
sage: An error occurred while installing python-2.5.2.p9
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/prabhu/src/build/sage-3.4/install.log.  Describe your
computer, operating system, etc.

-----------------

Searching the lists for this gave me this:

http://groups.google.com/group/sage-devel/browse_thread/thread/e2fcb3...

which isn't very helpful.

After spending a little while figuring out what is wrong I realize that
I've done something a little non-standard that broke things.  I have
a default ~/.pydistutils.cfg which reads like so:

[install]
install_lib = ~/Library/Python/$py_version_short/site-packages
install_scripts = ~/usr/bin

I completely forgot about this and my install logs indicated a large
number of files being installed in the `install_lib` directory. So
moving this .pydistutils.cfg out of the way helped resolve the problem
and the build went well.

I think this should be documented somewhere so others don't fall into
the same trap.  Thanks.

cheers,
prabhu 
```

Issue created by migration from https://trac.sagemath.org/ticket/5961





---

archive/issue_events_013977.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5961",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5961#event-13977"
}
```



---

archive/issue_events_013978.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5961",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5961#event-13978"
}
```



---

archive/issue_events_013979.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5961",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5961#event-13979"
}
```



---

archive/issue_events_013980.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5961",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5961#event-13980"
}
```



---

archive/issue_events_013981.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5961",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5961#event-13981"
}
```



---

archive/issue_events_013982.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5961",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5961#event-13982"
}
```



---

archive/issue_events_013983.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5961",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5961#event-13983"
}
```



---

archive/issue_comments_047119.json:
```json
{
    "body": "This is a dup of #9536.",
    "created_at": "2015-01-05T16:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5961#issuecomment-47119",
    "user": "https://github.com/kcrisman"
}
```

This is a dup of #9536.



---

archive/issue_comments_047120.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-01-05T16:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5961#issuecomment-47120",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_047121.json:
```json
{
    "body": "Not that that one has had much activity lately either, but it has an actual patch and some conversation.",
    "created_at": "2015-01-05T16:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5961#issuecomment-47121",
    "user": "https://github.com/kcrisman"
}
```

Not that that one has had much activity lately either, but it has an actual patch and some conversation.



---

archive/issue_comments_047122.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-01-05T16:13:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5961#issuecomment-47122",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_013984.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-01-13T01:14:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5961",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5961#event-13984"
}
```



---

archive/issue_comments_047123.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2015-01-13T01:14:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5961",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5961#issuecomment-47123",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate
