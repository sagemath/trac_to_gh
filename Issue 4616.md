# Issue 4616: cosine_series_coefficient hangs

archive/issues_004616.json:
```json
{
    "body": "Assignee: @wdjoyner\n\nThis is a method of the Piecewise class (which I use almost on a daily basis in teaching):\n\n\n```\nsage: f1 = lambda x: x*(pi-x)\nsage: f = Piecewise([[(0,pi),f1]])\nsage: f.cosine_series_coefficient(0,pi)\n                                               \n```\n\nRequires a ctl-c.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4616\n\n",
    "created_at": "2008-11-25T12:47:24Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "cosine_series_coefficient hangs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4616",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @wdjoyner

This is a method of the Piecewise class (which I use almost on a daily basis in teaching):


```
sage: f1 = lambda x: x*(pi-x)
sage: f = Piecewise([[(0,pi),f1]])
sage: f.cosine_series_coefficient(0,pi)
                                               
```

Requires a ctl-c.

Issue created by migration from https://trac.sagemath.org/ticket/4616





---

archive/issue_comments_034580.json:
```json
{
    "body": "I can confirm this problem on a box that has no problem with the Sage <-> Maxima communication (I was dubious initially since David has reported problems with Maxima for his recent Sage installs).\n\nCheers,\n\nMichael",
    "created_at": "2008-11-25T12:57:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4616#issuecomment-34580",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I can confirm this problem on a box that has no problem with the Sage <-> Maxima communication (I was dubious initially since David has reported problems with Maxima for his recent Sage installs).

Cheers,

Michael



---

archive/issue_comments_034581.json:
```json
{
    "body": "Does #4693 fix this bug?",
    "created_at": "2008-12-04T16:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4616#issuecomment-34581",
    "user": "https://github.com/wdjoyner"
}
```

Does #4693 fix this bug?



---

archive/issue_comments_034582.json:
```json
{
    "body": "Yes, #4693 fixes the bug:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: f1 = lambda x: x*(pi-x)\nsage: f = Piecewise([[(0,pi),f1]])\nsage: f.cosine_series_coefficient(0,pi)\npi^2/3\nsage: \nExiting SAGE (CPU time 0m0.17s, Wall time 2m3.53s).\nExiting spawned Maxima process.\n```\n\nDo you want to add a doctest so we can close this?\n| Sage Version 3.2.1, Release Date: 2008-12-01                       |\n| Type notebook() for the GUI, and license() for information.        |\nCheers,\n\nMichael",
    "created_at": "2008-12-04T17:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4616#issuecomment-34582",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yes, #4693 fixes the bug:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.2.alpha0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: f1 = lambda x: x*(pi-x)
sage: f = Piecewise([[(0,pi),f1]])
sage: f.cosine_series_coefficient(0,pi)
pi^2/3
sage: 
Exiting SAGE (CPU time 0m0.17s, Wall time 2m3.53s).
Exiting spawned Maxima process.
```

Do you want to add a doctest so we can close this?
| Sage Version 3.2.1, Release Date: 2008-12-01                       |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael



---

archive/issue_comments_034583.json:
```json
{
    "body": "I would but I still can't apply the patch for #4693:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: piecewise2\nsage: hg_sage.apply(\"/Volumes/G-DRIVE-MINI/sagestuff/trac_4693.2.patch\")\ncd \"/Volumes/G-DRIVE-MINI/sagestuff/sage-3.2.rc1/devel/sage\" && hg status\ncd \"/Volumes/G-DRIVE-MINI/sagestuff/sage-3.2.rc1/devel/sage\" && hg status\ncd \"/Volumes/G-DRIVE-MINI/sagestuff/sage-3.2.rc1/devel/sage\" && hg import   \"/Volumes/G-DRIVE-MINI/sagestuff/trac_4693.2.patch\"\napplying /Volumes/G-DRIVE-MINI/sagestuff/trac_4693.2.patch\npatching file sage/functions/piecewise.py\nHunk #25 FAILED at 717\n1 out of 44 hunks FAILED -- saving rejects to file sage/functions/piecewise.py.rej\nabort: patch failed to apply\nsage: \n```\n",
    "created_at": "2008-12-04T18:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4616#issuecomment-34583",
    "user": "https://github.com/wdjoyner"
}
```

I would but I still can't apply the patch for #4693:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: piecewise2
sage: hg_sage.apply("/Volumes/G-DRIVE-MINI/sagestuff/trac_4693.2.patch")
cd "/Volumes/G-DRIVE-MINI/sagestuff/sage-3.2.rc1/devel/sage" && hg status
cd "/Volumes/G-DRIVE-MINI/sagestuff/sage-3.2.rc1/devel/sage" && hg status
cd "/Volumes/G-DRIVE-MINI/sagestuff/sage-3.2.rc1/devel/sage" && hg import   "/Volumes/G-DRIVE-MINI/sagestuff/trac_4693.2.patch"
applying /Volumes/G-DRIVE-MINI/sagestuff/trac_4693.2.patch
patching file sage/functions/piecewise.py
Hunk #25 FAILED at 717
1 out of 44 hunks FAILED -- saving rejects to file sage/functions/piecewise.py.rej
abort: patch failed to apply
sage: 
```




---

archive/issue_comments_034584.json:
```json
{
    "body": "Attachment [trac-4616.patch](tarball://root/attachments/some-uuid/ticket4616/trac-4616.patch) by @rlmill created at 2009-01-22 17:27:50\n\nVerified that this is now fixed, attached a patch with a doctest.",
    "created_at": "2009-01-22T17:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4616#issuecomment-34584",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac-4616.patch](tarball://root/attachments/some-uuid/ticket4616/trac-4616.patch) by @rlmill created at 2009-01-22 17:27:50

Verified that this is now fixed, attached a patch with a doctest.



---

archive/issue_comments_034585.json:
```json
{
    "body": "I can read the docstring and check in Sage that it is correct. (I did not try to apply it though.)\n\n\n```\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: f1 = lambda x: x*(pi-x)\nsage: f = Piecewise([[(0,pi),f1]])\nsage: f.cosine_series_coefficient(0,pi)\npi^2/3\n| Sage Version 3.2.3, Release Date: 2009-01-05                       |\n| Type notebook() for the GUI, and license() for information.        |\n```\n\n\nHope this is sufficient for a positive review.",
    "created_at": "2009-01-22T17:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4616#issuecomment-34585",
    "user": "https://github.com/wdjoyner"
}
```

I can read the docstring and check in Sage that it is correct. (I did not try to apply it though.)


```

----------------------------------------------------------------------
----------------------------------------------------------------------
sage: f1 = lambda x: x*(pi-x)
sage: f = Piecewise([[(0,pi),f1]])
sage: f.cosine_series_coefficient(0,pi)
pi^2/3
| Sage Version 3.2.3, Release Date: 2009-01-05                       |
| Type notebook() for the GUI, and license() for information.        |
```


Hope this is sufficient for a positive review.



---

archive/issue_comments_034586.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T10:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4616#issuecomment-34586",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034587.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T10:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4616",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4616#issuecomment-34587",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1

Cheers,

Michael
