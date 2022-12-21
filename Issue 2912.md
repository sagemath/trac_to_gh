# Issue 2912: M4RI should be built with -O3

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-04-13 21:05:11

Assignee: was

Keywords: speed, build system

** it is fairly straight forward C so it shouldn't break under `-O3`
 * it makes a noticeable speed difference. To echelonise a random 10<sup>4</sup> x 10<sup>4</sup> matrix takes ~ 8 seconds with `-O2` and ~ 6 seconds with `-O3`.


---

Comment by malb created at 2008-04-13 21:55:17

New SPKG up at:

   http://sage.math.washington.edu/home/malb/libm4ri-20071224.p2.spkg


---

Comment by mabshoff created at 2008-04-13 23:41:50

Spkg looks good to me. Changes are minimal. We still need an SPKG.txt, but that can be done down the road. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-13 23:42:25

Resolution: fixed


---

Comment by mabshoff created at 2008-04-13 23:42:25

Merged in Sage 3.0.alpha5
