# Issue 3691: Fix permission issues in $SAGE_LOCAL/bin repo

archive/issues_003691.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\ncp: cannot open `/home/was/s/local/bin/sage-rebase_sage.sh' for reading: Permission denied\ncp: cannot open `/home/was/s/local/bin/sage-server-web' for reading: Permission denied\ncp: cannot open `/home/was/s/local/bin/phc' for reading: Permission denied\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3691\n\n",
    "created_at": "2008-07-21T06:03:35Z",
    "labels": [
        "build",
        "critical",
        "bug"
    ],
    "title": "Fix permission issues in $SAGE_LOCAL/bin repo",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3691",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
cp: cannot open `/home/was/s/local/bin/sage-rebase_sage.sh' for reading: Permission denied
cp: cannot open `/home/was/s/local/bin/sage-server-web' for reading: Permission denied
cp: cannot open `/home/was/s/local/bin/phc' for reading: Permission denied
```


Issue created by migration from https://trac.sagemath.org/ticket/3691





---

archive/issue_comments_026156.json:
```json
{
    "body": "Oops, as it turned out this is a specific issue with William's install:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/local/bin$ ls -al sage-rebase_sage.sh \n-rwxr-xr-x 1 mabshoff 1090 424 2008-07-16 21:05 sage-rebase_sage.sh\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/local/bin$ ls -la sage-server-web\n-rwxr-xr-x 1 mabshoff 1090 702 2008-07-21 00:56 sage-server-web\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/local/bin$ ls -la /home/was/s/local/bin/sage-rebase_sage.sh \n-rwx--x--x 1 was was 424 2008-05-05 06:51 /home/was/s/local/bin/sage-rebase_sage.sh\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/local/bin$ ls -la /home/was/s/local/bin/sage-server-web \n-rwx--x--x 1 was was 702 2008-07-16 16:21 /home/was/s/local/bin/sage-server-web\n```\n\nOn a fresh install is not an issue. It seems likely that some stupidity in hg caused this.\n\nErgo: wontfix.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-21T08:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3691#issuecomment-26156",
    "user": "mabshoff"
}
```

Oops, as it turned out this is a specific issue with William's install:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/local/bin$ ls -al sage-rebase_sage.sh 
-rwxr-xr-x 1 mabshoff 1090 424 2008-07-16 21:05 sage-rebase_sage.sh
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/local/bin$ ls -la sage-server-web
-rwxr-xr-x 1 mabshoff 1090 702 2008-07-21 00:56 sage-server-web
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/local/bin$ ls -la /home/was/s/local/bin/sage-rebase_sage.sh 
-rwx--x--x 1 was was 424 2008-05-05 06:51 /home/was/s/local/bin/sage-rebase_sage.sh
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.6.alpha1/local/bin$ ls -la /home/was/s/local/bin/sage-server-web 
-rwx--x--x 1 was was 702 2008-07-16 16:21 /home/was/s/local/bin/sage-server-web
```

On a fresh install is not an issue. It seems likely that some stupidity in hg caused this.

Ergo: wontfix.

Cheers,

Michael



---

archive/issue_comments_026157.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-07-21T08:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3691#issuecomment-26157",
    "user": "mabshoff"
}
```

Resolution: wontfix
