# Issue 3606: totallyreal_data.py: "Use of uninitialised value of size 8"

Issue created by migration from https://trac.sagemath.org/ticket/3606

Original creator: mabshoff

Original creation time: 2008-07-08 11:49:43

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


---

Comment by mabshoff created at 2008-09-23 00:12:35

Resolution: fixed


---

Comment by mabshoff created at 2008-09-23 00:12:35

This one is fixed by #4155. There are another one, but that one will be on a new ticket.

Cheers,

Michael
