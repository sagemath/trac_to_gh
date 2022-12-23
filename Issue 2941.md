# Issue 2941: sympy spkg updated + a test patch for Sage

Issue created by migration from https://trac.sagemath.org/ticket/2941

Original creator: certik

Original creation time: 2008-04-16 09:37:36

Assignee: mabshoff

Apply the attached patch to Sage, then install the attached spkg.


---

Comment by certik created at 2008-04-16 09:39:54

Sage patch, fixing the tests


---

Attachment

*Important note*: execute this command

rm -r sage/local/lib/python2.5/site-packages/sympy*

before installing the spkg, otherwise sympy will be broken.


---

Comment by mabshoff created at 2008-04-16 09:54:20

Changing component from Cygwin to packages.


---

Comment by mabshoff created at 2008-04-16 09:54:20

Replying to [comment:1 certik]:
> *Important note*: execute this command
> 
> rm -r sage/local/lib/python2.5/site-packages/sympy*
> 
> before installing the spkg, otherwise sympy will be broken.

Hi Ondrej,

this must be done in spkg-install, otherwise it will break people's install. 

On another note: There already way #1633 assigned to you as the sympy upgrade ticket. I have closed that as a duplicate.

Cheers,

Michael


---

Attachment


---

Comment by certik created at 2008-04-16 11:52:50

Thanks I committed the patch below and attached a new spkg.

diff -r 029e5541f507 -r 2111fce6f538 spkg-install
--- a/spkg-install	Wed Apr 16 11:28:19 2008 +0200
+++ b/spkg-install	Wed Apr 16 13:44:47 2008 +0200
`@``@` -1,4 +1,14 `@``@`
 #!/bin/sh
+
+# We need to delete the old path, so that there are no leftovers from the
+# previous installation, otherwise sympy could get broken (for example by
+# importing some local files instead of the standard library ones...)
+if [ "$SAGE_ROOT" = "" ]; then
+    echo "Please set the SAGE_ROOT variable"
+    exit 1
+fi
+echo "Deleting $SAGE_ROOT/local/lib/python2.5/site-packages/sympy*"
+rm -rf $SAGE_ROOT/local/lib/python2.5/site-packages/sympy*
 
 cd src/


---

Comment by certik created at 2008-04-16 11:53:37

The patch got screwed up, so again:


```
diff -r 029e5541f507 -r 2111fce6f538 spkg-install
--- a/spkg-install	Wed Apr 16 11:28:19 2008 +0200
+++ b/spkg-install	Wed Apr 16 13:44:47 2008 +0200
@@ -1,4 +1,14 @@
 #!/bin/sh
+
+# We need to delete the old path, so that there are no leftovers from the
+# previous installation, otherwise sympy could get broken (for example by
+# importing some local files instead of the standard library ones...)
+if [ "$SAGE_ROOT" = "" ]; then
+    echo "Please set the SAGE_ROOT variable"
+    exit 1
+fi
+echo "Deleting $SAGE_ROOT/local/lib/python2.5/site-packages/sympy*"
+rm -rf $SAGE_ROOT/local/lib/python2.5/site-packages/sympy*
 
 cd src/
```



---

Comment by mabshoff created at 2008-04-17 06:35:32

Parch and spgk are good, pass doctests. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-17 06:35:51

Resolution: fixed


---

Comment by mabshoff created at 2008-04-17 06:35:51

Merged in Sage 3.0.alpha6
