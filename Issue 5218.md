# Issue 5218: Update Pyhton to 2.5.4

archive/issues_005218.json:
```json
{
    "body": "Assignee: mabshoff\n\nPython 2.5.4 fixes a couple of security problems in Python 2.5.2. So let's update to it since the difference to 2.5.2 are minimal.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5218\n\n",
    "created_at": "2009-02-09T12:31:43Z",
    "labels": [
        "packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Update Pyhton to 2.5.4",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5218",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Python 2.5.4 fixes a couple of security problems in Python 2.5.2. So let's update to it since the difference to 2.5.2 are minimal.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5218





---

archive/issue_comments_039978.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-09T12:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39978",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039979.json:
```json
{
    "body": "An spkg is coming up :), but I needed to correct the spelling problem in the meantime.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T05:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39979",
    "user": "mabshoff"
}
```

An spkg is coming up :), but I needed to correct the spelling problem in the meantime.

Cheers,

Michael



---

archive/issue_comments_039980.json:
```json
{
    "body": "The spkg at\n\n http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/python-2.5.4.spkg\n\nswitches to Python 2.5.4. Note that no changes were made aside from \n\n* rebasing the ctypes/__init__.py patch\n* update SPKG.txt, especially with patch information\n* rename two patches to be consistent with SPKG guidelines\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T06:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39980",
    "user": "mabshoff"
}
```

The spkg at

 http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc1/python-2.5.4.spkg

switches to Python 2.5.4. Note that no changes were made aside from 

* rebasing the ctypes/__init__.py patch
* update SPKG.txt, especially with patch information
* rename two patches to be consistent with SPKG guidelines

Cheers,

Michael



---

archive/issue_comments_039981.json:
```json
{
    "body": "I have not extensively tested this, but Michael says he has, and I have installed it and done some limited tests.  Seems to be fine.",
    "created_at": "2009-02-16T11:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39981",
    "user": "mhampton"
}
```

I have not extensively tested this, but Michael says he has, and I have installed it and done some limited tests.  Seems to be fine.



---

archive/issue_comments_039982.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-16T11:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39982",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039983.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T11:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39983",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael



---

archive/issue_comments_039984.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-02-16T15:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39984",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_039985.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-02-16T15:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39985",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_039986.json:
```json
{
    "body": "Unfortunately this introduced an unpleasant side effect since -sdist now does not include the hg repo in the sage-x.y.z.spkg. I know too little about distutils to deal with this in 3.3.rc1, so I am reverting the spkg until we fix the bug in setup.py.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T15:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39986",
    "user": "mabshoff"
}
```

Unfortunately this introduced an unpleasant side effect since -sdist now does not include the hg repo in the sage-x.y.z.spkg. I know too little about distutils to deal with this in 3.3.rc1, so I am reverting the spkg until we fix the bug in setup.py.

Cheers,

Michael



---

archive/issue_comments_039987.json:
```json
{
    "body": "Bumped to 3.4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T06:11:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39987",
    "user": "mabshoff"
}
```

Bumped to 3.4.

Cheers,

Michael



---

archive/issue_comments_039988.json:
```json
{
    "body": "Better luck in Sage 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-27T23:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39988",
    "user": "mabshoff"
}
```

Better luck in Sage 3.4.1.

Cheers,

Michael



---

archive/issue_comments_039989.json:
```json
{
    "body": "A new spkg which fixes the sdist issue is at http://sage.math.washington.edu/home/mhansen/python-2.5.4.p0.spkg",
    "created_at": "2009-05-28T20:25:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39989",
    "user": "mhansen"
}
```

A new spkg which fixes the sdist issue is at http://sage.math.washington.edu/home/mhansen/python-2.5.4.p0.spkg



---

archive/issue_comments_039990.json:
```json
{
    "body": "Note:\nThe patch that fixes this sdist issue is:\n\n```\nwstein@sage:~/tmp/python-2.5.4.p0$ diff src/Lib/distutils/command/sdist.py patches/sdist.py\n350c350\n<           * any RCS, CVS, .svn, .hg, .git, .bzr, _darcs directories\n---\n>           * any RCS, CVS, .svn, .git, .bzr, _darcs directories\n357c357\n<         self.filelist.exclude_pattern(r'(^|/)(RCS|CVS|\\.svn|\\.hg|\\.git|\\.bzr|_darcs)/.*', is_regex=1)\n---\n>         self.filelist.exclude_pattern(r'(^|/)(RCS|CVS|\\.svn|\\.git|\\.bzr|_darcs)/.*', is_regex=1)\n```\n\n\nI'm concerned since I bet this problem will just come back later again when we upgrade to some newer python, since it seems that it is the intention of the python devs to make it impossible to include repo's in sdists.  Thus, in the long run, we may have to fix this by (1) doing sdist, then (2) extract the sdist tar ball and manually copying over the hg repo, then (3) remaking the sdist tar ball.    We already extract and remake the tar ball to go from .tar.gz to .tar.bz2 format, so this isn't so bad. \n\nSo, positive review, but with a \"just for the record\" caveat.",
    "created_at": "2009-05-28T22:07:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39990",
    "user": "was"
}
```

Note:
The patch that fixes this sdist issue is:

```
wstein@sage:~/tmp/python-2.5.4.p0$ diff src/Lib/distutils/command/sdist.py patches/sdist.py
350c350
<           * any RCS, CVS, .svn, .hg, .git, .bzr, _darcs directories
---
>           * any RCS, CVS, .svn, .git, .bzr, _darcs directories
357c357
<         self.filelist.exclude_pattern(r'(^|/)(RCS|CVS|\.svn|\.hg|\.git|\.bzr|_darcs)/.*', is_regex=1)
---
>         self.filelist.exclude_pattern(r'(^|/)(RCS|CVS|\.svn|\.git|\.bzr|_darcs)/.*', is_regex=1)
```


I'm concerned since I bet this problem will just come back later again when we upgrade to some newer python, since it seems that it is the intention of the python devs to make it impossible to include repo's in sdists.  Thus, in the long run, we may have to fix this by (1) doing sdist, then (2) extract the sdist tar ball and manually copying over the hg repo, then (3) remaking the sdist tar ball.    We already extract and remake the tar ball to go from .tar.gz to .tar.bz2 format, so this isn't so bad. 

So, positive review, but with a "just for the record" caveat.



---

archive/issue_comments_039991.json:
```json
{
    "body": "I made http://sage.math.washington.edu/home/mhansen/python-2.5.4.p1.spkg which includes the fix done in sage-2.5.2.p9.spkg.",
    "created_at": "2009-05-29T04:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39991",
    "user": "mhansen"
}
```

I made http://sage.math.washington.edu/home/mhansen/python-2.5.4.p1.spkg which includes the fix done in sage-2.5.2.p9.spkg.



---

archive/issue_comments_039992.json:
```json
{
    "body": "This looks suspicous:\n\n```\nwstein@sage:~/tmp/python-2.5.4.p1$ hg status\n? patches/posixmodule.c.patch.rej\n```\n\n\nOtherwise this looks perfect.  \n\nhttp://sage.math.washington.edu/home/wstein/tmp/python-2.5.4.p1.spkg\n\nis the spkg but with that rej file deleted.",
    "created_at": "2009-05-29T13:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39992",
    "user": "was"
}
```

This looks suspicous:

```
wstein@sage:~/tmp/python-2.5.4.p1$ hg status
? patches/posixmodule.c.patch.rej
```


Otherwise this looks perfect.  

http://sage.math.washington.edu/home/wstein/tmp/python-2.5.4.p1.spkg

is the spkg but with that rej file deleted.



---

archive/issue_comments_039993.json:
```json
{
    "body": "This also seems to fix some problems I was having in 64-bit Fedora 10: segmentation faults when trying to use tab completion, and mysterious \"out of memory\" errors. (I tried it against 4.0.rc1.)",
    "created_at": "2009-05-29T13:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39993",
    "user": "kedlaya"
}
```

This also seems to fix some problems I was having in 64-bit Fedora 10: segmentation faults when trying to use tab completion, and mysterious "out of memory" errors. (I tried it against 4.0.rc1.)



---

archive/issue_comments_039994.json:
```json
{
    "body": "Merged http://sage.math.washington.edu/home/wstein/tmp/python-2.5.4.p1.spkg in 4.0.rc2.",
    "created_at": "2009-05-29T17:33:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39994",
    "user": "mhansen"
}
```

Merged http://sage.math.washington.edu/home/wstein/tmp/python-2.5.4.p1.spkg in 4.0.rc2.



---

archive/issue_comments_039995.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-29T17:34:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5218#issuecomment-39995",
    "user": "mhansen"
}
```

Resolution: fixed
