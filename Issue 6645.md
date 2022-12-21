# Issue 6645: make sure bdist of sage-4.1.1 works before release

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-07-28 03:01:36

Assignee: tbd

CC:  mhansen


```
Hi,

I took the sage-4.1.1.alpha1 release build I had, then did "./sage -bdist", took the result, extracted it, and did "make test". 

 1) It sits there and builds the documentation again, which takes a *long* time.  It shouldn't do this for a binary.

 2) Worse, every single test failed, with errors like this:

sage -t  "/home/wstein/build/sage-4.1.1.alpha1/dist/sage-4.1.1.alpha1-x86_64-Linux/devel/sage/doc/common/buil
der.py"
  File "./builder.py", line 18
    from /home/wstein/build/sage-4.1.1.alpha1/dist/sage-4.1.1.alpha1-x86_64-Linux/devel/sage/doc/common/build
er import *
         ^

  3) I tried do "./sage" to run Sage, then typed "make test" again about 10 minutes ago.  For some reason, the docs are building again... and I expect the same behavior as above after that finally finishes.

Buiding Sage, doing "./sage -bdist", then extracting the result and having "make test" 100% is a blocker for making the sage-4.1.1 release.

William
```



---

Comment by mpatel created at 2009-07-28 10:40:22

It appears that the doc rebuild is a consequence of

```
#Build the documentation
rm -rf "$SAGE_ROOT"/devel/sage-main/doc/output/doctrees
rm -rf "$SAGE_ROOT"/devel/sage-main/doc/en/reference/sage/*
"$SAGE_ROOT"/sage -docbuild --jsmath all html
```

at the end of `spkg/install`.  Perhaps we should recast this as a `make` target?  I think this is a problem in a source distribution, too.

But if I comment out these lines, then run `make test` in the binary distribution's root directory, the tests *still* fail...


---

Comment by mpatel created at 2009-07-28 13:07:53

Apply to scripts repository.


---

Attachment

