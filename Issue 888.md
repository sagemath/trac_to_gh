# Issue 888: 2.8.7-alpha0: doctest failure in dsage/tests/testdoc.py (requires previous dsage setup)

archive/issues_000888.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nFile \"testdoc.py\", line 12:\n    age: d = DSage(port=port, ssl=False)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/cwitty/pre-sage/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[5]>\", line 1, in <module>\n        d = DSage(port=port, ssl=False)###line 12:\n    age: d = DSage(port=port, ssl=False)\n      File \"/home/cwitty/pre-sage/local/lib/python/site-packages/sage/dsage/all.py\", line 52, in DSage\n        ssl=ssl)\n      File \"/home/cwitty/pre-sage/local/lib/python/site-packages/sage/dsage/interface/dsage_interface.py\", line 392, in __init__\n        self.pubkey_str = keys.getPublicKeyString(filename=self.pubkey_file)\n      File \"/home/cwitty/pre-sage/local/lib/python2.5/site-packages/twisted/conch/ssh/keys.py\", line 48, in getPublicKeyString\n        lines = open(filename).readlines()\n    IOError: [Errno 2] No such file or directory: '/home/cwitty/.sage/dsage/dsage_key.pub'\n```\n\n\n(The last line is the most interesting.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/888\n\n",
    "created_at": "2007-10-13T20:36:32Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "2.8.7-alpha0: doctest failure in dsage/tests/testdoc.py (requires previous dsage setup)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/888",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein


```
File "testdoc.py", line 12:
    age: d = DSage(port=port, ssl=False)
Exception raised:
    Traceback (most recent call last):
      File "/home/cwitty/pre-sage/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[5]>", line 1, in <module>
        d = DSage(port=port, ssl=False)###line 12:
    age: d = DSage(port=port, ssl=False)
      File "/home/cwitty/pre-sage/local/lib/python/site-packages/sage/dsage/all.py", line 52, in DSage
        ssl=ssl)
      File "/home/cwitty/pre-sage/local/lib/python/site-packages/sage/dsage/interface/dsage_interface.py", line 392, in __init__
        self.pubkey_str = keys.getPublicKeyString(filename=self.pubkey_file)
      File "/home/cwitty/pre-sage/local/lib/python2.5/site-packages/twisted/conch/ssh/keys.py", line 48, in getPublicKeyString
        lines = open(filename).readlines()
    IOError: [Errno 2] No such file or directory: '/home/cwitty/.sage/dsage/dsage_key.pub'
```


(The last line is the most interesting.)

Issue created by migration from https://trac.sagemath.org/ticket/888





---

archive/issue_comments_005460.json:
```json
{
    "body": "I've disabled dsage doctesting for that file for sage-2.8.7, and moved this to 2.8.8.",
    "created_at": "2007-10-14T05:12:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5460",
    "user": "https://github.com/williamstein"
}
```

I've disabled dsage doctesting for that file for sage-2.8.7, and moved this to 2.8.8.



---

archive/issue_events_002464.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-14T05:12:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/888#event-2464"
}
```



---

archive/issue_comments_005461.json:
```json
{
    "body": "I reassigned this bug to me so I don't lose track of it.  I will fix this one ASAP.  \nPlease reassign DSAGE related bugs to me in the future so they will show up under \"My Active Tickets\" for me.",
    "created_at": "2007-10-19T06:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5461",
    "user": "https://github.com/yqiang"
}
```

I reassigned this bug to me so I don't lose track of it.  I will fix this one ASAP.  
Please reassign DSAGE related bugs to me in the future so they will show up under "My Active Tickets" for me.



---

archive/issue_comments_005462.json:
```json
{
    "body": "Changing assignee from @williamstein to @yqiang.",
    "created_at": "2007-10-19T06:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5462",
    "user": "https://github.com/yqiang"
}
```

Changing assignee from @williamstein to @yqiang.



---

archive/issue_events_002465.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-19T16:13:21Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "milestone": "sage-2.8.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/888#event-2465"
}
```



---

