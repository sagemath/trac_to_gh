# Issue 151: clisp.run being left running

Issue created by migration from https://trac.sagemath.org/ticket/151

Original creator: was

Original creation time: 2006-10-25 21:07:01

Assignee: was


```
On Wed, 25 Oct 2006 15:42:31 -0500, Justin C. Walker <justin@mac.com> wrote:
> On Oct 25, 2006, at 12:50 PM, Kate Minola wrote:
>> Running sage-1.4.1.2 on my x86_64-Linux system,
>> if I run the following command:
>>
>> maxima.eval("-(1/2)*taylor (sqrt (1-4*x^2), x, 0, 15)")
>>
>> and then quit, I find that there is a process
>> 'lisp.run' unexpectedly still running on my system
>> (and using up CPU resources).
>>
>> Does this happen on anyone else's system?
>
> I've tried this specific sequence (run the above; exit) several
> times, and it doesn't happen for me (Mac OS X, 32-bit, Intellimac).
>
> When you quit, do you recall whether you saw this:
>
> Exiting SAGE (CPU time 0m0.11s, Wall time 0m10.64s).
> Exiting spawned Maxima process.

I just observed the problem on sage.math.  (64-bit amd linux).
It doesn't happen on OS X.  The code's identical, so I guess 
things like killpg work better on OS X...  In any case, I consider
this a very serious bug, and *will* add extra code to deal with it
better on Linux 64-bit. 

I've posted this to trac.

William
```



---

Comment by was created at 2006-10-25 21:36:32


```
Here is a reproducible way to trigger this bug on my system (enter an
incorrect maxima command):
 
maxima('2e^15')
 
The lisp process is not terminated after exiting sage.
 
Greg
 
PS: there is another bug that I have to report too,
float(maxima('1.e12')) (but not float(maxima('1.e-12'))
```



---

Comment by was created at 2006-10-31 16:10:56


```
On Tue, 31 Oct 2006 05:35:30 -0800, David Harvey <dmharvey@math.harvard.edu> wrote:
 
 
This is getting out of control.
 
moretti is running 15 of those zombie lisp.run processes and probably
doesn't even realise. (It's not your fault Bobby!)
 
It's chewing up a very large proportion of CPU cycles on sage.math.
 
We've got to track down this bug.
 
I've killed them.
 
It may be impossible to completely deal with this problem just using the
techniques I currently use.   The master SAGE process that spawns though's
lisp.run (etc) processes can be kill -9'd at any time, and then it has absolutely
no chance to clean up after itself.
 
Thus probably, in *addition* to anything we do to deal with this, I should
make it so that by default when SAGE starts up it cleans up any messes
left around from previous runs (this is the sort of thing Firefox does):
 
     1. deletes any directories in $HOME/.sage/tmp
     2. kill -9 any processes that got left running -- this could be done by
         saving pid's of processes that in a file in $HOME/.sage/tmp/
 
There are of course potential problems with 2, especially if working on
a cluster or with a home directory over NSF.  So the hostname of the machine
where the processes were started and the name of the program could be stored
as well.  Also, there would be a flag to turn off such startup behavior.
 
Thoughts?  At least then if Bobby starts one copy of SAGE all that cruft
would be gone.
 
I don't think the above would be difficult to implement.  The main question
is if it is stupid and/or dangerous in any way.  E.g., we don't want SAGE to
accidently kill your week-long running super important SAGE computation!
 
 
William
```



---

Comment by was created at 2006-11-06 08:25:12

I just tested this:

```
sawas@sage:~$ sage
--------------------------------------------------------
--------------------------------------------------------
| SAGE Version 1.4.1.3, Build Date: 2006-10-20         |
| Distributed under the GNU General Public License V2. |

sage: maxima.eval("-(1/2)*taylor (sqrt (1-4*x^2), x, 0, 15)")
'-1/2 + x^2 + x^4 + 2*x^6 + 5*x^8 + 14*x^10 + 42*x^12 + 132*x^14'
sage: quit
Exiting SAGE (CPU time 0m0.07s, Wall time 0m8.26s).
Exiting spawned Maxima process.
```


with several versions of sage and in no cases were clisp.run's left
running.  So the example in the error report isn't good.

That said, having some sort of cleanup system like I describe above 
would maybe be good.


---

Comment by was created at 2006-11-08 17:29:32


