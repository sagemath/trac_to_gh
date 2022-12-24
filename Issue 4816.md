# Issue 4816: Test failure in ell_rational_field.py

archive/issues_004816.json:
```json
{
    "body": "Assignee: tbd\n\nTesting in sage-3.2.2.rc0 yields a failure, below, (on Mac OS X, 10.5.5, on a Dual Quad Xeon).  To spoil the fun, there are two differences between \"Expected\" and \"Got\":\n\n\n```\nExpected:\n    ...\n    lambda 0.485997517468082\n    ...\n    k5,k6,k7 0.321154513240167 1.55246328915541 0.161999172489361\n```\n\n\n\n```\nGot:\n    ...\n    lambda 0.485997517468080\n    ...\n    k5,k6,k7 0.321154513240167 1.55246328915541 0.161999172489360\n```\n\n\nHere's the full failure:\n\n```\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\"\n**********************************************************************\nFile \"/Users/tmp/sage-3.2.2.alpha2/devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\", line 3248, in __main__.example_111\nFailed example:\n    a=E.S_integral_points(S=[Integer(2),Integer(3)], mw_base=[P1,P2,P3], verbose=True);a###line 4640:_sage_    >>> a=E.S_integral_points(S=[2,3], mw_base=[P1,P2,P3], verbose=True);a\nExpected:\n    max_S: 3 len_S: 3 len_tors: 1\n    lambda 0.485997517468082\n    k1,k2,k3,k4 6.68597129142710e234 1.31952866480763 3.31908110593519e9 2.42767548272846e17\n    mw_base [(1 : -1 : 1), (2 : 0 : 1), (0 : -3 : 1)]\n    mw_base_log [0.667789378224099, 0.552642660712417, 0.818477222895703]\n    mp [5, 7]\n    mw_base_p_log [[2^2 + 2^3 + 2^6 + 2^7 + 2^8 + 2^9 + 2^14 + 2^15 + 2^18 + 2^19 + O(2^20), 2^2 + 2^3 + 2^5 + 2^6 + 2^9 + 2^11 + 2^12 + 2^14 + 2^15 + 2^16 + 2^18 + O(2^20), 2 + 2^3 + 2^6 + 2^7 + 2^8 + 2^9 + 2^11 + 2^12 + 2^13 + 2^16 + 2^17 + 2^19 + O(2^20)], [2*3^2 + 2*3^5 + 2*3^6 + 2*3^7 + 3^8 + 3^9 + 2*3^10 + 3^12 + 2*3^14 + 3^15 + 3^17 + 2*3^19 + O(3^20), 2*3 + 2*3^2 + 2*3^3 + 2*3^4 + 2*3^6 + 2*3^7 + 2*3^8 + 3^10 + 2*3^12 + 3^13 + 2*3^14 + 3^15 + 3^18 + O(3^20), 3 + 3^2 + 2*3^3 + 3^6 + 2*3^7 + 2*3^8 + 3^9 + 2*3^11 + 2*3^12 + 2*3^13 + 3^15 + 2*3^16 + 3^18 + 2*3^19 + O(3^20)]]\n    k5,k6,k7 0.321154513240167 1.55246328915541 0.161999172489361\n    initial bound 2.62270974833657e117\n    bound_list [58, 58, 58]\n    bound_list [8, 9, 9]\n    bound_list [8, 7, 7]\n    bound_list [8, 7, 7]\n    starting search of points using coefficient bound  8\n    x-coords of S-integral points via linear combination of mw_base and torsion:\n    [-3, -26/9, -8159/2916, -2759/1024, -151/64, -1343/576, -2, -7/4, -1, -47/256, 0, 1/4, 4/9, 9/16, 58/81, 7/9, 6169/6561, 1, 17/16, 2, 33/16, 172/81, 9/4, 25/9, 3, 31/9, 4, 25/4, 1793/256, 8, 625/64, 11, 14, 21, 37, 52, 6142/81, 93, 4537/36, 342, 406, 816, 207331217/4096]\n    starting search of extra S-integer points with absolute value bounded by 3.89321964979420\n    x-coords of points with bounded absolute value\n    [-3, -2, -1, 0, 1, 2]\n    Total number of S-integral points: 43\n    [(-3 : 0 : 1), (-26/9 : 28/27 : 1), (-8159/2916 : 233461/157464 : 1), (-2759/1024 : 60819/32768 : 1), (-151/64 : 1333/512 : 1), (-1343/576 : 36575/13824 : 1), (-2 : 3 : 1), (-7/4 : 25/8 : 1), (-1 : 3 : 1), (-47/256 : 9191/4096 : 1), (0 : 2 : 1), (1/4 : 13/8 : 1), (4/9 : 35/27 : 1), (9/16 : 69/64 : 1), (58/81 : 559/729 : 1), (7/9 : 17/27 : 1), (6169/6561 : 109871/531441 : 1), (1 : 0 : 1), (17/16 : -25/64 : 1), (2 : 0 : 1), (33/16 : 17/64 : 1), (172/81 : 350/729 : 1), (9/4 : 7/8 : 1), (25/9 : 64/27 : 1), (3 : 3 : 1), (31/9 : 116/27 : 1), (4 : 6 : 1), (25/4 : 111/8 : 1), (1793/256 : 68991/4096 : 1), (8 : 21 : 1), (625/64 : 14839/512 : 1), (11 : 35 : 1), (14 : 51 : 1), (21 : 95 : 1), (37 : 224 : 1), (52 : 374 : 1), (6142/81 : 480700/729 : 1), (93 : 896 : 1), (4537/36 : 305425/216 : 1), (342 : 6324 : 1), (406 : 8180 : 1), (816 : 23309 : 1), (207331217/4096 : 2985362173625/262144 : 1)]\nGot:\n    max_S: 3 len_S: 3 len_tors: 1\n    lambda 0.485997517468080\n    k1,k2,k3,k4 6.68597129142710e234 1.31952866480763 3.31908110593519e9 2.42767548272846e17\n    mw_base [(1 : -1 : 1), (2 : 0 : 1), (0 : -3 : 1)]\n    mw_base_log [0.667789378224099, 0.552642660712417, 0.818477222895703]\n    mp [5, 7]\n    mw_base_p_log [[2^2 + 2^3 + 2^6 + 2^7 + 2^8 + 2^9 + 2^14 + 2^15 + 2^18 + 2^19 + O(2^20), 2^2 + 2^3 + 2^5 + 2^6 + 2^9 + 2^11 + 2^12 + 2^14 + 2^15 + 2^16 + 2^18 + O(2^20), 2 + 2^3 + 2^6 + 2^7 + 2^8 + 2^9 + 2^11 + 2^12 + 2^13 + 2^16 + 2^17 + 2^19 + O(2^20)], [2*3^2 + 2*3^5 + 2*3^6 + 2*3^7 + 3^8 + 3^9 + 2*3^10 + 3^12 + 2*3^14 + 3^15 + 3^17 + 2*3^19 + O(3^20), 2*3 + 2*3^2 + 2*3^3 + 2*3^4 + 2*3^6 + 2*3^7 + 2*3^8 + 3^10 + 2*3^12 + 3^13 + 2*3^14 + 3^15 + 3^18 + O(3^20), 3 + 3^2 + 2*3^3 + 3^6 + 2*3^7 + 2*3^8 + 3^9 + 2*3^11 + 2*3^12 + 2*3^13 + 3^15 + 2*3^16 + 3^18 + 2*3^19 + O(3^20)]]\n    k5,k6,k7 0.321154513240167 1.55246328915541 0.161999172489360\n    initial bound 2.62270974833657e117\n    bound_list [58, 58, 58]\n    bound_list [8, 9, 9]\n    bound_list [8, 7, 7]\n    bound_list [8, 7, 7]\n    starting search of points using coefficient bound  8\n    x-coords of S-integral points via linear combination of mw_base and torsion:\n    [-3, -26/9, -8159/2916, -2759/1024, -151/64, -1343/576, -2, -7/4, -1, -47/256, 0, 1/4, 4/9, 9/16, 58/81, 7/9, 6169/6561, 1, 17/16, 2, 33/16, 172/81, 9/4, 25/9, 3, 31/9, 4, 25/4, 1793/256, 8, 625/64, 11, 14, 21, 37, 52, 6142/81, 93, 4537/36, 342, 406, 816, 207331217/4096]\n    starting search of extra S-integer points with absolute value bounded by 3.89321964979420\n    x-coords of points with bounded absolute value\n    [-3, -2, -1, 0, 1, 2]\n    Total number of S-integral points: 43\n    [(-3 : 0 : 1), (-26/9 : 28/27 : 1), (-8159/2916 : 233461/157464 : 1), (-2759/1024 : 60819/32768 : 1), (-151/64 : 1333/512 : 1), (-1343/576 : 36575/13824 : 1), (-2 : 3 : 1), (-7/4 : 25/8 : 1), (-1 : 3 : 1), (-47/256 : 9191/4096 : 1), (0 : 2 : 1), (1/4 : 13/8 : 1), (4/9 : 35/27 : 1), (9/16 : 69/64 : 1), (58/81 : 559/729 : 1), (7/9 : 17/27 : 1), (6169/6561 : 109871/531441 : 1), (1 : 0 : 1), (17/16 : -25/64 : 1), (2 : 0 : 1), (33/16 : 17/64 : 1), (172/81 : 350/729 : 1), (9/4 : 7/8 : 1), (25/9 : 64/27 : 1), (3 : 3 : 1), (31/9 : 116/27 : 1), (4 : 6 : 1), (25/4 : 111/8 : 1), (1793/256 : 68991/4096 : 1), (8 : 21 : 1), (625/64 : 14839/512 : 1), (11 : 35 : 1), (14 : 51 : 1), (21 : 95 : 1), (37 : 224 : 1), (52 : 374 : 1), (6142/81 : 480700/729 : 1), (93 : 896 : 1), (4537/36 : 305425/216 : 1), (342 : 6324 : 1), (406 : 8180 : 1), (816 : 23309 : 1), (207331217/4096 : 2985362173625/262144 : 1)]\n**********************************************************************\n1 items had failures:\n   1 of   9 in __main__.example_111\n***Test Failed*** 1 failures.\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4816\n\n",
    "created_at": "2008-12-16T16:44:39Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "Test failure in ell_rational_field.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4816",
    "user": "justin"
}
```
Assignee: tbd

Testing in sage-3.2.2.rc0 yields a failure, below, (on Mac OS X, 10.5.5, on a Dual Quad Xeon).  To spoil the fun, there are two differences between "Expected" and "Got":


```
Expected:
    ...
    lambda 0.485997517468082
    ...
    k5,k6,k7 0.321154513240167 1.55246328915541 0.161999172489361
