# Issue 2720: Sage 2.11.alpha2: fix documentation build issues

archive/issues_002720.json:
```json
{
    "body": "Assignee: tba\n\nI got a patch for this. Coming up shortly.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2720\n\n",
    "created_at": "2008-03-29T17:12:34Z",
    "labels": [
        "documentation",
        "blocker",
        "bug"
    ],
    "title": "Sage 2.11.alpha2: fix documentation build issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2720",
    "user": "mabshoff"
}
```
Assignee: tba

I got a patch for this. Coming up shortly.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2720





---

archive/issue_comments_018751.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-29T17:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2720#issuecomment-18751",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018752.json:
```json
{
    "body": "Changing assignee from tba to mabshoff.",
    "created_at": "2008-03-29T17:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2720#issuecomment-18752",
    "user": "mabshoff"
}
```

Changing assignee from tba to mabshoff.



---

archive/issue_comments_018753.json:
```json
{
    "body": "Attachment [trac_2720.patch](tarball://root/attachments/some-uuid/ticket2720/trac_2720.patch) by mabshoff created at 2008-03-29 17:28:59\n\nThere is one hunk in the patch I am unhappy with:\n\n```\n295\t \t            sage: pf._str_() \n296\t \t            '_application PolyhedralFan\\n_version 2.2\\n_type PolyhedralFan\\n\n\\nAMBIENT_DIM\\n3\\n\\nDIM\\n3\\n\\nLINEALITY_DIM\\n0\\n\\nRAYS\\n1 0 0\\t# 0\\n0 1 0\\t# 1\\n0 0 1\\t# \n2\\n\\nN_RAYS\\n3\\n\\nLINEALITY_SPACE\\n\\nORTH_LINEALITY_SPACE\\n0 0 1\\n0 1 0\\n1 0 0\\n\\nF_VECTOR\\n1 \n3 1\\n\\nCONES\\n{}\\t# Dimension 0\\n{0}\\t# Dimension 1\\n{1}\\n{2}\\n{0 1}\\t# Dimension 2\\n{0 2}\\n{1 \n2}\\n{0 1 2}\\t# Dimension 3\\n\\nMAXIMAL_CONES\\n{0 1 2}\\t# Dimension 3\\n\\nPURE\\n1\\n' \n \t295\t            sage: len(pf._str_()) \n \t296\t            369 \n```\n\nThe output from `pf._str_()` doesn't play nice with TeX at all due to the `#` characters. I see no other elegant workaround for this issue but to just test the lenght of the output. \n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-03-29T17:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2720#issuecomment-18753",
    "user": "mabshoff"
}
```

Attachment [trac_2720.patch](tarball://root/attachments/some-uuid/ticket2720/trac_2720.patch) by mabshoff created at 2008-03-29 17:28:59

There is one hunk in the patch I am unhappy with:

```
295	 	            sage: pf._str_() 
296	 	            '_application PolyhedralFan\n_version 2.2\n_type PolyhedralFan\n
\nAMBIENT_DIM\n3\n\nDIM\n3\n\nLINEALITY_DIM\n0\n\nRAYS\n1 0 0\t# 0\n0 1 0\t# 1\n0 0 1\t# 
2\n\nN_RAYS\n3\n\nLINEALITY_SPACE\n\nORTH_LINEALITY_SPACE\n0 0 1\n0 1 0\n1 0 0\n\nF_VECTOR\n1 
3 1\n\nCONES\n{}\t# Dimension 0\n{0}\t# Dimension 1\n{1}\n{2}\n{0 1}\t# Dimension 2\n{0 2}\n{1 
2}\n{0 1 2}\t# Dimension 3\n\nMAXIMAL_CONES\n{0 1 2}\t# Dimension 3\n\nPURE\n1\n' 
 	295	            sage: len(pf._str_()) 
 	296	            369 
```

The output from `pf._str_()` doesn't play nice with TeX at all due to the `#` characters. I see no other elegant workaround for this issue but to just test the lenght of the output. 

Thoughts?

Cheers,

Michael



---

