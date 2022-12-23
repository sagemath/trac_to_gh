# Issue 4366: sys.path is searched ("stat"ed) for *.pyx-files insanely often

Issue created by migration from https://trac.sagemath.org/ticket/4366

Original creator: GeorgSWeber

Original creation time: 2008-10-24 21:05:30

Assignee: somebody

CC:  robertwb

Hi, Emmanuel Thomé noted that
there is a speed/system call activity regression in between Sage 3.0.5 and 3.1.3.
If in Sage 3.1.3/3.1.4/3.2.alpha0 one issues something like

```
sage: time for i in range(10): float(1)/2
```

and looks at the same at the system call activity of this python "sage.bin" process (in another terminal with something like "strace -p 'pidof sage.bin' -e trace='stat'" under Linux, or using "sudo fs_usage 4711" under Mac OS X, 4711 being the sage.bin pid gotten e.g. via the activity tool), then one sees:

The (sage/python) sys.path is searched by the system call "stat" for "coerce.pyx", "coerce_maps.pyx", "parent.pyx" and "integer.pyx" many times, that whole path, and over and over again.

This does not happen under Sage 3.0.5.

Willem Jan Palenstijn proposed this code fragment, which triggers the behaviour in Sage 3.2.alpha0, too:

```
sage: cm=sage.structure.element.get_coercion_model()
sage: cm.canonical_coercion(float(1),1)
```

and noted that

"This seems to be the _record_exception() function in the coercion model."

(See also the recent sage_devel thread started by Emmanuel Thomé about this.)



---

Comment by GeorgSWeber created at 2008-10-26 21:05:42

Changing assignee from somebody to GeorgSWeber.


---

Comment by GeorgSWeber created at 2008-10-26 21:14:12

I know now how to change the code so that when we had before:

```
sage: time for i in range(10^4): float(1)/2
CPU times: user 17.72 s, sys: 13.44 s, total: 31.16 s
Wall time: 31.20 s
```

then after the changes we get:

```
sage: time for i in range(10^4): float(1)/2
CPU times: user 0.37 s, sys: 0.00 s, total: 0.37 s
Wall time: 0.37 s
```

which is quite impressive, I think (the sys time is used up only by these insanely many calls to "stat")!

Essentially all one has to do is not to call "sys.exc_info()" in "_record_exception" (file: sage/structure/coerce.pyx) unless you really want to do so. But to fix that nicely (e.g. not leaving a broken doctest) will take me another evening or two.


---

Comment by GeorgSWeber created at 2008-10-26 21:14:12

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-10-26 21:24:57

Very, very nice. Any chance that RobertWB might have some clue here? I would really like to have this fixed in 3.2 :)

Cheers,

Michael


---

Comment by robertwb created at 2008-10-27 16:42:41

Coincidentally, I just responded to this thread on sage-devel. I'll repost here 


```
Thanks for tracking this down. Just out of curiosity, how does one decide if one "really wants to." Ideally one could snapshot the traceback without touching every file involved.

BTW, using RDF rather than float will be 10x faster in this case even after your speedup.

sage: sage: time for i in range(10^4): RDF(1)/2
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.03 s

- Robert

```


The point is that when something goes wrong, one wants to be able to ask "what happened" which is why these tracebacks are stored. Re-running the command may not give you all the information because of the caching involved. Is there a better way to get the traceback information than invoking sys.exc_info?


---

Attachment


---

Comment by GeorgSWeber created at 2008-10-27 23:36:03

Oops,
I had cached this page in my browser so your point about caching completely went past me up to now.

Hmmmmmm.

My first feeling about this that whenever one gets a such failure, it is important to be able to reproduce it. If so, then this means you can "rerun" the code.
If not, then you are hunting some "sporadic" phantom.
In that case, one should have "enabled the exception stack" all the time.

But for everyday usage of Sage, it might be allowable to have this feature disabled, considering its costs. 

