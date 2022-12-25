# Issue 5239: Sage 3.3.rc0: even more numerical noise in sage/sage/plot/plot.py

archive/issues_005239.json:
```json
{
    "body": "Assignee: mabshoff\n\nReported by David M. Monarres on OSX 10.5.6:\n\n```\nsage -t  \"devel/sage/sage/plot/plot.py\" \n********************************************************************** \nFile \"/Users/ayeq/sage-3.3.alpha5/devel/sage/sage/plot/plot.py\", line   \n2582: \n     sage: generate_plot_points(sin(x), (-pi, pi), randomize=False) \nExpected: \n     [(-3.1415926535897931, -1.2246...e-16), (-2.748893571891069, \n     -0.38268343236508989), (-2.3561944901923448, -0.707106781186547...), \n     (-2.1598449493429825, -0.831469612302545...), (-1.9634954084936207, \n     -0.92387953251128674), (-1.7671458676442586, -0.98078528040323043), \n     (-1.5707963267948966, -1.0), (-1.3744467859455345, \n     -0.98078528040323043), (-1.1780972450961724, -0.92387953251128674), \n     (-0.98174770424681035, -0.83146961230254524), (-0.78539816339744828, \n     -0.707106781186547...), (-0.39269908169872414, -0.38268343236508978), \n     (0.0, 0.0), (0.39269908169872414, 0.38268343236508978), \n     (0.78539816339744828, 0.707106781186547...), (0.98174770424681035, \n     0.83146961230254524), (1.1780972450961724, 0.92387953251128674), \n     (1.3744467859455345, 0.98078528040323043), (1.5707963267948966, 1.0), \n     (1.7671458676442586, 0.98078528040323043), (1.9634954084936207, \n     0.92387953251128674), (2.1598449493429825, 0.831469612302545...), \n     (2.3561944901923448, 0.707106781186547...), (2.748893571891069, \n     0.38268343236508989), (3.1415926535897931, 1.2246...e-16)] \nGot: \n     [(-3.1415926535897931, -1.2246467991473532e-16),   \n(-2.748893571891069, -0.38268343236508984), (-2.3561944901923448,   \n-0.70710678118654757), (-2.1598449493429825, -0.83146961230254546),   \n(-1.9634954084936207, -0.92387953251128674), (-1.7671458676442586,   \n-0.98078528040323043), (-1.5707963267948966, -1.0),   \n(-1.3744467859455345, -0.98078528040323043), (-1.1780972450961724,   \n-0.92387953251128674), (-0.98174770424681035, -0.83146961230254512),   \n(-0.78539816339744828, -0.70710678118654746), (-0.39269908169872414,   \n-0.38268343236508978), (0.0, 0.0), (0.39269908169872414,   \n0.38268343236508978), (0.78539816339744828, 0.70710678118654746),   \n(0.98174770424681035, 0.83146961230254512), (1.1780972450961724,   \n0.92387953251128674), (1.3744467859455345, 0.98078528040323043),   \n(1.5707963267948966, 1.0), (1.7671458676442586, 0.98078528040323043),   \n(1.9634954084936207, 0.92387953251128674), (2.1598449493429825,   \n0.83146961230254546), (2.3561944901923448, 0.70710678118654757),   \n(2.748893571891069, 0.38268343236508984), (3.1415926535897931,   \n1.2246467991473532e-16)] \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5239\n\n",
    "created_at": "2009-02-12T00:14:48Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Sage 3.3.rc0: even more numerical noise in sage/sage/plot/plot.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5239",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Reported by David M. Monarres on OSX 10.5.6:

```
sage -t  "devel/sage/sage/plot/plot.py" 
********************************************************************** 
File "/Users/ayeq/sage-3.3.alpha5/devel/sage/sage/plot/plot.py", line   
2582: 
     sage: generate_plot_points(sin(x), (-pi, pi), randomize=False) 
Expected: 
     [(-3.1415926535897931, -1.2246...e-16), (-2.748893571891069, 
     -0.38268343236508989), (-2.3561944901923448, -0.707106781186547...), 
     (-2.1598449493429825, -0.831469612302545...), (-1.9634954084936207, 
     -0.92387953251128674), (-1.7671458676442586, -0.98078528040323043), 
     (-1.5707963267948966, -1.0), (-1.3744467859455345, 
     -0.98078528040323043), (-1.1780972450961724, -0.92387953251128674), 
     (-0.98174770424681035, -0.83146961230254524), (-0.78539816339744828, 
     -0.707106781186547...), (-0.39269908169872414, -0.38268343236508978), 
     (0.0, 0.0), (0.39269908169872414, 0.38268343236508978), 
     (0.78539816339744828, 0.707106781186547...), (0.98174770424681035, 
     0.83146961230254524), (1.1780972450961724, 0.92387953251128674), 
     (1.3744467859455345, 0.98078528040323043), (1.5707963267948966, 1.0), 
     (1.7671458676442586, 0.98078528040323043), (1.9634954084936207, 
     0.92387953251128674), (2.1598449493429825, 0.831469612302545...), 
     (2.3561944901923448, 0.707106781186547...), (2.748893571891069, 
     0.38268343236508989), (3.1415926535897931, 1.2246...e-16)] 
Got: 
     [(-3.1415926535897931, -1.2246467991473532e-16),   
(-2.748893571891069, -0.38268343236508984), (-2.3561944901923448,   
-0.70710678118654757), (-2.1598449493429825, -0.83146961230254546),   
(-1.9634954084936207, -0.92387953251128674), (-1.7671458676442586,   
-0.98078528040323043), (-1.5707963267948966, -1.0),   
(-1.3744467859455345, -0.98078528040323043), (-1.1780972450961724,   
-0.92387953251128674), (-0.98174770424681035, -0.83146961230254512),   
(-0.78539816339744828, -0.70710678118654746), (-0.39269908169872414,   
-0.38268343236508978), (0.0, 0.0), (0.39269908169872414,   
0.38268343236508978), (0.78539816339744828, 0.70710678118654746),   
(0.98174770424681035, 0.83146961230254512), (1.1780972450961724,   
0.92387953251128674), (1.3744467859455345, 0.98078528040323043),   
(1.5707963267948966, 1.0), (1.7671458676442586, 0.98078528040323043),   
(1.9634954084936207, 0.92387953251128674), (2.1598449493429825,   
0.83146961230254546), (2.3561944901923448, 0.70710678118654757),   
(2.748893571891069, 0.38268343236508984), (3.1415926535897931,   
1.2246467991473532e-16)] 
```


