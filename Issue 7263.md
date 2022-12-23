# Issue 7263: sage-4.2: jmol plotting on the command line is completely broken

Issue created by migration from https://trac.sagemath.org/ticket/7263

Original creator: was

Original creation time: 2009-10-21 23:21:15

Assignee: was

CC:  kcrisman

I replicated the following with a fresh build under Linux and OS X too.  Basically *all* plotting of 3d jmol plots at the command line is broken!  The notebook works fine.  This is serious.

```
I'm having trouble with jmol from the command line in 4.1.2 and
4.2.alpha0.  E.g.,
sage: var('A,B,C')
(A, B, C)
sage: implicit_plot3d(sin(A)*cos(B)+sin(B)*cos(C)+sin(C)*cos(A),
(A,-2*pi,2*pi),(B,-2*pi,2*pi),(C,-2*pi,2*pi))
does nothing.  Adding .show() also fails, and quicker.  On
alpha.sagenb.org I don't have the same problems (though sometimes I
get the featureless black box), so I think it may be a command-line
issue.  Any ideas? I do NOT get this in 4.1.1.  I am on a MacIntel
running OSX 10.5.
```





---

Comment by jason created at 2009-10-22 01:55:31

This error is in base.pyx:

`   1085             viewer_app = "sage-native-execute " + sage.misc.misc.SAGE_LOCAL + "/java/jmol/jmol"`

jmol has apparently moved...


---

Comment by jason created at 2009-10-22 02:08:41

after this patch:


```
diff -r 241b5ed6dbbe sage/plot/plot3d/base.pyx
--- a/sage/plot/plot3d/base.pyx	Fri May 15 06:48:50 2009 -0500
+++ b/sage/plot/plot3d/base.pyx	Wed Oct 21 21:06:46 2009 -0500
@@ -1064,7 +1064,7 @@
             f.write(self.mtl_str())
             f.close()
             ext = "obj"
-            viewer_app = sage.misc.misc.SAGE_LOCAL + "/java/java3d/start_viewer"
+            viewer_app = sage.misc.misc.SAGE_LOCAL + "lib/python2.6/site-packages/sagenb/data/java/3d/lib/sage3d.jar"
 
         if DOCTEST_MODE or viewer=='jmol':
             # Temporary hack: encode the desired applet size in the end of the filename:
@@ -1082,7 +1082,7 @@
 
             T = self._prepare_for_jmol(frame, axes, frame_aspect_ratio, aspect_ratio, zoom)
             T.export_jmol(archive_name, force_reload=EMBEDDED_MODE, zoom=zoom*100, **kwds)
-            viewer_app = "sage-native-execute " + sage.misc.misc.SAGE_LOCAL + "/java/jmol/jmol"
+            viewer_app = "sage-native-execute " + sage.misc.misc.SAGE_LOCAL + "/lib/python2.6/site-packages/sagenb/data/java/jmol/Jmol.jar"
 
             # We need a script to load the file
             f = open(filename + '.jmol', 'w')
```


I get: 


```
sage: var('x,y')
(x, y)
sage: plot3d(x^2*sin(y), (x,0,1), (y,0,1)).show(viewer='java3d',verbosity=True)
sh: /home/jason/sage/local/lib/python2.6/site-packages/sagenb/data/java/3d/lib/sage3d.jar: Permission denied
sage: plot3d(x^2*sin(y), (x,0,1), (y,0,1)).show(viewer='jmol',verbosity=True)
/home/jason/sage/local/bin/sage-native-execute: 8: /home/jason/sage/local//lib/python2.6/site-packages/sagenb/data/java/jmol/Jmol.jar: Permission denied
```


What happened to the jmol application?

Also, how come jmol and the java3d viewer aren't their own spkgs?


---

Comment by jason created at 2009-10-22 02:10:50

The jmol application in 4.1.2.alpha2 was:


```/bin/sh
JMOL_HOME=`dirname "$0"`


# Collect -D & -m options as java arguments
command=java
while [ `echo $1 | egrep '^-D|^-m' | wc -l` != 0 ]; do
        command="$command $1"
        shift
done

if [ -f ./Jmol.jar ] ; then
  jarpath=./Jmol.jar
elif [ -f $JMOL_HOME/Jmol.jar ] ; then
  jarpath=$JMOL_HOME/Jmol.jar
elif [ -f /usr/share/jmol/Jmol.jar ] ; then
  jarpath=/usr/share/jmol/Jmol.jar
else
  echo Jmol.jar not found
  exit
fi
$command -Xmx512m -jar $jarpath $@
```



---

Comment by mpatel created at 2009-10-22 05:27:21

Fix paths for command-line 3d viewers.  Apply to sage repository.


---

Attachment

Update command-line 3d viewer scripts.  Apply to sagenb repository.


---

Attachment

The patches depend on #7196.


---

Comment by mpatel created at 2009-10-22 20:38:54

Changing status from new to needs_review.


---

Comment by was created at 2009-10-23 03:42:59

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-10-23 03:42:59

I merged the sagenb part of this into the official notebook hg repo.   Mhansen will have to merge the other part into sage itself.


---

Comment by mhansen created at 2009-10-23 09:03:21

Resolution: fixed
