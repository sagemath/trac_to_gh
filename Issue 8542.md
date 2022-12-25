# Issue 8542: Pynac does not build a DLL on Cygwin

archive/issues_008542.json:
```json
{
    "body": "Assignee: tbd\n\nHowever, if I go into src/ginac/.libs and run\n\n\n```\ngcc -shared -L/home/mhansen/sage-4.3.3.alpha0/local//lib -L/home/mhansen/sage-4.3.3.alpha0/local/lib/python2.6/config -o libpynac.dll *.o -lstdc++ -lpython2.6\n```\n\n\na working DLL gets built.  The trick would be to figure out how to get autotools to do this for us.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8542\n\n",
    "created_at": "2010-03-15T05:27:50Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "Pynac does not build a DLL on Cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8542",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tbd

However, if I go into src/ginac/.libs and run


```
gcc -shared -L/home/mhansen/sage-4.3.3.alpha0/local//lib -L/home/mhansen/sage-4.3.3.alpha0/local/lib/python2.6/config -o libpynac.dll *.o -lstdc++ -lpython2.6
```


a working DLL gets built.  The trick would be to figure out how to get autotools to do this for us.

Issue created by migration from https://trac.sagemath.org/ticket/8542





---

archive/issue_comments_077097.json:
```json
{
    "body": "It basically comes down to adding the following changes\n\n\n```\ndiff -r 1cf1634d68b0 configure.ac\n--- a/configure.ac\tSun Mar 14 20:20:48 2010 -0800\n+++ b/configure.ac\tMon Mar 15 00:15:49 2010 -0800\n@@ -71,6 +71,7 @@\n AC_PROG_CXXCPP\n AC_PROG_INSTALL\n AM_PROG_LIBTOOL\n+AC_LIBTOOL_WIN32_DLL\n \n dnl Check for data types which are needed by the hash function \n dnl (golden_ratio_hash).\ndiff -r 1cf1634d68b0 ginac/Makefile.am\n--- a/ginac/Makefile.am\tSun Mar 14 20:20:48 2010 -0800\n+++ b/ginac/Makefile.am\tMon Mar 15 00:15:49 2010 -0800\n@@ -10,7 +10,7 @@\n   pseries.cpp print.cpp symbol.cpp symmetry.cpp tensor.cpp \\\n   utils.cpp wildcard.cpp \\\n   remember.h tostring.h utils.h compiler.h\n-libpynac_la_LDFLAGS = -version-info $(LT_VERSION_INFO) -release $(LT_RELEASE)\n+libpynac_la_LDFLAGS = -version-info $(LT_VERSION_INFO) -release $(LT_RELEASE) -no-undefined\n ginacincludedir = $(includedir)/pynac\n ginacinclude_HEADERS = ginac.h add.h archive.h assertion.h basic.h class_info.h \\\n   clifford.h color.h constant.h container.h ex.h expair.h expairseq.h \\\n```\n\n\nand fixing the fallout by making sure that Python gets linked in.",
    "created_at": "2010-03-15T08:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77097",
    "user": "https://github.com/mwhansen"
}
```

It basically comes down to adding the following changes


```
diff -r 1cf1634d68b0 configure.ac
--- a/configure.ac	Sun Mar 14 20:20:48 2010 -0800
+++ b/configure.ac	Mon Mar 15 00:15:49 2010 -0800
@@ -71,6 +71,7 @@
 AC_PROG_CXXCPP
 AC_PROG_INSTALL
 AM_PROG_LIBTOOL
+AC_LIBTOOL_WIN32_DLL
 
 dnl Check for data types which are needed by the hash function 
 dnl (golden_ratio_hash).
diff -r 1cf1634d68b0 ginac/Makefile.am
--- a/ginac/Makefile.am	Sun Mar 14 20:20:48 2010 -0800
+++ b/ginac/Makefile.am	Mon Mar 15 00:15:49 2010 -0800
@@ -10,7 +10,7 @@
   pseries.cpp print.cpp symbol.cpp symmetry.cpp tensor.cpp \
   utils.cpp wildcard.cpp \
   remember.h tostring.h utils.h compiler.h
-libpynac_la_LDFLAGS = -version-info $(LT_VERSION_INFO) -release $(LT_RELEASE)
+libpynac_la_LDFLAGS = -version-info $(LT_VERSION_INFO) -release $(LT_RELEASE) -no-undefined
 ginacincludedir = $(includedir)/pynac
 ginacinclude_HEADERS = ginac.h add.h archive.h assertion.h basic.h class_info.h \
   clifford.h color.h constant.h container.h ex.h expair.h expairseq.h \
```


