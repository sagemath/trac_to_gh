# Issue 5752: Bring doctests of sage/games/sudoku.py to 100%

archive/issues_005752.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5752\n\n",
    "created_at": "2009-04-11T15:47:56Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Bring doctests of sage/games/sudoku.py to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5752",
    "user": "rbeezer"
}
```
Assignee: mabshoff



Issue created by migration from https://trac.sagemath.org/ticket/5752





---

archive/issue_comments_044962.json:
```json
{
    "body": "Coverage is now 100%, Several additional examples, including a minimal-hint, uniquely-solvable puzzle.  Some minor code and comment clean-ups.",
    "created_at": "2009-04-11T19:28:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5752#issuecomment-44962",
    "user": "rbeezer"
}
```

Coverage is now 100%, Several additional examples, including a minimal-hint, uniquely-solvable puzzle.  Some minor code and comment clean-ups.



---

archive/issue_comments_044963.json:
```json
{
    "body": "Attachment [trac_5752_sudoku_doctest.patch](tarball://root/attachments/some-uuid/ticket5752/trac_5752_sudoku_doctest.patch) by rbeezer created at 2009-04-11 19:29:09",
    "created_at": "2009-04-11T19:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5752#issuecomment-44963",
    "user": "rbeezer"
}
```

Attachment [trac_5752_sudoku_doctest.patch](tarball://root/attachments/some-uuid/ticket5752/trac_5752_sudoku_doctest.patch) by rbeezer created at 2009-04-11 19:29:09



---

archive/issue_comments_044964.json:
```json
{
    "body": "Cool example in the docstring, though of course that the sudoku command at the top level takes forever on this hard one is a bummer.  I wish there were a better solver in sage..\n\n\n```\nsage: B = matrix(ZZ, 9, 9, [ [0,0,0,0,1,0,9,0,0], [8,0,0,4,0,0,0,0,0], [2,0,0,0,0,0,0,0,0], [0,7,0,0,3,0,0,0,0], [0,0,0,0,0,0,2,0,4], [0,0,0,0,0,0,0,5,8], [0,6,0,0,0,0,1,3,0], [7,0,0,2,0,0,0,0,0], [0,0,0,8,0,0,0,0,0] ])\nsage: sudoku(B)\n[wait forever...]\n```\n\n\nVery nice job adding doctests!!",
    "created_at": "2009-04-12T05:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5752#issuecomment-44964",
    "user": "was"
}
```

Cool example in the docstring, though of course that the sudoku command at the top level takes forever on this hard one is a bummer.  I wish there were a better solver in sage..


```
sage: B = matrix(ZZ, 9, 9, [ [0,0,0,0,1,0,9,0,0], [8,0,0,4,0,0,0,0,0], [2,0,0,0,0,0,0,0,0], [0,7,0,0,3,0,0,0,0], [0,0,0,0,0,0,2,0,4], [0,0,0,0,0,0,0,5,8], [0,6,0,0,0,0,1,3,0], [7,0,0,2,0,0,0,0,0], [0,0,0,8,0,0,0,0,0] ])
sage: sudoku(B)
[wait forever...]
```


Very nice job adding doctests!!



---

archive/issue_comments_044965.json:
```json
{
    "body": "Replying to [comment:2 was]:\n> I wish there were a better solver in sage..\n\nI did have some thoughts about that while working through this...\n\n> ` [wait forever...] `\n\nI did eventually get a solution on that one, but didn't go back to do a timing on it!",
    "created_at": "2009-04-12T06:00:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5752#issuecomment-44965",
    "user": "rbeezer"
}
```

Replying to [comment:2 was]:
> I wish there were a better solver in sage..

I did have some thoughts about that while working through this...

> ` [wait forever...] `

I did eventually get a solution on that one, but didn't go back to do a timing on it!



---

archive/issue_comments_044966.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-12T21:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5752#issuecomment-44966",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_044967.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-12T21:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5752",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5752#issuecomment-44967",
    "user": "mabshoff"
}
```

Resolution: fixed
