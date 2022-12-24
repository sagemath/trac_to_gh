# Issue 1488: [with easy patch] fix output of symbolic vectors

archive/issues_001488.json:
```json
{
    "body": "Assignee: was\n\n\n```\n\n\nOn Dec 13, 2007 9:39 AM, pgdoyle <petergrantdoyle@gmail.com> wrote:\n> \n> The vector v2 doesn't display properly in the attached Sage output.\n> Or rather, the free module element v2.\n> (Should I be worried that I got a free module element when I expected\n> a vector, or will everything work out for the best?)\n\nVectors are elements of \"free modules\" :-).    The \"vector\" command is just\na command to create vectors. \n\nThe output of vectors with symbolic entries is crap, as you illustrate below. \nI've fixed this:\n\n    \n\n> \n> Cheers,\n> \n> Peter\n> -----------------------------------\n> sage: v1=vector([1/2,1/2])\n> sage: v1\n> (1/2, 1/2)\n> sage: type(v1)\n> <type 'sage.modules.vector_rational_dense.Vector_rational_dense'>\n> sage: v2=vector([x/(2*x),x/(2*x)])\n> sage: v2\n> (                                       1\n>                                        -\n> \n> 2,                                        1\n>                                        -\n>                                        2)\n> sage: type(v2)\n> <type\n> 'sage.modules.free_module_element.FreeModuleElement_generic_dense'>\n> sage: type(v2[1])\n> <class 'sage.calculus.calculus.SymbolicArithmetic'>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1488\n\n",
    "created_at": "2007-12-13T18:10:04Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "[with easy patch] fix output of symbolic vectors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1488",
    "user": "was"
}
```
Assignee: was


```


On Dec 13, 2007 9:39 AM, pgdoyle <petergrantdoyle@gmail.com> wrote:
> 
> The vector v2 doesn't display properly in the attached Sage output.
> Or rather, the free module element v2.
> (Should I be worried that I got a free module element when I expected
> a vector, or will everything work out for the best?)

Vectors are elements of "free modules" :-).    The "vector" command is just
a command to create vectors. 

The output of vectors with symbolic entries is crap, as you illustrate below. 
I've fixed this:

    

> 
> Cheers,
> 
> Peter
> -----------------------------------
> sage: v1=vector([1/2,1/2])
> sage: v1
> (1/2, 1/2)
> sage: type(v1)
> <type 'sage.modules.vector_rational_dense.Vector_rational_dense'>
> sage: v2=vector([x/(2*x),x/(2*x)])
> sage: v2
> (                                       1
>                                        -
> 
> 2,                                        1
>                                        -
>                                        2)
> sage: type(v2)
> <type
> 'sage.modules.free_module_element.FreeModuleElement_generic_dense'>
> sage: type(v2[1])
> <class 'sage.calculus.calculus.SymbolicArithmetic'>
```


Issue created by migration from https://trac.sagemath.org/ticket/1488





---

archive/issue_comments_009579.json:
```json
{
    "body": "Attachment [trac-1488.patch](tarball://root/attachments/some-uuid/ticket1488/trac-1488.patch) by was created at 2007-12-13 18:11:18",
    "created_at": "2007-12-13T18:11:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1488#issuecomment-9579",
    "user": "was"
}
```

Attachment [trac-1488.patch](tarball://root/attachments/some-uuid/ticket1488/trac-1488.patch) by was created at 2007-12-13 18:11:18



---

archive/issue_comments_009580.json:
```json
{
    "body": "looks good.",
    "created_at": "2007-12-13T18:14:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1488#issuecomment-9580",
    "user": "malb"
}
```

looks good.



---

archive/issue_comments_009581.json:
```json
{
    "body": "Merged in 2.9.alpha7.",
    "created_at": "2007-12-14T05:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1488#issuecomment-9581",
    "user": "mabshoff"
}
```

Merged in 2.9.alpha7.



---

archive/issue_comments_009582.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-14T05:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1488",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1488#issuecomment-9582",
    "user": "mabshoff"
}
```

Resolution: fixed
