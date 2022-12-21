# Issue 3786: [with patch, needs review] Refactor binary code isom code.

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-08-07 01:13:10

Assignee: rlm

This is *not* a full replacement of `binary_code`, only the half of it that computes automorphism groups and canonical labels. The other half will be refactored later in the summer.


---

Comment by wdj created at 2008-08-07 10:37:58

Is this based on 3.1.alpha0?


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: coding
sage: hg_sage.apply("/home/wdj/sagefiles/trac3786-linear_binary_codes.patch")
cd "/home/wdj/sagefiles/sage-3.1.alpha0/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.alpha0/devel/sage" && hg status
cd "/home/wdj/sagefiles/sage-3.1.alpha0/devel/sage" && hg import   "/home/wdj/sagefiles/trac3786-linear_binary_codes.patch"
applying /home/wdj/sagefiles/trac3786-linear_binary_codes.patch
patching file setup.py
Hunk #1 FAILED at 680
1 out of 1 hunk FAILED -- saving rejects to file setup.py.rej
abort: patch failed to apply
```



---

Comment by rlm created at 2008-08-07 18:15:43

Depends on the patches at #3676.


---

Comment by rlm created at 2008-08-09 22:23:40

Changing type from defect to enhancement.


---

Comment by wdj created at 2008-08-10 13:37:11

I applied the patches at #3676 and then this patch to sage-3.1.alpha0. They applied cleanly and passes sage -testall on a amd64 hardy heron machine.

Though I think this is a very important contribution, there is a lot of code here and I didn't understand most of it. However, I did notice that some of the key functions (for me anyway) had only fairly trivial examples attached to them. For example, automorphism_group. There were *lots* of good examples in run (which automorphism_group seems to require), so I don't think it is necessary to redo the docstrings but people who type "sage: B.automorphism_group?" won't find any interesting examples, though people who type "sage: B.run?" will. However, if the real referee makes suggested changes, I don't think it will hurt to add to the docstring of automorphism_group either (a) something like "See the docstring for run for more examples" or (b) simply copy some of the examples from run (or make some simply modifications) into the docstring of automorphism_group.

As a general question, I'd like to know will this code will make it easier to create a fast matrix_automorphism function?


---

Comment by rlm created at 2008-08-10 17:55:39

Replying to [comment:4 wdj]:
> some of the key functions (for me anyway) had only fairly trivial examples attached to them...
> people who type "sage: B.automorphism_group?" won't find any interesting examples, though people who type "sage: B.run?" will.

This is meant to be a developer-level file, not a user-level file. Much like `binary_code.pyx`, it is supposed to be doing the work behind the scenes, when someone does something like B.permutation_automorphism_group() where B is a normal LinearCode over GF(2). The docstring for B.run() contains a large number of doctests to ensure that the file is working properly, but the idea is that since the objects in this file are never exported, only minimal examples are necessary for each function in order to see the syntax, in order for developers to plug into it.

> As a general question, I'd like to know will this code will make it easier to create a fast matrix_automorphism function? 

The objects and methods of this file bring us about half way from #3676 to having a matrix automorphism group function. They also bring us about half way to linear codes in general, and all of these are on my list, probably for when I get back from SD9, I'm not sure. Expect them soon, however (as well as hypergraphs!).


---

Comment by ncalexan created at 2008-08-11 19:37:47

This all looks good to me.

After discussion with rlmiller, he is going to address some small documentation concerns concurrently with #3676, mostly to use this as the example for his general framework.

I cannot vouch to the correctness of the code but I'm happy with the documentation, code cleanliness, and testing regimen.

Soon to be applied!


---

Comment by ncalexan created at 2008-08-12 02:02:24

After discussion with rlm, I think this looks good.


---

Comment by mabshoff created at 2008-08-12 06:01:05

Resolution: fixed


---

Attachment

Merged in Sage 3.1.alpha2
