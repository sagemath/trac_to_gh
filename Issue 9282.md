# Issue 9282: Sage doctest failures

Issue created by migration from Trac.

Original creator: retry

Original creation time: 2010-06-20 12:58:22

Assignee: mvngu

sage -testall fails at:

sage -t  "devel/sage/sage/modular/hecke/submodule.py"

sage -t  "devel/sage/sage/modular/abvar/abvar.py"

sage -t  "devel/sage/sage/lfunctions/sympow.py"

sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"

sage -t  "devel/sage/sage/interfaces/qepcad.py"



Compiled with: GCC 4.5.0

Distribution: Arch Linux 32 bit


---

Comment by retry created at 2010-06-20 12:59:08

sage -testall log, with tracebacks.


---

Attachment

Recompiled sage - no more problems.


---

Comment by retry created at 2010-06-22 07:45:38

Resolution: invalid
