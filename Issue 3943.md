# Issue 3943: pydesign patch [not ready for review]

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-08-24 12:27:42

Assignee: wdj

CC:  sage-combinat

pydesign is a very basic GPL2+ package for block designs (http://www.designtheory.org/software/pydesign/). This patch adds a little functionality and a few examples. Needs *lots* more work!

In creates a new subdirectory of sage/combinat and adds several files to that subdirectory. See block_design.py for some examples.


---

Comment by wdj created at 2008-09-01 02:36:03

Second patch applied. Still not ready for review. Now has block designs, insidence matrix and graph, automorphism group and block designs from finite projective geometries.


---

Comment by wdj created at 2008-09-05 12:25:07

Added affine geometry designs, Witt designs and significant "polishing".


---

Comment by rlm created at 2008-09-10 12:34:56

I am unsure what pydesign has that we don't. For example, the main thing they seem to implement is isomorphism of block designs, which is already part of the `partn_ref` module (nonlinear binary codes, in `refinement_binary`), and if pydesign is truly a Python implementation, then I think it's a safe bet that the Cython implementations are faster. The other things, such as translation from one format to another, should probably be ported to a Sage-native implementation.


---

Comment by wdj created at 2008-09-10 12:48:10

Thank you for the comments. Questions:

(1) How is a block design a nonlinear binary code? Via its incidence matrix? If yes, then users who wish to "play" with block designs using Sage will want commands which are fairly intuitive. So pydesign creates a BaseBlockDesign class and methods for that class.

(2) Re "the main thing they seem to implement is isomorphism of block designs, which is already part of the partn_ref module (nonlinear binary codes, in refinement_binary),...": First, "we" is me in this case. (Peter D wrote the base class, which I butchered/hacked up/modified, and most of the XML stuff; I did the rest - GAP wrappers, etc. See http://designtheory.org/software/pydesign/ for his version.). Second, the automorphism of a block design is computed using NICE, so that function *does* call Cython. 
Should I rewrite it to the new matrix automorphism function?

(3) I'm happy to scrap the XML stuff for now and maybe add it back in later. I don't really understand how they use that interface anyway. The files bd* in the pydesign subdirectory could also possibly be eliminated and the statistics format could be deleted. Suggestions/comments appreciated!


---

Comment by rlm created at 2008-09-10 13:10:07

> (1) How is a block design a nonlinear binary code? Via its incidence matrix?

Correct.

> If yes, then users who wish to "play" with block designs using Sage will want commands which are fairly intuitive.

I agree. Optimally, a `BlockDesign` class would extend a more general `IncidenceStructure` class, and much of the functionality would go in there. Incidentally, "incidence structure" is yet another word for hypergraph/nonlinear binary code... Without polish, the pydesign classes don't hold up to the current standards for inclusion into Sage, and the `BaseBlockDesign` class itself doesn't seem to provide much functionality. It seems much smarter to implement these things "the Sage way," porting the needed functions from pydesign.

> ... the automorphism of a block design is computed using NICE, so that function *does* call Cython. 
> Should I rewrite it to the new matrix automorphism function?

You should probably be using the nonlinear binary code routines for this (you should only use the matrix automorphism routines for matrices which have more than 0 and 1 as entries), as they would probably be the fastest. Certainly faster than NICE, since these routines know not to include the blocks in the partitions which determine the search tree (I can explain a little more if you want...).

> (3) I'm happy to scrap the XML stuff for now and maybe add it back in later. I don't really understand how they use that interface anyway.

In my opinion, the way block designs are stored (in XML) is about the least efficient way possible. For example, the Fano plane looks like this (snipped from one of the patches):

```
 BD.xml(name="Fano plane") 
 	219	            <?xml version="1.0"?> 
 	220	            <block design 
 	221	             b="7" 
 	222	             id="Fano plane" 
 	223	             v="7"> 
 	224	             <blocks ordered="true"> 
 	225	              <block> 
 	226	               <z>0</z> 
 	227	               <z>1</z> 
 	228	               <z>2</z> 
 	229	              </block> 
 	230	              <block> 
 	231	               <z>0</z> 
 	232	               <z>3</z> 
 	233	               <z>4</z> 
 	234	              </block> 
 	235	              <block> 
 	236	               <z>0</z> 
 	237	               <z>5</z> 
 	238	               <z>6</z> 
 	239	              </block> 
 	240	              <block> 
 	241	               <z>1</z> 
 	242	               <z>3</z> 
 	243	               <z>5</z> 
 	244	              </block> 
 	245	              <block> 
 	246	               <z>1</z> 
 	247	               <z>4</z> 
 	248	               <z>6</z> 
 	249	              </block> 
 	250	              <block> 
 	251	               <z>2</z> 
 	252	               <z>3</z> 
 	253	               <z>6</z> 
 	254	              </block> 
 	255	              <block> 
 	256	               <z>2</z> 
 	257	               <z>4</z> 
 	258	               <z>5</z> 
 	259	              </block> 
 	260	             </blocks> 
 	261	            </block design> 
```


Once people start using large block designs, this would be completely ridiculous. That's three whole lines for one block on seven points-- this should fit into at most one byte!


---

Comment by wdj created at 2008-09-21 02:35:10

I've made some revisions following (offlist) suggestions of Robert Miller. This patch 10575 is rebased on 3.1.3.alpha0 and does not use the other patches. 

It passes sage -t .../block_design.py. However, for me it fails sage -testall (it triggers a mysterious-to-me SEGFAULT in some of the calculus files).


---

Comment by mabshoff created at 2008-09-21 05:31:51

I just want to raise the initial point rlm made: Why should we merge this? The XML seems like a bad, bad idea and whatever functionality is missing can (according to rlm) be easily added via our own code. 

Since this requires an spkg I see little possibility for this make to make it past the inclusion procedure. We had the first rejection in form of gp2c and I feel the same that we should stop including "random" and likely half baked code.

Cheers,

Michae


---

Comment by wdj created at 2008-09-21 12:06:40

> Since this requires an spkg I see little possibility for 

Huh?? What spkg??

This is (AFAIK) pure Sage/python. I stripped out the majority of the original pydesign code and rewrote it. It does have one (very short) method which outputs the design in xml. Are you suggesting to delete that method? It does not communicate in xml (though I think the original pydesign has that option) since I stripped that part out. I did leave the xml output method (which I partially wrote) in.


---

Comment by mabshoff created at 2008-09-21 17:40:01

Replying to [comment:8 wdj]:
> > Since this requires an spkg I see little possibility for 
> 
> Huh?? What spkg??

Ok, taking a closer look I see that you copy some substantial amount of code from that Python code base. It seems to duplicate a bunch if things already in Sage in one form or another, i.e. 

 * def binomial_new(n, k)
 * def int_div

The version number code is more than ugly and uses IMHO rather non-standard tags, i.e. why the external CVS version?

> This is (AFAIK) pure Sage/python. I stripped out the majority of the original pydesign code and rewrote it. It does have one (very short) method which outputs the design in xml. Are you suggesting to delete that method? It does not communicate in xml (though I think the original pydesign has that option) since I stripped that part out. I did leave the xml output method (which I partially wrote) in.

Then why add the XML method? Is that some kind of standard that is actually used by other code? As rlm originally pointed out: If you turn 7 bits of info into a couple dozen lines of ASCII the efficiency goes right out of the window and it isn't exactly human readable.

This ticket also does not belong to the sage-combinat milestone unless you plan to submit the code via the sage-combinat patch server. 

Cheers,

Michael


---

Comment by wdj created at 2008-09-21 18:27:06

Michael:
Thanks for looking at it. I'll take out binomial_new, int_div, xml, cvs (though I'm not sure what "external cvs" refers to but I'll look into it). The xml is a "standard" format (for databases I guess) but I don't plan to use it and it is easy to add back in if it's requested.


---

Comment by wdj created at 2008-09-23 10:06:27

I think I have implemented everything both Robert M and Michael have suggested. It needs more functionality but this is a basic start and passes sage -testall. To install,
apply 10575 and 10576 to 3.1.3.alpha0.


---

Comment by rlm created at 2008-09-24 01:05:42

Replying to [comment:11 wdj]:
> I think I have implemented everything both Robert M and Michael have suggested. It needs more functionality but this is a basic start and passes sage -testall. To install,
> apply 10575 and 10576 to 3.1.3.alpha0.

There are many added functions without doctests -- my hands are tied, those are the rules. Also, the format 

```
""" 
'designs' package. 
 
Modules: 
 
    block_design 
    ext_rep 
""" 
 
__version__     = '0.7' 
_revision       = '$Id: __init__.py 274 2004-11-18 13:13:10Z peter $' 
_author         = 'Peter Dobcsanyi <peter`@`designtheory.org>, David Joyner <wdjoyner`@`gmail.com>' 
	 
License = ''' 
Copyright (c) 2004, 2008 Peter Dobcsanyi, David Joyner. 
This program is free software; you can redistribute it and/or modify it 
under the terms of the GNU General Public License as published by the 
Free Software Foundation; either version 2 of the License, or (at your 
option) any later version.  This program is distributed in the hope that 
it will be useful, but WITHOUT ANY WARRANTY; without even the implied 
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
GNU General Public License for more details. 
''' 
```

mismatches with almost every other sage module out there.

If you are comparing two lists of ints, `block_cmp` gives exactly the same output as `cmp`, so I'm not sure why it's there. `int_div`, `binomial_new` similarly don't seem necessary. 

`ProjectiveGeometryDesign` is a perfect example, I think, of how not to use the GAP interface in Sage. I think the number of calls to `gap.eval` could certainly be reduced.

`IncidenceStructure` should not be the base class for block designs, since it is in fact much more general than block designs.

Why is `#!/usr/bin/env python` appearing in the Sage library?


---

Comment by wdj created at 2008-09-24 01:16:42

Just to confirm:
Did you apply both 10575 and 10576? If so, I somehow created these incorrectly because int_div, binomial_new are gone and also ProjectiveGeometryDesign was rewritten.

However, regarding IncidenceStructure I guess I'm not sure what to do. I thought one wanted more general objects for the base class. For example, the base class for PermutationGroup_generic is group.FiniteGroup.


---

Comment by rlm created at 2008-09-24 01:28:16

David,

Normally, patches on trac follow the format `trac_XXXX-description-of-patch.patch`. You should start using this syntax. Also, sorry about the comments above, I was just skimming the first patch.

What you should do is flatten the two patches into a new one with the syntax above (if you want, I can delete the rest to clean up the ticket). Sorry I wasn't more careful in reviewing, but I've been very busy lately and I might not have the full attention span necessary for this right now (general exam coming up very soon!).

Cheers,
Robert


---

Comment by AlexGhitza created at 2008-09-24 01:41:07

Actually, can I suggest getting rid of the "trac_" part and just going with "XXXX-description-of-patch.patch"?  Our policy is that all patches go through trac, so it's somewhat redundant.  Also, it's quicker easier to tab-complete if the "trac_" prefix is not there.


---

Comment by rlm created at 2008-09-24 01:42:10

This is not a discussion for this particular ticket, but for sage-devel.


---

Comment by mabshoff created at 2008-09-24 01:43:16

Replying to [comment:16 AlexGhitza]:
> Actually, can I suggest getting rid of the "trac_" part and just going with "XXXX-description-of-patch.patch"?  Our policy is that all patches go through trac, so it's somewhat redundant.  Also, it's quicker easier to tab-complete if the "trac_" prefix is not there.

I use that prefix for all the patches I apply to contrast them with the spkgs I merge, so I am strongly in favor of using the prefix. Either way, encoding the ticket is essential to make things easy.

Cheers,

Michael


---

Comment by wdj created at 2008-09-24 12:29:30

I'll be sure to do all these things. I can do them tomorrow 
but it is no problem with me if it doesn't get reviewed 
until after 3.1.3.final is out this weekend.


---

Attachment

This is based on 3.1.3.alpha1. Apply this patch only - ignore all previous patches.


---

Comment by wdj created at 2008-09-25 19:10:58

I think this patch includes all the suggestions made by everyone. It is based on 3.1.3.alpha1 and passes sage -testall. The rest of the patches (10***.patch) can be deleted. 

Here is the correct description of this patch:
This patch is a minimalistic beginning of an implementation of some basic block design algorithms. A few functions require GAP's Design package (which is included in gap_packages-4.4.10_6.spkg) but calling GAP or GAP's Design was only done when the corresponding Sage functionality was (AFAIK) missing. Robert Miller's recent code on computing the automorphism group of a non-linear binary code was used to implement the automorphism group of a block design.


---

Comment by rlm created at 2008-09-25 20:28:15

David,

Thank you for putting up with such a tedious review process. This new patch is looking good. Here are a few comments I have on the new patch:

- I only recently learned this. When you have a block comment at the top of the file, the first line is used as a subject heading for the reference manual. Whatever that line is, is used for the title of that section in the manual. So, something like `A module to help with constructions and computations of block designs and other incidence structures.` as you have it in block_design.py is better off as something more like `Block Designs`.

- I still think that the class `IncidenceStructure` belongs somewhere else than in `block_design.py`, although I'm not sure where it should go. I had once thought that `sage.graphs` should be something like `sage.incidence_structures`, and from there we would have designs, graphs, hypergraphs, etc. Although, the naming is ugly, and this is probably not the right approach. Any thoughts you have on this are welcome.

- There cannot be any new functions in any patch to be merged without doctests, including auxiliary functions used only internally. In particular, `tdesign_params`, `IncidenceStructure.__init__`, `IncidenceStructure.__repr__`, `IncidenceStructure.blocks`, `IncidenceStructure.blocks_from_gap`, `IncidenceStructure._get_block_sizes`, and `IncidenceStructure.points` all need doctests.

- Is there any particular reason you define `_get_incidence_matrix` and `incidence_matrix`? The latter seems good enough, and there are a couple functions that start with `_get`, and I don't see why.

- You have commented out the check in `BlockDesign` to see whether the input satisfies the definition. I think this is a good idea, and should be put back in. As it is right now, you can create an IncidenceStructure which does not satisfy the definitions, and if you call `is_block_design`, it will blindly return True, i.e. all IncidenceStrucures are taken to be block designs. This is bad. Further, the code in the commented block calls GAP, when in fact the axioms of a block design are easily checked, and should be done in Sage. Also, would there be in the future any functions which are particular to the block design assumption? If so you might consider making `BlockDesign` a separate class which inherits from `IncidenceStructure`.

- Have you run these doctests with `sage -t -optional`? I don't think you have, since for example `gap.eval("IsBinaryBlockDesign("+gD+")")=="true"` will surely fail because of the quotation marks.

- I'd really like to see this patch's dependence on GAP decrease more. One task which would go a very far way in doing this would be to implement #1323, which shouldn't really be all that hard, since it would ultimately just be an exercise in linear algebra.


---

Comment by wdj created at 2008-09-25 23:34:21

Robert:

> I still think that the class IncidenceStructure belongs 
> somewhere else than in block_design.py, although I'm not 
> sure where it should go. I had once thought that 
> sage.graphs should be something like 
> sage.incidence_structures, and from 
> there we would have designs, graphs, hypergraphs, etc. 
> Although, the naming is ugly, and this is probably not the 
> right approach. Any thoughts you have on this are welcome. 

Maybe the class `IncidenceStructure` belongs in its own module, say `incidence_structures.py`? Which directory it goes in might does not matter so much, so why not put both in designs? What do you think?

> I'd really like to see this patch's dependence on 
> GAP decrease more. One task which would go a very 
> far way in doing this would be to implement #1323, 
> which shouldn't really be all that hard, since it 
> would ultimately just be an exercise in linear algebra. 

I just saw your post regarding a `subspaces` method for a
`FreeModule` over a finite field. I'll work on that next.
(I don't think I need the projective case - as you pointed out in your second post it is a trivial consquence of the affine case.)

> ... subject heading ... (more) doctests ...

Will do. Please let me know what you think of the above 
`IncidenceStructure` idea though.


---

Comment by rlm created at 2008-09-25 23:52:41

Replying to [comment:22 wdj]:
> Robert:
> 
> Maybe the class `IncidenceStructure` belongs in its own module, say `incidence_structures.py`? Which directory it goes in might does not matter so much, so why not put both in designs? What do you think?

That definitely works for me. If anyone wants to move it around, they can discuss it later.


---

Comment by mabshoff created at 2008-09-25 23:59:49

Replying to [comment:23 rlm]:
> Replying to [comment:22 wdj]:
> > Robert:
> > 
> > Maybe the class `IncidenceStructure` belongs in its own module, say `incidence_structures.py`? Which directory it goes in might does not matter so much, so why not put both in designs? What do you think?
> 
> That definitely works for me. If anyone wants to move it around, they can discuss it later.
> 

Moving things around breaks the ABI and we would need to deprecate the code in the old location. So let's write an email to [sage-devel] and/or [sage-combinat-devel] and hope that someone smarter than us three here comes up with a good suggestion. If no one cares we just go ahead as planned :p

Cheers,

Michael


---

Comment by wdj created at 2008-09-27 00:07:22

First apply trac_3943-block-designs.patch then apply this patch. Based on 3.1.3.alpha1.


---

Attachment

Now apply this patch after the other 2. Based on 3.1.3.alpha1.


---

Comment by wdj created at 2008-09-27 00:35:24

I think these patches satisfy all the docstring requirements you listed above. They pass sage -t -optional
and sage -t. Sorry for the ridiculous number of patches. I kept forgetting things, eg, hg details. Not the dual of a block design is not necessarily a block design, so I made BlockDesign with a test=False option.


---

Comment by wdj created at 2008-09-27 00:36:15

This is the last patch, I hope. Again, based on 3.1.3.alpha1 and to be applied after the others.


---

Attachment

Appliy this after the others. Based on 3.1.3.alpha1. Arrgghh.


---

Comment by rlm created at 2008-09-27 20:55:16

1. These need to be fixed:

```
SCORE devel/sage/sage/combinat/designs//incidence_structures.py: 94% (16 of 17)

Missing documentation:
	 * incidence_matrix(self):

Possibly wrong (function name doesn't occur in doctests):
	 * block_sizes(self):
```


2. Earlier, I made the comment "If you are comparing two lists of ints, `block_cmp` gives exactly the same output as `cmp`." This hasn't yet been addressed. I think you can just remove the function and replace calls to it with just `cmp` and be fine.

3. Like I said before, `BlockDesign` should be a class which inherits from the Incidence structure class-- not just a function which returns an incidence structure (e.g. Graph and DiGraph inheriting from GenericGraph in graph.py). Does `dual_block_design` make sense as a function of just any incidence structure? If so, maybe it should be called `dual_incidence_structure`. Either way it should not call BlockDesign unless it is guaranteed to be one.

Once these three issues are taken care of I am prepared to give the ticket a positive review.


---

Comment by mabshoff created at 2008-09-27 22:24:38

There is no such thing as an almost positive review :). Please stick to the default tags.

Cheers,

Michael


---

Attachment

based on 3.1.3.alpha1. To be applied after the 5 others before this one.


---

Comment by wdj created at 2008-09-28 01:17:27

> 1. These need to be fixed:
> ...
> Missing documentation:
>	 * incidence_matrix(self):

I don't understand this. It had a docstring and a test.

> 2. Earlier, I made the comment "If you are comparing 
> two lists of ints, block_cmp gives exactly the same 
> output as cmp." This hasn't yet been addressed. 
> I think you can just remove the function and 
> replace calls to it with just cmp and be fine. 

Sorry I forgot. Done now. 

> 3. Like I said before, BlockDesign should be a class 
> which inherits from the Incidence structure 
> class-- not just a function which returns an 
> incidence structure (e.g. Graph and DiGraph? 
> inheriting from GenericGraph? in graph.py). 

To me this makes mathematical sense so I added a 
line 

```
BlockDesign_generic = IncidenceStructure
```

but there are no methods I know of currently
(maybe this will change in the future) which
apply to block designs and not incidence structures.

> Does dual_block_design make sense as a function 
> of just any incidence structure? 

Yes.

> If so, maybe it should be called 
> dual_incidence_structure. Either way it should 
> not call BlockDesign unless it is guaranteed to 
> be one. 

Done. I added an option method="gap" as well.

Please apply the 7 patches in order to 3.1.3.alpha1. They pass sage -t -optional.


---

Attachment

Forgot one change suggested by the referee. Apply this after the others to 3.1.3.alpha1.


---

Comment by wdj created at 2008-09-30 02:58:33

based on 3.1.3.alpha1. To be applied after the others.


---

Attachment

This last patch may or may not improve things. It passes sage -t -optional.

1. I moved __repr__ to __str__ and created a very simple __repr__ method.
2. I moved is_block_design to block_design_checker
3. Created a new an rigorous (and very slow) is_block_design, following an off-list suggestion of the referee.
4. Added some material to some of the docstrings.


---

Comment by rlm created at 2008-09-30 03:45:00

Looks good to me.


---

Comment by rlm created at 2008-09-30 03:45:25

Apply all patches in order.


---

Comment by mabshoff created at 2008-09-30 06:22:36

Replying to [comment:32 rlm]:
> Apply all patches in order.

I am merging this to get this ticket over with, but next time please post a cumulative patch since this is trivial to do. All the changes go into the repo and add up in the end.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-30 07:02:25

Merged all *eight* patches in Sage 3.1.3.alpha2


---

Comment by mabshoff created at 2008-09-30 07:02:25

Resolution: fixed
