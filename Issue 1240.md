# Issue 1240: wrong unix rights of some files

archive/issues_001240.json:
```json
{
    "body": "Assignee: mabshoff\n\n[This was reported to me by Emmanuel Thome.]\n\nWhen installing SAGE 2.8.13 on a multi-user site (make dist), the Unix rights of some files are wrong:\n\n```\nhelene% find . ! -perm +004 | xargs ls -lLd\n-rwx--x--x 1 zimmerma spaces    414 2007-11-22 08:56 ./local/bin/sage-rebase_sage.sh\n-rwx--x--x 1 zimmerma spaces    702 2007-11-22 10:13 ./local/bin/sage-server-web\n-rw------- 1 zimmerma spaces   5292 2007-11-22 09:09 ./local/include/cremona/cperiods.h\n...\n-rw-r----- 1 zimmerma spaces   1360 2006-10-26 20:26 ./local/share/moin/underlay/pages/SystemPagesSetup/attachments/all_languages.zip\n...\n```\n\n\nShouldn't all files be at least readable (r) by everybody?\n\nIssue created by migration from https://trac.sagemath.org/ticket/1240\n\n",
    "created_at": "2007-11-22T12:12:52Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "wrong unix rights of some files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1240",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: mabshoff

[This was reported to me by Emmanuel Thome.]

When installing SAGE 2.8.13 on a multi-user site (make dist), the Unix rights of some files are wrong:

```
helene% find . ! -perm +004 | xargs ls -lLd
-rwx--x--x 1 zimmerma spaces    414 2007-11-22 08:56 ./local/bin/sage-rebase_sage.sh
-rwx--x--x 1 zimmerma spaces    702 2007-11-22 10:13 ./local/bin/sage-server-web
-rw------- 1 zimmerma spaces   5292 2007-11-22 09:09 ./local/include/cremona/cperiods.h
...
-rw-r----- 1 zimmerma spaces   1360 2006-10-26 20:26 ./local/share/moin/underlay/pages/SystemPagesSetup/attachments/all_languages.zip
...
```


Shouldn't all files be at least readable (r) by everybody?

Issue created by migration from https://trac.sagemath.org/ticket/1240





---

archive/issue_comments_007734.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-22T21:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1240#issuecomment-7734",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007735.json:
```json
{
    "body": "I will take care of those.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-22T21:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1240#issuecomment-7735",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I will take care of those.

Cheers,

Michael



---

archive/issue_comments_007736.json:
```json
{
    "body": "Ok, I have fixed \n\n```\nlocal/bin/sage-rebase_sage.sh\nlocal/bin/sage-server-web\nlocal/include/cremona/cperiods.h\n```\n\nand I will take care of the moin moin issue in 2.8.15.\n\nCheers,\n\nMichael",
    "created_at": "2007-11-24T11:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1240#issuecomment-7736",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, I have fixed 

```
local/bin/sage-rebase_sage.sh
local/bin/sage-server-web
local/include/cremona/cperiods.h
```

and I will take care of the moin moin issue in 2.8.15.

Cheers,

Michael



---

archive/issue_comments_007737.json:
```json
{
    "body": "The moin issue is still there in 2.9 (28 files are concerned).",
    "created_at": "2007-12-17T12:30:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1240#issuecomment-7737",
    "user": "https://github.com/zimmermann6"
}
```

The moin issue is still there in 2.9 (28 files are concerned).



---

archive/issue_comments_007738.json:
```json
{
    "body": "The moinmoin issues are fixed in \n\nhttp://sage.math.washington.edu/home/mabshoff/moin-1.5.7.p2.spkg\n\nCheers,\n\nMichael",
    "created_at": "2007-12-19T10:48:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1240#issuecomment-7738",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The moinmoin issues are fixed in 

http://sage.math.washington.edu/home/mabshoff/moin-1.5.7.p2.spkg

Cheers,

Michael



---

archive/issue_comments_007739.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-19T19:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1240#issuecomment-7739",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_001380.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2007-12-19T19:11:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1240#event-1380"
}
```



---

archive/issue_comments_007740.json:
```json
{
    "body": "Merged in 2.9.1 alpha2",
    "created_at": "2007-12-19T19:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1240#issuecomment-7740",
    "user": "https://github.com/rlmill"
}
```

Merged in 2.9.1 alpha2



---

archive/issue_comments_007741.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-03-04T13:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1240#issuecomment-7741",
    "user": "https://github.com/zimmermann6"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_007742.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-03-04T13:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1240#issuecomment-7742",
    "user": "https://github.com/zimmermann6"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_007743.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-03-04T13:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1240#issuecomment-7743",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from closed to new.



---

archive/issue_events_001381.json:
```json
{
    "actor": "@zimmermann6",
    "created_at": "2010-03-04T13:54:01Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1240#event-1381"
}
```



---

archive/issue_comments_007744.json:
```json
{
    "body": "I reopen this ticket, since this issue is back with Sage 4.3.3:\n\n```\ntarte% sage\n**************************************************************************\nYou must compile Sage first using 'make' in the Sage root directory.\n(If you have already compiled Sage, you must set the SAGE_ROOT variable in \nthe file '/usr/local/sage-core2/sage').\n**************************************************************************\n```\n\nThis is due to wrong permissions (Sage was installed by Emmanuel Thome with `make dist`):\n\n```\ntiramisu ~ $ ls -l /usr/local/sage-core2/\ntotal 29884\n-rw-r--r--  2 thome caramel    71842 Mar  1 14:43 COPYING.txt\n-rw-r--r--  2 thome caramel    11123 Mar  1 14:43 README.txt\ndrwxr-xr-x  8 thome caramel     4096 Mar  1 16:42 data\ndrwxr-xr-x  4 thome caramel     4096 Mar  1 15:58 devel\ndrwx------ 15 thome caramel     4096 Mar  3 22:01 examples\n-rw-r--r--  1 thome caramel 30427884 Mar  1 17:04 install.log\ndrwx------  2 thome caramel     4096 Mar  3 22:01 ipython\ndrwx------ 12 thome caramel     4096 Mar  3 21:46 local\n-rw-r--r--  2 thome caramel     2618 Feb 11 17:55 makefile\n-rwxr-xr-x  2 thome caramel     1449 Feb 11 17:56 sage\n-rw-r--r--  2 thome caramel     1622 Mar  1 14:43 sage-README-osx.txt\n-rwxr-xr-x  2 thome caramel       38 Mar  1 14:43 sage-python\ndrwx------  6 thome caramel     4096 Mar  3 22:07 spkg\ndrwx------  2 thome caramel     4096 Mar  3 22:07 tmp\n```\n\nI declare this as a blocker since this issue should be fixed *once for all*\n(and automatically checked before doing a release).",
    "created_at": "2010-03-04T13:54:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1240#issuecomment-7744",
    "user": "https://github.com/zimmermann6"
}
```

I reopen this ticket, since this issue is back with Sage 4.3.3:

```
tarte% sage
**************************************************************************
You must compile Sage first using 'make' in the Sage root directory.
(If you have already compiled Sage, you must set the SAGE_ROOT variable in 
the file '/usr/local/sage-core2/sage').
**************************************************************************
```

This is due to wrong permissions (Sage was installed by Emmanuel Thome with `make dist`):

```
tiramisu ~ $ ls -l /usr/local/sage-core2/
total 29884
-rw-r--r--  2 thome caramel    71842 Mar  1 14:43 COPYING.txt
-rw-r--r--  2 thome caramel    11123 Mar  1 14:43 README.txt
drwxr-xr-x  8 thome caramel     4096 Mar  1 16:42 data
drwxr-xr-x  4 thome caramel     4096 Mar  1 15:58 devel
drwx------ 15 thome caramel     4096 Mar  3 22:01 examples
-rw-r--r--  1 thome caramel 30427884 Mar  1 17:04 install.log
drwx------  2 thome caramel     4096 Mar  3 22:01 ipython
drwx------ 12 thome caramel     4096 Mar  3 21:46 local
-rw-r--r--  2 thome caramel     2618 Feb 11 17:55 makefile
-rwxr-xr-x  2 thome caramel     1449 Feb 11 17:56 sage
-rw-r--r--  2 thome caramel     1622 Mar  1 14:43 sage-README-osx.txt
-rwxr-xr-x  2 thome caramel       38 Mar  1 14:43 sage-python
drwx------  6 thome caramel     4096 Mar  3 22:07 spkg
drwx------  2 thome caramel     4096 Mar  3 22:07 tmp
```

I declare this as a blocker since this issue should be fixed *once for all*
(and automatically checked before doing a release).



---

archive/issue_comments_007745.json:
```json
{
    "body": "Changing assignee from mabshoff to mvngu.",
    "created_at": "2010-03-04T13:55:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1240#issuecomment-7745",
    "user": "https://github.com/zimmermann6"
}
```

Changing assignee from mabshoff to mvngu.



---

archive/issue_events_001382.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-03-04T16:43:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1240#event-1382"
}
```



---

archive/issue_comments_007746.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-04T16:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1240#issuecomment-7746",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_007747.json:
```json
{
    "body": "Please do not reopen tickets that are already closed. Open another ticket for the specific issue related to this ticket and concerning Sage 4.3.3. Then reference this ticket from the newly opened ticket. The issue of the current ticket concerns Sage 2.9.1 and it has already been fixed for that release.",
    "created_at": "2010-03-04T16:43:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1240#issuecomment-7747",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Please do not reopen tickets that are already closed. Open another ticket for the specific issue related to this ticket and concerning Sage 4.3.3. Then reference this ticket from the newly opened ticket. The issue of the current ticket concerns Sage 2.9.1 and it has already been fixed for that release.



---

archive/issue_comments_007748.json:
```json
{
    "body": "> Please do not reopen tickets that are already closed. Open another ticket ...\n\nok, see #8437.",
    "created_at": "2010-03-04T19:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1240#issuecomment-7748",
    "user": "https://github.com/zimmermann6"
}
```

> Please do not reopen tickets that are already closed. Open another ticket ...

ok, see #8437.
