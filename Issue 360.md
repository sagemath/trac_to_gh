# Issue 360: Port Cremona's implementation of elliptic curve height bounds to SAGE

archive/issues_000360.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @JohnCremona @pjbruin\n\nJohn Cremona has implemented a wide range of height bounds for elliptic curves in \nthis magma program:\n\n  http://www.maths.nott.ac.uk/personal/jec/ftp/progs/magma/nfhtbound.m\n\n(see also attached file).  Upon my request he GPL'd this program.  Thus we can\nlegally port it line-by-line to SAGE.  \n\nwilliam\n\nIssue created by migration from https://trac.sagemath.org/ticket/360\n\n",
    "created_at": "2007-04-27T16:15:33Z",
    "labels": [
        "number theory",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Port Cremona's implementation of elliptic curve height bounds to SAGE",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/360",
    "user": "@williamstein"
}
```
Assignee: @williamstein

CC:  @JohnCremona @pjbruin

John Cremona has implemented a wide range of height bounds for elliptic curves in 
this magma program:

  http://www.maths.nott.ac.uk/personal/jec/ftp/progs/magma/nfhtbound.m

(see also attached file).  Upon my request he GPL'd this program.  Thus we can
legally port it line-by-line to SAGE.  

william

Issue created by migration from https://trac.sagemath.org/ticket/360





---

archive/issue_comments_001734.json:
```json
{
    "body": "Attachment [nfhtbound.m](tarball://root/attachments/some-uuid/ticket360/nfhtbound.m) by mabshoff created at 2007-09-10 02:20:27",
    "created_at": "2007-09-10T02:20:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1734",
    "user": "mabshoff"
}
```

Attachment [nfhtbound.m](tarball://root/attachments/some-uuid/ticket360/nfhtbound.m) by mabshoff created at 2007-09-10 02:20:27



---

archive/issue_comments_001735.json:
```json
{
    "body": "Changing assignee from @williamstein to @roed314.",
    "created_at": "2007-10-13T00:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1735",
    "user": "@roed314"
}
```

Changing assignee from @williamstein to @roed314.



---

archive/issue_comments_001736.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-13T00:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1736",
    "user": "@roed314"
}
```

Changing status from new to assigned.



---

archive/issue_comments_001737.json:
```json
{
    "body": "Has there been any progress here? What is the status of this in general? Now that John is a full Sage developer wouldn't it be something he would do the best job at?\n\nCheers,\n\nMichael",
    "created_at": "2008-03-16T09:05:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1737",
    "user": "mabshoff"
}
```

Has there been any progress here? What is the status of this in general? Now that John is a full Sage developer wouldn't it be something he would do the best job at?

Cheers,

Michael



---

archive/issue_comments_001738.json:
```json
{
    "body": "Hi John,\n\nI am curious how much of this code has found its way into Sage and it this ticket can be closed. I did add you to the CC field.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T04:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1738",
    "user": "mabshoff"
}
```

Hi John,

I am curious how much of this code has found its way into Sage and it this ticket can be closed. I did add you to the CC field.

Cheers,

Michael



---

archive/issue_comments_001739.json:
```json
{
    "body": "Replying to [comment:4 mabshoff]:\n> Hi John,\n> \n> I am curious how much of this code has found its way into Sage and it this ticket can be closed. I did add you to the CC field.\n> \n\nNone of this is in Sage at all yet.  Over Q the functionality is there (provided by eclib) but not over number fields.\n\nIt's something I could do, yes.  So please keep the ticket open.\n\n> Cheers,\n> \n> Michael",
    "created_at": "2008-04-07T08:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1739",
    "user": "@JohnCremona"
}
```

Replying to [comment:4 mabshoff]:
> Hi John,
> 
> I am curious how much of this code has found its way into Sage and it this ticket can be closed. I did add you to the CC field.
> 

None of this is in Sage at all yet.  Over Q the functionality is there (provided by eclib) but not over number fields.

It's something I could do, yes.  So please keep the ticket open.

> Cheers,
> 
> Michael



---

