# Issue 6495: Break up the PDF reference manual into smaller pieces

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-07-09 08:29:32

Assignee: tba

CC:  jhpalmieri leif niles hivert mguaypaq mhansen

Is the logical division at the module level, with the non-auto-generated `.rst` files as guides?

Related: Should the indices be single-column?


---

Comment by mpatel created at 2009-07-09 08:53:14

Experimental.


---

Attachment

The attached patch is experimental.  Notes:

 * `sage -docbuild reference pdf` fails to build `arithgroup.pdf`, apparently because of the math macro `\ZZ` in the title.  Unfortunately, I don't know how to fix this.  
 * Since it _replaces_ the top level PDF file with several smaller files, it breaks the patch at #4460.
 * It's not clear what happens to cross-ReST document links.  I'll try to investigate.


---

Comment by mpatel created at 2009-09-11 03:12:00

On cross-PDF document links:  It seems that Sphinx does not produce these.  This may OK, since `file://` URLs can break easily.


---

Comment by mpatel created at 2009-09-11 08:12:31

On the `\ZZ` in `arithgroup.tex`:  It seems the problem stems from `\`@`title` in

```
    \ifsphinxpdfoutput
      \begingroup
      % This \def is required to deal with multi-line authors; it               
      % changes \\ to ', ' (comma-space), making it pass muster for             
      % generating document info in the PDF file.                               
      \def\\{, }
      \pdfinfo{
        /Author (\`@`author)
        /Title (\`@`title)
      }
      \endgroup
    \fi
```

in Sphinx's `manual.cls`.  For some reason, the `\math*` font commands do not work in this context.  I gather that `\mathbf` is preferred, but one workaround is to use

```
Arithmetic Subgroups of `{\rm SL}_2({\bf Z})`
```

in place of 

```
Arithmetic Subgroups of `{\rm SL}_2(\ZZ)`
```

in `arithgroup.rst`.


---

Attachment

Another approach.  Depends on #7549.  Still experimental.  This patch only.  sage repo.


---

Comment by mpatel created at 2009-11-29 19:52:23

The [attachment:trac_6495-reference_breakup.patch new patch] may make it possible to build and update reference manual chapters semi-independently.  I think we can use the [intersphinx extension](http://sphinx.pocoo.org/ext/intersphinx.html) to fix the cross-chapter references.  But we'll need to build the manual twice, a la LaTeX.

To build just a chapter, try, e.g.,

```
sage -docbuild reference/algebras html -juiv3
```


Still to do:

 * Make a combined index page and search page.
 * Check that PDF generation works.
 * Combine chapter PDF files into one large [optional] PDF file (with [pdfjam's](http://www2.warwick.ac.uk/fac/sci/statistics/staff/academic/firth/software/pdfjam) pdfjoin)?
 * Use a specific LaTeX doc title in each `conf.py`.
 * Fix the "Arithmetic Subgroups" heading on the top-level page.
 * Use a visual, 2D layout for the top-level page?  Group by general area?  Add icons?
 * Get a reply from [sphinx-dev](http://groups.google.com/group/sphinx-dev/browse_thread/thread/c8e6f0683c65930a) about making relative paths work.
 * Build docs in parallel (cf. #6255) with [multiprocessing](http://docs.python.org/library/multiprocessing.html)?
 * Replace the "website" PDF link?
 * User-friendliness improvements.
 * Encourage more compact chapters?  It seems that "Combinatorics" takes the most time and memory.
 * ...


---

Comment by mpatel created at 2009-11-29 19:52:23

Changing priority from minor to major.


---

Comment by mpatel created at 2009-11-29 19:52:23

Changing type from defect to enhancement.


---

Comment by mpatel created at 2009-11-29 19:55:16

Another important item:

 * Use just one `_static` directory for the manual, not 50+!


---

Comment by mpatel created at 2009-11-29 19:57:26

If this approach is viable, I suggest leaving many (most?) of the "To Do" items for other tickets.


---

Comment by mpatel created at 2009-11-29 20:14:35

While I'm here:

 * *Copy* PDFs from `output/latex/` to `output/pdf`, so that `make all-pdf`, at least, doesn't do unnecessary work?


---

Comment by mpatel created at 2009-12-03 00:30:49

PDF fixes.  This patch only.  sage repo.


---

Attachment

Sphinx caches "foreign" object inventories in a document's `environment.pickle`.  These now use a lot of disk space.


---

Comment by mpatel created at 2009-12-06 00:41:38

Replying to [comment:9 mpatel]:
> Sphinx caches "foreign" object inventories in a document's `environment.pickle`.  These now use a lot of disk space.
Another [sphinx-dev query](http://groups.google.com/group/sphinx-dev/browse_thread/thread/7c0238fe2b8b8b56/e0969058c69b65de?#e0969058c69b65de).


---

Comment by jhpalmieri created at 2011-07-07 03:00:18

Here's a new patch, rebased to Sage 4.7.1.alpha4.  This implements parallel building, and it provides a great speedup, at least on systems with lots of processors.  For example, on sage.math, the time to execute `sage -docbuild reference html -j` went from about 18 minutes to just under 2 minutes.  The main idea is to build each module of the reference manual separately, and use the Sphinx [intersphinx](http://sphinx.pocoo.org/ext/intersphinx.html) extension to handle cross-references (so `:class:`blah`` will work in the algebras module, even if `blah` is defined in the rings module).

Remaining issues:

 - The new build uses up more disk space than the old, by about 120 megabytes.  I don't know if anything can be done about this, and I also don't think it's a big deal.  (With the previous patch, it took about 1 gigabyte more, but the more recent patch manages to cut that down: in the previous patch, the `_static` subdirectory of the documentation was being copied, once for each module of the reference manual, and with the new version, a symlink is used instead.)
 - There are now some missing bibliographic references: at some point in the past, people have gone through the documentation and unified the references, but this means that references in one module are not seen by any other.  This can be fixed just by copying the references to the module where they're used.  For example: CMR05 is referenced somewhere in the module on polynomial rings, but the actual item is described in `crypto/mq/sr.py`.
 - The cross-referencing in intersphinx is not perfect; in particular, it doesn't seem to work after building the documents once, it needs to have the full doctree "inventory" for any module available before resolving references to that module.  Since the inventory files are built alongside the documentation, this means it has to be built twice (as far as I can tell) before cross-all of the references work.  We could try to figure out dependencies and make sure that if module A is referenced in module B, then A is built first, but that seems complicated, and there is no reason for there not to be circular references.  I'm tempted to just allow broken cross-references.  For the docs on the web site, we would have to make sure they got built twice.
 - There is a main index for the reference manual, but once you click on any entry (like "Cryptography"), you get to that module's index, and there is no link taking you back to the main index.  There ought to be a way to fix this, but I haven't figured it out yet.


---

Comment by vbraun created at 2011-07-07 21:45:55

In an ideal world sphinx would be multithreaded, but we probably shouldn't wait for that ;-) The remaining issues about disk space, bibliographic references, and needing two runs seem to be unavoidable. Building parallel gets more and more important, so I think the benefits outweigh the disadvantages. 

I tried the patch on Sage-4.7.1.alpha4 without any other patches applied:
  * Only the main page has proper css. For example, `html/en/reference/cmd/index.html` refers to `_static/sage.css` but the correct path would be `../_static/sage.css`.
  * patch conflicts with #11251 (todo extension). Given that the latter is already positively reviewed, maybe this ticket could be rebased on top of it?
  * During the sage build, I think we should then run the docbuilder twice for the reference manual. Perhaps this should always be done for `sage -docbuild all`. 
  * Can we make output less verbose? The whole intersphinx output scrolled forever off my screen. Ideally, an interspinx failure to find an inventory file would only add one extra line at the end of the build along the lines of "You should re-run docbuild to get references right."


---

Comment by jhpalmieri created at 2011-07-08 17:38:01

Replying to [comment:13 vbraun]:
> 
> I tried the patch on Sage-4.7.1.alpha4 without any other patches applied:
>   * Only the main page has proper css. For example, `html/en/reference/cmd/index.html` refers to `_static/sage.css` but the correct path would be `../_static/sage.css`.

This was a mistake in the previous version: it was supposed to create a link from `reference/_static` to `reference/cmd/_static`.  Now it should work.

>   * patch conflicts with #11251 (todo extension). Given that the latter is already positively reviewed, maybe this ticket could be rebased on top of it?

Good point.  This raises another problem: intersphinx doesn't easily pass todo lists between different documents, so I don't know how to get a master todo list for the Sage library.  Right now, I've put the todolist for each module after its table of contents.  I think combinat is the only module with any actual to do elements.

>   * During the sage build, I think we should then run the docbuilder twice for the reference manual. Perhaps this should always be done for `sage -docbuild all`. 

Done: `sage -docbuild all` now builds the reference manual twice.  I also added a few print statements to the docbuild process.

>   * Can we make output less verbose? The whole intersphinx output scrolled forever off my screen. Ideally, an interspinx failure to find an inventory file would only add one extra line at the end of the build along the lines of "You should re-run docbuild to get references right."

I've tried to do this when doing `sage -docbuild all` and not in general, but it may be suppressing too much output.  (In the first pass, all warnings are suppressed, including intersphinx warnings, and in the second pass, any warnings should be printed.  But in the second pass, it's just rewriting output, taking intersphinx links into account -- it's not reading the sources a second time, so it doesn't produce warnings about missing bibliographic references.)

Other issues:

 - In PDF output, this produces one PDF file for each module, but there is no "master" file linking to them. I hope we can create one. Should it be an html file or a PDF file?

 - We could perhaps speed things up more by breaking the `combinat` module, which is by far the largest, into several pieces.  This can happen on another ticket.

 - I've reorganized the main index for the reference manual, grouping modules together by topic.  I hope it's easier to find things this way.  I wonder if we can get intersphinx to produce a master index for all of the documents...

 - in the old version, at least on my computer, when I clicked on the Sage logo in the top left corner, it wasn't taking me to the right place.  I've fixed that.  Along the same lines, with the new reorganization, the other links on the top line look a little funny to me in the reference manual.  They looked worse before and I've tried to clean them up, but maybe they could use more work?


---

Comment by jhpalmieri created at 2011-07-12 05:37:10

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2011-07-12 05:37:10

Here's a new version of the patch. This still has the same issue with "todo" items: I don't know a way to accumulate all of them from the different Sage modules, so they are just recorded module-by-module.  For PDF output, the main documentation page (in `SAGE_ROOT/devel/sage/doc/output/html/en/index.html`) has the little PDF icons, and now when you click on the one for the reference manual, it actually opens an html file with links to all of the different PDF files.

I'm marking this for review.  If we can come up with a good solution for "todo" items, that would be great, but perhaps we could defer it to another ticket.


---

Comment by jhpalmieri created at 2011-07-12 19:44:15

Okay, so this is not the most elegant solution, but in the most recent patch, in the html version of the reference manual, after everything is built, it searches through all of the output files algebra/index.html, arithgroup/index.html, etc., looking for todo lists.  When it finds them, it copies them to todolist/index.html.  This only works for the html version; for other formats, the todo list file says "The combined to do list is only available in the html version of the reference manual."


---

Comment by jhpalmieri created at 2011-07-13 23:07:38

Here's a new version; the only difference is this change to SAGE_ROOT/devel/sage/spkg-dist:

```diff
diff --git a/spkg-dist b/spkg-dist
--- a/spkg-dist
+++ b/spkg-dist
`@``@` -38,15 +38,23 `@``@` fi
 
 # Remove the .cython_hash file, since including this in the bdist will
 # completely break "sage -br". 
-# Also, do not distribute these build files (.os and .os); 
+# Also, do not distribute these build files (.so and .os);
 # it wastes space and causes problems!
 
-rm -f .cython_hash c_lib/*.so c_lib/*.os  
+rm -f .cython_hash c_lib/*.so c_lib/*.os
 
 # Delete all the autogenerated files, since they will get created again
 # when SAGE is built or upgraded.  
 cd sage; "$CUR"/spkg-delauto .; cd ..
 
+# Delete the autogenerated files in the doc directory.
+rm -rf doc/output
+rm -rf doc/en/reference/sage
+rm -rf doc/en/reference/sagenb
+rm -rf doc/en/reference/static
+rm -rf doc/en/reference/templates
+rm -rf doc/en/reference/*/sage sage/doc/en/reference/*/static sage/doc/en/reference/*/templates
+
 # Create the sdist using Python's distutils.
 python setup.py sdist
```

This makes for a slightly smaller sage-....spkg file, and more importantly, if the old autogenerated files are there, they can confuse the docbuild process.


---

Comment by jhpalmieri created at 2011-07-13 23:10:15

Some recent timings on sage.math.  

Before the patch:

```
$ rm -rf SAGE_ROOT/devel/sage/doc/output
$ time sage -docbuild reference html
...
real	17m49.313s
user	16m57.530s
sys	0m45.390s

$ rm -rf SAGE_ROOT/devel/sage/doc/output
$ time sage -docbuild reference pdf
...
real	26m3.623s
user	24m40.290s
sys	0m43.030s
```

After the patch:

```

$ rm -rf SAGE_ROOT/devel/sage/doc/output
$ time sage -docbuild reference html
...
real	2m30.092s
user	10m34.900s
sys	1m12.590s

$ rm -rf SAGE_ROOT/devel/sage/doc/output
$ time sage -docbuild reference pdf
...
real	3m35.064s
user	15m49.790s
sys	1m11.070s
```



---

Comment by jhpalmieri created at 2011-07-13 23:16:10

Question: if you type "sage -docbuild -D" now, it says

```
$ sage -docbuild -D
DOCUMENTs:
    de/tutorial          a_tour_of_sage       bordeaux_2008        
    constructions        developer            faq                  
    installation         numerical_sage       reference            
    thematic_tutorials   tutorial             website              
    fr/a_tour_of_sage    fr/tutorial          ru/tutorial          
    all  (!)             
