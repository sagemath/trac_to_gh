# Issue 1521: rebuilding ntl_GF2.pyx fails spectecularly on OSX 10.4 with moved install/binary install

archive/issues_001521.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\ng++ -bundle -undefined dynamic_lookup build/temp.macosx-10.3-ppc-2.5/sage/libs/ntl/ntl_GF2.o \n-L/Users/mabshoff/sage-2.9.alpha7-PowerMacintosh-Darwin/local//lib -lcsage -lcsage -lntl -lstdc++ \n-lstdc++ -lntl -o build/lib.macosx-10.3-ppc-2.5/sage/libs/ntl/ntl_GF2.so\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1521\n\n",
    "created_at": "2007-12-15T06:29:50Z",
    "labels": [
        "relocation",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "rebuilding ntl_GF2.pyx fails spectecularly on OSX 10.4 with moved install/binary install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1521",
    "user": "mabshoff"
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

archive/issue_comments_009739.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T06:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1521#issuecomment-9739",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009740.json:
```json
{
    "body": "Craig Citro was faster, see #1520.",
    "created_at": "2007-12-15T06:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1521#issuecomment-9740",
    "user": "mabshoff"
}
```

Craig Citro was faster, see #1520.



---

archive/issue_comments_009741.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-12-15T06:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1521#issuecomment-9741",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_009742.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-12-15T06:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1521#issuecomment-9742",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_009743.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2007-12-15T06:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1521#issuecomment-9743",
    "user": "mabshoff"
}
```

Resolution: duplicate
