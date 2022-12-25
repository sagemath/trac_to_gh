# Issue 3779: inconsistency for variables method, leads to errors in differentiation

archive/issues_003779.json:
```json
{
    "body": "Assignee: @garyfurnish\n\n\n```\n\nHi William:\n\nI was running Sage 3.0.2 on Linux when the error occurred.  Just now i\nupgraded to 'sage-3.0.6-i686-Linux-debian-intel' without problems, ran\nthe same code (in a notebook and on the command line), and got the\nsame error.  Hmm, i don't understand why Sage can do 'diff(f*SR(2),x)'\nbut not 'diff(f*SR(1),x)'.\n\nAlex\n```\n\n\nThis boils down to the fact that some symbolic objects take an extra argument in their `variables` method. It is unclear what the meaning of this argument is (couldn't find any examples) and if it should be removed, or added, to make things consistent. (I'd guess removed, but I don't want to break things.) \n\nIssue created by migration from https://trac.sagemath.org/ticket/3779\n\n",
    "created_at": "2008-08-06T04:29:22Z",
    "labels": [
        "component: calculus",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "inconsistency for variables method, leads to errors in differentiation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3779",
    "user": "https://github.com/robertwb"
}
```
Assignee: @garyfurnish


```

Hi William:

I was running Sage 3.0.2 on Linux when the error occurred.  Just now i
upgraded to 'sage-3.0.6-i686-Linux-debian-intel' without problems, ran
the same code (in a notebook and on the command line), and got the
same error.  Hmm, i don't understand why Sage can do 'diff(f*SR(2),x)'
but not 'diff(f*SR(1),x)'.

Alex
```


This boils down to the fact that some symbolic objects take an extra argument in their `variables` method. It is unclear what the meaning of this argument is (couldn't find any examples) and if it should be removed, or added, to make things consistent. (I'd guess removed, but I don't want to break things.) 

Issue created by migration from https://trac.sagemath.org/ticket/3779





---

archive/issue_comments_026810.json:
```json
{
    "body": "The argument doesn't exist in symbolics, so I'm in favor of removal (and I have no idea what it does either)",
    "created_at": "2008-08-06T06:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26810",
    "user": "https://github.com/garyfurnish"
}
```

The argument doesn't exist in symbolics, so I'm in favor of removal (and I have no idea what it does either)



---

archive/issue_comments_026811.json:
```json
{
    "body": "Changing assignee from @garyfurnish to @mwhansen.",
    "created_at": "2008-08-06T20:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26811",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @garyfurnish to @mwhansen.



---

archive/issue_comments_026812.json:
```json
{
    "body": "The argument was used to pass in additional variables to the variables method which would then be subsequently returned.  This functionality was never used, and I can't / couldn't think of a case where it would be needed.  So, I do think the correct fix is to remove it.  I've attached a patch which does that and passes tests.",
    "created_at": "2008-08-06T20:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26812",
    "user": "https://github.com/mwhansen"
}
```

The argument was used to pass in additional variables to the variables method which would then be subsequently returned.  This functionality was never used, and I can't / couldn't think of a case where it would be needed.  So, I do think the correct fix is to remove it.  I've attached a patch which does that and passes tests.



---

archive/issue_comments_026813.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-06T20:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26813",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_events_008659.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-08-06T20:09:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "milestone": "sage-3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3779#event-8659"
}
```



---

archive/issue_comments_026814.json:
```json
{
    "body": "Attachment [trac_3779.patch](tarball://root/attachments/some-uuid/ticket3779/trac_3779.patch) by @robertwb created at 2008-08-07 02:02:48\n\nLooks good to me, and fixes the bug. The only question I had is why you wrote tuple([]) rather than (), but I'm OK with that.",
    "created_at": "2008-08-07T02:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26814",
    "user": "https://github.com/robertwb"
}
```

Attachment [trac_3779.patch](tarball://root/attachments/some-uuid/ticket3779/trac_3779.patch) by @robertwb created at 2008-08-07 02:02:48

Looks good to me, and fixes the bug. The only question I had is why you wrote tuple([]) rather than (), but I'm OK with that.



---

archive/issue_comments_026815.json:
```json
{
    "body": "There's no real reason -- it's just what I happened to type :-)",
    "created_at": "2008-08-07T02:12:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26815",
    "user": "https://github.com/mwhansen"
}
```

There's no real reason -- it's just what I happened to type :-)



---

archive/issue_comments_026816.json:
```json
{
    "body": "Attachment [trac_3779-2.patch](tarball://root/attachments/some-uuid/ticket3779/trac_3779-2.patch) by @mwhansen created at 2008-08-10 06:13:37",
    "created_at": "2008-08-10T06:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26816",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_3779-2.patch](tarball://root/attachments/some-uuid/ticket3779/trac_3779-2.patch) by @mwhansen created at 2008-08-10 06:13:37



---

archive/issue_comments_026817.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-10T06:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26817",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_008660.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-10T06:33:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3779#event-8660"
}
```



---

archive/issue_comments_026818.json:
```json
{
    "body": "Merged both patches in Sage 3.1.alpha1",
    "created_at": "2008-08-10T06:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3779#issuecomment-26818",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.1.alpha1
