# Issue 5138: implement computing manin constants of elliptic curves

archive/issues_005138.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5138\n\n",
    "created_at": "2009-01-30T15:59:11Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "implement computing manin constants of elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5138",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/5138





---

archive/issue_comments_039211.json:
```json
{
    "body": "Logic looks ok, but patch does not apply to 3.3.alpha2 cleanly.  Does it need alpha3?  If so a proper review will have to wait (at least until I get home).\n\nHave you remembered 990h where the optimal curve is not #1?",
    "created_at": "2009-01-30T17:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5138#issuecomment-39211",
    "user": "https://github.com/JohnCremona"
}
```

Logic looks ok, but patch does not apply to 3.3.alpha2 cleanly.  Does it need alpha3?  If so a proper review will have to wait (at least until I get home).

Have you remembered 990h where the optimal curve is not #1?



---

archive/issue_comments_039212.json:
```json
{
    "body": "> Have you remembered 990h where the optimal curve is not #1? \n\nNo, I forgot about that.  Is that the only example?  I will add a new command optimal_curve() that finds the optimal curve using your database and includes a workaround for 990h (and any other examples). \n\n> Logic looks ok, but patch does not apply to 3.3.alpha2 cleanly. \n> Does it need alpha3? If so a proper review will have to wait \n>(at least until I get home). \n\nI did it against alpha0.  I'll rebase it for alpha3.",
    "created_at": "2009-01-30T17:26:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5138#issuecomment-39212",
    "user": "https://github.com/williamstein"
}
```

> Have you remembered 990h where the optimal curve is not #1? 

No, I forgot about that.  Is that the only example?  I will add a new command optimal_curve() that finds the optimal curve using your database and includes a workaround for 990h (and any other examples). 

> Logic looks ok, but patch does not apply to 3.3.alpha2 cleanly. 
> Does it need alpha3? If so a proper review will have to wait 
>(at least until I get home). 

I did it against alpha0.  I'll rebase it for alpha3.



---

archive/issue_comments_039213.json:
```json
{
    "body": "Replying to [comment:3 was]:\n> > Have you remembered 990h where the optimal curve is not #1? \n> \n> No, I forgot about that.  Is that the only example?  I will add a new command optimal_curve() that finds the optimal curve using your database and includes a workaround for 990h (and any other examples). \n\nThat's the only example, luckily.\n\n> \n> > Logic looks ok, but patch does not apply to 3.3.alpha2 cleanly. \n> > Does it need alpha3? If so a proper review will have to wait \n> >(at least until I get home). \n> \n> I did it against alpha0.  I'll rebase it for alpha3. \n\nOK, I'll look at it again over the weekend.",
    "created_at": "2009-01-30T17:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5138#issuecomment-39213",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:3 was]:
> > Have you remembered 990h where the optimal curve is not #1? 
> 
> No, I forgot about that.  Is that the only example?  I will add a new command optimal_curve() that finds the optimal curve using your database and includes a workaround for 990h (and any other examples). 

That's the only example, luckily.

> 
> > Logic looks ok, but patch does not apply to 3.3.alpha2 cleanly. 
> > Does it need alpha3? If so a proper review will have to wait 
> >(at least until I get home). 
> 
> I did it against alpha0.  I'll rebase it for alpha3. 

OK, I'll look at it again over the weekend.



---

archive/issue_comments_039214.json:
```json
{
    "body": "Thanks for pointing out the 990h issue which I had forgot.  I found a bug related to that (but not this ticket) and posted a fix at #5149.",
    "created_at": "2009-02-01T08:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5138#issuecomment-39214",
    "user": "https://github.com/williamstein"
}
```

Thanks for pointing out the 990h issue which I had forgot.  I found a bug related to that (but not this ticket) and posted a fix at #5149.



---

archive/issue_comments_039215.json:
```json
{
    "body": "Attachment [trac_5138.patch](tarball://root/attachments/some-uuid/ticket5138/trac_5138.patch) by @williamstein created at 2009-02-01 09:24:43",
    "created_at": "2009-02-01T09:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5138#issuecomment-39215",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5138.patch](tarball://root/attachments/some-uuid/ticket5138/trac_5138.patch) by @williamstein created at 2009-02-01 09:24:43



---

archive/issue_comments_039216.json:
```json
{
    "body": "The attached patch implements computation of the Manin constant with some caveats that are clearly spelled out in the docstrings.  Also, it fixes a serious bug in an internal function (_multiple_of_degree_of_isogeny_to_optimal_curve, which was just nonsense before).",
    "created_at": "2009-02-01T09:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5138#issuecomment-39216",
    "user": "https://github.com/williamstein"
}
```

The attached patch implements computation of the Manin constant with some caveats that are clearly spelled out in the docstrings.  Also, it fixes a serious bug in an internal function (_multiple_of_degree_of_isogeny_to_optimal_curve, which was just nonsense before).



---

archive/issue_comments_039217.json:
```json
{
    "body": "Patch applies cleanly to 3.3.alpha2 + #5139.  Tests pass BUT:\n\n```\nsage: Ellsage: EllipticCurve('990a1').optimal_curve()\n---------------------------------------------------------------------------\nRuntimeError          \n```\n\nsince on line 3099 you set the number to 3 when N=990 for all isogeny classes, not just class h.\n\nSomewhere in the database code I think we have utilities for splitting the label into its 3 components, by the way, which might be more transparent than (e.g.) stripping off the last character to get the number.",
    "created_at": "2009-02-01T11:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5138#issuecomment-39217",
    "user": "https://github.com/JohnCremona"
}
```

Patch applies cleanly to 3.3.alpha2 + #5139.  Tests pass BUT:

```
sage: Ellsage: EllipticCurve('990a1').optimal_curve()
---------------------------------------------------------------------------
RuntimeError          
```

since on line 3099 you set the number to 3 when N=990 for all isogeny classes, not just class h.

Somewhere in the database code I think we have utilities for splitting the label into its 3 components, by the way, which might be more transparent than (e.g.) stripping off the last character to get the number.



---

archive/issue_comments_039218.json:
```json
{
    "body": "Thanks John -- excellent catch.  And, I changed the code to use the code from database/cremona, as you suggested.",
    "created_at": "2009-02-01T21:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5138#issuecomment-39218",
    "user": "https://github.com/williamstein"
}
```

Thanks John -- excellent catch.  And, I changed the code to use the code from database/cremona, as you suggested.



---

archive/issue_comments_039219.json:
```json
{
    "body": "Attachment [trac_5138_part2.patch](tarball://root/attachments/some-uuid/ticket5138/trac_5138_part2.patch) by @JohnCremona created at 2009-02-01 22:12:40\n\nLooks good!",
    "created_at": "2009-02-01T22:12:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5138#issuecomment-39219",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_5138_part2.patch](tarball://root/attachments/some-uuid/ticket5138/trac_5138_part2.patch) by @JohnCremona created at 2009-02-01 22:12:40

Looks good!



---

archive/issue_comments_039220.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-02T02:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5138#issuecomment-39220",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039221.json:
```json
{
    "body": "Merged both patches in Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T02:46:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5138",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5138#issuecomment-39221",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.3.alpha4.

Cheers,

Michael



---

archive/issue_events_011906.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-02T02:46:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5138",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5138#event-11906"
}
```
