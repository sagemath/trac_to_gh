# Issue 5629: refactor dimension() of schemes

Issue created by migration from https://trac.sagemath.org/ticket/5629

Original creator: AlexGhitza

Original creation time: 2009-03-29 03:58:49

Assignee: was

Keywords: dimension scheme

The dimension() method for schemes is confusing and sometimes inconsistent or plain broken when working over bases that are not fields.  The attached patch implements methods dimension_absolute() and dimension_relative() and makes dimension() into an alias for dimension_absolute().



---

Attachment


---

Comment by AlexGhitza created at 2009-03-29 04:02:16

See the following thread for more details:

http://groups.google.com/group/sage-devel/browse_thread/thread/cab22c1376251540


---

Comment by AlexGhitza created at 2009-03-29 08:16:19

Changing assignee from was to AlexGhitza.


---

Comment by AlexGhitza created at 2009-03-29 08:16:29

Changing status from new to assigned.


---

Comment by was created at 2009-03-29 17:25:19

REFEREE REPORT.

Looks great.  I rebased this patch against 3.4.1.alpha0 and added a doctest for the following new function.  I also doctested this patch against the schemes directory.

```
 	137	    def is_noetherian(self): 
 	138	        """ 
 	139	        Return True if this scheme is Noetherian. 
 	140	        """ 
 	141	        return self.__R.is_noetherian() 
```



---

Comment by was created at 2009-03-29 17:26:53

rebased against 3.4.1.alpha0 and added a missing doctst


---

Attachment


---

Comment by mabshoff created at 2009-03-31 08:49:57

Resolution: fixed


---

Comment by mabshoff created at 2009-03-31 08:49:57

Merged trac_5629-rebase.patch in Sage 3.4.1.rc0.

Cheers,

Michael
