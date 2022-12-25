# Issue 3011: Set R_HOMES properly so rpy works with an existing R installed

archive/issues_003011.json:
```json
{
    "body": "Assignee: mabshoff\n\nSteve reported:\n\n```\nOn my Gentoo box I unpacked the subject tarball, changed to the sage\ndirectory and did a make with the results:\n\ngcc version 4.1.2 (Gentoo 4.1.2 p1.0.2)\n****************************************************\n****************************************************\nRHOMES= []\nDEBUG= True\nSetting RHOMES to  ['/usr/lib64/R']\nRHOMES= []\nDEBUG= True\nSetting RHOMES to  ['/usr/lib64/R']\nTraceback (most recent call last):\nTraceback (most recent call last):\n  File \"setup.py\", line 106, in <module>\n  File \"setup.py\", line 106, in <module>\n        RVERSION = rpy_tools.get_R_VERSION(RHOME, force_exec=True)\nRVERSION = rpy_tools.get_R_VERSION(RHOME, force_exec=True)\n  File \"/local/sage-3.0/spkg/build/rpy-1.0.1.p1/src/rpy_tools.py\",\nline 99, in get_R_VERSION\n  File \"/local/sage-3.0/spkg/build/rpy-1.0.1.p1/src/rpy_tools.py\",\nline 99, in get_R_VERSION\n        \" `%s'.\\n\" % rexec )\n\" `%s'.\\n\" % rexec )\nRuntimeErrorRuntimeError: : Couldn't execute the R interpreter `/usr/\nlib64/R/bin/R'.\nCouldn't execute the R interpreter `/usr/lib64/R/bin/R'.\n\nError building RPY -- Python interface to R.\nError building RPY -- Python interface to R.\n\nI tried several corrective measures and the only one that allowed sage\nto build was to issue:\n\nRHOMES=\"`pwd`/local/lib/R\" make\n\nHowever, the following test failed:\n\nsage -t  devel/sage/sage/stats/test.py \n```\n\nFollow up:\n\n```\nMichael,\n\nYes I do have R installed on my system. No, RHOMES is not set;\nhowever, R_HOMES is set to /usr/lib64/R. Apparently, the R\ninstallation does this. And yes I do have the install.log. The\nspecific test fails as:\n\nsage -t  devel/sage/sage/stats/test.py\n**********************************************************************\nFile \"/local/sage-3.0/tmp/test.py\", line 5:\n    sage: import rpy\nException raised:\n    Traceback (most recent call last):\n      File \"/local/sage-3.0/local/lib/python2.5/doctest.py\", line\n1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[1]>\", line 1, in <module>\n        import rpy###line 5:\n    sage: import rpy\n      File \"/local/sage-3.0/local/lib/python2.5/site-packages/rpy.py\",\nline 58, in <m\nodule>\n        RVERSION = rpy_tools.get_R_VERSION(RHOME)\n      File \"/local/sage-3.0/local/lib/python2.5/site-packages/\nrpy_tools.py\", line 99,\n in get_R_VERSION\n        \" `%s'.\\n\" % rexec )\n    RuntimeError: Couldn't execute the R interpreter `/usr/lib64/R/bin/\nR'.\n\n**********************************************************************\n1 items had failures:\n   1 of   2 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /local/sage-3.0/\ntmp/.doctest_test.py\n         [1.5 s]\nexit code: 1024\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n        sage -t  devel/sage/sage/stats/test.py\nTotal time for all tests: 1.5 seconds\n\nI've built sage previously, but without R installed. I suspect the\ninstalled (Portage) R is conflicting with what sage does. Let me know\nif you wish to see the install.log. I'm presently re-building sage in\na shell where I've disabled the R_HOME variable.\n\nSteve \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3011\n\n",
    "created_at": "2008-04-23T21:25:50Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Set R_HOMES properly so rpy works with an existing R installed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3011",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Steve reported:

