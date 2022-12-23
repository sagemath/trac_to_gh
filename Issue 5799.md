# Issue 5799: [with patch, needs review] jsMath, favicon, and logo for live, static, and offline docs

Issue created by migration from https://trac.sagemath.org/ticket/5799

Original creator: mpatel

Original creation time: 2009-04-16 04:35:32

Assignee: tba

A few changes to

* Enable jsMath in static and offline docs.

* Display a Sage favicon in static and offline docs.

* Display a Sage logo in live, static, and offline docs.

"Offline" docs are just those accessed via file:///.

I'm not sure whether/how Mercurial handles binary files, so I've attached two patches.  One mentions the added favicon and logo files; the other doesn't.  To get the png files themselves in the right place, I first created doc/common/static.  Then, in this directory I did

wget http://www.sagemath.org/pix/sageicon.png

and

ln -s ../../../../../data/extcode/notebook/images/sagelogo.png .

I've attached these, too.

Note: There's a favicon.ico in the same extcode directory, but it's not transparent.  There is another sagelogo.png in SAGE_ROOT/data/extcode/images, but its dimensions are larger.

The jsMath issue was mentioned on sage-devel:

http://groups.google.com/group/sage-devel/browse_thread/thread/40eab3f9610e061d/eb93a3930e79ea3a?#eb93a3930e79ea3a

The favicon and logo were mentioned in connection with a doc sidebar toggle:

http://groups.google.com/group/sage-devel/browse_thread/thread/8c8fe7c5d0c0f725/4807f5553bdbd6b0?#4807f5553bdbd6b0

I'll make a separate ticket for the toggle.


---

Comment by mabshoff created at 2009-04-16 05:56:43

To create a patch that contains a png you need to export a git style patch. Then export two patches, one for the Sage library and one for the ext repo. The names should be 

 * trac_5799_sage_$FOO
 * trac_5799_ext_$BAR
 
respectively. It is generally a good idea to split tickets into independent tasks, i.e. this is a borderline case and can be done via one ticket.

This also strikes me as kind of odd:

```
<script type="text/javascript" src="../../../../../../../local/notebook/javascript/jsmath/easy/load.js"></script> 
```

given that everywhere else we use 

```
<script type="text/javascript" src="/javascript_local/$FOO"></script>
```

but that might be unavoidable. 


Cheers,

Michael


---

Attachment


---

Comment by mpatel created at 2009-04-16 08:20:56

Replying to [comment:1 mabshoff]:
> To create a patch [...]

Thanks for the tips!  Take two attached.

> This also strikes me as kind of odd:

I'm about to attach an alternative to trac_5799_sage_jsmath_doc.patch.


---

Attachment

Somewhat less efficient alternative to trac_5799_sage_jsmath_doc.patch.


---

Comment by mabshoff created at 2009-04-16 08:57:41

Cool, I deleted the old patches to make the history cleaner. If you post updated patches you should also change back the summary to "needs review". I did that in this case already.

Cheers,

Michael


---

Comment by justin created at 2009-04-17 15:49:46

I applied the 'ext' and 'alt sage' patches, and tested "en/tutorial html".  It all looks good.


---

Comment by mpatel created at 2009-06-10 09:23:55

Better cross-browser favicon support. Goes with trac_5799_sage_jsmath_doc_v2.patch.


---

Attachment

Better cross-browser favicon support, auto relative paths. Apply trac_5799_ext_icons_v2.patch first.


---

Comment by mpatel created at 2009-06-10 10:24:04

