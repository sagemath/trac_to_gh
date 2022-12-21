# Issue 2864: Weyl groups are implemented in rootsystem.py

Issue created by migration from Trac.

Original creator: bump

Original creation time: 2008-04-09 16:51:12

Assignee: mhansen

CC:  sage-combinat

The original Weyl group patch was described here:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/80515528dc9648fd?hl=en

No trac ticket was made, and the patch no longer applies without modification so I
revised it and am uploading it as this ticket.

Mike Hansen told me he wants to revise the patch in connection with a reorganization
in which case this ticket might be superfluous. However I added one thing, which is
instructions for obtaining the character tables.


---

Attachment


---

Comment by wdj created at 2008-04-09 18:27:12

I realize this is "not ready for review" but I tested it out anyway. It down not apply to sage-3.0.alpga3 but can be applied "manually" (namely, read the man page for "patch" ...).

I just checked that the above linked-to email does what it claims this patch does:


```
sage: G = WeylGroup(['F',4])
sage: L = G.lattice()
sage: G; L
The Weyl Group of type ['F', 4]
Ambient lattice of the root system of type ['F', 4]
sage: L = RootSystem(['F',4]).ambient_lattice()
sage: G = L.weyl_group()
sage: G; L
The Weyl Group of type ['F', 4]
Ambient lattice of the root system of type ['F', 4]
sage: G.order()
1152
sage: G.simple_reflections()

[[1 0 0 0]
[0 0 1 0]
[0 1 0 0]
[0 0 0 1],
 [1 0 0 0]
[0 1 0 0]
[0 0 0 1]
[0 0 1 0],
 [ 1  0  0  0]
[ 0  1  0  0]
[ 0  0  1  0]
[ 0  0  0 -1],
 [ 1/2  1/2  1/2  1/2]
[ 1/2  1/2 -1/2 -1/2]
[ 1/2 -1/2  1/2 -1/2]
[ 1/2 -1/2 -1/2  1/2]]
sage: g = G.simple_reflections()[0]*G.simple_reflections()[2]
sage: g.order()
2
sage: g.length()
2
sage: L2 = G.lattice()
sage: L == L2
True
sage: fw = L.fundamental_weights(); fw
[(1, 1, 0, 0), (2, 1, 1, 0), (3/2, 1/2, 1/2, 1/2), (1, 0, 0, 0)]
sage: rho = sum(fw); rho
(11/2, 5/2, 3/2, 1/2)
sage: g.action(rho)
(11/2, 3/2, 5/2, -1/2)
```


Very nice so far! I'm posting the rebased patch to
http://sage.math.washington.edu/home/wdj/patches/9467.patch
in case it helps. (I hesitate to attach it to this ticket since I don't know if there are
other plans in mind and don't want to confuse the issue.)


---

Comment by bump created at 2008-04-09 19:15:24

Replying to [comment:2 wdj]:

>I realize this is "not ready for review" but I tested it out anyway. It down not apply to >sage-3.0.alpga3 but can be applied "manually" (namely, read the man page for "patch" ...).

It does apply directly to 3.0.alpha3 since it's a patch against 3.0.alpha3. 

From the combinat directory "patch <weylgroup3.patch" applies cleanly.

I'm unsure why Michael Abshoff described it as not ready for review. One possible reason is that Mike Hanson intends reorganization of root_system.py.


---

Comment by wdj created at 2008-04-09 19:25:26

"From the combinat directory "patch <weylgroup3.patch" applies cleanly."

I would say that is the definition of "applies manually", so i agree with you!
When I say it "does not apply to sage-3.0.alpha3" I mean that 
the following does *not* occur:


```
sage: hg_sage.apply("/home/wdj/wdj/sagefiles/weylgroup3.patch")
cd "/home/wdj/wdj/sagefiles/sage-3.0.alpha3/devel/sage" && hg status
cd "/home/wdj/wdj/sagefiles/sage-3.0.alpha3/devel/sage" && hg status
cd "/home/wdj/wdj/sagefiles/sage-3.0.alpha3/devel/sage" && hg import   "/home/wdj/wdj/sagefiles/weylgroup3.patch"
applying /home/wdj/wdj/sagefiles/weylgroup3.patch
transaction abort!
rollback completed
sage:
```

Did you create your patch using hg_sage.commit, hg_sage.bundle, hg_sage.log, hg_sage.export, as described (well, more-or-less described :-) on http://www.sagemath.org/doc/html/prog/node72.html ? If yes, then maybe my download was corrupted or something.


---

Comment by mabshoff created at 2008-04-09 19:29:32

Replying to [comment:3 bump]:
> 
> I'm unsure why Michael Abshoff described it as not ready for review. One possible reason is that Mike Hanson intends reorganization of root_system.py.

Hi Dan,

this was the precise reason I marked it this way and I assume Mike will take care of this later.

Cheers,

Michael


---

Comment by bump created at 2008-04-09 19:39:08

Replying to [comment:4 wdj]:

The patch was made by running "hg diff". Michael Abshoff told me on IRC not to make patches that way so thanks for the doc link.

But to be clear, the patch didn't need to be rebased since it is a patch against 3.0-alpha3.


---

Comment by mhansen created at 2008-04-10 03:11:37

Changing status from new to assigned.


---

Attachment

I've done some work on the the patch (for example, caching the Weyl group, adding doctests to all the functions, etc.)  I've also put all the root_system code in  combinat/root_system/ which will be necessary as it grows.  This patch is made against 3.0.alpha3.


---

Comment by bump created at 2008-04-10 13:55:34

It's a big patch. I'll look at it today.

Maybe Justin Walker should be added to the copyright in one file since he did a lot of work to code the exceptional root systems.


---

Attachment

Although the patch appears large, it is mostly reorganization. Apart from moving files around, a hash method is added to CartanType_simple and Weyl Groups are cached in improvement over the original patch. 

Two minor problems:

(1) the G2 patch (track #2808) was accidentally reverted.
(2) Some words about how to get the character table were lost.

These are addressed by 2864a.patch which goes on top of 2864.patch.

My recommendation would be to merge 2864.patch + 2864a.patch.

Dan


---

Attachment


---

Attachment

Merged 2864.patch, 2864a.patch and 2864b.patch in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-10 20:31:14

Resolution: fixed
