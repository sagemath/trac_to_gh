# Issue 7943: move docbuild commands to their own targets in SAGE_ROOT/makefile

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-01-16 09:10:54

Assignee: mvngu

CC:  drkirkby georgsweber jhpalmieri tornaria

As of Sage 4.3, every time you make a clone or build an spkg, the whole documentation is also rebuilt. This is very annoying. See this [sage-devel](http://groups.google.com/group/sage-devel/msg/f6d2c21372a7d1d7) message for the vote to move the docbuild commands to their own targets in the script `SAGE_ROOT/makefile`. Or at least make it so that creating a clone or rebuilding an spkg doesn't also trigger a rebuild of the documentation.


---

Comment by mpatel created at 2010-01-17 14:51:11

For changes to `makefile` and `spkg/install`, should we attach "diffs"?


---

Comment by mvngu created at 2010-01-17 15:00:42

Replying to [comment:1 mpatel]:
> For changes to `makefile` and `spkg/install`, should we attach "diffs"?

Both `makefile` and `spkg/install` are not under revision control. To update them, you need to upload updated versions of these files. But you also need to upload diff files showing changes between the updated and current version. This is to show the proposed changes. The diff files are not to be applied.


---

Comment by mpatel created at 2010-02-19 11:04:21

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-02-19 11:04:21

I've attached an updated `makefile` and `spkg/install`, and their diffs.  I started with 4.3.3.alpha1.

Do we still use `spkg/archive`?


---

Comment by mpatel created at 2010-02-19 11:16:01

On math: Users who prefer JSMath to PNGmath can use `make doc-html-jsmath` or


```sh
export DOCBUILD_OPTS="-j"
make doc-html
```

On log proliferation: For parallel inter-spkg builds, we'll need to have one log file per spkg.  We could put them all in `SAGE_ROOT/logs`, say.

On cloning: #8258 may help.


---

Comment by mvngu created at 2010-02-20 14:45:55

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-20 14:45:55

Looks good to me. Typing "make" on a binary distribution won't rebuild the documentation. Also, cloning doesn't rebuild the doc.


---

Comment by mpatel created at 2010-02-20 16:50:29

The patches above shouldn't affect the docbuild-on-clone problem, which may necessitate changes to Sphinx.  But we could make or appropriate a separate ticket for that "bottom favorite."


---

Comment by mpatel created at 2010-02-20 21:43:54

Since the test targets in `SAGE_ROOT/makefile` do not depend on the doc targets, we may get reports about failed doctests in `sage.misc.sagedoc`:


```python
sage: len(search_doc('tree', interact=False).splitlines()) > 2000
sage: len(search_doc('tree', whole_word=True, interact=False).splitlines()) < 100
sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)
```

What if we make the first two `optional` and insert `or 'Warning, the following Sage documentation'` in the third?


---

Comment by mpatel created at 2010-02-20 21:46:14

Oops.  I suppose that should be "make all three optional or conditional, somehow."


---

Comment by jhpalmieri created at 2010-02-21 01:06:28

I think I object to the positive review here, because having complete documentation is an important part of Sage, but it looks like with these patches, building Sage from source will not build the documentation.  Correct me if I'm wrong about this.

At the very least, since this is a major change, this should discussed more thoroughly in sage-devel before doing this.

What happens if we add "doc" to the targets in the makefile for "make all"?

> Since the test targets in SAGE_ROOT/makefile do not depend on the doc targets, we may get reports about failed doctests in sage.misc.sagedoc

If you feel, as I do, that the documentation is an integral part of Sage, then it's reasonable that if you try doctesting with an incomplete Sage build (for example, if you're missing the documentation), you should not be surprised if there are doctest failures.  The failures do say "Warning, the following Sage documentation...", so it's more or less clear why they failed.


---

Comment by mvngu created at 2010-02-21 01:24:08

Replying to [comment:9 jhpalmieri]:
> If you feel, as I do, that the documentation is an integral part of Sage, then it's reasonable that if you try doctesting with an incomplete Sage build (for example, if you're missing the documentation), you should not be surprised if there are doctest failures.  The failures do say "Warning, the following Sage documentation...", so it's more or less clear why they failed.

That's a point I missed.


---

Comment by mvngu created at 2010-02-21 01:24:08

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-02-21 02:25:59

I apologize about the first versions.  I've attached an updated `makefile` and `makefile.diff`.  The target(s)

 * `build` builds Sage but not the documentation.
 * `all` depends on `build` and `doc`.
 * `*test*` depend on `all`.

