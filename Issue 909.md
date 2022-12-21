# Issue 909: Cython without recompile

Issue created by migration from Trac.

Original creator: jvoight

Original creation time: 2007-10-16 18:42:53

Assignee: was

Loading a file in sage by
  load foo.spyx 
seems to result in a recompile every time--or at least it is doing something that takes time.  Is this really necessary, or is something else going on?  Shouldn't it instead check to see if there has been a change to foo.spyx?  (This recompiling is expensive if the Cython file is quite long!)


---

Comment by mabshoff created at 2007-10-16 18:57:39

Well, 

if we had a makefile or SCons based buildsystem for external Cython code like the sagelib this wouldn't happen. I think it used to be the way that the compiled objects would be kept around, but I am not sure why this no longer happens. There is also a problem with C++ files if you change compilers which break ABI compability, but this would be a rather rare occurance for the vast majority of people.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-03 00:01:00

RobertWB opened #4238 with a patch, so I am closing this as a dupe.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-03 00:01:00

Resolution: duplicate
