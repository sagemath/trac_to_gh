# Issue 80: Clarify: version.py versus sage-version

archive/issues_000080.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nOn Sat, 23 Sep 2006 07:55:20 -0700, David Joyner <wdjoyner@gmail.com> wrote:\n\n>> To try it out in the latest SAGE (1.3.7.3.3 and not earlier!),\n>> type (from <SAGE_ROOT>/deve/sage)\n>>\n>> sage -hg pull http://sage.math.washington.edu/sage/hg/sage-main\n>> sage -hg merge    # if necessary\n>> sage -hg update\n>>\n>>\n>\n> wdj@wooster:~/sagefiles/sage-1.2.0/devel/sage$ ../../sage -hg update\n> remote changed .hgtags which local deleted\n> (k)eep or (d)elete?   k\n> remote changed export which local deleted\n> (k)eep or (d)elete? k\n> merging sage/version.py\n>\n> Now kdiff3 (which I mistook for a browser window) opens with some text\n> highlighted\n> in yellow and red. The bar at the bottom says \"Number of remaining\n> unsolved conflicts: 1\".\n> The conflict appears to be in version.py. I clicked on \"merge\" on the\n> top bar and then\n> picked \"line 1 from C\", which was one of the options in the pop-down  \n> menu,\n> then then clicked on \"save\" and quit. If memory serves (which is iffy),\n> line C\n> indicated the version was 1.3.7.3.3. However, when I start sage I get:\n>\n> --------------------------------------------------------\n> | SAGE Version 1.3.7.3, Build Date: 2006-09-21-0448    |\n> | Distributed under the GNU General Public License V2. |\n> --------------------------------------------------------\n>\n> sage: version()\n>  'SAGE Version 1.3.7.3, Build Date: 2006-09-21-0448'\n>\n> This is different than what\n> /home/wdj/sagefiles/sage-1.2.0/devel/sage-main/sage/version.py\n> indicates: version='1.3.7.3.3'; date='2006-09-21'\n>\n> This seems funny to me. Is there a mistake here?\n\nThe banner is not the output of version().   The banner is the output\nof <SAGE_ROOT>/local/bin/sage-banner, which gets updated when you\nupgrade sage_scripts.    In contrast, the version() function outputs\nthe version number of the SAGE library, i.e., what is in version.py,\nwhich you just upgraded (correctly).    I should make the output\nof version() much different.\n\nWilliam\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/80\n\n",
    "created_at": "2006-09-23T15:50:59Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Clarify: version.py versus sage-version",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/80",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
On Sat, 23 Sep 2006 07:55:20 -0700, David Joyner <wdjoyner@gmail.com> wrote:

>> To try it out in the latest SAGE (1.3.7.3.3 and not earlier!),
>> type (from <SAGE_ROOT>/deve/sage)
>>
>> sage -hg pull http://sage.math.washington.edu/sage/hg/sage-main
>> sage -hg merge    # if necessary
>> sage -hg update
>>
>>
>
> wdj@wooster:~/sagefiles/sage-1.2.0/devel/sage$ ../../sage -hg update
> remote changed .hgtags which local deleted
> (k)eep or (d)elete?   k
> remote changed export which local deleted
> (k)eep or (d)elete? k
> merging sage/version.py
>
> Now kdiff3 (which I mistook for a browser window) opens with some text
> highlighted
> in yellow and red. The bar at the bottom says "Number of remaining
> unsolved conflicts: 1".
> The conflict appears to be in version.py. I clicked on "merge" on the
> top bar and then
> picked "line 1 from C", which was one of the options in the pop-down  
> menu,
> then then clicked on "save" and quit. If memory serves (which is iffy),
> line C
> indicated the version was 1.3.7.3.3. However, when I start sage I get:
>
> --------------------------------------------------------
> | SAGE Version 1.3.7.3, Build Date: 2006-09-21-0448    |
> | Distributed under the GNU General Public License V2. |
> --------------------------------------------------------
>
> sage: version()
>  'SAGE Version 1.3.7.3, Build Date: 2006-09-21-0448'
>
> This is different than what
> /home/wdj/sagefiles/sage-1.2.0/devel/sage-main/sage/version.py
> indicates: version='1.3.7.3.3'; date='2006-09-21'
>
> This seems funny to me. Is there a mistake here?

