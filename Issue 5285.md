# Issue 5285: Dyck Paths documentation problem

Issue created by migration from https://trac.sagemath.org/ticket/5285

Original creator: jbandlow

Original creation time: 2009-02-16 14:30:22

Assignee: jbandlow

CC:  sage-combinat

Keywords: dyck words

Mike Zabrocki posted the following to sage.combinat.devel:

Hi,
I'm making a bug report instead of fixing this myself.

I have a student who is working on Dyck paths and
she read the documentation for some of the code
and noticed a few inconsistencies.

a.b_statistic(self)

Returns the b-statistic for the Dyck word.

One can view a balanced Dyck word as a lattice path from (0,0) to
(n,n) in the first quadrant by letting '1's represent steps in
the direction (1,0) and '0's represent steps in the direction
(0,1).  The resulting path will remain weakly above the
diagonal y = x.

As she points out (1,0) should mean horizontal step (following
Descartes) and (0,1) should be a vertical step in which case
the path will be below the diagonal compared to what the code
used (e.g. 11100010 steps horizontally first by the documentation
hence is 'below' the diagonal).  I believe that interchanging (1,0)
and (0,1) should fix the inconsistency in this part of the
documentation.

Then further down the documentation reads:

We can think of our bounce path as describing the trail of a 
billiard ball shot North from (0, 0), which "bounces" right
whenever it encounters a horizontal step and "bounces" up
when it encounters the line y = x. The bouncing ball will strike
the diagonal at places (0, 0), (j_1, j_1), (j_2, j_2), ... ,
(j_r-1, j_r-1), (j_r, j_r) = (n, n). We define the b-statistic to
be the sum sum_{i=1}^{r-1} n - j_i.

and in the the examples (one of many):

```
  sage: DyckWord([1,1,1,0,0,1,0,0]).b_statistic()
  2
```


does not agree with the description because the diagonal
places it hits are (0,0), (3,3), (4,4) and 4-3 = 1.
The documentation does not agree with the code.

What is really happening is different.  The bounce path starts
at (n,n), moves left and down and the statistic is the sum
of the coordinates j_i where the bounce path hits the diagonal
at (j_i, j_i).

The paragraph should read (which is no
longer quoting *directly* from Jim Haglund's reference):

We can think of our bounce path as describing the trail of a
billiard ball shot West from (n, n), which "bounces" down
whenever it encounters a vertical step and "bounces" left
when it encounters the line y = x. The bouncing ball will strike
the diagonal at places (0, 0), (j_1, j_1), (j_2, j_2), ... ,
(j_r-1, j_r-1), (j_r, j_r) = (n, n). We define the b-statistic to
be the sum sum_{i=1}^{r-1} j_i.

It seems easier to me to change the documentation than the code.
Both definitions of bounce statistic are valid.
The documentation was included directly from the reference,
but does not follow the code which does indeed refer to "left" and
"drop" rather than "right" and "up"

-Mike


---

Comment by mabshoff created at 2009-02-16 14:35:12

Changing component from algebra to combinatorics.


---

Attachment


---

Comment by jbandlow created at 2009-02-16 14:46:45

Michael,

Any chance of this getting into 3.3 if it gets a quick review?


---

Comment by mabshoff created at 2009-02-16 14:48:56

Replying to [comment:2 jbandlow]:
> Michael,

Hi Jason,

> Any chance of this getting into 3.3 if it gets a quick review?

Yep, the patch is documentation only, so get a review and it will be merged.

Cheers,

Michael


---

Comment by mhansen created at 2009-02-17 13:51:28

Looks good to me.


---

Comment by mabshoff created at 2009-02-17 20:21:34

Resolution: fixed


---

Comment by mabshoff created at 2009-02-17 20:21:34

Merged in Sage 3.3.rc2.

Cheers,

Michael
