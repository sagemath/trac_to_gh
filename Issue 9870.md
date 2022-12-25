# Issue 9870: Update Cliquer to 1.21 and get the library buiilding properly on Solaris.

archive/issues_009870.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @nathanncohen @qed777 @jhpalmieri\n\nAs documented at #9833, the Cliquer library is causing problems on 64-bit Solaris and 64-bit OpenSolaris. This needs **urgently** resolving, as it is the first problem hit when building a 64-bit version of Sage on Solaris or OpenSolaris. \n\nAs documented at #9521, the test suite for Cliquer is not run correctly. It should generally be run from `spkg-install`, but given it takes only a few seconds to run on even slow hardware, it makes sense to run the tests each time Sage is built. \n\nThe upstream source code has modifications too. Given the latest version is a bug-fix only release, it is wise to update this. (Rather confusingly, the version currently in Sage is 1.2, but the bug-fix release is 1.21. I believe the authors should have called it 1.2.1) See http://users.tkk.fi/pat/cliquer.html\n\n**There are a number of other issues with Cliquer's spkg-install and Makefile. These are the subject of ticket #9870 and will NOT be addressed here to save time, and allow the critical Solaris fix to be integrated as soon as possible.**\n\nThe changes which are made are:\n* Change the compiler options for Solaris from \n\n `-G -Bdynamic`\n\n to \n\n `-shared`\n\n as this avoid the fatal relocation error documented at #9833. \n* Update the source code to the latest version. \n* Run the test cases every time Sage is built, as they take only a few seconds to run. Since the exit code of `make test` is always zero, even if tests fail, it was decided to save the output of `make test` into a file, then check for the word \"ERROR\" in that file. If it exists, a test has failed. If not, all tests have passed. \n* Add correct compiler flags for AIX and HP-UX. These have not been checked, but should work. \n* Add an `spkg-check` file which prints a message that the self-tests are run each time Sage is built. \n* Copy the shared library to the filename `libcliquer.sl` on HP-UX, as that is the extension HP use for shared libraries. (The package currently always builds this as `libcliquer.so` on all platforms), despite that is wrong for several platforms. Most cases are already covered in `spkg-install`, but HP-UX was not.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9871\n\n",
    "created_at": "2010-09-07T22:05:09Z",
    "labels": [
        "component: build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Update Cliquer to 1.21 and get the library buiilding properly on Solaris.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9870",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @nathanncohen @qed777 @jhpalmieri

As documented at #9833, the Cliquer library is causing problems on 64-bit Solaris and 64-bit OpenSolaris. This needs **urgently** resolving, as it is the first problem hit when building a 64-bit version of Sage on Solaris or OpenSolaris. 

As documented at #9521, the test suite for Cliquer is not run correctly. It should generally be run from `spkg-install`, but given it takes only a few seconds to run on even slow hardware, it makes sense to run the tests each time Sage is built. 

The upstream source code has modifications too. Given the latest version is a bug-fix only release, it is wise to update this. (Rather confusingly, the version currently in Sage is 1.2, but the bug-fix release is 1.21. I believe the authors should have called it 1.2.1) See http://users.tkk.fi/pat/cliquer.html

**There are a number of other issues with Cliquer's spkg-install and Makefile. These are the subject of ticket #9870 and will NOT be addressed here to save time, and allow the critical Solaris fix to be integrated as soon as possible.**

The changes which are made are:
* Change the compiler options for Solaris from 

 `-G -Bdynamic`

 to 

 `-shared`

 as this avoid the fatal relocation error documented at #9833. 
* Update the source code to the latest version. 
* Run the test cases every time Sage is built, as they take only a few seconds to run. Since the exit code of `make test` is always zero, even if tests fail, it was decided to save the output of `make test` into a file, then check for the word "ERROR" in that file. If it exists, a test has failed. If not, all tests have passed. 
* Add correct compiler flags for AIX and HP-UX. These have not been checked, but should work. 
* Add an `spkg-check` file which prints a message that the self-tests are run each time Sage is built. 
* Copy the shared library to the filename `libcliquer.sl` on HP-UX, as that is the extension HP use for shared libraries. (The package currently always builds this as `libcliquer.so` on all platforms), despite that is wrong for several platforms. Most cases are already covered in `spkg-install`, but HP-UX was not.

Issue created by migration from https://trac.sagemath.org/ticket/9871





---

archive/issue_comments_097347.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-07T22:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97347",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_events_024865.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/drkirkby",
    "created_at": "2010-09-07T22:36:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "milestone": "sage-4.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9870#event-24865"
}
```



---

archive/issue_comments_097348.json:
```json
{
    "body": "I just realised Cliquer was updated to `cliquer-1.2.p6` - I should have remembered this, as I reviewed it!!\n\nI need to change this, to take into account the changes at `cliquer-1.2.p6`. I'm setting to \"needs work\" for now. It will not take long to resolve.\n\nDave",
    "created_at": "2010-09-07T23:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97348",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I just realised Cliquer was updated to `cliquer-1.2.p6` - I should have remembered this, as I reviewed it!!

I need to change this, to take into account the changes at `cliquer-1.2.p6`. I'm setting to "needs work" for now. It will not take long to resolve.

Dave



---

archive/issue_comments_097349.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-07T23:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97349",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_097350.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-08T00:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97350",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_097351.json:
```json
{
    "body": "Attachment [9871-update-cliquer-and-add-Solaris-fix.patch](tarball://root/attachments/some-uuid/ticket9871/9871-update-cliquer-and-add-Solaris-fix.patch) by drkirkby created at 2010-09-08 02:01:29\n\nMercurial patch. Note, the patched Makefile was not under revision control before, so the patch is quite big.",
    "created_at": "2010-09-08T02:01:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97351",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9871-update-cliquer-and-add-Solaris-fix.patch](tarball://root/attachments/some-uuid/ticket9871/9871-update-cliquer-and-add-Solaris-fix.patch) by drkirkby created at 2010-09-08 02:01:29

Mercurial patch. Note, the patched Makefile was not under revision control before, so the patch is quite big.



---

archive/issue_comments_097352.json:
```json
{
    "body": "Note, since the old Makefile was not under revision control, the patches look a **LOT** bigger than they actually are. If we compare the old Makefile and the new Makefile, the change is only that two characters \"./\" are added in front of the executable `testcases`. \n\n\n```\ndrkirkby@hawk:~/sage-4.5.3/spkg/standard$ diff -u cliquer-1.2.p6/patch/Makefile cliquer-1.21/patches/Makefile\n--- cliquer-1.2.p6/patch/Makefile\tTue Feb 16 04:26:55 2010\n+++ cliquer-1.21/patches/Makefile\tWed Sep  8 02:42:06 2010\n@@ -66,4 +66,4 @@\n \tcp * \"`date \"+backup-%Y-%m-%d-%H-%M\"`\"  2>/dev/null || true\n \n test: testcases\n-\ttestcases\n+\t./testcases\n```\n\n\nSo when reviewing this, be aware most of the changes that are seen in the attached patch are simply a result of the old files not being under revision control, and the `patch` directory was in the `.hgignore` file. \n\nWith the change in the compiler options, there are no text relocations which were seen on #9833. Now, using `elfdump`, no such problems are observed. \n\n\n```\ndrkirkby@hawk:~/sage-4.5.3$ elfdump -d local/lib/libcliquer.so | grep TEXTREL\ndrkirkby@hawk:~/sage-4.5.3$ \n```\n\n\nThis means the library will be more reliable - see #9833 for a discussion of why we need to avoid this. \n\n\n\nDave",
    "created_at": "2010-09-08T02:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97352",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Note, since the old Makefile was not under revision control, the patches look a **LOT** bigger than they actually are. If we compare the old Makefile and the new Makefile, the change is only that two characters "./" are added in front of the executable `testcases`. 


```
drkirkby@hawk:~/sage-4.5.3/spkg/standard$ diff -u cliquer-1.2.p6/patch/Makefile cliquer-1.21/patches/Makefile
--- cliquer-1.2.p6/patch/Makefile	Tue Feb 16 04:26:55 2010
+++ cliquer-1.21/patches/Makefile	Wed Sep  8 02:42:06 2010
@@ -66,4 +66,4 @@
 	cp * "`date "+backup-%Y-%m-%d-%H-%M"`"  2>/dev/null || true
 
 test: testcases
-	testcases
+	./testcases
```


So when reviewing this, be aware most of the changes that are seen in the attached patch are simply a result of the old files not being under revision control, and the `patch` directory was in the `.hgignore` file. 

With the change in the compiler options, there are no text relocations which were seen on #9833. Now, using `elfdump`, no such problems are observed. 


```
drkirkby@hawk:~/sage-4.5.3$ elfdump -d local/lib/libcliquer.so | grep TEXTREL
drkirkby@hawk:~/sage-4.5.3$ 
```


This means the library will be more reliable - see #9833 for a discussion of why we need to avoid this. 



Dave



---

archive/issue_comments_097353.json:
```json
{
    "body": "See #9833 for at least two reasons.\n\nNote that\n\n```sh\n    make something | tee output_file\n```\n\nwill **almost always** have a zero exit status, namely unless `tee` fails (or you use `bash`'s `set -o pipefail` feature). In fact `make test`, i.e. `src/testcases`, won't exit with a non-zero exit status in *all* cases (but at least *some*); I would change that and post the fix upstream (changing some functions from `void` to return an `int`, accumulating the number of failures and returning that at the end of `main()`).   \n\nThere are \"of course\"<sup>TM</sup> typos and other things that IMHO have to be changed ;-) (e.g. using `$MAKE` instead of `make`; `SAGE_PORT` is not tested but reported to be set, ...).\n\n\n```sh\nif [ \"x`grep ERROR test.out`\" != x ]; then\n    ...\n```\n\nshould e.g. be\n\n```sh\nif grep -q ERROR test.out; then\n    ...\n```\n\n\n...\n\nBtw, I think the spkg's name should have a `.p0` or `.p1` in it.",
    "created_at": "2010-09-08T20:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97353",
    "user": "https://github.com/nexttime"
}
```

See #9833 for at least two reasons.

Note that

```sh
    make something | tee output_file
```

will **almost always** have a zero exit status, namely unless `tee` fails (or you use `bash`'s `set -o pipefail` feature). In fact `make test`, i.e. `src/testcases`, won't exit with a non-zero exit status in *all* cases (but at least *some*); I would change that and post the fix upstream (changing some functions from `void` to return an `int`, accumulating the number of failures and returning that at the end of `main()`).   

There are "of course"<sup>TM</sup> typos and other things that IMHO have to be changed ;-) (e.g. using `$MAKE` instead of `make`; `SAGE_PORT` is not tested but reported to be set, ...).


```sh
if [ "x`grep ERROR test.out`" != x ]; then
    ...
```

should e.g. be

```sh
if grep -q ERROR test.out; then
    ...
```


...

Btw, I think the spkg's name should have a `.p0` or `.p1` in it.



---

archive/issue_comments_097354.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-08T20:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97354",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_097355.json:
```json
{
    "body": "> Note that\n\n```\n    make something | tee output_file\n```\n\n> will almost always have a zero exit status\n\nThe comment in the file suggests that \"make test\" itself will have a zero exit status even if there are failures, and this is why the \"tee ...\" is there at all.  (This indicates problems with the makefile, I suppose.)  But I may be misunderstanding the situation.  We could also use the \"pipestatus\" script...",
    "created_at": "2010-09-08T20:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97355",
    "user": "https://github.com/jhpalmieri"
}
```

> Note that

```
    make something | tee output_file
```

> will almost always have a zero exit status

The comment in the file suggests that "make test" itself will have a zero exit status even if there are failures, and this is why the "tee ..." is there at all.  (This indicates problems with the makefile, I suppose.)  But I may be misunderstanding the situation.  We could also use the "pipestatus" script...



---

archive/issue_comments_097356.json:
```json
{
    "body": "* There's no need for this to be a .p0 or .p1. It is a new upstream source code (version 1.21), so the patch level in Sage is removed. \n  * It is `make test` which exits with 0, even when I alter the file `src/testcases.c` to force tests to fail. A bunch of errors are reported, then `make` exits with an exit code of 0. \n  * `make test` actually creates a binary called `testcases` and then executes that. That exits with 0 in all cases. \n  * I agree this is an upstream bug in the test code - it should exit with a non-zero code in the case of errors. \n  * I'm not trying to test the exit code of `tee`, but rather `grep`. \n  * I thought `grep -q` was not portable, but it was `cmp -q` which caused a portability issue. So I'll change that. \n  * I take Leif's point about the fact that there should be no main in a shared library. But the code works with the compiler options `-shared -Wl,-h,libcliquer.so` on Linux and OS X, even though Leif says there's a main there. I do not want to start re-writing the source code or Makefile to remove main(). That's an upstream problem. If it was the only way to fix the text relocations, then I would do it. But simply using the same compiler options as on other platforms works. \n\nI've created #9870 to address the other issues. I agree there are many, but I don't want this ticket drag on like #9603. \n\nDave",
    "created_at": "2010-09-08T21:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97356",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

* There's no need for this to be a .p0 or .p1. It is a new upstream source code (version 1.21), so the patch level in Sage is removed. 
  * It is `make test` which exits with 0, even when I alter the file `src/testcases.c` to force tests to fail. A bunch of errors are reported, then `make` exits with an exit code of 0. 
  * `make test` actually creates a binary called `testcases` and then executes that. That exits with 0 in all cases. 
  * I agree this is an upstream bug in the test code - it should exit with a non-zero code in the case of errors. 
  * I'm not trying to test the exit code of `tee`, but rather `grep`. 
  * I thought `grep -q` was not portable, but it was `cmp -q` which caused a portability issue. So I'll change that. 
  * I take Leif's point about the fact that there should be no main in a shared library. But the code works with the compiler options `-shared -Wl,-h,libcliquer.so` on Linux and OS X, even though Leif says there's a main there. I do not want to start re-writing the source code or Makefile to remove main(). That's an upstream problem. If it was the only way to fix the text relocations, then I would do it. But simply using the same compiler options as on other platforms works. 

I've created #9870 to address the other issues. I agree there are many, but I don't want this ticket drag on like #9603. 

Dave



---

archive/issue_comments_097357.json:
```json
{
    "body": "Replying to [comment:7 jhpalmieri]:\n> > Note that\n\n```\n    make something | tee output_file\n```\n\n> > will almost always have a zero exit status\n> \n> The comment in the file suggests that \"make test\" itself will have a zero exit status even if there are failures, and this is why the \"tee ...\" is there at all.\n\nIt **does** return 1 on **some** errors, but not all. (And I suggested to modify `testcases.c` to return a non-zero value *on all errors*. This is almost trivial.) \n\n> (This indicates problems with the makefile, I suppose.)  But I may be misunderstanding the situation.\n\nThe Makefile does not cause problems; just the comment is not (fully) correct.\n\n> We could also use the \"pipestatus\" script...\n\nThe correct way would be to redirect the output in the `make` rule itself (with `> test.out`), or - if you want to see the test running live - not redirect it at all. Of course you can also write it to a file and use `tail [-f]`; the written file will usually be deleted after the spkg is installed (and tested) anyhow, unless you use `sage-spkg -i -s ...`. So I'd prefer changing the source code and let `testcases` just write to `stdout` and `stderr`, s.t. the test output ends up in `spkg/logs/*.log`, as usual.",
    "created_at": "2010-09-08T22:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97357",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:7 jhpalmieri]:
> > Note that

```
    make something | tee output_file
```

> > will almost always have a zero exit status
> 
> The comment in the file suggests that "make test" itself will have a zero exit status even if there are failures, and this is why the "tee ..." is there at all.

It **does** return 1 on **some** errors, but not all. (And I suggested to modify `testcases.c` to return a non-zero value *on all errors*. This is almost trivial.) 

> (This indicates problems with the makefile, I suppose.)  But I may be misunderstanding the situation.

The Makefile does not cause problems; just the comment is not (fully) correct.

> We could also use the "pipestatus" script...

The correct way would be to redirect the output in the `make` rule itself (with `> test.out`), or - if you want to see the test running live - not redirect it at all. Of course you can also write it to a file and use `tail [-f]`; the written file will usually be deleted after the spkg is installed (and tested) anyhow, unless you use `sage-spkg -i -s ...`. So I'd prefer changing the source code and let `testcases` just write to `stdout` and `stderr`, s.t. the test output ends up in `spkg/logs/*.log`, as usual.



---

archive/issue_comments_097358.json:
```json
{
    "body": "Leif, \n\nDifferent people have different ways of doing things. Much is personal style. We have numerous examples of that on #9603, where each of us will do something in a different way. \n\nCan you tell me what is wrong with the current method? I can't see anything particularly wrong with what I have. I want to get a patch into Sage asap that will allow the library to build on 64-bit Solaris. \n\nI will report the issue of the source code to the upstream developers. You can add further suggestions to #9870 if you want. But as far as I can see, this achieves the aim. It is an improvement on what we had before and allows us to make progress with the Solaris 64-bit port. I do not want to go around editing the source code, when a couple of lines in a script does the job. If you look in detail at the source code, you will find it is rather strange anyway. I simply do not want to get involved in editing that. \n\nI created #9870 to address other issues\n\nDave",
    "created_at": "2010-09-09T00:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97358",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Leif, 

Different people have different ways of doing things. Much is personal style. We have numerous examples of that on #9603, where each of us will do something in a different way. 

Can you tell me what is wrong with the current method? I can't see anything particularly wrong with what I have. I want to get a patch into Sage asap that will allow the library to build on 64-bit Solaris. 

I will report the issue of the source code to the upstream developers. You can add further suggestions to #9870 if you want. But as far as I can see, this achieves the aim. It is an improvement on what we had before and allows us to make progress with the Solaris 64-bit port. I do not want to go around editing the source code, when a couple of lines in a script does the job. If you look in detail at the source code, you will find it is rather strange anyway. I simply do not want to get involved in editing that. 

I created #9870 to address other issues

Dave



---

archive/issue_comments_097359.json:
```json
{
    "body": "Replying to [comment:8 drkirkby]:\n>  * There's no need for this to be a .p0 or .p1. It is a new upstream source code (version 1.21), so the patch level in Sage is removed.\n\nThis seems to be an endless discussion. I'd prefer having *always* a patch level, be it `.p0` for unpatched upstream code. But here we actually (still) do patch a fresh upstream release, so it should IMHO be `.p1` (or `.p0` for those who think the *first unpatched new release* should *not* have a patch level extension).\n\n>  * It is `make test` which exits with 0, even when I alter the file `src/testcases.c` to force tests to fail.\n\nWhen `testcases` returns 1, so does `make test` (or `$MAKE test`); see above.\n \n>  * `make test` actually creates a binary called `testcases` and then executes that. That exits with 0 in all cases.\n\nNot really, though not really relevant if it doesn't in *all* error cases. But\n\n```\nmake test | tee test.out\nif [ $? -ne 0 ]; then\n    echo \"Failed to compile test cases of cliquer... exiting\"\n    exit 1\nfi\n```\n\ndoes not even catch the cases in which it *does* return 1, nor errors *compiling* the test program - which is perhaps even worse, since\n\n```sh\n[ \"x`grep ERROR non_existing_file`\" != x ] && never_happens\n```\n\n(There will just be an error message of grep in the spkg's installation log file. You know [these messages](http://trac.sagemath.org/sage_trac/ticket/9434) well...)\n\n\n```sh\n~/Sage/spkgs/cliquer-1.21$ egrep -B2 \"return |exit\" src/testcases.c\n        printf(\"Please reconfigure and recompile.\\n\");\n        printf(\"\\n\");\n        exit(1);\n--\n    if ((fp=fopen(\"testcase-small.a\",\"rt\"))==NULL) {\n        perror(\"testcase-small.a\");\n        return 1;\n--\n    fclose(fp);\n    if (!small) {\n        return 1;\n--\n    large=graph_read_dimacs_file(\"testcase-large.b\");\n    if (!large) {\n        return 1;\n--\n    if ((fp=fopen(\"testcase-large-w.b\",\"rb\"))==NULL) {\n        perror(\"testcase-large-w.b\");\n        return 1;\n--\n    fclose(fp);\n    if (!wlarge) {\n        return 1;\n--\n        printf(\"ERROR\\n\");\n        graph_test(small,stdout);\n        return 1;\n--\n        printf(\"ERROR\\n\");\n        graph_test(large,stdout);\n        return 1;\n--\n        printf(\"ERROR\\n\");\n        graph_test(wlarge,stdout);\n        return 1;\n--\n            small,0,0,FALSE,small_max_cliques);\n\n    return 0;\n--\n        printf(\")\\n\");\n    }\n    return found;\n--\n\n    if (!list_contains(sets,s,g))\n        return FALSE;\n    user_fnct_cnt--;\n    if (!user_fnct_cnt)\n        return FALSE;\n    return TRUE;\n--\n    if (n!=correct_n) {\n        printf(\"ERROR (returned %d cliques (!=%d))\\n\",n,correct_n);\n        return FALSE;\n--\n        if (!list_contains(sopt->sets,s[i],sopt->g)) {\n            printf(\"(inner loop)\\n\");\n            return FALSE;\n        }\n    }\n    return TRUE;\n```\n\n\nAlso, running the test suite just in `spkg-install` is IMHO a bad idea; that disturbs upcoming improvements to `sage-spkg` wrt. `SAGE_CHECK`, since we don't want the [whole] *build* to fail (or stop) just because *some* package failed to pass its tests; cf. the Python package. And we won't be able to log test results separately.\n\n>  * I agree this is an upstream bug in the test code - it should exit with a non-zero code in the case of errors.\n\n>  * I'm not trying to test the exit code of `tee`, but rather `grep`.\n\nSee above. (You do both, or actually currently only the former.)\n \n>  * I thought `grep -q` was not portable, but it was `cmp -q` which caused a portability issue. So I'll change that.\n\nI think there are still but very rarely dumb `grep`s around that don't understand `-q`, in which case one can omit the `-q` and redirect `stdout` to `/dev/null`; this anyway doesn't affect `grep`'s exit status. (But we should IMHO ignore that and use `-q`. POSIX isn't of the 1970s either.)\n  \n>  * I take Leif's point about the fact that there should be no main in a shared library. But the code works with the compiler options `-shared -Wl,-h,libcliquer.so` on Linux and OS X, even though Leif says there's a main there. I do not want to start re-writing the source code or Makefile to remove main(). That's an upstream problem.\n\nThe original code was - sorry - messed up by some *Sage* developer. (I already mentioned `src/` was *not* vanilla.)\n\n> If it was the only way to fix the text relocations, then I would do it. But simply using the same compiler options as on other platforms works.\n\nOk, (in my opinion) a work-around, but doesn't remove the real cause, namely bad adaption / conversion of a program to a library.\n\nThe \"bad\" flags btw. originate from Sage, too - not upstream.\n\n> I've created #9870 to address the other issues. I agree there are many, but I don't want this ticket drag on like #9603.\n\nCreated six weeks ago, starting with a minor issue. Now we won't have to touch that for a long time I think, since all currently desirable changes are made - on *one* ticket, by creating *one* new spkg. (The situation with blockers is a bit different.)\n\nBut regarding the previous Cliquer tickets (which weren't quick ones either), `SPKG.txt` still fails to spell the algorithm's developer's name correctly. \n\nI've taken over *that* ticket (#9870). If this ticket here quickly gets positively reviewed, I can make the remaining changes, based on it. Changing `testcases.c` is rather independent of that, but not the rest.",
    "created_at": "2010-09-09T04:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97359",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:8 drkirkby]:
>  * There's no need for this to be a .p0 or .p1. It is a new upstream source code (version 1.21), so the patch level in Sage is removed.

This seems to be an endless discussion. I'd prefer having *always* a patch level, be it `.p0` for unpatched upstream code. But here we actually (still) do patch a fresh upstream release, so it should IMHO be `.p1` (or `.p0` for those who think the *first unpatched new release* should *not* have a patch level extension).

>  * It is `make test` which exits with 0, even when I alter the file `src/testcases.c` to force tests to fail.

When `testcases` returns 1, so does `make test` (or `$MAKE test`); see above.
 
>  * `make test` actually creates a binary called `testcases` and then executes that. That exits with 0 in all cases.

Not really, though not really relevant if it doesn't in *all* error cases. But

```
make test | tee test.out
if [ $? -ne 0 ]; then
    echo "Failed to compile test cases of cliquer... exiting"
    exit 1
fi
```

does not even catch the cases in which it *does* return 1, nor errors *compiling* the test program - which is perhaps even worse, since

```sh
[ "x`grep ERROR non_existing_file`" != x ] && never_happens
```

(There will just be an error message of grep in the spkg's installation log file. You know [these messages](http://trac.sagemath.org/sage_trac/ticket/9434) well...)


```sh
~/Sage/spkgs/cliquer-1.21$ egrep -B2 "return |exit" src/testcases.c
        printf("Please reconfigure and recompile.\n");
        printf("\n");
        exit(1);
--
    if ((fp=fopen("testcase-small.a","rt"))==NULL) {
        perror("testcase-small.a");
        return 1;
--
    fclose(fp);
    if (!small) {
        return 1;
--
    large=graph_read_dimacs_file("testcase-large.b");
    if (!large) {
        return 1;
--
    if ((fp=fopen("testcase-large-w.b","rb"))==NULL) {
        perror("testcase-large-w.b");
        return 1;
--
    fclose(fp);
    if (!wlarge) {
        return 1;
--
        printf("ERROR\n");
        graph_test(small,stdout);
        return 1;
--
        printf("ERROR\n");
        graph_test(large,stdout);
        return 1;
--
        printf("ERROR\n");
        graph_test(wlarge,stdout);
        return 1;
--
            small,0,0,FALSE,small_max_cliques);

    return 0;
--
        printf(")\n");
    }
    return found;
--

    if (!list_contains(sets,s,g))
        return FALSE;
    user_fnct_cnt--;
    if (!user_fnct_cnt)
        return FALSE;
    return TRUE;
--
    if (n!=correct_n) {
        printf("ERROR (returned %d cliques (!=%d))\n",n,correct_n);
        return FALSE;
--
        if (!list_contains(sopt->sets,s[i],sopt->g)) {
            printf("(inner loop)\n");
            return FALSE;
        }
    }
    return TRUE;
```


Also, running the test suite just in `spkg-install` is IMHO a bad idea; that disturbs upcoming improvements to `sage-spkg` wrt. `SAGE_CHECK`, since we don't want the [whole] *build* to fail (or stop) just because *some* package failed to pass its tests; cf. the Python package. And we won't be able to log test results separately.

>  * I agree this is an upstream bug in the test code - it should exit with a non-zero code in the case of errors.

>  * I'm not trying to test the exit code of `tee`, but rather `grep`.

See above. (You do both, or actually currently only the former.)
 
>  * I thought `grep -q` was not portable, but it was `cmp -q` which caused a portability issue. So I'll change that.

I think there are still but very rarely dumb `grep`s around that don't understand `-q`, in which case one can omit the `-q` and redirect `stdout` to `/dev/null`; this anyway doesn't affect `grep`'s exit status. (But we should IMHO ignore that and use `-q`. POSIX isn't of the 1970s either.)
  
>  * I take Leif's point about the fact that there should be no main in a shared library. But the code works with the compiler options `-shared -Wl,-h,libcliquer.so` on Linux and OS X, even though Leif says there's a main there. I do not want to start re-writing the source code or Makefile to remove main(). That's an upstream problem.

The original code was - sorry - messed up by some *Sage* developer. (I already mentioned `src/` was *not* vanilla.)

> If it was the only way to fix the text relocations, then I would do it. But simply using the same compiler options as on other platforms works.

Ok, (in my opinion) a work-around, but doesn't remove the real cause, namely bad adaption / conversion of a program to a library.

The "bad" flags btw. originate from Sage, too - not upstream.

> I've created #9870 to address the other issues. I agree there are many, but I don't want this ticket drag on like #9603.

Created six weeks ago, starting with a minor issue. Now we won't have to touch that for a long time I think, since all currently desirable changes are made - on *one* ticket, by creating *one* new spkg. (The situation with blockers is a bit different.)

But regarding the previous Cliquer tickets (which weren't quick ones either), `SPKG.txt` still fails to spell the algorithm's developer's name correctly. 

I've taken over *that* ticket (#9870). If this ticket here quickly gets positively reviewed, I can make the remaining changes, based on it. Changing `testcases.c` is rather independent of that, but not the rest.



---

archive/issue_comments_097360.json:
```json
{
    "body": "Replying to [comment:11 leif]:\n \n> I've taken over *that* ticket (#9870). If this ticket here quickly gets positively reviewed, I can make the remaining changes, based on it. Changing `testcases.c` is rather independent of that, but not the rest.\n\nLeif, \nsince you have taken on #9870, I think it's sensible if I restrict this ticket to **only** changing the compiler flags on Solaris, to allow this to build properly on Solaris without the text relocations. It's pointless me making other changes, which you are going to change anyway. \n\nI've written code to enable the tests, but you intend changing the source code. As such I am going to make only a dozen or so bytes of changes. \n\nDave",
    "created_at": "2010-09-13T21:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97360",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:11 leif]:
 
> I've taken over *that* ticket (#9870). If this ticket here quickly gets positively reviewed, I can make the remaining changes, based on it. Changing `testcases.c` is rather independent of that, but not the rest.

Leif, 
since you have taken on #9870, I think it's sensible if I restrict this ticket to **only** changing the compiler flags on Solaris, to allow this to build properly on Solaris without the text relocations. It's pointless me making other changes, which you are going to change anyway. 

I've written code to enable the tests, but you intend changing the source code. As such I am going to make only a dozen or so bytes of changes. 

Dave



---

archive/issue_comments_097361.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-13T21:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97361",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_097362.json:
```json
{
    "body": "I'm marking for needing review. This just changes the compiler flags for Solaris. Now the library has no issues:\n\n\n```\ndrkirkby@hawk:~/sage-4.6.alpha0/local/lib$ elfdump -d libcliquer.so | grep TEXTREL\ndrkirkby@hawk:~/sage-4.6.alpha0/local/lib$ \n```\n\n\nThis constrasts with one of the libraries that does still have this problem, which is ECL\n\n\n```\ndrkirkby@hawk:~/sage-4.6.alpha0/local/lib$ elfdump -d libecl*.so | grep TEXTREL\n      [24]  TEXTREL           0                   \n      [33]  FLAGS             0x4                 [ TEXTREL ]\ndrkirkby@hawk:~/sage-4.6.alpha0/local/lib$ \n```\n\n\nThe changes to the complier flags avoid this problem. \n\nDave",
    "created_at": "2010-09-13T21:11:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97362",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm marking for needing review. This just changes the compiler flags for Solaris. Now the library has no issues:


```
drkirkby@hawk:~/sage-4.6.alpha0/local/lib$ elfdump -d libcliquer.so | grep TEXTREL
drkirkby@hawk:~/sage-4.6.alpha0/local/lib$ 
```


This constrasts with one of the libraries that does still have this problem, which is ECL


```
drkirkby@hawk:~/sage-4.6.alpha0/local/lib$ elfdump -d libecl*.so | grep TEXTREL
      [24]  TEXTREL           0                   
      [33]  FLAGS             0x4                 [ TEXTREL ]
drkirkby@hawk:~/sage-4.6.alpha0/local/lib$ 
```


The changes to the complier flags avoid this problem. 

Dave



---

archive/issue_comments_097363.json:
```json
{
    "body": "Attachment [9871-simpler-patch-to-ONLY-solve-Solaris-problems.patch](tarball://root/attachments/some-uuid/ticket9871/9871-simpler-patch-to-ONLY-solve-Solaris-problems.patch) by drkirkby created at 2010-09-13 21:12:44\n\nSimple patch which *replaces* the earlier patch.",
    "created_at": "2010-09-13T21:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97363",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9871-simpler-patch-to-ONLY-solve-Solaris-problems.patch](tarball://root/attachments/some-uuid/ticket9871/9871-simpler-patch-to-ONLY-solve-Solaris-problems.patch) by drkirkby created at 2010-09-13 21:12:44

Simple patch which *replaces* the earlier patch.



---

archive/issue_comments_097364.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-13T21:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97364",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097365.json:
```json
{
    "body": "Then put a comment at #9833 (where I would have expected this fix) that it can be closed as a duplicate as soon as this ticket gets merged.\n\nReporting this upstream is IMHO inappropriate, since *Sage* messed up the build.",
    "created_at": "2010-09-13T21:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97365",
    "user": "https://github.com/nexttime"
}
```

Then put a comment at #9833 (where I would have expected this fix) that it can be closed as a duplicate as soon as this ticket gets merged.

Reporting this upstream is IMHO inappropriate, since *Sage* messed up the build.



---

archive/issue_comments_097366.json:
```json
{
    "body": "This seems to work on fulvia in 64-bit mode; I'm still building on t2 (I'm starting a 64-bit build from scratch there, so it will take another half hour before it gets to cliquer).\n\nHowever, I can't get this to build in 32-bit mode.  On both fulvia and t2 I get essentially the same error:\n\n```\ngcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC  -DENABLE_LONG_OPTIONS -o cl.o -c cl.c\ngcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/include   -c -o cliquer.o cliquer.c\ngcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/include   -c -o graph.o graph.c\ngcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/include   -c -o reorder.o reorder.c\ngcc  -L/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/lib  -shared -Wl,-soname,libcliquer.so -o libcliquer.so cl.o cliquer.o graph.o reorder.o\nld: warning: option -o appears more than once, first setting taken\nld: fatal: file libcliquer.so: unknown file type\nld: fatal: File processing errors. No output written to libcliquer.so\ncollect2: ld returned 1 exit status\nmake: *** [cl] Error 1\nFailed to compile cliquer... exiting\n```\n\nOr did I do something stupid?",
    "created_at": "2010-09-13T21:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97366",
    "user": "https://github.com/jhpalmieri"
}
```

This seems to work on fulvia in 64-bit mode; I'm still building on t2 (I'm starting a 64-bit build from scratch there, so it will take another half hour before it gets to cliquer).

However, I can't get this to build in 32-bit mode.  On both fulvia and t2 I get essentially the same error:

```
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC  -DENABLE_LONG_OPTIONS -o cl.o -c cl.c
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/include   -c -o cliquer.o cliquer.c
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/include   -c -o graph.o graph.c
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/include   -c -o reorder.o reorder.c
gcc  -L/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/lib  -shared -Wl,-soname,libcliquer.so -o libcliquer.so cl.o cliquer.o graph.o reorder.o
ld: warning: option -o appears more than once, first setting taken
ld: fatal: file libcliquer.so: unknown file type
ld: fatal: File processing errors. No output written to libcliquer.so
collect2: ld returned 1 exit status
make: *** [cl] Error 1
Failed to compile cliquer... exiting
```

Or did I do something stupid?



---

archive/issue_comments_097367.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-13T21:46:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97367",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_097368.json:
```json
{
    "body": "Replying to [comment:15 jhpalmieri]:\n> This seems to work on fulvia in 64-bit mode; I'm still building on t2 (I'm starting a 64-bit build from scratch there, so it will take another half hour before it gets to cliquer).\n> \n> However, I can't get this to build in 32-bit mode.  On both fulvia and t2 I get essentially the same error:\n> {{{\n> gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC  -DENABLE_LONG_OPTIONS -o cl.o -c cl.c\n> gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/include   -c -o cliquer.o cliquer.c\n> gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/include   -c -o graph.o graph.c\n> gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/include   -c -o reorder.o reorder.c\n> gcc  -L/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/lib  -shared -Wl,-soname,libcliquer.so -o libcliquer.so cl.o cliquer.o graph.o reorder.o\n> ld: warning: option -o appears more than once, first setting taken\n> ld: fatal: file libcliquer.so: unknown file type\n> ld: fatal: File processing errors. No output written to libcliquer.so\n> collect2: ld returned 1 exit status\n> make: *** [cl] Error 1\n> Failed to compile cliquer... exiting\n> }}}\n> Or did I do something stupid?\n\nEm, this is odd. On OpenSolaris I get the following in 32-bit mode. \n\nI was pretty sure I'd checked this on SPARC too. \n\n```\ngcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC  -DENABLE_LONG_OPTIONS -o cl.o -c cl.c\ngcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/export/home/drkirkby/sage-4.6.alpha0/local/include   -c -o cliquer.o cliquer.c\ngcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/export/home/drkirkby/sage-4.6.alpha0/local/include   -c -o graph.o graph.c\ngcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/export/home/drkirkby/sage-4.6.alpha0/local/include   -c -o reorder.o reorder.c\ngcc  -L/export/home/drkirkby/sage-4.6.alpha0/local/lib  -shared -Wl,-soname,libcliquer.so -o libcliquer.so cl.o cliquer.o graph.o reorder.o\n\nreal\t0m1.760s\nuser\t0m1.661s\nsys\t0m0.083s\nSuccessfully installed cliquer-1.2.p7\n```\n",
    "created_at": "2010-09-13T22:04:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97368",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:15 jhpalmieri]:
> This seems to work on fulvia in 64-bit mode; I'm still building on t2 (I'm starting a 64-bit build from scratch there, so it will take another half hour before it gets to cliquer).
> 
> However, I can't get this to build in 32-bit mode.  On both fulvia and t2 I get essentially the same error:
> {{{
> gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC  -DENABLE_LONG_OPTIONS -o cl.o -c cl.c
> gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/include   -c -o cliquer.o cliquer.c
> gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/include   -c -o graph.o graph.c
> gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/include   -c -o reorder.o reorder.c
> gcc  -L/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/lib  -shared -Wl,-soname,libcliquer.so -o libcliquer.so cl.o cliquer.o graph.o reorder.o
> ld: warning: option -o appears more than once, first setting taken
> ld: fatal: file libcliquer.so: unknown file type
> ld: fatal: File processing errors. No output written to libcliquer.so
> collect2: ld returned 1 exit status
> make: *** [cl] Error 1
> Failed to compile cliquer... exiting
> }}}
> Or did I do something stupid?

Em, this is odd. On OpenSolaris I get the following in 32-bit mode. 

I was pretty sure I'd checked this on SPARC too. 

```
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC  -DENABLE_LONG_OPTIONS -o cl.o -c cl.c
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/export/home/drkirkby/sage-4.6.alpha0/local/include   -c -o cliquer.o cliquer.c
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/export/home/drkirkby/sage-4.6.alpha0/local/include   -c -o graph.o graph.c
gcc  -O2  -g  -Wall -fomit-frame-pointer -funroll-loops -c -fPIC   -I/export/home/drkirkby/sage-4.6.alpha0/local/include   -c -o reorder.o reorder.c
gcc  -L/export/home/drkirkby/sage-4.6.alpha0/local/lib  -shared -Wl,-soname,libcliquer.so -o libcliquer.so cl.o cliquer.o graph.o reorder.o

real	0m1.760s
user	0m1.661s
sys	0m0.083s
Successfully installed cliquer-1.2.p7
```




---

archive/issue_comments_097369.json:
```json
{
    "body": "I get the same error in 64-bit mode on t2.  You can look at my logs on t2 in /scratch/palmieri/sage-4.5.3.rc0/spkg/logs and also /scratch/palmieri/64bit/sage-4.6.alpha0/spkg/logs.",
    "created_at": "2010-09-13T22:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97369",
    "user": "https://github.com/jhpalmieri"
}
```

I get the same error in 64-bit mode on t2.  You can look at my logs on t2 in /scratch/palmieri/sage-4.5.3.rc0/spkg/logs and also /scratch/palmieri/64bit/sage-4.6.alpha0/spkg/logs.



---

archive/issue_comments_097370.json:
```json
{
    "body": "Replying to [comment:15 jhpalmieri]:\n> I can't get this to build in 32-bit mode.  On both fulvia and t2 I get essentially the same error:\n\n```\n...\ngcc  -L/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/lib  -shared -Wl,-soname,libcliquer.so -o libcliquer.so cl.o cliquer.o graph.o reorder.o\nld: warning: option -o appears more than once, first setting taken\n...\n```\n\n\nLooks like a linker bug. (Or incapability?)\n\nIs this the Sun linker? Then you should pass `-Wl,-h,libcliquer.so` IIRC.",
    "created_at": "2010-09-13T22:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97370",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:15 jhpalmieri]:
> I can't get this to build in 32-bit mode.  On both fulvia and t2 I get essentially the same error:

```
...
gcc  -L/home/palmieri/fulvia/32bit/sage-4.6.alpha0/local/lib  -shared -Wl,-soname,libcliquer.so -o libcliquer.so cl.o cliquer.o graph.o reorder.o
ld: warning: option -o appears more than once, first setting taken
...
```


Looks like a linker bug. (Or incapability?)

Is this the Sun linker? Then you should pass `-Wl,-h,libcliquer.so` IIRC.



---

archive/issue_comments_097371.json:
```json
{
    "body": "The linker is the problem. \n\nOn Solaris 10, only the Sun options are accepted. \n\nOn OpenSolaris, both the Sun and GNU options are given. \n\n\n```\ngcc -m64 -G -Wl,-h,libcliquer.so cl.o cliquer.o graph.o reorder.o -o libcliquer.so\n```\n\n\nshould work on both, but it has the text relocations problems still. Hopefully we can find some options to pass to the linker which don't exhibit this problem. \n\nIf I build with the Sun compiler, no such problem is seen. \n\nDave",
    "created_at": "2010-09-13T22:34:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97371",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The linker is the problem. 

On Solaris 10, only the Sun options are accepted. 

On OpenSolaris, both the Sun and GNU options are given. 


```
gcc -m64 -G -Wl,-h,libcliquer.so cl.o cliquer.o graph.o reorder.o -o libcliquer.so
```


should work on both, but it has the text relocations problems still. Hopefully we can find some options to pass to the linker which don't exhibit this problem. 

If I build with the Sun compiler, no such problem is seen. 

Dave



---

archive/issue_comments_097372.json:
```json
{
    "body": "I know Leif said shared libraries should not have a main, which is true. But putting \n\n\n```\n#ifdef BUILD_EXECUTABLE\nmain()\n{\nblah blah blah\n}\n#endif\n```\n\n\nin cl.c does not help the text relocation problem.",
    "created_at": "2010-09-13T22:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97372",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I know Leif said shared libraries should not have a main, which is true. But putting 


```
#ifdef BUILD_EXECUTABLE
main()
{
blah blah blah
}
#endif
```


in cl.c does not help the text relocation problem.



---

archive/issue_comments_097373.json:
```json
{
    "body": "It looks like we need `-z text` to be passed to the linker. From the linker man page:\n\n\n```\n    -z text\n\n         In dynamic mode only, forces a fatal error if any  relo-\n         cations   against   non-writable,  allocatable  sections\n         remain. For historic  reasons,  this  mode  is  not  the\n         default  when  building  an executable or shared object.\n         However, its use is recommended to insure that the  text\n         segment  of  the dynamic object being built is shareable\n         between multiple running processes. A shared  text  seg-\n         ment  incurs  the  least relocation overhead when loaded\n         into memory.\n```\n\n\nAdding that to the linker flags avoids the issue:\n\n\n```\n(sage subshell) t2:src kirkby$ make\ngcc -m64  -DENABLE_LONG_OPTIONS -o cl.o -c cl.c\ngcc -m64    -c -o cliquer.o cliquer.c\ngcc -m64    -c -o graph.o graph.c\ngcc -m64    -c -o reorder.o reorder.c\ngcc -m64   -Wl,-ztext -o libcliquer.so cl.o cliquer.o graph.o reorder.o\nSAGE_ROOT=/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha2\n(sage subshell) t2:src kirkby$ elfdump -d libcliquer.so | grep TEXTRE\nSAGE_ROOT=/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha2\n```\n\n\nHowever, I have **not** checked if this produces a usable shared library or not. (Note, it is OK to use `-ztext` rather than `-z text`. It stops one having to put quotes around things and is perfectly acceptable to the Sun linker and in fact Sun tools in general. \n\nThis **could** be the magic option needed to sort out R and ECL, both of which suffer this problem. \n\nDave",
    "created_at": "2010-09-13T23:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97373",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It looks like we need `-z text` to be passed to the linker. From the linker man page:


```
    -z text

         In dynamic mode only, forces a fatal error if any  relo-
         cations   against   non-writable,  allocatable  sections
         remain. For historic  reasons,  this  mode  is  not  the
         default  when  building  an executable or shared object.
         However, its use is recommended to insure that the  text
         segment  of  the dynamic object being built is shareable
         between multiple running processes. A shared  text  seg-
         ment  incurs  the  least relocation overhead when loaded
         into memory.
```


Adding that to the linker flags avoids the issue:


```
(sage subshell) t2:src kirkby$ make
gcc -m64  -DENABLE_LONG_OPTIONS -o cl.o -c cl.c
gcc -m64    -c -o cliquer.o cliquer.c
gcc -m64    -c -o graph.o graph.c
gcc -m64    -c -o reorder.o reorder.c
gcc -m64   -Wl,-ztext -o libcliquer.so cl.o cliquer.o graph.o reorder.o
SAGE_ROOT=/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha2
(sage subshell) t2:src kirkby$ elfdump -d libcliquer.so | grep TEXTRE
SAGE_ROOT=/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha2
```


However, I have **not** checked if this produces a usable shared library or not. (Note, it is OK to use `-ztext` rather than `-z text`. It stops one having to put quotes around things and is perfectly acceptable to the Sun linker and in fact Sun tools in general. 

This **could** be the magic option needed to sort out R and ECL, both of which suffer this problem. 

Dave



---

archive/issue_comments_097374.json:
```json
{
    "body": "I take that back. The options above only create an executable - not a shared library! \n\nOh well, I am sure this can be solved.",
    "created_at": "2010-09-13T23:24:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97374",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I take that back. The options above only create an executable - not a shared library! 

Oh well, I am sure this can be solved.



---

archive/issue_comments_097375.json:
```json
{
    "body": "I meant `SAGESOFLAGS=\"-shared -Wl,-h,libcliquer.so\"` (for SunOS/Oraclis).\n\nOmitting the `-shared` still produces an executable.",
    "created_at": "2010-09-14T07:30:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97375",
    "user": "https://github.com/nexttime"
}
```

I meant `SAGESOFLAGS="-shared -Wl,-h,libcliquer.so"` (for SunOS/Oraclis).

Omitting the `-shared` still produces an executable.



---

archive/issue_comments_097376.json:
```json
{
    "body": "I've had a look at the source code for cliquer - it clearly is not upstream source as Leif noticed. \n\nAlso, the Sage-specific coding is very dubious - endless calls to `malloc` without bothering to check if the allocation failed or not. I had this distant memory when I learned C that one was supposed to check if calls to `malloc` failed, but perhaps dementia has set in and I'm mistaken. Either that, or the programmer is demented. \n\nAdding `-ztext` with the Sun linker stops the build when there are text relocations against read only segments, so it makes testing a bit easier, as one does not need to actually run `elfdump` on the library. \n\nDave",
    "created_at": "2010-09-14T09:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97376",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've had a look at the source code for cliquer - it clearly is not upstream source as Leif noticed. 

Also, the Sage-specific coding is very dubious - endless calls to `malloc` without bothering to check if the allocation failed or not. I had this distant memory when I learned C that one was supposed to check if calls to `malloc` failed, but perhaps dementia has set in and I'm mistaken. Either that, or the programmer is demented. 

Adding `-ztext` with the Sun linker stops the build when there are text relocations against read only segments, so it makes testing a bit easier, as one does not need to actually run `elfdump` on the library. 

Dave



---

archive/issue_comments_097377.json:
```json
{
    "body": "The problem John ran into was just the (old) Sun linker not understanding `-soname`; the GNU linker and (I think) newer versions of the Sun linker understand both `-h` and `-soname`, so setting `SAGESOFLAGS` to `\"-shared -Wl,-h,libcliquer.so\"` as mentioned earlier should work on SunOS regardless of the linker.",
    "created_at": "2010-09-14T12:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97377",
    "user": "https://github.com/nexttime"
}
```

The problem John ran into was just the (old) Sun linker not understanding `-soname`; the GNU linker and (I think) newer versions of the Sun linker understand both `-h` and `-soname`, so setting `SAGESOFLAGS` to `"-shared -Wl,-h,libcliquer.so"` as mentioned earlier should work on SunOS regardless of the linker.



---

archive/issue_comments_097378.json:
```json
{
    "body": "Replying to [comment:25 drkirkby]:\n\nBtw, I vaguely remember there was some counterpart of `malloc()` and friends..., wasn't there?",
    "created_at": "2010-09-14T13:03:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97378",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:25 drkirkby]:

Btw, I vaguely remember there was some counterpart of `malloc()` and friends..., wasn't there?



---

archive/issue_comments_097379.json:
```json
{
    "body": "Replying to [comment:26 leif]:\n> The problem John ran into was just the (old) Sun linker not understanding `-soname`; the GNU linker and (I think) newer versions of the Sun linker understand both `-h` and `-soname`, so setting `SAGESOFLAGS` to `\"-shared -Wl,-h,libcliquer.so\"` as mentioned earlier should work on SunOS regardless of the linker.\n\nI could have swore I tried that before, and found it still had text relocation issues, but it does in fact work! \n\nI've tested it on:\n\n* OpenSolaris on x86 hardware (32-bit)\n* Solaris 10 on SPARC 32-bit \n* Solaris 10 on SPARC 64-bit\n\nI've **not** yet checked it on \n\n* Solaris 10 (x86) 32-bit \n* Solaris 10 (x86) 64-bit\n* OpenSolaris (x86) 64-bit\n\nI added the linker options `Wl,-ztext` too, as that will cause the build to fail as soon as there are these problems. So the issue will be noticed immediately, before anyone runs elfdump. \n\nDo you want me to add you to the author list? It seems only fair since you came up with the fix, but you might not want to be associated with such poor code overall! \n\nI've updated the package at http://boxen.math.washington.edu/home/kirkby/patches/cliquer-1.2.p7.spkg\n\nbut have not committed the changes until I've more fully tested this, and know whether you want to be on the author list. \n\nDave",
    "created_at": "2010-09-14T14:36:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97379",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:26 leif]:
> The problem John ran into was just the (old) Sun linker not understanding `-soname`; the GNU linker and (I think) newer versions of the Sun linker understand both `-h` and `-soname`, so setting `SAGESOFLAGS` to `"-shared -Wl,-h,libcliquer.so"` as mentioned earlier should work on SunOS regardless of the linker.

I could have swore I tried that before, and found it still had text relocation issues, but it does in fact work! 

I've tested it on:

* OpenSolaris on x86 hardware (32-bit)
* Solaris 10 on SPARC 32-bit 
* Solaris 10 on SPARC 64-bit

I've **not** yet checked it on 

* Solaris 10 (x86) 32-bit 
* Solaris 10 (x86) 64-bit
* OpenSolaris (x86) 64-bit

I added the linker options `Wl,-ztext` too, as that will cause the build to fail as soon as there are these problems. So the issue will be noticed immediately, before anyone runs elfdump. 

Do you want me to add you to the author list? It seems only fair since you came up with the fix, but you might not want to be associated with such poor code overall! 

I've updated the package at http://boxen.math.washington.edu/home/kirkby/patches/cliquer-1.2.p7.spkg

but have not committed the changes until I've more fully tested this, and know whether you want to be on the author list. 

Dave



---

archive/issue_comments_097380.json:
```json
{
    "body": "Further test it and add a disclaimer... ;-)",
    "created_at": "2010-09-14T15:26:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97380",
    "user": "https://github.com/nexttime"
}
```

Further test it and add a disclaimer... ;-)



---

archive/issue_comments_097381.json:
```json
{
    "body": "It seems to build correctly on t2 (32-bit and 64-bit), mark (32-bit), and fulvia (32-bit and 64-bit).  The \"elfdump\" command produces no output on any of these systems.  I don't have a functioning 64-bit Sage build, but on the 32-bit systems, tests pass on the file `sage/graphs/cliquer.pyx`.  These are all good signs...",
    "created_at": "2010-09-14T16:56:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97381",
    "user": "https://github.com/jhpalmieri"
}
```

It seems to build correctly on t2 (32-bit and 64-bit), mark (32-bit), and fulvia (32-bit and 64-bit).  The "elfdump" command produces no output on any of these systems.  I don't have a functioning 64-bit Sage build, but on the 32-bit systems, tests pass on the file `sage/graphs/cliquer.pyx`.  These are all good signs...



---

archive/issue_comments_097382.json:
```json
{
    "body": "Replying to [comment:30 jhpalmieri]:\n> It seems to build correctly on t2 (32-bit and 64-bit), mark (32-bit), and fulvia (32-bit and 64-bit).  The \"elfdump\" command produces no output on any of these systems.  I don't have a functioning 64-bit Sage build, but on the 32-bit systems, tests pass on the file `sage/graphs/cliquer.pyx`.  These are all good signs...\n\nThank you John. I don't have a workable 64-bit build either, though I have managed to get something on t2 that sort of works. It's in \n\n\n```\n/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha1\n```\n\n\nWhilst it can do simple computations, it fails pretty soon. Even exiting causes a core dump. It's not even worth reporting the results of doctesting! \n\n\n```\nkirkby@t2:32 ~/t2/64/sage-4.5.3.alpha1$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: factor(4333333333333333333333333333333)\n1049 * 10477 * 68848139 * 5726871782749939\nsage: factorial(12)\n479001600\nsage: quit\nExiting Sage (CPU time 0m0.47s, Wall time 0m24.05s).\nExiting spawned Gap process.\n/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha1/local/bin/sage-sage: line 206:  6732 Segmentation Fault      (core dumped) sage-ipython \"$@\" -i\n```\n\n| Sage Version 4.5.3.alpha1, Release Date: 2010-08-14                |\n| Type notebook() for the GUI, and license() for information.        |\nOn OpenSolaris at least, it is even less stable, and crashes as soon as one tries to run `sage`. \n\n\nThank you for the testing, and test results. I'll do a bit more testing, then commit the changes. I'll Leif as an author, but with a disclaimer. Perhaps he would suggest what he wants written. \n\nDave",
    "created_at": "2010-09-14T18:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97382",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:30 jhpalmieri]:
> It seems to build correctly on t2 (32-bit and 64-bit), mark (32-bit), and fulvia (32-bit and 64-bit).  The "elfdump" command produces no output on any of these systems.  I don't have a functioning 64-bit Sage build, but on the 32-bit systems, tests pass on the file `sage/graphs/cliquer.pyx`.  These are all good signs...

Thank you John. I don't have a workable 64-bit build either, though I have managed to get something on t2 that sort of works. It's in 


```
/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha1
```


Whilst it can do simple computations, it fails pretty soon. Even exiting causes a core dump. It's not even worth reporting the results of doctesting! 


```
kirkby@t2:32 ~/t2/64/sage-4.5.3.alpha1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: factor(4333333333333333333333333333333)
1049 * 10477 * 68848139 * 5726871782749939
sage: factorial(12)
479001600
sage: quit
Exiting Sage (CPU time 0m0.47s, Wall time 0m24.05s).
Exiting spawned Gap process.
/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha1/local/bin/sage-sage: line 206:  6732 Segmentation Fault      (core dumped) sage-ipython "$@" -i
```

| Sage Version 4.5.3.alpha1, Release Date: 2010-08-14                |
| Type notebook() for the GUI, and license() for information.        |
On OpenSolaris at least, it is even less stable, and crashes as soon as one tries to run `sage`. 


Thank you for the testing, and test results. I'll do a bit more testing, then commit the changes. I'll Leif as an author, but with a disclaimer. Perhaps he would suggest what he wants written. 

Dave



---

archive/issue_comments_097383.json:
```json
{
    "body": "Dave, do not always take me that serious...",
    "created_at": "2010-09-14T19:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97383",
    "user": "https://github.com/nexttime"
}
```

Dave, do not always take me that serious...



---

archive/issue_comments_097384.json:
```json
{
    "body": "Replying to [comment:32 leif]:\n> Dave, do not always take me that serious...\n\nSorry I did. I'll just leave a reference to cleaning the package up on another ticket. Perhaps Nathann (the package maintainer) can help you with that. \n\nDave",
    "created_at": "2010-09-14T19:11:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97384",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:32 leif]:
> Dave, do not always take me that serious...

Sorry I did. I'll just leave a reference to cleaning the package up on another ticket. Perhaps Nathann (the package maintainer) can help you with that. 

Dave



---

archive/issue_comments_097385.json:
```json
{
    "body": "On 32-bit OpenSolaris this is passing tests, and having no text relocation issues:\n\n\n```\nsage: /export/home/drkirkby/sage-4.5.3/http://boxen.math.washington.edu/home/kirkby/patches/cliquer-1.2.p7.spkg is already installed\ndrkirkby@hawk:~/sage-4.5.3$ ./sage -t devel/sage/sage/graphs/cliquer.pyx\nsage -t  \"devel/sage/sage/graphs/cliquer.pyx\"               \n\t [5.2 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 5.2 seconds\ndrkirkby@hawk:~/sage-4.5.3$ elfdump -d local/lib/libcliquer.so | grep TEXTREL\n```\n\n\nOn 64-bit OpenSolaris there are no text relocation issues, though I'm not even going to bother doctesting, as Sage is too unstable. \n\nI think between John and I we now have. \n* 32-bit Solaris 10 on SPARC - builds with no text relocation problems and passes `devel/sage/sage/graphs/cliquer.pyx`. \n* 64-bit Solaris 10 on SPARC - build without test relocation problems. Not doctested, as there is no stable 64-bit Sage on any sort of Solaris. \n* 32-bit Solaris 10 on x86 - builds with no text relocation problems and  passes `devel/sage/sage/graphs/cliquer.pyx`. \n* 64-bit Solaris 10 on x86 - builds with no text relocation problems. Again not doctested. \n* 32-bit OpenSolaris on x86 - builds with no text relocation problems and passes `devel/sage/sage/graphs/cliquer.pyx`. \n* 64-bit OpenSolaris on x86 - builds with no text relocation problems. Again not doctested. \n\nThat covers any sort of \"Solaris\" system in common use. The only exception is OpenSolaris on SPARC, which is quite rare. \n\nSo I think this is ok now. I will update the package, commit the changes and mark it for review. \n\nDave",
    "created_at": "2010-09-14T20:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97385",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

On 32-bit OpenSolaris this is passing tests, and having no text relocation issues:


```
sage: /export/home/drkirkby/sage-4.5.3/http://boxen.math.washington.edu/home/kirkby/patches/cliquer-1.2.p7.spkg is already installed
drkirkby@hawk:~/sage-4.5.3$ ./sage -t devel/sage/sage/graphs/cliquer.pyx
sage -t  "devel/sage/sage/graphs/cliquer.pyx"               
	 [5.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 5.2 seconds
drkirkby@hawk:~/sage-4.5.3$ elfdump -d local/lib/libcliquer.so | grep TEXTREL
```


On 64-bit OpenSolaris there are no text relocation issues, though I'm not even going to bother doctesting, as Sage is too unstable. 

I think between John and I we now have. 
* 32-bit Solaris 10 on SPARC - builds with no text relocation problems and passes `devel/sage/sage/graphs/cliquer.pyx`. 
* 64-bit Solaris 10 on SPARC - build without test relocation problems. Not doctested, as there is no stable 64-bit Sage on any sort of Solaris. 
* 32-bit Solaris 10 on x86 - builds with no text relocation problems and  passes `devel/sage/sage/graphs/cliquer.pyx`. 
* 64-bit Solaris 10 on x86 - builds with no text relocation problems. Again not doctested. 
* 32-bit OpenSolaris on x86 - builds with no text relocation problems and passes `devel/sage/sage/graphs/cliquer.pyx`. 
* 64-bit OpenSolaris on x86 - builds with no text relocation problems. Again not doctested. 

That covers any sort of "Solaris" system in common use. The only exception is OpenSolaris on SPARC, which is quite rare. 

So I think this is ok now. I will update the package, commit the changes and mark it for review. 

Dave



---

archive/issue_comments_097386.json:
```json
{
    "body": "This is now ready for review - the package, complete with all changes committed to the repository can be found at\n\n http://boxen.math.washington.edu/home/kirkby/patches/cliquer-1.2.p7.spkg\n\nDave",
    "created_at": "2010-09-14T20:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97386",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This is now ready for review - the package, complete with all changes committed to the repository can be found at

 http://boxen.math.washington.edu/home/kirkby/patches/cliquer-1.2.p7.spkg

Dave



---

archive/issue_comments_097387.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-14T20:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97387",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_097388.json:
```json
{
    "body": "Only one typo! (`s/ztest/ztext/` in `SPKG.txt`) But never mind...\n\nThe GNU linker doesn't know `-ztext`, but bravely ignores it for Solaris compatibility.",
    "created_at": "2010-09-14T21:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97388",
    "user": "https://github.com/nexttime"
}
```

Only one typo! (`s/ztest/ztext/` in `SPKG.txt`) But never mind...

The GNU linker doesn't know `-ztext`, but bravely ignores it for Solaris compatibility.



---

archive/issue_comments_097389.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-14T21:13:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97389",
    "user": "https://github.com/nexttime"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097390.json:
```json
{
    "body": "John, revert this again in case you encounter new errors... ;-)",
    "created_at": "2010-09-14T21:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97390",
    "user": "https://github.com/nexttime"
}
```

John, revert this again in case you encounter new errors... ;-)



---

archive/issue_events_024866.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-16T00:49:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9870#event-24866"
}
```



---

archive/issue_comments_097391.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-16T00:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97391",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_097392.json:
```json
{
    "body": "Leif should have been on here as an author too - though the SPKG.txt says it anyway. \n\nThanks for your help Leif. \n\nDave",
    "created_at": "2010-09-16T22:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9870#issuecomment-97392",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Leif should have been on here as an author too - though the SPKG.txt says it anyway. 

Thanks for your help Leif. 

Dave
