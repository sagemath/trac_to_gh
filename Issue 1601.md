# Issue 1601: issue with noclobber and building sage

archive/issues_001601.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\n\n > Hi, William,\n >\n > I have had trouble getting the most recent versions of sage to\n > compile.  (This is Mac OS X 10.4.11, gcc 4.0.1, 5367.)  My problem\n > started with 2.8.15, and continued with 2.9.  Eventually, I found out\n > that something (I can't figure out what just yet) is returning the\n > string \"noclobber\", which in turn is being passed along as an argument\n > to local/bin/sage-spkg.\n >\n > After the line\n >\n >     PKG_BASE=`echo \"$PKG_NAME\" | sed -e \"s/-.*//\"`\n >\n > I added\n >\n >     if [ $PKG_SRC == \"noclobber\" ]; then\n >       exit 0\n >     fi\n >\n > which cleared up the problem; otherwise, sage tries (and obviously\n > fails) to compile noclobber.spkg.\n >\n > I wish that I had the time to track down which environment variable or\n > alias is causing the problem.  This has something to do with\n > redirecting output, and specifically 2>&1 as an option to some\n > command.  I never quite worked out where the problem is, and I don't\n > think that my work-around could be harmful, so I suggest that you\n > include it in the next release.--Rob\n >\n\nHi,\n\nI found out that I had the line \"set noclobber\" in both my .bashrc and\n.bash_profile files.  Removing that cleared up the problem.  I have no\nclue why I ever put added the line in the first place, nor why it\nwould have caused a problem.--Rob\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1601\n\n",
    "created_at": "2007-12-27T01:16:55Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "issue with noclobber and building sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1601",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty


```

 > Hi, William,
 >
 > I have had trouble getting the most recent versions of sage to
 > compile.  (This is Mac OS X 10.4.11, gcc 4.0.1, 5367.)  My problem
 > started with 2.8.15, and continued with 2.9.  Eventually, I found out
 > that something (I can't figure out what just yet) is returning the
 > string "noclobber", which in turn is being passed along as an argument
 > to local/bin/sage-spkg.
 >
 > After the line
 >
 >     PKG_BASE=`echo "$PKG_NAME" | sed -e "s/-.*//"`
 >
 > I added
 >
 >     if [ $PKG_SRC == "noclobber" ]; then
 >       exit 0
 >     fi
 >
 > which cleared up the problem; otherwise, sage tries (and obviously
 > fails) to compile noclobber.spkg.
 >
 > I wish that I had the time to track down which environment variable or
 > alias is causing the problem.  This has something to do with
 > redirecting output, and specifically 2>&1 as an option to some
 > command.  I never quite worked out where the problem is, and I don't
 > think that my work-around could be harmful, so I suggest that you
 > include it in the next release.--Rob
 >

Hi,

I found out that I had the line "set noclobber" in both my .bashrc and
.bash_profile files.  Removing that cleared up the problem.  I have no
clue why I ever put added the line in the first place, nor why it
would have caused a problem.--Rob
```


Issue created by migration from https://trac.sagemath.org/ticket/1601





---

archive/issue_comments_010150.json:
```json
{
    "body": "\n```\n[17:47] <mabshoff> wstein-2190: Who is \"Rob\" from #1601?\n[17:47] <wstein-2190> Rob Gross; a number theorist at Boston College.\n```\n",
    "created_at": "2008-02-18T17:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1601#issuecomment-10150",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```


```
[17:47] <mabshoff> wstein-2190: Who is "Rob" from #1601?
[17:47] <wstein-2190> Rob Gross; a number theorist at Boston College.
```




---

archive/issue_comments_010151.json:
```json
{
    "body": "Changing assignee from cwitty to mabshoff.",
    "created_at": "2008-02-18T17:58:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1601#issuecomment-10151",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from cwitty to mabshoff.



---

archive/issue_comments_010152.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-18T17:58:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1601#issuecomment-10152",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010153.json:
```json
{
    "body": "Attachment [Sage-2.10.2-trac_1601.patch](tarball://root/attachments/some-uuid/ticket1601/Sage-2.10.2-trac_1601.patch) by mabshoff created at 2008-02-18 18:02:19",
    "created_at": "2008-02-18T18:02:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1601#issuecomment-10153",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [Sage-2.10.2-trac_1601.patch](tarball://root/attachments/some-uuid/ticket1601/Sage-2.10.2-trac_1601.patch) by mabshoff created at 2008-02-18 18:02:19



---

archive/issue_events_001759.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-18T21:28:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1601",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1601#event-1759"
}
```



---

archive/issue_comments_010154.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-18T21:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1601#issuecomment-10154",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010155.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-18T21:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1601#issuecomment-10155",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha1
