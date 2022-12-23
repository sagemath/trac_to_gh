# Issue 6908: programmers' guide --- doctesting and parallel doctesting

Issue created by migration from https://trac.sagemath.org/ticket/6908

Original creator: mvngu

Original creation time: 2009-09-09 09:08:11

Assignee: tba

Add a section to the Programmers' Guide, explaining how to perform basic doctesting. Also add some information on how to do parallel doctesting. See this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/c6508083de9bedc1) thread for some background information.


---

Comment by kcrisman created at 2009-09-09 17:27:21

I don't have time now to review this patch BUT wanted to point out that it should not be automatically doctested - I know that at one point there was discussion about doctesting the tutorial, not sure about the programmer's guide.


---

Comment by jhpalmieri created at 2009-09-09 18:08:32

line 93:

```
[mvngu@mod sage-4.1.1]$ sage devel/sage-main/sage/games/sudoku.py 
```

is missing "-t".  I don't understand this example, though.  If I do `./sage -t devel/sage/sage/games/sudoku.py`, it works.  If I use the system version instead -- `sage -t devel/...` -- I get

```
(sage-4.1.2.alpha1-64bit) [10:48]$ sage -t devel/sage/sage/games/sudoku.py 
sage -t  "builds/sage-4.1.2.alpha1-64bit/devel/sage/sage/games/sudoku.py"
  File "./sudoku.py", line 18
    from devel/sage/sage/games/sudoku import *
              ^
SyntaxError: invalid syntax

	 [1.0 s]
```

