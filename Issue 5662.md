# Issue 5662: Nasty hang (deadlock?) in maxima pexpect interface on core 2 quad

Issue created by migration from https://trac.sagemath.org/ticket/5662

Original creator: tornaria

Original creation time: 2009-04-01 22:02:15

Assignee: was

I've spent the past few days tracking down a very nasty issue in my recently installed sage notebook server. I have the problem nailed down, and I can reproduce it with relative ease. This seems a timing issue between threads running in parallel, so a heisenbug, but I have a way to reproduce it with high chance (with expected time in the order of a minute) in the actual hardware, and with *extremely* high chance in the KVM virtual machine.

I have no idea how to fix the issue, but I have a (quite unsatisfactory) workaround: use a KVM with one processor only, or pin sage and its children processes to a fixed core (read below for more info). In the real hardware, pinning sage to a couple of processors which share L2 seems to completely "fix" the issue, while pinning sage to a couple processors with different L2 seems to hit the issue more often.

I wasn't able to reproduce any of this on a core 2 duo -- I don't remember something like this happening to me before, but these days I've been trying harder with the specific things which hang the core 2 quad.

Additionally, I discussed the issue on IRC with Dan Drake, who also had the same issue after switching to a core 2 quad.

I've been unable to reproduce this on sage.math either.

### Hardware

 - real: core 2 quad Q9550. This is a pair of two core chips with 6Mb L2 each, in a single package. IOW, cpus 0 and 1 share 6MB of L2, while cpus 2 and 3 share another 6MB of L2. There's no L3 cache. The main memory is 8Gb of DDR-2 in two channels (4 x 2Gb modules). The clock speed is 2.83GHz (no overclocking) and the FSB should be 1333 according to cpu and mb specs (I don't know how to tell).

 I can't reproduce the issues described here in the real hardware using only the pair of cpus 0,1 (which share L2), neither using only the pair of cpus 2,3 (also share L2). OTOH, using a pair of processors with different L2 seems to make the issue easier to reproduce. Also, 0,2 and 0,3 seem to cause the issue more often than 1,2 or 1,3.

 To pin sage and subprocesses to a specific cpuset, I use taskset(1).

 - virtual: KVM version 72, for the notebook server with 2GB ram and 2 cpu.

 I can't reproduce any of this in a virtual machine with only 1 virtual cpu, and neither with a virtual machine with 2 virtual cpus but pinning sage to a unique virtual cpu.

 OTOH, I tried pinning the KVM process (with 2 virtual cpus) in the real hardware to cpus 0,1 or alternatively to cpus 2,3, but this doesn't seem to prevent the issue inside the VM.


### Sage version

 Everything here is based on sage-3.4. This was compiled in the real hardware and -bdist'ed to the vitual CPUs, and I've also tried with trees compiled inside the virtual machines themselves.


### Original symptoms (nastyness factor of this issue)

 a. *the notebook*: random hangs which cannot be interrupted (sometimes not even "restart the worksheet" will work, it seems the worksheet can be stopped from the home page only). Empirically seems to always be related to symbolic stuff. 

 This affects me a lot in the notebook server for the department, which I run inside a KVM machine as described above. Starting today, as a workaround, I'm trying to use taskset to run the sage notebook process group pinned to cpu=1 exclusively (I don't know if this will stick or change when processes get renewed).

 This is a very unsatisfactory workaround... OTOH I could try with the server_pool option to use two users -- one pinned to cpu=0, the other to cpu=1, which could be a more satisfactory setup.

 b. *doctest*: many doctests failures by timeout --- a particular doctest hangs for 360s before being killed --- no CPU time is used while the doctest is hung. This happens much less often in the real hardware, but it happens nevertheless.

 Here's a typical run of the -testall in the real hardware (no cpu pinning). Failed tests:

```
sage -t  "devel/sage/sage/rings/power_series_ring.py"
sage -t  "devel/sage/sage/calculus/calculus.py"
```

 with total time for all tests: 2935.1 seconds.

 A run of -testall inside the KVM may have the following failed tests:

```
        sage -t  "devel/sage/doc/fr/tutorial/tour_plotting.rst"
        sage -t  "devel/sage/sage/functions/piecewise.py"
        sage -t  "devel/sage/sage/functions/special.py"
        sage -t  "devel/sage/sage/matrix/matrix_symbolic_dense.pyx"
        sage -t  "devel/sage/sage/matrix/matrix2.pyx"
        sage -t  "devel/sage/sage/matrix/matrix_sparse.pyx"
        sage -t  "devel/sage/sage/matrix/matrix_integer_dense.pyx"
        sage -t  "devel/sage/sage/rings/arith.py"
        sage -t  "devel/sage/sage/rings/number_field/order.py"
        sage -t  "devel/sage/sage/rings/number_field/number_field_ideal.py"
        sage -t  "devel/sage/sage/rings/number_field/number_field.py"
        sage -t  "devel/sage/sage/libs/fplll/fplll.pyx"
        sage -t  "devel/sage/sage/libs/pari/gen.pyx"
        sage -t  "devel/sage/sage/interfaces/lisp.py"
        sage -t  "devel/sage/sage/interfaces/maxima.py"
        sage -t  "devel/sage/sage/calculus/wester.py"
        sage -t  "devel/sage/sage/calculus/tests.py"
        sage -t  "devel/sage/sage/calculus/calculus.py"
        sage -t  "devel/sage/sage/calculus/equations.py"
        sage -t  "devel/sage/sage/combinat/partition.py"
        sage -t  "devel/sage/sage/plot/tachyon.py"
        sage -t  "devel/sage/sage/plot/line.py"
        sage -t  "devel/sage/sage/plot/plot.py"
        sage -t  "devel/sage/sage/plot/animate.py"
        sage -t  "devel/sage/sage/plot/plot3d/parametric_plot3d.py"
        sage -t  "devel/sage/sage/plot/plot3d/plot3d.py"
        sage -t  "devel/sage/sage/tests/book_stein_ent.py"
        sage -t  "devel/sage/sage/gsl/integration.pyx"
        sage -t  "devel/sage/sage/quadratic_forms/extras.py"
```

 with total time for all tests: 13042.9 seconds. This is quite long, but 29 timed out tests at 360 seconds each accounts for 10440 seconds...

 Note that the actual doctests which fail vary among runs of the test suite. I'd expect all of them to have symbolics of some sort used.

### How I reproduce the issue

 Choosing randomly from one of the failed doctests, I settled on this sage line as a trigger:

```
L = [(i/100.0, maxima.eval("jacobi_sn (%s/100.0,2.0)" % i)) for i in range(-300,300)]
```

 This line takes less than 5-10 seconds to evaluate --- when it finishes. If it hangs, it will hang forever --- using 0% cpu time. It only uses about 1 second or less of cpu before hanging.

 I use the following script to repeatedly test to failure (up to 1000 times):

