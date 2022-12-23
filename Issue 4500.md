# Issue 4500: cython files missing from build directory after install

Issue created by migration from https://trac.sagemath.org/ticket/4500

Original creator: craigcitro

Original creation time: 2008-11-12 11:10:47

Assignee: mabshoff

Immediately after building sage from source, the cython files from the sage library aren't in `$SAGE_ROOT/devel/sage/build/sage` where they belong. One can see them get copied when doing a `sage -b` or `sage -clone`, but why aren't they there in the first place?

Even stranger -- they get copied over during the build, as one can see in `install.log` ... where do they get deleted?


---

Comment by mabshoff created at 2008-11-12 15:03:04

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-11-12 15:03:04

If there ever was a blocker for 3.2 this would be one :)

Cheers,

Michael


---

Comment by GeorgSWeber created at 2008-11-12 20:59:34

Unbelievable! But true (I checked older Sage versions, too). I read the ticket while building Sage 3.2.rc0 and had a look. While in the shell where I issued the build it was printing:

```
g++ -o libcsage.dylib -single_module -flat_namespace -undefined dynamic_lookup -dynamiclib src/convert.os src/interrupt.os src/mpn_pylong.os src/mpz_pylong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/Users/georgweber/Public/sage/sage-3.2.rc0/local/lib -lntl -lgmp -lpari
*** TOUCHING ALL CYTHON (.pyx) FILES ***
scons: `install' is up to date.

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
sage/structure/sage_object.pyx --> /Users/georgweber/Public/sage/sage-3.2.rc0/local//lib/python/site-packages//sage/structure/sage_object.pyx
sage/structure/category_object.pyx --> /Users/georgweber/Public/sage/sage-3.2.rc0/local//lib/python/site-packages//sage/structure/category_object.pyx
```

one should assume that then in the following the .pyx files were copied over.

But this was not the case!

In fact, the directory /Users/georgweber/Public/sage/sage-3.2.rc0/devel/sage/build/sage/ was empty (!!!) at that time, and thus the (linked) directory /Users/georgweber/Public/sage/sage-3.2.rc0/local//lib/python/site-packages/sage/ was empty too, i.e. had no subdirectory structure. I wasn't fast enough to create by hand some of the missung directories and see whether then, the .pyx files would be copied over there as the log output shows resp. wants to make us believe, but that might be worth another try.

I do now think the .pyx were not deleted, but were never successfully copied over.


---

Comment by GeorgSWeber created at 2008-11-12 22:26:53

First patch doesn't work of course (I forgot one subdirectory level)


---

Attachment

now tested


---

Comment by GeorgSWeber created at 2008-11-12 22:59:59

Changing status from new to assigned.


---

Comment by GeorgSWeber created at 2008-11-12 22:59:59

Changing assignee from mabshoff to GeorgSWeber.


---

Comment by GeorgSWeber created at 2008-11-12 22:59:59

Ahh, I didn't forget a subdirectory level, but forgot to take into account that the directory "build" under "devel/sage" does not exist at that time.

Works fine at my install, please review.


---

Comment by GeorgSWeber created at 2008-11-12 23:11:48

Zut alors, it seems I have to recheck this one ... still working


---

Comment by GeorgSWeber created at 2008-11-12 23:17:52

Before the current patch:

```
Time to execute 216 commands: 2665.62391996 seconds
Finished compiling Cython code (time = 2668.81615806 seconds)
```

after the current patch:

```
Time to execute 95 commands: 967.580175877 seconds
Finished compiling Cython code (time = 969.730924129 seconds)
```

And then things go awry because more than half of the needed Cython compiled files are missing ...


---

Comment by GeorgSWeber created at 2008-11-12 23:39:02

apply after the first one


---

Attachment

Yeah, the patch2 for the patch is coyote ugly, but does the job.

And probably we don't need anymore to "touch all Cython files" in the next lines after the added ones, but for the time being I let that stand as it is.

This ticket (both patches are needed) is for review now (again).


---

Comment by GeorgSWeber created at 2008-11-13 13:35:28

Changing assignee from GeorgSWeber to craigcitro.


---

Attachment

Craigs approach is way more elegant than mine. I hope his patch passes the necessary (and timeconsuming) tests. I never imagined I could ever write code this ugly as I did, and would be happy if it wasn't necessary to include it into Sage ;-)

Cheers, gsw


---

Comment by GeorgSWeber created at 2008-11-13 13:35:28

Changing status from assigned to new.


---

Comment by craigcitro created at 2008-11-13 13:43:36

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-11-13 13:43:36

Well, you pointing out what going on made my job much easier! :) 

So does that translate to "positive review"?


---

Comment by GeorgSWeber created at 2008-11-13 16:17:47

This will lead to a positive review in the end, I'm sure.

But from past experience, I would like to see with my own eyes the patch passing the necessary tests before I give the "go!". It will take at least several hours, maybe a day, before I can do the testing, because right now I don't have access to a Sage installation.

Maybe someone else is quicker.

Cheers, gsw


---

Comment by mabshoff created at 2008-11-13 16:26:46

Replying to [comment:10 GeorgSWeber]:
> This will lead to a positive review in the end, I'm sure.
> 
> But from past experience, I would like to see with my own eyes the patch passing the necessary tests before I give the "go!". It will take at least several hours, maybe a day, before I can do the testing, because right now I don't have access to a Sage installation.

Yeah, any patch to the build system gets additional scrutiny since screw ups here affect a lot of people. 

> Maybe someone else is quicker.

I will do a full cycle, i.e. force a complete rebuild after devel/sage-main with the patch applied to the spkg to see what happens, i.e. if a "sage -b" forces a rebuild on all files.

Either way: thanks to both of you of putting this issue down.

> Cheers, gsw

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-13 16:46:13

Hmm, this blows up (also with the patch from #4480 applied) when doing a virgin build:

```
Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Traceback (most recent call last):
  File "setup.py", line 435, in <module>
    queue = compile_command_list(ext_modules, deps)
  File "setup.py", line 400, in compile_command_list
    dest_time = deps.timestamp(dest_file)
  File "setup.py", line 244, in timestamp
    self._timestamps[filename] = os.path.getmtime(filename)
  File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/posixpath.py", line 143, in getmtime
    return os.stat(filename).st_mtime
