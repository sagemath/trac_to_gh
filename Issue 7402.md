# Issue 7402: SageNB -- Use `pkg_resources` to locate `DATA` directory

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-11-06 11:24:02

Assignee: boothby

CC:  mpatel

[`pkg_resources`](http://peak.telecommunity.com/DevCenter/PkgResources) is the official way to access data directories in a `setuptools` package. Using `pkg_resources` to locate the `DATA` directory will allow us to use [`.pth` files](http://bob.pythonmac.org/archives/2005/02/06/using-pth-files-for-python-development/) for ease of development. For example:


```
$ pwd
/home/timdumol/devel/sagenb-0.3.5/src
$ dev_dir=`pwd`
$ cd /opt/sage/local/lib/python2.6/site-packages/
$ rm -r sagenb*
$ cat "$dev_dir" > sagenb.pth
```


Thus, there will no longer be a need to `sage -python setup.py install` after every change.


---

Comment by timdumol created at 2009-11-06 11:25:38

Uses `pkg_resources` to locate the DATA directory.


---

Attachment

This patch should do it.

As a note, we won't even need to restart the server if all we edit are template files. A big plus in ease of development, IMHO.


---

Comment by timdumol created at 2009-11-06 11:31:18

Changing status from new to needs_review.


---

Comment by timdumol created at 2009-11-06 11:31:18

Changing keywords from "" to "sagenb notebook".


---

Comment by mpatel created at 2009-11-13 23:01:03

This works for me.  In particular, the Se test suite is oblivious to the change.

For me, an existing `site-packages/sagenb` takes precedence over `sagenb.pth`.  Short of deleting the former, can we reverse this?  How about a flag (e.g, `--dev-mode` or `--in-source`) to `sage -python setup.py install` that toggles between "standard" and "developer" modes?


---

Comment by mpatel created at 2009-11-13 23:01:03

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2009-11-14 00:06:19

A Sphinx warning to keep in mind:

```
copying static files... WARNING: static directory '/home/apps/sage/local/lib/python/site-packages/sagenb/data/jsmath/' does not exist
```



---

Comment by timdumol created at 2009-11-15 05:10:38

Replying to [comment:3 mpatel]:
> A Sphinx warning to keep in mind:
> {{{
> copying static files... WARNING: static directory '/home/apps/sage/local/lib/python/site-packages/sagenb/data/jsmath/' does not exist
> }}}
Since this is only used for development, I don't think there's much of a problem. It should be possible to fix by making Sphinx read the .pth file and look there, but I am inexperienced regarding that.

Regards the --dev-mode thing, I just noticed that SageNB uses disttools, not setuptools, which is why the `sage -python setup.py develop` command does not exist. This is now #7467.


---

Comment by was created at 2009-12-08 05:33:36

Resolution: fixed