```



```
Got:
    ...
    lambda 0.485997517468080
    ...
    k5,k6,k7 0.321154513240167 1.55246328915541 0.161999172489360
```


Here's the full failure:

```
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
**********************************************************************
File "/Users/tmp/sage-3.2.2.alpha2/devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py", line 3248, in __main__.example_111
Failed example:
    a=E.S_integral_points(S=[Integer(2),Integer(3)], mw_base=[P1,P2,P3], verbose=True);a###line 4640:_sage_    >>> a=E.S_integral_points(S=[2,3], mw_base=[P1,P2,P3], verbose=True);a
Expected:
    max_S: 3 len_S: 3 len_tors: 1
    lambda 0.485997517468082
    k1,k2,k3,k4 6.68597129142710e234 1.31952866480763 3.31908110593519e9 2.42767548272846e17
    mw_base [(1 : -1 : 1), (2 : 0 : 1), (0 : -3 : 1)]
    mw_base_log [0.667789378224099, 0.552642660712417, 0.818477222895703]
    mp [5, 7]
    mw_base_p_log [[2^2 + 2^3 + 2^6 + 2^7 + 2^8 + 2^9 + 2^14 + 2^15 + 2^18 + 2^19 + O(2^20), 2^2 + 2^3 + 2^5 + 2^6 + 2^9 + 2^11 + 2^12 + 2^14 + 2^15 + 2^16 + 2^18 + O(2^20), 2 + 2^3 + 2^6 + 2^7 + 2^8 + 2^9 + 2^11 + 2^12 + 2^13 + 2^16 + 2^17 + 2^19 + O(2^20)], [2*3^2 + 2*3^5 + 2*3^6 + 2*3^7 + 3^8 + 3^9 + 2*3^10 + 3^12 + 2*3^14 + 3^15 + 3^17 + 2*3^19 + O(3^20), 2*3 + 2*3^2 + 2*3^3 + 2*3^4 + 2*3^6 + 2*3^7 + 2*3^8 + 3^10 + 2*3^12 + 3^13 + 2*3^14 + 3^15 + 3^18 + O(3^20), 3 + 3^2 + 2*3^3 + 3^6 + 2*3^7 + 2*3^8 + 3^9 + 2*3^11 + 2*3^12 + 2*3^13 + 3^15 + 2*3^16 + 3^18 + 2*3^19 + O(3^20)]]
    k5,k6,k7 0.321154513240167 1.55246328915541 0.161999172489361
    initial bound 2.62270974833657e117
    bound_list [58, 58, 58]
    bound_list [8, 9, 9]
    bound_list [8, 7, 7]
    bound_list [8, 7, 7]
    starting search of points using coefficient bound  8
    x-coords of S-integral points via linear combination of mw_base and torsion:
    [-3, -26/9, -8159/2916, -2759/1024, -151/64, -1343/576, -2, -7/4, -1, -47/256, 0, 1/4, 4/9, 9/16, 58/81, 7/9, 6169/6561, 1, 17/16, 2, 33/16, 172/81, 9/4, 25/9, 3, 31/9, 4, 25/4, 1793/256, 8, 625/64, 11, 14, 21, 37, 52, 6142/81, 93, 4537/36, 342, 406, 816, 207331217/4096]
    starting search of extra S-integer points with absolute value bounded by 3.89321964979420
    x-coords of points with bounded absolute value
    [-3, -2, -1, 0, 1, 2]
    Total number of S-integral points: 43
    [(-3 : 0 : 1), (-26/9 : 28/27 : 1), (-8159/2916 : 233461/157464 : 1), (-2759/1024 : 60819/32768 : 1), (-151/64 : 1333/512 : 1), (-1343/576 : 36575/13824 : 1), (-2 : 3 : 1), (-7/4 : 25/8 : 1), (-1 : 3 : 1), (-47/256 : 9191/4096 : 1), (0 : 2 : 1), (1/4 : 13/8 : 1), (4/9 : 35/27 : 1), (9/16 : 69/64 : 1), (58/81 : 559/729 : 1), (7/9 : 17/27 : 1), (6169/6561 : 109871/531441 : 1), (1 : 0 : 1), (17/16 : -25/64 : 1), (2 : 0 : 1), (33/16 : 17/64 : 1), (172/81 : 350/729 : 1), (9/4 : 7/8 : 1), (25/9 : 64/27 : 1), (3 : 3 : 1), (31/9 : 116/27 : 1), (4 : 6 : 1), (25/4 : 111/8 : 1), (1793/256 : 68991/4096 : 1), (8 : 21 : 1), (625/64 : 14839/512 : 1), (11 : 35 : 1), (14 : 51 : 1), (21 : 95 : 1), (37 : 224 : 1), (52 : 374 : 1), (6142/81 : 480700/729 : 1), (93 : 896 : 1), (4537/36 : 305425/216 : 1), (342 : 6324 : 1), (406 : 8180 : 1), (816 : 23309 : 1), (207331217/4096 : 2985362173625/262144 : 1)]
