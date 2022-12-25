# Issue 8756: random segfault in planarity.pyx test

archive/issues_008756.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  @jasongrout boothby mvngu @nathanncohen @nexttime\n\n\n```\nwstein@ubuntu32:/tmp/wstein/farm/sage-4.4.rc0$ grep \"long\" \"devel/sage/sage/graphs/planarity.pyx\"\n        sage: import networkx.generators.atlas  # long time\n        sage: atlas_graphs = [Graph(i) for i in networkx.generators.atlas.graph_atlas_g()] # long time\n        sage: a = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time\n        sage: b = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time\n        sage: a == b # long time\nwstein@ubuntu32:/tmp/wstein/farm/sage-4.4.rc0$ grep \"long\" \"devel/sage/sage/graphs/planarity.pyx\" | ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\n| Sage Version 4.4.rc0, Release Date: 2010-04-23                     |\n| Type notebook() for the GUI, and license() for information.        |\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in Sage.\nThis probably occured because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n------------------------------------------------------------\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8756\n\n",
    "created_at": "2010-04-24T21:59:18Z",
    "labels": [
        "component: graph theory",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "random segfault in planarity.pyx test",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8756",
    "user": "https://github.com/williamstein"
}
```
Assignee: jason, ncohen, rlm

CC:  @jasongrout boothby mvngu @nathanncohen @nexttime


```
wstein@ubuntu32:/tmp/wstein/farm/sage-4.4.rc0$ grep "long" "devel/sage/sage/graphs/planarity.pyx"
        sage: import networkx.generators.atlas  # long time
        sage: atlas_graphs = [Graph(i) for i in networkx.generators.atlas.graph_atlas_g()] # long time
        sage: a = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time
        sage: b = [i for i in [1..1252] if atlas_graphs[i].is_planar()] # long time
        sage: a == b # long time
wstein@ubuntu32:/tmp/wstein/farm/sage-4.4.rc0$ grep "long" "devel/sage/sage/graphs/planarity.pyx" | ./sage
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


Issue created by migration from https://trac.sagemath.org/ticket/8756





---

archive/issue_comments_079966.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2010-04-24T22:03:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79966",
    "user": "https://github.com/williamstein"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_079967.json:
```json
{
    "body": "This could be related to #4509.",
    "created_at": "2010-04-24T22:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79967",
    "user": "https://github.com/jhpalmieri"
}
```

This could be related to #4509.



---

archive/issue_comments_079968.json:
```json
{
    "body": "This may be relevant data:  I am doing a long test of everything in a fresh build of 4.4.rc0 (the non-long passed ok) on 32-bit ubuntu.  After more than 10 hours this has not yet finished, and currently running are\n\n```\njohn@ubuntu%ps ux | grep sage\njohn      4886  0.0  0.1   5136  3452 pts/1    S+   17:37   0:00 python /home/john/sage-current/local/bin/sage-cleaner\njohn      5352  0.0  0.0   4296  1504 pts/1    S+   10:49   0:00 bash /home/john/bin/sage -t -long sage-4.4.rc0/devel/\njohn      5355  0.0  0.0   4400  1632 pts/1    S+   10:49   0:00 bash /home/john/sage-current/local/bin/sage-sage -t -long sage-4.4.rc0/devel/\njohn      5367  0.0  0.1   5652  3912 pts/1    S+   10:49   0:09 python /home/john/sage-current/local/bin/sage-test -long sage-4.4.rc0/devel/\njohn      5770  0.0  0.0   1772   484 pts/1    S+   21:38   0:00 sh -c /home/john/sage-current/local/bin/sage-doctest -long \"sage-4.4.rc0/devel/sage-main/build/sage/graphs/digraph.py\"\njohn      5773  5.0  0.1   6684  5000 pts/1    S+   21:38   0:00 python /home/john/sage-current/local/bin/sage-doctest -long sage-4.4.rc0/devel/sage-main/build/sage/graphs/digraph.py\njohn      5778  0.0  0.0   1772   484 pts/1    S+   21:38   0:00 /bin/sh -c python /home/john/.sage//tmp/.doctest_digraph.py\njohn      5779 77.0  2.7 157512 86152 pts/1    R+   21:38   0:01 python /home/john/.sage//tmp/.doctest_digraph.py\njohn      5785  0.0  0.0   3008   756 pts/3    R+   21:38   0:00 grep sage\njohn     15235 96.7  2.9 163720 91196 pts/1    R+   18:36 175:47 python /home/john/.sage//tmp/.doctest_planarity.py\n```\n\nNow 10:49 is when the test started, and now it's 21:39.  But note that the planarity thing has been running for almost 3 hours.  No segfault, but surely doctests should not run for 3 hours even with the \"-l\" option?",
    "created_at": "2010-04-25T20:40:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79968",
    "user": "https://github.com/JohnCremona"
}
```

This may be relevant data:  I am doing a long test of everything in a fresh build of 4.4.rc0 (the non-long passed ok) on 32-bit ubuntu.  After more than 10 hours this has not yet finished, and currently running are

```
john@ubuntu%ps ux | grep sage
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

