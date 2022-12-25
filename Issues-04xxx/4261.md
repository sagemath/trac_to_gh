# Issue 4261: [with patch, positive review] sympow Configure fails to handle aliases

archive/issues_004261.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  dkohel\n\nThe sympow Configure script has a `whichexe` function to determine which `rm`, `grep`, etc to call that effectively does `RM=`which rm``. If `rm` is an alias (e.g., aliased to `rm -i`), this fails.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4261\n\n",
    "closed_at": "2008-12-01T01:04:03Z",
    "created_at": "2008-10-10T09:43:01Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "[with patch, positive review] sympow Configure fails to handle aliases",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4261",
    "user": "https://github.com/wjp"
}
```
Assignee: mabshoff

CC:  dkohel

The sympow Configure script has a `whichexe` function to determine which `rm`, `grep`, etc to call that effectively does `RM=`which rm``. If `rm` is an alias (e.g., aliased to `rm -i`), this fails.



Issue created by migration from https://trac.sagemath.org/ticket/4261





---

archive/issue_comments_031010.json:
```json
{
    "body": "Forgot to mention: this was reported by David Kohel in Nancy during SD10.",
    "created_at": "2008-10-10T12:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4261#issuecomment-31010",
    "user": "https://github.com/wjp"
}
```

Forgot to mention: this was reported by David Kohel in Nancy during SD10.



---

archive/issue_comments_031011.json:
```json
{
    "body": "Attachment [trac4261_sympow_Configure.patch](tarball://root/attachments/some-uuid/ticket4261/trac4261_sympow_Configure.patch) by @wjp created at 2008-10-12 11:51:16",
    "created_at": "2008-10-12T11:51:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4261#issuecomment-31011",
    "user": "https://github.com/wjp"
}
```

Attachment [trac4261_sympow_Configure.patch](tarball://root/attachments/some-uuid/ticket4261/trac4261_sympow_Configure.patch) by @wjp created at 2008-10-12 11:51:16



---

archive/issue_comments_031012.json:
```json
{
    "body": "This will be fixed in 3.1.3 :)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-13T09:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4261#issuecomment-31012",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This will be fixed in 3.1.3 :)

Cheers,

Michael



---

archive/issue_events_009625.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-13T09:45:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "milestone": "sage-3.1.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4261#event-9625"
}
```



---

archive/issue_events_009626.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-28T16:40:55Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "milestone": "sage-3.1.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4261#event-9626"
}
```



---

