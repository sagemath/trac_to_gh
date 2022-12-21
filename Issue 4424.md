# Issue 4424: magma -- make sure .m files have their precompiled versions shiped with Sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-11-02 17:28:12

Assignee: was


```


On Sun, Nov 2, 2008 at 7:38 AM, Kevin Buzzard <k.buzzard`@`imperial.ac.uk> wrote:
> I'm still unclear about the philosophy of permissions.
>
> I downloaded sage 3.1.4 source and compiled from source. As root. Into
> /usr/local. Because I wasn't sure how to make the installation global.
>
> And today I tried (as a non-root user)
>
> sage: magma('sqrt(2)')
>
> [yes, I know it should be Sqrt but I'm guessing that isn't the problem]
>
> and I got
>
> ---------------------------------------------------------------------------
> TypeError                                 Traceback (most recent call last)
>
> /home/buzzard/<ipython console> in <module>()
>
> /usr/local/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/magma.pyc
> in __call__(self, x, gens)
>    502             if isinstance(x, bool):
>    503                 return Expect.__call__(self, str(x).lower())
> --> 504             return Expect.__call__(self, x)
>    505         return self.objgens(x, gens)
>    506
>
> /usr/local/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc
> in __call__(self, x, name)
>    963             return x
>    964         if isinstance(x, basestring):
> --> 965             return cls(self, x, name=name)
>    966         try:
>    967             return self._coerce_from_special_method(x)
>
> /usr/local/sage-3.1.4/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc
> in __init__(self, parent, value, is_name, name)
>   1281             except (TypeError, KeyboardInterrupt, RuntimeError,
> ValueError), x:
>   1282                 self._session_number = -1
> -> 1283                 raise TypeError, x
>   1284         self._session_number = parent._session_number
>   1285
>
> TypeError: While attempting to compile
> /usr/local/sage-3.1.4/data/extcode//magma/latex/latex.m (Data file
> non-existent):
> Can't open lock file
> /usr/local/sage-3.1.4/data/extcode//magma/latex/latex.lck for writing
> (Permission denied)
>
> While attempting to compile
> /usr/local/sage-3.1.4/data/extcode//magma/sage/basic.m (Data file
> non-existent):
> Can't open lock file
> /usr/local/sage-3.1.4/data/extcode//magma/sage/basic.lck for writing
> (Permission denied)
> sage:
>
> ***
>
> and I su-ed to root and tried again and got it right and then changed back
> to
> a non-root user and now it's OK. But what struck me, as a general user,
> was that the sage installation instructions didn't seem to explain anything
> to me about what the "correct" way to install sage system-wide on a unix
> machine was. Did I do the wrong thing?>
> Kevin
>
> PS this is sort of a 'bug report' but I'll send some general comments
> about your Bordeaux write-up to you later.

I think this is a reasonable bug report.  The fix is for Sage to
include the cached precompiled versions of the Magma files.
It used to be with Magma that one had to start it up as root
once because they didn't include precompiled files.  I think
this has changed, i.e., I think they now ship the precompiled
cached files in addition to the source files. 
```



---

Attachment

I attched each m file from the extcode repo and then added each .sig file to the repo. Pointless, but what the hell :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-02 18:05:39

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-02 18:05:39

Changing assignee from was to mabshoff.


---

Comment by was created at 2008-11-02 19:39:26

Resolution: wontfix


---

Comment by was created at 2008-11-02 19:39:26

Unfortunately, this doesn't work.  Probably the .sig files depend on the version of Magma.  I tried applying your patch and got then using it as a different user and got:


```
Runtime error in 'AttachSpec': Could not remove the invalid signature file /Users/wstein/sage/data/extcode//magma/latex/latex.sig
```


Since there are dozens of Magma versions out there, and we can't know which one people are using, there is literally *no possible way* to solve this problem without the user running a command such as 

```
sage: magma('2') 
```

as a user with write permissions to the extcode/magma directory. 

Since the error message clearly states that this is a permissions problem, there is nothing further to do really (i.e., nothing on the sage side).  This is just the way Magma works.
