# Issue 4904: convert sage.categories.* docstrings to Sphinx

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-01-01 22:46:45

Assignee: tba




---

Attachment


---

Comment by was created at 2009-01-03 04:51:40

This is not your fault at all, but I just noticed this dubious line in a docstring for morphism.pyx:

```
134	 	        function -- a Python function that takes elements of the domain as input 
135	 	                    and returns elements of the domain. 
```


I think the last "domain" should be "codomain".


---

Comment by jhpalmieri created at 2009-01-07 22:09:01

Everything looks good here.


---

Comment by mabshoff created at 2009-02-24 18:43:20

Resolution: fixed


---

Attachment

Merged in Sage 3.4.alpha0.

Cheers,

Michael
