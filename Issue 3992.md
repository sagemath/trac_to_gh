# Issue 3992: Sage 3.1.2.alpha2: three tests in sage/interfaces/octave.py need to be optional

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-08-29 17:07:08

Assignee: mabshoff

CC:  cremona


```
sage -t  devel/sage/sage/interfaces/octave.py 
********************************************************************** 
File "/home/jec/sage-3.1.2.alpha2/tmp/octave.py", line 279: 
    sage: octave.set('x', '2') #optonal -- requires Octave 
Exception raised: 
    Traceback (most recent call last): 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/doctest.py", 
line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_10[2]>", line 1, in <module> 
        octave.set('x', '2') #optonal -- requires Octave###line 279: 
    sage: octave.set('x', '2') #optonal -- requires Octave 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py", 
line 284, in set 
        out = self.eval(cmd) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 935, in eval 
        return '\n'.join([self._eval_line(L, **kwds) for L in 
code.split('\n') if L != '']) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 631, in _eval_line 
        self._start() 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py", 
line 270, in _start 
        Expect._start(self) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 455, in _start 
        self.__name, cmd, self._install_hints()) 
    RuntimeError: Unable to start octave because the command 'octave 
--no-line-editing --silent' failed. 
            You must get the program "octave" in order to use Octave 
            from SAGE.   You can read all about Octave at 
                    http://www.gnu.org/software/octave/ 
            LINUX / WINDOWS (colinux): 
               Do apt-get install octave as root on your machine 
               (or, in Windows, in the colinux console). 
            OS X: 
               * This website has links to binaries for OS X PowerPC 
                 and OS X Intel builds of the latest version of Octave: 
                         http://hpc.sourceforge.net/ 
                 Once you get the tarball from there, go to the / directory 
                 and type 
                         tar zxvf octave-intel-bin.tar.gz 
                 to extract it to usr/local/...   Make sure /usr/local/bin 
                 is in your PATH.  Then type "octave" and verify that 
                 octave starts up. 
               * Darwin ports and fink have Octave as well. 
********************************************************************** 
File "/home/jec/sage-3.1.2.alpha2/tmp/octave.py", line 293: 
    sage: octave.set('x', '2') #optonal -- requires Octave 
Exception raised: 
    Traceback (most recent call last): 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/doctest.py", 
line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_11[2]>", line 1, in <module> 
        octave.set('x', '2') #optonal -- requires Octave###line 293: 
    sage: octave.set('x', '2') #optonal -- requires Octave 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py", 
line 284, in set 
        out = self.eval(cmd) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 935, in eval 
        return '\n'.join([self._eval_line(L, **kwds) for L in 
code.split('\n') if L != '']) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 631, in _eval_line 
        self._start() 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py", 
line 270, in _start 
        Expect._start(self) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 455, in _start 
        self.__name, cmd, self._install_hints()) 
    RuntimeError: Unable to start octave because the command 'octave 
--no-line-editing --silent' failed. 
            You must get the program "octave" in order to use Octave 
            from SAGE.   You can read all about Octave at 
                    http://www.gnu.org/software/octave/ 
            LINUX / WINDOWS (colinux): 
               Do apt-get install octave as root on your machine 
               (or, in Windows, in the colinux console). 
            OS X: 
               * This website has links to binaries for OS X PowerPC 
                 and OS X Intel builds of the latest version of Octave: 
                         http://hpc.sourceforge.net/ 
                 Once you get the tarball from there, go to the / directory 
                 and type 
                         tar zxvf octave-intel-bin.tar.gz 
                 to extract it to usr/local/...   Make sure /usr/local/bin 
                 is in your PATH.  Then type "octave" and verify that 
                 octave starts up. 
               * Darwin ports and fink have Octave as well. 
********************************************************************** 
File "/home/jec/sage-3.1.2.alpha2/tmp/octave.py", line 306: 
    sage: octave.set('x', '2') #optonal -- requires Octave 
Exception raised: 
    Traceback (most recent call last): 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/doctest.py", 
line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_12[2]>", line 1, in <module> 
        octave.set('x', '2') #optonal -- requires Octave###line 306: 
    sage: octave.set('x', '2') #optonal -- requires Octave 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py", 
line 284, in set 
        out = self.eval(cmd) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 935, in eval 
        return '\n'.join([self._eval_line(L, **kwds) for L in 
code.split('\n') if L != '']) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 631, in _eval_line 
        self._start() 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/octave.py", 
line 270, in _start 
        Expect._start(self) 
      File "/home/jec/sage-3.1.2.alpha2/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 455, in _start 
        self.__name, cmd, self._install_hints()) 
    RuntimeError: Unable to start octave because the command 'octave 
--no-line-editing --silent' failed. 
            You must get the program "octave" in order to use Octave 
            from SAGE.   You can read all about Octave at 
                    http://www.gnu.org/software/octave/ 
            LINUX / WINDOWS (colinux): 
               Do apt-get install octave as root on your machine 
               (or, in Windows, in the colinux console). 
            OS X: 
               * This website has links to binaries for OS X PowerPC 
                 and OS X Intel builds of the latest version of Octave: 
                         http://hpc.sourceforge.net/ 
                 Once you get the tarball from there, go to the / directory 
                 and type 
                         tar zxvf octave-intel-bin.tar.gz 
                 to extract it to usr/local/...   Make sure /usr/local/bin 
                 is in your PATH.  Then type "octave" and verify that 
                 octave starts up. 
               * Darwin ports and fink have Octave as well. 
********************************************************************** 
3 items had failures: 
   1 of   3 in __main__.example_10 
   1 of   3 in __main__.example_11 
   1 of   3 in __main__.example_12 
***Test Failed*** 3 failures. 
For whitespace errors, see the file 
/home/jec/sage-3.1.2.alpha2/tmp/.doctest_octave.py 
```



---

Comment by mabshoff created at 2008-08-29 17:07:21

Changing status from new to assigned.


---

Attachment

John,

since you hit this can you do the (trivial) review?

Cheers,

Michael


---

Comment by cremona created at 2008-08-29 18:16:25

Patch applies and pases doctests on both the systems where it failed before.

Done!


---

Comment by mabshoff created at 2008-08-29 18:29:24

Merged in Sage 3.1.2.alpha3


---

Comment by mabshoff created at 2008-08-29 18:29:24

Resolution: fixed
