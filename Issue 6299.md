# Issue 6299: major scoping error introduced by refactoring dsage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-15 15:37:32

Assignee: boothby

Configuration of dsage / notebook's secure certificate was completely 100% broken by factoring Dsage out from sage:


```
----------------------------------------------------------------------
sage: notebook.setup()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/scratch/wstein/sage/temp/sage.math.washington.edu/15047/_scratch_wstein_sage_init_sage_0.py in <module>()

AttributeError: NotebookObject instance has no attribute 'settup'
sage: notebook.setup()
Using dsage certificates.
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/scratch/wstein/sage/temp/sage.math.washington.edu/15047/_scratch_wstein_sage_init_sage_0.py in <module>()

/scratch/wstein/build/sage-4.0.2.rc0/local/lib/python2.5/site-packages/sage/server/notebook/run_notebook.pyc in notebook_setup(self)
     39         print "Using dsage certificates."
     40         dsage = os.path.join(DOT_SAGE, 'dsage')
---> 41         sage.dsage.all.dsage.setup()
     42         shutil.copyfile(dsage + '/cacert.pem', private_pem)
     43         shutil.copyfile(dsage + '/pubcert.pem', public_pem)

NameError: global name 'sage' is not defined
sage: 

----

```



---

Attachment


---

Comment by mhansen created at 2009-06-15 19:03:06

Changing status from new to assigned.


---

Comment by mhansen created at 2009-06-15 19:03:06

Changing assignee from boothby to mhansen.


---

Comment by ncalexan created at 2009-06-15 20:38:42

`notebook.setup()` worked for me on sage.math.


---

Comment by boothby created at 2009-06-15 22:42:23

works for me too; tested on 4.0.2.rc0


---

Comment by was created at 2009-06-15 23:18:18

merged into 4.0.2.rc1


---

Comment by was created at 2009-06-15 23:18:18

Resolution: fixed
