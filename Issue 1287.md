# Issue 1287: [with patch] wrappers for Dokchitser L-series

archive/issues_001287.json:
```json
{
    "body": "Assignee: was\n\nWrappers for Dokchitser L-series for various types of modular forms, e.g.,:\n\n\n```\n        sage: L = delta_Lseries()\n        sage: L(1)\n        0.0374412812685155\n\n        sage: f = CuspForms(2,8).0\n        sage: L = f.cuspform_Lseries()\n        sage: L(1)\n        0.0884317737041015\n        sage: L(0.5)\n        0.0296568512531983\n\n        sage: f = ModularForms(1,4).0\n        sage: L = f.modform_Lseries()\n        sage: L(1)\n        -0.0304484570583933\n\n        sage: L = eisenstein_series_Lseries(20)\n        sage: L(2)\n        -5.02355351645987 \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1287\n\n",
    "created_at": "2007-11-27T04:17:26Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with patch] wrappers for Dokchitser L-series",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1287",
    "user": "jen"
}
```
Assignee: was

Wrappers for Dokchitser L-series for various types of modular forms, e.g.,:


```
        sage: L = delta_Lseries()
        sage: L(1)
        0.0374412812685155

        sage: f = CuspForms(2,8).0
        sage: L = f.cuspform_Lseries()
        sage: L(1)
        0.0884317737041015
        sage: L(0.5)
        0.0296568512531983

        sage: f = ModularForms(1,4).0
        sage: L = f.modform_Lseries()
        sage: L(1)
        -0.0304484570583933

        sage: L = eisenstein_series_Lseries(20)
        sage: L(2)
        -5.02355351645987 
```


Issue created by migration from https://trac.sagemath.org/ticket/1287





---

archive/issue_comments_008082.json:
```json
{
    "body": "Attachment [patch.hg](tarball://root/attachments/some-uuid/ticket1287/patch.hg) by jen created at 2007-11-27 04:18:20",
    "created_at": "2007-11-27T04:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1287#issuecomment-8082",
    "user": "jen"
}
```

Attachment [patch.hg](tarball://root/attachments/some-uuid/ticket1287/patch.hg) by jen created at 2007-11-27 04:18:20



---

archive/issue_comments_008083.json:
```json
{
    "body": "Unfortunately there is a bug somewhere or some sort of mathematical contradiction going on here, as the following calculation illustrates:\n\n\n```\nsage: M = ModularSymbols(1,12)\nsage: d = M.cuspidal_submodule().rational_period_mapping()\nsage: for i in range(11):\n...      print i, d(M.modular_symbol((i, 0,oo)))\n0 (1620/691, 0)\n1 (0, 1)\n2 (-1, 0)\n3 (0, -25/48)\n4 (9/14, 0)\n5 (0, 5/12)\n6 (-9/14, 0)\n7 (0, -25/48)\n8 (1, 0)\n9 (0, 1)\n10 (-1620/691, 0)\nsage: L = eisenstein_series_Lseries(12)\nsage: L(3)\n2.89830333000000e-17\nsage: L(5)\n7.35601685000000e-17\n```\n\n\nThe modular symbols calculation verifies that L(i) for odd integers i=3,5, etc. is nonzero.  This also agrees with the Riemann Hypothesis for L(Delta, s).  However, for some strange reason the Dokchitser L that you're computing is 0 at some odd integers.  This means there is something wrong. \n\nI haven't figured out what yet.  I'll let Jen see if she can.\n\nThis can't go in sage as is though.",
    "created_at": "2007-12-02T06:35:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1287#issuecomment-8083",
    "user": "was"
}
```

Unfortunately there is a bug somewhere or some sort of mathematical contradiction going on here, as the following calculation illustrates:


```
sage: M = ModularSymbols(1,12)
sage: d = M.cuspidal_submodule().rational_period_mapping()
sage: for i in range(11):
...      print i, d(M.modular_symbol((i, 0,oo)))
0 (1620/691, 0)
1 (0, 1)
2 (-1, 0)
3 (0, -25/48)
4 (9/14, 0)
5 (0, 5/12)
6 (-9/14, 0)
7 (0, -25/48)
8 (1, 0)
9 (0, 1)
10 (-1620/691, 0)
sage: L = eisenstein_series_Lseries(12)
sage: L(3)
2.89830333000000e-17
sage: L(5)
7.35601685000000e-17
```


The modular symbols calculation verifies that L(i) for odd integers i=3,5, etc. is nonzero.  This also agrees with the Riemann Hypothesis for L(Delta, s).  However, for some strange reason the Dokchitser L that you're computing is 0 at some odd integers.  This means there is something wrong. 

I haven't figured out what yet.  I'll let Jen see if she can.

This can't go in sage as is though.



---

archive/issue_comments_008084.json:
```json
{
    "body": "*Doh* -- I was being stupid / confused between Eisenstein series and cusp form, since it was a long day.\n\nChange this to a positive review!",
    "created_at": "2007-12-02T18:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1287#issuecomment-8084",
    "user": "was"
}
```

*Doh* -- I was being stupid / confused between Eisenstein series and cusp form, since it was a long day.

Change this to a positive review!



---

archive/issue_comments_008085.json:
```json
{
    "body": "Merged in 2.8.15.rc0.",
    "created_at": "2007-12-02T19:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1287#issuecomment-8085",
    "user": "mabshoff"
}
```

Merged in 2.8.15.rc0.



---

archive/issue_comments_008086.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T19:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1287",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1287#issuecomment-8086",
    "user": "mabshoff"
}
```

Resolution: fixed
