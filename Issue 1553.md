# Issue 1553: Investigate PolyBoRi on 64-bit RHEL5

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2007-12-17 15:00:38

Assignee: was

CC:  burcin

See http://groups.google.com/group/sage-support/browse_thread/thread/cdf2ae8087d5637e?hl=en at  Dec 17, 8:37 am.


---

Comment by mabshoff created at 2007-12-17 16:09:11

Hi Kiran,

> I tried sage -upgrade on my 64-bit RHEL5 box (Opteron 246), and the
> upgrade dies pretty definitively at PolyBoRi. As far as I can tell, on
> the first file it is throwing lots of compile errors of the form

> /tmp/cciylcHI.s:17647: Error: suffix or operands invalid for `push'
> /tmp/cciylcHI.s:17697: Error: suffix or operands invalid for `pop'

> I'm guessing/hoping this is probably some easy fix on my end. Any
> suggestions?

That is a bashism that was supposedly fixed by Burcin. It might have
snuck back into the latest spkg. I will investigate this. rlm created
#1553 for this.

> Kiran

Cheers,

Michael


---

Comment by burcin created at 2007-12-27 11:09:19

The `spkg-install` in `polybori-0.1-r5.spkg` does not contain `popd`, or `pushd`. The original error my changes fixed was:


```
./spkg-install: 69: pushd: not found
```


The file names on the error message (`/tmp/cciylcHI.s`) indicates that this is a temporary file created during the build, not the `spkg-install` script.

More information from the build log would be helpful.


---

Comment by burcin created at 2007-12-27 11:09:19

Changing status from new to assigned.


---

Comment by burcin created at 2007-12-27 11:09:19

Changing assignee from was to burcin.


---

Comment by kedlaya created at 2008-01-02 19:54:39

The problem seems to be that my machine has an old version of gcc lying around (back when it was only running a 32-bit kernel) and SCons has set up its default path so that it hits /usr/local/bin (where the old gcc is) before /usr/bin (where the new one is). 

It seems to fix things to change the line:

```
env=Environment(options=opts,tools = tools, toolpath = '.')
```

in the SConstruct file to:

```
env=Environment(ENV = {'PATH': os.environ['PATH']}, options=opts,tools = tools, toolpath = '.')
```

so that the local PATH gets imported. (This turns out to have been the same issue I had when we first switched to SCons, although I didn't recognize it as such at first.)


---

Comment by burcin created at 2008-01-03 15:08:56

This issue will be fixed along with #1663.


---

Comment by burcin created at 2008-01-03 15:13:18

Replying to [comment:6 comment 6]:
> This issue will be fixed along with #1663.
                                      
This should have been #1656, sorry for the noise.


---

Comment by mabshoff created at 2008-01-04 17:02:52

Some more info from Kiran:

```
f I describe my setup, it might seem less uncommon than you might
have previously thought.

Mine is a 64-bit box on a network consisting mostly of 32-bit
machines. On my machine, /usr/bin is locally mounted, and there is a
local 64-bit gcc there.

But /usr/local is NFS mounted, and there is a 32-bit gcc in /usr/local/
bin for the benefit of the benighted masses. Persuading my sysadmin to
instead install a local 32-bit gcc on every single 32-bit machine in
the department is not going to happen.

So I have to switch rather than fight. My $PATH has /usr/bin ahead of /
usr/local/bin, so ordinarily (and even in SCons if I force it to
import my PATH environment variable) this causes no problems.

But SCons defaults not to importing any environment variables, which
means it has to come up with its own guess for the path. And what it
comes up with on my box is:
   /usr/local/bin:/opt/bin:/bin:/usr/bin
I have no idea why. There isn't even a directory /opt/bin on my
system! This might be some sort of hard-coded default (either in SCons
or in the RHEL configs somewhere).

Anyway, I'm able to manually patch the relevant SConstruct files to
get around this, so it's not a high priority for me to get this fixed.
But I suspect that sooner or later, someone else will run into this if
nothing is done about it. 
```

As it turns out SCons itself is at fault: `local/lib/scons-0.97/SCons/Platform/posix.py`:

```
    if not env.has_key('ENV'):
        env['ENV']        = {}
    env['ENV']['PATH']    = '/usr/local/bin:/opt/bin:/bin:/usr/bin'
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-01-08 01:54:28

The new spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha0/polybori-0.1-r6.spkg

fixes the issue as Kiran suggested.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-08 01:55:26

Merged in 2.10.alpha0.


---

Comment by mabshoff created at 2008-01-08 01:55:26

Resolution: fixed
