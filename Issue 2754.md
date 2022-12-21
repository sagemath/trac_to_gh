# Issue 2754: plotting with frame=True and ymin/ymax sometimes is buggy as a Florida swamp in summer

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-01 15:59:45

Assignee: was

CC:  jason mvngu


```

On Tue, Apr 1, 2008 at 7:29 AM, Axel <axelgrau`@`gmail.com> wrote:
> 
>  How can I specify the range of y coordinates in a 2d plot? I tried
>  
>  show(plot(sin(x),-10,10),ymin=-0.5, ymax=0.5,frame=true)
>  
>  but the actual plot goes between -0.6, and 0.6, and the curve goes out
>  of the frame.

I think that's an honest-to-goodness *bug*.  For now you can try
to workaround it sort of with:
    show(plot(sin(x),-10,10),ymin=-0.41, ymax=0.41,frame=true)
but still the curve goes outside the frame.
```



---

Comment by mhansen created at 2008-09-03 00:54:42

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-03 00:54:42

Changing assignee from was to mhansen.


---

Comment by kcrisman created at 2009-09-29 14:52:13

This is now fixed, presumably with the new matplotlib.

Question: is it possible to verify this in a doctest?  The problem is that show uses save, but the saved figure is just a png.


---

Comment by jason created at 2009-09-29 15:50:30

Resolution: fixed


---

Comment by jason created at 2009-09-29 15:50:30

Nope, I don't think a doctest makes much sense here, with our current framework.

Sometime, we'll probably use matplotlib's image testing framework...

Minh, can you close this?  It works now on alpha.sagenb.org


---

Comment by jason created at 2009-09-29 15:50:41

Changing status from closed to reopened.


---

Comment by jason created at 2009-09-29 15:50:41

Resolution changed from fixed to 


---

Comment by jason created at 2009-09-29 15:51:10

(oops, I didn't mean to close it---I don't know exactly what your procedure is for things to do when you close a ticket...)


---

Attachment

based on Sage 4.1.2.alpha4


---

Comment by mvngu created at 2009-09-29 15:58:29

I can confirm this is now fixed:

```
[mvngu`@`darkstar sage-4.1.2.alpha4]$ ./sage -br main

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Time to execute 0 commands: 2.50339508057e-05 seconds
Finished compiling Cython code (time = 6.12911605835 seconds)
running install
running build
running build_py
running build_ext
Total time spent compiling C/C++ extensions:  0.919514894485 seconds.
running install_lib
running install_egg_info
Removing /home/mvngu/scratch/sandbox/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /home/mvngu/scratch/sandbox/sage-4.1.2.alpha4/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: show(plot(sin(x),-10,10),ymin=-0.5, ymax=0.5,frame=true)
```

The resulting plot is attached.


---

Comment by mvngu created at 2009-09-29 15:58:29

Resolution: fixed
