# Issue 8420: [work in progress] new feature : class of perfect matching

Issue created by migration from Trac.

Original creator: vferay

Original creation time: 2010-03-02 14:12:00

Assignee: sage-combinat

Keywords: perfect matching

I am working on implementing the enumerated set of perfect matchings of a ground set (with, in particular, an iterator), a class of matching and simple methods.

I wrote code about this for my own research and thought it could be useful for other people.


---

Comment by ncohen created at 2010-03-02 15:02:50

Exceeeeeeeeellent Idea :-)

Nathann


---

Comment by vferay created at 2010-03-05 16:40:37

Changing status from new to needs_review.


---

Comment by hivert created at 2010-03-05 17:04:47

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2010-03-05 17:04:47

Replying to [comment:2 vferay]:
Hi Valentin,

I started to review your patch. Here is a comment:

When you construct a new class of parent or elements, you should add a call to the standard tests suite. Namely, inside each `__init__` method, you should build a representative object say `Obj` of the class and add

```
sage: TestSuite(Obj).run()
```

The result should be nothing. If you get something then the error message is supposed to explain the problem.

Cheers,

Florent


---

Attachment


---

Comment by vferay created at 2010-03-08 09:01:29

Hi Florent,

I added the test you suggested inside the __classcall__ method and it passed.

Cheers,
Valentin


---

Comment by vferay created at 2010-03-08 09:01:29

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-03-08 10:53:45

Hi Valentin,

I've got a some comments about your code ;-). I've already taken care of most of them. For the other I need you. I've uploaded here the patch with all my modifications and put it also in the Sage-Combinat queue. You should formally review this patch, and then either fold it in yours (using in the queue

```
sage -hg qgoto your_patch
sage -hg qfold my_patch
sage -b
```

) add your new modification or add the new modification in a new patch after mine. Please ask me if you have some trouble with that.

## Problems already taken care of

Please review the patch to see if you agree with all those.

 - (done) You should put a title to the file and insert it in the doc `doc/en/reference/combinat/index.rst`
 - (done) You should put the imports at the beginning of the file, unless you have a good reason not to do so (eg:loop in import).
 - (done) You should avoid too lines in comment, code and documentation. Please break them at 80 columns.
 - (done) Every single function must be tested.
 - (done, must be reread) ``...`` is for math, ```...``` is for code.
 - (done) You can add cross references to other method with `:meth:`name_of_the_method``
 - (done) I don't like the way your wrote three time (or probably copy-paste) the code for computing crossing/number_of_crossing/is_non_crossing. A good way it to write an iterator. An even better way is to write yet a new `EnumeratedSet` for the crossing.

## Work still to be done

 - Just after the title, you should define mathematically in one or two lines what is a perfect matching and add some references
 - You should also then add yourself as the author of the file (please see the [coding conventions](http://www.sagemath.org/doc/developer/conventions.html) and in particular the [heading section](http://www.sagemath.org/doc/developer/conventions.html#headings-of-sage-library-code-files) of the developper guide). 

 - in method `loop_type`, It would probably be useful to expose a method called `loops` since you compute it inside. I can imagine it could be of use for some problems. Then of course you should use it in `loop_type`.

 - I don't like the following behavior. Is there any good reason for it:

```
 The class constructor does not check that the perfect matching is correct,
 one has to use the method :meth:`__contains__` for that::

            sage: m=PerfectMatching([(1,2,3),(4,5)])
            sage: isinstance(m,PerfectMatching)
            True
            sage: m in m.parent()
            False
```


 - Could you add some reference about perfect-matching and Weingarten_matrix

 - Could you finally add some more tests and in particular corner cases (empty or odd size sets).

## Final Comments

Sorry for this frightening review. Despite of the bunch of remarks, the code is good ! I'd just rather it to match perfectly with sage standard ;-)

Florent


---

Comment by hivert created at 2010-03-08 10:53:45

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2010-03-08 10:59:36

Review patch.


---

Attachment

2nd version, after Florent's comments


---

Comment by vferay created at 2010-03-10 10:51:39

Hi Florent,

   thanks a lot for this deep review of my patch and don't apologize for the quantity of remarks, it's a very good thing for me to learn. Moreover, you had done already a big part of the needed corrections, so thanks for that also. I have done the remaining corrections and I think the patch is ready for a new review.

Best,
Valentin

More specific comments:

- concerning the imports (on the beginning of the file or of the function), Nicolas (Thiery) told me to try to put the high-level imports (so, in my case, I think it would be Partition, Permutation, Matrix) at the beginning of the functions to prevent apparition of loops...

- I did the change you requested:
* I created a loops_iterator and a function which gives the list of the loops.
* The correctness of the data given to create a perfect matching is checked when the syntax PerfectMatching(...) is used.

- I also added some new methods:
* nestings_iterator and related function: the code is very similar to the one of crossings_iterator and I saw in literature that this notion appears often.
* coset-type for permutations, which was one of the thing I was interested in.


---

Comment by vferay created at 2010-03-10 10:51:39

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-03-15 15:36:48

Replying to [comment:7 vferay]:

> * coset-type for permutations, which was one of the thing I was interested in.

I don't like the name coset-type ! It applies to too many different things (eg: coset by young subgroups...)

What about: `hyperoctahedral_double_coset_type` ?


---

Comment by hivert created at 2010-03-15 16:07:18

Hi Valentin !

I just uploaded a review patch. It purpose is:
 - fix some doc issues (references, indentation, ...).
 - remove the methods `__init__` in `PerfectMatching` since it was properly inherited;
 - add a few doctests;
 - change the name of `coset_type` to `hyperoctahedral_double_coset_type`. 
 
I need you (or anyone else) to review this patch and tell me if the change of name suits to you. If it does and if my patch is correct, you can set positive review to this ticket. Your patch is fine for me.

Some tip for the doc:
 - inside single back quote ``...`` you put things in LaTeX format. so beware of "{" and "}" vanishing...

 - in a bullet list you should indent the lines after the bullet:
   {{{
 - plenty of text; plenty of text; plenty of text; 
   plenty of text; plenty of text;
   plenty of text;
 - More text
   }}}
   and not
   {{{
 - plenty of text; plenty of text; plenty of text;
 plenty of text; plenty of text;
 plenty of text;
 - More text
   }}}


---

Attachment


---

Comment by vferay created at 2010-03-16 17:34:59

Hi Florent!

Thanks for this new review. The patch seems ready, except for two small things:

- line 144 of the file perfect_matching.py, it is written in the doc
 `PerfectMatchings(objects)(data)`. 
Should it not be
 ``PerfectMatchings(objects)(data)``.
as this is sage code?

- second: the function now called
hyperoctahedral_double_coset_type
(which name is fine like this by the way)
does not return a PerfectMatching as you suggest in the doc,
but a partition.

As I am learning, I would like to know what is the best way to deal with very small changes like that:
- to do a new review patch as in the case of big changes?
- to let you do these changes and switch to positive review?
- to do the changes myself and switch to positive review? (but I believe this is not a good idea as I am not supposed to write in your patch)

Another thing that I did not know how to do was the following:
I remember that you said something about compiling the documentation to check that it is well written. How does it work?

Yours,
Valentin


---

Comment by hivert created at 2010-03-18 23:19:59

Hi Valentin,

First of all, please have a look at http://trac.sagemath.org/sage_trac/wiki/WikiFormatting
so that your message appear nicely in trac (sorry yet another stupid syntax to learn)...

> Thanks for this new review. The patch seems ready, except for two small things:
> 
> - line 144 of the file perfect_matching.py, it is written in the doc
``PerfectMatchings(objects)(data)`.` 
> Should it not be
```PerfectMatchings(objects)(data)```
> as this is sage code?

You are perfectly right ! Thanks for spotting this little mistake. 

> - second: the function now called
> hyperoctahedral_double_coset_type
> (which name is fine like this by the way)
> does not return a PerfectMatching as you suggest in the doc,
> but a partition.

Again right... 

> As I am learning, I would like to know what is the best way to deal with very small changes like that:
> - to do a new review patch as in the case of big changes?

Usually when you spot those kind a little mistakes, it takes as long as explaining them in trac than fixing them directly in the file. So the fastest and time saving way (for the sage community in general, maybe not for you) is to write yet another tiny review patch and put in on trac. If the change is bigger or more involved, you can ask the author to do it. That's when you check the need work button. 

In the present case, since I understood it wrong, can you give a little explanation of this coset stuff and correct it as a being a partition. If it's too complicated explaining it, keeping only the ref to Macdonald (as it is now) can be sufficient. Also, since I spend times explaining this to you, It's your turn to make the change (sorry that I found a reason for being lazy ;-). 

Then the usual way is to submit yet another review of review patch and ask for a review of the review of the review patch ;-) Looks like a joke but this is not. 

> - to let you do these changes and switch to positive review?

It's forbidden by rule 2 below. If I change my patch, you have to review it again.  

> - to do the changes myself and switch to positive review? (but I believe this is not a good idea as I am not supposed to write in your patch)

Again forbidden by both rule 1 and 2 below. 

Two strict rules:
 1 - in the path queue of sage-combinat, it's forbidden to write on someone's else patch, except if explicitely authorized (unless you're fond of editing second derivative of a file)... In some very rare occasion, we broke this rule with Nicolas but you really have to know what you are doing... A much better way is to write a new patch and either to submit it to trac or to ask the owner to fold it.
 
 2 - No code (or doc or anything) can go into Sage, unless it has been reviewed by someone different from its author. Even a trivial typo correction. As far as I know since a few year, this rule has never been broken.
  
Also it's easier for the different review to keep the consecutive changes in different patches. An the end, for the release manager, you have to indicate which patch has to be applied in which order. If you want to be kind with him. after deciding to put the positive review, you can fold the whole bunch of patch in a single one (useful when the review has been particularily messy). 


> Another thing that I did not know how to do was the following:
> I remember that you said something about compiling the documentation to check that it is well written. How does it work?

I must suggest you to read the [Developer's Guide](http://www.sagemath.org/doc/developer/index.html) in particular the section reviewing a patch (the command about applying the patch don't strictly apply to our case since we are using the queue).
The answer of you question is found in point 4:

```
./sage -docbuild reference html
```

could take some time. 

Cheers,

Florent


---

Comment by vferay created at 2010-03-19 17:35:36

Hi Florent,


> Also, since I spend times explaining this to you, It's your turn to make the change
A new review patch is in the queue right after your review patch.

*Thanks* for taking the time to explain me all these staffs. I should have read more the documentation, but I am a little lost in this jungle (and also a little lazy perhaps).

Best,

Valentin


---

Comment by hivert created at 2010-03-21 22:07:33

Changing status from needs_review to needs_work.


---

Comment by hivert created at 2010-03-21 22:07:33

Hi Valentin,

> *Thanks* for taking the time to explain me all these staffs. I should have read more the documentation, but I am a little lost in this jungle (and also a little lazy perhaps).

:-)

There is a little mistake which was pointed out by Samuele in #8548. Can you fold his patch in yours, add a test for the error and reupload ?


---

Comment by vferay created at 2010-03-22 09:58:11

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by hivert created at 2010-03-22 14:26:31

Everything seems ok. Positive review.

Florent

PS: for the release manager:
I applied the following patches in the this order:

 - [trac_8420_features_perfect_matchings_vf.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8420/trac_8420_features_perfect_matchings_vf.2.patch) 
 - [trac_8420_perfect_matchings_review-fh.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8420/trac_8420_perfect_matchings_review-fh.patch)
 - [trac_8420_features_perfect_matchings_review_review_vf.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8420/trac_8420_features_perfect_matchings_review_review_vf.patch)


---

Comment by hivert created at 2010-03-22 14:26:31

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 23:49:50

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 23:49:50

Merged into 4.4.alpha0:
 - trac_8420_features_perfect_matchings_vf.2.patch
 - trac_8420_perfect_matchings_review-fh.patch
 - trac_8420_features_perfect_matchings_review_review_vf.patch


---

Comment by chapoton created at 2017-07-19 08:25:40

name with accent
