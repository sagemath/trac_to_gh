# Issue 1521: rebuilding ntl_GF2.pyx fails spectecularly on OSX 10.4 with moved install/binary install

archive/issues_001521.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\ng++ -bundle -undefined dynamic_lookup build/temp.macosx-10.3-ppc-2.5/sage/libs/ntl/ntl_GF2.o \n-L/Users/mabshoff/sage-2.9.alpha7-PowerMacintosh-Darwin/local//lib -lcsage -lcsage -lntl -lstdc++ \n-lstdc++ -lntl -o build/lib.macosx-10.3-ppc-2.5/sage/libs/ntl/ntl_GF2.so\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1521\n\n",
    "created_at": "2007-12-15T06:29:50Z",
    "labels": [
        "component: relocation",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "rebuilding ntl_GF2.pyx fails spectecularly on OSX 10.4 with moved install/binary install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1521",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
g++ -bundle -undefined dynamic_lookup build/temp.macosx-10.3-ppc-2.5/sage/libs/ntl/ntl_GF2.o 
-L/Users/mabshoff/sage-2.9.alpha7-PowerMacintosh-Darwin/local//lib -lcsage -lcsage -lntl -lstdc++ 
-lstdc++ -lntl -o build/lib.macosx-10.3-ppc-2.5/sage/libs/ntl/ntl_GF2.so
```


Issue created by migration from https://trac.sagemath.org/ticket/1521





---

archive/issue_comments_009714.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T06:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1521#issuecomment-9714",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001675.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-15T06:30:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1521",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1521#event-1675"
}
```



---

archive/issue_comments_009715.json:
```json
{
    "body": "Craig Citro was faster, see #1520.",
    "created_at": "2007-12-15T06:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1521#issuecomment-9715",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Craig Citro was faster, see #1520.



---

archive/issue_comments_009716.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-15T06:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1521#issuecomment-9716",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_009717.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-15T06:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1521#issuecomment-9717",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_001676.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-15T06:35:53Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/1521",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1521#event-1676"
}
```



---

archive/issue_events_001677.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2007-12-15T06:36:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1521",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1521#event-1677"
}
```



---

archive/issue_comments_009718.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2007-12-15T06:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1521#issuecomment-9718",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate
