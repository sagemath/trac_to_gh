# Issue 7466: 21 warnings when building the HTML version of the reference manual, Sage 4.2.1

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-11-15 01:10:46

Assignee: mvngu

CC:  sage-combinat

Building the HTML version of the reference manual for Sage 4.2.1, I received 21 warnings. These are warnings are:

```
/scratch/mvngu/build/sage-4.2.1/devel/sage/doc/en/reference/sage/geometry/lattice_polytope.rst:: (ERROR/3) Content block expected for the "note" directive; none found.
/scratch/mvngu/build/sage-4.2.1/local/lib/python2.6/site-packages/sage/plot/contour_plot.py:docstring of sage.plot.contour_plot.region_plot:30: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
/scratch/mvngu/build/sage-4.2.1/devel/sage/doc/en/reference/sage/rings/polynomial/polynomial_element.rst:: (ERROR/3) Content block expected for the "warning" directive; none found.
/scratch/mvngu/build/sage-4.2.1/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py:docstring of sage.rings.polynomial.polynomial_ring_constructor.PolynomialRing:200: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
/scratch/mvngu/build/sage-4.2.1/local/lib/python2.6/site-packages/sagenb/notebook/config.py:docstring of sagenb.notebook.config:26: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.
/scratch/mvngu/build/sage-4.2.1/devel/sage/doc/en/reference/sagenb/notebook/twist.rst:6: (WARNING/2) autodoc can't import/find class 'sagenb.notebook.twist.UserToplevel.userchild_download_worksheets.zip', it reported error: "userchild_download_worksheets", please check your spelling and sys.path
/scratch/mvngu/build/sage-4.2.1/local/lib/python2.6/site-packages/sagenb/storage/abstract_storage.py:docstring of sagenb.storage.abstract_storage.Datastore.worksheets:7: (WARNING/2) Literal block expected; none found.
/scratch/mvngu/build/sage-4.2.1/local/lib/python2.6/site-packages/sagenb/storage/filesystem_storage.py:docstring of sagenb.storage.filesystem_storage.FilesystemDatastore.worksheets:7: (WARNING/2) Literal block expected; none found.
looking for now-outdated files... none found
pickling environment... done
checking consistency... /scratch/mvngu/build/sage-4.2.1/devel/sage/doc/en/reference/sage/server/introspect.rst:: WARNING: document isn't included in any toctree
/scratch/mvngu/build/sage-4.2.1/devel/sage/doc/en/reference/sage/server/misc.rst:: WARNING: document isn't included in any toctree
/scratch/mvngu/build/sage-4.2.1/devel/sage/doc/en/reference/sage/server/notebook/cell.rst:: WARNING: document isn't included in any toctree
/scratch/mvngu/build/sage-4.2.1/devel/sage/doc/en/reference/sage/server/notebook/css.rst:: WARNING: document isn't included in any toctree
/scratch/mvngu/build/sage-4.2.1/devel/sage/doc/en/reference/sage/server/notebook/docHTMLProcessor.rst:: WARNING: document isn't included in any toctree
/scratch/mvngu/build/sage-4.2.1/devel/sage/doc/en/reference/sage/server/notebook/interact.rst:: WARNING: document isn't included in any toctree
/scratch/mvngu/build/sage-4.2.1/devel/sage/doc/en/reference/sage/server/notebook/js.rst:: WARNING: document isn't included in any toctree
/scratch/mvngu/build/sage-4.2.1/devel/sage/doc/en/reference/sage/server/notebook/notebook.rst:: WARNING: document isn't included in any toctree
/scratch/mvngu/build/sage-4.2.1/devel/sage/doc/en/reference/sage/server/notebook/template.rst:: WARNING: document isn't included in any toctree
/scratch/mvngu/build/sage-4.2.1/devel/sage/doc/en/reference/sage/server/notebook/twist.rst:: WARNING: document isn't included in any toctree
/scratch/mvngu/build/sage-4.2.1/devel/sage/doc/en/reference/sage/server/notebook/worksheet.rst:: WARNING: document isn't included in any toctree
/scratch/mvngu/build/sage-4.2.1/devel/sage/doc/en/reference/sage/server/simple/twist.rst:: WARNING: document isn't included in any toctree
/scratch/mvngu/build/sage-4.2.1/devel/sage/doc/en/reference/sage/server/support.rst:: WARNING: document isn't included in any toctree
```



---

Comment by jhpalmieri created at 2009-12-05 05:00:00

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2009-12-05 05:00:00

With 4.3.alpha1, I get these warnings and some others.  The attached patch fixes some of these, leaving seven.  Four of those come from sagenb, and so should that spkg should be patched.  The other three have to do with the new category stuff, and I don't know how to fix them:

```
/Applications/sage/devel/sage/doc/en/reference/sage/categories/hopf_algebras.rst:6: (WARNING/2) autodoc can't import/find class 'sage.categories.hopf_algebras.DualCategory.ParentMethods', it reported error: "DualCategory", please check your spelling and sys.path
/Applications/sage/devel/sage/doc/en/reference/sage/categories/semigroups.rst:6: (WARNING/2) autodoc can't import/find class 'sage.categories.semigroups.SubQuotients.ElementMethods', it reported error: "SubQuotients", please check your spelling and sys.path
/Applications/sage/devel/sage/doc/en/reference/sage/categories/semigroups.rst:6: (WARNING/2) autodoc can't import/find class 'sage.categories.semigroups.SubQuotients.ParentMethods', it reported error: "SubQuotients", please check your spelling and sys.path
```

Instructions: apply the patch.  Also delete (by hand) everything in the directory `SAGE_ROOT/devel/sage/doc/en/reference/sage/server/` *except* for 

```
trac/trac.rst
wiki/moin.rst
```

(These files are not tracked by Mercurial, so we have to delete them by hand, as far as I can tell.)


---

Attachment


---

Comment by mvngu created at 2009-12-05 14:52:30

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2009-12-05 14:52:30

On Sage 4.3.alpha1, I first deleted the `output/` directory and then proceeded to rebuild the HTML version of the reference manual:

```
[mvngu`@`sage sage-4.3.alpha1-7466-reference]$ rm -rf devel/sage-main/doc/output/
./sage -docbuild reference html
```

This resulted in 34 warnings. To apply patches to Sage 4.3.alpha1, first you must resolve the issue of missing image files as reported at ticket #7606. I again removed the `output/` directory, deleted everything under the directory `SAGE_ROOT/devel/sage/doc/en/reference/sage/server/` *except* for

```
trac/trac.rst
wiki/moin.rst
```

and finally I applied the patch `trac_7466.patch`. Rebuilding the HTML version of the reference manual now only resulted in 8 warnings. So positive review from me. The remaining warnings can be dealt with in another ticket. I don't see those remaining warnings as a reason to hold back this ticket.


---

Comment by mhansen created at 2009-12-06 08:23:23

Resolution: fixed
