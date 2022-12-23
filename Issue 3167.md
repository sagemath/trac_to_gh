# Issue 3167: notebook -- jmol 3d plots in the dynamic live worksheet-based reference manual do not work

Issue created by migration from https://trac.sagemath.org/ticket/3167

Original creator: was

Original creation time: 2008-05-12 03:58:55

Assignee: was

1. Go to the 3d plots section of the reference manual, e.g.,
 http://localhost:8000/doc/live/ref/module-sage.plot.plot3d.parametric-plot3d.html

2. Hit shift-enter to evaluate a plot.

3. Observe that the plot doesn't work. 


This should be easy to replicate on all operating systems, etc.  This bug was 
reported by walter neumann on March 11, 2008.


----

As a temporary workaround you can do the following:

  1. View the page of the html reference manual of interest to you that contains 3d plotting code.
  2. Click in the upper left on File -> Copy Worksheet.

You'll get a complete copy of the page of the reference manual
as a normal worksheet.  You can then use shift-enter to evaluate
3d plots and they should work fine in that copy (since it is
just a normal worksheet).




---

Comment by mabshoff created at 2008-05-29 20:29:29

It would be nice if we could fix this soon.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-29 20:29:29

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-09-29 22:41:07

Changing assignee from was to mhansen.


---

Comment by mabshoff created at 2008-09-29 22:41:07

This is fixed by Mike Hansen's transformation of the documentation to ReST. So once this happens this ticket ought to be closed.

Cheers,

Michael


---

Comment by was created at 2009-04-22 13:34:38


```
This is about http://trac.sagemath.org/sage_trac/ticket/3167

If I open a new worksheet and execute

x,y=var('x,y')
plot3d(sin(x*y),(x,-4,4),(y,-4,4))

I see this in Opera's Java Console:

Jmol applet jmolApplet1__319875117923755__ destroyed
Jmol applet jmolApplet2__319875117923755__ initializing
AppletRegistry.checkIn(jmolApplet2__319875117923755__)
applet context: -applet
appletDocumentBase=http://localhost:8000/home/admin/11/
appletCodeBase=http://localhost:8000/java/jmol/
(C) 2008 Jmol Development
Jmol Version 11.6.16  2008-11-24 13:39
java.vendor:Sun Microsystems Inc.
java.version:1.6.0_13
os.name:Linux
memory:13.2/55.1
useCommandThread: false
appletId:jmolApplet2__319875117923755__
FileManager opening http://localhost:8000/java/jmol/appletweb/SageMenu.mnu
urlImage=jar:http://localhost:8000/java/jmol/JmolApplet0.jar!/jmol75x29x8.gif
defaults = "Jmol"
backgroundColor = "black"
language=en_US
FileManager opening
http://localhost:8000/home/admin/11/cells/17/sage0-size500.jmol?1240378461
FileManager opening
http://localhost:8000/home/admin/11/sage0-size500-481666882.jmol.zip
FileManager.openStringInline()
The Resolver thinks Xyz
ModelSet: haveSymmetry:false haveUnitcells:false haveFractionalCoord:false
1 model in this collection. Use getProperty "modelInfo" or getProperty
"auxiliaryInfo" to inspect them.
ModelSet: autobonding; use  autobond=false  to not generate bonds
automatically
data "model list"
10
empty
Xx -6.0 -7.0 -3.0
Xx 0.0 -7.0 -3.0
Xx 6.0 -7.0 -3.0
Xx 7.0 -6.0 -3.0
Xx 7.0 0.0 -3.0
Xx 7.0 6.0 -3.0
Xx -7.0 -6.0 -3.0
Xx -7.0 -6.0 0.0
Xx -7.0 -6.0 3.0
Xx 5.5 5.5 5.5

end "model list";
FileManager opening
http://localhost:8000/home/admin/11/sage0-size500-481666882.jmol.zip
reading pmesh data from
http://localhost:8000/home/admin/11/sage0-size500-481666882.jmol.zip|obj_832199.pmesh



If I do the same in a docbrowser sheet, I see

Jmol applet jmolApplet0__307075267903545__ initializing
urlImage=jar:http://localhost:8000/java/jmol/JmolApplet0.jar!/jmol75x29x8.gif
AppletRegistry.checkIn(jmolApplet0__307075267903545__)
applet context: -applet
appletDocumentBase=http://localhost:8000/doc/live/tutorial/tour_plotting.html
appletCodeBase=http://localhost:8000/java/jmol/
(C) 2008 Jmol Development
Jmol Version 11.6.16  2008-11-24 13:39
java.vendor:Sun Microsystems Inc.
java.version:1.6.0_13
os.name:Linux
memory:14.2/58.9
useCommandThread: false
appletId:jmolApplet0__307075267903545__
FileManager opening http://localhost:8000/java/jmol/appletweb/SageMenu.mnu
defaults = "Jmol"
backgroundColor = "black"
language=en_US
FileManager opening
http://localhost:8000/home/_sage_/85/cells/33/sage0-size500.jmol?1240378560
FileManager opening
http://localhost:8000/doc/live/tutorial/sage0-size500-224802342.jmol.zip
script ERROR: io error reading
http://localhost:8000/doc/live/tutorial/sage0-size500-224802342.jmol.zip|SCRIPT:
java.io.FileNotFoundException:
http://localhost:8000/doc/live/tutorial/sage0-size500-224802342.jmol.zip
eval ERROR:
----line 2 command 2 of file
/home/_sage_/85/cells/33/sage0-size500.jmol?1240378560:
        script >> "SCRIPT" <<
----line 1 command 1:
        script >>
"/home/_sage_/85/cells/33/sage0-size500.jmol?1240378560" <<


which "explains" the blank applet (i.e., no plot).  Apparently, the
notebook finds and serves up the zip file when it's requested relative
to the base URL of an ordinary worksheet, but it does not do the same
for a live doc worksheet.

Though I have not yet tried it, one fix that springs to mind is to
encode the full URL of the archive in plot.plot3d.base.show().  But this
seems to be a server (permissions?) issue.  Once again, I'm in over my
head, so it would be great to get some input.

The logs above are from Sun's 64-bit JDK in Opera 9 on Fedora 9.  I
don't know how to access the Java console in Firefox, but I've
experienced the same behavior in both the 32-bit and 64-bit versions.

 -- "Pat LeSmithe"
```



