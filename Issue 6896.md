# Issue 6896: update README.txt about GCC versions

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-09-06 02:50:22

Assignee: tba

The README.txt file in SAGE_ROOT should be updated on the supported versions of GCC. See this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/804f2c21b070902b) thread for some background.


---

Comment by mvngu created at 2009-09-06 03:40:22

An updated README.txt is attached with this ticket. That file is not under revision control. But if you want to see the changes new to this updated version, refer to `trac_6896-readme.patch`. That patch is not meant to be applied.


---

Comment by was created at 2009-09-06 04:21:26

1. This is redundant:

```
Sage builds with GCC >= 4.x and GCC >= 4.1.x.
```

how about just

```
Sage requires GCC >= 4.x.
```



---

Attachment

don't apply this patch


---

Comment by mvngu created at 2009-09-06 11:57:41

New README.txt is up together with corresponding patch file. Don't apply the patch; it's there to show differences between the README.txt currently in Sage and the new README.txt.


---

Attachment

Updates to Supperted Compilers


---

Comment by joskarsson created at 2009-09-06 22:42:27

Patch to README.txt, changing supported compilers


---

Attachment

The relevant lines of the file README.2.txt looks very good to me.


---

Comment by mvngu created at 2009-09-07 17:51:52

with changes suggested by README.txt.trac-6896-1.patch


---

Attachment

Applied the changes suggested in `README.txt.trac-6896-1.patch` and the updated README.txt is attached. See `README.txt` as `README.2.txt` doesn't have the changes in `README.txt.trac-6896-1.patch`.



joskarsson --- Please fill in your real name in the "Author(s):" field. That way, your contribution is properly acknowledged.


---

Comment by mvngu created at 2009-09-07 17:58:18

Resolution: fixed
