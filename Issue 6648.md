# Issue 6648: [with patch, needs review] adds riemann mapping and complex interpolation

archive/issues_006648.json:
```json
{
    "body": "Assignee: evanandel\n\nCC:  robertwb\n\nKeywords: complex\n\nThis patch add's Riemann mapping functionality to sage: http://en.wikipedia.org/wiki/Riemann_mapping_theorem\n\nIt can compute numerical maps and has multiple utilities for plotting/visualizing the maps.\n\nIt also includes 2 functions to parametrically interpolate lists of complex points. This makes it far easier for the user to define the boundary of the figure that they wish to Riemann map.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6648\n\n",
    "created_at": "2009-07-28T17:10:46Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] adds riemann mapping and complex interpolation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6648",
    "user": "evanandel"
}
```
Assignee: evanandel

CC:  robertwb

Keywords: complex

This patch add's Riemann mapping functionality to sage: http://en.wikipedia.org/wiki/Riemann_mapping_theorem

It can compute numerical maps and has multiple utilities for plotting/visualizing the maps.

It also includes 2 functions to parametrically interpolate lists of complex points. This makes it far easier for the user to define the boundary of the figure that they wish to Riemann map.

Issue created by migration from https://trac.sagemath.org/ticket/6648





---

archive/issue_comments_054534.json:
```json
{
    "body": "patch for riemann and comp interpolation",
    "created_at": "2009-07-28T17:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54534",
    "user": "evanandel"
}
```

patch for riemann and comp interpolation



---

archive/issue_comments_054535.json:
```json
{
    "body": "Attachment [12659.patch](tarball://root/attachments/some-uuid/ticket6648/12659.patch) by evanandel created at 2009-07-28 17:28:45\n\nReplying to [ticket:6648 evanandel]:\n> This patch add's Riemann mapping functionality to sage: http://en.wikipedia.org/wiki/Riemann_mapping_theorem\n> \n> It can compute numerical maps and has multiple utilities for plotting/visualizing the maps.\n> \n> It also includes 2 functions to parametrically interpolate lists of complex points. This makes it far easier for the user to define the boundary of the figure that they wish to Riemann map.",
    "created_at": "2009-07-28T17:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54535",
    "user": "evanandel"
}
```

