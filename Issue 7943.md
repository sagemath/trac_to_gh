# Issue 7943: move docbuild commands to their own targets in SAGE_ROOT/makefile

archive/issues_007943.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  drkirkby georgsweber @jhpalmieri @tornaria\n\nAs of Sage 4.3, every time you make a clone or build an spkg, the whole documentation is also rebuilt. This is very annoying. See this [sage-devel](http://groups.google.com/group/sage-devel/msg/f6d2c21372a7d1d7) message for the vote to move the docbuild commands to their own targets in the script `SAGE_ROOT/makefile`. Or at least make it so that creating a clone or rebuilding an spkg doesn't also trigger a rebuild of the documentation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7943\n\n",
    "closed_at": "2010-03-09T07:49:28Z",
    "created_at": "2010-01-16T09:10:54Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "move docbuild commands to their own targets in SAGE_ROOT/makefile",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7943",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

CC:  drkirkby georgsweber @jhpalmieri @tornaria

As of Sage 4.3, every time you make a clone or build an spkg, the whole documentation is also rebuilt. This is very annoying. See this [sage-devel](http://groups.google.com/group/sage-devel/msg/f6d2c21372a7d1d7) message for the vote to move the docbuild commands to their own targets in the script `SAGE_ROOT/makefile`. Or at least make it so that creating a clone or rebuilding an spkg doesn't also trigger a rebuild of the documentation.

Issue created by migration from https://trac.sagemath.org/ticket/7943





---

archive/issue_comments_069164.json:
```json
{
    "body": "For changes to `makefile` and `spkg/install`, should we attach \"diffs\"?",
    "created_at": "2010-01-17T14:51:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69164",
    "user": "https://github.com/qed777"
}
```

For changes to `makefile` and `spkg/install`, should we attach "diffs"?



---

archive/issue_comments_069165.json:
```json
{
    "body": "Replying to [comment:1 mpatel]:\n> For changes to `makefile` and `spkg/install`, should we attach \"diffs\"?\n\n\nBoth `makefile` and `spkg/install` are not under revision control. To update them, you need to upload updated versions of these files. But you also need to upload diff files showing changes between the updated and current version. This is to show the proposed changes. The diff files are not to be applied.",
    "created_at": "2010-01-17T15:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69165",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:1 mpatel]:
> For changes to `makefile` and `spkg/install`, should we attach "diffs"?


Both `makefile` and `spkg/install` are not under revision control. To update them, you need to upload updated versions of these files. But you also need to upload diff files showing changes between the updated and current version. This is to show the proposed changes. The diff files are not to be applied.



---

archive/issue_comments_069166.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-19T11:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69166",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069167.json:
```json
{
    "body": "I've attached an updated `makefile` and `spkg/install`, and their diffs.\u00a0 I started with 4.3.3.alpha1.\n\nDo we still use `spkg/archive`?",
    "created_at": "2010-02-19T11:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69167",
    "user": "https://github.com/qed777"
}
```

I've attached an updated `makefile` and `spkg/install`, and their diffs.  I started with 4.3.3.alpha1.

Do we still use `spkg/archive`?



---

archive/issue_comments_069168.json:
```json
{
    "body": "On math: Users who prefer JSMath to PNGmath can use `make doc-html-jsmath` or\n\n```sh\nexport DOCBUILD_OPTS=\"-j\"\nmake doc-html\n```\nOn log proliferation: For parallel inter-spkg builds, we'll need to have one log file per spkg.  We could put them all in `SAGE_ROOT/logs`, say.\n\nOn cloning: #8258 may help.",
    "created_at": "2010-02-19T11:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69168",
    "user": "https://github.com/qed777"
}
```

On math: Users who prefer JSMath to PNGmath can use `make doc-html-jsmath` or

```sh
export DOCBUILD_OPTS="-j"
make doc-html
```
On log proliferation: For parallel inter-spkg builds, we'll need to have one log file per spkg.  We could put them all in `SAGE_ROOT/logs`, say.

On cloning: #8258 may help.



---

archive/issue_comments_069169.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-20T14:45:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69169",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069170.json:
```json
{
    "body": "Looks good to me. Typing \"make\" on a binary distribution won't rebuild the documentation. Also, cloning doesn't rebuild the doc.",
    "created_at": "2010-02-20T14:45:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69170",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Looks good to me. Typing "make" on a binary distribution won't rebuild the documentation. Also, cloning doesn't rebuild the doc.



---

archive/issue_comments_069171.json:
```json
{
    "body": "The patches above shouldn't affect the docbuild-on-clone problem, which may necessitate changes to Sphinx.  But we could make or appropriate a separate ticket for that \"bottom favorite.\"",
    "created_at": "2010-02-20T16:50:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69171",
    "user": "https://github.com/qed777"
}
```

The patches above shouldn't affect the docbuild-on-clone problem, which may necessitate changes to Sphinx.  But we could make or appropriate a separate ticket for that "bottom favorite."



---

archive/issue_comments_069172.json:
```json
{
    "body": "Since the test targets in `SAGE_ROOT/makefile` do not depend on the doc targets, we may get reports about failed doctests in `sage.misc.sagedoc`:\n\n```python\nsage: len(search_doc('tree', interact=False).splitlines()) > 2000\nsage: len(search_doc('tree', whole_word=True, interact=False).splitlines()) < 100\nsage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)\n```\nWhat if we make the first two `optional` and insert `or 'Warning, the following Sage documentation'` in the third?",
    "created_at": "2010-02-20T21:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69172",
    "user": "https://github.com/qed777"
}
```

Since the test targets in `SAGE_ROOT/makefile` do not depend on the doc targets, we may get reports about failed doctests in `sage.misc.sagedoc`:

```python
sage: len(search_doc('tree', interact=False).splitlines()) > 2000
sage: len(search_doc('tree', whole_word=True, interact=False).splitlines()) < 100
sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology', 'variety', interact=False)
```
What if we make the first two `optional` and insert `or 'Warning, the following Sage documentation'` in the third?



---

archive/issue_comments_069173.json:
```json
{
    "body": "Oops.\u00a0 I suppose that should be \"make all three optional or conditional, somehow.\"",
    "created_at": "2010-02-20T21:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69173",
    "user": "https://github.com/qed777"
}
```

Oops.  I suppose that should be "make all three optional or conditional, somehow."



---

archive/issue_comments_069174.json:
```json
{
    "body": "I think I object to the positive review here, because having complete documentation is an important part of Sage, but it looks like with these patches, building Sage from source will not build the documentation.  Correct me if I'm wrong about this.\n\nAt the very least, since this is a major change, this should discussed more thoroughly in sage-devel before doing this.\n\nWhat happens if we add \"doc\" to the targets in the makefile for \"make all\"?\n\n> Since the test targets in SAGE_ROOT/makefile do not depend on the doc targets, we may get reports about failed doctests in sage.misc.sagedoc\n\n\nIf you feel, as I do, that the documentation is an integral part of Sage, then it's reasonable that if you try doctesting with an incomplete Sage build (for example, if you're missing the documentation), you should not be surprised if there are doctest failures.  The failures do say \"Warning, the following Sage documentation...\", so it's more or less clear why they failed.",
    "created_at": "2010-02-21T01:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69174",
    "user": "https://github.com/jhpalmieri"
}
```

I think I object to the positive review here, because having complete documentation is an important part of Sage, but it looks like with these patches, building Sage from source will not build the documentation.  Correct me if I'm wrong about this.

At the very least, since this is a major change, this should discussed more thoroughly in sage-devel before doing this.

What happens if we add "doc" to the targets in the makefile for "make all"?

> Since the test targets in SAGE_ROOT/makefile do not depend on the doc targets, we may get reports about failed doctests in sage.misc.sagedoc


If you feel, as I do, that the documentation is an integral part of Sage, then it's reasonable that if you try doctesting with an incomplete Sage build (for example, if you're missing the documentation), you should not be surprised if there are doctest failures.  The failures do say "Warning, the following Sage documentation...", so it's more or less clear why they failed.



---

archive/issue_comments_069175.json:
```json
{
    "body": "Replying to [comment:9 jhpalmieri]:\n> If you feel, as I do, that the documentation is an integral part of Sage, then it's reasonable that if you try doctesting with an incomplete Sage build (for example, if you're missing the documentation), you should not be surprised if there are doctest failures.  The failures do say \"Warning, the following Sage documentation...\", so it's more or less clear why they failed.\n\n\nThat's a point I missed.",
    "created_at": "2010-02-21T01:24:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69175",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:9 jhpalmieri]:
> If you feel, as I do, that the documentation is an integral part of Sage, then it's reasonable that if you try doctesting with an incomplete Sage build (for example, if you're missing the documentation), you should not be surprised if there are doctest failures.  The failures do say "Warning, the following Sage documentation...", so it's more or less clear why they failed.


That's a point I missed.



---

archive/issue_comments_069176.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-02-21T01:24:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69176",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_069177.json:
```json
{
    "body": "I apologize about the first versions.\u00a0 I've attached an updated `makefile` and `makefile.diff`.  The target(s)\n\n* `build` builds Sage but not the documentation.\n* `all` depends on `build` and `doc`.\n* `*test*` depend on `all`.\n\nWhat are the circumstances under which [rebuilding just an spkg triggers a rebuild of the docs](http://groups.google.com/group/sage-devel/msg/2ed1823b567d6d26)?",
    "created_at": "2010-02-21T02:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69177",
    "user": "https://github.com/qed777"
}
```

I apologize about the first versions.  I've attached an updated `makefile` and `makefile.diff`.  The target(s)

* `build` builds Sage but not the documentation.
* `all` depends on `build` and `doc`.
* `*test*` depend on `all`.

What are the circumstances under which [rebuilding just an spkg triggers a rebuild of the docs](http://groups.google.com/group/sage-devel/msg/2ed1823b567d6d26)?



---

archive/issue_comments_069178.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-21T02:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69178",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069179.json:
```json
{
    "body": "Replying to [comment:11 mpatel]:\n> I apologize about the first versions.\n\n\nNo need to apologize: this is why patches are refereed.\n\n> What are the circumstances under which [rebuilding just an spkg triggers a rebuild of the docs](http://groups.google.com/group/sage-devel/msg/2ed1823b567d6d26)?\n\n\nI'm curious about this, too.  Maybe if you rebuild the spkg by deleting the appropriate file spkg/installed and then typing \"make\"?  With the new patch you could type \"make build\" instead, and it should build the spkg without rebuilding the docs.",
    "created_at": "2010-02-21T03:43:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69179",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:11 mpatel]:
> I apologize about the first versions.


No need to apologize: this is why patches are refereed.

> What are the circumstances under which [rebuilding just an spkg triggers a rebuild of the docs](http://groups.google.com/group/sage-devel/msg/2ed1823b567d6d26)?


I'm curious about this, too.  Maybe if you rebuild the spkg by deleting the appropriate file spkg/installed and then typing "make"?  With the new patch you could type "make build" instead, and it should build the spkg without rebuilding the docs.



---

archive/issue_comments_069180.json:
```json
{
    "body": "I've \"rebased\" `spkg/install` against #8191.",
    "created_at": "2010-02-21T22:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69180",
    "user": "https://github.com/qed777"
}
```

I've "rebased" `spkg/install` against #8191.



---

archive/issue_comments_069181.json:
```json
{
    "body": "I've added [.PHONY targets](http://www.gnu.org/software/automake/manual/make/Phony-Targets.html) to `makefile`.  Aside: Run `make -d` to see how GNU `make` processes dependencies.\n\nShould we change `DOCBUILD_OPTS` to `SAGE_DOCBUILD_OPTS`?",
    "created_at": "2010-03-02T22:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69181",
    "user": "https://github.com/qed777"
}
```

I've added [.PHONY targets](http://www.gnu.org/software/automake/manual/make/Phony-Targets.html) to `makefile`.  Aside: Run `make -d` to see how GNU `make` processes dependencies.

Should we change `DOCBUILD_OPTS` to `SAGE_DOCBUILD_OPTS`?



---

archive/issue_comments_069182.json:
```json
{
    "body": "Replying to [comment:15 mpatel]:\n> Should we change `DOCBUILD_OPTS` to `SAGE_DOCBUILD_OPTS`?\n\n\nI would endorse that decision, primarily on the ground of consistency. Currently, many (if not most) Sage-specific environment variables are prefixed with \"SAGE_\". If you change `DOCBUILD_OPTS` to `SAGE_DOCBUILD_OPTS`, please consider writing some documentation regarding its intended purpose and use. Ticket #8263 is the natural place to do so.",
    "created_at": "2010-03-02T22:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69182",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:15 mpatel]:
> Should we change `DOCBUILD_OPTS` to `SAGE_DOCBUILD_OPTS`?


I would endorse that decision, primarily on the ground of consistency. Currently, many (if not most) Sage-specific environment variables are prefixed with "SAGE_". If you change `DOCBUILD_OPTS` to `SAGE_DOCBUILD_OPTS`, please consider writing some documentation regarding its intended purpose and use. Ticket #8263 is the natural place to do so.



---

archive/issue_comments_069183.json:
```json
{
    "body": "Updated `makefile`.",
    "created_at": "2010-03-02T23:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69183",
    "user": "https://github.com/qed777"
}
```

Updated `makefile`.



---

archive/issue_comments_069184.json:
```json
{
    "body": "Attachment [makefile.diff](tarball://root/attachments/some-uuid/ticket7943/makefile.diff) by @qed777 created at 2010-03-02 23:03:43\n\nDiff of `makefile`.",
    "created_at": "2010-03-02T23:03:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69184",
    "user": "https://github.com/qed777"
}
```

Attachment [makefile.diff](tarball://root/attachments/some-uuid/ticket7943/makefile.diff) by @qed777 created at 2010-03-02 23:03:43

Diff of `makefile`.



---

archive/issue_comments_069185.json:
```json
{
    "body": "I've changed `DOCBUILD_OPTS` to `SAGE_DOCBUILD_OPTS`.  I'll update #8263's description if this ticket passes review.",
    "created_at": "2010-03-02T23:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69185",
    "user": "https://github.com/qed777"
}
```

I've changed `DOCBUILD_OPTS` to `SAGE_DOCBUILD_OPTS`.  I'll update #8263's description if this ticket passes review.



---

archive/issue_comments_069186.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-04T03:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69186",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069187.json:
```json
{
    "body": "A comparison of the file `install` on this ticket and the corresponding file in Sage 4.3.4.alpha0 shows this:\n\n```\n[mvngu@sage spkg]$ diff -Naur install.orig install\n--- install.orig\t2010-03-03 10:45:48.991436483 -0800\n+++ install\t2010-02-21 14:51:11.000000000 -0800\n@@ -131,6 +131,9 @@\n PIL=`$newest pil`\n export PIL\n \n+PYPROCESSING=`$newest pyprocessing`\n+export PYPROCESSING\n+\n LIBM4RI=`$newest libm4ri`\n export LIBM4RI\n \n@@ -364,14 +367,6 @@\n     exit 1\n fi\n \n-# Build the documentation\n-# The following three lines have been commented out. They cause the\n-# documentation to rebuild when doing \"make test\". See trac 6645.\n-#rm -rf \"$SAGE_ROOT\"/devel/sage-main/doc/output/doctrees\n-#rm -rf \"$SAGE_ROOT\"/devel/sage-main/doc/en/reference/sage/*\n-#\"$SAGE_ROOT\"/sage -docbuild --jsmath all html\n-\"$SAGE_ROOT\"/sage -docbuild all html\n-\n if [ \"$1\" = \"all\" -a $? = 0 ]; then\n     echo \"To install gap, gp, singular, etc., scripts\"\n     echo \"in a standard bin directory, start sage and\"\n@@ -379,5 +374,8 @@\n     echo \"   sage: install_scripts('/usr/local/bin')\"\n     echo \"at the Sage command prompt.\"\n     echo \"\"\n+    echo \"To build the documentation, run\"\n+    echo \"   make doc\"\n+    echo \"\"\n     echo \"Sage build/upgrade complete!\"\n fi\n```\nThe problematic snippet is:\n\n```\n+PYPROCESSING=`$newest pyprocessing`\n+export PYPROCESSING\n+\n```\nTicket #6503 has removed pyprocessing from the standard spkg repository. Could the file `install` here be rebased on top of that in Sage 4.3.4.alpha0?",
    "created_at": "2010-03-04T03:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69187",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

A comparison of the file `install` on this ticket and the corresponding file in Sage 4.3.4.alpha0 shows this:

```
[mvngu@sage spkg]$ diff -Naur install.orig install
--- install.orig	2010-03-03 10:45:48.991436483 -0800
+++ install	2010-02-21 14:51:11.000000000 -0800
@@ -131,6 +131,9 @@
 PIL=`$newest pil`
 export PIL
 
+PYPROCESSING=`$newest pyprocessing`
+export PYPROCESSING
+
 LIBM4RI=`$newest libm4ri`
 export LIBM4RI
 
@@ -364,14 +367,6 @@
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
@@ -379,5 +374,8 @@
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

archive/issue_comments_069188.json:
```json
{
    "body": "I think except for the rebasing, this looks ready to go.",
    "created_at": "2010-03-04T04:49:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69188",
    "user": "https://github.com/jhpalmieri"
}
```

I think except for the rebasing, this looks ready to go.



---

archive/issue_comments_069189.json:
```json
{
    "body": "Diff of `spkg/install`.",
    "created_at": "2010-03-04T07:14:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69189",
    "user": "https://github.com/qed777"
}
```

Diff of `spkg/install`.



---

archive/issue_comments_069190.json:
```json
{
    "body": "Attachment [install](tarball://root/attachments/some-uuid/ticket7943/install) by @qed777 created at 2010-03-04 07:15:55\n\nRebased vs. 4.3.4.alpha0.  Updated `spkg/install`.",
    "created_at": "2010-03-04T07:15:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69190",
    "user": "https://github.com/qed777"
}
```

Attachment [install](tarball://root/attachments/some-uuid/ticket7943/install) by @qed777 created at 2010-03-04 07:15:55

Rebased vs. 4.3.4.alpha0.  Updated `spkg/install`.



---

archive/issue_comments_069191.json:
```json
{
    "body": "I've attached a rebased `spkg/install`.",
    "created_at": "2010-03-04T07:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69191",
    "user": "https://github.com/qed777"
}
```

I've attached a rebased `spkg/install`.



---

archive/issue_comments_069192.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-04T07:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69192",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069193.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-04T16:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69193",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069194.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-09T07:49:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7943#issuecomment-69194",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_019008.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-03-09T07:49:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7943",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7943#event-19008"
}
```
