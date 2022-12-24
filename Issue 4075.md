# Issue 4075: bug in BCHCode

archive/issues_004075.json:
```json
{
    "body": "Assignee: @rlmill\n\nThis was reported by Felipe Voloch:\n\n\n```\nHi,\n\nI am not sure how to report bugs in Sage but I see you are involved\nwith their coding theory. I was playing around with BCH codes and\nin particular I wanted the BCH code over F_5 of length 26 and designed\ndistance 5. Sage reports this code as having dimension 25 (see below)\nbut the dimension should be 10, which Magma computes correctly (see\nbelow also).\n\nThanks \n\nFelipe\n\n---------------------SAGE---------------------------------------------\namd13:~> sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.0.5, Release Date: 2008-07-11                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: C = BCHCode(26,5,GF(5)); C\nLinear code of length 26, dimension 25 over Finite Field of size 5\n\n\n---------------------MAGMA--------------------------------------------\nlinux182~> magma\nMagma V2.14-10    Fri Sep  5 2008 14:24:48 on linux182 [Seed = 1390124479]\nType ? for help.  Type <Ctrl>-D to quit.\n> > C:=BCHCode(GF(5),26,5); \n> > Dimension(C);\n10\n```\n\n\nIncidently, Guava does this correctly. The problem is that I used the wrong element to construct the generator polynomial. \n\nThis is fixed in the attached patch, based on 3.1.2.alpha4. It passes sage -testall and also adds a test in the docstring to include the example reported by Felipe.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4075\n\n",
    "created_at": "2008-09-08T11:15:56Z",
    "labels": [
        "coding theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "bug in BCHCode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4075",
    "user": "@wdjoyner"
}
```
Assignee: @rlmill

This was reported by Felipe Voloch:


```
Hi,

I am not sure how to report bugs in Sage but I see you are involved
with their coding theory. I was playing around with BCH codes and
in particular I wanted the BCH code over F_5 of length 26 and designed
distance 5. Sage reports this code as having dimension 25 (see below)
but the dimension should be 10, which Magma computes correctly (see
below also).

Thanks 

Felipe

---------------------SAGE---------------------------------------------
amd13:~> sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.5, Release Date: 2008-07-11                       |
| Type notebook() for the GUI, and license() for information.        |
sage: C = BCHCode(26,5,GF(5)); C
Linear code of length 26, dimension 25 over Finite Field of size 5


---------------------MAGMA--------------------------------------------
linux182~> magma
Magma V2.14-10    Fri Sep  5 2008 14:24:48 on linux182 [Seed = 1390124479]
Type ? for help.  Type <Ctrl>-D to quit.
> > C:=BCHCode(GF(5),26,5); 
> > Dimension(C);
10
```


Incidently, Guava does this correctly. The problem is that I used the wrong element to construct the generator polynomial. 

This is fixed in the attached patch, based on 3.1.2.alpha4. It passes sage -testall and also adds a test in the docstring to include the example reported by Felipe.

Issue created by migration from https://trac.sagemath.org/ticket/4075





---

archive/issue_comments_029410.json:
```json
{
    "body": "Attachment [10463.patch](tarball://root/attachments/some-uuid/ticket4075/10463.patch) by @wdjoyner created at 2008-09-08 11:16:27\n\nbased on 3.1.2.alpha4",
    "created_at": "2008-09-08T11:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4075#issuecomment-29410",
    "user": "@wdjoyner"
}
```

Attachment [10463.patch](tarball://root/attachments/some-uuid/ticket4075/10463.patch) by @wdjoyner created at 2008-09-08 11:16:27

based on 3.1.2.alpha4



---

archive/issue_comments_029411.json:
```json
{
    "body": "If tests pass, this looks good to me.",
    "created_at": "2008-09-08T20:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4075#issuecomment-29411",
    "user": "@rlmill"
}
```

If tests pass, this looks good to me.



---

archive/issue_comments_029412.json:
```json
{
    "body": "Doctests pass in my current 3.1.2.rc1 merge tree with this patch applied. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-08T20:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4075#issuecomment-29412",
    "user": "mabshoff"
}
```

Doctests pass in my current 3.1.2.rc1 merge tree with this patch applied. Positive review.

Cheers,

Michael



---

archive/issue_comments_029413.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-08T20:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4075#issuecomment-29413",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc1



---

archive/issue_comments_029414.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-08T20:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4075#issuecomment-29414",
    "user": "mabshoff"
}
```

Resolution: fixed
