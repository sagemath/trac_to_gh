# Issue 5825: sage -i $FOO.spkg should abort cleanly when write permissions are lacking

archive/issues_005825.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @jhpalmieri\n\nI just ran into the following:\n\n```\n<SNIP>\n**********************************************************************\n* Unable to download clisp-2.47\n* Please see http://www.sagemath.org//packages for a list of valid\n* packages or check the package name.\n**********************************************************************\n/Users/mabshoff/sage-3.3.rc3/spkg/build\nbunzip2: Can't open input file clisp-2.47.spkg: No such file or directory.\ntar: clisp-2.47.spkg: Cannot open: No such file or directory\ntar: Error is not recoverable: exiting now\nSecond download resulted in a corrupted package.\nvarro:/Users/mabshoff/sage-3.3.rc3 mabshoff$ file /home/mabshoff/clisp-2.47.spkg \n/home/mabshoff/clisp-2.47.spkg: bzip2 compressed data, block size = 900k\nvarro:/Users/mabshoff/sage-3.3.rc3 mabshoff$ cp /home/mabshoff/clisp-2.47.spkg .\ncp: ./clisp-2.47.spkg: Permission denied\n```\n\nNote that I do not have write permissions in the local directory.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5825\n\n",
    "created_at": "2009-04-20T01:07:19Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.10",
    "title": "sage -i $FOO.spkg should abort cleanly when write permissions are lacking",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5825",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @jhpalmieri

I just ran into the following:

```
<SNIP>
**********************************************************************
* Unable to download clisp-2.47
* Please see http://www.sagemath.org//packages for a list of valid
* packages or check the package name.
**********************************************************************
/Users/mabshoff/sage-3.3.rc3/spkg/build
bunzip2: Can't open input file clisp-2.47.spkg: No such file or directory.
tar: clisp-2.47.spkg: Cannot open: No such file or directory
tar: Error is not recoverable: exiting now
Second download resulted in a corrupted package.
varro:/Users/mabshoff/sage-3.3.rc3 mabshoff$ file /home/mabshoff/clisp-2.47.spkg 
/home/mabshoff/clisp-2.47.spkg: bzip2 compressed data, block size = 900k
varro:/Users/mabshoff/sage-3.3.rc3 mabshoff$ cp /home/mabshoff/clisp-2.47.spkg .
cp: ./clisp-2.47.spkg: Permission denied
```

Note that I do not have write permissions in the local directory.

Issue created by migration from https://trac.sagemath.org/ticket/5825





---

archive/issue_comments_045701.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-05-16T08:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5825#issuecomment-45701",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_045702.json:
```json
{
    "body": "Changing component from packages: standard to scripts.",
    "created_at": "2013-05-16T08:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5825#issuecomment-45702",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from packages: standard to scripts.



---

archive/issue_comments_045703.json:
```json
{
    "body": "Is it worth checking permissions before attempting to download an spkg?\n\n```\n$ sage -i pybtex\ntee: /Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/logs/install.log: Permission denied\ntee: /Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/logs/pkgs/pybtex.log: Permission denied\nAttempting to download package pybtex\n>>> Checking online list of optional packages.\n[.]\n>>> Found pybtex-20120618\n>>> Downloading http://www.sagemath.org/spkg/optional/pybtex-20120618.spkg.\n/Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/spkg/bin/sage-spkg: line 354: pybtex-20120618.tmp: Permission denied\nError: failed to download package pybtex-20120618\n```\nThis is not as nice an error message as you added in other situations:\n\n```\n$ sage -f gcc\ntee: /Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/logs/install.log: Permission denied\ntee: /Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/logs/pkgs/gcc.log: Permission denied\nFound package gcc in spkg/standard/gcc-4.7.3.p0.spkg\nError: no write access to build directory /Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/spkg/build.\n```",
    "created_at": "2013-05-21T18:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5825#issuecomment-45703",
    "user": "https://github.com/jhpalmieri"
}
```

Is it worth checking permissions before attempting to download an spkg?

```
$ sage -i pybtex
tee: /Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/logs/install.log: Permission denied
tee: /Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/logs/pkgs/pybtex.log: Permission denied
Attempting to download package pybtex
>>> Checking online list of optional packages.
[.]
>>> Found pybtex-20120618
>>> Downloading http://www.sagemath.org/spkg/optional/pybtex-20120618.spkg.
/Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/spkg/bin/sage-spkg: line 354: pybtex-20120618.tmp: Permission denied
Error: failed to download package pybtex-20120618
```
This is not as nice an error message as you added in other situations:

```
$ sage -f gcc
tee: /Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/logs/install.log: Permission denied
tee: /Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/logs/pkgs/gcc.log: Permission denied
Found package gcc in spkg/standard/gcc-4.7.3.p0.spkg
Error: no write access to build directory /Users/palmieri/Desktop/Sage_stuff/sage_builds/sage-5.10.beta4/spkg/build.
```



---

archive/issue_comments_045704.json:
```json
{
    "body": "Attachment [5825_install_perm.patch](tarball://root/attachments/some-uuid/ticket5825/5825_install_perm.patch) by @jdemeyer created at 2013-05-22 08:47:36\n\nOK, fixed.",
    "created_at": "2013-05-22T08:47:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5825#issuecomment-45704",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [5825_install_perm.patch](tarball://root/attachments/some-uuid/ticket5825/5825_install_perm.patch) by @jdemeyer created at 2013-05-22 08:47:36

OK, fixed.



---

archive/issue_comments_045705.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-22T17:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5825#issuecomment-45705",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_045706.json:
```json
{
    "body": "Great, looks good.",
    "created_at": "2013-05-22T17:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5825#issuecomment-45706",
    "user": "https://github.com/jhpalmieri"
}
```

Great, looks good.



---

archive/issue_comments_045707.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-05-24T09:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5825",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5825#issuecomment-45707",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_013691.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-24T09:39:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5825",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5825#event-13691"
}
```
