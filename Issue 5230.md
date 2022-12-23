# Issue 5230: implement boundary_style parameter for parametric 3d plots

archive/issues_005230.json:
```json
{
    "body": "Assignee: was\n\nBasically make it easy to create plots like this but in 1 line:\n\n```\nu, v = var('u,v')\nG = parametric_plot3d((cos(u), sin(u) + cos(v), sin(v)), (u, 0, pi), (v, 0, pi), opacity=0.9)    \nC = parametric_plot3d((cos(0), sin(0) + cos(v), sin(v)), (v, 0, pi), color='black', thickness=2)    \nD = parametric_plot3d((cos(pi), sin(pi) + cos(v), sin(v)), (v, 0, pi), color='black', thickness=2)\nE = parametric_plot3d((cos(u), sin(u) + cos(0), sin(0)), (u, 0, pi), color='black', thickness=2)    \nF = parametric_plot3d((cos(u), sin(u) + cos(pi), sin(pi)), (u, 0, pi), color='black', thickness=2)\nK = G + C + D + E + F\n```\n\n\nInput would probably be like this (dictionary):\n\n```\nu, v = var('u,v')\nparametric_plot3d((cos(u), sin(u) + cos(v), sin(v)), (u, 0, pi), (v, 0, pi),\n      boundary_style={'color':'black', 'thickness':2})    \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5230\n\n",
    "created_at": "2009-02-10T22:12:41Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "implement boundary_style parameter for parametric 3d plots",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5230",
    "user": "was"
}
```
Assignee: was

Basically make it easy to create plots like this but in 1 line:

```
u, v = var('u,v')
G = parametric_plot3d((cos(u), sin(u) + cos(v), sin(v)), (u, 0, pi), (v, 0, pi), opacity=0.9)    
C = parametric_plot3d((cos(0), sin(0) + cos(v), sin(v)), (v, 0, pi), color='black', thickness=2)    
D = parametric_plot3d((cos(pi), sin(pi) + cos(v), sin(v)), (v, 0, pi), color='black', thickness=2)
E = parametric_plot3d((cos(u), sin(u) + cos(0), sin(0)), (u, 0, pi), color='black', thickness=2)    
F = parametric_plot3d((cos(u), sin(u) + cos(pi), sin(pi)), (u, 0, pi), color='black', thickness=2)
K = G + C + D + E + F
```


Input would probably be like this (dictionary):

```
u, v = var('u,v')
parametric_plot3d((cos(u), sin(u) + cos(v), sin(v)), (u, 0, pi), (v, 0, pi),
      boundary_style={'color':'black', 'thickness':2})    
```


Issue created by migration from https://trac.sagemath.org/ticket/5230





---

archive/issue_comments_040084.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-12T00:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5230#issuecomment-40084",
    "user": "wcauchois"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040085.json:
```json
{
    "body": "Changing assignee from was to wcauchois.",
    "created_at": "2009-02-12T00:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5230#issuecomment-40085",
    "user": "wcauchois"
}
```

Changing assignee from was to wcauchois.



---

archive/issue_comments_040086.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-02-25T00:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5230#issuecomment-40086",
    "user": "wcauchois"
}
```

Attachment



---

archive/issue_comments_040087.json:
```json
{
    "body": "REFEREE REPORT:\n\nIt works perfectly. \n\n* Add to \"        boundary_style -- (default: None, no boundary) a dict that describes\n                         how to draw boundaries of regions\"\nthat the dict just gives the options that are passed to the line3d command.\n\n* Put a space after the doctest:\n\n```\n \t105\t        sage: parametric_plot3d((cos(u), sin(u) + cos(v), sin(v)), (u, 0, pi), (v, 0, pi), boundary_style={\"color\": \"black\", \"thickness\": 2}) \n \t106\t    Any options you would normally use to specify the appearance of a curve are valid \n \t107\t    as entries in the boundary_style dict. \n```\n\n\nI attached a patch that makes these trivial changes.  With this, positive review.\n\nNOTE: This patch will have to be rebased for 3.4.alpha because of the ReST transition.  It applies fine to 3.3 though.",
    "created_at": "2009-02-25T23:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5230#issuecomment-40087",
    "user": "was"
}
```

REFEREE REPORT:

It works perfectly. 

* Add to "        boundary_style -- (default: None, no boundary) a dict that describes
                         how to draw boundaries of regions"
that the dict just gives the options that are passed to the line3d command.

* Put a space after the doctest:

```
 	105	        sage: parametric_plot3d((cos(u), sin(u) + cos(v), sin(v)), (u, 0, pi), (v, 0, pi), boundary_style={"color": "black", "thickness": 2}) 
 	106	    Any options you would normally use to specify the appearance of a curve are valid 
 	107	    as entries in the boundary_style dict. 
```


I attached a patch that makes these trivial changes.  With this, positive review.

NOTE: This patch will have to be rebased for 3.4.alpha because of the ReST transition.  It applies fine to 3.3 though.



---

archive/issue_comments_040088.json:
```json
{
    "body": "Attachment\n\nThis needs to be rebased, as mentioned in the comment:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.4.alpha1/devel/sage$ patch -p1 < trac_5230_boundary-style.patch \npatching file sage/plot/plot3d/parametric_plot3d.py\nHunk #1 succeeded at 10 with fuzz 2 (offset 1 line).\nHunk #2 FAILED at 39.\nHunk #3 FAILED at 100.\nHunk #4 succeeded at 492 (offset 106 lines).\nHunk #5 succeeded at 537 with fuzz 2 (offset 107 lines).\nHunk #6 succeeded at 565 (offset 108 lines).\n```\n\n\nSo I am changing the summary properly so I won't find it out that way again :)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T19:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5230#issuecomment-40088",
    "user": "mabshoff"
}
```

Attachment

This needs to be rebased, as mentioned in the comment:

```
mabshoff@sage:/scratch/mabshoff/sage-3.4.alpha1/devel/sage$ patch -p1 < trac_5230_boundary-style.patch 
patching file sage/plot/plot3d/parametric_plot3d.py
Hunk #1 succeeded at 10 with fuzz 2 (offset 1 line).
Hunk #2 FAILED at 39.
Hunk #3 FAILED at 100.
Hunk #4 succeeded at 492 (offset 106 lines).
Hunk #5 succeeded at 537 with fuzz 2 (offset 107 lines).
Hunk #6 succeeded at 565 (offset 108 lines).
```


So I am changing the summary properly so I won't find it out that way again :)

Cheers,

Michael



---

archive/issue_comments_040089.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-07T17:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5230#issuecomment-40089",
    "user": "wcauchois"
}
```

Attachment



---

archive/issue_comments_040090.json:
```json
{
    "body": "Please apply ONLY trac5230-rebased.patch! It should apply fine to Sage 3.4 now.",
    "created_at": "2009-04-07T17:50:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5230#issuecomment-40090",
    "user": "wcauchois"
}
```

Please apply ONLY trac5230-rebased.patch! It should apply fine to Sage 3.4 now.



---

archive/issue_comments_040091.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-09T08:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5230#issuecomment-40091",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040092.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T08:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5230#issuecomment-40092",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc2.

Cheers,

Michael
