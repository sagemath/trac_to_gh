# Issue 3318: improve 64 bit osx python 2.5.2 build

archive/issues_003318.json:
```json
{
    "body": "Assignee: mabshoff\n\nThere are are two issues that need to be fixed with the current python.spkg:\n\n* we need to pass OPT flags to configure since otherwise we end up missing \"-m64\"\n* Instead of \"--enable-toolbox-glue=false\" we need to use \"--disable-toolbox-glue\" to avoid building the Mac specific extensions that do not work in 64 bit mode anyway since there is no 64 bit Carbon\n* we need to slightly patch pymactoolbox.h so that twisted-8.0.1 work in 64 bit mode, see #3193\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3318\n\n",
    "created_at": "2008-05-28T09:10:46Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "improve 64 bit osx python 2.5.2 build",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3318",
    "user": "mabshoff"
}
```
Assignee: mabshoff

There are are two issues that need to be fixed with the current python.spkg:

* we need to pass OPT flags to configure since otherwise we end up missing "-m64"
* Instead of "--enable-toolbox-glue=false" we need to use "--disable-toolbox-glue" to avoid building the Mac specific extensions that do not work in 64 bit mode anyway since there is no 64 bit Carbon
* we need to slightly patch pymactoolbox.h so that twisted-8.0.1 work in 64 bit mode, see #3193

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3318





---

archive/issue_comments_023009.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-28T09:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3318#issuecomment-23009",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023010.json:
```json
{
    "body": "Attachment [python-2.5.2.p0-osx64-part3.patch](tarball://root/attachments/some-uuid/ticket3318/python-2.5.2.p0-osx64-part3.patch) by mabshoff created at 2008-05-28 09:43:32",
    "created_at": "2008-05-28T09:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3318#issuecomment-23010",
    "user": "mabshoff"
}
```

Attachment [python-2.5.2.p0-osx64-part3.patch](tarball://root/attachments/some-uuid/ticket3318/python-2.5.2.p0-osx64-part3.patch) by mabshoff created at 2008-05-28 09:43:32



---

archive/issue_comments_023011.json:
```json
{
    "body": "Attachment [python-2.5.2.p0-osx64-part4.patch](tarball://root/attachments/some-uuid/ticket3318/python-2.5.2.p0-osx64-part4.patch) by mabshoff created at 2008-05-28 09:43:44",
    "created_at": "2008-05-28T09:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3318#issuecomment-23011",
    "user": "mabshoff"
}
```

Attachment [python-2.5.2.p0-osx64-part4.patch](tarball://root/attachments/some-uuid/ticket3318/python-2.5.2.p0-osx64-part4.patch) by mabshoff created at 2008-05-28 09:43:44



---

archive/issue_comments_023012.json:
```json
{
    "body": "Attachment [python-2.5.2.p0-osx64-part5.patch](tarball://root/attachments/some-uuid/ticket3318/python-2.5.2.p0-osx64-part5.patch) by mabshoff created at 2008-05-28 09:43:53",
    "created_at": "2008-05-28T09:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3318#issuecomment-23012",
    "user": "mabshoff"
}
```

Attachment [python-2.5.2.p0-osx64-part5.patch](tarball://root/attachments/some-uuid/ticket3318/python-2.5.2.p0-osx64-part5.patch) by mabshoff created at 2008-05-28 09:43:53



---

archive/issue_comments_023013.json:
```json
{
    "body": "Attachment [python-pymactoolbox.h-64bit-osx.patch](tarball://root/attachments/some-uuid/ticket3318/python-pymactoolbox.h-64bit-osx.patch) by mabshoff created at 2008-05-28 09:49:11\n\nThe spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/python-2.5.2.p1.spkg\n\ncontains the above fixes. It has been build tested with Linux and 32 & 64 bit OSX.\n\nCurrently the _ctypes.so extension is broken. Since the fix is complicated this will be another ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-28T09:49:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3318#issuecomment-23013",
    "user": "mabshoff"
}
```

Attachment [python-pymactoolbox.h-64bit-osx.patch](tarball://root/attachments/some-uuid/ticket3318/python-pymactoolbox.h-64bit-osx.patch) by mabshoff created at 2008-05-28 09:49:11

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/python-2.5.2.p1.spkg

contains the above fixes. It has been build tested with Linux and 32 & 64 bit OSX.

Currently the _ctypes.so extension is broken. Since the fix is complicated this will be another ticket.

Cheers,

Michael



---

archive/issue_comments_023014.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha0",
    "created_at": "2008-05-28T13:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3318#issuecomment-23014",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha0



---

archive/issue_comments_023015.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-28T13:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3318#issuecomment-23015",
    "user": "mabshoff"
}
```

Resolution: fixed
