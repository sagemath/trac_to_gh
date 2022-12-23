# Issue 7750: search_doc: print warning if some Sage docs are missing

Issue created by migration from https://trac.sagemath.org/ticket/7750

Original creator: jhpalmieri

Original creation time: 2009-12-22 21:14:50

Assignee: mvngu

If you call search_doc and one piece of the Sage docs are missing, this patch prints the following warning (and then proceeds with the search):

```
sage: search_doc('factorial')
Warning, the following Sage documentation hasn't been built,
so documentation search results may be incomplete:

/Applications/sage/devel/sage/doc/output/html/fr/tutorial

You can build this with 'sage -docbuild fr/tutorial html'.
```

If more than one piece is missing, it prints this warning:

```
sage: search_doc('factorial')
Warning, the following Sage documentation hasn't been built,
so documentation search results may be incomplete:

/Applications/sage/devel/sage/doc/output/html/en/developer
/Applications/sage/devel/sage/doc/output/html/en/installation
/Applications/sage/devel/sage/doc/output/html/fr/tutorial

You can build these with 'sage -docbuild DOCUMENT html',
where DOCUMENT is one of 'developer', 'installation', 'fr/tutorial', 
or you can use 'sage -docbuild all html' to build all of the missing documentation.
```

You can test this by installing the patch and selectively deleting and building pieces of the documentation.  You don't need to restart Sage between deletions or builds -- do that in another window, and each call to search_doc will check for existence of the docs each time.

There are no doctests for this, because I think that doctests should assume that the Sage build is complete: all documentation should be assumed to be built.



---

Comment by jhpalmieri created at 2009-12-22 21:15:35

Changing status from new to needs_review.


---

Attachment


---

Comment by was created at 2009-12-22 21:31:10

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-22 21:31:10

This is *awesome*.  Positive review.


---

Comment by mhansen created at 2010-01-04 02:12:14

Resolution: fixed
