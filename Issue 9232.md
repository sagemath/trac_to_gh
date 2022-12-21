# Issue 9232: jmol on commandline broken

Issue created by migration from Trac.

Original creator: vbraun

Original creation time: 2010-06-13 20:57:16

Assignee: jason, was

CC:  kcrisman jason jdemeyer

I can't see Graphics3d objects on the command line. For example, 

```
sage: sphere()
sage: 
```

The command returns without starting jmol or producing any other graphical output.

Strangely enough, I can start jmol from the sage command line:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: !jmol
splash_image=jar:file:/home/vbraun/opt/sage-hg/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/data/jmol/Jmol.jar!/org/openscience/jmol/images/Jmol_splash.jpg
history file is /home/vbraun/.jmol/history
using Smarter Model Adapter
(C) 2008 Jmol Development
Jmol Version 11.6.16  2008-11-24 13:39
java.vendor:Sun Microsystems Inc.
java.version:1.6.0_18
os.name:Linux
memory:9.8/21.1
useCommandThread: false
User macros dir: /home/vbraun/.jmol/macros
       exists: false
  isDirectory: false
```

| Sage Version 4.4.3, Release Date: 2010-06-04                       |
| Type notebook() for the GUI, and license() for information.        |
The following also works and shows a tachyon-generated plot:

```
sphere(viewer='tachyon')
```


More verbosity:

```
sage: sphere(verbosity=99)
Traceback (most recent call last):
  File "/home/vbraun/Sage/sage/local/bin/sage-pypkg-location", line 3, in <module>
    from pkg_resources import Requirement, working_set
zipimport.ZipImportError: can't decompress data; zlib not available
Jmol.jar not found
```


For the record, I'm running Fedora 13 x86_64


---

Comment by gutow created at 2010-07-14 22:15:48

Does it work if you install the new version of Jmol?  See trac # 9238.  I think this broke when the notebook was put inside an egg.  I took that into account with the new version of Jmol.


---

Comment by vbraun created at 2010-07-14 23:25:56

I installed http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.spkg (#9238) but it did not change anything. The verbose output above indicates that Jmol.jar is never opened, so it is not particularly surprising that an updated Jmol spkg has no effect.


---

Comment by gutow created at 2010-07-15 00:08:06

It was worth a try as that still could have been a hidden Jmol.jar file not found error.  This is different than the problem I addressed.  Sorry.  I would guess it is a problem with the "sphere" command.  Does it work with a simple plot3d command?  I've tested the 1.1 version on MacOS and Ubuntu and it seems to work for me.
Replying to [comment:2 vbraun]:
> I installed http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.spkg (#9238) but it did not change anything. The verbose output above indicates that Jmol.jar is never opened, so it is not particularly surprising that an updated Jmol spkg has no effect.


---

Comment by vbraun created at 2010-07-15 00:54:44

I only used the `sphere()` command because it is the fastest way to generate 3d graphics. Other 3d plotting commands fail in the same way:

```
sage: plot3d(lambda x, y: x^2 + y^2, (-2,2), (-2,2))  # note: no output
sage: plot3d(lambda x, y: x^2 + y^2, (-2,2), (-2,2), verbosity=99)
Traceback (most recent call last):
  File "/home/vbraun/Sage/sage/local/bin/sage-pypkg-location", line 3, in <module>
    from pkg_resources import Requirement, working_set
