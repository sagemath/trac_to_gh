# Issue 3161: sdist: #3046 seems to have broken sage-banner

archive/issues_003161.json:
```json
{
    "body": "Assignee: mabshoff\n\nRunning sdist on 3.0.2.alpha1 results in:\n\n```\nrunning install_egg_info\nWriting /scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage-3.0.2.alpha1-py2.5.egg-info\nls: devel/sage: No such file or directory\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py\", line 56, in banner\n    print banner_text()\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py\", line 48, in banner_text\n    s += \"\\n| %-66s |\\n\"%version()\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py\", line 38, in version\n    branch = os.popen(\"ls -l devel/sage\").read().split()[-1][5:]\nIndexError: list index out of range\ncp: cannot stat `ipythonrc': No such file or directory\ncp: cannot stat `spkg/update': No such file or directory\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3161\n\n",
    "created_at": "2008-05-11T23:41:28Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "sdist: #3046 seems to have broken sage-banner",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3161",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Running sdist on 3.0.2.alpha1 results in:

```
running install_egg_info
Writing /scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage-3.0.2.alpha1-py2.5.egg-info
ls: devel/sage: No such file or directory
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py", line 56, in banner
    print banner_text()
  File "/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py", line 48, in banner_text
    s += "\n| %-66s |\n"%version()
  File "/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py", line 38, in version
    branch = os.popen("ls -l devel/sage").read().split()[-1][5:]
IndexError: list index out of range
cp: cannot stat `ipythonrc': No such file or directory
cp: cannot stat `spkg/update': No such file or directory
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3161





---

archive/issue_comments_021879.json:
```json
{
    "body": "The problem boils down to the following:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0$ echo \"import sage.misc.banner; sage.misc.banner.banner()\" | ./local/bin/python\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0$ cd local/bin/\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/bin$ echo \"import sage.misc.banner; sage.misc.banner.banner()\" | ./python\nls: devel/sage: No such file or directory\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py\", line 56, in banner\n    print banner_text()\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py\", line 48, in banner_text\n    s += \"\\n| %-66s |\\n\"%version()\n  File \"/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py\", line 38, in version\n    branch = os.popen(\"ls -l devel/sage\").read().split()[-1][5:]\nIndexError: list index out of range\n```\n\n| SAGE Version 3.0.2.alpha1, Release Date: 2008-05-11                |\n| Type notebook() for the GUI, and license() for information.        |\nCheers,\n\nMichael",
    "created_at": "2008-05-11T23:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3161#issuecomment-21879",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The problem boils down to the following:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0$ echo "import sage.misc.banner; sage.misc.banner.banner()" | ./local/bin/python
----------------------------------------------------------------------
----------------------------------------------------------------------
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0$ cd local/bin/
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/bin$ echo "import sage.misc.banner; sage.misc.banner.banner()" | ./python
ls: devel/sage: No such file or directory
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py", line 56, in banner
    print banner_text()
  File "/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py", line 48, in banner_text
    s += "\n| %-66s |\n"%version()
  File "/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py", line 38, in version
    branch = os.popen("ls -l devel/sage").read().split()[-1][5:]
IndexError: list index out of range
```

| SAGE Version 3.0.2.alpha1, Release Date: 2008-05-11                |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael



---

archive/issue_comments_021880.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-11T23:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3161#issuecomment-21880",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021881.json:
```json
{
    "body": "Ok. Figured it out: #3046 determines the branch by using \"ls -la devel/sage\" and that assume that the current working directory is in $SAGE_ROOT. Patch coming up.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-19T06:40:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3161#issuecomment-21881",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok. Figured it out: #3046 determines the branch by using "ls -la devel/sage" and that assume that the current working directory is in $SAGE_ROOT. Patch coming up.

Cheers,

Michael



---

archive/issue_comments_021882.json:
```json
{
    "body": "Attachment [trac_3161.patch](tarball://root/attachments/some-uuid/ticket3161/trac_3161.patch) by mabshoff created at 2008-05-19 06:51:43",
    "created_at": "2008-05-19T06:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3161#issuecomment-21882",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_3161.patch](tarball://root/attachments/some-uuid/ticket3161/trac_3161.patch) by mabshoff created at 2008-05-19 06:51:43



---

archive/issue_comments_021883.json:
```json
{
    "body": "To test this run \n\n```\necho \"import sage.misc.banner; sage.misc.banner.banner()\" | ./python\n```\n\ni.e. with #3041 *and* #3161 we get:\n\n```\nsage-3.0.2.alpha1/local/bin$ echo \"import sage.misc.banner; sage.misc.banner.banner()\" | ./python\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n```\n\n| SAGE Version 3.0.2.alpha0, Release Date: 2008-05-11                |\n| Type notebook() for the GUI, and license() for information.        |\nCheers,\n\nMichael",
    "created_at": "2008-05-19T06:53:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3161#issuecomment-21883",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

To test this run 

```
echo "import sage.misc.banner; sage.misc.banner.banner()" | ./python
```

i.e. with #3041 *and* #3161 we get:

```
sage-3.0.2.alpha1/local/bin$ echo "import sage.misc.banner; sage.misc.banner.banner()" | ./python
----------------------------------------------------------------------
----------------------------------------------------------------------
```

| SAGE Version 3.0.2.alpha0, Release Date: 2008-05-11                |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael



---

archive/issue_comments_021884.json:
```json
{
    "body": "mabshoff's patch works for me against a 3.0 tree.",
    "created_at": "2008-05-19T07:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3161#issuecomment-21884",
    "user": "https://github.com/dandrake"
}
```

mabshoff's patch works for me against a 3.0 tree.



---

archive/issue_comments_021885.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-19T07:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3161#issuecomment-21885",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021886.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-19T07:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3161#issuecomment-21886",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha1



---

archive/issue_events_003381.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-19T07:16:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3161",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3161#event-3381"
}
```
