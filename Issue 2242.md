# Issue 2242: optional nauty package

Issue created by migration from https://trac.sagemath.org/ticket/2242

Original creator: jason

Original creation time: 2008-02-21 00:41:09

Assignee: rlm

It's available here:

http://sage.math.washington.edu/home/jason/nauty-24b7.spkg

It is the 2.4 beta 7 version, since Brendan says that it is pretty stable.  It would be trivial to make a nauty 2.2 stable version if people wanted it.

This is the spkg for #1306.  Now we just need to make the interface in Sage.


---

Comment by jason created at 2008-02-21 00:41:42

I mean, it is the spkg for #1301 (not #1306).


---

Comment by jason created at 2008-02-21 00:58:15

To use this right now, for example, to generate the graphs of order 3, do:


```
sage: a=os.popen("nauty-geng 3").read().split()
>A nauty-geng -d0D2 n=3 e=0-3
>Z 4 graphs generated in 0.00 sec
sage: a
['B?', 'BO', 'BW', 'Bw']
sage: graph_list = [Graph(i) for i in a]
sage: graph_list

[Graph on 3 vertices,
 Graph on 3 vertices,
 Graph on 3 vertices,
 Graph on 3 vertices]
```



---

Comment by jason created at 2008-02-21 01:01:00

Or, for a pretty picture:


```
sage: graph_list = [Graph(g) for g in os.popen("nauty-geng -l 4").read().split()]
>A nauty-geng -ld0D3 n=4 e=0-6
>Z 11 graphs generated in 0.00 sec
sage: show(graph_list)
sage: # to compare to Robert Miller's NICE algorithm in Sage:
sage: show(graphs(4))
```



---

Comment by jason created at 2008-02-21 01:33:17

I've added a patch which implements the graphs.nauty_geng() command (basically doing what the examples above do).

The patch depends on the is_package_installed function, which won't appear until 2.10.2.


---

Attachment

Is there a better way to call nauty than from the command line? Is there some way to call the functions directly, by compiling nauty as a shared object, dynamic library, or something?


---

Comment by malb created at 2008-02-21 09:57:43

Excuse my ignorance, but isn't Nauty _obsolete_ since rlm implemented Nice? Why is there the need for Nauty? You guys probably have a good reason but it would be nice to mention it somewhere :-)


---

Comment by jason created at 2008-02-21 10:11:18

rlm: It is best to call the automorphism group computation or the canonical label computation from the library function.  However, many utility programs (like the planarity checker, etc.) are not readily available as libraries.  The geng program (generates graphs with certain constraints) can be modified to compile as a library.  This was clearly a quick "get it working" solution to generate feedback and get something that was useful.  It sounds like it's succeeding on both accounts.

malb: NICE does implement the main algorithms that are implemented in nauty.  However, nauty is more comprehensive and much more mature.  It is also much faster in some cases that I checked (automorphism groups of cycles and generation of graphs).  Having an optional spkg allows us to use the functionality while NICE continues to improve and also provides a timing and correctness benchmark for NICE.


---

Comment by jason created at 2008-02-21 10:15:08

rlm: is there a way to create a cython library interface for an optional spkg?  I would love to create a cython interface to the library functions, but the cython needs to be compiled and put into the sage system when the nauty package is installed, not when sage is compiled.


---

Comment by mabshoff created at 2008-02-21 12:22:08

Replying to [comment:11 jason]:
> rlm: is there a way to create a cython library interface for an optional spkg?  I would love to create a cython interface to the library functions, but the cython needs to be compiled and put into the sage system when the nauty package is installed, not when sage is compiled.
> 

So far there is now way to do this, at least I am not aware of any way to do this. The ticket to fix this is #2088.

Cheers,

Michael


---

Attachment

I think this should go in now.  I've updated the patch against 3.0.alpha2, and only 2242.patch should be applied.  The spkg installs fine on sage.math, and the code passes tests.


---

Comment by mabshoff created at 2008-04-07 21:37:29

I agree that the spkg is alright. Some things like the license confirmation are unavoidable, the internal structure of the spkg is a little odd. But for an optional spkg it ought to be enough.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-07 21:40:41

Resolution: fixed


---

Comment by mabshoff created at 2008-04-07 21:40:41

Merged 2242.patch in Sage 3.0.alpha3. Add nauty-24b7.spkg into the optional spkg repo on sagemath.org and mirrored it out.