archive/issue_comments_079969.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2010-04-27T05:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79969",
    "user": "https://github.com/williamstein"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_079970.json:
```json
{
    "body": "More data:  that long test run of 4.4.rc0 was still running after more than 24 hours.  It seemed to be going round in circles, i.e. rerunning everything over and over.  And the test on this particular file ran for hours, and also kept on duplicating itself.  As this was on just a laptop with 2-core processor, I killed it.",
    "created_at": "2010-04-27T08:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79970",
    "user": "https://github.com/JohnCremona"
}
```

More data:  that long test run of 4.4.rc0 was still running after more than 24 hours.  It seemed to be going round in circles, i.e. rerunning everything over and over.  And the test on this particular file ran for hours, and also kept on duplicating itself.  As this was on just a laptop with 2-core processor, I killed it.



---

archive/issue_comments_079971.json:
```json
{
    "body": "Whoever investigates this, here was another segfault in the planarity testing that was fixed a while ago: #4509\n\nI hope they're not related, but it might be something to keep in mind if someone is investigating the issue (maybe someone can try *just* running the code on connected graphs, or just on disconnected graphs to try to narrow things down). In that case, according to John Boyer (the author of the C code we use):\n\n\"I'll say up front that you're absolutely right that my reference implementation does not pay any real attention to isolated vertices as they have nothing really to do with the correctness of the algorithm.\"\n\nThe problem in that case was that we were segfaulting on graphs with vertices of degree zero (i.e., isolated vertices).  I wonder if that is causing a problem somewhere else in his code, or if somehow we are seeing the same issue again (was that code changed recently?).\n\nOne possible option is to upgrade to John Boyer's latest complete rewrite of planarity testing code, of which he says:\n\n\"the only code on which I am comfortable with claiming support for disconnected graphs is the new \"version 2.0\" code.\n\n\"The reason I say it is possibly fortunate is that it should be precious little effort for you to consider adopting this new code since I kept backwards compatibility at a high priority. You are quite unlikely to have done anything that is not supported under the new code, though I can help you if there are *any* issues. Best of all, you can actually get the code because I've made it publicly available from a Google Code project.\n\n     http://code.google.com/p/planarity\"",
    "created_at": "2010-04-27T12:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79971",
    "user": "https://github.com/jasongrout"
}
```

Whoever investigates this, here was another segfault in the planarity testing that was fixed a while ago: #4509

I hope they're not related, but it might be something to keep in mind if someone is investigating the issue (maybe someone can try *just* running the code on connected graphs, or just on disconnected graphs to try to narrow things down). In that case, according to John Boyer (the author of the C code we use):

"I'll say up front that you're absolutely right that my reference implementation does not pay any real attention to isolated vertices as they have nothing really to do with the correctness of the algorithm."

The problem in that case was that we were segfaulting on graphs with vertices of degree zero (i.e., isolated vertices).  I wonder if that is causing a problem somewhere else in his code, or if somehow we are seeing the same issue again (was that code changed recently?).

One possible option is to upgrade to John Boyer's latest complete rewrite of planarity testing code, of which he says:

"the only code on which I am comfortable with claiming support for disconnected graphs is the new "version 2.0" code.

"The reason I say it is possibly fortunate is that it should be precious little effort for you to consider adopting this new code since I kept backwards compatibility at a high priority. You are quite unlikely to have done anything that is not supported under the new code, though I can help you if there are *any* issues. Best of all, you can actually get the code because I've made it publicly available from a Google Code project.

     http://code.google.com/p/planarity"



---

archive/issue_comments_079972.json:
```json
{
    "body": "I attached three patches.  The first removes the current version of the planarity code from Sage.  The second updates the planarity C code to the most recent SVN version of John Boyer's code (at  http://code.google.com/p/planarity).  The third makes some changes in Sage so that it will compile and build.\n\nThese patches are against 4.3.4, and are after the networkx upgrading patches in my queue, so they may depend on upgrading networkx to 1.0.1 (see #7608).\n\nThe patches do not conform to the standards (no good commit messages; no trac number noted), and may possibly break other stuff.  However, -long doctests pass in graphs/*.py[x], and John Boyer said that he worked hard to make the new code compatible with the old code, so I *hope* the patches work.\n\nI mainly post these to provide a starting point for someone to finish fixing this.  I'll probably do it in several weeks (after the semester ends) if someone else hasn't done it.\n\nIdeally, we'd make this a standard spkg at this point, instead of including this code in Sage.  ncohen I think would know how to do that (i.e., make a standard spkg that a pyx file in Sage depends on to compile).",
    "created_at": "2010-04-27T17:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79972",
    "user": "https://github.com/jasongrout"
}
```

I attached three patches.  The first removes the current version of the planarity code from Sage.  The second updates the planarity C code to the most recent SVN version of John Boyer's code (at  http://code.google.com/p/planarity).  The third makes some changes in Sage so that it will compile and build.

