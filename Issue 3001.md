# Issue 3001: sage ignores custom environment variables

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2008-04-22 16:48:10

Assignee: mabshoff

In sage-spkg "gcc -v" is used, instead of "${CC-gcc} -v". Easy fix:

```

---------------------------------------------------------------
--- a/sage-spkg Mon Apr 21 01:43:53 2008 -0700
+++ b/sage-spkg Tue Apr 22 12:37:48 2008 -0300
`@``@` -241,8 +241,8 `@``@`

 echo "****************************************************"
 echo "GCC Version"
-echo "gcc -v"
-gcc -v
+echo "${CC-gcc} -v"
+${CC-gcc} -v
 if [ $? -ne 0 ]; then
   echo "Unable to determine gcc version."
 fi
---------------------------------------------------------------
```



In sage-env, tests if CC is gcc, which means "CC=gcc-4.3" might not
work exactly the same as if gcc is a symlink to gcc-4.3, for instance:

```
if [ "$SAGE64" = "yes" -a CC = "gcc" ]; then
  CFLAGS="$CFLAGS -m64"
fi
```



---

Comment by mabshoff created at 2008-04-26 10:46:04

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-26 10:50:37

After thinking about this a little more: ${CC-gcc} is gcc specific and we can no longer assume that we are compiling with gcc in the first place. Hence I would like to suggest that we use `CC` and `CXX` in those places and make sure in `sage-env` that they are set.

Cheers,

Michael


---

Attachment


---

Comment by ddrake created at 2009-07-02 02:32:56

I also noticed that the sage_scripts spkg has an uncommitted change (from #6248), and a couple files that aren't checked in that perhaps should be. Whoever merges this patch should also take care of those little issues.


---

Comment by mvngu created at 2009-07-26 02:28:14

Resolution: fixed