```
CPU=0,2
for i in {0,1,2,3,4,5,6,7,8,9}{0,1,2,3,4,5,6,7,8,9}{0,1,2,3,4,5,6,7,8,9}
do
  echo
  echo RUN "$i ($CPU):"
  /usr/bin/time taskset -c $CPU ./sage -c 'L = [(i/100.0, maxima.eval("jacobi_sn (%s/100.0,2.0)" % i)) for i in range(-300,300)]' || break
done
```

 This uses `taskset -c 0,2` to force running on a couple of cores with different L2 cache, as described above. If the CPU variable is set to 0,1 or 2,3 instead, the issue doesn't happen 

 In typical tests on the real hardware, this hangs in less than 10 runs for CPU=0,2 or CPU=0,3, but it only hung in run 28 for a test with CPU=1,2. It completes 1000 runs with CPU=0,1 or CPU=2,3.

 On the KVM with 2 virtual cpus, this hangs much more often when using two processors (CPU=0,1, or don't use taskset). When using a single processor (either taskset inside 2 virtual cpus, or just run KVM with 1 virtual cpu) it completes the 1000 runs without failure.

 I did some tests in `sage.math`, but there are many more pairs of cpus to try... I tried using CPU=2,14 ; CPU=2,15 ; CPU=2,16 without failure on a run of 1000 as above (these 2,14,15,16 are 4 of the 6 cores in the physical unit = 2, if I correctly interpreted `/proc/cpuinfo`).


---

Comment by tornaria created at 2009-04-01 22:20:55

Running

```
taskset -c 0 /usr/bin/time ./sage -testall
```

In a KVM with 2 cpus, yielded the following test failures and timing:

```
        sage -t  "devel/sage/sage/interfaces/r.py"
Total time for all tests: 2873.7 seconds
Please see /home/tornaria/sage-3.4/tmp/test.log for the complete log from this test.
1933.32user 665.16system 47:59.33elapsed 90%CPU (0avgtext+0avgdata 0maxresident)k
152272inputs+530048outputs (326major+61934226minor)pagefaults 0swaps
```

I don't know what's with the `r.py` doctests, but it seems inocuous... (something about missing documentation).


---

Comment by ddrake created at 2009-04-01 23:31:48

I've run the script, and it always fails. Over ten runs, on average it hung on run 19.3 and never got past 50 runs. I'll change the script and see what happens when the threads share some L2.


---

Comment by tornaria created at 2009-04-02 00:58:34

WRT doctesting, here's a more careful comparision in the actual hardware:
 a. using `taskset -c 0,1`

```
All tests passed!
Total time for all tests: 2194.2 seconds
Please see /home/tornaria/sage/sage-3.4/tmp/test.log for the complete log from this test.
1749.80user 243.11system 36:40.26elapsed 90%CPU (0avgtext+0avgdata 0maxresident)k
141736inputs+448744outputs (365major+62065374minor)pagefaults 0swaps
```

 b. using `taskset -c 0,2`

```
The following tests failed:


        sage -t  "devel/sage/sage/rings/number_field/number_field.py"
        sage -t  "devel/sage/sage/matrix/matrix_symbolic_dense.pyx"
        sage -t  "devel/sage/sage/calculus/var.pyx"
        sage -t  "devel/sage/sage/misc/functional.py"
        sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_generic.py"
        sage -t  "devel/sage/sage/functions/piecewise.py"
Total time for all tests: 4299.8 seconds
Please see /home/tornaria/sage/sage-3.4/tmp/test.log for the complete log from this test.
1685.06user 257.93system 1:11:45elapsed 45%CPU (0avgtext+0avgdata 0maxresident)k
616inputs+447160outputs (0major+61392473minor)pagefaults 0swaps
```

The 6 failed tests where due to timeout after 360 sec, making up for 2160 secs in the total time.


---

Comment by ddrake created at 2009-04-02 05:43:11

When change the script do use cores 0 and 1, I still get timeouts, but on average it takes 229 runs before the process hangs. So it does seem like the choice of cores affects this.


---

Comment by ddrake created at 2009-04-03 07:05:02

I've done further testing, and things go indeed work better when running on cores 0 and 1, or on cores 2 and 3. The average number of runs before failure on those pairs of cores is 241 and 263, respectively, and on any other combination (I'm a combinatorialist, and had to try all six possibilities :) the average was 19, 31, 38, and 69 runs before failure. Each of these averages is from ten iterations of the script.


---

Comment by tornaria created at 2009-04-03 14:18:41

Expect script to demonstrate the maxima hang outside of sage/python


---

Attachment

Thanks Dan for your testing.

I have two new developments on this story:

 a. I kind of understand what is happening (but not why!), and I am able to reproduce the hang outside of sage with a small expect script ([attachment:maxima_expect maxima_expect]). Just `apt-get install expect` if you don't already have it installed, and run

```
taskset -c 0,2 expect -f maxima_expect > /dev/null
```

 Using this taskset seems to maximize the chances to hit the bug. The expect is quite verbose, so it's wise to redirect the output -- besides, the race condition seems to hit easier when redirecting to /dev/null; but it still happens when echoing to the console (it may help to pipe the output through cat for buffering).
 b. I have a _very_ preliminary workaround in sage -- the idea is to add a timeout at the exact point where the hang happens, and if so resynchronize everything and reissue the command. This has the potential to affect slow hardware which misses the timeout. In my tests with timeout=0.05 I can miss the timeout for long input strings running inside a VM -- I'm suggesting timeout=0.5. In any case, missing the timeout should reissue the computation, so...

 Here's the patch, in case someone wants to try; all tests pass for me with this --- either `taskset -c 0,2` on the real hardware, or inside a 2 cpu virtual machine.

