# Issue 9870: Update Cliquer to 1.21 and get the library buiilding properly on Solaris.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-09-07 22:05:09

Assignee: GeorgSWeber

CC:  ncohen mpatel jhpalmieri

As documented at #9833, the Cliquer library is causing problems on 64-bit Solaris and 64-bit OpenSolaris. This needs *urgently* resolving, as it is the first problem hit when building a 64-bit version of Sage on Solaris or OpenSolaris. 

As documented at #9521, the test suite for Cliquer is not run correctly. It should generally be run from `spkg-install`, but given it takes only a few seconds to run on even slow hardware, it makes sense to run the tests each time Sage is built. 

The upstream source code has modifications too. Given the latest version is a bug-fix only release, it is wise to update this. (Rather confusingly, the version currently in Sage is 1.2, but the bug-fix release is 1.21. I believe the authors should have called it 1.2.1) See http://users.tkk.fi/pat/cliquer.html

*There are a number of other issues with Cliquer's spkg-install and Makefile. These are the subject of ticket #9870 and will NOT be addressed here to save time, and allow the critical Solaris fix to be integrated as soon as possible.*

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


---

Comment by drkirkby created at 2010-09-07 22:36:24

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-09-07 23:25:15

I just realised Cliquer was updated to `cliquer-1.2.p6` - I should have remembered this, as I reviewed it!!

I need to change this, to take into account the changes at `cliquer-1.2.p6`. I'm setting to "needs work" for now. It will not take long to resolve.

Dave


---

Comment by drkirkby created at 2010-09-07 23:25:15

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-09-08 00:23:49

Changing status from needs_work to needs_review.


---

Attachment

Mercurial patch. Note, the patched Makefile was not under revision control before, so the patch is quite big.


---

Comment by drkirkby created at 2010-09-08 02:26:55

Note, since the old Makefile was not under revision control, the patches look a *LOT* bigger than they actually are. If we compare the old Makefile and the new Makefile, the change is only that two characters "./" are added in front of the executable `testcases`. 


```
drkirkby`@`hawk:~/sage-4.5.3/spkg/standard$ diff -u cliquer-1.2.p6/patch/Makefile cliquer-1.21/patches/Makefile
--- cliquer-1.2.p6/patch/Makefile	Tue Feb 16 04:26:55 2010
+++ cliquer-1.21/patches/Makefile	Wed Sep  8 02:42:06 2010
`@``@` -66,4 +66,4 `@``@`
 	cp * "`date "+backup-%Y-%m-%d-%H-%M"`"  2>/dev/null || true
 
 test: testcases
-	testcases
+	./testcases
```


So when reviewing this, be aware most of the changes that are seen in the attached patch are simply a result of the old files not being under revision control, and the `patch` directory was in the `.hgignore` file. 

With the change in the compiler options, there are no text relocations which were seen on #9833. Now, using `elfdump`, no such problems are observed. 


```
drkirkby`@`hawk:~/sage-4.5.3$ elfdump -d local/lib/libcliquer.so | grep TEXTREL
drkirkby`@`hawk:~/sage-4.5.3$ 
```


This means the library will be more reliable - see #9833 for a discussion of why we need to avoid this. 



Dave


---

Comment by leif created at 2010-09-08 20:50:13

See #9833 for at least two reasons.

Note that

```sh
    make something | tee output_file
```

