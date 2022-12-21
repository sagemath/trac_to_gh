# Issue 433: Add -version, -root, and -branch for printing version, SAGE_ROOT, and branch information.

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2007-08-16 20:06:59

Assignee: was

Keywords: version root branch

*Add -version, -root, and -branch for printing version, SAGE_ROOT, and branch information.

Useful from the command line.

Version information is taken from sage-banner; I would prefer it to be taken from the mercurial tags, but these are not kept updated.

The root information is taken from the environment via sage-env.

The branch information is taken from readlink SAGE_ROOT/devel/sage.

mero:~/sage/local/bin ncalexan$ sage -v
SAGE Version 2.8, Release Date: 2007-08-12

mero:~/sage/local/bin ncalexan$ sage -version
SAGE Version 2.8, Release Date: 2007-08-12

mero:~/sage/local/bin ncalexan$ sage -branch
nca

mero:~/sage/local/bin ncalexan$ sage -root
/Users/ncalexan/sage


---

Comment by ncalexan created at 2007-08-16 20:10:03

This thing won't let me attach a bundle, so here's the text of the trivial patch.


```
# HG changeset patch
# User Nick Alexander <ncalexander`@`gmail.com>
# Date 1187292085 25200
# Node ID da40e197fbefada36d098a0c449e65c3622387e1
# Parent  840d064e20ea5bdbce4f71bb5ea5af07025d6f1b
Add -version, -root, and -branch for printing version, SAGE_ROOT, and branch information.

diff -r 840d064e20ea -r da40e197fbef sage-sage
--- a/sage-sage Sun Aug 12 18:17:20 2007 -0700
+++ b/sage-sage Thu Aug 16 12:21:25 2007 -0700
`@``@` -6,6 +6,7 `@``@` usage() {
     echo "-----------------------------------------------------------"
     echo " Optional arguments:"
     echo "  -h            -- print this help message"
+    echo "  -v, -version  -- print the SAGE version"
     echo "  -notebook [options] -- start the SAGE notebook (options are"
     echo "                   the same as to the notebook command in SAGE)"
     echo "  -inotebook [options] -- start the *insecure* SAGE notebook "
`@``@` -32,6 +33,7 `@``@` usage_advanced() {
     echo "  -ba [branch]  -- switch to, rebuild all Cython code, and run SAGE branch in devel/sage-branch"
     echo "  -ba-force [branch] -- same as -ba, but don't query before rebuilding"
     echo "  -bdist VER    -- build a binary distribution of SAGE"
+    echo "  -branch       -- print the current SAGE branch"
     echo "  -cleaner      -- run the SAGE cleaner"
     echo "  -clisp [...]  -- run Common Lisp"
     echo "  -clone [new branch] -- clone and run a new branch of the SAGE library from current branch"
`@``@` -62,6 +64,7 `@``@` usage_advanced() {
     echo "  -preparse <file.sage> -- produce corresponding file.sage.py "
     echo "  -python       -- run the python interpreter"
     echo "  -q            -- quiet; start with no banner"
+    echo "  -root         -- print the SAGE root directory"
     echo "  -sdist VER    -- build a source distribution of SAGE"
     echo "  -singular <..>-- run SAGE's singular with given arguments"
     echo "  -twistd <..>  -- run Twisted server"
`@``@` -203,6 +206,25 `@``@` fi
 fi
 
 #####################################################################
+# Report information about the SAGE environment
+#####################################################################
+
+if [ $1 = '-v' -o $1 = '-version' ]; then
+    cat "$SAGE_LOCAL/bin/sage-banner" | grep -i "version" | sed "s/\| //" | sed "s/ *\|//"
+    exit $?
+fi
+
+if [ $1 = '-root' ]; then
+    echo "$SAGE_ROOT"
+    exit 0
+fi
+
+if [ $1 = '-branch' ]; then
+    readlink "$SAGE_ROOT/devel/sage" | sed "s/sage-//"
+    exit $?
+fi
+
+#####################################################################
 # Run SAGE's versions of the standard Algebra/Geometry etc. software
 #####################################################################
```



---

Comment by ncalexan created at 2007-08-17 06:02:31

Changing type from defect to enhancement.


---

Comment by ncalexan created at 2007-08-18 19:40:31

Bundle at

http://sage.math.washington.edu/home/ncalexan/patches/ncalexan-version-branch-root.hg


---

Comment by ncalexan created at 2007-08-18 19:40:31

Changing assignee from was to ncalexan.


---

Comment by was created at 2007-08-19 00:47:08

Resolution: fixed
