# Issue 2813: Add keycodes to split / join cells.

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2008-04-05 19:30:19

Assignee: boothby


```
From: Andrey Novoseltsev
Subject: [sage-devel] Cell splitting/merging in notebook


Is it possible to realize some convenient and fast (in the sense of
keyboard use) cell splitting/merging? It seems to me that now it
involves manual copying of a part of code and creating/removing a
cell, or editing the text representation. I really liked the ability
to do it in Maple (back when I was using it ;-) by pressing some hot
keys since it allows you to group cells for executing in one step and
nicer visual presentation or break them back when you want to interact
with intermediate values.
```



---

Attachment


---

Comment by was created at 2008-04-05 20:58:40

Hi Tom,

In OS X firefox I tried this patch and it is really broken.  Splitting cells does absolutely nothing.  Joining works, but puts the active focus in the wrong cell. 

I'll see if I can fix it.


---

Comment by was created at 2008-04-05 20:59:53

On OS X with safari split does work.  Join has the same problem as described above.


---

Comment by was created at 2008-04-05 21:52:37

Another REFEREE COMMENT:

Absolutely none of the functions you added in this patch have any documentation. 
That has to be fixed before this patch gets accepted.  Even javascript functions have to have docs.   Again, I'm trying to work out what they do -- contact me before working on this.


---

Attachment

this should be applied after tom's first patch


---

Attachment

this adds opera support, at least under os x.


---

Attachment


---

Comment by robertwb created at 2008-04-06 06:37:56

Works great in Camino, but it has issues joining cells in Safari 3.1 on OS X 10.4.11.


---

Comment by robertwb created at 2008-04-06 06:40:42

Safari 3.1 isn't supported by Sage yet. Works great elsewhere.


---

Comment by mabshoff created at 2008-04-06 06:54:20

Merged all four patches in Sage 3.0.alpha2


---

Comment by mabshoff created at 2008-04-06 06:54:20

Resolution: fixed