and fixing the fallout by making sure that Python gets linked in.



---

archive/issue_comments_077098.json:
```json
{
    "body": "Shall I include the diff above in the next Pynac release?\n\nI could have done this for the version I just released (#8644) if I had known earlier...",
    "created_at": "2010-04-02T14:59:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77098",
    "user": "https://github.com/burcin"
}
```

Shall I include the diff above in the next Pynac release?

I could have done this for the version I just released (#8644) if I had known earlier...



---

archive/issue_comments_077099.json:
```json
{
    "body": "No, not quite yet.  Basically, we'll also have the stuff to autotools to detect where Python is, etc.",
    "created_at": "2010-04-02T19:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77099",
    "user": "https://github.com/mwhansen"
}
```

No, not quite yet.  Basically, we'll also have the stuff to autotools to detect where Python is, etc.



---

archive/issue_comments_077100.json:
```json
{
    "body": "Attachment [trac_8542-pynac_pointer_table.patch](tarball://root/attachments/some-uuid/ticket8542/trac_8542-pynac_pointer_table.patch) by @mwhansen created at 2010-05-03 13:33:27",
    "created_at": "2010-05-03T13:33:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77100",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_8542-pynac_pointer_table.patch](tarball://root/attachments/some-uuid/ticket8542/trac_8542-pynac_pointer_table.patch) by @mwhansen created at 2010-05-03 13:33:27



---

archive/issue_comments_077101.json:
```json
{
    "body": "I'll post the spkg shortly.",
    "created_at": "2010-05-03T13:33:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77101",
    "user": "https://github.com/mwhansen"
}
```

I'll post the spkg shortly.



---

archive/issue_events_020584.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-05-03T13:33:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "milestone": "sage-4.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8542#event-20584"
}
```



---

archive/issue_comments_077102.json:
```json
{
    "body": "There's an spkg at http://sage.math.washington.edu/home/mhansen/pynac-0.13.spkg, but it needs to have changes committed / SPKG.txt made / version number updated.",
    "created_at": "2010-05-04T23:32:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77102",
    "user": "https://github.com/mwhansen"
}
```

There's an spkg at http://sage.math.washington.edu/home/mhansen/pynac-0.13.spkg, but it needs to have changes committed / SPKG.txt made / version number updated.



---

archive/issue_comments_077103.json:
```json
{
    "body": "Replying to [comment:6 mhansen]:\n> There's an spkg at http://sage.math.washington.edu/home/mhansen/pynac-0.13.spkg, but it needs to have changes committed / SPKG.txt made / version number updated.\n\nI'll take a look at these and merge #8651 as well.",
    "created_at": "2010-05-05T02:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77103",
    "user": "https://github.com/burcin"
}
```

Replying to [comment:6 mhansen]:
> There's an spkg at http://sage.math.washington.edu/home/mhansen/pynac-0.13.spkg, but it needs to have changes committed / SPKG.txt made / version number updated.

I'll take a look at these and merge #8651 as well.



---

archive/issue_comments_077104.json:
```json
{
    "body": "Changing assignee from tbd to @burcin.",
    "created_at": "2010-05-05T15:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77104",
    "user": "https://github.com/burcin"
}
```

Changing assignee from tbd to @burcin.



---

archive/issue_comments_077105.json:
```json
{
    "body": "Changing keywords from \"\" to \"pynac\".",
    "created_at": "2010-05-05T15:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77105",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "" to "pynac".



---

archive/issue_comments_077106.json:
```json
{
    "body": "Both patches, for pynac and Sage, look good to me.\n\nBuilding the new pynac package fails with the following error:\n\n\n```\n...\n/usr/lib/gcc/x86_64-pc-linux-gnu/4.3.4/../../../../x86_64-pc-linux-gnu/bin/ld: /home/burcin/sage/sage-4.4.1.alpha2-patched/local/lib/python2.6/config/libpython2.6.a(abstract.o): relocation R_X86_64_32 against `a local symbol' can not be used when making a shared object; recompile with -fPIC\n/home/burcin/sage/sage-4.4.1.alpha2-patched/local/lib/python2.6/config/libpython2.6.a: could not read symbols: Bad value\ncollect2: ld returned 1 exit status\nmake[2]: *** [libpynac.la] Error 1\nmake[2]: Leaving directory `/home/burcin/sage/sage-4.4.1.alpha2-patched/spkg/build/pynac-0.1.13/src/ginac'\n...\n```\n\n\nDo we have a python package that uses `-fPIC`?",
    "created_at": "2010-05-05T15:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77106",
    "user": "https://github.com/burcin"
}
```

Both patches, for pynac and Sage, look good to me.

Building the new pynac package fails with the following error:


```
...
/usr/lib/gcc/x86_64-pc-linux-gnu/4.3.4/../../../../x86_64-pc-linux-gnu/bin/ld: /home/burcin/sage/sage-4.4.1.alpha2-patched/local/lib/python2.6/config/libpython2.6.a(abstract.o): relocation R_X86_64_32 against `a local symbol' can not be used when making a shared object; recompile with -fPIC
/home/burcin/sage/sage-4.4.1.alpha2-patched/local/lib/python2.6/config/libpython2.6.a: could not read symbols: Bad value
collect2: ld returned 1 exit status
make[2]: *** [libpynac.la] Error 1
make[2]: Leaving directory `/home/burcin/sage/sage-4.4.1.alpha2-patched/spkg/build/pynac-0.1.13/src/ginac'
...
```


Do we have a python package that uses `-fPIC`?



---

archive/issue_comments_077107.json:
```json
{
    "body": "Does this work for you http://sage.math.washington.edu/home/mhansen/python-2.6.4.p8.spkg ?",
    "created_at": "2010-05-05T16:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77107",
    "user": "https://github.com/mwhansen"
}
```

Does this work for you http://sage.math.washington.edu/home/mhansen/python-2.6.4.p8.spkg ?



---

archive/issue_comments_077108.json:
```json
{
    "body": "It works! I'll put your changes on the latest spkg included in sage (including the patch for #8753), merge some other fixes (#8651, maybe #8775), bump the version to 2.0 and make a new package.",
    "created_at": "2010-05-05T18:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77108",
    "user": "https://github.com/burcin"
}
```

It works! I'll put your changes on the latest spkg included in sage (including the patch for #8753), merge some other fixes (#8651, maybe #8775), bump the version to 2.0 and make a new package.



---

archive/issue_comments_077109.json:
```json
{
    "body": "I'll test the Python spkg on other systems.",
    "created_at": "2010-05-05T18:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77109",
    "user": "https://github.com/mwhansen"
}
```

I'll test the Python spkg on other systems.



---

archive/issue_comments_077110.json:
```json
{
    "body": "New pynac package containing Mike's function table and autoconf patches is available at #8903 or directly from:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg\n\nThe package also requires patches from #8651, #8775 and #8688.",
    "created_at": "2010-05-06T04:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77110",
    "user": "https://github.com/burcin"
}
```

New pynac package containing Mike's function table and autoconf patches is available at #8903 or directly from:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.2.0.spkg

The package also requires patches from #8651, #8775 and #8688.



---

archive/issue_comments_077111.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-06T04:14:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77111",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077112.json:
```json
{
    "body": "Great work Mike! Cygwin, here we come!",
    "created_at": "2010-05-06T04:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77112",
    "user": "https://github.com/burcin"
}
```

Great work Mike! Cygwin, here we come!



---

archive/issue_comments_077113.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-06T04:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77113",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_020585.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-05-28T19:31:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8542#event-20585"
}
```



---

archive/issue_comments_077114.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-28T19:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8542",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8542#issuecomment-77114",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
