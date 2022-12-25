# Issue 22: 32/64/32-bit building switch

archive/issues_000022.json:
```json
{
    "body": "Assignee: somebody\n\nShould there be something to keep people from building on 32-bit then 64-bit then 32-bit.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/22\n\n",
    "created_at": "2006-09-12T23:21:52Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "32/64/32-bit building switch",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/22",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

Should there be something to keep people from building on 32-bit then 64-bit then 32-bit.


Issue created by migration from https://trac.sagemath.org/ticket/22





---

archive/issue_comments_000162.json:
```json
{
    "body": "```\n[01:10] <william> the problem was doing something like \"sage -br\" on both a 32-bit and 64-bit machine but\n[01:10] <william> with a shared filesystem.\n[01:10] <mabshoff> Ah, that makes sense.\n[01:10] <william> I.e., when you build sage for one architecture, maybe you shouldn't be allowed to\n[01:10] <william> do \"sage -br\" or \"sage -i\" if the architectrue doesn't match.\n[01:11] <mabshoff> okay,\n[01:11] <william> or something like that.\n```",
    "created_at": "2007-08-19T08:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-162",
    "user": "https://github.com/williamstein"
}
```

```
[01:10] <william> the problem was doing something like "sage -br" on both a 32-bit and 64-bit machine but
[01:10] <william> with a shared filesystem.
[01:10] <mabshoff> Ah, that makes sense.
[01:10] <william> I.e., when you build sage for one architecture, maybe you shouldn't be allowed to
[01:10] <william> do "sage -br" or "sage -i" if the architectrue doesn't match.
[01:11] <mabshoff> okay,
[01:11] <william> or something like that.
```



---

archive/issue_comments_000163.json:
```json
{
    "body": "```\n[10:01] <wstein> regarding #22 the idea is that people might do \"sage -br\" on one machine, then login to another machine that\n[10:02] <wstein> nsf mounts the same directory, and muck things up.\n[10:02] <wstein> We should cache \"uname -p\" in SAGE_ROOT, and if it changes not allow \"sage -br\" unless the user\n[10:02] <wstein> (or sage -i) or sage -upgrade, unless the user manually deletes the file.\n[10:03] <wstein> Thoughts?\n```",
    "created_at": "2007-09-18T17:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-163",
    "user": "https://github.com/williamstein"
}
```

```
[10:01] <wstein> regarding #22 the idea is that people might do "sage -br" on one machine, then login to another machine that
[10:02] <wstein> nsf mounts the same directory, and muck things up.
[10:02] <wstein> We should cache "uname -p" in SAGE_ROOT, and if it changes not allow "sage -br" unless the user
[10:02] <wstein> (or sage -i) or sage -upgrade, unless the user manually deletes the file.
[10:03] <wstein> Thoughts?
```



---

archive/issue_comments_000164.json:
```json
{
    "body": "Changing assignee from somebody to mabshoff.",
    "created_at": "2007-11-26T01:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-164",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from somebody to mabshoff.



---

archive/issue_events_000039.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-26T01:12:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "milestone": "sage-2.8.15",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/22#event-39"
}
```



---

archive/issue_comments_000165.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-26T01:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-165",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_000166.json:
```json
{
    "body": "Changing assignee from mabshoff to @garyfurnish.",
    "created_at": "2008-03-21T23:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-166",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from mabshoff to @garyfurnish.



---

archive/issue_comments_000167.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-03-21T23:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-167",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from assigned to new.



---

archive/issue_comments_000168.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-21T23:53:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-168",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_000169.json:
```json
{
    "body": "Fixed in #1261 (PBuild)",
    "created_at": "2008-03-23T12:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-169",
    "user": "https://github.com/garyfurnish"
}
```

Fixed in #1261 (PBuild)



---

archive/issue_comments_000170.json:
```json
{
    "body": "Changing component from basic arithmetic to build.",
    "created_at": "2008-04-04T19:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-170",
    "user": "https://github.com/garyfurnish"
}
```

Changing component from basic arithmetic to build.



---

archive/issue_comments_000171.json:
```json
{
    "body": "Attachment [trac_22.patch](tarball://root/attachments/some-uuid/ticket22/trac_22.patch) by mabshoff created at 2009-01-16 17:29:08",
    "created_at": "2009-01-16T17:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-171",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_22.patch](tarball://root/attachments/some-uuid/ticket22/trac_22.patch) by mabshoff created at 2009-01-16 17:29:08



---

archive/issue_comments_000172.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-01-16T17:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-172",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from assigned to new.



---

archive/issue_events_000040.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-16T17:30:08Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "milestone": "sage-2.8.15",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/22#event-40"
}
```



---

archive/issue_events_000041.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-16T17:30:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/22#event-41"
}
```



---

archive/issue_comments_000173.json:
```json
{
    "body": "Changing assignee from @garyfurnish to mabshoff.",
    "created_at": "2009-01-16T17:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-173",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @garyfurnish to mabshoff.



---

archive/issue_comments_000174.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-16T17:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-174",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_000175.json:
```json
{
    "body": "Mhh, looking at the complete ticket history this patch does not cover all what needs to be fixed on this ticket. I will post a patch on top that also fixes this issue.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-16T17:46:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-175",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mhh, looking at the complete ticket history this patch does not cover all what needs to be fixed on this ticket. I will post a patch on top that also fixes this issue.

Cheers,

Michael



---

archive/issue_comments_000176.json:
```json
{
    "body": "Unfortunately the trick William suggested does not work everywhere, i.e. even on the latest stable Debian release this happens:\n\n```\nmabshoff@modular:~$ uname -p\nunknown\n```\nFrom **man uname** on that box:\n\n```\n       -p, --processor\n              print the processor type or \"unknown\"\n```\n\nSo we might want to make that part of the ticket a followup ticket.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-16T17:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-176",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Unfortunately the trick William suggested does not work everywhere, i.e. even on the latest stable Debian release this happens:

```
mabshoff@modular:~$ uname -p
unknown
```
From **man uname** on that box:

```
       -p, --processor
              print the processor type or "unknown"
```

So we might want to make that part of the ticket a followup ticket.

Cheers,

Michael



---

archive/issue_comments_000177.json:
```json
{
    "body": "Having thought about this and played around a little with uname it seems that it will not work and is not fine grained enough anyway. I would suggest to do write a small C program that identifies the following:\n\n* mode: i.e. 32, 64 bit\n* os: linux, osx, solaris, freebsd, cygwin\n* release: this would be the distribution on Linux, OSX 10.4/10.5, Solaris 10/Solaris 11/Opensolaris and so on\n\nThe way we can properly identify the build platform and decide more intelligently if we issue a warning, i.e running the Fedora 10 build on a Fedora 9 box should abort since it doesn't work. The test should be wrapped in a shell script since the binary will obviously only run on a subset of arches, i.e. if the binary fails to run we just about and print a canned warning together with a config info saved as text that is created when building the binary.\n\nThis is enough a task to split it off to a new ticket. I have some basic code that does some of the above already for OSX since I need this kind of code while cleaning up the build system.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-01-16T18:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-177",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Having thought about this and played around a little with uname it seems that it will not work and is not fine grained enough anyway. I would suggest to do write a small C program that identifies the following:

* mode: i.e. 32, 64 bit
* os: linux, osx, solaris, freebsd, cygwin
* release: this would be the distribution on Linux, OSX 10.4/10.5, Solaris 10/Solaris 11/Opensolaris and so on

The way we can properly identify the build platform and decide more intelligently if we issue a warning, i.e running the Fedora 10 build on a Fedora 9 box should abort since it doesn't work. The test should be wrapped in a shell script since the binary will obviously only run on a subset of arches, i.e. if the binary fails to run we just about and print a canned warning together with a config info saved as text that is created when building the binary.

This is enough a task to split it off to a new ticket. I have some basic code that does some of the above already for OSX since I need this kind of code while cleaning up the build system.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_000178.json:
```json
{
    "body": "This is a \"perfect patch.\"\n\n... ;-)",
    "created_at": "2009-01-22T17:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-178",
    "user": "https://github.com/rlmill"
}
```

This is a "perfect patch."

... ;-)



---

archive/issue_events_000042.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T00:34:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/22#event-42"
}
```



---

archive/issue_comments_000179.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1.\n\nNote that the remaining issue from this ticket has been moved to #5062.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T00:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-179",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1.

Note that the remaining issue from this ticket has been moved to #5062.

Cheers,

Michael



---

archive/issue_comments_000180.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T00:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/22",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/22#issuecomment-180",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
