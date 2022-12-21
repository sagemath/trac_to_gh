# Issue 6187: After making a clone, the reference manual (and other docs) should not have to be completely rebuilt.

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-06-02 17:00:10

Assignee: tba

CC:  mhansen mvngu davidloeffler

From [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/87a143a395bd1297):

```
> What does force a complete rebuild is making a new branch with "sage - 
> clone". This is annoying; I don't know enough about the build 
> machinery to know if this can be changed. 

I agree.  If I have built the docs in the main branch and make a 
clone, it would be great of the docs were clones too, as then we would 
only need to build the docs once per release. 
I imagine this is easily doable by adapting the clone script.  If 
people agree, could someone  make a ticket? 
```

Note that the documentation output is copied (because of #5469), but something is still triggering a rebuild.  I don't know enough about Sphinx to know what is causing this.


---

Comment by mhansen created at 2009-06-02 20:24:19

I think the file modification times need to be copied over as well with a "cp -a" instead of "cp -r".  I'm not sure if there are any hardcoded paths in the Sphinx environment pickle that would need to be changed.


---

Comment by jhpalmieri created at 2009-06-02 21:25:45

I'm not having any luck with this.  If in sage-clone I copy the library files with "cp -a" (or what I think is the equivalent, e.g. "cp -pr" on my mac, or `shutil.copytree("sage/build","%s/build"%branch)`), then when it gets to the `sage -b` part of things, it rebuilds all of the cython files, so cloning takes way too long.

No matter what, if after cloning, I delete the directory doc/output and then recopy it, `sage -docbuild reference html` rebuilds everything.  This happens whether the modification times are preserved or not: even if the times are not preserved, so everything in the output directory is newer than everything in the build directory, Sphinx seems to think that the files have changed and so need to be rebuilt.  Same thing if I recopy the entire "doc" directory.  So I'm confused.


---

Comment by burcin created at 2009-06-03 07:18:38

#5350 might be relevant here. The script there could be adapted to create hard links for the documentation.


---

Comment by jhpalmieri created at 2009-06-14 17:00:02

This is kind of brutal, but we can replace the cloning part of sage-clone with a single line like

```
cmd = 'cp -pr sage %s'%branch
```

(This is with the BSD version of cp on Mac OS X; it might be more portable to use a python equivalent, like shutil.copytree.)

This has the disadvantage that some crap gets copied along with the good stuff. This is probably a bad idea from other points of view, too; what else goes wrong?  

It has the advantage that modification times are preserved, while they are not (as far as I can tell) when you use 'hg clone' to copy the repository.

By the way, the 'clone' section of the hg man page says:

```
In some cases, you can clone repositories and checked out files
using full hardlinks with
$ cp -al REPO REPOCLONE
This is the fastest way to clone, but it is not always safe. The
operation is not atomic (making sure REPO is not modified during
the operation is up to you) and you have to make sure your editor
breaks hardlinks (Emacs and most Linux Kernel tools do so). Also,
this is not compatible with certain extensions that place their
metadata under the .hg directory, such as mq.
```

This is where I got the idea, although their version creates hard links, which I suppose is why it would be "the fastest way"...


---

Comment by jhpalmieri created at 2009-06-16 02:19:50

One issue to keep in mind when testing: if you do

```
sage -docbuild --jsmath reference html
```

as is done at the end of 'make', and then you do

```
sage -docbuild reference html
```

the entire reference manual gets rebuilt (and similarly for the other pieces of documentation).  So if you're testing out an idea for how to fix this, make sure that you're consistent with the `--jsmath` setting before and after cloning.


---

Comment by jhpalmieri created at 2009-06-16 04:11:09

This patch might very well be a bad idea, but I don't know enough about the Sage cloning process to know any better.  Please review it carefully.

(Actually, I'm posting two patches.  'cloning_scripts_short.patch' just copies over the whole Sage library.  'cloning_scripts.patch' uses the Python 2.6 version of shutil.copytree to allow us to skip certain files when copying, so I copied the source code for that into sage-clone and used that, thereby not copying absolutely everything.  If I'm skipping too many things or not enough things, this is easy to adjust.  Only apply one of these two patches.)


---

Attachment

use this patch or cloning_scripts.patch, but not both -- see my comments


---

Attachment

I have read the comments here with interest, and could try out those patches, but I'm not qualified to say whether they work "well" or are robust enough to be released -- sorry!


---

Comment by jhpalmieri created at 2009-06-26 15:12:17

Here's a patch rebased against 4.1.alpha1.


---

Comment by jhpalmieri created at 2009-06-26 15:13:55

rebased against 4.1.alpha1, use instead of either of the other patches


---

Attachment

Here's what I did.  1. Starting in main branch of a 4.1.alpha2 build, did "sage -docbuild all html" and waited until it finished.  2. Made a clone called test1.  3.  In that clone, did "sage -docbuild again" and watched it build all over again.  4. In the clone, applied the third patch.  5. From that clone made a new clone test2.  6. In the new clone once again did "sage -docbuild all html" -- and nothing was rebuilt!

That looks like success to me.  The new script also looks very much simpler than the old one, which is good.

This is on linux (ubuntu 32-bit);  since you use a standard python utility for the copying I would hope that it would work anywhere, so I'm giving it a positive review and hope that others will try on other systems.


---

Comment by mpatel created at 2009-06-29 00:21:12

The following may help with rebuilding the reference manual after cloning:

 * Start with v4.0.2, or a vanilla `sage-clone` script, at least.
 * Apply 

```
diff --git a/doc/common/builder.py b/doc/common/builder.py
--- a/doc/common/builder.py
+++ b/doc/common/builder.py
`@``@` -353,6 +353,16 `@``@` class ReferenceBuilder(DocBuilder):
         if os.path.exists(_sage):
             copytree(_sage, os.path.join(self.dir, 'sage'))
                 
+        # After "sage -clone", refresh the .rst file mtimes in
+        # environment.pickle.
+        if update_mtimes:
+            import time
+            env = self.get_sphinx_environment()
+            for doc in env.all_docs:
+                env.all_docs[doc] = time.time()
+            env_pickle = os.path.join(self._doctrees_dir(), 'environment.pickle')
+            env.topickle(env_pickle)
+
         getattr(DocBuilder, build_type)(self, *args, **kwds)
     
     def cache_filename(self):
`@``@` -645,6 +655,8 `@``@` def help_message():
 parser = optparse.OptionParser(usage="usage: sage -docbuild [options] name type")
 parser.add_option("--jsmath", action="store_true",
                   help="render math using jsMath")
+parser.add_option("--update_mtimes", action="store_true",
+                  help='update .rst file mtimes (e.g., after "sage -clone")')
 parser.print_help = help_message
 
 if __name__ == '__main__':
`@``@` -653,6 +665,11 `@``@` if __name__ == '__main__':
     if options.jsmath:
         os.environ['SAGE_DOC_JSMATH'] = "True"
 
+    if options.update_mtimes:
+        update_mtimes = True
+    else:
+        update_mtimes = False
+
     #Get the name of the document we are trying to build
     try:
         name, type = args
```

 * Do `sage -clone foo` or, e.g., `cd $SAGE_ROOT/devel/sage-foo; cp -pr ../sage-bar/doc .`
 * Update `builder.py`, if necessary.
 * Do `sage -docbuild reference html --update_mtimes --jsmath`
 * Do `sage -docbuild reference html --jsmath`

Note: I haven't tested this idea with #5350, other documents, other builders, etc.


---

Comment by jhpalmieri created at 2009-06-29 03:15:55

So we could add `sage -docbuild reference html --update_mtimes --jsmath` to the `sage-clone` script, right?

The only issue I see is that if someone has made some changes and then clones before rebuilding the reference manual, the `-update_mtimes` option tells Sage/Sphinx that the ref manual page doesn't need to be changed.  I guess we can add a warning to sage-clone like the warning already there.

This works with or without the patch at #5350, and it works appropriately with or without the `--jsmath` switch.  It has no effect on other documents, as one would expect, but I think that's fine.  Same for the other builders.

Here are two new patches, one which is just mpatel's patch to builder.py (and which receives a positive review from me).  The other adds some code to sage-clone to do the `update_mtimes` thing to the reference manual; it tries to figure out whether to use `--jsmath` or not; is there a better way to do this than what I have?  It also prints a brief message about the reference manual. The only thing that needs to be reviewed is this second patch (to the scripts repository).

I like this version better than my old patch: it keeps the old cloning process, so it seems safer to me.  So I'm changing this from "positive review" (for the old patch) to "needs review" (for the new scripts patch).

Apply "trac_6187_mpatel.patch" to the sage repository, and apply "trac_6187_new_scripts.patch" to the scripts repository.


---

Attachment

I noticed an error occurs during cloning if `environment.pickle` doesn't already exist.

I'll try to make a new patch for `builder.py,` after I build 4.1.alpha2.


---

Comment by mpatel created at 2009-07-01 15:01:07

use this and trac_6187_new_scripts.patch only


---

Attachment

Replying to [comment:12 mpatel]:
> I noticed an error occurs during cloning if `environment.pickle` doesn't already exist.

The new patch should now work in this case.

The pickle's `srcdir` attribute contains what appears to be the only trace of the name of the cloned (i.e., previous) branch.  This can become an issue when branches are renamed or deleted, as Sphinx will throw an OSError.  The new patch now tells Sphinx to use the sym-linked '.../devel/sage/...'

> I'll try to make a new patch for `builder.py,` after I build 4.1.alpha2.

Apply [trac_6187_new_scripts.patch] to the scripts repository and [trac_6187_mpatel_v2.patch] to the sage repository.


---

Comment by jhpalmieri created at 2009-07-02 22:50:16

What should the output from 'sage -docbuild --update_mtimes reference html' look like?  Right now I see

```
sphinx-build -b html -d /Applications/sage/devel/sage/doc/output/doctrees/en/reference    /Applications/sage/devel/sage/doc/en/reference /Applications/sage/devel/sage/doc/output/html/en/reference
Sphinx v0.5.1, building html
loading pickled environment... done
building [html]: targets for 0 source files that are out of date
updating environment: 0 added, 0 changed, 0 removed
no targets are out of date.
Build finished.  The built documents can be found in /Applications/sage/devel/sage/doc/output/html/en/reference
```

Since it's not actually building anything (is it?), I think this is misleading.  In the new scripts patch, I've changed sage-clone so that it suppresses the standard output from this command.


---

Attachment

apply to scripts repo. use this and trac_6187_mpatel_v2.patch only.


---

Attachment

Apply this to scripts repo and trac_6187_mpatel_v3.patch to sage repo.


---

Comment by mpatel created at 2009-07-06 11:02:29

Apply this to sage repo and trac_6187_new_scripts_v3.patch to scripts repo.


---

Attachment

I've attached new versions of both patches.  Apply only the `v3` pair to the indicated repositories.  Changes:

 * `sage-clone` now copies any existing auto-generated `.rst` files to the new branch, preserving modification times.
 * `builder.py` now updates the pickle first, since otherwise it always regenerates existing `.rst` files after cloning.
 * `jsMath` --> `jsmath` in `sage-clone`.

It's OK to delete existing auto-generated `.rst` files prior to cloning, as long as `doc/output/doctrees/en/reference/reference.pickle` disappears, too.  The patches don't cover this case, since I think it occurs rarely in practice.  I conjecture that *most* of the time, the `update_mtimes` line doesn't actually build anything, but I've been wrong before.


---

Comment by mpatel created at 2009-07-14 18:56:19

Adds a document called 'testreference' for testing the reference builder.  It's non-essential and should be independent of the other patches.


---

Attachment

Apply to scripts repo.  Apply trac_6187_builder_v4.patch to the sage repo.


---

Attachment

Apply to sage repo.  Apply trac_6187_new_scripts_v4.patch to the scripts repo.


---

Attachment

Apply only the v4 pair to the appropriate repositories.  The `testreference` patch just adds a non-trivial test document that should build quickly.  It may give an indication, at least, of the behavior to expect when building the full reference manual.

Changes in v4:
 * Reordering of some code and somewhat better case / exception handling in the reference builder.
 * First steps with Python's [logging](http://docs.python.org/library/logging.html) framework.  It's powerful and easy to use, at least inside one module.  One of Sphinx's utility modules colorizes some of the output.
 * More aggressive use of Python's [optparse](http://docs.python.org/library/optparse.html) module, in order to provide several new command-line options (cf. #6488).  The previous syntax should still work, however.
 * `sage-clone` should now be compatible with #6512. `--update_mtimes` is now `--update-mtimes`.

I've focused on the reference manual, but I hope the new pieces make it easier to improve the docbuild system for the other documents, too.  Feel free to make constructive comments, as well as changes.  In particular, we should settle on the option names.

Anyway, if possible, please test the patches in multiple real-world scenarios, including those mentioned on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/f28cef82a0a3ccd1/05b695146514021d?#05b695146514021d).  I'd like to take care of all known, relevant "ref-cloning" issues (cf. #5350) before this ticket closes.  It is likely we're not there yet.

I've added a few recipients to the CC list.  I hope that's OK.


---

Comment by mpatel created at 2009-07-14 20:44:25

I should add that I selected capital letters for listing commands (`-C`), formats (`-F`), and documents (`-D`), so that we could use the corresponding lower-case letters, if it's desired, to carry out multiple actions, e.g.,

```
sage -docbuild -d reference,tutorial -f pdf,html -jv2
```

Is the command-format distinction useful?  We could add commands to "pre-process" groups of docstrings, e.g., to check for and enforce style conventions or to search for cross-references that point to a given object.  However, I'm not very familiar with actually writing ReST docstrings.


---

Comment by mpatel created at 2009-07-22 04:35:02

Run, e.g., `sage -docbuild` to see a "short" help message and `sage -docbuild -H` to see an extended message, including several examples.  Please feel free to edit any parts to make the system easier to use.  Should I post to sage-devel about the new options?

I'm changing the status of this ticket to WPNR to signal that the patches are [again] ready for testing, comment, and perhaps even review.


---

Comment by mpatel created at 2009-07-22 04:40:38

To see colored logging output, try `sage -docbuild testreference html -jv3 -S -E`, say.  I haven't colorized the help messages, since the user's terminal may not support ANSI color escape sequences.


---

Comment by jhpalmieri created at 2009-07-22 23:24:33

Reminder: Make sure to include something like the patch at #6488 (documenting "--jsmath").  

When this ticket is closed, close #6488 as well.


---

Comment by jhpalmieri created at 2009-07-23 17:50:10

Overall, this works as advertised.  I like the new options, the new option parsing, and the help messages.  We might consider eventually updating mtimes on all of the docs, not just the reference manual, but everything else is quick enoug to build that it's not a big deal.  (To test: I installed the two patches here and made sure the docs were built.  Then I cloned the current repository and rebuilt the docs.  The reference manual built almost instantly, because it was using the version from the clone.)

Someone else should take a good look at it, though, since I am an author of part of this (the scripts part).  Also, there are a number of changes to builder.py, and other people should look carefully at them, more carefully than I have so far.

Other comments: if I do something like `sage -docbuild hello html`, then it says

```
sphinx-build -b html -d /Applications/sage/devel/sage/doc/output/doctrees/en/hello    /Applications/sage/devel/sage/doc/en/hello /Applications/sage/devel/sage/doc/output/html/en/hello
Error: Source directory doesn't contain conf.py file.
Build finished.  The built documents can be found in /Applications/sage/devel/sage/doc/output/html/en/hello
```

The problem is, it creates a directory SAGE_ROOT/devel/sage/doc/en/hello, and now "hello" appears in the list of documents.  Should there be better error checking to prevent this from happening?

Actually, I think this belongs on another ticket: it's a "pre-existing condition", and can be dealt with separately.  See #6605.


---

Comment by mpatel created at 2009-07-24 15:47:46

A reminder to myself:  Change `sys.exit(0)` to `sys.exit(1)`.


---

Comment by mpatel created at 2009-08-02 22:36:19

Replying to [comment:23 mpatel]:
> A reminder to myself:  Change `sys.exit(0)` to `sys.exit(1)`.
Also:  Update the scripts patch, if necessary, for consistency with #6614.


---

Attachment

Updated for #6673.  Apply to scripts repo.


---

Attachment

Fixed sys.exit() code. Apply to sage repo.


---

Comment by mpatel created at 2009-08-22 14:51:15

V5 just squares `sage-clone` with #6673 and changes `sys.exit(0)` to `sys.exit(1)` in one instance in `builder.py`.


---

Comment by cremona created at 2009-09-06 16:45:42

It's asking a lot of a reviewer to apply over a dozen patches!  Any chance of combining them all into one?


---

Comment by mpatel created at 2009-09-06 17:02:24

I apologize for not being explicit.  Please apply just the v5 pair: the "new_scripts" patch to the scripts repository and the "builder" patch to the sage repository.


---

Comment by mhansen created at 2009-10-15 16:32:13

After look at this and testing it out, I think that it can go in.


---

Comment by mhansen created at 2009-10-15 16:32:13

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-15 16:32:52

Resolution: fixed
