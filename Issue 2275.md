# Issue 2275: [with patch, needs review] get sloane_functions.py to 100% coverage

archive/issues_002275.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2275\n\n",
    "created_at": "2008-02-23T04:44:31Z",
    "labels": [
        "component: combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch, needs review] get sloane_functions.py to 100% coverage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2275",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @mwhansen

CC:  sage-combinat



Issue created by migration from https://trac.sagemath.org/ticket/2275





---

archive/issue_comments_015059.json:
```json
{
    "body": "Attachment [2275.patch.gz](tarball://root/attachments/some-uuid/ticket2275/2275.patch.gz) by @mwhansen created at 2008-02-23 05:21:43\n\nHere is a link:  http://sage.math.washington.edu/home/mhansen/2275.patch",
    "created_at": "2008-02-23T05:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2275#issuecomment-15059",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2275.patch.gz](tarball://root/attachments/some-uuid/ticket2275/2275.patch.gz) by @mwhansen created at 2008-02-23 05:21:43

Here is a link:  http://sage.math.washington.edu/home/mhansen/2275.patch



---

archive/issue_comments_015060.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-23T05:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2275#issuecomment-15060",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015061.json:
```json
{
    "body": "I don't think this is a good idea:\n\n```\nAll sloane_functions have extensive examples, but from design they are\nplaced just after the class declaration.\nIt feels stupid to have \"internal\" functions\nstarting with '__' or '_' documented with EXAMPLES!\n\nLet us think at the effect on the reference manual.\nI don't think it is a good idea to have internal functions like\n__init, _repr and other \"hidden\" fuctions documented with examples\nfiguring in the Reference Manual.\n\nIf we want users of the OEIS to use Sage, we have to provide them with\nadequate examples. Maybe raising the doctest coverage with 2% looks good\nbut it isn't in this case.\n\nAdding some sloane-functions I was following the 'template'. So there\nis, maybe, something wrong with the overall design.\n\n\nJaap\n\n\n\n```\n",
    "created_at": "2008-02-24T19:12:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2275#issuecomment-15061",
    "user": "https://github.com/jaapspies"
}
```

I don't think this is a good idea:

```
All sloane_functions have extensive examples, but from design they are
placed just after the class declaration.
It feels stupid to have "internal" functions
starting with '__' or '_' documented with EXAMPLES!

Let us think at the effect on the reference manual.
I don't think it is a good idea to have internal functions like
__init, _repr and other "hidden" fuctions documented with examples
figuring in the Reference Manual.

If we want users of the OEIS to use Sage, we have to provide them with
adequate examples. Maybe raising the doctest coverage with 2% looks good
but it isn't in this case.

Adding some sloane-functions I was following the 'template'. So there
is, maybe, something wrong with the overall design.


Jaap



```




---

archive/issue_comments_015062.json:
```json
{
    "body": "I disagree with Jaap here.  I think getting coverage to 100% is a good idea.",
    "created_at": "2008-02-24T20:35:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2275#issuecomment-15062",
    "user": "https://github.com/williamstein"
}
```

I disagree with Jaap here.  I think getting coverage to 100% is a good idea.



---

archive/issue_comments_015063.json:
```json
{
    "body": "Replying to [comment:3 was]:\n> I disagree with Jaap here.  I think getting coverage to 100% is a good idea. \n\nGenerally spoken yes, but in this case I have my doubts.\n\nJaap",
    "created_at": "2008-02-24T20:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2275#issuecomment-15063",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:3 was]:
> I disagree with Jaap here.  I think getting coverage to 100% is a good idea. 

Generally spoken yes, but in this case I have my doubts.

Jaap



---

archive/issue_comments_015064.json:
```json
{
    "body": "Looks superb to me.",
    "created_at": "2008-03-03T05:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2275#issuecomment-15064",
    "user": "https://github.com/williamstein"
}
```

Looks superb to me.



---

archive/issue_events_002446.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-03T12:33:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2275",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2275#event-2446"
}
```



---

archive/issue_comments_015065.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc1",
    "created_at": "2008-03-03T12:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2275#issuecomment-15065",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc1



---

archive/issue_comments_015066.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-03T12:33:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2275#issuecomment-15066",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
