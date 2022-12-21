# Issue 3567: optimize startup of sage -- don't import global transaction module

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-06 19:48:57

Assignee: tbd

BEFORE:

```
teragon-2:databases was$ sage -startuptime |grep transaction
        transaction: 0.104 (sage.databases.db)
         transaction._transaction: 0.103 (transaction)
          logging: 0.004 (transaction._transaction)
          zope: 0.096 (transaction._transaction)
         transaction._manager: 0.000 (transaction)
             transaction.interfaces: 0.000 (ZODB.Connection)
0.104 transaction (sage.databases.db)
0.103 transaction._transaction (transaction)
0.096 zope (transaction._transaction)
```

and that's *with* disk caching (on os x though). 

AFTER this patch:

```
teragon-2:databases was$ sage -startuptime |grep transaction
             transaction.interfaces: 0.004 (ZODB.Connection)
              transaction._transaction: 0.003 (transaction.interfaces)
               zope: 0.000 (transaction._transaction)
               transaction: 0.001 (transaction._transaction)
              transaction._manager: 0.000 (transaction.interfaces)
```


Sweet!


---

Attachment


---

Comment by was created at 2008-07-06 19:50:48

Changing component from algebra to misc.


---

Comment by was created at 2008-07-06 19:50:48

Changing assignee from tbd to cwitty.


---

Comment by mhansen created at 2008-07-06 19:53:35

+1


---

Comment by mabshoff created at 2008-07-06 20:09:55

Merged in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-06 20:09:55

Resolution: fixed
