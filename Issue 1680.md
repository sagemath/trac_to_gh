# Issue 1680: Unusual behaviour of the built-in complex numbers

archive/issues_001680.json:
```json
{
    "body": "Assignee: malb\n\nCC:  mhansen mvngu\n\nSAGE has a built-in copy of the complex numbers, so it knows what I is. However, one gets slightly odd behaviour from this:\n\n`sage: (1+I)^2 - 2*I`\n\n`(1+I)^2 - 2*I`\n\nand one has to use the .expand() command to get the correct answer 2*I. This is not the behaviour of a user-defined quadratic field, which automatically evaluates such things. I think that the computation should resolve to 0 without having to be expanded.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1680\n\n",
    "created_at": "2008-01-04T17:17:29Z",
    "labels": [
        "commutative algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Unusual behaviour of the built-in complex numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1680",
    "user": "ljpk"
}
```
Assignee: malb

CC:  mhansen mvngu

SAGE has a built-in copy of the complex numbers, so it knows what I is. However, one gets slightly odd behaviour from this:

`sage: (1+I)^2 - 2*I`

`(1+I)^2 - 2*I`

and one has to use the .expand() command to get the correct answer 2*I. This is not the behaviour of a user-defined quadratic field, which automatically evaluates such things. I think that the computation should resolve to 0 without having to be expanded.

Issue created by migration from https://trac.sagemath.org/ticket/1680





---

archive/issue_comments_010654.json:
```json
{
    "body": "This behavior of the symbolic I is imposed by Maxima.  I do not know if there is any way to change it to behave like you want.   You might want to use the I of the number field QQ(sqrt(-1))...  \n\n\n```\nsage: I = NumberField(x^2 + 1, 'I').gen()\nsage: (1+I)^2 - 2*I\n0\n```\n\n\nSome day (who knows when) probably the Sage \"I\" will be the number field I, but where the number field is equipped with a canonical embedding in the symbolic ring, and then your example above will work as you want.  I don't know when this will happen.  It might not be too hard to implement. \n\nWilliam",
    "created_at": "2008-01-14T05:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1680#issuecomment-10654",
    "user": "was"
}
```

This behavior of the symbolic I is imposed by Maxima.  I do not know if there is any way to change it to behave like you want.   You might want to use the I of the number field QQ(sqrt(-1))...  


```
sage: I = NumberField(x^2 + 1, 'I').gen()
sage: (1+I)^2 - 2*I
0
```


Some day (who knows when) probably the Sage "I" will be the number field I, but where the number field is equipped with a canonical embedding in the symbolic ring, and then your example above will work as you want.  I don't know when this will happen.  It might not be too hard to implement. 

William



---

archive/issue_comments_010655.json:
```json
{
    "body": "This is certainly on the TODO list... currently for a number field \n\n\n```\nsage: I = NumberField(x^2 + 1, 'I').gen()\n```\n\n\nit doesn't know whether to send I to -I or I in `CC`, and a mechanism for this needs to be implemented.",
    "created_at": "2008-01-15T06:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1680#issuecomment-10655",
    "user": "robertwb"
}
```

This is certainly on the TODO list... currently for a number field 


```
sage: I = NumberField(x^2 + 1, 'I').gen()
```


it doesn't know whether to send I to -I or I in `CC`, and a mechanism for this needs to be implemented.



---

archive/issue_comments_010656.json:
```json
{
    "body": "Changing assignee from malb to robertwb.",
    "created_at": "2008-01-15T06:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1680#issuecomment-10656",
    "user": "robertwb"
}
```

Changing assignee from malb to robertwb.



---

archive/issue_comments_010657.json:
```json
{
    "body": "Number fields now have embedddings, and these are used by the Pynac Symbolics. When that goes in, this ticket should be closed.",
    "created_at": "2009-05-18T22:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1680#issuecomment-10657",
    "user": "robertwb"
}
```

Number fields now have embedddings, and these are used by the Pynac Symbolics. When that goes in, this ticket should be closed.



---

archive/issue_comments_010658.json:
```json
{
    "body": "I think this can be closed now.",
    "created_at": "2009-07-22T02:26:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1680#issuecomment-10658",
    "user": "jhpalmieri"
}
```

I think this can be closed now.



---

archive/issue_comments_010659.json:
```json
{
    "body": "Please note the request to close this.",
    "created_at": "2009-10-06T19:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1680#issuecomment-10659",
    "user": "jason"
}
```

Please note the request to close this.



---

archive/issue_comments_010660.json:
```json
{
    "body": "Yep, this has been fixed.",
    "created_at": "2009-10-07T04:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1680#issuecomment-10660",
    "user": "mhansen"
}
```

Yep, this has been fixed.



---

archive/issue_comments_010661.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-07T04:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1680#issuecomment-10661",
    "user": "mhansen"
}
```

Resolution: fixed
