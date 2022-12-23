# Issue 7772: resolve 15 warnings when building the tutorial

archive/issues_007772.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  maoziyang@gmail.com\n\nBuilding the tutorial in Sage 4.3 results in 15 warnings, all of which are related to references and bibliography:\n\n```\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/afterword.rst:180: WARNING: duplicate citation Py, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/afterword.rst:182: WARNING: duplicate citation PyDev, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst:27: WARNING: duplicate citation Py, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/afterword.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst:30: WARNING: duplicate citation PyDev, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/afterword.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/interactive_shell.rst:948: WARNING: duplicate citation Py, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/interfaces.rst:355: WARNING: duplicate citation GAPkg, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/introduction.rst:149: WARNING: duplicate citation Dive, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/introduction.rst:152: WARNING: duplicate citation PyT, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/programming.rst:853: WARNING: duplicate citation PyT, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/introduction.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_algebra.rst:416: WARNING: duplicate citation GAP, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_algebra.rst:418: WARNING: duplicate citation Max, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_functions.rst:4: WARNING: duplicate label section-plot, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_plotting.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_plotting.rst:4: WARNING: duplicate label section-plot, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_functions.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_plotting.rst:230: WARNING: duplicate citation Jmol, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_polynomial.rst:332: WARNING: duplicate citation Si, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\nlooking for now-outdated files... none found\npickling environment... done\nchecking consistency... done\npreparing documents... done\nwriting output... [100%] tour_rings             \nwriting additional files... genindex search\ncopying static files... done\ndumping search index... done\ndumping object inventory... done\nbuild succeeded, 15 warnings.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7772\n\n",
    "created_at": "2009-12-27T12:43:44Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "resolve 15 warnings when building the tutorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7772",
    "user": "mvngu"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/7772





---

archive/issue_comments_066992.json:
```json
{
    "body": "Attachment\n\nbased on Sage 4.3",
    "created_at": "2009-12-27T12:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66992",
    "user": "mvngu"
}
```

Attachment

based on Sage 4.3



---

archive/issue_comments_066993.json:
```json
{
    "body": "Attachment\n\napply on top of previous",
    "created_at": "2009-12-27T12:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66993",
    "user": "mvngu"
}
```

Attachment

apply on top of previous



---

archive/issue_comments_066994.json:
```json
{
    "body": "Changing keywords from \"\" to \"tutorial\".",
    "created_at": "2009-12-27T12:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66994",
    "user": "mvngu"
}
```

Changing keywords from "" to "tutorial".



---

archive/issue_comments_066995.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-27T12:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66995",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066996.json:
```json
{
    "body": "Here's a description of the attachments:\n\n* `trac_7772-typo.patch` -- change suggestions reported by Mao Ziyang on [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/d9f229c7d019faec). This patch contains two typo fixes.\n \n* `trac_7772-bib.patch` -- this patch resolves the 15 warnings obtained when building the tutorial. To resolve the warnings, I re-organized the bibliography. This involves deleting duplicate references. All references are now centrally managed in the section \"Bibliography\".",
    "created_at": "2009-12-27T12:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66996",
    "user": "mvngu"
}
```

Here's a description of the attachments:

* `trac_7772-typo.patch` -- change suggestions reported by Mao Ziyang on [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/d9f229c7d019faec). This patch contains two typo fixes.
 
* `trac_7772-bib.patch` -- this patch resolves the 15 warnings obtained when building the tutorial. To resolve the warnings, I re-organized the bibliography. This involves deleting duplicate references. All references are now centrally managed in the section "Bibliography".



---

archive/issue_comments_066997.json:
```json
{
    "body": "diff between old and new patches",
    "created_at": "2009-12-27T17:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66997",
    "user": "jhpalmieri"
}
```

diff between old and new patches



---

archive/issue_comments_066998.json:
```json
{
    "body": "Attachment\n\napply only this patch",
    "created_at": "2009-12-27T17:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66998",
    "user": "jhpalmieri"
}
```

Attachment

apply only this patch



---

archive/issue_comments_066999.json:
```json
{
    "body": "Mostly looks good, although the math environment dealt with in `trac_7772-typo.patch` doesn't look good either before or after the patch.  I'm attaching a patch to fix this.  In fact, there are two attachments: the \"delta\" patch shows my changes, and for the convenience of the release manager, the \"all-in-one\" patch is just that.\n\nFor anyone else who looks at this, to get rid of the \"duplicate citation\" messages, I had to delete the output and then rebuild the tutorial; otherwise, the cached versions were confusing Sphinx.",
    "created_at": "2009-12-27T17:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66999",
    "user": "jhpalmieri"
}
```

Mostly looks good, although the math environment dealt with in `trac_7772-typo.patch` doesn't look good either before or after the patch.  I'm attaching a patch to fix this.  In fact, there are two attachments: the "delta" patch shows my changes, and for the convenience of the release manager, the "all-in-one" patch is just that.

For anyone else who looks at this, to get rid of the "duplicate citation" messages, I had to delete the output and then rebuild the tutorial; otherwise, the cached versions were confusing Sphinx.



---

archive/issue_comments_067000.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-27T17:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-67000",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067001.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T21:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-67001",
    "user": "mhansen"
}
```

Resolution: fixed
