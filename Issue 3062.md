# Issue 3062: implement __oct__ special method for the integers

archive/issues_003062.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\n>  oct(2345) fails in Sage (but works in Python)\n>  oct(int(2345)) works\n>  hex(2345) works\n>  \n>  Irc said it was the preparser. Why would the input of oct be preparsed\n>  correctly and not that of hex ?\n\nI think you asked this question backwards.  Anyway, the problem\nis that nobody implemented __oct__ for Sage integers, but they\ndid implement __hex__.  Note that oct(...) calls __oct__:\n\nsage: a = 2345\nsage: a.__hex__()\n'929'\nsage: a.__oct__()\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/Users/was/<ipython console> in <module>()\n\n<type 'exceptions.AttributeError'>: 'sage.rings.integer.Integer' object has no attribute '__oct__'\n\nIn the meantime you can do either\n\nsage: oct(int(a))\n'04451'\n\nor\n\nsage: a.digits(8)\n[1, 5, 4, 4]\n\nor\n\nsage: a.str(base=8)\n'4451'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3062\n\n",
    "created_at": "2008-04-30T14:35:57Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "implement __oct__ special method for the integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3062",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody


```
>  oct(2345) fails in Sage (but works in Python)
>  oct(int(2345)) works
>  hex(2345) works
>  
>  Irc said it was the preparser. Why would the input of oct be preparsed
>  correctly and not that of hex ?

I think you asked this question backwards.  Anyway, the problem
is that nobody implemented __oct__ for Sage integers, but they
did implement __hex__.  Note that oct(...) calls __oct__:

sage: a = 2345
sage: a.__hex__()
'929'
sage: a.__oct__()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'sage.rings.integer.Integer' object has no attribute '__oct__'

In the meantime you can do either

sage: oct(int(a))
'04451'

or

sage: a.digits(8)
[1, 5, 4, 4]

or

sage: a.str(base=8)
'4451'
```


Issue created by migration from https://trac.sagemath.org/ticket/3062





---

archive/issue_comments_021094.json:
```json
{
    "body": "Code looks okay to me but the documentation could do with improvement. \"Numerial\" is not a word. Also I'd like some explanation that the behaviour is *different* from the behaviour on python ints and doctests illustrating the difference, since this is likely to be confusing (i.e. for python ints you get a prepended 0, but not for sage ints). See the documentation of `Integer.__hex__` for an example. Also I want to see an example with negative numbers.",
    "created_at": "2008-05-01T05:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3062#issuecomment-21094",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Code looks okay to me but the documentation could do with improvement. "Numerial" is not a word. Also I'd like some explanation that the behaviour is *different* from the behaviour on python ints and doctests illustrating the difference, since this is likely to be confusing (i.e. for python ints you get a prepended 0, but not for sage ints). See the documentation of `Integer.__hex__` for an example. Also I want to see an example with negative numbers.



---

archive/issue_comments_021095.json:
```json
{
    "body": "Improved documentation per David's review.",
    "created_at": "2008-05-01T05:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3062#issuecomment-21095",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Improved documentation per David's review.



---

archive/issue_comments_021096.json:
```json
{
    "body": "Tim, there are still no examples showing what happens with plain python ints. I mean like\n\n\n```\nsage: oct(int(10))\n'012'\n```\n\n\nvs oct(Integer(10))",
    "created_at": "2008-05-01T05:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3062#issuecomment-21096",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Tim, there are still no examples showing what happens with plain python ints. I mean like


```
sage: oct(int(10))
'012'
```


vs oct(Integer(10))



---

archive/issue_comments_021097.json:
```json
{
    "body": "Added examples showing difference between int and Integer oct behavior per David's request.",
    "created_at": "2008-05-01T06:03:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3062#issuecomment-21097",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Added examples showing difference between int and Integer oct behavior per David's request.



---

archive/issue_comments_021098.json:
```json
{
    "body": "Tim... I don't understand now why you have *two* EXAMPLES blocks, and moreover one of them is contained inside the latex \\note block! Why not just keep it simple? Just one block of examples, showing all the key issues, and don't put them inside the latex tags! :-)",
    "created_at": "2008-05-01T06:10:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3062#issuecomment-21098",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Tim... I don't understand now why you have *two* EXAMPLES blocks, and moreover one of them is contained inside the latex \note block! Why not just keep it simple? Just one block of examples, showing all the key issues, and don't put them inside the latex tags! :-)



---

archive/issue_comments_021099.json:
```json
{
    "body": "Attachment [3062_flatten.patch](tarball://root/attachments/some-uuid/ticket3062/3062_flatten.patch) by TimothyClemans created at 2008-05-01 06:30:01",
    "created_at": "2008-05-01T06:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3062#issuecomment-21099",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [3062_flatten.patch](tarball://root/attachments/some-uuid/ticket3062/3062_flatten.patch) by TimothyClemans created at 2008-05-01 06:30:01



---

archive/issue_comments_021100.json:
```json
{
    "body": "Flatten the patches and merged the two example blocks per David's review.",
    "created_at": "2008-05-01T06:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3062#issuecomment-21100",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Flatten the patches and merged the two example blocks per David's review.



---

archive/issue_comments_021101.json:
```json
{
    "body": "Ok this is fine.\n\nNote to release manager: only apply the last patch (3062_flatten.patch).",
    "created_at": "2008-05-01T15:30:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3062#issuecomment-21101",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Ok this is fine.

Note to release manager: only apply the last patch (3062_flatten.patch).



---

archive/issue_comments_021102.json:
```json
{
    "body": "Merged in Sage 3.0.1.rc0",
    "created_at": "2008-05-02T12:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3062#issuecomment-21102",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.rc0



---

archive/issue_comments_021103.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-02T12:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3062#issuecomment-21103",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
