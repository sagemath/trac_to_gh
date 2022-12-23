# Issue 7995: sage-test doesn't handle all of sage-doctest's return values

Issue created by migration from https://trac.sagemath.org/ticket/7995

Original creator: wjp

Original creation time: 2010-01-19 07:38:35

Assignee: tbd

The `sage-doctest` script returns some status info in its exit code, like if it was aborted with a `KeyboardInterrupt`. The `sage-ptest` script interprets this information, but `sage-test` mostly ignores it.

One symptom is that Ctrl-C-ing a `sage -t` run of multiple files doesn't work.


---

Comment by wjp created at 2010-01-20 02:12:31

Changing status from new to needs_review.


---

Comment by wjp created at 2010-01-20 02:13:27

Patch attached.

In the future we may want to merge the sage-ptest and sage-test scripts entirely. They have a lot of duplicate code and minor unnecessary differences.


---

Attachment


---

Comment by nthiery created at 2010-01-20 08:59:29

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2010-01-20 08:59:29

I don't know much the doctest framework. But the code looks good, and this removes two seriously annoying misfeatures of doctests. Thanks so much for scratching this itch for me!

Quick remarks:

 - When there is an exception in the doctesting framework; will we get
   a traceback? That would be most handy!

 - in "... Check the process exit codes ...": codes -> code?

 - The following two comments seem contradictory. Or am I
   misunderstanding something?

> # Return value in process exit code: 
> # 0: all tests passed 
> # 1: file not found 
> # 2: KeyboardInterrupt 
> # 3: doctest process was terminated by a signal 
> # 4: the doctesting framework raised an exception 
> # 100: failed doctests 
> #################################################################### 
>
> def test_code(filename): 
>     # Return value in the doctest process exit code: 
>     # 0: everything passed 
>     # 1-253: number of failed doctests 
>     # 254: >= 254 doctests failed 
>     # 255: exception raised by doctesting framework


---

Comment by nthiery created at 2010-01-20 09:01:09

Sorry, I screwed up my citation. Here it is again.

 - The following two comments seem contradictory. Or am I
   misunderstanding something?


```
 # Return value in process exit code: 
 # 0: all tests passed 
 # 1: file not found 
 # 2: KeyboardInterrupt 
 # 3: doctest process was terminated by a signal 
 # 4: the doctesting framework raised an exception 
 # 100: failed doctests 
 #################################################################### 

 def test_code(filename): 
     # Return value in the doctest process exit code: 
     # 0: everything passed 
     # 1-253: number of failed doctests 
     # 254: >= 254 doctests failed 
     # 255: exception raised by doctesting framework 
```



---

Comment by nthiery created at 2010-01-20 09:05:40

Replying to [comment:4 nthiery]:
> Sorry, I screwed up my citation. Here it is again.

Oops again. This remark is actually about #7993. I was looking at both, and got confused.


---

Comment by wjp created at 2010-01-20 17:44:11

Thanks for the feedback.

The `sage-doctest` script generates a new python file that runs the actual doctests, and runs this script in a seperate thread. The second block of process exit codes are for this 'inner' doctest process. I'll clarify the confusing comment (and fix the typo you mentioned).

As for the exception: you can get a traceback if you re-run with the -verbose. Do you think we should show them by default?


---

Comment by wjp created at 2010-01-20 18:54:27

I attached a new patch to #7993 that changes the exit code comments.


---

Comment by AlexGhitza created at 2010-01-23 01:15:17

Changing status from needs_work to needs_review.


---

Comment by AlexGhitza created at 2010-01-23 01:31:17

I played with this a bit and it works well.


---

Comment by AlexGhitza created at 2010-01-23 01:31:17

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-23 09:58:40

Merged in the script repository.


---

Comment by mvngu created at 2010-01-23 09:58:40

Resolution: fixed


---

Comment by ddrake created at 2010-04-13 13:26:42

The patch here doesn't work; it exits sage-doctest with sys.exit(2), and then munges the error code with "err = err // 256" -- that is, it does floor division by 256, so the 2 becomes 0 and KeyboardInterrupts are never detected!

I hope to fix this while working on #8641.


---

Comment by wjp created at 2010-04-13 13:41:27

I tested this, and it worked for me, as well as matching what the python docs say it does on unix systems. Does it not work on your system?

The python docs for `os.system`:


```
On Unix, the return value is the exit status of the process encoded in
the format specified for wait().
```


And for `os.wait`:


```
Wait for completion of a child process, and return a tuple containing
its pid and exit status indication: a 16-bit number, whose low byte is
the signal number that killed the process, and whose high byte is the
exit status (if the signal number is zero); the high bit of the low byte
is set if a core file was produced. Availability: Unix.
```



---

Comment by jhpalmieri created at 2010-04-13 20:19:21

See #8641 for a followup.


---

Comment by ddrake created at 2010-04-13 22:05:05

Replying to [comment:12 wjp]:
> I tested this, and it worked for me, as well as matching what the python docs say it does on unix systems. Does it not work on your system?

No, it doesn't. I'll work on this more, but I know that, on my Ubuntu 9.10 system, if I ctrl-c while running tests on a bunch of files, it doesn't interrupt the whole process. In sage-test, I have this:

```
print 'finished with %s, err: %s' % (F, err)
err = err // 256
print 'finished with %s, err: %s' % (F, err)
```

and here's what I get:

```
drake@sagenb:~/s/sage-4.3.5$ ./sage -t devel/sage/sage/combinat/t*.py
sage -t  "devel/sage/sage/combinat/tableau.py"              
^CKeyboardInterrupt -- interrupted after 2.3 seconds!
finished with devel/sage/sage/combinat/tableau.py, err: 2
finished with devel/sage/sage/combinat/tableau.py, err: 0
         [2.4 s]
sage -t  "devel/sage/sage/combinat/tools.py"                
finished with devel/sage/sage/combinat/tools.py, err: 0
finished with devel/sage/sage/combinat/tools.py, err: 0
         [1.6 s]
sage -t  "devel/sage/sage/combinat/tuple.py"                
finished with devel/sage/sage/combinat/tuple.py, err: 0
finished with devel/sage/sage/combinat/tuple.py, err: 0
         [2.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 6.2 seconds
```


I'm not sure why this isn't working.


---

Comment by jhpalmieri created at 2010-04-13 22:28:11

I put in a few print statements, like Dan did:

```
    print err,
    err = err // 256
    print err
```

On my iMac running OS X 10.6, when I hit ctrl-C, I see

```
515 2
```

which looks okay.

On sage.math, I see

```
2 0
```

which doesn't.
