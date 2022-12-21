# Issue 8756: random segfault in planarity.pyx test

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-24 21:59:18

Assignee: jason, ncohen, rlm

CC:  jason boothby mvngu ncohen leif


```
wstein`@`ubuntu32:/tmp/wstein/farm/sage-4.4.rc0$ grep "long" "devel/sage/sage/graphs/planarity.pyx"
        sage: import networkx.generators.atlas  # long time
        sage: atlas_graphs = [Graph(i) for i in networkx.generators.atlas.graph_atlas_g()] # long time
        sage: a = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time
        sage: b = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time
        sage: a == b # long time
wstein`@`ubuntu32:/tmp/wstein/farm/sage-4.4.rc0$ grep "long" "devel/sage/sage/graphs/planarity.pyx" | ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
| Sage Version 4.4.rc0, Release Date: 2010-04-23                     |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in Sage.
This probably occured because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------
```



---

Comment by was created at 2010-04-24 22:03:57

Changing priority from blocker to critical.


---

Comment by jhpalmieri created at 2010-04-24 22:17:44

This could be related to #4509.


---

Comment by cremona created at 2010-04-25 20:40:32

This may be relevant data:  I am doing a long test of everything in a fresh build of 4.4.rc0 (the non-long passed ok) on 32-bit ubuntu.  After more than 10 hours this has not yet finished, and currently running are

```
john`@`ubuntu%ps ux | grep sage
john      4886  0.0  0.1   5136  3452 pts/1    S+   17:37   0:00 python /home/john/sage-current/local/bin/sage-cleaner
john      5352  0.0  0.0   4296  1504 pts/1    S+   10:49   0:00 bash /home/john/bin/sage -t -long sage-4.4.rc0/devel/
john      5355  0.0  0.0   4400  1632 pts/1    S+   10:49   0:00 bash /home/john/sage-current/local/bin/sage-sage -t -long sage-4.4.rc0/devel/
john      5367  0.0  0.1   5652  3912 pts/1    S+   10:49   0:09 python /home/john/sage-current/local/bin/sage-test -long sage-4.4.rc0/devel/
john      5770  0.0  0.0   1772   484 pts/1    S+   21:38   0:00 sh -c /home/john/sage-current/local/bin/sage-doctest -long "sage-4.4.rc0/devel/sage-main/build/sage/graphs/digraph.py"
john      5773  5.0  0.1   6684  5000 pts/1    S+   21:38   0:00 python /home/john/sage-current/local/bin/sage-doctest -long sage-4.4.rc0/devel/sage-main/build/sage/graphs/digraph.py
john      5778  0.0  0.0   1772   484 pts/1    S+   21:38   0:00 /bin/sh -c python /home/john/.sage//tmp/.doctest_digraph.py
john      5779 77.0  2.7 157512 86152 pts/1    R+   21:38   0:01 python /home/john/.sage//tmp/.doctest_digraph.py
john      5785  0.0  0.0   3008   756 pts/3    R+   21:38   0:00 grep sage
john     15235 96.7  2.9 163720 91196 pts/1    R+   18:36 175:47 python /home/john/.sage//tmp/.doctest_planarity.py
```

Now 10:49 is when the test started, and now it's 21:39.  But note that the planarity thing has been running for almost 3 hours.  No segfault, but surely doctests should not run for 3 hours even with the "-l" option?


---

Comment by was created at 2010-04-27 05:00:18

Changing priority from critical to blocker.


---

Comment by cremona created at 2010-04-27 08:17:19

More data:  that long test run of 4.4.rc0 was still running after more than 24 hours.  It seemed to be going round in circles, i.e. rerunning everything over and over.  And the test on this particular file ran for hours, and also kept on duplicating itself.  As this was on just a laptop with 2-core processor, I killed it.


---

Comment by jason created at 2010-04-27 12:19:26

Whoever investigates this, here was another segfault in the planarity testing that was fixed a while ago: #4509

I hope they're not related, but it might be something to keep in mind if someone is investigating the issue (maybe someone can try *just* running the code on connected graphs, or just on disconnected graphs to try to narrow things down). In that case, according to John Boyer (the author of the C code we use):

