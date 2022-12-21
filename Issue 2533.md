# Issue 2533: add "-p" flag to $CP for make install

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-03-15 22:15:35

Assignee: mabshoff


```
On Saturday 15 March 2008, Paul Zimmermann wrote:
>        Hi,

> I wonder why sage -br takes so much time after a fresh build from source
> and make install. Normally, since everything was just compiled, it should
> have nothing to do. I guess the reason lies in:

>    bash-3.00$ make install DESTDIR=/usr/local/sage-2.10.3 -n
>    ...
>    cp -rv * /usr/local/sage-2.10.3/sage/
>    ...

> where 'cp' does not preserve the dates of the files, and thus the correct
> dependencies are lost. Maybe "mv * /usr/local/sage-2.10.3/sage/" would
> solve that problem?

Or use
    cp -prv * ...
the -p option preserve timestamps.

Bill
```



---

Attachment


---

Comment by mabshoff created at 2008-03-15 22:19:45

Changing status from new to assigned.


---

Comment by mhansen created at 2008-03-15 22:22:13

Looks good to me.


---

Comment by mabshoff created at 2008-03-15 22:26:04

Merged in Sage 2.10.4.rc0


---

Comment by mabshoff created at 2008-03-15 22:26:04

Resolution: fixed