zipimport.ZipImportError: can't decompress data; zlib not available
Jmol.jar not found
```



---

Comment by gutow created at 2010-07-15 03:57:38

Try installing the Jmol for notebook again.  It looks like the file on my server got corrupted and was missing the Jmol.jar application file as well as some others..Not sure what happened but we've had some power outages and the server may have been rebuilt from backups.  I've uploaded a new copy.

Because the name hasn't changed you will probably have to do some surgery to get it to download and do an install.  You will need to delete any copies of the .spkg (or its uncompressed directory) that you find in any of these subdirectories of your sage install before trying an install.  If you don't get a message about downloading the file you missed something:
spkg/build
spkg/installed
spkg/optional

Let us know if this fixes it.  Sorry for the inconvenience.
Jonathan
Replying to [comment:4 vbraun]:
> I only used the `sphere()` command because it is the fastest way to generate 3d graphics. Other 3d plotting commands fail in the same way:
> {{{
> sage: plot3d(lambda x, y: x^2 + y^2, (-2,2), (-2,2))  # note: no output
> sage: plot3d(lambda x, y: x^2 + y^2, (-2,2), (-2,2), verbosity=99)
> Traceback (most recent call last):
>   File "/home/vbraun/Sage/sage/local/bin/sage-pypkg-location", line 3, in <module>
>     from pkg_resources import Requirement, working_set
> zipimport.ZipImportError: can't decompress data; zlib not available
> Jmol.jar not found
> }}}


---

Comment by vbraun created at 2010-07-15 04:59:25

I did a

```
[vbraun`@`localhost sage]$ rm ./spkg/optional/Jmol_for_SageNoteBook-1.1.spkg
[vbraun`@`localhost sage]$ ./sage -f http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.spkg
```

and it re-downloaded the Jmol spkg. Still fails with the same error message.


---

Comment by gutow created at 2010-07-15 12:42:34

There is something special about your system...I've just retested that things work for Sage 4.4.3 on MacOS and Ubuntu Linux.  Let's see if everything actually got installed:
Can you please post the directory listing (ls -l please) for the following two directories:
<sage directory>/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/data/jmol
and
<sage directory>/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/data/jmol/appletweb

If everything is there, I'm mystified.  If everything is not, then something is wrong with the install for your system and the .spkg needs to be fixed.

Jonathan
Replying to [comment:6 vbraun]:
> I did a
> {{{
> [vbraun`@`localhost sage]$ rm ./spkg/optional/Jmol_for_SageNoteBook-1.1.spkg
> [vbraun`@`localhost sage]$ ./sage -f http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.spkg
> }}}
> and it re-downloaded the Jmol spkg. Still fails with the same error message.
>


---

Comment by vbraun created at 2010-07-15 14:54:07

I saved the `sys.path` within `sage-pypkg-location`, and it reads:

```
/home/vbraun/opt/sage-4.5.alpha1/local/bin
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/setuptools-0.6c9-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/Twisted-9.0.0-py2.6-linux-x86_64.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/ZODB3-3.7.0-py2.6-linux-x86_64.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zdaemon-2.0.0-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/ZConfig-2.5-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.testing-3.5.0-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.proxy-3.4.0-py2.6-linux-x86_64.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/Pygments-0.11.1-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/Jinja-1.2-py2.6-linux-x86_64.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/Jinja2-2.1.1-py2.6-linux-x86_64.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/Sphinx-0.6.3-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/SQLAlchemy-0.5.8-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/pytz-2010h-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.i18nmessageid-3.5.2-py2.6-linux-x86_64.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.event-3.5.0_1-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/ClientForm-0.2.10-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/mechanize-0.1.11-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.interface-3.6.1-py2.6-linux-x86_64.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.schema-3.6.3-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/zope.testbrowser-3.8.1-py2.6.egg
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg
/home/vbraun/opt/sage-4.5.alpha1
/home/vbraun/Sage/sage/local/lib/python
/home/vbraun/Sage/sage/local/lib64/python26.zip
/home/vbraun/Sage/sage/local/lib64/python2.6
/home/vbraun/Sage/sage/local/lib64/python2.6/plat-linux2
/home/vbraun/Sage/sage/local/lib64/python2.6/lib-tk
/home/vbraun/Sage/sage/local/lib64/python2.6/lib-old
/home/vbraun/Sage/sage/local/lib64/python2.6/lib-dynload
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages
/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/PIL
```

But sage install zlib in

```
[vbraun`@`volker-two sage-4.5.alpha1]$ find | grep zlib.so
./local/lib/python2.6/lib-dynload/zlib.so
```

Note: `/lib/`, not `/lib64/`. This explains why zlib cannot be imported. For the record, all libraries are 64-bit on my system.

From within Sage, on the other hand, `sys.path` is set appropriately:

```
sage: '/home/vbraun/Sage/sage/local/lib/python2.6/lib-dynload' in sys.path
True
```



---

Comment by vbraun created at 2010-08-05 16:39:44

For the record, creating a symlink $SAGE_ROOT/local/lib64 pointing to $SAGE_ROOT/local/lib works. Another workaround is adding LIBRARY_PATH to DYLD_LIBRARY_PATH in sage-native-execute (from logix/#sage-devel).

I still don't understand the underlying cause, where does python get the incorrect path from?


---

Comment by leif created at 2010-12-13 15:59:37

#10286 is a follow-up which hopefully fixes this, such that this ticket can be closed as a duplicate when #10286 got merged.


---

Comment by gutow created at 2011-03-21 13:49:54

Changing assignee from jason, was to gutow.


---

Comment by gutow created at 2011-03-21 13:50:09

Changing status from new to needs_work.


---

Attachment

plot3d/base.pyx fixes to launch Jmol from cmd line


---

Comment by gutow created at 2011-03-22 14:50:06

Notebook fixes for launch Jmol from cmd line


---

Attachment

The above patches combined with installation of a newer version of Jmol fix this problem for Sage 4.6.2.  To install the new Jmol

```
./sage -f "http://www.uwosh.edu/faculty_staff/gutow/Jmol_for_SageNoteBook-1.1.5.spkg"
```


Note that my linux and MacOS versions of sage seemed to have slightly different mercurial tracking.  On MacOS you get a warning about the SageMenu.mnu file, when you apply the notebook_fixes patch.  That is OK, the other untracked files are properly added.


---

Comment by gutow created at 2011-03-22 15:09:44

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2011-03-22 16:10:52

This will have to be part of a new SageNB package before it can be merged.  See also #9238.


---

Comment by gutow created at 2011-03-22 16:43:06

Replying to [comment:14 kcrisman]:
> This will have to be part of a new SageNB package before it can be merged.  See also #9238.

OK, so what does that involve? Does this mean make a complete .spkg of the sageNB?  Then where do things have to go?  Also don't we need positive reviews first?


---

Comment by kcrisman created at 2011-03-22 16:46:01

Replying to [comment:15 gutow]:
> Replying to [comment:14 kcrisman]:
> > This will have to be part of a new SageNB package before it can be merged.  See also #9238.
> 
> OK, so what does that involve? Does this mean make a complete .spkg of the sageNB?  Then where do things have to go?  Also don't we need positive reviews first?
Yes, eventually!  This is just for informational purposes to someone coming to the ticket.


---

Comment by kcrisman created at 2011-03-23 15:35:22

Getting bad news:

```
tar: This does not look like a tar archive
tar: Skipping to next header
tar: Archive contains obsolescent base-64 headers
```



---

Comment by kcrisman created at 2011-03-23 15:47:55

Did you use `./sage -pkg` to create this?  When I did, I got 

```
Creating Sage package Jmol_for_SageNoteBook-1.1.5

