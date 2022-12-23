# Issue 5040: Bug in NTL's ./configure

Issue created by migration from https://trac.sagemath.org/ticket/5040

Original creator: was

Original creation time: 2009-01-20 22:37:46

Assignee: mabshoff

If you build sage and the directory path contains a "-h" anywhere in it, then NTL's perl DoConfig script displays a help message and exists.  This totally breaks building sage.  The code at fault is:

```

   if ($arg =~ '-h|help|-help|--help') {
      system("more ../doc/config.txt");
      exit;
   }
```


In particular, PREFIX will get passed in and if your directory were, e.g,. build-sage-help-me-foobar then Sage won't work.




---

Comment by mabshoff created at 2009-01-29 03:32:05

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha3/ntl-5.4.2.p5.spkg

fixes the problem by removing the help option for now. Note that this spkg also fixes #4978.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 03:32:05

Changing status from new to assigned.


---

Comment by cwitty created at 2009-01-29 04:02:33

Code looks good.  The new spkg does build, and relevant doctests still pass after rebuilding NTL-related .pyx files.

Positive review.


---

Comment by mabshoff created at 2009-01-29 04:04:33

Merged in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 04:04:33

Resolution: fixed
