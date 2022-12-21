# Issue 8677: race condition creating dirs during Sage build on RH 5.4

Issue created by migration from Trac.

Original creator: GeorgSWeber

Original creation time: 2010-04-12 20:58:49

Assignee: GeorgSWeber

In a recent thread: http://groups.google.com/group/sage-devel/browse_thread/thread/97f1e17019caf2d0# it was reported, that  " sage 4.3.5 won't build on Red Hat Enterprise Linux 5.4: File exists: '/usr/local_machine/sage-4.3.5/local//lib/python/site-packages//sage/structure' " The partial log output was:


```
python `which cython` --embed-positions --directive cdivision=True
-I/usr/local_machine/sage-4.3.5/devel/sage-main -o sage/stats/hmm/chmm.c
sage/stats/hmm/chmm.pyx
sage/stats/hmm/chmm.pyx -->
/usr/local_machine/sage-4.3.5/local//lib/python/site-packages//sage/stats/hmm/chmm.pyx
python `which cython` --embed-positions --directive cdivision=True
-I/usr/local_machine/sage-4.3.5/devel/sage-main -o
sage/structure/coerce_dict.c sage/structure/coerce_dict.pyx
sage/structure/coerce_dict.pyx -->
/usr/local_machine/sage-4.3.5/local//lib/python/site-packages//sage/structure/coerce_dict.pyx
python `which cython` --emTraceback (most recent call last):
   File "setup.py", line 754, in <module>
     execute_list_of_commands(queue)
   File "setup.py", line 250, in execute_list_of_commands
     execute_list_of_commands_in_parallel(command_list, nthreads)
   File "setup.py", line 191, in execute_list_of_commands_in_parallel
     for r in p.imap(apply_pair, command_list):
   File
"/usr/local_machine/sage-4.3.5/local/lib/python/multiprocessing/pool.py",
line 520, in next
     raise value
OSError: [Errno 17] File exists:
'/usr/local_machine/sage-4.3.5/local//lib/python/site-packages//sage/structure'
sage: There was an error installing modified sage library code.

ERROR installing SAGE

real    1m56.499s
user    8m27.884s
sys     0m19.321s
sage: An error occurred while installing sage-4.3.5
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /usr/local_machine/sage-4.3.5/install.log.  Describe your computer,
operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/usr/local_machine/sage-4.3.5/spkg/build/sage-4.3.5 and type 'make
check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/usr/local_machine/sage-4.3.5/spkg/build/sage-4.3.5' &&
'/usr/local_machine/sage-4.3.5/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
make[1]: *** [installed/sage-4.3.5] Error 1
make[1]: Leaving directory `/usr/local_machine/sage-4.3.5/spkg'

real    59m35.961s
user    64m50.926s
sys     11m16.115s
Error building Sage.
warning:
/usr/local_machine/sage-4.3.5/devel/sage-main/sage/structure/parent_base.pyx:63:4:
Overriding cdef method with def method.
warning:
/usr/local_machine/sage-4.3.5/devel/sage-main/sage/structure/parent.pyx:118:4:
dict already a builtin Cython type 
```

My suspicion is, that the reason is some race condition in checking, whether during the build some directory has to be newly added, or already exists.


---

Comment by tomc created at 2010-04-13 09:23:11

That is consistent with the fact that I have previously built Sage successfully: this was exactly the same version of Sage, on exactly the same hardware.  The only difference between the two situations was that before the unsuccessful build I did 'export MAKE="make -j6"' to make the build process use 6 jobs in parallel, whereas the successful build used only one build job.


---

Comment by craigcitro created at 2010-04-14 06:15:27

Yep, this is a race condition. I hit exactly this problem for the "second" half of the parallel build stuff -- namely dispatching calls to gcc in parallel. The fix there would work here: at some point before the parallel dispatch, I walked the tree and made sure to create all the necessary directories. The other option would be to catch and ignore the `OSError`, but I think that's a horrible idea. Well, that's not completely true -- if you checked the error message, and confirmed that the filename it complained about was a directory that does now exist, it would probably be fine to ignore it and move on.

There's nothing RH specific about this -- I think it was just bad luck.


---

Comment by was created at 2010-10-02 06:26:21

I setup NFS on disk.math and sage.math, and when I export an NSF share using the async option two things happen: 

    (1) the filesystem is noticeably *much* faster,

    (2) I can repeatedly get the error that is being discussed here with, e.g., MAKE="make -j8" on sage.math. 

Probably the RedHat system Tom Coates was using has a similar NFS setup.


---

Comment by was created at 2010-10-02 06:36:21

Changing priority from major to critical.


---

Attachment


---

Comment by was created at 2010-10-02 06:44:32

Changing priority from critical to blocker.


---

Comment by was created at 2010-10-02 06:44:32

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-10-02 08:21:29

With `async` set, do we need to worry more than usual about data corruption?  According to [this Linux NFS FAQ](http://nfs.sourceforge.net/#faq_b6), `async` is potentially unsafe.

Should we do as Craig suggests above, e.g., `pass` in the `except` block if `dirname` now exists, but `raise` otherwise?


---

Comment by vbraun created at 2010-10-02 09:48:22

A correctly working NFSv3 shouldn't need the `async` options to achieve fast writes, but maybe some older servers/clients are being used? With `async`, data will be corrupted if the server crashes, but thats probably acceptable on a build system.

I take issue with the patch, however. The current race seems to be 

```
    if not os.path.exists(path): 
        # another process can create path here
        os.makedirs(path) 
        # error!