The `*_v2` pair replaces the earlier versions.

 * Same [sageicon.png](http://www.sagemath.org/pix/sageicon.png) as in the first patch.
 * ImageMagick gives a "true" ico file: `convert sageicon.png favicon.ico`.
 * Tested in FF3, O9 on Linux, and in Cr2, FF3, IE8, O9, S3 on Windows XP. Whether the icon is transparent and visible for live, static, and offline docs is browser-dependent.
 * Automatic relative paths for the favicon, logo, and jsMath.  This is important, e.g., in the reference manual.
 * #4714 should take care of the unknown jsMath macros.


---

Comment by jhpalmieri created at 2009-06-27 17:06:07

Looks good.  Positive review.

Does this mean that we should make `--jsmath` the default for building html docs?  It's much faster than building without using jsmath.


---

Comment by mpatel created at 2009-06-27 22:39:28

Replying to [comment:7 jhpalmieri]:
> Does this mean that we should make `--jsmath` the default for building html docs?  It's much faster than building without using jsmath.

I think `\QQ` and friends generate an unsightly error message.  I'll try to learn how to make an spkg, for #4714 and #5447.


---

Comment by rlm created at 2009-07-04 01:40:30

Resolution: fixed


---

Comment by rlm created at 2009-07-04 21:10:14

In order to get the `sage -sdist` command to work after applying this patch, I had to copy all of the files over to `doc/common/static` as actual files, since something in the build system could not find the files as links. I will post the extra patch on this ticket, which was necessary to roll `sage-4.1.rc0`.


---

Comment by rlm created at 2009-07-04 21:20:03

This is what happened:

```
[geom sage-4.1.alpha3]$ ./sage -sdist 4.1.rc0
Updating Cython code....
Time to execute 0 commands: 1.50203704834e-05 seconds
Finished compiling Cython code (time = 0.324697971344 seconds)
running install
running build
running build_py
copying sage/version.py -> build/lib.linux-x86_64-2.6/sage
running build_ext
Total time spent compiling C/C++ extensions:  0.00903582572937 seconds.
running install_lib
copying build/lib.linux-x86_64-2.6/sage/version.py -> /space/rlm/sage-4.1.alpha3/local/lib/python2.6/site-packages/sage
byte-compiling /space/rlm/sage-4.1.alpha3/local/lib/python2.6/site-packages/sage/version.py to version.pyc
running install_egg_info
Writing /space/rlm/sage-4.1.alpha3/local/lib/python2.6/site-packages/sage-4.1.rc0-py2.6.egg-info
cp: cannot stat `*.sage': No such file or directory
cp: cannot stat `ipythonrc': No such file or directory
cp: cannot stat `spkg/update': No such file or directory
rm: cannot remove `doc-*.spkg': No such file or directory
diff -r f307132d9d7c sage/version.py
--- a/sage/version.py   Thu Jul 02 11:52:36 2009 +0200
+++ b/sage/version.py   Sat Jul 04 12:58:13 2009 -0700
@@ -1,2 +1,2 @@
 """nodoctests"""
-version='4.1.alpha3'; date='2009-07-02'
+version='4.1.rc0'; date='2009-07-04'
M sage/version.py
cp: cannot stat `build.py': No such file or directory
cp: cannot stat `clib.py': No such file or directory
cp: cannot stat `sagebuild.py': No such file or directory
cp: warning: source file `spkg-delauto' specified more than once
cp: cannot stat `debian': No such file or directory
rm: cannot remove `c_lib/*.so': No such file or directory
rm: cannot remove `c_lib/*.os': No such file or directory
Deleting autogenerated file ./matrix/matrix_rational_dense.c

...<SNIP>...

Deleting autogenerated file ./algebras/quatalg/quaternion_algebra_cython.cpp
running sdist
error: doc/common/static/sageicon.png: No such file or directory
./spkg-dist: line 54: cd: dist: No such file or directory
gzip: sage-4.1.rc0.tar.gz: No such file or directory
bzip2: Can't open input file sage-4.1.rc0.tar: No such file or directory.
mv: cannot stat `sage-4.1.rc0.tar.bz2': No such file or directory
mv: cannot stat `dist/sage-4.1.rc0.spkg': No such file or directory
The package sage-4.1.rc0.spkg wasn't created.
Error building the Sage packages.
```


No point in posting a huge patch, so here is a link:

http://sage.math.washington.edu/home/rlmill/trac_5799-unlink.patch


---

Comment by mpatel created at 2009-07-05 23:26:51

The new patch seems to have the same observable effect as the previous set in the usual browsers on Linux and Windows XP.  But the AMS symbol font `msbm10` won't be available in the static and offline docs.

I'll venture that having extra copies of the favicons and logo in the Sage tree is not a big deal.  Ideally, jsMath should have a single home, e.g., so that planned changes (cf. #4714) to `easy/load.js` affect the live, static, and offline docs equally.

Perhaps we can make the symbolic link itself in jsMath's `spkg-install`.  Does this mean we should remove the link from version control?  If so, we're [almost] done.


---

Comment by rlm created at 2009-07-07 18:51:46

I'm worried, since a fresh install of sage-4.1.rc0 is missing most of these files in `doc/common/static`:


```
[geom sage-main]$ cd doc/common/static/
[geom static]$ ls
total 4.0K
drwxr-xr-x 3 rlmill rlmill 4.0K 2009-07-04 14:18 jsmath
[geom static]$ ls jsmath
total 16K
-rw-r--r-- 1 rlmill rlmill  12K 2009-07-04 14:13 COPYING.txt
drwxr-xr-x 3 rlmill rlmill 4.0K 2009-07-04 14:18 fonts
```


Has anyone tested a fresh build of sage-4.1.rc0 to see if things related to this ticket work?


---

Comment by rlm created at 2009-07-07 18:58:27

I'm seriously thinking about reverting this ticket, since there are obviously some assumptions the sdist script is making, which are conflicting with the solutions used for this patch. For now, I'm reopening the ticket, until I can get this resolved one way or another.


---

Comment by rlm created at 2009-07-07 18:58:27

Changing status from closed to reopened.


---

Comment by rlm created at 2009-07-07 18:58:27

Resolution changed from fixed to 


---

Attachment


---

Comment by jhpalmieri created at 2009-07-07 19:41:23

This is a bit of a shot in the dark, but does trac_5799_manifest.patch help?


---

Comment by rlm created at 2009-07-07 19:55:29

Replying to [comment:15 jhpalmieri]:
> This is a bit of a shot in the dark, but does trac_5799_manifest.patch help?

I think this is what I was looking for. Thank you!


---

Comment by rlm created at 2009-07-07 21:22:17

Resolution: fixed


---

Comment by rlm created at 2009-07-07 21:22:17

`trac_5799_manifest.patch` merged in sage-4.1.rc1


---

Comment by rlm created at 2009-07-08 01:55:35

As suggested by William, the `MANIFEST.in` changes were reverted to just adding the line `recursive-include doc/common/static *`.

http://docs.python.org/distutils/commandref.html#sdist-cmd


---

Comment by mpatel created at 2009-07-19 06:51:07

Is it possible to include symbolic links in `MANIFEST.in`?  Unless I'm wrong, we now have jsMath installed in `doc/common/static` *and* `javascript_local`.  Do we really want this?  Besides putting upstream code under version control in the Sage library, this complicates, e.g., the resolution of #4714.


---

Comment by rlm created at 2009-07-20 14:44:00

Replying to [comment:20 mpatel]:
> Is it possible to include symbolic links in `MANIFEST.in`?

I had wondered this myself. The only way to know for sure is to try it, roll a new source tarball (via `sage -sdist`), install the "new version," and see whether the notebook still works...


---

Comment by mpatel created at 2009-07-21 10:52:44

Attempt to get distutils to preserve symbolic links.


---

Attachment

Replying to [comment:21 rlm]:
> Replying to [comment:20 mpatel]:
> > Is it possible to include symbolic links in `MANIFEST.in`?
> I had wondered this myself. The only way to know for sure is to try it, roll a new source tarball (via `sage -sdist`), install the "new version," and see whether the notebook still works...
This [attachment:trac_5799-redux_setup_py.patch patch] alters `setup.py` so that it preserves symlinks.  However, I'm far from convinced that it's the right approach.  Is it possible to identify and copy broken links in Python?  In particular:

 * In `sage_findall()`, can we refine or avoid using the exception handler?  Perhaps it's better to use [os.walk()](http://markmail.org/message/dcv4g5b2b4exw64u), but the `os.path.is*()` family actually follows symlinks.
 * Is there a Pythonic analogue of `cp --preserve=links --no-dereference`?

Possible alternatives:

 * Make a symlink in some `spkg-install`.
 * Have Mercurial reconstitute the link.


---

Comment by rlm created at 2009-07-21 14:45:09

We really need to create a new ticket for this issue and continue there. I would also suggest taking this up on sage-devel.


---

Comment by mpatel created at 2009-07-24 15:17:51

Replying to [comment:23 rlm]:
> We really need to create a new ticket for this issue and continue there. I would also suggest taking this up on sage-devel.
I've opened #6614.