archive/issue_comments_001740.json:
```json
{
    "body": "Replying to [comment:5 cremona]:\n> Replying to [comment:4 mabshoff]:\n> > Hi John,\n\nHi John,\n\n> > \n> > I am curious how much of this code has found its way into Sage and it this ticket can be closed. I did add you to the CC field.\n> > \n> \n> None of this is in Sage at all yet.  Over Q the functionality is there (provided by eclib) but not over number fields.\n> \n> It's something I could do, yes.  So please keep the ticket open.\n\nSure. I just wanted to make sure that the ticket hadn't already been solved. If you plan to work on it you might want to take ownership of this ticket since roed is rather busy these days.\n \n> > Cheers,\n> > \n> > Michael\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T14:00:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1740",
    "user": "mabshoff"
}
```

Replying to [comment:5 cremona]:
> Replying to [comment:4 mabshoff]:
> > Hi John,

Hi John,

> > 
> > I am curious how much of this code has found its way into Sage and it this ticket can be closed. I did add you to the CC field.
> > 
> 
> None of this is in Sage at all yet.  Over Q the functionality is there (provided by eclib) but not over number fields.
> 
> It's something I could do, yes.  So please keep the ticket open.

Sure. I just wanted to make sure that the ticket hadn't already been solved. If you plan to work on it you might want to take ownership of this ticket since roed is rather busy these days.
 
> > Cheers,
> > 
> > Michael

Cheers,

Michael



---

archive/issue_comments_001741.json:
```json
{
    "body": "By the way, before this (=height bounds) is done we should also implement heights on elliptic curves over number fields.  For this reason I have changed the ticket's summary description as well as taking ownership.",
    "created_at": "2008-04-07T19:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1741",
    "user": "@JohnCremona"
}
```

By the way, before this (=height bounds) is done we should also implement heights on elliptic curves over number fields.  For this reason I have changed the ticket's summary description as well as taking ownership.



---

archive/issue_comments_001742.json:
```json
{
    "body": "Changing assignee from @roed314 to @JohnCremona.",
    "created_at": "2008-04-07T19:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1742",
    "user": "@JohnCremona"
}
```

Changing assignee from @roed314 to @JohnCremona.



---

archive/issue_comments_001743.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-04-07T19:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1743",
    "user": "@JohnCremona"
}
```

Changing status from assigned to new.



---

archive/issue_comments_001744.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2009-07-20T19:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1744",
    "user": "@loefflerd"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_001745.json:
```json
{
    "body": "Assigned to new \"elliptic curves\" component.",
    "created_at": "2009-07-20T19:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1745",
    "user": "@loefflerd"
}
```

Assigned to new "elliptic curves" component.



---

archive/issue_comments_001746.json:
```json
{
    "body": "Implementation of heights in done in #8496 so should be available from 4.3.4.\n\nHence I changed the ticket's title back so that it only refers to height bounds.",
    "created_at": "2010-03-15T20:35:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1746",
    "user": "@JohnCremona"
}
```

Implementation of heights in done in #8496 so should be available from 4.3.4.

Hence I changed the ticket's title back so that it only refers to height bounds.



---

archive/issue_comments_001747.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2018-04-04T18:12:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1747",
    "user": "@fchapoton"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_001748.json:
```json
{
    "body": "Is this still pertinent in any way ?",
    "created_at": "2018-04-04T18:12:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1748",
    "user": "@fchapoton"
}
```

Is this still pertinent in any way ?



---

archive/issue_comments_001749.json:
```json
{
    "body": "It is all now implemented, by Robert Bradshaw with some input from me: see sage/schemes/elliptic_curves/height.py.  So this ticket is redundant.",
    "created_at": "2018-04-04T18:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1749",
    "user": "@JohnCremona"
}
```

It is all now implemented, by Robert Bradshaw with some input from me: see sage/schemes/elliptic_curves/height.py.  So this ticket is redundant.



---

archive/issue_comments_001750.json:
```json
{
    "body": "thanks",
    "created_at": "2018-04-04T18:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1750",
    "user": "@fchapoton"
}
```

thanks



---

archive/issue_comments_001751.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2018-04-04T18:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1751",
    "user": "@fchapoton"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_001752.json:
```json
{
    "body": "closing positively reviewed duplicates",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1752",
    "user": "@videlec"
}
```

closing positively reviewed duplicates



---

archive/issue_comments_001753.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/360",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/360#issuecomment-1753",
    "user": "@videlec"
}
```

Resolution: wontfix
