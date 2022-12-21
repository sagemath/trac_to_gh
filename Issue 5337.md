# Issue 5337: update French to tutorial to reflect the fact that "I in CC" works in tour_rings.rst

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-02-22 18:08:19

Assignee: tba

Old French version:

```
Il y a une subtilité dans la définition des nombres complexes. Comme
mentionné ci-dessus, le symbole  ``i`` représente une racine carrée de
:math:`-1`, mais il s'agit d'une racine carrée *formelle* de
:math:`-1`, qui n'appartient pas aux nombres complexes. L'appel ``CC(i)``
renvoie la racine carrée complexe de :math:`-1`.
```


New English version:


```
There is one subtlety in defining complex numbers: as mentioned
above, the symbol ``i`` represents a square root of :math:`-1`, but it is a
*formal* square root of :math:`-1`.  Calling
``CC(i)`` returns the complex square root of :math:`-1`.
```




---

Comment by mmezzarobba created at 2009-03-05 20:09:35

Resolution: fixed


---

Comment by mhansen created at 2009-03-05 20:13:20

Hi Marc,

I was wondering where this was fixed?  In general, we don't close tickets until the appropriate changes have been merged into the main tree.

--Mike


---

Comment by mhansen created at 2009-03-05 20:13:20

Resolution changed from fixed to 


---

Comment by mhansen created at 2009-03-05 20:13:20

Changing status from closed to reopened.


---

Comment by mmezzarobba created at 2009-03-07 12:01:03

Hi,

Replying to [comment:2 mhansen]:
> In general, we don't close tickets until the appropriate
> changes have been merged into the main tree.

Actually I sent you an email asking precisely this question when I closed this ticket--but it seems you saw my action on the ticket first. Sorry for my mistake; I have just reopened #4318 too.

-- Marc


---

Comment by mmezzarobba created at 2009-04-27 21:23:44

This should be fixed by the patch attached to #5850.


---

Comment by mmezzarobba created at 2009-06-24 19:13:36

Replying to [comment:4 mmezzarobba]:
> This should be fixed by the patch attached to #5850.

And now #5850 has been closed, so I think this ticket should be closed too.


---

Comment by mvngu created at 2009-09-09 07:59:28

Fixed via #5850.


---

Comment by mvngu created at 2009-09-09 07:59:28

Resolution: fixed
