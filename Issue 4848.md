# Issue 4848: [with patch, needs review] Remove deadwood: sage/schemes/elliptic_curves/heegner.py

archive/issues_004848.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  wstein\n\nThe file sage/schemes/elliptic_curves/heegner.py is mainly some comments and a bunch of Magma code. I don't see anything useful in there, so let's get rid of it.\n\nLong doctests pass with the file and its copies removed from build.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4848\n\n",
    "created_at": "2008-12-21T16:19:30Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Remove deadwood: sage/schemes/elliptic_curves/heegner.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4848",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  wstein

The file sage/schemes/elliptic_curves/heegner.py is mainly some comments and a bunch of Magma code. I don't see anything useful in there, so let's get rid of it.

Long doctests pass with the file and its copies removed from build.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4848





---

archive/issue_comments_036760.json:
```json
{
    "body": "Attachment\n\nThe file is also from 2005 and hasn't been touched for ages:\n\n```\nchangeset:   1097:e9c1649fcc14\nuser:        wstein@gmail.com\ndate:        Fri Sep 01 02:31:25 2006 +0000\nsummary:     [project @ wstein@ucsd.edu --> wstein@gmail.com (hundreds of changes)]\n\nchangeset:   0:039f6310c6fe\nuser:        tornaria@math.utexas.edu\ndate:        Sat Feb 11 01:13:08 2006 +0000\nsummary:     [project @ original sage-0.10.12]\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-12-21T16:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4848#issuecomment-36760",
    "user": "mabshoff"
}
```

Attachment

The file is also from 2005 and hasn't been touched for ages:

```
changeset:   1097:e9c1649fcc14
user:        wstein@gmail.com
date:        Fri Sep 01 02:31:25 2006 +0000
summary:     [project @ wstein@ucsd.edu --> wstein@gmail.com (hundreds of changes)]

changeset:   0:039f6310c6fe
user:        tornaria@math.utexas.edu
date:        Sat Feb 11 01:13:08 2006 +0000
summary:     [project @ original sage-0.10.12]
```


Cheers,

Michael



---

archive/issue_comments_036761.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-21T16:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4848#issuecomment-36761",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036762.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2008-12-21T16:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4848#issuecomment-36762",
    "user": "mhampton"
}
```

Changing priority from major to minor.



---

archive/issue_comments_036763.json:
```json
{
    "body": "This is all magma code.  If it does something useful then it should be moved upstream or perhaps put in an optional spkg.  Since its William Stein's code perhaps he could bless its removal...",
    "created_at": "2008-12-21T16:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4848#issuecomment-36763",
    "user": "mhampton"
}
```

This is all magma code.  If it does something useful then it should be moved upstream or perhaps put in an optional spkg.  Since its William Stein's code perhaps he could bless its removal...



---

archive/issue_comments_036764.json:
```json
{
    "body": "What should happen is that there should be a new *enhancement* ticket that is called \"add functionality for computing Heegner points to Sage\".   Then the file heegner.py should be attached to that ticket, since to do that ticket, one might want to port some of what's in there to Sage.   That said, it's not so simple, since better algorithms for computing Heegner points were found after that code was written. \n\nSo I am OK with this ticket if and only if the above enhancement ticket is created.",
    "created_at": "2008-12-21T17:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4848#issuecomment-36764",
    "user": "was"
}
```

What should happen is that there should be a new *enhancement* ticket that is called "add functionality for computing Heegner points to Sage".   Then the file heegner.py should be attached to that ticket, since to do that ticket, one might want to port some of what's in there to Sage.   That said, it's not so simple, since better algorithms for computing Heegner points were found after that code was written. 

So I am OK with this ticket if and only if the above enhancement ticket is created.



---

archive/issue_comments_036765.json:
```json
{
    "body": "Replying to [comment:3 was]:\n\n> So I am OK with this ticket if and only if the above enhancement ticket is created. \n\nSee #4849.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-21T22:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4848#issuecomment-36765",
    "user": "mabshoff"
}
```

Replying to [comment:3 was]:

> So I am OK with this ticket if and only if the above enhancement ticket is created. 

See #4849.

Cheers,

Michael



---

archive/issue_comments_036766.json:
```json
{
    "body": "Merged in Sage 3.2.3.alpha0",
    "created_at": "2008-12-21T22:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4848#issuecomment-36766",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.3.alpha0



---

archive/issue_comments_036767.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-21T22:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4848#issuecomment-36767",
    "user": "mabshoff"
}
```

Resolution: fixed
