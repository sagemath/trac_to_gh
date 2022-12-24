# Issue 5671: Create a spkg for minisat

archive/issues_005671.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  fichtejo\n\nWe want miniSAT.  spkg it up!\n\nIssue created by migration from https://trac.sagemath.org/ticket/5671\n\n",
    "created_at": "2009-04-02T22:10:41Z",
    "labels": [
        "packages: standard",
        "minor",
        "enhancement"
    ],
    "title": "Create a spkg for minisat",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5671",
    "user": "boothby"
}
```
Assignee: boothby

CC:  fichtejo

We want miniSAT.  spkg it up!

Issue created by migration from https://trac.sagemath.org/ticket/5671





---

archive/issue_comments_044358.json:
```json
{
    "body": "Attachment [trac_5671-part1.patch](tarball://root/attachments/some-uuid/ticket5671/trac_5671-part1.patch) by boothby created at 2009-04-02 22:28:11",
    "created_at": "2009-04-02T22:28:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44358",
    "user": "boothby"
}
```

Attachment [trac_5671-part1.patch](tarball://root/attachments/some-uuid/ticket5671/trac_5671-part1.patch) by boothby created at 2009-04-02 22:28:11



---

archive/issue_comments_044359.json:
```json
{
    "body": "Might I point out that this is a dupe of #418.\n\nYou also \n\n* should assign a milestone when you open a ticket\n* not attach spkgs to tickets, but post a link. Given that this one is 77kb it might be a borderline case.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-02T22:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44359",
    "user": "mabshoff"
}
```

Might I point out that this is a dupe of #418.

You also 

* should assign a milestone when you open a ticket
* not attach spkgs to tickets, but post a link. Given that this one is 77kb it might be a borderline case.

Cheers,

Michael



---

archive/issue_comments_044360.json:
```json
{
    "body": "Attachment [trac_5671-part2.patch](tarball://root/attachments/some-uuid/ticket5671/trac_5671-part2.patch) by boothby created at 2009-04-02 22:55:32",
    "created_at": "2009-04-02T22:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44360",
    "user": "boothby"
}
```

Attachment [trac_5671-part2.patch](tarball://root/attachments/some-uuid/ticket5671/trac_5671-part2.patch) by boothby created at 2009-04-02 22:55:32



---

archive/issue_comments_044361.json:
```json
{
    "body": "Attachment [trac_5671-part3.patch](tarball://root/attachments/some-uuid/ticket5671/trac_5671-part3.patch) by was created at 2009-04-02 23:11:34\n\nWith just the posted code to this point:\n\n```\nsage: S = minisat.Solver(verbosity=2)\nsage: S.new_var()\n0\nsage: S.new_var()\n1\nsage: S.new_var()\n2\nsage: S.new_var()\n3\nsage: S.add_clause([1])\npushing lit.p =  Literal 1\nsage: S.add_clause([2])\npushing lit.p =  Literal 2\nsage: S.solve()\n============================[ Search Statistics ]==============================\n===============================================================================\n===============================================================================\nVerified 0 original clauses.\nTrue\n```\n",
    "created_at": "2009-04-02T23:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44361",
    "user": "was"
}
```

Attachment [trac_5671-part3.patch](tarball://root/attachments/some-uuid/ticket5671/trac_5671-part3.patch) by was created at 2009-04-02 23:11:34

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

archive/issue_comments_044362.json:
```json
{
    "body": "This\n\n   http://planete.inrialpes.fr/~soos/CryptoMiniSat/index.html\n\nmight be relevant. It is an enhanced MiniSat with:\n\n* Natively handled XOR functions\n* Statistics generation\n* Search randomization\n* Detailed solving process visualization\n* Clause grouping and group naming\n* Variable naming\n* Debug mode\n* Code cleanup",
    "created_at": "2009-09-02T10:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44362",
    "user": "malb"
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

archive/issue_comments_044363.json:
```json
{
    "body": "Replying to [comment:5 malb]:\n> This\n> \n>    http://planete.inrialpes.fr/~soos/CryptoMiniSat/index.html\n> \n> might be relevant. It is an enhanced MiniSat with:\n> \n>  * Natively handled XOR functions\n>  * Statistics generation\n>  * Search randomization\n>  * Detailed solving process visualization\n>  * Clause grouping and group naming\n>  * Variable naming\n>  * Debug mode\n>  * Code cleanup\n\nGiven this and recent developments at #418, perhaps this is a dupe?",
    "created_at": "2012-06-04T19:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44363",
    "user": "kcrisman"
}
```

Replying to [comment:5 malb]:
> This
> 
>    http://planete.inrialpes.fr/~soos/CryptoMiniSat/index.html
> 
> might be relevant. It is an enhanced MiniSat with:
> 
>  * Natively handled XOR functions
>  * Statistics generation
>  * Search randomization
>  * Detailed solving process visualization
>  * Clause grouping and group naming
>  * Variable naming
>  * Debug mode
>  * Code cleanup

Given this and recent developments at #418, perhaps this is a dupe?



---

archive/issue_comments_044364.json:
```json
{
    "body": "I vote for declaring this ticket a dupe.",
    "created_at": "2012-06-15T16:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44364",
    "user": "malb"
}
```

I vote for declaring this ticket a dupe.



---

archive/issue_comments_044365.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-03-14T15:29:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44365",
    "user": "mmezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_044366.json:
```json
{
    "body": "I'm not sure what needs review here?",
    "created_at": "2014-03-14T15:47:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44366",
    "user": "malb"
}
```

I'm not sure what needs review here?



---

archive/issue_comments_044367.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-14T15:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44367",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_044368.json:
```json
{
    "body": "Replying to [comment:12 malb]:\n> I'm not sure what needs review here?\n\nAs far as I understand the way to have a ticket closes as \"wontfix\" or similar is to set the milestone to `duplicate/invalid/wontfix` and wait for someone else to review that choice.",
    "created_at": "2014-03-14T16:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44368",
    "user": "mmezzarobba"
}
```

Replying to [comment:12 malb]:
> I'm not sure what needs review here?

As far as I understand the way to have a ticket closes as "wontfix" or similar is to set the milestone to `duplicate/invalid/wontfix` and wait for someone else to review that choice.



---

archive/issue_comments_044369.json:
```json
{
    "body": "Which has been done :)  mmezz, just add your real name in the reviewers field.",
    "created_at": "2014-03-14T16:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44369",
    "user": "kcrisman"
}
```

Which has been done :)  mmezz, just add your real name in the reviewers field.



---

archive/issue_comments_044370.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-03-19T04:41:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5671",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5671#issuecomment-44370",
    "user": "vbraun"
}
```

Resolution: duplicate
