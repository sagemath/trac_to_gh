# Issue 6543: improve doctests for tachyon

archive/issues_006543.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: tachyon, graphics, 3d, raytracer\n\nCurrently tachyon is hardly documented or doctested at all, which is bad.  I (Marshall Hampton) will try to work on bringing it up to 100% coverage within the next month or so.  If someone wants to beat me to it, please let me know.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6543\n\n",
    "created_at": "2009-07-16T18:24:18Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "improve doctests for tachyon",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6543",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```
Assignee: @williamstein

Keywords: tachyon, graphics, 3d, raytracer

Currently tachyon is hardly documented or doctested at all, which is bad.  I (Marshall Hampton) will try to work on bringing it up to 100% coverage within the next month or so.  If someone wants to beat me to it, please let me know.

Issue created by migration from https://trac.sagemath.org/ticket/6543





---

archive/issue_comments_053243.json:
```json
{
    "body": "Attachment [trac_6543_tachyon_doctests.patch](tarball://root/attachments/some-uuid/ticket6543/trac_6543_tachyon_doctests.patch) by mhampton created at 2009-07-22 04:14:58",
    "created_at": "2009-07-22T04:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6543#issuecomment-53243",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_6543_tachyon_doctests.patch](tarball://root/attachments/some-uuid/ticket6543/trac_6543_tachyon_doctests.patch) by mhampton created at 2009-07-22 04:14:58



---

archive/issue_comments_053244.json:
```json
{
    "body": "Attachment [trac_6543_tachyon_doctests.4-1.patch](tarball://root/attachments/some-uuid/ticket6543/trac_6543_tachyon_doctests.4-1.patch) by mhampton created at 2009-07-22 04:21:11\n\nthis one is for a vanilla sage-4.1, previous patch needs #6542",
    "created_at": "2009-07-22T04:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6543#issuecomment-53244",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_6543_tachyon_doctests.4-1.patch](tarball://root/attachments/some-uuid/ticket6543/trac_6543_tachyon_doctests.4-1.patch) by mhampton created at 2009-07-22 04:21:11

this one is for a vanilla sage-4.1, previous patch needs #6542



---

archive/issue_comments_053245.json:
```json
{
    "body": "Seems like I posted a comment here that hasn't shown up.  Here it is again:\n\nI have brought coverage to 100%, and also added some functionality like axis-aligned boxes and rings (annuli).  I did delete the TachyonPlot class, which was not used by any function either in tachon.py or anywhere else in sage.  I cannot find any record of its use anywhere, so it seems like something that got 98% implemented and then abandoned.",
    "created_at": "2009-07-22T14:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6543#issuecomment-53245",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Seems like I posted a comment here that hasn't shown up.  Here it is again:

I have brought coverage to 100%, and also added some functionality like axis-aligned boxes and rings (annuli).  I did delete the TachyonPlot class, which was not used by any function either in tachon.py or anywhere else in sage.  I cannot find any record of its use anywhere, so it seems like something that got 98% implemented and then abandoned.



---

archive/issue_comments_053246.json:
```json
{
    "body": "Changing assignee from @williamstein to mhampton.",
    "created_at": "2009-07-23T03:21:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6543#issuecomment-53246",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing assignee from @williamstein to mhampton.



---

archive/issue_comments_053247.json:
```json
{
    "body": "I got a hunk rejection on Sage 4.1.1.rc2:\n\n```\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6543/trac_6543_tachyon_doctests.4-1.patch && hg qpush\nadding trac_6543_tachyon_doctests.4-1.patch to series file\napplying trac_6543_tachyon_doctests.4-1.patch\npatching file sage/plot/plot3d/tachyon.py\nHunk #19 FAILED at 1368\n1 out of 19 hunks FAILED -- saving rejects to file sage/plot/plot3d/tachyon.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nErrors during apply, please fix and refresh trac_6543_tachyon_doctests.4-1.patch\n```\n\nThe relevant hunk is:\n\n```\n--- tachyon.py                                                                  \n+++ tachyon.py                                                                  \n@@ -985,6 +1369,22 @@\n                                                                                \n         return False                                                           \n                                                                                \n-def tostr(s):                                                                  \n+def tostr(s, length = 3, out_type = float):                                    \n+    \"\"\"                                                                        \n+    Converts vector information to a space-seperated string.                   \n+                                                                               \n+    EXAMPLES::                                                                 \n+                                                                               \n+        sage: from sage.plot.plot3d.tachyon import tostr                       \n+       sage: tostr((1,1,1))                                                    \n+       ' 1.0 1.0 1.0 '                                                         \n+       sage: tostr('2 3 2')                                                    \n+       '2 3 2'                                                                 \n+    \"\"\"                                                                        \n     if isinstance(s, str):                                                     \n         return s                                                               \n+    output = ' '                                                               \n+    for an_item in s:                                                          \n+        output = output + str(out_type(an_item)) + ' '                         \n+    return output                                                              \n+\n```\n\nNote a typo in \"space-seperated\"; it should be \"space-separated\". One might also want to consider rebasing the patch `trac_6543_tachyon_doctests.4-1.patch` on top of #6727.",
    "created_at": "2009-08-12T07:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6543#issuecomment-53247",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I got a hunk rejection on Sage 4.1.1.rc2:

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6543/trac_6543_tachyon_doctests.4-1.patch && hg qpush
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
@@ -985,6 +1369,22 @@
                                                                                
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

archive/issue_comments_053248.json:
```json
{
    "body": "Rebased against 4.1.1.rc2, along with changes from patch 6727",
    "created_at": "2009-08-12T23:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6543#issuecomment-53248",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Rebased against 4.1.1.rc2, along with changes from patch 6727



---

archive/issue_comments_053249.json:
```json
{
    "body": "Attachment [trac_6543_tachyon_doctests_4.1.1.rc2.patch](tarball://root/attachments/some-uuid/ticket6543/trac_6543_tachyon_doctests_4.1.1.rc2.patch) by mvngu created at 2009-08-13 16:28:25\n\n* There is no documentation for the function `smooth_triangle()`. Can you explain what that function does?\n  * There is no docstring for the class `FractalLandscape`. The function `__init__()` seems to explain what that class does. But at the moment and with the version of Sphinx currently shipped with Sage, docstrings of functions starting with an underscore character don't show up in the generated reference manual.\n  * There is no docstring for the class `TachyonSmoothTriangle`. A docstring for that class would be nice.\n  * Can you comment out the class `TachyonPlot` instead of deleting it? It might not be used and incomplete. But someone might want to polish it up in the future.\n  * And here is a list of typos found in the rebased patch:\n  {{{\ndiff -r b0afd5bab6d9 sage/plot/plot3d/tachyon.py\n--- a/sage/plot/plot3d/tachyon.py\n+++ b/sage/plot/plot3d/tachyon.py\n`@``@` -243,6 +243,7 `@``@`\n         which is just the scene string input to tachyon.\n \n         EXAMPLES::\n+\n             sage: q = Tachyon()\n             sage: q.light((1,1,1), 1,(1,1,1))\n             sage: q.texture('s')\n`@``@` -300,9 +301,10 `@``@`\n \n     def show(self, verbose=0, extra_opts=''):\n         \"\"\"\n-        Creates a png file of the scene.\n+        Creates a PNG file of the scene.\n \n         EXAMPLES::\n+\n             sage: q = Tachyon()\n             sage: q.light((-1,-1,10), 1,(1,1,1))\n             sage: q.texture('s')\n`@``@` -338,7 +340,7 `@``@`\n     def _camera(self):\n         \"\"\"\n         An internal function that writes the tachyon string for the \n-        camera and other rendering information (raydepth, antialiasing).\n+        camera and other rendering information (ray depth, antialiasing).\n \n         EXAMPLES::\n \n`@``@` -367,7 +369,8 `@``@`\n         \"\"\"\n         Returns the complete tachyon scene file as a string.\n \n-        EXAMPLES:\n+        EXAMPLES::\n+\n             sage: t = Tachyon(xres=500,yres=500, camera_center=(2,0,0))\n             sage: t.light((4,3,2), 0.2, (1,1,1))\n             sage: t.texture('t2', ambient=0.1, diffuse=0.9, specular=0.5, opacity=1.0, color=(1,0,0))\n`@``@` -528,6 +531,7 `@``@`\n         center, radius, and texture.\n \n         EXAMPLES::\n+\n             sage: t = Tachyon()\n             sage: t.texture('sphere_texture')\n             sage: t.sphere((1,2,3), .1, 'sphere_texture')\n`@``@` -551,7 +555,7 `@``@`\n \n     def cylinder(self, center, axis, radius, texture):\n         \"\"\"\n-        Creates the scene information for a infinite cylinder with the \n+        Creates the scene information for an infinite cylinder with the \n         given center, axis direction, radius, and texture.\n \n         EXAMPLES::\n`@``@` -1138,7 +1142,7 `@``@`\n \n     def str(self):\n         \"\"\"\n-        Returns the scene string of the axis-aligned box..\n+        Returns the scene string of the axis-aligned box.\n \n         EXAMPLES::\n }}}\n* I got the following 16 warnings when building the reference manual. All of these warnings relate to the modifications made by the rebased patch. There shouldn't be any warnings at all when building the reference manual.\n {{{\nWARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.Axis_aligned_box.str:9: (WARNING/2) Literal block ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.Cylinder.str:10: (WARNING/2) Literal block ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.FCylinder.str:9: (WARNING/2) Literal block ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.FractalLandscape.str:9: (WARNING/2) Literal block ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.Plane.str:9: (WARNING/2) Literal block ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.Ring.str:9: (WARNING/2) Literal block ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.Sphere.str:11: (WARNING/2) Literal block ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.Tachyon.light:8: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.Tachyon.sphere:11: (WARNING/2) Literal block ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.TachyonSmoothTriangle.str:9: (WARNING/2) Literal block ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.TachyonSmoothTriangle.str:11: (WARNING/2) Definition list ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.TachyonTriangle.str:9: (WARNING/2) Literal block ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.TachyonTriangle.str:11: (WARNING/2) Definition list ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.TachyonTriangleFactory.smooth_triangle:12: (WARNING/2) Literal block ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.TachyonTriangleFactory.triangle:12: (WARNING/2) Literal block ends without a blank line; unexpected unindent.\nWARNING: /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python2.6/site-packages/sage/plot/plot3d/tachyon.py:docstring of sage.plot.plot3d.tachyon.TachyonTriangleFactory.triangle:14: (WARNING/2) Definition list ends without a blank line; unexpected unindent.\n }}}",
    "created_at": "2009-08-13T16:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6543#issuecomment-53249",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6543_tachyon_doctests_4.1.1.rc2.patch](tarball://root/attachments/some-uuid/ticket6543/trac_6543_tachyon_doctests_4.1.1.rc2.patch) by mvngu created at 2009-08-13 16:28:25

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

archive/issue_comments_053250.json:
```json
{
    "body": "I don't understand these docbuild problems, I need some help.  Unfortunately I haven't had time to wrestle with this lately.",
    "created_at": "2009-10-17T16:56:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6543#issuecomment-53250",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I don't understand these docbuild problems, I need some help.  Unfortunately I haven't had time to wrestle with this lately.



---

archive/issue_comments_053251.json:
```json
{
    "body": "At least one of the problems has to do with \\n characters in the docstrings. Using raw strings (r\"\"\" \"\"\") should fix it.",
    "created_at": "2009-10-23T16:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6543#issuecomment-53251",
    "user": "https://github.com/TimDumol"
}
```

At least one of the problems has to do with \n characters in the docstrings. Using raw strings (r""" """) should fix it.



---

archive/issue_comments_053252.json:
```json
{
    "body": "OK, thanks.  I will spend a little more time on this today, hopefully I can fix it up.  I replaced all strings using \"\"\" with r\"\"\", and that seems to fix the errors.  I will try to address the rest of Minh's review too.",
    "created_at": "2009-10-24T14:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6543#issuecomment-53252",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

OK, thanks.  I will spend a little more time on this today, hopefully I can fix it up.  I replaced all strings using """ with r""", and that seems to fix the errors.  I will try to address the rest of Minh's review too.



---

archive/issue_comments_053253.json:
```json
{
    "body": "new standalone patch adding doctests to Tachyon interface.  Based on 4.2.alpha1.",
    "created_at": "2009-10-24T15:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6543#issuecomment-53253",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

new standalone patch adding doctests to Tachyon interface.  Based on 4.2.alpha1.



---

archive/issue_comments_053254.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-24T15:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6543#issuecomment-53254",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_053255.json:
```json
{
    "body": "Attachment [trac_6543_tachyon_doctests_v3.patch](tarball://root/attachments/some-uuid/ticket6543/trac_6543_tachyon_doctests_v3.patch) by mhampton created at 2009-10-24 15:14:59\n\nOK, hopefully the new patch addresses all the review comments.",
    "created_at": "2009-10-24T15:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6543#issuecomment-53255",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_6543_tachyon_doctests_v3.patch](tarball://root/attachments/some-uuid/ticket6543/trac_6543_tachyon_doctests_v3.patch) by mhampton created at 2009-10-24 15:14:59

OK, hopefully the new patch addresses all the review comments.



---

archive/issue_comments_053256.json:
```json
{
    "body": "No doc warnings this time, and I cannot spot any typos. Positive review.",
    "created_at": "2009-10-26T16:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6543#issuecomment-53256",
    "user": "https://github.com/TimDumol"
}
```

No doc warnings this time, and I cannot spot any typos. Positive review.



---

archive/issue_comments_053257.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-26T16:29:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6543#issuecomment-53257",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_006779.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-10-31T07:41:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6543#event-6779"
}
```



---

archive/issue_comments_053258.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T07:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6543",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6543#issuecomment-53258",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