On the failed tests:  The attached patch may help.  [os.path.realpath()](http://docs.python.org/library/os.path.html#os.path.realpath) expands all symbolic links.

Should `sage-bdist` set `SAGE_ROOT="....."` in `SAGE_ROOT/sage`?  *Lots* of tests fail, if `SAGE_ROOT` points to the original source distribution, at least for me.

On rebuilding the docs:  Is it enough to remove just the `rm -rf` lines?


---

Comment by mvngu created at 2009-08-05 15:18:40

The idea is that a binary version shouldn't rebuild the documentation when you issue the command

```
make test
```

in the Sage root directory. But with the patch, this still happens. I may be wrong, but here are the steps I followed:
 1. Take a binary version of Sage 4.1.1.rc1.
 1. Apply the patch `trac_6645-scripts_doctest.patch` and commit all changes.
 1. Create another binary version from that binary version.
 1. Extract the new binary version.
 1. Navigate to `SAGE_ROOT` of the new binary version. Do `./sage`, exit Sage, and then do `./sage -br main` and exit Sage again.
 1. Run the command `make test`
And the documentation is rebuilt regardless of whether or not I first build the HTML version of the documentation.


---

Comment by mpatel created at 2009-08-05 15:36:03

I'm not even sure that the patch still works for the failed tests.

It should not work for the doc-rebuild problem.  As far as I can tell, `SAGE_ROOT/spkg/install` is not under version control, but this is what I have in mind:

```
--- install.orig        2009-08-05 08:28:30.099076846 -0700
+++ install     2009-08-05 07:35:39.097918589 -0700
`@``@` -373,8 +373,8 `@``@` if [ $? -ne 0 ]; then
 fi
 
 #Build the documentation
-rm -rf "$SAGE_ROOT"/devel/sage-main/doc/output/doctrees
-rm -rf "$SAGE_ROOT"/devel/sage-main/doc/en/reference/sage/*
+#rm -rf "$SAGE_ROOT"/devel/sage-main/doc/output/doctrees
+#rm -rf "$SAGE_ROOT"/devel/sage-main/doc/en/reference/sage/*
 "$SAGE_ROOT"/sage -docbuild --jsmath all html
 
 if [ "$1" = "all" -a $? = 0 ]; then
```



---

Comment by mpatel created at 2009-08-07 22:57:15

Non-Mercurial patch for SAGE_ROOT/spkg/install


---

Attachment

To apply the new *non-Mercurial* patch, save it to `SAGE_ROOT/spkg`.  In that directory, run `patch < trac_6645-spkg_install.patch`.

Both patches together appear to solve the problems described in this ticket's description, at least for me.  But let me know, if they're not enough.

Why were the `rm -rf` lines first added to `spkg/install`?


---

Comment by jhpalmieri created at 2009-08-07 23:32:59

Replying to [comment:5 mpatel]:

> Why were the `rm -rf` lines first added to `spkg/install`?

I think Mike Hansen had a reason for it, but I don't remember what it was.  I'll cc him on the ticket, on the off-chance he can look at it.


---

Comment by mvngu created at 2009-08-08 13:32:47

Here are the steps I went through to test the proposed solution:
 1. Take the source tarball of Sage 4.1.1.rc2 and compile that version.
 1. Once the compilation has finished, build the HTML version of the documentation with
 {{{
./sage -docbuild all html
 }}}
 1. Apply the patch `trac_6645-scripts_doctest.patch` to the script repository in `SAGE_ROOT/local/bin`.
 1. Manually patch the file `SAGE_ROOT/spkg/install` with the patch `trac_6645-spkg_install.patch`.
 1. Make an experimental source distribution and call it, say, sage-4.1.1-exp using the command
 {{{
./sage -sdist 4.1.1-exp
 }}}
 The new experimental source distribution can be found in `SAGE_ROOT/dist`.
 1. Uncompress the tarball of that source distribution and compile it.
 1. Once the compilation has finished, build the HTML version of the documentation using `./sage -docbuild all html`.
 1. Make a binary distribution of the newly compiled experimental source distribution, with the command
 {{{
./sage -bdist 4.1.1-exp
 }}}
 The binary version can be found in `SAGE_ROOT/dist`.
 1. Uncompress the binary tarball and run the binary version. Then exit Sage and run Sage again with
 {{{
./sage -br main
 }}}
 Quit Sage again, and now do
 {{{
make test
 }}}
 Notice that the documentation wouldn't rebuild when running the test suite with the latter command.
 1. Here comes a show-stopper: Wait for the test suite to finish or just preempt it with control-C. Manually rebuild the documentation with `./sage -docbuild all html`. Once the HTML version of the documentation has finished building, now run the test suite again with `make test`. This time, running the test suite would also rebuild the documentation.
 1. Wait for the documentation to finish rebuilding so that the test suite would proceed. When the test suite starts running, you can let it finish or again you can preempt it with control-C. If you run the test suite a third time with `make test`, the documentation won't rebuild this time; the rebuild of the documentation would be skipped over and the test suite would proceed. 
 1. But if you manually rebuild the documentation again with `./sage -docbuild all html`, then the HTML version of the documentation would be rebuilt as requested. This is interesting because we have already manually rebuilt the HTML version of the documentation.


The upshot is that manually rebuilding the HTML version of the documentation would also cause the documentation to be rebuilt when running the test suite with `make test`. But if you run the test suite with the latter command, then requesting a manual build of the documentation would be done as requested, regardless of whether or not the documentation has been built.


---

Comment by mpatel created at 2009-08-08 21:27:16

Could [some of] this have happened because `spkg/install` builds the documentation with `--jsmath`?  I don't know if Sphinx 0.5.2 reliably determines whether to rebuild, based on command-line options, template differences, source changes, etc.


---

Comment by mpatel created at 2009-08-08 21:43:38

Or Sphinx 0.5.1.  What if the _all_ build commands, explicit or implicit, include (or exclude) `--jsmath`?

Do the binary distributions generally include documentation built with `pngmath`, only because the `jsmath` builds do not properly render some pages?  If so, #6673 may help (in the future).


---

Comment by mpatel created at 2009-08-08 23:07:58

I did some testing with [this binary](http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.rc2-sage.math.washington.edu-x86_64-Linux.tar.gz). I

 * Applied the patches above.
 * Applied #6187's "testreference" patch.
 * Edited `spkg/install` to build just the HTML version of the `testreference` target, _without_ `--jsmath`.
 * `make`, `make test`, `./sage -docbuild testreference html`, in various permutations.
 * `./sage -bdist 101`
 * `cd dist/; mkdir foo; cd foo; tar zxvf ../sage-101.tar.gz; cd sage-101` (or equivalent)
 * `make`, `make test`, `./sage -docbuild testreference html`, in various permutations.

In this scenario, the docbuild operator, whether it's invoked explicitly or implicitly, appears to be idempotent.  I noticed the same behavior with consistent use of `--jsmath`.


---

Comment by mvngu created at 2009-08-09 16:57:04

Here's another test which offers some hope: 

 1. I took the source tarball of [sage-4.1.1.rc2](http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.rc2.tar), compiled it and built the documentation both in HTML and PDF formats with:
 {{{
./sage -docbuild all html
./sage -docbuild all pdf
 }}}
 1. Applied the patch `trac_6645-scripts_doctest.patch` to the scripts repository in `SAGE_ROOT/local/bin`. Manually edited the file `SAGE_ROOT/spkg/install` so it now reads
 {{{
#Build the documentation
#rm -rf "$SAGE_ROOT"/devel/sage-main/doc/output/doctrees
#rm -rf "$SAGE_ROOT"/devel/sage-main/doc/en/reference/sage/*
#"$SAGE_ROOT"/sage -docbuild --jsmath all html
"$SAGE_ROOT"/sage -docbuild all html
 }}}
 1. Made an experimental source distribution of the patched `sage-4.1.1.rc2`, calling it say `sage-4.1.1.rc2-6645`.
 1. Unpacked the experimental source distribution `sage-4.1.1.rc2-6645` and compiled it.
 1. Made a binary version from the compiled source.
 1. Unpacked the binary tarball. Issued `make`, `make test`, and `./sage -docbuild all html` in various permutations. In this case, the documentation didn't rebuild.
 1. Ran the command `./sage -docbuild --jsmath all html` and the documentation was rebuilt. It also rebuilt with the command `./sage -docbuild all html`. But then `make test` skipped over rebuilding the documentation.
 1. Ran the command `./sage -docbuild --jsmath all html` again and the documentation was rebuilt another time. Executed the command `make test` and the documentation was rebuilt again. But `./sage -docbuild all html` skipped over rebuilding the documentation.
So the culprit here is the option `--jsmath` to the docbuild script. I'm prepared to give the patches a positive review, provided that William is happy with them.


---

Comment by mpatel created at 2009-08-10 01:04:17

Replying to [comment:10 mpatel]:
> In this scenario, the docbuild operator, whether it's invoked explicitly or implicitly, appears to be idempotent.  I noticed the same behavior with consistent use of `--jsmath`.
At least, it's not nilpotent, though that would be quite interesting.


---

Comment by mvngu created at 2009-08-13 18:58:39

I'm pretty happy with the changes proposed in the ticket. But another/different opinion would be be very helpful as it affects the
building of the documentation when running "make test" with a binary version of Sage.


---

Comment by mvngu created at 2009-08-14 11:13:38

Resolution: fixed


---

Comment by mvngu created at 2009-08-14 11:13:38

The proposed changes are fine by me.


---

Comment by mpatel created at 2009-08-15 00:33:51

For the record: The "scripts_doctest" patch was merged, along with a modified "spkg_install" patch.  In effect, the change drops `--jsmath` from the docbuild command.