archive/issue_comments_018754.json:
```json
{
    "body": "Attachment [trac_2720-followup.patch](tarball://root/attachments/some-uuid/ticket2720/trac_2720-followup.patch) by mabshoff created at 2008-03-29 17:54:56",
    "created_at": "2008-03-29T17:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2720#issuecomment-18754",
    "user": "mabshoff"
}
```

Attachment [trac_2720-followup.patch](tarball://root/attachments/some-uuid/ticket2720/trac_2720-followup.patch) by mabshoff created at 2008-03-29 17:54:56



---

archive/issue_comments_018755.json:
```json
{
    "body": "Replying to [comment:2 mabshoff]:\n> There is one hunk in the patch I am unhappy with:\n> {{{\n> 295\t \t            sage: pf._str_() \n> 296\t \t            '_application PolyhedralFan\\n_version 2.2\\n_type PolyhedralFan\\n\n> \\nAMBIENT_DIM\\n3\\n\\nDIM\\n3\\n\\nLINEALITY_DIM\\n0\\n\\nRAYS\\n1 0 0\\t# 0\\n0 1 0\\t# 1\\n0 0 1\\t# \n> 2\\n\\nN_RAYS\\n3\\n\\nLINEALITY_SPACE\\n\\nORTH_LINEALITY_SPACE\\n0 0 1\\n0 1 0\\n1 0 0\\n\\nF_VECTOR\\n1 \n> 3 1\\n\\nCONES\\n{}\\t# Dimension 0\\n{0}\\t# Dimension 1\\n{1}\\n{2}\\n{0 1}\\t# Dimension 2\\n{0 2}\\n{1 \n> 2}\\n{0 1 2}\\t# Dimension 3\\n\\nMAXIMAL_CONES\\n{0 1 2}\\t# Dimension 3\\n\\nPURE\\n1\\n' \n>  \t295\t            sage: len(pf._str_()) \n>  \t296\t            369 \n> }}}\n> The output from `pf._str_()` doesn't play nice with TeX at all due to the `#` characters. I see no other elegant workaround for this issue but to just test the lenght of the output. \n\nThanks to some input from cwitty I fixed the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-29T17:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2720#issuecomment-18755",
    "user": "mabshoff"
}
```

Replying to [comment:2 mabshoff]:
> There is one hunk in the patch I am unhappy with:
> {{{
> 295	 	            sage: pf._str_() 
> 296	 	            '_application PolyhedralFan\n_version 2.2\n_type PolyhedralFan\n
> \nAMBIENT_DIM\n3\n\nDIM\n3\n\nLINEALITY_DIM\n0\n\nRAYS\n1 0 0\t# 0\n0 1 0\t# 1\n0 0 1\t# 
> 2\n\nN_RAYS\n3\n\nLINEALITY_SPACE\n\nORTH_LINEALITY_SPACE\n0 0 1\n0 1 0\n1 0 0\n\nF_VECTOR\n1 
> 3 1\n\nCONES\n{}\t# Dimension 0\n{0}\t# Dimension 1\n{1}\n{2}\n{0 1}\t# Dimension 2\n{0 2}\n{1 
> 2}\n{0 1 2}\t# Dimension 3\n\nMAXIMAL_CONES\n{0 1 2}\t# Dimension 3\n\nPURE\n1\n' 
>  	295	            sage: len(pf._str_()) 
>  	296	            369 
> }}}
> The output from `pf._str_()` doesn't play nice with TeX at all due to the `#` characters. I see no other elegant workaround for this issue but to just test the lenght of the output. 

Thanks to some input from cwitty I fixed the issue.

Cheers,

Michael



---

archive/issue_comments_018756.json:
```json
{
    "body": "Based only on reading the patches, these two patches look good.",
    "created_at": "2008-03-29T18:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2720#issuecomment-18756",
    "user": "cwitty"
}
```

Based only on reading the patches, these two patches look good.



---

archive/issue_comments_018757.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T18:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2720#issuecomment-18757",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018758.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T18:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2720",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2720#issuecomment-18758",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.rc0