will *almost always* have a zero exit status, namely unless `tee` fails (or you use `bash`'s `set -o pipefail` feature). In fact `make test`, i.e. `src/testcases`, won't exit with a non-zero exit status in _all_ cases (but at least _some_); I would change that and post the fix upstream (changing some functions from `void` to return an `int`, accumulating the number of failures and returning that at the end of `main()`).   

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

Comment by leif created at 2010-09-08 20:50:13

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-09-08 20:59:32

> Note that

```
    make something | tee output_file
```

> will almost always have a zero exit status

The comment in the file suggests that "make test" itself will have a zero exit status even if there are failures, and this is why the "tee ..." is there at all.  (This indicates problems with the makefile, I suppose.)  But I may be misunderstanding the situation.  We could also use the "pipestatus" script...


---

Comment by drkirkby created at 2010-09-08 21:46:03

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

Comment by leif created at 2010-09-08 22:46:01

Replying to [comment:7 jhpalmieri]:
> > Note that

```
    make something | tee output_file
```

> > will almost always have a zero exit status
> 
> The comment in the file suggests that "make test" itself will have a zero exit status even if there are failures, and this is why the "tee ..." is there at all.

It *does* return 1 on *some* errors, but not all. (And I suggested to modify `testcases.c` to return a non-zero value _on all errors_. This is almost trivial.) 

> (This indicates problems with the makefile, I suppose.)  But I may be misunderstanding the situation.

The Makefile does not cause problems; just the comment is not (fully) correct.

> We could also use the "pipestatus" script...

The correct way would be to redirect the output in the `make` rule itself (with `> test.out`), or - if you want to see the test running live - not redirect it at all. Of course you can also write it to a file and use `tail [-f]`; the written file will usually be deleted after the spkg is installed (and tested) anyhow, unless you use `sage-spkg -i -s ...`. So I'd prefer changing the source code and let `testcases` just write to `stdout` and `stderr`, s.t. the test output ends up in `spkg/logs/*.log`, as usual.


---

Comment by drkirkby created at 2010-09-09 00:04:12

Leif, 

Different people have different ways of doing things. Much is personal style. We have numerous examples of that on #9603, where each of us will do something in a different way. 

Can you tell me what is wrong with the current method? I can't see anything particularly wrong with what I have. I want to get a patch into Sage asap that will allow the library to build on 64-bit Solaris. 

I will report the issue of the source code to the upstream developers. You can add further suggestions to #9870 if you want. But as far as I can see, this achieves the aim. It is an improvement on what we had before and allows us to make progress with the Solaris 64-bit port. I do not want to go around editing the source code, when a couple of lines in a script does the job. If you look in detail at the source code, you will find it is rather strange anyway. I simply do not want to get involved in editing that. 

I created #9870 to address other issues

Dave


---

Comment by leif created at 2010-09-09 04:48:06

Replying to [comment:8 drkirkby]:
>  * There's no need for this to be a .p0 or .p1. It is a new upstream source code (version 1.21), so the patch level in Sage is removed.

This seems to be an endless discussion. I'd prefer having _always_ a patch level, be it `.p0` for unpatched upstream code. But here we actually (still) do patch a fresh upstream release, so it should IMHO be `.p1` (or `.p0` for those who think the _first unpatched new release_ should _not_ have a patch level extension).

>  * It is `make test` which exits with 0, even when I alter the file `src/testcases.c` to force tests to fail.

When `testcases` returns 1, so does `make test` (or `$MAKE test`); see above.
 
>  * `make test` actually creates a binary called `testcases` and then executes that. That exits with 0 in all cases.

Not really, though not really relevant if it doesn't in _all_ error cases. But

```
make test | tee test.out
if [ $? -ne 0 ]; then
    echo "Failed to compile test cases of cliquer... exiting"
    exit 1
fi
```

does not even catch the cases in which it _does_ return 1, nor errors _compiling_ the test program - which is perhaps even worse, since

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


Also, running the test suite just in `spkg-install` is IMHO a bad idea; that disturbs upcoming improvements to `sage-spkg` wrt. `SAGE_CHECK`, since we don't want the [whole] _build_ to fail (or stop) just because _some_ package failed to pass its tests; cf. the Python package. And we won't be able to log test results separately.

>  * I agree this is an upstream bug in the test code - it should exit with a non-zero code in the case of errors.

>  * I'm not trying to test the exit code of `tee`, but rather `grep`.

See above. (You do both, or actually currently only the former.)
 
>  * I thought `grep -q` was not portable, but it was `cmp -q` which caused a portability issue. So I'll change that.

I think there are still but very rarely dumb `grep`s around that don't understand `-q`, in which case one can omit the `-q` and redirect `stdout` to `/dev/null`; this anyway doesn't affect `grep`'s exit status. (But we should IMHO ignore that and use `-q`. POSIX isn't of the 1970s either.)
  
