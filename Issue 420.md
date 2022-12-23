# Issue 420: SAGE's optional axiom package doesn't build on os x

Issue created by migration from https://trac.sagemath.org/ticket/420

Original creator: was

Original creation time: 2007-08-10 20:20:28

Assignee: was

The title says it all. 


---

Comment by pdehaye created at 2007-08-13 08:37:28

gcl hasn't been ported to intel macs yet.
in short no one has created the file 
axiom4sage-0.1/lsp/gcl-2.6.8pre/h/intel-macosx.defs 
, and the file 
axiom4sage-0.1/lsp/gcl-2.6.8pre/h/powerpc-macosx.defs
won't do

when trying to build, the problem appears when configure has no type to chose from.


---

Comment by was created at 2007-08-18 23:36:52

i fixed this on the plane to san diego.  now it works with the *new* aiom package that builds on CLISP.

William


---

Comment by was created at 2007-08-18 23:36:52

Resolution: fixed
