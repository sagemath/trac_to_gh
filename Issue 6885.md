# Issue 6885: Excessive nesting in PDF reference manual, possibly from ring.pyx

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-09-04 08:02:16

Assignee: tba

When building the PDF reference manual on 64-bit Fedora 10:

```
[1913] [1914] [1915] [1916]
Chapter 24.

! LaTeX Error: Too deeply nested.

See the LaTeX manual or LaTeX Companion for explanation.
Type  H <return>  for immediate help.
 ...

l.154726 \begin{itemize}

?
```

I think this is near the beginning of `sage/rings/ring.pyx`.



---

Comment by mvngu created at 2009-09-22 20:14:25

Resolution: duplicate


---

Comment by mvngu created at 2009-09-22 20:14:25

Close this ticket as duplicate of #6988.
