# Issue 4891: make a command that installs all optional spkg's and reports the ones that don't work.

Issue created by migration from https://trac.sagemath.org/ticket/4891

Original creator: was

Original creation time: 2008-12-30 07:28:37

Assignee: mabshoff

This is 100% for testing use.  I've written this and will post a patch soon.

NOTE: Nauty has a stupid interactive license agreement which somewhat messes up this command, since it makes it not 100% automatic.    I hate that.  I've made trac #4890 to get rid of it.


---

Attachment

For the record, when I run this on sage.math it takes a total of a half hour (pretty fast!) and finishes with the following:

```
...
Successfully installed valgrind_3.3.1
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing valgrind_3.3.1.spkg
CPU times: user 0.03 s, sys: 1.54 s, total: 1.57 s
Wall time: 1925.36 s
['boehm_gc-7.1.p0', 'mpi4py-0.3.1']
```


So boehm and mpi4py failed to install.  But everything else in optional succeeded.  Note that there is  an inconsistency, since according to the output of optional_packages() in fact mpi4py and fricas failed but everything else succeeded:

```
 ['fricas-1.0.3.p0', 'mpi4py-0.3.1'])
```

This I think points to bugs in the package install system, not in this patch.


---

Comment by mabshoff created at 2008-12-30 10:49:56

boehm_gc-7.1.p0 is already in standard Sage, but also in the optional repo in case someone wants to install M2 into an older version of Sage.

Cheers,

Michael


---

Comment by was created at 2008-12-30 17:44:45

I tested on OS X and got:

```
Thread model: posix
gcc version 4.0.1 (Apple Inc. build 5465)
****************************************************
Valgring does not work on non-Linux yet

real    0m0.012s
user    0m0.003s
sys     0m0.007s
sage: An error occurred while installing valgrind_3.3.1
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /Users/was/build/sage-3.2.2/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/Users/was/build/sage-3.2.2/spkg/build/valgrind_3.3.1 and type 'make'.
Instead type "/Users/was/build/sage-3.2.2/sage -sh"
in order to set all environment variables correctly, then cd to
/Users/was/build/sage-3.2.2/spkg/build/valgrind_3.3.1
(When you are done debugging, you can type "exit" to leave the
subshell.)
CPU times: user 0.07 s, sys: 1.29 s, total: 1.37 s
Wall time: 4061.35 s
sage:
sage: v
['boehm_gc-7.1.p0', 'mpi4py-0.3.1']
sage:
```


So the error detection (i.e., when an exception is raised) in install_packages is clearly buggy.  But I don't think that should hold this patch back, since that's a separate bug in a different function, and should be addressed in another ticket.


---

Comment by was created at 2008-12-30 17:45:38

> boehm_gc-7.1.p0 is already in standard Sage, but also in the optional repo in case 
> someone wants to install M2 into an older version of Sage. 

I propose removing it or at least moving it to experimental, since M2 is only in experimental after all.


---

Comment by mabshoff created at 2008-12-30 17:48:44

Replying to [comment:5 was]:

> I propose removing it or at least moving it to experimental, since M2 is only in experimental after all. 
> 

Fine by me since we have shipped it with standard for a while. Maybe the install_package routine should be smarter about already installed spkgs, too?

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-30 17:50:55

Replying to [comment:4 was]:

<SNIP>

> So the error detection (i.e., when an exception is raised) in install_packages is clearly buggy.  But I don't think that should hold this patch back, since that's a separate bug in a different function, and should be addressed in another ticket. 

Sure. Should we chose a certain exit code if the spkg does not work on a given platform to signal that? So far we always seem to exit spkg-install with 1 when a failure occurs, so assigning meaningful exit codes could come in handy.

Cheers,

Michael


---

Comment by malb created at 2009-01-24 12:17:33

Code looks fine, here's the test output:


```
...
Making script relocatable
Finished installing valgrind_3.3.1.spkg
['boehm_gc-7.1.p0', 'mpi4py-0.3.1']
sage: optional_packages()
...
  'trac-20071204',
  'valgrind_3.3.1'],
 ['mpi4py-0.3.1', 'polymake-2.2.p5'])
```



---

Comment by malb created at 2009-01-24 12:18:44

I guess that means *positiv review*


---

Comment by mabshoff created at 2009-01-28 15:22:59

Resolution: fixed


---

Comment by mabshoff created at 2009-01-28 15:22:59

Merged in Sage 3.3.alpha3.

Cheers,

Michael
