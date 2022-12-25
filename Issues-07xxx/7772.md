# Issue 7772: resolve 15 warnings when building the tutorial

archive/issues_007772.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  maoziyang@gmail.com\n\nKeywords: tutorial\n\nBuilding the tutorial in Sage 4.3 results in 15 warnings, all of which are related to references and bibliography:\n\n```\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/afterword.rst:180: WARNING: duplicate citation Py, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/afterword.rst:182: WARNING: duplicate citation PyDev, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst:27: WARNING: duplicate citation Py, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/afterword.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst:30: WARNING: duplicate citation PyDev, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/afterword.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/interactive_shell.rst:948: WARNING: duplicate citation Py, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/interfaces.rst:355: WARNING: duplicate citation GAPkg, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/introduction.rst:149: WARNING: duplicate citation Dive, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/introduction.rst:152: WARNING: duplicate citation PyT, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/programming.rst:853: WARNING: duplicate citation PyT, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/introduction.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_algebra.rst:416: WARNING: duplicate citation GAP, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_algebra.rst:418: WARNING: duplicate citation Max, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_functions.rst:4: WARNING: duplicate label section-plot, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_plotting.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_plotting.rst:4: WARNING: duplicate label section-plot, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_functions.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_plotting.rst:230: WARNING: duplicate citation Jmol, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\n/virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/tour_polynomial.rst:332: WARNING: duplicate citation Si, other instance in /virtual/scratch/mvngu/sage-4.3/devel/sage/doc/en/tutorial/bibliography.rst\nlooking for now-outdated files... none found\npickling environment... done\nchecking consistency... done\npreparing documents... done\nwriting output... [100%] tour_rings             \nwriting additional files... genindex search\ncopying static files... done\ndumping search index... done\ndumping object inventory... done\nbuild succeeded, 15 warnings.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7772\n\n",
    "closed_at": "2010-01-03T21:01:16Z",
    "created_at": "2009-12-27T12:43:44Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "resolve 15 warnings when building the tutorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7772",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

CC:  maoziyang@gmail.com

Keywords: tutorial

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

archive/issue_comments_066876.json:
```json
{
    "body": "Attachment [trac_7772-typo.patch](tarball://root/attachments/some-uuid/ticket7772/trac_7772-typo.patch) by mvngu created at 2009-12-27 12:48:50\n\nbased on Sage 4.3",
    "created_at": "2009-12-27T12:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66876",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7772-typo.patch](tarball://root/attachments/some-uuid/ticket7772/trac_7772-typo.patch) by mvngu created at 2009-12-27 12:48:50

based on Sage 4.3



---

archive/issue_comments_066877.json:
```json
{
    "body": "Attachment [trac_7772-bib.patch](tarball://root/attachments/some-uuid/ticket7772/trac_7772-bib.patch) by mvngu created at 2009-12-27 12:49:09\n\napply on top of previous",
    "created_at": "2009-12-27T12:49:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66877",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_7772-bib.patch](tarball://root/attachments/some-uuid/ticket7772/trac_7772-bib.patch) by mvngu created at 2009-12-27 12:49:09

apply on top of previous



---

archive/issue_comments_066878.json:
```json
{
    "body": "Changing keywords from \"\" to \"tutorial\".",
    "created_at": "2009-12-27T12:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66878",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing keywords from "" to "tutorial".



---

archive/issue_comments_066879.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-27T12:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66879",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066880.json:
```json
{
    "body": "Here's a description of the attachments:\n\n* `trac_7772-typo.patch` -- change suggestions reported by Mao Ziyang on [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/d9f229c7d019faec). This patch contains two typo fixes.\n \n* `trac_7772-bib.patch` -- this patch resolves the 15 warnings obtained when building the tutorial. To resolve the warnings, I re-organized the bibliography. This involves deleting duplicate references. All references are now centrally managed in the section \"Bibliography\".",
    "created_at": "2009-12-27T12:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66880",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Here's a description of the attachments:

* `trac_7772-typo.patch` -- change suggestions reported by Mao Ziyang on [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/d9f229c7d019faec). This patch contains two typo fixes.
 
* `trac_7772-bib.patch` -- this patch resolves the 15 warnings obtained when building the tutorial. To resolve the warnings, I re-organized the bibliography. This involves deleting duplicate references. All references are now centrally managed in the section "Bibliography".



---

archive/issue_comments_066881.json:
```json
{
    "body": "diff between old and new patches",
    "created_at": "2009-12-27T17:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66881",
    "user": "https://github.com/jhpalmieri"
}
```

diff between old and new patches



---

archive/issue_comments_066882.json:
```json
{
    "body": "Attachment [trac_7772-all-in-one.patch](tarball://root/attachments/some-uuid/ticket7772/trac_7772-all-in-one.patch) by @jhpalmieri created at 2009-12-27 17:26:28\n\napply only this patch",
    "created_at": "2009-12-27T17:26:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66882",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_7772-all-in-one.patch](tarball://root/attachments/some-uuid/ticket7772/trac_7772-all-in-one.patch) by @jhpalmieri created at 2009-12-27 17:26:28

apply only this patch



---

archive/issue_comments_066883.json:
```json
{
    "body": "Mostly looks good, although the math environment dealt with in `trac_7772-typo.patch` doesn't look good either before or after the patch.  I'm attaching a patch to fix this.  In fact, there are two attachments: the \"delta\" patch shows my changes, and for the convenience of the release manager, the \"all-in-one\" patch is just that.\n\nFor anyone else who looks at this, to get rid of the \"duplicate citation\" messages, I had to delete the output and then rebuild the tutorial; otherwise, the cached versions were confusing Sphinx.",
    "created_at": "2009-12-27T17:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66883",
    "user": "https://github.com/jhpalmieri"
}
```

Mostly looks good, although the math environment dealt with in `trac_7772-typo.patch` doesn't look good either before or after the patch.  I'm attaching a patch to fix this.  In fact, there are two attachments: the "delta" patch shows my changes, and for the convenience of the release manager, the "all-in-one" patch is just that.

For anyone else who looks at this, to get rid of the "duplicate citation" messages, I had to delete the output and then rebuild the tutorial; otherwise, the cached versions were confusing Sphinx.



---

archive/issue_comments_066884.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-27T17:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66884",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066885.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T21:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7772#issuecomment-66885",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_018597.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-01-03T21:01:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7772",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7772#event-18597"
}
```
