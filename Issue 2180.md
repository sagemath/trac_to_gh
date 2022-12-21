# Issue 2180: cython skipping build optimization

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2008-02-16 20:56:40

Assignee: was

CC:  moretti

In 2.10.2.alpha0, there appears to be a small problem with the cython skipping 
step.  To illustrate the bug:
1)  Start with a 2.10.2.alpha0 (with padic import patch) which is built 
up-to-date
2)  Add a new patch which adds a new .pyx file
3)  sage -br
4)  The bug is that you get a message like: 
building 'sage.rings.polynomial.multi_polynomial_factor' extension
error: unknown file type '.pyx' 
(from 'sage/rings/polynomial/multi_polynomial_factor.pyx')
sage: There was an error installing modified sage library code.


This appears to arise because the new .pyx file is not in the cache and so the 
build optimizer believes that there are no .pyx files to build and just lets 
the ordinary disttools do their work.  Of course, the ordinary disttools 
don't know what to do with .pyx files.

A work-around is to 'touch' a .pyx file anywhere in the tree which is already 
in the cache.  A build after the touch will build the touch'ed file and the 
new file.


---

Comment by jbmohler created at 2008-02-16 20:58:05

Changing component from algebraic geometry to packages.


---

Comment by jbmohler created at 2008-02-16 20:58:05

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2008-02-24 00:26:35

I have seen this issue before and I believe the new caching code is at fault, so it should be assigned to Bobby Moretti. I have speculated that if you patch in a new file the time stamp of the new file is too old for the precomputed hashes to be recomputed. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-24 00:26:35

Changing assignee from mabshoff to moretti.


---

Comment by moretti created at 2008-02-24 02:27:21

Replying to [comment:2 mabshoff]:
> I have seen this issue before and I believe the new caching code is at fault, so it should be assigned to Bobby Moretti. I have speculated that if you patch in a new file the time stamp of the new file is too old for the precomputed hashes to be recomputed. 
> 
> Cheers,
> 
> Michael

Micheal, I think you're dead on. This is actually William's code, but I'm pretty familiar with it and I'll try to implement a fix.

-Bobby


---

Comment by moretti created at 2008-02-24 03:16:59

Joel,

Were you running hg from the command line or were you applying the patch from within Sage? I cannot get the error to reproduce.

-Bobby


---

Comment by was created at 2008-02-24 05:15:18

I do not know how to reproduce this.  I've tried what you suggested and I can't.
I also think it is very unlikely that this is caused by the initial caching (i.e., my code) as Bobby suggests, since that code is really ridiculously simple.  It's just this: 

```
def hash_of_cython_file_timestamps():
    h = 0
    extensions = set(['.pyx', '.pxd', '.pxi'])
    def hash_of_dir(dir):
        h = 0
        for f in os.listdir(dir):
            z = dir + '/' + f
            if os.path.isdir(z):
                h += hash_of_dir(z)
            elif f[-4:] in extensions and f[0] != '.':
                h += hash(os.path.getmtime(z))
        return h
    return hash_of_dir('sage')
```


The above just computes a hash of *all* cython related files in all subdirectories.
If you change anything it changes and the cythoning code reruns.  All that matters is that something has changed in any timestamp of any cython-related file, even something not listed in setup.py.  This gets run and if it isn't the same as last time then the usual Cython code gets run (Bobby's code).  If a patch has a Cython file in it, even if it hasn't changed in a long time, it'll change the above hash, which will make the Cythoning rerun.  

So I can't understand how to reproduce your bug.  Could you please please find a systematic way to reproduce it, so we can fix it?  I'm not clever enough to think of anything based on the hints.

Did you definitely do `hg_sage.update()`?

WAIT -- idea!
Actually, one possibility might be that the patch added a .pyx file that you 
already had with the same time stamp, but it *only* added it to setup.py.  Thus setup.py changed but no Cython files changed, but indeed it's now necessary to
rerun Cython.  Ah ha.  I bet the fix is to just add setup.py to the list of "cython"
related files. 

I've made a patch based on this idea, and also added a little bit of nice
verbose timing information about how long Cython'ing takes and attached a patch.
Joel -- please referee this and let me know if this maybe solves this problem.

Once again, thanks for reporting these subtle bugs!


---

Comment by was created at 2008-02-24 05:15:38

this might (?) completely fix the bug; it also adds some nice timing output


---

Attachment


---

Comment by roed created at 2008-02-24 10:22:02

This error happened when I created a .pyx file, saved it, then put it into setup.py.  This would suggest that William is right about what's going on.


---

Comment by mabshoff created at 2008-02-24 20:35:09

This patch looks good. It does fix the bug in question, but #2295 is also relevant in this case for a bug with the same symptoms, but different cause. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-24 20:37:50

Resolution: fixed


---

Comment by mabshoff created at 2008-02-24 20:37:50

Merged in Sage 2.10.3.alpha0
