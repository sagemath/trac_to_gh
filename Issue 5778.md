# Issue 5778: More p-adic doctests

archive/issues_005778.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: doctests\n\nI've added some doctests, and improved ReST compatibility.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5778\n\n",
    "created_at": "2009-04-13T17:44:04Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "More p-adic doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5778",
    "user": "https://github.com/roed314"
}
```
Assignee: @williamstein

Keywords: doctests

I've added some doctests, and improved ReST compatibility.

Issue created by migration from https://trac.sagemath.org/ticket/5778





---

archive/issue_comments_045103.json:
```json
{
    "body": "Hi David,\n\nThis patch fails to apply to my 3.4.1.rc2:\n\n\n```\napplying padic_doctests.patch\npatching file sage/rings/padics/factory.py\nHunk #1 FAILED at 291\nHunk #2 FAILED at 358\nHunk #3 FAILED at 483\nHunk #4 FAILED at 518\nHunk #5 FAILED at 529\nHunk #6 FAILED at 787\nHunk #7 FAILED at 805\nHunk #8 FAILED at 820\nHunk #9 FAILED at 829\nHunk #10 FAILED at 1141\nHunk #11 FAILED at 1207\nHunk #12 FAILED at 1679\nHunk #13 FAILED at 1705\nHunk #14 FAILED at 1714\nHunk #15 FAILED at 1723\nHunk #16 FAILED at 1732\nHunk #17 FAILED at 1744\nHunk #18 succeeded at 525 with fuzz 2 (offset -1295 lines).\nHunk #19 succeeded at 570 with fuzz 2 (offset -1300 lines).\nHunk #20 FAILED at 1879\nHunk #21 succeeded at 582 with fuzz 1 (offset -1307 lines).\n18 out of 23 hunks FAILED -- saving rejects to file sage/rings/padics/factory.py.rej\npatching file sage/rings/padics/padic_ZZ_pX_CA_element.pyx\nHunk #39 FAILED at 1625\n1 out of 45 hunks FAILED -- saving rejects to file sage/rings/padics/padic_ZZ_pX_CA_element.pyx.rej\npatching file sage/rings/padics/padic_printing.pyx\nHunk #1 FAILED at 19\nHunk #9 FAILED at 228\nHunk #10 FAILED at 303\nHunk #11 FAILED at 385\nHunk #13 FAILED at 519\nHunk #15 FAILED at 562\nHunk #16 succeeded at 556 with fuzz 2 (offset -107 lines).\nHunk #20 FAILED at 894\nHunk #21 FAILED at 923\nHunk #22 FAILED at 975\nHunk #23 succeeded at 797 with fuzz 1 (offset -197 lines).\n9 out of 24 hunks FAILED -- saving rejects to file sage/rings/padics/padic_printing.pyx.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh padic_doctests.patch\n```\n\n\nI'll try to take a look and see what's going on, but it might take a while.",
    "created_at": "2009-04-15T00:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45103",
    "user": "https://github.com/aghitza"
}
```

Hi David,

This patch fails to apply to my 3.4.1.rc2:


```
applying padic_doctests.patch
patching file sage/rings/padics/factory.py
Hunk #1 FAILED at 291
Hunk #2 FAILED at 358
Hunk #3 FAILED at 483
Hunk #4 FAILED at 518
Hunk #5 FAILED at 529
Hunk #6 FAILED at 787
Hunk #7 FAILED at 805
Hunk #8 FAILED at 820
Hunk #9 FAILED at 829
Hunk #10 FAILED at 1141
Hunk #11 FAILED at 1207
Hunk #12 FAILED at 1679
Hunk #13 FAILED at 1705
Hunk #14 FAILED at 1714
Hunk #15 FAILED at 1723
Hunk #16 FAILED at 1732
Hunk #17 FAILED at 1744
Hunk #18 succeeded at 525 with fuzz 2 (offset -1295 lines).
Hunk #19 succeeded at 570 with fuzz 2 (offset -1300 lines).
Hunk #20 FAILED at 1879
Hunk #21 succeeded at 582 with fuzz 1 (offset -1307 lines).
18 out of 23 hunks FAILED -- saving rejects to file sage/rings/padics/factory.py.rej
patching file sage/rings/padics/padic_ZZ_pX_CA_element.pyx
Hunk #39 FAILED at 1625
1 out of 45 hunks FAILED -- saving rejects to file sage/rings/padics/padic_ZZ_pX_CA_element.pyx.rej
patching file sage/rings/padics/padic_printing.pyx
Hunk #1 FAILED at 19
Hunk #9 FAILED at 228
Hunk #10 FAILED at 303
Hunk #11 FAILED at 385
Hunk #13 FAILED at 519
Hunk #15 FAILED at 562
Hunk #16 succeeded at 556 with fuzz 2 (offset -107 lines).
Hunk #20 FAILED at 894
Hunk #21 FAILED at 923
Hunk #22 FAILED at 975
Hunk #23 succeeded at 797 with fuzz 1 (offset -197 lines).
9 out of 24 hunks FAILED -- saving rejects to file sage/rings/padics/padic_printing.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh padic_doctests.patch
```


I'll try to take a look and see what's going on, but it might take a while.



---

archive/issue_comments_045104.json:
```json
{
    "body": "This patch does not import particularly well:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.4.1.rc3/devel/sage$ hg import padic_doctests.patch \napplying padic_doctests.patch\npatching file sage/rings/padics/factory.py\nHunk #1 FAILED at 291\nHunk #2 FAILED at 358\nHunk #3 FAILED at 483\nHunk #4 FAILED at 518\nHunk #5 FAILED at 529\nHunk #6 FAILED at 787\nHunk #7 FAILED at 805\nHunk #8 FAILED at 820\nHunk #9 FAILED at 829\nHunk #10 FAILED at 1141\nHunk #11 FAILED at 1207\nHunk #12 FAILED at 1679\nHunk #13 FAILED at 1705\nHunk #14 FAILED at 1714\nHunk #15 FAILED at 1723\nHunk #16 FAILED at 1732\nHunk #17 FAILED at 1744\nHunk #18 succeeded at 525 with fuzz 2 (offset -1295 lines).\nHunk #19 succeeded at 570 with fuzz 2 (offset -1300 lines).\nHunk #20 FAILED at 1879\nHunk #21 succeeded at 582 with fuzz 1 (offset -1307 lines).\n18 out of 23 hunks FAILED -- saving rejects to file sage/rings/padics/factory.py.rej\npatching file sage/rings/padics/padic_ZZ_pX_CA_element.pyx\nHunk #39 FAILED at 1625\n1 out of 45 hunks FAILED -- saving rejects to file sage/rings/padics/padic_ZZ_pX_CA_element.pyx.rej\npatching file sage/rings/padics/padic_printing.pyx\nHunk #1 FAILED at 19\nHunk #9 FAILED at 228\nHunk #10 FAILED at 303\nHunk #11 FAILED at 385\nHunk #13 FAILED at 519\nHunk #15 FAILED at 562\nHunk #16 succeeded at 556 with fuzz 2 (offset -107 lines).\nHunk #20 FAILED at 894\nHunk #21 FAILED at 923\nHunk #22 FAILED at 975\nHunk #23 succeeded at 797 with fuzz 1 (offset -197 lines).\n9 out of 24 hunks FAILED -- saving rejects to file sage/rings/padics/padic_printing.pyx.rej\nabort: patch failed to apply\n```\n\n\nI am not sure if there is a missing dependency. \n\nDavid: any ideas?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T01:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45104",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch does not import particularly well:

```
mabshoff@sage:/scratch/mabshoff/sage-3.4.1.rc3/devel/sage$ hg import padic_doctests.patch 
applying padic_doctests.patch
patching file sage/rings/padics/factory.py
Hunk #1 FAILED at 291
Hunk #2 FAILED at 358
Hunk #3 FAILED at 483
Hunk #4 FAILED at 518
Hunk #5 FAILED at 529
Hunk #6 FAILED at 787
Hunk #7 FAILED at 805
Hunk #8 FAILED at 820
Hunk #9 FAILED at 829
Hunk #10 FAILED at 1141
Hunk #11 FAILED at 1207
Hunk #12 FAILED at 1679
Hunk #13 FAILED at 1705
Hunk #14 FAILED at 1714
Hunk #15 FAILED at 1723
Hunk #16 FAILED at 1732
Hunk #17 FAILED at 1744
Hunk #18 succeeded at 525 with fuzz 2 (offset -1295 lines).
Hunk #19 succeeded at 570 with fuzz 2 (offset -1300 lines).
Hunk #20 FAILED at 1879
Hunk #21 succeeded at 582 with fuzz 1 (offset -1307 lines).
18 out of 23 hunks FAILED -- saving rejects to file sage/rings/padics/factory.py.rej
patching file sage/rings/padics/padic_ZZ_pX_CA_element.pyx
Hunk #39 FAILED at 1625
1 out of 45 hunks FAILED -- saving rejects to file sage/rings/padics/padic_ZZ_pX_CA_element.pyx.rej
patching file sage/rings/padics/padic_printing.pyx
Hunk #1 FAILED at 19
Hunk #9 FAILED at 228
Hunk #10 FAILED at 303
Hunk #11 FAILED at 385
Hunk #13 FAILED at 519
Hunk #15 FAILED at 562
Hunk #16 succeeded at 556 with fuzz 2 (offset -107 lines).
Hunk #20 FAILED at 894
Hunk #21 FAILED at 923
Hunk #22 FAILED at 975
Hunk #23 succeeded at 797 with fuzz 1 (offset -197 lines).
9 out of 24 hunks FAILED -- saving rejects to file sage/rings/padics/padic_printing.pyx.rej
abort: patch failed to apply
```


I am not sure if there is a missing dependency. 

David: any ideas?

Cheers,

Michael



---

archive/issue_comments_045105.json:
```json
{
    "body": "Oops, for whatever reason I did not have #4637 in my tree - so apologies.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T02:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45105",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oops, for whatever reason I did not have #4637 in my tree - so apologies.

Cheers,

Michael



---

archive/issue_comments_045106.json:
```json
{
    "body": "Ok, with this patch applied:\n\n```\nsage-3.4.1.rc3/devel/sage$ patch -p1 < padic_doctests.patch \npatching file sage/rings/padics/factory.py\npatching file sage/rings/padics/padic_ZZ_pX_CA_element.pyx\npatching file sage/rings/padics/padic_ZZ_pX_CR_element.pyx\npatching file sage/rings/padics/padic_ZZ_pX_FM_element.pyx\npatching file sage/rings/padics/padic_capped_absolute_element.pyx\npatching file sage/rings/padics/padic_capped_relative_element.pxd\npatching file sage/rings/padics/padic_capped_relative_element.pyx\npatching file sage/rings/padics/padic_ext_element.pxd\npatching file sage/rings/padics/padic_ext_element.pyx\npatching file sage/rings/padics/padic_fixed_mod_element.pyx\npatching file sage/rings/padics/padic_generic.py\npatching file sage/rings/padics/padic_generic_element.pyx\npatching file sage/rings/padics/padic_printing.pyx\npatching file sage/rings/padics/pow_computer.pyx\npatching file sage/rings/padics/pow_computer_ext.pyx\n```\n\nWe also get:\n\n```\nOverall weighted coverage score:  38.2%\nTotal number of functions:  840\nWe need  250 more function to get to 68% coverage.\nWe need  267 more function to get to 70% coverage.\nWe need  309 more function to get to 75% coverage.\n```\n\nfor the padics directory **only**.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T02:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45106",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, with this patch applied:

```
sage-3.4.1.rc3/devel/sage$ patch -p1 < padic_doctests.patch 
patching file sage/rings/padics/factory.py
patching file sage/rings/padics/padic_ZZ_pX_CA_element.pyx
patching file sage/rings/padics/padic_ZZ_pX_CR_element.pyx
patching file sage/rings/padics/padic_ZZ_pX_FM_element.pyx
patching file sage/rings/padics/padic_capped_absolute_element.pyx
patching file sage/rings/padics/padic_capped_relative_element.pxd
patching file sage/rings/padics/padic_capped_relative_element.pyx
patching file sage/rings/padics/padic_ext_element.pxd
patching file sage/rings/padics/padic_ext_element.pyx
patching file sage/rings/padics/padic_fixed_mod_element.pyx
patching file sage/rings/padics/padic_generic.py
patching file sage/rings/padics/padic_generic_element.pyx
patching file sage/rings/padics/padic_printing.pyx
patching file sage/rings/padics/pow_computer.pyx
patching file sage/rings/padics/pow_computer_ext.pyx
```

We also get:

```
Overall weighted coverage score:  38.2%
Total number of functions:  840
We need  250 more function to get to 68% coverage.
We need  267 more function to get to 70% coverage.
We need  309 more function to get to 75% coverage.
```

for the padics directory **only**.

Cheers,

Michael



---

archive/issue_comments_045107.json:
```json
{
    "body": "There are some slight doctesting failures:\n\n```\nThe following tests failed:\n\nsage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # 3 doctests failed\nsage -t -long devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 2 doctests failed\nsage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 2 doctests failed\nsage -t -long devel/sage/sage/schemes/elliptic_curves/ell_tate_curve.py # 4 doctests failed\nsage -t -long devel/sage/sage/rings/padics/factory.py # 2 doctests failed\nsage -t -long devel/sage/sage/rings/padics/padic_capped_relative_element.pyx # 1 doctests failed\n```\n\n\nCheers,\n\nMicheal",
    "created_at": "2009-04-15T02:49:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45107",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There are some slight doctesting failures:

```
The following tests failed:

sage -t -long devel/sage/sage/schemes/elliptic_curves/padics.py # 3 doctests failed
sage -t -long devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 2 doctests failed
sage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 2 doctests failed
sage -t -long devel/sage/sage/schemes/elliptic_curves/ell_tate_curve.py # 4 doctests failed
sage -t -long devel/sage/sage/rings/padics/factory.py # 2 doctests failed
sage -t -long devel/sage/sage/rings/padics/padic_capped_relative_element.pyx # 1 doctests failed
```


Cheers,

Micheal



---

archive/issue_comments_045108.json:
```json
{
    "body": "Bouncing it to 3.4.2 - if the patch is updated, passes doctests and is reviewed there might be a chance to get this into 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-15T06:58:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45108",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Bouncing it to 3.4.2 - if the patch is updated, passes doctests and is reviewed there might be a chance to get this into 3.4.1.

Cheers,

Michael



---

archive/issue_comments_045109.json:
```json
{
    "body": "Looks much better. One trivial hashing issue (32 vs. 64 bit) needs to be fixed:\n\n```\nsage -t -long \"devel/sage/sage/rings/padics/padic_capped_relative_element.pyx\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.rc4/devel/sage/sage/rings/padics/padic_capped_relative_element.pyx\", line 2357:\n    sage: hash(R(-1))\nExpected:\n    1977822444\nGot:\n    95367431640624\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T03:56:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45109",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Looks much better. One trivial hashing issue (32 vs. 64 bit) needs to be fixed:

```
sage -t -long "devel/sage/sage/rings/padics/padic_capped_relative_element.pyx"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc4/devel/sage/sage/rings/padics/padic_capped_relative_element.pyx", line 2357:
    sage: hash(R(-1))
Expected:
    1977822444
Got:
    95367431640624
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_045110.json:
```json
{
    "body": "Michael,  are you actually reviewing this or just making sure that it applies and passes tests before it can be reviewed?  John",
    "created_at": "2009-04-18T16:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45110",
    "user": "https://github.com/JohnCremona"
}
```

Michael,  are you actually reviewing this or just making sure that it applies and passes tests before it can be reviewed?  John



---

archive/issue_comments_045111.json:
```json
{
    "body": "Replying to [comment:10 cremona]:\n\nHi John,\n\n> Michael,  are you actually reviewing this or just making sure that it applies and passes tests before it can be reviewed?  John\n\nI am not reviewing this since I don't feel qualified, I just made sure that the patch applied and passes doctests.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T16:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45111",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:10 cremona]:

Hi John,

> Michael,  are you actually reviewing this or just making sure that it applies and passes tests before it can be reviewed?  John

I am not reviewing this since I don't feel qualified, I just made sure that the patch applied and passes doctests.

Cheers,

Michael



---

archive/issue_comments_045112.json:
```json
{
    "body": "Replying to [comment:11 mabshoff]:\n\n> I am not reviewing this since I don't feel qualified, I just made sure that the patch applied and passes doctests.\n\nThat's what I thought.  I'll take a look.  John",
    "created_at": "2009-04-18T16:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45112",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:11 mabshoff]:

> I am not reviewing this since I don't feel qualified, I just made sure that the patch applied and passes doctests.

That's what I thought.  I'll take a look.  John



---

archive/issue_comments_045113.json:
```json
{
    "body": "The patch applies and tests pass.\n\nAs I cannot view the patch (it is too big) I don't actually know what has changed.  Apparently the files have been restified, but the only way to test that would be to add them to the reference manual and try building.  I started with factory.py as that seemed pretty important.  I found that the file while partially restified on a superficial level was completely broken as far as actually processing it is concerned.  I started correcting it and got to line 430, but it is 2200 lines long and so will take a lot longer.\n\nI suggest that this patch goes in since it is a step in the right direction;  but I don't promise to even get to the end of properly getting the docs for factory.py into the manual, let alone any of the rest (ha ha ) of it.\n\nOn the positive side I not the very comprhjensive explanation of the p-adic code in a separate tutorial file which is in the reference manual;  but I think that we do need the individual files (of which there are a large number) in there too.",
    "created_at": "2009-04-18T20:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45113",
    "user": "https://github.com/JohnCremona"
}
```

The patch applies and tests pass.

As I cannot view the patch (it is too big) I don't actually know what has changed.  Apparently the files have been restified, but the only way to test that would be to add them to the reference manual and try building.  I started with factory.py as that seemed pretty important.  I found that the file while partially restified on a superficial level was completely broken as far as actually processing it is concerned.  I started correcting it and got to line 430, but it is 2200 lines long and so will take a lot longer.

I suggest that this patch goes in since it is a step in the right direction;  but I don't promise to even get to the end of properly getting the docs for factory.py into the manual, let alone any of the rest (ha ha ) of it.

On the positive side I not the very comprhjensive explanation of the p-adic code in a separate tutorial file which is in the reference manual;  but I think that we do need the individual files (of which there are a large number) in there too.



---

archive/issue_comments_045114.json:
```json
{
    "body": "The patch is not ready to be build with ReST, David just started changing the doctests as a step in the right direction. About 2/3 of the patch are indentation changes, the other 1/3 adds new doctests. I have taken a look a the patch via a local diff viewer since as you point out the patch is too large for trac. \n\nGiven your reservations I would like someone else to take another look, so I am setting this to \"needs review\" again. \n\nDavid is also working on subsequent patches to add more doctests and his eventual goal here is to get all of padics 100% tested and in the reference manual. It might be a good idea to stay below 256kb/patch in the future ;)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T22:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45114",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch is not ready to be build with ReST, David just started changing the doctests as a step in the right direction. About 2/3 of the patch are indentation changes, the other 1/3 adds new doctests. I have taken a look a the patch via a local diff viewer since as you point out the patch is too large for trac. 

Given your reservations I would like someone else to take another look, so I am setting this to "needs review" again. 

David is also working on subsequent patches to add more doctests and his eventual goal here is to get all of padics 100% tested and in the reference manual. It might be a good idea to stay below 256kb/patch in the future ;)

Cheers,

Michael



---

archive/issue_comments_045115.json:
```json
{
    "body": "I'm adding a bunch more doctests and breaking this up into more managable chunks (viewable at least).  If anyone wants to review this, let me know, but you probably don't want to get started quite yet.",
    "created_at": "2009-04-22T10:27:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45115",
    "user": "https://github.com/roed314"
}
```

I'm adding a bunch more doctests and breaking this up into more managable chunks (viewable at least).  If anyone wants to review this, let me know, but you probably don't want to get started quite yet.



---

archive/issue_comments_045116.json:
```json
{
    "body": "Replying to [comment:15 roed]:\n> I'm adding a bunch more doctests and breaking this up into more managable chunks (viewable at least).  If anyone wants to review this, let me know, but you probably don't want to get started quite yet.\n\nOk, could you please made a series of tickets (in case you have clear dependencies and the patches can be layered) then so that one reviewer does not end up with say 1MB total of patches to review on one ticket?\n\nFor this ticket it would be nice if you could split the ReST formatting changes from the other fixes because I am happy to review the ReST changes. Then the other new doctests and fixes should go to a followup ticket. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-22T18:37:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45116",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:15 roed]:
> I'm adding a bunch more doctests and breaking this up into more managable chunks (viewable at least).  If anyone wants to review this, let me know, but you probably don't want to get started quite yet.

Ok, could you please made a series of tickets (in case you have clear dependencies and the patches can be layered) then so that one reviewer does not end up with say 1MB total of patches to review on one ticket?

For this ticket it would be nice if you could split the ReST formatting changes from the other fixes because I am happy to review the ReST changes. Then the other new doctests and fixes should go to a followup ticket. 

Cheers,

Michael



---

archive/issue_comments_045117.json:
```json
{
    "body": "This warrants changing the summart :)\n\nDavid will post a patch set that is split up and easier to review in a short while.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T03:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45117",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This warrants changing the summart :)

David will post a patch set that is split up and easier to review in a short while.

Cheers,

Michael



---

archive/issue_comments_045118.json:
```json
{
    "body": "For the record: This patch is not fully rebased against 3.4.1 yet, but it should be in a couple hours, so no point in attempting to apply it yet. The patch does raise coverage in the total of Sage by 2.1%, so we should really get it into 3.4.2 :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T04:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45118",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record: This patch is not fully rebased against 3.4.1 yet, but it should be in a couple hours, so no point in attempting to apply it yet. The patch does raise coverage in the total of Sage by 2.1%, so we should really get it into 3.4.2 :)

Cheers,

Michael



---

archive/issue_comments_045119.json:
```json
{
    "body": "These are split up so that they edit different files; one should therefore be able to apply them in any order (I've given the order I applied them in).  They're now small enough to view on trac.",
    "created_at": "2009-04-24T20:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45119",
    "user": "https://github.com/roed314"
}
```

These are split up so that they edit different files; one should therefore be able to apply them in any order (I've given the order I applied them in).  They're now small enough to view on trac.



---

archive/issue_comments_045120.json:
```json
{
    "body": "The last patch fail against 3.4.1: \n\n```\npatching file sage/rings/padics/padic_generic_element.pyx\nHunk #13 FAILED at 737.\nHunk #14 succeeded at 869 (offset -3 lines).\nHunk #15 succeeded at 898 (offset -3 lines).\nHunk #16 succeeded at 930 (offset -3 lines).\nHunk #17 succeeded at 956 (offset -3 lines).\nHunk #18 FAILED at 1006.\n2 out of 18 hunks FAILED -- saving rejects to file sage/rings/padics/padic_generic_element.pyx.rej\n```\n\nThere are some more issues with 3.4.2.alpha0, but I can revert the changes from there and just patch them back in after merging padics instead of rebasing the patch :)\n\nOne more thing: You credit Genya Zaytman for writing doctests, but AFAIK the person has never been credited for contributing to Sage. \n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T23:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45120",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The last patch fail against 3.4.1: 

```
patching file sage/rings/padics/padic_generic_element.pyx
Hunk #13 FAILED at 737.
Hunk #14 succeeded at 869 (offset -3 lines).
Hunk #15 succeeded at 898 (offset -3 lines).
Hunk #16 succeeded at 930 (offset -3 lines).
Hunk #17 succeeded at 956 (offset -3 lines).
Hunk #18 FAILED at 1006.
2 out of 18 hunks FAILED -- saving rejects to file sage/rings/padics/padic_generic_element.pyx.rej
```

There are some more issues with 3.4.2.alpha0, but I can revert the changes from there and just patch them back in after merging padics instead of rebasing the patch :)

One more thing: You credit Genya Zaytman for writing doctests, but AFAIK the person has never been credited for contributing to Sage. 

Cheers,

Michael



---

archive/issue_comments_045121.json:
```json
{
    "body": "Oh, and these are diffs, not patches, but I will commit in David's name should he not fix this.\n\nDavid: You can use export on queue patches by the way.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T23:07:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45121",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Oh, and these are diffs, not patches, but I will commit in David's name should he not fix this.

David: You can use export on queue patches by the way.

Cheers,

Michael



---

archive/issue_comments_045122.json:
```json
{
    "body": "I am seeing three doctest failure in 3.4.1.final on sage.math:\n\n```\nsage -t -long \"devel/sage/sage/rings/integer_ring.pyx\"      \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.final/devel/sage/sage/rings/integer_ring.pyx\", line 848:\n    sage: ZZ.completion(5, 15, print_mode='bars')\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.4.1.final/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.4.1.final/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.4.1.final/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_25[3]>\", line 1, in <module>\n        ZZ.completion(Integer(5), Integer(15), print_mode='bars')###line 848:\n    sage: ZZ.completion(5, 15, print_mode='bars')\n      File \"integer_ring.pyx\", line 840, in sage.rings.integer_ring.IntegerRing_class.completion (sage/rings/integer_ring.c:9144)\n    TypeError: completion() got an unexpected keyword argument 'print_mode'\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_25\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/sage-3.4.1.final/tmp/.doctest_integer_ring.py\n\t [2.5 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long \"devel/sage/sage/rings/integer_ring.pyx\"\nTotal time for all tests: 2.5 seconds\nmabshoff@sage:/scratch/mabshoff/sage-3.4.1.final$ sage -t -long devel/sage/sage/rings/padics/padic_capped_relative_element.pyx # 1 doctests failed\nsage -t -long \"devel/sage/sage/rings/padics/padic_capped_relative_element.pyx\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.final/devel/sage/sage/rings/padics/padic_capped_relative_element.pyx\", line 2283:\n    sage: hash(R(17)) #indirect doctest\nExpected:\n    17\n    1977822444\nGot:\n    17\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_57\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mabshoff/sage-3.4.1.final/tmp/.doctest_padic_capped_relative_element.py\n\t [1.3 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long \"devel/sage/sage/rings/padics/padic_capped_relative_element.pyx\"\nTotal time for all tests: 1.3 seconds\nmabshoff@sage:/scratch/mabshoff/sage-3.4.1.final$ sage -t -long devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx # 2 doctests failed\nsage -t -long \"devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.final/devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx\", line 667:\n    sage: _find_val_aprec_test(Zq(25,names='a'), [15, int(75), ntl_ZZ(625)])\nExpected:\n    (1, 340282366920938463463374607431768211457, 2)\nGot:\n    (4, 340282366920938463463374607431768211457, 2)\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.1.final/devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx\", line 699:\n    sage: _find_val_aprec_test(Zq(25,names='a'), [15, int(75), ntl_ZZ(625)]) #indirect doctest\nExpected:\n    (1, 340282366920938463463374607431768211457, 2)\nGot:\n    (4, 340282366920938463463374607431768211457, 2)\n**********************************************************************\n2 items had failures:\n   1 of   8 in __main__.example_14\n   1 of   8 in __main__.example_15\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/mabshoff/sage-3.4.1.final/tmp/.doctest_padic_ZZ_pX_element.py\n\t [1.4 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long \"devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx\"\nTotal time for all tests: 1.4 seconds\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-04-25T05:28:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45122",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am seeing three doctest failure in 3.4.1.final on sage.math:

```
sage -t -long "devel/sage/sage/rings/integer_ring.pyx"      
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.final/devel/sage/sage/rings/integer_ring.pyx", line 848:
    sage: ZZ.completion(5, 15, print_mode='bars')
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.4.1.final/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.1.final/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.1.final/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_25[3]>", line 1, in <module>
        ZZ.completion(Integer(5), Integer(15), print_mode='bars')###line 848:
    sage: ZZ.completion(5, 15, print_mode='bars')
      File "integer_ring.pyx", line 840, in sage.rings.integer_ring.IntegerRing_class.completion (sage/rings/integer_ring.c:9144)
    TypeError: completion() got an unexpected keyword argument 'print_mode'
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_25
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/sage-3.4.1.final/tmp/.doctest_integer_ring.py
	 [2.5 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage/sage/rings/integer_ring.pyx"
Total time for all tests: 2.5 seconds
mabshoff@sage:/scratch/mabshoff/sage-3.4.1.final$ sage -t -long devel/sage/sage/rings/padics/padic_capped_relative_element.pyx # 1 doctests failed
sage -t -long "devel/sage/sage/rings/padics/padic_capped_relative_element.pyx"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.final/devel/sage/sage/rings/padics/padic_capped_relative_element.pyx", line 2283:
    sage: hash(R(17)) #indirect doctest
Expected:
    17
    1977822444
Got:
    17
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_57
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/sage-3.4.1.final/tmp/.doctest_padic_capped_relative_element.py
	 [1.3 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage/sage/rings/padics/padic_capped_relative_element.pyx"
Total time for all tests: 1.3 seconds
mabshoff@sage:/scratch/mabshoff/sage-3.4.1.final$ sage -t -long devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx # 2 doctests failed
sage -t -long "devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.final/devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx", line 667:
    sage: _find_val_aprec_test(Zq(25,names='a'), [15, int(75), ntl_ZZ(625)])
Expected:
    (1, 340282366920938463463374607431768211457, 2)
Got:
    (4, 340282366920938463463374607431768211457, 2)
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.final/devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx", line 699:
    sage: _find_val_aprec_test(Zq(25,names='a'), [15, int(75), ntl_ZZ(625)]) #indirect doctest
Expected:
    (1, 340282366920938463463374607431768211457, 2)
Got:
    (4, 340282366920938463463374607431768211457, 2)
**********************************************************************
2 items had failures:
   1 of   8 in __main__.example_14
   1 of   8 in __main__.example_15
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mabshoff/sage-3.4.1.final/tmp/.doctest_padic_ZZ_pX_element.py
	 [1.4 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx"
Total time for all tests: 1.4 seconds
```


Cheers,

Michael



---

archive/issue_comments_045123.json:
```json
{
    "body": "Fixed the first two doctest problems mabs mentioned.  I have no idea what's up with the ZZ_pX_element.py one: it doesn't occur on my machine.  Robert, any thoughts?",
    "created_at": "2009-04-25T06:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45123",
    "user": "https://github.com/roed314"
}
```

Fixed the first two doctest problems mabs mentioned.  I have no idea what's up with the ZZ_pX_element.py one: it doesn't occur on my machine.  Robert, any thoughts?



---

archive/issue_comments_045124.json:
```json
{
    "body": "These changes fix 5105 (as might be guessed from the dependency), but also 5076 (no need to apply the patch there, it's included in this one).",
    "created_at": "2009-04-25T07:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45124",
    "user": "https://github.com/roed314"
}
```

These changes fix 5105 (as might be guessed from the dependency), but also 5076 (no need to apply the patch there, it's included in this one).



---

archive/issue_comments_045125.json:
```json
{
    "body": "I've rebased 5236 against this as well.  Want to review that one too Robert?",
    "created_at": "2009-04-25T07:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45125",
    "user": "https://github.com/roed314"
}
```

I've rebased 5236 against this as well.  Want to review that one too Robert?



---

archive/issue_comments_045126.json:
```json
{
    "body": "I created a padics component with default asignee David.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-26T19:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45126",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I created a padics component with default asignee David.

Cheers,

Michael



---

archive/issue_comments_045127.json:
```json
{
    "body": "Changing assignee from @williamstein to @roed314.",
    "created_at": "2009-04-26T19:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45127",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to @roed314.



---

archive/issue_comments_045128.json:
```json
{
    "body": "Changing component from number theory to padics.",
    "created_at": "2009-04-26T19:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45128",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from number theory to padics.



---

archive/issue_comments_045129.json:
```json
{
    "body": "I'll start reviewing these tomorrow.",
    "created_at": "2009-04-29T03:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45129",
    "user": "https://github.com/robertwb"
}
```

I'll start reviewing these tomorrow.



---

archive/issue_comments_045130.json:
```json
{
    "body": "FYI: #5864 touches code the above patch touches.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-29T23:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45130",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

FYI: #5864 touches code the above patch touches.

Cheers,

Michael



---

archive/issue_comments_045131.json:
```json
{
    "body": "Replying to [comment:31 mabshoff]:\n> FYI: #5864 touches code the above patch touches.\n\nSorry, I meant #5846 and it does **not** - sorry for the noise :)\n\n> Cheers,\n> \n> Michael\n\nCheers,\n\nMichael",
    "created_at": "2009-04-30T00:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45131",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:31 mabshoff]:
> FYI: #5864 touches code the above patch touches.

Sorry, I meant #5846 and it does **not** - sorry for the noise :)

> Cheers,
> 
> Michael

Cheers,

Michael



---

archive/issue_comments_045132.json:
```json
{
    "body": "Once this is merged #610 should be closed.",
    "created_at": "2009-04-30T00:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45132",
    "user": "https://github.com/roed314"
}
```

Once this is merged #610 should be closed.



---

archive/issue_comments_045133.json:
```json
{
    "body": "Could you post a summary of how things got moved around (e.g. for every file deleted, where, if anywhere, the deleted code got put?)",
    "created_at": "2009-05-01T07:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45133",
    "user": "https://github.com/robertwb"
}
```

Could you post a summary of how things got moved around (e.g. for every file deleted, where, if anywhere, the deleted code got put?)



---

archive/issue_comments_045134.json:
```json
{
    "body": "Certainly.\n\ncapped_absolute_generic.py, capped_relative_field_generic.py, capped_relative_generic.py, capped_relative_ring_generic.py, fixed_mod_generic.py, padic_capped_absolute_ring_generic.py, padic_capped_relative_field_generic.py, padic_capped_relative_ring_generic.py, padic_field_base_generic.py, padic_field_generic.py, padic_fixed_mod_ring_generic.py, padic_ring_base_generic.py, padic_ring_generic.py ----> generic_nodes.py\n\npadic_field_capped_relative.py, padic_ring_capped_absolute.py, padic_ring_capped_relative.py, padic_ring_fixed_mod.py ----> padic_base_leaves.py\n\nlazy_field_generic.py, lazy_generic.py, lazy_ring_generic.py, padic_field_lazy.py, padic_lazy_element.py, padic_lazy_field_generic.py, padic_lazy_generic.py, padic_lazy_ring_generic.py, padic_ring_lazy.py, valuation.py ----> deleted because lazy p-adics not supported and won't be for a while\n\nrigid_functions.pyx, rigid_functions.pxd ----> deleted because I didn't want to write the doctest and make parents.",
    "created_at": "2009-05-01T07:56:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45134",
    "user": "https://github.com/roed314"
}
```

Certainly.

capped_absolute_generic.py, capped_relative_field_generic.py, capped_relative_generic.py, capped_relative_ring_generic.py, fixed_mod_generic.py, padic_capped_absolute_ring_generic.py, padic_capped_relative_field_generic.py, padic_capped_relative_ring_generic.py, padic_field_base_generic.py, padic_field_generic.py, padic_fixed_mod_ring_generic.py, padic_ring_base_generic.py, padic_ring_generic.py ----> generic_nodes.py

padic_field_capped_relative.py, padic_ring_capped_absolute.py, padic_ring_capped_relative.py, padic_ring_fixed_mod.py ----> padic_base_leaves.py

lazy_field_generic.py, lazy_generic.py, lazy_ring_generic.py, padic_field_lazy.py, padic_lazy_element.py, padic_lazy_field_generic.py, padic_lazy_generic.py, padic_lazy_ring_generic.py, padic_ring_lazy.py, valuation.py ----> deleted because lazy p-adics not supported and won't be for a while

rigid_functions.pyx, rigid_functions.pxd ----> deleted because I didn't want to write the doctest and make parents.



---

archive/issue_comments_045135.json:
```json
{
    "body": "First, the patches can't be partially applied and used one at a time. But it is better than one monolithic patch. \n\nOK, the first two patches (outside-padics and deletions/moving look good). I'm all for a generic_nodes.py rather than a dozen files with three lines in them each (it makes it a lot easier to trace the code for instance). \n\nI'm most of the way through padic_doctests_1.patch--it looks good for the most part. Lots of the patch is whitespace/line wrapping--it would be nice to be able to filter stuff like this out better for review purposes. There's a fair amount of commenting stuff out/ReSTification as well, and new doctests. The only issues I've found are \n\nsage/rings/padics/eisenstein_extension_generic.py:97 - typo \"extensinos\"\n\nsage/rings/padics/factory.py:2323: def krasner_check(poly, prec): always returns True, but comments state that it's really not implemented, which is a bit worrisome.",
    "created_at": "2009-05-02T06:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45135",
    "user": "https://github.com/robertwb"
}
```

First, the patches can't be partially applied and used one at a time. But it is better than one monolithic patch. 

OK, the first two patches (outside-padics and deletions/moving look good). I'm all for a generic_nodes.py rather than a dozen files with three lines in them each (it makes it a lot easier to trace the code for instance). 

I'm most of the way through padic_doctests_1.patch--it looks good for the most part. Lots of the patch is whitespace/line wrapping--it would be nice to be able to filter stuff like this out better for review purposes. There's a fair amount of commenting stuff out/ReSTification as well, and new doctests. The only issues I've found are 

sage/rings/padics/eisenstein_extension_generic.py:97 - typo "extensinos"

sage/rings/padics/factory.py:2323: def krasner_check(poly, prec): always returns True, but comments state that it's really not implemented, which is a bit worrisome.



---

archive/issue_comments_045136.json:
```json
{
    "body": "Some more comments: \n\n**padic_doctests_2.patch** \n\nlooks good, again, mostly rest/whitespace changes. \n\n**padic_doctests_3.patch**\n\n* `sage/rings/padics/padic_ZZ_pX_element.pyx:74` extraneous print statements\n\n* `sage/rings/padics/padic_base_generic.py::33`  generic `__reduce__` commented out, should probably be outright deleted if it's not used (do subclasses always override this?)\n\n* `sage/rings/padics/padic_base_generic_element.pyx:43` (nitpicky) I think it's easier to read\n\n  {{{\n\"%s + O(%s^%s)\" % (self.lift(), self.parent().prime(), self.precision_absolute())\n}}}\n\nthan\n   \n   {{{\n        self.lift().str() + \" + O(\" + self.parent().prime().str() + \"^\" + self.precision_absolute().str() + \")\"\n}}}\n\nAlso, something I just noticed (not part of this patch). The functions `_set_to_mpz`, `_set_to_mpq` don't change self (as one would expect) but set the input parameter. Perhaps `_set_mpz_to` or something similar would be better.",
    "created_at": "2009-05-03T08:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45136",
    "user": "https://github.com/robertwb"
}
```

Some more comments: 

**padic_doctests_2.patch** 

looks good, again, mostly rest/whitespace changes. 

**padic_doctests_3.patch**

* `sage/rings/padics/padic_ZZ_pX_element.pyx:74` extraneous print statements

* `sage/rings/padics/padic_base_generic.py::33`  generic `__reduce__` commented out, should probably be outright deleted if it's not used (do subclasses always override this?)

* `sage/rings/padics/padic_base_generic_element.pyx:43` (nitpicky) I think it's easier to read

  {{{
"%s + O(%s^%s)" % (self.lift(), self.parent().prime(), self.precision_absolute())
}}}

than
   
   {{{
        self.lift().str() + " + O(" + self.parent().prime().str() + "^" + self.precision_absolute().str() + ")"
}}}

Also, something I just noticed (not part of this patch). The functions `_set_to_mpz`, `_set_to_mpq` don't change self (as one would expect) but set the input parameter. Perhaps `_set_mpz_to` or something similar would be better.



---

archive/issue_comments_045137.json:
```json
{
    "body": "sage/rings/padics/padic_capped_absolute_element.pyx:382\n\n\n```\n-            sage: R(7^5)._is_inexact_zero() \n+            sage: R(0,4)._is_inexact_zero() \n```\n\n\nThe former is a better example, IMHO.",
    "created_at": "2009-05-03T08:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45137",
    "user": "https://github.com/robertwb"
}
```

sage/rings/padics/padic_capped_absolute_element.pyx:382


```
-            sage: R(7^5)._is_inexact_zero() 
+            sage: R(0,4)._is_inexact_zero() 
```


The former is a better example, IMHO.



---

archive/issue_comments_045138.json:
```json
{
    "body": "Some general remarks: \n\n* The `AUTHORS` block is not a verbatim/code block, no need for double colons. \n\n* Several docstrings are duplicated in their entirety, e.g. for a cdef function and its testing function. There really should just be one copy of the docstring, and the other should reference the first. \n\n* Some examples, e.g. for `_div_` could be more illustrative (e.g. showing that div produces multiplicative inverses would be interesting, as would dividing by non-units). \n\n* I like that there is some variety in the primes used, including big ones, but I would like to see more variety in the extension fields used. The field Q_5(a) where a is a root of `f = x^5 + 75*x^3 - 15*x^2 +125*x - 5` is used in nearly every example (i.e. over 150 times).",
    "created_at": "2009-05-03T08:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45138",
    "user": "https://github.com/robertwb"
}
```

Some general remarks: 

* The `AUTHORS` block is not a verbatim/code block, no need for double colons. 

* Several docstrings are duplicated in their entirety, e.g. for a cdef function and its testing function. There really should just be one copy of the docstring, and the other should reference the first. 

* Some examples, e.g. for `_div_` could be more illustrative (e.g. showing that div produces multiplicative inverses would be interesting, as would dividing by non-units). 

* I like that there is some variety in the primes used, including big ones, but I would like to see more variety in the extension fields used. The field Q_5(a) where a is a root of `f = x^5 + 75*x^3 - 15*x^2 +125*x - 5` is used in nearly every example (i.e. over 150 times).



---

archive/issue_comments_045139.json:
```json
{
    "body": "Things left to do:\n\n1. Continue through the padic_ZZ_pX files and add more examples and tests using other extensions (started in padic_ZZ_pX_CR_element.pyx).\n2. Continue improving ReST compliance in files after padic_capped_absolute_element.pyx\n\nRobert, are there other files besides padic_ZZ_pX_element.pyx that you had in mind for the comment about docstrings being duplicated?",
    "created_at": "2009-05-04T09:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45139",
    "user": "https://github.com/roed314"
}
```

Things left to do:

1. Continue through the padic_ZZ_pX files and add more examples and tests using other extensions (started in padic_ZZ_pX_CR_element.pyx).
2. Continue improving ReST compliance in files after padic_capped_absolute_element.pyx

Robert, are there other files besides padic_ZZ_pX_element.pyx that you had in mind for the comment about docstrings being duplicated?



---

archive/issue_comments_045140.json:
```json
{
    "body": "`padic_ZZ_pX_element.pyx` was the first place I noticed duplicated doctests, but it's a pattern I think I saw several times.",
    "created_at": "2009-05-06T05:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45140",
    "user": "https://github.com/robertwb"
}
```

`padic_ZZ_pX_element.pyx` was the first place I noticed duplicated doctests, but it's a pattern I think I saw several times.



---

archive/issue_comments_045141.json:
```json
{
    "body": "There's also some verbatim duplicated doctests in `sage/rings/padics/padic_ext_element.pyx`\n\nThere's no way the doctes for `long valuation_c` at `sage/rings/padics/padic_generic.py:814` is actually being tested.",
    "created_at": "2009-05-07T03:24:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45141",
    "user": "https://github.com/robertwb"
}
```

There's also some verbatim duplicated doctests in `sage/rings/padics/padic_ext_element.pyx`

There's no way the doctes for `long valuation_c` at `sage/rings/padics/padic_generic.py:814` is actually being tested.



---

archive/issue_comments_045142.json:
```json
{
    "body": "I've finished reading everything. \n\n`PowComputer_ext._pow_ZZ_tmp_demo` is basically a verbatim copy of `PowComputer_class._pow_ZZ_tmp_demo`\n\n`pAdicZZpXFMElement._teichmuller_set` and `PowComputer_ZZ_pX.teichmuller_set_c` have nearly the same exact doctest, as do `pAdicCappedRelativeElement._to_gen` and `pAdicCappedRelativeElement._pari_`. I can see why one would want to test it in both places, but it would be better to test with distinct elements. There's probably others, I just get a very deja-vu feeling reading some of these doctests...\n\nHow many more files need to be ReSTified? If its more than a one or two, lets defer doing this to a later ticket so we can focus on getting this in. \n\nYour referee patch looks good too, and does address most of my concerns.",
    "created_at": "2009-05-07T06:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45142",
    "user": "https://github.com/robertwb"
}
```

I've finished reading everything. 

`PowComputer_ext._pow_ZZ_tmp_demo` is basically a verbatim copy of `PowComputer_class._pow_ZZ_tmp_demo`

`pAdicZZpXFMElement._teichmuller_set` and `PowComputer_ZZ_pX.teichmuller_set_c` have nearly the same exact doctest, as do `pAdicCappedRelativeElement._to_gen` and `pAdicCappedRelativeElement._pari_`. I can see why one would want to test it in both places, but it would be better to test with distinct elements. There's probably others, I just get a very deja-vu feeling reading some of these doctests...

How many more files need to be ReSTified? If its more than a one or two, lets defer doing this to a later ticket so we can focus on getting this in. 

Your referee patch looks good too, and does address most of my concerns.



---

archive/issue_comments_045143.json:
```json
{
    "body": "About 13 more files need improved ReSTification.\n\nI'll try to diversify the doctests for those functions in a bit.  Right now I'm working on p-adic polynomials though.  :-)",
    "created_at": "2009-05-07T06:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45143",
    "user": "https://github.com/roed314"
}
```

About 13 more files need improved ReSTification.

I'll try to diversify the doctests for those functions in a bit.  Right now I'm working on p-adic polynomials though.  :-)



---

archive/issue_comments_045144.json:
```json
{
    "body": "\n```\nrobert$ ls sage/rings/padics/*.py* | wc\n      30      30    1192\n```\n\n\nSo nearly half of the files still need ReST conversion? Let's put this off to a later ticket, so we can get this one here into 4.0.",
    "created_at": "2009-05-07T07:02:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45144",
    "user": "https://github.com/robertwb"
}
```


```
robert$ ls sage/rings/padics/*.py* | wc
      30      30    1192
```


So nearly half of the files still need ReST conversion? Let's put this off to a later ticket, so we can get this one here into 4.0.



---

archive/issue_comments_045145.json:
```json
{
    "body": "Yep, I agree.  There are no build errors for any of them, but there are lots of files that need many ` added.",
    "created_at": "2009-05-07T07:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45145",
    "user": "https://github.com/roed314"
}
```

Yep, I agree.  There are no build errors for any of them, but there are lots of files that need many ` added.



---

archive/issue_comments_045146.json:
```json
{
    "body": "With #5105 applied all patches apply and I am seeing one issue on sage.math:\n\n```\nsage -t -long \"devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-4.0.alpha0/devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx\", line 654:\n    sage: _find_val_aprec_test(Zq(25,names='a'), [15, int(75), ntl_ZZ(625)])\nExpected:\n    (1, 340282366920938463463374607431768211457, 2)\nGot:\n    (4, 340282366920938463463374607431768211457, 2)\n**********************************************************************\n1 items had failures:\n```\n\nBut padic_referee_fixes_2.patch  introduces some problem since the latex() methods use mathbf() instead of ZZ or QQ for example.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-10T13:40:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45146",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With #5105 applied all patches apply and I am seeing one issue on sage.math:

```
sage -t -long "devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx"
**********************************************************************
File "/scratch/mabshoff/sage-4.0.alpha0/devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx", line 654:
    sage: _find_val_aprec_test(Zq(25,names='a'), [15, int(75), ntl_ZZ(625)])
Expected:
    (1, 340282366920938463463374607431768211457, 2)
Got:
    (4, 340282366920938463463374607431768211457, 2)
**********************************************************************
1 items had failures:
```

But padic_referee_fixes_2.patch  introduces some problem since the latex() methods use mathbf() instead of ZZ or QQ for example.

Cheers,

Michael



---

archive/issue_comments_045147.json:
```json
{
    "body": "Hah.  On sage.math:\n\n\n```\nsage: from sage.libs.ntl.all import ZZ as ntl_ZZ\nsage: ntl_ZZ(4) < 1\nTrue\nsage: ntl_ZZ(1) < 4\nTrue\n```\n\n\nOn my machine:\n\n```\nsage: from sage.libs.ntl.all import ZZ as ntl_ZZ\nsage: ntl_ZZ(4) < 1\nFalse\nsage: ntl_ZZ(1) < 4\nFalse\n```\n\n\nntl_ZZ is just comparing types.  I'll change the code to convert to Integers earlier.\n\nReplying to [comment:47 mabshoff]:\n> With #5105 applied all patches apply and I am seeing one issue on sage.math:\n> {{{\n> sage -t -long \"devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx\"\n> **********************************************************************\n> File \"/scratch/mabshoff/sage-4.0.alpha0/devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx\", line 654:\n>     sage: _find_val_aprec_test(Zq(25,names='a'), [15, int(75), ntl_ZZ(625)])\n> Expected:\n>     (1, 340282366920938463463374607431768211457, 2)\n> Got:\n>     (4, 340282366920938463463374607431768211457, 2)\n> **********************************************************************\n> 1 items had failures:\n> }}}\n> But padic_referee_fixes_2.patch  introduces some problem since the latex() methods use mathbf() instead of ZZ or QQ for example.\n> \n> Cheers,\n> \n> Michael",
    "created_at": "2009-05-11T06:17:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45147",
    "user": "https://github.com/roed314"
}
```

Hah.  On sage.math:


```
sage: from sage.libs.ntl.all import ZZ as ntl_ZZ
sage: ntl_ZZ(4) < 1
True
sage: ntl_ZZ(1) < 4
True
```


On my machine:

```
sage: from sage.libs.ntl.all import ZZ as ntl_ZZ
sage: ntl_ZZ(4) < 1
False
sage: ntl_ZZ(1) < 4
False
```


ntl_ZZ is just comparing types.  I'll change the code to convert to Integers earlier.

Replying to [comment:47 mabshoff]:
> With #5105 applied all patches apply and I am seeing one issue on sage.math:
> {{{
> sage -t -long "devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx"
> **********************************************************************
> File "/scratch/mabshoff/sage-4.0.alpha0/devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx", line 654:
>     sage: _find_val_aprec_test(Zq(25,names='a'), [15, int(75), ntl_ZZ(625)])
> Expected:
>     (1, 340282366920938463463374607431768211457, 2)
> Got:
>     (4, 340282366920938463463374607431768211457, 2)
> **********************************************************************
> 1 items had failures:
> }}}
> But padic_referee_fixes_2.patch  introduces some problem since the latex() methods use mathbf() instead of ZZ or QQ for example.
> 
> Cheers,
> 
> Michael



---

archive/issue_comments_045148.json:
```json
{
    "body": "Attachment [padic_doctests_1.patch](tarball://root/attachments/some-uuid/ticket5778/padic_doctests_1.patch) by @roed314 created at 2009-05-11 09:20:31",
    "created_at": "2009-05-11T09:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45148",
    "user": "https://github.com/roed314"
}
```

Attachment [padic_doctests_1.patch](tarball://root/attachments/some-uuid/ticket5778/padic_doctests_1.patch) by @roed314 created at 2009-05-11 09:20:31



---

archive/issue_comments_045149.json:
```json
{
    "body": "Attachment [padic_doctests_3.patch](tarball://root/attachments/some-uuid/ticket5778/padic_doctests_3.patch) by @roed314 created at 2009-05-11 09:20:43",
    "created_at": "2009-05-11T09:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45149",
    "user": "https://github.com/roed314"
}
```

Attachment [padic_doctests_3.patch](tarball://root/attachments/some-uuid/ticket5778/padic_doctests_3.patch) by @roed314 created at 2009-05-11 09:20:43



---

archive/issue_comments_045150.json:
```json
{
    "body": "Attachment [padic_referee_fixes.patch](tarball://root/attachments/some-uuid/ticket5778/padic_referee_fixes.patch) by @roed314 created at 2009-05-11 09:21:41",
    "created_at": "2009-05-11T09:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45150",
    "user": "https://github.com/roed314"
}
```

Attachment [padic_referee_fixes.patch](tarball://root/attachments/some-uuid/ticket5778/padic_referee_fixes.patch) by @roed314 created at 2009-05-11 09:21:41



---

archive/issue_comments_045151.json:
```json
{
    "body": "Attachment [padic_referee_fixes_2.patch](tarball://root/attachments/some-uuid/ticket5778/padic_referee_fixes_2.patch) by @roed314 created at 2009-05-11 10:16:50",
    "created_at": "2009-05-11T10:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45151",
    "user": "https://github.com/roed314"
}
```

Attachment [padic_referee_fixes_2.patch](tarball://root/attachments/some-uuid/ticket5778/padic_referee_fixes_2.patch) by @roed314 created at 2009-05-11 10:16:50



---

archive/issue_comments_045152.json:
```json
{
    "body": "Attachment [padic_doctests_deletions.patch](tarball://root/attachments/some-uuid/ticket5778/padic_doctests_deletions.patch) by @roed314 created at 2009-05-11 10:19:29",
    "created_at": "2009-05-11T10:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45152",
    "user": "https://github.com/roed314"
}
```

Attachment [padic_doctests_deletions.patch](tarball://root/attachments/some-uuid/ticket5778/padic_doctests_deletions.patch) by @roed314 created at 2009-05-11 10:19:29



---

archive/issue_comments_045153.json:
```json
{
    "body": "Attachment [padic_doctests_outside.patch](tarball://root/attachments/some-uuid/ticket5778/padic_doctests_outside.patch) by mabshoff created at 2009-05-11 10:38:11\n\nI am giving this ticket a positive review in RobertWB's name. It now passes all doctests on sage.math, it applies and builds, so any more concerns should be addressed via followup tickets. Post merge we are definitely in better shape than before and given the size of this patch it seems like a good idea to get this in. With all 8 patches applied:\n\n```\nOverall weighted coverage score:  74.4%\nTotal number of functions:  21967\nWe need  133 more function to get to 75% coverage.\n```\n",
    "created_at": "2009-05-11T10:38:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45153",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [padic_doctests_outside.patch](tarball://root/attachments/some-uuid/ticket5778/padic_doctests_outside.patch) by mabshoff created at 2009-05-11 10:38:11

I am giving this ticket a positive review in RobertWB's name. It now passes all doctests on sage.math, it applies and builds, so any more concerns should be addressed via followup tickets. Post merge we are definitely in better shape than before and given the size of this patch it seems like a good idea to get this in. With all 8 patches applied:

```
Overall weighted coverage score:  74.4%
Total number of functions:  21967
We need  133 more function to get to 75% coverage.
```




---

archive/issue_comments_045154.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T10:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45154",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_045155.json:
```json
{
    "body": "Merged \n\n* trac_5778_padic_doctests_1.patch\n* trac_5778_padic_doctests_2.patch\n* trac_5778_padic_doctests_3.patch\n* trac_5778_padic_doctests_4.patch\n* trac_5778_padic_doctests_deletions.patch\n* trac_5778_padic_doctests_outside.patch\n* trac_5778_padic_referee_fixes_2.patch\n* trac_5778_padic_referee_fixes.patch\n\nin Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T10:38:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45155",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 

* trac_5778_padic_doctests_1.patch
* trac_5778_padic_doctests_2.patch
* trac_5778_padic_doctests_3.patch
* trac_5778_padic_doctests_4.patch
* trac_5778_padic_doctests_deletions.patch
* trac_5778_padic_doctests_outside.patch
* trac_5778_padic_referee_fixes_2.patch
* trac_5778_padic_referee_fixes.patch

in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_045156.json:
```json
{
    "body": "To followup now that I've had a chance to look at the last patch, yet, positive review deserved.",
    "created_at": "2009-05-11T19:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5778#issuecomment-45156",
    "user": "https://github.com/robertwb"
}
```

To followup now that I've had a chance to look at the last patch, yet, positive review deserved.
