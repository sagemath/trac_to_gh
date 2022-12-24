# Issue 2223: sage-2.10.2.alpha1 -- bessel_J -- precision errors

archive/issues_002223.json:
```json
{
    "body": "Assignee: somebody\n\nOn OSX \n\n```\nsage -t  devel/sage-main/sage/functions/special.py          **********************************************************************\nFile \"special.py\", line 506:\n    sage: bessel_J(3,10,\"scipy\")\nExpected:\n    0.0583793793052... - 1.65905485529...e-17*I\nGot:\n    0.0583793793052000 - 2.93425242844000e-17*I\n**********************************************************************\n1 items had failures:\n```\n\n\nThoughts:\n\nIt's likely a theorem that bessel_J is always real\nfor integer first argument?  If so, let's just return\nthe real part and be done with these weird imaginary\npart issues:\n\n```\nsage: bessel_J(3,10,\"scipy\")\n0.0583793793052000 - 2.93425242844000e-17*I\nsage: bessel_J(4,10,\"scipy\")\n9.69299109301000e-17*I - 0.219602686102000\nsage: bessel_J(5,10,\"scipy\")\n1.11203257018000e-16*I - 0.234061528187000\nsage: bessel_J(10,10,\"scipy\")\n0.207486106633000 - 1.17732704470000e-16*I\nsage: bessel_J(10,20,\"scipy\")\n0.186482558024000 - 2.10019326787000e-16*I\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2223\n\n",
    "created_at": "2008-02-20T06:54:22Z",
    "labels": [
        "basic arithmetic",
        "blocker",
        "bug"
    ],
    "title": "sage-2.10.2.alpha1 -- bessel_J -- precision errors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2223",
    "user": "was"
}
```
Assignee: somebody

On OSX 

```
sage -t  devel/sage-main/sage/functions/special.py          **********************************************************************
File "special.py", line 506:
    sage: bessel_J(3,10,"scipy")
Expected:
    0.0583793793052... - 1.65905485529...e-17*I
Got:
    0.0583793793052000 - 2.93425242844000e-17*I