These patches are against 4.3.4, and are after the networkx upgrading patches in my queue, so they may depend on upgrading networkx to 1.0.1 (see #7608).

The patches do not conform to the standards (no good commit messages; no trac number noted), and may possibly break other stuff.  However, -long doctests pass in graphs/*.py[x], and John Boyer said that he worked hard to make the new code compatible with the old code, so I *hope* the patches work.

I mainly post these to provide a starting point for someone to finish fixing this.  I'll probably do it in several weeks (after the semester ends) if someone else hasn't done it.

Ideally, we'd make this a standard spkg at this point, instead of including this code in Sage.  ncohen I think would know how to do that (i.e., make a standard spkg that a pyx file in Sage depends on to compile).



---

archive/issue_comments_079973.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-04-27T17:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79973",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_079974.json:
```json
{
    "body": "The new C code also has some new features, I think, like testing for outerplanarity, some sort of graph coloring stuff, etc.",
    "created_at": "2010-04-27T17:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79974",
    "user": "https://github.com/jasongrout"
}
```

The new C code also has some new features, I think, like testing for outerplanarity, some sort of graph coloring stuff, etc.



---

archive/issue_comments_079975.json:
```json
{
    "body": "In an email exchange with John Boyer, he says:\n\n\"Finally, if you did grab the latest copy of my code, you probably didn't notice that the copyright message on the four graphK4*.* files is not the BSD license, but rather a do-not-copy message.  This was because I haven't submitted a paper covering this one, though I do now have the write-up for it as part of a larger paper.  Anyway, sorry about the inconvenience here. I've amended the files to apply the bsd license to the K4 search, so if you simply download the trunk again, using your patch technique to get rid of nauty, you should be good to go.\"\n\nSo the above patch should be rebased on the current SVN sources of the planarity code (with the right license statements on those files).",
    "created_at": "2010-04-30T05:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79975",
    "user": "https://github.com/jasongrout"
}
```

In an email exchange with John Boyer, he says:

"Finally, if you did grab the latest copy of my code, you probably didn't notice that the copyright message on the four graphK4*.* files is not the BSD license, but rather a do-not-copy message.  This was because I haven't submitted a paper covering this one, though I do now have the write-up for it as part of a larger paper.  Anyway, sorry about the inconvenience here. I've amended the files to apply the bsd license to the K4 search, so if you simply download the trunk again, using your patch technique to get rid of nauty, you should be good to go."

So the above patch should be rebased on the current SVN sources of the planarity code (with the right license statements on those files).



---

archive/issue_comments_079976.json:
```json
{
    "body": "Previously, **every** long test run on planarity.pyx failed on my Ubuntu 9.04 x86/Prescott (gcc 4.3.3) (see http://groups.google.com/group/sage-release/msg/560824983a71627f).\n\nAfter applying the three patches on top of 4.4.2.rc0 (no rejects), all seems fine: \nRunning 100 times\n\n```\n./sage -t -long devel/sage/sage/graphs/planarity.pyx\n```\n\nno errors occurred. (Also `devel/sage/sage/graphs` passed.)\n\nJust for the record, the (second) patch contains two Eclipse project files (and some text files for comparing the output of tests I guess).\n\n-Leif",
    "created_at": "2010-05-15T23:03:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79976",
    "user": "https://github.com/nexttime"
}
```

Previously, **every** long test run on planarity.pyx failed on my Ubuntu 9.04 x86/Prescott (gcc 4.3.3) (see http://groups.google.com/group/sage-release/msg/560824983a71627f).

After applying the three patches on top of 4.4.2.rc0 (no rejects), all seems fine: 
Running 100 times

```
./sage -t -long devel/sage/sage/graphs/planarity.pyx
```

no errors occurred. (Also `devel/sage/sage/graphs` passed.)

Just for the record, the (second) patch contains two Eclipse project files (and some text files for comparing the output of tests I guess).

-Leif



---

archive/issue_comments_079977.json:
```json
{
    "body": "John Boyer also said this to me about the new planarity code:\n\n\n\"I had to change NONPLANAR to NONEMBEDDABLE due to outerplanarity, but otherwise there's really only additions to the interface, so you're in pretty good shape once you can compile.  The only other question I would have is whether you have any code that traversed adjacency lists, or do you just call my functions.  I found I got more speed when I changed from a circular list that included the vertex. There is a macro you can define to put the CIRCULAR back in the lists, but the code is faster if you don't use it.  Moreover, if you traverse adjacency lists using my actual functions, you were good anyway.\n\n\"You should also note that my library sets a default graph size capable of accommodating 3N edges (6N arcs, or half edges), but it is easy in the new version to override that by calling gp_EnsureArcCapacity().  Of course, the 3N setting is there because you only need 3N of the edges in any graph to ensure that it comes to the right conclusion for any of the planarity-related algorithms in the current package.  My code that called nauty would increase the arc capacity to ensure the whole graph was processed, but it's your choice whether you want to do that.\n\n\"You should also note that the latest copy of the package contains a new algorithm that is not strictly planarity-related.  It creates a correct coloring of a graph using minimum degree selection.  However, it also implements a special technique that ensures any planar graph will have at most 5 colors.  And linear time in the size of the graph of course. \"\n\nThe third patch above makes the necessary changes in Sage regarding NONPLANAR vs. NONEMBEDDABLE.  The other issues should be checked, though.",
    "created_at": "2010-05-16T03:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79977",
    "user": "https://github.com/jasongrout"
}
```

John Boyer also said this to me about the new planarity code:


"I had to change NONPLANAR to NONEMBEDDABLE due to outerplanarity, but otherwise there's really only additions to the interface, so you're in pretty good shape once you can compile.  The only other question I would have is whether you have any code that traversed adjacency lists, or do you just call my functions.  I found I got more speed when I changed from a circular list that included the vertex. There is a macro you can define to put the CIRCULAR back in the lists, but the code is faster if you don't use it.  Moreover, if you traverse adjacency lists using my actual functions, you were good anyway.

"You should also note that my library sets a default graph size capable of accommodating 3N edges (6N arcs, or half edges), but it is easy in the new version to override that by calling gp_EnsureArcCapacity().  Of course, the 3N setting is there because you only need 3N of the edges in any graph to ensure that it comes to the right conclusion for any of the planarity-related algorithms in the current package.  My code that called nauty would increase the arc capacity to ensure the whole graph was processed, but it's your choice whether you want to do that.

"You should also note that the latest copy of the package contains a new algorithm that is not strictly planarity-related.  It creates a correct coloring of a graph using minimum degree selection.  However, it also implements a special technique that ensures any planar graph will have at most 5 colors.  And linear time in the size of the graph of course. "

The third patch above makes the necessary changes in Sage regarding NONPLANAR vs. NONEMBEDDABLE.  The other issues should be checked, though.



---

archive/issue_comments_079978.json:
```json
{
    "body": "Attachment [trac-8756-planarity-v2.patch](tarball://root/attachments/some-uuid/ticket8756/trac-8756-planarity-v2.patch) by @jasongrout created at 2010-05-16 03:32:01\n\napply on top of previous patches",
    "created_at": "2010-05-16T03:32:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79978",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8756-planarity-v2.patch](tarball://root/attachments/some-uuid/ticket8756/trac-8756-planarity-v2.patch) by @jasongrout created at 2010-05-16 03:32:01

apply on top of previous patches



---

archive/issue_comments_079979.json:
```json
{
    "body": "apply on top of previous patches",
    "created_at": "2010-05-16T03:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79979",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patches



---

archive/issue_comments_079980.json:
```json
{
    "body": "Attachment [trac-8756-planarity-sage-changes.patch](tarball://root/attachments/some-uuid/ticket8756/trac-8756-planarity-sage-changes.patch) by @jasongrout created at 2010-05-16 03:38:12\n\nI've attached patches which have the necessary commit messages.  I also removed the Eclipse and example data files from the code.  The new second patch now also has the updated BSD license in the graphK4* files.\n\nThere is a problem compiling these patches on OSX (the C code has #include <malloc.h>, which is apparently a problem on OSX).",
    "created_at": "2010-05-16T03:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79980",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8756-planarity-sage-changes.patch](tarball://root/attachments/some-uuid/ticket8756/trac-8756-planarity-sage-changes.patch) by @jasongrout created at 2010-05-16 03:38:12

I've attached patches which have the necessary commit messages.  I also removed the Eclipse and example data files from the code.  The new second patch now also has the updated BSD license in the graphK4* files.

There is a problem compiling these patches on OSX (the C code has #include <malloc.h>, which is apparently a problem on OSX).



---

archive/issue_comments_079981.json:
```json
{
    "body": "Replying to [comment:14 jason]:\n> I've attached patches which have the necessary commit messages.  I also removed the Eclipse and example data files from the code.  The new second patch now also has the updated BSD license in the graphK4* files.\n\nI tried ~5 times to get the new ones (I saw the changes in trac) but the browser always \"downloaded\" the old ones... 8/\n\nThe new ones still work with Ubuntu 9.04 x86/Prescott. :)\n\n> There is a problem compiling these patches on OSX (the C code has #include <malloc.h>, which is apparently a problem on OSX).\n\nI don't have apples here (besides a IIe), so somebody else has to test/fix that.\n\n(Enhancements should perhaps be made on another ticket.)\n\n-Leif",
    "created_at": "2010-05-16T04:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79981",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:14 jason]:
> I've attached patches which have the necessary commit messages.  I also removed the Eclipse and example data files from the code.  The new second patch now also has the updated BSD license in the graphK4* files.

I tried ~5 times to get the new ones (I saw the changes in trac) but the browser always "downloaded" the old ones... 8/

The new ones still work with Ubuntu 9.04 x86/Prescott. :)

> There is a problem compiling these patches on OSX (the C code has #include <malloc.h>, which is apparently a problem on OSX).

I don't have apples here (besides a IIe), so somebody else has to test/fix that.

(Enhancements should perhaps be made on another ticket.)

-Leif



---

archive/issue_comments_079982.json:
```json
{
    "body": "The patch just `#define`s `_XOPEN_SOURCE` (if not already defined) and includes `stdlib.h` instead of `malloc.h` in two files.\n\nNote that compiling with `-std=c99` (ISO C99) already implies presence of `stdlib.h` (and `malloc()` being defined *there*).\n\n(Apply only if needed, on top of the other three patches.)",
    "created_at": "2010-05-16T05:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79982",
    "user": "https://github.com/nexttime"
}
```

The patch just `#define`s `_XOPEN_SOURCE` (if not already defined) and includes `stdlib.h` instead of `malloc.h` in two files.

Note that compiling with `-std=c99` (ISO C99) already implies presence of `stdlib.h` (and `malloc()` being defined *there*).

(Apply only if needed, on top of the other three patches.)



---

archive/issue_comments_079983.json:
```json
{
    "body": "Replying to [comment:16 leif]:\n\nP.S.: Shouldn't we report/fix this upstream?",
    "created_at": "2010-05-16T05:43:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79983",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:16 leif]:

P.S.: Shouldn't we report/fix this upstream?



---

archive/issue_comments_079984.json:
```json
{
    "body": "Attachment [trac_8756-replaces_malloc_h_by_stdlib_h.patch](tarball://root/attachments/some-uuid/ticket8756/trac_8756-replaces_malloc_h_by_stdlib_h.patch) by @nexttime created at 2010-05-16 06:19:16\n\nRemoves <malloc.h> inclusion by <stdlib.h>. (2nd version)",
    "created_at": "2010-05-16T06:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79984",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_8756-replaces_malloc_h_by_stdlib_h.patch](tarball://root/attachments/some-uuid/ticket8756/trac_8756-replaces_malloc_h_by_stdlib_h.patch) by @nexttime created at 2010-05-16 06:19:16

Removes <malloc.h> inclusion by <stdlib.h>. (2nd version)



---

archive/issue_comments_079985.json:
```json
{
    "body": "My comments above apply to the patch I've just uploaded/freshened (too).",
    "created_at": "2010-05-16T06:22:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79985",
    "user": "https://github.com/nexttime"
}
```

My comments above apply to the patch I've just uploaded/freshened (too).



---

archive/issue_comments_079986.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-27T23:32:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79986",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079987.json:
```json
{
    "body": "This newest patch allows the code to compile on OS X, as I have verified.",
    "created_at": "2010-05-27T23:32:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79987",
    "user": "https://github.com/rlmill"
}
```

This newest patch allows the code to compile on OS X, as I have verified.



---

archive/issue_comments_079988.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-27T23:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79988",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079989.json:
```json
{
    "body": "Looks good to me. Compiles on OS X, doesn't segfault on ubuntu32...",
    "created_at": "2010-05-27T23:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79989",
    "user": "https://github.com/rlmill"
}
```

Looks good to me. Compiles on OS X, doesn't segfault on ubuntu32...



---

archive/issue_comments_079990.json:
```json
{
    "body": "Funny, I just realized that *this* doctest failure seemed to have vanished in 4.4.3.alpha0 (again on Ubuntu 9.04 x86/32-bit, ptestlong), because there's now *another* test failing, but in `sage/graphs/generic_graph.py`.\n\nTesting only the single file `sage/graphs/planarity.pyx` on vanilla 4.4.3.alpha0, it reproducably shows up again.\n\nI'll apply this patch to 4.4.3.alpha0 later...",
    "created_at": "2010-05-28T02:47:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79990",
    "user": "https://github.com/nexttime"
}
```

Funny, I just realized that *this* doctest failure seemed to have vanished in 4.4.3.alpha0 (again on Ubuntu 9.04 x86/32-bit, ptestlong), because there's now *another* test failing, but in `sage/graphs/generic_graph.py`.

Testing only the single file `sage/graphs/planarity.pyx` on vanilla 4.4.3.alpha0, it reproducably shows up again.

I'll apply this patch to 4.4.3.alpha0 later...



---

archive/issue_comments_079991.json:
```json
{
    "body": "Replying to [comment:21 leif]:\n> I'll apply this patch to 4.4.3.alpha0 later...\n\nptestlong: No doctest failures related to this patch (Ubuntu 9.04 x86/32-bit).",
    "created_at": "2010-05-31T19:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79991",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:21 leif]:
> I'll apply this patch to 4.4.3.alpha0 later...

ptestlong: No doctest failures related to this patch (Ubuntu 9.04 x86/32-bit).



---

archive/issue_events_008924.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2010-06-03T04:05:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8756#event-8924"
}
```



---

archive/issue_comments_079992.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-03T04:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79992",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_079993.json:
```json
{
    "body": "Merged into sage-4.4.3.alpha2",
    "created_at": "2010-06-03T04:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8756#issuecomment-79993",
    "user": "https://github.com/williamstein"
}
```

Merged into sage-4.4.3.alpha2
