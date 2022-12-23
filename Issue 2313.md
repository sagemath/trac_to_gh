# Issue 2313: old spkg's -- delete to save space

Issue created by migration from https://trac.sagemath.org/ticket/2313

Original creator: was

Original creation time: 2008-02-26 06:18:18

Assignee: mabshoff


```


On Mon, Feb 25, 2008 at 9:40 PM, Jonathan Bober <jwbober@gmail.com> wrote:
> 
>  An old sage directory that I have that's been upgraded only a few times
>  has an spkg directory that's got more than 850 megs. This was only
>  upgraded from 2.8.15.alpha1 to 2.10.1, so I imagine that this directory
>  can get even larger. With the exception of the 'installed' directory,
>  can everything else be safely deleted?

No.

>  (Actually, the same question stands for a new sage install, in which the
>  spkg directory holds abound 200 megs. Is there a reason that already
>  installed spkg's should be kept around?)

If you delete spkg/standard then the dependency system will get completely confused
and rebuild all of Sage from scratch.

If you use the following script you can shrink all the files to be empty, and everything
will work fine:

login@sage:~$ more /usr/local/bin/shrink 
#!/usr/bin/env python

import os

for F in os.listdir('.'):
    print F
    if F.endswith('.spkg'):
       open(F,'w').close()

---

The main issue is that the build system was written when there were
3 Sage users in the whole world, and issues like this weren't our
top priority.   Nobody ever got around to dealing with this.  I'm not
going to immediately suggest the right fix, since there are several options
and I'd rather people discuss them. 

```



---

Comment by mabshoff created at 2008-12-02 02:21:47

Resolution: fixed


---

Comment by mabshoff created at 2008-12-02 02:21:47

Now that #463 is merged this ticket can be closed since -upgrade will delete any older and no longer used spkgs.

Cheers,

Michael
