# Issue 589: improve doctesting of sage-sage script

Issue created by migration from https://trac.sagemath.org/ticket/589

Original creator: was

Original creation time: 2007-09-05 14:14:31

Assignee: was


```
On 9/4/07, Jonathan Bober <jwbober@gmail.com> wrote:
> My memory could be wrong, but I feel that this exact problem has
> occurred before. (The problem of running scripts on the command line not
> working -- not necessarily the exact same underlying cause for the
> problem.)
>
> This kind of basic functionality should probably be tested somewhere
> automatically. Maybe a doctect with a line like
>
> sage: os.system('.\sage something_or_other.sage')
>
> might work. Or maybe this would need to be somehow tested outside the
> doctest framework. I don't know. Just a thought.

True.

Implement some doctests like that  and post a patch to trac. :-)
```



---

Comment by kcrisman created at 2009-12-30 04:51:06

This seems not too hard.  In what file would such doctests live?


---

Comment by kcrisman created at 2012-07-07 04:15:41

Note that this is now `$SAGE_ROOT/spkg/bin/sage`.  If this ticket is still valid.


---

Comment by jdemeyer created at 2013-02-08 13:54:56

Duplicate of #10300 + #10326 + #12249 + #9191.


---

Comment by jdemeyer created at 2013-02-08 13:54:56

Resolution: duplicate