archive/issue_events_002466.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-10-29T07:51:38Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "milestone": "sage-2.8.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/888#event-2466"
}
```



---

archive/issue_comments_005463.json:
```json
{
    "body": "I've turned off doctesting of this file until Yi's resolve the issue.\n\nWilliam",
    "created_at": "2007-11-07T05:24:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5463",
    "user": "https://github.com/williamstein"
}
```

I've turned off doctesting of this file until Yi's resolve the issue.

William



---

archive/issue_comments_005464.json:
```json
{
    "body": "WAIT -- requiring that dsage.setup() has been run is *not* an unreasonable requirement\nbefore doctesting.    How else can we expect to truly doctest that dsage work and have\nit eventually appear in examples all over the place, etc.?\n\nTo resolve this ticket, we just need to require dsage setup has been run, say at the\nbeginning of doing \"make test\".",
    "created_at": "2007-11-07T05:30:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5464",
    "user": "https://github.com/williamstein"
}
```

WAIT -- requiring that dsage.setup() has been run is *not* an unreasonable requirement
before doctesting.    How else can we expect to truly doctest that dsage work and have
it eventually appear in examples all over the place, etc.?

To resolve this ticket, we just need to require dsage setup has been run, say at the
beginning of doing "make test".



---

archive/issue_comments_005465.json:
```json
{
    "body": "By the way, I think dsage.setup() should either fail completely or print a huge warning if the openssl Linux package isn't installed, since then it takes *minutes* to generate a key (using gnutls).  It might be that the new gpl v3 only gnutls fixes this crap.  But we have to wait for singular to update their license first to find out.",
    "created_at": "2007-11-07T05:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5465",
    "user": "https://github.com/williamstein"
}
```

By the way, I think dsage.setup() should either fail completely or print a huge warning if the openssl Linux package isn't installed, since then it takes *minutes* to generate a key (using gnutls).  It might be that the new gpl v3 only gnutls fixes this crap.  But we have to wait for singular to update their license first to find out.



---

archive/issue_comments_005466.json:
```json
{
    "body": "Just for clarity -- I *have* turned doctesting this file off in this sage release.\nBut I think the right solution is to require dsage.setup(), and to make it clear\nto the user how to do that...",
    "created_at": "2007-11-07T05:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5466",
    "user": "https://github.com/williamstein"
}
```

Just for clarity -- I *have* turned doctesting this file off in this sage release.
But I think the right solution is to require dsage.setup(), and to make it clear
to the user how to do that...



---

archive/issue_comments_005467.json:
```json
{
    "body": "Since we will update to GNUTLS 2.2.0 (see #1622) soon we should revisit this issue.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-29T17:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5467",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Since we will update to GNUTLS 2.2.0 (see #1622) soon we should revisit this issue.

Cheers,

Michael



---

archive/issue_comments_005468.json:
```json
{
    "body": "Ok, it's easy enough to check that dsage.setup() has been run (i.e. check that DOT_SAGE/dsage exists).  Where should this check go?",
    "created_at": "2007-12-30T00:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5468",
    "user": "https://github.com/yqiang"
}
```

Ok, it's easy enough to check that dsage.setup() has been run (i.e. check that DOT_SAGE/dsage exists).  Where should this check go?



---

archive/issue_events_002467.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-21T23:39:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/888#event-2467"
}
```



---

archive/issue_comments_005469.json:
```json
{
    "body": "According to yi the issue has been fixed:\n\n```\n[00:09] <mabshoff> yi: what is the status of #888 - is that fixed by any chance?\n[00:09] <yi> mabshoff: yes, please close it\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-21T23:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5469",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

According to yi the issue has been fixed:

```
[00:09] <mabshoff> yi: what is the status of #888 - is that fixed by any chance?
[00:09] <yi> mabshoff: yes, please close it
```


Cheers,

Michael



---

archive/issue_comments_005470.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-21T23:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5470",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002468.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-21T23:39:49Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "milestone": "sage-2.8.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/888#event-2468"
}
```



---

archive/issue_events_002469.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-21T23:39:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/888#event-2469"
}
```
