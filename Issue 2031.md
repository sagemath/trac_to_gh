# Issue 2031: serious preparser lameness involving time and comments

Issue created by migration from https://trac.sagemath.org/ticket/2031

Original creator: was

Original creation time: 2008-02-02 08:36:25

Assignee: was

CC:  mjo

It would be fair to argue that this is pretty sucky behavior in Sage:


```
teragon:~ was$ build/sage-2.10.1.rc4/sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.1.rc4, Release Date: 2008-01-31                  |
| Type notebook() for the GUI, and license() for information.        |
sage: time 2 + 2     # can Sage add 2 and 2?
Object `time Integer(2) + Integer(2)     # can Sage add 2 and 2` not found.
sage: time 2 + 2     # Sage can add 2 and 2
------------------------------------------------------------
   File "<timed exec>", line 1
     Integer(2) + Integer(2)     \# Sage can add 2 and 2
                                                       ^
<type 'exceptions.SyntaxError'>: unexpected character after line continuation character

```


I'm to blame for both bugs, of course... :-)


---

Comment by was created at 2008-02-02 08:37:51

Here is yet another problem with time. The following should print out 4 but doesn't.

```
sage: time a = 2 + 2; a
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
```

It should print 4 since this does:

```
sage: a = 2 + 2; a
4
```



---

Comment by was created at 2008-02-25 18:14:51

A related problem:

```


On Mon, Feb 25, 2008 at 10:06 AM, Nick Alexander  wrote:
> 
>  > It might be.  I don't like the time function as it is written now,
>  > since it's
>  > done with the preparser and doesn't work when it isn't the first
>  > thing on
>  > a line, which is annoying.
>  >
>  > sage: 2 + 2; time 2 + 2
>  > ------------------------------------------------------------
>  >    File "<ipython console>", line 1
>  >      Integer(2) + Integer(2); time Integer(2) + Integer(2)
>  >                                          ^
>  > <type 'exceptions.SyntaxError'>: invalid syntax
>  >
>  > Hey, Nick, want to fix that? ;-)
>  
>  Such things are legion, and it's actually an IPython problem.  

I think this is a Sage problem.  

  sage: time foo

is dealt with by the Sage preparser.  It's code I wrote and you've
probably looked at...

William

> For
>  example, 'x = 2; x?' will also fail.

That's an ipython problem. 

>  We could fix it, but it's likely to not be a general fix.  Open a
>  trac ticket and maybe it will get dealt with :)
>  
>  Nick
>  
> 

```



---

Comment by mjo created at 2012-01-09 02:03:46

Well, some of them are fixed:


```
sage: time a = 2 + 2; a
Time: CPU 0.00 s, Wall: 0.00 s
4
sage: 2 + 2; time 2 + 2
4
4
Time: CPU 0.00 s, Wall: 0.00 s
```


But with a comment on the line, we get no timings:


```
sage: time 2 + 2     # Or don't
4
sage:
```



---

Comment by mhansen created at 2013-07-22 16:04:01

`%time` is now handled by IPython and works with the comment lines.  We still have 


```
sage: %time a = 2 + 2; a      
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
```


but I think we can close this ticket.


---

Comment by mhansen created at 2013-07-22 16:04:19

Resolution: invalid


---

Comment by was created at 2013-07-23 17:50:42

Replying to [comment:4 mhansen]:
> `%time` is now handled by IPython and works with the comment lines.  We still have 
> 
> {{{
> sage: %time a = 2 + 2; a      
> CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
> Wall time: 0.00 s
> }}}
> 
> but I think we can close this ticket.

My 2 cents.   I wouldn't close this.  This is in my opinion a bug in Ipython now, but it is still a bug.  

For comparison in a worksheet in https://cloud.sagemath.com, where I implemented things from scratch (yet again), this works just fine:


```
INPUT: %time a = 2 + 2; a # or don't
OUTPUT: 4
CPU time: 0.00 s, Wall time: 0.00 s
```


It's bad for the behavior of a single line to depend on whether or not it has %time in front of it.    I don't know why IPython doesn't respect the sys.displayhook though.

Perhaps this should be a new ticket though, and it should be reported upstream to ipython.  I.e., it's not longer a "Sage preparser" issue.
