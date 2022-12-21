# Issue 3726: stats/finance -- add support for hidden markov models to sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-25 16:21:26

Assignee: was

The spkg:

  http://sage.math.washington.edu/home/was/patches/ghmm-20080725.spkg

builds ghmm and doesn't depend on anything not in sage (I hope).  It does not
build the official GHMM bindings.  I am replacing those bindings with cleaner
Cython bindings that have better documentation, but initially expose less
functionality.


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment

The attached patches bring the coverage of this code to 100% and cleanly wrap a solid set of functionality.


---

Attachment


---

Attachment

patches 1 - 8 in a clean bundle against 3.0.5


---

Attachment


---

Comment by jkantor created at 2008-08-11 05:59:03

Code quality is of course excellent and of course positive review

but

Actual Bugs 

   1. No checks are made that matrices given are valid stochastic matrices (rows add to 1).  Or more importantly that the probabilities are actually positive.  There is a function to normalize but it isn't called by default. Actually I'm not sure if this is a bug but there should be some documentation about what to expect  if the inputs matrices are not stochastic, does it do reasonable things or is the result numerical junk. 


   2. For continuous hidden markov models baum welch does not accept a set of sequences only a single sequence.


Miscellaneous comments

   1. Doc string locations are sort of hidden. It would be nice if hmm? or hmm.DiscreteHiddenMarkovModel? hit something. 
  

   2. (very minor) sample vs sample_single annoyed me, I would have rather sample had the number of sequences be optional which defaulted to 1. 

   3. Does there need to be a discussion as to whether or not we want to support this in standard or optional since it involves adding another spkg.


---

Comment by was created at 2008-08-11 06:11:00

>   1. No checks are made that matrices given are valid stochastic matrices (rows add to 1). Or more 
> importantly that the probabilities are actually positive. There is a function to normalize but it
>  isn't called by default. Actually I'm not sure if this is a bug but there should be some 
> documentation about what to expect if the inputs matrices are not stochastic, does it do 
> reasonable things or is the result numerical junk. 

I have no idea what it will do :-).  I will find out by looking at the GHMM docs.   I'm not sure what the best behavior would be on invalid input yet. 

>   2. For continuous hidden markov models baum welch does not accept a set of sequences only a single sequence. 

You're right, this is a bug.  It does take multiple sequences but only like this with a weight:

```
sage: z.baum_welch([([1,2,3], 1), ([1,2,8], 2)])
```


It should also work with no weights. 

DiscreteMarkovModels in this patch don't take single sequences (only multiple), but I fixed that in #3773 (I think).

>   1. Doc string locations are sort of hidden. It would be nice if hmm? or hmm.DiscreteHiddenMarkovModel?? hit something. 

Thanks for finding this.  I consider this a serious problem and will fix it. 

   2. (very minor) sample vs sample_single annoyed me, I would have rather sample had the number of sequences be optional which defaulted to 1. 

I'm annoyed by not having it since foo.sample(n) returns something like [This is the Trac macro *1,2,5,3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,2,5,3-macro) so one ends up typing foo.sample(n)[0] a lot, which seems odd.   Wait, this is easy.  Do this:

```
23:08 < wstein-3514> I can just make M.sample(n, None) give a single list,
23:08 < wstein-3514> whereas M.sample(n, k) with k >= 1 give a list of lists.
23:08 < jkantor> right
23:08 < wstein-3514> That is way better.
23:08 < wstein-3514> Thanks.
```


>   3. Does there need to be a discussion as to whether or not we want to support this in standard or > optional since it involves adding another spkg. 

Yes.  This will not go in standard until the spkg is officially voted on in sage-devel.
This will happen in the next day, as soon as I fix all the problems you point out above.


---

Comment by jkantor created at 2008-08-11 06:20:54

1. Regarding invalid input, I would suggest accepting positive inputs and normalizing but printing a message to that affect (that the probabilities didn't sum to 1  and were normalized) and I would raise an exception on negative inputs.


2. The solution to 2 in what I had in mind.


---

Comment by mabshoff created at 2008-08-18 23:43:14

The latest spkg seems to be

  http://sage.math.washington.edu/home/was/patches/ghmm-20080813.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-19 00:12:37

Resolution: fixed


---

Comment by mabshoff created at 2008-08-19 00:12:37

Merged hmm-bundle-3.0.5.hg in Sage 3.1.2.alpha0. This bundle contains 12 changesets, so there are some patches missing in the broken out series. Oh well ...

Cheers,

Michael
