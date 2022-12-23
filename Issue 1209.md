# Issue 1209: make it so maple.gcd?? shows source code

Issue created by migration from https://trac.sagemath.org/ticket/1209

Original creator: was

Original creation time: 2007-11-19 16:58:02

Assignee: was


```
On Nov 19, 2007 8:29 AM, Jason Grout <jason-sage@creativetrax.com> wrote:
> 
> William Stein wrote:
> 
> >  3. Dumb question -- Where is the actual source code of anything in Maple?
> >      I'm skimming through my Maple install to see some actual source code and
> >      I can't find anything.  The lib/ directory has lots of .mla
> > files, but these are all
> >      pre-compiled binary files -- no source code.  Is there some tool
> > included with
> >      Maple to decompile them?     (I'm not being rhetorical, I simply don't know
> >      how to actually view source code of Maple functions, even if I wanted to.)
> 
> Some links dealing with this:
> 
> http://www.mapleprimes.com/blog/jacquesc/old-timer-techniques
> 
> http://www.mapleprimes.com/forum/algorithms-used-in-maple
> 
> http://thproxy.jinr.ru/Documents/MapleV/qa/section3_4.html
> 
> I've used the printlevel and I think the showstat techniques before.
> Unfortunately, I can't test them because I no longer have access to
> Maple (at least on my home machine).  I guess that's they whole point
> again---even if there is some way for someone to get the output of the
> procedure, it doesn't do me any good because I don't have Maple and
> can't check it anyway.

This *does* work in Maple 11:

sage: maple_console()
    |\^/|     Maple 11 (APPLE UNIVERSAL OSX)
._|\|   |/|_. Copyright (c) Maplesoft, a division of Waterloo Maple Inc. 2007
 \  MAPLE  /  All rights reserved. Maple is a trademark of
 <____ ____>  Waterloo Maple Inc.
      |       Type ? for help.
> print(gcd);
                                  proc(aa, bb, cofa::name, cofb::name)  ...  end proc

> interface(verboseproc=2);
                                                           1

> print(gcd);              
proc(aa, bb, cofa::name, cofb::name)
local Z, GCD, a, b;
option `Copyright (c) 1992 by the University of Waterloo. All rights reserved.`;
    if 2 < nargs and member(cofa, indets(aa) union indets(bb)) then error "The optional 3rd argument given to `\
...

I wonder what proportion of the 1300 or so top-level functions in Maple (according
to a sage's maple.[tab]) actually have source code.    

Interestingly, I bet I can make it so 

  sage: maple.gcd??

will show the source code using one you suggest above.  Trac ticket:
   

> Whether or not using printlevel or showstat is legal (in light of Josh's
> response from Maple) is an interesting question.  They are built-in
> capabilities meant for introspection.  They were also encouraged by the
> Maple people in the above posts.

<tinfoil hat> Maybe it is a trap.  :-)  </tinfoil hat>

 - William
```



---

Comment by was created at 2007-11-19 16:58:09

Changing type from defect to enhancement.


---

Comment by mhansen created at 2008-01-27 07:18:16

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-01-27 07:18:16

Changing status from new to assigned.


---

Comment by mhansen created at 2008-01-27 07:37:59

New patch added.


---

Comment by ncalexan created at 2008-01-27 07:40:03

I say apply, even though this patch spawns a new maple for each query.  mhansen couldn't get 'maple.gcd?' to work without doing that, so it can be a new ticket.


---

Comment by mabshoff created at 2008-01-27 07:47:47

Resolution: fixed


---

Comment by mabshoff created at 2008-01-27 07:47:47

Merged in Sage 2.10.1.rc1


---

Comment by was created at 2008-01-27 13:06:51

Referee report:

  * All doctests pass.  Excellent. 

  * Line 455: "trys" --> "tries"

  * It would be good if you also added something to the programming guide that explains the new `_sage_src_` "protocol" that you just invented in the course of making this patch.


---

Comment by was created at 2008-01-27 13:06:51

Changing status from closed to reopened.


---

Comment by was created at 2008-01-27 13:06:51

Resolution changed from fixed to 


---

Attachment


---

Comment by mhansen created at 2008-02-27 19:52:45

New patch that fixes the typo is posted.  I made the programming guide suggestion #2335 .


---

Comment by mabshoff created at 2008-02-28 00:27:40

I get some reject against my 2.10.3.rc0:

```
sage$ patch -p1 --dry-run < trac_1209.patch
patching file sage/interfaces/maple.py
Hunk #1 succeeded at 485 with fuzz 2 (offset 35 lines).
Hunk #2 FAILED at 584.
1 out of 2 hunks FAILED -- saving rejects to file sage/interfaces/maple.py.rej
patching file sage/misc/sagedoc.py
Reversed (or previously applied) patch detected!  Assume -R? [n] n
Apply anyway? [n] n
Skipping patch.
1 out of 1 hunk ignored -- saving rejects to file sage/misc/sagedoc.py.rej
```

Am I missing a dependency or do I just need a rebase here?

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-02-28 00:37:36

New patch posted which should apply cleanly.


---

Comment by mabshoff created at 2008-02-28 00:55:22

Closer, but still not across the finish line:

```
sage$ patch -p1 --dry-run < trac_1209.2.patch
patching file sage/interfaces/maple.py
Hunk #1 succeeded at 485 with fuzz 2 (offset 35 lines).
Hunk #2 FAILED at 584.
1 out of 2 hunks FAILED -- saving rejects to file sage/interfaces/maple.py.rej
```


Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-02-28 01:16:06

This last one should do it.


---

Comment by mabshoff created at 2008-02-28 01:19:27

Merged 1209.3.patch in Sage 2.10.3.rc0


---

Comment by mabshoff created at 2008-02-28 01:19:27

Resolution: fixed