---

Comment by was created at 2009-06-15 23:20:19

If we're going to release for months and months without fixing this, it's clearly not a blocker.


---

Comment by was created at 2009-06-15 23:20:19

Changing priority from blocker to critical.


---

Attachment


---

Comment by mpatel created at 2009-06-20 15:41:00

Maybe there's a better way with Jmol itself, but the patch appears to work.  `cell.py` seems to be a convenient place to do this.


---

Comment by jhpalmieri created at 2009-06-28 23:41:43

Works for me: 3d plots in the tutorial produced black boxes before this, and produced nice plots after applying the patch.  (Is it right that the only relevant place is the tutorial: the reference manual is no longer live, is it?)


---

Comment by mpatel created at 2009-06-29 00:57:26

Replying to [comment:7 jhpalmieri]:
> Works for me: 3d plots in the tutorial produced black boxes before this, and produced nice plots after applying the patch.  (Is it right that the only relevant place is the tutorial: the reference manual is no longer live, is it?)

I just checked that the tutorial, developer guide, and constructions guide are [or can be] live, but the reference manual is not, apparently.  It may not be difficult to render a reference or docstring docbrowser on-the-fly.  Perhaps it's better to set up inline frames, a la [this example](http://groups.google.com/group/sage-devel/browse_thread/thread/1ea045d16e60b1b2/4f07263ea5982965?#4f07263ea5982965), so that doc frames have their own instances of the Sage engine.  I think this would also enable interactive, live documentation, even while the main worksheet process is busy with a computation.


---

Comment by rlm created at 2009-07-03 17:09:42

Resolution: fixed
