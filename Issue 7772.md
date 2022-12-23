# Issue 7772: resolve 15 warnings when building the tutorial

Issue created by migration from https://trac.sagemath.org/ticket/7772

Original creator: mvngu

Original creation time: 2009-12-27 12:43:44

Assignee: mvngu

CC:  maoziyang@gmail.com

Building the tutorial in Sage 4.3 results in 15 warnings, all of which are related to references and bibliography:

```
/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/afterword.rst:180: WARNING: duplicate citation Py, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst
/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/afterword.rst:182: WARNING: duplicate citation PyDev, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst
/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst:27: WARNING: duplicate citation Py, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/afterword.rst
/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst:30: WARNING: duplicate citation PyDev, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/afterword.rst
/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/interactive_shell.rst:948: WARNING: duplicate citation Py, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst
/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/interfaces.rst:355: WARNING: duplicate citation GAPkg, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst
/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/introduction.rst:149: WARNING: duplicate citation Dive, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst
/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/introduction.rst:152: WARNING: duplicate citation PyT, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst
/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/programming.rst:853: WARNING: duplicate citation PyT, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/introduction.rst
/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_algebra.rst:416: WARNING: duplicate citation GAP, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst
/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_algebra.rst:418: WARNING: duplicate citation Max, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst
/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_functions.rst:4: WARNING: duplicate label section-plot, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_plotting.rst
/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_plotting.rst:4: WARNING: duplicate label section-plot, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_functions.rst
/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_plotting.rst:230: WARNING: duplicate citation Jmol, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst
/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_polynomial.rst:332: WARNING: duplicate citation Si, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] tour_rings             
writing additional files... genindex search
copying static files... done
dumping search index... done
dumping object inventory... done
build succeeded, 15 warnings.
```



---

Attachment

based on Sage 4.3


---

Attachment

apply on top of previous


---

Comment by mvngu created at 2009-12-27 12:54:43

Changing keywords from "" to "tutorial".


---

Comment by mvngu created at 2009-12-27 12:54:43

Changing status from new to needs_review.


---

Comment by mvngu created at 2009-12-27 12:54:43

Here's a description of the attachments:

 * `trac_7772-typo.patch` -- change suggestions reported by Mao Ziyang on [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/d9f229c7d019faec). This patch contains two typo fixes.
 
 * `trac_7772-bib.patch` -- this patch resolves the 15 warnings obtained when building the tutorial. To resolve the warnings, I re-organized the bibliography. This involves deleting duplicate references. All references are now centrally managed in the section "Bibliography".


---

Comment by jhpalmieri created at 2009-12-27 17:26:13

diff between old and new patches


---

Attachment

apply only this patch


---

Comment by jhpalmieri created at 2009-12-27 17:28:10

Mostly looks good, although the math environment dealt with in `trac_7772-typo.patch` doesn't look good either before or after the patch.  I'm attaching a patch to fix this.  In fact, there are two attachments: the "delta" patch shows my changes, and for the convenience of the release manager, the "all-in-one" patch is just that.

For anyone else who looks at this, to get rid of the "duplicate citation" messages, I had to delete the output and then rebuild the tutorial; otherwise, the cached versions were confusing Sphinx.


---

Comment by jhpalmieri created at 2009-12-27 17:28:10

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 21:01:16

Resolution: fixed