The banner is not the output of version().   The banner is the output
of <SAGE_ROOT>/local/bin/sage-banner, which gets updated when you
upgrade sage_scripts.    In contrast, the version() function outputs
the version number of the SAGE library, i.e., what is in version.py,
which you just upgraded (correctly).    I should make the output
of version() much different.

William
```

Issue created by migration from https://trac.sagemath.org/ticket/80





---

archive/issue_comments_000396.json:
```json
{
    "body": "Changing component from algebraic geometry to user interface.",
    "created_at": "2006-09-23T15:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/80#issuecomment-396",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebraic geometry to user interface.



---

archive/issue_comments_000397.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2006-09-23T15:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/80#issuecomment-397",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to minor.



---

archive/issue_comments_000398.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2006-09-23T15:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/80#issuecomment-398",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_000399.json:
```json
{
    "body": "```\npaul-olivier-dehayes-computer:~ pdehaye$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8, Release Date: 2007-08-12                         |\n| Type notebook() for the GUI, and license() for information.        |\nsage: version()\n'SAGE Version 2.8.1, Release Date: 2007-08-18'\nsage: \n```",
    "created_at": "2007-08-21T16:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/80#issuecomment-399",
    "user": "https://trac.sagemath.org/admin/accounts/users/pdehaye"
}
```

```
paul-olivier-dehayes-computer:~ pdehaye$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8, Release Date: 2007-08-12                         |
| Type notebook() for the GUI, and license() for information.        |
sage: version()
'SAGE Version 2.8.1, Release Date: 2007-08-18'
sage: 
```



---

archive/issue_events_000172.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-08-24T22:39:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/80#event-172"
}
```



---

archive/issue_comments_000400.json:
```json
{
    "body": "I am not sure if there is anything to fix here. Opinions?",
    "created_at": "2008-03-16T08:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/80#issuecomment-400",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am not sure if there is anything to fix here. Opinions?



---

archive/issue_comments_000401.json:
```json
{
    "body": "> I am not sure if there is anything to fix here. Opinions?\n\n\nYes, we need to \"make the output of version() much different.\"",
    "created_at": "2008-03-16T09:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/80#issuecomment-401",
    "user": "https://github.com/williamstein"
}
```

> I am not sure if there is anything to fix here. Opinions?


Yes, we need to "make the output of version() much different."



---

archive/issue_comments_000402.json:
```json
{
    "body": "Replying to [comment:5 was]:\n> Yes, we need to \"make the output of version() much different.\"\n\n\nOk, I would prefer then that version returns a dictionary with major, minor and tiny version numbers. That would make it quite easy to write a set of functions that could check for a minimum version at startup for example.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-12T13:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/80#issuecomment-402",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 was]:
> Yes, we need to "make the output of version() much different."


Ok, I would prefer then that version returns a dictionary with major, minor and tiny version numbers. That would make it quite easy to write a set of functions that could check for a minimum version at startup for example.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_000403.json:
```json
{
    "body": "See #2039, to which I've just added a patch. Does this do what you want?\n\n  John",
    "created_at": "2008-10-31T19:12:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/80#issuecomment-403",
    "user": "https://github.com/jhpalmieri"
}
```

See #2039, to which I've just added a patch. Does this do what you want?

  John



---

archive/issue_comments_000404.json:
```json
{
    "body": "Replying to [comment:5 was]:\n> > I am not sure if there is anything to fix here. Opinions?\n\n> \n> Yes, we need to \"make the output of version() much different.\"\n\n\nWhy? I don't see any reason to do so. I re-read the above email and still do not understand how making version() any different than the output from sage-banner would accomplish anything?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T19:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/80#issuecomment-404",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 was]:
> > I am not sure if there is anything to fix here. Opinions?

> 
> Yes, we need to "make the output of version() much different."


Why? I don't see any reason to do so. I re-read the above email and still do not understand how making version() any different than the output from sage-banner would accomplish anything?

Cheers,

Michael



---

archive/issue_comments_000405.json:
```json
{
    "body": "In fact: banner_text() which is used for sage-banner uses version to construct the string printed at Sage startup:\n\n```\n s += \"\\n| %-66s |\\n\"%version() \n```\n\nI am very tempted to make this ticket invalid unless someone can actually come up with a concrete suggestion what to do and why to do it.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T19:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/80#issuecomment-405",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

In fact: banner_text() which is used for sage-banner uses version to construct the string printed at Sage startup:

```
 s += "\n| %-66s |\n"%version() 
```

I am very tempted to make this ticket invalid unless someone can actually come up with a concrete suggestion what to do and why to do it.

Cheers,

Michael



---

archive/issue_comments_000406.json:
```json
{
    "body": "I'm not sure I understand.  SAGE_ROOT/local/bin/sage-banner seems to be responsible for the startup message.  Is this file autogenerated from banner_text() somehow?  If I change banner_text(), the startup message is not affected.\n\n(However, I still don't quite see the point of this ticket, and would have no objections to invalidating it.)\n\n  John",
    "created_at": "2008-10-31T20:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/80#issuecomment-406",
    "user": "https://github.com/jhpalmieri"
}
```

I'm not sure I understand.  SAGE_ROOT/local/bin/sage-banner seems to be responsible for the startup message.  Is this file autogenerated from banner_text() somehow?  If I change banner_text(), the startup message is not affected.

(However, I still don't quite see the point of this ticket, and would have no objections to invalidating it.)

  John



---

archive/issue_comments_000407.json:
```json
{
    "body": "Replying to [comment:10 jhpalmieri]:\n> I'm not sure I understand.  SAGE_ROOT/local/bin/sage-banner seems to be responsible for the startup message.  Is this file autogenerated from banner_text() somehow?  \n\n\nYes, in $SAGE_ROOT/local/bin/sage-sdist\n\n> If I change banner_text(), the startup message is not affected.\n\n\nIt is only changed once $SAGE_ROOT/local/bin/sage-sdist is run.\n\n> (However, I still don't quite see the point of this ticket, and would have no objections to invalidating it.)\n\n\n+1 from me, but that wasn't in doubt :)\n \n>   John\n\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T20:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/80#issuecomment-407",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:10 jhpalmieri]:
> I'm not sure I understand.  SAGE_ROOT/local/bin/sage-banner seems to be responsible for the startup message.  Is this file autogenerated from banner_text() somehow?  


Yes, in $SAGE_ROOT/local/bin/sage-sdist

> If I change banner_text(), the startup message is not affected.


It is only changed once $SAGE_ROOT/local/bin/sage-sdist is run.

> (However, I still don't quite see the point of this ticket, and would have no objections to invalidating it.)


+1 from me, but that wasn't in doubt :)
 
>   John


Cheers,

Michael



---

archive/issue_events_000173.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T21:08:00Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/80#event-173"
}
```



---

archive/issue_events_000174.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T21:08:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/80#event-174"
}
```



---

archive/issue_events_000175.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T21:08:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/80#event-175"
}
```



---

archive/issue_comments_000408.json:
```json
{
    "body": "William agreed via Google chat, so this is invalidated.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T21:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/80#issuecomment-408",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

William agreed via Google chat, so this is invalidated.

Cheers,

Michael



---

archive/issue_comments_000409.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-10-31T21:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/80",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/80#issuecomment-409",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid
