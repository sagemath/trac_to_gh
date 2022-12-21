# Issue 4054: [with patch, needs review] shorten doctesting in graph_generators.py

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-09-03 22:53:32

Assignee: tbd

On my MacBook Pro, before this patch:

```
sage -t  devel/sage-main/sage/graphs/graph_generators.py    
	 [117.4 s]
sage -t -long devel/sage-main/sage/graphs/graph_generators.py
	 [242.7 s]
```


And after this patch:

```
sage -t  devel/sage-main/sage/graphs/graph_generators.py    
	 [20.7 s]
sage -t -long devel/sage-main/sage/graphs/graph_generators.py
	 [86.9 s]
```



---

Comment by rlm created at 2008-09-03 23:25:06

Changing assignee from tbd to rlm.


---

Comment by mabshoff created at 2008-09-04 00:12:49

Hi,

I would make the "not tested" "long" since one day we will have a framework that compares expected with actual plotting output. Other than that positive review.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-09-04 23:02:47

Positive review now that the "not tested" have been converted.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-04 23:22:43

Resolution: fixed


---

Comment by mabshoff created at 2008-09-04 23:22:43

Merged in Sage 3.1.2.rc0
