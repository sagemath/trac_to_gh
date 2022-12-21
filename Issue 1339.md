# Issue 1339: Solaris: number of partitions broken

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-29 10:01:34

Assignee: mhansen

CC:  sage-combinat

Hello,

number of partitions is broken on Solaris/Sparc:

```
sage -t  devel/sage-main/sage/combinat/combinat.py          **********************************************************************
File "combinat.py", line 1869:
    sage: number_of_partitions(100000)
Expected:
    274935105697756965126775163209863526881734293159800547582031259843021473281149641730550507416607366215901578447742962489
4049306307020046179276449303351011607934245719015571894350972531246610845200636955893446424871682878983218234500926285383140
4597021307130674510624419227311238999702284408609370935531629697851569569892196108480158600569421098519
Got:
    274935105697756965126775163209863526881734293159800547582031259843021473281149641730550507416607366215901578447742962489
4049306307020046179276449303351011607934245719015571894350972531246610845200636955893446424871682878983218234500926285383140
4597021307130674510624419227311238999702284408609370935531629697851569569892196108480158600582558780007
**********************************************************************
File "combinat.py", line 1896:
```

but also more worringly the "small" case:

```
**********************************************************************
File "combinat.py", line 1924:
    sage: len([n for n in [1..500] if number_of_partitions(n) != number_of_partitions(n,algorithm='pari')])
Expected:
    0
Got:
    245
**********************************************************************
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-12-26 03:15:40

I suspect floating point precision issues. Didn't we do something on MaxOSX/PPC about this by lowering certain precision bounds?

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-29 17:42:19

Changing assignee from mhansen to mabshoff.


---

Comment by mabshoff created at 2008-07-29 17:42:19

The solution here is to reduce the various precisions used in the partition code. For qd we have to reduce the precision to *170* bits which indicates either a severe bug on our end or something is seriously wrong in qd.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-29 17:42:19

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-08 03:12:32

Resolution: fixed


---

Comment by mabshoff created at 2009-02-08 03:12:32

This has been fixed by the deprecation of quaddouble via #3762 by Robert Bradshaw.

Cheers,

Michael