archive/issue_events_009627.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-28T16:40:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4261#event-9627"
}
```



---

archive/issue_comments_031013.json:
```json
{
    "body": "Sorry that this didn't make it into 3.1.3/4. But I will attempt to get this into 3.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-28T16:40:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4261#issuecomment-31013",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Sorry that this didn't make it into 3.1.3/4. But I will attempt to get this into 3.2.

Cheers,

Michael



---

archive/issue_comments_031014.json:
```json
{
    "body": "REFEREE REPORT:\n\n1. It does not fail is rm is an alias.  It gives the original executable with an exact path. \n\n```\nteragon-2:sympow-1.018.1.p5 wstein$ alias rm=\"rm -i\"\nteragon-2:sympow-1.018.1.p5 wstein$ which rm\n/bin/rm\nteragon-2:sympow-1.018.1.p5 wstein$ RM=`which rm`\nteragon-2:sympow-1.018.1.p5 wstein$ echo $RM\n/bin/rm\n```\n\nSo I totally don't get what the problem is.  The above patch would have the effect of making it so the scripts would annoyingly suddenly actually *be* interactive if one has aliased rm to \"rm -i\".\n\nSo from my point of view, it looks like this patch introduces a bug instead of fixing one.\n\n2. This patch would replace all the absolute paths to programs to their names, thus completely removing whatever \"upstream's\" point was in having those variables.  That's suspicious.\n\nSo I'm dubious.",
    "created_at": "2008-11-28T05:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4261#issuecomment-31014",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:

1. It does not fail is rm is an alias.  It gives the original executable with an exact path. 

```
teragon-2:sympow-1.018.1.p5 wstein$ alias rm="rm -i"
teragon-2:sympow-1.018.1.p5 wstein$ which rm
/bin/rm
teragon-2:sympow-1.018.1.p5 wstein$ RM=`which rm`
teragon-2:sympow-1.018.1.p5 wstein$ echo $RM
/bin/rm
```

So I totally don't get what the problem is.  The above patch would have the effect of making it so the scripts would annoyingly suddenly actually *be* interactive if one has aliased rm to "rm -i".

So from my point of view, it looks like this patch introduces a bug instead of fixing one.

2. This patch would replace all the absolute paths to programs to their names, thus completely removing whatever "upstream's" point was in having those variables.  That's suspicious.

So I'm dubious.



---

archive/issue_comments_031015.json:
```json
{
    "body": "The behavior of \"alias\" might be shell dependent which might contribute to the problem here. This was initially reported by David Kohel, so let's CC him.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T05:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4261#issuecomment-31015",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The behavior of "alias" might be shell dependent which might contribute to the problem here. This was initially reported by David Kohel, so let's CC him.

Cheers,

Michael



---

archive/issue_comments_031016.json:
```json
{
    "body": "```\nHi,\n\nBased on Mark's remark below, I give #4261 a positive review, since it does\nin fact do just what Mark suggests below.\n\nWilliam\n\nOn Thu, Nov 27, 2008 at 9:57 PM, Mark Watkins <watkins@maths.usyd.edu.au> wrote:\n> William Stein wrote:\n>> Do you guy's have any comments on this:\n>>    http://trac.sagemath.org/sage_trac/ticket/4261\n>> I'm tempted to mark it invalid, but maybe I'm missing the point.\n>\n> I think I agree that the problem is with the shell-version of alias.\n>\n> I was only trying to make something that would be more likely to work than\n> the simple /bin/rm, etc., but it seems that I failed. Probably it is safe to\n> just use $RM=rm (same with $CP, $TAR, $MKDIR, $TOUCH) in the Makefile and\n> hope the user has a sufficient path. Also, echo might be shell-dependent.\n>\n> I think some buildutils simply tree-search the path and/or the\n> whole directory structure, but I didn't want to attempt that.\n>\n> ===\n> Mark Watkins\n> watkins@maths.usyd.edu.au\n>\n\n\n\n-- \nWilliam Stein\nAssociate Professor of Mathematics\nUniversity of Washington\nhttp://wstein.org\n\n```",
    "created_at": "2008-11-28T06:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4261#issuecomment-31016",
    "user": "https://github.com/williamstein"
}
```

```
Hi,

Based on Mark's remark below, I give #4261 a positive review, since it does
in fact do just what Mark suggests below.

William

On Thu, Nov 27, 2008 at 9:57 PM, Mark Watkins <watkins@maths.usyd.edu.au> wrote:
> William Stein wrote:
>> Do you guy's have any comments on this:
>>    http://trac.sagemath.org/sage_trac/ticket/4261
>> I'm tempted to mark it invalid, but maybe I'm missing the point.
>
> I think I agree that the problem is with the shell-version of alias.
>
> I was only trying to make something that would be more likely to work than
> the simple /bin/rm, etc., but it seems that I failed. Probably it is safe to
> just use $RM=rm (same with $CP, $TAR, $MKDIR, $TOUCH) in the Makefile and
> hope the user has a sufficient path. Also, echo might be shell-dependent.
>
> I think some buildutils simply tree-search the path and/or the
> whole directory structure, but I didn't want to attempt that.
>
> ===
> Mark Watkins
> watkins@maths.usyd.edu.au
>



-- 
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org

```



---

archive/issue_comments_031017.json:
```json
{
    "body": "This is going into 3.2.1.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T09:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4261#issuecomment-31017",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is going into 3.2.1.

Cheers,

Michael



---

archive/issue_events_009628.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-30T09:00:19Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4261#event-9628"
}
```



---

archive/issue_events_009629.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-30T09:00:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "milestone": "sage-3.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4261#event-9629"
}
```



---

archive/issue_comments_031018.json:
```json
{
    "body": "Wjp's fixes have been merged into \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/rc1/sympow-1.018.1.p6.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-12-01T01:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4261#issuecomment-31018",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Wjp's fixes have been merged into 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/rc1/sympow-1.018.1.p6.spkg

Cheers,

Michael



---

archive/issue_comments_031019.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc1",
    "created_at": "2008-12-01T01:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4261#issuecomment-31019",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.rc1



---

archive/issue_events_009630.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-01T01:04:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4261#event-9630"
}
```



---

archive/issue_comments_031020.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-01T01:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4261",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4261#issuecomment-31020",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
