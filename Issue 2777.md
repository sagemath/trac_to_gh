# Issue 2777: '??' can't always find the source

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2008-04-02 17:54:30

Assignee: was

Here's an example:

```
sage: notebook??
```

Then the screen clears and is replaced by

```
Type:             instance
Base Class:       sage.server.notebook.notebook_object.NotebookObject
String Form:   <sage.server.notebook.notebook_object.NotebookObject instance at 0xb5d66c0>
Namespace:        Interactive
Docstring [source file open failed]:
    
        Start the SAGE Notebook server. 
    
        INPUT:
...
```

piped through my PAGER ('less').  After quitting this, I see


```
Error getting source: arg is not a module, class, method, function, traceback, frame, or code object

```


This is in  $SAGE_ROOT for sage-2.11. "./sage" is not modified to fix SAGE_ROOT, and "." is in my PATH.  Oh, and I'm using the command-line, of course :-}





---

Comment by aginiewicz created at 2008-09-21 22:19:42

quick'n


---

Attachment

added quick'n'dirty patch...

the case with notebook?? can be also seen with all class instances, I made quick patch that make sage.misc.sageinspect.sage_get* functions work with class instances by returning data of class coresponding to given instance... also made notebook version of ?? check for _sage_src_ like was already done in console version.

I don't know if this covers all cases, but works for reported notebook (and also for R functions and probably more)


---

Comment by robertwb created at 2008-09-24 01:25:51

Works for me for instance classes. New style classes still don't work, but it's not immediately obvious how to handle that case (#4183) so I think this should be merged.


---

Comment by mabshoff created at 2008-09-24 02:04:56

Andrzej,

please post patches in the future and not diffs since I can accidentally import diffs and then the credit in the log would go to me. Not that I mind .... :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-24 02:07:37

Merged in Sage 3.1.3.alpha1


---

Comment by mabshoff created at 2008-09-24 02:07:37

Resolution: fixed
