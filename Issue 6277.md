# Issue 6277: sage -tp a.py a.py will test a.py twice

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-06-13 19:45:17

Assignee: tbd

I think this is a bug, but maybe not.


---

Comment by was created at 2009-06-14 09:54:25

Resolution: invalid


---

Comment by was created at 2009-06-14 09:54:25

Just for the record, 
`sage -tp a.py a.py`
results in 

```
ValueError: invalid literal for int() with base 10: 'devel/sage/sage/rings/arith.py'
```

so I'm fixing the title of the ticket.  

I also consider this invalid.  There are good reasons to want to test the same file a bunch of times, e.g.,

```
sage -tp 10 a.py a.py  a.py a.py a.py a.py a.py a.py a.py a.py a.py
```

would be very useful when tracking down errors that only happen with some probability.
