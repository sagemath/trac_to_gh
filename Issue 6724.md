# Issue 6724: spell-check all modules under sage/modules

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-08-10 08:41:04

Assignee: tba

As the subject says.


---

Comment by mvngu created at 2009-08-11 16:09:29

based on Sage 4.1.1.rc2


---

Attachment

I don't think I should give a positive review here. The docbuild gives me :

```
Warning: could not import sage.modules.fg_pid.fgp_morphism
cannot import name FGP_Morphism
```



---

Comment by mvngu created at 2009-08-12 12:01:40

With Sage 4.1.1.rc2, the only warnings I see when building the reference manual are:

```
WARNING: /scratch/mvngu/sage-4.1.1.rc2-sage.math/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.GenericGraph.kirchhoff_matrix:56: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sage-4.1.1.rc2-sage.math/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.GenericGraph.laplacian_matrix:56: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sage-4.1.1.rc2-sage.math/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.Graph.clique_number:19: (WARNING/2) Inline literal start-string without end-string.
```

These warnings are fixed by #6684. So I applied patches against Sage 4.1.1.rc2 in this order:
 1. the patch at #6684
 1. the patch on this ticket
The reference manual then rebuilt without any warnings. So I'm curious where and how you got the warning you reported.


---

Comment by wuthrich created at 2009-08-12 12:19:44

It was on sage4.1.1.rc2 + the two other spelling-tickets that you just closed #6723 and #6731.

This warning appeared in sage -docbuild reference html

and the table of contents of the html reference contained as the last entry of Modules

```
UNABLE TO IMPORT MODULE
```


...

and I just did it again on a brand new clone from sage 4.1.1.rc2; importing only this patch; doing sage -b (which went all fine) and then sage -docbuild reference html gives me the same warning as before, namely


```
chrigu`@`linux-ljo8:~/sage/trac_spell> sage -docbuild reference html
Warning: could not import sage.modules.fg_pid.fgp_morphism        
cannot import name FGP_Morphism                                   
sphinx-build -b html -d /usr/local/sage/devel/sage/doc/output/doctrees/en/reference   .  /usr/local/sage/devel/sage/doc/output/html/en/reference                                                                                                                          
Sphinx v0.5.1, building html                                                                                                         
loading pickled environment... done                                                                                                  
building [html]: targets for 0 source files that are out of date                                                                     
updating environment: 0 added, 617 changed, 0 removed                                                                                
reading sources... algebras etc
```


Am I doing something wrong ?


---

Attachment

based on Sage 4.1.1.rc2


---

Comment by mvngu created at 2009-08-12 15:23:07

