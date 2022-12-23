# Issue 3084: Solve Sudoku faster!

Issue created by migration from https://trac.sagemath.org/ticket/3084

Original creator: boothby

Original creation time: 2008-05-02 21:59:18

Assignee: mabshoff

I've got a faster Sudoku-solving class than what's currently in Sage.


---

Attachment


---

Comment by boothby created at 2008-05-02 22:00:09

Changing type from defect to enhancement.


---

Comment by boothby created at 2008-05-02 22:00:09

Changing assignee from mabshoff to cwitty.


---

Comment by boothby created at 2008-05-02 22:00:09

Changing component from Cygwin to misc.


---

Comment by rbeezer created at 2009-06-07 00:01:08

Apply just this patch


---

Attachment

Current patch has a "sudoku puzzle" class, with tools for input/output of puzzles and two algorithms for finding solutions, including obtaining multiple solutions.

DLX algorithm by Tom Boothby consistently solves 9x9 hard puzzles at a rate of about 700 per second on modern, but not extravagant, hardware.  Cythonized backtracking algorithm by Rob Beezer is more variable in performance, and can solve some hard puzzles at the rate of 4000 per second, though other problems can take close to a full second.

DLX will work on any size puzzle (array dimensions must be perfect squares), string format works on up to 36x36, backtracking works on up to 16x16 since memory is not allocated dynamically.


---

Comment by mvngu created at 2009-06-08 04:12:59

If the patch results in better performance, there should be ("good") code to illustrate this both before and after applying the patch. Such information is good for release tours.


---

Comment by rbeezer created at 2009-06-08 06:52:55

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

Comment by ncalexan created at 2009-06-15 19:45:40

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

Comment by rlm created at 2009-06-24 10:12:44

Resolution: fixed
