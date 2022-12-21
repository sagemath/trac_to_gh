# Issue 64: division in pAdicField truncates precision

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-09-15 21:28:30

Assignee: somebody


```
sage: 1/(1 + 3*5^5 + O(5^50))
1 + 2*5^5 + 4*5^6 + 4*5^7 + 4*5^8 + 4*5^9 + 3*5^10 + 5^11 + 3*5^15 + 4*5^16 + 3*5^17
+ 4*5^18 + 4*5^19 + O(5^20)
```


The answer should be returned to precision 50.



---

Comment by dmharvey created at 2006-09-26 22:24:21

Changing assignee from somebody to dmharvey.


---

Comment by dmharvey created at 2006-10-10 23:56:42

Resolution: fixed


---

Comment by dmharvey created at 2006-10-10 23:56:42

this is fixed in sage 1.4
