# Issue 2278: notebook -- when uploading a new worksheet be sure to set the permissions on any directories that are created to be readable by all

Issue created by migration from https://trac.sagemath.org/ticket/2278

Original creator: was

Original creation time: 2008-02-23 16:35:05

Assignee: boothby


```
Hello William,

I spoke too soon ... I stated on the forum that it was fixed.
However, I just uploaded another worksheet called Graphing, and I'm
receiving the Permission Denied error again.

Regards,
Andy


On Feb 22, 9:45 am, "William Stein" <wst...@gmail.com> wrote:
- Hide quoted text -
> On Thu, Feb 21, 2008 at 9:09 PM, AprèsTech <andyunr...@gmail.com> wrote:
>
> >  Hello,
>
> >  After uploading a worksheet from my PC to the sagenb.org server, I
> >  can't edit or evaluate cells within it.  I'm receiving the error
> >  message
>
> >  Traceback (most recent call last):
> >   File "<stdin>", line 1, in <module>
> >  IOError: [Errno 13] Permission denied: '/home/server2/sage_notebook/
> >  worksheets/aprestech/4/code/3.py'
>
> >  Did I do something wrong, or is this a bug?
>
> This is *definitely* a bug on my part.  I'll look into it immediately.
> If you still have this problem after you get this email, please
> respond and let me know.
>
> Also, can you get the bug to occur again by uploading another worksheet?
> This problem is caused by the too-strict in this case security model.  It can
> be fixed once for all if it is easily repeatable.
>
> William
```



---

Comment by was created at 2008-05-11 06:31:38

In sage-3.0.1 already this line is around line 1370 of worksheet.py:

```
        os.system('chmod -R a+rw "%s"'%absD)
```

That must do enough to set permissions as needed.  I suspect this problem
is either completely solved or was very special to some unix setup I had.  Also, the user reporting the problem has been using the public notebook even recently (two months later) with no further complaints.


---

Comment by was created at 2008-05-11 06:31:38

Resolution: fixed
