# Issue 1006: Port Sage to 64 bit OSX 10.5

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-10-26 20:44:34

Assignee: mabshoff

Keywords: Leopard




---

Comment by mabshoff created at 2007-10-26 20:44:44

Changing status from new to assigned.


---

Comment by cwitty created at 2007-10-27 03:55:24

When this is fixed, inst/inst.tex should be updated; I just changed that file to say that OS X 10.5 is not yet supported.


---

Comment by mabshoff created at 2008-01-20 02:56:28

Changing keywords from "Leopard" to "Leopard, 64 bit".


---

Comment by mabshoff created at 2008-01-20 02:56:28

A short update: I am tracking progress at http://wiki.sagemath.org/osx64

So far there are a couple problems:

 * libSingular segfaults on import
 * numpy fails to build
 * twistedweb2 depends on some OSX specfic python extensions

Other than that it is mostly supplying the right flags in the build process. I am currently merging those OSX 10.5 64 bit build fixes for every spkg I touch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-19 05:55:47

Sage 3.0.2.alpha1 will contain a massive number of fixes. I cannot believe that it has been seven month since we opened this ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-31 09:24:47

And time marches on: ten months and counting, but 3.1.2 will get us very close to a working OSX 64 bit port. But we need to push hard to get it a fully working port.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-08 03:14:10

Provided one uses the new experimental Fortran.spkg Sage 3.3.alpha5 and later build out of the box in 64 bit mode on OSX 10.5. There are some doctesting issues left, but those will be addressed via other tickets.

So I am closing this "meta" ticket - it took way too long to fix this.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-08 03:14:10

Resolution: fixed