**********************************************************************
1 items had failures:
```


Thoughts:

It's likely a theorem that bessel_J is always real
for integer first argument?  If so, let's just return
the real part and be done with these weird imaginary
part issues:

```
sage: bessel_J(3,10,"scipy")
0.0583793793052000 - 2.93425242844000e-17*I
sage: bessel_J(4,10,"scipy")
9.69299109301000e-17*I - 0.219602686102000
sage: bessel_J(5,10,"scipy")
1.11203257018000e-16*I - 0.234061528187000
sage: bessel_J(10,10,"scipy")
0.207486106633000 - 1.17732704470000e-16*I
sage: bessel_J(10,20,"scipy")
0.186482558024000 - 2.10019326787000e-16*I
```


Issue created by migration from https://trac.sagemath.org/ticket/2223





---

archive/issue_comments_014728.json:
```json
{
    "body": "I assumed (stupdly) that ...e-(large) would be parsed as 0. I can replace all terms with\ne-(large) by 0.000... if that seems reasonable.",
    "created_at": "2008-02-20T11:30:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2223#issuecomment-14728",
    "user": "wdj"
}
```

I assumed (stupdly) that ...e-(large) would be parsed as 0. I can replace all terms with
e-(large) by 0.000... if that seems reasonable.



---

archive/issue_comments_014729.json:
```json
{
    "body": "More precisely: I can replace all terms with e-(large)*I by \n(a) \"0.000...*I\" (to indicate that the user might get a small number returned from scipy) or \n(b) \"0.0*I\" or \n(c) nothing (as William stated), \nwhichever seems more reasonable.",
    "created_at": "2008-02-20T11:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2223#issuecomment-14729",
    "user": "wdj"
}
```

More precisely: I can replace all terms with e-(large)*I by 
(a) "0.000...*I" (to indicate that the user might get a small number returned from scipy) or 
(b) "0.0*I" or 
(c) nothing (as William stated), 
whichever seems more reasonable.



---

archive/issue_comments_014730.json:
```json
{
    "body": "Attachment [8632.patch](tarball://root/attachments/some-uuid/ticket2223/8632.patch) by wdj created at 2008-02-20 23:58:29",
    "created_at": "2008-02-20T23:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2223#issuecomment-14730",
    "user": "wdj"
}
```

Attachment [8632.patch](tarball://root/attachments/some-uuid/ticket2223/8632.patch) by wdj created at 2008-02-20 23:58:29



---

archive/issue_comments_014731.json:
```json
{
    "body": "The attached patch fixes the problem referred to above. It replaces *e-(large)*I by nothing in the docstring. Paases sage -t. sage -testall has lots of failures, but none seem related to this patch.",
    "created_at": "2008-02-21T00:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2223#issuecomment-14731",
    "user": "wdj"
}
```

The attached patch fixes the problem referred to above. It replaces *e-(large)*I by nothing in the docstring. Paases sage -t. sage -testall has lots of failures, but none seem related to this patch.



---

archive/issue_comments_014732.json:
```json
{
    "body": "David, the patch you posted only removes one space. You probably need to export at least one commit prior to that.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-21T00:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2223#issuecomment-14732",
    "user": "mabshoff"
}
```

David, the patch you posted only removes one space. You probably need to export at least one commit prior to that.

Cheers,

Michael



---

archive/issue_comments_014733.json:
```json
{
    "body": "Sorry. I don't know what I did wrong. I thin this new patch is better.",
    "created_at": "2008-02-21T01:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2223#issuecomment-14733",
    "user": "wdj"
}
```

Sorry. I don't know what I did wrong. I thin this new patch is better.



---

archive/issue_comments_014734.json:
```json
{
    "body": "Attachment [8631.patch](tarball://root/attachments/some-uuid/ticket2223/8631.patch) by mabshoff created at 2008-02-21 19:35:51\n\nWilliam's pat",
    "created_at": "2008-02-21T19:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2223#issuecomment-14734",
    "user": "mabshoff"
}
```

Attachment [8631.patch](tarball://root/attachments/some-uuid/ticket2223/8631.patch) by mabshoff created at 2008-02-21 19:35:51

William's pat



---

archive/issue_comments_014735.json:
```json
{
    "body": "As is the patch doesn't apply:\n\n```\nsage$ patch -p1 --dry-run < trac_2223.patch\npatching file sage/functions/special.py\nHunk #1 FAILED at 5.\nHunk #2 succeeded at 500 (offset 7 lines).\nHunk #3 FAILED at 514.\nHunk #4 succeeded at 537 with fuzz 2 (offset 10 lines).\n2 out of 4 hunks FAILED -- saving rejects to file sage/functions/special.py.rej\n```\n\nI guess the only important hunk is the third one, so I will probably merge that one manually.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-22T01:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2223#issuecomment-14735",
    "user": "mabshoff"
}
```

As is the patch doesn't apply:

```
sage$ patch -p1 --dry-run < trac_2223.patch
patching file sage/functions/special.py
Hunk #1 FAILED at 5.
Hunk #2 succeeded at 500 (offset 7 lines).
Hunk #3 FAILED at 514.
Hunk #4 succeeded at 537 with fuzz 2 (offset 10 lines).
2 out of 4 hunks FAILED -- saving rejects to file sage/functions/special.py.rej
```

I guess the only important hunk is the third one, so I will probably merge that one manually.

Cheers,

Michael



---

archive/issue_comments_014736.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-22T01:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2223#issuecomment-14736",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014737.json:
```json
{
    "body": "Merged hunk 3 manually in Sage 2.10.2.rc0",
    "created_at": "2008-02-22T01:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2223",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2223#issuecomment-14737",
    "user": "mabshoff"
}
```

Merged hunk 3 manually in Sage 2.10.2.rc0
