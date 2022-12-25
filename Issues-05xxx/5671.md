# Issue 5671: Create a documented minimal useful Cython wrapper for miniSAT along with an spkg

archive/issues_005671.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  fichtejo\n\nSage lacks a SAT solver.  First step, lets make a spkg and wrap it.  In the future, we should add boolean functions, etc., but one step at a time.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5671\n\n",
    "closed_at": "2014-03-19T04:41:52Z",
    "created_at": "2009-04-02T22:10:41Z",
    "labels": [
        "component: packages: standard",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Create a documented minimal useful Cython wrapper for miniSAT along with an spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5671",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: boothby

CC:  fichtejo

Sage lacks a SAT solver.  First step, lets make a spkg and wrap it.  In the future, we should add boolean functions, etc., but one step at a time.

Issue created by migration from https://trac.sagemath.org/ticket/5671





---

archive/issue_comments_044273.json:
```json
{
    "body": "Attachment [trac_5671-part1.patch](tarball://root/attachments/some-uuid/ticket5671/trac_5671-part1.patch) by boothby created at 2009-04-02 22:28:11",
    "created_at": "2009-04-02T22:28:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44273",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [trac_5671-part1.patch](tarball://root/attachments/some-uuid/ticket5671/trac_5671-part1.patch) by boothby created at 2009-04-02 22:28:11



---

archive/issue_events_013335.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-02T22:42:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5671#event-13335"
}
```



---

archive/issue_comments_044274.json:
```json
{
    "body": "Might I point out that this is a dupe of #418.\n\nYou also \n\n* should assign a milestone when you open a ticket\n* not attach spkgs to tickets, but post a link. Given that this one is 77kb it might be a borderline case.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-02T22:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44274",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Might I point out that this is a dupe of #418.

You also 

* should assign a milestone when you open a ticket
* not attach spkgs to tickets, but post a link. Given that this one is 77kb it might be a borderline case.

Cheers,

Michael



---

archive/issue_comments_044275.json:
```json
{
    "body": "Attachment [trac_5671-part2.patch](tarball://root/attachments/some-uuid/ticket5671/trac_5671-part2.patch) by boothby created at 2009-04-02 22:55:32",
    "created_at": "2009-04-02T22:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44275",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [trac_5671-part2.patch](tarball://root/attachments/some-uuid/ticket5671/trac_5671-part2.patch) by boothby created at 2009-04-02 22:55:32



---

archive/issue_comments_044276.json:
```json
{
    "body": "Attachment [trac_5671-part3.patch](tarball://root/attachments/some-uuid/ticket5671/trac_5671-part3.patch) by @williamstein created at 2009-04-02 23:11:34\n\nWith just the posted code to this point:\n\n```\nsage: S = minisat.Solver(verbosity=2)\nsage: S.new_var()\n0\nsage: S.new_var()\n1\nsage: S.new_var()\n2\nsage: S.new_var()\n3\nsage: S.add_clause([1])\npushing lit.p =  Literal 1\nsage: S.add_clause([2])\npushing lit.p =  Literal 2\nsage: S.solve()\n============================[ Search Statistics ]==============================\n===============================================================================\n===============================================================================\nVerified 0 original clauses.\nTrue\n```",
    "created_at": "2009-04-02T23:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44276",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5671-part3.patch](tarball://root/attachments/some-uuid/ticket5671/trac_5671-part3.patch) by @williamstein created at 2009-04-02 23:11:34

With just the posted code to this point:

```
sage: S = minisat.Solver(verbosity=2)
sage: S.new_var()
0
sage: S.new_var()
1
sage: S.new_var()
2
sage: S.new_var()
3
sage: S.add_clause([1])
pushing lit.p =  Literal 1
sage: S.add_clause([2])
pushing lit.p =  Literal 2
sage: S.solve()
============================[ Search Statistics ]==============================
===============================================================================
===============================================================================
Verified 0 original clauses.
True
```



---

archive/issue_comments_044277.json:
```json
{
    "body": "This\n\n   http://planete.inrialpes.fr/~soos/CryptoMiniSat/index.html\n\nmight be relevant. It is an enhanced MiniSat with:\n\n* Natively handled XOR functions\n* Statistics generation\n* Search randomization\n* Detailed solving process visualization\n* Clause grouping and group naming\n* Variable naming\n* Debug mode\n* Code cleanup",
    "created_at": "2009-09-02T10:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44277",
    "user": "https://github.com/malb"
}
```

This

   http://planete.inrialpes.fr/~soos/CryptoMiniSat/index.html

might be relevant. It is an enhanced MiniSat with:

* Natively handled XOR functions
* Statistics generation
* Search randomization
* Detailed solving process visualization
* Clause grouping and group naming
* Variable naming
* Debug mode
* Code cleanup



---

archive/issue_comments_044278.json:
```json
{
    "body": "Replying to [comment:5 malb]:\n> This\n> \n>    http://planete.inrialpes.fr/~soos/CryptoMiniSat/index.html\n> \n> might be relevant. It is an enhanced MiniSat with:\n> \n> * Natively handled XOR functions\n> * Statistics generation\n> * Search randomization\n> * Detailed solving process visualization\n> * Clause grouping and group naming\n> * Variable naming\n> * Debug mode\n> * Code cleanup\n\n\nGiven this and recent developments at #418, perhaps this is a dupe?",
    "created_at": "2012-06-04T19:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44278",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:5 malb]:
> This
> 
>    http://planete.inrialpes.fr/~soos/CryptoMiniSat/index.html
> 
> might be relevant. It is an enhanced MiniSat with:
> 
> * Natively handled XOR functions
> * Statistics generation
> * Search randomization
> * Detailed solving process visualization
> * Clause grouping and group naming
> * Variable naming
> * Debug mode
> * Code cleanup


Given this and recent developments at #418, perhaps this is a dupe?



---

archive/issue_comments_044279.json:
```json
{
    "body": "I vote for declaring this ticket a dupe.",
    "created_at": "2012-06-15T16:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44279",
    "user": "https://github.com/malb"
}
```

I vote for declaring this ticket a dupe.



---

archive/issue_events_013336.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5671#event-13336"
}
```



---

archive/issue_events_013337.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5671#event-13337"
}
```



---

archive/issue_events_013338.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5671#event-13338"
}
```



---

archive/issue_events_013339.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5671#event-13339"
}
```



---

archive/issue_comments_044280.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-03-14T15:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44280",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_events_013340.json:
```json
{
    "actor": "https://github.com/mezzarobba",
    "created_at": "2014-03-14T15:29:41Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5671#event-13340"
}
```



---

archive/issue_events_013341.json:
```json
{
    "actor": "https://github.com/mezzarobba",
    "created_at": "2014-03-14T15:29:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5671#event-13341"
}
```



---

archive/issue_comments_044281.json:
```json
{
    "body": "I'm not sure what needs review here?",
    "created_at": "2014-03-14T15:47:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44281",
    "user": "https://github.com/malb"
}
```

I'm not sure what needs review here?



---

archive/issue_comments_044282.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-14T15:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44282",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_044283.json:
```json
{
    "body": "Replying to [comment:12 malb]:\n> I'm not sure what needs review here?\n\n\nAs far as I understand the way to have a ticket closes as \"wontfix\" or similar is to set the milestone to `duplicate/invalid/wontfix` and wait for someone else to review that choice.",
    "created_at": "2014-03-14T16:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44283",
    "user": "https://github.com/mezzarobba"
}
```

Replying to [comment:12 malb]:
> I'm not sure what needs review here?


As far as I understand the way to have a ticket closes as "wontfix" or similar is to set the milestone to `duplicate/invalid/wontfix` and wait for someone else to review that choice.



---

archive/issue_comments_044284.json:
```json
{
    "body": "Which has been done :)  mmezz, just add your real name in the reviewers field.",
    "created_at": "2014-03-14T16:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44284",
    "user": "https://github.com/kcrisman"
}
```

Which has been done :)  mmezz, just add your real name in the reviewers field.



---

archive/issue_events_013342.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-03-19T04:41:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5671#event-13342"
}
```



---

archive/issue_comments_044285.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-03-19T04:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44285",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate
