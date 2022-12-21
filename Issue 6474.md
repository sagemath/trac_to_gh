# Issue 6474: PDF version of the reference manual should build successfully

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-07-07 14:34:43

Assignee: tba

Keywords: reference manual

It seems that in Sage 4.0.1.rc0, there is an error when I tried building the PDF version of the reference manual. The problem was reported on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/cae6eae2efb898b5). Here's a relevant snippet of the error log:

```
! Package inputenc Error: Keyboard character used is undefined
(inputenc)                in inputencoding `utf8'.

See the inputenc package documentation for explanation.
Type  H <return>  for immediate help.
 ...                                              
                                                  
l.64903 ...sto y[]`.  {^^Hf Bold face}.]`@`PYGaB['])
                                                  
? x
```

If you're interested, the complete LaTeX log is here:

http://sage.math.washington.edu/home/mvngu/doc/reference.log

I think this should be fixed before releasing the final version of Sage 4.1.


---

Comment by jhpalmieri created at 2009-07-07 14:59:01

Changing assignee from tba to jhpalmieri.


---

Comment by jhpalmieri created at 2009-07-07 14:59:01

I think this patch fixes it.


---

Comment by jhpalmieri created at 2009-07-07 14:59:01

Changing status from new to assigned.


---

Attachment


---

Comment by mvngu created at 2009-07-07 16:06:06

Here's how I went about testing the patch `trac_6474_pdf.patch`:
 1. Take a copy of the compressed sage.math only binary for Sage 4.1.rc0, uncompressed it, started up Sage, quit Sage, and then do `./sage -b main`.
 1. Built the HTML version of the reference manual for the main repository.
 1. Made a fresh clone of the main repository and built the HTML version of the reference manual for that cloned repository.
 1. Applied the patch `trac_6474_pdf.patch` to the cloned repository and rebuilt the HTML version of the reference manual.
 1. Finally, I built the PDF version of the reference manual. And it built successfully.


---

Comment by rlm created at 2009-07-07 20:01:13

Resolution: fixed
