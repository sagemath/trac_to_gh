# Issue 3084: Solve Sudoku faster!

archive/issues_003084.json:
```json
{
    "body": "Assignee: mabshoff\n\nI've got a faster Sudoku-solving class than what's currently in Sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3084\n\n",
    "created_at": "2008-05-02T21:59:18Z",
    "labels": [
        "Cygwin",
        "trivial",
        "bug"
    ],
    "title": "Solve Sudoku faster!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3084",
    "user": "boothby"
}
```
Assignee: mabshoff

I've got a faster Sudoku-solving class than what's currently in Sage.

Issue created by migration from https://trac.sagemath.org/ticket/3084





---

archive/issue_comments_021292.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-05-02T21:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3084#issuecomment-21292",
    "user": "boothby"
}
```

Attachment



---

archive/issue_comments_021293.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-05-02T22:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3084#issuecomment-21293",
    "user": "boothby"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_021294.json:
```json
{
    "body": "Changing assignee from mabshoff to cwitty.",
    "created_at": "2008-05-02T22:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3084#issuecomment-21294",
    "user": "boothby"
}
```

Changing assignee from mabshoff to cwitty.



---

archive/issue_comments_021295.json:
```json
{
    "body": "Changing component from Cygwin to misc.",
    "created_at": "2008-05-02T22:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3084#issuecomment-21295",
    "user": "boothby"
}
```

Changing component from Cygwin to misc.



---

archive/issue_comments_021296.json:
```json
{
    "body": "Apply just this patch",
    "created_at": "2009-06-07T00:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3084#issuecomment-21296",
    "user": "rbeezer"
}
```

Apply just this patch



---

archive/issue_comments_021297.json:
```json
{
    "body": "Attachment\n\nCurrent patch has a \"sudoku puzzle\" class, with tools for input/output of puzzles and two algorithms for finding solutions, including obtaining multiple solutions.\n\nDLX algorithm by Tom Boothby consistently solves 9x9 hard puzzles at a rate of about 700 per second on modern, but not extravagant, hardware.  Cythonized backtracking algorithm by Rob Beezer is more variable in performance, and can solve some hard puzzles at the rate of 4000 per second, though other problems can take close to a full second.\n\nDLX will work on any size puzzle (array dimensions must be perfect squares), string format works on up to 36x36, backtracking works on up to 16x16 since memory is not allocated dynamically.",
    "created_at": "2009-06-07T00:10:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3084#issuecomment-21297",
    "user": "rbeezer"
}
```

Attachment

Current patch has a "sudoku puzzle" class, with tools for input/output of puzzles and two algorithms for finding solutions, including obtaining multiple solutions.

DLX algorithm by Tom Boothby consistently solves 9x9 hard puzzles at a rate of about 700 per second on modern, but not extravagant, hardware.  Cythonized backtracking algorithm by Rob Beezer is more variable in performance, and can solve some hard puzzles at the rate of 4000 per second, though other problems can take close to a full second.

DLX will work on any size puzzle (array dimensions must be perfect squares), string format works on up to 36x36, backtracking works on up to 16x16 since memory is not allocated dynamically.



---

archive/issue_comments_021298.json:
```json
{
    "body": "If the patch results in better performance, there should be (\"good\") code to illustrate this both before and after applying the patch. Such information is good for release tours.",
    "created_at": "2009-06-08T04:12:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3084#issuecomment-21298",
    "user": "mvngu"
}
```

If the patch results in better performance, there should be ("good") code to illustrate this both before and after applying the patch. Such information is good for release tours.



---

archive/issue_comments_021299.json:
```json
{
    "body": "Replying to [comment:4 mvngu]:\n> If the patch results in better performance, there should be (\"good\") code to illustrate this both before and after applying the patch. Such information is good for release tours.\n\nMinh,\n\nHere you go.\n\nThanks,\nRob\n\n\n```\nOriginal doctest example\nA = '5...8..49...5...3..673....115..........2.8..........187....415..3...2...49..5...3'\n\nA 17-hint puzzle (no 16-hint puzzles known)\nB = '....1.9..8..4.....2.........7..3..........2.4.......58.6....13.7..2........8.....'\n\nDifficult for backtracking, Wikipedia's \"worst case\"\nC = '..............3.85..1.2.......5.7.....4...1...9.......5......73..2.1........4...9'\n\nTimings on 3 GHz Intel Core Duo, KUbuntu 8.10\n  4.0.1 = backtracking via recursive calls\n  DLX = Exact Cover, Dancing Links algorithm\n  BackTrack = Cythonized backtracking with propogation\n\n    4.0.1    Patch/DLX  Patch/BT    Factors\nA   34 ms    1.11 ms    187 us      31x, 182x\n\nB   1494 s   1.20 ms    441 ms      1245000x, 3388x\n\nC   4798 s   1.21 ms    944 ms      4000000x, 5000x\n```\n",
    "created_at": "2009-06-08T06:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3084#issuecomment-21299",
    "user": "rbeezer"
}
```

Replying to [comment:4 mvngu]:
> If the patch results in better performance, there should be ("good") code to illustrate this both before and after applying the patch. Such information is good for release tours.

Minh,

Here you go.

Thanks,
Rob


```
Original doctest example
A = '5...8..49...5...3..673....115..........2.8..........187....415..3...2...49..5...3'

