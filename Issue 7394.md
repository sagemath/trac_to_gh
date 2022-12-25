# Issue 7394: sqrt(e) causes segfaults

archive/issues_007394.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @jasongrout\n\nmultiplying/dividing sqrt(e) with anything other than 1 causes a segfault, for example:\n\n\n```\n2*sqrt(e)\n```\n\n\ntested with source compile i686 and sagenb.org\n\nIssue created by migration from https://trac.sagemath.org/ticket/7394\n\n",
    "created_at": "2009-11-05T07:07:06Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sqrt(e) causes segfaults",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7394",
    "user": "https://trac.sagemath.org/admin/accounts/users/edrex"
}
```
Assignee: @aghitza

CC:  @jasongrout

multiplying/dividing sqrt(e) with anything other than 1 causes a segfault, for example:


```
2*sqrt(e)
```


tested with source compile i686 and sagenb.org

Issue created by migration from https://trac.sagemath.org/ticket/7394





---

archive/issue_comments_062065.json:
```json
{
    "body": "Pynac gets into an infinite recursion with these lines:\n\n\n```\n#141 0x00007ff794d21de6 in GiNaC::ex::construct_from_basic (other=@0x7fff450abfe6) at ex.cpp:312\n#142 0x00007ff794dc7405 in GiNaC::mul::eval (this=0x57772f0, level=<value optimized out>) at ex.h:267\n```\n",
    "created_at": "2009-11-05T14:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7394#issuecomment-62065",
    "user": "https://github.com/mwhansen"
}
```

Pynac gets into an infinite recursion with these lines:


```
#141 0x00007ff794d21de6 in GiNaC::ex::construct_from_basic (other=@0x7fff450abfe6) at ex.cpp:312
#142 0x00007ff794dc7405 in GiNaC::mul::eval (this=0x57772f0, level=<value optimized out>) at ex.h:267
```




---

archive/issue_comments_062066.json:
```json
{
    "body": "Changing component from algebra to symbolics.",
    "created_at": "2009-11-15T13:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7394#issuecomment-62066",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to symbolics.



---

archive/issue_comments_062067.json:
```json
{
    "body": "Changing assignee from @aghitza to @burcin.",
    "created_at": "2009-11-15T13:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7394#issuecomment-62067",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @aghitza to @burcin.



---

archive/issue_events_017488.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2009-11-22T18:02:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7394",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7394#event-17488"
}
```



---

archive/issue_comments_062068.json:
```json
{
    "body": "This is a duplicate of #7264. The patch attached to that ticket contains this example as a doctest as well.",
    "created_at": "2009-11-22T18:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7394#issuecomment-62068",
    "user": "https://github.com/burcin"
}
```

This is a duplicate of #7264. The patch attached to that ticket contains this example as a doctest as well.



---

archive/issue_events_017489.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2009-11-22T18:02:37Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7394",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7394#event-17489"
}
```



---

archive/issue_comments_062069.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-11-22T18:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7394#issuecomment-62069",
    "user": "https://github.com/burcin"
}
```

Resolution: duplicate
