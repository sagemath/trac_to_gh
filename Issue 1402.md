# Issue 1402: 'mwrank' has termination issues

archive/issues_001402.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe program needs to be terminated with a \"null curve\", \"[0,0,0,0,0]\", and does not handle an EOF gracefully (whether at the end of a \"real file\" or a \"CTRL-D\" from the terminal).\n\nIn 'getcurve()' (in \"getcurve.cc\"), input of a curve is handled by\n\n```\n   cin >> C0\n```\nand \"c.input()\" (in \"curve.cc\") doesn't deal with EOF.  Instead, it aborts, causing problems upstream.\n\nThe fix is to turn EOF into \"[0.0.0.0.0]\" or its moral equivalent.  I don't know  the code well enough to know whether this is feasible.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1402\n\n",
    "created_at": "2007-12-05T05:35:01Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "'mwrank' has termination issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1402",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: @williamstein

The program needs to be terminated with a "null curve", "[0,0,0,0,0]", and does not handle an EOF gracefully (whether at the end of a "real file" or a "CTRL-D" from the terminal).

In 'getcurve()' (in "getcurve.cc"), input of a curve is handled by

```
   cin >> C0
```
and "c.input()" (in "curve.cc") doesn't deal with EOF.  Instead, it aborts, causing problems upstream.

The fix is to turn EOF into "[0.0.0.0.0]" or its moral equivalent.  I don't know  the code well enough to know whether this is feasible.

Issue created by migration from https://trac.sagemath.org/ticket/1402





---

