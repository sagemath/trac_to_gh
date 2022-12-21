# Issue 5931: [with patch, needs review] Greatly speed up sage.combinat.symmetric_group_algebra.e

Issue created by migration from Trac.

Original creator: jdc

Original creation time: 2009-04-29 02:01:49

Assignee: mhansen

The old code essentially reimplemented the multiplication in the group algebra.  The new code accumulates the symmetrizers and antisymmetrizers separately, and then does one multiply at the end.  This probably results in the same number of operations, but it avoids creating many intermediate objects, so it is about 10x faster.

Also update docs for e and e_hat.

Timing on 2.2 GHz Core2Duo running 32-bit Ubuntu 8.04 of

from sage.combinat.symmetric_group_algebra import e


time dummy=e([[1,2,3,4],[5,6,7]])

Before patch:

Time: CPU 3.38 s, Wall: 3.73 s

After patch:

Time: CPU 0.26 s, Wall: 0.40 s



---

Attachment


---

Attachment

I think the main reason the old code was slow was that it multiplied GAP group elements in the inner loop, while the new code in e.patch uses the combinatorial algebra multiplication, which internally multiplies sage Permutations.  Another reason the old code was slower is that it looped over the GAP column_stabilizer group multiple times (probably requiring interaction with GAP) and re-computed v.sign() each time.  However, I did some tests where I avoid just these problems, and still the new code in e.patch is better, almost certainly because it avoids creating lots of intermediate elements of QSn.

We can avoid even more of the intermediate elements of QSn with dict.patch which I will attach below.  But it only speeds things up by about 2% in the test I ran, since the runtime is dominated by the antisym*sym multiplication.

If we are willing to assume that the entries in the tableau are distinct, I have another method which is 25% faster, but I don't think we want to make that assumption.  Just for the record, the point is that if the entries are distinct, then each of the products v*h is distinct, so we can easily construct a dictionary for the final result whose values are plus or minus 1.

Summary: I recommend the new dict.patch (which includes the documentation change), but it would also be ok to use e.patch and doc.patch if that method is preferred.

PS: Note that these patches seem to reverse the order of multiplication from h*v to v*h.  That's because of differing conventions between GAP group elements and permutations.

PPS: My latest test case has been e([[1,2,3,4,5],[6,7,8],[9,10],[11]]), which takes forever with sage 3.4, but takes 20-30 seconds with the above patches.


---

Comment by jdc created at 2009-04-29 16:09:48

Replaces both e.patch and doc.patch; relative to 3.4


---

Attachment


---

Comment by mhansen created at 2009-06-04 19:19:14

Looks good to me.  Thanks for this!

Merged in 4.0.1.rc1.


---

Comment by mhansen created at 2009-06-04 19:19:14

Resolution: fixed
