# Issue 8225: %time now hugely broken in sagenb-0.7.4 (sage-4.3.2)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-02-10 01:39:34

Assignee: was


```


On Tue, Feb 9, 2010 at 1:22 PM, finotti <luis.finotti`@`gmail.com> wrote:
> Dear all,
>
> Cells starting with "%time" stopped working with 4.3.2.  (It works
> with 4.3.1.)  Is it no long supported or is it a bug? (time still
> works with the command line.)
>
> Running on Linux 32-bit, ubuntu binary.
>
> Thanks,
```

Wow, what a horrible, horrible regression!   Indeed, I've confirmed that what happens is that doing %time causes the notebook to hang forever, and be pretty broken thereafter.   Ouch.


---

Attachment

Fix `%time` and `%timeit`.  sagenb repo.


---

Comment by mpatel created at 2010-02-14 03:23:26

Changing status from new to needs_review.


---

Comment by ddrake created at 2010-02-23 06:49:18

I can confirm that this patch fixes the problem with `%time` on 4.3.3, and `%timeit` also works, but doesn't work as it does on the command line -- there, `%timeit` runs multiple loops and so on. Is that how `%timeit` has always worked in the notebook?

I don't know this particular code very well, but the patch appears to fix the problem and seems okay. So consider this a quite weak positive review.


---

Comment by mpatel created at 2010-02-23 07:37:31

I think `%timeit` has worked that way in the notebook.  See [this sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/4346a582d393916c/a21fa13cb5d54ff7?q=timeit+group:sage-devel+notebook#).  The worksheet I mentioned is now [here](http://www.sagenb.org/home/pub/1518/).


---

Comment by was created at 2010-03-06 18:55:14

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-07 00:04:10

Remove assignee was.


---

Comment by mpatel created at 2010-03-09 04:58:43

Resolution: fixed
