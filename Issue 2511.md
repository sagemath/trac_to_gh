# Issue 2511: fix mistake in the animate docs (trivial to fix)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-13 22:30:20

Assignee: was


```
On Thu, Mar 13, 2008 at 11:41 AM, Hector Villafuerte <hectorvd`@`gmail.com> wrote:
> 
>  Hi,
>  the docstring for animate gives the following example:
>  
>  sage: a = animate([sin(x + float(k)) for k in srange(0,4,0.3)],
>  xmin=0, xmax=2*pi, figsize=[2,1])
>  sage: a.show()
>  
>  
>  Which fails on my brand new sage-2.10.3 with:
>  
>  Traceback (most recent call last):
>  ...
>  AttributeError: Unknown property xmin
>  
>  
>  The following code gives the desired animation:
>  
>  sage: a = animate([plot(sin(x + float(k)), 0, pi) for k in
>  srange(0,4,0.3)], xmin=0, xmax=2*pi, figsize=[2,1])
>  sage: a.show()
>  
>  Question: is this a bug? i.e. should animate work as shown in it's
>  docstring example?
>  Just for completion, I also tried it on www.sagenb.org and got the same results.
>  Best,

Yes, this is *definitely* a bug.  It wasn't caught because the docstrings
for animate are marked optional, since animate currently depends on
the convert command being present to make animate gif's (is there any
better way?!).  

William
```



---

Comment by AlexGhitza created at 2008-03-16 02:11:38

I think the issue got fixed when #2066 was merged.  Can anybody confirm?  (It's working on my machines.)


---

Comment by mabshoff created at 2008-03-28 08:45:59

Resolution: fixed


---

Comment by mabshoff created at 2008-03-28 08:45:59

Replying to [comment:1 AlexGhitza]:
> I think the issue got fixed when #2066 was merged.  Can anybody confirm?  (It's working on my machines.)
> 

I can confirm this. Both cases gives above work fine with my 2.11.alpha2.

Cheers,

Michael