A 17-hint puzzle (no 16-hint puzzles known)
B = '....1.9..8..4.....2.........7..3..........2.4.......58.6....13.7..2........8.....'

Difficult for backtracking, Wikipedia's "worst case"
C = '..............3.85..1.2.......5.7.....4...1...9.......5......73..2.1........4...9'

Timings on 3 GHz Intel Core Duo, KUbuntu 8.10
  4.0.1 = backtracking via recursive calls
  DLX = Exact Cover, Dancing Links algorithm
  BackTrack = Cythonized backtracking with propogation

    4.0.1    Patch/DLX  Patch/BT    Factors
A   34 ms    1.11 ms    187 us      31x, 182x

B   1494 s   1.20 ms    441 ms      1245000x, 3388x

C   4798 s   1.21 ms    944 ms      4000000x, 5000x
```




---

archive/issue_comments_021300.json:
```json
{
    "body": "This looks great, albeit with some long lines (in the algorithm description, not doctests).  Apply!\n\nOn sage.math:\n\n\n```\nsage: %timeit sage.games.sudoku.Sudoku('5...8..49...5...3..673....115..........2.8..........187....415..3...2...49..5...3').solve().next()\n1000 loops, best of 3: 1.37 ms per loop\nsage: %timeit sage.games.sudoku.Sudoku('....1.9..8..4.....2.........7..3..........2.4.......58.6....13.7..2........8.....').solve().next()\n1000 loops, best of 3: 1.48 ms per loop\nsage: %timeit sage.games.sudoku.Sudoku('..............3.85..1.2.......5.7.....4...1...9.......5......73..2.1........4...9').solve().next()1000 loops, best of 3: 1.48 ms per loop\n```\n",
    "created_at": "2009-06-15T19:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3084#issuecomment-21300",
    "user": "ncalexan"
}
```

This looks great, albeit with some long lines (in the algorithm description, not doctests).  Apply!

On sage.math:


```
sage: %timeit sage.games.sudoku.Sudoku('5...8..49...5...3..673....115..........2.8..........187....415..3...2...49..5...3').solve().next()
1000 loops, best of 3: 1.37 ms per loop
sage: %timeit sage.games.sudoku.Sudoku('....1.9..8..4.....2.........7..3..........2.4.......58.6....13.7..2........8.....').solve().next()
1000 loops, best of 3: 1.48 ms per loop
sage: %timeit sage.games.sudoku.Sudoku('..............3.85..1.2.......5.7.....4...1...9.......5......73..2.1........4...9').solve().next()1000 loops, best of 3: 1.48 ms per loop
```




---

archive/issue_comments_021301.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T10:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3084#issuecomment-21301",
    "user": "rlm"
}
```

Resolution: fixed
