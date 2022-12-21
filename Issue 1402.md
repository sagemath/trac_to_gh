# Issue 1402: 'mwrank' has termination issues

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2007-12-05 05:35:01

Assignee: was

The program needs to be terminated with a "null curve", "[0,0,0,0,0]", and does not handle an EOF gracefully (whether at the end of a "real file" or a "CTRL-D" from the terminal).

In 'getcurve()' (in "getcurve.cc"), input of a curve is handled by

```
   cin >> C0
```

and "c.input()" (in "curve.cc") doesn't deal with EOF.  Instead, it aborts, causing problems upstream.

The fix is to turn EOF into "[0.0.0.0.0]" or its moral equivalent.  I don't know  the code well enough to know whether this is feasible.


---

Comment by mabshoff created at 2007-12-18 21:59:57

The updated spkg at

http://sage.math.washington.edu/home/mabshoff/cremona-20071124.p5.spkg

*might* fix the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-19 13:48:12

Do not merge the above spkg, but the one at

http://www.warwick.ac.uk/staff/J.E.Cremona/cremona-20071219.spkg

I still haven't tested if the above fixes *this* issue or nor, so please leave this ticket open.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-19 14:23:46

The following spkg at

http://sage.math.washington.edu/home/mabshoff/cremona-20071219.p0.spkg

builds fine on sage.math and bsd.

Cheers,

Michael


---

Comment by cartman created at 2008-01-04 22:00:57

GCC used : gcc version 4.3.0 20080104 [trunk revision 131325] (Pardus Linux)

eclib-20071231.p1.spkg

I got no crash :

[~/la/eclib-20071231.p1/src/qrank]> ./mwrank
Program mwrank: uses 2-descent (via 2-isogeny if possible) to
determine the rank of an elliptic curve E over Q, and list a
set of points which generate E(Q) modulo 2E(Q).
and finally saturate to obtain generating points on the curve.
For more details see the file mwrank.doc.
For details of algorithms see the author's book.

Please acknowledge use of this program in published work,
and send problems to john.cremona`@`gmail.com.

Version compiled on Jan  4 2008 at 23:55:58 by GCC 4.3.0 20080104 [trunk revision 131325]
using base arithmetic option NTL_ALL (NTL bigints and multiprecision floating point)
Using NTL multiprecision floating point with 15 decimal places.
Enter curve: [0,0,1,-1,0]
Curve [0,0,1,-1,0] :    Basic pair: I=48, J=-432
disc=255744
2-adic index bound = 2
By Lemma 5.1(a), 2-adic index = 1
2-adic index = 1
One (I,J) pair
Looking for quartics with I = 48, J = -432
Looking for Type 2 quartics:
Trying positive a from 1 up to 1 (square a first...)
(1,0,-6,4,1)    --trivial
Trying positive a from 1 up to 1 (...then non-square a)
Finished looking for Type 2 quartics.
Looking for Type 1 quartics:
Trying positive a from 1 up to 2 (square a first...)
(1,0,0,4,4)     --nontrivial...(x:y:z) = (1 : 1 : 0)
Point = [0:0:1]
        height = 0.0511114082399688
Rank of B=im(eps) increases to 1 (The previous point is on the egg)
Exiting search for Type 1 quartics after finding one which is globally soluble.
Mordell rank contribution from B=im(eps) = 1
Selmer  rank contribution from B=im(eps) = 1
Sha     rank contribution from B=im(eps) = 0
Mordell rank contribution from A=ker(eps) = 0
Selmer  rank contribution from A=ker(eps) = 0
Sha     rank contribution from A=ker(eps) = 0
Rank = 1
Searching for points (bound = 8)...done:
  found points of rank 1
  and regulator 0.0511114082399688
Processing points found during 2-descent...done:
  now regulator = 0.0511114082399688
Saturating (bound = 100)...done:
  points were already saturated.
Transferring points from minimal curve [0,0,1,-1,0] back to original curve [0,0,1,-1,0]

Generator 1 is [0:-1:1]; height 0.0511114082399688

Regulator = 0.0511114082399688

The rank and full Mordell-Weil basis have been determined unconditionally.
 (0.64004 seconds)


---

Comment by cartman created at 2008-01-04 22:01:59

And with correct formatting


```
[~/la/eclib-20071231.p1/src/qrank]> ./mwrank
Program mwrank: uses 2-descent (via 2-isogeny if possible) to
determine the rank of an elliptic curve E over Q, and list a
set of points which generate E(Q) modulo 2E(Q).
and finally saturate to obtain generating points on the curve.
For more details see the file mwrank.doc.
For details of algorithms see the author's book.

Please acknowledge use of this program in published work,
and send problems to john.cremona`@`gmail.com.

Version compiled on Jan  4 2008 at 23:55:58 by GCC 4.3.0 20080104 [trunk revision 131325]
using base arithmetic option NTL_ALL (NTL bigints and multiprecision floating point)
Using NTL multiprecision floating point with 15 decimal places.
Enter curve: [0,0,1,-1,0]
Curve [0,0,1,-1,0] :    Basic pair: I=48, J=-432
disc=255744
2-adic index bound = 2
By Lemma 5.1(a), 2-adic index = 1
2-adic index = 1
One (I,J) pair
Looking for quartics with I = 48, J = -432
Looking for Type 2 quartics:
Trying positive a from 1 up to 1 (square a first...)
(1,0,-6,4,1)    --trivial
Trying positive a from 1 up to 1 (...then non-square a)
Finished looking for Type 2 quartics.
Looking for Type 1 quartics:
Trying positive a from 1 up to 2 (square a first...)
(1,0,0,4,4)     --nontrivial...(x:y:z) = (1 : 1 : 0)
Point = [0:0:1]
        height = 0.0511114082399688
Rank of B=im(eps) increases to 1 (The previous point is on the egg)
Exiting search for Type 1 quartics after finding one which is globally soluble.
Mordell rank contribution from B=im(eps) = 1
Selmer  rank contribution from B=im(eps) = 1
Sha     rank contribution from B=im(eps) = 0
Mordell rank contribution from A=ker(eps) = 0
Selmer  rank contribution from A=ker(eps) = 0
Sha     rank contribution from A=ker(eps) = 0
Rank = 1
Searching for points (bound = 8)...done:
  found points of rank 1
  and regulator 0.0511114082399688
Processing points found during 2-descent...done:
  now regulator = 0.0511114082399688
Saturating (bound = 100)...done:
  points were already saturated.
Transferring points from minimal curve [0,0,1,-1,0] back to original curve [0,0,1,-1,0]

Generator 1 is [0:-1:1]; height 0.0511114082399688

Regulator = 0.0511114082399688

The rank and full Mordell-Weil basis have been determined unconditionally.
 (0.64004 seconds)
```



---

Comment by mabshoff created at 2008-02-15 23:14:21

Closing against Sage 2.10.1 since the issue has been fixed an the latest eclib.spkg merged in Sage 2.10.1 or so.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-15 23:14:21

Resolution: fixed
