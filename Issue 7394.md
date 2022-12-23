# Issue 7394: sqrt(e) causes segfaults

archive/issues_007394.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  jason\n\nmultiplying/dividing sqrt(e) with anything other than 1 causes a segfault, for example:\n\n\n```\n2*sqrt(e)\n```\n\n\ntested with source compile i686 and sagenb.org\n\nIssue created by migration from https://trac.sagemath.org/ticket/7394\n\n",
    "created_at": "2009-11-05T07:07:06Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "sqrt(e) causes segfaults",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7394",
    "user": "edrex"
}
```
Assignee: AlexGhitza

CC:  jason

multiplying/dividing sqrt(e) with anything other than 1 causes a segfault, for example:


```
2*sqrt(e)
```


tested with source compile i686 and sagenb.org

Issue created by migration from https://trac.sagemath.org/ticket/7394





---

archive/issue_comments_062180.json:
```json
{
    "body": "Pynac gets into an infinite recursion with these lines:\n\n\n```\n#141 0x00007ff794d21de6 in GiNaC::ex::construct_from_basic (other=@0x7fff450abfe6) at ex.cpp:312\n#142 0x00007ff794dc7405 in GiNaC::mul::eval (this=0x57772f0, level=<value optimized out>) at ex.h:267\n```\n",
    "created_at": "2009-11-05T14:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7394#issuecomment-62180",
    "user": "mhansen"
}
```

Pynac gets into an infinite recursion with these lines:


```
#141 0x00007ff794d21de6 in GiNaC::ex::construct_from_basic (other=@0x7fff450abfe6) at ex.cpp:312
#142 0x00007ff794dc7405 in GiNaC::mul::eval (this=0x57772f0, level=<value optimized out>) at ex.h:267
```




---

archive/issue_comments_062181.json:
```json
{
    "body": "Changing component from algebra to symbolics.",
    "created_at": "2009-11-15T13:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7394#issuecomment-62181",
    "user": "AlexGhitza"
}
```

Changing component from algebra to symbolics.



---

archive/issue_comments_062182.json:
```json
{
    "body": "Changing assignee from AlexGhitza to burcin.",
    "created_at": "2009-11-15T13:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7394#issuecomment-62182",
    "user": "AlexGhitza"
}
```

Changing assignee from AlexGhitza to burcin.



---

archive/issue_comments_062183.json:
```json
{
    "body": "This is a duplicate of #7264. The patch attached to that ticket contains this example as a doctest as well.",
    "created_at": "2009-11-22T18:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7394#issuecomment-62183",
    "user": "burcin"
}
```

This is a duplicate of #7264. The patch attached to that ticket contains this example as a doctest as well.



---

archive/issue_comments_062184.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-11-22T18:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7394#issuecomment-62184",
    "user": "burcin"
}
```

Resolution: duplicate
