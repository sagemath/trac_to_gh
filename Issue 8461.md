# Issue 8461: Numerical noise in /sage/sage/plot/colors.py

archive/issues_008461.json:
```json
{
    "body": "Assignee: was\n\nCC:  kcrisman robertwb wcauchois\n\nRunning Solaris 10 on a SPARC, I get some numerical noise on this. Since these are RGB values. \n\n\n```\n**********************************************************************\nFile \"/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/plot/colors.py\", line 660:\n    sage: gold / pi + yellow * e\nExpected:\n    RGB color (0.51829585732141792, 0.49333037605210095, 0.0)\nGot:\n    RGB color (0.51829585732141814, 0.49333037605210117, 0.0)\n**********************************************************************\n```\n\n\nThe test makes use of 'e'. As has been shown on various other trac tickets (e.g. #8374, #8375), the value of 'e' returned by the SPARC processor is less accurate then the Intel/ADM chips. \n\nI'll attach a patch soon. \n\nDave \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8461\n\n",
    "created_at": "2010-03-06T22:23:54Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Numerical noise in /sage/sage/plot/colors.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8461",
    "user": "drkirkby"
}
```
Assignee: was

CC:  kcrisman robertwb wcauchois

Running Solaris 10 on a SPARC, I get some numerical noise on this. Since these are RGB values. 


```
**********************************************************************
File "/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/plot/colors.py", line 660:
    sage: gold / pi + yellow * e
Expected:
    RGB color (0.51829585732141792, 0.49333037605210095, 0.0)
Got:
    RGB color (0.51829585732141814, 0.49333037605210117, 0.0)
**********************************************************************
```


The test makes use of 'e'. As has been shown on various other trac tickets (e.g. #8374, #8375), the value of 'e' returned by the SPARC processor is less accurate then the Intel/ADM chips. 

I'll attach a patch soon. 

Dave 



Issue created by migration from https://trac.sagemath.org/ticket/8461





---

archive/issue_comments_076169.json:
```json
{
    "body": "This can be closed as a duplicate of #8462. It's better to do it this way, rather than close the later ticket, as that has a patch and more information attached. \n\ndave",
    "created_at": "2010-03-06T23:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8461#issuecomment-76169",
    "user": "drkirkby"
}
```

This can be closed as a duplicate of #8462. It's better to do it this way, rather than close the later ticket, as that has a patch and more information attached. 

dave



---

archive/issue_comments_076170.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-03-06T23:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8461#issuecomment-76170",
    "user": "mhansen"
}
```

Resolution: duplicate
