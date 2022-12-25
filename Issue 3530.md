# Issue 3530: [with patch, needs review] documentation for clib, cinclude pragmas

archive/issues_003530.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @craigcitro wstein\n\nKeywords: cython, documentation\n\nCraig wrote off list:\n> hey martin -- william tells me you created these pragmas for .spyx\n> files. can you document them somewhere?\n\nThis patch documents the pragmas in the docstring. I also changed the behaviour of atlas() which now assumes that ATLAS is installed, since we ship it. mabshoff/wstein please check if my assumption is correct e.g. on OSX.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3530\n\n",
    "created_at": "2008-06-28T14:45:26Z",
    "labels": [
        "component: misc",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, needs review] documentation for clib, cinclude pragmas",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3530",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @craigcitro wstein

Keywords: cython, documentation

Craig wrote off list:
> hey martin -- william tells me you created these pragmas for .spyx
> files. can you document them somewhere?

This patch documents the pragmas in the docstring. I also changed the behaviour of atlas() which now assumes that ATLAS is installed, since we ship it. mabshoff/wstein please check if my assumption is correct e.g. on OSX.

Issue created by migration from https://trac.sagemath.org/ticket/3530





---

archive/issue_comments_024847.json:
```json
{
    "body": "Attachment [clib_pragmas.patch](tarball://root/attachments/some-uuid/ticket3530/clib_pragmas.patch) by @malb created at 2008-06-28 14:45:47",
    "created_at": "2008-06-28T14:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24847",
    "user": "https://github.com/malb"
}
```

Attachment [clib_pragmas.patch](tarball://root/attachments/some-uuid/ticket3530/clib_pragmas.patch) by @malb created at 2008-06-28 14:45:47



---

archive/issue_comments_024848.json:
```json
{
    "body": "Craig can you review my patch?",
    "created_at": "2008-07-02T20:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24848",
    "user": "https://github.com/malb"
}
```

Craig can you review my patch?



---

archive/issue_comments_024849.json:
```json
{
    "body": "I'm on it.",
    "created_at": "2008-07-02T22:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24849",
    "user": "https://github.com/craigcitro"
}
```

I'm on it.



---

archive/issue_comments_024850.json:
```json
{
    "body": "This looks great. I've already updated the note on `wiki.sagemath.org` to include a reference to this docstring for more info. \n\nI also don't know the answer to Martin's question about ATLAS -- mabshoff or wstein, do you want to answer that?",
    "created_at": "2008-07-04T23:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24850",
    "user": "https://github.com/craigcitro"
}
```

This looks great. I've already updated the note on `wiki.sagemath.org` to include a reference to this docstring for more info. 

I also don't know the answer to Martin's question about ATLAS -- mabshoff or wstein, do you want to answer that?



---

archive/issue_comments_024851.json:
```json
{
    "body": "The patch will break some functionality since SAGE_CBLAS is no longer checked. I also tend to think that on OSX the whole BLAS function has not worked and will not ever work as is, so I would recommend splitting that part off to another ticket and dealing with it there. I can merge the \"good\" part and open another ticket for the \"bad\" part of the patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-05T22:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24851",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch will break some functionality since SAGE_CBLAS is no longer checked. I also tend to think that on OSX the whole BLAS function has not worked and will not ever work as is, so I would recommend splitting that part off to another ticket and dealing with it there. I can merge the "good" part and open another ticket for the "bad" part of the patch.

Cheers,

Michael



---

archive/issue_comments_024852.json:
```json
{
    "body": "I'm all for splitting, so please go ahead. Actually, I don't think that this patch breaks anything it just reveals something that was broken for some time now.",
    "created_at": "2008-07-06T11:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24852",
    "user": "https://github.com/malb"
}
```

I'm all for splitting, so please go ahead. Actually, I don't think that this patch breaks anything it just reveals something that was broken for some time now.



---

archive/issue_comments_024853.json:
```json
{
    "body": "Since I agree with malb I will merge the patch as is and have opened #3563 to deal with the issue on OSX.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T12:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24853",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Since I agree with malb I will merge the patch as is and have opened #3563 to deal with the issue on OSX.

Cheers,

Michael



---

archive/issue_comments_024854.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-06T18:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24854",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha2



---

archive/issue_comments_024855.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-06T18:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24855",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024856.json:
```json
{
    "body": "Attachment [trac_3530_clib_pragmas-doctest-fixes.patch](tarball://root/attachments/some-uuid/ticket3530/trac_3530_clib_pragmas-doctest-fixes.patch) by mabshoff created at 2008-07-06 18:55:04\n\nOops, somebody forgot to doctest on his install :)",
    "created_at": "2008-07-06T18:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24856",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_3530_clib_pragmas-doctest-fixes.patch](tarball://root/attachments/some-uuid/ticket3530/trac_3530_clib_pragmas-doctest-fixes.patch) by mabshoff created at 2008-07-06 18:55:04

Oops, somebody forgot to doctest on his install :)



---

archive/issue_comments_024857.json:
```json
{
    "body": "Looks good. *sheepishly*: I actually doctested it this time. :)",
    "created_at": "2008-07-06T19:05:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24857",
    "user": "https://github.com/craigcitro"
}
```

Looks good. *sheepishly*: I actually doctested it this time. :)
