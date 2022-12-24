# Issue 4635: Sage 3.2.1.a1: numerical noise in sage/plot/plot.py

archive/issues_004635.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  jhpalmieri\n\n\n```\nFile \"/Applications/sage-3.2.1.alpha1/devel/sage/sage/plot/plot.py\",\nline 4576:\n   sage: adaptive_refinement(sin, (0,0), (pi,0),\nadaptive_tolerance=0.01)\nExpected:\n   [(0.125*pi, 0.38268343236508978), (0.1875*pi,\n0.55557023301960218), (0.25*pi, 0.70710678118654746), (0.3125*pi,\n0.83146961230254524), (0.375*pi, 0.92387953251128674), (0.4375*pi,\n0.98078528040323043), (0.5*pi, 1.0), (0.5625*pi, 0.98078528040323043),\n(0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254546),\n(0.75*pi, 0.70710678118654757), (0.8125*pi, 0.55557023301960218),\n(0.875*pi, 0.38268343236508989)]\nGot:\n   [(0.125*pi, 0.38268343236508978), (0.1875*pi,\n0.55557023301960218), (0.25*pi, 0.70710678118654746), (0.3125*pi,\n0.83146961230254512), (0.375*pi, 0.92387953251128674), (0.4375*pi,\n0.98078528040323043), (0.5*pi, 1.0), (0.5625*pi, 0.98078528040323043),\n(0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254546),\n(0.75*pi, 0.70710678118654757), (0.8125*pi, 0.55557023301960218),\n(0.875*pi, 0.38268343236508984)]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4635\n\n",
    "created_at": "2008-11-27T03:44:10Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "Sage 3.2.1.a1: numerical noise in sage/plot/plot.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4635",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  jhpalmieri


```
File "/Applications/sage-3.2.1.alpha1/devel/sage/sage/plot/plot.py",
line 4576:
   sage: adaptive_refinement(sin, (0,0), (pi,0),
adaptive_tolerance=0.01)
Expected:
   [(0.125*pi, 0.38268343236508978), (0.1875*pi,
0.55557023301960218), (0.25*pi, 0.70710678118654746), (0.3125*pi,
0.83146961230254524), (0.375*pi, 0.92387953251128674), (0.4375*pi,
0.98078528040323043), (0.5*pi, 1.0), (0.5625*pi, 0.98078528040323043),
(0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254546),
(0.75*pi, 0.70710678118654757), (0.8125*pi, 0.55557023301960218),
(0.875*pi, 0.38268343236508989)]
Got:
   [(0.125*pi, 0.38268343236508978), (0.1875*pi,
0.55557023301960218), (0.25*pi, 0.70710678118654746), (0.3125*pi,
0.83146961230254512), (0.375*pi, 0.92387953251128674), (0.4375*pi,
0.98078528040323043), (0.5*pi, 1.0), (0.5625*pi, 0.98078528040323043),
(0.625*pi, 0.92387953251128674), (0.6875*pi, 0.83146961230254546),
(0.75*pi, 0.70710678118654757), (0.8125*pi, 0.55557023301960218),
(0.875*pi, 0.38268343236508984)]
```


Issue created by migration from https://trac.sagemath.org/ticket/4635





---

archive/issue_comments_034851.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-27T04:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4635#issuecomment-34851",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034852.json:
```json
{
    "body": "The problem is this:\n\n```\n0.83146961230254524), (0.375*pi, 0.92387953251128674), (0.4375*pi,\n0.83146961230254512), (0.375*pi, 0.92387953251128674), (0.4375*pi,\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T04:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4635#issuecomment-34852",
    "user": "mabshoff"
}
```

The problem is this:

```
0.83146961230254524), (0.375*pi, 0.92387953251128674), (0.4375*pi,
0.83146961230254512), (0.375*pi, 0.92387953251128674), (0.4375*pi,
```


Cheers,

Michael



---

archive/issue_comments_034853.json:
```json
{
    "body": "Attachment [trac_4635.patch](tarball://root/attachments/some-uuid/ticket4635/trac_4635.patch) by mabshoff created at 2008-11-27 04:16:22",
    "created_at": "2008-11-27T04:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4635#issuecomment-34853",
    "user": "mabshoff"
}
```

Attachment [trac_4635.patch](tarball://root/attachments/some-uuid/ticket4635/trac_4635.patch) by mabshoff created at 2008-11-27 04:16:22



---

archive/issue_comments_034854.json:
```json
{
    "body": "Fine by me.",
    "created_at": "2008-11-27T04:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4635#issuecomment-34854",
    "user": "ncalexan"
}
```

Fine by me.



---

archive/issue_comments_034855.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha2",
    "created_at": "2008-11-27T04:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4635#issuecomment-34855",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha2



---

archive/issue_comments_034856.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-27T04:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4635#issuecomment-34856",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034857.json:
```json
{
    "body": "Wait, it doesn't work for me!  The very last digit differs in the two cases -- see the output in the description of the ticket.",
    "created_at": "2008-11-27T04:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4635#issuecomment-34857",
    "user": "jhpalmieri"
}
```

Wait, it doesn't work for me!  The very last digit differs in the two cases -- see the output in the description of the ticket.



---

archive/issue_comments_034858.json:
```json
{
    "body": "Replying to [comment:4 jhpalmieri]:\n> Wait, it doesn't work for me!  The very last digit differs in the two cases -- see the output in the description of the ticket.\n> \n> \n\nOk, I will recheck and post an patch on top.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T04:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4635#issuecomment-34858",
    "user": "mabshoff"
}
```

Replying to [comment:4 jhpalmieri]:
> Wait, it doesn't work for me!  The very last digit differs in the two cases -- see the output in the description of the ticket.
> 
> 

Ok, I will recheck and post an patch on top.

Cheers,

Michael



---

archive/issue_comments_034859.json:
```json
{
    "body": "Indeed: the last line is different, too:\n\n```\n(0.875*pi, 0.38268343236508989)]\n(0.875*pi, 0.38268343236508984)]\n```\n\nI will recheck all of it again - patch coming up.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T04:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4635#issuecomment-34859",
    "user": "mabshoff"
}
```

Indeed: the last line is different, too:

```
(0.875*pi, 0.38268343236508989)]
(0.875*pi, 0.38268343236508984)]
```

I will recheck all of it again - patch coming up.

Cheers,

Michael



---

archive/issue_comments_034860.json:
```json
{
    "body": "this replaces the old patch",
    "created_at": "2008-11-27T04:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4635#issuecomment-34860",
    "user": "jhpalmieri"
}
```

this replaces the old patch



---

archive/issue_comments_034861.json:
```json
{
    "body": "Attachment [4635-new.patch](tarball://root/attachments/some-uuid/ticket4635/4635-new.patch) by jhpalmieri created at 2008-11-27 04:27:44\n\nHere's a patch.",
    "created_at": "2008-11-27T04:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4635#issuecomment-34861",
    "user": "jhpalmieri"
}
```

Attachment [4635-new.patch](tarball://root/attachments/some-uuid/ticket4635/4635-new.patch) by jhpalmieri created at 2008-11-27 04:27:44

Here's a patch.



---

archive/issue_comments_034862.json:
```json
{
    "body": "Replying to [comment:7 jhpalmieri]:\n> Here's a patch.\n\nThanks for the patch. I had already applied mine, but I will rebase your patch relative to my fix.\n\nPositive review for John's patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T04:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4635#issuecomment-34862",
    "user": "mabshoff"
}
```

Replying to [comment:7 jhpalmieri]:
> Here's a patch.

Thanks for the patch. I had already applied mine, but I will rebase your patch relative to my fix.

Positive review for John's patch.

Cheers,

Michael



---

archive/issue_comments_034863.json:
```json
{
    "body": "I also merged John's additional fix from 4635-new.patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-27T04:49:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4635",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4635#issuecomment-34863",
    "user": "mabshoff"
}
```

I also merged John's additional fix from 4635-new.patch.

Cheers,

Michael