(!) Builds everything.
```

Should we also mention "reference/MODULE" as a valid target?


---

Comment by jhpalmieri created at 2011-07-14 15:26:50

use only this patch


---

Attachment


---

Comment by jhpalmieri created at 2011-07-15 20:10:33

use only this patch


---

Attachment

Here's a new version, with #11298 as a new dependency.  (It may apply without #11298, perhaps with fuzz.)  To help with reviewing, I've broken the patch into two pieces, as explained in the ticket description.


---

Comment by robertwb created at 2011-07-26 05:36:39

Could you post a link to the generated docs so people could browse them?


---

Comment by jhpalmieri created at 2011-07-26 17:29:16

Replying to [comment:24 robertwb]:
> Could you post a link to the generated docs so people could browse them? 

Good idea:

 - [html version](http://sage.math.washington.edu/home/palmieri/misc/6495/output/html/en/reference/)
 - [PDF version](http://sage.math.washington.edu/home/palmieri/misc/6495/output/pdf/en/reference/) (this points to an html document which has links to the pieces of the reference manual in PDF format)


---

Comment by was created at 2011-08-24 23:47:53

Changing keywords from "" to "sd32".


---

Comment by jdemeyer created at 2011-11-11 23:24:39

Testing this against sage-4.8.alpha1 + #10620...


---

Comment by jdemeyer created at 2011-11-11 23:30:48

Against sage-4.8.alpha1:

```
patching file doc/en/reference/games/index.rst
Hunk #1 FAILED at 6
1 out of 1 hunks FAILED -- saving rejects to file doc/en/reference/games/index.rst.rej
patching file doc/en/reference/graphs/index.rst
Hunk #1 succeeded at 52 with fuzz 1 (offset 2 lines).
abort: patch failed to apply
```



---

Comment by jdemeyer created at 2011-11-11 23:32:47

Also: I'm not sure whether building totally in parallel should be the default.


---

Comment by jhpalmieri created at 2011-11-12 02:04:54

Here are rebased patches, along with the following change: there is now an environment variable, `SAGE_PARALLEL_DOCBUILD`, which if set to anything nonempty which doesn't start with "n", causes the reference manual to be built in parallel.  I also added "doc-parallel" and "doc-pdf-parallel" targets to the main Makefile with a patch to the root repo.


---

Attachment

root repo


---

Comment by jhpalmieri created at 2011-11-12 02:11:28

By the way, the default in the new patch is to build serially.  I've also added a brief description of SAGE_PARALLEL_DOCBUILD to the installation guide.


---

Comment by jhpalmieri created at 2011-11-12 03:11:41

Some other possible changes: in the parallel-building code (from builder.py)

```python
            from multiprocessing import Pool, cpu_count
            max_cpus = 8 if SAGE_PARALLEL_DOCBUILD else 1
            pool = Pool(min(max_cpus, cpu_count()))
```

perhaps change "else 1" to "else 2"?  As it is, building serially (with max_cpus set to 1) is slower than the current system, because in the new system, the manual has to be built twice to resolve cross-references.

We could also change "pool" to just "Pool(cpu_count())" or "Pool(int(1.5 * cpu_count()))" or something like that, eliminating the minimum of 8 and possibly increasing the maximum.


---

Comment by jdemeyer created at 2011-11-12 07:17:41

Replying to [comment:34 jhpalmieri]:
> Some other possible changes: in the parallel-building code (from builder.py)
> {{{
> #!python
>             from multiprocessing import Pool, cpu_count
>             max_cpus = 8 if SAGE_PARALLEL_DOCBUILD else 1
>             pool = Pool(min(max_cpus, cpu_count()))
> }}}
> perhaps change "else 1" to "else 2"?
Why?  It wouldn't make sense to build with more processes than there are CPUs.

> We could also change "pool" to just "Pool(cpu_count())" or "Pool(int(1.5 * cpu_count()))" or something like that, eliminating the minimum of 8 and possibly increasing the maximum.
Why?  It wouldn't make sense to build with more processes than there are CPUs.

As I mentioned on sage-devel, I don't like that there is an option to doctest in parallel, a different option to build the docs in parallel, a different option to build in parallel...  I would say: let there be one environment variable `SAGE_NUM_PROCESSES` or something like that and use that for everything.


---

Comment by jhpalmieri created at 2011-11-12 15:56:05

Replying to [comment:35 jdemeyer]:
> Replying to [comment:34 jhpalmieri]:
> > Some other possible changes: in the parallel-building code (from builder.py)
> > {{{
> > #!python
> >             from multiprocessing import Pool, cpu_count
> >             max_cpus = 8 if SAGE_PARALLEL_DOCBUILD else 1
> >             pool = Pool(min(max_cpus, cpu_count()))
> > }}}
> > perhaps change "else 1" to "else 2"?
> Why?  It wouldn't make sense to build with more processes than there are CPUs.

This version still does `min(max_cpus, cpu_count())`, so it won't use more processes than there are CPUs.

> > We could also change "pool" to just "Pool(cpu_count())" or "Pool(int(1.5 * cpu_count()))" or something like that, eliminating the minimum of 8 and possibly increasing the maximum.
> Why?  It wouldn't make sense to build with more processes than there are CPUs.

I see lots of suggestions on the internet to set `MAKE=make -jN` where `N` is 1.5 * (the number of cpus), or 1 or 2 more than the number of cpus.  Why not here as well?

> As I mentioned on sage-devel, I don't like that there is an option to doctest in parallel, a different option to build the docs in parallel, a different option to build in parallel...  I would say: let there be one environment variable `SAGE_NUM_PROCESSES` or something like that and use that for everything.

I think maybe two variables: one (`SAGE_PARALLEL`) to enable parallel processes, one (`SAGE_NUM_THREADS`) to determine the maximum number of processes.  The first could be "no" by default, and the second could be "0" by default, meaning use `cpu_count()` or `min(8, cpu_count())` or some other variant on this, the way we do with `NUM_THREADS` in `Makefile` and `sage-ptest`.  Then it's easy to turn on and off without remembering how many cores your machine has.


---

Comment by was created at 2011-11-12 16:14:20

Why not exactly one environment variable "MAKE" which gets set to "make -jN" for some N, and that is it?     I suggest this, since that's what I'm used to already for years.  I don't claim it is the best solution, but it's in all my .bash* files already, and as John points out above it is documented already all over.   Why don't we just stick with it?


---

Comment by jhpalmieri created at 2011-11-12 20:47:32

Replying to [comment:37 was]:
> Why not exactly one environment variable "MAKE" which gets set to "make -jN" for some N, and that is it?

That's an interesting idea.  See #12016.


---

Comment by jhpalmieri created at 2011-11-12 21:00:08

Here's a new patch which uses the setting of `MAKE` to build docs in parallel (or not).  It's very similar to the code in `sage-ptest` from #12016, except that when you run `sage-ptest`, the assumption should be that you want to work in parallel, so the default number of threads (if MAKE is not set) is min(8, #cpus).  For doc building, we shouldn't assume parallel building by default, I guess, so the default number of threads is 1.


---

Comment by jdemeyer created at 2011-11-14 08:23:38

Replying to [comment:39 jhpalmieri]:
> For doc building, we shouldn't assume parallel building by default, I guess, so the default number of threads is 1.

Indeed!


---

Comment by jdemeyer created at 2011-11-14 09:24:54

Replying to [comment:39 jhpalmieri]:
> Here's a new patch which uses the setting of `MAKE` to build docs in parallel (or not).  It's very similar to the code in `sage-ptest` from #12016, except that when you run `sage-ptest`, the assumption should be that you want to work in parallel, so the default number of threads (if MAKE is not set) is min(8, #cpus).  For doc building, we shouldn't assume parallel building by default, I guess, so the default number of threads is 1.

So then we don't need the environment variable `SAGE_PARALLEL_DOCBUILD`, nor the `Makefile` patch, anymore.


---

Comment by jdemeyer created at 2011-11-14 09:24:54

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2011-11-14 11:48:17

With sage-4.8.alpha1, I get

```
Building reference manual, first pass.

sphinx-build -b html -d /mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha2/devel/sage/doc/output/doctrees/en/reference   -A hide_pdf_links=1 -Q  /mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha2/devel/sage/doc/en/reference /mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha2/devel/sage/doc/output/html/en/reference
Build finished.  The built documents can be found in /mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha2/devel/sage/doc/output/html/en/reference
Traceback (most recent call last):
  File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha2/devel/sage/doc/common/builder.py", line 1332, in <module>
    getattr(get_builder(name), type)()
  File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha2/devel/sage/doc/common/builder.py", line 288, in _wrapper
    getattr(get_builder(document), 'html')(*args, **kwds)
  File "/mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha2/devel/sage/doc/common/builder.py", line 405, in _wrapper
    N = re.search('(-j|--jobs[=]?)\s*([0-9]*)', MAKE).groups()[1]
