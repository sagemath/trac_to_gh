# Issue 6828: [with patch, needs review] Random Bipartite Graph

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-08-26 13:36:17

Assignee: rlm

I needed to create one of those, and thought it may be useful in sage... Several lines for a new Graph generator ;-)

I used the position dictionary from CompleteBipartiteGraph, so we should be out of trouble on this point ;-)


---

Attachment


---

Comment by rbeezer created at 2009-09-22 06:21:16

Hi Nathann,

Several of my comments at #6823 apply here - just a diff file rather than a Mercurial file, use "trac_xxxx" for the filename, and the inputs should be checked for errors.  In this case the probability should be checked and n1 and n2 should be checked that they are positive - making one negative does decrease the total.

It would seem that the final call to the `BipartiteGraph` generator can cause problems.  Try 15 to 20 vertices in each part with a very low edge-probability like 0.01, then despite having a good pos_dict, the isolated vertices of one part move into a different "half" of the plot.

Can you make the name look better than `Random bipartite graph: graph on 30 vertices`?  Maybe this is a consequence of final call as well.  Maybe the probability could be included in the name?

I think the construction `range(n1+n2)[n1:]` can be accomplished more clearly with `range(n1,n1+n2)`.

Rob


---

Comment by ncohen created at 2009-09-26 15:26:20

Looks like I went into a lot of trouble for nothing ;-)

I did not even need to create the positions myself !

Thanks for your remarks, I am slowly learning Python through reviews :-)

Nathann


---

Comment by rbeezer created at 2009-09-27 06:25:09

Hi Nathann,

I like the new names for the vertices, and it looks much better for graphs with low edge probability the way you are doing it now.  Some more comments:

1.  Checking for errors usually involves raising an error, rather than using an assert.  Poke around in the code and I think you will see more often a style like:


```
if not((p>=0 and p<=1):
  raise ValueError, "Parameter p is a probability, and so should be a real value between 0 and 1"
```


I'd place them after the imports, but that's just me.

2.  You need to paste in the output of your test.  Right now it is failing.  You really should make sure all your tests pass before someone stops in to do a review.

3.  You should also test the two checks on the input - in a section called `TESTS`

4.  Your EXAMPLE section needs to have two semicolons to create the verbatim section, so at least you need a `::` on a line by itself prior to each test.  (Maybe two semicolons right after EXAMPLE will work as well - I'm having trouble checking this right now with my setup.)  This ensures you get the right formatting in the reference manual.  Again, take a look at what is done elsewhere in the source and compare with the output, then make sure your output also works properly before seeking a review.

I think most of the above applies to #6823, which I haven't commented on.  Adding the Odd graphs there is great, though.

Rob


---

Comment by ncohen created at 2009-09-29 09:51:13

This one should be Ok, sorry for the trouble... ;-)

By the way, I built the documentation and was able to see a TESTS:: section.. I thought this part would be hided in the documentation as it is meant to be read by users and "tests" is something like an "internal tool".

I thought I'd put the "raise" after the "import", because in case the inputs are wrong there is no need to import libraries.. ^^;

Nathann


---

Attachment


---

Comment by rbeezer created at 2009-09-30 05:25:11

Nathann,

Looks real good.  Yes, you would think the TESTS section would not migrate to the reference manual, but right now I think it is really treated no differently.  But I guess in some cases what it contains is useful to read.  Maybe.

All three new graph generators are welcome additions - thanks for adding them.  And thanks for your patience with all the suggestions.

Builds on 4.1.2.alpha2, passes all long tests.  Positive review.

Rob


---

Comment by rbeezer created at 2009-09-30 05:25:11

Changing keywords from "" to "bipartite graph generator".


---

Comment by mhansen created at 2009-10-15 10:11:12

Resolution: fixed
