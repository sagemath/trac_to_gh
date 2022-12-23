# Issue 6495: Break up the PDF reference manual into smaller pieces

archive/issues_006495.json:
```json
{
    "body": "Assignee: tba\n\nCC:  jhpalmieri leif niles hivert mguaypaq mhansen\n\nIs the logical division at the module level, with the non-auto-generated `.rst` files as guides?\n\nRelated: Should the indices be single-column?\n\nIssue created by migration from https://trac.sagemath.org/ticket/6495\n\n",
    "created_at": "2009-07-09T08:29:32Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "Break up the PDF reference manual into smaller pieces",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6495",
    "user": "mpatel"
}
```
Assignee: tba

CC:  jhpalmieri leif niles hivert mguaypaq mhansen

Is the logical division at the module level, with the non-auto-generated `.rst` files as guides?

Related: Should the indices be single-column?

Issue created by migration from https://trac.sagemath.org/ticket/6495





---

archive/issue_comments_052558.json:
```json
{
    "body": "Experimental.",
    "created_at": "2009-07-09T08:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52558",
    "user": "mpatel"
}
```

Experimental.



---

archive/issue_comments_052559.json:
```json
{
    "body": "Attachment\n\nThe attached patch is experimental.  Notes:\n\n* `sage -docbuild reference pdf` fails to build `arithgroup.pdf`, apparently because of the math macro `\\ZZ` in the title.  Unfortunately, I don't know how to fix this.  \n* Since it *replaces* the top level PDF file with several smaller files, it breaks the patch at #4460.\n* It's not clear what happens to cross-ReST document links.  I'll try to investigate.",
    "created_at": "2009-07-09T09:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52559",
    "user": "mpatel"
}
```

Attachment

The attached patch is experimental.  Notes:

* `sage -docbuild reference pdf` fails to build `arithgroup.pdf`, apparently because of the math macro `\ZZ` in the title.  Unfortunately, I don't know how to fix this.  
* Since it *replaces* the top level PDF file with several smaller files, it breaks the patch at #4460.
* It's not clear what happens to cross-ReST document links.  I'll try to investigate.



---

archive/issue_comments_052560.json:
```json
{
    "body": "On cross-PDF document links:  It seems that Sphinx does not produce these.  This may OK, since `file://` URLs can break easily.",
    "created_at": "2009-09-11T03:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52560",
    "user": "mpatel"
}
```

On cross-PDF document links:  It seems that Sphinx does not produce these.  This may OK, since `file://` URLs can break easily.



---

archive/issue_comments_052561.json:
```json
{
    "body": "On the `\\ZZ` in `arithgroup.tex`:  It seems the problem stems from `\\`@`title` in\n\n```\n    \\ifsphinxpdfoutput\n      \\begingroup\n      % This \\def is required to deal with multi-line authors; it               \n      % changes \\\\ to ', ' (comma-space), making it pass muster for             \n      % generating document info in the PDF file.                               \n      \\def\\\\{, }\n      \\pdfinfo{\n        /Author (\\@author)\n        /Title (\\@title)\n      }\n      \\endgroup\n    \\fi\n```\n\nin Sphinx's `manual.cls`.  For some reason, the `\\math*` font commands do not work in this context.  I gather that `\\mathbf` is preferred, but one workaround is to use\n\n```\nArithmetic Subgroups of `{\\rm SL}_2({\\bf Z})`\n```\n\nin place of \n\n```\nArithmetic Subgroups of `{\\rm SL}_2(\\ZZ)`\n```\n\nin `arithgroup.rst`.",
    "created_at": "2009-09-11T08:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52561",
    "user": "mpatel"
}
```

On the `\ZZ` in `arithgroup.tex`:  It seems the problem stems from `\`@`title` in

```
    \ifsphinxpdfoutput
      \begingroup
      % This \def is required to deal with multi-line authors; it               
      % changes \\ to ', ' (comma-space), making it pass muster for             
      % generating document info in the PDF file.                               
      \def\\{, }
      \pdfinfo{
        /Author (\@author)
        /Title (\@title)
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

archive/issue_comments_052562.json:
```json
{
    "body": "Attachment\n\nAnother approach.  Depends on #7549.  Still experimental.  This patch only.  sage repo.",
    "created_at": "2009-11-29T19:18:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52562",
    "user": "mpatel"
}
```

Attachment

Another approach.  Depends on #7549.  Still experimental.  This patch only.  sage repo.



---

archive/issue_comments_052563.json:
```json
{
    "body": "The [attachment:trac_6495-reference_breakup.patch new patch] may make it possible to build and update reference manual chapters semi-independently.  I think we can use the [intersphinx extension](http://sphinx.pocoo.org/ext/intersphinx.html) to fix the cross-chapter references.  But we'll need to build the manual twice, a la LaTeX.\n\nTo build just a chapter, try, e.g.,\n\n```\nsage -docbuild reference/algebras html -juiv3\n```\n\n\nStill to do:\n\n* Make a combined index page and search page.\n* Check that PDF generation works.\n* Combine chapter PDF files into one large [optional] PDF file (with [pdfjam's](http://www2.warwick.ac.uk/fac/sci/statistics/staff/academic/firth/software/pdfjam) pdfjoin)?\n* Use a specific LaTeX doc title in each `conf.py`.\n* Fix the \"Arithmetic Subgroups\" heading on the top-level page.\n* Use a visual, 2D layout for the top-level page?  Group by general area?  Add icons?\n* Get a reply from [sphinx-dev](http://groups.google.com/group/sphinx-dev/browse_thread/thread/c8e6f0683c65930a) about making relative paths work.\n* Build docs in parallel (cf. #6255) with [multiprocessing](http://docs.python.org/library/multiprocessing.html)?\n* Replace the \"website\" PDF link?\n* User-friendliness improvements.\n* Encourage more compact chapters?  It seems that \"Combinatorics\" takes the most time and memory.\n* ...",
    "created_at": "2009-11-29T19:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52563",
    "user": "mpatel"
}
```

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

archive/issue_comments_052564.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2009-11-29T19:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52564",
    "user": "mpatel"
}
```

Changing priority from minor to major.



---

archive/issue_comments_052565.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-11-29T19:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52565",
    "user": "mpatel"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_052566.json:
```json
{
    "body": "Another important item:\n\n* Use just one `_static` directory for the manual, not 50+!",
    "created_at": "2009-11-29T19:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52566",
    "user": "mpatel"
}
```

Another important item:

* Use just one `_static` directory for the manual, not 50+!



---

archive/issue_comments_052567.json:
```json
{
    "body": "If this approach is viable, I suggest leaving many (most?) of the \"To Do\" items for other tickets.",
    "created_at": "2009-11-29T19:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52567",
    "user": "mpatel"
}
```

If this approach is viable, I suggest leaving many (most?) of the "To Do" items for other tickets.



---

archive/issue_comments_052568.json:
```json
{
    "body": "While I'm here:\n\n* **Copy** PDFs from `output/latex/` to `output/pdf`, so that `make all-pdf`, at least, doesn't do unnecessary work?",
    "created_at": "2009-11-29T20:14:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52568",
    "user": "mpatel"
}
```

While I'm here:

* **Copy** PDFs from `output/latex/` to `output/pdf`, so that `make all-pdf`, at least, doesn't do unnecessary work?



---

archive/issue_comments_052569.json:
```json
{
    "body": "PDF fixes.  This patch only.  sage repo.",
    "created_at": "2009-12-03T00:30:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52569",
    "user": "mpatel"
}
```

PDF fixes.  This patch only.  sage repo.



---

archive/issue_comments_052570.json:
```json
{
    "body": "Attachment\n\nSphinx caches \"foreign\" object inventories in a document's `environment.pickle`.  These now use a lot of disk space.",
    "created_at": "2009-12-03T00:37:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52570",
    "user": "mpatel"
}
```

Attachment

Sphinx caches "foreign" object inventories in a document's `environment.pickle`.  These now use a lot of disk space.



---

archive/issue_comments_052571.json:
```json
{
    "body": "Replying to [comment:9 mpatel]:\n> Sphinx caches \"foreign\" object inventories in a document's `environment.pickle`.  These now use a lot of disk space.\nAnother [sphinx-dev query](http://groups.google.com/group/sphinx-dev/browse_thread/thread/7c0238fe2b8b8b56/e0969058c69b65de?#e0969058c69b65de).",
    "created_at": "2009-12-06T00:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52571",
    "user": "mpatel"
}
```

Replying to [comment:9 mpatel]:
> Sphinx caches "foreign" object inventories in a document's `environment.pickle`.  These now use a lot of disk space.
Another [sphinx-dev query](http://groups.google.com/group/sphinx-dev/browse_thread/thread/7c0238fe2b8b8b56/e0969058c69b65de?#e0969058c69b65de).



---

archive/issue_comments_052572.json:
```json
{
    "body": "Here's a new patch, rebased to Sage 4.7.1.alpha4.  This implements parallel building, and it provides a great speedup, at least on systems with lots of processors.  For example, on sage.math, the time to execute `sage -docbuild reference html -j` went from about 18 minutes to just under 2 minutes.  The main idea is to build each module of the reference manual separately, and use the Sphinx [intersphinx](http://sphinx.pocoo.org/ext/intersphinx.html) extension to handle cross-references (so `:class:`blah`` will work in the algebras module, even if `blah` is defined in the rings module).\n\nRemaining issues:\n\n- The new build uses up more disk space than the old, by about 120 megabytes.  I don't know if anything can be done about this, and I also don't think it's a big deal.  (With the previous patch, it took about 1 gigabyte more, but the more recent patch manages to cut that down: in the previous patch, the `_static` subdirectory of the documentation was being copied, once for each module of the reference manual, and with the new version, a symlink is used instead.)\n- There are now some missing bibliographic references: at some point in the past, people have gone through the documentation and unified the references, but this means that references in one module are not seen by any other.  This can be fixed just by copying the references to the module where they're used.  For example: CMR05 is referenced somewhere in the module on polynomial rings, but the actual item is described in `crypto/mq/sr.py`.\n- The cross-referencing in intersphinx is not perfect; in particular, it doesn't seem to work after building the documents once, it needs to have the full doctree \"inventory\" for any module available before resolving references to that module.  Since the inventory files are built alongside the documentation, this means it has to be built twice (as far as I can tell) before cross-all of the references work.  We could try to figure out dependencies and make sure that if module A is referenced in module B, then A is built first, but that seems complicated, and there is no reason for there not to be circular references.  I'm tempted to just allow broken cross-references.  For the docs on the web site, we would have to make sure they got built twice.\n- There is a main index for the reference manual, but once you click on any entry (like \"Cryptography\"), you get to that module's index, and there is no link taking you back to the main index.  There ought to be a way to fix this, but I haven't figured it out yet.",
    "created_at": "2011-07-07T03:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52572",
    "user": "jhpalmieri"
}
```

Here's a new patch, rebased to Sage 4.7.1.alpha4.  This implements parallel building, and it provides a great speedup, at least on systems with lots of processors.  For example, on sage.math, the time to execute `sage -docbuild reference html -j` went from about 18 minutes to just under 2 minutes.  The main idea is to build each module of the reference manual separately, and use the Sphinx [intersphinx](http://sphinx.pocoo.org/ext/intersphinx.html) extension to handle cross-references (so `:class:`blah`` will work in the algebras module, even if `blah` is defined in the rings module).

Remaining issues:

- The new build uses up more disk space than the old, by about 120 megabytes.  I don't know if anything can be done about this, and I also don't think it's a big deal.  (With the previous patch, it took about 1 gigabyte more, but the more recent patch manages to cut that down: in the previous patch, the `_static` subdirectory of the documentation was being copied, once for each module of the reference manual, and with the new version, a symlink is used instead.)
- There are now some missing bibliographic references: at some point in the past, people have gone through the documentation and unified the references, but this means that references in one module are not seen by any other.  This can be fixed just by copying the references to the module where they're used.  For example: CMR05 is referenced somewhere in the module on polynomial rings, but the actual item is described in `crypto/mq/sr.py`.
- The cross-referencing in intersphinx is not perfect; in particular, it doesn't seem to work after building the documents once, it needs to have the full doctree "inventory" for any module available before resolving references to that module.  Since the inventory files are built alongside the documentation, this means it has to be built twice (as far as I can tell) before cross-all of the references work.  We could try to figure out dependencies and make sure that if module A is referenced in module B, then A is built first, but that seems complicated, and there is no reason for there not to be circular references.  I'm tempted to just allow broken cross-references.  For the docs on the web site, we would have to make sure they got built twice.
- There is a main index for the reference manual, but once you click on any entry (like "Cryptography"), you get to that module's index, and there is no link taking you back to the main index.  There ought to be a way to fix this, but I haven't figured it out yet.



---

archive/issue_comments_052573.json:
```json
{
    "body": "In an ideal world sphinx would be multithreaded, but we probably shouldn't wait for that ;-) The remaining issues about disk space, bibliographic references, and needing two runs seem to be unavoidable. Building parallel gets more and more important, so I think the benefits outweigh the disadvantages. \n\nI tried the patch on Sage-4.7.1.alpha4 without any other patches applied:\n* Only the main page has proper css. For example, `html/en/reference/cmd/index.html` refers to `_static/sage.css` but the correct path would be `../_static/sage.css`.\n* patch conflicts with #11251 (todo extension). Given that the latter is already positively reviewed, maybe this ticket could be rebased on top of it?\n* During the sage build, I think we should then run the docbuilder twice for the reference manual. Perhaps this should always be done for `sage -docbuild all`. \n* Can we make output less verbose? The whole intersphinx output scrolled forever off my screen. Ideally, an interspinx failure to find an inventory file would only add one extra line at the end of the build along the lines of \"You should re-run docbuild to get references right.\"",
    "created_at": "2011-07-07T21:45:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52573",
    "user": "vbraun"
}
```

In an ideal world sphinx would be multithreaded, but we probably shouldn't wait for that ;-) The remaining issues about disk space, bibliographic references, and needing two runs seem to be unavoidable. Building parallel gets more and more important, so I think the benefits outweigh the disadvantages. 

I tried the patch on Sage-4.7.1.alpha4 without any other patches applied:
* Only the main page has proper css. For example, `html/en/reference/cmd/index.html` refers to `_static/sage.css` but the correct path would be `../_static/sage.css`.
* patch conflicts with #11251 (todo extension). Given that the latter is already positively reviewed, maybe this ticket could be rebased on top of it?
* During the sage build, I think we should then run the docbuilder twice for the reference manual. Perhaps this should always be done for `sage -docbuild all`. 
* Can we make output less verbose? The whole intersphinx output scrolled forever off my screen. Ideally, an interspinx failure to find an inventory file would only add one extra line at the end of the build along the lines of "You should re-run docbuild to get references right."



---

archive/issue_comments_052574.json:
```json
{
    "body": "Replying to [comment:13 vbraun]:\n> \n> I tried the patch on Sage-4.7.1.alpha4 without any other patches applied:\n>   * Only the main page has proper css. For example, `html/en/reference/cmd/index.html` refers to `_static/sage.css` but the correct path would be `../_static/sage.css`.\n\nThis was a mistake in the previous version: it was supposed to create a link from `reference/_static` to `reference/cmd/_static`.  Now it should work.\n\n>   * patch conflicts with #11251 (todo extension). Given that the latter is already positively reviewed, maybe this ticket could be rebased on top of it?\n\nGood point.  This raises another problem: intersphinx doesn't easily pass todo lists between different documents, so I don't know how to get a master todo list for the Sage library.  Right now, I've put the todolist for each module after its table of contents.  I think combinat is the only module with any actual to do elements.\n\n>   * During the sage build, I think we should then run the docbuilder twice for the reference manual. Perhaps this should always be done for `sage -docbuild all`. \n\nDone: `sage -docbuild all` now builds the reference manual twice.  I also added a few print statements to the docbuild process.\n\n>   * Can we make output less verbose? The whole intersphinx output scrolled forever off my screen. Ideally, an interspinx failure to find an inventory file would only add one extra line at the end of the build along the lines of \"You should re-run docbuild to get references right.\"\n\nI've tried to do this when doing `sage -docbuild all` and not in general, but it may be suppressing too much output.  (In the first pass, all warnings are suppressed, including intersphinx warnings, and in the second pass, any warnings should be printed.  But in the second pass, it's just rewriting output, taking intersphinx links into account -- it's not reading the sources a second time, so it doesn't produce warnings about missing bibliographic references.)\n\nOther issues:\n\n- In PDF output, this produces one PDF file for each module, but there is no \"master\" file linking to them. I hope we can create one. Should it be an html file or a PDF file?\n\n- We could perhaps speed things up more by breaking the `combinat` module, which is by far the largest, into several pieces.  This can happen on another ticket.\n\n- I've reorganized the main index for the reference manual, grouping modules together by topic.  I hope it's easier to find things this way.  I wonder if we can get intersphinx to produce a master index for all of the documents...\n\n- in the old version, at least on my computer, when I clicked on the Sage logo in the top left corner, it wasn't taking me to the right place.  I've fixed that.  Along the same lines, with the new reorganization, the other links on the top line look a little funny to me in the reference manual.  They looked worse before and I've tried to clean them up, but maybe they could use more work?",
    "created_at": "2011-07-08T17:38:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52574",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_052575.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-07-12T05:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52575",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_052576.json:
```json
{
    "body": "Here's a new version of the patch. This still has the same issue with \"todo\" items: I don't know a way to accumulate all of them from the different Sage modules, so they are just recorded module-by-module.  For PDF output, the main documentation page (in `SAGE_ROOT/devel/sage/doc/output/html/en/index.html`) has the little PDF icons, and now when you click on the one for the reference manual, it actually opens an html file with links to all of the different PDF files.\n\nI'm marking this for review.  If we can come up with a good solution for \"todo\" items, that would be great, but perhaps we could defer it to another ticket.",
    "created_at": "2011-07-12T05:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52576",
    "user": "jhpalmieri"
}
```

Here's a new version of the patch. This still has the same issue with "todo" items: I don't know a way to accumulate all of them from the different Sage modules, so they are just recorded module-by-module.  For PDF output, the main documentation page (in `SAGE_ROOT/devel/sage/doc/output/html/en/index.html`) has the little PDF icons, and now when you click on the one for the reference manual, it actually opens an html file with links to all of the different PDF files.

I'm marking this for review.  If we can come up with a good solution for "todo" items, that would be great, but perhaps we could defer it to another ticket.



---

archive/issue_comments_052577.json:
```json
{
    "body": "Okay, so this is not the most elegant solution, but in the most recent patch, in the html version of the reference manual, after everything is built, it searches through all of the output files algebra/index.html, arithgroup/index.html, etc., looking for todo lists.  When it finds them, it copies them to todolist/index.html.  This only works for the html version; for other formats, the todo list file says \"The combined to do list is only available in the html version of the reference manual.\"",
    "created_at": "2011-07-12T19:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52577",
    "user": "jhpalmieri"
}
```

Okay, so this is not the most elegant solution, but in the most recent patch, in the html version of the reference manual, after everything is built, it searches through all of the output files algebra/index.html, arithgroup/index.html, etc., looking for todo lists.  When it finds them, it copies them to todolist/index.html.  This only works for the html version; for other formats, the todo list file says "The combined to do list is only available in the html version of the reference manual."



---

archive/issue_comments_052578.json:
```json
{
    "body": "Here's a new version; the only difference is this change to SAGE_ROOT/devel/sage/spkg-dist:\n\n```diff\ndiff --git a/spkg-dist b/spkg-dist\n--- a/spkg-dist\n+++ b/spkg-dist\n@@ -38,15 +38,23 @@ fi\n \n # Remove the .cython_hash file, since including this in the bdist will\n # completely break \"sage -br\". \n-# Also, do not distribute these build files (.os and .os); \n+# Also, do not distribute these build files (.so and .os);\n # it wastes space and causes problems!\n \n-rm -f .cython_hash c_lib/*.so c_lib/*.os  \n+rm -f .cython_hash c_lib/*.so c_lib/*.os\n \n # Delete all the autogenerated files, since they will get created again\n # when SAGE is built or upgraded.  \n cd sage; \"$CUR\"/spkg-delauto .; cd ..\n \n+# Delete the autogenerated files in the doc directory.\n+rm -rf doc/output\n+rm -rf doc/en/reference/sage\n+rm -rf doc/en/reference/sagenb\n+rm -rf doc/en/reference/static\n+rm -rf doc/en/reference/templates\n+rm -rf doc/en/reference/*/sage sage/doc/en/reference/*/static sage/doc/en/reference/*/templates\n+\n # Create the sdist using Python's distutils.\n python setup.py sdist\n```\n\nThis makes for a slightly smaller sage-....spkg file, and more importantly, if the old autogenerated files are there, they can confuse the docbuild process.",
    "created_at": "2011-07-13T23:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52578",
    "user": "jhpalmieri"
}
```

Here's a new version; the only difference is this change to SAGE_ROOT/devel/sage/spkg-dist:

```diff
diff --git a/spkg-dist b/spkg-dist
--- a/spkg-dist
+++ b/spkg-dist
@@ -38,15 +38,23 @@ fi
 
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

