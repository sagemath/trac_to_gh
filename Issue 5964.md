# Issue 5964: Some R doctests related to documentation fail when perl-modules not installed at compile-time

Issue created by migration from https://trac.sagemath.org/ticket/5964

Original creator: tornaria

Original creation time: 2009-05-02 22:59:26

Assignee: was

CC:  charpent chapoton

The doctest failures:

```
sage -t  "devel/sage/sage/interfaces/r.py"
**********************************************************************
File "/usr/src/sage-3.4.1/devel/sage/sage/interfaces/r.py", line 665:
    sage: r.help('print.anova')
Expected:
    anova                 package:stats                 R Documentation
    ...  
         'coefficients', 'effects', 'fitted.values', 'residuals',
         'summary', 'drop1', 'add1'.
Got:
    No documentation for 'print.anova' in specified packages and libraries:
    you could try 'help.search("print.anova")'
**********************************************************************
File "/usr/src/sage-3.4.1/devel/sage/sage/interfaces/r.py", line 1707:
    sage: print length._sage_doc_()
Expected:
    length                 package:base                 R Documentation
    ...
    <BLANKLINE>
Got:
    No documentation for 'length' in specified packages and libraries:
    you could try 'help.search("length")'
**********************************************************************
File "/usr/src/sage-3.4.1/devel/sage/sage/interfaces/r.py", line 1780:
    sage: print length._sage_doc_()
Expected:
    length                 package:base                 R Documentation
    ...
    <BLANKLINE>
Got:
    No documentation for 'length' in specified packages and libraries:
    you could try 'help.search("length")'
**********************************************************************
3 items had failures:
   1 of   3 in __main__.example_23
   1 of   5 in __main__.example_68
   1 of   4 in __main__.example_73
***Test Failed*** 3 failures.
For whitespace errors, see the file /usr/src/sage-3.4.1/tmp/.doctest_r.py
         [5.1 s]
```


----

Looking at the `install.log` shows two types of "failure":

 - missing `makeinfo`:

```
you should 'make docs' now ...
make[3]: Entering directory `/usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/doc'
make[4]: Entering directory `/usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/doc/manual'
'makeinfo' v4.7 or later needed to make HTML docs but missing on your system.
file R-FAQ.html will be missing
creating doc/manual/version.texi
'makeinfo' v4.7 or later needed to make HTML docs but missing on your system.
file R-data.html will be missing
'makeinfo' v4.7 or later needed to make HTML docs but missing on your system.
file R-exts.html will be missing
'makeinfo' v4.7 or later needed to make HTML docs but missing on your system.
file R-intro.html will be missing
'makeinfo' v4.7 or later needed to make HTML docs but missing on your system.
file R-ints.html will be missing
'makeinfo' v4.7 or later needed to make HTML docs but missing on your system.
file R-lang.html will be missing
make[5]: Entering directory `/usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/doc/html'
make[5]: Leaving directory `/usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/doc/html'
make[4]: Leaving directory `/usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/doc/manual'
make[3]: Leaving directory `/usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/doc'
```

 - missing perl module `File/Basename.pm`:

```
make[3]: Entering directory `/usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/src/library'
building all R object docs (text, HTML, LaTeX, examples)
make[4]: Entering directory `/usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/src/library'
Can't locate File/Basename.pm in @INC (@INC contains: /usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/share/perl /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ../../share/perl/build-help.pl line 18.
BEGIN failed--compilation aborted at ../../share/perl/build-help.pl line 18.
Can't locate File/Basename.pm in @INC (@INC contains: /usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/share/perl /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ../../share/perl/build-help.pl line 18.
BEGIN failed--compilation aborted at ../../share/perl/build-help.pl line 18.
Can't locate File/Basename.pm in @INC (@INC contains: /usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/share/perl /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ../../share/perl/build-help.pl line 18.
BEGIN failed--compilation aborted at ../../share/perl/build-help.pl line 18.
Can't locate File/Basename.pm in @INC (@INC contains: /usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/share/perl /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ../../share/perl/build-help.pl line 18.
BEGIN failed--compilation aborted at ../../share/perl/build-help.pl line 18.
Can't locate File/Basename.pm in @INC (@INC contains: /usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/share/perl /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ../../share/perl/build-help.pl line 18.
BEGIN failed--compilation aborted at ../../share/perl/build-help.pl line 18.
Can't locate File/Basename.pm in @INC (@INC contains: /usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/share/perl /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ../../share/perl/build-help.pl line 18.
BEGIN failed--compilation aborted at ../../share/perl/build-help.pl line 18.
Can't locate File/Basename.pm in @INC (@INC contains: /usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/share/perl /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ../../share/perl/build-help.pl line 18.
BEGIN failed--compilation aborted at ../../share/perl/build-help.pl line 18.
Can't locate File/Basename.pm in @INC (@INC contains: /usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/share/perl /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ../../share/perl/build-help.pl line 18.
BEGIN failed--compilation aborted at ../../share/perl/build-help.pl line 18.
Can't locate File/Basename.pm in @INC (@INC contains: /usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/share/perl /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ../../share/perl/build-help.pl line 18.
BEGIN failed--compilation aborted at ../../share/perl/build-help.pl line 18.
Can't locate File/Basename.pm in @INC (@INC contains: /usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/share/perl /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ../../share/perl/build-help.pl line 18.
BEGIN failed--compilation aborted at ../../share/perl/build-help.pl line 18.
Can't locate File/Basename.pm in @INC (@INC contains: /usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/share/perl /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ../../share/perl/build-help.pl line 18.
BEGIN failed--compilation aborted at ../../share/perl/build-help.pl line 18.
Can't locate File/Basename.pm in @INC (@INC contains: /usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/share/perl /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ../../share/perl/build-help.pl line 18.
BEGIN failed--compilation aborted at ../../share/perl/build-help.pl line 18.
make[4]: *** [help-indices] Error 2
make[4]: Leaving directory `/usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/src/library'
make[3]: *** [docs] Error 2
make[3]: Leaving directory `/usr/src/sage-3.4.1/spkg/build/r-2.6.1.p22/src/src/library'
make[2]: [docs] Error 2 (ignored)
```

----
This is on a "barebones" debian lenny, which only has `perl-base`, but no `perl-modules` installed, thus `File/Basename.pm` is indeed missing.

Reinstalling r-2.6.1.p22.spkg _after_ `apt-get install perl-modules` fixes the issue: the `install.log` still complains about missing `makeinfo`, but that seems irrelevant, and the doctest in `devel/sage/sage/interfaces/r.py` pass.

I believe the prereq test actually checks if perl is installed, but that seems to not be enough. Adding a check for a few required perl modules may be in order... (cf #5517, whose dependency on `File/Copy.pm` was actually eliminated, but the point stands).


---

Comment by jmantysalo created at 2015-07-17 05:32:30

Emmanuel, I found this on oooold tickets. I guess this can be closed. (Or could have been years ago.)


---

Comment by jmantysalo created at 2016-08-25 10:13:04

Can't reproduce. Frédéric, put on positive review if you agree.


---

Comment by jmantysalo created at 2016-08-25 10:13:04

Changing status from new to needs_review.


---

Comment by chapoton created at 2016-08-25 12:37:05

ok, no perl-modules and no problem


---

Comment by chapoton created at 2016-08-25 12:37:05

Changing status from needs_review to positive_review.


---

Comment by embray created at 2016-08-30 13:32:25

Resolution: wontfix


---

Comment by embray created at 2016-08-30 13:32:25

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).
