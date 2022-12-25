# Issue 4500: cython files missing from build directory after install

archive/issues_004500.json:
```json
{
    "body": "Assignee: mabshoff\n\nImmediately after building sage from source, the cython files from the sage library aren't in `$SAGE_ROOT/devel/sage/build/sage` where they belong. One can see them get copied when doing a `sage -b` or `sage -clone`, but why aren't they there in the first place?\n\nEven stranger -- they get copied over during the build, as one can see in `install.log` ... where do they get deleted?\n\nIssue created by migration from https://trac.sagemath.org/ticket/4500\n\n",
    "created_at": "2008-11-12T11:10:47Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "cython files missing from build directory after install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4500",
    "user": "https://github.com/craigcitro"
}
```
Assignee: mabshoff

Immediately after building sage from source, the cython files from the sage library aren't in `$SAGE_ROOT/devel/sage/build/sage` where they belong. One can see them get copied when doing a `sage -b` or `sage -clone`, but why aren't they there in the first place?

Even stranger -- they get copied over during the build, as one can see in `install.log` ... where do they get deleted?

Issue created by migration from https://trac.sagemath.org/ticket/4500





---

archive/issue_comments_033246.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-11-12T15:03:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33246",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_033247.json:
```json
{
    "body": "If there ever was a blocker for 3.2 this would be one :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-12T15:03:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33247",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

If there ever was a blocker for 3.2 this would be one :)

Cheers,

Michael



---

archive/issue_comments_033248.json:
```json
{
    "body": "Unbelievable! But true (I checked older Sage versions, too). I read the ticket while building Sage 3.2.rc0 and had a look. While in the shell where I issued the build it was printing:\n\n```\ng++ -o libcsage.dylib -single_module -flat_namespace -undefined dynamic_lookup -dynamiclib src/convert.os src/interrupt.os src/mpn_pylong.os src/mpz_pylong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/Users/georgweber/Public/sage/sage-3.2.rc0/local/lib -lntl -lgmp -lpari\n*** TOUCHING ALL CYTHON (.pyx) FILES ***\nscons: `install' is up to date.\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nsage/structure/sage_object.pyx --> /Users/georgweber/Public/sage/sage-3.2.rc0/local//lib/python/site-packages//sage/structure/sage_object.pyx\nsage/structure/category_object.pyx --> /Users/georgweber/Public/sage/sage-3.2.rc0/local//lib/python/site-packages//sage/structure/category_object.pyx\n```\n\none should assume that then in the following the .pyx files were copied over.\n\nBut this was not the case!\n\nIn fact, the directory /Users/georgweber/Public/sage/sage-3.2.rc0/devel/sage/build/sage/ was empty (!!!) at that time, and thus the (linked) directory /Users/georgweber/Public/sage/sage-3.2.rc0/local//lib/python/site-packages/sage/ was empty too, i.e. had no subdirectory structure. I wasn't fast enough to create by hand some of the missung directories and see whether then, the .pyx files would be copied over there as the log output shows resp. wants to make us believe, but that might be worth another try.\n\nI do now think the .pyx were not deleted, but were never successfully copied over.",
    "created_at": "2008-11-12T20:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33248",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

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

archive/issue_comments_033249.json:
```json
{
    "body": "First patch doesn't work of course (I forgot one subdirectory level)",
    "created_at": "2008-11-12T22:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33249",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

First patch doesn't work of course (I forgot one subdirectory level)



---

archive/issue_comments_033250.json:
```json
{
    "body": "Attachment [4500_sage-build.patch](tarball://root/attachments/some-uuid/ticket4500/4500_sage-build.patch) by GeorgSWeber created at 2008-11-12 22:55:13\n\nnow tested",
    "created_at": "2008-11-12T22:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33250",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [4500_sage-build.patch](tarball://root/attachments/some-uuid/ticket4500/4500_sage-build.patch) by GeorgSWeber created at 2008-11-12 22:55:13

now tested



---

archive/issue_comments_033251.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-12T22:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33251",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing status from new to assigned.



---

archive/issue_comments_033252.json:
```json
{
    "body": "Changing assignee from mabshoff to GeorgSWeber.",
    "created_at": "2008-11-12T22:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33252",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing assignee from mabshoff to GeorgSWeber.



---

archive/issue_comments_033253.json:
```json
{
    "body": "Ahh, I didn't forget a subdirectory level, but forgot to take into account that the directory \"build\" under \"devel/sage\" does not exist at that time.\n\nWorks fine at my install, please review.",
    "created_at": "2008-11-12T22:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33253",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Ahh, I didn't forget a subdirectory level, but forgot to take into account that the directory "build" under "devel/sage" does not exist at that time.

Works fine at my install, please review.



---

archive/issue_comments_033254.json:
```json
{
    "body": "Zut alors, it seems I have to recheck this one ... still working",
    "created_at": "2008-11-12T23:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33254",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Zut alors, it seems I have to recheck this one ... still working



---

archive/issue_comments_033255.json:
```json
{
    "body": "Before the current patch:\n\n```\nTime to execute 216 commands: 2665.62391996 seconds\nFinished compiling Cython code (time = 2668.81615806 seconds)\n```\n\nafter the current patch:\n\n```\nTime to execute 95 commands: 967.580175877 seconds\nFinished compiling Cython code (time = 969.730924129 seconds)\n```\n\nAnd then things go awry because more than half of the needed Cython compiled files are missing ...",
    "created_at": "2008-11-12T23:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33255",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

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

archive/issue_comments_033256.json:
```json
{
    "body": "apply after the first one",
    "created_at": "2008-11-12T23:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33256",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

apply after the first one



---

archive/issue_comments_033257.json:
```json
{
    "body": "Attachment [4500_sage-build-patch2.patch](tarball://root/attachments/some-uuid/ticket4500/4500_sage-build-patch2.patch) by GeorgSWeber created at 2008-11-13 00:34:20\n\nYeah, the patch2 for the patch is coyote ugly, but does the job.\n\nAnd probably we don't need anymore to \"touch all Cython files\" in the next lines after the added ones, but for the time being I let that stand as it is.\n\nThis ticket (both patches are needed) is for review now (again).",
    "created_at": "2008-11-13T00:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33257",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [4500_sage-build-patch2.patch](tarball://root/attachments/some-uuid/ticket4500/4500_sage-build-patch2.patch) by GeorgSWeber created at 2008-11-13 00:34:20

Yeah, the patch2 for the patch is coyote ugly, but does the job.

And probably we don't need anymore to "touch all Cython files" in the next lines after the added ones, but for the time being I let that stand as it is.

This ticket (both patches are needed) is for review now (again).



---

archive/issue_comments_033258.json:
```json
{
    "body": "Changing assignee from GeorgSWeber to @craigcitro.",
    "created_at": "2008-11-13T13:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33258",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing assignee from GeorgSWeber to @craigcitro.



---

archive/issue_comments_033259.json:
```json
{
    "body": "Attachment [trac-4500.patch](tarball://root/attachments/some-uuid/ticket4500/trac-4500.patch) by GeorgSWeber created at 2008-11-13 13:35:28\n\nCraigs approach is way more elegant than mine. I hope his patch passes the necessary (and timeconsuming) tests. I never imagined I could ever write code this ugly as I did, and would be happy if it wasn't necessary to include it into Sage ;-)\n\nCheers, gsw",
    "created_at": "2008-11-13T13:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33259",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [trac-4500.patch](tarball://root/attachments/some-uuid/ticket4500/trac-4500.patch) by GeorgSWeber created at 2008-11-13 13:35:28

Craigs approach is way more elegant than mine. I hope his patch passes the necessary (and timeconsuming) tests. I never imagined I could ever write code this ugly as I did, and would be happy if it wasn't necessary to include it into Sage ;-)

Cheers, gsw



---

archive/issue_comments_033260.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-11-13T13:35:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33260",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing status from assigned to new.



---

archive/issue_comments_033261.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-13T13:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33261",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_033262.json:
```json
{
    "body": "Well, you pointing out what going on made my job much easier! :) \n\nSo does that translate to \"positive review\"?",
    "created_at": "2008-11-13T13:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33262",
    "user": "https://github.com/craigcitro"
}
```

Well, you pointing out what going on made my job much easier! :) 

So does that translate to "positive review"?



---

archive/issue_comments_033263.json:
```json
{
    "body": "This will lead to a positive review in the end, I'm sure.\n\nBut from past experience, I would like to see with my own eyes the patch passing the necessary tests before I give the \"go!\". It will take at least several hours, maybe a day, before I can do the testing, because right now I don't have access to a Sage installation.\n\nMaybe someone else is quicker.\n\nCheers, gsw",
    "created_at": "2008-11-13T16:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33263",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

This will lead to a positive review in the end, I'm sure.

But from past experience, I would like to see with my own eyes the patch passing the necessary tests before I give the "go!". It will take at least several hours, maybe a day, before I can do the testing, because right now I don't have access to a Sage installation.

Maybe someone else is quicker.

Cheers, gsw



---

archive/issue_comments_033264.json:
```json
{
    "body": "Replying to [comment:10 GeorgSWeber]:\n> This will lead to a positive review in the end, I'm sure.\n> \n> But from past experience, I would like to see with my own eyes the patch passing the necessary tests before I give the \"go!\". It will take at least several hours, maybe a day, before I can do the testing, because right now I don't have access to a Sage installation.\n\nYeah, any patch to the build system gets additional scrutiny since screw ups here affect a lot of people. \n\n> Maybe someone else is quicker.\n\nI will do a full cycle, i.e. force a complete rebuild after devel/sage-main with the patch applied to the spkg to see what happens, i.e. if a \"sage -b\" forces a rebuild on all files.\n\nEither way: thanks to both of you of putting this issue down.\n\n> Cheers, gsw\n\nCheers,\n\nMichael",
    "created_at": "2008-11-13T16:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33264",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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

archive/issue_comments_033265.json:
```json
{
    "body": "Hmm, this blows up (also with the patch from #4480 applied) when doing a virgin build:\n\n```\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nTraceback (most recent call last):\n  File \"setup.py\", line 435, in <module>\n    queue = compile_command_list(ext_modules, deps)\n  File \"setup.py\", line 400, in compile_command_list\n    dest_time = deps.timestamp(dest_file)\n  File \"setup.py\", line 244, in timestamp\n    self._timestamps[filename] = os.path.getmtime(filename)\n  File \"/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/posixpath.py\", line 143, in getmtime\n    return os.stat(filename).st_mtime\nOSError: [Errno 2] No such file or directory: '/scratch/mabshoff/release-cycle/sage-3.1.3.final/local//lib/python/site-packages//sage/structure/sage_object.pyx'\nsage: There was an error installing modified sage library code.\n```\n\nDon't let the path names fool you - this is a 3.2.rc0 build.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-13T16:46:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33265",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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

archive/issue_comments_033266.json:
```json
{
    "body": "This patch fixes the issue for me:\n\n```\ndiff -r c543000d6447 setup.py\n--- a/setup.py\tThu Nov 13 05:32:07 2008 -0800\n+++ b/setup.py\tThu Nov 13 09:43:33 2008 -0800\n@@ -241,7 +241,10 @@\n         Look up the last modified time of a file, with caching. \n         \"\"\"\n         if filename not in self._timestamps:\n-            self._timestamps[filename] = os.path.getmtime(filename)\n+            try:\n+                 self._timestamps[filename] = os.path.getmtime(filename)\n+            except:\n+                 self._timestamps[filename] = 0\n         return self._timestamps[filename]\n \n     def parse_deps(self, filename, verify=True):\n```\n\nI would guess this is more a #4480 issue, but since I started on this ticket and I want to merge both of them I will mention it here.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-13T17:50:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33266",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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

archive/issue_comments_033267.json:
```json
{
    "body": "I give a positive review to mabshoff's suggested fix ... now we just need someone to review this patch. :)",
    "created_at": "2008-11-13T22:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33267",
    "user": "https://github.com/craigcitro"
}
```

I give a positive review to mabshoff's suggested fix ... now we just need someone to review this patch. :)



---

archive/issue_comments_033268.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-14T04:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33268",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004746.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-14T04:02:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4500#event-4746"
}
```



---

archive/issue_comments_033269.json:
```json
{
    "body": "Merged trac-4500.patch in Sage 3.2.rc1",
    "created_at": "2008-11-14T04:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4500#issuecomment-33269",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac-4500.patch in Sage 3.2.rc1
