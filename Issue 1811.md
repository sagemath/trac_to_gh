# Issue 1811: command line detach -- completely missing from Sage!?

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-17 21:59:31

Assignee: was


```


On Jan 17, 2008 12:08 AM, Dan Drake <dr.dan.drake`@`gmail.com> wrote:
> Hello,
> 
> I'd like to unattach a file that is currently attached. The

The command to do this used to be called "detach".  It has mysteriously completely
vanished from Sage since when I wrote it!  It's in the notebook still, but it isn't available
from the command line anymore.  

Anyway, I've reported this as trac #

In the meantime you can work around this problem as illustrated below:

sage: sage: attach example.sage
This is a simple SAGE example script.
...
sage: import sage.misc.interpreter
sage: sage.misc.interpreter.attached
{'/home2/sage/build/sage-2.10.alpha4/example.sage': 1197908255.0}
sage: del sage.misc.interpreter.attached['/home2/sage/build/sage-2.10.alpha4/example.sage']
sage: attached_files()
[]




> documentation for attach says that I can remove files from
> attached_files() to do this, but that doesn't seem to work:
> 
>   sage: attached_files()
>   ['/home/drake/code/sage/foo.sage']
>   sage: attached_files().pop()
>   '/home/drake/code/sage/foo.sage'
>   sage: attached_files()
>   ['/home/drake/code/sage/foo.sage']
> 
> It doesn't work because I'm accessing the list *returned by*
> attached_files; I need to access whatever attached_files() looks at to
> get that list. I used ??attached_files, but I don't seem to have access
> to the 'attached' variable.
> 
> What I'd really like, though, is an 'unattach' function!
> 

```



---

Comment by malb created at 2009-01-22 22:37:35

Changing type from defect to enhancement.


---

Comment by mpatel created at 2010-01-16 19:45:28

With #7514 merged, should we close this ticket?


---

Comment by mpatel created at 2010-01-16 19:45:36

Changing status from new to needs_info.


---

Comment by was created at 2010-01-17 14:12:12

Yes, #7514 does this, I think.


---

Comment by mpatel created at 2010-01-20 11:18:49

Quirk: Use `detach('test.sage')` to detach `test.sage`.


---

Comment by mvngu created at 2010-02-01 01:41:09

Close as fixed by #7514.


---

Comment by mvngu created at 2010-02-01 01:41:09

Resolution: fixed
