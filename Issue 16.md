# Issue 16: failures building optional packages

archive/issues_000016.json:
```json
{
    "body": "Assignee: somebody\n\n* Building optional packages under OS X Intel (status report on 08-25-06 by William Stein)\n   Everything works except the following --\n      * dvipng doesn't build (but shouldn't be needed, since this comes with tex)\n      * RealLib3 -- fails with \"LongFloat.cpp:6:20: error: malloc.h: No such file or directory\"\n      * numpy-2006-08-16.spkg -- fails with \"KeyError: 'linker_exe'\"\n      * scipy-2006-08-16.spkg -- depends on numpy\n      * soya-0.11.2.p0.spkg -- fails to find GL/glew.h  (soya is probably very hard to build in OSX...)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/16\n\n",
    "created_at": "2006-09-12T23:17:16Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "title": "failures building optional packages",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/16",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

* Building optional packages under OS X Intel (status report on 08-25-06 by William Stein)
   Everything works except the following --
      * dvipng doesn't build (but shouldn't be needed, since this comes with tex)
      * RealLib3 -- fails with "LongFloat.cpp:6:20: error: malloc.h: No such file or directory"
      * numpy-2006-08-16.spkg -- fails with "KeyError: 'linker_exe'"
      * scipy-2006-08-16.spkg -- depends on numpy
      * soya-0.11.2.p0.spkg -- fails to find GL/glew.h  (soya is probably very hard to build in OSX...)


Issue created by migration from https://trac.sagemath.org/ticket/16





---

archive/issue_comments_000068.json:
```json
{
    "body": "```\n  * numpy and scipy now fixed\n  * soya is not and never will be supported\n```",
    "created_at": "2007-01-12T21:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/16",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/16#issuecomment-68",
    "user": "https://github.com/williamstein"
}
```

```
  * numpy and scipy now fixed
  * soya is not and never will be supported
```



---

archive/issue_comments_000069.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-01-12T21:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/16",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/16#issuecomment-69",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_000070.json:
```json
{
    "body": "fixed.",
    "created_at": "2007-08-09T21:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/16",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/16#issuecomment-70",
    "user": "https://github.com/malb"
}
```

fixed.



---

archive/issue_comments_000071.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-09T21:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/16",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/16#issuecomment-71",
    "user": "https://github.com/malb"
}
```

Resolution: fixed



---

archive/issue_events_000025.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-08-09T21:52:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/16",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/16#event-25"
}
```