Cheers,
gsw


---

Comment by robertwb created at 2008-10-28 00:47:26

The coercion model caching what the right action is is essential to its speed, so the behavior remains the same but it remembers to not go down (all) the failed code paths the next time around. The only exceptions are float+ZZ and float+QQ. There's a ticket to handle these better. 

One should be able to cache the exceptions *without* stating every file in the path, and I think this is what we should do.


---

Comment by mabshoff created at 2008-10-28 02:32:38

Replying to [comment:7 robertwb]:
> The coercion model caching what the right action is is essential to its speed, so the behavior remains the same but it remembers to not go down (all) the failed code paths the next time around. The only exceptions are float+ZZ and float+QQ. There's a ticket to handle these better. 

Which ticket would that be?

> One should be able to cache the exceptions *without* stating every file in the path, and I think this is what we should do. 

I agree. The patch might solve the problem, but Robert's suggestion to solve the problem should be preferred.

Cheers,

Michael


---

Attachment

apply this patch only


---

Comment by robertwb created at 2008-10-28 06:57:05

As it turns out, it's the formating of the exceptions that's expensive, not the call to sys.exc_info. This is good news for us, as we can defer that to later. See attached patch.


---

Comment by robertwb created at 2008-10-28 06:59:08

The aforementioned tickets would be #3938 and #2898


---

Comment by GeorgSWeber created at 2008-10-28 08:02:00

Excellent!
And this is how solutions evolve:
1. primitive (just comment out the last line of _record_exception)
2. complicated (my patch)
3. simple (Robert's patch)

I have to go to work now, but I'll try hard to run and review the patch this evening.
(It looks perfect at first sight.)

Cheers,
gsw


---

Comment by mabshoff created at 2008-10-28 12:48:14

With RobertWB's patch applied I am seeing one easy to fix doctest failure:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha2$ ./sage -t -long devel/sage/sage/structure/coerce.pyx
sage -t -long devel/sage/sage/structure/coerce.pyx          
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha2/tmp/coerce.py", line 331:
    sage: cm.exception_stack()
Expected:
    [(<type 'exceptions.TypeError'>,  TypeError("no common canonical parent for objects with parents: 'Rational Field' and 'Finite Field of size 3'",),  <traceback object at ...>)]
Got:
    [(<type 'exceptions.TypeError'>, TypeError("BUG: the base_extend method must be defined for 'Monoid of ideals of Integer Ring' (class '<class 'sage.rings.ideal_monoid.IdealMonoid_c'>')",), <traceback object at 0x2b75e90e8ef0>), (<type 'exceptions.TypeError'>, TypeError("no common canonical parent for objects with parents: 'Rational Field' and 'Finite Field of size 3'",), <traceback object at 0x2b75fd781950>)]
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_9
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.2.alpha2/tmp/.doctest_coerce.py
	 [2.9 s]
exit code: 1024
```



---

Comment by robertwb created at 2008-10-28 17:24:53

Ah, yes. That fix is fine to make (I saw it on my end, but thought it was due to an earlier patch I had in my repo changing some stuff).


---

Attachment

apply this patch only


---

Comment by GeorgSWeber created at 2008-10-28 20:53:39

Yep, this does the job.

Since I had trouble to get hg / mercurial queues to produce me another patch on top of Robert's original patch (telling me "abort: cannot commit over an applied mq patch" in the course), I just hacked that single line to be fixed in Robert's patch and loaded up the result.

(I'll find out how to do it correctly as soon as I did send this comment ...)

`@`Robert:

Please take care with this hacked patch and your personal hg repo, the hacked patch still contains your original hg Node ID / parent strings ...

Cheers, gsw


---

Comment by mabshoff created at 2008-10-28 21:28:51

Resolution: fixed


---

Comment by mabshoff created at 2008-10-28 21:28:51

Merged 4366-coercion-traceback-fixed.patch in Sage 3.2.alpha2
