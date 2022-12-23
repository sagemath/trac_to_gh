# Issue 6701: prereq-0.3.tar has many issues and needs updating.

Issue created by migration from https://trac.sagemath.org/ticket/6701

Original creator: drkirkby

Original creation time: 2009-08-09 08:24:09

Assignee: tbd

There are numerous sensible things the prereq-0.3.tar could do which it does not currently do. 

 * The old version detects if gcc is version 3 or above, yet at least 4.0.1 is needed to build Sage. 

 * The old version fails to let one use a non-GNU compiler. Whilst I realise such compilers are unsupported in Sage, it would be sensible to issue a warning and let people continue. The Sun compilers are better than gcc on Solaris - particularly for 64-bit code.  

 * The old version does not check if the versions of the GNU compilers are all the same. So if one sets CC to one version of gcc (say 4.4.0) and forgets to set CXX and/or SAGE_FORTRAN, this will not be detected. So older version of those might be found. Building some files with one version of gcc and other files with another will not work reliably (if at all)


 * I understand some version of 4.0.1 on OS X will build Sage, but an older release of the tools with gcc 4.0.1 will not. This problem is not detected. 

 * The old configure.ac is not really written as configure.ac scripts are supposed to be written. It does not make sensible use of macros, but has inline code which is not even working well. 


 * No doubt other things. 

I intend making an updated version of at least configure.ac which fixes these and any other possible build issues I can think of. 




---

Comment by was created at 2009-10-07 15:43:14

Resolution: fixed