```

The correct fix would be to replace the whole if clause with 

```
    try: 
        os.makedirs(path) 
    except OSError: 
        pass 
```

But the patch mixes up both. It still contains the original race and then hacks around it to trap the error.


---

Comment by was created at 2010-10-02 17:18:23

> A correctly working NFSv3 shouldn't need the async options to achieve fast writes

Are you just making this up, or?!

> The correct fix would be to replace the whole if clause with ...

I strongly disagree.  I see no point in not including the

```
if not os.path.exists(dirname):
```

code, since that makes perfect sense when doing a serial build, which is what most people do.


---

Comment by vbraun created at 2010-10-02 17:35:41

Replying to [comment:8 was]:
> Are you just making this up, or?!

Thats what the aforementioned FAQ says:

```
For the Linux implementation of NFS Version 3, using the "async" export option to allow faster writes is no longer necessary. NFS Version 3 explicitly allows a server to reply before writing data to disk, under controlled circumstances.
```


> I strongly disagree.  I see no point in not including the
> if not os.path.exists(dirname):

The point is that the pattern "if (look at filesystem) then (modify filesystem)" is fundamentally flawed. Its the origin of countless security problems from temp races etc. The world is a better place without it :-) And the only way to make it die is to stomp it out wherever we encounter it...


---

Comment by mpatel created at 2010-10-02 22:40:21

Replying to [comment:9 vbraun]:
> Replying to [comment:8 was]:
> > I strongly disagree.  I see no point in not including the
> > if not os.path.exists(dirname):
> The point is that the pattern "if (look at filesystem) then (modify filesystem)" is fundamentally flawed. Its the origin of countless security problems from temp races etc. The world is a better place without it :-) And the only way to make it die is to stomp it out wherever we encounter it...

What if we use William's solution for the first "hunk" and Volker's for the second?  Then we can avoid many unnecessary exceptions in the first.  In the second, we only call `os.makedirs` if copying the Cython-compiled file fails.


---

Attachment

Alternate version, fix commit string.  Apply just one patch.


---

Comment by mpatel created at 2010-10-05 05:56:39

Replying to [comment:10 mpatel]:
> What if we use William's solution for the first "hunk" and Volker's for the second?  Then we can avoid many unnecessary exceptions in the first.  In the second, we only call `os.makedirs` if copying the Cython-compiled file fails.

I've add a patch that does this.


---

Comment by vbraun created at 2010-10-05 10:00:18

Sorry, maybe I did not understand the issue. Is this about improving performance? Is that microsecond really going to matter in a loop where we copy files and/or call the compiler?

In any case, I think mixing the two patterns is taking the worst of both worlds ;-) I'll attach my version of the patch in case I wasn't clear enough.


---

Comment by vbraun created at 2010-10-05 10:00:49

Yet another alternate version


---

Attachment

With a clean, built-from-scratch 4.6.alpha3 on sage.math, I applied v3, did `rm -rf devel/sage/build/` and then `env MAKE="make -j20" ./sage -ba-force`.  The latter fails after a number of 
`python `which cython`` commands:

```python
[...]
Traceback (most recent call last):
  File "setup.py", line 799, in <module>
    execute_list_of_commands(queue)
  File "setup.py", line 319, in execute_list_of_commands
    execute_list_of_commands_in_parallel(command_list, nthreads)
  File "setup.py", line 252, in execute_list_of_commands_in_parallel
    process_command_results(p.imap(apply_pair, command_list))
  File "setup.py", line 256, in process_command_results
    for r in result_values:
  File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha3-working2/local/lib/python/multiprocessing/pool.py", line 520, in next
    raise value
NameError: global name 'path' is not defined
sage: There was an error installing modified sage library code.
```

This doesn't happen with v1 or v2, but I'm not sure why.  Thoughts?


---

Comment by jhpalmieri created at 2010-10-11 20:37:50

> This doesn't happen with v1 or v2, but I'm not sure why. Thoughts?

Probably on lines 687-690, "path" should be "dirname"?  I'm attaching a new version with this change.  Since all of the other patches list William as the author, I'm doing the same for this one...


---

Attachment

Still another alternate version


---

Comment by mpatel created at 2010-10-11 21:54:47

Replying to [comment:14 jhpalmieri]:
> > This doesn't happen with v1 or v2, but I'm not sure why. Thoughts?
> 
> Probably on lines 687-690, "path" should be "dirname"? [...]

"D'oh!" Thanks, John.


---

Comment by mpatel created at 2010-10-11 23:29:29

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-10-21 07:38:29

Resolution: fixed


---

Comment by leif created at 2010-10-22 09:19:24

Just for the record:

Though I've seen this not very often (I think the first time with 4.6.alpha2), I can confirm that running into the race condition wasn't limited to NFS-mounted file systems...