What are the circumstances under which [rebuilding just an spkg triggers a rebuild of the docs](http://groups.google.com/group/sage-devel/msg/2ed1823b567d6d26)?


---

Comment by mpatel created at 2010-02-21 02:25:59

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-02-21 03:43:44

Replying to [comment:11 mpatel]:
> I apologize about the first versions.

No need to apologize: this is why patches are refereed.

> What are the circumstances under which [rebuilding just an spkg triggers a rebuild of the docs](http://groups.google.com/group/sage-devel/msg/2ed1823b567d6d26)?

I'm curious about this, too.  Maybe if you rebuild the spkg by deleting the appropriate file spkg/installed and then typing "make"?  With the new patch you could type "make build" instead, and it should build the spkg without rebuilding the docs.


---

Comment by mpatel created at 2010-02-21 22:52:41

I've "rebased" `spkg/install` against #8191.


---

Comment by mpatel created at 2010-03-02 22:47:22

I've added [.PHONY targets](http://www.gnu.org/software/automake/manual/make/Phony-Targets.html) to `makefile`.  Aside: Run `make -d` to see how GNU `make` processes dependencies.

Should we change `DOCBUILD_OPTS` to `SAGE_DOCBUILD_OPTS`?


---

Comment by mvngu created at 2010-03-02 22:58:45

Replying to [comment:15 mpatel]:
> Should we change `DOCBUILD_OPTS` to `SAGE_DOCBUILD_OPTS`?

I would endorse that decision, primarily on the ground of consistency. Currently, many (if not most) Sage-specific environment variables are prefixed with "SAGE_". If you change `DOCBUILD_OPTS` to `SAGE_DOCBUILD_OPTS`, please consider writing some documentation regarding its intended purpose and use. Ticket #8263 is the natural place to do so.


---

Comment by mpatel created at 2010-03-02 23:03:36

Updated `makefile`.


---

Attachment

Diff of `makefile`.


---

Comment by mpatel created at 2010-03-02 23:07:01

I've changed `DOCBUILD_OPTS` to `SAGE_DOCBUILD_OPTS`.  I'll update #8263's description if this ticket passes review.


---

Comment by mvngu created at 2010-03-04 03:02:48

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2010-03-04 03:02:48

A comparison of the file `install` on this ticket and the corresponding file in Sage 4.3.4.alpha0 shows this:

```
[mvngu`@`sage spkg]$ diff -Naur install.orig install
--- install.orig	2010-03-03 10:45:48.991436483 -0800
+++ install	2010-02-21 14:51:11.000000000 -0800
`@``@` -131,6 +131,9 `@``@`
 PIL=`$newest pil`
 export PIL
 
+PYPROCESSING=`$newest pyprocessing`
+export PYPROCESSING
+
 LIBM4RI=`$newest libm4ri`
 export LIBM4RI
 
`@``@` -364,14 +367,6 `@``@`
     exit 1
 fi
 
-# Build the documentation
-# The following three lines have been commented out. They cause the
-# documentation to rebuild when doing "make test". See trac 6645.
-#rm -rf "$SAGE_ROOT"/devel/sage-main/doc/output/doctrees
-#rm -rf "$SAGE_ROOT"/devel/sage-main/doc/en/reference/sage/*
-#"$SAGE_ROOT"/sage -docbuild --jsmath all html
-"$SAGE_ROOT"/sage -docbuild all html
-
 if [ "$1" = "all" -a $? = 0 ]; then
     echo "To install gap, gp, singular, etc., scripts"
     echo "in a standard bin directory, start sage and"
`@``@` -379,5 +374,8 `@``@`
     echo "   sage: install_scripts('/usr/local/bin')"
     echo "at the Sage command prompt."
     echo ""
+    echo "To build the documentation, run"
+    echo "   make doc"
+    echo ""
     echo "Sage build/upgrade complete!"
 fi
```

The problematic snippet is:

```
+PYPROCESSING=`$newest pyprocessing`
+export PYPROCESSING
+
```

Ticket #6503 has removed pyprocessing from the standard spkg repository. Could the file `install` here be rebased on top of that in Sage 4.3.4.alpha0?


---

Comment by jhpalmieri created at 2010-03-04 04:49:47

I think except for the rebasing, this looks ready to go.


---

Comment by mpatel created at 2010-03-04 07:14:44

Diff of `spkg/install`.


---

Attachment

Rebased vs. 4.3.4.alpha0.  Updated `spkg/install`.


---

Comment by mpatel created at 2010-03-04 07:17:44

I've attached a rebased `spkg/install`.


---

Comment by mpatel created at 2010-03-04 07:17:44

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-03-04 16:12:18

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-09 07:49:28

Resolution: fixed
