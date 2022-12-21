# Issue 5059: [with patch, needs review] Fix a bunch of broken pickles

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2009-01-22 23:57:16

Assignee: craigcitro

At a workshop in Seattle last June, a *massive* number of spaces of modular symbols were computed. However, the pickles were broken in shortly thereafter by a refactoring of some code in Sage. 

The attached patch fixes this -- now the old pickles can be loaded, and new pickles still work fine.


---

Attachment


---

Comment by robertwb created at 2009-01-23 02:15:55

Are there some example broken pickles that this fixes?


---

Comment by robertwb created at 2009-01-23 04:01:10

Some examples: http://sage.math.washington.edu/home/wstein/db/modsym/data/

Looks good and works great.


---

Comment by mabshoff created at 2009-01-23 09:01:43

Unfortunately this patch breaks two doctests:

```
        sage -t -long devel/sage/sage/modular/congroup.py # 5 doctests failed
        sage -t -long devel/sage/sage/modular/congroup_element.py # 1 doctests failed
```


Cheers,

Michael


---

Attachment

That seems to have addressed those doctest failures.


---

Comment by mabshoff created at 2009-01-23 10:02:22

Merged in Sage 3.3.alpha0

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 10:02:22

Resolution: fixed