Created package Jmol_for_SageNoteBook-1.1.5.spkg.

    NAME: Jmol_for_SageNoteBook
 VERSION: 1.1.5
    SIZE: 11.1M
 HG REPO: Error reading repository
SPKG.txt: Good

Please test this package using
```


which is actually ok since I don't think you have an HG repo and this is a temporary package for testing.  Then success:

```
Temporary package directory: /Users/student/Desktop/sage-4.6.2/spkg/build/Jmol_for_SageNoteBook-1.1.5
replacing Jmol.js...
Jmol.js replaced.
removing Jmol*.jar and license files.
rm: /Users/student/Desktop/sage-4.6.2/devel/sagenb/sagenb/data/jmol/LICENSE.txt: No such file or directory
installing Jmol.jar and license files…
New Jmol*.jar and license files installed.

real    0m1.051s
user    0m0.034s
sys     0m0.320s
Successfully installed Jmol_for_SageNoteBook-1.1.5
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing Jmol_for_SageNoteBook-1.1.5.spkg
```


Then applying the files is ok until

```
applying /Users/student/.sage/temp/Dasher_03.local/468/tmp_4.patch
file sagenb/data/jmol/appletweb/SageMenu.mnu already exists
1 out of 1 hunks FAILED -- saving rejects to file sagenb/data/jmol/appletweb/SageMenu.mnu.rej
```

Problematic is that then it's rejected?  I guess I'll see what happens... but this error will probably need to be fixed.


---

Comment by kcrisman created at 2011-03-23 16:19:30

Still zapped, probably because of the problem with the menu?

But then I tried it again, and it worked!  I don't get that.  

I'll try the notebook next.  Okay, works, but I do not see the new stuff for the applet.  I guess that's okay, since that's the other ticket, right?

Is there any way I can tell if the correct menu item is in there?  (Such as something to look for in the menu for the applet?)


---

Comment by gutow created at 2011-03-23 17:12:37

1. The correct menu is much shorter in the notebook than in the application launched from the command line.  The application launched from the command line uses the default menu.  I'll look into making them match.
 1. Apply the patches in #9238 to see the updated notebook Jmol interface.
 1. The .spkg problem is odd.  I've got no errors ever.  I just use ./sage -f "<web address of patch>".
 1. The patch with the problem with the .mnu file means redoing it against a 4.6.2 that had the .mnu file in the repo.  For some reason the version I got for ubuntu 10.04 lts did not.


---

Comment by kcrisman created at 2011-03-23 19:50:21

>  1. The correct menu is much shorter in the notebook than in the application launched from the command line.  The application launched from the command line uses the default menu.  I'll look into making them match.
Well, no need on this ticket!

As for this, the *first patch only* suffices to fix the command line problem, and the notebook still works right.  

So I would say that the second patch is _not_ relevant to this ticket, esp. given its problems with import (which I am looking into - I think has to do with HG not applying some things correctly because of perceived line endings.  Look at the view of the attachment on this ticket, and look at the lines with `bond100` and `bond150` and note the weirdness there.  It looks like 

```
bond100 | 0.10 √Ö = wireframe .1
```

instead of angstroms like I think it's supposed to

```
bond100 | 0.10 Å = wireframe .1
```

No wonder it's not applying, since it's not being interpreted right.  Anyway, not relevant for the ticket.

>  1. Apply the patches in #9238 to see the updated notebook Jmol interface.
As I thought - thanks, not relevant for reviewing this.

>  1. The .spkg problem is odd.  I've got no errors ever.  I just use ./sage -f "<web address of patch>".
Yes, that is what should work.  Since this isn't an spkg that would actually ever exist, it's not a problem, I hope.

>  1. The patch with the problem with the .mnu file means redoing it against a 4.6.2 that had the .mnu file in the repo.  For some reason the version I got for ubuntu 10.04 lts did not.
See above.

I get the following issue as well.

```
rm: /Users/.../sage-4.7.alpha2-jmol/devel/sagenb/sagenb/data/jmol/LICENSE.txt: No such file or directory
```

So was there not a license before?  Apparently not - I can confirm that in an install that does not have the new Jmol.  So it's not a big deal, but at any rate you didn't have to put that in the script.

Otherwise I think this is ready to go.  It would be nice to have someone on a system where command line plotting did _not_ work before to try this.  Volker, du bist ja bei Sage Days 29, oder?  Probierst du es mal aus?


---

Comment by kcrisman created at 2011-03-23 19:52:52

Oh, and of course this can't actually be _merged_ until a new SageNB package is produced.  I think I might be willing to do that once this and #9238 and one or two other things are ready; it would sure be worth it!


---

Comment by vbraun created at 2011-03-25 18:18:01

I applied the jmol spkg and `trac_9232_plot3d_base_pyx.patch` and jmol is still broken on the command line, Fedora 14 x86_64.  I need to add `trac_10286_call_jmol_correctly.patch` from #10286 on top of it. The issue is that `sage-native-execute` must not be used for sage components like jmol.


---

Comment by kcrisman created at 2011-03-25 18:25:25

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2011-03-25 18:25:25

Replying to [comment:23 vbraun]:
> I applied the jmol spkg and `trac_9232_plot3d_base_pyx.patch` and jmol is still broken on the command line, Fedora 14 x86_64.  I need to add `trac_10286_call_jmol_correctly.patch` from #10286 on top of it. The issue is that `sage-native-execute` must not be used for sage components like jmol.
Thanks for that feedback very much.  Ok, then I propose that that patch gets moved here, and then #10286 can be just about sage-native-execute.  Am I correct in assuming that _only_ that patch from #10286 is needed to fix the behavior?


---

Comment by vbraun created at 2011-03-25 18:38:50

Yes, it would be fine to move `trac_10286_call_jmol_correctly.patch` here. Only that one-liner is needed.


---

Attachment

Apply this second.


---

Comment by kcrisman created at 2011-03-25 18:45:54

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2011-03-25 18:45:54

Okay, this _should_ be all okay then.


---

Comment by kcrisman created at 2011-03-29 00:29:21

Things are a little bit of a mess because of the potential for flask changeover in SageNB.  What do people think of this?
 1. This ticket is used just for adding Volker's patch.  No sagenb change needed.
 1. Jonathan's patches for the menu, help, and surface lighting/spt files are moved to #9238.
 1. #9238 and all its attendant pieces become part of the flask notebook changeover, and henceforth the property of those doing that :)
Otherwise this has the potential to just bitrot forever.


---

Comment by jason created at 2011-03-29 01:01:41

The flask notebook has already split off of the current notebook.  So any patches that are applied to the current sage notebook will also need to be applied to the new notebook, probably in parallel.

I'm already working on moving #9238 over to the new notebook.  It's just a matter of applying the patch to the new notebook, as far as I can tell.  (We'll find out better once we actually get jmol working with the new notebook!)


---

Comment by gutow created at 2011-03-29 02:27:46

Should I continue to put my patches into #9238? I've still got some fixes that should reduce memory problems making Safari somewhat more reliable and I may be able to get the advanced controls working in IE.


---

Comment by kcrisman created at 2011-03-29 13:34:50

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-03-29 13:34:50

Jonathan, definitely keep working on #9238.  Jason can just put those things in the new notebook.  Having something working completely is a very good idea, and we can continue to test it on the old notebook, which is still the current notebook, after all.

I do think we need to also add the piece of #9238 that changes the lighting.  Currently I have good lighting in the command line and bad lighting in the notebook, even without the new jmol - someone the new jmol is called from the notebook, even though I didn't install it in this version!!!  I even checked this in the advanced menu.  Mystifying. 

I'm just testing quick, and then I'll post patches.  Since they aren't mine, I feel free to give positive review.


---

Attachment


---

Comment by kcrisman created at 2011-03-29 13:37:40

Apply [attachment:trac_9232_call_jmol_correctly.patch] and [attachment:trac_9232-lighting.patch].


---

Comment by kcrisman created at 2011-04-06 12:15:04

Just a ping to let the release manager know this is ready for alpha4.

:-)


---

Comment by jdemeyer created at 2011-04-07 08:51:31

Please confirm that the `sagenb` does _not_ need to be applied.


---

Comment by jdemeyer created at 2011-04-07 09:00:45

I meant to say more precisely: please confirm that the patch [attachment:trac_9232_notebook_fixes.patch] may be ignored.


---

Comment by gutow created at 2011-04-07 12:55:39

That is correct.  Only the two patches listed at the end of the description are necessary.  The other two have been incorporated into ticket #9238 because they are enhancements to how Jmol works.


---

Comment by jdemeyer created at 2011-04-07 13:48:29

Resolution: fixed