Issue created by migration from https://trac.sagemath.org/ticket/5239





---

archive/issue_comments_040060.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-13T15:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5239#issuecomment-40060",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040061.json:
```json
{
    "body": "The problems seem to be the following:\n\n```\n    -0.38268343236508989), (-2.3561944901923448, -0.707106781186547...),\n    -0.38268343236508984), (-2.3561944901923448, -0.707106781186547   ), \n\n    (-0.98174770424681035, -0.83146961230254524), (-0.78539816339744828,\n    (-0.98174770424681035, -0.83146961230254512), (-0.78539816339744828, \n\n    0.83146961230254524), (1.1780972450961724, 0.92387953251128674),\n    0.83146961230254512), (1.1780972450961724, 0.92387953251128674), \n\n    0.38268343236508989), (3.1415926535897931, 1.2246...e-16)]\n    0.38268343236508984), (3.1415926535897931, 1.2246...e-16)]\n```\n\n\nPatch coming up.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-13T15:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5239#issuecomment-40061",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The problems seem to be the following:

```
    -0.38268343236508989), (-2.3561944901923448, -0.707106781186547...),
    -0.38268343236508984), (-2.3561944901923448, -0.707106781186547   ), 

    (-0.98174770424681035, -0.83146961230254524), (-0.78539816339744828,
    (-0.98174770424681035, -0.83146961230254512), (-0.78539816339744828, 

    0.83146961230254524), (1.1780972450961724, 0.92387953251128674),
    0.83146961230254512), (1.1780972450961724, 0.92387953251128674), 

    0.38268343236508989), (3.1415926535897931, 1.2246...e-16)]
    0.38268343236508984), (3.1415926535897931, 1.2246...e-16)]
```


Patch coming up.

Cheers,

Michael



---

archive/issue_comments_040062.json:
```json
{
    "body": "Attachment [trac_5239.patch](tarball://root/attachments/some-uuid/ticket5239/trac_5239.patch) by mabshoff created at 2009-02-14 09:46:04",
    "created_at": "2009-02-14T09:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5239#issuecomment-40062",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5239.patch](tarball://root/attachments/some-uuid/ticket5239/trac_5239.patch) by mabshoff created at 2009-02-14 09:46:04



---

archive/issue_comments_040063.json:
```json
{
    "body": "With the patch applied I get:\n\n```\nsage -t -long \"devel/sage/sage/plot/plot.py\"                \n\t [56.7 s]\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T09:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5239#issuecomment-40063",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With the patch applied I get:

```
sage -t -long "devel/sage/sage/plot/plot.py"                
	 [56.7 s]
```


Cheers,

Michael



---

archive/issue_comments_040064.json:
```json
{
    "body": "This patch looks trivial enough.  The changes look reasonable, and mabshoff ran the doctests, so positive review.\n\n\n```\n[04:09] <jason--> I got rejects on 5239\n[04:09] <mabs> Mhhh\n[04:10] <mabs> I build against rc0.\n[04:10] <jason--> yeah, I have a messed up rc0\n[04:10] <mabs> Well, I patched against rc0.\n[04:10] <mabs> Ok\n[04:10] <mabs> It works, trust me :)\n[04:10] <jason--> can I give this a \"I looked at it\" positive review?\n[04:10] <mabs> Yes, just don't tell anyone.\n[04:10] <mabs> :)\n[04:10] <jason--> okay, I'll whisper it very quietly on the ticket.\n[04:11] <jason--> (with this IRC log :)\n[04:11] <mabs> I do have the same OS, compiler and hardware as the reporter and I also took the report to produce the patch.\n[04:11] <mabs> And it does fix the issue on my box, so this is a pretty sure thing.\n```\n",
    "created_at": "2009-02-14T10:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5239#issuecomment-40064",
    "user": "https://github.com/jasongrout"
}
```

This patch looks trivial enough.  The changes look reasonable, and mabshoff ran the doctests, so positive review.


```
[04:09] <jason--> I got rejects on 5239
[04:09] <mabs> Mhhh
[04:10] <mabs> I build against rc0.
[04:10] <jason--> yeah, I have a messed up rc0
[04:10] <mabs> Well, I patched against rc0.
[04:10] <mabs> Ok
[04:10] <mabs> It works, trust me :)
[04:10] <jason--> can I give this a "I looked at it" positive review?
[04:10] <mabs> Yes, just don't tell anyone.
[04:10] <mabs> :)
[04:10] <jason--> okay, I'll whisper it very quietly on the ticket.
[04:11] <jason--> (with this IRC log :)
[04:11] <mabs> I do have the same OS, compiler and hardware as the reporter and I also took the report to produce the patch.
[04:11] <mabs> And it does fix the issue on my box, so this is a pretty sure thing.
```




---

archive/issue_events_005495.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-14T13:24:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5239",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5239#event-5495"
}
```



---

archive/issue_comments_040065.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-14T13:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5239#issuecomment-40065",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040066.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T13:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5239",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5239#issuecomment-40066",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael
