# Issue 5591: alt-enter makes new input cell *after* the following text cell

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-03-23 14:43:45

Assignee: boothby


```
If I want to insert a 
> calculation cell before an html cell, I can't just press Alt-Enter in 
> the foregoing calculation cell, because this creates a new calculation 
> cell AFTER the html cell. Is there another way?. 
```


alt-enter should put a new input cell directly after the current input cell (i.e., before any text cell following the current input cell).


---

Comment by kcrisman created at 2014-09-17 02:20:29

Reported "upstream" at https://github.com/sagemath/sagenb/issues/222


---

Comment by boothby created at 2020-03-29 02:09:48

Closing deprecated notebook tickets


---

Comment by boothby created at 2020-03-29 02:09:48

Resolution: invalid
