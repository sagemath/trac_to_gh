# Issue 6908: programmers' guide --- doctesting and parallel doctesting

archive/issues_006908.json:
```json
{
    "body": "Assignee: tba\n\nAdd a section to the Programmers' Guide, explaining how to perform basic doctesting. Also add some information on how to do parallel doctesting. See this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/c6508083de9bedc1) thread for some background information.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6908\n\n",
    "created_at": "2009-09-09T09:08:11Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "programmers' guide --- doctesting and parallel doctesting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6908",
    "user": "mvngu"
}
```
Assignee: tba

Add a section to the Programmers' Guide, explaining how to perform basic doctesting. Also add some information on how to do parallel doctesting. See this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/c6508083de9bedc1) thread for some background information.

Issue created by migration from https://trac.sagemath.org/ticket/6908





---

archive/issue_comments_057065.json:
```json
{
    "body": "I don't have time now to review this patch BUT wanted to point out that it should not be automatically doctested - I know that at one point there was discussion about doctesting the tutorial, not sure about the programmer's guide.",
    "created_at": "2009-09-09T17:27:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6908#issuecomment-57065",
    "user": "kcrisman"
}
```

I don't have time now to review this patch BUT wanted to point out that it should not be automatically doctested - I know that at one point there was discussion about doctesting the tutorial, not sure about the programmer's guide.



---

