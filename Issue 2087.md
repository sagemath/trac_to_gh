# Issue 2087: make the final output of "sage -i" more user friendly (easy to fix)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-07 18:58:42

Assignee: was


```
When I install an optional package via

 ./sage -i [optional package]

the last line of output is "Making script relocatable".

I frequently do the install in the background, redirecting
the output to a file
and then use "tail -f" to monitor the output (and then go off
and do something else).   When I come back, it is unclear
to me whether the install has finished.  Perhaps something
like "install finished" could be added as a last line.

Just a suggestion.
Kate
```



---

Comment by mabshoff created at 2008-02-25 18:39:50

The patch I will attach shortly does print the following at the end of an install:

```
Successfully installed valgrind_3.3.0
Now cleaning up tmp files.
Making SAGE/Python scripts relocatable...
Making script relocatable
Finished installing valgrind_3.3.0.spkg
```

where valgrind_3.3.0.spkg in this case was `$PKG_NAME.spkg`

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-02-25 19:49:42

Resolution: fixed


---

Comment by mabshoff created at 2008-02-25 19:49:42

Merged in Sage 2.10.3.alpha0