UnboundLocalError: local variable 're' referenced before assignment
make: *** [doc-html] Error 1
```



---

Comment by jhpalmieri created at 2011-11-14 20:56:44

> So then we don't need the environment variable SAGE_PARALLEL_DOCBUILD, nor the Makefile patch, anymore.

Right, fixed.  Also, I added `import re` into builder.py; this should fix the other problem as well.


---

Comment by jhpalmieri created at 2011-11-14 20:56:44

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2011-11-16 04:30:03

This now uses `SAGE_NUM_THREADS` from #12016.


---

Comment by jdemeyer created at 2011-12-10 13:51:21

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2011-12-10 13:51:21

Regarding #12016: you should simply use the value of `SAGE_NUM_THREADS`, nothing fancier than that.

Regarding `spkg-dist`: this is essentially a duplicate of #12081 and #12086, so this patch should be removed.  In any case, removing the files from `MANIFEST.in` is the proper way of dealing with this, as opposed to removing the files before packaging the repository.  Ideally, `sage-sdist` should not change the current Sage source tree at all.

What's the rationale for adding all these files to `doc/common/themes/sageref`?

Instead of always building twice, would it be possible to *detect* whether the manual has already been built once.  For example, if I want both the HTML and PDF documentation, the current patch would do 4 passes, even if 3 would be sufficient.


---

Comment by jhpalmieri created at 2012-04-18 04:42:21

Changing keywords from "sd32" to "".


---

Comment by jhpalmieri created at 2012-04-18 04:42:21

Rebased to 5.0.beta13, but the intersphinx stuff needs fixing (the use of intersphinx here conflicts with the changes in #9128, and I haven't fixed this).  Part 1 of the patch was mostly generated automatically using the attached script. After running the script, I removed lines like `.. _ch:algebras:` (from algebras/index.rst, in this case) by hand.

Replying to [comment:45 jdemeyer]:
> Regarding #12016: you should simply use the value of `SAGE_NUM_THREADS`, nothing fancier than that.

Okay, done.

> Regarding `spkg-dist`: this is essentially a duplicate of #12081 and #12086, so this patch should be removed.  In any case, removing the files from `MANIFEST.in` is the proper way of dealing with this, as opposed to removing the files before packaging the repository.  Ideally, `sage-sdist` should not change the current Sage source tree at all.

I removed that part of the patch.

> What's the rationale for adding all these files to `doc/common/themes/sageref`?

The new structure of the reference manual, in particular the new directory structure, means we need new templates for the files coming from `reference/algebras/index.rst`, as opposed to the old templates, which work for the main file `reference/index.rst`.

> Instead of always building twice, would it be possible to *detect* whether the manual has already been built once.  For example, if I want both the HTML and PDF documentation, the current patch would do 4 passes, even if 3 would be sufficient.

I don't know how to do this.


---

Comment by jdemeyer created at 2012-04-18 11:13:18

This patch would allow building the reference manual with less memory usage.  1.5GB (still a lot) is sufficient to build the manual, as opposed to more than 2GB without the patch.


---

Comment by jdemeyer created at 2012-04-18 11:18:03

I do get several warnings when building the HTML manual.  The following is repeated many times:

```
sphinx-build -b html -d /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/doctrees/de/tutorial   -A hide_pdf_links=1  /fast_scr
atch/jdemeyer/sage-5.0.beta13/devel/sage/doc/de/tutorial /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/html/de/tutorial
Running Sphinx v1.1.2
loading translations [de]... done
loading pickled environment... not yet created
loading intersphinx inventory from /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/common/python.inv...
loading intersphinx inventory from /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/html/en/reference/objects.inv...
WARNING: intersphinx inventory '/fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/html/en/reference/objects.inv' not fetchable
due to <type 'exceptions.IOError'>: [Errno 2] No such file or directory: '/fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/htm
l/en/reference/objects.inv'
building [html]: targets for 22 source files that are out of date
updating environment: 22 added, 0 changed, 0 removed
[...]
Build finished.  The built documents can be found in /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/html/de/tutorial
```


There are several of the form:

```
sphinx-build -b html -d /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/doctrees/en/reference/schemes   -A hide_pdf_links=1  -q  -a  /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/en/reference/schemes /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/html/en/reference/schemes
None:37: WARNING: citation not found: Fulton
Build finished.  The built documents can be found in /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/html/en/reference/schemes
```



---

Comment by jhpalmieri created at 2012-04-18 17:04:49

The intersphinx stuff actually seems to be working, despite [comment:47 my earlier comment]. I'll keep testing it to make sure, but I think it's okay.

Regarding the warnings: the missing intersphinx inventories are expected. That's why we have to build everything twice: once to create all of the inventory files, and then a second time to use them. At least for me, if I run `sage --docbuild reference html` twice in a row, I don't get these warnings the second time through. The citation warnings need to be fixed, though.


---

Comment by hivert created at 2012-04-20 22:12:58

Hi John,

What is the status of this one ? It this robust ?

I'm quite glad that I didn't stomp on your foot with #9128, but I may be right
now in the process on jumping high to land on your foot ;-/: I just dived deep
inside Sphinx and using ``@`parallel`, I managed to have the "writing
output..." part of the doc compilation in parallel. I've right now no idea how
robust it is. I'll put a log of my experiment on #6255. Also, it seems
possible that the read part could also be made parallel.

Florent


---

Comment by jhpalmieri created at 2012-04-20 22:26:25

Hi Florent,

This is in pretty good shape, but it's not perfect. It undoes some of what you did in #9128 (mainly because I haven't tried to rewrite the patch to do it differently), and in particular, I'm not sure that the other parts of the Sage documentation can use intersphinx to access information from the reference manual. Citations may be an issue, in particular if the same reference is cited twice in two different parts of the reference manual: we may just need to add another copy of the citation, or perhaps a master list of citations that gets used by everything. I don't know if that's practical.

There are also issues with having to build the reference manual twice so that all of the references are resolved. This is not ideal.

I think that doing the reading and/or writing in parallel would be good, but given the size of the reference manual, breaking it into pieces seems worthwhile as well. If the parallel reading and writing help to cut down on the memory usage, which seems to be getting out of hand, then maybe that is good enough for now.  (At least on sage.math, the writing part seems to take way too long, so doing that in parallel might help significantly.)

So if you have a workable solution which accomplishes some of what is done here, and perhaps does it more simply, go right ahead. I'll take a look at your comments at #6255.

John


---

Comment by hivert created at 2012-04-20 22:45:40

Hi John,

Thanks for the quick answer.

> This is in pretty good shape, but it's not perfect. It undoes some of what
> you did in #9128 (mainly because I haven't tried to rewrite the patch to do
> it differently), and in particular, I'm not sure that the other parts of the
> Sage documentation can use intersphinx to access information from the
> reference manual.

I'll have a look at it. Please do not hesitate to ask for some more
explanation on the hack I did with intersphinx. Is there a specific reason why
you doubt intersphinx will work for the other part of the doc ?

> There are also issues with having to build the reference manual twice so
> that all of the references are resolved. This is not ideal.

It doesn't seem to be a huge problem with LaTeX, since this never has been
solved since years... Though I never seen a LaTeX compilation as long as
Sage's doc.

> I think that doing the reading and/or writing in parallel would be good, but
> given the size of the reference manual, breaking it into pieces seems
> worthwhile as well.

I agree.

> If the parallel reading and writing help to cut down on the memory usage,
> which seems to be getting out of hand, then maybe that is good enough for
> now.  (At least on sage.math, the writing part seems to take way too long,
> so doing that in parallel might help significantly.)

I don't think it will cut down memory usage in any way. I'd rather expect the
contrary. My solution seems to be working but since I currently for a sage for
every single file, a lot of time is wasted in forking. I'll try to improve it
tomorrow.

> So if you have a workable solution which accomplishes some of what is done
> here, and perhaps does it more simply, go right ahead. I'll take a look at
> your comments at #6255.

I don't think I really will. As I said I'll probably trade speed against
memory usage... I'll keep you in touch.

Cheers,

Florent


---

Comment by jdemeyer created at 2012-04-21 10:18:11

Replying to [comment:54 hivert]:
> I don't think it will cut down memory usage in any way. I'd rather expect the
> contrary.
Memory usage is already too much, so anything that further increases memory usage is very bad.


---

Comment by hivert created at 2012-04-21 11:24:49

Replying to [comment:55 jdemeyer]:
> Replying to [comment:54 hivert]:
> > I don't think it will cut down memory usage in any way. I'd rather expect the
> > contrary.
> Memory usage is already too much, so anything that further increases memory usage is very bad.

I respectfully disagree if 
- it is optional
- it divide by more than 10 the documentation compile time


---

Comment by leif created at 2012-04-21 13:32:53

Replying to [comment:56 hivert]:
> Replying to [comment:55 jdemeyer]:
> > Replying to [comment:54 hivert]:
> > > I don't think it will cut down memory usage in any way. I'd rather expect the
> > > contrary.
> > Memory usage is already too much, so anything that further increases memory usage is very bad.

Like adding more modules and functions to the Sage library, and rising the "doc[test] coverage"... ;-)




> I respectfully disagree if 
> - it is optional

That would be fine.

> - it divides by more than 10 the documentation compile time

Wow... :P


---

Comment by hivert created at 2012-04-23 16:33:50

This is an _extremely_ useful patch which should go in Sage ASAP. It
effectively reduce the compilation time to 10min on my I7 laptop. This is
brilliant. It will certainly prove more maintainable in the long term than my
parallelization of Sphinx expertiment. Though, I think we should discuss of is
with Georges Brandl (the maintainer of Sphinx).

I'm now reviewing the code itself. You'll find below some comments.

Florent

*Suggestion of improvement*:

- I think we should get rid of the warning on the first pass, maybe by
  patching a little bit intersphinx. Also, now the compilation is a lot more
  verbose. Maybe we should silent the info for loading the bunch of
  intersphinx load at least in `reference/*`. If you agree with the idea,
  I'm Ok to look at this one.

- Some directories are much longer than the other (eg: combinat) they should
  be launched first (or maybe in this case broken in even smaller parts). This
  could wait for another ticket.

*Some remaining problems*:

- Interrupting the compilation with `ctrl+C` doesn't work. I had to kill
  by hand the master compilation process. I'm not sure what we can do for
  solving this problem.

- On the main page, you managed to gather the todos which is great ! Is it
  possible to do the same for the index (mine is empty). The module index is
  moreover broken.


---

Comment by hivert created at 2012-04-23 21:26:09

Hi John, 

Using your patch I realized that for the first stage, you don't need to get the html file only the pickle and `object.inv` file. Did you try to do that ? It seems that this is easily feasible with a custom Builder. I'm currently testing this workflow.

Florent


---

Comment by hivert created at 2012-04-23 21:48:31

Another comment: You should start by building the reference manual and then the other component. Currently in
`class AllBuilder` method `_wrapper` you start by building the other documents.

Florent


---

Comment by hivert created at 2012-04-23 21:59:24

I just attached a new patch which defines a new builder for creating the pickle and `object.inv` file. It can be called by 

```
sage -docbuild DOCUMENT invpickle
```

It is automatically called for the first pass when building `DOCUMENT=all`. As a consequence on my laptop the first pass in only 2 min and a half long. 

Florent


---

Comment by hivert created at 2012-04-23 22:24:38

The `invpickle` builder seem quite efficient here are the timing on my I7 laptop:
- First stage:  02:36
- Second Stage: 08:06
Without my patch the first stage is 10:19 long. 

Florent


---

Comment by hivert created at 2012-04-23 23:03:36

There is also a failure:

```
sage -t  builder.py
File "/home/data/Sage-Install/sage-5.0.beta13/devel/sage-doc/doc/common/builder.py", line 862:
    [...]
    sage: builder.ReferenceBuilder("reference").auto_rest_filename("sage.combinat.partition")
      File "/home/data/Sage-Install/sage-5.0.beta13/devel/sage/doc/common/builder.py", line 409, in _wrapper
        getattr(DocBuilder(self.name, lang), format)(*args, **kwds)
    AttributeError: 'DocBuilder' object has no attribute 'auto_rest_filename'
```



---

Comment by jhpalmieri created at 2012-04-24 17:09:35

Hi Florent,

Your ideas look great; I hope you can keep working on them. I am happy with all of your suggestions. In particular:

 - building the reference manual before the other documents is fine. I think that was your approach in #9128, and the original patch here built the reference manual last. I hadn't gotten around to changing it to build the reference manual first.

 - I'll try to take a look at combining the indices, the way the todo lists are combined.

 - further subdividing combinat (for example) is a good idea, but I also agree that it belongs on another ticket.

 - I've also noticed that ctrl-C doesn't quit the process. Any ideas why? Should we run the parallel processes differently, maybe using the methods you suggested at #6255?

By the way, mpatel should get a lot of the credit for this; he wrote the original patches, which I've just cleaned up and reorganized.


---

Comment by jhpalmieri created at 2012-04-24 18:40:53

I got two doctest failures (after applying your patch), which can be fixed with this patch:

```diff
diff --git a/doc/common/builder.py b/doc/common/builder.py
--- a/doc/common/builder.py
+++ b/doc/common/builder.py
`@``@` -200,7 +200,7 `@``@` class DocBuilder(object):
             sage: import os, sys; sys.path.append(os.environ['SAGE_DOC']+'/common/'); import builder
             sage: b = builder.DocBuilder('tutorial')
             sage: b._output_formats()
-            ['changes', 'html', 'htmlhelp', 'json', 'latex', 'linkcheck', 'pickle', 'web']
+            ['changes', 'html', 'htmlhelp', 'invpickle', 'json', 'latex', 'linkcheck', 'pickle', 'web']
 
         """
         #Go through all the attributes of self and check to
`@``@` -859,7 +859,7 `@``@` class ReferenceSubBuilder(DocBuilder):
 
             sage: import os, sys; sys.path.append(os.environ['SAGE_DOC']+'/common/'); import builder
             sage: import builder
-            sage: builder.ReferenceBuilder("reference").auto_rest_filename("sage.combinat.partition")
+            sage: builder.ReferenceSubBuilder("reference").auto_rest_filename("sage.combinat.partition")
             '.../devel/sage/doc/en/reference/sage/combinat/partition.rst'
         """
         return self.dir + os.path.sep + module_name.replace('.',os.path.sep) + '.rst'
```



---

Comment by jhpalmieri created at 2012-04-24 18:53:09

By the way, searching is broken with these patches. The files `searchindex.js` (both in `reference/` and in its various subdirectories) are all essentially empty.  Hmm.

It looks like combining the indices should be doable, but a little annoying: read in the html from each, extract the entries, sort them, and rewrite to a new index file. The same should work for the module index. I think talking to Georg Brandl makes sense: if we wanted Sphinx to support this kind of thing out of the box, what exactly would we be looking for?  I guess at the least we want separate Sphinx documents which share indices, searches, and inventories. It would be nice to have a specific "Sphinx Enhancement Proposal", or even some code to contribute.


---

Comment by hivert created at 2012-04-24 23:36:09

Hi John,

Another reason to have this in Sage ASAP: #12878

I'm willing to help on this one but we need to coordinate. I'll be in Montreal
for the next Sage days 38 so hopefully will have so time for Sphinx. Do you think
you'll have so time on it in the forthcoming weeks ? Please tell me what I can
do to help. Here are a few suggestions:

- *avoiding to build the full doc twice*: If you agree with the idea of
  the invpicke builder, I can polish it a little more. Also the name is far
  from being perfect and I'm open to any suggestion.

- *Intersphinx being too verbose*: I don't think we can silence
  intersphinx a little without patching Sphinx. I can try to do it by some
  Monkey patch.

- *Parallelizing the rests of the doc*: I noticed that the refman is build
  in parallel but the other documents are build in series. We should build
  them in parallel too. I'll look for the easiest way.

Cheers,

Florent


---

Comment by jhpalmieri created at 2012-04-25 03:59:51

I hope I have time to work on it next week, although right now I have other things I need to be doing (like reading my student's PhD thesis).

 - I really like the idea of the invpickle builder, so please continue with that. I don't have any better suggestions for the name.
 - The verbosity of intersphinx is a minor issue. If we can reduce it, that would be fine, but it's not the highest priority, in my opinion.
 - I think it shouldn't be too hard to parallelize building the rest of the docs. We want to do it so that hitting ctrl-c will quit the build. I think we should try using tools from sage.parallel rather than the Python multiprocessing module. If you want to work on that, that would be great.

Also:

 - I can try to work on the indices.
 - I will investigate why the searchindex.js files are empty, but right now I have no idea.

I will try to post any progress that I make, and you should do likewise, so we don't end up duplicating each other's work.


---

Comment by jhpalmieri created at 2012-04-25 05:25:44

As far as handling ctrl-c, I found [this question](http://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-pool). It seems we can replace `pool.apply_async(ARGS)` with `pool.apply_async(ARGS).get(999999)`. This apparently adds a (very long) timeout to the process, and it apparently works around a bug in Python. In practice, it seems to work for me.

```diff
diff --git a/doc/common/builder.py b/doc/common/builder.py
--- a/doc/common/builder.py
+++ b/doc/common/builder.py
`@``@` -415,7 +415,7 `@``@` class ReferenceBuilder(AllBuilder):
             for doc in self.get_all_documents(refdir):
                 pool.apply_async(build_ref_doc,
                                  (doc, lang, format,
-                                  os.path.split(output_dir)[0]) + args, kwds)
+                                  os.path.split(output_dir)[0]) + args, kwds).get(999999)
             pool.close()
             pool.join()
             if format == 'html':
```



---

Comment by leif created at 2012-04-25 05:40:39

Replying to [comment:68 jhpalmieri]:
>  - I really like the idea of the invpickle builder, so please continue with that. I don't have any better suggestions for the name.

One should perhaps just expand the name to contain "inventory"; "pickle" is IMHO minor (or irrelevant) and won't tell most(?) people much.
 
>  - The verbosity of intersphinx is a minor issue. If we can reduce it, that would be fine, but it's not the highest priority, in my opinion.

Mine, too.  Although I hate Sphinx's / Sage's current messages already, especially since _"Build succeeded.  The built documents can be found in ..."_ is *always* printed, so is plain wrong in case of an error.  (We tried to fix that once, but then I think Jeroen decided to keep it as is.)

>  - I think it shouldn't be too hard to parallelize building the rest of the docs. We want to do it so that hitting ctrl-c will quit the build. I think we should try using tools from sage.parallel rather than the Python multiprocessing module. If you want to work on that, that would be great.

Why not just use `make`?  Either add (and change the) targets in the top-level `Makefile`, or add one to `devel/sage/doc/`.  To me seems cleanest (preferably the latter), and docbuilding IMHO shouldn't depend [more] on the Sage library [as needed / it already does].


---

Comment by jhpalmieri created at 2012-04-25 17:16:03

The problem with using `make` is that I want to be able to run `sage --docbuild all html`, and I don't think that running this should call `make`. The fix I mentioned above for interrupts (adding a timeout) doesn't make use of the sage.parallel module, just plain Python, by the way. So we should be able to do this for building all of the documents in parallel.


---

Comment by hivert created at 2012-05-01 20:26:59

Replying to [comment:69 jhpalmieri]:
> As far as handling ctrl-c, I found [this question](http://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-pool). It seems we can replace `pool.apply_async(ARGS)` with `pool.apply_async(ARGS).get(999999)`. This apparently adds a (very long) timeout to the process, and it apparently works around a bug in Python. In practice, it seems to work for me.

Does it really work ? For me is seems that ctrl-c is now working but the doc is no more compiling in parallel.

Florent


---

Comment by hivert created at 2012-05-01 21:43:22

Concerning todos (and maybe indexes too), I think I've found an alternative:
they are pickled in the files `environment.pickle`. Here is an example, in
the directory `doc/output/doctrees/en/reference/modules`:

```
sage: import cPickle
sage: f = open('environment.pickle', 'rb')
sage: env = cPickle.load(f)
sage: f.close()
sage: env.todo_all_todos
[{'docname': 'sage/modules/free_module', 'source': u'/home/data/Sage-Install/sage-5.0.beta14/local/lib/python2.7/site-packages/sage/modules/free_module.py:docstring of sage.modules.free_module.FreeModuleFactory', 'todo': <todo_node: <title...><paragraph...>>, 'lineno': 122, 'target': <target: >}]
sage: env.indexentries.keys()
['index', 'sage/modules/free_module_element', 'sage/modules/real_double_vector', 'sage/modules/matrix_morphism', 'sage/modules/fg_pid/fgp_module', 'sage/modules/free_module_homspace', 'sage/modules/vector_space_homspace', 'sage/modules/fg_pid/fgp_element', 'sage/modules/complex_double_vector', 'sage/modules/fg_pid/fgp_morphism', 'sage/modules/vector_callable_symbolic_dense', 'sage/modules/module', 'sage/modules/free_module_morphism', 'sage/modules/vector_space_morphism', 'sage/modules/free_module']
```

So it seems that we can get them from there from the pickle concatenate them
and let sphinx output the todo list and the index.

Florent


---

Comment by hivert created at 2012-05-01 23:54:00

Replying to [comment:73 hivert]:
> So it seems that we can get them from there from the pickle concatenate them
> and let sphinx output the todo list and the index.

I've a proof of concept which seems to be working upto two problems:

- The generated links to the "original entry" generated by `app.builder.get_relative_uri` is missing the subdirectory (ie: "reference/sage/modules/..." instead of "reference/modules/sage/modules/...". This could probably either be fixed by fixing the builder or playing with symlinks.

- if one recompile the doc twice, all the todos are duplicated. This could probably also be fixed by removing duplicates or clearing the todo-list at the right moment.

I think both problem can be fixed.


---

Comment by hivert created at 2012-05-02 10:57:38

Hi there,

I just uploaded a new [attachment:invbuilder.patch]; you need to apply it after the two mentionned patch in the header of this ticket. It seems to solve the problems of

- merging todo lists
- merging the html indexes

It remains to merge the javascript indexes.

Please tests.

Florent


---

Comment by hivert created at 2012-05-03 16:18:24

I just uploaded a new patch which merge the javascript indexes as well !!! It was a little more tricky but it seems to work now. The only things that remains to be merged is the list of modules. I'll write a proposal to Sphinx for my merging tool.

Florent


---

Comment by hivert created at 2012-05-03 19:38:17

The new version now also merge modules indexes !!! The obtained doc seems to be in quite a good shape.


---

Comment by hivert created at 2012-05-03 23:22:05

inventory builder + merge todo list & html / js indexes


---

Attachment

> Citations may be an issue, in particular if the same reference is cited
> twice in two different parts of the reference manual: we may just need to
> add another copy of the citation, or perhaps a master list of citations that
> gets used by everything. I don't know if that's practical.

I've probably a way to handle cross-citation as well. They are stored in the
environement and I can get them to gather the link in the main reference
manual, exactly the way I gather TODO and indexes. It is just a little more
tricky because I need to redispatch them to the other documents. I'm
experimenting...

Florent


---

Comment by hivert created at 2012-05-07 18:52:41

Changing status from needs_work to needs_review.


---

Attachment

Hi there,

I just uploaded which seems to solve most of the problems we had here,
including merging of
- the todo list if this extension is activated;
- the python indexes;
- the list of python modules;
- the javascript index;
- the citations.

I put a need review though I'm quite not sure everything is ready for
inclusion into Sage. I do need feedback and people shaking my code to see if
it's robust.

Florent


---

Comment by hivert created at 2012-05-07 21:26:03

Changing keywords from "" to "days38".


---

Comment by jhpalmieri created at 2012-05-07 22:25:43

Hi Florent,

I am quite busy with other things right now, so I hope you can get people at Sage Days 38 to take a good look at this. Maybe you can figure out the ctrl-c issue as well; maybe tinkering with what I had might work; if not, the link I provided had some other ideas, too.

Thanks, John


---

Comment by hivert created at 2012-05-08 05:17:01

Hi John,

Replying to [comment:81 jhpalmieri]:
> I am quite busy with other things right now, so I hope you can get people at Sage Days 38 to take a good look at this. Maybe you can figure out the ctrl-c issue as well; maybe tinkering with what I had might work; if not, the link I provided had some other ideas, too.

well, they are very few people knowing the documentation building system here and I used quite a few Sphinx internal stuff. I think a good reviewer would be George Brandle himself but I need to sit for a moment to write him an e-mail.

Cheers,

Florent


---

Comment by mguaypaq created at 2012-05-15 17:28:31

I haven't had time yet to read the whole ticket description and discussion, but I will note that this patch has allowed me to build the documentation on my old laptop (with only 1GB of RAM) in a couple of hours, whereas trying to build it without the patch causes my laptop to become unresponsive and eventually crash. (Also, Florent had a look at the output and seemed satisfied that everything was fine.) So, a huge +1 from me!

I will try to do as much as I can to review this ticket, but I know almost nothing about the documentation building process.


---

Comment by jhpalmieri created at 2012-05-16 05:23:48

After a lot of swearing at my computer, I think I have the ctrl-c situation figured out. We've been using `Pool.apply_async`, and this didn't handle ctrl-c well. Adding a timeout (using the `get` method) caused it to handle interrupts, but it no longer build in parallel.  If we instead use `Pool.map_async` together with `get` to provide a timeout, it seems to work. Please take a look at the new patch.


---

Comment by jhpalmieri created at 2012-05-16 21:15:12

Several quick comments and questions:

 - First, the combined indices and search are great! At first I thought that searching was broken, but that's my browser, not the code. I'm still looking over the patch, but in practice it seems to work.
 - This is an old problem: I object to the use of "type" as a global variable, set by `__main__`. Then I can't use `print type(var)` anywhere in the rest of the code (as I tried to do when debugging something). I may change `type` to something else; any suggestions? Perhaps `format` (which also has a meaning in Python)?
 - When we're happy about the patches, I'll try to combine them into just one or two chunks. Right now, for example, one of my patches creates the "todolist" directory, and then Florent's patch moves all of the files out of it, so we end up with an empty directory. I don't know if there are other similar things which will need cleaning up.
 - I get some warnings about missing citations. Should we worry about those now?


---

Comment by jhpalmieri created at 2012-05-16 21:56:56

I've modified the part 4 patch to do a little cleanup:

 - I moved the detection of the number of threads to `build_options.py`, and expanded on the comment about loading `build_options.py`. This way if someone is reading `builder.py` and wants to know where `NUM_THREADS` is defined, at least they'll find a comment pointing them to that file.
 - I modified the `mkdir` function, making it a bit more secure: the new approach seems to be preferred, as far as I can tell.


---

Comment by jhpalmieri created at 2012-05-18 01:23:43

Another update to part 4: fix the main index.html file for the pdf build of the reference manual.


---

Comment by jhpalmieri created at 2012-05-19 05:12:35

One more update to part 4, to fix a few doctests.


---

Comment by jhpalmieri created at 2012-05-21 20:11:46

I think this looks very good. I'm just about ready to give Florent's part a positive review. Two questions: can we reinstate the `-Q` flag for the first pass on the reference manual, to silence all of the warnings? Also, I see this warning message; do you know if it's important?

```
preparing documents... WARNING: search index couldn't be loaded, but not all documents will be built: the index will be incomplete.
```

(This occurs if I do `sage --docbuild all html`, at the end of the second pass through the reference manual.)

I'm attaching one more version of the part 4 patch, just to fix a few typos and grammar issues in the files Florent added.


---

Comment by hivert created at 2012-05-21 22:36:14

Hi John,

> I think this looks very good. I'm just about ready to give Florent's part a
> positive review.

Wow !!! This is extremely cool. Thanks a lot ! I'm sorry for my current
silence. I didn't had the time to look at your part4 code. I'll try to do it
shortly.

> Two questions: can we reinstate the `-Q` flag for the first pass on the
> reference manual, to silence all of the warnings?

No problem. I just wanted to have some idea of the progress and forgot to
switch back to a silent mode.

> Also, I see this warning message; do you know if it's important?

```
preparing documents... WARNING: search index couldn't be loaded, but not all documents will be built: the index will be incomplete.
```

> (This occurs if I do `sage --docbuild all html`, at the end of the second
pass through the reference manual.)

I'm not sure now. I'll though I had silenced this warning. Give me a few day
to investigate a little more. It is probably not important as the produced
index is correct but I may be missing to merge somme part of it.

> I'm attaching one more version of the part 4 patch, just to fix a few typos
> and grammar issues in the files Florent added.

Thanks for those rereading. I planned to polish more the code and try to get
some feedback from Sphinx and didn't find the time. However I now think that
we should let the code enter sage as soon as possible because it allows the
doc to compile on small machine. At sage days 48, with mguaypaq (see above) we
manage to compile the documentation in a seemingly satisfactory way on a 1GB
machine. Moreover its a requirement to the feature #12878 which I think is
definitely needed at least for huge classes such as graphs...

Thanks a lot,

Florent


---

Comment by jhpalmieri created at 2012-05-22 20:54:32

See #12991 for a peripherally-related ticket: don't doctest the autogenerated rst files.


---

Comment by jdemeyer created at 2012-06-19 13:42:40

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2012-06-19 13:42:40

This needs to be rebased to sage-5.1.beta5:

```
applying /release/merger/patches/trac_6495-part2-everything-else.patch
patching file doc/en/reference/combinat/index.rst
Hunk #1 FAILED at 3
1 out of 2 hunks FAILED -- saving rejects to file doc/en/reference/combinat/index.rst.rej
patching file doc/en/reference/misc/index.rst
Hunk #1 succeeded at 31 with fuzz 1 (offset 3 lines).
abort: patch failed to apply
```



---

Comment by jhpalmieri created at 2012-06-19 22:12:35

Okay, this is now rebased.


---

Comment by jhpalmieri created at 2012-06-19 22:12:35

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2012-06-20 03:04:45

I've added a link to the built documents for Sage 5.1.beta5, in case anyone wants to look at it without applying the patches here. The reference manual is organized differently and as a result looks different. The other documents should be unchanged.


---

Comment by jhpalmieri created at 2012-06-20 21:44:37

This now depends on #9774. If you want to try it without the patches at #9774 (thus using jsMath instead of MathJax), apply [attachment:trac_6495-part2-everything-else.patch] instead of [attachment:trac_6495-part2-everything-else-9774.patch].


---

Comment by jhpalmieri created at 2012-06-22 17:58:22

A slight issue with the reference manual is that it takes up a little more room, and most of the difference is in `devel/sage/doc/output/doctrees`. There is some redundancy in the `environment.pickle` files. I wonder if there is any way to avoid this. 

In more detail: using MathJax instead of jsMath saves room in the directory `doc/output/html`: with the old version, jsMath and non-parallel, that directory takes about 325M, while the new version, MathJax and parallel, takes about 200M, saving 125M. Unfortunately, the doctree directory has increased by about 150M, so the whole thing has gone up by 25M. Not a big difference, but if there were a way to improve it, it would be nice. Maybe on another ticket...


---

Comment by jdemeyer created at 2012-06-25 10:34:11

Clarified recursive dependencies.


---

Comment by jdemeyer created at 2012-06-27 07:47:18

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2012-06-27 07:47:18

I get tons of warnings (1043 to be precise) when building the manuals.  I don't like this, because it's hard to distinguish warnings due to this ticket with true warnings about bad formatting.  Is there a way not to produce any warnings during the first run (I assume the warnings should only appear in the first run)?


---

Comment by jhpalmieri created at 2012-06-27 20:42:50

Rebased because of #12299. I'll try to work on the warnings. I think it might be best to only suppress the warnings when you run `sage --docbuild all html`, because that is when both passes of the reference manual are actually run, and the first pass is designed to be fast: it just produces the inventory files, not html output. If you run `sage --docbuild reference html`, then it will just do one pass, html format.

Edit: actually, the warnings are easy to get rid of. Florent intentionally left them there while working on the ticket: see these lines in builder.py:

```python
        global ALLSPHINXOPTS
        # ALLSPHINXOPTS += ' -Q -D multidoc_first_pass=1'
        ALLSPHINXOPTS += ' -D multidoc_first_pass=1'
```

If we uncomment the second line and remove the third, the warnings will go away. I'll incorporate this change into the 4th patch.


---

Comment by jhpalmieri created at 2012-06-27 20:47:20

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2012-06-27 21:33:43

I see one warning now:

```
WARNING: search index couldn't be loaded, but not all documents will be built: the index will be incomplete.
```

I don't know what this means. The search index looks pretty good to me. Florent might have some idea, when he has a chance to look at this.


---

Comment by jhpalmieri created at 2012-07-10 04:14:43

In addition to the warning mentioned [comment:105 in comment #105], I have a question about `.buildinfo` files. It seems that on the first pass through the reference manual, these files contain lines like

```
config: 6a23e6beb735e39dc46994bfb813cf55
tags: fbb0d17656682115ca4d033fb2f83ba1
```

On the second pass, these files get overwritten, and the new files have

```
config:
tags:
```

Then running `sage --docbuild reference all` produces warnings like

```
WARNING: unsupported build info format in '.../devel/sage/doc/output/html/en/reference/libs/.buildinfo', building all
```

and then everything is rebuilt again. I propose this change, which seems to fix this issue:

```diff
diff --git a/doc/common/builder.py b/doc/common/builder.py
--- a/doc/common/builder.py
+++ b/doc/common/builder.py
`@``@` -300,7 +300,7 `@``@` class AllBuilder(object):
         logger.warning("Building reference manual, second pass.\n")
         ALLSPHINXOPTS = ALLSPHINXOPTS.replace(
             'multidoc_first_pass=1', 'multidoc_first_pass=0')
-        ALLSPHINXOPTS = ALLSPHINXOPTS.replace('-Q', '-q') + ' -a '
+        ALLSPHINXOPTS = ALLSPHINXOPTS.replace('-Q', '-q') + ' '
         for document in refs:
             getattr(get_builder(document), name)(*args, **kwds)
 
```



---

Comment by jhpalmieri created at 2012-07-10 13:50:44

apply second (if you've applied the patches at #9774)


---

Attachment


---

Comment by jhpalmieri created at 2012-09-11 05:27:58

Rebased to Sage 5.4.beta0.


---

Comment by jhpalmieri created at 2012-09-11 22:18:27

Florent: any chance you can work on this? I think that the only thing needed reviewing is the part 4 patch. (There is also the warning at [comment:105 comment 105], but I think that the actual output is good, so suppressing the warning would be nice but not absolutely necessary. You might also look at [comment:110 comment 110], but I can't reproduce that issue right now.)


---

Comment by hivert created at 2012-09-12 05:58:26

Hi John,

Replying to [comment:118 jhpalmieri]:
> Florent: any chance you can work on this? I think that the only thing needed reviewing is the part 4 patch. (There is also the warning at [comment:105 comment 105], but I think that the actual output is good, so suppressing the warning would be nice but not absolutely necessary. You might also look at [comment:110 comment 110], but I can't reproduce that issue right now.)

Yes ! And thanks for your work and your patience. This is very high on my
priority list, but it has to remain after the list "things that must be done
right now" (such as teaching or meeting the dead-line to get money for
Sage-Combinat) or even "thing that should have been done
yesterday". Unfortunately, until the end of September, I will still be moving
a flat, so I definitely won't be able to work during the Week-End. I
definitely want to do this done ASAP. So I didn't give-up, but the summer
didn't went as expected and I had to stop working on sage for a few
month. Please ping me in the first week of October if I didn't manage to do it
.

Cheers,

Florent


---

Comment by jhpalmieri created at 2012-09-13 21:58:39

Rebased to Sage 5.4.beta1.


---

Comment by jhpalmieri created at 2012-10-01 15:52:44

Made #13143 a dependency and rebased to that.


---

Comment by hivert created at 2012-10-01 19:47:58

Hi John,

Replying to [comment:121 jhpalmieri]:
> Made #13143 a dependency and rebased to that.

Consider me as pinged. And don't hesitate to email me more aggressively if nothing come up before the end of the week. 

Florent


---

Attachment

Rebased to #13143 and Sage 5.4.rc2 (because of changes to builder.py in #13579).


---

Comment by kcrisman created at 2012-12-13 02:49:19

John, I've tried to use this on an existing Sage installation (well, previous versions of this) a few different times, and it always ends up causing problems, even when I delete the whole output directory.   Is there something to do other than apply the all-in-one patch, delete output, do `sage -b`, and start building docs?  For instance, is there an env var (e.g. `SAGE_NUM_THREADS`) to set or something?  I feel like I must have done something obvious wrong...

On a related note, this no longer applies :-(


---

Comment by kcrisman created at 2012-12-13 02:49:19

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2012-12-13 16:28:57

What sort of problems do you see? As far as environment variables, setting `MAKE` is the right thing to do: `export MAKE='make -j2'` for example.

I just rebased the patches on top of 5.5.rc0.


---

Comment by jhpalmieri created at 2012-12-13 16:34:58

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2012-12-13 17:29:55

> What sort of problems do you see? As far as environment variables, setting `MAKE` is the right thing to do: `export MAKE='make -j2'` for example.

Lots of 

```
WARNING: intersphinx inventory '/Users/.../sage-5.5.rc0/devel/sage/doc/output/html/en/reference/monoids/objects.inv' not fetchable due to <type 'exceptions.IOError'>: [Errno 2] No such file or directory: '/Users/.../sage-5.5.rc0/devel/sage/doc/output/html/en/reference/monoids/objects.inv'
```

stuff.

```
build succeeded, 1074 warnings.
```

That's while building `reference html`, and now I see upon careful reading of the ticket description that perhaps that's implicitly expected.  When I build the whole documentation as a target, I don't get this problem, though I do get one warning:

```
WARNING: search index couldn't be loaded, but not all documents will be built: the index will be incomplete.
```



---

Comment by jhpalmieri created at 2012-12-13 18:28:51

Yes, the warnings are somewhat expected. Those are like what happens when you run LaTeX on a file for the first time: all of the unknown reference warnings which get resolved the second time through. I think typically people will do the following:

- either build Sage from scratch or download a binary. In the first case, `sage --docbuild all html` will get run and so the intersphinx warnings have been turned off explicitly in this case. I also get the one about "search index couldn't be loaded...". I don't know the cause of that; Florent might be able to help.

- then modify parts of the Sage library and do `sage --docbuild reference html` or `sage --docbuild reference/combinat html` or .... At this point, the various parts of the reference manual have been built along with their intersphinx inventories, so there shouldn't be any intersphinx warnings.

That is, I hope that most users/developers won't see all of these warnings. I've updated the ticket description so it mentions the warnings. (We could turn off all of the warnings all of the time, but I don't think that's a good idea.)


---

Comment by jdemeyer created at 2012-12-19 20:44:06

I consider it a requirement that there are no visible warnings/errors when building the documentation from scratch. Otherwise, it becomes difficult to differentiate warnings caused by this ticket from true warnings.


---

Comment by jdemeyer created at 2013-01-03 15:29:22

Does this patch enable links like `:func:`plot()`` from other manuals (e.g. the developer manual) to the reference manual?


---

Comment by kcrisman created at 2013-01-03 19:59:02

> I consider it a requirement that there are no visible warnings/errors when building the documentation from scratch. Otherwise, it becomes difficult to differentiate warnings caused by this ticket from true warnings.
John, is this even possible under this setup? It would really be a shame to hold this up but Jeroen makes a good point as well.


---

Comment by jhpalmieri created at 2013-01-03 20:06:39

Replying to [comment:132 jdemeyer]:
> Does this patch enable links like `:func:`plot()`` from other manuals (e.g. the developer manual) to the reference manual?

I think so, but it ought to be tested. You might need to specify the cross-reference more explicitly, the way you might if you want to reference the Python docs, for instance.

Replying to [comment:133 kcrisman]:
> > I consider it a requirement that there are no visible warnings/errors when building the documentation from scratch. Otherwise, it becomes difficult to differentiate warnings caused by this ticket from true warnings.
> John, is this even possible under this setup? It would really be a shame to hold this up but Jeroen makes a good point as well.

I thought that Florent had ideas about how to get rid of the one remaining warning. (As I said before, the intersphinx warnings are turned off on the first pass through the reference manual when you do `sage --docbuild all html`, and I think this is appropriate.)

I'll try to look into both of these. Anyone else is welcome, also. Florent, do you have any time these days?


---

Comment by dimpase created at 2013-01-11 12:57:53

please rebase for 5.6.beta3:

```
$sage-5.6.beta3/devel/sage$ ../../sage -hg qpushapplying trac_6495-all-in-one.patch
patching file doc/en/reference/combinat/index.rst
Hunk #1 FAILED at 3
1 out of 3 hunks FAILED -- saving rejects to file doc/en/reference/combinat/index.rst.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_6495-all-in-one.patch
```



---

Comment by hivert created at 2013-01-11 13:48:03

Replying to [comment:134 jhpalmieri]:
> I thought that Florent had ideas about how to get rid of the one remaining warning. (As I said before, the intersphinx warnings are turned off on the first pass through the reference manual when you do `sage --docbuild all html`, and I think this is appropriate.)
> 
> I'll try to look into both of these. Anyone else is welcome, also. Florent, do you have any time these days?

I'm deeply sorry for letting time pass and not finishing this one... I'll be in Sage-Days in Edimbourg in two weeks so I hopefully will finish this one.

Florent


---

Comment by Snark created at 2013-01-11 22:19:18

I did the following:
* Apply the patch against 5.5 - there was fuzz
* Run sage -b - ok
* Run sage -docbuild all html - ok
* Run sage -docbuild all pdf - error at the ru/tutorial stage, because I don't have cyrillic encoding definitions available for babel

Does that help?


---

Comment by jhpalmieri created at 2013-01-11 22:46:58

Snark: is that specific to this ticket, or does `sage --docbuild ru/tutorial pdf` fail before applying these patches?


---

Comment by jhpalmieri created at 2013-01-11 22:54:52

Rebased for 5.6.beta3.


---

Comment by Snark created at 2013-01-12 09:02:49

I installed the needed cyrillic support and it went through without problem.


---

Comment by jhpalmieri created at 2013-01-14 16:06:08

Another approach to parallel building (not that we want to throw away all of this work): [a proposed patch to Sphinx](https://bitbucket.org/birkenfeld/sphinx/pull-request/108/wip-parallel-build-experimentation/diff). I don't know if using this proposal would affect Sphinx's memory usage, though, which is another issue that is helped by breaking up the reference manual.


---

Comment by jdemeyer created at 2013-01-14 16:09:51

Replying to [comment:141 jhpalmieri]:
> Another approach to parallel building (not that we want to throw away all of this work): [a proposed patch to Sphinx](https://bitbucket.org/birkenfeld/sphinx/pull-request/108/wip-parallel-build-experimentation/diff).
It only parallelizes the "writing output" phase, not the "reading" phase, so it cannot be that useful.

> I don't know if using this proposal would affect Sphinx's memory usage, though
Most likely not.


---

Comment by jdemeyer created at 2013-01-14 16:40:49

Just for fun, I packaged it: [http://boxen.math.washington.edu/home/jdemeyer/spkg/sphinx-parallel.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/sphinx-parallel.spkg) and made it support the Sage standard MAKE="-j20" mechanism.


---

Comment by hivert created at 2013-01-14 17:54:54

Replying to [comment:142 jdemeyer]:
> It only parallelizes the "writing output" phase, not the "reading" phase, so it cannot be that useful.

This is more or less what I did when experimenting on #6255. At that time, since I was building the whole documentation it increased the memory usage. By the way, we probably should close #6255 at some point as a duplicate of this one.

Florent


---

Comment by jdemeyer created at 2013-01-14 20:54:32

With the parallel Sphinx package I get lots of errors, some might be due to the "upgrade" to the devleopment version of Sphinx 1.2, but some also to the parallel code.


---

Comment by jhpalmieri created at 2013-01-14 22:38:16

I think our Sphinx package needs some work. In particular, the file `SAGE_ROOT/devel/sage/common/sage-autodoc.py` should be part of the Sphinx package, built by patching Sphinx's `autodoc.py`. This would make it easier to incorporate modifications to `autodoc.py`. I don't know if this has to do with the problems with using Sphinx 1.2, but it might.

It's probably also not a good idea to use Sphinx's parallel building at the same time as ours, or else we'll be using more threads than we intended: maybe building 8 pieces of documentation at the same time, and then writing each of those using 8 processes. That sounds like a bad idea to me.

Having said all of that, do the errors you get suggest problems with our parallel code?


---

Comment by jdemeyer created at 2013-01-15 07:09:50

Replying to [comment:146 jhpalmieri]:
> Having said all of that, do the errors you get suggest problems with our parallel code?
I didn't use any code from this ticket, I only used the patch you linked to for parallel Sphinx writing.


---

Attachment

apply third


---

Comment by jhpalmieri created at 2013-01-18 06:42:25

Rebased to 5.6.rc0 (among other things, dealing with the addition of `doc/en/reference/sat.rst`).


---

Comment by hivert created at 2013-01-22 01:34:33

This is an answer to Mike Hansen:

He asked if the page url are kept or not. The answer is that they moved:
For example:

```
doc/output/html/en/reference/sage/symbolic/expression.html
```

is now

```
doc/output/html/en/reference/calculus/sage/symbolic/expression.html
```

So the location is not kept.

Florent


---

Comment by kcrisman created at 2013-01-22 01:36:49

Replying to [comment:149 hivert]:
> This is an answer to Mike Hansen:
> 
> He asked if the page url are kept or not. The answer is that they moved:
Hmm, I was dimly aware of this but didn't think it through.  That will break a loooot of links (e.g., on ask.sagemath.org).  Is there any way to auto-generate forwarding or 'mirrors' from the old pages?


---

Comment by dimpase created at 2013-01-24 04:04:38

Replying to [comment:150 kcrisman]:
> Replying to [comment:149 hivert]:
> > This is an answer to Mike Hansen:
> > 
> > He asked if the page url are kept or not. The answer is that they moved:
> Hmm, I was dimly aware of this but didn't think it through.  That will break a loooot of links (e.g., on ask.sagemath.org).  Is there any way to auto-generate forwarding or 'mirrors' from the old pages?

there are several options:

 1. use `.htaccess` thing to fix this on any particular website;
 
 2.  write a script to look through all `href` targets in each file with changed location, and create for it a file with forwards;

 3.  maybe sphinx can help in this business, I don't know.

In any event we do not want to keep the old links around forever, I think, so there should be some kind of deprecation being turned on.


---

Comment by hivert created at 2013-01-24 10:42:16

> > > He asked if the page url are kept or not. The answer is that they moved:
> > Hmm, I was dimly aware of this but didn't think it through.  That will break a loooot of links (e.g., on ask.sagemath.org).  Is there any way to auto-generate forwarding or 'mirrors' from the old pages?
> 
> there are several options:
> 
>  1. use `.htaccess` thing to fix this on any particular website;
>  
>  2.  write a script to look through all `href` targets in each file with changed location, and create for it a file with forwards;
> 
>  3.  maybe sphinx can help in this business, I don't know.

I don't thinks it does. On the contrary, it makes it a nightmare (at least to me). Sphinx made the assumption that creating a new document needs creating a new directory (storing html, markup, indexes...). Since we splitting the reference manual in different documents we had to move files around.

Mike Hansen was considering implementing something which is close to option 2, because it it seems that option 1 is not easily doable (whereas I'm starting to now more than a little about Sphinx, I shamefully admitting that I don't know how to write/configure a website). 

Florent


---

Comment by vbraun created at 2013-01-24 12:04:29

We should just have versioned documentation on sagemath.org, just like Singular:
  * http://www.singular.uni-kl.de/Manual/3-1-0/index.htm
  * http://www.singular.uni-kl.de/Manual/latest/index.htm
The "latest" manual would then never be stable; independent of this ticket in particular there is always the danger of a module being renamed or moved around.

Having said that, Apache `mod_rewrite` could be used to dull some of the pain and automatically guess the new location.


---

Comment by mhansen created at 2013-01-24 12:41:36

Replying to [comment:154 vbraun]:
> Having said that, Apache `mod_rewrite` could be used to dull some of the pain and automatically guess the new location.

Can you really use mod_rewrite to do this?  You have to turn a request like reference/sage/symbolic/expression.html to something like reference/calculus/sage/symbolic/expression.html .  So, you'd have to walk to filesystem in order to find out the analog of "calculus".


---

Comment by vbraun created at 2013-01-24 12:48:12

Yes and no... its not beautiful but you can just add a rule for each `sage/` subdirectory that does the equivalent of 

```
sed s-sage/symbolic-calculus/sage/symbolic-
```



---

Attachment


---

Comment by mhansen created at 2013-01-24 16:52:56

Replying to [comment:157 vbraun]:
> Yes and no... its not beautiful but you can just add a rule for each `sage/` subdirectory that does the equivalent of 
> {{{
> sed s-sage/symbolic-calculus/sage/symbolic-
> }}}

I don't think that you can really do this since it isn't guaranteed that all of the files that are in say sage/misc/ will all go to the same document.

I wrote a patch which adds small HTML files to do the redirect.  I've looked through Florent's code as well, and things seem fine to me -- trac_6495-all-in-one.patch and trac-6495_silence_warning-fh.patch .

If someone reviews trac_6495-redirect_html.patch , we can mark this as positive_review.


---

Comment by kcrisman created at 2013-01-24 19:22:18

> I wrote a patch which adds small HTML files to do the redirect.  I've looked through Florent's code as well, and things seem fine to me -- trac_6495-all-in-one.patch and trac-6495_silence_warning-fh.patch .
> 
> If someone reviews trac_6495-redirect_html.patch , we can mark this as positive_review.

Thank you so much for adding this, Mike - I hope to try it out tonight and see if it works fine, but I doubt I'll be competent to give positive review.

Here is a question about all the patches.  There are a lot of functions (esp. underscore ones) in doc/... that have no doctests.  Problem?  (This includes Mike's new function, but is not limited to it.)  Hope this isn't evil to ask.


---

Comment by jhpalmieri created at 2013-01-24 20:03:49

I have yet to test [attachment:trac_6495-redirect_html.patch], but the docstring for `html` ends rather abruptly.


---

Comment by jhpalmieri created at 2013-01-24 20:55:03

If I run `sage --docbuild all html`, at the end of the second pass for the reference manual, I see

```
*******************SKIPPING Load indexer call*******************
WARNING: search index couldn't be loaded, but not all documents will be built: the index will be incomplete.
Build finished.  The built documents can be found in /scratch/palmieri/6495/sage-5.7.beta0/devel/sage/doc/output/html/en/reference
```

So the warning isn't gone.


---

Comment by jhpalmieri created at 2013-01-24 22:04:00

Addendum: if I delete documentation output and run `sage --docbuild reference html` twice, I don't see the warning message. So perhaps something can be tweaked to make it go away on the second pass when running `sage --docbuild all html`.


---

Comment by jhpalmieri created at 2013-01-24 22:16:13

Rebased to 5.7.beta0.


---

Comment by jhpalmieri created at 2013-01-25 06:22:59

[attachment:trac_6495-redirect_html.patch] doesn't quite work, because `os.path.split(path)` always returns a list of length 2. With this change, it works for me:

```diff
diff --git a/doc/common/builder.py b/doc/common/builder.py
--- a/doc/common/builder.py
+++ b/doc/common/builder.py
`@``@` -391,7 +391,7 `@``@` class WebsiteBuilder(DocBuilder):
                     redirect_filename = os.path.join(reference_dir, shorter_path, filename)
 
                     # the number of levels up we need to use in the relative url
-                    levels_up = len(os.path.split(shorter_path))
+                    levels_up = len(shorter_path.split(os.sep))
 
                     # the relative url that we will redirect to
                     redirect_url = "/".join(['..']*levels_up + [document_name, shorter_path, filename])
```

Fix that, and fix the docstring for the html method, and I think this part is good. 

The warning is still an issue, and I don't know why it still shows up during the second pass for the reference manual when doing `sage --docbuild all html` but not when running `sage --docbuild reference html` twice. Florent, any ideas? Does anyone else see this?

kcrisman, I don't know about doctests for all of these methods.


---

Comment by hivert created at 2013-01-25 09:43:11

Strange, It's working for me. Can you post the log of the docbuild which shows the warning, please

Florent


---

Attachment


---

Comment by hivert created at 2013-01-25 12:12:22

Sorry, I ended up uploading the wrong version of my patch. I uploaded a new version.

Florent


---

Comment by hivert created at 2013-01-25 12:42:43

Hi there

I'm at the point where everything seems to work for me. I'd like to test this
automatically it I can't see how. So provided someone testify that the new
version of [attachment:trac-6495_silence_warning-fh.patch] works for him, I'm
ready to put a positive review here.

Cheers,

Florent


---

Comment by jdemeyer created at 2013-01-25 12:48:16

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-01-25 13:27:49

This conflicts with #12719 and should be rebased.


---

Comment by leif created at 2013-01-25 15:04:33

Replying to [comment:169 jdemeyer]:

Positive review without the HTML redirection patch?  (Cf. John's comments above.)


---

Attachment


---

Comment by hivert created at 2013-01-25 16:24:36

When I Said "I'm ready to put a positive review" that was including John's
modification. I uploaded a new version of patch with it. Jeroen, do we need to
go in a re-review process (except of rebasing) ? Or should I leave a positive
review ?

Florent


---

Comment by jhpalmieri created at 2013-01-25 16:49:37

Well, the docstrings are still a bit of a mess. Here's a patch; maybe the last one?


---

Attachment


---

Comment by hivert created at 2013-01-25 17:09:46

Replying to [comment:175 jhpalmieri]:
> Well, the docstrings are still a bit of a mess. Here's a patch; maybe the last one? 

Thanks for this cleanup. I'm positive reviewing these new changes.

Florent


---

Comment by jhpalmieri created at 2013-01-25 19:40:39

Replying to [comment:170 jdemeyer]:
> This conflicts with #12719 and should be rebased.

I don't see any conflicts: starting with 5.7.beta0, I applied the patches from #12719 and then the patches here with no problem. Can you clarify?


---

Comment by jdemeyer created at 2013-01-26 22:33:17

This is totally a pain w.r.t. rebasing.  For example, there are again conflicts with #11641 and #13077.  If this is mostly the automatic scripted part which needs to be rebased, could you please split off the scripted part again such that I could simply run the script instead of applying the patch?


---

Comment by jdemeyer created at 2013-01-26 22:33:17

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2013-01-26 23:41:24

Changing status from needs_work to positive_review.


---

Comment by jhpalmieri created at 2013-01-26 23:41:51

everything except "part 1"


---

Attachment

This is definitely the most painful patch I've ever put into Sage. It would be a huge relief to have it integrated into sage. So I hope nothing more is blocking it. Is the rebase done with your script ?

Florent


---

Comment by jhpalmieri created at 2013-01-27 03:33:25

Yes, the script does the main work of moving all of the `MODULE.rst` files around. That is the part that change the most (as people add files to the reference manual), so that's where the rebasing happens.

Florent, thank you for all of your help with this; your contributions have made this much better. And much of the thanks goes to Mitesh Patel, wherever he is, who put in most of the original work on the patch.


---

Comment by hivert created at 2013-01-27 09:52:11

Replying to [comment:181 jhpalmieri]:
> Florent, thank you for all of your help with this; your contributions have
> made this much better. And much of the thanks goes to Mitesh Patel, wherever
> he is, who put in most of the original work on the patch.

And thanks a lot for your patience, awaiting for me, not giving up, keeping
trying to have this patch moving forward and constantly rebasing it.


---

Comment by jdemeyer created at 2013-01-27 11:46:21

Updated script.


---

Comment by jdemeyer created at 2013-01-27 13:34:00


```
WARNING: intersphinx inventory '/release/merger/sage-5.7.beta2/devel/sage/doc/output/html/en/reference/combinat/objects.inv' not readable due to AssertionError:
```

and

```
/release/merger/sage-5.7.beta2/devel/sage/doc/en/reference/sat/index.rst:77: WARNING: toctree contains reference to nonexisting document 'sat/sage/sat/solvers/dimacs'
/release/merger/sage-5.7.beta2/devel/sage/doc/en/reference/sat/index.rst:104: WARNING: toctree contains reference to nonexisting document 'sat/sage/sat/converters/polybori'
/release/merger/sage-5.7.beta2/devel/sage/doc/en/reference/sat/index.rst:124: WARNING: toctree contains reference to nonexisting document 'sat/sage/sat/boolean_polynomials'
```



---

Comment by jdemeyer created at 2013-01-27 13:34:00

Changing status from positive_review to needs_work.


---

Comment by hivert created at 2013-01-27 21:08:25

First of all, let me express my frustration: `#%)&<sup>`@`$(&%#</sup>#%`

> {{{
> /release/merger/sage-5.7.beta2/devel/sage/doc/en/reference/sat/index.rst:77: WARNING: toctree contains reference to nonexisting document 'sat/sage/sat/solvers/dimacs'
> /release/merger/sage-5.7.beta2/devel/sage/doc/en/reference/sat/index.rst:104: WARNING: toctree contains reference to nonexisting document 'sat/sage/sat/converters/polybori'
> /release/merger/sage-5.7.beta2/devel/sage/doc/en/reference/sat/index.rst:124: WARNING: toctree contains reference to nonexisting document 'sat/sage/sat/boolean_polynomials'
> }}}
Though I don't yet fully understand why, looking at the other doc suggest that
replacing the three `:maxdepth: 1` by `:maxdepth: 2` should solve this
particular problem. I don't have time to propose a patch now.

Replying to [comment:185 jdemeyer]:
> {{{
> WARNING: intersphinx inventory '/release/merger/sage-5.7.beta2/devel/sage/doc/output/html/en/reference/combinat/objects.inv' not readable due to AssertionError:
> }}}

To investigate this one I need to install `sage-5.7.beta2` which takes
time. Jeroen, could you give a some context for this second error. I've never
seen it but I only used `sage-5.6.rc1`.

Cheers,

Florent


---

Comment by jhpalmieri created at 2013-01-27 21:56:41

I don't understand these problems, either. I've never seen the one about the intersphinx inventory. For the other one, aside from `maxdepth: 1`, the other difference is that sage.sat is not imported anywhere:

```
sage: sage.sat
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/palmieri/Desktop/Sage_stuff/sage_builds/6495/sage-5.7.beta0/<ipython console> in <module>()

AttributeError: 'module' object has no attribute 'sat'
```

Could that be related? Should that be fixed in any case?


---

Comment by jdemeyer created at 2013-01-28 07:27:18

See the logfile [attachment:dochtml.log] (this is from a second build, note the error message is slightly different).


---

Comment by jdemeyer created at 2013-01-28 07:27:18

Changing assignee from tba to jdemeyer.


---

Comment by hivert created at 2013-01-28 08:11:59

Replying to [comment:188 jdemeyer]:
> See the logfile [attachment:dochtml.log] (this is from a second build, note the error message is slightly different).

I'm seriously scared that it could come from a race condition, an nightmare to debug. Is it deterministic ?


---

Comment by jhpalmieri created at 2013-01-28 19:44:34

On what platforms, and how reliably, do you see the `WARNING: intersphinx inventory ...`?

For the other problem, this patch fixes it for me:

```diff
diff --git a/doc/common/builder.py b/doc/common/builder.py
--- a/doc/common/builder.py
+++ b/doc/common/builder.py
`@``@` -274,7 +274,7 `@``@` class AllBuilder(object):
         global ALLSPHINXOPTS
         ALLSPHINXOPTS += ' -Q -D multidoc_first_pass=1'
         for document in refs:
-            getattr(get_builder(document), 'inventory')(*args, **kwds)
+            getattr(get_builder(document), name)(*args, **kwds)
         logger.warning("Building reference manual, second pass.\n")
         ALLSPHINXOPTS = ALLSPHINXOPTS.replace(
             'multidoc_first_pass=1', 'multidoc_first_pass=0')
```

Or perhaps we should use this one:

```diff
diff --git a/doc/common/builder.py b/doc/common/builder.py
--- a/doc/common/builder.py
+++ b/doc/common/builder.py
`@``@` -274,7 +274,10 `@``@` class AllBuilder(object):
         global ALLSPHINXOPTS
         ALLSPHINXOPTS += ' -Q -D multidoc_first_pass=1'
         for document in refs:
-            getattr(get_builder(document), 'inventory')(*args, **kwds)
+            if name == 'pdf':
+                getattr(get_builder(document), 'inventory')(*args, **kwds)
+            else:
+                getattr(get_builder(document), name)(*args, **kwds)
         logger.warning("Building reference manual, second pass.\n")
         ALLSPHINXOPTS = ALLSPHINXOPTS.replace(
             'multidoc_first_pass=1', 'multidoc_first_pass=0')
```

With an html build, building with this patch does not take any more time. Opinions?


---

Comment by jhpalmieri created at 2013-01-28 19:52:06

By the way, the new version of the script doesn't work on OS X, because OS X uses a BSD version of `sed` which is not completely compatible with the linux version. To get it to work, you have to make these changes:

```diff
--- a/trac_6495-script.sh	2013-01-27 03:44:32.000000000 -0800
+++ b/trac_6495-script.sh	2013-01-28 10:53:39.000000000 -0800
`@``@` -16,9 +16,9 `@``@`
 do
     hg rename $f.rst $f/index.rst
     # delete lines of the form ".. _ch:blah"
-    sed -e 's|^\.\. _ch:.*$||' -i $f/index.rst
+    sed -e 's|^\.\. _ch:.*$||' -i '' $f/index.rst
     # remove resulting blank lines from top of file
-    sed -e '/./,$!d' -i $f/index.rst
+    sed -e '/./,$!d' -i '' $f/index.rst
     cat >$f/conf.py <<EOF
 # -*- coding: utf-8 -*-
 # This file is execfile()d with the current directory set to its
`@``@` -47,7 +47,7 `@``@`
 cp cmd/conf.py combinat/conf.py
 hg add combinat/conf.py
 # in combinat/index.rst: change "../sage/combinat/blah" to "sage/combinat/blah"
-sed -e "s|\.\./||" -i combinat/index.rst
+sed -e "s|\.\./||" -i '' combinat/index.rst
 
 cat >> combinat/index.rst <<EOF
 
```



---

Comment by jdemeyer created at 2013-01-29 07:30:35

Replying to [comment:190 jhpalmieri]:
> On what platforms
Only tried `sage.math` so far.

> and how reliably, do you see the `WARNING: intersphinx inventory ...`?
Two out of two builds so far.


---

Comment by jdemeyer created at 2013-01-29 12:51:57

script used to generate "part 1" patch


---

Attachment

Third attempt, now it's the notebook which gives problems:

```
WARNING: intersphinx inventory '/release/merger/sage-5.7.beta3/devel/sage/doc/output/html/en/reference/notebook/objects.inv' not readable due to ValueError: unknown or unsupported inventory version
```


So it's certainly not deterministic, but quite likely that *something* goes wrong.


---

Comment by hivert created at 2013-01-29 18:02:22

Hi there,

Replying to [comment:193 jdemeyer]:
> Third attempt, now it's the notebook which gives problems:
> {{{
> WARNING: intersphinx inventory '/release/merger/sage-5.7.beta3/devel/sage/doc/output/html/en/reference/notebook/objects.inv' not readable due to ValueError: unknown or unsupported inventory version
> }}}
>
> So it's certainly not deterministic, but quite likely that *something* goes wrong.

Unfortunately the one week window for sage days I had is over. I didn't had
time to make any experiment, and I don't expect to find much time to work on
this in the forthcoming days (the new semester is starting and I'm moving from
one house to another in two weeks).

Anyway, I have a guess one what could be happening. The first pass of
compilation is designed to build the intersphinx inventory. However, they are
rewritten during the second phase. Due to parallelism, it is fairly possible
that one process is trying to read the inventory just at the time another one
is writing it. The more process you have, the larger the probability of this
happening. This explain why we don't see this on small laptop. I'm not sure
how to test that this is precisely what's happening. But if it's the case, the
solution should be easy: similarly to what I did recently for indexes, we
should deactivate the output of the inventory for a second pass compilation of
a sub-document.

Does anyone have time to experiment more ?


---

Comment by jhpalmieri created at 2013-01-29 18:29:40

I have not been able to reproduce this on sage.math. I've tried building in /scratch and in /home. Could there be something about /release that's contributing to this? Jeroen, what do you have `MAKE` set to?


---

Comment by jdemeyer created at 2013-01-29 18:36:54

Replying to [comment:195 jhpalmieri]:
> Could there be something about /release that's contributing to this?
It's quite a fast disk, could that play a role?

> Jeroen, what do you have `MAKE` set to?

```
MAKE=make -j6
```



---

Comment by vbraun created at 2013-01-29 18:38:59

You just have to `strace -o logfile -ff` the build process, then you'll see who is writing to the offending file. Also, can we have a beta with this ticket? Too many patches ;-)


---

Comment by kcrisman created at 2013-01-29 19:28:37

> You just have to `strace -o logfile -ff` the build process, then you'll see who is writing to the offending file. Also, can we have a beta with this ticket? Too many patches ;-)
+1


---

Comment by jhpalmieri created at 2013-01-29 22:15:04

[Here's a tar file](http://sage.math.washington.edu/home/palmieri/misc/6495/sage-5.7.beta1_6495.tar), based on 5.7.beta1.


---

Comment by kcrisman created at 2013-01-30 03:03:28

Wow, going fast already.

```
Elapsed time: 284.1 seconds.
```

Just a _slight_ improvement.

I couldn't find (i.e., browser says it's not there)

file:///Users/.../sage-5.7.beta1_6495/devel/sage-main/doc/output/html/en/reference/functions.html

and the like, but most redirection of actual pages of content seem to be working fine - it's the old ones corresponding to 

file:///Users/.../sage-5.7.beta1_6495/devel/sage-main/doc/output/html/en/reference/functions/index.html

that seem to have not been "translated" properly.


---

Attachment

Initial patch


---

Comment by vbraun created at 2013-01-31 12:50:48

I can totally reproduce the issue, works every time.

I've started by adding a framework to suppress unwanted messages and print the ones that we do intact (that is, line buffered). Now I can at least start to see what is going on...


---

Comment by vbraun created at 2013-02-01 11:04:19

The issue was indeed that the object inventory was written to and read from parallel processes. Sphinx makes no attempt to update the `object.inv` atomically.

I've changed things such that
* the inventory build process outputs to `output/inventory` and does not read inventory
* the second pass then reads the object inventory from `output/inventory` and writes to `output/html`

Now I don't see any races any more. The first stage still warns erroneously about a few missing citations, but thats not a big deal. 

Also, the whole thing runs just shy of 200 seconds on my desktop (i7-3770K)

```
sage -docbuild all html
...
Elapsed time: 196.5 seconds.
Done building the documentation!
```



---

Attachment

Initial patch


---

Comment by vbraun created at 2013-02-01 11:09:16

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2013-02-01 16:41:30

Not sure why you removed the script, because the patches still fail to apply:

```
patching file doc/en/reference/combinat/index.rst
Hunk #1 FAILED at 3
Hunk #3 FAILED at 66
2 out of 3 hunks FAILED -- saving rejects to file doc/en/reference/combinat/index.rst.rej
patching file doc/en/reference/groups/index.rst
Hunk #2 succeeded at 39 with fuzz 1 (offset 9 lines).
abort: patch failed to apply
```



---

Comment by vbraun created at 2013-02-01 16:53:50

I removed the "apply" script since I based my patch on top of John's source dist tar file at comment:199.


---

Comment by jdemeyer created at 2013-02-01 16:59:02

But in the end the patch will need to be rebased to the latest development version.  Do you want to wait with that until after positive_review?


---

Comment by vbraun created at 2013-02-01 17:00:22

Ok I've rebased the first patch on top of sage-5.7.beta2. All apply cleanly now.


---

Comment by vbraun created at 2013-02-01 17:07:43

Ok some more fixes needed as more documentation was changed


---

Comment by vbraun created at 2013-02-01 17:15:36

Updated patch


---

Attachment

Ok I've now correctly resolved the merge conflict ;-) Just a minor change in the combinat docs, its all fine now.

The only thing left to review would be my final patch. I made all changes that I wanted, so I'm fine with anything else thats in this ticket.


---

Comment by jhpalmieri created at 2013-02-01 23:55:09

I haven't verified that the intersphinx warning is gone, but I see two other possible problems: I get a warning 

```
[reference] .../sage-5.7.beta2/devel/sage/doc/en/reference/sat/index.rst:: WARNING: document isn't included in any toctree
```

along with some citations not being found. Also with [attachment:trac_6495_separate_inventory.patch], the build is a bit slower than without: on my OS X box (with only two threads), the fastest time with the patch was 858 seconds, and more typical (5 out of 6 runs) was 885 seconds or more. Without the patch, the slowest time was 813 seconds.  On sage.math, with `MAKE="make -j12"`: with the patch, 450 seconds, without the patch, 390 seconds.


---

Comment by vbraun created at 2013-02-02 11:10:34

Are you always nuking the output directory for timings? Also, I'm always adding all inventory files to the intersphinx-mapping whereas before Sphinx would only add them as needed. But there Sphinx assumes that the inventory is in the html directory, so its not good if you want to avoid races.

As I said already, the first stage still warns erroneously about a few missing cross-document citations. We could hide them, but I don't think its a big deal.

The `sat/index.rst` isn't included warning is correct. The sat subdoc was not listed in `multidocs_subdoc_list` (`en/reference/conf.py`).


---

Comment by vbraun created at 2013-02-02 12:40:22

The last patch fixes the unlisted sat subdoc and moves the citations pickle to the inventory dir. Also, write the citation pickle atomically to avoid another potential race. Now everything builds without any warnings.


---

Comment by jhpalmieri created at 2013-02-02 16:56:33

> Are you always nuking the output directory for timings?

Yes. Good catch on finding sat not being listed in `multidocs_subdoc_list`, by the way.


---

Comment by jhpalmieri created at 2013-02-04 04:51:38

I'm pretty happy with the latest patches, but I'm not quite ready to give a positive review. In my testing, I'm not seeing the intersphinx warning any more, but I was only sporadically able to reproduce it in the first place.

With the current `useless_chatter` settings, on the first pass through the reference manual, I see two summaries

```
[polynomia] build succeeded, 1 warning.
[geometry ] build succeeded, 3 warnings.
```

The actual warnings are suppressed, though. Should these message be suppressed (or modified), also? Otherwise, someone might wonder what the warnings actually were.


---

Comment by jhpalmieri created at 2013-02-04 06:57:26

Another thing: if I have built the documentation already and then run `./sage --docbuild reference html`, then all of the output from building the individual parts of the reference manual is suppressed, so there is a long pause (several minutes, enough to wonder whether it's hung), and then finally 

```
[reference] Compiling the master document
[reference] updating environment: 0 added, 0 changed, 1098 removed
[reference] Merging environment/index files...
```



---

Comment by jhpalmieri created at 2013-02-04 17:00:31

Maybe just removing one line from `useless_chatter` would address my last point:

```diff
diff --git a/doc/common/custom-sphinx-build.py b/doc/common/custom-sphinx-build.py
--- a/doc/common/custom-sphinx-build.py
+++ b/doc/common/custom-sphinx-build.py
`@``@` -31,7 +31,6 `@``@`
     re.compile('^Compiling a sub-document'),
     re.compile('^updating environment: 0 added, 0 changed, 0 removed'),
     re.compile('^looking for now-outdated files... none found'),
-    re.compile('^no targets are out of date.'),
     re.compile('^building \[.*\]: targets for 0 source files that are out of date'),
     re.compile('^loading pickled environment... done'),
     re.compile('^loading cross citations... done \([0-9]* citations\).')
```

doesn't look too bad: if you change one file in `homology` then rebuild the docs, then you get

```
[polynomia] no targets are out of date.
[combinat ] no targets are out of date.
[cmd      ] no targets are out of date.
[arithgrou] no targets are out of date.
[graphs   ] no targets are out of date.
[misc     ] no targets are out of date.
...
```

until it finally gets to something which has changed.


---

Attachment

combined patch


---

Attachment


---

Attachment

I rebased the patches to 5.7.beta3. The only change of substance: in the "part2" patch:

```diff
diff --git a/sage/graphs/graph_plot.py b/sage/graphs/graph_plot.py
--- a/sage/graphs/graph_plot.py
+++ b/sage/graphs/graph_plot.py
`@``@` -106,7 +106,7 `@``@`
       settings from ``DEFAULT_SHOW_OPTIONS`` only affects ``G.show()``.
 
     * In order to define a default value permanently, you can add a couple of
-      lines to :doc:`Sage's startup scripts <../../startup>`. Example ::
+      lines to `Sage's startup scripts <../../../cmd/startup.html>`_. Example ::
 
        sage: import sage.graphs.graph_plot
        sage: sage.graphs.graph_plot.DEFAULT_SHOW_OPTIONS['figsize'] = [4,4]
```

(The only change to the "part3" patch was to change the commit message.) With the newest patch ([attachment:trac_6495-filtering.patch]), all superfluous warnings are suppressed. I'm happy with this now.

I think it might be best to include every single patch, or else credit will not get assigned appropriately; for example, the old "all in one" patch combined my work (which is really based on mpatel's, but I don't know how to get his name back in here...) with Florent's.


---

Attachment

apply first


---

Attachment


---

Comment by SimonKing created at 2013-02-09 21:58:34

Are you sure that the first patch applies? At least with sage-5.7.beta2, I get a mismatch in doc/en
/reference/rings_standard/index.rst, which is not surprising as this file does not seem to exist.

But I suppose it is better anyway to run the sript?


---

Comment by jhpalmieri created at 2013-02-09 22:01:43

Rebased to Sage 5.7.beta4 (because of the recently added file `doc/en/reference/finite_rings.rst`).


---

Attachment


---

Comment by SimonKing created at 2013-02-09 22:05:26

Aha, now I understand! It starts with doc/en/reference/rings_standard.rst, adds one line and moves the result to doc/en/reference/rings_standard/index.rst.

Problem: The line

```
sage/rings/universal_cyclotomic_field/universal_cyclotomic_field
```

does not exist in sage-5.7.beta2.

In what ticket has this line been introduced? That would be a new dependency.


---

Comment by jhpalmieri created at 2013-02-09 22:12:12

Simon: the patches should apply to 5.7.beta4, and probably only to this version. The script also may only work on this version (or any later version, I hope). This patch is very sensitive to changes, so it needs to be rebased frequently. I'm sorry I haven't kept track of the dependencies -- I just keep rebasing to the latest beta.

[Here's a tar file](http://sage.math.washington.edu/home/palmieri/misc/6495/sage-5.7.beta4-6495.tar) for 5.7.beta4 source with these patches applied.


---

Comment by SimonKing created at 2013-02-09 22:28:30

Bad. It seems that I managed to destroy my sage-5.7.beta2 by this patch. No idea how that happened. Could it be that popping the patch does not revert all changes?

Replying to [comment:221 jhpalmieri]:
> [Here's a tar file](http://sage.math.washington.edu/home/palmieri/misc/6495/sage-5.7.beta4-6495.tar) for 5.7.beta4 source with these patches applied.

I currently don't have the bandwith to download a Sage tarball.


---

Comment by jhpalmieri created at 2013-02-09 22:38:18

How about downloading [just the sage library spkg](http://sage.math.washington.edu/home/palmieri/misc/6495/sage-5.7.beta4-6495/spkg/standard/sage-5.7.beta4-6495.spkg) (which is 57M)?

Again, I apologize for not keeping track of the dependencies. My general reaction when a new beta comes out is to try to apply the patches, find that they don't apply, swear a bit, and then rebase them. If someone does something minor (say, modify `doc/en/reference/algebras.rst`), then running the script instead of applying the "part1" patch should take care of things. But if someone adds a new file to `doc/en/reference/`, then several of the patch files will need to be rebased. This happened between 5.7.beta3 and 5.7.beta4.

Is there a good way with mercurial to find out all of the recent changes to files in a certain directory? Then I could identify the dependencies easily.


---

Comment by SimonKing created at 2013-02-09 22:47:37

Replying to [comment:223 jhpalmieri]:
> How about downloading [just the sage library spkg](http://sage.math.washington.edu/home/palmieri/misc/6495/sage-5.7.beta4-6495/spkg/standard/sage-5.7.beta4-6495.spkg) (which is 57M)?

That could be a good idea.


---

Comment by SimonKing created at 2013-02-09 23:27:58

Hooray, the patches apply cleanly! Thank you for naming the additional dependencies!

By the way, I still don't understand why seemingly my hg repository became dysfunctional, but now it seems to be fine again (which I don't understand either...).


---

Comment by jhpalmieri created at 2013-02-09 23:46:03

I don't understand it either. I occasionally have seen this, too, but not at all reproducibly, and not recently. Maybe mercurial is just more likely get confused if it moves lot of files around and creates a lot of directories, and then the patch is popped? Or maybe it also requires the patch not to apply cleanly first?


---

Comment by SimonKing created at 2013-02-09 23:56:31

In the ticket description, it is said: "Also create a file algebras/conf.py for the build configuration. All of these new conf.py files are identical."

If they are all identical, why is there not just a single conf.py, to which all other locations refer by a soft link? In that way, it would be easier to maintain changes.


---

Comment by jhpalmieri created at 2013-02-10 03:26:47

Good question. The files `conf.py` are pretty minimal, and most of the content is in `en/reference/conf_sub.py`, which is imported by each `conf.py` file. So the idea is that to maintain it, you would just need to modify `conf_sub.py`. But here's a new version of the part 1 patch and the script which creates links directly from `en/reference/MODULE/conf.py` pointing to `en/reference/conf_sub.py`. This seems to work. I'll check on OpenSolaris to make sure there's nothing strange going on there.


---

Comment by jhpalmieri created at 2013-02-10 03:27:09

apply first


---

Attachment

[attachment:trac_6495-script-jhp.2.sh] is identical to the old script; it can be deleted. (Why can't I delete my own attachments?)


---

Attachment

script used to generate "part 1" patch


---

Comment by kcrisman created at 2013-02-10 04:11:47

> [attachment:trac_6495-script-jhp.2.sh] is identical to the old script; it can be deleted. (Why can't I delete my own attachments?)
I suppose so that the history is preserved.  That said, it would be helpful to have that ability for at least some users.

Given your post at [this sage-support thread](https://groups.google.com/forum/?fromgroups=#!topic/sage-support/vj_W8wc9Mic), now it's really exciting to think about this getting in.


---

Comment by SimonKing created at 2013-02-10 07:39:20

For the record: Documentation builds for me, at least with the old patches. And now I am really curious what will happen if I add a thematic tutorial and try to link to the reference manual, via `:class:`sage.structure.parent.Parent``


---

Comment by SimonKing created at 2013-02-10 07:52:30

That said: I am not totally sure, but my impression is that building the documentation took longer than in the old way. Also, it surprises me that `sage --docbuild all pdf` takes more than three minutes after previously doing `sage --docbuild all html`.


---

Comment by SimonKing created at 2013-02-10 08:23:04

OK, processing the `LaTeX` files seems less trivial than I thought, and does take time.

Currently, I am seeing a lot of unresolved references, and one fatal error:

```
...

! LaTeX Error: Too deeply nested.

See the LaTeX manual or LaTeX Companion for explanation.
Type  H <return>  for immediate help.
 ...                                              
                                                  
l.26942 \begin{Verbatim}[commandchars=\\\{\}]
                                             
? 
! Emergency stop.
 ...                                              
                                                  
l.26942 \begin{Verbatim}[commandchars=\\\{\}]
                                             
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on categories.log.
make: *** [categories.pdf] Fehler 1
Build finished.  The built documents can be found in /home/simon/SAGE/debug/sage-5.7.beta2/devel/sage/doc/output/pdf/en/reference/categories
[coding   ] building [latex]: all documents
[coding   ] updating environment: [config changed] 6 added, 0 changed, 0 removed
[coding   ] reading sources... [ 16%] index
...
```


I suppose there will automatically be a second run, which resolves the cross-references. And we will see about the fatal error.


---

Comment by SimonKing created at 2013-02-10 09:03:02

OK, the links in the pdf and the mathematics in the html do not seem to work.

For example, I am looking at the documentation of sage.structure.coerce, The Coercion Model.

I see

```
Coercions are canonical (possibly modulo a finite number of deterministic choices) morphisms, and the set of all coercions between all parents forms a commuting diagram (modulo possibly rounding issues). [Math Processing Error] is an example of a coercion. These are invoked implicitly by the coercion model.
```

in the html. It is fine in the pdf.

Both in pdf and html, I read

```
For more information on how to specify coercions, conversions, and actions, see the documentation for Parent.

class sage.structure.coerce.CoercionModel_cache_maps

    Bases: sage.structure.element.CoercionModel

    See also sage.categories.pushout
```


I would expect the "see the documentation for Parent" and "See also sage.categories.pushout" come with a link, but apparently that has been forgotten (bug in the documentation).

In the html, `Bases: sage.structure.element.CoercionModel` is a link. In the pdf, it is _not_ a link. I guess it should be a link in pdf, too, isn't it?


---

Comment by SimonKing created at 2013-02-10 09:07:35

And now the good news: When I added my (not yet completed) thematic tutorial on categories and coercion, both the mathematical type-setting _and_ the links to the reference manual (!) work fine.


---

Comment by jhpalmieri created at 2013-02-10 21:22:58

Replying to [comment:235 SimonKing]:
> OK, the links in the pdf and the mathematics in the html do not seem to work.

For the links in the pdf, I don't know what to do about that. Intersphinx seems to work only in html, not pdf, or at least that's what I gather from [its documentation](http://sphinx-doc.org/ext/intersphinx.html). I don't even know if it's possible to put relative links into a PDF file. 

For mathematics in the html, I don't see this at all, either on OS X (with any of the browsers I've tried) or on sage.math. See [the coercion model page](http://sage.math.washington.edu/home/palmieri/misc/6495-jsmath/html/en/reference/coercion/sage/structure/coerce.html) on sage.math, for instance -- this renders fine for me with my browser.

Did you delete the directory `devel/sage/doc/output` before the first attempt at a parallel build? If not, maybe there were artifacts there which caused problems. Otherwise, I don't know what's causing it. What is your OS and what is your browser?

Replying to [comment:236 SimonKing]:
> And now the good news: When I added my (not yet completed) thematic tutorial on categories and coercion, both the mathematical type-setting _and_ the links to the reference manual (!) work fine.

Great.


---

Comment by SimonKing created at 2013-02-10 22:32:56

Replying to [comment:237 jhpalmieri]:
> Did you delete the directory `devel/sage/doc/output` before the first attempt at a parallel build?

I deleted it, and I think I did not do a parallel build (or at least, I did not define MAKE to be `make -j2`).

> If not, maybe there were artifacts there which caused problems. Otherwise, I don't know what's causing it. What is your OS and what is your browser?

`openSuse` 12.1 Asparagus, and Firefox 18.0

> Replying to [comment:236 SimonKing]:
> > And now the good news: When I added my (not yet completed) thematic tutorial on categories and coercion, both the mathematical type-setting _and_ the links to the reference manual (!) work fine.

And that's why I wonder: The maths is fine in the tutorial, but not in the reference manual.

I just observed: When I load a page from the reference manual, there is a message on the lower left corner of my browser, `Loading [MathJax]/jax/output/HTML-CSS/imageFonts.js`, and a bit later there is a message "File failed to load" (but too quickly disappearing, I didn't manage to copy the message).


---

Comment by vbraun created at 2013-02-11 13:46:52

To debug Firefox issues: Tools->Web Developer->Web Console. 

Simon's issue sounds a lot like http://docs.mathjax.org/en/v1.1-latest/installation.html#firefox-and-local-fonts. Either use a different browser or install the stix fonts. Should be fine if served over http instead of a local dir.


---

Comment by SimonKing created at 2013-02-11 14:07:34

Replying to [comment:239 vbraun]:
> To debug Firefox issues: Tools->Web Developer->Web Console. 
> 
> Simon's issue sounds a lot like http://docs.mathjax.org/en/v1.1-latest/installation.html#firefox-and-local-fonts. Either use a different browser or install the stix fonts.

Would this explain why the maths typesetting is fine in one document and broken in another document?


---

Comment by vbraun created at 2013-02-11 14:19:44

Replying to [comment:240 SimonKing]:
> Would this explain why the maths typesetting is fine in one document and broken in another document?

Yes. It depends on whether or not mathjax is loaded from the same directory as the document. And we don't plaster a copy of mathjax into every subdirectory.


---

Comment by SimonKing created at 2013-02-11 15:42:53

Replying to [comment:241 vbraun]:
> Replying to [comment:240 SimonKing]:
> > Would this explain why the maths typesetting is fine in one document and broken in another document?
> 
> Yes. It depends on whether or not mathjax is loaded from the same directory as the document. And we don't plaster a copy of mathjax into every subdirectory.

OK, by installing the fonts as suggested on the link you provided, I can now see the reference manual in all its beauty.


---

Comment by vbraun created at 2013-02-12 11:46:50

Is there anything left to review? 

There are no inter-document links to specific anchors in the PDF reference manual. Its not a big loss since it your pdf viewer probably doesn't support them anyways (e.g. the PDF viewer in Chrome does not). If you want hyperlinks just use the html version.


---

Comment by jhpalmieri created at 2013-02-12 15:36:06

Replying to [comment:243 vbraun]:
> Is there anything left to review? 

The only unreviewed parts are [attachment:trac_6495-filtering.patch] and the change to [attachment:trac_6495-part1-moving-files-link.patch] to use symbolic links for `reference/MODULE/conf.py` (see [comment:229]).


---

Comment by vbraun created at 2013-02-12 15:55:07

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2013-02-12 15:55:07

Looks reasonable to me.


---

Attachment

Log file of troublesome build


---

Comment by jdemeyer created at 2013-02-13 11:12:35

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-02-13 11:12:35

It still doesn't quite work completely. During one build, I got

```
Building reference manual, first pass.

[polynomia] Exception occurred:
[polynomia] File "/release/merger/sage-5.8.beta0/local/lib/python/pickle.py", line 880, in load_eof
[polynomia] raise EOFError
[polynomia] EOFError
[polynomia] The full traceback has been saved in /tmp/release/sphinx-err-2hqEZ_.log, if you want to report the issue to the developers.
[polynomia] Please also report this if it was a user error, so that a better error message can be provided next time.
[polynomia] Either send bugs to the mailing list at <http://groups.google.com/group/sphinx-dev/>,
[polynomia] or report them in the tracker at <http://bitbucket.org/birkenfeld/sphinx/issues/>. Thanks!
```

where the "full traceback" reads

```
# Sphinx version: 1.1.2
# Python version: 2.7.3
# Docutils version: 0.7 release
# Jinja2 version: 2.5.5
Traceback (most recent call last):
  File "/release/merger/sage-5.8.beta0/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/cmdline.py", line 188, in main
    warningiserror, tags)
  File "/release/merger/sage-5.8.beta0/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/application.py", line 114, in __init__
    self.setup_extension(extension)
  File "/release/merger/sage-5.8.beta0/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/application.py", line 247, in setup_extension
    mod = __import__(extension, None, None, ['setup'])
  File "/release/merger/sage-5.8.beta0/devel/sage-main/doc/common/sage_autodoc.py", line 35, in <module>
    from sphinx.pycode import ModuleAnalyzer, PycodeError
  File "/release/merger/sage-5.8.beta0/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/pycode/__init__.py", line 25, in <module>
    pygrammar = driver.load_grammar(_grammarfile)
  File "/release/merger/sage-5.8.beta0/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/pycode/pgen2/driver.py", line 135, in load_grammar
    g.load(gp)
  File "/release/merger/sage-5.8.beta0/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/pycode/pgen2/grammar.py", line 96, in load
    d = pickle.load(f)
  File "/release/merger/sage-5.8.beta0/local/lib/python/pickle.py", line 1378, in load
    return Unpickler(file).load()
  File "/release/merger/sage-5.8.beta0/local/lib/python/pickle.py", line 858, in load
    dispatch[key](self)
  File "/release/merger/sage-5.8.beta0/local/lib/python/pickle.py", line 880, in load_eof
    raise EOFError
EOFError
```

The second pass of this build starts with:

```
Building reference manual, second pass.

[polynomia] loading pickled environment... not yet created
[homology ] loading pickled environment... not yet created
[polynomia] WARNING: intersphinx inventory '/release/merger/sage-5.8.beta0/devel/sage/doc/output/inventory/en/reference/polynomial_rings/objects.inv' not fetchable due to <type 'exceptions.IOError'>: [Errno 2] No such file or directory: '/release/merger/sage-5.8.beta0/devel/sage/doc/output/inventory/en/reference/polynomial_rings/objects.inv'
```


See [attachment:dochtml.log]


---

Comment by vbraun created at 2013-02-13 12:29:25

Upon first use, Sphinx apparenty saves a cached pickle of its grammar under `site-packages/` (!) non-atomically (!). Thats just peachy...


---

Comment by jdemeyer created at 2013-02-13 12:55:07

I think the best place to solve this would be in the Sphinx installer: generate the grammar pickle at install time. It's completely normal to put files in `site-packages/` during install and you won't need to worry about non-atomic accesses.


---

Comment by jhpalmieri created at 2013-02-13 19:35:58

So I don't know exactly what to do. We could create a script like this in the Sphinx spkg, and then run it as part of the installation. How does that sound?

```python

# Code taken from sphinx/pycode/__init__.py to generate the grammar pickle.

from os import path
from sphinx import package_dir
from sphinx.pycode.pgen2 import driver

# load the Python grammar
_grammarfile = path.join(package_dir, 'pycode', 'Grammar.txt')
pygrammar = driver.load_grammar(_grammarfile)
```



---

Comment by jhpalmieri created at 2013-02-13 20:11:49

New spkg: http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-1.1.2.p2.spkg.
See [attachment:trac_6495-sphinx-grammar.patch] for the changes.


---

Comment by jhpalmieri created at 2013-02-13 20:12:14

patch for Sphinx spkg; for review only


---

Attachment

Thanks, looks good and works for me. Hopefully that was the last race in Sphinx, fingers crossed ;-)


---

Comment by vbraun created at 2013-02-13 20:26:00

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2013-02-14 07:45:32

The spkg is not clean:

```
$ hg status
? create_grammar_pickle.py~
```



---

Comment by jdemeyer created at 2013-02-14 07:45:32

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2013-02-14 15:36:32

Fixed. Sorry about that.


---

Comment by jhpalmieri created at 2013-02-14 15:36:32

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2013-02-15 08:19:51

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-02-15 08:19:51

In `devel/sage/doc/common/custom-sphinx-build.py`, you write

```
    def write(self, str):
        try:
            self._write(str)
        except:
            import traceback
            traceback.print_exc(file=self._stream)
```

One should never use bare `except:` statements, because these usually catch too much, for example `KeyboardInterrupt`s. Use `except StandardError` if you want to catch all errors, or catch a specific exception instead.

And in `devel/sage/doc/common/themes/sageref/layout.html`, indentation is done mostly with spaces but there are a few TABs. You should use spaces consistently.

But most importantly: the code actually seems to work now! It still needs buildbot testing though.


---

Comment by jhpalmieri created at 2013-02-15 17:53:25

I got rid of the tabs in `layout.html`.


---

Comment by jhpalmieri created at 2013-02-15 17:54:26

apply second


---

Attachment

Updated patch


---

Comment by vbraun created at 2013-02-15 20:43:07

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2013-02-15 20:43:07

I've replaced the bare `except:`.


---

Comment by jdemeyer created at 2013-02-17 22:41:24

Resolution: fixed


---

Comment by hivert created at 2013-02-17 23:36:23

Hurrah !!!


---

Comment by aschilling created at 2013-02-19 20:46:56

Could I make one suggestion (perhaps for a later ticket)? Compiling the docs does not say any longer where to look on one's machine for the compiled docs. This was a very useful feature beforehand!

Thanks for your work on this!

Anne


---

Comment by jhpalmieri created at 2013-02-19 23:08:10

Replying to [comment:261 aschilling]:
> Could I make one suggestion (perhaps for a later ticket)? Compiling the docs does not say any longer where to look on one's machine for the compiled docs. This was a very useful feature beforehand!

See #14148.


---

Comment by jdemeyer created at 2013-02-21 13:02:03

See #14156 for a blocker follow-up.


---

Comment by jdemeyer created at 2013-02-27 20:23:59

See #14199 for another follow-up.


---

Comment by jdemeyer created at 2013-03-06 20:33:29

Can somebody here please review *blocker* ticket #14199?


---

Comment by hivert created at 2013-03-08 12:24:51

Another followup #14245: cloning is broken.


---

Comment by jdemeyer created at 2013-05-22 15:11:29

Followup #14626: docbuilder hangs if latex fails.
