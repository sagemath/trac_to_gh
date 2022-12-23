# Issue 3135: bug in solve_mod -- variable sorting

archive/issues_003135.json:
```json
{
    "body": "Assignee: was\n\n\n```\nCarlo Hamalainen: \n>  OK, but in solve_mod() perhaps the line\n>  \n>     vars.sort()\n>  \n>  should be\n>  \n>     vars.sort(cmp)\n>  \n>  so that the variables are actually sorted?\n>  \n\nYes, *that* is certainly a bug!\n\nWilliam\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3135\n\n",
    "created_at": "2008-05-08T18:21:40Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "bug in solve_mod -- variable sorting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3135",
    "user": "was"
}
```
Assignee: was


```
Carlo Hamalainen: 
>  OK, but in solve_mod() perhaps the line
>  
>     vars.sort()
>  
>  should be
>  
>     vars.sort(cmp)
>  
>  so that the variables are actually sorted?
>  

Yes, *that* is certainly a bug!

William
```


Issue created by migration from https://trac.sagemath.org/ticket/3135





---

archive/issue_comments_021778.json:
```json
{
    "body": "This is fixed by the patch up at #3124, so should be closed when #3124 gets closed.",
    "created_at": "2009-01-21T23:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3135#issuecomment-21778",
    "user": "AlexGhitza"
}
```

This is fixed by the patch up at #3124, so should be closed when #3124 gets closed.



---

archive/issue_comments_021779.json:
```json
{
    "body": "Fixed in Sage 3.3.alpha1 by merging #3124.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-23T08:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3135#issuecomment-21779",
    "user": "mabshoff"
}
```

Fixed in Sage 3.3.alpha1 by merging #3124.

Cheers,

Michael



---

archive/issue_comments_021780.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T08:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3135",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3135#issuecomment-21780",
    "user": "mabshoff"
}
```

Resolution: fixed
