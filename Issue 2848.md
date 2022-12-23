# Issue 2848: numerical noise in sage/misc/prandom.py on MacIntel OSX 10.5/

Issue created by migration from https://trac.sagemath.org/ticket/2848

Original creator: mabshoff

Original creation time: 2008-04-07 19:49:36

Assignee: mabshoff

CC:  justin

Justin Walker reported:

```
     sage -t  devel/sage/sage/misc/prandom.py
     File "/Users/tmp/sage-3.0.alpha2/tmp/prandom.py", line 241:
         sage: [gauss(0, 100) for i in range(3)]
     Expected:
         [24.916051749154448, -62.992720615792727, -8.1993122536718097]
     Got:
         [24.916051749154448, -62.992720615792727, -8.1993122536718115] 
```



---

Attachment


---

Comment by mabshoff created at 2008-04-07 20:03:27

Justin, 

can you check if this patch fixes it for you. Provided it does fix the issue feel free to give it a positive review ;)

Cheers,

Michael


---

Comment by mhansen created at 2008-04-07 22:22:07

Looks good to me.


---

Comment by mabshoff created at 2008-04-07 22:25:37

Merged in Sage 3.0.alpha3


---

Comment by mabshoff created at 2008-04-07 22:25:37

Resolution: fixed