OSError: [Errno 2] No such file or directory: '/scratch/mabshoff/release-cycle/sage-3.1.3.final/local//lib/python/site-packages//sage/structure/sage_object.pyx'
sage: There was an error installing modified sage library code.
```

Don't let the path names fool you - this is a 3.2.rc0 build.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-13 17:50:59

This patch fixes the issue for me:

```
diff -r c543000d6447 setup.py
--- a/setup.py	Thu Nov 13 05:32:07 2008 -0800
+++ b/setup.py	Thu Nov 13 09:43:33 2008 -0800
@@ -241,7 +241,10 @@
         Look up the last modified time of a file, with caching. 
         """
         if filename not in self._timestamps:
-            self._timestamps[filename] = os.path.getmtime(filename)
+            try:
+                 self._timestamps[filename] = os.path.getmtime(filename)
+            except:
+                 self._timestamps[filename] = 0
         return self._timestamps[filename]
 
     def parse_deps(self, filename, verify=True):
```

I would guess this is more a #4480 issue, but since I started on this ticket and I want to merge both of them I will mention it here.

Cheers,

Michael


---

Comment by craigcitro created at 2008-11-13 22:38:12

I give a positive review to mabshoff's suggested fix ... now we just need someone to review this patch. :)


---

Comment by mabshoff created at 2008-11-14 04:02:24

Resolution: fixed


---

Comment by mabshoff created at 2008-11-14 04:02:24

Merged trac-4500.patch in Sage 3.2.rc1