archive/issue_comments_057066.json:
```json
{
    "body": "line 93:\n\n```\n[mvngu@mod sage-4.1.1]$ sage devel/sage-main/sage/games/sudoku.py \n```\n\nis missing \"-t\".  I don't understand this example, though.  If I do `./sage -t devel/sage/sage/games/sudoku.py`, it works.  If I use the system version instead -- `sage -t devel/...` -- I get\n\n```\n(sage-4.1.2.alpha1-64bit) [10:48]$ sage -t devel/sage/sage/games/sudoku.py \nsage -t  \"builds/sage-4.1.2.alpha1-64bit/devel/sage/sage/games/sudoku.py\"\n  File \"./sudoku.py\", line 18\n    from devel/sage/sage/games/sudoku import *\n              ^\nSyntaxError: invalid syntax\n\n\t [1.0 s]\n```\n\nIf you can reproduce this error, perhaps it should be included also?  (By the way, the only way I've found to doctest a .py file (for example) in a different build of Sage, or completely outside the Sage library, is to cd to the actual directory containing the file and then running `sage -t sudoku.py`.)\n\nLines 134-135 have a line break which shouldn't be there.\n\nAt the end, is it worth giving brief descriptions of what these do?\n\n```\nmake test\nmake check\nmake testlong\nmake ptest\nmake ptestlong\n```\n\nOr do you think it's clear enough without that?\n\nOther than that, I think it looks pretty good.\n\nRegarding kcrisman's comment about doctesting, this file doesn't contain anything which gets doctested: run \"sage -t -verbose -long\" on it.",
    "created_at": "2009-09-09T18:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6908#issuecomment-57066",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_057067.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n> At the end, is it worth giving brief descriptions of what these do?\n> {{{\n> make test\n> make check\n> make testlong\n> make ptest\n> make ptestlong\n> }}}\n\nYes, please!",
    "created_at": "2009-09-09T18:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6908#issuecomment-57067",
    "user": "kcrisman"
}
```

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

archive/issue_comments_057068.json:
```json
{
    "body": "Replying to [comment:3 jhpalmieri]:\n> line 93:\n\n```\n[mvngu@mod sage-4.1.1]$ sage devel/sage-main/sage/games/sudoku.py \n```\n\n> is missing \"-t\".\nFixed. That example shouldn't be there.\n\n\n\n\n> I don't understand this example, though.  If I do `./sage -t devel/sage/sage/games/sudoku.py`, it works.  If I use the system version instead -- `sage -t devel/...` -- I get\n> {{{\n> (sage-4.1.2.alpha1-64bit) [10:48]$ sage -t devel/sage/sage/games/sudoku.py \n> sage -t  \"builds/sage-4.1.2.alpha1-64bit/devel/sage/sage/games/sudoku.py\"\n>   File \"./sudoku.py\", line 18\n>     from devel/sage/sage/games/sudoku import *\n>               ^\n> SyntaxError: invalid syntax\n> \n> \t [1.0 s]\n> }}}\n> If you can reproduce this error, perhaps it should be included also?\nI don't know how to reproduce that error. With Sage 4.1.1, I got this:\n\n```\n[mvngu@sage sage-4.1.1]$ ./sage -t devel/sage/sage/games/sudoku.py\nsage -t  \"devel/sage/sage/games/sudoku.py\"\n         [4.9 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 4.9 seconds\n[mvngu@sage sage-4.1.1]$ sage -t devel/sage/sage/games/sudoku.py\nTraceback (most recent call last):\n  File \"/usr/local/sage/local/bin/sage-test\", line 49, in <module>\n    os.makedirs(TMP)\n  File \"/usr/local/sage/local/lib/python/os.py\", line 157, in makedirs\n    mkdir(name, mode)\nOSError: [Errno 13] Permission denied: '/usr/local/sage/tmp/tmp'\n```\n\nWith Sage 4.1.2.alpha1, I got this:\n\n```\n[mvngu@sage sage-4.1.2.alpha1]$ ./sage -t devel/sage/sage/games/sudoku.py\nsage -t  \"devel/sage/sage/games/sudoku.py\"\n         [5.4 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 5.4 seconds\n[mvngu@sage sage-4.1.2.alpha1]$ sage -t devel/sage/sage/games/sudoku.py\nTraceback (most recent call last):\n  File \"/usr/local/sage/local/bin/sage-test\", line 49, in <module>\n    os.makedirs(TMP)\n  File \"/usr/local/sage/local/lib/python/os.py\", line 157, in makedirs\n    mkdir(name, mode)\nOSError: [Errno 13] Permission denied: '/usr/local/sage/tmp/tmp'\n```\n\nIn both cases, using a system-wide Sage resulted in permission error.\n\n\n\n\n> (By the way, the only way I've found to doctest a .py file (for example) in a different build of Sage, or completely outside the Sage library, is to cd to the actual directory containing the file and then running `sage -t sudoku.py`.)\nYes, if you're using a local Sage installation, not a system-wide one:\n\n```\n[mvngu@sage sage-4.1.1]$ cd devel/sage-main/sage/games/\n[mvngu@sage games]$ ls\nall.py    __init__.py         sudoku_backtrack.pyx\nhexad.py  sudoku_backtrack.c  sudoku.py\n[mvngu@sage games]$ pwd\n/scratch/mvngu/build/sage-4.1.1/devel/sage-main/sage/games\n[mvngu@sage games]$ /scratch/mvngu/build/sage-4.1.1/sage -t sudoku.py \nsage -t  \"devel/sage-main/sage/games/sudoku.py\"             \n         [5.1 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 5.1 seconds\n[mvngu@sage games]$ sage -t sudoku.py \nTraceback (most recent call last):\n  File \"/usr/local/sage/local/bin/sage-test\", line 49, in <module>\n    os.makedirs(TMP)\n  File \"/usr/local/sage/local/lib/python/os.py\", line 157, in makedirs\n    mkdir(name, mode)\nOSError: [Errno 13] Permission denied: '/usr/local/sage/tmp/tmp'\n```\n\n\n\n\n\n> Lines 134-135 have a line break which shouldn't be there.\nFixed.\n\n\n\n\nReplying to [comment:4 kcrisman]:\n> Replying to [comment:3 jhpalmieri]:\n> > At the end, is it worth giving brief descriptions of what these do?\n\n```\nmake test\nmake check\nmake testlong\nmake ptest\nmake ptestlong\n```\n\n> Yes, please!\nDone.",
    "created_at": "2009-09-11T13:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6908#issuecomment-57068",
    "user": "mvngu"
}
```

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

archive/issue_comments_057069.json:
```json
{
    "body": "Overall, it's looking good.  I have a few more comments and questions.\n\nReplying to [comment:5 mvngu]:\n> I don't know how to reproduce that error.\n\nTry using a version of Sage for which you have all the necessary permissions, and doctest a file outside of the Sage library by specifying a path name including slashes:\n\n```\n[mvngu@sage sage-4.1.1]$ ./sage -t ../testing/junk.py\n```\n\nor\n\n```\n[mvngu@sage sage-4.1.1]$ ./sage -t [path to sage-4.0]/devel/sage/sage/algebras/steenrod_algebra.py\n```\n\nDoes that give you an error?\n\nMaybe my point is that \"sage -t\" is inconsistent: it can accept a filename within the current directory, or it can accept a pathname if that path points to a location within the Sage library (can it accept any such path?), but it won't accept a path which includes directories pointing outside of the Sage library.  This throws me off all the time, and I don't think I even knew the pattern until writing this.  I'm not even sure that I have it right.  Since inconsistencies are confusing, perhaps this could be mentioned, or the allowable file- and/or path-name arguments to `sage -t` described.\n\nAlong these lines, do you want cross-references between this new chapter and the section on \"Automated Testing\" in conventions.rst?",
    "created_at": "2009-09-11T19:01:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6908#issuecomment-57069",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_057070.json:
```json
{
    "body": "based on Sage 4.1.2.alpha1",
    "created_at": "2009-09-12T08:44:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6908#issuecomment-57070",
    "user": "mvngu"
}
```

based on Sage 4.1.2.alpha1



---

archive/issue_comments_057071.json:
```json
{
    "body": "Attachment [trac_6908-doctesting-howto.patch](tarball://root/attachments/some-uuid/ticket6908/trac_6908-doctesting-howto.patch) by mvngu created at 2009-09-12 08:50:39\n\nReplying to [comment:6 jhpalmieri]:\n> Try using a version of Sage for which you have all the necessary permissions, and doctest a file outside of the Sage library by specifying a path name including slashes:\n\n```\n[mvngu@sage sage-4.1.1]$ ./sage -t ../testing/junk.py\n```\n\n> or\n\n```\n[mvngu@sage sage-4.1.1]$ ./sage -t [path to sage-4.0]/devel/sage/sage/algebras/steenrod_algebra.py\n```\n\n> Does that give you an error?\nYes, it did.\n\n\n\n\n\n> Maybe my point is that \"sage -t\" is inconsistent: it can accept a filename within the current directory, or it can accept a pathname if that path points to a location within the Sage library (can it accept any such path?), but it won't accept a path which includes directories pointing outside of the Sage library.  This throws me off all the time, and I don't think I even knew the pattern until writing this.  I'm not even sure that I have it right.  Since inconsistencies are confusing, perhaps this could be mentioned, or the allowable file- and/or path-name arguments to `sage -t` described.\nI added a little explanation at the start on the general syntax to use for doctesting. It doesn't cover all cases, but I think it should cover cases where someone wants to do basic doctesting. There is now a new section called \"Beyond the Sage library\" that explains the limited support for doctesting modules outside of the Sage library.\n\n\n\n\n\n> Along these lines, do you want cross-references between this new chapter and the section on \"Automated Testing\" in conventions.rst?\nDone.",
    "created_at": "2009-09-12T08:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6908#issuecomment-57071",
    "user": "mvngu"
}
```

Attachment [trac_6908-doctesting-howto.patch](tarball://root/attachments/some-uuid/ticket6908/trac_6908-doctesting-howto.patch) by mvngu created at 2009-09-12 08:50:39

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

archive/issue_comments_057072.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-12T15:46:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6908",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6908#issuecomment-57072",
    "user": "mvngu"
}
```

Resolution: fixed