If you can reproduce this error, perhaps it should be included also?  (By the way, the only way I've found to doctest a .py file (for example) in a different build of Sage, or completely outside the Sage library, is to cd to the actual directory containing the file and then running `sage -t sudoku.py`.)

Lines 134-135 have a line break which shouldn't be there.

At the end, is it worth giving brief descriptions of what these do?

```
make test
make check
make testlong
make ptest
make ptestlong
```

Or do you think it's clear enough without that?

Other than that, I think it looks pretty good.

Regarding kcrisman's comment about doctesting, this file doesn't contain anything which gets doctested: run "sage -t -verbose -long" on it.


---

Comment by kcrisman created at 2009-09-09 18:14:49

Replying to [comment:3 jhpalmieri]:
> At the end, is it worth giving brief descriptions of what these do?
> {{{
> make test
> make check
> make testlong
> make ptest
> make ptestlong
> }}}

Yes, please!


---

Comment by mvngu created at 2009-09-11 13:15:02

Replying to [comment:3 jhpalmieri]:
> line 93:

```
[mvngu@mod sage-4.1.1]$ sage devel/sage-main/sage/games/sudoku.py 
```

> is missing "-t".
Fixed. That example shouldn't be there.




> I don't understand this example, though.  If I do `./sage -t devel/sage/sage/games/sudoku.py`, it works.  If I use the system version instead -- `sage -t devel/...` -- I get
> {{{
> (sage-4.1.2.alpha1-64bit) [10:48]$ sage -t devel/sage/sage/games/sudoku.py 
> sage -t  "builds/sage-4.1.2.alpha1-64bit/devel/sage/sage/games/sudoku.py"
>   File "./sudoku.py", line 18
>     from devel/sage/sage/games/sudoku import *
>               ^
> SyntaxError: invalid syntax
> 
> 	 [1.0 s]
> }}}
> If you can reproduce this error, perhaps it should be included also?
I don't know how to reproduce that error. With Sage 4.1.1, I got this:

```
[mvngu@sage sage-4.1.1]$ ./sage -t devel/sage/sage/games/sudoku.py
sage -t  "devel/sage/sage/games/sudoku.py"
         [4.9 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.9 seconds
[mvngu@sage sage-4.1.1]$ sage -t devel/sage/sage/games/sudoku.py
Traceback (most recent call last):
  File "/usr/local/sage/local/bin/sage-test", line 49, in <module>
    os.makedirs(TMP)
  File "/usr/local/sage/local/lib/python/os.py", line 157, in makedirs
    mkdir(name, mode)
OSError: [Errno 13] Permission denied: '/usr/local/sage/tmp/tmp'
```

With Sage 4.1.2.alpha1, I got this:

```
[mvngu@sage sage-4.1.2.alpha1]$ ./sage -t devel/sage/sage/games/sudoku.py
sage -t  "devel/sage/sage/games/sudoku.py"
         [5.4 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 5.4 seconds
[mvngu@sage sage-4.1.2.alpha1]$ sage -t devel/sage/sage/games/sudoku.py
Traceback (most recent call last):
  File "/usr/local/sage/local/bin/sage-test", line 49, in <module>
    os.makedirs(TMP)
  File "/usr/local/sage/local/lib/python/os.py", line 157, in makedirs
    mkdir(name, mode)
OSError: [Errno 13] Permission denied: '/usr/local/sage/tmp/tmp'
```

In both cases, using a system-wide Sage resulted in permission error.




> (By the way, the only way I've found to doctest a .py file (for example) in a different build of Sage, or completely outside the Sage library, is to cd to the actual directory containing the file and then running `sage -t sudoku.py`.)
Yes, if you're using a local Sage installation, not a system-wide one:

```
[mvngu@sage sage-4.1.1]$ cd devel/sage-main/sage/games/
[mvngu@sage games]$ ls
all.py    __init__.py         sudoku_backtrack.pyx
hexad.py  sudoku_backtrack.c  sudoku.py
[mvngu@sage games]$ pwd
/scratch/mvngu/build/sage-4.1.1/devel/sage-main/sage/games
[mvngu@sage games]$ /scratch/mvngu/build/sage-4.1.1/sage -t sudoku.py 
sage -t  "devel/sage-main/sage/games/sudoku.py"             
         [5.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 5.1 seconds
[mvngu@sage games]$ sage -t sudoku.py 
Traceback (most recent call last):
  File "/usr/local/sage/local/bin/sage-test", line 49, in <module>
    os.makedirs(TMP)
  File "/usr/local/sage/local/lib/python/os.py", line 157, in makedirs
    mkdir(name, mode)
OSError: [Errno 13] Permission denied: '/usr/local/sage/tmp/tmp'
```





> Lines 134-135 have a line break which shouldn't be there.
Fixed.




Replying to [comment:4 kcrisman]:
> Replying to [comment:3 jhpalmieri]:
> > At the end, is it worth giving brief descriptions of what these do?

```
make test
make check
make testlong
make ptest
make ptestlong
```

> Yes, please!
Done.


---

Comment by jhpalmieri created at 2009-09-11 19:01:12

Overall, it's looking good.  I have a few more comments and questions.

Replying to [comment:5 mvngu]:
> I don't know how to reproduce that error.

Try using a version of Sage for which you have all the necessary permissions, and doctest a file outside of the Sage library by specifying a path name including slashes:

```
[mvngu@sage sage-4.1.1]$ ./sage -t ../testing/junk.py
```

or

```
[mvngu@sage sage-4.1.1]$ ./sage -t [path to sage-4.0]/devel/sage/sage/algebras/steenrod_algebra.py
```

Does that give you an error?

Maybe my point is that "sage -t" is inconsistent: it can accept a filename within the current directory, or it can accept a pathname if that path points to a location within the Sage library (can it accept any such path?), but it won't accept a path which includes directories pointing outside of the Sage library.  This throws me off all the time, and I don't think I even knew the pattern until writing this.  I'm not even sure that I have it right.  Since inconsistencies are confusing, perhaps this could be mentioned, or the allowable file- and/or path-name arguments to `sage -t` described.

Along these lines, do you want cross-references between this new chapter and the section on "Automated Testing" in conventions.rst?


---

Comment by mvngu created at 2009-09-12 08:44:53

based on Sage 4.1.2.alpha1


---

Attachment

Replying to [comment:6 jhpalmieri]:
> Try using a version of Sage for which you have all the necessary permissions, and doctest a file outside of the Sage library by specifying a path name including slashes:

```
[mvngu@sage sage-4.1.1]$ ./sage -t ../testing/junk.py
```

> or

```
[mvngu@sage sage-4.1.1]$ ./sage -t [path to sage-4.0]/devel/sage/sage/algebras/steenrod_algebra.py
```

> Does that give you an error?
Yes, it did.





> Maybe my point is that "sage -t" is inconsistent: it can accept a filename within the current directory, or it can accept a pathname if that path points to a location within the Sage library (can it accept any such path?), but it won't accept a path which includes directories pointing outside of the Sage library.  This throws me off all the time, and I don't think I even knew the pattern until writing this.  I'm not even sure that I have it right.  Since inconsistencies are confusing, perhaps this could be mentioned, or the allowable file- and/or path-name arguments to `sage -t` described.
I added a little explanation at the start on the general syntax to use for doctesting. It doesn't cover all cases, but I think it should cover cases where someone wants to do basic doctesting. There is now a new section called "Beyond the Sage library" that explains the limited support for doctesting modules outside of the Sage library.





> Along these lines, do you want cross-references between this new chapter and the section on "Automated Testing" in conventions.rst?
Done.


---

Comment by mvngu created at 2009-09-12 15:46:55

Resolution: fixed
