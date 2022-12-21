# Issue 6543: improve doctests for tachyon

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2009-07-16 18:24:18

Assignee: was

Keywords: tachyon, graphics, 3d, raytracer

Currently tachyon is hardly documented or doctested at all, which is bad.  I (Marshall Hampton) will try to work on bringing it up to 100% coverage within the next month or so.  If someone wants to beat me to it, please let me know.


---

Attachment


---

Attachment

this one is for a vanilla sage-4.1, previous patch needs #6542


---

Comment by mhampton created at 2009-07-22 14:49:59

Seems like I posted a comment here that hasn't shown up.  Here it is again:

I have brought coverage to 100%, and also added some functionality like axis-aligned boxes and rings (annuli).  I did delete the TachyonPlot class, which was not used by any function either in tachon.py or anywhere else in sage.  I cannot find any record of its use anywhere, so it seems like something that got 98% implemented and then abandoned.


---

Comment by mhampton created at 2009-07-23 03:21:46

Changing assignee from was to mhampton.


---

Comment by mvngu created at 2009-08-12 07:20:02

I got a hunk rejection on Sage 4.1.1.rc2:

```
[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6543/trac_6543_tachyon_doctests.4-1.patch && hg qpush
adding trac_6543_tachyon_doctests.4-1.patch to series file
applying trac_6543_tachyon_doctests.4-1.patch
patching file sage/plot/plot3d/tachyon.py
Hunk #19 FAILED at 1368
1 out of 19 hunks FAILED -- saving rejects to file sage/plot/plot3d/tachyon.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_6543_tachyon_doctests.4-1.patch
```

The relevant hunk is:

```
--- tachyon.py                                                                  
+++ tachyon.py                                                                  
`@``@` -985,6 +1369,22 `@``@`
                                                                                
         return False                                                           
                                                                                
-def tostr(s):                                                                  
+def tostr(s, length = 3, out_type = float):                                    
+    """                                                                        
+    Converts vector information to a space-seperated string.                   
+                                                                               
+    EXAMPLES::                                                                 
+                                                                               
+        sage: from sage.plot.plot3d.tachyon import tostr                       
+       sage: tostr((1,1,1))                                                    
+       ' 1.0 1.0 1.0 '                                                         
+       sage: tostr('2 3 2')                                                    
+       '2 3 2'                                                                 
+    """                                                                        
     if isinstance(s, str):                                                     
         return s                                                               
+    output = ' '                                                               
+    for an_item in s:                                                          
+        output = output + str(out_type(an_item)) + ' '                         
+    return output                                                              
+
```

Note a typo in "space-seperated"; it should be "space-separated". One might also want to consider rebasing the patch `trac_6543_tachyon_doctests.4-1.patch` on top of #6727.


---

Comment by mhampton created at 2009-08-12 23:07:40

Rebased against 4.1.1.rc2, along with changes from patch 6727


---

Attachment

