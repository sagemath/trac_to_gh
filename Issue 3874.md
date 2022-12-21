# Issue 3874: Moebius plot bug

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2008-08-15 13:20:01

Assignee: was

plot(moebius) plots the Moebius function nicely from 0 to 50.
plot(moebius,50,100) plots the y-values of the Moebius function nicely from 50 to 100. Unfortunately, the x-values are still from 0 to 50!


---

Attachment


---

Comment by kcrisman created at 2008-08-15 13:22:46

Changing assignee from was to kcrisman.


---

Comment by was created at 2008-08-15 16:41:46


```

Can you throw in a call to

  p.xmin(xmin)

before returning p?  The plot of  plot(moebius, 500,550) would look
much nicer as a result. 
```



---

Comment by was created at 2008-08-15 17:08:03


```
> William,
>
> If you are referring to the viewing window starting around x=-1, my
> understanding was that this is taken care of by the patches to
> http://trac.sagemath.org/sage_trac/ticket/3806, which will be in 3.1.
> I attach the output of
> sage: plot(moebius,500,550)
> on my system, with those patches included.
>
> If that's not what you mean, let me know what the problem with the
> plot is and I will be happy to have the code reset the xmin. Thanks
> for the feedback!
>
> - kcrisman

With the excellent work at #3806, I immediately change my opinion to
positive review for your patch as is. 

```



---

Comment by mabshoff created at 2008-08-18 23:15:42

Resolution: fixed


---

Comment by mabshoff created at 2008-08-18 23:15:42

Merged in Sage 3.1.2.alpha0
