# Issue 897: number_of_partitions -- now broken on OS X PPC

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-14 20:35:28

Assignee: was

CC:  sage-combinat

On OS X PPC with the new number_of_partitions optimized code:


```
fermat:~/sage-2.8.7.rc1 was$ ./sage -t  devel/sage-main/sage/combinat/combinat.py
sage -t  devel/sage-main/sage/combinat/combinat.py          *******************************************
***************************  
File "combinat.py", line 1843:
    sage: number_of_partitions(100000)
Expected:
    274935105697756965126775163209863526881734293159800547582031259843021473281149641730550507416607366
2159015784477429624894049306307020046179276449303351011607934245719015571894350972531246610845200636955
8934464248716828789832182345009262853831404597021307130674510624419227311238999702284408609370935531629
697851569569892196108480158600569421098519
Got:
    274935105697756965126775163209863526881734293159800547582031259843021473281149641730550507416607366
2159015784477429624894049306307020046179276449303351011607934245719015571894350972531246610845200636955
8934464248716828789832182345009262853831404597021307130674510624419227311238999702284408609370935531629
697851569569892196108480158600569420104082
**********************************************************************
File "combinat.py", line 1867:
    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
Expected:
    True
Got:
    False
**********************************************************************
File "combinat.py", line 1870:
    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
Expected:
    True
Got:
    False

```


The code works on everything else, i.e., all x86 machines. 


---

Comment by was created at 2007-10-14 20:35:54

Changing priority from major to critical.


---

Comment by was created at 2007-10-14 22:53:55

Resolution: fixed


---

Comment by was created at 2007-10-14 22:53:55

It was always broken on OS X!

Anyway, I've patched this up for the release, but more work needs to be done...


---

Comment by was created at 2007-10-15 00:33:34

ok, everything is all fixed for sage-2.8.7.