* There is no documentation for the function `smooth_triangle()`. Can you explain what that function does?
 * There is no docstring for the class `FractalLandscape`. The function `__init__()` seems to explain what that class does. But at the moment and with the version of Sphinx currently shipped with Sage, docstrings of functions starting with an underscore character don't show up in the generated reference manual.
 * There is no docstring for the class `TachyonSmoothTriangle`. A docstring for that class would be nice.
 * Can you comment out the class `TachyonPlot` instead of deleting it? It might not be used and incomplete. But someone might want to polish it up in the future.
 * And here is a list of typos found in the rebased patch:
 {{{
diff -r b0afd5bab6d9 sage/plot/plot3d/tachyon.py
--- a/sage/plot/plot3d/tachyon.py
+++ b/sage/plot/plot3d/tachyon.py
`@``@` -243,6 +243,7 `@``@`
         which is just the scene string input to tachyon.
 
         EXAMPLES::
+
             sage: q = Tachyon()
             sage: q.light((1,1,1), 1,(1,1,1))
             sage: q.texture('s')
`@``@` -300,9 +301,10 `@``@`
 
     def show(self, verbose=0, extra_opts=''):
         """
-        Creates a png file of the scene.
+        Creates a PNG file of the scene.
 
         EXAMPLES::
+
             sage: q = Tachyon()
             sage: q.light((-1,-1,10), 1,(1,1,1))
             sage: q.texture('s')
`@``@` -338,7 +340,7 `@``@`
     def _camera(self):
         """
         An internal function that writes the tachyon string for the 
-        camera and other rendering information (raydepth, antialiasing).
+        camera and other rendering information (ray depth, antialiasing).
 
         EXAMPLES::
 
`@``@` -367,7 +369,8 `@``@`
         """
         Returns the complete tachyon scene file as a string.
 
-        EXAMPLES:
+        EXAMPLES::
+
             sage: t = Tachyon(xres=500,yres=500, camera_center=(2,0,0))
             sage: t.light((4,3,2), 0.2, (1,1,1))
             sage: t.texture('t2', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(1,0,0))
`@``@` -528,6 +531,7 `@``@`
         center, radius, and texture.
 
         EXAMPLES::
+
             sage: t = Tachyon()
             sage: t.texture('sphere_texture')
             sage: t.sphere((1,2,3), .1, 'sphere_texture')
`@``@` -551,7 +555,7 `@``@`
 
     def cylinder(self, center, axis, radius, texture):
         """
-        Creates the scene information for a infinite cylinder with the 
+        Creates the scene information for an infinite cylinder with the 
         given center, axis direction, radius, and texture.
 
         EXAMPLES::
`@``@` -1138,7 +1142,7 `@``@`
 
     def str(self):
         """
-        Returns the scene string of the axis-aligned box..
+        Returns the scene string of the axis-aligned box.
 
         EXAMPLES::
 }}}
 * I got the following 16 warnings when building the reference manual. All of these warnings relate to the modifications made by the rebased patch. There shouldn't be any warnings at all when building the reference manual.
 {{{
WARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.Axis_aligned_box.str:9: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.Cylinder.str:10: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.FCylinder.str:9: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.FractalLandscape.str:9: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.Plane.str:9: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.Ring.str:9: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.Sphere.str:11: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.Tachyon.light:8: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.Tachyon.sphere:11: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.TachyonSmoothTriangle.str:9: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.TachyonSmoothTriangle.str:11: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.TachyonTriangle.str:9: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.TachyonTriangle.str:11: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.TachyonTriangleFactory.smooth_triangle:12: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.TachyonTriangleFactory.triangle:12: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.TachyonTriangleFactory.triangle:14: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
 }}}


---

Comment by mhampton created at 2009-10-17 16:56:56

I don't understand these docbuild problems, I need some help.  Unfortunately I haven't had time to wrestle with this lately.


---

Comment by timdumol created at 2009-10-23 16:32:57

At least one of the problems has to do with \n characters in the docstrings. Using raw strings (r""" """) should fix it.


---

Comment by mhampton created at 2009-10-24 14:46:28

OK, thanks.  I will spend a little more time on this today, hopefully I can fix it up.  I replaced all strings using """ with r""", and that seems to fix the errors.  I will try to address the rest of Minh's review too.


---

Comment by mhampton created at 2009-10-24 15:13:28

new standalone patch adding doctests to Tachyon interface.  Based on 4.2.alpha1.


---

Comment by mhampton created at 2009-10-24 15:14:59

Changing status from needs_work to needs_review.


---

Attachment

OK, hopefully the new patch addresses all the review comments.


---

Comment by timdumol created at 2009-10-26 16:29:29

No doc warnings this time, and I cannot spot any typos. Positive review.


---

Comment by timdumol created at 2009-10-26 16:29:29

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-31 07:41:56

Resolution: fixed