```
diff -r 5c72dbb92d82 sage/interfaces/maxima.py
--- a/sage/interfaces/maxima.py	Wed Mar 11 21:57:15 2009 -0700
+++ b/sage/interfaces/maxima.py	Fri Apr 03 11:57:29 2009 -0300
@@ -708,7 +708,14 @@
         if not wait_for_prompt:
             return
 
-        self._expect_expr(self._display_prompt)
+        try:
+            self._expect_expr(self._display_prompt, timeout=0.5)
+        except pexpect.TIMEOUT:
+            #see trac #5662
+            #print "RESEND (%s)" % line
+            self._synchronize()
+            self._sendline(line)
+
         self._expect_expr()
         out = self._before()
         if error_check:
```

 I'm not proposing this as a fix (yet), but it may be useful to test it (a. on quad cores where the issue is found and b. on other machines/slow machines to see if this affects them somehow).
 In the end, as suggested by (a) above, the true bug may lie either in maxima or clisp, and it would be nice to have it fixed there --- but reading lisp makes me sick... (it always has, it's an innate virtue of mine).


---

Comment by tornaria created at 2009-04-04 03:13:17

Changing status from new to assigned.


---

Comment by tornaria created at 2009-04-04 03:13:17

Changing assignee from was to tornaria.


---

Comment by tornaria created at 2009-04-04 04:12:28

FOR REVIEW ONLY: proposed changes to clisp spkg (part 2)


---

Attachment

In seems the issue is caused by some bug in clisp and/or readline. Disabling readline seems to get rid of the isue. The proposed changes are as follows:

 1. add a hack to clisp so that readline is disabled when the environment variable `SAGE_CLISP_DISABLE_READLINE_HACK` is set. This subverts the function `stdio_same_tty_p()` which is only used in clisp to decide whether to disable readline or not, c.f.
http://article.gmane.org/gmane.lisp.clisp.devel/16534.
 Note that
  a. `maxima --disable-readline` is broken, which would be an ideal solution.
  b. the alternative to this hack is to disable readline support when compiling clisp. But this would mean that `sage -maxima` (presumably run interactively) would not support readline at all.
 This hack is implemented in a proposed [clisp-2.46.p8.spkg](http://sage.math.washington.edu/home/tornaria/maxima-pexpect-bug/clisp-2.46.p8.spkg). As an aid to the reviewer, the changes in this spkg are displayed in attachment:clisp-2.46.p7-p8.reduced.patch and attachment:stream.d.patch.

 2. In order for this fix to be inherited by maxima, a version bump is required. For that purpose I've prepared [maxima-5.16.3.p0.spkg](http://sage.math.washington.edu/home/tornaria/maxima-pexpect-bug/maxima-5.16.3.p0.spkg). The change is minimal, just add a line to the changelog as exhibited in attachment:maxima-5.16.3-p0.patch.

 3. To enable the hack in the maxima pexpect interface in Sage, a patch to the library needs to be applied. This is the content of attachment:trac_5662.patch which needs to be merged if the proposal gets positive review.

Please ignore the attachment `unix.d.patch` which I uploaded by mistake.


---

Comment by tornaria created at 2009-04-04 04:42:09

A (minor) quirk with this fix is that after the maxima pexpect interface is run at least once, the environment variable `SAGE_CLISP_DISABLE_READLINE_HACK` will be globally set in the Sage process. Hence, if we launch a shell from Sage, the variable will be set, and thus maxima will have readline disabled in the shell.


---

Comment by mabshoff created at 2009-04-05 22:48:41

After talking to William about this: We will merge the fix, but use a different solution to the env variable problem by creating a special maxima-no-readline script that just sets the env variable before calling Maxima.

Cheers,

Michael


---

Comment by ddrake created at 2009-04-06 01:48:24

Wow:

```
RUN 999 (0,2):
1.20user 0.61system 0:04.02elapsed 45%CPU (0avgtext+0avgdata 0maxresident)k
0inputs+8outputs (0major+54195minor)pagefaults 0swaps
```

It completed when running on cores 0 and 2!


---

Comment by tornaria created at 2009-04-06 03:30:42

Replying to [comment:12 mabshoff]:
> After talking to William about this: We will merge the fix, but use a different solution to the env variable problem by creating a special maxima-no-readline script that just sets the env variable before calling Maxima.

Sounds like the proper way to do this. It will avoid the "quirk" I mentioned above.

Instead of adding a new script, I suggest adding a command line option --disable-readline to the maxima script. This will make a lot of sense since "maxima --help" indeed lists --disable-readline as an option.

*Also note* that the same issue with _maxima interface_ arises with _lisp interface_. I've been doing lots of testing, and I've finally been hit by a timeout in `sage/interfaces/lisp.py` which is clearly due to the same issue. _We should apply the same fix to that interface as well!!!_

This (lisp.py) is the only timeout that I've got since I applied the proposed fix.


---

Comment by tornaria created at 2009-04-06 04:42:08

I've put up new spkg's for clisp and maxima up in
 - http://sage.math.washington.edu/home/tornaria/maxima-pexpect-bug/clisp-2.46.p9.spkg
 - http://sage.math.washington.edu/home/tornaria/maxima-pexpect-bug/maxima-5.16.3.p1.spkg
These implement command line option "--disable-readline" for lisp/clisp and maxima scripts.

I'll post a new patch to the sage library which uses this option in the pexpect interfaces for maxima and lisp.


---

Comment by tornaria created at 2009-04-06 05:43:52

Auch... disabling readline in lisp pexpect interface causes some issues (doctest failures in lisp.py) which I don't understand...


---

Comment by tornaria created at 2009-04-06 16:01:27

Note that the lisp interface had a couple of issues before, which were not tested. The part2 patch above adds two doctests which _fail_ in sage-3.4, and fixes those as well. Somebody should read the documentation for function `str.lstrip()` more carefully :-)

Hint: try

```
"20.085537".strip("sage2")
```


The following exhibits these bugs, as tested on sage.math /usr/local/bin/sage which is stock 3.4:

```
sage: lisp.eval("2")
''
sage: lisp.set("x", 2)
sage: lisp.get("x")
'2'
sage: lisp.eval("x")
'x\n2'
```



---

Comment by mabshoff created at 2009-04-06 18:29:56

This is a 3.4.1 blocker.

Cheers,

Michael


---

Comment by ddrake created at 2009-04-08 01:07:22

With the most recent clisp and maxima spkgs and the two patches applied to 3.4.1.rc1, this problem seems completely fixed. I ran the bash script that previously never ran to completion for me, and for all six pairs of cores, it finished the 1000 iterations without getting stuck. I also ran doctests in a continuous loop overnight; before, when I ran a lot of doctests, over time I would find stuck clisp processes that just hung around. After eight hours of continuous doctesting, I had NO leftover clisp processes.

The only doctest failures with the spkgs and patches applied are already known and fixed, so this solution fixes the problem and passes doctests.


---

Comment by ddrake created at 2009-04-13 02:19:00

William asked me to change this to positive review, so I'm doing that, although I haven't in any real sense reviewed the spkg updates. But the basic idea of disabling readline when it should be disabled is sound, and the problem is gone, so I suppose a positive review is reasonable.


---

Comment by GeorgSWeber created at 2009-04-18 19:42:33

Some notes:

The changes (in the two patches for the Sage Library, and in both of the new clib spkg and the new maxima spkg) are tiny and do a good job, as Dan Drake was able to verify. They do not seem to introduce regressions (with Sage 3.1.4.r3 plus the spkgs at #5788 and #5219 and the patches/spkgs here, "make testlong" had no failures for my MacIntel OS X 10.4); I'm just building on my MacPPC to test and see whether the pexpect/maxima situation ("calculus.py" and friends) now is better there.

But --- trying to "hg import" the two patches "trac_5662.patch" and "trac_5662-part2.patch" prompts me both times to write some commit message; and neither of the two linked spkgs has a clean "hg status": in both cases, too, a "hg commit -A -m "trac #5662: some message"" (in the respective package root directories) would have been needed before the "sage -pkg" command.

Nothing that Michael (or I, for that matters) couldn't do in a few minutes, but then the wrong person, and not Gonzalo Tornaria, would show up in the three Mercurial (hg repository) histories, as the one to have done the changes. And for the public out there, the clisp spkg and the maxima spkg both bump two version numbers each, without the intermediate versions ever having had an official status. 

Cheers, gsw


---

Comment by mabshoff created at 2009-04-18 22:03:27

Replying to [comment:21 GeorgSWeber]:

> But --- trying to "hg import" the two patches "trac_5662.patch" and "trac_5662-part2.patch" prompts me both times to write some commit message; and neither of the two linked spkgs has a clean "hg status": in both cases, too, a "hg commit -A -m "trac #5662: some message"" (in the respective package root directories) would have been needed before the "sage -pkg" command.

None of the above patches will go in unchanged aside from the clisp one that patches out readline dynamically. I will also commit a diff in the posters name.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-19 07:19:48

Ok, I have deleted various patches and changed the summary. I will post a patch in Gonzalo's name shortly. You need the two spkgs from #5823 to make this work.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-19 07:22:49

This is Gonzalo's patch fixed up to match the latest clisp+maxima spkgs - apply only this patch


---

Attachment

For the record, I had a look and tested the latest version of the patch posted by mabshoff above and it looks and behaves fine for me (when used with the new spkgs from #5823).


---

Comment by mabshoff created at 2009-04-20 03:46:36

Merged trac_5662.patch in Sage 3.4.1.rc4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-20 03:46:36

Resolution: fixed