>  * I take Leif's point about the fact that there should be no main in a shared library. But the code works with the compiler options `-shared -Wl,-h,libcliquer.so` on Linux and OS X, even though Leif says there's a main there. I do not want to start re-writing the source code or Makefile to remove main(). That's an upstream problem.

The original code was - sorry - messed up by some _Sage_ developer. (I already mentioned `src/` was _not_ vanilla.)

> If it was the only way to fix the text relocations, then I would do it. But simply using the same compiler options as on other platforms works.

Ok, (in my opinion) a work-around, but doesn't remove the real cause, namely bad adaption / conversion of a program to a library.

The "bad" flags btw. originate from Sage, too - not upstream.

> I've created #9870 to address the other issues. I agree there are many, but I don't want this ticket drag on like #9603.

Created six weeks ago, starting with a minor issue. Now we won't have to touch that for a long time I think, since all currently desirable changes are made - on _one_ ticket, by creating _one_ new spkg. (The situation with blockers is a bit different.)

But regarding the previous Cliquer tickets (which weren't quick ones either), `SPKG.txt` still fails to spell the algorithm's developer's name correctly. 

I've taken over _that_ ticket (#9870). If this ticket here quickly gets positively reviewed, I can make the remaining changes, based on it. Changing `testcases.c` is rather independent of that, but not the rest.


---

Comment by drkirkby created at 2010-09-13 21:05:13

Replying to [comment:11 leif]:
 
> I've taken over _that_ ticket (#9870). If this ticket here quickly gets positively reviewed, I can make the remaining changes, based on it. Changing `testcases.c` is rather independent of that, but not the rest.

Leif, 
since you have taken on #9870, I think it's sensible if I restrict this ticket to *only* changing the compiler flags on Solaris, to allow this to build properly on Solaris without the text relocations. It's pointless me making other changes, which you are going to change anyway. 

I've written code to enable the tests, but you intend changing the source code. As such I am going to make only a dozen or so bytes of changes. 

Dave


---

Comment by drkirkby created at 2010-09-13 21:11:32

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2010-09-13 21:11:32

I'm marking for needing review. This just changes the compiler flags for Solaris. Now the library has no issues:


```
drkirkby`@`hawk:~/sage-4.6.alpha0/local/lib$ elfdump -d libcliquer.so | grep TEXTREL
drkirkby`@`hawk:~/sage-4.6.alpha0/local/lib$ 
```


This constrasts with one of the libraries that does still have this problem, which is ECL


```
drkirkby`@`hawk:~/sage-4.6.alpha0/local/lib$ elfdump -d libecl*.so | grep TEXTREL
      [24]  TEXTREL           0                   
      [33]  FLAGS             0x4                 [ TEXTREL ]
drkirkby`@`hawk:~/sage-4.6.alpha0/local/lib$ 
```


The changes to the complier flags avoid this problem. 

Dave


---

Attachment

Simple patch which *replaces* the earlier patch.


---

Comment by leif created at 2010-09-13 21:34:54

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-09-13 21:34:54

Then put a comment at #9833 (where I would have expected this fix) that it can be closed as a duplicate as soon as this ticket gets merged.

Reporting this upstream is IMHO inappropriate, since _Sage_ messed up the build.


---

Comment by jhpalmieri created at 2010-09-13 21:46:17

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

Comment by jhpalmieri created at 2010-09-13 21:46:17

Changing status from positive_review to needs_work.


---

Comment by drkirkby created at 2010-09-13 22:04:57

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

Comment by jhpalmieri created at 2010-09-13 22:12:37

I get the same error in 64-bit mode on t2.  You can look at my logs on t2 in /scratch/palmieri/sage-4.5.3.rc0/spkg/logs and also /scratch/palmieri/64bit/sage-4.6.alpha0/spkg/logs.


---

Comment by leif created at 2010-09-13 22:20:16

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

Comment by drkirkby created at 2010-09-13 22:34:09

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

Comment by drkirkby created at 2010-09-13 22:52:57

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

Comment by drkirkby created at 2010-09-13 23:16:02

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


However, I have *not* checked if this produces a usable shared library or not. (Note, it is OK to use `-ztext` rather than `-z text`. It stops one having to put quotes around things and is perfectly acceptable to the Sun linker and in fact Sun tools in general. 

This *could* be the magic option needed to sort out R and ECL, both of which suffer this problem. 

Dave


---

Comment by drkirkby created at 2010-09-13 23:24:20

I take that back. The options above only create an executable - not a shared library! 

Oh well, I am sure this can be solved.


---

Comment by leif created at 2010-09-14 07:30:07

I meant `SAGESOFLAGS="-shared -Wl,-h,libcliquer.so"` (for SunOS/Oraclis).

Omitting the `-shared` still produces an executable.


---

Comment by drkirkby created at 2010-09-14 09:53:33

I've had a look at the source code for cliquer - it clearly is not upstream source as Leif noticed. 

Also, the Sage-specific coding is very dubious - endless calls to `malloc` without bothering to check if the allocation failed or not. I had this distant memory when I learned C that one was supposed to check if calls to `malloc` failed, but perhaps dementia has set in and I'm mistaken. Either that, or the programmer is demented. 

Adding `-ztext` with the Sun linker stops the build when there are text relocations against read only segments, so it makes testing a bit easier, as one does not need to actually run `elfdump` on the library. 

Dave


---

Comment by leif created at 2010-09-14 12:20:03

The problem John ran into was just the (old) Sun linker not understanding `-soname`; the GNU linker and (I think) newer versions of the Sun linker understand both `-h` and `-soname`, so setting `SAGESOFLAGS` to `"-shared -Wl,-h,libcliquer.so"` as mentioned earlier should work on SunOS regardless of the linker.


---

Comment by leif created at 2010-09-14 13:03:44

Replying to [comment:25 drkirkby]:

Btw, I vaguely remember there was some counterpart of `malloc()` and friends..., wasn't there?


---

Comment by drkirkby created at 2010-09-14 14:36:26

Replying to [comment:26 leif]:
> The problem John ran into was just the (old) Sun linker not understanding `-soname`; the GNU linker and (I think) newer versions of the Sun linker understand both `-h` and `-soname`, so setting `SAGESOFLAGS` to `"-shared -Wl,-h,libcliquer.so"` as mentioned earlier should work on SunOS regardless of the linker.

I could have swore I tried that before, and found it still had text relocation issues, but it does in fact work! 

I've tested it on:

 * OpenSolaris on x86 hardware (32-bit)
 * Solaris 10 on SPARC 32-bit 
 * Solaris 10 on SPARC 64-bit

I've *not* yet checked it on 

 * Solaris 10 (x86) 32-bit 
 * Solaris 10 (x86) 64-bit
 * OpenSolaris (x86) 64-bit

I added the linker options `Wl,-ztext` too, as that will cause the build to fail as soon as there are these problems. So the issue will be noticed immediately, before anyone runs elfdump. 

Do you want me to add you to the author list? It seems only fair since you came up with the fix, but you might not want to be associated with such poor code overall! 

I've updated the package at http://boxen.math.washington.edu/home/kirkby/patches/cliquer-1.2.p7.spkg

but have not committed the changes until I've more fully tested this, and know whether you want to be on the author list. 

Dave


---

Comment by leif created at 2010-09-14 15:26:06

Further test it and add a disclaimer... ;-)


---

Comment by jhpalmieri created at 2010-09-14 16:56:55

It seems to build correctly on t2 (32-bit and 64-bit), mark (32-bit), and fulvia (32-bit and 64-bit).  The "elfdump" command produces no output on any of these systems.  I don't have a functioning 64-bit Sage build, but on the 32-bit systems, tests pass on the file `sage/graphs/cliquer.pyx`.  These are all good signs...


---

Comment by drkirkby created at 2010-09-14 18:42:41

Replying to [comment:30 jhpalmieri]:
> It seems to build correctly on t2 (32-bit and 64-bit), mark (32-bit), and fulvia (32-bit and 64-bit).  The "elfdump" command produces no output on any of these systems.  I don't have a functioning 64-bit Sage build, but on the 32-bit systems, tests pass on the file `sage/graphs/cliquer.pyx`.  These are all good signs...

Thank you John. I don't have a workable 64-bit build either, though I have managed to get something on t2 that sort of works. It's in 


```
/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha1
```


Whilst it can do simple computations, it fails pretty soon. Even exiting causes a core dump. It's not even worth reporting the results of doctesting! 


```
kirkby`@`t2:32 ~/t2/64/sage-4.5.3.alpha1$ ./sage
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
/rootpool2/local/kirkby/t2/64/sage-4.5.3.alpha1/local/bin/sage-sage: line 206:  6732 Segmentation Fault      (core dumped) sage-ipython "$`@`" -i
```

| Sage Version 4.5.3.alpha1, Release Date: 2010-08-14                |
| Type notebook() for the GUI, and license() for information.        |
On OpenSolaris at least, it is even less stable, and crashes as soon as one tries to run `sage`. 


Thank you for the testing, and test results. I'll do a bit more testing, then commit the changes. I'll Leif as an author, but with a disclaimer. Perhaps he would suggest what he wants written. 

Dave


---

Comment by leif created at 2010-09-14 19:01:04

Dave, do not always take me that serious...


---

Comment by drkirkby created at 2010-09-14 19:11:09

Replying to [comment:32 leif]:
> Dave, do not always take me that serious...

Sorry I did. I'll just leave a reference to cleaning the package up on another ticket. Perhaps Nathann (the package maintainer) can help you with that. 

Dave


---

Comment by drkirkby created at 2010-09-14 20:21:11

On 32-bit OpenSolaris this is passing tests, and having no text relocation issues:


```
sage: /export/home/drkirkby/sage-4.5.3/http://boxen.math.washington.edu/home/kirkby/patches/cliquer-1.2.p7.spkg is already installed
drkirkby`@`hawk:~/sage-4.5.3$ ./sage -t devel/sage/sage/graphs/cliquer.pyx
sage -t  "devel/sage/sage/graphs/cliquer.pyx"               
	 [5.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 5.2 seconds
drkirkby`@`hawk:~/sage-4.5.3$ elfdump -d local/lib/libcliquer.so | grep TEXTREL
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

Comment by drkirkby created at 2010-09-14 20:52:19

This is now ready for review - the package, complete with all changes committed to the repository can be found at

 http://boxen.math.washington.edu/home/kirkby/patches/cliquer-1.2.p7.spkg

Dave


---

Comment by drkirkby created at 2010-09-14 20:52:19

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-09-14 21:13:56

Only one typo! (`s/ztest/ztext/` in `SPKG.txt`) But never mind...

The GNU linker doesn't know `-ztext`, but bravely ignores it for Solaris compatibility.


---

Comment by leif created at 2010-09-14 21:13:56

Changing status from needs_review to positive_review.


---

Comment by leif created at 2010-09-14 21:15:08

John, revert this again in case you encounter new errors... ;-)


---

Comment by mpatel created at 2010-09-16 00:49:42

Resolution: fixed


---

Comment by drkirkby created at 2010-09-16 22:36:46

Leif should have been on here as an author too - though the SPKG.txt says it anyway. 

Thanks for your help Leif. 

Dave
