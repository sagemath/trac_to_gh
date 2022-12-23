# Issue 8560: magma interface should be changed to use sage-native-execute

Issue created by migration from https://trac.sagemath.org/ticket/8560

Original creator: klee

Original creation time: 2010-03-19 09:14:06

Assignee: was

Latest Magma v2.16-6 fails to load under Sage 4.3.3, with 
  the following error message: 


sage: magma_console() 
  dyld: Library not loaded: `@`executable_path/libgmp.3.dylib 
    Referenced from: /Applications/Magma/bin/magma.exe 
   Reason:  Incompatible library version: magma.exe requires version 
 9.0.0 or  later, but libgmp.3.dylib provides version 8.0.0 
 /usr/bin/magma:  line 72: 16880 Trace/BPT trap          "${ROOT}/bin/ 
 magma.exe" $* 


The reason of the failure is  that Sage defines the variable DYLD_LIBRARY_PATH when it executes  Magma. If you undefine it or define it to point to the right place,  then there is no problem

The solution is to use sage-native-execute in Magma interface.


---

Comment by klee created at 2010-03-20 03:38:05

Changing status from new to needs_review.


---

Attachment

I implemented the simple solution.


---

Comment by was created at 2010-04-01 00:44:06

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 18:47:14

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-16 18:47:14

Merged "trac_8560.patch" in 4.4.alpha0.