archive/issue_comments_052579.json:
```json
{
    "body": "Some recent timings on sage.math.  \n\nBefore the patch:\n\n```\n$ rm -rf SAGE_ROOT/devel/sage/doc/output\n$ time sage -docbuild reference html\n...\nreal\t17m49.313s\nuser\t16m57.530s\nsys\t0m45.390s\n\n$ rm -rf SAGE_ROOT/devel/sage/doc/output\n$ time sage -docbuild reference pdf\n...\nreal\t26m3.623s\nuser\t24m40.290s\nsys\t0m43.030s\n```\n\nAfter the patch:\n\n```\n\n$ rm -rf SAGE_ROOT/devel/sage/doc/output\n$ time sage -docbuild reference html\n...\nreal\t2m30.092s\nuser\t10m34.900s\nsys\t1m12.590s\n\n$ rm -rf SAGE_ROOT/devel/sage/doc/output\n$ time sage -docbuild reference pdf\n...\nreal\t3m35.064s\nuser\t15m49.790s\nsys\t1m11.070s\n```\n",
    "created_at": "2011-07-13T23:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52579",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_052580.json:
```json
{
    "body": "Question: if you type \"sage -docbuild -D\" now, it says\n\n```\n$ sage -docbuild -D\nDOCUMENTs:\n    de/tutorial          a_tour_of_sage       bordeaux_2008        \n    constructions        developer            faq                  \n    installation         numerical_sage       reference            \n    thematic_tutorials   tutorial             website              \n    fr/a_tour_of_sage    fr/tutorial          ru/tutorial          \n    all  (!)             \n(!) Builds everything.\n```\n\nShould we also mention \"reference/MODULE\" as a valid target?",
    "created_at": "2011-07-13T23:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52580",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_052581.json:
```json
{
    "body": "use only this patch",
    "created_at": "2011-07-14T15:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52581",
    "user": "jhpalmieri"
}
```

use only this patch



---

archive/issue_comments_052582.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-07-14T15:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52582",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_052583.json:
```json
{
    "body": "use only this patch",
    "created_at": "2011-07-15T20:10:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52583",
    "user": "jhpalmieri"
}
```

use only this patch



---

archive/issue_comments_052584.json:
```json
{
    "body": "Attachment\n\nHere's a new version, with #11298 as a new dependency.  (It may apply without #11298, perhaps with fuzz.)  To help with reviewing, I've broken the patch into two pieces, as explained in the ticket description.",
    "created_at": "2011-07-21T05:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52584",
    "user": "jhpalmieri"
}
```

Attachment

Here's a new version, with #11298 as a new dependency.  (It may apply without #11298, perhaps with fuzz.)  To help with reviewing, I've broken the patch into two pieces, as explained in the ticket description.



---

archive/issue_comments_052585.json:
```json
{
    "body": "Could you post a link to the generated docs so people could browse them?",
    "created_at": "2011-07-26T05:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52585",
    "user": "robertwb"
}
```

Could you post a link to the generated docs so people could browse them?



---

archive/issue_comments_052586.json:
```json
{
    "body": "Replying to [comment:24 robertwb]:\n> Could you post a link to the generated docs so people could browse them? \n\nGood idea:\n\n- [html version](http://sage.math.washington.edu/home/palmieri/misc/6495/output/html/en/reference/)\n- [PDF version](http://sage.math.washington.edu/home/palmieri/misc/6495/output/pdf/en/reference/) (this points to an html document which has links to the pieces of the reference manual in PDF format)",
    "created_at": "2011-07-26T17:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52586",
    "user": "jhpalmieri"
}
```

Replying to [comment:24 robertwb]:
> Could you post a link to the generated docs so people could browse them? 

Good idea:

- [html version](http://sage.math.washington.edu/home/palmieri/misc/6495/output/html/en/reference/)
- [PDF version](http://sage.math.washington.edu/home/palmieri/misc/6495/output/pdf/en/reference/) (this points to an html document which has links to the pieces of the reference manual in PDF format)



---

archive/issue_comments_052587.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-24T23:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52587",
    "user": "was"
}
```

Changing keywords from "" to "sd32".



---

archive/issue_comments_052588.json:
```json
{
    "body": "Testing this against sage-4.8.alpha1 + #10620...",
    "created_at": "2011-11-11T23:24:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52588",
    "user": "jdemeyer"
}
```

Testing this against sage-4.8.alpha1 + #10620...



---

archive/issue_comments_052589.json:
```json
{
    "body": "Against sage-4.8.alpha1:\n\n```\npatching file doc/en/reference/games/index.rst\nHunk #1 FAILED at 6\n1 out of 1 hunks FAILED -- saving rejects to file doc/en/reference/games/index.rst.rej\npatching file doc/en/reference/graphs/index.rst\nHunk #1 succeeded at 52 with fuzz 1 (offset 2 lines).\nabort: patch failed to apply\n```\n",
    "created_at": "2011-11-11T23:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52589",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_052590.json:
```json
{
    "body": "Also: I'm not sure whether building totally in parallel should be the default.",
    "created_at": "2011-11-11T23:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52590",
    "user": "jdemeyer"
}
```

Also: I'm not sure whether building totally in parallel should be the default.



---

archive/issue_comments_052591.json:
```json
{
    "body": "Here are rebased patches, along with the following change: there is now an environment variable, `SAGE_PARALLEL_DOCBUILD`, which if set to anything nonempty which doesn't start with \"n\", causes the reference manual to be built in parallel.  I also added \"doc-parallel\" and \"doc-pdf-parallel\" targets to the main Makefile with a patch to the root repo.",
    "created_at": "2011-11-12T02:04:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52591",
    "user": "jhpalmieri"
}
```

Here are rebased patches, along with the following change: there is now an environment variable, `SAGE_PARALLEL_DOCBUILD`, which if set to anything nonempty which doesn't start with "n", causes the reference manual to be built in parallel.  I also added "doc-parallel" and "doc-pdf-parallel" targets to the main Makefile with a patch to the root repo.



---

archive/issue_comments_052592.json:
```json
{
    "body": "Attachment\n\nroot repo",
    "created_at": "2011-11-12T02:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52592",
    "user": "jhpalmieri"
}
```

Attachment

root repo



---

archive/issue_comments_052593.json:
```json
{
    "body": "By the way, the default in the new patch is to build serially.  I've also added a brief description of SAGE_PARALLEL_DOCBUILD to the installation guide.",
    "created_at": "2011-11-12T02:11:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52593",
    "user": "jhpalmieri"
}
```

By the way, the default in the new patch is to build serially.  I've also added a brief description of SAGE_PARALLEL_DOCBUILD to the installation guide.



---

archive/issue_comments_052594.json:
```json
{
    "body": "Some other possible changes: in the parallel-building code (from builder.py)\n\n```python\n            from multiprocessing import Pool, cpu_count\n            max_cpus = 8 if SAGE_PARALLEL_DOCBUILD else 1\n            pool = Pool(min(max_cpus, cpu_count()))\n```\n\nperhaps change \"else 1\" to \"else 2\"?  As it is, building serially (with max_cpus set to 1) is slower than the current system, because in the new system, the manual has to be built twice to resolve cross-references.\n\nWe could also change \"pool\" to just \"Pool(cpu_count())\" or \"Pool(int(1.5 * cpu_count()))\" or something like that, eliminating the minimum of 8 and possibly increasing the maximum.",
    "created_at": "2011-11-12T03:11:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52594",
    "user": "jhpalmieri"
}
```

Some other possible changes: in the parallel-building code (from builder.py)

```python
            from multiprocessing import Pool, cpu_count
            max_cpus = 8 if SAGE_PARALLEL_DOCBUILD else 1
            pool = Pool(min(max_cpus, cpu_count()))
```

perhaps change "else 1" to "else 2"?  As it is, building serially (with max_cpus set to 1) is slower than the current system, because in the new system, the manual has to be built twice to resolve cross-references.

We could also change "pool" to just "Pool(cpu_count())" or "Pool(int(1.5 * cpu_count()))" or something like that, eliminating the minimum of 8 and possibly increasing the maximum.



---

archive/issue_comments_052595.json:
```json
{
    "body": "Replying to [comment:34 jhpalmieri]:\n> Some other possible changes: in the parallel-building code (from builder.py)\n> {{{\n> #!python\n>             from multiprocessing import Pool, cpu_count\n>             max_cpus = 8 if SAGE_PARALLEL_DOCBUILD else 1\n>             pool = Pool(min(max_cpus, cpu_count()))\n> }}}\n> perhaps change \"else 1\" to \"else 2\"?\nWhy?  It wouldn't make sense to build with more processes than there are CPUs.\n\n> We could also change \"pool\" to just \"Pool(cpu_count())\" or \"Pool(int(1.5 * cpu_count()))\" or something like that, eliminating the minimum of 8 and possibly increasing the maximum.\nWhy?  It wouldn't make sense to build with more processes than there are CPUs.\n\nAs I mentioned on sage-devel, I don't like that there is an option to doctest in parallel, a different option to build the docs in parallel, a different option to build in parallel...  I would say: let there be one environment variable `SAGE_NUM_PROCESSES` or something like that and use that for everything.",
    "created_at": "2011-11-12T07:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52595",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_052596.json:
```json
{
    "body": "Replying to [comment:35 jdemeyer]:\n> Replying to [comment:34 jhpalmieri]:\n> > Some other possible changes: in the parallel-building code (from builder.py)\n> > {{{\n> > #!python\n> >             from multiprocessing import Pool, cpu_count\n> >             max_cpus = 8 if SAGE_PARALLEL_DOCBUILD else 1\n> >             pool = Pool(min(max_cpus, cpu_count()))\n> > }}}\n> > perhaps change \"else 1\" to \"else 2\"?\n> Why?  It wouldn't make sense to build with more processes than there are CPUs.\n\nThis version still does `min(max_cpus, cpu_count())`, so it won't use more processes than there are CPUs.\n\n> > We could also change \"pool\" to just \"Pool(cpu_count())\" or \"Pool(int(1.5 * cpu_count()))\" or something like that, eliminating the minimum of 8 and possibly increasing the maximum.\n> Why?  It wouldn't make sense to build with more processes than there are CPUs.\n\nI see lots of suggestions on the internet to set `MAKE=make -jN` where `N` is 1.5 * (the number of cpus), or 1 or 2 more than the number of cpus.  Why not here as well?\n\n> As I mentioned on sage-devel, I don't like that there is an option to doctest in parallel, a different option to build the docs in parallel, a different option to build in parallel...  I would say: let there be one environment variable `SAGE_NUM_PROCESSES` or something like that and use that for everything.\n\nI think maybe two variables: one (`SAGE_PARALLEL`) to enable parallel processes, one (`SAGE_NUM_THREADS`) to determine the maximum number of processes.  The first could be \"no\" by default, and the second could be \"0\" by default, meaning use `cpu_count()` or `min(8, cpu_count())` or some other variant on this, the way we do with `NUM_THREADS` in `Makefile` and `sage-ptest`.  Then it's easy to turn on and off without remembering how many cores your machine has.",
    "created_at": "2011-11-12T15:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52596",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_052597.json:
```json
{
    "body": "Why not exactly one environment variable \"MAKE\" which gets set to \"make -jN\" for some N, and that is it?     I suggest this, since that's what I'm used to already for years.  I don't claim it is the best solution, but it's in all my .bash* files already, and as John points out above it is documented already all over.   Why don't we just stick with it?",
    "created_at": "2011-11-12T16:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52597",
    "user": "was"
}
```

Why not exactly one environment variable "MAKE" which gets set to "make -jN" for some N, and that is it?     I suggest this, since that's what I'm used to already for years.  I don't claim it is the best solution, but it's in all my .bash* files already, and as John points out above it is documented already all over.   Why don't we just stick with it?



---

archive/issue_comments_052598.json:
```json
{
    "body": "Replying to [comment:37 was]:\n> Why not exactly one environment variable \"MAKE\" which gets set to \"make -jN\" for some N, and that is it?\n\nThat's an interesting idea.  See #12016.",
    "created_at": "2011-11-12T20:47:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52598",
    "user": "jhpalmieri"
}
```

Replying to [comment:37 was]:
> Why not exactly one environment variable "MAKE" which gets set to "make -jN" for some N, and that is it?

That's an interesting idea.  See #12016.



---

archive/issue_comments_052599.json:
```json
{
    "body": "Here's a new patch which uses the setting of `MAKE` to build docs in parallel (or not).  It's very similar to the code in `sage-ptest` from #12016, except that when you run `sage-ptest`, the assumption should be that you want to work in parallel, so the default number of threads (if MAKE is not set) is min(8, #cpus).  For doc building, we shouldn't assume parallel building by default, I guess, so the default number of threads is 1.",
    "created_at": "2011-11-12T21:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52599",
    "user": "jhpalmieri"
}
```

Here's a new patch which uses the setting of `MAKE` to build docs in parallel (or not).  It's very similar to the code in `sage-ptest` from #12016, except that when you run `sage-ptest`, the assumption should be that you want to work in parallel, so the default number of threads (if MAKE is not set) is min(8, #cpus).  For doc building, we shouldn't assume parallel building by default, I guess, so the default number of threads is 1.



---

archive/issue_comments_052600.json:
```json
{
    "body": "Replying to [comment:39 jhpalmieri]:\n> For doc building, we shouldn't assume parallel building by default, I guess, so the default number of threads is 1.\n\nIndeed!",
    "created_at": "2011-11-14T08:23:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52600",
    "user": "jdemeyer"
}
```

Replying to [comment:39 jhpalmieri]:
> For doc building, we shouldn't assume parallel building by default, I guess, so the default number of threads is 1.

Indeed!



---

archive/issue_comments_052601.json:
```json
{
    "body": "Replying to [comment:39 jhpalmieri]:\n> Here's a new patch which uses the setting of `MAKE` to build docs in parallel (or not).  It's very similar to the code in `sage-ptest` from #12016, except that when you run `sage-ptest`, the assumption should be that you want to work in parallel, so the default number of threads (if MAKE is not set) is min(8, #cpus).  For doc building, we shouldn't assume parallel building by default, I guess, so the default number of threads is 1.\n\nSo then we don't need the environment variable `SAGE_PARALLEL_DOCBUILD`, nor the `Makefile` patch, anymore.",
    "created_at": "2011-11-14T09:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52601",
    "user": "jdemeyer"
}
```

Replying to [comment:39 jhpalmieri]:
> Here's a new patch which uses the setting of `MAKE` to build docs in parallel (or not).  It's very similar to the code in `sage-ptest` from #12016, except that when you run `sage-ptest`, the assumption should be that you want to work in parallel, so the default number of threads (if MAKE is not set) is min(8, #cpus).  For doc building, we shouldn't assume parallel building by default, I guess, so the default number of threads is 1.

So then we don't need the environment variable `SAGE_PARALLEL_DOCBUILD`, nor the `Makefile` patch, anymore.



---

archive/issue_comments_052602.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-11-14T09:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52602",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_052603.json:
```json
{
    "body": "With sage-4.8.alpha1, I get\n\n```\nBuilding reference manual, first pass.\n\nsphinx-build -b html -d /mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha2/devel/sage/doc/output/doctrees/en/reference   -A hide_pdf_links=1 -Q  /mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha2/devel/sage/doc/en/reference /mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha2/devel/sage/doc/output/html/en/reference\nBuild finished.  The built documents can be found in /mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha2/devel/sage/doc/output/html/en/reference\nTraceback (most recent call last):\n  File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha2/devel/sage/doc/common/builder.py\", line 1332, in <module>\n    getattr(get_builder(name), type)()\n  File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha2/devel/sage/doc/common/builder.py\", line 288, in _wrapper\n    getattr(get_builder(document), 'html')(*args, **kwds)\n  File \"/mnt/usb1/scratch/jdemeyer/merger/sage-4.8.alpha2/devel/sage/doc/common/builder.py\", line 405, in _wrapper\n    N = re.search('(-j|--jobs[=]?)\\s*([0-9]*)', MAKE).groups()[1]\nUnboundLocalError: local variable 're' referenced before assignment\nmake: *** [doc-html] Error 1\n```\n",
    "created_at": "2011-11-14T11:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52603",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_052604.json:
```json
{
    "body": "> So then we don't need the environment variable SAGE_PARALLEL_DOCBUILD, nor the Makefile patch, anymore.\n\nRight, fixed.  Also, I added `import re` into builder.py; this should fix the other problem as well.",
    "created_at": "2011-11-14T20:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52604",
    "user": "jhpalmieri"
}
```

> So then we don't need the environment variable SAGE_PARALLEL_DOCBUILD, nor the Makefile patch, anymore.

Right, fixed.  Also, I added `import re` into builder.py; this should fix the other problem as well.



---

archive/issue_comments_052605.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-11-14T20:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52605",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_052606.json:
```json
{
    "body": "This now uses `SAGE_NUM_THREADS` from #12016.",
    "created_at": "2011-11-16T04:30:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52606",
    "user": "jhpalmieri"
}
```

This now uses `SAGE_NUM_THREADS` from #12016.



---

archive/issue_comments_052607.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-12-10T13:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52607",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_052608.json:
```json
{
    "body": "Regarding #12016: you should simply use the value of `SAGE_NUM_THREADS`, nothing fancier than that.\n\nRegarding `spkg-dist`: this is essentially a duplicate of #12081 and #12086, so this patch should be removed.  In any case, removing the files from `MANIFEST.in` is the proper way of dealing with this, as opposed to removing the files before packaging the repository.  Ideally, `sage-sdist` should not change the current Sage source tree at all.\n\nWhat's the rationale for adding all these files to `doc/common/themes/sageref`?\n\nInstead of always building twice, would it be possible to **detect** whether the manual has already been built once.  For example, if I want both the HTML and PDF documentation, the current patch would do 4 passes, even if 3 would be sufficient.",
    "created_at": "2011-12-10T13:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52608",
    "user": "jdemeyer"
}
```

Regarding #12016: you should simply use the value of `SAGE_NUM_THREADS`, nothing fancier than that.

Regarding `spkg-dist`: this is essentially a duplicate of #12081 and #12086, so this patch should be removed.  In any case, removing the files from `MANIFEST.in` is the proper way of dealing with this, as opposed to removing the files before packaging the repository.  Ideally, `sage-sdist` should not change the current Sage source tree at all.

What's the rationale for adding all these files to `doc/common/themes/sageref`?

Instead of always building twice, would it be possible to **detect** whether the manual has already been built once.  For example, if I want both the HTML and PDF documentation, the current patch would do 4 passes, even if 3 would be sufficient.



---

archive/issue_comments_052609.json:
```json
{
    "body": "Changing keywords from \"sd32\" to \"\".",
    "created_at": "2012-04-18T04:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52609",
    "user": "jhpalmieri"
}
```

Changing keywords from "sd32" to "".



---

archive/issue_comments_052610.json:
```json
{
    "body": "Rebased to 5.0.beta13, but the intersphinx stuff needs fixing (the use of intersphinx here conflicts with the changes in #9128, and I haven't fixed this).  Part 1 of the patch was mostly generated automatically using the attached script. After running the script, I removed lines like `.. _ch:algebras:` (from algebras/index.rst, in this case) by hand.\n\nReplying to [comment:45 jdemeyer]:\n> Regarding #12016: you should simply use the value of `SAGE_NUM_THREADS`, nothing fancier than that.\n\nOkay, done.\n\n> Regarding `spkg-dist`: this is essentially a duplicate of #12081 and #12086, so this patch should be removed.  In any case, removing the files from `MANIFEST.in` is the proper way of dealing with this, as opposed to removing the files before packaging the repository.  Ideally, `sage-sdist` should not change the current Sage source tree at all.\n\nI removed that part of the patch.\n\n> What's the rationale for adding all these files to `doc/common/themes/sageref`?\n\nThe new structure of the reference manual, in particular the new directory structure, means we need new templates for the files coming from `reference/algebras/index.rst`, as opposed to the old templates, which work for the main file `reference/index.rst`.\n\n> Instead of always building twice, would it be possible to **detect** whether the manual has already been built once.  For example, if I want both the HTML and PDF documentation, the current patch would do 4 passes, even if 3 would be sufficient.\n\nI don't know how to do this.",
    "created_at": "2012-04-18T04:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52610",
    "user": "jhpalmieri"
}
```

Rebased to 5.0.beta13, but the intersphinx stuff needs fixing (the use of intersphinx here conflicts with the changes in #9128, and I haven't fixed this).  Part 1 of the patch was mostly generated automatically using the attached script. After running the script, I removed lines like `.. _ch:algebras:` (from algebras/index.rst, in this case) by hand.

Replying to [comment:45 jdemeyer]:
> Regarding #12016: you should simply use the value of `SAGE_NUM_THREADS`, nothing fancier than that.

Okay, done.

> Regarding `spkg-dist`: this is essentially a duplicate of #12081 and #12086, so this patch should be removed.  In any case, removing the files from `MANIFEST.in` is the proper way of dealing with this, as opposed to removing the files before packaging the repository.  Ideally, `sage-sdist` should not change the current Sage source tree at all.

I removed that part of the patch.

> What's the rationale for adding all these files to `doc/common/themes/sageref`?

The new structure of the reference manual, in particular the new directory structure, means we need new templates for the files coming from `reference/algebras/index.rst`, as opposed to the old templates, which work for the main file `reference/index.rst`.

> Instead of always building twice, would it be possible to **detect** whether the manual has already been built once.  For example, if I want both the HTML and PDF documentation, the current patch would do 4 passes, even if 3 would be sufficient.

I don't know how to do this.



---

archive/issue_comments_052611.json:
```json
{
    "body": "This patch would allow building the reference manual with less memory usage.  1.5GB (still a lot) is sufficient to build the manual, as opposed to more than 2GB without the patch.",
    "created_at": "2012-04-18T11:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52611",
    "user": "jdemeyer"
}
```

This patch would allow building the reference manual with less memory usage.  1.5GB (still a lot) is sufficient to build the manual, as opposed to more than 2GB without the patch.



---

archive/issue_comments_052612.json:
```json
{
    "body": "I do get several warnings when building the HTML manual.  The following is repeated many times:\n\n```\nsphinx-build -b html -d /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/doctrees/de/tutorial   -A hide_pdf_links=1  /fast_scr\natch/jdemeyer/sage-5.0.beta13/devel/sage/doc/de/tutorial /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/html/de/tutorial\nRunning Sphinx v1.1.2\nloading translations [de]... done\nloading pickled environment... not yet created\nloading intersphinx inventory from /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/common/python.inv...\nloading intersphinx inventory from /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/html/en/reference/objects.inv...\nWARNING: intersphinx inventory '/fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/html/en/reference/objects.inv' not fetchable\ndue to <type 'exceptions.IOError'>: [Errno 2] No such file or directory: '/fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/htm\nl/en/reference/objects.inv'\nbuilding [html]: targets for 22 source files that are out of date\nupdating environment: 22 added, 0 changed, 0 removed\n[...]\nBuild finished.  The built documents can be found in /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/html/de/tutorial\n```\n\n\nThere are several of the form:\n\n```\nsphinx-build -b html -d /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/doctrees/en/reference/schemes   -A hide_pdf_links=1  -q  -a  /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/en/reference/schemes /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/html/en/reference/schemes\nNone:37: WARNING: citation not found: Fulton\nBuild finished.  The built documents can be found in /fast_scratch/jdemeyer/sage-5.0.beta13/devel/sage/doc/output/html/en/reference/schemes\n```\n",
    "created_at": "2012-04-18T11:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52612",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_052613.json:
```json
{
    "body": "The intersphinx stuff actually seems to be working, despite [comment:47 my earlier comment]. I'll keep testing it to make sure, but I think it's okay.\n\nRegarding the warnings: the missing intersphinx inventories are expected. That's why we have to build everything twice: once to create all of the inventory files, and then a second time to use them. At least for me, if I run `sage --docbuild reference html` twice in a row, I don't get these warnings the second time through. The citation warnings need to be fixed, though.",
    "created_at": "2012-04-18T17:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52613",
    "user": "jhpalmieri"
}
```

The intersphinx stuff actually seems to be working, despite [comment:47 my earlier comment]. I'll keep testing it to make sure, but I think it's okay.

Regarding the warnings: the missing intersphinx inventories are expected. That's why we have to build everything twice: once to create all of the inventory files, and then a second time to use them. At least for me, if I run `sage --docbuild reference html` twice in a row, I don't get these warnings the second time through. The citation warnings need to be fixed, though.



---

archive/issue_comments_052614.json:
```json
{
    "body": "Hi John,\n\nWhat is the status of this one ? It this robust ?\n\nI'm quite glad that I didn't stomp on your foot with #9128, but I may be right\nnow in the process on jumping high to land on your foot ;-/: I just dived deep\ninside Sphinx and using ``@`parallel`, I managed to have the \"writing\noutput...\" part of the doc compilation in parallel. I've right now no idea how\nrobust it is. I'll put a log of my experiment on #6255. Also, it seems\npossible that the read part could also be made parallel.\n\nFlorent",
    "created_at": "2012-04-20T22:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52614",
    "user": "hivert"
}
```

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

archive/issue_comments_052615.json:
```json
{
    "body": "Hi Florent,\n\nThis is in pretty good shape, but it's not perfect. It undoes some of what you did in #9128 (mainly because I haven't tried to rewrite the patch to do it differently), and in particular, I'm not sure that the other parts of the Sage documentation can use intersphinx to access information from the reference manual. Citations may be an issue, in particular if the same reference is cited twice in two different parts of the reference manual: we may just need to add another copy of the citation, or perhaps a master list of citations that gets used by everything. I don't know if that's practical.\n\nThere are also issues with having to build the reference manual twice so that all of the references are resolved. This is not ideal.\n\nI think that doing the reading and/or writing in parallel would be good, but given the size of the reference manual, breaking it into pieces seems worthwhile as well. If the parallel reading and writing help to cut down on the memory usage, which seems to be getting out of hand, then maybe that is good enough for now.  (At least on sage.math, the writing part seems to take way too long, so doing that in parallel might help significantly.)\n\nSo if you have a workable solution which accomplishes some of what is done here, and perhaps does it more simply, go right ahead. I'll take a look at your comments at #6255.\n\nJohn",
    "created_at": "2012-04-20T22:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52615",
    "user": "jhpalmieri"
}
```

Hi Florent,

This is in pretty good shape, but it's not perfect. It undoes some of what you did in #9128 (mainly because I haven't tried to rewrite the patch to do it differently), and in particular, I'm not sure that the other parts of the Sage documentation can use intersphinx to access information from the reference manual. Citations may be an issue, in particular if the same reference is cited twice in two different parts of the reference manual: we may just need to add another copy of the citation, or perhaps a master list of citations that gets used by everything. I don't know if that's practical.

There are also issues with having to build the reference manual twice so that all of the references are resolved. This is not ideal.

I think that doing the reading and/or writing in parallel would be good, but given the size of the reference manual, breaking it into pieces seems worthwhile as well. If the parallel reading and writing help to cut down on the memory usage, which seems to be getting out of hand, then maybe that is good enough for now.  (At least on sage.math, the writing part seems to take way too long, so doing that in parallel might help significantly.)

So if you have a workable solution which accomplishes some of what is done here, and perhaps does it more simply, go right ahead. I'll take a look at your comments at #6255.

John



---

archive/issue_comments_052616.json:
```json
{
    "body": "Hi John,\n\nThanks for the quick answer.\n\n> This is in pretty good shape, but it's not perfect. It undoes some of what\n> you did in #9128 (mainly because I haven't tried to rewrite the patch to do\n> it differently), and in particular, I'm not sure that the other parts of the\n> Sage documentation can use intersphinx to access information from the\n> reference manual.\n\nI'll have a look at it. Please do not hesitate to ask for some more\nexplanation on the hack I did with intersphinx. Is there a specific reason why\nyou doubt intersphinx will work for the other part of the doc ?\n\n> There are also issues with having to build the reference manual twice so\n> that all of the references are resolved. This is not ideal.\n\nIt doesn't seem to be a huge problem with LaTeX, since this never has been\nsolved since years... Though I never seen a LaTeX compilation as long as\nSage's doc.\n\n> I think that doing the reading and/or writing in parallel would be good, but\n> given the size of the reference manual, breaking it into pieces seems\n> worthwhile as well.\n\nI agree.\n\n> If the parallel reading and writing help to cut down on the memory usage,\n> which seems to be getting out of hand, then maybe that is good enough for\n> now.  (At least on sage.math, the writing part seems to take way too long,\n> so doing that in parallel might help significantly.)\n\nI don't think it will cut down memory usage in any way. I'd rather expect the\ncontrary. My solution seems to be working but since I currently for a sage for\nevery single file, a lot of time is wasted in forking. I'll try to improve it\ntomorrow.\n\n> So if you have a workable solution which accomplishes some of what is done\n> here, and perhaps does it more simply, go right ahead. I'll take a look at\n> your comments at #6255.\n\nI don't think I really will. As I said I'll probably trade speed against\nmemory usage... I'll keep you in touch.\n\nCheers,\n\nFlorent",
    "created_at": "2012-04-20T22:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52616",
    "user": "hivert"
}
```

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

archive/issue_comments_052617.json:
```json
{
    "body": "Replying to [comment:54 hivert]:\n> I don't think it will cut down memory usage in any way. I'd rather expect the\n> contrary.\nMemory usage is already too much, so anything that further increases memory usage is very bad.",
    "created_at": "2012-04-21T10:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52617",
    "user": "jdemeyer"
}
```

Replying to [comment:54 hivert]:
> I don't think it will cut down memory usage in any way. I'd rather expect the
> contrary.
Memory usage is already too much, so anything that further increases memory usage is very bad.



---

archive/issue_comments_052618.json:
```json
{
    "body": "Replying to [comment:55 jdemeyer]:\n> Replying to [comment:54 hivert]:\n> > I don't think it will cut down memory usage in any way. I'd rather expect the\n> > contrary.\n> Memory usage is already too much, so anything that further increases memory usage is very bad.\n\nI respectfully disagree if \n- it is optional\n- it divide by more than 10 the documentation compile time",
    "created_at": "2012-04-21T11:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52618",
    "user": "hivert"
}
```

Replying to [comment:55 jdemeyer]:
> Replying to [comment:54 hivert]:
> > I don't think it will cut down memory usage in any way. I'd rather expect the
> > contrary.
> Memory usage is already too much, so anything that further increases memory usage is very bad.

I respectfully disagree if 
- it is optional
- it divide by more than 10 the documentation compile time



---

archive/issue_comments_052619.json:
```json
{
    "body": "Replying to [comment:56 hivert]:\n> Replying to [comment:55 jdemeyer]:\n> > Replying to [comment:54 hivert]:\n> > > I don't think it will cut down memory usage in any way. I'd rather expect the\n> > > contrary.\n> > Memory usage is already too much, so anything that further increases memory usage is very bad.\n\nLike adding more modules and functions to the Sage library, and rising the \"doc[test] coverage\"... ;-)\n\n\n\n\n> I respectfully disagree if \n> - it is optional\n\nThat would be fine.\n\n> - it divides by more than 10 the documentation compile time\n\nWow... :P",
    "created_at": "2012-04-21T13:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52619",
    "user": "leif"
}
```

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

archive/issue_comments_052620.json:
```json
{
    "body": "This is an *extremely* useful patch which should go in Sage ASAP. It\neffectively reduce the compilation time to 10min on my I7 laptop. This is\nbrilliant. It will certainly prove more maintainable in the long term than my\nparallelization of Sphinx expertiment. Though, I think we should discuss of is\nwith Georges Brandl (the maintainer of Sphinx).\n\nI'm now reviewing the code itself. You'll find below some comments.\n\nFlorent\n\n**Suggestion of improvement**:\n\n- I think we should get rid of the warning on the first pass, maybe by\n  patching a little bit intersphinx. Also, now the compilation is a lot more\n  verbose. Maybe we should silent the info for loading the bunch of\n  intersphinx load at least in `reference/*`. If you agree with the idea,\n  I'm Ok to look at this one.\n\n- Some directories are much longer than the other (eg: combinat) they should\n  be launched first (or maybe in this case broken in even smaller parts). This\n  could wait for another ticket.\n\n**Some remaining problems**:\n\n- Interrupting the compilation with `ctrl+C` doesn't work. I had to kill\n  by hand the master compilation process. I'm not sure what we can do for\n  solving this problem.\n\n- On the main page, you managed to gather the todos which is great ! Is it\n  possible to do the same for the index (mine is empty). The module index is\n  moreover broken.",
    "created_at": "2012-04-23T16:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52620",
    "user": "hivert"
}
```

This is an *extremely* useful patch which should go in Sage ASAP. It
effectively reduce the compilation time to 10min on my I7 laptop. This is
brilliant. It will certainly prove more maintainable in the long term than my
parallelization of Sphinx expertiment. Though, I think we should discuss of is
with Georges Brandl (the maintainer of Sphinx).

I'm now reviewing the code itself. You'll find below some comments.

Florent

**Suggestion of improvement**:

- I think we should get rid of the warning on the first pass, maybe by
  patching a little bit intersphinx. Also, now the compilation is a lot more
  verbose. Maybe we should silent the info for loading the bunch of
  intersphinx load at least in `reference/*`. If you agree with the idea,
  I'm Ok to look at this one.

- Some directories are much longer than the other (eg: combinat) they should
  be launched first (or maybe in this case broken in even smaller parts). This
  could wait for another ticket.

**Some remaining problems**:

- Interrupting the compilation with `ctrl+C` doesn't work. I had to kill
  by hand the master compilation process. I'm not sure what we can do for
  solving this problem.

- On the main page, you managed to gather the todos which is great ! Is it
  possible to do the same for the index (mine is empty). The module index is
  moreover broken.



---

archive/issue_comments_052621.json:
```json
{
    "body": "Hi John, \n\nUsing your patch I realized that for the first stage, you don't need to get the html file only the pickle and `object.inv` file. Did you try to do that ? It seems that this is easily feasible with a custom Builder. I'm currently testing this workflow.\n\nFlorent",
    "created_at": "2012-04-23T21:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52621",
    "user": "hivert"
}
```

Hi John, 

Using your patch I realized that for the first stage, you don't need to get the html file only the pickle and `object.inv` file. Did you try to do that ? It seems that this is easily feasible with a custom Builder. I'm currently testing this workflow.

Florent



---

archive/issue_comments_052622.json:
```json
{
    "body": "Another comment: You should start by building the reference manual and then the other component. Currently in\n`class AllBuilder` method `_wrapper` you start by building the other documents.\n\nFlorent",
    "created_at": "2012-04-23T21:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52622",
    "user": "hivert"
}
```

Another comment: You should start by building the reference manual and then the other component. Currently in
`class AllBuilder` method `_wrapper` you start by building the other documents.

Florent



---

archive/issue_comments_052623.json:
```json
{
    "body": "I just attached a new patch which defines a new builder for creating the pickle and `object.inv` file. It can be called by \n\n```\nsage -docbuild DOCUMENT invpickle\n```\n\nIt is automatically called for the first pass when building `DOCUMENT=all`. As a consequence on my laptop the first pass in only 2 min and a half long. \n\nFlorent",
    "created_at": "2012-04-23T21:59:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52623",
    "user": "hivert"
}
```

I just attached a new patch which defines a new builder for creating the pickle and `object.inv` file. It can be called by 

```
sage -docbuild DOCUMENT invpickle
```

It is automatically called for the first pass when building `DOCUMENT=all`. As a consequence on my laptop the first pass in only 2 min and a half long. 

Florent



---

archive/issue_comments_052624.json:
```json
{
    "body": "The `invpickle` builder seem quite efficient here are the timing on my I7 laptop:\n- First stage:  02:36\n- Second Stage: 08:06\nWithout my patch the first stage is 10:19 long. \n\nFlorent",
    "created_at": "2012-04-23T22:24:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52624",
    "user": "hivert"
}
```

The `invpickle` builder seem quite efficient here are the timing on my I7 laptop:
- First stage:  02:36
- Second Stage: 08:06
Without my patch the first stage is 10:19 long. 

Florent



---

archive/issue_comments_052625.json:
```json
{
    "body": "There is also a failure:\n\n```\nsage -t  builder.py\nFile \"/home/data/Sage-Install/sage-5.0.beta13/devel/sage-doc/doc/common/builder.py\", line 862:\n    [...]\n    sage: builder.ReferenceBuilder(\"reference\").auto_rest_filename(\"sage.combinat.partition\")\n      File \"/home/data/Sage-Install/sage-5.0.beta13/devel/sage/doc/common/builder.py\", line 409, in _wrapper\n        getattr(DocBuilder(self.name, lang), format)(*args, **kwds)\n    AttributeError: 'DocBuilder' object has no attribute 'auto_rest_filename'\n```\n",
    "created_at": "2012-04-23T23:03:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52625",
    "user": "hivert"
}
```

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

archive/issue_comments_052626.json:
```json
{
    "body": "Hi Florent,\n\nYour ideas look great; I hope you can keep working on them. I am happy with all of your suggestions. In particular:\n\n- building the reference manual before the other documents is fine. I think that was your approach in #9128, and the original patch here built the reference manual last. I hadn't gotten around to changing it to build the reference manual first.\n\n- I'll try to take a look at combining the indices, the way the todo lists are combined.\n\n- further subdividing combinat (for example) is a good idea, but I also agree that it belongs on another ticket.\n\n- I've also noticed that ctrl-C doesn't quit the process. Any ideas why? Should we run the parallel processes differently, maybe using the methods you suggested at #6255?\n\nBy the way, mpatel should get a lot of the credit for this; he wrote the original patches, which I've just cleaned up and reorganized.",
    "created_at": "2012-04-24T17:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52626",
    "user": "jhpalmieri"
}
```

Hi Florent,

Your ideas look great; I hope you can keep working on them. I am happy with all of your suggestions. In particular:

- building the reference manual before the other documents is fine. I think that was your approach in #9128, and the original patch here built the reference manual last. I hadn't gotten around to changing it to build the reference manual first.

- I'll try to take a look at combining the indices, the way the todo lists are combined.

- further subdividing combinat (for example) is a good idea, but I also agree that it belongs on another ticket.

- I've also noticed that ctrl-C doesn't quit the process. Any ideas why? Should we run the parallel processes differently, maybe using the methods you suggested at #6255?

By the way, mpatel should get a lot of the credit for this; he wrote the original patches, which I've just cleaned up and reorganized.



---

archive/issue_comments_052627.json:
```json
{
    "body": "I got two doctest failures (after applying your patch), which can be fixed with this patch:\n\n```diff\ndiff --git a/doc/common/builder.py b/doc/common/builder.py\n--- a/doc/common/builder.py\n+++ b/doc/common/builder.py\n@@ -200,7 +200,7 @@ class DocBuilder(object):\n             sage: import os, sys; sys.path.append(os.environ['SAGE_DOC']+'/common/'); import builder\n             sage: b = builder.DocBuilder('tutorial')\n             sage: b._output_formats()\n-            ['changes', 'html', 'htmlhelp', 'json', 'latex', 'linkcheck', 'pickle', 'web']\n+            ['changes', 'html', 'htmlhelp', 'invpickle', 'json', 'latex', 'linkcheck', 'pickle', 'web']\n \n         \"\"\"\n         #Go through all the attributes of self and check to\n@@ -859,7 +859,7 @@ class ReferenceSubBuilder(DocBuilder):\n \n             sage: import os, sys; sys.path.append(os.environ['SAGE_DOC']+'/common/'); import builder\n             sage: import builder\n-            sage: builder.ReferenceBuilder(\"reference\").auto_rest_filename(\"sage.combinat.partition\")\n+            sage: builder.ReferenceSubBuilder(\"reference\").auto_rest_filename(\"sage.combinat.partition\")\n             '.../devel/sage/doc/en/reference/sage/combinat/partition.rst'\n         \"\"\"\n         return self.dir + os.path.sep + module_name.replace('.',os.path.sep) + '.rst'\n```\n",
    "created_at": "2012-04-24T18:40:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52627",
    "user": "jhpalmieri"
}
```

I got two doctest failures (after applying your patch), which can be fixed with this patch:

```diff
diff --git a/doc/common/builder.py b/doc/common/builder.py
--- a/doc/common/builder.py
+++ b/doc/common/builder.py
@@ -200,7 +200,7 @@ class DocBuilder(object):
             sage: import os, sys; sys.path.append(os.environ['SAGE_DOC']+'/common/'); import builder
             sage: b = builder.DocBuilder('tutorial')
             sage: b._output_formats()
-            ['changes', 'html', 'htmlhelp', 'json', 'latex', 'linkcheck', 'pickle', 'web']
+            ['changes', 'html', 'htmlhelp', 'invpickle', 'json', 'latex', 'linkcheck', 'pickle', 'web']
 
         """
         #Go through all the attributes of self and check to
@@ -859,7 +859,7 @@ class ReferenceSubBuilder(DocBuilder):
 
             sage: import os, sys; sys.path.append(os.environ['SAGE_DOC']+'/common/'); import builder
             sage: import builder
-            sage: builder.ReferenceBuilder("reference").auto_rest_filename("sage.combinat.partition")
+            sage: builder.ReferenceSubBuilder("reference").auto_rest_filename("sage.combinat.partition")
             '.../devel/sage/doc/en/reference/sage/combinat/partition.rst'
         """
         return self.dir + os.path.sep + module_name.replace('.',os.path.sep) + '.rst'
```




---

archive/issue_comments_052628.json:
```json
{
    "body": "By the way, searching is broken with these patches. The files `searchindex.js` (both in `reference/` and in its various subdirectories) are all essentially empty.  Hmm.\n\nIt looks like combining the indices should be doable, but a little annoying: read in the html from each, extract the entries, sort them, and rewrite to a new index file. The same should work for the module index. I think talking to Georg Brandl makes sense: if we wanted Sphinx to support this kind of thing out of the box, what exactly would we be looking for?  I guess at the least we want separate Sphinx documents which share indices, searches, and inventories. It would be nice to have a specific \"Sphinx Enhancement Proposal\", or even some code to contribute.",
    "created_at": "2012-04-24T18:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52628",
    "user": "jhpalmieri"
}
```

By the way, searching is broken with these patches. The files `searchindex.js` (both in `reference/` and in its various subdirectories) are all essentially empty.  Hmm.

It looks like combining the indices should be doable, but a little annoying: read in the html from each, extract the entries, sort them, and rewrite to a new index file. The same should work for the module index. I think talking to Georg Brandl makes sense: if we wanted Sphinx to support this kind of thing out of the box, what exactly would we be looking for?  I guess at the least we want separate Sphinx documents which share indices, searches, and inventories. It would be nice to have a specific "Sphinx Enhancement Proposal", or even some code to contribute.



---

archive/issue_comments_052629.json:
```json
{
    "body": "Hi John,\n\nAnother reason to have this in Sage ASAP: #12878\n\nI'm willing to help on this one but we need to coordinate. I'll be in Montreal\nfor the next Sage days 38 so hopefully will have so time for Sphinx. Do you think\nyou'll have so time on it in the forthcoming weeks ? Please tell me what I can\ndo to help. Here are a few suggestions:\n\n- **avoiding to build the full doc twice**: If you agree with the idea of\n  the invpicke builder, I can polish it a little more. Also the name is far\n  from being perfect and I'm open to any suggestion.\n\n- **Intersphinx being too verbose**: I don't think we can silence\n  intersphinx a little without patching Sphinx. I can try to do it by some\n  Monkey patch.\n\n- **Parallelizing the rests of the doc**: I noticed that the refman is build\n  in parallel but the other documents are build in series. We should build\n  them in parallel too. I'll look for the easiest way.\n\nCheers,\n\nFlorent",
    "created_at": "2012-04-24T23:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52629",
    "user": "hivert"
}
```

Hi John,

Another reason to have this in Sage ASAP: #12878

I'm willing to help on this one but we need to coordinate. I'll be in Montreal
for the next Sage days 38 so hopefully will have so time for Sphinx. Do you think
you'll have so time on it in the forthcoming weeks ? Please tell me what I can
do to help. Here are a few suggestions:

- **avoiding to build the full doc twice**: If you agree with the idea of
  the invpicke builder, I can polish it a little more. Also the name is far
  from being perfect and I'm open to any suggestion.

- **Intersphinx being too verbose**: I don't think we can silence
  intersphinx a little without patching Sphinx. I can try to do it by some
  Monkey patch.

- **Parallelizing the rests of the doc**: I noticed that the refman is build
  in parallel but the other documents are build in series. We should build
  them in parallel too. I'll look for the easiest way.

Cheers,

Florent



---

archive/issue_comments_052630.json:
```json
{
    "body": "I hope I have time to work on it next week, although right now I have other things I need to be doing (like reading my student's PhD thesis).\n\n- I really like the idea of the invpickle builder, so please continue with that. I don't have any better suggestions for the name.\n- The verbosity of intersphinx is a minor issue. If we can reduce it, that would be fine, but it's not the highest priority, in my opinion.\n- I think it shouldn't be too hard to parallelize building the rest of the docs. We want to do it so that hitting ctrl-c will quit the build. I think we should try using tools from sage.parallel rather than the Python multiprocessing module. If you want to work on that, that would be great.\n\nAlso:\n\n- I can try to work on the indices.\n- I will investigate why the searchindex.js files are empty, but right now I have no idea.\n\nI will try to post any progress that I make, and you should do likewise, so we don't end up duplicating each other's work.",
    "created_at": "2012-04-25T03:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52630",
    "user": "jhpalmieri"
}
```

I hope I have time to work on it next week, although right now I have other things I need to be doing (like reading my student's PhD thesis).

- I really like the idea of the invpickle builder, so please continue with that. I don't have any better suggestions for the name.
- The verbosity of intersphinx is a minor issue. If we can reduce it, that would be fine, but it's not the highest priority, in my opinion.
- I think it shouldn't be too hard to parallelize building the rest of the docs. We want to do it so that hitting ctrl-c will quit the build. I think we should try using tools from sage.parallel rather than the Python multiprocessing module. If you want to work on that, that would be great.

Also:

- I can try to work on the indices.
- I will investigate why the searchindex.js files are empty, but right now I have no idea.

I will try to post any progress that I make, and you should do likewise, so we don't end up duplicating each other's work.



---

archive/issue_comments_052631.json:
```json
{
    "body": "As far as handling ctrl-c, I found [this question](http://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-pool). It seems we can replace `pool.apply_async(ARGS)` with `pool.apply_async(ARGS).get(999999)`. This apparently adds a (very long) timeout to the process, and it apparently works around a bug in Python. In practice, it seems to work for me.\n\n```diff\ndiff --git a/doc/common/builder.py b/doc/common/builder.py\n--- a/doc/common/builder.py\n+++ b/doc/common/builder.py\n@@ -415,7 +415,7 @@ class ReferenceBuilder(AllBuilder):\n             for doc in self.get_all_documents(refdir):\n                 pool.apply_async(build_ref_doc,\n                                  (doc, lang, format,\n-                                  os.path.split(output_dir)[0]) + args, kwds)\n+                                  os.path.split(output_dir)[0]) + args, kwds).get(999999)\n             pool.close()\n             pool.join()\n             if format == 'html':\n```\n",
    "created_at": "2012-04-25T05:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52631",
    "user": "jhpalmieri"
}
```

As far as handling ctrl-c, I found [this question](http://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-pool). It seems we can replace `pool.apply_async(ARGS)` with `pool.apply_async(ARGS).get(999999)`. This apparently adds a (very long) timeout to the process, and it apparently works around a bug in Python. In practice, it seems to work for me.

```diff
diff --git a/doc/common/builder.py b/doc/common/builder.py
--- a/doc/common/builder.py
+++ b/doc/common/builder.py
@@ -415,7 +415,7 @@ class ReferenceBuilder(AllBuilder):
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

archive/issue_comments_052632.json:
```json
{
    "body": "Replying to [comment:68 jhpalmieri]:\n>  - I really like the idea of the invpickle builder, so please continue with that. I don't have any better suggestions for the name.\n\nOne should perhaps just expand the name to contain \"inventory\"; \"pickle\" is IMHO minor (or irrelevant) and won't tell most(?) people much.\n \n>  - The verbosity of intersphinx is a minor issue. If we can reduce it, that would be fine, but it's not the highest priority, in my opinion.\n\nMine, too.  Although I hate Sphinx's / Sage's current messages already, especially since *\"Build succeeded.  The built documents can be found in ...\"* is **always** printed, so is plain wrong in case of an error.  (We tried to fix that once, but then I think Jeroen decided to keep it as is.)\n\n>  - I think it shouldn't be too hard to parallelize building the rest of the docs. We want to do it so that hitting ctrl-c will quit the build. I think we should try using tools from sage.parallel rather than the Python multiprocessing module. If you want to work on that, that would be great.\n\nWhy not just use `make`?  Either add (and change the) targets in the top-level `Makefile`, or add one to `devel/sage/doc/`.  To me seems cleanest (preferably the latter), and docbuilding IMHO shouldn't depend [more] on the Sage library [as needed / it already does].",
    "created_at": "2012-04-25T05:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52632",
    "user": "leif"
}
```

Replying to [comment:68 jhpalmieri]:
>  - I really like the idea of the invpickle builder, so please continue with that. I don't have any better suggestions for the name.

One should perhaps just expand the name to contain "inventory"; "pickle" is IMHO minor (or irrelevant) and won't tell most(?) people much.
 
>  - The verbosity of intersphinx is a minor issue. If we can reduce it, that would be fine, but it's not the highest priority, in my opinion.

Mine, too.  Although I hate Sphinx's / Sage's current messages already, especially since *"Build succeeded.  The built documents can be found in ..."* is **always** printed, so is plain wrong in case of an error.  (We tried to fix that once, but then I think Jeroen decided to keep it as is.)

>  - I think it shouldn't be too hard to parallelize building the rest of the docs. We want to do it so that hitting ctrl-c will quit the build. I think we should try using tools from sage.parallel rather than the Python multiprocessing module. If you want to work on that, that would be great.

Why not just use `make`?  Either add (and change the) targets in the top-level `Makefile`, or add one to `devel/sage/doc/`.  To me seems cleanest (preferably the latter), and docbuilding IMHO shouldn't depend [more] on the Sage library [as needed / it already does].



---

archive/issue_comments_052633.json:
```json
{
    "body": "The problem with using `make` is that I want to be able to run `sage --docbuild all html`, and I don't think that running this should call `make`. The fix I mentioned above for interrupts (adding a timeout) doesn't make use of the sage.parallel module, just plain Python, by the way. So we should be able to do this for building all of the documents in parallel.",
    "created_at": "2012-04-25T17:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52633",
    "user": "jhpalmieri"
}
```

The problem with using `make` is that I want to be able to run `sage --docbuild all html`, and I don't think that running this should call `make`. The fix I mentioned above for interrupts (adding a timeout) doesn't make use of the sage.parallel module, just plain Python, by the way. So we should be able to do this for building all of the documents in parallel.



---

archive/issue_comments_052634.json:
```json
{
    "body": "Replying to [comment:69 jhpalmieri]:\n> As far as handling ctrl-c, I found [this question](http://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-pool). It seems we can replace `pool.apply_async(ARGS)` with `pool.apply_async(ARGS).get(999999)`. This apparently adds a (very long) timeout to the process, and it apparently works around a bug in Python. In practice, it seems to work for me.\n\nDoes it really work ? For me is seems that ctrl-c is now working but the doc is no more compiling in parallel.\n\nFlorent",
    "created_at": "2012-05-01T20:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52634",
    "user": "hivert"
}
```

Replying to [comment:69 jhpalmieri]:
> As far as handling ctrl-c, I found [this question](http://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-pool). It seems we can replace `pool.apply_async(ARGS)` with `pool.apply_async(ARGS).get(999999)`. This apparently adds a (very long) timeout to the process, and it apparently works around a bug in Python. In practice, it seems to work for me.

Does it really work ? For me is seems that ctrl-c is now working but the doc is no more compiling in parallel.

Florent



---

archive/issue_comments_052635.json:
```json
{
    "body": "Concerning todos (and maybe indexes too), I think I've found an alternative:\nthey are pickled in the files `environment.pickle`. Here is an example, in\nthe directory `doc/output/doctrees/en/reference/modules`:\n\n```\nsage: import cPickle\nsage: f = open('environment.pickle', 'rb')\nsage: env = cPickle.load(f)\nsage: f.close()\nsage: env.todo_all_todos\n[{'docname': 'sage/modules/free_module', 'source': u'/home/data/Sage-Install/sage-5.0.beta14/local/lib/python2.7/site-packages/sage/modules/free_module.py:docstring of sage.modules.free_module.FreeModuleFactory', 'todo': <todo_node: <title...><paragraph...>>, 'lineno': 122, 'target': <target: >}]\nsage: env.indexentries.keys()\n['index', 'sage/modules/free_module_element', 'sage/modules/real_double_vector', 'sage/modules/matrix_morphism', 'sage/modules/fg_pid/fgp_module', 'sage/modules/free_module_homspace', 'sage/modules/vector_space_homspace', 'sage/modules/fg_pid/fgp_element', 'sage/modules/complex_double_vector', 'sage/modules/fg_pid/fgp_morphism', 'sage/modules/vector_callable_symbolic_dense', 'sage/modules/module', 'sage/modules/free_module_morphism', 'sage/modules/vector_space_morphism', 'sage/modules/free_module']\n```\n\nSo it seems that we can get them from there from the pickle concatenate them\nand let sphinx output the todo list and the index.\n\nFlorent",
    "created_at": "2012-05-01T21:43:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52635",
    "user": "hivert"
}
```

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

archive/issue_comments_052636.json:
```json
{
    "body": "Replying to [comment:73 hivert]:\n> So it seems that we can get them from there from the pickle concatenate them\n> and let sphinx output the todo list and the index.\n\nI've a proof of concept which seems to be working upto two problems:\n\n- The generated links to the \"original entry\" generated by `app.builder.get_relative_uri` is missing the subdirectory (ie: \"reference/sage/modules/...\" instead of \"reference/modules/sage/modules/...\". This could probably either be fixed by fixing the builder or playing with symlinks.\n\n- if one recompile the doc twice, all the todos are duplicated. This could probably also be fixed by removing duplicates or clearing the todo-list at the right moment.\n\nI think both problem can be fixed.",
    "created_at": "2012-05-01T23:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52636",
    "user": "hivert"
}
```

Replying to [comment:73 hivert]:
> So it seems that we can get them from there from the pickle concatenate them
> and let sphinx output the todo list and the index.

I've a proof of concept which seems to be working upto two problems:

- The generated links to the "original entry" generated by `app.builder.get_relative_uri` is missing the subdirectory (ie: "reference/sage/modules/..." instead of "reference/modules/sage/modules/...". This could probably either be fixed by fixing the builder or playing with symlinks.

- if one recompile the doc twice, all the todos are duplicated. This could probably also be fixed by removing duplicates or clearing the todo-list at the right moment.

I think both problem can be fixed.



---

archive/issue_comments_052637.json:
```json
{
    "body": "Hi there,\n\nI just uploaded a new [attachment:invbuilder.patch]; you need to apply it after the two mentionned patch in the header of this ticket. It seems to solve the problems of\n\n- merging todo lists\n- merging the html indexes\n\nIt remains to merge the javascript indexes.\n\nPlease tests.\n\nFlorent",
    "created_at": "2012-05-02T10:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52637",
    "user": "hivert"
}
```

Hi there,

I just uploaded a new [attachment:invbuilder.patch]; you need to apply it after the two mentionned patch in the header of this ticket. It seems to solve the problems of

- merging todo lists
- merging the html indexes

It remains to merge the javascript indexes.

Please tests.

Florent



---

archive/issue_comments_052638.json:
```json
{
    "body": "I just uploaded a new patch which merge the javascript indexes as well !!! It was a little more tricky but it seems to work now. The only things that remains to be merged is the list of modules. I'll write a proposal to Sphinx for my merging tool.\n\nFlorent",
    "created_at": "2012-05-03T16:18:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52638",
    "user": "hivert"
}
```

I just uploaded a new patch which merge the javascript indexes as well !!! It was a little more tricky but it seems to work now. The only things that remains to be merged is the list of modules. I'll write a proposal to Sphinx for my merging tool.

Florent



---

archive/issue_comments_052639.json:
```json
{
    "body": "The new version now also merge modules indexes !!! The obtained doc seems to be in quite a good shape.",
    "created_at": "2012-05-03T19:38:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52639",
    "user": "hivert"
}
```

The new version now also merge modules indexes !!! The obtained doc seems to be in quite a good shape.



---

archive/issue_comments_052640.json:
```json
{
    "body": "inventory builder + merge todo list & html / js indexes",
    "created_at": "2012-05-03T23:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52640",
    "user": "hivert"
}
```

inventory builder + merge todo list & html / js indexes



---

archive/issue_comments_052641.json:
```json
{
    "body": "Attachment\n\n> Citations may be an issue, in particular if the same reference is cited\n> twice in two different parts of the reference manual: we may just need to\n> add another copy of the citation, or perhaps a master list of citations that\n> gets used by everything. I don't know if that's practical.\n\nI've probably a way to handle cross-citation as well. They are stored in the\nenvironement and I can get them to gather the link in the main reference\nmanual, exactly the way I gather TODO and indexes. It is just a little more\ntricky because I need to redispatch them to the other documents. I'm\nexperimenting...\n\nFlorent",
    "created_at": "2012-05-07T01:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52641",
    "user": "hivert"
}
```

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

archive/issue_comments_052642.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-05-07T18:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52642",
    "user": "hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_052643.json:
```json
{
    "body": "Attachment\n\nHi there,\n\nI just uploaded which seems to solve most of the problems we had here,\nincluding merging of\n- the todo list if this extension is activated;\n- the python indexes;\n- the list of python modules;\n- the javascript index;\n- the citations.\n\nI put a need review though I'm quite not sure everything is ready for\ninclusion into Sage. I do need feedback and people shaking my code to see if\nit's robust.\n\nFlorent",
    "created_at": "2012-05-07T18:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52643",
    "user": "hivert"
}
```

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

archive/issue_comments_052644.json:
```json
{
    "body": "Changing keywords from \"\" to \"days38\".",
    "created_at": "2012-05-07T21:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52644",
    "user": "hivert"
}
```

Changing keywords from "" to "days38".



---

archive/issue_comments_052645.json:
```json
{
    "body": "Hi Florent,\n\nI am quite busy with other things right now, so I hope you can get people at Sage Days 38 to take a good look at this. Maybe you can figure out the ctrl-c issue as well; maybe tinkering with what I had might work; if not, the link I provided had some other ideas, too.\n\nThanks, John",
    "created_at": "2012-05-07T22:25:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52645",
    "user": "jhpalmieri"
}
```

Hi Florent,

I am quite busy with other things right now, so I hope you can get people at Sage Days 38 to take a good look at this. Maybe you can figure out the ctrl-c issue as well; maybe tinkering with what I had might work; if not, the link I provided had some other ideas, too.

Thanks, John



---

archive/issue_comments_052646.json:
```json
{
    "body": "Hi John,\n\nReplying to [comment:81 jhpalmieri]:\n> I am quite busy with other things right now, so I hope you can get people at Sage Days 38 to take a good look at this. Maybe you can figure out the ctrl-c issue as well; maybe tinkering with what I had might work; if not, the link I provided had some other ideas, too.\n\nwell, they are very few people knowing the documentation building system here and I used quite a few Sphinx internal stuff. I think a good reviewer would be George Brandle himself but I need to sit for a moment to write him an e-mail.\n\nCheers,\n\nFlorent",
    "created_at": "2012-05-08T05:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52646",
    "user": "hivert"
}
```

Hi John,

Replying to [comment:81 jhpalmieri]:
> I am quite busy with other things right now, so I hope you can get people at Sage Days 38 to take a good look at this. Maybe you can figure out the ctrl-c issue as well; maybe tinkering with what I had might work; if not, the link I provided had some other ideas, too.

well, they are very few people knowing the documentation building system here and I used quite a few Sphinx internal stuff. I think a good reviewer would be George Brandle himself but I need to sit for a moment to write him an e-mail.

Cheers,

Florent



---

archive/issue_comments_052647.json:
```json
{
    "body": "I haven't had time yet to read the whole ticket description and discussion, but I will note that this patch has allowed me to build the documentation on my old laptop (with only 1GB of RAM) in a couple of hours, whereas trying to build it without the patch causes my laptop to become unresponsive and eventually crash. (Also, Florent had a look at the output and seemed satisfied that everything was fine.) So, a huge +1 from me!\n\nI will try to do as much as I can to review this ticket, but I know almost nothing about the documentation building process.",
    "created_at": "2012-05-15T17:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52647",
    "user": "mguaypaq"
}
```

I haven't had time yet to read the whole ticket description and discussion, but I will note that this patch has allowed me to build the documentation on my old laptop (with only 1GB of RAM) in a couple of hours, whereas trying to build it without the patch causes my laptop to become unresponsive and eventually crash. (Also, Florent had a look at the output and seemed satisfied that everything was fine.) So, a huge +1 from me!

I will try to do as much as I can to review this ticket, but I know almost nothing about the documentation building process.



---

archive/issue_comments_052648.json:
```json
{
    "body": "After a lot of swearing at my computer, I think I have the ctrl-c situation figured out. We've been using `Pool.apply_async`, and this didn't handle ctrl-c well. Adding a timeout (using the `get` method) caused it to handle interrupts, but it no longer build in parallel.  If we instead use `Pool.map_async` together with `get` to provide a timeout, it seems to work. Please take a look at the new patch.",
    "created_at": "2012-05-16T05:23:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52648",
    "user": "jhpalmieri"
}
```

After a lot of swearing at my computer, I think I have the ctrl-c situation figured out. We've been using `Pool.apply_async`, and this didn't handle ctrl-c well. Adding a timeout (using the `get` method) caused it to handle interrupts, but it no longer build in parallel.  If we instead use `Pool.map_async` together with `get` to provide a timeout, it seems to work. Please take a look at the new patch.



---

archive/issue_comments_052649.json:
```json
{
    "body": "Several quick comments and questions:\n\n- First, the combined indices and search are great! At first I thought that searching was broken, but that's my browser, not the code. I'm still looking over the patch, but in practice it seems to work.\n- This is an old problem: I object to the use of \"type\" as a global variable, set by `__main__`. Then I can't use `print type(var)` anywhere in the rest of the code (as I tried to do when debugging something). I may change `type` to something else; any suggestions? Perhaps `format` (which also has a meaning in Python)?\n- When we're happy about the patches, I'll try to combine them into just one or two chunks. Right now, for example, one of my patches creates the \"todolist\" directory, and then Florent's patch moves all of the files out of it, so we end up with an empty directory. I don't know if there are other similar things which will need cleaning up.\n- I get some warnings about missing citations. Should we worry about those now?",
    "created_at": "2012-05-16T21:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52649",
    "user": "jhpalmieri"
}
```

Several quick comments and questions:

- First, the combined indices and search are great! At first I thought that searching was broken, but that's my browser, not the code. I'm still looking over the patch, but in practice it seems to work.
- This is an old problem: I object to the use of "type" as a global variable, set by `__main__`. Then I can't use `print type(var)` anywhere in the rest of the code (as I tried to do when debugging something). I may change `type` to something else; any suggestions? Perhaps `format` (which also has a meaning in Python)?
- When we're happy about the patches, I'll try to combine them into just one or two chunks. Right now, for example, one of my patches creates the "todolist" directory, and then Florent's patch moves all of the files out of it, so we end up with an empty directory. I don't know if there are other similar things which will need cleaning up.
- I get some warnings about missing citations. Should we worry about those now?



---

archive/issue_comments_052650.json:
```json
{
    "body": "I've modified the part 4 patch to do a little cleanup:\n\n- I moved the detection of the number of threads to `build_options.py`, and expanded on the comment about loading `build_options.py`. This way if someone is reading `builder.py` and wants to know where `NUM_THREADS` is defined, at least they'll find a comment pointing them to that file.\n- I modified the `mkdir` function, making it a bit more secure: the new approach seems to be preferred, as far as I can tell.",
    "created_at": "2012-05-16T21:56:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52650",
    "user": "jhpalmieri"
}
```

I've modified the part 4 patch to do a little cleanup:

- I moved the detection of the number of threads to `build_options.py`, and expanded on the comment about loading `build_options.py`. This way if someone is reading `builder.py` and wants to know where `NUM_THREADS` is defined, at least they'll find a comment pointing them to that file.
- I modified the `mkdir` function, making it a bit more secure: the new approach seems to be preferred, as far as I can tell.



---

archive/issue_comments_052651.json:
```json
{
    "body": "Another update to part 4: fix the main index.html file for the pdf build of the reference manual.",
    "created_at": "2012-05-18T01:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52651",
    "user": "jhpalmieri"
}
```

Another update to part 4: fix the main index.html file for the pdf build of the reference manual.



---

archive/issue_comments_052652.json:
```json
{
    "body": "One more update to part 4, to fix a few doctests.",
    "created_at": "2012-05-19T05:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52652",
    "user": "jhpalmieri"
}
```

One more update to part 4, to fix a few doctests.



---

archive/issue_comments_052653.json:
```json
{
    "body": "I think this looks very good. I'm just about ready to give Florent's part a positive review. Two questions: can we reinstate the `-Q` flag for the first pass on the reference manual, to silence all of the warnings? Also, I see this warning message; do you know if it's important?\n\n```\npreparing documents... WARNING: search index couldn't be loaded, but not all documents will be built: the index will be incomplete.\n```\n\n(This occurs if I do `sage --docbuild all html`, at the end of the second pass through the reference manual.)\n\nI'm attaching one more version of the part 4 patch, just to fix a few typos and grammar issues in the files Florent added.",
    "created_at": "2012-05-21T20:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52653",
    "user": "jhpalmieri"
}
```

I think this looks very good. I'm just about ready to give Florent's part a positive review. Two questions: can we reinstate the `-Q` flag for the first pass on the reference manual, to silence all of the warnings? Also, I see this warning message; do you know if it's important?

```
preparing documents... WARNING: search index couldn't be loaded, but not all documents will be built: the index will be incomplete.
```

(This occurs if I do `sage --docbuild all html`, at the end of the second pass through the reference manual.)

I'm attaching one more version of the part 4 patch, just to fix a few typos and grammar issues in the files Florent added.



---

archive/issue_comments_052654.json:
```json
{
    "body": "Hi John,\n\n> I think this looks very good. I'm just about ready to give Florent's part a\n> positive review.\n\nWow !!! This is extremely cool. Thanks a lot ! I'm sorry for my current\nsilence. I didn't had the time to look at your part4 code. I'll try to do it\nshortly.\n\n> Two questions: can we reinstate the `-Q` flag for the first pass on the\n> reference manual, to silence all of the warnings?\n\nNo problem. I just wanted to have some idea of the progress and forgot to\nswitch back to a silent mode.\n\n> Also, I see this warning message; do you know if it's important?\n\n```\npreparing documents... WARNING: search index couldn't be loaded, but not all documents will be built: the index will be incomplete.\n```\n\n> (This occurs if I do `sage --docbuild all html`, at the end of the second\npass through the reference manual.)\n\nI'm not sure now. I'll though I had silenced this warning. Give me a few day\nto investigate a little more. It is probably not important as the produced\nindex is correct but I may be missing to merge somme part of it.\n\n> I'm attaching one more version of the part 4 patch, just to fix a few typos\n> and grammar issues in the files Florent added.\n\nThanks for those rereading. I planned to polish more the code and try to get\nsome feedback from Sphinx and didn't find the time. However I now think that\nwe should let the code enter sage as soon as possible because it allows the\ndoc to compile on small machine. At sage days 48, with mguaypaq (see above) we\nmanage to compile the documentation in a seemingly satisfactory way on a 1GB\nmachine. Moreover its a requirement to the feature #12878 which I think is\ndefinitely needed at least for huge classes such as graphs...\n\nThanks a lot,\n\nFlorent",
    "created_at": "2012-05-21T22:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52654",
    "user": "hivert"
}
```

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

archive/issue_comments_052655.json:
```json
{
    "body": "See #12991 for a peripherally-related ticket: don't doctest the autogenerated rst files.",
    "created_at": "2012-05-22T20:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52655",
    "user": "jhpalmieri"
}
```

See #12991 for a peripherally-related ticket: don't doctest the autogenerated rst files.



---

archive/issue_comments_052656.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-06-19T13:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52656",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_052657.json:
```json
{
    "body": "This needs to be rebased to sage-5.1.beta5:\n\n```\napplying /release/merger/patches/trac_6495-part2-everything-else.patch\npatching file doc/en/reference/combinat/index.rst\nHunk #1 FAILED at 3\n1 out of 2 hunks FAILED -- saving rejects to file doc/en/reference/combinat/index.rst.rej\npatching file doc/en/reference/misc/index.rst\nHunk #1 succeeded at 31 with fuzz 1 (offset 3 lines).\nabort: patch failed to apply\n```\n",
    "created_at": "2012-06-19T13:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52657",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_052658.json:
```json
{
    "body": "Okay, this is now rebased.",
    "created_at": "2012-06-19T22:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52658",
    "user": "jhpalmieri"
}
```

Okay, this is now rebased.



---

archive/issue_comments_052659.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-06-19T22:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52659",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_052660.json:
```json
{
    "body": "I've added a link to the built documents for Sage 5.1.beta5, in case anyone wants to look at it without applying the patches here. The reference manual is organized differently and as a result looks different. The other documents should be unchanged.",
    "created_at": "2012-06-20T03:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52660",
    "user": "jhpalmieri"
}
```

I've added a link to the built documents for Sage 5.1.beta5, in case anyone wants to look at it without applying the patches here. The reference manual is organized differently and as a result looks different. The other documents should be unchanged.



---

archive/issue_comments_052661.json:
```json
{
    "body": "This now depends on #9774. If you want to try it without the patches at #9774 (thus using jsMath instead of MathJax), apply [attachment:trac_6495-part2-everything-else.patch] instead of [attachment:trac_6495-part2-everything-else-9774.patch].",
    "created_at": "2012-06-20T21:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52661",
    "user": "jhpalmieri"
}
```

This now depends on #9774. If you want to try it without the patches at #9774 (thus using jsMath instead of MathJax), apply [attachment:trac_6495-part2-everything-else.patch] instead of [attachment:trac_6495-part2-everything-else-9774.patch].



---

archive/issue_comments_052662.json:
```json
{
    "body": "A slight issue with the reference manual is that it takes up a little more room, and most of the difference is in `devel/sage/doc/output/doctrees`. There is some redundancy in the `environment.pickle` files. I wonder if there is any way to avoid this. \n\nIn more detail: using MathJax instead of jsMath saves room in the directory `doc/output/html`: with the old version, jsMath and non-parallel, that directory takes about 325M, while the new version, MathJax and parallel, takes about 200M, saving 125M. Unfortunately, the doctree directory has increased by about 150M, so the whole thing has gone up by 25M. Not a big difference, but if there were a way to improve it, it would be nice. Maybe on another ticket...",
    "created_at": "2012-06-22T17:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52662",
    "user": "jhpalmieri"
}
```

A slight issue with the reference manual is that it takes up a little more room, and most of the difference is in `devel/sage/doc/output/doctrees`. There is some redundancy in the `environment.pickle` files. I wonder if there is any way to avoid this. 

In more detail: using MathJax instead of jsMath saves room in the directory `doc/output/html`: with the old version, jsMath and non-parallel, that directory takes about 325M, while the new version, MathJax and parallel, takes about 200M, saving 125M. Unfortunately, the doctree directory has increased by about 150M, so the whole thing has gone up by 25M. Not a big difference, but if there were a way to improve it, it would be nice. Maybe on another ticket...



---

archive/issue_comments_052663.json:
```json
{
    "body": "Clarified recursive dependencies.",
    "created_at": "2012-06-25T10:34:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52663",
    "user": "jdemeyer"
}
```

Clarified recursive dependencies.



---

archive/issue_comments_052664.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-06-27T07:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52664",
    "user": "jdemeyer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_052665.json:
```json
{
    "body": "I get tons of warnings (1043 to be precise) when building the manuals.  I don't like this, because it's hard to distinguish warnings due to this ticket with true warnings about bad formatting.  Is there a way not to produce any warnings during the first run (I assume the warnings should only appear in the first run)?",
    "created_at": "2012-06-27T07:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52665",
    "user": "jdemeyer"
}
```

I get tons of warnings (1043 to be precise) when building the manuals.  I don't like this, because it's hard to distinguish warnings due to this ticket with true warnings about bad formatting.  Is there a way not to produce any warnings during the first run (I assume the warnings should only appear in the first run)?



---

archive/issue_comments_052666.json:
```json
{
    "body": "Rebased because of #12299. I'll try to work on the warnings. I think it might be best to only suppress the warnings when you run `sage --docbuild all html`, because that is when both passes of the reference manual are actually run, and the first pass is designed to be fast: it just produces the inventory files, not html output. If you run `sage --docbuild reference html`, then it will just do one pass, html format.\n\nEdit: actually, the warnings are easy to get rid of. Florent intentionally left them there while working on the ticket: see these lines in builder.py:\n\n```python\n        global ALLSPHINXOPTS\n        # ALLSPHINXOPTS += ' -Q -D multidoc_first_pass=1'\n        ALLSPHINXOPTS += ' -D multidoc_first_pass=1'\n```\n\nIf we uncomment the second line and remove the third, the warnings will go away. I'll incorporate this change into the 4th patch.",
    "created_at": "2012-06-27T20:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52666",
    "user": "jhpalmieri"
}
```

Rebased because of #12299. I'll try to work on the warnings. I think it might be best to only suppress the warnings when you run `sage --docbuild all html`, because that is when both passes of the reference manual are actually run, and the first pass is designed to be fast: it just produces the inventory files, not html output. If you run `sage --docbuild reference html`, then it will just do one pass, html format.

Edit: actually, the warnings are easy to get rid of. Florent intentionally left them there while working on the ticket: see these lines in builder.py:

```python
        global ALLSPHINXOPTS
        # ALLSPHINXOPTS += ' -Q -D multidoc_first_pass=1'
        ALLSPHINXOPTS += ' -D multidoc_first_pass=1'
```

If we uncomment the second line and remove the third, the warnings will go away. I'll incorporate this change into the 4th patch.



---

archive/issue_comments_052667.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-06-27T20:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52667",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_052668.json:
```json
{
    "body": "I see one warning now:\n\n```\nWARNING: search index couldn't be loaded, but not all documents will be built: the index will be incomplete.\n```\n\nI don't know what this means. The search index looks pretty good to me. Florent might have some idea, when he has a chance to look at this.",
    "created_at": "2012-06-27T21:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52668",
    "user": "jhpalmieri"
}
```

I see one warning now:

```
WARNING: search index couldn't be loaded, but not all documents will be built: the index will be incomplete.
```

I don't know what this means. The search index looks pretty good to me. Florent might have some idea, when he has a chance to look at this.



---

archive/issue_comments_052669.json:
```json
{
    "body": "In addition to the warning mentioned [comment:105 in comment #105], I have a question about `.buildinfo` files. It seems that on the first pass through the reference manual, these files contain lines like\n\n```\nconfig: 6a23e6beb735e39dc46994bfb813cf55\ntags: fbb0d17656682115ca4d033fb2f83ba1\n```\n\nOn the second pass, these files get overwritten, and the new files have\n\n```\nconfig:\ntags:\n```\n\nThen running `sage --docbuild reference all` produces warnings like\n\n```\nWARNING: unsupported build info format in '.../devel/sage/doc/output/html/en/reference/libs/.buildinfo', building all\n```\n\nand then everything is rebuilt again. I propose this change, which seems to fix this issue:\n\n```diff\ndiff --git a/doc/common/builder.py b/doc/common/builder.py\n--- a/doc/common/builder.py\n+++ b/doc/common/builder.py\n@@ -300,7 +300,7 @@ class AllBuilder(object):\n         logger.warning(\"Building reference manual, second pass.\\n\")\n         ALLSPHINXOPTS = ALLSPHINXOPTS.replace(\n             'multidoc_first_pass=1', 'multidoc_first_pass=0')\n-        ALLSPHINXOPTS = ALLSPHINXOPTS.replace('-Q', '-q') + ' -a '\n+        ALLSPHINXOPTS = ALLSPHINXOPTS.replace('-Q', '-q') + ' '\n         for document in refs:\n             getattr(get_builder(document), name)(*args, **kwds)\n \n```\n",
    "created_at": "2012-07-10T04:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52669",
    "user": "jhpalmieri"
}
```

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
@@ -300,7 +300,7 @@ class AllBuilder(object):
         logger.warning("Building reference manual, second pass.\n")
         ALLSPHINXOPTS = ALLSPHINXOPTS.replace(
             'multidoc_first_pass=1', 'multidoc_first_pass=0')
-        ALLSPHINXOPTS = ALLSPHINXOPTS.replace('-Q', '-q') + ' -a '
+        ALLSPHINXOPTS = ALLSPHINXOPTS.replace('-Q', '-q') + ' '
         for document in refs:
             getattr(get_builder(document), name)(*args, **kwds)
 
```




---

archive/issue_comments_052670.json:
```json
{
    "body": "apply second (if you've applied the patches at #9774)",
    "created_at": "2012-07-10T13:50:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52670",
    "user": "jhpalmieri"
}
```

apply second (if you've applied the patches at #9774)



---

archive/issue_comments_052671.json:
```json
{
    "body": "Attachment",
    "created_at": "2012-07-10T13:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52671",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_052672.json:
```json
{
    "body": "Rebased to Sage 5.4.beta0.",
    "created_at": "2012-09-11T05:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52672",
    "user": "jhpalmieri"
}
```

Rebased to Sage 5.4.beta0.



---

archive/issue_comments_052673.json:
```json
{
    "body": "Florent: any chance you can work on this? I think that the only thing needed reviewing is the part 4 patch. (There is also the warning at [comment:105 comment 105], but I think that the actual output is good, so suppressing the warning would be nice but not absolutely necessary. You might also look at [comment:110 comment 110], but I can't reproduce that issue right now.)",
    "created_at": "2012-09-11T22:18:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52673",
    "user": "jhpalmieri"
}
```

Florent: any chance you can work on this? I think that the only thing needed reviewing is the part 4 patch. (There is also the warning at [comment:105 comment 105], but I think that the actual output is good, so suppressing the warning would be nice but not absolutely necessary. You might also look at [comment:110 comment 110], but I can't reproduce that issue right now.)



---

archive/issue_comments_052674.json:
```json
{
    "body": "Hi John,\n\nReplying to [comment:118 jhpalmieri]:\n> Florent: any chance you can work on this? I think that the only thing needed reviewing is the part 4 patch. (There is also the warning at [comment:105 comment 105], but I think that the actual output is good, so suppressing the warning would be nice but not absolutely necessary. You might also look at [comment:110 comment 110], but I can't reproduce that issue right now.)\n\nYes ! And thanks for your work and your patience. This is very high on my\npriority list, but it has to remain after the list \"things that must be done\nright now\" (such as teaching or meeting the dead-line to get money for\nSage-Combinat) or even \"thing that should have been done\nyesterday\". Unfortunately, until the end of September, I will still be moving\na flat, so I definitely won't be able to work during the Week-End. I\ndefinitely want to do this done ASAP. So I didn't give-up, but the summer\ndidn't went as expected and I had to stop working on sage for a few\nmonth. Please ping me in the first week of October if I didn't manage to do it\n.\n\nCheers,\n\nFlorent",
    "created_at": "2012-09-12T05:58:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52674",
    "user": "hivert"
}
```

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

archive/issue_comments_052675.json:
```json
{
    "body": "Rebased to Sage 5.4.beta1.",
    "created_at": "2012-09-13T21:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52675",
    "user": "jhpalmieri"
}
```

Rebased to Sage 5.4.beta1.



---

archive/issue_comments_052676.json:
```json
{
    "body": "Made #13143 a dependency and rebased to that.",
    "created_at": "2012-10-01T15:52:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52676",
    "user": "jhpalmieri"
}
```

Made #13143 a dependency and rebased to that.



---

archive/issue_comments_052677.json:
```json
{
    "body": "Hi John,\n\nReplying to [comment:121 jhpalmieri]:\n> Made #13143 a dependency and rebased to that.\n\nConsider me as pinged. And don't hesitate to email me more aggressively if nothing come up before the end of the week. \n\nFlorent",
    "created_at": "2012-10-01T19:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52677",
    "user": "hivert"
}
```

Hi John,

Replying to [comment:121 jhpalmieri]:
> Made #13143 a dependency and rebased to that.

Consider me as pinged. And don't hesitate to email me more aggressively if nothing come up before the end of the week. 

Florent



---

archive/issue_comments_052678.json:
```json
{
    "body": "Attachment\n\nRebased to #13143 and Sage 5.4.rc2 (because of changes to builder.py in #13579).",
    "created_at": "2012-10-19T17:21:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52678",
    "user": "jhpalmieri"
}
```

Attachment

Rebased to #13143 and Sage 5.4.rc2 (because of changes to builder.py in #13579).



---

archive/issue_comments_052679.json:
```json
{
    "body": "John, I've tried to use this on an existing Sage installation (well, previous versions of this) a few different times, and it always ends up causing problems, even when I delete the whole output directory.   Is there something to do other than apply the all-in-one patch, delete output, do `sage -b`, and start building docs?  For instance, is there an env var (e.g. `SAGE_NUM_THREADS`) to set or something?  I feel like I must have done something obvious wrong...\n\nOn a related note, this no longer applies :-(",
    "created_at": "2012-12-13T02:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52679",
    "user": "kcrisman"
}
```

John, I've tried to use this on an existing Sage installation (well, previous versions of this) a few different times, and it always ends up causing problems, even when I delete the whole output directory.   Is there something to do other than apply the all-in-one patch, delete output, do `sage -b`, and start building docs?  For instance, is there an env var (e.g. `SAGE_NUM_THREADS`) to set or something?  I feel like I must have done something obvious wrong...

On a related note, this no longer applies :-(



---

archive/issue_comments_052680.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-12-13T02:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52680",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_052681.json:
```json
{
    "body": "What sort of problems do you see? As far as environment variables, setting `MAKE` is the right thing to do: `export MAKE='make -j2'` for example.\n\nI just rebased the patches on top of 5.5.rc0.",
    "created_at": "2012-12-13T16:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52681",
    "user": "jhpalmieri"
}
```

What sort of problems do you see? As far as environment variables, setting `MAKE` is the right thing to do: `export MAKE='make -j2'` for example.

I just rebased the patches on top of 5.5.rc0.



---

archive/issue_comments_052682.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-12-13T16:34:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52682",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_052683.json:
```json
{
    "body": "> What sort of problems do you see? As far as environment variables, setting `MAKE` is the right thing to do: `export MAKE='make -j2'` for example.\n\nLots of \n\n```\nWARNING: intersphinx inventory '/Users/.../sage-5.5.rc0/devel/sage/doc/output/html/en/reference/monoids/objects.inv' not fetchable due to <type 'exceptions.IOError'>: [Errno 2] No such file or directory: '/Users/.../sage-5.5.rc0/devel/sage/doc/output/html/en/reference/monoids/objects.inv'\n```\n\nstuff.\n\n```\nbuild succeeded, 1074 warnings.\n```\n\nThat's while building `reference html`, and now I see upon careful reading of the ticket description that perhaps that's implicitly expected.  When I build the whole documentation as a target, I don't get this problem, though I do get one warning:\n\n```\nWARNING: search index couldn't be loaded, but not all documents will be built: the index will be incomplete.\n```\n",
    "created_at": "2012-12-13T17:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52683",
    "user": "kcrisman"
}
```

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

archive/issue_comments_052684.json:
```json
{
    "body": "Yes, the warnings are somewhat expected. Those are like what happens when you run LaTeX on a file for the first time: all of the unknown reference warnings which get resolved the second time through. I think typically people will do the following:\n\n- either build Sage from scratch or download a binary. In the first case, `sage --docbuild all html` will get run and so the intersphinx warnings have been turned off explicitly in this case. I also get the one about \"search index couldn't be loaded...\". I don't know the cause of that; Florent might be able to help.\n\n- then modify parts of the Sage library and do `sage --docbuild reference html` or `sage --docbuild reference/combinat html` or .... At this point, the various parts of the reference manual have been built along with their intersphinx inventories, so there shouldn't be any intersphinx warnings.\n\nThat is, I hope that most users/developers won't see all of these warnings. I've updated the ticket description so it mentions the warnings. (We could turn off all of the warnings all of the time, but I don't think that's a good idea.)",
    "created_at": "2012-12-13T18:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52684",
    "user": "jhpalmieri"
}
```

Yes, the warnings are somewhat expected. Those are like what happens when you run LaTeX on a file for the first time: all of the unknown reference warnings which get resolved the second time through. I think typically people will do the following:

- either build Sage from scratch or download a binary. In the first case, `sage --docbuild all html` will get run and so the intersphinx warnings have been turned off explicitly in this case. I also get the one about "search index couldn't be loaded...". I don't know the cause of that; Florent might be able to help.

- then modify parts of the Sage library and do `sage --docbuild reference html` or `sage --docbuild reference/combinat html` or .... At this point, the various parts of the reference manual have been built along with their intersphinx inventories, so there shouldn't be any intersphinx warnings.

That is, I hope that most users/developers won't see all of these warnings. I've updated the ticket description so it mentions the warnings. (We could turn off all of the warnings all of the time, but I don't think that's a good idea.)



---

archive/issue_comments_052685.json:
```json
{
    "body": "I consider it a requirement that there are no visible warnings/errors when building the documentation from scratch. Otherwise, it becomes difficult to differentiate warnings caused by this ticket from true warnings.",
    "created_at": "2012-12-19T20:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52685",
    "user": "jdemeyer"
}
```

I consider it a requirement that there are no visible warnings/errors when building the documentation from scratch. Otherwise, it becomes difficult to differentiate warnings caused by this ticket from true warnings.



---

archive/issue_comments_052686.json:
```json
{
    "body": "Does this patch enable links like `:func:`plot()`` from other manuals (e.g. the developer manual) to the reference manual?",
    "created_at": "2013-01-03T15:29:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52686",
    "user": "jdemeyer"
}
```

Does this patch enable links like `:func:`plot()`` from other manuals (e.g. the developer manual) to the reference manual?



---

archive/issue_comments_052687.json:
```json
{
    "body": "> I consider it a requirement that there are no visible warnings/errors when building the documentation from scratch. Otherwise, it becomes difficult to differentiate warnings caused by this ticket from true warnings.\nJohn, is this even possible under this setup? It would really be a shame to hold this up but Jeroen makes a good point as well.",
    "created_at": "2013-01-03T19:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52687",
    "user": "kcrisman"
}
```

> I consider it a requirement that there are no visible warnings/errors when building the documentation from scratch. Otherwise, it becomes difficult to differentiate warnings caused by this ticket from true warnings.
John, is this even possible under this setup? It would really be a shame to hold this up but Jeroen makes a good point as well.



---

archive/issue_comments_052688.json:
```json
{
    "body": "Replying to [comment:132 jdemeyer]:\n> Does this patch enable links like `:func:`plot()`` from other manuals (e.g. the developer manual) to the reference manual?\n\nI think so, but it ought to be tested. You might need to specify the cross-reference more explicitly, the way you might if you want to reference the Python docs, for instance.\n\nReplying to [comment:133 kcrisman]:\n> > I consider it a requirement that there are no visible warnings/errors when building the documentation from scratch. Otherwise, it becomes difficult to differentiate warnings caused by this ticket from true warnings.\n> John, is this even possible under this setup? It would really be a shame to hold this up but Jeroen makes a good point as well.\n\nI thought that Florent had ideas about how to get rid of the one remaining warning. (As I said before, the intersphinx warnings are turned off on the first pass through the reference manual when you do `sage --docbuild all html`, and I think this is appropriate.)\n\nI'll try to look into both of these. Anyone else is welcome, also. Florent, do you have any time these days?",
    "created_at": "2013-01-03T20:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52688",
    "user": "jhpalmieri"
}
```

Replying to [comment:132 jdemeyer]:
> Does this patch enable links like `:func:`plot()`` from other manuals (e.g. the developer manual) to the reference manual?

I think so, but it ought to be tested. You might need to specify the cross-reference more explicitly, the way you might if you want to reference the Python docs, for instance.

Replying to [comment:133 kcrisman]:
> > I consider it a requirement that there are no visible warnings/errors when building the documentation from scratch. Otherwise, it becomes difficult to differentiate warnings caused by this ticket from true warnings.
> John, is this even possible under this setup? It would really be a shame to hold this up but Jeroen makes a good point as well.

I thought that Florent had ideas about how to get rid of the one remaining warning. (As I said before, the intersphinx warnings are turned off on the first pass through the reference manual when you do `sage --docbuild all html`, and I think this is appropriate.)

I'll try to look into both of these. Anyone else is welcome, also. Florent, do you have any time these days?



---

archive/issue_comments_052689.json:
```json
{
    "body": "please rebase for 5.6.beta3:\n\n```\n$sage-5.6.beta3/devel/sage$ ../../sage -hg qpushapplying trac_6495-all-in-one.patch\npatching file doc/en/reference/combinat/index.rst\nHunk #1 FAILED at 3\n1 out of 3 hunks FAILED -- saving rejects to file doc/en/reference/combinat/index.rst.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_6495-all-in-one.patch\n```\n",
    "created_at": "2013-01-11T12:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52689",
    "user": "dimpase"
}
```

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

archive/issue_comments_052690.json:
```json
{
    "body": "Replying to [comment:134 jhpalmieri]:\n> I thought that Florent had ideas about how to get rid of the one remaining warning. (As I said before, the intersphinx warnings are turned off on the first pass through the reference manual when you do `sage --docbuild all html`, and I think this is appropriate.)\n> \n> I'll try to look into both of these. Anyone else is welcome, also. Florent, do you have any time these days?\n\nI'm deeply sorry for letting time pass and not finishing this one... I'll be in Sage-Days in Edimbourg in two weeks so I hopefully will finish this one.\n\nFlorent",
    "created_at": "2013-01-11T13:48:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52690",
    "user": "hivert"
}
```

Replying to [comment:134 jhpalmieri]:
> I thought that Florent had ideas about how to get rid of the one remaining warning. (As I said before, the intersphinx warnings are turned off on the first pass through the reference manual when you do `sage --docbuild all html`, and I think this is appropriate.)
> 
> I'll try to look into both of these. Anyone else is welcome, also. Florent, do you have any time these days?

I'm deeply sorry for letting time pass and not finishing this one... I'll be in Sage-Days in Edimbourg in two weeks so I hopefully will finish this one.

Florent



---

archive/issue_comments_052691.json:
```json
{
    "body": "I did the following:\n* Apply the patch against 5.5 - there was fuzz\n* Run sage -b - ok\n* Run sage -docbuild all html - ok\n* Run sage -docbuild all pdf - error at the ru/tutorial stage, because I don't have cyrillic encoding definitions available for babel\n\nDoes that help?",
    "created_at": "2013-01-11T22:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52691",
    "user": "Snark"
}
```

I did the following:
* Apply the patch against 5.5 - there was fuzz
* Run sage -b - ok
* Run sage -docbuild all html - ok
* Run sage -docbuild all pdf - error at the ru/tutorial stage, because I don't have cyrillic encoding definitions available for babel

Does that help?



---

archive/issue_comments_052692.json:
```json
{
    "body": "Snark: is that specific to this ticket, or does `sage --docbuild ru/tutorial pdf` fail before applying these patches?",
    "created_at": "2013-01-11T22:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52692",
    "user": "jhpalmieri"
}
```

Snark: is that specific to this ticket, or does `sage --docbuild ru/tutorial pdf` fail before applying these patches?



---

archive/issue_comments_052693.json:
```json
{
    "body": "Rebased for 5.6.beta3.",
    "created_at": "2013-01-11T22:54:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52693",
    "user": "jhpalmieri"
}
```

Rebased for 5.6.beta3.



---

archive/issue_comments_052694.json:
```json
{
    "body": "I installed the needed cyrillic support and it went through without problem.",
    "created_at": "2013-01-12T09:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52694",
    "user": "Snark"
}
```

I installed the needed cyrillic support and it went through without problem.



---

archive/issue_comments_052695.json:
```json
{
    "body": "Another approach to parallel building (not that we want to throw away all of this work): [a proposed patch to Sphinx](https://bitbucket.org/birkenfeld/sphinx/pull-request/108/wip-parallel-build-experimentation/diff). I don't know if using this proposal would affect Sphinx's memory usage, though, which is another issue that is helped by breaking up the reference manual.",
    "created_at": "2013-01-14T16:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52695",
    "user": "jhpalmieri"
}
```

Another approach to parallel building (not that we want to throw away all of this work): [a proposed patch to Sphinx](https://bitbucket.org/birkenfeld/sphinx/pull-request/108/wip-parallel-build-experimentation/diff). I don't know if using this proposal would affect Sphinx's memory usage, though, which is another issue that is helped by breaking up the reference manual.



---

archive/issue_comments_052696.json:
```json
{
    "body": "Replying to [comment:141 jhpalmieri]:\n> Another approach to parallel building (not that we want to throw away all of this work): [a proposed patch to Sphinx](https://bitbucket.org/birkenfeld/sphinx/pull-request/108/wip-parallel-build-experimentation/diff).\nIt only parallelizes the \"writing output\" phase, not the \"reading\" phase, so it cannot be that useful.\n\n> I don't know if using this proposal would affect Sphinx's memory usage, though\nMost likely not.",
    "created_at": "2013-01-14T16:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52696",
    "user": "jdemeyer"
}
```

Replying to [comment:141 jhpalmieri]:
> Another approach to parallel building (not that we want to throw away all of this work): [a proposed patch to Sphinx](https://bitbucket.org/birkenfeld/sphinx/pull-request/108/wip-parallel-build-experimentation/diff).
It only parallelizes the "writing output" phase, not the "reading" phase, so it cannot be that useful.

> I don't know if using this proposal would affect Sphinx's memory usage, though
Most likely not.



---

archive/issue_comments_052697.json:
```json
{
    "body": "Just for fun, I packaged it: [http://boxen.math.washington.edu/home/jdemeyer/spkg/sphinx-parallel.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/sphinx-parallel.spkg) and made it support the Sage standard MAKE=\"-j20\" mechanism.",
    "created_at": "2013-01-14T16:40:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52697",
    "user": "jdemeyer"
}
```

Just for fun, I packaged it: [http://boxen.math.washington.edu/home/jdemeyer/spkg/sphinx-parallel.spkg](http://boxen.math.washington.edu/home/jdemeyer/spkg/sphinx-parallel.spkg) and made it support the Sage standard MAKE="-j20" mechanism.



---

archive/issue_comments_052698.json:
```json
{
    "body": "Replying to [comment:142 jdemeyer]:\n> It only parallelizes the \"writing output\" phase, not the \"reading\" phase, so it cannot be that useful.\n\nThis is more or less what I did when experimenting on #6255. At that time, since I was building the whole documentation it increased the memory usage. By the way, we probably should close #6255 at some point as a duplicate of this one.\n\nFlorent",
    "created_at": "2013-01-14T17:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52698",
    "user": "hivert"
}
```

Replying to [comment:142 jdemeyer]:
> It only parallelizes the "writing output" phase, not the "reading" phase, so it cannot be that useful.

This is more or less what I did when experimenting on #6255. At that time, since I was building the whole documentation it increased the memory usage. By the way, we probably should close #6255 at some point as a duplicate of this one.

Florent



---

archive/issue_comments_052699.json:
```json
{
    "body": "With the parallel Sphinx package I get lots of errors, some might be due to the \"upgrade\" to the devleopment version of Sphinx 1.2, but some also to the parallel code.",
    "created_at": "2013-01-14T20:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52699",
    "user": "jdemeyer"
}
```

With the parallel Sphinx package I get lots of errors, some might be due to the "upgrade" to the devleopment version of Sphinx 1.2, but some also to the parallel code.



---

archive/issue_comments_052700.json:
```json
{
    "body": "I think our Sphinx package needs some work. In particular, the file `SAGE_ROOT/devel/sage/common/sage-autodoc.py` should be part of the Sphinx package, built by patching Sphinx's `autodoc.py`. This would make it easier to incorporate modifications to `autodoc.py`. I don't know if this has to do with the problems with using Sphinx 1.2, but it might.\n\nIt's probably also not a good idea to use Sphinx's parallel building at the same time as ours, or else we'll be using more threads than we intended: maybe building 8 pieces of documentation at the same time, and then writing each of those using 8 processes. That sounds like a bad idea to me.\n\nHaving said all of that, do the errors you get suggest problems with our parallel code?",
    "created_at": "2013-01-14T22:38:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52700",
    "user": "jhpalmieri"
}
```

I think our Sphinx package needs some work. In particular, the file `SAGE_ROOT/devel/sage/common/sage-autodoc.py` should be part of the Sphinx package, built by patching Sphinx's `autodoc.py`. This would make it easier to incorporate modifications to `autodoc.py`. I don't know if this has to do with the problems with using Sphinx 1.2, but it might.

It's probably also not a good idea to use Sphinx's parallel building at the same time as ours, or else we'll be using more threads than we intended: maybe building 8 pieces of documentation at the same time, and then writing each of those using 8 processes. That sounds like a bad idea to me.

Having said all of that, do the errors you get suggest problems with our parallel code?



---

archive/issue_comments_052701.json:
```json
{
    "body": "Replying to [comment:146 jhpalmieri]:\n> Having said all of that, do the errors you get suggest problems with our parallel code?\nI didn't use any code from this ticket, I only used the patch you linked to for parallel Sphinx writing.",
    "created_at": "2013-01-15T07:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52701",
    "user": "jdemeyer"
}
```

Replying to [comment:146 jhpalmieri]:
> Having said all of that, do the errors you get suggest problems with our parallel code?
I didn't use any code from this ticket, I only used the patch you linked to for parallel Sphinx writing.



---

archive/issue_comments_052702.json:
```json
{
    "body": "Attachment\n\napply third",
    "created_at": "2013-01-18T06:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52702",
    "user": "jhpalmieri"
}
```

Attachment

apply third



---

archive/issue_comments_052703.json:
```json
{
    "body": "Rebased to 5.6.rc0 (among other things, dealing with the addition of `doc/en/reference/sat.rst`).",
    "created_at": "2013-01-18T06:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52703",
    "user": "jhpalmieri"
}
```

Rebased to 5.6.rc0 (among other things, dealing with the addition of `doc/en/reference/sat.rst`).



---

archive/issue_comments_052704.json:
```json
{
    "body": "This is an answer to Mike Hansen:\n\nHe asked if the page url are kept or not. The answer is that they moved:\nFor example:\n\n```\ndoc/output/html/en/reference/sage/symbolic/expression.html\n```\n\nis now\n\n```\ndoc/output/html/en/reference/calculus/sage/symbolic/expression.html\n```\n\nSo the location is not kept.\n\nFlorent",
    "created_at": "2013-01-22T01:34:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52704",
    "user": "hivert"
}
```

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

archive/issue_comments_052705.json:
```json
{
    "body": "Replying to [comment:149 hivert]:\n> This is an answer to Mike Hansen:\n> \n> He asked if the page url are kept or not. The answer is that they moved:\nHmm, I was dimly aware of this but didn't think it through.  That will break a loooot of links (e.g., on ask.sagemath.org).  Is there any way to auto-generate forwarding or 'mirrors' from the old pages?",
    "created_at": "2013-01-22T01:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52705",
    "user": "kcrisman"
}
```

Replying to [comment:149 hivert]:
> This is an answer to Mike Hansen:
> 
> He asked if the page url are kept or not. The answer is that they moved:
Hmm, I was dimly aware of this but didn't think it through.  That will break a loooot of links (e.g., on ask.sagemath.org).  Is there any way to auto-generate forwarding or 'mirrors' from the old pages?



---

archive/issue_comments_052706.json:
```json
{
    "body": "Replying to [comment:150 kcrisman]:\n> Replying to [comment:149 hivert]:\n> > This is an answer to Mike Hansen:\n> > \n> > He asked if the page url are kept or not. The answer is that they moved:\n> Hmm, I was dimly aware of this but didn't think it through.  That will break a loooot of links (e.g., on ask.sagemath.org).  Is there any way to auto-generate forwarding or 'mirrors' from the old pages?\n\nthere are several options:\n\n1. use `.htaccess` thing to fix this on any particular website;\n \n2.  write a script to look through all `href` targets in each file with changed location, and create for it a file with forwards;\n\n3.  maybe sphinx can help in this business, I don't know.\n\nIn any event we do not want to keep the old links around forever, I think, so there should be some kind of deprecation being turned on.",
    "created_at": "2013-01-24T04:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52706",
    "user": "dimpase"
}
```

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

archive/issue_comments_052707.json:
```json
{
    "body": "> > > He asked if the page url are kept or not. The answer is that they moved:\n> > Hmm, I was dimly aware of this but didn't think it through.  That will break a loooot of links (e.g., on ask.sagemath.org).  Is there any way to auto-generate forwarding or 'mirrors' from the old pages?\n> \n> there are several options:\n> \n>  1. use `.htaccess` thing to fix this on any particular website;\n>  \n>  2.  write a script to look through all `href` targets in each file with changed location, and create for it a file with forwards;\n> \n>  3.  maybe sphinx can help in this business, I don't know.\n\nI don't thinks it does. On the contrary, it makes it a nightmare (at least to me). Sphinx made the assumption that creating a new document needs creating a new directory (storing html, markup, indexes...). Since we splitting the reference manual in different documents we had to move files around.\n\nMike Hansen was considering implementing something which is close to option 2, because it it seems that option 1 is not easily doable (whereas I'm starting to now more than a little about Sphinx, I shamefully admitting that I don't know how to write/configure a website). \n\nFlorent",
    "created_at": "2013-01-24T10:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52707",
    "user": "hivert"
}
```

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

archive/issue_comments_052708.json:
```json
{
    "body": "We should just have versioned documentation on sagemath.org, just like Singular:\n* http://www.singular.uni-kl.de/Manual/3-1-0/index.htm\n* http://www.singular.uni-kl.de/Manual/latest/index.htm\nThe \"latest\" manual would then never be stable; independent of this ticket in particular there is always the danger of a module being renamed or moved around.\n\nHaving said that, Apache `mod_rewrite` could be used to dull some of the pain and automatically guess the new location.",
    "created_at": "2013-01-24T12:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52708",
    "user": "vbraun"
}
```

We should just have versioned documentation on sagemath.org, just like Singular:
* http://www.singular.uni-kl.de/Manual/3-1-0/index.htm
* http://www.singular.uni-kl.de/Manual/latest/index.htm
The "latest" manual would then never be stable; independent of this ticket in particular there is always the danger of a module being renamed or moved around.

Having said that, Apache `mod_rewrite` could be used to dull some of the pain and automatically guess the new location.



---

archive/issue_comments_052709.json:
```json
{
    "body": "Replying to [comment:154 vbraun]:\n> Having said that, Apache `mod_rewrite` could be used to dull some of the pain and automatically guess the new location.\n\nCan you really use mod_rewrite to do this?  You have to turn a request like reference/sage/symbolic/expression.html to something like reference/calculus/sage/symbolic/expression.html .  So, you'd have to walk to filesystem in order to find out the analog of \"calculus\".",
    "created_at": "2013-01-24T12:41:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52709",
    "user": "mhansen"
}
```

Replying to [comment:154 vbraun]:
> Having said that, Apache `mod_rewrite` could be used to dull some of the pain and automatically guess the new location.

Can you really use mod_rewrite to do this?  You have to turn a request like reference/sage/symbolic/expression.html to something like reference/calculus/sage/symbolic/expression.html .  So, you'd have to walk to filesystem in order to find out the analog of "calculus".



---

archive/issue_comments_052710.json:
```json
{
    "body": "Yes and no... its not beautiful but you can just add a rule for each `sage/` subdirectory that does the equivalent of \n\n```\nsed s-sage/symbolic-calculus/sage/symbolic-\n```\n",
    "created_at": "2013-01-24T12:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52710",
    "user": "vbraun"
}
```

Yes and no... its not beautiful but you can just add a rule for each `sage/` subdirectory that does the equivalent of 

```
sed s-sage/symbolic-calculus/sage/symbolic-
```




---

archive/issue_comments_052711.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-01-24T16:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52711",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_052712.json:
```json
{
    "body": "Replying to [comment:157 vbraun]:\n> Yes and no... its not beautiful but you can just add a rule for each `sage/` subdirectory that does the equivalent of \n> {{{\n> sed s-sage/symbolic-calculus/sage/symbolic-\n> }}}\n\nI don't think that you can really do this since it isn't guaranteed that all of the files that are in say sage/misc/ will all go to the same document.\n\nI wrote a patch which adds small HTML files to do the redirect.  I've looked through Florent's code as well, and things seem fine to me -- trac_6495-all-in-one.patch and trac-6495_silence_warning-fh.patch .\n\nIf someone reviews trac_6495-redirect_html.patch , we can mark this as positive_review.",
    "created_at": "2013-01-24T16:52:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52712",
    "user": "mhansen"
}
```

Replying to [comment:157 vbraun]:
> Yes and no... its not beautiful but you can just add a rule for each `sage/` subdirectory that does the equivalent of 
> {{{
> sed s-sage/symbolic-calculus/sage/symbolic-
> }}}

I don't think that you can really do this since it isn't guaranteed that all of the files that are in say sage/misc/ will all go to the same document.

I wrote a patch which adds small HTML files to do the redirect.  I've looked through Florent's code as well, and things seem fine to me -- trac_6495-all-in-one.patch and trac-6495_silence_warning-fh.patch .

If someone reviews trac_6495-redirect_html.patch , we can mark this as positive_review.



---

archive/issue_comments_052713.json:
```json
{
    "body": "> I wrote a patch which adds small HTML files to do the redirect.  I've looked through Florent's code as well, and things seem fine to me -- trac_6495-all-in-one.patch and trac-6495_silence_warning-fh.patch .\n> \n> If someone reviews trac_6495-redirect_html.patch , we can mark this as positive_review.\n\nThank you so much for adding this, Mike - I hope to try it out tonight and see if it works fine, but I doubt I'll be competent to give positive review.\n\nHere is a question about all the patches.  There are a lot of functions (esp. underscore ones) in doc/... that have no doctests.  Problem?  (This includes Mike's new function, but is not limited to it.)  Hope this isn't evil to ask.",
    "created_at": "2013-01-24T19:22:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52713",
    "user": "kcrisman"
}
```

> I wrote a patch which adds small HTML files to do the redirect.  I've looked through Florent's code as well, and things seem fine to me -- trac_6495-all-in-one.patch and trac-6495_silence_warning-fh.patch .
> 
> If someone reviews trac_6495-redirect_html.patch , we can mark this as positive_review.

Thank you so much for adding this, Mike - I hope to try it out tonight and see if it works fine, but I doubt I'll be competent to give positive review.

Here is a question about all the patches.  There are a lot of functions (esp. underscore ones) in doc/... that have no doctests.  Problem?  (This includes Mike's new function, but is not limited to it.)  Hope this isn't evil to ask.



---

archive/issue_comments_052714.json:
```json
{
    "body": "I have yet to test [attachment:trac_6495-redirect_html.patch], but the docstring for `html` ends rather abruptly.",
    "created_at": "2013-01-24T20:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52714",
    "user": "jhpalmieri"
}
```

I have yet to test [attachment:trac_6495-redirect_html.patch], but the docstring for `html` ends rather abruptly.



---

archive/issue_comments_052715.json:
```json
{
    "body": "If I run `sage --docbuild all html`, at the end of the second pass for the reference manual, I see\n\n```\n*******************SKIPPING Load indexer call*******************\nWARNING: search index couldn't be loaded, but not all documents will be built: the index will be incomplete.\nBuild finished.  The built documents can be found in /scratch/palmieri/6495/sage-5.7.beta0/devel/sage/doc/output/html/en/reference\n```\n\nSo the warning isn't gone.",
    "created_at": "2013-01-24T20:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52715",
    "user": "jhpalmieri"
}
```

If I run `sage --docbuild all html`, at the end of the second pass for the reference manual, I see

```
*******************SKIPPING Load indexer call*******************
WARNING: search index couldn't be loaded, but not all documents will be built: the index will be incomplete.
Build finished.  The built documents can be found in /scratch/palmieri/6495/sage-5.7.beta0/devel/sage/doc/output/html/en/reference
```

So the warning isn't gone.



---

archive/issue_comments_052716.json:
```json
{
    "body": "Addendum: if I delete documentation output and run `sage --docbuild reference html` twice, I don't see the warning message. So perhaps something can be tweaked to make it go away on the second pass when running `sage --docbuild all html`.",
    "created_at": "2013-01-24T22:04:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52716",
    "user": "jhpalmieri"
}
```

Addendum: if I delete documentation output and run `sage --docbuild reference html` twice, I don't see the warning message. So perhaps something can be tweaked to make it go away on the second pass when running `sage --docbuild all html`.



---

archive/issue_comments_052717.json:
```json
{
    "body": "Rebased to 5.7.beta0.",
    "created_at": "2013-01-24T22:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52717",
    "user": "jhpalmieri"
}
```

Rebased to 5.7.beta0.



---

archive/issue_comments_052718.json:
```json
{
    "body": "[attachment:trac_6495-redirect_html.patch] doesn't quite work, because `os.path.split(path)` always returns a list of length 2. With this change, it works for me:\n\n```diff\ndiff --git a/doc/common/builder.py b/doc/common/builder.py\n--- a/doc/common/builder.py\n+++ b/doc/common/builder.py\n@@ -391,7 +391,7 @@ class WebsiteBuilder(DocBuilder):\n                     redirect_filename = os.path.join(reference_dir, shorter_path, filename)\n \n                     # the number of levels up we need to use in the relative url\n-                    levels_up = len(os.path.split(shorter_path))\n+                    levels_up = len(shorter_path.split(os.sep))\n \n                     # the relative url that we will redirect to\n                     redirect_url = \"/\".join(['..']*levels_up + [document_name, shorter_path, filename])\n```\n\nFix that, and fix the docstring for the html method, and I think this part is good. \n\nThe warning is still an issue, and I don't know why it still shows up during the second pass for the reference manual when doing `sage --docbuild all html` but not when running `sage --docbuild reference html` twice. Florent, any ideas? Does anyone else see this?\n\nkcrisman, I don't know about doctests for all of these methods.",
    "created_at": "2013-01-25T06:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52718",
    "user": "jhpalmieri"
}
```

[attachment:trac_6495-redirect_html.patch] doesn't quite work, because `os.path.split(path)` always returns a list of length 2. With this change, it works for me:

```diff
diff --git a/doc/common/builder.py b/doc/common/builder.py
--- a/doc/common/builder.py
+++ b/doc/common/builder.py
@@ -391,7 +391,7 @@ class WebsiteBuilder(DocBuilder):
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

archive/issue_comments_052719.json:
```json
{
    "body": "Strange, It's working for me. Can you post the log of the docbuild which shows the warning, please\n\nFlorent",
    "created_at": "2013-01-25T09:43:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52719",
    "user": "hivert"
}
```

Strange, It's working for me. Can you post the log of the docbuild which shows the warning, please

Florent



---

archive/issue_comments_052720.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-01-25T12:10:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52720",
    "user": "hivert"
}
```

Attachment



---

archive/issue_comments_052721.json:
```json
{
    "body": "Sorry, I ended up uploading the wrong version of my patch. I uploaded a new version.\n\nFlorent",
    "created_at": "2013-01-25T12:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52721",
    "user": "hivert"
}
```

Sorry, I ended up uploading the wrong version of my patch. I uploaded a new version.

Florent



---

archive/issue_comments_052722.json:
```json
{
    "body": "Hi there\n\nI'm at the point where everything seems to work for me. I'd like to test this\nautomatically it I can't see how. So provided someone testify that the new\nversion of [attachment:trac-6495_silence_warning-fh.patch] works for him, I'm\nready to put a positive review here.\n\nCheers,\n\nFlorent",
    "created_at": "2013-01-25T12:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52722",
    "user": "hivert"
}
```

Hi there

I'm at the point where everything seems to work for me. I'd like to test this
automatically it I can't see how. So provided someone testify that the new
version of [attachment:trac-6495_silence_warning-fh.patch] works for him, I'm
ready to put a positive review here.

Cheers,

Florent



---

archive/issue_comments_052723.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-25T12:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52723",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_052724.json:
```json
{
    "body": "This conflicts with #12719 and should be rebased.",
    "created_at": "2013-01-25T13:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52724",
    "user": "jdemeyer"
}
```

This conflicts with #12719 and should be rebased.



---

archive/issue_comments_052725.json:
```json
{
    "body": "Replying to [comment:169 jdemeyer]:\n\nPositive review without the HTML redirection patch?  (Cf. John's comments above.)",
    "created_at": "2013-01-25T15:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52725",
    "user": "leif"
}
```

Replying to [comment:169 jdemeyer]:

Positive review without the HTML redirection patch?  (Cf. John's comments above.)



---

archive/issue_comments_052726.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-01-25T16:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52726",
    "user": "hivert"
}
```

Attachment



---

archive/issue_comments_052727.json:
```json
{
    "body": "When I Said \"I'm ready to put a positive review\" that was including John's\nmodification. I uploaded a new version of patch with it. Jeroen, do we need to\ngo in a re-review process (except of rebasing) ? Or should I leave a positive\nreview ?\n\nFlorent",
    "created_at": "2013-01-25T16:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52727",
    "user": "hivert"
}
```

When I Said "I'm ready to put a positive review" that was including John's
modification. I uploaded a new version of patch with it. Jeroen, do we need to
go in a re-review process (except of rebasing) ? Or should I leave a positive
review ?

Florent



---

archive/issue_comments_052728.json:
```json
{
    "body": "Well, the docstrings are still a bit of a mess. Here's a patch; maybe the last one?",
    "created_at": "2013-01-25T16:49:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52728",
    "user": "jhpalmieri"
}
```

Well, the docstrings are still a bit of a mess. Here's a patch; maybe the last one?



---

archive/issue_comments_052729.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-01-25T16:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52729",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_052730.json:
```json
{
    "body": "Replying to [comment:175 jhpalmieri]:\n> Well, the docstrings are still a bit of a mess. Here's a patch; maybe the last one? \n\nThanks for this cleanup. I'm positive reviewing these new changes.\n\nFlorent",
    "created_at": "2013-01-25T17:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52730",
    "user": "hivert"
}
```

Replying to [comment:175 jhpalmieri]:
> Well, the docstrings are still a bit of a mess. Here's a patch; maybe the last one? 

Thanks for this cleanup. I'm positive reviewing these new changes.

Florent



---

archive/issue_comments_052731.json:
```json
{
    "body": "Replying to [comment:170 jdemeyer]:\n> This conflicts with #12719 and should be rebased.\n\nI don't see any conflicts: starting with 5.7.beta0, I applied the patches from #12719 and then the patches here with no problem. Can you clarify?",
    "created_at": "2013-01-25T19:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52731",
    "user": "jhpalmieri"
}
```

Replying to [comment:170 jdemeyer]:
> This conflicts with #12719 and should be rebased.

I don't see any conflicts: starting with 5.7.beta0, I applied the patches from #12719 and then the patches here with no problem. Can you clarify?



---

archive/issue_comments_052732.json:
```json
{
    "body": "This is totally a pain w.r.t. rebasing.  For example, there are again conflicts with #11641 and #13077.  If this is mostly the automatic scripted part which needs to be rebased, could you please split off the scripted part again such that I could simply run the script instead of applying the patch?",
    "created_at": "2013-01-26T22:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52732",
    "user": "jdemeyer"
}
```

This is totally a pain w.r.t. rebasing.  For example, there are again conflicts with #11641 and #13077.  If this is mostly the automatic scripted part which needs to be rebased, could you please split off the scripted part again such that I could simply run the script instead of applying the patch?



---

archive/issue_comments_052733.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-01-26T22:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52733",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_052734.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-01-26T23:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52734",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_052735.json:
```json
{
    "body": "everything except \"part 1\"",
    "created_at": "2013-01-26T23:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52735",
    "user": "jhpalmieri"
}
```

everything except "part 1"



---

archive/issue_comments_052736.json:
```json
{
    "body": "Attachment\n\nThis is definitely the most painful patch I've ever put into Sage. It would be a huge relief to have it integrated into sage. So I hope nothing more is blocking it. Is the rebase done with your script ?\n\nFlorent",
    "created_at": "2013-01-27T00:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52736",
    "user": "hivert"
}
```

Attachment

This is definitely the most painful patch I've ever put into Sage. It would be a huge relief to have it integrated into sage. So I hope nothing more is blocking it. Is the rebase done with your script ?

Florent



---

archive/issue_comments_052737.json:
```json
{
    "body": "Yes, the script does the main work of moving all of the `MODULE.rst` files around. That is the part that change the most (as people add files to the reference manual), so that's where the rebasing happens.\n\nFlorent, thank you for all of your help with this; your contributions have made this much better. And much of the thanks goes to Mitesh Patel, wherever he is, who put in most of the original work on the patch.",
    "created_at": "2013-01-27T03:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52737",
    "user": "jhpalmieri"
}
```

Yes, the script does the main work of moving all of the `MODULE.rst` files around. That is the part that change the most (as people add files to the reference manual), so that's where the rebasing happens.

Florent, thank you for all of your help with this; your contributions have made this much better. And much of the thanks goes to Mitesh Patel, wherever he is, who put in most of the original work on the patch.



---

archive/issue_comments_052738.json:
```json
{
    "body": "Replying to [comment:181 jhpalmieri]:\n> Florent, thank you for all of your help with this; your contributions have\n> made this much better. And much of the thanks goes to Mitesh Patel, wherever\n> he is, who put in most of the original work on the patch.\n\nAnd thanks a lot for your patience, awaiting for me, not giving up, keeping\ntrying to have this patch moving forward and constantly rebasing it.",
    "created_at": "2013-01-27T09:52:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52738",
    "user": "hivert"
}
```

Replying to [comment:181 jhpalmieri]:
> Florent, thank you for all of your help with this; your contributions have
> made this much better. And much of the thanks goes to Mitesh Patel, wherever
> he is, who put in most of the original work on the patch.

And thanks a lot for your patience, awaiting for me, not giving up, keeping
trying to have this patch moving forward and constantly rebasing it.



---

archive/issue_comments_052739.json:
```json
{
    "body": "Updated script.",
    "created_at": "2013-01-27T11:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52739",
    "user": "jdemeyer"
}
```

Updated script.



---

archive/issue_comments_052740.json:
```json
{
    "body": "\n```\nWARNING: intersphinx inventory '/release/merger/sage-5.7.beta2/devel/sage/doc/output/html/en/reference/combinat/objects.inv' not readable due to AssertionError:\n```\n\nand\n\n```\n/release/merger/sage-5.7.beta2/devel/sage/doc/en/reference/sat/index.rst:77: WARNING: toctree contains reference to nonexisting document 'sat/sage/sat/solvers/dimacs'\n/release/merger/sage-5.7.beta2/devel/sage/doc/en/reference/sat/index.rst:104: WARNING: toctree contains reference to nonexisting document 'sat/sage/sat/converters/polybori'\n/release/merger/sage-5.7.beta2/devel/sage/doc/en/reference/sat/index.rst:124: WARNING: toctree contains reference to nonexisting document 'sat/sage/sat/boolean_polynomials'\n```\n",
    "created_at": "2013-01-27T13:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52740",
    "user": "jdemeyer"
}
```


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

archive/issue_comments_052741.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-01-27T13:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52741",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_052742.json:
```json
{
    "body": "First of all, let me express my frustration: `#%)&<sup>`@`$(&%#</sup>#%`\n\n> {{{\n> /release/merger/sage-5.7.beta2/devel/sage/doc/en/reference/sat/index.rst:77: WARNING: toctree contains reference to nonexisting document 'sat/sage/sat/solvers/dimacs'\n> /release/merger/sage-5.7.beta2/devel/sage/doc/en/reference/sat/index.rst:104: WARNING: toctree contains reference to nonexisting document 'sat/sage/sat/converters/polybori'\n> /release/merger/sage-5.7.beta2/devel/sage/doc/en/reference/sat/index.rst:124: WARNING: toctree contains reference to nonexisting document 'sat/sage/sat/boolean_polynomials'\n> }}}\nThough I don't yet fully understand why, looking at the other doc suggest that\nreplacing the three `:maxdepth: 1` by `:maxdepth: 2` should solve this\nparticular problem. I don't have time to propose a patch now.\n\nReplying to [comment:185 jdemeyer]:\n> {{{\n> WARNING: intersphinx inventory '/release/merger/sage-5.7.beta2/devel/sage/doc/output/html/en/reference/combinat/objects.inv' not readable due to AssertionError:\n> }}}\n\nTo investigate this one I need to install `sage-5.7.beta2` which takes\ntime. Jeroen, could you give a some context for this second error. I've never\nseen it but I only used `sage-5.6.rc1`.\n\nCheers,\n\nFlorent",
    "created_at": "2013-01-27T21:08:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52742",
    "user": "hivert"
}
```

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

archive/issue_comments_052743.json:
```json
{
    "body": "I don't understand these problems, either. I've never seen the one about the intersphinx inventory. For the other one, aside from `maxdepth: 1`, the other difference is that sage.sat is not imported anywhere:\n\n```\nsage: sage.sat\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/Users/palmieri/Desktop/Sage_stuff/sage_builds/6495/sage-5.7.beta0/<ipython console> in <module>()\n\nAttributeError: 'module' object has no attribute 'sat'\n```\n\nCould that be related? Should that be fixed in any case?",
    "created_at": "2013-01-27T21:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52743",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_052744.json:
```json
{
    "body": "See the logfile [attachment:dochtml.log] (this is from a second build, note the error message is slightly different).",
    "created_at": "2013-01-28T07:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52744",
    "user": "jdemeyer"
}
```

See the logfile [attachment:dochtml.log] (this is from a second build, note the error message is slightly different).



---

archive/issue_comments_052745.json:
```json
{
    "body": "Changing assignee from tba to jdemeyer.",
    "created_at": "2013-01-28T07:27:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52745",
    "user": "jdemeyer"
}
```

Changing assignee from tba to jdemeyer.



---

archive/issue_comments_052746.json:
```json
{
    "body": "Replying to [comment:188 jdemeyer]:\n> See the logfile [attachment:dochtml.log] (this is from a second build, note the error message is slightly different).\n\nI'm seriously scared that it could come from a race condition, an nightmare to debug. Is it deterministic ?",
    "created_at": "2013-01-28T08:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52746",
    "user": "hivert"
}
```

Replying to [comment:188 jdemeyer]:
> See the logfile [attachment:dochtml.log] (this is from a second build, note the error message is slightly different).

I'm seriously scared that it could come from a race condition, an nightmare to debug. Is it deterministic ?



---

archive/issue_comments_052747.json:
```json
{
    "body": "On what platforms, and how reliably, do you see the `WARNING: intersphinx inventory ...`?\n\nFor the other problem, this patch fixes it for me:\n\n```diff\ndiff --git a/doc/common/builder.py b/doc/common/builder.py\n--- a/doc/common/builder.py\n+++ b/doc/common/builder.py\n@@ -274,7 +274,7 @@ class AllBuilder(object):\n         global ALLSPHINXOPTS\n         ALLSPHINXOPTS += ' -Q -D multidoc_first_pass=1'\n         for document in refs:\n-            getattr(get_builder(document), 'inventory')(*args, **kwds)\n+            getattr(get_builder(document), name)(*args, **kwds)\n         logger.warning(\"Building reference manual, second pass.\\n\")\n         ALLSPHINXOPTS = ALLSPHINXOPTS.replace(\n             'multidoc_first_pass=1', 'multidoc_first_pass=0')\n```\n\nOr perhaps we should use this one:\n\n```diff\ndiff --git a/doc/common/builder.py b/doc/common/builder.py\n--- a/doc/common/builder.py\n+++ b/doc/common/builder.py\n@@ -274,7 +274,10 @@ class AllBuilder(object):\n         global ALLSPHINXOPTS\n         ALLSPHINXOPTS += ' -Q -D multidoc_first_pass=1'\n         for document in refs:\n-            getattr(get_builder(document), 'inventory')(*args, **kwds)\n+            if name == 'pdf':\n+                getattr(get_builder(document), 'inventory')(*args, **kwds)\n+            else:\n+                getattr(get_builder(document), name)(*args, **kwds)\n         logger.warning(\"Building reference manual, second pass.\\n\")\n         ALLSPHINXOPTS = ALLSPHINXOPTS.replace(\n             'multidoc_first_pass=1', 'multidoc_first_pass=0')\n```\n\nWith an html build, building with this patch does not take any more time. Opinions?",
    "created_at": "2013-01-28T19:44:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52747",
    "user": "jhpalmieri"
}
```

On what platforms, and how reliably, do you see the `WARNING: intersphinx inventory ...`?

For the other problem, this patch fixes it for me:

```diff
diff --git a/doc/common/builder.py b/doc/common/builder.py
--- a/doc/common/builder.py
+++ b/doc/common/builder.py
@@ -274,7 +274,7 @@ class AllBuilder(object):
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
@@ -274,7 +274,10 @@ class AllBuilder(object):
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

archive/issue_comments_052748.json:
```json
{
    "body": "By the way, the new version of the script doesn't work on OS X, because OS X uses a BSD version of `sed` which is not completely compatible with the linux version. To get it to work, you have to make these changes:\n\n```diff\n--- a/trac_6495-script.sh\t2013-01-27 03:44:32.000000000 -0800\n+++ b/trac_6495-script.sh\t2013-01-28 10:53:39.000000000 -0800\n@@ -16,9 +16,9 @@\n do\n     hg rename $f.rst $f/index.rst\n     # delete lines of the form \".. _ch:blah\"\n-    sed -e 's|^\\.\\. _ch:.*$||' -i $f/index.rst\n+    sed -e 's|^\\.\\. _ch:.*$||' -i '' $f/index.rst\n     # remove resulting blank lines from top of file\n-    sed -e '/./,$!d' -i $f/index.rst\n+    sed -e '/./,$!d' -i '' $f/index.rst\n     cat >$f/conf.py <<EOF\n # -*- coding: utf-8 -*-\n # This file is execfile()d with the current directory set to its\n@@ -47,7 +47,7 @@\n cp cmd/conf.py combinat/conf.py\n hg add combinat/conf.py\n # in combinat/index.rst: change \"../sage/combinat/blah\" to \"sage/combinat/blah\"\n-sed -e \"s|\\.\\./||\" -i combinat/index.rst\n+sed -e \"s|\\.\\./||\" -i '' combinat/index.rst\n \n cat >> combinat/index.rst <<EOF\n \n```\n",
    "created_at": "2013-01-28T19:52:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52748",
    "user": "jhpalmieri"
}
```

By the way, the new version of the script doesn't work on OS X, because OS X uses a BSD version of `sed` which is not completely compatible with the linux version. To get it to work, you have to make these changes:

```diff
--- a/trac_6495-script.sh	2013-01-27 03:44:32.000000000 -0800
+++ b/trac_6495-script.sh	2013-01-28 10:53:39.000000000 -0800
@@ -16,9 +16,9 @@
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
@@ -47,7 +47,7 @@
 cp cmd/conf.py combinat/conf.py
 hg add combinat/conf.py
 # in combinat/index.rst: change "../sage/combinat/blah" to "sage/combinat/blah"
-sed -e "s|\.\./||" -i combinat/index.rst
+sed -e "s|\.\./||" -i '' combinat/index.rst
 
 cat >> combinat/index.rst <<EOF
 
```




---

archive/issue_comments_052749.json:
```json
{
    "body": "Replying to [comment:190 jhpalmieri]:\n> On what platforms\nOnly tried `sage.math` so far.\n\n> and how reliably, do you see the `WARNING: intersphinx inventory ...`?\nTwo out of two builds so far.",
    "created_at": "2013-01-29T07:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52749",
    "user": "jdemeyer"
}
```

Replying to [comment:190 jhpalmieri]:
> On what platforms
Only tried `sage.math` so far.

> and how reliably, do you see the `WARNING: intersphinx inventory ...`?
Two out of two builds so far.



---

archive/issue_comments_052750.json:
```json
{
    "body": "script used to generate \"part 1\" patch",
    "created_at": "2013-01-29T12:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52750",
    "user": "jdemeyer"
}
```

script used to generate "part 1" patch



---

archive/issue_comments_052751.json:
```json
{
    "body": "Attachment\n\nThird attempt, now it's the notebook which gives problems:\n\n```\nWARNING: intersphinx inventory '/release/merger/sage-5.7.beta3/devel/sage/doc/output/html/en/reference/notebook/objects.inv' not readable due to ValueError: unknown or unsupported inventory version\n```\n\n\nSo it's certainly not deterministic, but quite likely that **something** goes wrong.",
    "created_at": "2013-01-29T16:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52751",
    "user": "jdemeyer"
}
```

Attachment

Third attempt, now it's the notebook which gives problems:

```
WARNING: intersphinx inventory '/release/merger/sage-5.7.beta3/devel/sage/doc/output/html/en/reference/notebook/objects.inv' not readable due to ValueError: unknown or unsupported inventory version
```


So it's certainly not deterministic, but quite likely that **something** goes wrong.



---

archive/issue_comments_052752.json:
```json
{
    "body": "Hi there,\n\nReplying to [comment:193 jdemeyer]:\n> Third attempt, now it's the notebook which gives problems:\n> {{{\n> WARNING: intersphinx inventory '/release/merger/sage-5.7.beta3/devel/sage/doc/output/html/en/reference/notebook/objects.inv' not readable due to ValueError: unknown or unsupported inventory version\n> }}}\n>\n> So it's certainly not deterministic, but quite likely that **something** goes wrong.\n\nUnfortunately the one week window for sage days I had is over. I didn't had\ntime to make any experiment, and I don't expect to find much time to work on\nthis in the forthcoming days (the new semester is starting and I'm moving from\none house to another in two weeks).\n\nAnyway, I have a guess one what could be happening. The first pass of\ncompilation is designed to build the intersphinx inventory. However, they are\nrewritten during the second phase. Due to parallelism, it is fairly possible\nthat one process is trying to read the inventory just at the time another one\nis writing it. The more process you have, the larger the probability of this\nhappening. This explain why we don't see this on small laptop. I'm not sure\nhow to test that this is precisely what's happening. But if it's the case, the\nsolution should be easy: similarly to what I did recently for indexes, we\nshould deactivate the output of the inventory for a second pass compilation of\na sub-document.\n\nDoes anyone have time to experiment more ?",
    "created_at": "2013-01-29T18:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52752",
    "user": "hivert"
}
```

Hi there,

Replying to [comment:193 jdemeyer]:
> Third attempt, now it's the notebook which gives problems:
> {{{
> WARNING: intersphinx inventory '/release/merger/sage-5.7.beta3/devel/sage/doc/output/html/en/reference/notebook/objects.inv' not readable due to ValueError: unknown or unsupported inventory version
> }}}
>
> So it's certainly not deterministic, but quite likely that **something** goes wrong.

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

archive/issue_comments_052753.json:
```json
{
    "body": "I have not been able to reproduce this on sage.math. I've tried building in /scratch and in /home. Could there be something about /release that's contributing to this? Jeroen, what do you have `MAKE` set to?",
    "created_at": "2013-01-29T18:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52753",
    "user": "jhpalmieri"
}
```

I have not been able to reproduce this on sage.math. I've tried building in /scratch and in /home. Could there be something about /release that's contributing to this? Jeroen, what do you have `MAKE` set to?



---

archive/issue_comments_052754.json:
```json
{
    "body": "Replying to [comment:195 jhpalmieri]:\n> Could there be something about /release that's contributing to this?\nIt's quite a fast disk, could that play a role?\n\n> Jeroen, what do you have `MAKE` set to?\n\n```\nMAKE=make -j6\n```\n",
    "created_at": "2013-01-29T18:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52754",
    "user": "jdemeyer"
}
```

Replying to [comment:195 jhpalmieri]:
> Could there be something about /release that's contributing to this?
It's quite a fast disk, could that play a role?

> Jeroen, what do you have `MAKE` set to?

```
MAKE=make -j6
```




---

archive/issue_comments_052755.json:
```json
{
    "body": "You just have to `strace -o logfile -ff` the build process, then you'll see who is writing to the offending file. Also, can we have a beta with this ticket? Too many patches ;-)",
    "created_at": "2013-01-29T18:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52755",
    "user": "vbraun"
}
```

You just have to `strace -o logfile -ff` the build process, then you'll see who is writing to the offending file. Also, can we have a beta with this ticket? Too many patches ;-)



---

archive/issue_comments_052756.json:
```json
{
    "body": "> You just have to `strace -o logfile -ff` the build process, then you'll see who is writing to the offending file. Also, can we have a beta with this ticket? Too many patches ;-)\n+1",
    "created_at": "2013-01-29T19:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52756",
    "user": "kcrisman"
}
```

> You just have to `strace -o logfile -ff` the build process, then you'll see who is writing to the offending file. Also, can we have a beta with this ticket? Too many patches ;-)
+1



---

archive/issue_comments_052757.json:
```json
{
    "body": "[Here's a tar file](http://sage.math.washington.edu/home/palmieri/misc/6495/sage-5.7.beta1_6495.tar), based on 5.7.beta1.",
    "created_at": "2013-01-29T22:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52757",
    "user": "jhpalmieri"
}
```

[Here's a tar file](http://sage.math.washington.edu/home/palmieri/misc/6495/sage-5.7.beta1_6495.tar), based on 5.7.beta1.



---

archive/issue_comments_052758.json:
```json
{
    "body": "Wow, going fast already.\n\n```\nElapsed time: 284.1 seconds.\n```\n\nJust a *slight* improvement.\n\nI couldn't find (i.e., browser says it's not there)\n\nfile:///Users/.../sage-5.7.beta1_6495/devel/sage-main/doc/output/html/en/reference/functions.html\n\nand the like, but most redirection of actual pages of content seem to be working fine - it's the old ones corresponding to \n\nfile:///Users/.../sage-5.7.beta1_6495/devel/sage-main/doc/output/html/en/reference/functions/index.html\n\nthat seem to have not been \"translated\" properly.",
    "created_at": "2013-01-30T03:03:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52758",
    "user": "kcrisman"
}
```

Wow, going fast already.

```
Elapsed time: 284.1 seconds.
```

Just a *slight* improvement.

I couldn't find (i.e., browser says it's not there)

file:///Users/.../sage-5.7.beta1_6495/devel/sage-main/doc/output/html/en/reference/functions.html

and the like, but most redirection of actual pages of content seem to be working fine - it's the old ones corresponding to 

file:///Users/.../sage-5.7.beta1_6495/devel/sage-main/doc/output/html/en/reference/functions/index.html

that seem to have not been "translated" properly.



---

archive/issue_comments_052759.json:
```json
{
    "body": "Attachment\n\nInitial patch",
    "created_at": "2013-01-31T12:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52759",
    "user": "vbraun"
}
```

Attachment

Initial patch



---

archive/issue_comments_052760.json:
```json
{
    "body": "I can totally reproduce the issue, works every time.\n\nI've started by adding a framework to suppress unwanted messages and print the ones that we do intact (that is, line buffered). Now I can at least start to see what is going on...",
    "created_at": "2013-01-31T12:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52760",
    "user": "vbraun"
}
```

I can totally reproduce the issue, works every time.

I've started by adding a framework to suppress unwanted messages and print the ones that we do intact (that is, line buffered). Now I can at least start to see what is going on...



---

archive/issue_comments_052761.json:
```json
{
    "body": "The issue was indeed that the object inventory was written to and read from parallel processes. Sphinx makes no attempt to update the `object.inv` atomically.\n\nI've changed things such that\n* the inventory build process outputs to `output/inventory` and does not read inventory\n* the second pass then reads the object inventory from `output/inventory` and writes to `output/html`\n\nNow I don't see any races any more. The first stage still warns erroneously about a few missing citations, but thats not a big deal. \n\nAlso, the whole thing runs just shy of 200 seconds on my desktop (i7-3770K)\n\n```\nsage -docbuild all html\n...\nElapsed time: 196.5 seconds.\nDone building the documentation!\n```\n",
    "created_at": "2013-02-01T11:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52761",
    "user": "vbraun"
}
```

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

archive/issue_comments_052762.json:
```json
{
    "body": "Attachment\n\nInitial patch",
    "created_at": "2013-02-01T11:04:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52762",
    "user": "vbraun"
}
```

Attachment

Initial patch



---

archive/issue_comments_052763.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-02-01T11:09:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52763",
    "user": "vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_052764.json:
```json
{
    "body": "Not sure why you removed the script, because the patches still fail to apply:\n\n```\npatching file doc/en/reference/combinat/index.rst\nHunk #1 FAILED at 3\nHunk #3 FAILED at 66\n2 out of 3 hunks FAILED -- saving rejects to file doc/en/reference/combinat/index.rst.rej\npatching file doc/en/reference/groups/index.rst\nHunk #2 succeeded at 39 with fuzz 1 (offset 9 lines).\nabort: patch failed to apply\n```\n",
    "created_at": "2013-02-01T16:41:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52764",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_052765.json:
```json
{
    "body": "I removed the \"apply\" script since I based my patch on top of John's source dist tar file at comment:199.",
    "created_at": "2013-02-01T16:53:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52765",
    "user": "vbraun"
}
```

I removed the "apply" script since I based my patch on top of John's source dist tar file at comment:199.



---

archive/issue_comments_052766.json:
```json
{
    "body": "But in the end the patch will need to be rebased to the latest development version.  Do you want to wait with that until after positive_review?",
    "created_at": "2013-02-01T16:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52766",
    "user": "jdemeyer"
}
```

But in the end the patch will need to be rebased to the latest development version.  Do you want to wait with that until after positive_review?



---

archive/issue_comments_052767.json:
```json
{
    "body": "Ok I've rebased the first patch on top of sage-5.7.beta2. All apply cleanly now.",
    "created_at": "2013-02-01T17:00:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52767",
    "user": "vbraun"
}
```

Ok I've rebased the first patch on top of sage-5.7.beta2. All apply cleanly now.



---

archive/issue_comments_052768.json:
```json
{
    "body": "Ok some more fixes needed as more documentation was changed",
    "created_at": "2013-02-01T17:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52768",
    "user": "vbraun"
}
```

Ok some more fixes needed as more documentation was changed



---

archive/issue_comments_052769.json:
```json
{
    "body": "Updated patch",
    "created_at": "2013-02-01T17:15:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52769",
    "user": "vbraun"
}
```

Updated patch



---

archive/issue_comments_052770.json:
```json
{
    "body": "Attachment\n\nOk I've now correctly resolved the merge conflict ;-) Just a minor change in the combinat docs, its all fine now.\n\nThe only thing left to review would be my final patch. I made all changes that I wanted, so I'm fine with anything else thats in this ticket.",
    "created_at": "2013-02-01T17:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52770",
    "user": "vbraun"
}
```

Attachment

Ok I've now correctly resolved the merge conflict ;-) Just a minor change in the combinat docs, its all fine now.

The only thing left to review would be my final patch. I made all changes that I wanted, so I'm fine with anything else thats in this ticket.



---

archive/issue_comments_052771.json:
```json
{
    "body": "I haven't verified that the intersphinx warning is gone, but I see two other possible problems: I get a warning \n\n```\n[reference] .../sage-5.7.beta2/devel/sage/doc/en/reference/sat/index.rst:: WARNING: document isn't included in any toctree\n```\n\nalong with some citations not being found. Also with [attachment:trac_6495_separate_inventory.patch], the build is a bit slower than without: on my OS X box (with only two threads), the fastest time with the patch was 858 seconds, and more typical (5 out of 6 runs) was 885 seconds or more. Without the patch, the slowest time was 813 seconds.  On sage.math, with `MAKE=\"make -j12\"`: with the patch, 450 seconds, without the patch, 390 seconds.",
    "created_at": "2013-02-01T23:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52771",
    "user": "jhpalmieri"
}
```

I haven't verified that the intersphinx warning is gone, but I see two other possible problems: I get a warning 

```
[reference] .../sage-5.7.beta2/devel/sage/doc/en/reference/sat/index.rst:: WARNING: document isn't included in any toctree
```

along with some citations not being found. Also with [attachment:trac_6495_separate_inventory.patch], the build is a bit slower than without: on my OS X box (with only two threads), the fastest time with the patch was 858 seconds, and more typical (5 out of 6 runs) was 885 seconds or more. Without the patch, the slowest time was 813 seconds.  On sage.math, with `MAKE="make -j12"`: with the patch, 450 seconds, without the patch, 390 seconds.



---

archive/issue_comments_052772.json:
```json
{
    "body": "Are you always nuking the output directory for timings? Also, I'm always adding all inventory files to the intersphinx-mapping whereas before Sphinx would only add them as needed. But there Sphinx assumes that the inventory is in the html directory, so its not good if you want to avoid races.\n\nAs I said already, the first stage still warns erroneously about a few missing cross-document citations. We could hide them, but I don't think its a big deal.\n\nThe `sat/index.rst` isn't included warning is correct. The sat subdoc was not listed in `multidocs_subdoc_list` (`en/reference/conf.py`).",
    "created_at": "2013-02-02T11:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52772",
    "user": "vbraun"
}
```

Are you always nuking the output directory for timings? Also, I'm always adding all inventory files to the intersphinx-mapping whereas before Sphinx would only add them as needed. But there Sphinx assumes that the inventory is in the html directory, so its not good if you want to avoid races.

As I said already, the first stage still warns erroneously about a few missing cross-document citations. We could hide them, but I don't think its a big deal.

The `sat/index.rst` isn't included warning is correct. The sat subdoc was not listed in `multidocs_subdoc_list` (`en/reference/conf.py`).



---

archive/issue_comments_052773.json:
```json
{
    "body": "The last patch fixes the unlisted sat subdoc and moves the citations pickle to the inventory dir. Also, write the citation pickle atomically to avoid another potential race. Now everything builds without any warnings.",
    "created_at": "2013-02-02T12:40:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52773",
    "user": "vbraun"
}
```

The last patch fixes the unlisted sat subdoc and moves the citations pickle to the inventory dir. Also, write the citation pickle atomically to avoid another potential race. Now everything builds without any warnings.



---

archive/issue_comments_052774.json:
```json
{
    "body": "> Are you always nuking the output directory for timings?\n\nYes. Good catch on finding sat not being listed in `multidocs_subdoc_list`, by the way.",
    "created_at": "2013-02-02T16:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52774",
    "user": "jhpalmieri"
}
```

> Are you always nuking the output directory for timings?

Yes. Good catch on finding sat not being listed in `multidocs_subdoc_list`, by the way.



---

archive/issue_comments_052775.json:
```json
{
    "body": "I'm pretty happy with the latest patches, but I'm not quite ready to give a positive review. In my testing, I'm not seeing the intersphinx warning any more, but I was only sporadically able to reproduce it in the first place.\n\nWith the current `useless_chatter` settings, on the first pass through the reference manual, I see two summaries\n\n```\n[polynomia] build succeeded, 1 warning.\n[geometry ] build succeeded, 3 warnings.\n```\n\nThe actual warnings are suppressed, though. Should these message be suppressed (or modified), also? Otherwise, someone might wonder what the warnings actually were.",
    "created_at": "2013-02-04T04:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52775",
    "user": "jhpalmieri"
}
```

I'm pretty happy with the latest patches, but I'm not quite ready to give a positive review. In my testing, I'm not seeing the intersphinx warning any more, but I was only sporadically able to reproduce it in the first place.

With the current `useless_chatter` settings, on the first pass through the reference manual, I see two summaries

```
[polynomia] build succeeded, 1 warning.
[geometry ] build succeeded, 3 warnings.
```

The actual warnings are suppressed, though. Should these message be suppressed (or modified), also? Otherwise, someone might wonder what the warnings actually were.



---

archive/issue_comments_052776.json:
```json
{
    "body": "Another thing: if I have built the documentation already and then run `./sage --docbuild reference html`, then all of the output from building the individual parts of the reference manual is suppressed, so there is a long pause (several minutes, enough to wonder whether it's hung), and then finally \n\n```\n[reference] Compiling the master document\n[reference] updating environment: 0 added, 0 changed, 1098 removed\n[reference] Merging environment/index files...\n```\n",
    "created_at": "2013-02-04T06:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52776",
    "user": "jhpalmieri"
}
```

Another thing: if I have built the documentation already and then run `./sage --docbuild reference html`, then all of the output from building the individual parts of the reference manual is suppressed, so there is a long pause (several minutes, enough to wonder whether it's hung), and then finally 

```
[reference] Compiling the master document
[reference] updating environment: 0 added, 0 changed, 1098 removed
[reference] Merging environment/index files...
```




---

archive/issue_comments_052777.json:
```json
{
    "body": "Maybe just removing one line from `useless_chatter` would address my last point:\n\n```diff\ndiff --git a/doc/common/custom-sphinx-build.py b/doc/common/custom-sphinx-build.py\n--- a/doc/common/custom-sphinx-build.py\n+++ b/doc/common/custom-sphinx-build.py\n@@ -31,7 +31,6 @@\n     re.compile('^Compiling a sub-document'),\n     re.compile('^updating environment: 0 added, 0 changed, 0 removed'),\n     re.compile('^looking for now-outdated files... none found'),\n-    re.compile('^no targets are out of date.'),\n     re.compile('^building \\[.*\\]: targets for 0 source files that are out of date'),\n     re.compile('^loading pickled environment... done'),\n     re.compile('^loading cross citations... done \\([0-9]* citations\\).')\n```\n\ndoesn't look too bad: if you change one file in `homology` then rebuild the docs, then you get\n\n```\n[polynomia] no targets are out of date.\n[combinat ] no targets are out of date.\n[cmd      ] no targets are out of date.\n[arithgrou] no targets are out of date.\n[graphs   ] no targets are out of date.\n[misc     ] no targets are out of date.\n...\n```\n\nuntil it finally gets to something which has changed.",
    "created_at": "2013-02-04T17:00:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52777",
    "user": "jhpalmieri"
}
```

Maybe just removing one line from `useless_chatter` would address my last point:

```diff
diff --git a/doc/common/custom-sphinx-build.py b/doc/common/custom-sphinx-build.py
--- a/doc/common/custom-sphinx-build.py
+++ b/doc/common/custom-sphinx-build.py
@@ -31,7 +31,6 @@
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

archive/issue_comments_052778.json:
```json
{
    "body": "Attachment\n\ncombined patch",
    "created_at": "2013-02-06T03:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52778",
    "user": "jhpalmieri"
}
```

Attachment

combined patch



---

archive/issue_comments_052779.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-02-06T03:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52779",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_052780.json:
```json
{
    "body": "Attachment\n\nI rebased the patches to 5.7.beta3. The only change of substance: in the \"part2\" patch:\n\n```diff\ndiff --git a/sage/graphs/graph_plot.py b/sage/graphs/graph_plot.py\n--- a/sage/graphs/graph_plot.py\n+++ b/sage/graphs/graph_plot.py\n@@ -106,7 +106,7 @@\n       settings from ``DEFAULT_SHOW_OPTIONS`` only affects ``G.show()``.\n \n     * In order to define a default value permanently, you can add a couple of\n-      lines to :doc:`Sage's startup scripts <../../startup>`. Example ::\n+      lines to `Sage's startup scripts <../../../cmd/startup.html>`_. Example ::\n \n        sage: import sage.graphs.graph_plot\n        sage: sage.graphs.graph_plot.DEFAULT_SHOW_OPTIONS['figsize'] = [4,4]\n```\n\n(The only change to the \"part3\" patch was to change the commit message.) With the newest patch ([attachment:trac_6495-filtering.patch]), all superfluous warnings are suppressed. I'm happy with this now.\n\nI think it might be best to include every single patch, or else credit will not get assigned appropriately; for example, the old \"all in one\" patch combined my work (which is really based on mpatel's, but I don't know how to get his name back in here...) with Florent's.",
    "created_at": "2013-02-06T04:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52780",
    "user": "jhpalmieri"
}
```

Attachment

I rebased the patches to 5.7.beta3. The only change of substance: in the "part2" patch:

```diff
diff --git a/sage/graphs/graph_plot.py b/sage/graphs/graph_plot.py
--- a/sage/graphs/graph_plot.py
+++ b/sage/graphs/graph_plot.py
@@ -106,7 +106,7 @@
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

archive/issue_comments_052781.json:
```json
{
    "body": "Attachment\n\napply first",
    "created_at": "2013-02-09T21:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52781",
    "user": "jhpalmieri"
}
```

Attachment

apply first



---

archive/issue_comments_052782.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-02-09T21:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52782",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_052783.json:
```json
{
    "body": "Are you sure that the first patch applies? At least with sage-5.7.beta2, I get a mismatch in doc/en\n/reference/rings_standard/index.rst, which is not surprising as this file does not seem to exist.\n\nBut I suppose it is better anyway to run the sript?",
    "created_at": "2013-02-09T21:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52783",
    "user": "SimonKing"
}
```

Are you sure that the first patch applies? At least with sage-5.7.beta2, I get a mismatch in doc/en
/reference/rings_standard/index.rst, which is not surprising as this file does not seem to exist.

But I suppose it is better anyway to run the sript?



---

archive/issue_comments_052784.json:
```json
{
    "body": "Rebased to Sage 5.7.beta4 (because of the recently added file `doc/en/reference/finite_rings.rst`).",
    "created_at": "2013-02-09T22:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52784",
    "user": "jhpalmieri"
}
```

Rebased to Sage 5.7.beta4 (because of the recently added file `doc/en/reference/finite_rings.rst`).



---

archive/issue_comments_052785.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-02-09T22:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52785",
    "user": "jhpalmieri"
}
```

Attachment



---

archive/issue_comments_052786.json:
```json
{
    "body": "Aha, now I understand! It starts with doc/en/reference/rings_standard.rst, adds one line and moves the result to doc/en/reference/rings_standard/index.rst.\n\nProblem: The line\n\n```\nsage/rings/universal_cyclotomic_field/universal_cyclotomic_field\n```\n\ndoes not exist in sage-5.7.beta2.\n\nIn what ticket has this line been introduced? That would be a new dependency.",
    "created_at": "2013-02-09T22:05:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52786",
    "user": "SimonKing"
}
```

Aha, now I understand! It starts with doc/en/reference/rings_standard.rst, adds one line and moves the result to doc/en/reference/rings_standard/index.rst.

Problem: The line

```
sage/rings/universal_cyclotomic_field/universal_cyclotomic_field
```

does not exist in sage-5.7.beta2.

In what ticket has this line been introduced? That would be a new dependency.



---

archive/issue_comments_052787.json:
```json
{
    "body": "Simon: the patches should apply to 5.7.beta4, and probably only to this version. The script also may only work on this version (or any later version, I hope). This patch is very sensitive to changes, so it needs to be rebased frequently. I'm sorry I haven't kept track of the dependencies -- I just keep rebasing to the latest beta.\n\n[Here's a tar file](http://sage.math.washington.edu/home/palmieri/misc/6495/sage-5.7.beta4-6495.tar) for 5.7.beta4 source with these patches applied.",
    "created_at": "2013-02-09T22:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52787",
    "user": "jhpalmieri"
}
```

Simon: the patches should apply to 5.7.beta4, and probably only to this version. The script also may only work on this version (or any later version, I hope). This patch is very sensitive to changes, so it needs to be rebased frequently. I'm sorry I haven't kept track of the dependencies -- I just keep rebasing to the latest beta.

[Here's a tar file](http://sage.math.washington.edu/home/palmieri/misc/6495/sage-5.7.beta4-6495.tar) for 5.7.beta4 source with these patches applied.



---

archive/issue_comments_052788.json:
```json
{
    "body": "Bad. It seems that I managed to destroy my sage-5.7.beta2 by this patch. No idea how that happened. Could it be that popping the patch does not revert all changes?\n\nReplying to [comment:221 jhpalmieri]:\n> [Here's a tar file](http://sage.math.washington.edu/home/palmieri/misc/6495/sage-5.7.beta4-6495.tar) for 5.7.beta4 source with these patches applied.\n\nI currently don't have the bandwith to download a Sage tarball.",
    "created_at": "2013-02-09T22:28:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52788",
    "user": "SimonKing"
}
```

Bad. It seems that I managed to destroy my sage-5.7.beta2 by this patch. No idea how that happened. Could it be that popping the patch does not revert all changes?

Replying to [comment:221 jhpalmieri]:
> [Here's a tar file](http://sage.math.washington.edu/home/palmieri/misc/6495/sage-5.7.beta4-6495.tar) for 5.7.beta4 source with these patches applied.

I currently don't have the bandwith to download a Sage tarball.



---

archive/issue_comments_052789.json:
```json
{
    "body": "How about downloading [just the sage library spkg](http://sage.math.washington.edu/home/palmieri/misc/6495/sage-5.7.beta4-6495/spkg/standard/sage-5.7.beta4-6495.spkg) (which is 57M)?\n\nAgain, I apologize for not keeping track of the dependencies. My general reaction when a new beta comes out is to try to apply the patches, find that they don't apply, swear a bit, and then rebase them. If someone does something minor (say, modify `doc/en/reference/algebras.rst`), then running the script instead of applying the \"part1\" patch should take care of things. But if someone adds a new file to `doc/en/reference/`, then several of the patch files will need to be rebased. This happened between 5.7.beta3 and 5.7.beta4.\n\nIs there a good way with mercurial to find out all of the recent changes to files in a certain directory? Then I could identify the dependencies easily.",
    "created_at": "2013-02-09T22:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52789",
    "user": "jhpalmieri"
}
```

How about downloading [just the sage library spkg](http://sage.math.washington.edu/home/palmieri/misc/6495/sage-5.7.beta4-6495/spkg/standard/sage-5.7.beta4-6495.spkg) (which is 57M)?

Again, I apologize for not keeping track of the dependencies. My general reaction when a new beta comes out is to try to apply the patches, find that they don't apply, swear a bit, and then rebase them. If someone does something minor (say, modify `doc/en/reference/algebras.rst`), then running the script instead of applying the "part1" patch should take care of things. But if someone adds a new file to `doc/en/reference/`, then several of the patch files will need to be rebased. This happened between 5.7.beta3 and 5.7.beta4.

Is there a good way with mercurial to find out all of the recent changes to files in a certain directory? Then I could identify the dependencies easily.



---

archive/issue_comments_052790.json:
```json
{
    "body": "Replying to [comment:223 jhpalmieri]:\n> How about downloading [just the sage library spkg](http://sage.math.washington.edu/home/palmieri/misc/6495/sage-5.7.beta4-6495/spkg/standard/sage-5.7.beta4-6495.spkg) (which is 57M)?\n\nThat could be a good idea.",
    "created_at": "2013-02-09T22:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52790",
    "user": "SimonKing"
}
```

Replying to [comment:223 jhpalmieri]:
> How about downloading [just the sage library spkg](http://sage.math.washington.edu/home/palmieri/misc/6495/sage-5.7.beta4-6495/spkg/standard/sage-5.7.beta4-6495.spkg) (which is 57M)?

That could be a good idea.



---

archive/issue_comments_052791.json:
```json
{
    "body": "Hooray, the patches apply cleanly! Thank you for naming the additional dependencies!\n\nBy the way, I still don't understand why seemingly my hg repository became dysfunctional, but now it seems to be fine again (which I don't understand either...).",
    "created_at": "2013-02-09T23:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52791",
    "user": "SimonKing"
}
```

Hooray, the patches apply cleanly! Thank you for naming the additional dependencies!

By the way, I still don't understand why seemingly my hg repository became dysfunctional, but now it seems to be fine again (which I don't understand either...).



---

archive/issue_comments_052792.json:
```json
{
    "body": "I don't understand it either. I occasionally have seen this, too, but not at all reproducibly, and not recently. Maybe mercurial is just more likely get confused if it moves lot of files around and creates a lot of directories, and then the patch is popped? Or maybe it also requires the patch not to apply cleanly first?",
    "created_at": "2013-02-09T23:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52792",
    "user": "jhpalmieri"
}
```

I don't understand it either. I occasionally have seen this, too, but not at all reproducibly, and not recently. Maybe mercurial is just more likely get confused if it moves lot of files around and creates a lot of directories, and then the patch is popped? Or maybe it also requires the patch not to apply cleanly first?



---

archive/issue_comments_052793.json:
```json
{
    "body": "In the ticket description, it is said: \"Also create a file algebras/conf.py for the build configuration. All of these new conf.py files are identical.\"\n\nIf they are all identical, why is there not just a single conf.py, to which all other locations refer by a soft link? In that way, it would be easier to maintain changes.",
    "created_at": "2013-02-09T23:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52793",
    "user": "SimonKing"
}
```

In the ticket description, it is said: "Also create a file algebras/conf.py for the build configuration. All of these new conf.py files are identical."

If they are all identical, why is there not just a single conf.py, to which all other locations refer by a soft link? In that way, it would be easier to maintain changes.



---

archive/issue_comments_052794.json:
```json
{
    "body": "Good question. The files `conf.py` are pretty minimal, and most of the content is in `en/reference/conf_sub.py`, which is imported by each `conf.py` file. So the idea is that to maintain it, you would just need to modify `conf_sub.py`. But here's a new version of the part 1 patch and the script which creates links directly from `en/reference/MODULE/conf.py` pointing to `en/reference/conf_sub.py`. This seems to work. I'll check on OpenSolaris to make sure there's nothing strange going on there.",
    "created_at": "2013-02-10T03:26:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52794",
    "user": "jhpalmieri"
}
```

Good question. The files `conf.py` are pretty minimal, and most of the content is in `en/reference/conf_sub.py`, which is imported by each `conf.py` file. So the idea is that to maintain it, you would just need to modify `conf_sub.py`. But here's a new version of the part 1 patch and the script which creates links directly from `en/reference/MODULE/conf.py` pointing to `en/reference/conf_sub.py`. This seems to work. I'll check on OpenSolaris to make sure there's nothing strange going on there.



---

archive/issue_comments_052795.json:
```json
{
    "body": "apply first",
    "created_at": "2013-02-10T03:27:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52795",
    "user": "jhpalmieri"
}
```

apply first



---

archive/issue_comments_052796.json:
```json
{
    "body": "Attachment\n\n[attachment:trac_6495-script-jhp.2.sh] is identical to the old script; it can be deleted. (Why can't I delete my own attachments?)",
    "created_at": "2013-02-10T03:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52796",
    "user": "jhpalmieri"
}
```

Attachment

[attachment:trac_6495-script-jhp.2.sh] is identical to the old script; it can be deleted. (Why can't I delete my own attachments?)



---

archive/issue_comments_052797.json:
```json
{
    "body": "Attachment\n\nscript used to generate \"part 1\" patch",
    "created_at": "2013-02-10T03:30:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52797",
    "user": "jhpalmieri"
}
```

Attachment

script used to generate "part 1" patch



---

archive/issue_comments_052798.json:
```json
{
    "body": "> [attachment:trac_6495-script-jhp.2.sh] is identical to the old script; it can be deleted. (Why can't I delete my own attachments?)\nI suppose so that the history is preserved.  That said, it would be helpful to have that ability for at least some users.\n\nGiven your post at [this sage-support thread](https://groups.google.com/forum/?fromgroups=#!topic/sage-support/vj_W8wc9Mic), now it's really exciting to think about this getting in.",
    "created_at": "2013-02-10T04:11:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52798",
    "user": "kcrisman"
}
```

> [attachment:trac_6495-script-jhp.2.sh] is identical to the old script; it can be deleted. (Why can't I delete my own attachments?)
I suppose so that the history is preserved.  That said, it would be helpful to have that ability for at least some users.

Given your post at [this sage-support thread](https://groups.google.com/forum/?fromgroups=#!topic/sage-support/vj_W8wc9Mic), now it's really exciting to think about this getting in.



---

archive/issue_comments_052799.json:
```json
{
    "body": "For the record: Documentation builds for me, at least with the old patches. And now I am really curious what will happen if I add a thematic tutorial and try to link to the reference manual, via `:class:`sage.structure.parent.Parent``",
    "created_at": "2013-02-10T07:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52799",
    "user": "SimonKing"
}
```

For the record: Documentation builds for me, at least with the old patches. And now I am really curious what will happen if I add a thematic tutorial and try to link to the reference manual, via `:class:`sage.structure.parent.Parent``



---

archive/issue_comments_052800.json:
```json
{
    "body": "That said: I am not totally sure, but my impression is that building the documentation took longer than in the old way. Also, it surprises me that `sage --docbuild all pdf` takes more than three minutes after previously doing `sage --docbuild all html`.",
    "created_at": "2013-02-10T07:52:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52800",
    "user": "SimonKing"
}
```

That said: I am not totally sure, but my impression is that building the documentation took longer than in the old way. Also, it surprises me that `sage --docbuild all pdf` takes more than three minutes after previously doing `sage --docbuild all html`.



---

archive/issue_comments_052801.json:
```json
{
    "body": "OK, processing the `LaTeX` files seems less trivial than I thought, and does take time.\n\nCurrently, I am seeing a lot of unresolved references, and one fatal error:\n\n```\n...\n\n! LaTeX Error: Too deeply nested.\n\nSee the LaTeX manual or LaTeX Companion for explanation.\nType  H <return>  for immediate help.\n ...                                              \n                                                  \nl.26942 \\begin{Verbatim}[commandchars=\\\\\\{\\}]\n                                             \n? \n! Emergency stop.\n ...                                              \n                                                  \nl.26942 \\begin{Verbatim}[commandchars=\\\\\\{\\}]\n                                             \n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on categories.log.\nmake: *** [categories.pdf] Fehler 1\nBuild finished.  The built documents can be found in /home/simon/SAGE/debug/sage-5.7.beta2/devel/sage/doc/output/pdf/en/reference/categories\n[coding   ] building [latex]: all documents\n[coding   ] updating environment: [config changed] 6 added, 0 changed, 0 removed\n[coding   ] reading sources... [ 16%] index\n...\n```\n\n\nI suppose there will automatically be a second run, which resolves the cross-references. And we will see about the fatal error.",
    "created_at": "2013-02-10T08:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52801",
    "user": "SimonKing"
}
```

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

archive/issue_comments_052802.json:
```json
{
    "body": "OK, the links in the pdf and the mathematics in the html do not seem to work.\n\nFor example, I am looking at the documentation of sage.structure.coerce, The Coercion Model.\n\nI see\n\n```\nCoercions are canonical (possibly modulo a finite number of deterministic choices) morphisms, and the set of all coercions between all parents forms a commuting diagram (modulo possibly rounding issues). [Math Processing Error] is an example of a coercion. These are invoked implicitly by the coercion model.\n```\n\nin the html. It is fine in the pdf.\n\nBoth in pdf and html, I read\n\n```\nFor more information on how to specify coercions, conversions, and actions, see the documentation for Parent.\n\nclass sage.structure.coerce.CoercionModel_cache_maps\n\n    Bases: sage.structure.element.CoercionModel\n\n    See also sage.categories.pushout\n```\n\n\nI would expect the \"see the documentation for Parent\" and \"See also sage.categories.pushout\" come with a link, but apparently that has been forgotten (bug in the documentation).\n\nIn the html, `Bases: sage.structure.element.CoercionModel` is a link. In the pdf, it is *not* a link. I guess it should be a link in pdf, too, isn't it?",
    "created_at": "2013-02-10T09:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52802",
    "user": "SimonKing"
}
```

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

In the html, `Bases: sage.structure.element.CoercionModel` is a link. In the pdf, it is *not* a link. I guess it should be a link in pdf, too, isn't it?



---

archive/issue_comments_052803.json:
```json
{
    "body": "And now the good news: When I added my (not yet completed) thematic tutorial on categories and coercion, both the mathematical type-setting *and* the links to the reference manual (!) work fine.",
    "created_at": "2013-02-10T09:07:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52803",
    "user": "SimonKing"
}
```

And now the good news: When I added my (not yet completed) thematic tutorial on categories and coercion, both the mathematical type-setting *and* the links to the reference manual (!) work fine.



---

archive/issue_comments_052804.json:
```json
{
    "body": "Replying to [comment:235 SimonKing]:\n> OK, the links in the pdf and the mathematics in the html do not seem to work.\n\nFor the links in the pdf, I don't know what to do about that. Intersphinx seems to work only in html, not pdf, or at least that's what I gather from [its documentation](http://sphinx-doc.org/ext/intersphinx.html). I don't even know if it's possible to put relative links into a PDF file. \n\nFor mathematics in the html, I don't see this at all, either on OS X (with any of the browsers I've tried) or on sage.math. See [the coercion model page](http://sage.math.washington.edu/home/palmieri/misc/6495-jsmath/html/en/reference/coercion/sage/structure/coerce.html) on sage.math, for instance -- this renders fine for me with my browser.\n\nDid you delete the directory `devel/sage/doc/output` before the first attempt at a parallel build? If not, maybe there were artifacts there which caused problems. Otherwise, I don't know what's causing it. What is your OS and what is your browser?\n\nReplying to [comment:236 SimonKing]:\n> And now the good news: When I added my (not yet completed) thematic tutorial on categories and coercion, both the mathematical type-setting *and* the links to the reference manual (!) work fine.\n\nGreat.",
    "created_at": "2013-02-10T21:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52804",
    "user": "jhpalmieri"
}
```

Replying to [comment:235 SimonKing]:
> OK, the links in the pdf and the mathematics in the html do not seem to work.

For the links in the pdf, I don't know what to do about that. Intersphinx seems to work only in html, not pdf, or at least that's what I gather from [its documentation](http://sphinx-doc.org/ext/intersphinx.html). I don't even know if it's possible to put relative links into a PDF file. 

For mathematics in the html, I don't see this at all, either on OS X (with any of the browsers I've tried) or on sage.math. See [the coercion model page](http://sage.math.washington.edu/home/palmieri/misc/6495-jsmath/html/en/reference/coercion/sage/structure/coerce.html) on sage.math, for instance -- this renders fine for me with my browser.

Did you delete the directory `devel/sage/doc/output` before the first attempt at a parallel build? If not, maybe there were artifacts there which caused problems. Otherwise, I don't know what's causing it. What is your OS and what is your browser?

Replying to [comment:236 SimonKing]:
> And now the good news: When I added my (not yet completed) thematic tutorial on categories and coercion, both the mathematical type-setting *and* the links to the reference manual (!) work fine.

Great.



---

archive/issue_comments_052805.json:
```json
{
    "body": "Replying to [comment:237 jhpalmieri]:\n> Did you delete the directory `devel/sage/doc/output` before the first attempt at a parallel build?\n\nI deleted it, and I think I did not do a parallel build (or at least, I did not define MAKE to be `make -j2`).\n\n> If not, maybe there were artifacts there which caused problems. Otherwise, I don't know what's causing it. What is your OS and what is your browser?\n\n`openSuse` 12.1 Asparagus, and Firefox 18.0\n\n> Replying to [comment:236 SimonKing]:\n> > And now the good news: When I added my (not yet completed) thematic tutorial on categories and coercion, both the mathematical type-setting *and* the links to the reference manual (!) work fine.\n\nAnd that's why I wonder: The maths is fine in the tutorial, but not in the reference manual.\n\nI just observed: When I load a page from the reference manual, there is a message on the lower left corner of my browser, `Loading [MathJax]/jax/output/HTML-CSS/imageFonts.js`, and a bit later there is a message \"File failed to load\" (but too quickly disappearing, I didn't manage to copy the message).",
    "created_at": "2013-02-10T22:32:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52805",
    "user": "SimonKing"
}
```

Replying to [comment:237 jhpalmieri]:
> Did you delete the directory `devel/sage/doc/output` before the first attempt at a parallel build?

I deleted it, and I think I did not do a parallel build (or at least, I did not define MAKE to be `make -j2`).

> If not, maybe there were artifacts there which caused problems. Otherwise, I don't know what's causing it. What is your OS and what is your browser?

`openSuse` 12.1 Asparagus, and Firefox 18.0

> Replying to [comment:236 SimonKing]:
> > And now the good news: When I added my (not yet completed) thematic tutorial on categories and coercion, both the mathematical type-setting *and* the links to the reference manual (!) work fine.

And that's why I wonder: The maths is fine in the tutorial, but not in the reference manual.

I just observed: When I load a page from the reference manual, there is a message on the lower left corner of my browser, `Loading [MathJax]/jax/output/HTML-CSS/imageFonts.js`, and a bit later there is a message "File failed to load" (but too quickly disappearing, I didn't manage to copy the message).



---

archive/issue_comments_052806.json:
```json
{
    "body": "To debug Firefox issues: Tools->Web Developer->Web Console. \n\nSimon's issue sounds a lot like http://docs.mathjax.org/en/v1.1-latest/installation.html#firefox-and-local-fonts. Either use a different browser or install the stix fonts. Should be fine if served over http instead of a local dir.",
    "created_at": "2013-02-11T13:46:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52806",
    "user": "vbraun"
}
```

To debug Firefox issues: Tools->Web Developer->Web Console. 

Simon's issue sounds a lot like http://docs.mathjax.org/en/v1.1-latest/installation.html#firefox-and-local-fonts. Either use a different browser or install the stix fonts. Should be fine if served over http instead of a local dir.



---

archive/issue_comments_052807.json:
```json
{
    "body": "Replying to [comment:239 vbraun]:\n> To debug Firefox issues: Tools->Web Developer->Web Console. \n> \n> Simon's issue sounds a lot like http://docs.mathjax.org/en/v1.1-latest/installation.html#firefox-and-local-fonts. Either use a different browser or install the stix fonts.\n\nWould this explain why the maths typesetting is fine in one document and broken in another document?",
    "created_at": "2013-02-11T14:07:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52807",
    "user": "SimonKing"
}
```

Replying to [comment:239 vbraun]:
> To debug Firefox issues: Tools->Web Developer->Web Console. 
> 
> Simon's issue sounds a lot like http://docs.mathjax.org/en/v1.1-latest/installation.html#firefox-and-local-fonts. Either use a different browser or install the stix fonts.

Would this explain why the maths typesetting is fine in one document and broken in another document?



---

archive/issue_comments_052808.json:
```json
{
    "body": "Replying to [comment:240 SimonKing]:\n> Would this explain why the maths typesetting is fine in one document and broken in another document?\n\nYes. It depends on whether or not mathjax is loaded from the same directory as the document. And we don't plaster a copy of mathjax into every subdirectory.",
    "created_at": "2013-02-11T14:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52808",
    "user": "vbraun"
}
```

Replying to [comment:240 SimonKing]:
> Would this explain why the maths typesetting is fine in one document and broken in another document?

Yes. It depends on whether or not mathjax is loaded from the same directory as the document. And we don't plaster a copy of mathjax into every subdirectory.



---

archive/issue_comments_052809.json:
```json
{
    "body": "Replying to [comment:241 vbraun]:\n> Replying to [comment:240 SimonKing]:\n> > Would this explain why the maths typesetting is fine in one document and broken in another document?\n> \n> Yes. It depends on whether or not mathjax is loaded from the same directory as the document. And we don't plaster a copy of mathjax into every subdirectory.\n\nOK, by installing the fonts as suggested on the link you provided, I can now see the reference manual in all its beauty.",
    "created_at": "2013-02-11T15:42:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52809",
    "user": "SimonKing"
}
```

Replying to [comment:241 vbraun]:
> Replying to [comment:240 SimonKing]:
> > Would this explain why the maths typesetting is fine in one document and broken in another document?
> 
> Yes. It depends on whether or not mathjax is loaded from the same directory as the document. And we don't plaster a copy of mathjax into every subdirectory.

OK, by installing the fonts as suggested on the link you provided, I can now see the reference manual in all its beauty.



---

archive/issue_comments_052810.json:
```json
{
    "body": "Is there anything left to review? \n\nThere are no inter-document links to specific anchors in the PDF reference manual. Its not a big loss since it your pdf viewer probably doesn't support them anyways (e.g. the PDF viewer in Chrome does not). If you want hyperlinks just use the html version.",
    "created_at": "2013-02-12T11:46:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52810",
    "user": "vbraun"
}
```

Is there anything left to review? 

There are no inter-document links to specific anchors in the PDF reference manual. Its not a big loss since it your pdf viewer probably doesn't support them anyways (e.g. the PDF viewer in Chrome does not). If you want hyperlinks just use the html version.



---

archive/issue_comments_052811.json:
```json
{
    "body": "Replying to [comment:243 vbraun]:\n> Is there anything left to review? \n\nThe only unreviewed parts are [attachment:trac_6495-filtering.patch] and the change to [attachment:trac_6495-part1-moving-files-link.patch] to use symbolic links for `reference/MODULE/conf.py` (see [comment:229]).",
    "created_at": "2013-02-12T15:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52811",
    "user": "jhpalmieri"
}
```

Replying to [comment:243 vbraun]:
> Is there anything left to review? 

The only unreviewed parts are [attachment:trac_6495-filtering.patch] and the change to [attachment:trac_6495-part1-moving-files-link.patch] to use symbolic links for `reference/MODULE/conf.py` (see [comment:229]).



---

archive/issue_comments_052812.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-12T15:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52812",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_052813.json:
```json
{
    "body": "Looks reasonable to me.",
    "created_at": "2013-02-12T15:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52813",
    "user": "vbraun"
}
```

Looks reasonable to me.



---

archive/issue_comments_052814.json:
```json
{
    "body": "Attachment\n\nLog file of troublesome build",
    "created_at": "2013-02-13T11:09:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52814",
    "user": "jdemeyer"
}
```

Attachment

Log file of troublesome build



---

archive/issue_comments_052815.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-02-13T11:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52815",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_052816.json:
```json
{
    "body": "It still doesn't quite work completely. During one build, I got\n\n```\nBuilding reference manual, first pass.\n\n[polynomia] Exception occurred:\n[polynomia] File \"/release/merger/sage-5.8.beta0/local/lib/python/pickle.py\", line 880, in load_eof\n[polynomia] raise EOFError\n[polynomia] EOFError\n[polynomia] The full traceback has been saved in /tmp/release/sphinx-err-2hqEZ_.log, if you want to report the issue to the developers.\n[polynomia] Please also report this if it was a user error, so that a better error message can be provided next time.\n[polynomia] Either send bugs to the mailing list at <http://groups.google.com/group/sphinx-dev/>,\n[polynomia] or report them in the tracker at <http://bitbucket.org/birkenfeld/sphinx/issues/>. Thanks!\n```\n\nwhere the \"full traceback\" reads\n\n```\n# Sphinx version: 1.1.2\n# Python version: 2.7.3\n# Docutils version: 0.7 release\n# Jinja2 version: 2.5.5\nTraceback (most recent call last):\n  File \"/release/merger/sage-5.8.beta0/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/cmdline.py\", line 188, in main\n    warningiserror, tags)\n  File \"/release/merger/sage-5.8.beta0/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/application.py\", line 114, in __init__\n    self.setup_extension(extension)\n  File \"/release/merger/sage-5.8.beta0/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/application.py\", line 247, in setup_extension\n    mod = __import__(extension, None, None, ['setup'])\n  File \"/release/merger/sage-5.8.beta0/devel/sage-main/doc/common/sage_autodoc.py\", line 35, in <module>\n    from sphinx.pycode import ModuleAnalyzer, PycodeError\n  File \"/release/merger/sage-5.8.beta0/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/pycode/__init__.py\", line 25, in <module>\n    pygrammar = driver.load_grammar(_grammarfile)\n  File \"/release/merger/sage-5.8.beta0/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/pycode/pgen2/driver.py\", line 135, in load_grammar\n    g.load(gp)\n  File \"/release/merger/sage-5.8.beta0/local/lib/python2.7/site-packages/Sphinx-1.1.2-py2.7.egg/sphinx/pycode/pgen2/grammar.py\", line 96, in load\n    d = pickle.load(f)\n  File \"/release/merger/sage-5.8.beta0/local/lib/python/pickle.py\", line 1378, in load\n    return Unpickler(file).load()\n  File \"/release/merger/sage-5.8.beta0/local/lib/python/pickle.py\", line 858, in load\n    dispatch[key](self)\n  File \"/release/merger/sage-5.8.beta0/local/lib/python/pickle.py\", line 880, in load_eof\n    raise EOFError\nEOFError\n```\n\nThe second pass of this build starts with:\n\n```\nBuilding reference manual, second pass.\n\n[polynomia] loading pickled environment... not yet created\n[homology ] loading pickled environment... not yet created\n[polynomia] WARNING: intersphinx inventory '/release/merger/sage-5.8.beta0/devel/sage/doc/output/inventory/en/reference/polynomial_rings/objects.inv' not fetchable due to <type 'exceptions.IOError'>: [Errno 2] No such file or directory: '/release/merger/sage-5.8.beta0/devel/sage/doc/output/inventory/en/reference/polynomial_rings/objects.inv'\n```\n\n\nSee [attachment:dochtml.log]",
    "created_at": "2013-02-13T11:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52816",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_052817.json:
```json
{
    "body": "Upon first use, Sphinx apparenty saves a cached pickle of its grammar under `site-packages/` (!) non-atomically (!). Thats just peachy...",
    "created_at": "2013-02-13T12:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52817",
    "user": "vbraun"
}
```

Upon first use, Sphinx apparenty saves a cached pickle of its grammar under `site-packages/` (!) non-atomically (!). Thats just peachy...



---

archive/issue_comments_052818.json:
```json
{
    "body": "I think the best place to solve this would be in the Sphinx installer: generate the grammar pickle at install time. It's completely normal to put files in `site-packages/` during install and you won't need to worry about non-atomic accesses.",
    "created_at": "2013-02-13T12:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52818",
    "user": "jdemeyer"
}
```

I think the best place to solve this would be in the Sphinx installer: generate the grammar pickle at install time. It's completely normal to put files in `site-packages/` during install and you won't need to worry about non-atomic accesses.



---

archive/issue_comments_052819.json:
```json
{
    "body": "So I don't know exactly what to do. We could create a script like this in the Sphinx spkg, and then run it as part of the installation. How does that sound?\n\n```python\n\n# Code taken from sphinx/pycode/__init__.py to generate the grammar pickle.\n\nfrom os import path\nfrom sphinx import package_dir\nfrom sphinx.pycode.pgen2 import driver\n\n# load the Python grammar\n_grammarfile = path.join(package_dir, 'pycode', 'Grammar.txt')\npygrammar = driver.load_grammar(_grammarfile)\n```\n",
    "created_at": "2013-02-13T19:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52819",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_052820.json:
```json
{
    "body": "New spkg: http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-1.1.2.p2.spkg.\nSee [attachment:trac_6495-sphinx-grammar.patch] for the changes.",
    "created_at": "2013-02-13T20:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52820",
    "user": "jhpalmieri"
}
```

New spkg: http://sage.math.washington.edu/home/palmieri/SPKG/sphinx-1.1.2.p2.spkg.
See [attachment:trac_6495-sphinx-grammar.patch] for the changes.



---

archive/issue_comments_052821.json:
```json
{
    "body": "patch for Sphinx spkg; for review only",
    "created_at": "2013-02-13T20:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52821",
    "user": "jhpalmieri"
}
```

patch for Sphinx spkg; for review only



---

archive/issue_comments_052822.json:
```json
{
    "body": "Attachment\n\nThanks, looks good and works for me. Hopefully that was the last race in Sphinx, fingers crossed ;-)",
    "created_at": "2013-02-13T20:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52822",
    "user": "vbraun"
}
```

Attachment

Thanks, looks good and works for me. Hopefully that was the last race in Sphinx, fingers crossed ;-)



---

archive/issue_comments_052823.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-02-13T20:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52823",
    "user": "vbraun"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_052824.json:
```json
{
    "body": "The spkg is not clean:\n\n```\n$ hg status\n? create_grammar_pickle.py~\n```\n",
    "created_at": "2013-02-14T07:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52824",
    "user": "jdemeyer"
}
```

The spkg is not clean:

```
$ hg status
? create_grammar_pickle.py~
```




---

archive/issue_comments_052825.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-02-14T07:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52825",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_052826.json:
```json
{
    "body": "Fixed. Sorry about that.",
    "created_at": "2013-02-14T15:36:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52826",
    "user": "jhpalmieri"
}
```

Fixed. Sorry about that.



---

archive/issue_comments_052827.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-02-14T15:36:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52827",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_052828.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-02-15T08:19:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52828",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_052829.json:
```json
{
    "body": "In `devel/sage/doc/common/custom-sphinx-build.py`, you write\n\n```\n    def write(self, str):\n        try:\n            self._write(str)\n        except:\n            import traceback\n            traceback.print_exc(file=self._stream)\n```\n\nOne should never use bare `except:` statements, because these usually catch too much, for example `KeyboardInterrupt`s. Use `except StandardError` if you want to catch all errors, or catch a specific exception instead.\n\nAnd in `devel/sage/doc/common/themes/sageref/layout.html`, indentation is done mostly with spaces but there are a few TABs. You should use spaces consistently.\n\nBut most importantly: the code actually seems to work now! It still needs buildbot testing though.",
    "created_at": "2013-02-15T08:19:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52829",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_052830.json:
```json
{
    "body": "I got rid of the tabs in `layout.html`.",
    "created_at": "2013-02-15T17:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52830",
    "user": "jhpalmieri"
}
```

I got rid of the tabs in `layout.html`.



---

archive/issue_comments_052831.json:
```json
{
    "body": "apply second",
    "created_at": "2013-02-15T17:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52831",
    "user": "jhpalmieri"
}
```

apply second



---

archive/issue_comments_052832.json:
```json
{
    "body": "Attachment\n\nUpdated patch",
    "created_at": "2013-02-15T20:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52832",
    "user": "vbraun"
}
```

Attachment

Updated patch



---

archive/issue_comments_052833.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2013-02-15T20:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52833",
    "user": "vbraun"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_052834.json:
```json
{
    "body": "I've replaced the bare `except:`.",
    "created_at": "2013-02-15T20:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52834",
    "user": "vbraun"
}
```

I've replaced the bare `except:`.



---

archive/issue_comments_052835.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-02-17T22:41:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52835",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_052836.json:
```json
{
    "body": "Hurrah !!!",
    "created_at": "2013-02-17T23:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52836",
    "user": "hivert"
}
```

Hurrah !!!



---

archive/issue_comments_052837.json:
```json
{
    "body": "Could I make one suggestion (perhaps for a later ticket)? Compiling the docs does not say any longer where to look on one's machine for the compiled docs. This was a very useful feature beforehand!\n\nThanks for your work on this!\n\nAnne",
    "created_at": "2013-02-19T20:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52837",
    "user": "aschilling"
}
```

Could I make one suggestion (perhaps for a later ticket)? Compiling the docs does not say any longer where to look on one's machine for the compiled docs. This was a very useful feature beforehand!

Thanks for your work on this!

Anne



---

archive/issue_comments_052838.json:
```json
{
    "body": "Replying to [comment:261 aschilling]:\n> Could I make one suggestion (perhaps for a later ticket)? Compiling the docs does not say any longer where to look on one's machine for the compiled docs. This was a very useful feature beforehand!\n\nSee #14148.",
    "created_at": "2013-02-19T23:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52838",
    "user": "jhpalmieri"
}
```

Replying to [comment:261 aschilling]:
> Could I make one suggestion (perhaps for a later ticket)? Compiling the docs does not say any longer where to look on one's machine for the compiled docs. This was a very useful feature beforehand!

See #14148.



---

archive/issue_comments_052839.json:
```json
{
    "body": "See #14156 for a blocker follow-up.",
    "created_at": "2013-02-21T13:02:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52839",
    "user": "jdemeyer"
}
```

See #14156 for a blocker follow-up.



---

archive/issue_comments_052840.json:
```json
{
    "body": "See #14199 for another follow-up.",
    "created_at": "2013-02-27T20:23:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52840",
    "user": "jdemeyer"
}
```

See #14199 for another follow-up.



---

archive/issue_comments_052841.json:
```json
{
    "body": "Can somebody here please review **blocker** ticket #14199?",
    "created_at": "2013-03-06T20:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52841",
    "user": "jdemeyer"
}
```

Can somebody here please review **blocker** ticket #14199?



---

archive/issue_comments_052842.json:
```json
{
    "body": "Another followup #14245: cloning is broken.",
    "created_at": "2013-03-08T12:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52842",
    "user": "hivert"
}
```

Another followup #14245: cloning is broken.



---

archive/issue_comments_052843.json:
```json
{
    "body": "Followup #14626: docbuilder hangs if latex fails.",
    "created_at": "2013-05-22T15:11:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6495",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6495#issuecomment-52843",
    "user": "jdemeyer"
}
```

Followup #14626: docbuilder hangs if latex fails.
