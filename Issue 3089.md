# Issue 3089: removing an attached file doesn't work

Issue created by migration from https://trac.sagemath.org/ticket/3089

Original creator: gnprice

Original creation time: 2008-05-03 06:51:25

Assignee: somebody

The help page given by attach? claims:


```
        Type attached_files() for a list of all currently attached files.
        You can remove files from this list to stop them from being watched. 
```


In fact, this has no effect when I try it:


```
sage: version()
'SAGE Version 2.10.1, Release Date: 2008-02-02'
sage: attached_files()
['/mit/price/tmp/hessian.sage']
sage: attached_files().pop()
'/mit/price/tmp/hessian.sage'
sage: attached_files()
['/mit/price/tmp/hessian.sage']
```




---

Comment by mabshoff created at 2008-05-03 07:02:43

Changing assignee from somebody to tba.


---

Comment by mabshoff created at 2008-05-03 07:02:43

Changing component from basic arithmetic to documentation.


---

Comment by mabshoff created at 2008-05-03 07:02:43

This part of the documentation is plainly wrong and no longer valid.

Cheers,

Michael


---

Comment by gnprice created at 2008-05-03 07:43:59

OK, that's one possible response.  I'd like to be able to make Sage stop watching a file, though; either in the admittedly hackish way the documentation describes, or by a "detach" or "unattach" command.

Thanks,
Greg


---

Comment by mabshoff created at 2008-05-03 12:32:49

Yes, I thought we had either a detach or unattach command, but I couldn't find either one. So it has either been discussed and never implemented or it isn't in the global namespace. Either way it should be fixed.

Cheers,

Michael


---

Comment by mpatel created at 2010-01-16 19:01:43

Cf. #7514.


---

Comment by was created at 2010-01-17 14:13:17

Resolution: fixed
