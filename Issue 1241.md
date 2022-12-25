# Issue 1241: absolute symbolic links left in "make install"

archive/issues_001241.json:
```json
{
    "body": "Assignee: mabshoff\n\nAnother problem reported by Emmanuel Thome: the following symbolic links are absolute with respect to the\nbuild directory of SAGE, thus won't work any more after \"make install\":\n\n```\n$ find sage-2.8.13/ | while read f ; do [ -h \"$f\" ] && [ ! \\\n-e \"$f\" ] && ls -l \"$f\" ; done\nlrwxrwxrwx 1 zimmerma spaces 41 2007-11-22 11:03 sage-2.8.13/sage/local/bin/bzc\\\nmp -> /tmp/sage-2.8.13/spkg/../local/bin/bzdiff\nlrwxrwxrwx 1 zimmerma spaces 41 2007-11-22 11:03 sage-2.8.13/sage/local/bin/bzf\\\ngrep -> /tmp/sage-2.8.13/spkg/../local/bin/bzgrep\nlrwxrwxrwx 1 zimmerma spaces 41 2007-11-22 11:03 sage-2.8.13/sage/local/bin/bzl\\\ness -> /tmp/sage-2.8.13/spkg/../local/bin/bzmore\nlrwxrwxrwx 1 zimmerma spaces 41 2007-11-22 11:03 sage-2.8.13/sage/local/bin/bze\\\ngrep -> /tmp/sage-2.8.13/spkg/../local/bin/bzgrep\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1241\n\n",
    "created_at": "2007-11-22T12:15:36Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "absolute symbolic links left in \"make install\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1241",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: mabshoff

Another problem reported by Emmanuel Thome: the following symbolic links are absolute with respect to the
build directory of SAGE, thus won't work any more after "make install":

```
$ find sage-2.8.13/ | while read f ; do [ -h "$f" ] && [ ! \
-e "$f" ] && ls -l "$f" ; done
lrwxrwxrwx 1 zimmerma spaces 41 2007-11-22 11:03 sage-2.8.13/sage/local/bin/bzc\
mp -> /tmp/sage-2.8.13/spkg/../local/bin/bzdiff
lrwxrwxrwx 1 zimmerma spaces 41 2007-11-22 11:03 sage-2.8.13/sage/local/bin/bzf\
grep -> /tmp/sage-2.8.13/spkg/../local/bin/bzgrep
lrwxrwxrwx 1 zimmerma spaces 41 2007-11-22 11:03 sage-2.8.13/sage/local/bin/bzl\
ess -> /tmp/sage-2.8.13/spkg/../local/bin/bzmore
lrwxrwxrwx 1 zimmerma spaces 41 2007-11-22 11:03 sage-2.8.13/sage/local/bin/bze\
grep -> /tmp/sage-2.8.13/spkg/../local/bin/bzgrep
```


Issue created by migration from https://trac.sagemath.org/ticket/1241





---

archive/issue_comments_007749.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-22T21:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1241#issuecomment-7749",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007750.json:
```json
{
    "body": "I will take care of those issues.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-22T21:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1241#issuecomment-7750",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I will take care of those issues.

Cheers,

Michael



---

archive/issue_comments_007751.json:
```json
{
    "body": "This problem seems fixed in sage-2.9:\n\n```\nbash-3.2$ pwd\n/usr/local/sage-2.9/sage/local/bin\nbash-3.2$ ls -l bz*\n-rwxr-xr-x 1 zimmerma spaces 131001 2007-12-17 11:25 bzcat\nlrwxrwxrwx 1 zimmerma spaces      6 2007-12-17 11:25 bzcmp -> bzdiff\n-rwxr-xr-x 1 zimmerma spaces   2128 2007-12-17 11:25 bzdiff\nlrwxrwxrwx 1 zimmerma spaces      6 2007-12-17 11:25 bzegrep -> bzgrep\nlrwxrwxrwx 1 zimmerma spaces      6 2007-12-17 11:25 bzfgrep -> bzgrep\n-rwxr-xr-x 1 zimmerma spaces   1677 2007-12-17 11:25 bzgrep\n-rwxr-xr-x 1 zimmerma spaces 131001 2007-12-17 11:25 bzip2\n-rwxr-xr-x 1 zimmerma spaces  14861 2007-12-17 11:25 bzip2recover\nlrwxrwxrwx 1 zimmerma spaces      6 2007-12-17 11:25 bzless -> bzmore\n-rwxr-xr-x 1 zimmerma spaces   1259 2007-12-17 11:25 bzmore\n```\n",
    "created_at": "2007-12-17T12:28:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1241#issuecomment-7751",
    "user": "https://github.com/zimmermann6"
}
```

This problem seems fixed in sage-2.9:

```
bash-3.2$ pwd
/usr/local/sage-2.9/sage/local/bin
bash-3.2$ ls -l bz*
-rwxr-xr-x 1 zimmerma spaces 131001 2007-12-17 11:25 bzcat
lrwxrwxrwx 1 zimmerma spaces      6 2007-12-17 11:25 bzcmp -> bzdiff
-rwxr-xr-x 1 zimmerma spaces   2128 2007-12-17 11:25 bzdiff
lrwxrwxrwx 1 zimmerma spaces      6 2007-12-17 11:25 bzegrep -> bzgrep
lrwxrwxrwx 1 zimmerma spaces      6 2007-12-17 11:25 bzfgrep -> bzgrep
-rwxr-xr-x 1 zimmerma spaces   1677 2007-12-17 11:25 bzgrep
-rwxr-xr-x 1 zimmerma spaces 131001 2007-12-17 11:25 bzip2
-rwxr-xr-x 1 zimmerma spaces  14861 2007-12-17 11:25 bzip2recover
lrwxrwxrwx 1 zimmerma spaces      6 2007-12-17 11:25 bzless -> bzmore
-rwxr-xr-x 1 zimmerma spaces   1259 2007-12-17 11:25 bzmore
```




---

archive/issue_comments_007752.json:
```json
{
    "body": "William verified that this issue was fixed by 2.9.final.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-17T19:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1241#issuecomment-7752",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

William verified that this issue was fixed by 2.9.final.

Cheers,

Michael



---

archive/issue_comments_007753.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-17T19:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1241#issuecomment-7753",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007754.json:
```json
{
    "body": "Paul Zimmermann also confirmed that the issue has been solved.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-17T19:30:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1241#issuecomment-7754",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Paul Zimmermann also confirmed that the issue has been solved.

Cheers,

Michael
