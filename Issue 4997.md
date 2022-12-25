# Issue 4997: OSX64/Cygwin: fix memory.so import issue during doctesting

archive/issues_004997.json:
```json
{
    "body": "Assignee: mabshoff\n\nWhen doctesting a 64 bit OSX build of Sage we have these failures for every doctest:\n\n```\nsage -t  \"devel/sage/sage/rings/complex_interval_field.py\"  \nTraceback (most recent call last):\n  File \"/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/tmp/complex_interval_field.py\", line 2, in <module>\n    from sage.all_cmdline import *; \n  File \"/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/all_cmdline.py\", line 14, in <module>\n    from sage.all import *\n  File \"/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/all.py\", line 56, in <module>\n    from sage.rings.memory import pmem_malloc\nImportError: dlopen(/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/rings/memory.so, 2): Symbol not found: _rand_n\n  Referenced from: /Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/rings/memory.so\n  Expected in: dynamic lookup\n```\n\nThe fix is to link the first library to be imported against libcsage:\n\n```\n--- a/module_list.py    Mon Jan 05 23:03:45 2009 -0800\n+++ b/module_list.py    Tue Jan 06 17:13:03 2009 -0800\n@@ -854,7 +854,7 @@\n \n     Extension('sage.rings.memory',\n               sources = ['sage/rings/memory.pyx'],\n-              libraries=['gmp','stdc++']),\n+              libraries=['csage','ntl','gmp','stdc++']),\n \n     Extension('sage.rings.morphism',\n               sources = ['sage/rings/morphism.pyx']),\n```\n\nThis fix is also needed on Cygwin.\n\nA proper patch is coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4997\n\n",
    "created_at": "2009-01-17T15:41:29Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "OSX64/Cygwin: fix memory.so import issue during doctesting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4997",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

When doctesting a 64 bit OSX build of Sage we have these failures for every doctest:

```
sage -t  "devel/sage/sage/rings/complex_interval_field.py"  
Traceback (most recent call last):
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/tmp/complex_interval_field.py", line 2, in <module>
    from sage.all_cmdline import *; 
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/all_cmdline.py", line 14, in <module>
    from sage.all import *
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/all.py", line 56, in <module>
    from sage.rings.memory import pmem_malloc
ImportError: dlopen(/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/rings/memory.so, 2): Symbol not found: _rand_n
  Referenced from: /Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/rings/memory.so
  Expected in: dynamic lookup
```

The fix is to link the first library to be imported against libcsage:

```
--- a/module_list.py    Mon Jan 05 23:03:45 2009 -0800
+++ b/module_list.py    Tue Jan 06 17:13:03 2009 -0800
@@ -854,7 +854,7 @@
 
     Extension('sage.rings.memory',
               sources = ['sage/rings/memory.pyx'],
-              libraries=['gmp','stdc++']),
+              libraries=['csage','ntl','gmp','stdc++']),
 
     Extension('sage.rings.morphism',
               sources = ['sage/rings/morphism.pyx']),
```

This fix is also needed on Cygwin.

A proper patch is coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4997





---

archive/issue_comments_038051.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-17T15:41:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4997#issuecomment-38051",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_events_005241.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-06T23:22:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4997",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4997#event-5241"
}
```



---

archive/issue_comments_038052.json:
```json
{
    "body": "This is not needed, I am not sure what happened. Either way: invalid.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T23:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4997#issuecomment-38052",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is not needed, I am not sure what happened. Either way: invalid.

Cheers,

Michael



---

archive/issue_comments_038053.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-02-06T23:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4997#issuecomment-38053",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid
