# Issue 6945: [with spkg; needs review] Update readline to version 6.0

archive/issues_006945.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @williamstein\n\nThere are a number of issues associated with the readline 5.2 in Sage\n\n* #6933 (readline-5.2.p7 builds as 32-bit on Solaris even if SAGE64=yes)\n* It does not work on OS X 10.6 #6849 William has sorted these issues out. \n* grep was used on /etc/SuSE-release  - even if the file did not exist. #6844\n\nThis spkg hopes to clear them all up. Note its not the first version of readline 6.0 package I've created, hence the directory name. This is an improved version over another. \n\nIt has been tested on \n\n* 64-bit linux (sage.math)\n* Solaris 32-bit SPARC (my box)\n* Solaris 64-bit SPARC (my box)\n* OS X 32-bit (bsd.math)\n* OS X 64-bit (bsd.math)\n\nIt would be good if someone could test on Suse linux, as there are some Suse-specific bits in here. One of which I had to very slightly modify, to avoid a warning on every other platform. \n\nThis alone will not sort out all the OS X 10.6 issues (#6849), but it will allow #6933 and #6844 to be closed. \n\nThe spkg, spkg-install and SPKG.txt can be found here:\n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/readline-6.0-2nd-try/\n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/6945\n\n",
    "created_at": "2009-09-16T08:38:43Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with spkg; needs review] Update readline to version 6.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6945",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @williamstein

There are a number of issues associated with the readline 5.2 in Sage

* #6933 (readline-5.2.p7 builds as 32-bit on Solaris even if SAGE64=yes)
* It does not work on OS X 10.6 #6849 William has sorted these issues out. 
* grep was used on /etc/SuSE-release  - even if the file did not exist. #6844

This spkg hopes to clear them all up. Note its not the first version of readline 6.0 package I've created, hence the directory name. This is an improved version over another. 

It has been tested on 

* 64-bit linux (sage.math)
* Solaris 32-bit SPARC (my box)
* Solaris 64-bit SPARC (my box)
* OS X 32-bit (bsd.math)
* OS X 64-bit (bsd.math)

It would be good if someone could test on Suse linux, as there are some Suse-specific bits in here. One of which I had to very slightly modify, to avoid a warning on every other platform. 

This alone will not sort out all the OS X 10.6 issues (#6849), but it will allow #6933 and #6844 to be closed. 

The spkg, spkg-install and SPKG.txt can be found here:

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/readline-6.0-2nd-try/

Dave 

Issue created by migration from https://trac.sagemath.org/ticket/6945





---

archive/issue_comments_057315.json:
```json
{
    "body": "Added the executable flag to `spkg-install` using `chmod +x spkg-install`. These lines are suspect:\n\n```\nif [ `grep 11.1 /etc/SuSE-release > /dev/null; echo $?` == 0 ]; then\nif [ $OVERWRITE_READLINE == \"true\" ]; then\n```\n\nShould they be the following instead with only one equal sign?\n\n```\nif [ `grep 11.1 /etc/SuSE-release > /dev/null; echo $?` = 0 ]; then\nif [ $OVERWRITE_READLINE = \"true\" ]; then\n```\n\nAnyway, all changes have been committed in David Kirkby's name. The package is up at\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/readline-6.0.spkg\n\nI'm now testing it under various platforms, including openSUSE 11.1.",
    "created_at": "2009-09-17T00:01:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6945#issuecomment-57315",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Added the executable flag to `spkg-install` using `chmod +x spkg-install`. These lines are suspect:

```
if [ `grep 11.1 /etc/SuSE-release > /dev/null; echo $?` == 0 ]; then
if [ $OVERWRITE_READLINE == "true" ]; then
```

Should they be the following instead with only one equal sign?

```
if [ `grep 11.1 /etc/SuSE-release > /dev/null; echo $?` = 0 ]; then
if [ $OVERWRITE_READLINE = "true" ]; then
```

Anyway, all changes have been committed in David Kirkby's name. The package is up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/readline-6.0.spkg

I'm now testing it under various platforms, including openSUSE 11.1.



---

archive/issue_comments_057316.json:
```json
{
    "body": "Building from scratch on openSUSE 11.1 (menas on SkyNet) with drkirkby's package, I got the following compile failure:\n\n```\nOverwriting libreadline.so.6.0 with the system one\ncp: cannot stat `/lib64/libreadline.so.6.0': No such file or directory\n\nreal    1m6.544s\nuser    0m12.965s\nsys     0m4.596s\nsage: An error occurred while installing readline-6.0\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /home/mvngu/usr/menas/sandbox/sage-4.1.2.alpha1-6945-readline-cliquer/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem, yourself *don't* just cd to\n/home/mvngu/usr/menas/sandbox/sage-4.1.2.alpha1-6945-readline-cliquer/spkg/build/readline-6.0 and type 'make'.\nInstead type \"/home/mvngu/usr/menas/sandbox/sage-4.1.2.alpha1-6945-readline-cliquer/sage -sh\"\nin order to set all environment variables correctly, then cd to\n/home/mvngu/usr/menas/sandbox/sage-4.1.2.alpha1-6945-readline-cliquer/spkg/build/readline-6.0\n(When you are done debugging, you can type \"exit\" to leave the\nsubshell.)\nmake[1]: *** [installed/readline-6.0] Error 1\nmake[1]: Leaving directory `/home/mvngu/usr/menas/sandbox/sage-4.1.2.alpha1-6945-readline-cliquer/spkg'\n\nreal    1m8.134s\nuser    0m13.625s\nsys     0m4.672s\nError building Sage.\n```\n\nAn updated readline package is up at\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/readline-6.0.spkg\n\nThis package includes the following:\n\n* Check David Kirkby's changes in his name.\n\n* Fix some minor typos.\n\n* Change the line\n {{{\nif [ `grep 11.1 /etc/SuSE-release > /dev/null; echo $?` == 0 ]; then\n }}}\n to\n {{{\nif [ `grep 11.1 /etc/SuSE-release > /dev/null; echo $?` -eq 0 ]; then\n }}}\n since that conditional is a comparison of integers.\n\n* Change the line\n {{{\nif [ $OVERWRITE_READLINE == \"true\" ]; then\n }}}\n to\n {{{\nif [ $OVERWRITE_READLINE = \"true\" ]; then\n }}}",
    "created_at": "2009-09-17T02:16:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6945#issuecomment-57316",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Building from scratch on openSUSE 11.1 (menas on SkyNet) with drkirkby's package, I got the following compile failure:

```
Overwriting libreadline.so.6.0 with the system one
cp: cannot stat `/lib64/libreadline.so.6.0': No such file or directory

real    1m6.544s
user    0m12.965s
sys     0m4.596s
sage: An error occurred while installing readline-6.0
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/mvngu/usr/menas/sandbox/sage-4.1.2.alpha1-6945-readline-cliquer/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/home/mvngu/usr/menas/sandbox/sage-4.1.2.alpha1-6945-readline-cliquer/spkg/build/readline-6.0 and type 'make'.
Instead type "/home/mvngu/usr/menas/sandbox/sage-4.1.2.alpha1-6945-readline-cliquer/sage -sh"
in order to set all environment variables correctly, then cd to
/home/mvngu/usr/menas/sandbox/sage-4.1.2.alpha1-6945-readline-cliquer/spkg/build/readline-6.0
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/readline-6.0] Error 1
make[1]: Leaving directory `/home/mvngu/usr/menas/sandbox/sage-4.1.2.alpha1-6945-readline-cliquer/spkg'

real    1m8.134s
user    0m13.625s
sys     0m4.672s
Error building Sage.
```

An updated readline package is up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/readline-6.0.spkg

This package includes the following:

* Check David Kirkby's changes in his name.

* Fix some minor typos.

* Change the line
 {{{
if [ `grep 11.1 /etc/SuSE-release > /dev/null; echo $?` == 0 ]; then
 }}}
 to
 {{{
if [ `grep 11.1 /etc/SuSE-release > /dev/null; echo $?` -eq 0 ]; then
 }}}
 since that conditional is a comparison of integers.

* Change the line
 {{{
if [ $OVERWRITE_READLINE == "true" ]; then
 }}}
 to
 {{{
if [ $OVERWRITE_READLINE = "true" ]; then
 }}}



---

archive/issue_comments_057317.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2009-09-17T02:16:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6945#issuecomment-57317",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_057318.json:
```json
{
    "body": "Changing component from build to packages.",
    "created_at": "2009-09-17T02:16:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6945#issuecomment-57318",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing component from build to packages.



---

archive/issue_comments_057319.json:
```json
{
    "body": "I have been having trouble building Sage 4.1.2.alpha1 from scratch with readline 6.0 on openSUSE 11.1. The problem is due to the variable `OVERWRITE_READLINE` in `spkg-install`, which is set to true on openSUSE 11.1. That variable was introduced when the version of readline that was shipped with Sage was 5.2, which matches the readline version on openSUSE 11.1. When upgrading to readline 6.0, we no longer need that variable. I have commented out references to that variable in `spkg-install`:\n\n```\n# OVERWRITE_READLINE=false; export OVERWRITE_READLINE                           \n\n# First we check for OpenSUSE 11.1 since bash is linked dynamically with a      \n# readline that breaks when we build Sage's readline, so we work around this    \n# for now.                                                                      \n\nif [ -f /etc/SuSE-release ]; then\n    if [ `grep 11.1 /etc/SuSE-release > /dev/null; echo $?` -eq 0 ]; then\n        echo \"OpenSUSE 11.1 detected\"\n        if [ -d /usr/include/readline/ ]; then\n            echo \"The development version of libreadline is installed -> copying\"\n            if [ `uname -p` = \"x86_64\" ]; then\n                cp /lib64/libreadline.so.* $SAGE_LOCAL/lib\n            else\n                cp /lib/libreadline.so.* $SAGE_LOCAL/lib\n            fi\n            cp -r /usr/include/readline  $SAGE_LOCAL/include\n            exit 0\n        else\n            echo \"No headers found, building library.\"\n            # # This variable is only set to \"true\" on openSUSE 11.1.           \n            # OVERWRITE_READLINE=\"true\"; export OVERWRITE_READLINE              \n        fi\n    fi\nfi\n\n<SNIP>\n\n# # We only enter this block on openSUSE 11.1.                                  \n# if [ $OVERWRITE_READLINE = \"true\" ]; then                                     \n#   echo \"Overwriting libreadline.so.6.0 with the system one.\"                  \n#   rm -f $SAGE_LOCAL/lib/libreadline.so.6.0                                    \n#   if [ `uname -p` = \"x86_64\" ]; then                                          \n#     cp /lib64/libreadline.so.* $SAGE_LOCAL/lib                                \n#   else                                                                        \n#     cp /lib/libreadline.so.* $SAGE_LOCAL/lib                                  \n#   fi                                                                          \n# fi\n```\n\nAn updated package with the above changes is up at\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/readline-6.0.spkg",
    "created_at": "2009-09-17T04:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6945#issuecomment-57319",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I have been having trouble building Sage 4.1.2.alpha1 from scratch with readline 6.0 on openSUSE 11.1. The problem is due to the variable `OVERWRITE_READLINE` in `spkg-install`, which is set to true on openSUSE 11.1. That variable was introduced when the version of readline that was shipped with Sage was 5.2, which matches the readline version on openSUSE 11.1. When upgrading to readline 6.0, we no longer need that variable. I have commented out references to that variable in `spkg-install`:

```
# OVERWRITE_READLINE=false; export OVERWRITE_READLINE                           

# First we check for OpenSUSE 11.1 since bash is linked dynamically with a      
# readline that breaks when we build Sage's readline, so we work around this    
# for now.                                                                      

if [ -f /etc/SuSE-release ]; then
    if [ `grep 11.1 /etc/SuSE-release > /dev/null; echo $?` -eq 0 ]; then
        echo "OpenSUSE 11.1 detected"
        if [ -d /usr/include/readline/ ]; then
            echo "The development version of libreadline is installed -> copying"
            if [ `uname -p` = "x86_64" ]; then
                cp /lib64/libreadline.so.* $SAGE_LOCAL/lib
            else
                cp /lib/libreadline.so.* $SAGE_LOCAL/lib
            fi
            cp -r /usr/include/readline  $SAGE_LOCAL/include
            exit 0
        else
            echo "No headers found, building library."
            # # This variable is only set to "true" on openSUSE 11.1.           
            # OVERWRITE_READLINE="true"; export OVERWRITE_READLINE              
        fi
    fi
fi

<SNIP>

# # We only enter this block on openSUSE 11.1.                                  
# if [ $OVERWRITE_READLINE = "true" ]; then                                     
#   echo "Overwriting libreadline.so.6.0 with the system one."                  
#   rm -f $SAGE_LOCAL/lib/libreadline.so.6.0                                    
#   if [ `uname -p` = "x86_64" ]; then                                          
#     cp /lib64/libreadline.so.* $SAGE_LOCAL/lib                                
#   else                                                                        
#     cp /lib/libreadline.so.* $SAGE_LOCAL/lib                                  
#   fi                                                                          
# fi
```

An updated package with the above changes is up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/readline-6.0.spkg



---

archive/issue_comments_057320.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-17T22:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6945#issuecomment-57320",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_007169.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-17T22:01:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6945",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6945#event-7169"
}
```



---

archive/issue_comments_057321.json:
```json
{
    "body": "I tested the updated readline package on the following platforms:\n\n* sage.math: x86_64 Ubuntu 8.04.3 --- compiles OK; the following doctest failed:\n {{{\nsage -t -long \"devel/sage/sage/graphs/graph_bundle.py\"      \nlibpng error: Image width or height is zero in IHDR\n**********************************************************************\nFile \"/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/graphs/graph_bundle.py\", line 163:\n    sage: B.plot()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_5[5]>\", line 1, in <module>\n        B.plot()###line 163:\n    sage: B.plot()\n      File \"sage_object.pyx\", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1387)\n      File \"/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/plot/plot.py\", line 876, in _repr_\n        self.show()\n      File \"/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/plot/plot.py\", line 1398, in show\n        self.save(DOCTEST_MODE_FILE, **options)\n      File \"/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/plot/plot.py\", line 1939, in save\n        figure.savefig(filename,dpi=dpi,bbox_inches='tight',**options)\n      File \"/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/matplotlib/figure.py\", line 1033, in savefig\n        self.canvas.print_figure(*args, **kwargs)\n      File \"/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/matplotlib/backend_bases.py\", line 1455, in print_figure\n        **kwargs)\n      File \"/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/matplotlib/backends/backend_agg.py\", line 366, in print_png\n        filename_or_obj, self.figure.dpi)\n    RuntimeError: Error building image\n**********************************************************************\n1 items had failures:\n   1 of   6 in __main__.example_5\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/sage-4.1.2.alpha1-6945-readline/tmp/.doctest_graph_bundle.py\n         [2.2 s]\n }}}\n It passes on another try.\n\n\n* bsd.math 32-bit: Mac OS X 10.5.8 --- compiles OK; the following doctest failed:\n {{{\nsage -t -long \"dline-cliquer/devel/sage/doc/en/bordeaux_2008/birds_other.rst\"\nA mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.\n         [28.8 s]\n }}}\n which passes on another try.\n\n\n* bsd.math 64-bit mode: Mac OS X 10.5.8 --- compiles OK; the following doctest failed:\n {{{\nsage -t -long \"fort-cliq-ecl/devel/sage/sage/interfaces/maxima.py\"\n**********************************************************************\nFile \"/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-6945-readline-fort-cliq-ecl/devel/sage/sage/interfaces/maxima.py\", line 2108:\n    sage: list(v)\nExpected:\n    [0, x, 2*x^2, 3*x^3, 4*x^4, 5*x^5]\nGot:\n    [0, x, , 3*x^3, 4*x^4, 5*x^5]\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_64\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-6945-readline-fort-cliq-ecl/tmp/.doctest_maxima.py\n         [18.3 s]\n }}}\n which can be fixed by the patch at #6883.\n\n* eno: x86_64 Fedora 9 with GCC 4.4.1 --- compiles OK; the following doctest failed:\n {{{\nsage -t -long \"devel/sage/sage/rings/polynomial/polynomial_ring_constructor.py\"\nA mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.\n         [1.2 s]\n }}}\n which passed on another try.\n\n\n* cicero: 32-bit Fedora 9 with GCC 4.4.1 --- compiles OK; the following doctests failed:\n {{{\nsage -t -long \"devel/sage/sage/misc/randstate.pyx\"          \n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/misc/randstate.pyx\", line 124:\n    : s = ZZ(subsage('initial_seed()'))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[32]>\", line 1, in <module>\n        s = ZZ(subsage('initial_seed()'))###line 124:\n    : s = ZZ(subsage('initial_seed()'))\n      File \"parent.pyx\", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4171)\n      File \"coerce_maps.pyx\", line 156, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4064)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1726, in _integer_\n        return sage.rings.all.Integer(repr(self))\n      File \"integer.pyx\", line 564, in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6399)\n    TypeError: unable to convert x (=---------------------------------------------------------------------------\n    AttributeError                            Traceback (most recent call last)\n\n    /home/mvngu/.sage/temp/cicero/21500/_home_mvngu__sage_init_sage_0.py in <module>()\n\n    /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python2.6/site-packages/sage/misc/functional.pyc in gen(x)\n        353     Return the generator of x.\n        354     \"\"\"\n    --> 355     return x.gen()\n        356 \n        357 def gens(x):\n\n    AttributeError: 'int' object has no attribute 'gen') to an integer\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/misc/randstate.pyx\", line 131:\n    : r == ZZ.random_element(2^200)\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n1 items had failures:\n   2 of  62 in __main__.example_0\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/tmp/.doctest_randstate.py\n\t [21.4 s]\n\n<SNIP>\n\nsage -t -long \"devel/sage/sage/interfaces/expect.py\"        \n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/expect.py\", line 805:\n    sage: print sage0.eval(\"alarm(1); singular._expect_expr('1')\")\nExpected:\n    Control-C pressed.  Interrupting Singular. Please wait a few seconds...\n    ...\n    KeyboardInterrupt: computation timed out because alarm was set for 1 seconds\nGot:\n    \ufffd[0m\n**********************************************************************\n1 items had failures:\n   1 of  10 in __main__.example_15\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/tmp/.doctest_expect.py\n\t [16.5 s]\n\n<SNIP>\n\nsage -t -long \"devel/sage/sage/interfaces/sage0.py\"         \n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 55:\n    sage: a^3\nExpected:\n    8\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 62:\n    sage: V.gens()\nExpected:\n    ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 75:\n    sage: g = V.0;  g\nExpected:\n    (1, 0, 0, 0)\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 85:\n    sage: s('%s.parent()'%g.name())\nExpected:\n    Vector space of dimension 4 over Rational Field\nGot:\n    (1, 0, 0, 0)\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 93:\n    sage: s('x = 5')\nExpected:\n    5\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 97:\n    sage: s('x')\nExpected:\n    5\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 105:\n    sage: a\nExpected:\n    10\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 114:\n    sage: s3('\"x\"')\nExpected:\n    8\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 116:\n    sage: s('x')\nExpected:\n    5\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 320:\n    sage: sage0.eval('2+2')\nExpected:\n    '4'\nGot:\n    '\\x1b[0m'\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 334:\n    sage: sage0.get('x')\nExpected:\n    '2'\nGot:\n    '4'\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 364:\n    sage: sage0.get('x')\nExpected:\n    \"...NameError: name 'x' is not defined\"\nGot:\n    '2'\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 373:\n    sage: sage0._contains('2', 'QQ')\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 397:\n    sage: sage0.version()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_16[2]>\", line 1, in <module>\n        sage0.version()###line 397:\n    sage: sage0.version()\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/interfaces/sage0.py\", line 402, in version\n        return sage0_version()\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/interfaces/sage0.py\", line 547, in sage0_version\n        return str(sage0('version()'))\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/interfaces/sage0.py\", line 263, in __call__\n        return SageElement(self, x)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1433, in __init__\n        raise TypeError, x\n    TypeError: Error executing code in Sage\n    CODE:\n    \tsage0=version()\n    Sage ERROR:\n    \t---------------------------------------------------------------------------\n    NameError                                 Traceback (most recent call last)\n\n    /home/mvngu/.sage/temp/cicero/16032/_home_mvngu__sage_init_sage_0.py in <module>()\n\n    NameError: name 'x' is not defined\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 399:\n    sage: sage0.version() == version()\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 417:\n    sage: sage0.new(2)\nExpected:\n    2\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 445:\n    sage: F == sage0(F)._sage_()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_20[4]>\", line 1, in <module>\n        F == sage0(F)._sage_()###line 445:\n    sage: F == sage0(F)._sage_()\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/interfaces/sage0.py\", line 455, in _sage_\n        return load(P._local_tmpfile())\n      File \"sage_object.pyx\", line 529, in sage.structure.sage_object.load (sage/structure/sage_object.c:6504)\n    IOError: [Errno 2] No such file or directory: '/home/mvngu/.sage//temp/cicero/15862//interface//tmp15862.sobj'\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 463:\n    sage: four_gcd(6)\nExpected:\n    2\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 486:\n    sage: sage0(4).gcd\nExpected:\n    <built-in method gcd of sage.rings.integer.Integer object at 0x...>\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 512:\n    sage: half = reduce_load_element(s); half\nExpected:\n    1/2\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 544:\n    sage: sage0_version() == version()\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 174:\n    sage: print \"ignore this\";  sage0.cputime()     # random output\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[2]>\", line 1, in <module>\n        print \"ignore this\";  sage0.cputime()     # random output###line 174:\n    sage: print \"ignore this\";  sage0.cputime()     # random output\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/interfaces/sage0.py\", line 185, in cputime\n        return float(s)\n    ValueError: invalid literal for float(): Sage Version 4.1.2.alpha1, Release Date: 2009-09-07\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 176:\n    sage: sage0('factor(2^157-1)')\nExpected:\n    852133201 * 60726444167 * 1654058017289 * 2134387368610417\nGot:\n    5.0832259999999998\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 178:\n    sage: print \"ignore this\";  sage0.cputime()     # random output\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[4]>\", line 1, in <module>\n        print \"ignore this\";  sage0.cputime()     # random output###line 178:\n    sage: print \"ignore this\";  sage0.cputime()     # random output\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/interfaces/sage0.py\", line 185, in cputime\n        return float(s)\n    ValueError: empty string for float()\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 192:\n    sage: len(t) > 100\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[3]>\", line 1, in <module>\n        len(t) > Integer(100)###line 192:\n    sage: len(t) > 100\n    TypeError: object of type 'long' has no len()\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 194:\n    sage: 'gcd' in t\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[4]>\", line 1, in <module>\n        'gcd' in t###line 194:\n    sage: 'gcd' in t\n    TypeError: argument of type 'long' is not iterable\n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py\", line 204:\n    sage: s.eval('2+2')\nExpected:\n    '4'\nGot:\n    '\\x1b[0m'\n**********************************************************************\n15 items had failures:\n   9 of  23 in __main__.example_1\n   1 of   3 in __main__.example_10\n   1 of   4 in __main__.example_11\n   1 of   6 in __main__.example_13\n   1 of   3 in __main__.example_14\n   2 of   4 in __main__.example_16\n   1 of   4 in __main__.example_18\n   1 of   5 in __main__.example_20\n   1 of   4 in __main__.example_21\n   1 of   3 in __main__.example_22\n   1 of   6 in __main__.example_24\n   1 of   4 in __main__.example_26\n   3 of   5 in __main__.example_3\n   2 of   5 in __main__.example_4\n   1 of   5 in __main__.example_5\n***Test Failed*** 27 failures.\nFor whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/tmp/.doctest_sage0.py\n\t [27.4 s]\n\n<SNIP>\n\nsage -t -long \"devel/sage/sage/server/simple/twist.py\"      \n**********************************************************************\nFile \"/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/server/simple/twist.py\", line 51:\n    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))\nExpected:\n    {\n    \"status\": \"done\",\n    \"files\": [],\n    \"cell_id\": 1\n    }\n    ___S_A_G_E___\n    4\nGot:\n    {\n    \"status\": \"computing\",\n    \"files\": [],\n    \"cell_id\": 1\n    }\n    ___S_A_G_E___\n    <BLANKLINE>\n**********************************************************************\n1 items had failures:\n   1 of  24 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/tmp/.doctest_twist.py\n\t [18.3 s]\n }}}\n \n\n* lena: x86_64 RHEL 5.3 with GCC 4.4.1 --- compiles OK; all doctests pass.\n\n\n* opensuse32 virtualized guest on boxen.math: 32-bit openSUSE 11.1 --- compiles OK; all doctests pass.\n\n\n* opensuse64 virtualized guest on boxen.math: x86_64 openSUSE 11.1 --- compiles OK; all doctests pass.\n\n\n* menas: x86_64 openSUSE 11.1 with GCC 4.4.1 --- compiles OK but must be built together with the cliquer package at #6681; all doctests pass.\n\n\n* t2.math: SPARC Solaris with GCC 4.4.1 and Sun linker --- compiles OK. I can't run any doctests since Sage currently doesn't build completely on t2.math. The compilation now dies with this error message:\n {{{\n/bin/sh: ../.././install-sh: not found\nmake[3]: [install-libsingular] Error 1 (ignored)\n../.././install-sh -c kInline.cc /scratch/mvngu/sage-4.1.2.alpha1-6945-readline-cliquer-ecl/local/include/singular\nmake[3]: ../.././install-sh: Command not found\nmake[3]: *** [install-libsingular] Error 127\nmake[3]: Leaving directory `/scratch/mvngu/sage-4.1.2.alpha1-6945-readline-cliquer-ecl/spkg/build/singular-3-1-0-4-20090818/src/kernel'\nmake[2]: *** [install-libsingular] Error 2\nmake[2]: Leaving directory `/scratch/mvngu/sage-4.1.2.alpha1-6945-readline-cliquer-ecl/spkg/build/singular-3-1-0-4-20090818/src'\nUnable to install libsingular.\n\nreal    49m13.554s\nuser    46m0.079s\nsys     2m44.988s\nsage: An error occurred while installing singular-3-1-0-4-20090818\n }}}\n Ticket #6951 tracks this issue.\n\n\nAs far as I'm concerned, it's a positive review from me. Merged readline-6.0.spkg in the standard packages repository.",
    "created_at": "2009-09-17T22:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6945",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6945#issuecomment-57321",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I tested the updated readline package on the following platforms:

* sage.math: x86_64 Ubuntu 8.04.3 --- compiles OK; the following doctest failed:
 {{{
sage -t -long "devel/sage/sage/graphs/graph_bundle.py"      
libpng error: Image width or height is zero in IHDR
**********************************************************************
File "/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/graphs/graph_bundle.py", line 163:
    sage: B.plot()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[5]>", line 1, in <module>
        B.plot()###line 163:
    sage: B.plot()
      File "sage_object.pyx", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1387)
      File "/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/plot/plot.py", line 876, in _repr_
        self.show()
      File "/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/plot/plot.py", line 1398, in show
        self.save(DOCTEST_MODE_FILE, **options)
      File "/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/plot/plot.py", line 1939, in save
        figure.savefig(filename,dpi=dpi,bbox_inches='tight',**options)
      File "/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/matplotlib/figure.py", line 1033, in savefig
        self.canvas.print_figure(*args, **kwargs)
      File "/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/matplotlib/backend_bases.py", line 1455, in print_figure
        **kwargs)
      File "/scratch/mvngu/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/matplotlib/backends/backend_agg.py", line 366, in print_png
        filename_or_obj, self.figure.dpi)
    RuntimeError: Error building image
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/sage-4.1.2.alpha1-6945-readline/tmp/.doctest_graph_bundle.py
         [2.2 s]
 }}}
 It passes on another try.


* bsd.math 32-bit: Mac OS X 10.5.8 --- compiles OK; the following doctest failed:
 {{{
sage -t -long "dline-cliquer/devel/sage/doc/en/bordeaux_2008/birds_other.rst"
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [28.8 s]
 }}}
 which passes on another try.


* bsd.math 64-bit mode: Mac OS X 10.5.8 --- compiles OK; the following doctest failed:
 {{{
sage -t -long "fort-cliq-ecl/devel/sage/sage/interfaces/maxima.py"
**********************************************************************
File "/Volumes/LACIE/scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-6945-readline-fort-cliq-ecl/devel/sage/sage/interfaces/maxima.py", line 2108:
    sage: list(v)
Expected:
    [0, x, 2*x^2, 3*x^3, 4*x^4, 5*x^5]
Got:
    [0, x, , 3*x^3, 4*x^4, 5*x^5]
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_64
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/sandbox-64/sage-4.1.2.alpha1-6945-readline-fort-cliq-ecl/tmp/.doctest_maxima.py
         [18.3 s]
 }}}
 which can be fixed by the patch at #6883.

* eno: x86_64 Fedora 9 with GCC 4.4.1 --- compiles OK; the following doctest failed:
 {{{
sage -t -long "devel/sage/sage/rings/polynomial/polynomial_ring_constructor.py"
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [1.2 s]
 }}}
 which passed on another try.


* cicero: 32-bit Fedora 9 with GCC 4.4.1 --- compiles OK; the following doctests failed:
 {{{
sage -t -long "devel/sage/sage/misc/randstate.pyx"          
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/misc/randstate.pyx", line 124:
    : s = ZZ(subsage('initial_seed()'))
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[32]>", line 1, in <module>
        s = ZZ(subsage('initial_seed()'))###line 124:
    : s = ZZ(subsage('initial_seed()'))
      File "parent.pyx", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4171)
      File "coerce_maps.pyx", line 156, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4064)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/interfaces/expect.py", line 1726, in _integer_
        return sage.rings.all.Integer(repr(self))
      File "integer.pyx", line 564, in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6399)
    TypeError: unable to convert x (=---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)

    /home/mvngu/.sage/temp/cicero/21500/_home_mvngu__sage_init_sage_0.py in <module>()

    /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python2.6/site-packages/sage/misc/functional.pyc in gen(x)
        353     Return the generator of x.
        354     """
    --> 355     return x.gen()
        356 
        357 def gens(x):

    AttributeError: 'int' object has no attribute 'gen') to an integer
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/misc/randstate.pyx", line 131:
    : r == ZZ.random_element(2^200)
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   2 of  62 in __main__.example_0
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/tmp/.doctest_randstate.py
	 [21.4 s]

<SNIP>

sage -t -long "devel/sage/sage/interfaces/expect.py"        
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/expect.py", line 805:
    sage: print sage0.eval("alarm(1); singular._expect_expr('1')")
Expected:
    Control-C pressed.  Interrupting Singular. Please wait a few seconds...
    ...
    KeyboardInterrupt: computation timed out because alarm was set for 1 seconds
Got:
    �[0m
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_15
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/tmp/.doctest_expect.py
	 [16.5 s]

<SNIP>

sage -t -long "devel/sage/sage/interfaces/sage0.py"         
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 55:
    sage: a^3
Expected:
    8
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 62:
    sage: V.gens()
Expected:
    ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 75:
    sage: g = V.0;  g
Expected:
    (1, 0, 0, 0)
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 85:
    sage: s('%s.parent()'%g.name())
Expected:
    Vector space of dimension 4 over Rational Field
Got:
    (1, 0, 0, 0)
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 93:
    sage: s('x = 5')
Expected:
    5
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 97:
    sage: s('x')
Expected:
    5
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 105:
    sage: a
Expected:
    10
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 114:
    sage: s3('"x"')
Expected:
    8
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 116:
    sage: s('x')
Expected:
    5
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 320:
    sage: sage0.eval('2+2')
Expected:
    '4'
Got:
    '\x1b[0m'
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 334:
    sage: sage0.get('x')
Expected:
    '2'
Got:
    '4'
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 364:
    sage: sage0.get('x')
Expected:
    "...NameError: name 'x' is not defined"
Got:
    '2'
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 373:
    sage: sage0._contains('2', 'QQ')
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 397:
    sage: sage0.version()
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_16[2]>", line 1, in <module>
        sage0.version()###line 397:
    sage: sage0.version()
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/interfaces/sage0.py", line 402, in version
        return sage0_version()
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/interfaces/sage0.py", line 547, in sage0_version
        return str(sage0('version()'))
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/interfaces/sage0.py", line 263, in __call__
        return SageElement(self, x)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/interfaces/expect.py", line 1433, in __init__
        raise TypeError, x
    TypeError: Error executing code in Sage
    CODE:
    	sage0=version()
    Sage ERROR:
    	---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)

    /home/mvngu/.sage/temp/cicero/16032/_home_mvngu__sage_init_sage_0.py in <module>()

    NameError: name 'x' is not defined
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 399:
    sage: sage0.version() == version()
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 417:
    sage: sage0.new(2)
Expected:
    2
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 445:
    sage: F == sage0(F)._sage_()
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_20[4]>", line 1, in <module>
        F == sage0(F)._sage_()###line 445:
    sage: F == sage0(F)._sage_()
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/interfaces/sage0.py", line 455, in _sage_
        return load(P._local_tmpfile())
      File "sage_object.pyx", line 529, in sage.structure.sage_object.load (sage/structure/sage_object.c:6504)
    IOError: [Errno 2] No such file or directory: '/home/mvngu/.sage//temp/cicero/15862//interface//tmp15862.sobj'
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 463:
    sage: four_gcd(6)
Expected:
    2
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 486:
    sage: sage0(4).gcd
Expected:
    <built-in method gcd of sage.rings.integer.Integer object at 0x...>
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 512:
    sage: half = reduce_load_element(s); half
Expected:
    1/2
Got:
    <BLANKLINE>
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 544:
    sage: sage0_version() == version()
Expected:
    True
Got:
    False
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 174:
    sage: print "ignore this";  sage0.cputime()     # random output
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[2]>", line 1, in <module>
        print "ignore this";  sage0.cputime()     # random output###line 174:
    sage: print "ignore this";  sage0.cputime()     # random output
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/interfaces/sage0.py", line 185, in cputime
        return float(s)
    ValueError: invalid literal for float(): Sage Version 4.1.2.alpha1, Release Date: 2009-09-07
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 176:
    sage: sage0('factor(2^157-1)')
Expected:
    852133201 * 60726444167 * 1654058017289 * 2134387368610417
Got:
    5.0832259999999998
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 178:
    sage: print "ignore this";  sage0.cputime()     # random output
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[4]>", line 1, in <module>
        print "ignore this";  sage0.cputime()     # random output###line 178:
    sage: print "ignore this";  sage0.cputime()     # random output
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/lib/python/site-packages/sage/interfaces/sage0.py", line 185, in cputime
        return float(s)
    ValueError: empty string for float()
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 192:
    sage: len(t) > 100
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        len(t) > Integer(100)###line 192:
    sage: len(t) > 100
    TypeError: object of type 'long' has no len()
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 194:
    sage: 'gcd' in t
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[4]>", line 1, in <module>
        'gcd' in t###line 194:
    sage: 'gcd' in t
    TypeError: argument of type 'long' is not iterable
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/interfaces/sage0.py", line 204:
    sage: s.eval('2+2')
Expected:
    '4'
Got:
    '\x1b[0m'
**********************************************************************
15 items had failures:
   9 of  23 in __main__.example_1
   1 of   3 in __main__.example_10
   1 of   4 in __main__.example_11
   1 of   6 in __main__.example_13
   1 of   3 in __main__.example_14
   2 of   4 in __main__.example_16
   1 of   4 in __main__.example_18
   1 of   5 in __main__.example_20
   1 of   4 in __main__.example_21
   1 of   3 in __main__.example_22
   1 of   6 in __main__.example_24
   1 of   4 in __main__.example_26
   3 of   5 in __main__.example_3
   2 of   5 in __main__.example_4
   1 of   5 in __main__.example_5
***Test Failed*** 27 failures.
For whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/tmp/.doctest_sage0.py
	 [27.4 s]

<SNIP>

sage -t -long "devel/sage/sage/server/simple/twist.py"      
**********************************************************************
File "/home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/devel/sage/sage/server/simple/twist.py", line 51:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
Expected:
    {
    "status": "done",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    4
Got:
    {
    "status": "computing",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of  24 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/usr/cicero/sandbox/sage-4.1.2.alpha1-6945-readline/tmp/.doctest_twist.py
	 [18.3 s]
 }}}
 

* lena: x86_64 RHEL 5.3 with GCC 4.4.1 --- compiles OK; all doctests pass.


* opensuse32 virtualized guest on boxen.math: 32-bit openSUSE 11.1 --- compiles OK; all doctests pass.


* opensuse64 virtualized guest on boxen.math: x86_64 openSUSE 11.1 --- compiles OK; all doctests pass.


* menas: x86_64 openSUSE 11.1 with GCC 4.4.1 --- compiles OK but must be built together with the cliquer package at #6681; all doctests pass.


* t2.math: SPARC Solaris with GCC 4.4.1 and Sun linker --- compiles OK. I can't run any doctests since Sage currently doesn't build completely on t2.math. The compilation now dies with this error message:
 {{{
/bin/sh: ../.././install-sh: not found
make[3]: [install-libsingular] Error 1 (ignored)
../.././install-sh -c kInline.cc /scratch/mvngu/sage-4.1.2.alpha1-6945-readline-cliquer-ecl/local/include/singular
make[3]: ../.././install-sh: Command not found
make[3]: *** [install-libsingular] Error 127
make[3]: Leaving directory `/scratch/mvngu/sage-4.1.2.alpha1-6945-readline-cliquer-ecl/spkg/build/singular-3-1-0-4-20090818/src/kernel'
make[2]: *** [install-libsingular] Error 2
make[2]: Leaving directory `/scratch/mvngu/sage-4.1.2.alpha1-6945-readline-cliquer-ecl/spkg/build/singular-3-1-0-4-20090818/src'
Unable to install libsingular.

real    49m13.554s
user    46m0.079s
sys     2m44.988s
sage: An error occurred while installing singular-3-1-0-4-20090818
 }}}
 Ticket #6951 tracks this issue.


As far as I'm concerned, it's a positive review from me. Merged readline-6.0.spkg in the standard packages repository.
