# Issue 2993: [with spkg, needs review] OSX/gcc 4.2: disable padlock support per default

Issue created by migration from https://trac.sagemath.org/ticket/2993

Original creator: mabshoff

Original creation time: 2008-04-21 21:57:20

Assignee: mabshoff

Rob Goedman reported:

```
Robs-Intel:sage-3.0.rc0 rob$ gcc -v
Using built-in specs.
Target: i686-apple-darwin9
Configured with: /var/tmp/gcc_42/gcc_42-5531~1/src/configure --disable-
checking -enable-werror --prefix=/usr --mandir=/usr/share/man --enable-
languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/
$/-4.2/ --with-gxx-include-dir=/usr/include/c++/4.0.0 --with-slibdir=/
usr/lib --build=i686-apple-darwin9 --host=i686-apple-darwin9 --
target=i686-apple-darwin9
Thread model: posix
gcc version 4.2.1 (Apple Inc. build 5531)

make gives below (summarized) error on 2.11, alpha6, rc0 and rc1.  
Below attachment contains the complete rc1 install.log .

If, as a quick test, the Mac specific '-fasm-blocks' flag is added in  
the subdir cipher, make complains about the assembler code in the asm  
block in poll_padlock.

Do I have to disable ENABLE_PADLOCK_SUPPORT? If so, can I force the  
sage make to use './configure -disable_padlock_support'?

As this is not related to the upcoming Sage 3.0 release, I'm fine to  
wait for a binary release, although ultimately I would like to be able  
to build sage myself. 
```


The spkg at

http://sage.math.washington.edu/home/mabshoff/SPKG/libgcrypt-1.4.0.p2.spkg

will hopefully fix the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-21 21:57:26

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-23 11:44:35

Reviewed in https://groups.google.com/group/sage-devel/t/dbf2716e5c97e64b by Rob Goedman:

```
Michael, Thanks a lot. The new libgcrypt-1.4.0.p2.spkg indeed does fix the   problem, at least during the make!
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-04-23 11:45:20

Resolution: fixed


---

Comment by mabshoff created at 2008-04-23 11:45:20

Merged in Sage 3.0.1.alpha0
