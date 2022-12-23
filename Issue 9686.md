# Issue 9686: Polish documentation for canonical label

Issue created by migration from https://trac.sagemath.org/ticket/9686

Original creator: rlm

Original creation time: 2010-08-04 13:38:38

Assignee: jason, ncohen, rlm




---

Attachment


---

Comment by rlm created at 2010-08-04 13:41:11

Changing status from new to needs_review.


---

Attachment


---

Comment by mvngu created at 2010-08-04 19:58:54

With Sage 4.5.2.rc1 and the patch [attachment:trac_9686.patch], building the reference manual produces the following warning:

```sh
[mvngu@sage sage-4.5.2.rc1]$ ./sage -docbuild reference html
sphinx-build -b html -d /dev/shm/mvngu/sage-4.5.2.rc1/devel/sage/doc/output/doctrees/en/reference    /dev/shm/mvngu/sage-4.5.2.rc1/devel/sage/doc/en/reference /dev/shm/mvngu/sage-4.5.2.rc1/devel/sage/doc/output/html/en/reference
Running Sphinx v0.6.3
loading pickled environment... done
building [html]: targets for 1 source files that are out of date
updating environment: 0 added, 1 changed, 0 removed
reading sources... [100%] sage/graphs/generic_graph
:0: (ERROR/3) Unexpected indentation.
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] sage/graphs/generic_graph
writing additional files... genindex modindex search
copying static files... done
dumping search index... done
dumping object inventory... done
build succeeded, 1 warning.
Build finished.  The built documents can be found in /dev/shm/mvngu/sage-4.5.2.rc1/devel/sage/doc/output/html/en/reference
```

This is due to how the added list are indented. The indentation of lists in the enclosing method, i.e. `canonical_label`, is inconsistent. Look at how the list of input is indented as compared with the list immediately following the first docstring line and the new list proposed by the patch [attachment:trac_9686.patch]. The reviewer patch [attachment:trac_9686-reviewer.patch] should restore some consistency in how lists in `canonical_label` are indented. The reviewer patch also resolves the above warning. 



I'm happy with the content of [attachment:trac_9686.patch]. We need someone other than me to look over [attachment:trac_9686-reviewer.patch].


---

Comment by rlm created at 2010-08-04 22:45:14

Looks good.


---

Comment by rlm created at 2010-08-04 22:45:14

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-09 09:47:03

Resolution: fixed
