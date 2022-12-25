# Issue 9832: fatal relocation error with Cliquer library on 64-bit Solaris and OpenSolaris

archive/issues_009832.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jhpalmieri @nathanncohen @jasongrout @jaapspies mvngu @qed777\n\nIf a 64-bit version of Sage is built on OpenSolaris, Sage reports an error as soon as it is started. \n\n\n```\ndrkirkby@hawk:~$ 64/sage-4.5.3.alpha2/sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\n| Sage Version 4.5.3.alpha2, Release Date: 2010-08-23                |\n| Type notebook() for the GUI, and license() for information.        |\n<snip>\n\nImportError: ld.so.1: python: fatal: relocation error: R_AMD64_PC32: file /export/home/drkirkby/64/sage-4.5.3.alpha2/local/lib//libcliquer.so: symbol main: value 0x28152e8c7d4 does not fit\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n```\n\n\nThe problem of fatal relocation errors is discussed on this [Sun blog](http://blogs.sun.com/rie/entry/my_relocations_don_t_fit) by Rod Evans. \n\nA shared library should show no output from the following command:\n\n\n```\n$ elfdump -d library | fgrep TEXTREL\n```\n\n\nBut in a 64-bit builds of Sage on both OpenSolaris x64 and Solaris 10 on SPARC, but show output. The following is from an OpenSolaris machine, but similar is seen on a 64-bit SPARC build of Sage. \n\n\n```\ndrkirkby@hawk:~$ elfdump -d 64/sage-4.5.3.alpha2/local/lib/libcliquer.so  | grep TEXTREL\n      [17]  TEXTREL           0                   \n      [25]  FLAGS             0x4                 [ TEXTREL ]\ndrkirkby@hawk:~$ \n```\n\n\nIf this flag is found, then the link-editor thinks this file contains non-pic code. \n\nLooking at the way the shared library is built on Solaris, it is different from other platforms. \n\n\n```\n# Flags for building a dynamically linked shared object.\nSAGESOFLAGS=\" \"\nif [ \"$UNAME\" = \"Linux\" ] || [ \"$UNAME\" = \"FreeBSD\" ]; then\n    SAGESOFLAGS=\"-shared -Wl,-soname,libcliquer.so\"\n    export SAGESOFLAGS\nelif [ \"$UNAME\" = \"Darwin\" ]; then\n    MACOSX_DEPLOYMENT_TARGET=\"10.3\"\n    export MACOSX_DEPLOYMENT_TARGET\n    SAGESOFLAGS=\"-dynamiclib -single_module -flat_namespace -undefined dynamic_l\nookup\"\n    export SAGESOFLAGS\nelif [ \"$UNAME\" = \"SunOS\" ]; then\n    SAGESOFLAGS=\"-G -Bdynamic\"\n    export SAGESOFLAGS\nelif [ \"$UNAME\" = \"CYGWIN\" ]; then\n    SAGESOFLAGS=\"-shared -Wl,-soname,libcliquer.so\"\n```\n\n\nUsing just\n\n\n```\nelif [ \"$UNAME\" = \"SunOS\" ]; then\n   SAGESOFLAGS=\"-shared\"\n```\n\n\nwas sufficient to produce a shared library which did not exhibit this problem. When Sage was started, Sage no longer produced the libcliquer error message, though it did fail to run properly. \n\nThere are in fact several other libraries in Sage that show show output using the `elfdump` command above. \n\n\n```\n * libcliquer.so\n * libecl.so\n * libgroebner-0.6.4.so\n * libpboriCudd-0.6.4.so\n * libpolybori-0.6.4.so \n```\n\n(These were observed on OpenSolaris x64. I've confirmed the same is true of libcliquer.so on 64-bit SPARC using `t2.math`, but I've not verified if all the other libraries show this problem. )\n\nI doubt whether these are the only issues preventing Sage running properly on 64-bit Solaris, but these should be resolved. \n\nSince \n* The current version of Cliquer in Sage 1.2 is not the latest.\n* Cliquer 1.2.1 is a bug-fix only release, so should be safe. \n* The Cliquer test suite can't be run as there's no `spkg-check` file - see #9767\n\nit makes sense to update Cliquer and sort out the Solaris and `spkg-check` issues at the same time. \n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/9833\n\n",
    "created_at": "2010-08-28T19:19:25Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "fatal relocation error with Cliquer library on 64-bit Solaris and OpenSolaris",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9832",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jhpalmieri @nathanncohen @jasongrout @jaapspies mvngu @qed777

If a 64-bit version of Sage is built on OpenSolaris, Sage reports an error as soon as it is started. 


```
drkirkby@hawk:~$ 64/sage-4.5.3.alpha2/sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
| Sage Version 4.5.3.alpha2, Release Date: 2010-08-23                |
| Type notebook() for the GUI, and license() for information.        |
<snip>

ImportError: ld.so.1: python: fatal: relocation error: R_AMD64_PC32: file /export/home/drkirkby/64/sage-4.5.3.alpha2/local/lib//libcliquer.so: symbol main: value 0x28152e8c7d4 does not fit
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```


The problem of fatal relocation errors is discussed on this [Sun blog](http://blogs.sun.com/rie/entry/my_relocations_don_t_fit) by Rod Evans. 

A shared library should show no output from the following command:


```
$ elfdump -d library | fgrep TEXTREL
```


But in a 64-bit builds of Sage on both OpenSolaris x64 and Solaris 10 on SPARC, but show output. The following is from an OpenSolaris machine, but similar is seen on a 64-bit SPARC build of Sage. 


```
drkirkby@hawk:~$ elfdump -d 64/sage-4.5.3.alpha2/local/lib/libcliquer.so  | grep TEXTREL
      [17]  TEXTREL           0                   
      [25]  FLAGS             0x4                 [ TEXTREL ]
drkirkby@hawk:~$ 
```


If this flag is found, then the link-editor thinks this file contains non-pic code. 

Looking at the way the shared library is built on Solaris, it is different from other platforms. 


```
# Flags for building a dynamically linked shared object.
SAGESOFLAGS=" "
if [ "$UNAME" = "Linux" ] || [ "$UNAME" = "FreeBSD" ]; then
    SAGESOFLAGS="-shared -Wl,-soname,libcliquer.so"
    export SAGESOFLAGS
elif [ "$UNAME" = "Darwin" ]; then
    MACOSX_DEPLOYMENT_TARGET="10.3"
    export MACOSX_DEPLOYMENT_TARGET
    SAGESOFLAGS="-dynamiclib -single_module -flat_namespace -undefined dynamic_l
ookup"
    export SAGESOFLAGS
elif [ "$UNAME" = "SunOS" ]; then
    SAGESOFLAGS="-G -Bdynamic"
    export SAGESOFLAGS
elif [ "$UNAME" = "CYGWIN" ]; then
    SAGESOFLAGS="-shared -Wl,-soname,libcliquer.so"
```


Using just


```
elif [ "$UNAME" = "SunOS" ]; then
   SAGESOFLAGS="-shared"
```


was sufficient to produce a shared library which did not exhibit this problem. When Sage was started, Sage no longer produced the libcliquer error message, though it did fail to run properly. 

There are in fact several other libraries in Sage that show show output using the `elfdump` command above. 


```
 * libcliquer.so
 * libecl.so
 * libgroebner-0.6.4.so
 * libpboriCudd-0.6.4.so
 * libpolybori-0.6.4.so 
```

(These were observed on OpenSolaris x64. I've confirmed the same is true of libcliquer.so on 64-bit SPARC using `t2.math`, but I've not verified if all the other libraries show this problem. )

I doubt whether these are the only issues preventing Sage running properly on 64-bit Solaris, but these should be resolved. 

Since 
* The current version of Cliquer in Sage 1.2 is not the latest.
* Cliquer 1.2.1 is a bug-fix only release, so should be safe. 
* The Cliquer test suite can't be run as there's no `spkg-check` file - see #9767

it makes sense to update Cliquer and sort out the Solaris and `spkg-check` issues at the same time. 

Dave 

Issue created by migration from https://trac.sagemath.org/ticket/9833





---

archive/issue_comments_096864.json:
```json
{
    "body": "This is a general error in how Cliquer is adapted to/built for Sage.\n\nIt is intended as a stand-alone program, and therefore contains `main()`.\n\nYou **must** (or should)  **not** build [shared] libraries containing a `main()` function.\n\nInstead, use `#ifdef ...` and `-D...` depending on what you build. I think Sage should build and install both, the program and a library. (If you remove/omit `main()` for the shared library, the loader problems should vanish.)\n\n\n```diff\n--- cliquer-1.2.p6/src/Makefile\t2010-02-16 05:26:57.000000000 +0100\n+++ cliquer-1.2.p6/patch/Makefile\t2010-02-16 05:26:55.000000000 +0100\n@@ -1,14 +1,29 @@\n \n ##### Configurable options:\n \n+# Don't need to set any of these compiler variables. They have already been\n+# set when running SAGE_ROOT/local/bin/sage-env as part of installing a\n+# package.\n ## Compiler:\n-CC=gcc\n+# CC=gcc\n #CC=cc\n \n ## Compiler flags:\n \n # GCC:  (also -march=pentium etc, for machine-dependent optimizing)\n-CFLAGS=-Wall -O3 -fomit-frame-pointer -funroll-loops\n+# Build in 64-bit mode on Mac OS X with an Intel processor.\n+\n+# Flags for building a dynamically linked shared object.\n+# SAGESOFLAGS=\"\"\n+# ifeq (`uname`, Linux)\n+# \tSAGESOFLAGS=-shared -Wl,-soname,libcliquer.so\n+# endif\n+# ifeq (`uname`, Darwin)\n+# \tSAGESOFLAGS=-shared -dynamiclib\n+# endif\n+# ifeq (`uname`, SunOS)\n+# \tSAGESOFLAGS=-G -Bdynamic\n+# endif\n \n # GCC w/ debugging:\n #CFLAGS=-Wall -g -DINLINE=\n@@ -36,8 +51,7 @@\n \t$(CC) $(LDFLAGS) -o $@ testcases.o cliquer.o graph.o reorder.o\n \n cl: cl.o cliquer.o graph.o reorder.o\n-\t$(CC) $(LDFLAGS) -o $@ cl.o cliquer.o graph.o reorder.o\n-\n+\t$(CC) $(LDFLAGS) $(SAGESOFLAGS) -o libcliquer.so cl.o cliquer.o graph.o reorder.o\n \n cl.o testcases.o cliquer.o graph.o reorder.o: cliquer.h set.h graph.h misc.h reorder.h Makefile cliquerconf.h\n \n```\n\nNote the changes made to the `cl` target (which is [the name of] the stand-alone program).\n\nThis package really needs work (but there's - besides others - already a ticket (#9871) for an upstream update as well). The files in `src/` are not even vanilla, but contain weird changes in order to use Cliquer as a library from within Sage.",
    "created_at": "2010-09-08T20:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9832#issuecomment-96864",
    "user": "https://github.com/nexttime"
}
```

This is a general error in how Cliquer is adapted to/built for Sage.

It is intended as a stand-alone program, and therefore contains `main()`.

You **must** (or should)  **not** build [shared] libraries containing a `main()` function.

Instead, use `#ifdef ...` and `-D...` depending on what you build. I think Sage should build and install both, the program and a library. (If you remove/omit `main()` for the shared library, the loader problems should vanish.)


```diff
--- cliquer-1.2.p6/src/Makefile	2010-02-16 05:26:57.000000000 +0100
+++ cliquer-1.2.p6/patch/Makefile	2010-02-16 05:26:55.000000000 +0100
@@ -1,14 +1,29 @@
 
 ##### Configurable options:
 
+# Don't need to set any of these compiler variables. They have already been
+# set when running SAGE_ROOT/local/bin/sage-env as part of installing a
+# package.
 ## Compiler:
-CC=gcc
+# CC=gcc
 #CC=cc
 
 ## Compiler flags:
 
 # GCC:  (also -march=pentium etc, for machine-dependent optimizing)
-CFLAGS=-Wall -O3 -fomit-frame-pointer -funroll-loops
+# Build in 64-bit mode on Mac OS X with an Intel processor.
+
+# Flags for building a dynamically linked shared object.
+# SAGESOFLAGS=""
+# ifeq (`uname`, Linux)
+# 	SAGESOFLAGS=-shared -Wl,-soname,libcliquer.so
+# endif
+# ifeq (`uname`, Darwin)
+# 	SAGESOFLAGS=-shared -dynamiclib
+# endif
+# ifeq (`uname`, SunOS)
+# 	SAGESOFLAGS=-G -Bdynamic
+# endif
 
 # GCC w/ debugging:
 #CFLAGS=-Wall -g -DINLINE=
@@ -36,8 +51,7 @@
 	$(CC) $(LDFLAGS) -o $@ testcases.o cliquer.o graph.o reorder.o
 
 cl: cl.o cliquer.o graph.o reorder.o
-	$(CC) $(LDFLAGS) -o $@ cl.o cliquer.o graph.o reorder.o
-
+	$(CC) $(LDFLAGS) $(SAGESOFLAGS) -o libcliquer.so cl.o cliquer.o graph.o reorder.o
 
 cl.o testcases.o cliquer.o graph.o reorder.o: cliquer.h set.h graph.h misc.h reorder.h Makefile cliquerconf.h
 
```

Note the changes made to the `cl` target (which is [the name of] the stand-alone program).

This package really needs work (but there's - besides others - already a ticket (#9871) for an upstream update as well). The files in `src/` are not even vanilla, but contain weird changes in order to use Cliquer as a library from within Sage.



---

archive/issue_comments_096865.json:
```json
{
    "body": "This can be closed when #9871 is closed. \n\nAnother relevant ticket is #9870, which should sort out many of the issues with Cliquer. \n\nDave",
    "created_at": "2010-09-13T21:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9832#issuecomment-96865",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This can be closed when #9871 is closed. 

Another relevant ticket is #9870, which should sort out many of the issues with Cliquer. 

Dave



---

archive/issue_comments_096866.json:
```json
{
    "body": "Minh, \nthis ticket can be effectively ignored now. Since #9871 is merged in sage-4.6.alpha1, one might assume it will get to sage-4.6. With hindsight the issue resolved on this ticket should have been resolved here, but I intending updating the source, so created a wider ticket to do that, only to find that was not going to be possible. \n\nLeif intended resolving #9870. \n\nI'm not sure what the procedure his here, and whether this should be closed now (since it's merged in sage-4.6.alpha1, or wait until it's merged in sage-4.6. I believe the latter is probably more appropriate, as it could potentially be found to be problematic and not get merged in 4.6 at all. \n\nDave",
    "created_at": "2010-09-16T08:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9832#issuecomment-96866",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Minh, 
this ticket can be effectively ignored now. Since #9871 is merged in sage-4.6.alpha1, one might assume it will get to sage-4.6. With hindsight the issue resolved on this ticket should have been resolved here, but I intending updating the source, so created a wider ticket to do that, only to find that was not going to be possible. 

Leif intended resolving #9870. 

I'm not sure what the procedure his here, and whether this should be closed now (since it's merged in sage-4.6.alpha1, or wait until it's merged in sage-4.6. I believe the latter is probably more appropriate, as it could potentially be found to be problematic and not get merged in 4.6 at all. 

Dave



---

archive/issue_events_009954.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-09-16T21:54:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9832",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9832#event-9954"
}
```



---

archive/issue_comments_096867.json:
```json
{
    "body": "I'm closing this ticket as a \"duplicate\" of #9871.  Please reopen it, if the Cliquer relocation error remains or reappears.",
    "created_at": "2010-09-16T21:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9832#issuecomment-96867",
    "user": "https://github.com/qed777"
}
```

I'm closing this ticket as a "duplicate" of #9871.  Please reopen it, if the Cliquer relocation error remains or reappears.



---

archive/issue_comments_096868.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-09-16T21:54:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9832#issuecomment-96868",
    "user": "https://github.com/qed777"
}
```

Resolution: duplicate
