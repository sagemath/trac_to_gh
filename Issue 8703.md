# Issue 8703: Combinatorial Rooted Ordered and Binary Trees

Issue created by migration from https://trac.sagemath.org/ticket/8703

Original creator: hivert

Original creation time: 2010-04-17 09:36:21

Assignee: hivert

CC:  chapoton sage-combinat vivianepons darij

Patch in preparation in sage-combinat queue

Depends on #8702


---

Comment by hivert created at 2010-06-08 17:07:40

This is an experiment to see if user chapoton is receiving e-mail from trac...


---

Comment by hivert created at 2010-10-24 09:51:06

Updated a new patch after modification in #8702. Close to but not ready for review.


---

Comment by hivert created at 2010-11-01 15:17:53

Added Frédéric as an author to make sure not to forget him. He contributed several functions.


---

Comment by hivert created at 2011-05-31 14:58:24

Changing keywords from "" to "trees".


---

Comment by hivert created at 2011-05-31 14:58:24

Changing type from defect to enhancement.


---

Comment by hivert created at 2011-05-31 14:58:24

Changing status from new to needs_review.


---

Comment by hivert created at 2011-06-02 15:36:42

I just uploaded a new patch wich speedup element creation and remove some unnecessary imports.


---

Comment by chapoton created at 2011-06-11 21:21:18

There seems to be a problem with attributes insert, contains, get, get_min, get_max and contains. Please see the report of the buildbot.


---

Comment by hivert created at 2011-06-13 11:13:10

Replying to [comment:6 chapoton]:
> There seems to be a problem with attributes insert, contains, get, get_min, get_max and contains. Please see the report of the buildbot.

