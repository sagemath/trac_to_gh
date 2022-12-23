# Issue 3530: [with patch, needs review] documentation for clib, cinclude pragmas

archive/issues_003530.json:
```json
{
    "body": "Assignee: malb\n\nCC:  craigcitro wstein\n\nKeywords: cython, documentation\n\nCraig wrote off list:\n> hey martin -- william tells me you created these pragmas for .spyx\n> files. can you document them somewhere?\n\nThis patch documents the pragmas in the docstring. I also changed the behaviour of atlas() which now assumes that ATLAS is installed, since we ship it. mabshoff/wstein please check if my assumption is correct e.g. on OSX.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3530\n\n",
    "created_at": "2008-06-28T14:45:26Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] documentation for clib, cinclude pragmas",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3530",
    "user": "malb"
}
```
Assignee: malb

CC:  craigcitro wstein

Keywords: cython, documentation

Craig wrote off list:
> hey martin -- william tells me you created these pragmas for .spyx
> files. can you document them somewhere?

This patch documents the pragmas in the docstring. I also changed the behaviour of atlas() which now assumes that ATLAS is installed, since we ship it. mabshoff/wstein please check if my assumption is correct e.g. on OSX.

Issue created by migration from https://trac.sagemath.org/ticket/3530





---

archive/issue_comments_024896.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-06-28T14:45:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24896",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_024897.json:
```json
{
    "body": "Craig can you review my patch?",
    "created_at": "2008-07-02T20:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24897",
    "user": "malb"
}
```

Craig can you review my patch?



---

archive/issue_comments_024898.json:
```json
{
    "body": "I'm on it.",
    "created_at": "2008-07-02T22:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24898",
    "user": "craigcitro"
}
```

I'm on it.



---

archive/issue_comments_024899.json:
```json
{
    "body": "This looks great. I've already updated the note on `wiki.sagemath.org` to include a reference to this docstring for more info. \n\nI also don't know the answer to Martin's question about ATLAS -- mabshoff or wstein, do you want to answer that?",
    "created_at": "2008-07-04T23:52:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24899",
    "user": "craigcitro"
}
```

This looks great. I've already updated the note on `wiki.sagemath.org` to include a reference to this docstring for more info. 

I also don't know the answer to Martin's question about ATLAS -- mabshoff or wstein, do you want to answer that?



---

archive/issue_comments_024900.json:
```json
{
    "body": "The patch will break some functionality since SAGE_CBLAS is no longer checked. I also tend to think that on OSX the whole BLAS function has not worked and will not ever work as is, so I would recommend splitting that part off to another ticket and dealing with it there. I can merge the \"good\" part and open another ticket for the \"bad\" part of the patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-05T22:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24900",
    "user": "mabshoff"
}
```

The patch will break some functionality since SAGE_CBLAS is no longer checked. I also tend to think that on OSX the whole BLAS function has not worked and will not ever work as is, so I would recommend splitting that part off to another ticket and dealing with it there. I can merge the "good" part and open another ticket for the "bad" part of the patch.

Cheers,

Michael



---

archive/issue_comments_024901.json:
```json
{
    "body": "I'm all for splitting, so please go ahead. Actually, I don't think that this patch breaks anything it just reveals something that was broken for some time now.",
    "created_at": "2008-07-06T11:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24901",
    "user": "malb"
}
```

I'm all for splitting, so please go ahead. Actually, I don't think that this patch breaks anything it just reveals something that was broken for some time now.



---

archive/issue_comments_024902.json:
```json
{
    "body": "Since I agree with malb I will merge the patch as is and have opened #3563 to deal with the issue on OSX.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-06T12:04:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24902",
    "user": "mabshoff"
}
```

Since I agree with malb I will merge the patch as is and have opened #3563 to deal with the issue on OSX.

Cheers,

Michael



---

archive/issue_comments_024903.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-06T18:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24903",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha2



---

archive/issue_comments_024904.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-06T18:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24904",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024905.json:
```json
{
    "body": "Attachment\n\nOops, somebody forgot to doctest on his install :)",
    "created_at": "2008-07-06T18:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24905",
    "user": "mabshoff"
}
```

Attachment

Oops, somebody forgot to doctest on his install :)



---

archive/issue_comments_024906.json:
```json
{
    "body": "Looks good. *sheepishly*: I actually doctested it this time. :)",
    "created_at": "2008-07-06T19:05:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3530",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3530#issuecomment-24906",
    "user": "craigcitro"
}
```

Looks good. *sheepishly*: I actually doctested it this time. :)