```
 
On Wed, Nov 08, 2006 at 02:23:18AM -0800, William Stein wrote:
> Good question.  Longterm there are a couple of issues:
>  
>   (1) How do you tell the monitor about new processes that get spawned?
>       You could put that info in a temp file, but that feels a little
>       clunky.
 
You can read from a pipe or some other form of IPC (e.g. unix socket)
 
>   (3) I want to continue to support the spawned processes running on other
>       computers (or as different users) via ssh.  With a separate monitor
>       for each spawned process this is possible (though two ssh sessions
>       would be needed).  This isn't possible if there is only one monitor,
>       since it can only run on one computer.
 
Just run one monitor for each host.
 
>   (4) For reasons I don't understand, the slave process doesn't really die
>       until the monitor exits.  If in the monitor script instead of doing
>       a sys.exit(0) after the kill, I continue the monitor running, then the
>       process the monitor is watching doesn't terminate as it should.  This
>       is on OS X Intel, and is rather odd, but isn't an issue with the  
> 1-monitor
>       per process model.
 
See wait(2) and waitpid(2) (and also wait3 and wait4 for resource
information).
 
Essentially, when a process dies, it stays in "zombie" state so that
one can (a) get exit status (b) get resource usage information (c)
dump core IIRC, etc.
 
The usual trick to spawn e.g. a daemon is to fork / setsid(2) / fork,
run the process in question as a grandchild, and let the child die;
because of the setsid(2) call, the process is not adopted by its
grandparent, but by the init process, which is supposed to clean up on
exit of any process.  [ See also setsid(8) ]
 
Since we are talking about a monitor, the sensible thing is that the
monitor waits for all its subprocesses.
 
In addition, the monitor can get information about resource usage,
which could be interesting.
 
>   (5) The overhead is minimal -- it really is only 2MB to run a minimal
>       Python process.
 
However small, it's still O(n).
 
BTW, isn't it better to kill -15 first, wait some time, then kill -9
(give a chance to cleanup in case there is a SIGTERM handler)
 
Best,
Gonzalo
 }}}


---

Comment by was created at 2006-11-08 17:35:39


```
On Wed, 08 Nov 2006 07:27:39 -0800, Gonzalo Tornaria wrote:
 
 
On Wed, Nov 08, 2006 at 02:23:18AM -0800, William Stein wrote:
Good question.  Longterm there are a couple of issues:
 
  (1) How do you tell the monitor about new processes that get spawned?
      You could put that info in a temp file, but that feels a little
      clunky.
 
You can read from a pipe or some other form of IPC (e.g. unix socket)
 
Yes, that could work.
 
  (3) I want to continue to support the spawned processes running on other
      computers (or as different users) via ssh.  With a separate monitor
      for each spawned process this is possible (though two ssh sessions
      would be needed).  This isn't possible if there is only one monitor,
      since it can only run on one computer.
 
Just run one monitor for each host.
 
OK, but then what about question 1 again?  In particular, telling a monitor
over the network about new processes would be complicated.
 
  (4) For reasons I don't understand, the slave process doesn't really die
      until the monitor exits.  If in the monitor script instead of doing
      a sys.exit(0) after the kill, I continue the monitor running, then the
      process the monitor is watching doesn't terminate as it should.  This
      is on OS X Intel, and is rather odd, but isn't an issue with the
1-monitor
      per process model.
 
See wait(2) and waitpid(2) (and also wait3 and wait4 for resource
information).
 
Essentially, when a process dies, it stays in "zombie" state so that
one can (a) get exit status (b) get resource usage information (c)
dump core IIRC, etc.
 
The usual trick to spawn e.g. a daemon is to fork / setsid(2) / fork,
run the process in question as a grandchild, and let the child die;
because of the setsid(2) call, the process is not adopted by its
grandparent, but by the init process, which is supposed to clean up on
exit of any process.  [ See also setsid(8) ]
 
Since we are talking about a monitor, the sensible thing is that the
monitor waits for all its subprocesses.
 
One point that might not have been clear from my previous posting
is that the monitor does not have any subprocesses.  The gap/gp/magma,
etc., process that it monitors is a sibling rather than a subprocess.
 
In addition, the monitor can get information about resource usage,
which could be interesting.
 
Yes.
 
  (5) The overhead is minimal -- it really is only 2MB to run a minimal
      Python process.
 
However small, it's still O(n).
 
Yes but for a typically running SAGE program n is about 3-4, at most.
There's no reason in SAGE to launch numerous subprocesses.
 
BTW, isn't it better to kill -15 first, wait some time, then kill -9
(give a chance to cleanup in case there is a SIGTERM handler)
 
Yes.  Good point.
 
Many thanks for your email.
 
Anyway, this process monitor thing is a completely general purpose
unix tool.  It really a priori has nothing to do with SAGE.  Most
of the suggestions on the list are to turn it from what I wrote
into a generic daemon.  I wonder -- has such a generic daemon for
process monitoring *already* been written and I just don't know
about it?
 
William
```



---

Comment by was created at 2007-01-12 23:49:09

The example

```
maxima.eval("-(1/2)*taylor (sqrt (1-4*x^2), x, 0, 15)")
```


no longer causes problems.  But other things do.

William


---

Comment by was created at 2007-01-13 01:53:51

Idea: in addition to everything else we do, whenever SAGE starts up
an interface to another system, it could write the pid and time to a file.
Then next time SAGE starts, it could check taht the given pid is not running
(unless the pid is from more than 1 week ago?)
and delete it from that file (or kill it then delete it).  I.e., create 
a "processes that were started" log on disk.  This might help deal with
the problem of zombie processes... unless of course the pid of the zombie
is unknown ever !?


---

Comment by was created at 2007-01-22 21:37:29

I wrote a "sage-cleaner" daemon, which I *think* totally deals with this problem and more very nicely (and gets rid of the need for the monitor process).  I have tested it extensively on OS X and it works perfectly.   Only further testing will tell for sure, but for now (and for SAGE-1.8) this bug is closed.


---

Comment by was created at 2007-01-22 21:37:29

Resolution: fixed
