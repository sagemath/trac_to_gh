# Issue 888: 2.8.7-alpha0: doctest failure in dsage/tests/testdoc.py (requires previous dsage setup)

archive/issues_000888.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nFile \"testdoc.py\", line 12:\n    age: d = DSage(port=port, ssl=False)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/cwitty/pre-sage/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[5]>\", line 1, in <module>\n        d = DSage(port=port, ssl=False)###line 12:\n    age: d = DSage(port=port, ssl=False)\n      File \"/home/cwitty/pre-sage/local/lib/python/site-packages/sage/dsage/all.py\", line 52, in DSage\n        ssl=ssl)\n      File \"/home/cwitty/pre-sage/local/lib/python/site-packages/sage/dsage/interface/dsage_interface.py\", line 392, in __init__\n        self.pubkey_str = keys.getPublicKeyString(filename=self.pubkey_file)\n      File \"/home/cwitty/pre-sage/local/lib/python2.5/site-packages/twisted/conch/ssh/keys.py\", line 48, in getPublicKeyString\n        lines = open(filename).readlines()\n    IOError: [Errno 2] No such file or directory: '/home/cwitty/.sage/dsage/dsage_key.pub'\n```\n\n\n(The last line is the most interesting.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/888\n\n",
    "created_at": "2007-10-13T20:36:32Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "2.8.7-alpha0: doctest failure in dsage/tests/testdoc.py (requires previous dsage setup)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/888",
    "user": "cwitty"
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

archive/issue_comments_005477.json:
```json
{
    "body": "Changing priority from blocker to major.",
    "created_at": "2007-10-14T05:12:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5477",
    "user": "@williamstein"
}
```

Changing priority from blocker to major.



---

archive/issue_comments_005478.json:
```json
{
    "body": "I've disabled dsage doctesting for that file for sage-2.8.7, and moved this to 2.8.8.",
    "created_at": "2007-10-14T05:12:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5478",
    "user": "@williamstein"
}
```

I've disabled dsage doctesting for that file for sage-2.8.7, and moved this to 2.8.8.



---

archive/issue_comments_005479.json:
```json
{
    "body": "I reassigned this bug to me so I don't lose track of it.  I will fix this one ASAP.  \nPlease reassign DSAGE related bugs to me in the future so they will show up under \"My Active Tickets\" for me.",
    "created_at": "2007-10-19T06:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5479",
    "user": "@yqiang"
}
```

I reassigned this bug to me so I don't lose track of it.  I will fix this one ASAP.  
Please reassign DSAGE related bugs to me in the future so they will show up under "My Active Tickets" for me.



---

archive/issue_comments_005480.json:
```json
{
    "body": "Changing assignee from @williamstein to @yqiang.",
    "created_at": "2007-10-19T06:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5480",
    "user": "@yqiang"
}
```

Changing assignee from @williamstein to @yqiang.



---

archive/issue_comments_005481.json:
```json
{
    "body": "I've turned off doctesting of this file until Yi's resolve the issue.\n\nWilliam",
    "created_at": "2007-11-07T05:24:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5481",
    "user": "@williamstein"
}
```

I've turned off doctesting of this file until Yi's resolve the issue.

William



---

archive/issue_comments_005482.json:
```json
{
    "body": "WAIT -- requiring that dsage.setup() has been run is *not* an unreasonable requirement\nbefore doctesting.    How else can we expect to truly doctest that dsage work and have\nit eventually appear in examples all over the place, etc.?\n\nTo resolve this ticket, we just need to require dsage setup has been run, say at the\nbeginning of doing \"make test\".",
    "created_at": "2007-11-07T05:30:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5482",
    "user": "@williamstein"
}
```

WAIT -- requiring that dsage.setup() has been run is *not* an unreasonable requirement
before doctesting.    How else can we expect to truly doctest that dsage work and have
it eventually appear in examples all over the place, etc.?

To resolve this ticket, we just need to require dsage setup has been run, say at the
beginning of doing "make test".



---

archive/issue_comments_005483.json:
```json
{
    "body": "By the way, I think dsage.setup() should either fail completely or print a huge warning if the openssl Linux package isn't installed, since then it takes *minutes* to generate a key (using gnutls).  It might be that the new gpl v3 only gnutls fixes this crap.  But we have to wait for singular to update their license first to find out.",
    "created_at": "2007-11-07T05:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5483",
    "user": "@williamstein"
}
```

By the way, I think dsage.setup() should either fail completely or print a huge warning if the openssl Linux package isn't installed, since then it takes *minutes* to generate a key (using gnutls).  It might be that the new gpl v3 only gnutls fixes this crap.  But we have to wait for singular to update their license first to find out.



---

archive/issue_comments_005484.json:
```json
{
    "body": "Just for clarity -- I *have* turned doctesting this file off in this sage release.\nBut I think the right solution is to require dsage.setup(), and to make it clear\nto the user how to do that...",
    "created_at": "2007-11-07T05:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5484",
    "user": "@williamstein"
}
```

Just for clarity -- I *have* turned doctesting this file off in this sage release.
But I think the right solution is to require dsage.setup(), and to make it clear
to the user how to do that...



---

archive/issue_comments_005485.json:
```json
{
    "body": "Since we will update to GNUTLS 2.2.0 (see #1622) soon we should revisit this issue.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-29T17:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5485",
    "user": "mabshoff"
}
```

Since we will update to GNUTLS 2.2.0 (see #1622) soon we should revisit this issue.

Cheers,

Michael



---

archive/issue_comments_005486.json:
```json
{
    "body": "Ok, it's easy enough to check that dsage.setup() has been run (i.e. check that DOT_SAGE/dsage exists).  Where should this check go?",
    "created_at": "2007-12-30T00:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5486",
    "user": "@yqiang"
}
```

Ok, it's easy enough to check that dsage.setup() has been run (i.e. check that DOT_SAGE/dsage exists).  Where should this check go?



---

archive/issue_comments_005487.json:
```json
{
    "body": "According to yi the issue has been fixed:\n\n```\n[00:09] <mabshoff> yi: what is the status of #888 - is that fixed by any chance?\n[00:09] <yi> mabshoff: yes, please close it\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-03-21T23:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5487",
    "user": "mabshoff"
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

archive/issue_comments_005488.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-21T23:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/888",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/888#issuecomment-5488",
    "user": "mabshoff"
}
```

Resolution: fixed
