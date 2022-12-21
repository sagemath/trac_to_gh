# Issue 411: sage_c_lib moved into primary sage tree

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2007-08-09 02:26:12

Assignee: was

CC:  dmharvey@math.harvard.edu

The attached mercurial bundle has the c_lib moved into the tree and some other enhancements as well:

1)  Many modifications to .hgignore to make it ignore c_lib junk and keep it from ignore .h files and .c files only under sage/
2)  setup.py misc improvements
3)  setup.py checks for recursive dependencies on .pyx files.  So if you have a deep includes -- i.e. a .pxi included from a .pxi, it will now include this in the age comparisons.  Unfortunately, this approximately doubles the time on a no-op build.  I don't know what other people think about this, but I'm rather freakish about knowing that my builds are reliable so I think it is worth it.




---

Comment by jbmohler created at 2007-08-09 02:27:16

Mercurial bundle


---

Attachment


---

Comment by jbmohler created at 2007-08-28 18:50:27

Conversion to using SCons and integrated c_lib into tree


---

Attachment

Ignore the attachment c_lib_in_tree_and_setup_enhancements.hg

The attachment c_lib_into_main.patch lacks some setup_enhancements of the first patch, but it is converted to scons.

The scons-0.97.spkg from the experimental repository is needed for this patch.


---

Comment by was created at 2007-08-29 16:34:07

Changing priority from major to blocker.


---

Comment by dmharvey created at 2007-08-29 20:22:39

throw on top of c_lib_into_main.patch, fixes mysterious segfault in libsingular related to strdup()


---

Comment by was created at 2007-08-30 00:58:04

Resolution: fixed


---

Attachment

I incorporated this in.  There were some weird issues with mpz_get_pyintlong not being defined, which I fixed
by adding back some files to ext.  Fix this correctly in the future.
