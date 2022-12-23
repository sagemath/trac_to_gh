# Issue 5373: [with patch, needs review] fix problem in builder.copytree

Issue created by migration from https://trac.sagemath.org/ticket/5373

Original creator: mhansen

Original creation time: 2009-02-25 18:43:24

Assignee: tba


```
$ mv ~/sage/devel/sage/doc/output/html ~/sage/devel/sage/doc/output/jason

$ sage -docbuild website html
sphinx-build -b html -d
/home/jason/sage/devel/sage/doc/output/doctrees/en/website   .
/home/jason/sage/devel/sage/doc/output/html/en/website
Sphinx v0.5.1, building html
loading pickled environment... done
building [html]: targets for 1 source files that are out of date
updating environment: 0 added, 0 changed, 0 removed
preparing documents... WARNING: html_favicon is not an .ico file
done
writing output... index
writing additional files... genindex search index
copying static files... done
dumping search index... done
dumping object inventory... done
build succeeded, 1 warning.
Build finished.  The built documents can be found in
/home/jason/sage/devel/sage/doc/output/html/en/website

Then I try to build it again:

$ sage -docbuild website html
sphinx-build -b html -d
/home/jason/sage/devel/sage/doc/output/doctrees/en/website   .
/home/jason/sage/devel/sage/doc/output/html/en/website
Sphinx v0.5.1, building html
loading pickled environment... done
building [html]: targets for 0 source files that are out of date
updating environment: 0 added, 0 changed, 0 removed
no targets are out of date.
Build finished.  The built documents can be found in
/home/jason/sage/devel/sage/doc/output/html/en/website
Traceback (most recent call last):
  File "/home/jason/sage/devel/sage/doc/common/builder.py", line 674,
in <module>
    getattr(get_builder(name), type)(*args)
  File "/home/jason/sage/devel/sage/doc/common/builder.py", line 291,
in html
    os.path.realpath(os.path.join(html_output_dir, '..')))
  File "/home/jason/sage/devel/sage/doc/common/builder.py", line 101,
in copytree
    raise StandardError, errors
StandardError:
[('/home/jason/sage/devel/sage/doc/output/html/en/website/_static',
'/home/jason/sage/devel/sage-main/doc/output/html/en/_static', "[Errno
17] File exists:
'/home/jason/sage/devel/sage-main/doc/output/html/en/_static'"),
('/home/jason/sage/devel/sage/doc/output/html/en/website/_sources',
'/home/jason/sage/devel/sage-main/doc/output/html/en/_sources', "[Errno
17] File exists:
'/home/jason/sage/devel/sage-main/doc/output/html/en/_sources'")]

```



---

Attachment


---

Comment by mhansen created at 2009-02-25 18:45:13

The main thing was to make it so that copytree calls itself instead of shutil.copytree.  I fixed the problem with "Error" by making it shutil.Error.


---

Comment by mhansen created at 2009-02-25 18:45:13

Changing assignee from tba to mhansen.


---

Comment by mhansen created at 2009-02-25 18:45:13

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-03-01 02:49:09

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 02:49:28

Resolution: fixed


---

Comment by mabshoff created at 2009-03-01 02:49:28

Merged in Sage 3.4.rc0.

Cheers,

Michael