Yes ! There is already something in sage which is called `BinaryTree`. I
just asked for an incompatible change on
[sage-devel](https://groups.google.com/group/sage-devel/browse_thread/thread/1856db31a5cc54f2?hl=fr) and
[sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/1856db31a5cc54f2)


---

Comment by hivert created at 2011-06-13 11:13:10

Changing status from needs_review to needs_info.


---

Comment by hivert created at 2011-06-13 20:44:11

Changing status from needs_info to needs_review.


---

Comment by hivert created at 2011-11-21 16:52:03

Fixed 'labeled' vs 'labelled'


---

Comment by hivert created at 2011-12-03 14:30:32

Addressed Frederic Chaponton's remark (private email) about labelled/unlabelled.


---

Comment by hivert created at 2012-01-21 12:09:12

Fixed doctests.


---

Comment by hivert created at 2012-02-06 14:51:39

Changing keywords from "trees" to "trees, Cernay2012".


---

Comment by ncohen created at 2012-02-07 22:47:51

Hellooooooo Florent !

Here is a patch with some more documentation for the class. We discussed it a lot already, and there were two more things I had stored in a file while beginning the review.

Some notes before we forget :
    * The symmetry_factor should not be there, and only works for RootedTrees (not OrderedDDTrees)
    * What about the name itself ? I know "automorphism_group_size" is a bit long, but it woul be nice to find something more meaningful.
    * And I probably already forgot what I should have written there. Well, we wll find it again `^^;`

Nathann

P.S. : I updated the combinat queue -- how unusual for me !


---

Comment by ncohen created at 2012-02-07 22:47:51

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2012-06-08 18:59:15

Hello,

Nathan, your review patch has 2 problems :

* there lacks the ticket number in the first line of the description

* there is a trailing whitespace, see the bot report for the exact location

Florent, it seems the you are using several non-existing options for DiGraph, unless these options are introduced in another ticket ?


```
DiGraph(loop=False, layout='tree', tree_root=0)
```


I guess it has to be replaced by


```
DiGraph(loops=False)
```



---

Comment by stumpc5 created at 2013-02-13 18:29:24

Hi,

I wonder what the the current situation is here: we would very much appreciate if we could have a version of this patch that we can actually review. Do you think this is feasible during this week, or are there any complicated issues remaining?

Thanks, Christian


---

Comment by hivert created at 2013-02-13 18:45:06

Hi Christian,

No there is nothing complicated. The doc still need to be reread. I did some improvement in the train yesterday so I can upload a new version of the patch which can readily stated to be reviewed. However, I won't get time to rework it before the end of the week. So feel free to do whatever you think is good to improve the doc.

Florent


---

Comment by hivert created at 2013-02-13 18:49:12

Also the LateX output is currently crappy. Jean-Baptiste has a much better tikz output but it needs some cleanup. So I think we should leave this for another ticket.


---

Comment by hivert created at 2013-02-13 18:49:12

Changing status from needs_work to needs_review.


---

Comment by stumpc5 created at 2013-02-14 10:48:10

Replying to [comment:16 VivianePons]:

Viviane, do you want to take this over, should we do that later together, or should I do this?


---

Attachment

The patch looks very complete, thanks you!

One thing I noticed: I would like to be able to reconstruct a tree from its string representation. I.e.,

```
sage: BinaryTree("[., [[., [., .]], .]]")
```

Unfortunately, this resulted in an infinite recursion. It would be great if you could fix this.

(I am not yet done with my review...)

Cheers, Christian


---

Comment by VivianePons created at 2013-02-16 13:11:27

I added an extra patch to do exactly what you were asking. You can check and merge the two patches.


---

Comment by VivianePons created at 2013-02-16 13:12:10

(I added the feature for both ordered tree and binary trees)


---

Comment by stumpc5 created at 2013-02-16 13:15:18

Replying to [comment:23 VivianePons]:
> (I added the feature for both ordered tree and binary trees)

Thanks -- I wait for Florent or Fred for approval of your change.


---

Attachment

Replying to [comment:24 stumpc5]:
> Thanks -- I wait for Florent or Fred for approval of your change.

Thanks Viviane for this very good idea ! However, I feel that it should be more documented as well as tested. That's why I revamped your patch in a bigger patch. Please review it knowing that I'm Ok with your changes (the tests I added pass :-).

Florent


---

Comment by stumpc5 created at 2013-02-18 18:13:09

Replying to [comment:25 hivert]:

Two more things:

- what about lazily importing the new trees as this should be done by default?
- an_example / some_examples do not exist, so how am I supposed to get some binary tree to see what I can do with it?

btw: I would be okay with folding trac_8703-additional-feature-fh.patch and removing Viviane's patch in order to keep the ticket organized and the patchbot happy.

Cheers, Christian


---

Comment by hivert created at 2013-02-18 19:08:32

Replying to [comment:26 stumpc5]:
> Replying to [comment:25 hivert]:
> 
> Two more things:
> 
> - what about lazily importing the new trees as this should be done by default?

All the combinatorial objects are currently imported (not lazily). So I'd rather switching this once for all. Also there are some problems with lazy import (see eg #10906). 

> - an_example / some_examples do not exist, so how am I supposed to get some binary tree to see what I can do with it?

For combinatorial sets the convention is element rather than example which is
for categories. Anyway, if I had forgotten, `TestSuite` would had
complained.

```
sage: BinaryTrees().an_element()
.
sage: list(BinaryTrees().some_elements())
[., [., .],
...
[., [[[., .], [[., .], .]], .]]]
```


> btw: I would be okay with folding trac_8703-additional-feature-fh.patch and
> removing Viviane's patch in order to keep the ticket organized and the
> patchbot happy.

I kept thing separated to ease the review, planning to fold everything at the
end.

Florent


---

Comment by darij created at 2013-02-19 02:09:46

This is mostly way over my head, but I'm adding myself to cc because I'm highly interested in what comes out of this.

A bug: The as_digraph method yields not what it should yield when some labels are equal. Example:


```
sage: Q = LBT([LBT([],label=2),LBT([],label=4)],label=2) 
sage: Q.as_digraph()                                     
Digraph on 2 vertices
sage: Q
2[2[., .], 4[., .]]
```


While small examples suggest that this doesn't happen with "None" labels, this isn't actually the case (even though they somehow magically become nonnegative integers):


```
sage: Z = LabelledOrderedTree([[],[[[],[]], []]])
sage: Z   
None[None[], None[None[None[], None[]], None[]]]
sage: Z.as_digraph()
Digraph on 5 vertices
```


I suggest rewriting as_digraph from scratch, no longer using the labels as unique identifiers for nodes; independently, I think there should be more doctests checking what happens to trees with equal labels.

Some docstring gripes:

- I would add "BinaryTree([])" and "BinaryTree(None)" to the examples in te docstring of the BinaryTree class. Also, in the "INPUT" section, maybe add that [] is the same as [None, None]? I must say the "INPUT" part of the docstring for BinaryTree doesn't exactly explain to me how exactly the "children" argument is getting parsed; I am used to constructors for trees being free (in the sense of, no two different inputs lead to the same tree), so I wouldn't say this is very intuitive. It's "explained" in the __init__ sourcecode, but that's uncommented and I have no idea what it does :(

Might also want to point out that these binary trees are planar aka what you call ordered, i. e., the order of the children on each node matters. 

- In the "show" method of BinaryTree, can the tree_orientation be passed as a keyword? I know a lot of people who don't draw trees upside down...

- I don't understand from the docstrings what "make_node" and "make_leaf" do... Just replace the tree by a node resp. leaf? If so, what's the advantage over just redefining the tree?

- Docstring for "to_dyck_word": replace "where `T(l)` and `T(r)` are the trees" by "where `T(l)` and `T(r)` are the Dyck words".

- The docstring for "canopee" has a grammar error ("`1` is a left leaf" should be "`1` if the leaf is a left leaf").

- ordered_tree.py: Isn't this kind of "ordered trees" usually called planar trees? (Not like I want anything renamed. But it might be good to point out in the docstring that these ordered trees are not, e. g., Foissy's ordered trees.)

- Couple of typos in the docstring for OrderedTree: "a constructed" and "the the order".

- This appears weird to me: "The actual canonical labelling is currently unspecified." Isn't it just the left-to-right labelling, or are you saying that we shouldn't count on it staying that way?

Suggestions (I can figure myself working on them as well):

Do we have a checker function that looks if a given labelled binary tree is a binary search tree? A decreasing tree? The RSK-like algorithms from http://arxiv.org/abs/math/0401089 ? An binary_search_tree and an increasing_tree method for arbitrary words, not just permutations? (The "gen = self[::-1]" trick won't work here anymore, though.) Oh, well, and forests, of course, even if they can be internally the same as trees with one more vertex...


---

Comment by hivert created at 2013-02-19 20:49:22

Hi,

Thanks for all these comments. Before replying point by point, let me mention
that there is a lot of work done around the trees and that several patch are
waiting between this one. So we don't need to write everything in this patch
and we hope to have it in Sage soon.

Replying to [comment:28 darij]:
> This is mostly way over my head, but I'm adding myself to cc because I'm highly interested in what comes out of this.
> 
> A bug: The as_digraph method yields not what it should yield when some labels are equal. Example:
> I suggest rewriting as_digraph from scratch, no longer using the labels as unique identifiers for nodes; independently, I think there should be more doctests checking what happens to trees with equal labels.

When I wrote this function I plan to use it only for graph with distinct
label. I'm not sure what we want when there are repeated label. This must be
discussed. The particular case of None is by chance handled by the graph but
I'm not sure we should rely on it. In the mean time, I'd like to document that
the function currently only work for graph with disctinct label and open a new
ticket for more general cases. What do you think ?

> - I would add "BinaryTree([])" and "BinaryTree(None)"
> to the examples in te docstring of the BinaryTree class. Also, in the
> "INPUT" section, maybe add that [] is the same as [None, None]? I must say
> the "INPUT" part of the docstring for BinaryTree doesn't exactly explain to
> me how exactly the "children" argument is getting parsed; I am used to
> constructors for trees being free (in the sense of, no two different inputs
> lead to the same tree), so I wouldn't say this is very intuitive. It's
> "explained" in the __init__ sourcecode, but that's uncommented and I have no
> idea what it does :(

The idea is that to allows for short input, None can be omitted where there is
no ambiguity. Please, feel free to suggest a patch for doc improvements.

> Might also want to point out that these binary trees are planar aka what you
> call ordered, i. e., the order of the children on each node matters.

When you see tree from the graph point of view, all trees are of course planar
(IE: can be embedded in the plane without crossing). So I rather call them
ordered trees. From this point of view, the proper name is plane tree (See eg
http://en.wikipedia.org/wiki/Tree_%28graph_theory%29#Plane_Tree). Note that
they freely mix plane and ordered there. I feel (and I wasn't alone when
discussed on Sage-combinat-devel) that OrderedBinaryTree is too long.

> - In the "show" method of BinaryTree, can the tree_orientation be passed as
> a keyword? I know a lot of people who don't draw trees upside down...

Unless a quick fix is proposed, I'd rather leave it for a forthcomming patch.

> - I don't understand from the docstrings what "make_node" and "make_leaf"
> do... Just replace the tree by a node resp. leaf? If so, what's the
> advantage over just redefining the tree?

Some times it could be useful for algorithmic reason to modify a tree in place
without allocating a new object.

> - ordered_tree.py: Isn't this kind of "ordered trees" usually called planar trees? (Not like I want anything renamed. But it might be good to point out in the docstring that these ordered trees are not, e. g., Foissy's ordered trees.)

See my former comment on planar being improper.

> - This appears weird to me: "The actual canonical labelling is currently
> unspecified." Isn't it just the left-to-right labelling, or are you saying
> that we shouldn't count on it staying that way?

Yes it is for ordered trees, but it is defined in an abtract class and soon
after this patch there is another one for rooted unordered tree. Then
left-to-right labelling doesn't mean anything. There is also another
forthcoming patch where you can specify which order you want. I don't want to
choose the default now.

> Suggestions (I can figure myself working on them as well):

> Do we have a checker function that looks if a given labelled binary tree is
> a binary search tree? A decreasing tree? The RSK-like algorithms from
> http://arxiv.org/abs/math/0401089 ? An binary_search_tree and an
> increasing_tree method for arbitrary words, not just permutations? (The "gen
> = self[::-1]" trick won't work here anymore, though.) Oh, well, and forests,
> of course, even if they can be internally the same as trees with one more
> vertex...

There is also several other patch done around those question. In the
Sage-combinat queue there are implementation of the Loday-Ronco algebra, the
dendriform, prelie operads and more. As I said, this is just the beginning :-).


---

Comment by darij created at 2013-02-19 21:15:50

Hi Florent! Thanks for the reply. One reason why I did not propose any concrete changes to the code is that I have no idea what patches are currently dependent on this one (I only knew of Viviane's new one with the Dyck paths) and I want to avoid merge conflicts. I hoped some of you had a better overview of what's happening with trees these days. If you tell me there's no danger of conflicting changes, I can add the fixes I'd like to see; otherwise I'd prefer someone else to do it or to wait until the current slew of tree patches is merged. I'll try to come up with a doc for the initialization later today, though, provided I can wrap my head around it.

> When I wrote this function I plan to use it only for graph with
> distinct label. I'm not sure what we want when there are
> repeated label. This must be discussed.

Can we have a docstring warning about this, or a _ in the function name so as to avoid people getting a wrong impression?

> The particular case of None is by chance handled by the graph
> but I'm not sure we should rely on it.

As my second example shows, we should definitely *not* rely on it. Apparently None labels get translated into 0, 1, 2, 3, ..., but this translation starts anew for every subtree, so the resulting graph isn't the one you would expect.

> In the mean time, I'd like to document that the function
> currently only work for graph with disctinct label and open
> a new ticket for more general cases. What do you think ? 

Good idea.

I completely agree with you that planar/plane aren't good terms for this kind of trees. What I'd like is a mention in the docstring that these terms are occasionally used, whereas "ordered" is occasionally used for something else.

I can't wait to work with a real Loday-Ronco Hopf algebra rather than my hacky implementation from a year ago...


---

Comment by hivert created at 2013-02-19 21:34:04

Hi Darij,

Replying to [comment:31 darij]:
> Hi Florent! Thanks for the reply. One reason why I did not propose any
> concrete changes to the code is that I have no idea what patches are
> currently dependent on this one (I only knew of Viviane's new one with the
> Dyck paths) and I want to avoid merge conflicts. I hoped some of you had a
> better overview of what's happening with trees these days.

Here is some basic overview :-)

```
popcorn-*inat/.hg/patches $ grep -l Trees *.patch
algebras_over_operads-fc.patch
finite_semigroup-nt.patch
operads-fh.patch
operads_more-fc.patch
poset-from-tree-fc.patch
pretty_console_print-EliX-jbp.patch
q_tree_factorial-fc.patch
sage-demos-and-tutorials-nt.patch
shape_tree-fc.patch
shuffle-operads-fc.patch
trac_11529-rooted_trees-fh.patch
trac_13855_planar_binary_trees_hopf_algebra-EliX-jbp.patch
trac_13987_mary_trees-vp.patch
trac_14086-parking_functions-dm.patch
trac_8703-trees-fh.patch
trees_symmetry_factor-fh.patch
```



> If you tell me there's no danger of conflicting changes, I can add the fixes
> I'd like to see; otherwise I'd prefer someone else to do it or to wait until
> the current slew of tree patches is merged. I'll try to come up with a doc
> for the initialization later today, though, provided I can wrap my head
> around it.

I think if it's just docstring, there will only be trivial rebasing. Anyway,
they must be fixed. Unfortunately, I'm moving from my flat from a new house on
Saturday and Sunday so I won't have a lot of time working on trees... If you
can take care of all the docstring problem you mentioned once for all in a
review patch, I will really appreciate.


---

Comment by darij created at 2013-02-20 06:56:46

attempting manual override


---

Attachment

OK, I'm really not getting this:

```
darij@travis-virtualbox:~/sage-5.6/devel/sage-combinat$ hg commit
abort: cannot commit over an applied mq patch
```


Anyway, attaching my changed versions as a tar.gz [trees.tar.gz] containing the three relevant .py files (I only modified docstrings). Sorry for the format :( Hope someone transforms it into a .patch.

Here's something else I'm finding weird:

```
sage: a = []
sage: BinaryTree(a)
[., .]
sage: b = ()
sage: BinaryTree(b)
.
```

Or shouldn't lists and tuples behave alike here?


---

Comment by VivianePons created at 2013-03-01 15:18:36

Hi Darij,

I looked at your files, but you seemed to have also other patches applied because I see methods in your file that are not in mine. I don't want to mess everything up, so I would prefer if you put your changes into a patch: the reason it was not working is because the right command is "hg qrefresh". Thank's for reading the doc by the way.

Also, does anyone have sage 5.8.b2 to see why it is not applying ?


---

Comment by darij created at 2013-03-01 17:04:52

Hmm......


```
darij@travis-virtualbox:~/sage-5.6$ ./sage -hg qrefresh
/bin/sh: 1: [[: not found
Are you sure you want to refresh the following changes:
into the patch: no patches applied
(y/n)y
no patches applied
darij@travis-virtualbox:~/sage-5.6$ 
```


But maybe it's the wrong folder?


```
darij@travis-virtualbox:~/sage-5.6$ cd devel/sage-combinat/
darij@travis-virtualbox:~/sage-5.6/devel/sage-combinat$ ../../sage -hg qrefresh
/bin/sh: 1: [[: not found
Are you sure you want to refresh the following changes:
into the patch: patch.patch
(y/n)y
darij@travis-virtualbox:~/sage-5.6/devel/sage-combinat$ 
```


The fact that I have a newer file than you, Viviane, surprises me a bit since I remember the last trees-related activity on Sage to be from you...


---

Comment by VivianePons created at 2013-03-01 17:14:26

I think you're working on sage-combinat and you have other patches applied. There are patches on sage-combinat that are changing these files. I work on sage with only these two patches applied. 

I think your problem comes from the fact that you made changes but didn't create a patch beforehand to put your changes into.


---

Comment by darij created at 2013-03-01 17:22:02

Thanks! Looks like I missed qnew.
Will redo when sage 5.7 is finished installing.


---

Comment by VivianePons created at 2013-03-01 17:28:40

And by the way, you don't have to install sage-combinat to do that. You can clone your sage version and apply only the two patches which are on the ticket (this way, you're sure you don't have other changes to these files applied).


---

Comment by darij created at 2013-03-02 05:27:38

Viviane: thanks -- but I was installing 5.7 anyway due to the conference in a couple of days.

It seems I'm getting crazy or something, but now that I reinstalled sage again (and, yes, sage-combinat), there is no abstract_tree.py file in my devel/sage-combinat/sage/combinat folder. What did I do wrong? And how can I manually apply a patch that I've downloaded from trac?


---

Comment by stumpc5 created at 2013-03-02 05:55:54

Replying to [comment:39 darij]:
> Viviane: thanks -- but I was installing 5.7 anyway due to the conference in a couple of days.
> 
> It seems I'm getting crazy or something, but now that I reinstalled sage again (and, yes, sage-combinat), there is no abstract_tree.py file in my devel/sage-combinat/sage/combinat folder. What did I do wrong? And how can I manually apply a patch that I've downloaded from trac?

I think you should
- build the main Sage branch

```
$ sage -b main
```

- and clone it

```
$ sage -clone 8703
```

- then apply the patches

```
$ cd SAGEROOT/devel/sage-8703
$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8703/trac_8703-trees-fh.patch
$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8703/trac_8703-additional-feature-fh.patch
```

You should then have everything set to work on your features...

Cheers, Christian


---

Comment by darij created at 2013-03-02 06:59:17

Thank you, at least I've got the trees patch on my machine now... too bad hg still considers the patch itself, rather than only my meager additions to it, as my changes. Well, I guess it's easier if you just show me the right workflow in Providence in about 2 days; I'm groping in the dark for now as far as hg mq is concerned.


---

Comment by stumpc5 created at 2013-03-02 07:13:14

Replying to [comment:41 darij]:
> Thank you, at least I've got the trees patch on my machine now... too bad hg still considers the patch itself, rather than only my meager additions to it, as my changes. Well, I guess it's easier if you just show me the right workflow in Providence in about 2 days; I'm groping in the dark for now as far as hg mq is concerned.

Okay. After the above steps, you have to start a new patch

```
$ hg qnew trac_8703-trees_addition-dg.patch
```

and then you do your changes. Afterwards, you can review which files you have changed

```
$ hg status
```

and what you changed

```
$ hg diff
```

If you are happy with your changes, save them in the path using

```
$ hg qrefresh
```

and save this patch in your home folder

```
$ hg export tip > ~/trac_8703-trees_addition-dg.patch
```

Finally, upload it to trac!


---

Comment by darij created at 2013-03-02 07:32:10

Finally, it worked. Thank you!!

Is there a quick way to check the validity of the patch? I ended up with some changes I didn't want to make due to being new to kdiff3's merging function; I sanitized them out of the .patch file manually. Here's hoping I didn't corrupt it...

EDIT: Ooops... The changes to ordered_tree.py look weird to me; I certainly did not delete stuff but I added a sentence and fixed two typos. Am I reading the diff wrong or does it really have rogue changes?


---

Attachment

docstrings improved. let's see if this works...


---

Comment by darij created at 2013-03-02 08:26:49

File updated. Please ignore trees.tar.gz (no longer relevant), trac_8703-trees_addition-dg.2.patch (accidentally created by forgetting to check the "Replace existing file" toolbox) and trac_8703-trees_addition-dg.2.2.patch (accidentally created by trying to overwrite previous file).

Rogue edits are gone (they were due to me incorrectly resolving a conflict with fh's changes).


---

Attachment


---

Comment by VivianePons created at 2013-03-20 10:19:42

I have rebased trac_8703-trees-fh.patch so that it applies on sage-5.8. I cannot get trac_8703-trees_addition-dg.patch to apply, I get a "bad hunck" error and really, I just don't know what is wrong...


---

Comment by chapoton created at 2013-03-20 20:24:17

I have redone the dg review patch (with one or two more things)

for the bot:

apply trac_8703-trees-fh-rebase.patch trac_8703-additional-feature-fh.patch trac_8703-trees_addition-dg-v2.patch


---

Comment by darij created at 2013-03-20 20:32:23

Thanks, Frédéric! I was about to tell Viviane not to bother fixing my patch, as it was way more trouble than it was ever worth.

(I'm not surprised it had bank hunk errors since I messed around with the ,patch file in a text editor...)


---

Attachment

Thanks a lot Frédéric.

I just uploaded a new version of "additional feature", it's just a small fix about the "eval" function. I was using the "eval" function to transform a string into an object, I changed it to use "litteral_eval" which is more secured (it won't eval just any python code, it is restricted to simple objects).

Once the bot is happy, is there anything else to do on this patch or can it go with "positive review" ?

 for the bot:

apply trac_8703-trees-fh-rebase.patch trac_8703-additional-feature-vp.patch trac_8703-trees_addition-dg-v2.patch


---

Comment by chapoton created at 2013-03-21 13:11:03

better not import all of ast, but rather

```
from ast import literal_eval
```



---

Comment by chapoton created at 2013-03-21 13:46:17

There is still work to be done

* a whole paragraph about partitions at the beginning of BinaryTrees should be removed

* one should avoid using AssertionError

* a typo "only if they canonical labelled trees"

* a typo "labellel ordered tree"

I will try to make a review patch later.


---

Comment by darij created at 2013-03-21 15:49:54

Has anyone looked at the weirdness in http://trac.sagemath.org/sage_trac/ticket/8703#comment:33 ? It's not a serious problem, but might deserve documentation.


---

Comment by chapoton created at 2013-03-21 18:26:33

I have made more changes in the new review patch. And yes, comment 33 should be clarified.


---

Attachment

new patch, solving all issues in comments 33,52 and 53


---

Comment by chapoton created at 2013-03-31 19:27:37

a new small review patch, with typos essentially

Maybe this is good to go ?

for the bot:

apply trac_8703-trees-fh-rebase.patch trac_8703-additional-feature-vp.patch trac_8703-trees_addition-dg-v2.patch trac_8703-review-fc.patch


---

Attachment


---

Comment by VivianePons created at 2013-04-09 14:59:26

Thanks Frédéric for the review patches.

I have had a quick look and it seems alright. Anyway, Florent should look at the state of things now to see if he's happy and maybe we can go for a positive review!


---

Comment by hivert created at 2013-04-09 19:53:37

Changing status from needs_review to positive_review.


---

Attachment

I folded the patches for the release manager.

Florent


---

Comment by jdemeyer created at 2013-04-11 13:01:03

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2013-04-11 13:01:03

This shouldn't be in the commit message:

```
[mq]: trac_8703-additional-feature-vp.patch
```



---

Comment by jdemeyer created at 2013-04-12 07:12:38

And this patch should be rebased to sage-5.9.beta5.


---

Attachment

Rebased patch.

For patchbot:

Apply: trac_8703-trees-rebased.patch


---

Comment by tscrim created at 2013-04-15 00:32:40

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2013-04-15 08:42:45

Please review #14433, otherwise this patch cannot be merged.


---

Comment by jdemeyer created at 2013-04-23 09:40:46

Resolution: fixed
