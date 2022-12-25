# Issue 3606: totallyreal_data.py: "Use of uninitialised value of size 8"

archive/issues_003606.json:
```json
{
    "body": "Assignee: mabshoff\n\n```\n==18041== Use of uninitialised value of size 8\n==18041==    at 0x4FFB60D: __mpn_rshift (in /lib/libc-2.3.6.so)\n==18041==    by 0x500459D: __printf_fp (in /lib/libc-2.3.6.so)\n==18041==    by 0x4FFF669: vfprintf (in /lib/libc-2.3.6.so)\n==18041==    by 0x50216F9: vsnprintf (in /lib/libc-2.3.6.so)\n==18041==    by 0x4B868C: PyOS_vsnprintf (mysnprintf.c:65)\n==18041==    by 0x4B8651: PyOS_snprintf (mysnprintf.c:48)\n==18041==    by 0x4C53F5: PyOS_ascii_formatd (pystrtod.c:209)\n==18041==    by 0x42CB93: format_float (floatobject.c:235)\n==18041==    by 0x42CE19: float_repr (floatobject.c:345)\n==18041==    by 0x446517: PyObject_Repr (object.c:361)\n==18041==    by 0x433D41: list_repr (listobject.c:337)\n==18041==    by 0x462F1A: object_str (typeobject.c:2468)\n\n==18041== Conditional jump or move depends on uninitialised value(s)\n==18041==    at 0x50043F1: __printf_fp (in /lib/libc-2.3.6.so)\n==18041==    by 0x4FFF669: vfprintf (in /lib/libc-2.3.6.so)\n==18041==    by 0x50216F9: vsnprintf (in /lib/libc-2.3.6.so)\n==18041==    by 0x4B868C: PyOS_vsnprintf (mysnprintf.c:65)\n==18041==    by 0x4B8651: PyOS_snprintf (mysnprintf.c:48)\n==18041==    by 0x4C53F5: PyOS_ascii_formatd (pystrtod.c:209)\n==18041==    by 0x42CB93: format_float (floatobject.c:235)\n==18041==    by 0x42CE19: float_repr (floatobject.c:345)\n==18041==    by 0x446517: PyObject_Repr (object.c:361)\n==18041==    by 0x433D41: list_repr (listobject.c:337)\n==18041==    by 0x462F1A: object_str (typeobject.c:2468)\n==18041==    by 0x446709: _PyObject_Str (object.c:406)\n```\n\nI need to rerun this doctest with a longer stacktrace since as is this is pretty useless.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3606\n\n",
    "created_at": "2008-07-08T11:49:43Z",
    "labels": [
        "component: memleak",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "totallyreal_data.py: \"Use of uninitialised value of size 8\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3606",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

```
==18041== Use of uninitialised value of size 8
==18041==    at 0x4FFB60D: __mpn_rshift (in /lib/libc-2.3.6.so)
==18041==    by 0x500459D: __printf_fp (in /lib/libc-2.3.6.so)
==18041==    by 0x4FFF669: vfprintf (in /lib/libc-2.3.6.so)
==18041==    by 0x50216F9: vsnprintf (in /lib/libc-2.3.6.so)
==18041==    by 0x4B868C: PyOS_vsnprintf (mysnprintf.c:65)
==18041==    by 0x4B8651: PyOS_snprintf (mysnprintf.c:48)
==18041==    by 0x4C53F5: PyOS_ascii_formatd (pystrtod.c:209)
==18041==    by 0x42CB93: format_float (floatobject.c:235)
==18041==    by 0x42CE19: float_repr (floatobject.c:345)
==18041==    by 0x446517: PyObject_Repr (object.c:361)
==18041==    by 0x433D41: list_repr (listobject.c:337)
==18041==    by 0x462F1A: object_str (typeobject.c:2468)

==18041== Conditional jump or move depends on uninitialised value(s)
==18041==    at 0x50043F1: __printf_fp (in /lib/libc-2.3.6.so)
==18041==    by 0x4FFF669: vfprintf (in /lib/libc-2.3.6.so)
==18041==    by 0x50216F9: vsnprintf (in /lib/libc-2.3.6.so)
==18041==    by 0x4B868C: PyOS_vsnprintf (mysnprintf.c:65)
==18041==    by 0x4B8651: PyOS_snprintf (mysnprintf.c:48)
==18041==    by 0x4C53F5: PyOS_ascii_formatd (pystrtod.c:209)
==18041==    by 0x42CB93: format_float (floatobject.c:235)
==18041==    by 0x42CE19: float_repr (floatobject.c:345)
==18041==    by 0x446517: PyObject_Repr (object.c:361)
==18041==    by 0x433D41: list_repr (listobject.c:337)
==18041==    by 0x462F1A: object_str (typeobject.c:2468)
==18041==    by 0x446709: _PyObject_Str (object.c:406)
```

I need to rerun this doctest with a longer stacktrace since as is this is pretty useless.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3606





---

archive/issue_events_008262.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-23T00:12:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3606",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3606#event-8262"
}
```



---

archive/issue_comments_025425.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-23T00:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3606#issuecomment-25425",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025426.json:
```json
{
    "body": "This one is fixed by #4155. There are another one, but that one will be on a new ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-23T00:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3606",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3606#issuecomment-25426",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This one is fixed by #4155. There are another one, but that one will be on a new ticket.

Cheers,

Michael
