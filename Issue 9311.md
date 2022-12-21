# Issue 9311: Add an spkg-check file for ratpoints

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-06-22 15:25:09

Assignee: tbd

CC:  leif jhpalmieri pjeremy

Ratpoints is one of the many standard packages in Sage (see #9281 for a list), which do not have a spkg-check file. This means that if one builds Sage with the environment variable SAGE_CHECK set to "yes", no self-tests of ratpoints will be run. This is silly, as there is a small test suite. 

Dave 


---

Comment by drkirkby created at 2010-06-22 15:32:47

This is not quite as simple as one would like on Solaris, as the test suite makes use of a non-POSIX '-u' option to diff

http://www.opengroup.org/onlinepubs/009695399/utilities/diff.html

so generates this as an output:


```
Successfully installed ratpoints-2.1.3.p2
Running the test suite.
Testing a 64-bit version of ratpoints
gcc rptest.c -o rptest -I/export/home/drkirkby/sage-4.4.4.alpha1/local/include -Wall -O2 -fPIC -DRATPOINTS_MAX_BITS_IN_PRIME= -DUSE_SSE -L/export/home/drkirkby/sage-4.4.4.alpha1/local/lib -lgmp -lm -L. -lratpoints -m64 
time ./rptest > rptest.out

real	0m0.05s
user	0m0.00s
sys	0m0.00s
diff -q testbase rptest.out
diff: illegal option -- q
usage: diff [-bitw] [-c | -e | -f | -h | -n | -u] file1 file2
       diff [-bitw] [-C number | -U number] file1 file2
       diff [-bitw] [-D string] file1 file2
       diff [-bitw] [-c | -e | -f | -h | -n | -u] [-l] [-r] [-s] [-S name] directory1 directory2
make: *** [test] Error 2
An error occurred while testing ratpoints
```



---

Comment by drkirkby created at 2010-06-22 15:33:32

Sorry, the illegal option is '-q', not '-u' as stated.


---

Comment by drkirkby created at 2010-06-24 10:48:47

I emailed this bug report to the developer. I think using 'cmp' rather than 'diff -q' would work fine. Will test it for sure. 

Dave
