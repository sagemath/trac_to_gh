# Issue 5436: more miscellaneous typos

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-03-04 04:40:41

Assignee: tba

While reviewing ticket #5416, I came across a number of typos I saw in the rebased patch for that ticket. These problems were *not* introduced by the patch; they were not addressed.


---

Comment by mvngu created at 2009-03-04 05:46:55

fixed typos in response to ticket #5416


---

Attachment

The patch fixes a number of typos I noticed while reviewing ticket #5416. It depends, of course, on applying #5416 first, and is based on Sage 3.4.rc0.


---

Comment by mabshoff created at 2009-03-04 22:29:21

Looks good to me. This hunk

```
-        Watch out, Magma has different semantics than Sage, i.e., in Magma
+        Watch out, Magma has different semantics from Sage, i.e., in Magma
```

seemed on first reading a little odd, but now I do agree with the change.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-04 22:31:07

Resolution: fixed


---

Comment by mabshoff created at 2009-03-04 22:31:07

Merged in Sage 3.4.rc1.

Cheers,

Michael
