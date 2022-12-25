# Issue 2311: remove stupid timeout from sage-location

archive/issues_002311.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2311\n\n",
    "created_at": "2008-02-26T04:44:56Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "remove stupid timeout from sage-location",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2311",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff



Issue created by migration from https://trac.sagemath.org/ticket/2311





---

archive/issue_comments_015346.json:
```json
{
    "body": "Attachment [scripts-2311.patch](tarball://root/attachments/some-uuid/ticket2311/scripts-2311.patch) by @williamstein created at 2008-02-26 04:45:41",
    "created_at": "2008-02-26T04:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2311#issuecomment-15346",
    "user": "https://github.com/williamstein"
}
```

Attachment [scripts-2311.patch](tarball://root/attachments/some-uuid/ticket2311/scripts-2311.patch) by @williamstein created at 2008-02-26 04:45:41



---

archive/issue_comments_015347.json:
```json
{
    "body": "```\n>  > $ wgethttp://sagemath.org/SAGEbin/linux/64bit/sage-2.10.2-debian-64bit-inte...\n>  \n> > $ tar xzf sage-2.10.2-debian-64bit-intel-x86_64-Linux.tar.gz\n>  > $ ln -s sage-2.10.2-debian-64bit-intel-x86_64-Linux/ sage\n>  > $ cd sage\n>  > $ ./sage\n>  > ----------------------------------------------------------------------\n>  > | SAGE Version 2.10.2, Release Date: 2008-02-22                      |\n>  > | Type notebook() for the GUI, and license() for information.        |\n>  > ----------------------------------------------------------------------\n>  > The SAGE install tree may have moved.\n>  > Regenerating Python.pyo and .pyc files that hardcode the install PATH\n>  > (please wait less than a minute)...\n>  > Please do not interrupt this.\n>  > /home/ondra/ext/sage/local/bin/sage-sage: line 149: 18575 Alarm clock\n>  >            \"$SAGE_ROOT/local/bin/\"sage-location\n>  \n>  I just grepped through my tree and there is no \"Alarm clock\" string\n>  anywhere. I also checked the binary you tried and there is no string\n>  in there either. The log in SAGE_LOCAL/bin doesn't indicate any\n>  commits that I don't have and the repo is clean, i.e. no outstanding\n>  changes.\n>  \n>  So: can anybody else reproduce this?\n\nThis is in sage-location:\n\nimport signal   \nsignal.alarm(360)\n\nThis is *stupid*.  It's doing a process that really really better not get interrupted, and it's\ninterrupting itself if it takes more than 6 minutes.  I can't imagine what idiot wrote such \nbad code....\n\n... oh wait, that was me.  I think that was in there right when that code was first written,\nmainly for debugging purposes when I was doing some testing.  Anyway...  didn't\nDavid Harvey say something in irc about all my old code being \"impatient\" -- I guess\nthis is a prime example of that!\n\n```",
    "created_at": "2008-02-26T04:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2311#issuecomment-15347",
    "user": "https://github.com/williamstein"
}
```

```
>  > $ wgethttp://sagemath.org/SAGEbin/linux/64bit/sage-2.10.2-debian-64bit-inte...
>  
> > $ tar xzf sage-2.10.2-debian-64bit-intel-x86_64-Linux.tar.gz
>  > $ ln -s sage-2.10.2-debian-64bit-intel-x86_64-Linux/ sage
>  > $ cd sage
>  > $ ./sage
>  > ----------------------------------------------------------------------
>  > | SAGE Version 2.10.2, Release Date: 2008-02-22                      |
>  > | Type notebook() for the GUI, and license() for information.        |
>  > ----------------------------------------------------------------------
>  > The SAGE install tree may have moved.
>  > Regenerating Python.pyo and .pyc files that hardcode the install PATH
>  > (please wait less than a minute)...
>  > Please do not interrupt this.
>  > /home/ondra/ext/sage/local/bin/sage-sage: line 149: 18575 Alarm clock
>  >            "$SAGE_ROOT/local/bin/"sage-location
>  
>  I just grepped through my tree and there is no "Alarm clock" string
>  anywhere. I also checked the binary you tried and there is no string
>  in there either. The log in SAGE_LOCAL/bin doesn't indicate any
>  commits that I don't have and the repo is clean, i.e. no outstanding
>  changes.
>  
>  So: can anybody else reproduce this?

This is in sage-location:

import signal   
signal.alarm(360)

This is *stupid*.  It's doing a process that really really better not get interrupted, and it's
interrupting itself if it takes more than 6 minutes.  I can't imagine what idiot wrote such 
bad code....

... oh wait, that was me.  I think that was in there right when that code was first written,
mainly for debugging purposes when I was doing some testing.  Anyway...  didn't
David Harvey say something in irc about all my old code being "impatient" -- I guess
this is a prime example of that!

```



---

archive/issue_comments_015348.json:
```json
{
    "body": "Patch looks good.",
    "created_at": "2008-02-26T04:59:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2311#issuecomment-15348",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good.



---

archive/issue_comments_015349.json:
```json
{
    "body": "Merged in Sage 2.10.3.alpha0",
    "created_at": "2008-02-26T04:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2311#issuecomment-15349",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.alpha0



---

archive/issue_comments_015350.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-26T04:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2311#issuecomment-15350",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005443.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-26T04:59:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2311",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2311#event-5443"
}
```