```
On my Gentoo box I unpacked the subject tarball, changed to the sage
directory and did a make with the results:

gcc version 4.1.2 (Gentoo 4.1.2 p1.0.2)
****************************************************
****************************************************
RHOMES= []
DEBUG= True
Setting RHOMES to  ['/usr/lib64/R']
RHOMES= []
DEBUG= True
Setting RHOMES to  ['/usr/lib64/R']
Traceback (most recent call last):
Traceback (most recent call last):
  File "setup.py", line 106, in <module>
  File "setup.py", line 106, in <module>
        RVERSION = rpy_tools.get_R_VERSION(RHOME, force_exec=True)
RVERSION = rpy_tools.get_R_VERSION(RHOME, force_exec=True)
  File "/local/sage-3.0/spkg/build/rpy-1.0.1.p1/src/rpy_tools.py",
line 99, in get_R_VERSION
  File "/local/sage-3.0/spkg/build/rpy-1.0.1.p1/src/rpy_tools.py",
line 99, in get_R_VERSION
        " `%s'.\n" % rexec )
" `%s'.\n" % rexec )
RuntimeErrorRuntimeError: : Couldn't execute the R interpreter `/usr/
lib64/R/bin/R'.
Couldn't execute the R interpreter `/usr/lib64/R/bin/R'.

Error building RPY -- Python interface to R.
Error building RPY -- Python interface to R.

I tried several corrective measures and the only one that allowed sage
to build was to issue:

RHOMES="`pwd`/local/lib/R" make

However, the following test failed:

sage -t  devel/sage/sage/stats/test.py 
```

Follow up:

```
Michael,

Yes I do have R installed on my system. No, RHOMES is not set;
however, R_HOMES is set to /usr/lib64/R. Apparently, the R
installation does this. And yes I do have the install.log. The
specific test fails as:

sage -t  devel/sage/sage/stats/test.py
**********************************************************************
File "/local/sage-3.0/tmp/test.py", line 5:
    sage: import rpy
Exception raised:
    Traceback (most recent call last):
      File "/local/sage-3.0/local/lib/python2.5/doctest.py", line
1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[1]>", line 1, in <module>
        import rpy###line 5:
    sage: import rpy
      File "/local/sage-3.0/local/lib/python2.5/site-packages/rpy.py",
line 58, in <m
odule>
        RVERSION = rpy_tools.get_R_VERSION(RHOME)
      File "/local/sage-3.0/local/lib/python2.5/site-packages/
rpy_tools.py", line 99,
 in get_R_VERSION
        " `%s'.\n" % rexec )
    RuntimeError: Couldn't execute the R interpreter `/usr/lib64/R/bin/
R'.

**********************************************************************
1 items had failures:
   1 of   2 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /local/sage-3.0/
tmp/.doctest_test.py
         [1.5 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:

        sage -t  devel/sage/sage/stats/test.py
Total time for all tests: 1.5 seconds

I've built sage previously, but without R installed. I suspect the
installed (Portage) R is conflicting with what sage does. Let me know
if you wish to see the install.log. I'm presently re-building sage in
a shell where I've disabled the R_HOME variable.

Steve 
```


Issue created by migration from https://trac.sagemath.org/ticket/3011





---

archive/issue_comments_020658.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-23T21:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3011#issuecomment-20658",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020659.json:
```json
{
    "body": "See also #3086 about the update to R 2.7.0.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-05T03:31:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3011#issuecomment-20659",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

See also #3086 about the update to R 2.7.0.

Cheers,

Michael



---

archive/issue_comments_020660.json:
```json
{
    "body": "Francois opened another ticket about the same issues at #3328. Since he also posted a patch that fixes the issue there I am closing this as a duplicate.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-29T11:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3011#issuecomment-20660",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Francois opened another ticket about the same issues at #3328. Since he also posted a patch that fixes the issue there I am closing this as a duplicate.

Cheers,

Michael



---

archive/issue_comments_020661.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-05-29T11:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3011#issuecomment-20661",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate
