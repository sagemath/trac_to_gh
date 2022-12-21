# Issue 4907: convert sage.crypto.* docstrings to Sphinx

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-01-01 22:49:37

Assignee: tba




---

Attachment


---

Comment by wdj created at 2009-01-02 11:30:15

Looks good. There is one "then" which is caught in a latex math display mode. I wonder if changing


```
 	100	.. math:: 
 	101	 
 	102	     f(x)=1,\ \ \ \ g(x)=x^4+x+1,  
 	103	 
 	104	 then 
```

to


```
 	100	.. math:: 
 	101	 
 	102	     f(x)=1,\ \ \ \ g(x)=x^4+x+1,  
 	103	 
	104	 
 	105	then 
```

would fix that? Ie, add a blank line and delete a space?


---

Comment by mhansen created at 2009-01-02 11:42:27

Good catch.  Just deleting the space should be enough.  ReST works with indentation levels.  I'll post an updated patch.


---

Attachment

I've attached a patch which fixes this.


---

Comment by mabshoff created at 2009-02-24 18:36:09

Resolution: fixed


---

Attachment

Merged in Sage 3.4.alpha0.

Cheers,

Michael