Got:
    max_S: 3 len_S: 3 len_tors: 1
    lambda 0.485997517468080
    k1,k2,k3,k4 6.68597129142710e234 1.31952866480763 3.31908110593519e9 2.42767548272846e17
    mw_base [(1 : -1 : 1), (2 : 0 : 1), (0 : -3 : 1)]
    mw_base_log [0.667789378224099, 0.552642660712417, 0.818477222895703]
    mp [5, 7]
    mw_base_p_log [[2^2 + 2^3 + 2^6 + 2^7 + 2^8 + 2^9 + 2^14 + 2^15 + 2^18 + 2^19 + O(2^20), 2^2 + 2^3 + 2^5 + 2^6 + 2^9 + 2^11 + 2^12 + 2^14 + 2^15 + 2^16 + 2^18 + O(2^20), 2 + 2^3 + 2^6 + 2^7 + 2^8 + 2^9 + 2^11 + 2^12 + 2^13 + 2^16 + 2^17 + 2^19 + O(2^20)], [2*3^2 + 2*3^5 + 2*3^6 + 2*3^7 + 3^8 + 3^9 + 2*3^10 + 3^12 + 2*3^14 + 3^15 + 3^17 + 2*3^19 + O(3^20), 2*3 + 2*3^2 + 2*3^3 + 2*3^4 + 2*3^6 + 2*3^7 + 2*3^8 + 3^10 + 2*3^12 + 3^13 + 2*3^14 + 3^15 + 3^18 + O(3^20), 3 + 3^2 + 2*3^3 + 3^6 + 2*3^7 + 2*3^8 + 3^9 + 2*3^11 + 2*3^12 + 2*3^13 + 3^15 + 2*3^16 + 3^18 + 2*3^19 + O(3^20)]]
    k5,k6,k7 0.321154513240167 1.55246328915541 0.161999172489360
    initial bound 2.62270974833657e117
    bound_list [58, 58, 58]
    bound_list [8, 9, 9]
    bound_list [8, 7, 7]
    bound_list [8, 7, 7]
    starting search of points using coefficient bound  8
    x-coords of S-integral points via linear combination of mw_base and torsion:
    [-3, -26/9, -8159/2916, -2759/1024, -151/64, -1343/576, -2, -7/4, -1, -47/256, 0, 1/4, 4/9, 9/16, 58/81, 7/9, 6169/6561, 1, 17/16, 2, 33/16, 172/81, 9/4, 25/9, 3, 31/9, 4, 25/4, 1793/256, 8, 625/64, 11, 14, 21, 37, 52, 6142/81, 93, 4537/36, 342, 406, 816, 207331217/4096]
    starting search of extra S-integer points with absolute value bounded by 3.89321964979420
    x-coords of points with bounded absolute value
    [-3, -2, -1, 0, 1, 2]
    Total number of S-integral points: 43
    [(-3 : 0 : 1), (-26/9 : 28/27 : 1), (-8159/2916 : 233461/157464 : 1), (-2759/1024 : 60819/32768 : 1), (-151/64 : 1333/512 : 1), (-1343/576 : 36575/13824 : 1), (-2 : 3 : 1), (-7/4 : 25/8 : 1), (-1 : 3 : 1), (-47/256 : 9191/4096 : 1), (0 : 2 : 1), (1/4 : 13/8 : 1), (4/9 : 35/27 : 1), (9/16 : 69/64 : 1), (58/81 : 559/729 : 1), (7/9 : 17/27 : 1), (6169/6561 : 109871/531441 : 1), (1 : 0 : 1), (17/16 : -25/64 : 1), (2 : 0 : 1), (33/16 : 17/64 : 1), (172/81 : 350/729 : 1), (9/4 : 7/8 : 1), (25/9 : 64/27 : 1), (3 : 3 : 1), (31/9 : 116/27 : 1), (4 : 6 : 1), (25/4 : 111/8 : 1), (1793/256 : 68991/4096 : 1), (8 : 21 : 1), (625/64 : 14839/512 : 1), (11 : 35 : 1), (14 : 51 : 1), (21 : 95 : 1), (37 : 224 : 1), (52 : 374 : 1), (6142/81 : 480700/729 : 1), (93 : 896 : 1), (4537/36 : 305425/216 : 1), (342 : 6324 : 1), (406 : 8180 : 1), (816 : 23309 : 1), (207331217/4096 : 2985362173625/262144 : 1)]
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_111
***Test Failed*** 1 failures.
```




Issue created by migration from https://trac.sagemath.org/ticket/4816





---

archive/issue_comments_036512.json:
```json
{
    "body": "I'll put up a patch for this in a minute.",
    "created_at": "2008-12-16T16:50:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4816#issuecomment-36512",
    "user": "cremona"
}
```

I'll put up a patch for this in a minute.



---

archive/issue_comments_036513.json:
```json
{
    "body": "Attachment [trac-4816.patch](tarball://root/attachments/some-uuid/ticket4816/trac-4816.patch) by cremona created at 2008-12-16 17:00:11",
    "created_at": "2008-12-16T17:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4816#issuecomment-36513",
    "user": "cremona"
}
```

Attachment [trac-4816.patch](tarball://root/attachments/some-uuid/ticket4816/trac-4816.patch) by cremona created at 2008-12-16 17:00:11



---

archive/issue_comments_036514.json:
```json
{
    "body": "Patch attached which puts some ... at the end of the offending reals.  Based on 3.2.2.rc0.  Tested ok on 32-bit Suse.\n\nBUT when I made a clone of my fresh 64-bit build  (./sage -clone 4816 i nthe build directory) I found that I could not run sage (./sage quit with errors:\n\n```\nSyntaxError: Non-ASCII character '\\xc3' in file /home/jec/sage-3.2.2.rc0/local/lib/python2.5/site-packages/sage/combinat/ranker.py on line 3, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details (ranker.py, line 3)\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n```\n\nwhich looks like something else entirely!",
    "created_at": "2008-12-16T17:02:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4816#issuecomment-36514",
    "user": "cremona"
}
```

Patch attached which puts some ... at the end of the offending reals.  Based on 3.2.2.rc0.  Tested ok on 32-bit Suse.

BUT when I made a clone of my fresh 64-bit build  (./sage -clone 4816 i nthe build directory) I found that I could not run sage (./sage quit with errors:

```
SyntaxError: Non-ASCII character '\xc3' in file /home/jec/sage-3.2.2.rc0/local/lib/python2.5/site-packages/sage/combinat/ranker.py on line 3, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details (ranker.py, line 3)
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```

which looks like something else entirely!



---

archive/issue_comments_036515.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-12-16T18:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4816#issuecomment-36515",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_036516.json:
```json
{
    "body": "Changing component from algebra to doctest.",
    "created_at": "2008-12-16T18:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4816#issuecomment-36516",
    "user": "mabshoff"
}
```

Changing component from algebra to doctest.



---

archive/issue_comments_036517.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2008-12-16T18:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4816#issuecomment-36517",
    "user": "mabshoff"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_036518.json:
```json
{
    "body": "I am seeing the same numerical failure on an Itanium box:\n\n```\n<     lambda 0.485997517468082\n---\n>     lambda 0.485997517468080\n---\n<     k5,k6,k7 0.321154513240167 1.55246328915541 0.161999172489361\n---\n>     k5,k6,k7 0.321154513240167 1.55246328915541 0.161999172489360\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-12-16T18:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4816#issuecomment-36518",
    "user": "mabshoff"
}
```

I am seeing the same numerical failure on an Itanium box:

```
<     lambda 0.485997517468082
---
>     lambda 0.485997517468080
---
<     k5,k6,k7 0.321154513240167 1.55246328915541 0.161999172489361
---
>     k5,k6,k7 0.321154513240167 1.55246328915541 0.161999172489360
```


Cheers,

Michael



---

archive/issue_comments_036519.json:
```json
{
    "body": "Replying to [comment:3 mabshoff]:\n> I am seeing the same numerical failure on an Itanium box:\n\nBefore or after my patch?\n\nJohn\n\n> {{{\n> <     lambda 0.485997517468082\n> ---\n> >     lambda 0.485997517468080\n> ---\n> <     k5,k6,k7 0.321154513240167 1.55246328915541 0.161999172489361\n> ---\n> >     k5,k6,k7 0.321154513240167 1.55246328915541 0.161999172489360\n> }}}\n> \n> Cheers,\n> \n> Michael",
    "created_at": "2008-12-16T18:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4816#issuecomment-36519",
    "user": "cremona"
}
```

Replying to [comment:3 mabshoff]:
> I am seeing the same numerical failure on an Itanium box:

Before or after my patch?

John

> {{{
> <     lambda 0.485997517468082
> ---
> >     lambda 0.485997517468080
> ---
> <     k5,k6,k7 0.321154513240167 1.55246328915541 0.161999172489361
> ---
> >     k5,k6,k7 0.321154513240167 1.55246328915541 0.161999172489360
> }}}
> 
> Cheers,
> 
> Michael



---

archive/issue_comments_036520.json:
```json
{
    "body": "Before. With the patch:\n\n```\nsage -t -long \"devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\"\n         [403.0 s]\n```\n\n\nSo positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-16T18:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4816#issuecomment-36520",
    "user": "mabshoff"
}
```

Before. With the patch:

```
sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
         [403.0 s]
```


So positive review.

Cheers,

Michael



---

archive/issue_comments_036521.json:
```json
{
    "body": "Merged in Sage 3.2.2.rc1",
    "created_at": "2008-12-17T14:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4816#issuecomment-36521",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.rc1



---

archive/issue_comments_036522.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-17T14:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4816#issuecomment-36522",
    "user": "mabshoff"
}
```

Resolution: fixed