Here I start again, outlining specific steps so that we are in sync on what's going on.
 * I took the sage.math binary of Sage 4.1.1.rc2, uncompressed it and ran it:
 {{{
[mvngu`@`sage mvngu]$ pwd
/scratch/mvngu
[mvngu`@`sage mvngu]$ tar -zxf /home/mvngu/release/sage-4.1.1.rc2-sage.math.washington.edu-x86_64-Linux.tar.gz -C .
[mvngu`@`sage mvngu]$ cd sage-4.1.1.rc2-sage.math.washington.edu-x86_64-Linux/
[mvngu`@`sage sage-4.1.1.rc2-sage.math.washington.edu-x86_64-Linux]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
The Sage install tree may have moved.
Regenerating Python.pyo and .pyc files that hardcode the install PATH
(please wait at most a few minutes)...
Do not interrupt this.
sage: exit
Exiting SAGE (CPU time 0m0.08s, Wall time 0m2.80s).
Exiting spawned Gap process.
[mvngu`@`sage sage-4.1.1.rc2-sage.math.washington.edu-x86_64-Linux]$ ./sage -b main
<more output messages>
 }}}
 * With this clean slate, the content of the file `modules.rst` should be as follows:
 {{{
[mvngu`@`sage sage-4.1.1.rc2-sage.math.washington.edu-x86_64-Linux]$ cd devel/sage-main/
[mvngu`@`sage sage-main]$ cat doc/en/reference/modules.rst 
.. _ch:modules:
| Sage Version 4.1.1.rc2, Release Date: 2009-08-06                   |
| Type notebook() for the GUI, and license() for information.        |
Modules
=======

.. toctree::
   :maxdepth: 2

   sage/modules/module
   sage/modules/free_module
   sage/modules/free_module_element

   sage/modules/complex_double_vector
   sage/modules/real_double_vector
   
   sage/modules/free_module_homspace
   sage/modules/free_module_morphism
   
   sage/modules/matrix_morphism

   sage/modules/fg_pid/fgp_module
   sage/modules/fg_pid/fgp_element
   sage/modules/fg_pid/fgp_morphism
 }}}
 * Now I merge the patches at #6723, #6731, and #6724 (in that order) using Mercurial queue:
 {{{
[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6723/trac_6723-spell-check-modular.patch && hg qpush
adding trac_6723-spell-check-modular.patch to series file
applying trac_6723-spell-check-modular.patch
Now at: trac_6723-spell-check-modular.patch
[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6731/trac_6731-spell-check-schemes.patch && hg qpush
adding trac_6731-spell-check-schemes.patch to series file
applying trac_6731-spell-check-schemes.patch
Now at: trac_6731-spell-check-schemes.patch
[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6724/trac_6724-spell-check-modules.patch && hg qpush
adding trac_6724-spell-check-modules.patch to series file
applying trac_6724-spell-check-modules.patch
Now at: trac_6724-spell-check-modules.patch
 }}}
 * The content of the file `modules.rst` should not and have not been changed because the patches at #6723, #6731, and #6724 don't touch that file at all. This file controls what goes into the section on modules of the the built reference manual.
 {{{
[mvngu`@`sage sage-main]$ cat doc/en/reference/modules.rst 
.. _ch:modules:

Modules
=======

.. toctree::
   :maxdepth: 2

   sage/modules/module
   sage/modules/free_module
   sage/modules/free_module_element

   sage/modules/complex_double_vector
   sage/modules/real_double_vector
   
   sage/modules/free_module_homspace
   sage/modules/free_module_morphism
   
   sage/modules/matrix_morphism

   sage/modules/fg_pid/fgp_module
   sage/modules/fg_pid/fgp_element
   sage/modules/fg_pid/fgp_morphism
 }}}
 * I now rebuild those library files that have changed and then proceed to build the reference manual:
 {{{
[mvngu`@`sage sage-main]$ cd ../..
[mvngu`@`sage sage-4.1.1.rc2-sage.math.washington.edu-x86_64-Linux]$ ./sage -b main
<compiler messages>
[mvngu`@`sage sage-4.1.1.rc2-sage.math.washington.edu-x86_64-Linux]$ ./sage -docbuild reference html
<output messages>
 }}}
 * The only warnings I see are those relating to bad ReST formatting in `sage/graphs/graph.py`:
 {{{
WARNING: /scratch/mvngu/sage-4.1.1.rc2-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.GenericGraph.kirchhoff_matrix:56: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sage-4.1.1.rc2-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.GenericGraph.laplacian_matrix:56: (WARNING/2) Literal block ends without a blank line; unexpected unindent.
WARNING: /scratch/mvngu/sage-4.1.1.rc2-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/graphs/graph.py:docstring of sage.graphs.graph.Graph.clique_number:19: (WARNING/2) Inline literal start-string without end-string.
 }}}
 But this can be resolved with the patch at #6684.
 * If after following the steps above and you still get the same warnings you reported above, you might instead want to apply the patch `trac_6724-spell-check-modules-reduced.patch`. It's a reduced version of the patch `trac_6724-spell-check-modules.patch` with the following hunk removed:
 {{{
diff -r 87b600f2b8d5 -r e457c012dba6 sage/modules/fg_pid/fgp_morphism.py
--- a/sage/modules/fg_pid/fgp_morphism.py
+++ b/sage/modules/fg_pid/fgp_morphism.py
`@``@` -441,7 +441,7 `@``@`
             raise ValueError, "no lift of element to domain"
 
         # Write back in terms of rows of B, and delete rows not corresponding to A,
-        # since those coresponding to relations
+        # since those corresponding to relations
         v = (z*U)[:A.nrows()]
 
         # Take the linear combination that v defines.
 }}}


---

Comment by wuthrich created at 2009-08-12 15:49:25

Sorry, I noticed only now, that I have the same problem in without the patch. Everything looks like in your case except that the title of the file is changed.... I will download from scratch and see if I can get it to work.

Since I won't object any more if someone else gives a positive review I change the summary back; maybe someone else will be faster than me.


---

Comment by mpatel created at 2009-08-14 07:58:07

Both patches (separately) work for me.


---

Comment by mvngu created at 2009-08-14 08:10:10

Merged only `trac_6724-spell-check-modules.patch`.


---

Comment by mvngu created at 2009-08-14 08:10:10

Resolution: fixed