archive/issue_events_003618.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-05T11:32:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1402",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1402#event-3618"
}
```



---

archive/issue_comments_009018.json:
```json
{
    "body": "The updated spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/cremona-20071124.p5.spkg\n\n*might* fix the issue.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-18T21:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1402#issuecomment-9018",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The updated spkg at

http://sage.math.washington.edu/home/mabshoff/cremona-20071124.p5.spkg

*might* fix the issue.

Cheers,

Michael



---

archive/issue_comments_009019.json:
```json
{
    "body": "Do not merge the above spkg, but the one at\n\nhttp://www.warwick.ac.uk/staff/J.E.Cremona/cremona-20071219.spkg\n\nI still haven't tested if the above fixes *this* issue or nor, so please leave this ticket open.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-19T13:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1402#issuecomment-9019",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Do not merge the above spkg, but the one at

http://www.warwick.ac.uk/staff/J.E.Cremona/cremona-20071219.spkg

I still haven't tested if the above fixes *this* issue or nor, so please leave this ticket open.

Cheers,

Michael



---

archive/issue_comments_009020.json:
```json
{
    "body": "The following spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/cremona-20071219.p0.spkg\n\nbuilds fine on sage.math and bsd.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-19T14:23:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1402#issuecomment-9020",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The following spkg at

http://sage.math.washington.edu/home/mabshoff/cremona-20071219.p0.spkg

builds fine on sage.math and bsd.

Cheers,

Michael



---

archive/issue_comments_009021.json:
```json
{
    "body": "GCC used : gcc version 4.3.0 20080104 [trunk revision 131325] (Pardus Linux)\n\neclib-20071231.p1.spkg\n\nI got no crash :\n\n[~/la/eclib-20071231.p1/src/qrank]> ./mwrank\nProgram mwrank: uses 2-descent (via 2-isogeny if possible) to\ndetermine the rank of an elliptic curve E over Q, and list a\nset of points which generate E(Q) modulo 2E(Q).\nand finally saturate to obtain generating points on the curve.\nFor more details see the file mwrank.doc.\nFor details of algorithms see the author's book.\n\nPlease acknowledge use of this program in published work,\nand send problems to john.cremona`@`gmail.com.\n\nVersion compiled on Jan  4 2008 at 23:55:58 by GCC 4.3.0 20080104 [trunk revision 131325]\nusing base arithmetic option NTL_ALL (NTL bigints and multiprecision floating point)\nUsing NTL multiprecision floating point with 15 decimal places.\nEnter curve: [0,0,1,-1,0]\nCurve [0,0,1,-1,0] :    Basic pair: I=48, J=-432\ndisc=255744\n2-adic index bound = 2\nBy Lemma 5.1(a), 2-adic index = 1\n2-adic index = 1\nOne (I,J) pair\nLooking for quartics with I = 48, J = -432\nLooking for Type 2 quartics:\nTrying positive a from 1 up to 1 (square a first...)\n(1,0,-6,4,1)    --trivial\nTrying positive a from 1 up to 1 (...then non-square a)\nFinished looking for Type 2 quartics.\nLooking for Type 1 quartics:\nTrying positive a from 1 up to 2 (square a first...)\n(1,0,0,4,4)     --nontrivial...(x:y:z) = (1 : 1 : 0)\nPoint = [0:0:1]\n        height = 0.0511114082399688\nRank of B=im(eps) increases to 1 (The previous point is on the egg)\nExiting search for Type 1 quartics after finding one which is globally soluble.\nMordell rank contribution from B=im(eps) = 1\nSelmer  rank contribution from B=im(eps) = 1\nSha     rank contribution from B=im(eps) = 0\nMordell rank contribution from A=ker(eps) = 0\nSelmer  rank contribution from A=ker(eps) = 0\nSha     rank contribution from A=ker(eps) = 0\nRank = 1\nSearching for points (bound = 8)...done:\n  found points of rank 1\n  and regulator 0.0511114082399688\nProcessing points found during 2-descent...done:\n  now regulator = 0.0511114082399688\nSaturating (bound = 100)...done:\n  points were already saturated.\nTransferring points from minimal curve [0,0,1,-1,0] back to original curve [0,0,1,-1,0]\n\nGenerator 1 is [0:-1:1]; height 0.0511114082399688\n\nRegulator = 0.0511114082399688\n\nThe rank and full Mordell-Weil basis have been determined unconditionally.\n (0.64004 seconds)",
    "created_at": "2008-01-04T22:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1402#issuecomment-9021",
    "user": "https://trac.sagemath.org/admin/accounts/users/cartman"
}
```

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

archive/issue_comments_009022.json:
```json
{
    "body": "And with correct formatting\n\n```\n[~/la/eclib-20071231.p1/src/qrank]> ./mwrank\nProgram mwrank: uses 2-descent (via 2-isogeny if possible) to\ndetermine the rank of an elliptic curve E over Q, and list a\nset of points which generate E(Q) modulo 2E(Q).\nand finally saturate to obtain generating points on the curve.\nFor more details see the file mwrank.doc.\nFor details of algorithms see the author's book.\n\nPlease acknowledge use of this program in published work,\nand send problems to john.cremona@gmail.com.\n\nVersion compiled on Jan  4 2008 at 23:55:58 by GCC 4.3.0 20080104 [trunk revision 131325]\nusing base arithmetic option NTL_ALL (NTL bigints and multiprecision floating point)\nUsing NTL multiprecision floating point with 15 decimal places.\nEnter curve: [0,0,1,-1,0]\nCurve [0,0,1,-1,0] :    Basic pair: I=48, J=-432\ndisc=255744\n2-adic index bound = 2\nBy Lemma 5.1(a), 2-adic index = 1\n2-adic index = 1\nOne (I,J) pair\nLooking for quartics with I = 48, J = -432\nLooking for Type 2 quartics:\nTrying positive a from 1 up to 1 (square a first...)\n(1,0,-6,4,1)    --trivial\nTrying positive a from 1 up to 1 (...then non-square a)\nFinished looking for Type 2 quartics.\nLooking for Type 1 quartics:\nTrying positive a from 1 up to 2 (square a first...)\n(1,0,0,4,4)     --nontrivial...(x:y:z) = (1 : 1 : 0)\nPoint = [0:0:1]\n        height = 0.0511114082399688\nRank of B=im(eps) increases to 1 (The previous point is on the egg)\nExiting search for Type 1 quartics after finding one which is globally soluble.\nMordell rank contribution from B=im(eps) = 1\nSelmer  rank contribution from B=im(eps) = 1\nSha     rank contribution from B=im(eps) = 0\nMordell rank contribution from A=ker(eps) = 0\nSelmer  rank contribution from A=ker(eps) = 0\nSha     rank contribution from A=ker(eps) = 0\nRank = 1\nSearching for points (bound = 8)...done:\n  found points of rank 1\n  and regulator 0.0511114082399688\nProcessing points found during 2-descent...done:\n  now regulator = 0.0511114082399688\nSaturating (bound = 100)...done:\n  points were already saturated.\nTransferring points from minimal curve [0,0,1,-1,0] back to original curve [0,0,1,-1,0]\n\nGenerator 1 is [0:-1:1]; height 0.0511114082399688\n\nRegulator = 0.0511114082399688\n\nThe rank and full Mordell-Weil basis have been determined unconditionally.\n (0.64004 seconds)\n```",
    "created_at": "2008-01-04T22:01:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1402#issuecomment-9022",
    "user": "https://trac.sagemath.org/admin/accounts/users/cartman"
}
```

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
and send problems to john.cremona@gmail.com.

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

archive/issue_comments_009023.json:
```json
{
    "body": "Closing against Sage 2.10.1 since the issue has been fixed an the latest eclib.spkg merged in Sage 2.10.1 or so.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T23:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1402#issuecomment-9023",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Closing against Sage 2.10.1 since the issue has been fixed an the latest eclib.spkg merged in Sage 2.10.1 or so.

Cheers,

Michael



---

archive/issue_events_003619.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-15T23:14:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1402",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1402#event-3619"
}
```



---

archive/issue_comments_009024.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-15T23:14:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1402",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1402#issuecomment-9024",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003620.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-15T23:14:21Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1402",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1402#event-3620"
}
```



---

archive/issue_events_003621.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-15T23:14:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1402",
    "milestone": "sage-2.10.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1402#event-3621"
}
```
