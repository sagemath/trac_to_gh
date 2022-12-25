# Issue 5475: make it so ipython isn't imported when one does "sage -python"

archive/issues_005475.json:
```json
{
    "body": "Assignee: @williamstein\n\nIf one wants to use Sage from a C program, e.g., like this (see below), then it's important that \"from sage.all import *\" not import Ipython.  The point of this ticket is make the import of IPython lazy -- and only happen if needed.  This will also make \"sage -python\" and \"sage -c\" faster, since Ipython startup takes significant time. \n\n```\n/*\nsage -sh\ngcc -I$SAGE_LOCAL/include/python2.5 $SAGE_LOCAL/lib/python/config/libpython2.5.a embed.c -o embed; ./embed\n\nSee http://docs.python.org/extending/embedding.html\n*/\n\n\n#include <Python.h>\n\nint\nmain(int argc, char *argv[])\n{\n  Py_Initialize();\n  printf(\"Loading the Sage library...\\n\");\n  PyRun_SimpleString(\"from sage.all import *\");\n  printf(\"Factoring an integer:\\n\");\n  PyRun_SimpleString(\"print factor(193048120380)\");\n  printf(\"Popping up plot of a function:\\n\");\n  PyRun_SimpleString(\"x=var('x'); show(plot(sin(x)))\");\n  printf(\"Popping up plot of a 3-d function:\\n\");\n  PyRun_SimpleString(\"x,y=var('x,y'); show(plot3d(sin(x*y)-cos(x-y), (x,-4,4),(y,-4,4)))\");\n  printf(\"Type 0 then return\\n\");\n  int n;\n  scanf(\"%d\",&n);\n  printf(\"Exiting...\\n\");\n  Py_Finalize();\n  return 0;\n}\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5475\n\n",
    "created_at": "2009-03-10T21:39:27Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "make it so ipython isn't imported when one does \"sage -python\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5475",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

If one wants to use Sage from a C program, e.g., like this (see below), then it's important that "from sage.all import *" not import Ipython.  The point of this ticket is make the import of IPython lazy -- and only happen if needed.  This will also make "sage -python" and "sage -c" faster, since Ipython startup takes significant time. 

```
/*
sage -sh
gcc -I$SAGE_LOCAL/include/python2.5 $SAGE_LOCAL/lib/python/config/libpython2.5.a embed.c -o embed; ./embed

See http://docs.python.org/extending/embedding.html
*/


#include <Python.h>

int
main(int argc, char *argv[])
{
  Py_Initialize();
  printf("Loading the Sage library...\n");
  PyRun_SimpleString("from sage.all import *");
  printf("Factoring an integer:\n");
  PyRun_SimpleString("print factor(193048120380)");
  printf("Popping up plot of a function:\n");
  PyRun_SimpleString("x=var('x'); show(plot(sin(x)))");
  printf("Popping up plot of a 3-d function:\n");
  PyRun_SimpleString("x,y=var('x,y'); show(plot3d(sin(x*y)-cos(x-y), (x,-4,4),(y,-4,4)))");
  printf("Type 0 then return\n");
  int n;
  scanf("%d",&n);
  printf("Exiting...\n");
  Py_Finalize();
  return 0;
}
```

Issue created by migration from https://trac.sagemath.org/ticket/5475





---

archive/issue_comments_042390.json:
```json
{
    "body": "Attachment [trac_5475-ick.patch](tarball://root/attachments/some-uuid/ticket5475/trac_5475-ick.patch) by mabshoff created at 2009-03-10 22:23:03",
    "created_at": "2009-03-10T22:23:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5475#issuecomment-42390",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5475-ick.patch](tarball://root/attachments/some-uuid/ticket5475/trac_5475-ick.patch) by mabshoff created at 2009-03-10 22:23:03



---

archive/issue_comments_042391.json:
```json
{
    "body": "This patch causes some doctesting trouble:\n\n```\n        sage -t -long devel/sage/sage/misc/randstate.pyx # 3 doctests failed\n        sage -t -long devel/sage/sage/interfaces/psage.py # 2 doctests failed\n        sage -t -long devel/sage/sage/interfaces/sage0.py # 37 doctests failed\n        sage -t -long devel/sage/sage/misc/trace.py # 2 doctests failed\n```\n\nCheers,\n\nMichael",
    "created_at": "2009-03-10T22:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5475#issuecomment-42391",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch causes some doctesting trouble:

```
        sage -t -long devel/sage/sage/misc/randstate.pyx # 3 doctests failed
        sage -t -long devel/sage/sage/interfaces/psage.py # 2 doctests failed
        sage -t -long devel/sage/sage/interfaces/sage0.py # 37 doctests failed
        sage -t -long devel/sage/sage/misc/trace.py # 2 doctests failed
```

Cheers,

Michael



---

archive/issue_events_012797.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-10T22:30:12Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5475",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5475#event-12797"
}
```



---

archive/issue_comments_042392.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-07-22T14:38:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5475#issuecomment-42392",
    "user": "https://github.com/mwhansen"
}
```

Resolution: duplicate



---

archive/issue_events_012798.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2013-07-22T14:38:45Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5475",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5475#event-12798"
}
```



---

archive/issue_events_012799.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2013-07-22T14:38:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5475",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5475#event-12799"
}
```



---

archive/issue_events_012800.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2013-07-22T14:38:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5475",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5475#event-12800"
}
```



---

archive/issue_comments_042393.json:
```json
{
    "body": "This is a duplicate of #3685.",
    "created_at": "2013-07-22T14:38:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5475#issuecomment-42393",
    "user": "https://github.com/mwhansen"
}
```

This is a duplicate of #3685.
