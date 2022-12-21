# Issue 2039: add sage version const

Issue created by migration from Trac.

Original creator: benjamin.peterson

Original creation time: 2008-02-03 20:16:32

Assignee: cwitty

How does one determine the SAGE version? I can't find any information on this, so I propose that SAGE_VERSION (hex) and SAGE_VERSION_STR constants be added giving current running version.


---

Comment by was created at 2008-02-03 20:21:50

Do you mean from a running Sage?  Just use the version command. 


```
teragon:~ was$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.1, Release Date: 2008-02-02                      |
| Type notebook() for the GUI, and license() for information.        |
sage: version()
'SAGE Version 2.10.1, Release Date: 2008-02-02'
```



---

Comment by benjamin.peterson created at 2008-02-03 20:22:58

I was thinking from a SAGE program.


---

Comment by benjamin.peterson created at 2008-02-03 20:26:10

If you wanted to compare versions, then you'd have to parse out the version for the string. Correct?


---

Comment by mabshoff created at 2008-02-04 04:57:31

I think a function, maybe a variety of version(), should return some tuple with [major, minor, tiny]. We should also offer some functions, say something like require_version(X,Y,Z), that would return false for any sage release before X.Y.Z and print a helpful error message, i.e. 


```
The code needs at least Sage version X.Y.Z to work correctly. You are 
running Sage version K.P.L. To upgrade yada, yada, yada ...
```


Cheers,

Michael


---

Comment by benjamin.peterson created at 2008-02-04 17:35:35

That's a great idea. require_version is just what I need.


---

Comment by jhpalmieri created at 2008-10-31 19:10:07

Here's a patch, which also provides 100% coverage for the file banner.py.  The patch introduces functions `version_dict` and `require_version`.  I don't know if this is the sort of thing people had in mind...

  John


---

Attachment

Positive review. Nice work, I am considering importing version_dict() and require_version() into the global namespace, but we can do that via another ticket if there is demand.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-31 23:26:48

Merged in Sage 3.2.alpha2


---

Comment by mabshoff created at 2008-10-31 23:26:48

Resolution: fixed


---

Comment by mabshoff created at 2008-10-31 23:28:35

Oh yeah, I forgot: Should we expose some of the functions into the global namespace we should also add the banner.py to list of files where documentation is automatically extracted from.

Cheers,

Michael