Attachment [12659.patch](tarball://root/attachments/some-uuid/ticket6648/12659.patch) by evanandel created at 2009-07-28 17:28:45

Replying to [ticket:6648 evanandel]:
> This patch add's Riemann mapping functionality to sage: http://en.wikipedia.org/wiki/Riemann_mapping_theorem
> 
> It can compute numerical maps and has multiple utilities for plotting/visualizing the maps.
> 
> It also includes 2 functions to parametrically interpolate lists of complex points. This makes it far easier for the user to define the boundary of the figure that they wish to Riemann map.



---

archive/issue_comments_054536.json:
```json
{
    "body": "On an intel macbook running 10.4.11, I got this:\n\n\n```\nzeus:~/sagefiles/sage-4.1.1.alpha0 davidjoyner$ ./sage \n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading Sage library. Current Mercurial branch is: rmap\nsage: hg_sage.apply(\"/Users/davidjoyner/sagefiles/12659.patch\")\ncd \"/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage\" && hg status\n/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.\n  x = os.popen3(s)\ncd \"/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage\" && hg status\ncd \"/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage\" && hg import   \"/Users/davidjoyner/sagefiles/12659.patch\"\napplying /Users/davidjoyner/sagefiles/12659.patch\nsage: \nExiting SAGE (CPU time 0m0.18s, Wall time 0m45.59s).\nzeus:~/sagefiles/sage-4.1.1.alpha0 davidjoyner$ ./sage -br\n| Sage Version 4.1.1.alpha0, Release Date: 2009-07-22                |\n| Type notebook() for the GUI, and license() for information.        |\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nBuilding modified file sage/calculus/riemann.pyx.\nBuilding modified file sage/calculus/interpolators.pyx.\npython `which cython` --embed-positions --incref-local-binop -I/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage-rmap -o sage/calculus/riemann.c sage/calculus/riemann.pyx\n\nError converting Pyrex file to C:\n------------------------------------------------------------\n...\n\ncdef class Riemann_Map:\n    cdef int N, B, ncorners\n    cdef f\n    cdef opp\n    cdef double complex a\n                       ^\n------------------------------------------------------------\n\n/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage-rmap/sage/calculus/riemann.pyx:62:24: Syntax error in C variable declaration\nError running command, failed with status 256.\nsage: There was an error installing modified sage library code.\n\n```\n\n\n\nAny idea what the problem is?",
    "created_at": "2009-07-28T17:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54536",
    "user": "wdj"
}
```

On an intel macbook running 10.4.11, I got this:


```
zeus:~/sagefiles/sage-4.1.1.alpha0 davidjoyner$ ./sage 
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: rmap
sage: hg_sage.apply("/Users/davidjoyner/sagefiles/12659.patch")
cd "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage" && hg status
/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.
  x = os.popen3(s)
cd "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage" && hg status
cd "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage" && hg import   "/Users/davidjoyner/sagefiles/12659.patch"
applying /Users/davidjoyner/sagefiles/12659.patch
sage: 
Exiting SAGE (CPU time 0m0.18s, Wall time 0m45.59s).
zeus:~/sagefiles/sage-4.1.1.alpha0 davidjoyner$ ./sage -br
| Sage Version 4.1.1.alpha0, Release Date: 2009-07-22                |
| Type notebook() for the GUI, and license() for information.        |
----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Building modified file sage/calculus/riemann.pyx.
Building modified file sage/calculus/interpolators.pyx.
python `which cython` --embed-positions --incref-local-binop -I/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage-rmap -o sage/calculus/riemann.c sage/calculus/riemann.pyx

Error converting Pyrex file to C:
------------------------------------------------------------
...

cdef class Riemann_Map:
    cdef int N, B, ncorners
    cdef f
    cdef opp
    cdef double complex a
                       ^
------------------------------------------------------------

/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage-rmap/sage/calculus/riemann.pyx:62:24: Syntax error in C variable declaration
Error running command, failed with status 256.
sage: There was an error installing modified sage library code.

```



Any idea what the problem is?



---

archive/issue_comments_054537.json:
```json
{
    "body": "Attachment [12659.2.patch](tarball://root/attachments/some-uuid/ticket6648/12659.2.patch) by evanandel created at 2009-07-29 13:54:36",
    "created_at": "2009-07-29T13:54:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54537",
    "user": "evanandel"
}
```

Attachment [12659.2.patch](tarball://root/attachments/some-uuid/ticket6648/12659.2.patch) by evanandel created at 2009-07-29 13:54:36



---

archive/issue_comments_054538.json:
```json
{
    "body": "> Error converting Pyrex file to C:\n> ------------------------------------------------------------\n> ...\n> \n> cdef class Riemann_Map:\n>     cdef int N, B, ncorners\n>     cdef f\n>     cdef opp\n>     cdef double complex a\n>                        ^\n> ------------------------------------------------------------\n> \n> /Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage-rmap/sage/calculus/riemann.pyx:62:24: Syntax error in C variable declaration\n> Error running command, failed with status 256.\n> sage: There was an error installing modified sage library code.\n> \n> }}}\n> \n> \n> Any idea what the problem is?\n\nThat's a problem with sage's cython version. You need to update to 0.11.2. \nAccording to Mike Hanson:\n\n\" There is a ticket to update Cython in Sage at\nhttp://trac.sagemath.org/sage_trac/ticket/6438.  If you download\nhttp://sage.math.washington.edu/home/robertwb/cython/cython-0.11.2.spkg\nand run \"sage -f /path/to/cython-0.11.2.spkg\", then Cython 0.11.2 will\nbe used.\n\n--Mike \"",
    "created_at": "2009-07-29T13:57:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54538",
    "user": "evanandel"
}
```

> Error converting Pyrex file to C:
> ------------------------------------------------------------
> ...
> 
> cdef class Riemann_Map:
>     cdef int N, B, ncorners
>     cdef f
>     cdef opp
>     cdef double complex a
>                        ^
> ------------------------------------------------------------
> 
> /Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage-rmap/sage/calculus/riemann.pyx:62:24: Syntax error in C variable declaration
> Error running command, failed with status 256.
> sage: There was an error installing modified sage library code.
> 
> }}}
> 
> 
> Any idea what the problem is?

That's a problem with sage's cython version. You need to update to 0.11.2. 
According to Mike Hanson:

" There is a ticket to update Cython in Sage at
http://trac.sagemath.org/sage_trac/ticket/6438.  If you download
http://sage.math.washington.edu/home/robertwb/cython/cython-0.11.2.spkg
and run "sage -f /path/to/cython-0.11.2.spkg", then Cython 0.11.2 will
be used.

--Mike "



---

archive/issue_comments_054539.json:
```json
{
    "body": "I applied only the 2nd patch to 4.1.1.a0. It seemed to work fine trying out several examples form the docstrings by had. However, on an intel macbook running 10.4.11 there were several failures of sage -testall:\n\n\n```\n        sage -t  \"devel/sage/doc/en/bordeaux_2008/birds_other.rst\"\n        sage -t  \"devel/sage/sage/calculus/interpolators.pyx\"\n        sage -t  \"devel/sage/sage/interfaces/psage.py\"\n        sage -t  \"devel/sage/sage/interfaces/sage0.py\"\n        sage -t  \"devel/sage/sage/parallel/decorate.py\"\n        sage -t  \"devel/sage/sage/symbolic/expression.pyx\"\n```\n\n\nSome of these are probably spurious but some are not:\n\n\n```\nzeus:~/sagefiles/sage-4.1.1.alpha0 davidjoyner$ ./sage -t  \"devel/sage/sage/calculus/interpolators.pyx\"\nsage -t  \"devel/sage/sage/calculus/interpolators.pyx\"       \n**********************************************************************\nFile \"/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/calculus/interpolators.pyx\", line 89:\n    sage: ps.value(10)\nExpected:\n    (0.2676045526483728+1j)\nGot:\n    (0.26760455264837191+1j)\n**********************************************************************\nFile \"/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/calculus/interpolators.pyx\", line 146:\n    sage: cs.derivative(2)\nExpected:\n    (-0.049776540658333007+0.15109500643420509j)\nGot:\n    (-0.049776539604289502+0.15109500674962709j)\n**********************************************************************\nFile \"/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/calculus/interpolators.pyx\", line 221:\n    sage: cs.derivative(3/5)\nExpected:\n    (1.4057889232733602-0.22541713632654017j)\nGot:\n    (1.4057889243877602-0.22541713160563243j)\n**********************************************************************\nFile \"/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/calculus/interpolators.pyx\", line 225:\n    sage: cs.derivative(-6)\nExpected:\n    (2.5204769294914593-1.8939258831078529j)\nGot:\n    (2.5204768628640499-1.8939257072489877j)\n**********************************************************************\n3 items had failures:\n   1 of   7 in __main__.example_2\n   1 of  12 in __main__.example_4\n   2 of   7 in __main__.example_6\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/tmp/.doctest_interpolators.py\n         [45.7 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/calculus/interpolators.pyx\"\n```\n\n\nThis looks like numerical noise but I'm not sure. In any case, it is in a file you modified, so it\nis probably not spurious.",
    "created_at": "2009-07-30T12:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54539",
    "user": "wdj"
}
```

I applied only the 2nd patch to 4.1.1.a0. It seemed to work fine trying out several examples form the docstrings by had. However, on an intel macbook running 10.4.11 there were several failures of sage -testall:


```
        sage -t  "devel/sage/doc/en/bordeaux_2008/birds_other.rst"
        sage -t  "devel/sage/sage/calculus/interpolators.pyx"
        sage -t  "devel/sage/sage/interfaces/psage.py"
        sage -t  "devel/sage/sage/interfaces/sage0.py"
        sage -t  "devel/sage/sage/parallel/decorate.py"
        sage -t  "devel/sage/sage/symbolic/expression.pyx"
```


Some of these are probably spurious but some are not:


```
zeus:~/sagefiles/sage-4.1.1.alpha0 davidjoyner$ ./sage -t  "devel/sage/sage/calculus/interpolators.pyx"
sage -t  "devel/sage/sage/calculus/interpolators.pyx"       
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/calculus/interpolators.pyx", line 89:
    sage: ps.value(10)
Expected:
    (0.2676045526483728+1j)
Got:
    (0.26760455264837191+1j)
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/calculus/interpolators.pyx", line 146:
    sage: cs.derivative(2)
Expected:
    (-0.049776540658333007+0.15109500643420509j)
Got:
    (-0.049776539604289502+0.15109500674962709j)
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/calculus/interpolators.pyx", line 221:
    sage: cs.derivative(3/5)
Expected:
    (1.4057889232733602-0.22541713632654017j)
Got:
    (1.4057889243877602-0.22541713160563243j)
**********************************************************************
File "/Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/devel/sage/sage/calculus/interpolators.pyx", line 225:
    sage: cs.derivative(-6)
Expected:
    (2.5204769294914593-1.8939258831078529j)
Got:
    (2.5204768628640499-1.8939257072489877j)
**********************************************************************
3 items had failures:
   1 of   7 in __main__.example_2
   1 of  12 in __main__.example_4
   2 of   7 in __main__.example_6
***Test Failed*** 4 failures.
For whitespace errors, see the file /Users/davidjoyner/sagefiles/sage-4.1.1.alpha0/tmp/.doctest_interpolators.py
         [45.7 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/calculus/interpolators.pyx"
```


This looks like numerical noise but I'm not sure. In any case, it is in a file you modified, so it
is probably not spurious.



---

archive/issue_comments_054540.json:
```json
{
    "body": "I'm not sure about the ps.value failure, that does look like numerical noise. The cs ones were my mistake when creating the new patch. There's yet another version up now that should *fingers crossed* work better. \n\nThe whole package is highly dependent on numerical methods, so noise wouldn't surprise me, but maybe it should.",
    "created_at": "2009-07-30T13:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54540",
    "user": "evanandel"
}
```

I'm not sure about the ps.value failure, that does look like numerical noise. The cs ones were my mistake when creating the new patch. There's yet another version up now that should *fingers crossed* work better. 

The whole package is highly dependent on numerical methods, so noise wouldn't surprise me, but maybe it should.



---

archive/issue_comments_054541.json:
```json
{
    "body": "Attachment [12659.3.patch](tarball://root/attachments/some-uuid/ticket6648/12659.3.patch) by evanandel created at 2009-07-30 13:57:05",
    "created_at": "2009-07-30T13:57:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54541",
    "user": "evanandel"
}
```

Attachment [12659.3.patch](tarball://root/attachments/some-uuid/ticket6648/12659.3.patch) by evanandel created at 2009-07-30 13:57:05



---

archive/issue_comments_054542.json:
```json
{
    "body": "The patch 12659.3.patch applied fine (after upgrading cython as mentioned already).\nHowever, sage -testall failed again, this time on an amd64 ubuntu 9.04 machine:\n\n\n```\nwdj@hera:~/sagefiles/sage-4.1.1.alpha1$ ./sage -t  \"devel/sage/sage/calculus/interpolators.pyx\"\nsage -t  \"devel/sage/sage/calculus/interpolators.pyx\"                                          \n**********************************************************************                         \nFile \"/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/calculus/interpolators.pyx\", line 89:\n    sage: ps.value(10)                                                                           \nExpected:                                                                                        \n    (0.2676045526483728+1j)                                                                      \nGot:                                                                                             \n    (0.26760455264837191+1j)                                                                     \n**********************************************************************                           \nFile \"/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/calculus/interpolators.pyx\", line 146:\n    sage: cs.derivative(2)                                                                        \nExpected:                                                                                         \n    (-0.049776540658333007+0.15109500643420509j)                                                  \nGot:                                                                                              \n    (-0.049776540658333021+0.15109500643420506j)                                                  \n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/calculus/interpolators.pyx\", line 221:\n    sage: cs.derivative(3/5)\nExpected:\n    (1.4057889232733602-0.22541713632654017j)\nGot:\n    (1.4057889232733602-0.22541713632654015j)\n**********************************************************************\n3 items had failures:\n   1 of   7 in __main__.example_2\n   1 of  12 in __main__.example_4\n   1 of   7 in __main__.example_6\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /home/wdj/sagefiles/sage-4.1.1.alpha1/tmp/.doctest_interpolators.py\n         [6.4 s]\nexit code: 1024\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/calculus/interpolators.pyx\"\nTotal time for all tests: 6.4 seconds\n```\n",
    "created_at": "2009-07-30T18:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54542",
    "user": "wdj"
}
```

The patch 12659.3.patch applied fine (after upgrading cython as mentioned already).
However, sage -testall failed again, this time on an amd64 ubuntu 9.04 machine:


```
wdj@hera:~/sagefiles/sage-4.1.1.alpha1$ ./sage -t  "devel/sage/sage/calculus/interpolators.pyx"
sage -t  "devel/sage/sage/calculus/interpolators.pyx"                                          
**********************************************************************                         
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/calculus/interpolators.pyx", line 89:
    sage: ps.value(10)                                                                           
Expected:                                                                                        
    (0.2676045526483728+1j)                                                                      
Got:                                                                                             
    (0.26760455264837191+1j)                                                                     
**********************************************************************                           
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/calculus/interpolators.pyx", line 146:
    sage: cs.derivative(2)                                                                        
Expected:                                                                                         
    (-0.049776540658333007+0.15109500643420509j)                                                  
Got:                                                                                              
    (-0.049776540658333021+0.15109500643420506j)                                                  
**********************************************************************
File "/home/wdj/sagefiles/sage-4.1.1.alpha1/devel/sage/sage/calculus/interpolators.pyx", line 221:
    sage: cs.derivative(3/5)
Expected:
    (1.4057889232733602-0.22541713632654017j)
Got:
    (1.4057889232733602-0.22541713632654015j)
**********************************************************************
3 items had failures:
   1 of   7 in __main__.example_2
   1 of  12 in __main__.example_4
   1 of   7 in __main__.example_6
***Test Failed*** 3 failures.
For whitespace errors, see the file /home/wdj/sagefiles/sage-4.1.1.alpha1/tmp/.doctest_interpolators.py
         [6.4 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/calculus/interpolators.pyx"
Total time for all tests: 6.4 seconds
```




---

archive/issue_comments_054543.json:
```json
{
    "body": "Hmm... It runs fine for me, intel t3200, ubuntu 9.04\n\nI'm afraid I'm not knowledgeable enough to pinpoint the exact source of the differences. Is there some sort of flag that can make the test routine ignore numerical differences of a certain size?\n\nIs there some other way that it should be fixed?",
    "created_at": "2009-07-30T19:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54543",
    "user": "evanandel"
}
```

Hmm... It runs fine for me, intel t3200, ubuntu 9.04

I'm afraid I'm not knowledgeable enough to pinpoint the exact source of the differences. Is there some sort of flag that can make the test routine ignore numerical differences of a certain size?

Is there some other way that it should be fixed?



---

archive/issue_comments_054544.json:
```json
{
    "body": "Replying to [comment:7 evanandel]:\n> Hmm... It runs fine for me, intel t3200, ubuntu 9.04\n> \n> I'm afraid I'm not knowledgeable enough to pinpoint the exact source of the differences. Is there some sort of flag that can make the test routine ignore numerical differences of a certain size?\n> \n> Is there some other way that it should be fixed?\n\nYes there is such a \"flag\" but I am the wrong person to ask! I would ask Carl Witty, if you can get a hold of him. If that fails, just post to sage-support something about keeping track of numerical noise doctest failures.",
    "created_at": "2009-07-30T19:39:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54544",
    "user": "wdj"
}
```

Replying to [comment:7 evanandel]:
> Hmm... It runs fine for me, intel t3200, ubuntu 9.04
> 
> I'm afraid I'm not knowledgeable enough to pinpoint the exact source of the differences. Is there some sort of flag that can make the test routine ignore numerical differences of a certain size?
> 
> Is there some other way that it should be fixed?

Yes there is such a "flag" but I am the wrong person to ask! I would ask Carl Witty, if you can get a hold of him. If that fails, just post to sage-support something about keeping track of numerical noise doctest failures.



---

archive/issue_comments_054545.json:
```json
{
    "body": "Alright, new patch up. It truncates the required precision a bit.",
    "created_at": "2009-07-31T14:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54545",
    "user": "evanandel"
}
```

Alright, new patch up. It truncates the required precision a bit.



---

archive/issue_comments_054546.json:
```json
{
    "body": "Attachment [12659.4.patch](tarball://root/attachments/some-uuid/ticket6648/12659.4.patch) by wdj created at 2009-07-31 18:59:01\n\nThis passes sage -testall (except for the known failures for 4.1.1.a1 on an amd64 ubuntu 9.04 machine).\n\nPositive review from me. Should it undergo more testing?",
    "created_at": "2009-07-31T18:59:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54546",
    "user": "wdj"
}
```

Attachment [12659.4.patch](tarball://root/attachments/some-uuid/ticket6648/12659.4.patch) by wdj created at 2009-07-31 18:59:01

This passes sage -testall (except for the known failures for 4.1.1.a1 on an amd64 ubuntu 9.04 machine).

Positive review from me. Should it undergo more testing?



---

archive/issue_comments_054547.json:
```json
{
    "body": "If that question is directed to me (I'm new to this), I don't *think* so. Do I need to do anything other than change the summary to [with patch, positive review]?\n\nRegardless, thank you for the time you spent.",
    "created_at": "2009-07-31T20:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54547",
    "user": "evanandel"
}
```

If that question is directed to me (I'm new to this), I don't *think* so. Do I need to do anything other than change the summary to [with patch, positive review]?

Regardless, thank you for the time you spent.



---

archive/issue_comments_054548.json:
```json
{
    "body": "I'm changing this to postive review.\n\nMinh - if you want me to wait until a warnignless version of sage is released, please let me know and I'll be happy to retest.",
    "created_at": "2009-07-31T22:36:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54548",
    "user": "wdj"
}
```

I'm changing this to postive review.

Minh - if you want me to wait until a warnignless version of sage is released, please let me know and I'll be happy to retest.



---

archive/issue_comments_054549.json:
```json
{
    "body": "This patch needs work:\n\n\n```\nmalb@sage:~/sage-4.1/devel$ sage -coverage sage/sage/calculus/interpolators.pyx\n----------------------------------------------------------------------\nsage/sage/calculus/interpolators.pyx\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE sage/sage/calculus/interpolators.pyx: 75% (6 of 8)\n\nMissing documentation:\n         * __init__(self,pts,shift = (0,0)):\n         * __init__(self,pts):\n\n----------------------------------------------------------------------\n```\n\n\n\n\n```\nmalb@sage:~/sage-4.1/devel$ sage -coverage sage/sage/calculus/riemann.pyx\n----------------------------------------------------------------------\nsage/sage/calculus/riemann.pyx\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE sage/sage/calculus/riemann.pyx: 50% (7 of 14)\n\nMissing documentation:\n         * _repr_(self):\n         * __init__(self, z_values, xrange, yrange):\n         * get_minmax_data(self):\n         * _allowed_options(self):\n         * _repr_(self):\n         * _render_on_subplot(self, subplot):\n\n\nMissing doctests:\n         * __init__(self,fs,fprimes,a,int N = 500,int ncorners = 4,opp = False):\n```\n\n\nAlso, should these files be added to the reference manual?",
    "created_at": "2009-08-04T11:28:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54549",
    "user": "malb"
}
```

This patch needs work:


```
malb@sage:~/sage-4.1/devel$ sage -coverage sage/sage/calculus/interpolators.pyx
----------------------------------------------------------------------
sage/sage/calculus/interpolators.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE sage/sage/calculus/interpolators.pyx: 75% (6 of 8)

Missing documentation:
         * __init__(self,pts,shift = (0,0)):
         * __init__(self,pts):

----------------------------------------------------------------------
```




```
malb@sage:~/sage-4.1/devel$ sage -coverage sage/sage/calculus/riemann.pyx
----------------------------------------------------------------------
sage/sage/calculus/riemann.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE sage/sage/calculus/riemann.pyx: 50% (7 of 14)

Missing documentation:
         * _repr_(self):
         * __init__(self, z_values, xrange, yrange):
         * get_minmax_data(self):
         * _allowed_options(self):
         * _repr_(self):
         * _render_on_subplot(self, subplot):


Missing doctests:
         * __init__(self,fs,fprimes,a,int N = 500,int ncorners = 4,opp = False):
```


Also, should these files be added to the reference manual?



---

archive/issue_comments_054550.json:
```json
{
    "body": "Attachment [12659.5.patch](tarball://root/attachments/some-uuid/ticket6648/12659.5.patch) by evanandel created at 2009-08-04 15:00:22\n\nAlright, new patch is up that fixes the missing documentation.\n\nWhat would adding the files to the reference manual entail?",
    "created_at": "2009-08-04T15:00:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54550",
    "user": "evanandel"
}
```

Attachment [12659.5.patch](tarball://root/attachments/some-uuid/ticket6648/12659.5.patch) by evanandel created at 2009-08-04 15:00:22

Alright, new patch is up that fixes the missing documentation.

What would adding the files to the reference manual entail?



---

archive/issue_comments_054551.json:
```json
{
    "body": "> What would adding the files to the reference manual entail?\n\nhttp://www.sagemath.org/doc/developer/sage_manuals.html#editing-the-manuals\n\nAlso: is it correct that only the last (of the five) patch is to be applied?",
    "created_at": "2009-08-15T21:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54551",
    "user": "wdj"
}
```

> What would adding the files to the reference manual entail?

http://www.sagemath.org/doc/developer/sage_manuals.html#editing-the-manuals

Also: is it correct that only the last (of the five) patch is to be applied?



---

archive/issue_comments_054552.json:
```json
{
    "body": "Correct, only the last patch should be applied.\n\nFrom a quick look it seems that this should be added to the basic reference manual, but nowhere else. I'm on vacation now, so those edits may take a bit. I'll probably put them in a separate patch.",
    "created_at": "2009-08-16T04:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54552",
    "user": "evanandel"
}
```

Correct, only the last patch should be applied.

From a quick look it seems that this should be added to the basic reference manual, but nowhere else. I'm on vacation now, so those edits may take a bit. I'll probably put them in a separate patch.



---

archive/issue_comments_054553.json:
```json
{
    "body": "I applied the 5th patch to 4.1.1.rc2 on an intel macbook runing 10.4.11. I got\n\n\n```\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/doc/en/bordeaux_2008/birds_other.rst\"\n        sage -t  \"devel/sage/sage/interfaces/maxima.py\"\n        sage -t  \"devel/sage/sage/symbolic/expression.pyx\"\n```\n\nNone of these failures seem related. So this patch seems to be okay except for the reference manual addition. The patch author (in an offlist email)  said he would add another patch soon for the ref manual, so I am changing this to \"needs work\" for that reason.  I cannot vouch for the Cython or mathematics, though from the experimentation I did, I cn't find a problem.",
    "created_at": "2009-08-16T15:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54553",
    "user": "wdj"
}
```

I applied the 5th patch to 4.1.1.rc2 on an intel macbook runing 10.4.11. I got


```
The following tests failed:


        sage -t  "devel/sage/doc/en/bordeaux_2008/birds_other.rst"
        sage -t  "devel/sage/sage/interfaces/maxima.py"
        sage -t  "devel/sage/sage/symbolic/expression.pyx"
```

None of these failures seem related. So this patch seems to be okay except for the reference manual addition. The patch author (in an offlist email)  said he would add another patch soon for the ref manual, so I am changing this to "needs work" for that reason.  I cannot vouch for the Cython or mathematics, though from the experimentation I did, I cn't find a problem.



---

archive/issue_comments_054554.json:
```json
{
    "body": "New Patch, should add it to the reference manual properly (I hope).\nThis patch is independent from the prefious ones, that is you need to install both the latest 12659 and the 12660.",
    "created_at": "2009-08-27T17:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54554",
    "user": "evanandel"
}
```

New Patch, should add it to the reference manual properly (I hope).
This patch is independent from the prefious ones, that is you need to install both the latest 12659 and the 12660.



---

archive/issue_comments_054555.json:
```json
{
    "body": "Attachment [12660.patch](tarball://root/attachments/some-uuid/ticket6648/12660.patch) by wdj created at 2009-08-28 00:41:01\n\nPasses as before, so I give this a positive review again. However, I don't know how to check the reference docs, or what should be checked. Or is that part of the refereeing processing?",
    "created_at": "2009-08-28T00:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54555",
    "user": "wdj"
}
```

Attachment [12660.patch](tarball://root/attachments/some-uuid/ticket6648/12660.patch) by wdj created at 2009-08-28 00:41:01

Passes as before, so I give this a positive review again. However, I don't know how to check the reference docs, or what should be checked. Or is that part of the refereeing processing?



---

archive/issue_comments_054556.json:
```json
{
    "body": "I checked that the html built as part of the reference manual.",
    "created_at": "2009-08-30T15:29:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54556",
    "user": "wdj"
}
```

I checked that the html built as part of the reference manual.



---

archive/issue_comments_054557.json:
```json
{
    "body": "I assume that patches should be merged in this order:\n\n1. `12659.5.patch`\n2. `12660.patch`\n\nThese patches apply OK against Sage 4.1.1, with `12660.patch` resulting in some fuzz:\n\n```\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6648/12660.patch && hg qpush\nadding 12660.patch to series file\napplying 12660.patch\npatching file module_list.py\nHunk #1 succeeded at 125 with fuzz 2 (offset 8 lines).\npatching file sage/calculus/all.py\nHunk #1 succeeded at 20 with fuzz 2 (offset 4 lines).\nNow at: 12660.patch\n```\n\nDon't worry about the fuzz. However, building the reference manual results in 17 warnings:\n\n```\nWARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.\nWARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.\nWARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.\nWARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.\nWARNING: :0: (ERROR/3) Unexpected indentation.\nWARNING: :0: (ERROR/3) Unexpected indentation.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/calculus/riemann.so:docstring of sage.calculus.riemann:3: (ERROR/3) Unexpected indentation.\nWARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/calculus/riemann.so:docstring of sage.calculus.riemann:5: (ERROR/3) Unexpected indentation.\nWARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.\nWARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/calculus/riemann.so:docstring of sage.calculus.riemann:3: (ERROR/3) Unexpected indentation.\nWARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/calculus/riemann.so:docstring of sage.calculus.riemann:5: (ERROR/3) Unexpected indentation.\nWARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/calculus/riemann.so:docstring of sage.calculus.riemann.ColorPlot.get_minmax_data:5: (ERROR/3) Unexpected indentation.\nWARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.\npickling environment... done\nchecking consistency... done\npreparing documents... done\nwriting output... calculus index sage/calculus/interpolators sage/calculus/riemann \nwriting additional files... genindex modindex search\ncopying static files... done\ndumping search index... done\ndumping object inventory... done\nbuild succeeded, 17 warnings.\n```\n\nTwo crucial doctests are missing:\n\n```\n[mvngu@sage sage-4.1.1]$ ./sage -coverage devel/sage-main/sage/calculus/interpolators.pyx\n----------------------------------------------------------------------\ndevel/sage-main/sage/calculus/interpolators.pyx\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE devel/sage-main/sage/calculus/interpolators.pyx: 100% (8 of 8)\n----------------------------------------------------------------------\n\n[mvngu@sage sage-4.1.1]$ ./sage -coverage devel/sage-main/sage/calculus/riemann.pyx\n----------------------------------------------------------------------\ndevel/sage-main/sage/calculus/riemann.pyx\nERROR: Please define a s == loads(dumps(s)) doctest.\nSCORE devel/sage-main/sage/calculus/riemann.pyx: 100% (14 of 14)\n\nPossibly wrong (function name doesn't occur in doctests):\n         * _render_on_subplot(self, subplot):\n\n----------------------------------------------------------------------\n```\n\nAnd I get some doctest failure, which are mostly numerical noise:\n\n```\nsage -t -long devel/sage-main/sage/calculus/riemann.pyx\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/calculus/riemann.pyx\", line 459:\n    sage: m.inverse_riemann_map(.95) #long time\nExpected:\n    (0.486319431795...-4.90019052414...e-06j)\nGot:\n    (0.48631943179594372-4.9001905240969853e-06j)\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/calculus/riemann.pyx\", line 394:\n    sage: m.riemann_map(1.3*I) #long time\nExpected:\n    (-1.56102939636...e-05+0.989694535737...j)\nGot:\n    (-1.5610293963970239e-05+0.98969453573774413j)\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/calculus/riemann.pyx\", line 398:\n    sage: m.riemann_map(.4) #long time\nExpected:\n    (0.733242677182...+3.50767714620...e-06j)\nGot:\n    (0.73324267718245462+3.5076771462558728e-06j)\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/calculus/riemann.pyx\", line 402:\n    sage: m.riemann_map(np.complex(-3,.0001)) #long time\nExpected:\n    (1.40575713549...e-05+1.05106170694...e-09j)\nGot:\n    (1.4057571354958779e-05+1.0510616458088591e-09j)\n**********************************************************************\n2 items had failures:\n   1 of   8 in __main__.example_10\n   3 of   9 in __main__.example_8\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_riemann.py\n\t [76.3 s]\n```\n",
    "created_at": "2009-08-31T07:40:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54557",
    "user": "mvngu"
}
```

I assume that patches should be merged in this order:

1. `12659.5.patch`
2. `12660.patch`

These patches apply OK against Sage 4.1.1, with `12660.patch` resulting in some fuzz:

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6648/12660.patch && hg qpush
adding 12660.patch to series file
applying 12660.patch
patching file module_list.py
Hunk #1 succeeded at 125 with fuzz 2 (offset 8 lines).
patching file sage/calculus/all.py
Hunk #1 succeeded at 20 with fuzz 2 (offset 4 lines).
Now at: 12660.patch
```

Don't worry about the fuzz. However, building the reference manual results in 17 warnings:

```
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: :0: (ERROR/3) Unexpected indentation.
WARNING: :0: (ERROR/3) Unexpected indentation.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/calculus/riemann.so:docstring of sage.calculus.riemann:3: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/calculus/riemann.so:docstring of sage.calculus.riemann:5: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/calculus/riemann.so:docstring of sage.calculus.riemann:3: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/calculus/riemann.so:docstring of sage.calculus.riemann:5: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/calculus/riemann.so:docstring of sage.calculus.riemann.ColorPlot.get_minmax_data:5: (ERROR/3) Unexpected indentation.
WARNING: <autodoc>:0: (ERROR/3) Unexpected indentation.
pickling environment... done
checking consistency... done
preparing documents... done
writing output... calculus index sage/calculus/interpolators sage/calculus/riemann 
writing additional files... genindex modindex search
copying static files... done
dumping search index... done
dumping object inventory... done
build succeeded, 17 warnings.
```

Two crucial doctests are missing:

```
[mvngu@sage sage-4.1.1]$ ./sage -coverage devel/sage-main/sage/calculus/interpolators.pyx
----------------------------------------------------------------------
devel/sage-main/sage/calculus/interpolators.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE devel/sage-main/sage/calculus/interpolators.pyx: 100% (8 of 8)
----------------------------------------------------------------------

[mvngu@sage sage-4.1.1]$ ./sage -coverage devel/sage-main/sage/calculus/riemann.pyx
----------------------------------------------------------------------
devel/sage-main/sage/calculus/riemann.pyx
ERROR: Please define a s == loads(dumps(s)) doctest.
SCORE devel/sage-main/sage/calculus/riemann.pyx: 100% (14 of 14)

Possibly wrong (function name doesn't occur in doctests):
         * _render_on_subplot(self, subplot):

----------------------------------------------------------------------
```

And I get some doctest failure, which are mostly numerical noise:

```
sage -t -long devel/sage-main/sage/calculus/riemann.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/calculus/riemann.pyx", line 459:
    sage: m.inverse_riemann_map(.95) #long time
Expected:
    (0.486319431795...-4.90019052414...e-06j)
Got:
    (0.48631943179594372-4.9001905240969853e-06j)
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/calculus/riemann.pyx", line 394:
    sage: m.riemann_map(1.3*I) #long time
Expected:
    (-1.56102939636...e-05+0.989694535737...j)
Got:
    (-1.5610293963970239e-05+0.98969453573774413j)
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/calculus/riemann.pyx", line 398:
    sage: m.riemann_map(.4) #long time
Expected:
    (0.733242677182...+3.50767714620...e-06j)
Got:
    (0.73324267718245462+3.5076771462558728e-06j)
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/calculus/riemann.pyx", line 402:
    sage: m.riemann_map(np.complex(-3,.0001)) #long time
Expected:
    (1.40575713549...e-05+1.05106170694...e-09j)
Got:
    (1.4057571354958779e-05+1.0510616458088591e-09j)
**********************************************************************
2 items had failures:
   1 of   8 in __main__.example_10
   3 of   9 in __main__.example_8
***Test Failed*** 4 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_riemann.py
	 [76.3 s]
```




---

archive/issue_comments_054558.json:
```json
{
    "body": "I don't think I saw any of these latex/noise problems with an intel mac 10.4.11. (I'll be upgrading very soon to 10.6, whcih might help though.) However, I did see the \"fuzz\" on applying 12660.patch. I didn't know that was a problem though.",
    "created_at": "2009-08-31T09:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54558",
    "user": "wdj"
}
```

I don't think I saw any of these latex/noise problems with an intel mac 10.4.11. (I'll be upgrading very soon to 10.6, whcih might help though.) However, I did see the "fuzz" on applying 12660.patch. I didn't know that was a problem though.



---

archive/issue_comments_054559.json:
```json
{
    "body": "Alright, I'm back to working on this again.\nQuestions:\n\nHow far should I tell the doctests to ignore the numerical noise? \nIs there some point where I should start trying to track down and fix the cause? \nIs that even possible?\n\nShould I be worried about the reference manual compilation warnings?",
    "created_at": "2009-10-03T18:18:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54559",
    "user": "evanandel"
}
```

Alright, I'm back to working on this again.
Questions:

How far should I tell the doctests to ignore the numerical noise? 
Is there some point where I should start trying to track down and fix the cause? 
Is that even possible?

Should I be worried about the reference manual compilation warnings?



---

archive/issue_comments_054560.json:
```json
{
    "body": "Attachment [trac_6648-reviewer.patch](tarball://root/attachments/some-uuid/ticket6648/trac_6648-reviewer.patch) by mvngu created at 2009-12-05 19:48:49\n\nbased on Sage 4.3.alpha1",
    "created_at": "2009-12-05T19:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54560",
    "user": "mvngu"
}
```

Attachment [trac_6648-reviewer.patch](tarball://root/attachments/some-uuid/ticket6648/trac_6648-reviewer.patch) by mvngu created at 2009-12-05 19:48:49

based on Sage 4.3.alpha1



---

archive/issue_comments_054561.json:
```json
{
    "body": "**Referee Report**\n\n\n\nI have attached the reviewer patch `trac_6648-reviewer.patch`. My changes include:\n\n1. Proper ReST formatting to resolve dozens of warnings when building the HTML version of the reference manual.\n2. Fix various typos.\n3. Some formatting of the docstrings to keep them less than 80 characters wide. Beyond 80 characters, the docstring can be difficult to read from the command line interface.\n4. Proper formatting of code so it conforms to Python coding conventions as covered in the [Developers' Guide](http://www.sagemath.org/doc/developer/conventions.html#python-coding-conventions).\n5. In the file `sage/calculus/riemann.pyx`, don't redefine `xrange`, which is a built-in command of Python. Instead, define `x_range` and similarly define `y_range`. Also, don't use the name `list` as a parameter to the function `comp_pt()` because `list` is the name of the Python function for creating a list data structure. I have changed it to `clist` instead.\n6. For the file `sage/calculus/riemann.pyx`, in the `__init__()` method of the class `Riemann_Map`, I changed the test\n {{{\nif <= 2:\n    ...\n }}}\n to raise an exception instead. That is, if the number of collocations points is less than 3, then you don't want to proceed any further with initializing the `Riemann_Map` object.\n\n\nYou should apply patches in this order:\n\n1. `12659.5.patch`\n2. `12660.patch`\n3. `trac_6648-reviewer.patch`\n \nThe reviewer patch should resolve doctest failures and reference manual build warnings that I reported above. So my patch needs some reviewing. Also, here are some required changes once patches are applied in the above order:\n\n1. In the file `sage/calculus/riemann.pyx`, you need to explain what the function `_render_on_subplot` does.\n2. Also, you need to explain the purpose of the class `ColorPlot` and provide examples in the docstring of that class.\n3. In the file `sage/calculus/interpolators.pyx`, explain the purpose of the class `PSpline` and provide examples in the docstring of that class.\n4. Explain the purpose of the class `CCSpline` and provide examples in its docstring.",
    "created_at": "2009-12-05T19:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54561",
    "user": "mvngu"
}
```

**Referee Report**



I have attached the reviewer patch `trac_6648-reviewer.patch`. My changes include:

1. Proper ReST formatting to resolve dozens of warnings when building the HTML version of the reference manual.
2. Fix various typos.
3. Some formatting of the docstrings to keep them less than 80 characters wide. Beyond 80 characters, the docstring can be difficult to read from the command line interface.
4. Proper formatting of code so it conforms to Python coding conventions as covered in the [Developers' Guide](http://www.sagemath.org/doc/developer/conventions.html#python-coding-conventions).
5. In the file `sage/calculus/riemann.pyx`, don't redefine `xrange`, which is a built-in command of Python. Instead, define `x_range` and similarly define `y_range`. Also, don't use the name `list` as a parameter to the function `comp_pt()` because `list` is the name of the Python function for creating a list data structure. I have changed it to `clist` instead.
6. For the file `sage/calculus/riemann.pyx`, in the `__init__()` method of the class `Riemann_Map`, I changed the test
 {{{
if <= 2:
    ...
 }}}
 to raise an exception instead. That is, if the number of collocations points is less than 3, then you don't want to proceed any further with initializing the `Riemann_Map` object.


You should apply patches in this order:

1. `12659.5.patch`
2. `12660.patch`
3. `trac_6648-reviewer.patch`
 
The reviewer patch should resolve doctest failures and reference manual build warnings that I reported above. So my patch needs some reviewing. Also, here are some required changes once patches are applied in the above order:

1. In the file `sage/calculus/riemann.pyx`, you need to explain what the function `_render_on_subplot` does.
2. Also, you need to explain the purpose of the class `ColorPlot` and provide examples in the docstring of that class.
3. In the file `sage/calculus/interpolators.pyx`, explain the purpose of the class `PSpline` and provide examples in the docstring of that class.
4. Explain the purpose of the class `CCSpline` and provide examples in its docstring.



---

archive/issue_comments_054562.json:
```json
{
    "body": "I don't mind refereeing this after next week, but would first like to know\nthe author's response to this patch. Possibly another patch needs to be added?\n\nAlso, thanks Minh!\n\nReplying to [comment:24 mvngu]:\n> **Referee Report**\n> \n\n> \n> I have attached the reviewer patch `trac_6648-reviewer.patch`. My changes include:\n> \n>  1. Proper ReST formatting to resolve dozens of warnings when building the HTML version of the reference manual.\n>  1. Fix various typos.\n>  1. Some formatting of the docstrings to keep them less than 80 characters wide. Beyond 80 characters, the docstring can be difficult to read from the command line interface.\n>  1. Proper formatting of code so it conforms to Python coding conventions as covered in the [Developers' Guide](http://www.sagemath.org/doc/developer/conventions.html#python-coding-conventions).\n>  1. In the file `sage/calculus/riemann.pyx`, don't redefine `xrange`, which is a built-in command of Python. Instead, define `x_range` and similarly define `y_range`. Also, don't use the name `list` as a parameter to the function `comp_pt()` because `list` is the name of the Python function for creating a list data structure. I have changed it to `clist` instead.\n>  1. For the file `sage/calculus/riemann.pyx`, in the `__init__()` method of the class `Riemann_Map`, I changed the test\n>  {{{\n> if <= 2:\n>     ...\n>  }}}\n>  to raise an exception instead. That is, if the number of collocations points is less than 3, then you don't want to proceed any further with initializing the `Riemann_Map` object.\n> \n> \n> You should apply patches in this order:\n> \n>  1. `12659.5.patch`\n>  1. `12660.patch`\n>  1. `trac_6648-reviewer.patch`\n>  \n> The reviewer patch should resolve doctest failures and reference manual build warnings that I reported above. So my patch needs some reviewing. Also, here are some required changes once patches are applied in the above order:\n> \n>  1. In the file `sage/calculus/riemann.pyx`, you need to explain what the function `_render_on_subplot` does.\n>  1. Also, you need to explain the purpose of the class `ColorPlot` and provide examples in the docstring of that class.\n>  1. In the file `sage/calculus/interpolators.pyx`, explain the purpose of the class `PSpline` and provide examples in the docstring of that class.\n>  1. Explain the purpose of the class `CCSpline` and provide examples in its docstring.",
    "created_at": "2009-12-05T23:00:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54562",
    "user": "wdj"
}
```

I don't mind refereeing this after next week, but would first like to know
the author's response to this patch. Possibly another patch needs to be added?

Also, thanks Minh!

Replying to [comment:24 mvngu]:
> **Referee Report**
> 

> 
> I have attached the reviewer patch `trac_6648-reviewer.patch`. My changes include:
> 
>  1. Proper ReST formatting to resolve dozens of warnings when building the HTML version of the reference manual.
>  1. Fix various typos.
>  1. Some formatting of the docstrings to keep them less than 80 characters wide. Beyond 80 characters, the docstring can be difficult to read from the command line interface.
>  1. Proper formatting of code so it conforms to Python coding conventions as covered in the [Developers' Guide](http://www.sagemath.org/doc/developer/conventions.html#python-coding-conventions).
>  1. In the file `sage/calculus/riemann.pyx`, don't redefine `xrange`, which is a built-in command of Python. Instead, define `x_range` and similarly define `y_range`. Also, don't use the name `list` as a parameter to the function `comp_pt()` because `list` is the name of the Python function for creating a list data structure. I have changed it to `clist` instead.
>  1. For the file `sage/calculus/riemann.pyx`, in the `__init__()` method of the class `Riemann_Map`, I changed the test
>  {{{
> if <= 2:
>     ...
>  }}}
>  to raise an exception instead. That is, if the number of collocations points is less than 3, then you don't want to proceed any further with initializing the `Riemann_Map` object.
> 
> 
> You should apply patches in this order:
> 
>  1. `12659.5.patch`
>  1. `12660.patch`
>  1. `trac_6648-reviewer.patch`
>  
> The reviewer patch should resolve doctest failures and reference manual build warnings that I reported above. So my patch needs some reviewing. Also, here are some required changes once patches are applied in the above order:
> 
>  1. In the file `sage/calculus/riemann.pyx`, you need to explain what the function `_render_on_subplot` does.
>  1. Also, you need to explain the purpose of the class `ColorPlot` and provide examples in the docstring of that class.
>  1. In the file `sage/calculus/interpolators.pyx`, explain the purpose of the class `PSpline` and provide examples in the docstring of that class.
>  1. Explain the purpose of the class `CCSpline` and provide examples in its docstring.



---

archive/issue_comments_054563.json:
```json
{
    "body": "Thank you Minh. \nI will happily put up another patch with the doc additions you suggested. However, exams are starting for me, so I probably won't be able to get around to it for 2 weeks or so.\n\nIn addition, it's not clear to me that your patch fixes the primary problem, namely that the class doesn't know how to dump/save itself, and therefore wont pass the TestSuite test. Fixing that is outside my abilities.",
    "created_at": "2009-12-09T05:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54563",
    "user": "evanandel"
}
```

Thank you Minh. 
I will happily put up another patch with the doc additions you suggested. However, exams are starting for me, so I probably won't be able to get around to it for 2 weeks or so.

In addition, it's not clear to me that your patch fixes the primary problem, namely that the class doesn't know how to dump/save itself, and therefore wont pass the TestSuite test. Fixing that is outside my abilities.



---

archive/issue_comments_054564.json:
```json
{
    "body": "Replying to [comment:26 evanandel]:\n> In addition, it's not clear to me that your patch fixes the primary problem, namely that the class doesn't know how to dump/save itself, and therefore wont pass the TestSuite test. Fixing that is outside my abilities.\n\nAh... I forgot about the dump/save test. I'll work on that.",
    "created_at": "2009-12-09T05:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54564",
    "user": "mvngu"
}
```

Replying to [comment:26 evanandel]:
> In addition, it's not clear to me that your patch fixes the primary problem, namely that the class doesn't know how to dump/save itself, and therefore wont pass the TestSuite test. Fixing that is outside my abilities.

Ah... I forgot about the dump/save test. I'll work on that.



---

archive/issue_comments_054565.json:
```json
{
    "body": "Replying to [comment:27 mvngu]:\n> Replying to [comment:26 evanandel]:\n> > In addition, it's not clear to me that your patch fixes the primary problem, namely that the class doesn't know how to dump/save itself, and therefore wont pass the TestSuite test. Fixing that is outside my abilities.\n> \n> Ah... I forgot about the dump/save test. I'll work on that.\nSorry for the delay, this project has been buried for a while for me. I should have my patch up in a week or so.\n\nMinh, did you ever have any luck addressing the TestSuite issue?\nI'd really like to see this get finalized and out there.",
    "created_at": "2010-03-20T02:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54565",
    "user": "evanandel"
}
```

Replying to [comment:27 mvngu]:
> Replying to [comment:26 evanandel]:
> > In addition, it's not clear to me that your patch fixes the primary problem, namely that the class doesn't know how to dump/save itself, and therefore wont pass the TestSuite test. Fixing that is outside my abilities.
> 
> Ah... I forgot about the dump/save test. I'll work on that.
Sorry for the delay, this project has been buried for a while for me. I should have my patch up in a week or so.

Minh, did you ever have any luck addressing the TestSuite issue?
I'd really like to see this get finalized and out there.



---

archive/issue_comments_054566.json:
```json
{
    "body": "Replying to [comment:28 evanandel]:\n> Minh, did you ever have any luck addressing the TestSuite issue?\n> I'd really like to see this get finalized and out there.\n\nI must apologize for the delay. I'm just as stuck as you are concerning the TestSuite thing. Please see my post to [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/2d84701b47e6d3ee).",
    "created_at": "2010-03-20T02:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54566",
    "user": "mvngu"
}
```

Replying to [comment:28 evanandel]:
> Minh, did you ever have any luck addressing the TestSuite issue?
> I'd really like to see this get finalized and out there.

I must apologize for the delay. I'm just as stuck as you are concerning the TestSuite thing. Please see my post to [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/2d84701b47e6d3ee).



---

archive/issue_comments_054567.json:
```json
{
    "body": "Doc fixes",
    "created_at": "2010-03-31T04:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54567",
    "user": "evanandel"
}
```

Doc fixes



---

archive/issue_comments_054568.json:
```json
{
    "body": "Attachment [12661.patch](tarball://root/attachments/some-uuid/ticket6648/12661.patch) by evanandel created at 2010-03-31 04:20:24\n\nOk, I've put up a patch that fixes the missing documentation. Note that the relatively sparse documentation in the ColorPlot and _render_on_subplot is more than exists in the complex_plot module from which I obtained the code.\n\nAt this point all that is required is some kind knowledgeable soul to implement dump/load functionality so that the modules can pass the TestSuite requirement. Alternately direct me to a resource that provides an in depth tutorial on how to implement it. I appreciate all the help so far, and I would really like to get this published. If there's anything that I can do to speed it up, let me know.",
    "created_at": "2010-03-31T04:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54568",
    "user": "evanandel"
}
```

Attachment [12661.patch](tarball://root/attachments/some-uuid/ticket6648/12661.patch) by evanandel created at 2010-03-31 04:20:24

Ok, I've put up a patch that fixes the missing documentation. Note that the relatively sparse documentation in the ColorPlot and _render_on_subplot is more than exists in the complex_plot module from which I obtained the code.

At this point all that is required is some kind knowledgeable soul to implement dump/load functionality so that the modules can pass the TestSuite requirement. Alternately direct me to a resource that provides an in depth tutorial on how to implement it. I appreciate all the help so far, and I would really like to get this published. If there's anything that I can do to speed it up, let me know.



---

archive/issue_comments_054569.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-04-01T12:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54569",
    "user": "wdj"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_054570.json:
```json
{
    "body": "I applied 12659.5.patch, 12660.patch, trac_6648-reviewer.patch without much problem (there were some fuzz warnings). However, 12661.patch failed to apply. This is on a 10.6.2 mac running sage 4.3.5.\n\nThere is no indication which patches to apply, so maybe this is not the intended sequence?",
    "created_at": "2010-04-01T12:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54570",
    "user": "wdj"
}
```

I applied 12659.5.patch, 12660.patch, trac_6648-reviewer.patch without much problem (there were some fuzz warnings). However, 12661.patch failed to apply. This is on a 10.6.2 mac running sage 4.3.5.

There is no indication which patches to apply, so maybe this is not the intended sequence?



---

archive/issue_comments_054571.json:
```json
{
    "body": "New Monolithic patch. Apply only this one.",
    "created_at": "2010-04-20T01:40:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54571",
    "user": "evanandel"
}
```

New Monolithic patch. Apply only this one.



---

archive/issue_comments_054572.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-04-20T01:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54572",
    "user": "evanandel"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_054573.json:
```json
{
    "body": "Attachment [13911.patch](tarball://root/attachments/some-uuid/ticket6648/13911.patch) by evanandel created at 2010-04-20 01:41:00\n\nMy apologies, I apparently made some mistakes with mercurial and somehow produced someone else's patch. Regardless, I have created a new, monolithic patch that should be applied INSTEAD of applying the previous patches. It incorporates all the changes so far including the ones that I intended to be in 12661.",
    "created_at": "2010-04-20T01:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54573",
    "user": "evanandel"
}
```

Attachment [13911.patch](tarball://root/attachments/some-uuid/ticket6648/13911.patch) by evanandel created at 2010-04-20 01:41:00

My apologies, I apparently made some mistakes with mercurial and somehow produced someone else's patch. Regardless, I have created a new, monolithic patch that should be applied INSTEAD of applying the previous patches. It incorporates all the changes so far including the ones that I intended to be in 12661.



---

archive/issue_comments_054574.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-22T11:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54574",
    "user": "wdj"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054575.json:
```json
{
    "body": "This patch applies fine to 4.4.a1 and passes sage -testall on a 10.6.2 mac (except for the already reported and unrelated r.py failure). Also, sage -coverage reports 100%. It produces some cool graphs and I think will help people doing teaching or research in classical complex analysis.\n\nPositive review from me.",
    "created_at": "2010-04-22T11:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54575",
    "user": "wdj"
}
```

This patch applies fine to 4.4.a1 and passes sage -testall on a 10.6.2 mac (except for the already reported and unrelated r.py failure). Also, sage -coverage reports 100%. It produces some cool graphs and I think will help people doing teaching or research in classical complex analysis.

Positive review from me.



---

archive/issue_comments_054576.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-22T11:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54576",
    "user": "wdj"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054577.json:
```json
{
    "body": "As far as I can see, the author has addressed the comments of Martin and Minh above.",
    "created_at": "2010-04-22T11:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54577",
    "user": "wdj"
}
```

As far as I can see, the author has addressed the comments of Martin and Minh above.



---

archive/issue_comments_054578.json:
```json
{
    "body": "I'm excited to explore this functionality and show it to a fellow faculty member who does projects with students in complex analysis.\n\nThings could probably be sped up quite a bit if the class used fast_callable to \"compile\" the functions.\u00a0 For example:\n\n\n```\nsage: ff=fast_callable(e^(I*t),domain=CDF,vars=['t'])\nsage: gg=fast_callable(I*e^(I*t),domain=CDF,vars=['t'])\nsage: %time m = Riemann_Map([ff], [gg], 0, 1000)\nCPU times: user 2.44 s, sys: 0.12 s, total: 2.56 s\nWall time: 2.57 s\nsage: %time m = Riemann_Map([lambda t: e^(I*t)], [lambda t: I*e^(I*t)], 0, 1000) \nCPU times: user 21.25 s, sys: 0.25 s, total: 21.50 s\nWall time: 23.13 s\n```\n\n\nNotice that the fast_callable version is an order of magnitude faster.\n\nI don't think this patch ought to be delayed for this, but it would be a good additional ticket to speed up this functionality quite a bit by using fast_callable.",
    "created_at": "2010-04-24T00:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54578",
    "user": "jason"
}
```

I'm excited to explore this functionality and show it to a fellow faculty member who does projects with students in complex analysis.

Things could probably be sped up quite a bit if the class used fast_callable to "compile" the functions.  For example:


```
sage: ff=fast_callable(e^(I*t),domain=CDF,vars=['t'])
sage: gg=fast_callable(I*e^(I*t),domain=CDF,vars=['t'])
sage: %time m = Riemann_Map([ff], [gg], 0, 1000)
CPU times: user 2.44 s, sys: 0.12 s, total: 2.56 s
Wall time: 2.57 s
sage: %time m = Riemann_Map([lambda t: e^(I*t)], [lambda t: I*e^(I*t)], 0, 1000) 
CPU times: user 21.25 s, sys: 0.25 s, total: 21.50 s
Wall time: 23.13 s
```


Notice that the fast_callable version is an order of magnitude faster.

I don't think this patch ought to be delayed for this, but it would be a good additional ticket to speed up this functionality quite a bit by using fast_callable.



---

archive/issue_comments_054579.json:
```json
{
    "body": "Good point Jason.\n\nStarting next fall I plan to develop this further as my senior project in math and CS. I have several ideas planned including parallelization and fast-callable. However, if it would be helpful to have it sooner rather than later, I have no problem doing some basic work now (or having someone else do it if that is preferred).",
    "created_at": "2010-04-24T04:40:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54579",
    "user": "evanandel"
}
```

Good point Jason.

Starting next fall I plan to develop this further as my senior project in math and CS. I have several ideas planned including parallelization and fast-callable. However, if it would be helpful to have it sooner rather than later, I have no problem doing some basic work now (or having someone else do it if that is preferred).



---

archive/issue_comments_054580.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T05:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6648#issuecomment-54580",
    "user": "was"
}
```

Resolution: fixed
