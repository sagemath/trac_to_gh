# Issue 1521: rebuilding ntl_GF2.pyx fails spectecularly on OSX 10.4 with moved install/binary install

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-15 06:29:50

Assignee: mabshoff


```
g++ -bundle -undefined dynamic_lookup build/temp.macosx-10.3-ppc-2.5/sage/libs/ntl/ntl_GF2.o 
-L/Users/mabshoff/sage-2.9.alpha7-PowerMacintosh-Darwin/local//lib -lcsage -lcsage -lntl -lstdc++ 
-lstdc++ -lntl -o build/lib.macosx-10.3-ppc-2.5/sage/libs/ntl/ntl_GF2.so
```



---

Comment by mabshoff created at 2007-12-15 06:30:33

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 06:33:24

Craig Citro was faster, see #1520.


---

Comment by mabshoff created at 2007-12-15 06:35:53

Resolution changed from fixed to 


---

Comment by mabshoff created at 2007-12-15 06:35:53

Changing status from closed to reopened.


---

Comment by mabshoff created at 2007-12-15 06:36:01

Resolution: duplicate