"I'll say up front that you're absolutely right that my reference implementation does not pay any real attention to isolated vertices as they have nothing really to do with the correctness of the algorithm."

The problem in that case was that we were segfaulting on graphs with vertices of degree zero (i.e., isolated vertices).  I wonder if that is causing a problem somewhere else in his code, or if somehow we are seeing the same issue again (was that code changed recently?).

One possible option is to upgrade to John Boyer's latest complete rewrite of planarity testing code, of which he says:

"the only code on which I am comfortable with claiming support for disconnected graphs is the new "version 2.0" code.

"The reason I say it is possibly fortunate is that it should be precious little effort for you to consider adopting this new code since I kept backwards compatibility at a high priority. You are quite unlikely to have done anything that is not supported under the new code, though I can help you if there are *any* issues. Best of all, you can actually get the code because I've made it publicly available from a Google Code project.

     http://code.google.com/p/planarity"


---

Comment by jason created at 2010-04-27 17:40:00

I attached three patches.  The first removes the current version of the planarity code from Sage.  The second updates the planarity C code to the most recent SVN version of John Boyer's code (at  http://code.google.com/p/planarity).  The third makes some changes in Sage so that it will compile and build.

These patches are against 4.3.4, and are after the networkx upgrading patches in my queue, so they may depend on upgrading networkx to 1.0.1 (see #7608).

The patches do not conform to the standards (no good commit messages; no trac number noted), and may possibly break other stuff.  However, -long doctests pass in graphs/*.py[x], and John Boyer said that he worked hard to make the new code compatible with the old code, so I *hope* the patches work.

I mainly post these to provide a starting point for someone to finish fixing this.  I'll probably do it in several weeks (after the semester ends) if someone else hasn't done it.

Ideally, we'd make this a standard spkg at this point, instead of including this code in Sage.  ncohen I think would know how to do that (i.e., make a standard spkg that a pyx file in Sage depends on to compile).


---

Comment by jason created at 2010-04-27 17:40:12

Changing status from new to needs_work.


---

Comment by jason created at 2010-04-27 17:41:56

The new C code also has some new features, I think, like testing for outerplanarity, some sort of graph coloring stuff, etc.


---

Comment by jason created at 2010-04-30 05:37:56

In an email exchange with John Boyer, he says:

"Finally, if you did grab the latest copy of my code, you probably didn't notice that the copyright message on the four graphK4*.* files is not the BSD license, but rather a do-not-copy message.  This was because I haven't submitted a paper covering this one, though I do now have the write-up for it as part of a larger paper.  Anyway, sorry about the inconvenience here. I've amended the files to apply the bsd license to the K4 search, so if you simply download the trunk again, using your patch technique to get rid of nauty, you should be good to go."

So the above patch should be rebased on the current SVN sources of the planarity code (with the right license statements on those files).


---

Comment by leif created at 2010-05-15 23:03:50

Previously, *every* long test run on planarity.pyx failed on my Ubuntu 9.04 x86/Prescott (gcc 4.3.3) (see http://groups.google.com/group/sage-release/msg/560824983a71627f).

After applying the three patches on top of 4.4.2.rc0 (no rejects), all seems fine: 
Running 100 times

```
./sage -t -long devel/sage/sage/graphs/planarity.pyx
```

no errors occurred. (Also `devel/sage/sage/graphs` passed.)

Just for the record, the (second) patch contains two Eclipse project files (and some text files for comparing the output of tests I guess).

-Leif


---

Comment by jason created at 2010-05-16 03:09:49

John Boyer also said this to me about the new planarity code:


"I had to change NONPLANAR to NONEMBEDDABLE due to outerplanarity, but otherwise there's really only additions to the interface, so you're in pretty good shape once you can compile.  The only other question I would have is whether you have any code that traversed adjacency lists, or do you just call my functions.  I found I got more speed when I changed from a circular list that included the vertex. There is a macro you can define to put the CIRCULAR back in the lists, but the code is faster if you don't use it.  Moreover, if you traverse adjacency lists using my actual functions, you were good anyway.

"You should also note that my library sets a default graph size capable of accommodating 3N edges (6N arcs, or half edges), but it is easy in the new version to override that by calling gp_EnsureArcCapacity().  Of course, the 3N setting is there because you only need 3N of the edges in any graph to ensure that it comes to the right conclusion for any of the planarity-related algorithms in the current package.  My code that called nauty would increase the arc capacity to ensure the whole graph was processed, but it's your choice whether you want to do that.

"You should also note that the latest copy of the package contains a new algorithm that is not strictly planarity-related.  It creates a correct coloring of a graph using minimum degree selection.  However, it also implements a special technique that ensures any planar graph will have at most 5 colors.  And linear time in the size of the graph of course. "

The third patch above makes the necessary changes in Sage regarding NONPLANAR vs. NONEMBEDDABLE.  The other issues should be checked, though.


---

Attachment

apply on top of previous patches


---

Comment by jason created at 2010-05-16 03:32:20

apply on top of previous patches


---

Attachment

I've attached patches which have the necessary commit messages.  I also removed the Eclipse and example data files from the code.  The new second patch now also has the updated BSD license in the graphK4* files.

There is a problem compiling these patches on OSX (the C code has #include <malloc.h>, which is apparently a problem on OSX).


---

Comment by leif created at 2010-05-16 04:17:50

Replying to [comment:14 jason]:
> I've attached patches which have the necessary commit messages.  I also removed the Eclipse and example data files from the code.  The new second patch now also has the updated BSD license in the graphK4* files.

I tried ~5 times to get the new ones (I saw the changes in trac) but the browser always "downloaded" the old ones... 8/

The new ones still work with Ubuntu 9.04 x86/Prescott. :)

> There is a problem compiling these patches on OSX (the C code has #include <malloc.h>, which is apparently a problem on OSX).

I don't have apples here (besides a IIe), so somebody else has to test/fix that.

(Enhancements should perhaps be made on another ticket.)

-Leif


---

Comment by leif created at 2010-05-16 05:19:47

The patch just `#define`s `_XOPEN_SOURCE` (if not already defined) and includes `stdlib.h` instead of `malloc.h` in two files.

Note that compiling with `-std=c99` (ISO C99) already implies presence of `stdlib.h` (and `malloc()` being defined _there_).

(Apply only if needed, on top of the other three patches.)


---

Comment by leif created at 2010-05-16 05:43:58

Replying to [comment:16 leif]:

P.S.: Shouldn't we report/fix this upstream?


---

Attachment

Removes <malloc.h> inclusion by <stdlib.h>. (2nd version)


---

Comment by leif created at 2010-05-16 06:22:38

My comments above apply to the patch I've just uploaded/freshened (too).


---

Comment by rlm created at 2010-05-27 23:32:01

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-05-27 23:32:01

This newest patch allows the code to compile on OS X, as I have verified.


---

Comment by rlm created at 2010-05-27 23:40:00

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-05-27 23:40:00

Looks good to me. Compiles on OS X, doesn't segfault on ubuntu32...


---

Comment by leif created at 2010-05-28 02:47:37

Funny, I just realized that _this_ doctest failure seemed to have vanished in 4.4.3.alpha0 (again on Ubuntu 9.04 x86/32-bit, ptestlong), because there's now _another_ test failing, but in `sage/graphs/generic_graph.py`.

Testing only the single file `sage/graphs/planarity.pyx` on vanilla 4.4.3.alpha0, it reproducably shows up again.

I'll apply this patch to 4.4.3.alpha0 later...


---

Comment by leif created at 2010-05-31 19:29:54

Replying to [comment:21 leif]:
> I'll apply this patch to 4.4.3.alpha0 later...

ptestlong: No doctest failures related to this patch (Ubuntu 9.04 x86/32-bit).


---

Comment by was created at 2010-06-03 04:05:49

Resolution: fixed


---

Comment by was created at 2010-06-03 04:05:49

Merged into sage-4.4.3.alpha2
