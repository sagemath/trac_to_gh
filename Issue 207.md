# Issue 207: log in waaay slower than python's math.log

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-01-23 14:17:33

Assignee: somebody


```
sage: time x = [log(n) for n in range(1, 100000)]
CPU times: user 2.68 s, sys: 0.08 s, total: 2.75 s
Wall time: 2.76

sage: import math
sage: time x = [math.log(n) for n in range(1, 100000)]
CPU times: user 0.15 s, sys: 0.01 s, total: 0.17 s
Wall time: 0.17
```




---

Comment by was created at 2007-01-23 19:45:24

Improved for sage-1.9:

```

sage: time x = [math.log(n) for n in range(1, 100000)]
CPU times: user 0.07 s, sys: 0.01 s, total: 0.08 s
Wall time: 0.08
sage: time x = [log(n) for n in range(1, 100000)]
CPU times: user 0.37 s, sys: 0.01 s, total: 0.38 s
Wall time: 0.39
```


Note that the SAGE log does much more than the math one, since
it allows for calling a log method of the object (testing for
presense of already takes more time than math.log).  Also, it 
returns a native SAGE object -- in this case I've changed it to
return an RDF element, which is pretty logical. 

William


---

Comment by was created at 2007-01-23 19:45:24

Resolution: fixed
