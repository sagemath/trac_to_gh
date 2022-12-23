# Issue 6772: increase default ecl memory limits for maxima+ecl in sage

Issue created by migration from https://trac.sagemath.org/ticket/6772

Original creator: was

Original creation time: 2009-08-17 09:30:40

Assignee: mabshoff

Example:

```
Here's a simpler example to get this error:

sage: m = maxima(2*10^6)
sage: time n=m.factorial()
Maxima encountered a Lisp error:
Memory limit reached. Please jump to an outer point or quit program.

Or, directly in Maxima:

(%i3) n : factorial(10^7);
GC Warning: Out of Memory!  Returning NIL!
Maxima encountered a Lisp error:
 Memory limit reached. Please jump to an outer point or quit program.
Automatically continuing.
To reenable the Lisp debugger set *debugger-hook* to nil.
```


And the response from the main ECL guy:


```
On Mon, Aug 17, 2009 at 10:57 AM, William Stein<wstein@gmail.com> wrote:
> Note that Sage's Maxima uses ECL.  So the basic question is, how can
> we increase the memory that Maxima + ECL can use?

The limits ECL has are by default too small for big applications, but
it is intentionally done so. However, changing them is pretty easy:
add a call to ext:set-limit in any file of maxima that forms part of
the final executable.

The different memory limits that can be independently controlled are listed here
    http://ecls.sourceforge.net/new-manual/re34.html
So for instance, in your case, which hits the dynamically allocated
memory limit, you might add the following
    (ext:set-limit 'ext:heap-size (* 1024 1024 1024))
to maxima/src/ecl-port.lisp in order get 1GB memory limit.

Juanjo

```




---

Comment by was created at 2009-08-18 18:25:10


```
> My understanding is that one has to modify the maxima source code
> itself and recompile maxima.

Not so -- EXT:SET-LIMIT can be called anytime after the
Maxima session is launched.
To evaluate a single Lisp expression in Maxima:

:lisp (ext:set-limit 'ext:heap-size <whatever>)

Robert Dodier
```



---

Comment by was created at 2009-11-16 16:20:40

Maxima changed so that big factorials are symbolic (which is bizarre, but anyways...), so the above example no longer works.  The following does work:

```
sage: a = maxima(10)^(10^5)
sage: b = a^600
Boom!
```


I suggest the way to fix this problem is to add this line to the startup of code for the Maxima interface:

```
maxima._eval_line(":lisp (ext:set-limit 'ext:heap-size 100000000000)", 
wait_for_prompt=False)
```



---

Comment by was created at 2009-11-16 16:26:39

Changing status from new to needs_review.


---

Comment by was created at 2009-11-16 16:26:39

Even better:

```
self._sendline(":lisp (ext:set-limit 'ext:heap-size 0)")
```


The above appears to make the heap unlimited.


---

Attachment

Replying to [comment:3 was]:
> The above appears to make the heap unlimited.

Someone should check how Boehm decides if it should extend the heap area or try to reclaim garbage and reuse memory. A side-effect of removing a limit could be that ECL just keeps allocating more memory until everything is used up, before garbage collecting. Other processes might not like that too much.

I guess a sanity check would be to try some long computation that is supposed to use constant memory and see if ext:set-limit influences the memory footprint.


---

Comment by was created at 2009-11-17 15:43:47

Replying to [comment:4 nbruin]:
> Replying to [comment:3 was]:
> > The above appears to make the heap unlimited.
> 
> Someone should check how Boehm decides if it should extend 
> the heap area or try to reclaim garbage and reuse memory. 
> A side-effect of removing a limit could be that ECL just 
> keeps allocating more memory until everything is used up, 
> before garbage collecting. Other processes might not like that too much.

That would be really annoying. There's only one program I know that is that annoying -- PARI. Fortunately, that does not seem to be what happens here. 

I tried the following while watching top:

```
sage: maxima._eval_line(":lisp (ext:set-limit 'ext:heap-size 100000000000)",wait_for_prompt=False)
sage: sage: a = maxima(10)^(10^5)
sage: sage: b = a^600
sage: sage: b = a^600
sage: sage: b = a^600
sage: sage: b = a^600
sage: sage: b = a^600
sage: sage: b = a^600
sage: sage: b = a^600
sage: sage: b = a^600
sage: sage: b = a^600
```

The memory usage initially goes up from 50MB to 415MB, but then stays at 415MB ever after.


---

Comment by kcrisman created at 2009-11-18 17:22:18

I had a similar experience (476MB) with this example, except I had to use heap-size 0 (as suggested earlier) instead of what's above; if I use the above it goes boom at the second try, in fact it does even if I add another zero.


---

Comment by nbruin created at 2009-11-27 21:21:57

Replying to [comment:6 kcrisman]:
> I had a similar experience (476MB) with this example, except I had to use heap-size 0 (as suggested earlier) instead of what's above; if I use the above it goes boom at the second try, in fact it does even if I add another zero.

I bet you are on a 32 bit machine then, because Log(100000000000)/Log(2)=36.54

According to

http://ecls.sourceforge.net/new-manual/re30.html

setting a limit to 0 should indeed mean "no limit". If that is our intention then that would be more portable than 100000000000.
For safety, 2GB might not be an unreasonable limit, though. When people are debugging they might want to enforce a lower limit to see the crash sooner.


---

Comment by kcrisman created at 2009-11-28 04:19:11

Replying to [comment:7 nbruin]:
> Replying to [comment:6 kcrisman]:
> > I had a similar experience (476MB) with this example, except I had to use heap-size 0 (as suggested earlier) instead of what's above; if I use the above it goes boom at the second try, in fact it does even if I add another zero.
> 
> I bet you are on a 32 bit machine then, because Log(100000000000)/Log(2)=36.54

Yes, you are correct.


---

Comment by mhansen created at 2009-12-27 15:35:24

Looks good to me.


---

Comment by mhansen created at 2009-12-27 15:35:24

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 18:42:49

Resolution: fixed
