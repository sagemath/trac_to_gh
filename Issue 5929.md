# Issue 5929: switch from clisp to ecl

archive/issues_005929.json:
```json
{
    "body": "Assignee: mabshoff\n\nReplace clisp by ECL in Sage.  Need for the Solaris port.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5929\n\n",
    "created_at": "2009-04-29T01:50:33Z",
    "labels": [
        "component: porting",
        "blocker"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "switch from clisp to ecl",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5929",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

Replace clisp by ECL in Sage.  Need for the Solaris port.

Issue created by migration from https://trac.sagemath.org/ticket/5929





---

archive/issue_comments_046783.json:
```json
{
    "body": "fix for assumption hang with ecl",
    "created_at": "2009-05-11T03:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5929#issuecomment-46783",
    "user": "https://github.com/tornaria"
}
```

fix for assumption hang with ecl



---

archive/issue_comments_046784.json:
```json
{
    "body": "Attachment [trac_5929-fix_assumption_hang.patch](tarball://root/attachments/some-uuid/ticket5929/trac_5929-fix_assumption_hang.patch) by @tornaria created at 2009-05-11 03:32:52\n\nfix (workaround) for out of sync hang which timeouts a doctest",
    "created_at": "2009-05-11T03:32:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5929#issuecomment-46784",
    "user": "https://github.com/tornaria"
}
```

Attachment [trac_5929-fix_assumption_hang.patch](tarball://root/attachments/some-uuid/ticket5929/trac_5929-fix_assumption_hang.patch) by @tornaria created at 2009-05-11 03:32:52

fix (workaround) for out of sync hang which timeouts a doctest



---

archive/issue_comments_046785.json:
```json
{
    "body": "Attachment [trac_5929-fix_outofsync_hang.patch](tarball://root/attachments/some-uuid/ticket5929/trac_5929-fix_outofsync_hang.patch) by @tornaria created at 2009-05-11 03:35:35\n\nComment for attachment:trac_5929-fix_assumption_hang.patch:\n\nFor #5929: fix hang in maxima/ecl due to assumption questions\n\nWhen maxima asks a question, current code sends CTRL-C\ntwice to break, then raises an exception. This used to work with\nclisp, but for ecl it actually hangs. A test case is given by\n\n\n```\nvar(\"Ax,Bx,By\")\nt = -Ax*sin(sqrt(Ax^2)/2)/(sqrt(Ax^2)*sqrt(By^2 + Bx^2))\nlimit(t, Ax=0)\n```\n\n\nIt turns out that it is possible to \"break\" from the question by just\nsending \";\" by itself to maxima. The current patch changes to this\nmethod of escaping. It works with clisp or ecl.",
    "created_at": "2009-05-11T03:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5929#issuecomment-46785",
    "user": "https://github.com/tornaria"
}
```

Attachment [trac_5929-fix_outofsync_hang.patch](tarball://root/attachments/some-uuid/ticket5929/trac_5929-fix_outofsync_hang.patch) by @tornaria created at 2009-05-11 03:35:35

Comment for attachment:trac_5929-fix_assumption_hang.patch:

For #5929: fix hang in maxima/ecl due to assumption questions

When maxima asks a question, current code sends CTRL-C
twice to break, then raises an exception. This used to work with
clisp, but for ecl it actually hangs. A test case is given by


```
var("Ax,Bx,By")
t = -Ax*sin(sqrt(Ax^2)/2)/(sqrt(Ax^2)*sqrt(By^2 + Bx^2))
limit(t, Ax=0)
```


It turns out that it is possible to "break" from the question by just
sending ";" by itself to maxima. The current patch changes to this
method of escaping. It works with clisp or ecl.



---

archive/issue_comments_046786.json:
```json
{
    "body": "Comment for attachment:trac_5929-fix_outofsync_hang.patch:\n\nFor #5929: fix timeout in maxima/ecl due to out-of-synch condition\n\nThis is triggered by the following doctest\n\n```\nsage: maxima._sendstr('1/1'*500)\nsage: maxima('2+2')\n```\n\nIn fact, the first line is missing a semicolon, so maxima is stuck out\nof synch; the synchronization code is run for the second line, and\nafter a timeout, it tries to break by sending a ctrl-c (this happens\nin Expect._interrupt()), but ctrl-c is broken with ecl, so this hangs.\n\nThe current fix adds an explicit semicolon to the synchronization\ncode. This fixes the timeout in the above doctest. The hang is still\nlatent, because there seems to be no way to interrupt maxima/ecl.",
    "created_at": "2009-05-11T03:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5929#issuecomment-46786",
    "user": "https://github.com/tornaria"
}
```

Comment for attachment:trac_5929-fix_outofsync_hang.patch:

For #5929: fix timeout in maxima/ecl due to out-of-synch condition

This is triggered by the following doctest

```
sage: maxima._sendstr('1/1'*500)
sage: maxima('2+2')
```

In fact, the first line is missing a semicolon, so maxima is stuck out
of synch; the synchronization code is run for the second line, and
after a timeout, it tries to break by sending a ctrl-c (this happens
in Expect._interrupt()), but ctrl-c is broken with ecl, so this hangs.

The current fix adds an explicit semicolon to the synchronization
code. This fixes the timeout in the above doctest. The hang is still
latent, because there seems to be no way to interrupt maxima/ecl.



---

archive/issue_comments_046787.json:
```json
{
    "body": "I am splitting this off the ecl and maxima spkgs.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T07:33:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5929#issuecomment-46787",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am splitting this off the ecl and maxima spkgs.

Cheers,

Michael



---

archive/issue_comments_046788.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-11T07:33:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5929#issuecomment-46788",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046789.json:
```json
{
    "body": "Changing assignee from mabshoff to @tornaria.",
    "created_at": "2009-05-12T06:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5929#issuecomment-46789",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from mabshoff to @tornaria.



---

archive/issue_comments_046790.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2009-05-12T06:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5929#issuecomment-46790",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from assigned to new.



---

archive/issue_comments_046791.json:
```json
{
    "body": "Ok, I am removing the ecl doctest fix since the two patches posted by Gonzalo fix this problem, too. So to keep credit and review simple I am giving this a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T06:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5929#issuecomment-46791",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, I am removing the ecl doctest fix since the two patches posted by Gonzalo fix this problem, too. So to keep credit and review simple I am giving this a positive review.

Cheers,

Michael



---

archive/issue_comments_046792.json:
```json
{
    "body": "Merged both patches in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T06:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5929#issuecomment-46792",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_046793.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-12T06:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5929",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5929#issuecomment-46793",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006183.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-05-12T06:34:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5929",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5929#event-6183"
}
```
