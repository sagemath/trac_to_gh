# Issue 1777: jmol up/down metaphor confusing in the "View" right-click menu

archive/issues_001777.json:
```json
{
    "body": "Assignee: @williamstein\n\nI noticed a potentially confusing thing in the totally awesome 3d \ngraphics we now have with jmol.\n\nsage: arrow3d((0,0,0),(1,1,1))\n\ndraws a very nice-looking 3d arrow in a bounding cube.  When I \nright-click on the graphic and choose \"View | front\", it swings the \nviewpoint around so that I'm looking at the *top* of the original cube \n(so that I'm looking in the direction of the negative z-axis).  I \nrealize that the standard computer graphics viewpoint has the z-axis \ncoming out of the monitor, so \"front\" is a valid label for this position \nin that sense, but it can be confusing to students who would have said \nthat what is labeled as the \"front\" position is actually showing the top \nof graph.  I imagine that it would be even more confusing to calc 3 \nstudents that the labeled \"top\" position is looking in the negative \ny-axis direction *with the positive z pointing down*.\n\nThe positions and actual viewing directions are thus:\n\n\"front\" = looking down negative z-axis, positive y-axis pointing up\n\"back\" = looking down positive z-axis, positive y-axis pointing up\n\n\"left\" = looking down positive x-axis, positive y-axis pointing up\n\"right\" = looking down negative x-axis, positive y-axis pointing up\n\n\"top\" = looking down negative y-axis, positive z-axis pointing *down*\n\"bottom\" = looking down positive y-axis, positive z-axis pointing up\n\nI think it would be less confusing if the View menu just listed viewing \ndirections instead of assigning a \"up\" and \"down\" metaphor that can \nchange depending on if you are doing math or doing computer science.\n\nJason\n\nIssue created by migration from https://trac.sagemath.org/ticket/1777\n\n",
    "created_at": "2008-01-14T17:55:53Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "jmol up/down metaphor confusing in the \"View\" right-click menu",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1777",
    "user": "@jasongrout"
}
```
Assignee: @williamstein

I noticed a potentially confusing thing in the totally awesome 3d 
graphics we now have with jmol.

sage: arrow3d((0,0,0),(1,1,1))

draws a very nice-looking 3d arrow in a bounding cube.  When I 
right-click on the graphic and choose "View | front", it swings the 
viewpoint around so that I'm looking at the *top* of the original cube 
(so that I'm looking in the direction of the negative z-axis).  I 
realize that the standard computer graphics viewpoint has the z-axis 
coming out of the monitor, so "front" is a valid label for this position 
in that sense, but it can be confusing to students who would have said 
that what is labeled as the "front" position is actually showing the top 
of graph.  I imagine that it would be even more confusing to calc 3 
students that the labeled "top" position is looking in the negative 
y-axis direction *with the positive z pointing down*.

The positions and actual viewing directions are thus:

"front" = looking down negative z-axis, positive y-axis pointing up
"back" = looking down positive z-axis, positive y-axis pointing up

"left" = looking down positive x-axis, positive y-axis pointing up
"right" = looking down negative x-axis, positive y-axis pointing up

"top" = looking down negative y-axis, positive z-axis pointing *down*
"bottom" = looking down positive y-axis, positive z-axis pointing up

I think it would be less confusing if the View menu just listed viewing 
directions instead of assigning a "up" and "down" metaphor that can 
change depending on if you are doing math or doing computer science.

Jason

Issue created by migration from https://trac.sagemath.org/ticket/1777





---

archive/issue_comments_011249.json:
```json
{
    "body": "See #2873 for how to fix this.",
    "created_at": "2008-07-24T22:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1777#issuecomment-11249",
    "user": "@jasongrout"
}
```

See #2873 for how to fix this.



---

archive/issue_comments_011250.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-14T10:04:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1777#issuecomment-11250",
    "user": "@jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011251.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2009-02-14T10:04:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1777#issuecomment-11251",
    "user": "@jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_011252.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-14T14:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1777#issuecomment-11252",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011253.json:
```json
{
    "body": "Fixed via #2873 in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T14:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1777#issuecomment-11253",
    "user": "mabshoff"
}
```

Fixed via #2873 in Sage 3.3.rc1.

Cheers,

Michael
