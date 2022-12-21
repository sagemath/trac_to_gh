# Issue 3384: Issues a warning for all unsupported / poorly supported operating systems.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2008-06-08 20:32:25

Assignee: mabshoff

If one tries to build Sage on Solaris, a warning is issued saying Solaris is not fully supported and difficult to compile on. An option to set the variable SAGE_PORT to a non zero value is then issued, which allows one to attept to build on Solaris. 

In contrast, totally unsupported operating systems (e.g. HP-UX) generate no warning whatsoever. Trying to compile on HP-UX, will just start compiling with no warnings whatsoever. 

Hence there needs to take 3, depending on operating system

1) No message, if using a fully supported operating system such as Linux or OSX
2) A warning that building is likely to be difficult if the system is not fully supported, but actively developed (e.g. Solaris)
3) A clear warning that the operating system is totally unsupported, and therefore is likely to need some effort to port to, on any other operating system. I would suggest not testing for the OS, but leaving this as a default. 

ie. in pseudo code. 

OS=uname
if ($OS == Linux || $OS == OSX) {
  dont print any message
}
else if ($OS == Solaris) {
  issues warning about not fully supported, set SAGE_PORT to non-zero. 
} 
else {
  issue warning the platform is not supported at all, and might need a porting effort. Again offer SAGE_PORT option
} 




---

Comment by was created at 2009-10-07 15:43:26

Resolution: fixed
