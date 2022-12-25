# Issue 6812: Enumerate integer list up to the action of a Permutation Group

archive/issues_006812.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  sage-combinat\n\nKeywords: enumaration, integer, list, permutation, group\n\nThe goal is to enumerate lists up to the action of a Permutation Group. The final function is generate_list_of_sum(integer) which give all list which sum over all element is the integer.\n\nThe module in patch use the orderly generating algorithm. The goal is to select list which are maximals according the lexicographic order.\n\nThere is a lot of test on this module( strong_generating_system() are also test indirectly in this module... )\n\ndepends on #6647\n\nIssue created by migration from https://trac.sagemath.org/ticket/6812\n\n",
    "created_at": "2009-08-23T07:58:26Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.1",
    "title": "Enumerate integer list up to the action of a Permutation Group",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6812",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```
Assignee: tbd

CC:  sage-combinat

Keywords: enumaration, integer, list, permutation, group

The goal is to enumerate lists up to the action of a Permutation Group. The final function is generate_list_of_sum(integer) which give all list which sum over all element is the integer.

The module in patch use the orderly generating algorithm. The goal is to select list which are maximals according the lexicographic order.

There is a lot of test on this module( strong_generating_system() are also test indirectly in this module... )

depends on #6647

Issue created by migration from https://trac.sagemath.org/ticket/6812





---

archive/issue_comments_055967.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2009-08-23T08:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55967",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_comments_055968.json:
```json
{
    "body": "Changing assignee from tbd to @mwhansen.",
    "created_at": "2009-08-23T08:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55968",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing assignee from tbd to @mwhansen.



---

archive/issue_comments_055969.json:
```json
{
    "body": "I fixed some language mistakes. I already tell reviewers that there are probably still some typos, misunderstood or mistakes. I am sorry for that... It's hard!",
    "created_at": "2009-08-25T20:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55969",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

I fixed some language mistakes. I already tell reviewers that there are probably still some typos, misunderstood or mistakes. I am sorry for that... It's hard!



---

archive/issue_comments_055970.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-04T11:52:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55970",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from new to assigned.



---

archive/issue_comments_055971.json:
```json
{
    "body": "Refactoring : \n-> I move the code in sage/combinat/invariant_ring_perm_gps (advise form Nicolas Thi\u00e9ry)\n-> I implemented a new class InfiniteEnumeratedSet (with category)\n\nThere is no a shortcut in sage to IntegerVectorsUptoPermGroup which is a user friendly parent (with hope).\nThis code stay really strongly connected to the Invariant theory and connected with a the graded algebras of multivariate polynomial view as combination of orbit sum. This really why the code enter this new folder : sage/combinat/invariant_ring_perm_gps (other things have to come here....)",
    "created_at": "2009-09-04T11:52:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55971",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Refactoring : 
-> I move the code in sage/combinat/invariant_ring_perm_gps (advise form Nicolas Thiéry)
-> I implemented a new class InfiniteEnumeratedSet (with category)

There is no a shortcut in sage to IntegerVectorsUptoPermGroup which is a user friendly parent (with hope).
This code stay really strongly connected to the Invariant theory and connected with a the graded algebras of multivariate polynomial view as combination of orbit sum. This really why the code enter this new folder : sage/combinat/invariant_ring_perm_gps (other things have to come here....)



---

archive/issue_comments_055972.json:
```json
{
    "body": "Changing assignee from @mwhansen to nborie.",
    "created_at": "2009-09-04T11:52:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55972",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing assignee from @mwhansen to nborie.



---

archive/issue_comments_055973.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-22T09:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55973",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_055974.json:
```json
{
    "body": "Changing keywords from \"enumaration, integer, list, permutation, group\" to \"enumeration, integer, list, permutation, group\".",
    "created_at": "2009-11-22T10:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55974",
    "user": "https://github.com/aghitza"
}
```

Changing keywords from "enumaration, integer, list, permutation, group" to "enumeration, integer, list, permutation, group".



---

archive/issue_comments_055975.json:
```json
{
    "body": "Hi!\n\nThis is not a review yet, just some remarks.\n\nIndeed it seems to me that the comments and the documentation should be proof read by a native speaker. I am not a native speaker, I'm afraid.\n\nI also suggest to rename some methods. For example, the purpose of \"generate_list_of_sum\" is not clear from that name:\n\n* \"generate\" suggests a process. Therefore, I expected that the method would return an iterator. But in fact, an actual list is returned. A similar statement applies to \"get_orbit\". Why not simply \"orbit\"?\n* \"list_of_sums\" is not clear at all. I mean, there is the notion of \"partition\", so, there is no reason to describe it as \"list of sums\". Of course, not all partitions are returned, but representatives for each permutation class of partitions.\n\nSo, I think \"partition_class_representatives\" or slightly less precise \"partition_classes\" would be clearer.\n\nAnd \"generate_canonicals\": The return value is the list of canonical representatives of all children of the input. So, why not \"children_representatives\" or \"canonical_children\"?\n\nBest regards, Simon",
    "created_at": "2010-02-08T19:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55975",
    "user": "https://github.com/simon-king-jena"
}
```

Hi!

This is not a review yet, just some remarks.

Indeed it seems to me that the comments and the documentation should be proof read by a native speaker. I am not a native speaker, I'm afraid.

I also suggest to rename some methods. For example, the purpose of "generate_list_of_sum" is not clear from that name:

* "generate" suggests a process. Therefore, I expected that the method would return an iterator. But in fact, an actual list is returned. A similar statement applies to "get_orbit". Why not simply "orbit"?
* "list_of_sums" is not clear at all. I mean, there is the notion of "partition", so, there is no reason to describe it as "list of sums". Of course, not all partitions are returned, but representatives for each permutation class of partitions.

So, I think "partition_class_representatives" or slightly less precise "partition_classes" would be clearer.

And "generate_canonicals": The return value is the list of canonical representatives of all children of the input. So, why not "children_representatives" or "canonical_children"?

Best regards, Simon



---

archive/issue_comments_055976.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-11T18:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55976",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_055977.json:
```json
{
    "body": "Hi Simon,\n\nThank for these advises, I start a new cleanup and will update a better version shortly!",
    "created_at": "2010-02-11T18:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55977",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Hi Simon,

Thank for these advises, I start a new cleanup and will update a better version shortly!



---

archive/issue_comments_055978.json:
```json
{
    "body": "The patch use now the generic code from Search Forest (breadth_first_search....). So this patch now depends on #8288",
    "created_at": "2010-02-19T17:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55978",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

The patch use now the generic code from Search Forest (breadth_first_search....). So this patch now depends on #8288



---

archive/issue_comments_055979.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-19T17:22:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55979",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_055980.json:
```json
{
    "body": "Attachment [fast_generating_list_up_to_permgroup-nb.patch](tarball://root/attachments/some-uuid/ticket6812/fast_generating_list_up_to_permgroup-nb.patch) by nborie created at 2010-02-20 11:18:04",
    "created_at": "2010-02-20T11:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55980",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Attachment [fast_generating_list_up_to_permgroup-nb.patch](tarball://root/attachments/some-uuid/ticket6812/fast_generating_list_up_to_permgroup-nb.patch) by nborie created at 2010-02-20 11:18:04



---

archive/issue_comments_055981.json:
```json
{
    "body": "Add a canonical_representative method... This will perhaps help later...",
    "created_at": "2010-02-20T11:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55981",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Add a canonical_representative method... This will perhaps help later...



---

archive/issue_comments_055982.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-05T19:00:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55982",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_055983.json:
```json
{
    "body": "Please apply and look only the last patch...",
    "created_at": "2010-06-09T12:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55983",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Please apply and look only the last patch...



---

archive/issue_comments_055984.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-09T12:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55984",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_055985.json:
```json
{
    "body": "This looks very interesting, and I could definitely use it in my research (instead of looping over *all* integer vectors).  A few comments:\n\nThe syntax seems rather different than `IntegerVectors`, though; for instance, to access these vectors with a given sum one has to use a fairly awkward notation, instead of something analogous to `IntegerVectors(5,6)` for those sum 5, length 6.  Is it possible to streamline that?  \n\nAlso, there is fairly non-idiomatic English in some of the docstrings.  \n\nFinally, you should put your normal name in the \"Author\" field, instead of your Trac username, since the script which generates contributor lists uses this information directly.\n\nI am sorry that I am not familiar enough with the category framework to properly review this properly, though :(",
    "created_at": "2010-09-21T15:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55985",
    "user": "https://github.com/kcrisman"
}
```

This looks very interesting, and I could definitely use it in my research (instead of looping over *all* integer vectors).  A few comments:

The syntax seems rather different than `IntegerVectors`, though; for instance, to access these vectors with a given sum one has to use a fairly awkward notation, instead of something analogous to `IntegerVectors(5,6)` for those sum 5, length 6.  Is it possible to streamline that?  

Also, there is fairly non-idiomatic English in some of the docstrings.  

Finally, you should put your normal name in the "Author" field, instead of your Trac username, since the script which generates contributor lists uses this information directly.

I am sorry that I am not familiar enough with the category framework to properly review this properly, though :(



---

archive/issue_comments_055986.json:
```json
{
    "body": "Thanks for your remarks,\n\nI am going to open right now a vote for a better name and access to these class of parents on sage-combinat-devel (and you in CC to vote too). \n\nFeel free to point language mistakes to me! I have to improve my English. Use classical e-mail if you don't want to charge the trac.\n\nThanks very much, the code will be as much better as it will be used.\n\nNicolas.",
    "created_at": "2010-09-21T16:07:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55986",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Thanks for your remarks,

I am going to open right now a vote for a better name and access to these class of parents on sage-combinat-devel (and you in CC to vote too). 

Feel free to point language mistakes to me! I have to improve my English. Use classical e-mail if you don't want to charge the trac.

Thanks very much, the code will be as much better as it will be used.

Nicolas.



---

archive/issue_comments_055987.json:
```json
{
    "body": "I cleaned it, try to correct the language with some help and try to integrate previous advises... \n\napply trac_6812_integer_vectors_mod_permgroup.patch",
    "created_at": "2011-01-19T22:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55987",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

I cleaned it, try to correct the language with some help and try to integrate previous advises... 

apply trac_6812_integer_vectors_mod_permgroup.patch



---

archive/issue_comments_055988.json:
```json
{
    "body": "I will clean that after Nicolas (Thi\u00e9ry) would have review #8288...",
    "created_at": "2011-02-17T16:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55988",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

I will clean that after Nicolas (Thiéry) would have review #8288...



---

archive/issue_comments_055989.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-02-17T16:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55989",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_055990.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-04-05T14:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55990",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_055991.json:
```json
{
    "body": "For this last upload : \n\n* Cythonize the is_canonical test\n* Change syntax to have IntegerVectorsModPermgroup(G, sum=n) like IntegerVectors or other\n* Add a very heavy collection of tests in documentation for developers in the cython part\n\nI feel that my code is not very well polished, but I need advises, corrections and comments. Especially, I hope my English is not too much horrible. Flyspell is well configured on my emacs to american but I don't always use the right words. Sorry for that.\n\nOther things, I know the importance to have good tests in the code. But here, as the method `strong_generating_system` is very slow, test the module on any group take a very long time (around 3 seconds per group). I will be happy to get some advise and opinion on what deserve to be launch in doctest, what deserve to be kept in comment inside the code and what deserve to be trashed. Currently, the patch present a lot of tests in comments inside the code. It is perhaps too much (or the tests are not the goods one).",
    "created_at": "2011-04-05T14:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55991",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

For this last upload : 

* Cythonize the is_canonical test
* Change syntax to have IntegerVectorsModPermgroup(G, sum=n) like IntegerVectors or other
* Add a very heavy collection of tests in documentation for developers in the cython part

I feel that my code is not very well polished, but I need advises, corrections and comments. Especially, I hope my English is not too much horrible. Flyspell is well configured on my emacs to american but I don't always use the right words. Sorry for that.

Other things, I know the importance to have good tests in the code. But here, as the method `strong_generating_system` is very slow, test the module on any group take a very long time (around 3 seconds per group). I will be happy to get some advise and opinion on what deserve to be launch in doctest, what deserve to be kept in comment inside the code and what deserve to be trashed. Currently, the patch present a lot of tests in comments inside the code. It is perhaps too much (or the tests are not the goods one).



---

archive/issue_comments_055992.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-05T15:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55992",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_055993.json:
```json
{
    "body": "Any reason why you don't just use the tests but with this?\n\n```\nsage: long_test() # long time\n```\n\nIt's too much work to remove all the #s anyway if one wanted to try them out.\n\nI like the splitting things into pyx and not.  Also, any reason not to incorporate the pyx file into the documentation?  \n\nYou might want to add a couple examples to the cdef'd functions.  I realize this isn't required, but why not? :) \n\nWhat happens when you `list()` one of the infinite classes?  That should raise an error - I feel like we just had something like this somewhere else, but I can't remember where.  Also, you should put an example of how to get elements of the infinite class in the main class, since people may not ever read the documentation for something other than `IntegerVectorsModPermutationGroup`, which is the one intended to be used by people, right?  (It's the only one imported into the global namespace, at any rate.)  For this one, I put 'needs work'.\n\nFinally, you are right about the English; there are a few places where I'm not quite sure what is intended, even.  But that can be fixed.  Keep it up - this will be great!  (And very useful for me once I figure out how to use it correctly in my situation.)",
    "created_at": "2011-04-05T15:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55993",
    "user": "https://github.com/kcrisman"
}
```

Any reason why you don't just use the tests but with this?

```
sage: long_test() # long time
```

It's too much work to remove all the #s anyway if one wanted to try them out.

I like the splitting things into pyx and not.  Also, any reason not to incorporate the pyx file into the documentation?  

You might want to add a couple examples to the cdef'd functions.  I realize this isn't required, but why not? :) 

What happens when you `list()` one of the infinite classes?  That should raise an error - I feel like we just had something like this somewhere else, but I can't remember where.  Also, you should put an example of how to get elements of the infinite class in the main class, since people may not ever read the documentation for something other than `IntegerVectorsModPermutationGroup`, which is the one intended to be used by people, right?  (It's the only one imported into the global namespace, at any rate.)  For this one, I put 'needs work'.

Finally, you are right about the English; there are a few places where I'm not quite sure what is intended, even.  But that can be fixed.  Keep it up - this will be great!  (And very useful for me once I figure out how to use it correctly in my situation.)



---

archive/issue_comments_055994.json:
```json
{
    "body": "Thanks a lot for having regarded this...\n\nFor # long time, I do not know. I think I will select a subpart of the tests and include them with long time. The developer guide say : \"These will not be run regularly during Sage development, but will get run before major releases. No example should take more than about 30 seconds.\". Currently, on my three years old macbook, all tests take something like 6 minutes. Especially, there are also # optional - gap_database tests here. I will select some groups and add some tests with long time.\n\nI didn't know we can add pyx file in the doctree, I will add it. I will also add comments on the fact that the is_canonical test is polymorph. I just checked the only thing required is a comparison test:\n\n```\nsage: from sage.combinat.enumeration_mod_permgroup import is_canonical\nsage: G = PermutationGroup([[(1,2,3,4,5,6)]])\nsage: sgs = [map(lambda x: Permutation(x), trans) for trans in G.strong_generating_system()]\nsage: is_canonical(sgs, ['c','b','a','b','b','a'])\nTrue\nsage: is_canonical(sgs, [3,2,1,2,2,1])\nTrue\n```\n\nAs string can be compared with `<` and `>`, the function can be also used on such object.\n\nI think that examples in cdef functions aren't required just because one cannot import them in the sage console. Try from file.pyx import <tab>. There is perhaps another way to import them, but I don't know...\n\nFor the behavior of list(), I think it is ok. The category framework do the job:\n\n```\nsage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))\nsage: list(I)\n...\nNotImplementedError: infinite list\nsage: I = IntegerRange(1,+Infinity, 5)\nsage: I\n{1, 6, ..}\nsage: list(I)\n...\nNotImplementedError: infinite list\nsage: I = InfiniteEnumeratedSets().example()\nsage: I\nAn example of an infinite enumerated set: the non negative integers\nsage: list(I)\n...\nNotImplementedError: infinite list\n```\n\n\nI going to improve the doc of IntegerVectorsModPermutationGroup. You're definitely right and I think it deserves to stay the only entrance point for this module.\n\nThanks for your comments.",
    "created_at": "2011-04-05T16:10:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55994",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Thanks a lot for having regarded this...

For # long time, I do not know. I think I will select a subpart of the tests and include them with long time. The developer guide say : "These will not be run regularly during Sage development, but will get run before major releases. No example should take more than about 30 seconds.". Currently, on my three years old macbook, all tests take something like 6 minutes. Especially, there are also # optional - gap_database tests here. I will select some groups and add some tests with long time.

I didn't know we can add pyx file in the doctree, I will add it. I will also add comments on the fact that the is_canonical test is polymorph. I just checked the only thing required is a comparison test:

```
sage: from sage.combinat.enumeration_mod_permgroup import is_canonical
sage: G = PermutationGroup([[(1,2,3,4,5,6)]])
sage: sgs = [map(lambda x: Permutation(x), trans) for trans in G.strong_generating_system()]
sage: is_canonical(sgs, ['c','b','a','b','b','a'])
True
sage: is_canonical(sgs, [3,2,1,2,2,1])
True
```

As string can be compared with `<` and `>`, the function can be also used on such object.

I think that examples in cdef functions aren't required just because one cannot import them in the sage console. Try from file.pyx import <tab>. There is perhaps another way to import them, but I don't know...

For the behavior of list(), I think it is ok. The category framework do the job:

```
sage: I = IntegerVectorsModPermutationGroup(PermutationGroup([[(1,2,3,4)]]))
sage: list(I)
...
NotImplementedError: infinite list
sage: I = IntegerRange(1,+Infinity, 5)
sage: I
{1, 6, ..}
sage: list(I)
...
NotImplementedError: infinite list
sage: I = InfiniteEnumeratedSets().example()
sage: I
An example of an infinite enumerated set: the non negative integers
sage: list(I)
...
NotImplementedError: infinite list
```


I going to improve the doc of IntegerVectorsModPermutationGroup. You're definitely right and I think it deserves to stay the only entrance point for this module.

Thanks for your comments.



---

archive/issue_comments_055995.json:
```json
{
    "body": "Ok, I tried to include all previous remarks...\n\nI would say also that it is one of my first time with cython (I don't know if it is very well done...). This version integrate the tests with some with decorators long time.",
    "created_at": "2011-04-08T22:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55995",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Ok, I tried to include all previous remarks...

I would say also that it is one of my first time with cython (I don't know if it is very well done...). This version integrate the tests with some with decorators long time.



---

archive/issue_comments_055996.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-08T22:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55996",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_055997.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-09T23:21:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55997",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_055998.json:
```json
{
    "body": "I put a needs work because we must set on sage-combinat-devel if we plan to refactor integer vector as hashable type...\n\nI mainly implement this object to create an algebra whose basis is indexed by orbit_sum of monomial. But CombinatorialFreeModule requires hashable elements as basis keys. There is a choice here and I don't have the language overview to decide such direction.",
    "created_at": "2011-04-09T23:21:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55998",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

I put a needs work because we must set on sage-combinat-devel if we plan to refactor integer vector as hashable type...

I mainly implement this object to create an algebra whose basis is indexed by orbit_sum of monomial. But CombinatorialFreeModule requires hashable elements as basis keys. There is a choice here and I don't have the language overview to decide such direction.



---

archive/issue_comments_055999.json:
```json
{
    "body": "Just a question, as I've returned to the research where this could be helpful...\n\nI see at [this link](http://combinat.sagemath.org/doc/reference/sage/combinat/integer_vectors_mod_permgroup.html) that this stuff appears to actually be in the combinat branch already?  If so, is it possible that the 'needs work' issue has been resolved?",
    "created_at": "2011-06-04T11:49:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-55999",
    "user": "https://github.com/kcrisman"
}
```

Just a question, as I've returned to the research where this could be helpful...

I see at [this link](http://combinat.sagemath.org/doc/reference/sage/combinat/integer_vectors_mod_permgroup.html) that this stuff appears to actually be in the combinat branch already?  If so, is it possible that the 'needs work' issue has been resolved?



---

archive/issue_comments_056000.json:
```json
{
    "body": "As SearchForest as been integrated, let me one or two weeks (and FPSAC...) to finalize this... Stay in the area if you want to give review to this work. Feel free to give some comments, requests or advises especially if you have also use cases on this features.",
    "created_at": "2011-06-05T22:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56000",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

As SearchForest as been integrated, let me one or two weeks (and FPSAC...) to finalize this... Stay in the area if you want to give review to this work. Feel free to give some comments, requests or advises especially if you have also use cases on this features.



---

archive/issue_comments_056001.json:
```json
{
    "body": "I cleaned the imports, I improved a little the documentation...\n\nI am very sorry but it needs a STRONG REVIEW OF ENGLISH. My flyspell is well configured in my emacs but I feel that there are probably some not very well expressed sentences in my documentation. I tried to do my best... About the code, it is strongly tested, there is a lot of tests of consistences with other parts of combinat.\n\n\n```\nnicolas@lancelot:/opt/sage/devel/sage-combinat$ sage -t sage/combinat/integer_vectors_mod_permgroup.py -optional -long\nsage -t -optional -long \"devel/sage-combinat/sage/combinat/integer_vectors_mod_permgroup.py\"\n\t [10.3 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 10.3 seconds\nnicolas@lancelot:/opt/sage/devel/sage-combinat$ sage -t sage/combinat/enumeration_mod_permgroup.pyx -optional -long\nsage -t -optional -long \"devel/sage-combinat/sage/combinat/enumeration_mod_permgroup.pyx\"\n\t [38.5 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 38.5 seconds\n```\n\n\napply trac_6812_integer_vectors_mod_permgroup.patch (only)",
    "created_at": "2011-06-07T15:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56001",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

I cleaned the imports, I improved a little the documentation...

I am very sorry but it needs a STRONG REVIEW OF ENGLISH. My flyspell is well configured in my emacs but I feel that there are probably some not very well expressed sentences in my documentation. I tried to do my best... About the code, it is strongly tested, there is a lot of tests of consistences with other parts of combinat.


```
nicolas@lancelot:/opt/sage/devel/sage-combinat$ sage -t sage/combinat/integer_vectors_mod_permgroup.py -optional -long
sage -t -optional -long "devel/sage-combinat/sage/combinat/integer_vectors_mod_permgroup.py"
	 [10.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 10.3 seconds
nicolas@lancelot:/opt/sage/devel/sage-combinat$ sage -t sage/combinat/enumeration_mod_permgroup.pyx -optional -long
sage -t -optional -long "devel/sage-combinat/sage/combinat/enumeration_mod_permgroup.pyx"
	 [38.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 38.5 seconds
```


apply trac_6812_integer_vectors_mod_permgroup.patch (only)



---

archive/issue_comments_056002.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-06-07T15:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56002",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056003.json:
```json
{
    "body": "It depends on something in the sage combinat queue...",
    "created_at": "2011-06-07T17:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56003",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

It depends on something in the sage combinat queue...



---

archive/issue_comments_056004.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-07T17:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56004",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056005.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-06-07T18:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56005",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056006.json:
```json
{
    "body": "Ok, it depends on #10335\n\n\n```\nla pile de patchs est maintenant vide\nnicolas@lancelot:/opt/sage/devel/sage-review$ hg qpush\napplication de trac_10334-permgroup_cleanup-rebase-mh.patch\nactuellement \u00e0 : trac_10334-permgroup_cleanup-rebase-mh.patch\nnicolas@lancelot:/opt/sage/devel/sage-review$ hg qpush\napplication de trac_10335-permgroup_domain-mh.patch\nactuellement \u00e0 : trac_10335-permgroup_domain-mh.patch\nnicolas@lancelot:/opt/sage/devel/sage-review$ hg qpush\napplication de trac_6812_integer_vectors_mod_permgroup.patch\nactuellement \u00e0 : trac_6812_integer_vectors_mod_permgroup.patch\nnicolas@lancelot:/opt/sage/devel/sage-review$ sage -b\n...\nnicolas@lancelot:/opt/sage/devel/sage-review$ sage -t sage/combinat/enumeration_mod_permgroup.pyx \nsage -t  \"devel/sage-review/sage/combinat/enumeration_mod_permgroup.pyx\"\n\t [14.3 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 14.3 seconds\nnicolas@lancelot:/opt/sage/devel/sage-review$ sage -t sage/combinat/integer_vectors_mod_permgroup.py \nsage -t  \"devel/sage-review/sage/combinat/integer_vectors_mod_permgroup.py\"\n\t [5.7 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 5.7 seconds\n```\n",
    "created_at": "2011-06-07T18:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56006",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Ok, it depends on #10335


```
la pile de patchs est maintenant vide
nicolas@lancelot:/opt/sage/devel/sage-review$ hg qpush
application de trac_10334-permgroup_cleanup-rebase-mh.patch
actuellement à : trac_10334-permgroup_cleanup-rebase-mh.patch
nicolas@lancelot:/opt/sage/devel/sage-review$ hg qpush
application de trac_10335-permgroup_domain-mh.patch
actuellement à : trac_10335-permgroup_domain-mh.patch
nicolas@lancelot:/opt/sage/devel/sage-review$ hg qpush
application de trac_6812_integer_vectors_mod_permgroup.patch
actuellement à : trac_6812_integer_vectors_mod_permgroup.patch
nicolas@lancelot:/opt/sage/devel/sage-review$ sage -b
...
nicolas@lancelot:/opt/sage/devel/sage-review$ sage -t sage/combinat/enumeration_mod_permgroup.pyx 
sage -t  "devel/sage-review/sage/combinat/enumeration_mod_permgroup.pyx"
	 [14.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 14.3 seconds
nicolas@lancelot:/opt/sage/devel/sage-review$ sage -t sage/combinat/integer_vectors_mod_permgroup.py 
sage -t  "devel/sage-review/sage/combinat/integer_vectors_mod_permgroup.py"
	 [5.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 5.7 seconds
```




---

archive/issue_comments_056007.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-08T20:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56007",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056008.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-06-08T20:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56008",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056009.json:
```json
{
    "body": "After a big big rush on thesis finalization, I will try to dealt with this ticket as soon as possible... With all the comments that Karl-Dieter sent to me 4 months ago, I should be able to propose something interesting shortly.",
    "created_at": "2011-10-16T11:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56009",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

After a big big rush on thesis finalization, I will try to dealt with this ticket as soon as possible... With all the comments that Karl-Dieter sent to me 4 months ago, I should be able to propose something interesting shortly.



---

archive/issue_comments_056010.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-10-16T11:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56010",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056011.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-10-17T22:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56011",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056012.json:
```json
{
    "body": "The last version should be ready for review.",
    "created_at": "2011-10-17T22:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56012",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

The last version should be ready for review.



---

archive/issue_comments_056013.json:
```json
{
    "body": "please patchbot, \n\napply only [attachment:trac_6812_integer_vectors_mod_permgroup.patch]",
    "created_at": "2011-10-17T22:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56013",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

please patchbot, 

apply only [attachment:trac_6812_integer_vectors_mod_permgroup.patch]



---

archive/issue_comments_056014.json:
```json
{
    "body": "Second try for the buildbot:\n\napply trac_6812_integer_vectors_mod_permgroup.patch",
    "created_at": "2011-10-17T22:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56014",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Second try for the buildbot:

apply trac_6812_integer_vectors_mod_permgroup.patch



---

archive/issue_comments_056015.json:
```json
{
    "body": "Ok, it can't apply... I am sick of human dependencies coming from sharing a Mercurial queue... Sorry for all spam!",
    "created_at": "2011-10-17T22:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56015",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Ok, it can't apply... I am sick of human dependencies coming from sharing a Mercurial queue... Sorry for all spam!



---

archive/issue_comments_056016.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-10-17T22:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56016",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056017.json:
```json
{
    "body": "Are you talking about this patch depending on something in the combinat queue?",
    "created_at": "2011-10-18T02:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56017",
    "user": "https://github.com/jasongrout"
}
```

Are you talking about this patch depending on something in the combinat queue?



---

archive/issue_comments_056018.json:
```json
{
    "body": "Yes, precisely.\n\nAll works fine on the queue and I really spent a lot of time on that. But some patches (before me in the queue) and supposed to have the status \"Needs review\" on the trac make this patch can be apply (typically, file like '\\modules_list' or '\\doc\\bla\\foo' are concerned). As It was late in the night and I was tired, realize It doesn't work make me a little angry. Sorry for that.\n\nI will finalize it on a separate branch as much of Sage contributors usually do.",
    "created_at": "2011-10-18T07:36:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56018",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Yes, precisely.

All works fine on the queue and I really spent a lot of time on that. But some patches (before me in the queue) and supposed to have the status "Needs review" on the trac make this patch can be apply (typically, file like '\modules_list' or '\doc\bla\foo' are concerned). As It was late in the night and I was tired, realize It doesn't work make me a little angry. Sorry for that.

I will finalize it on a separate branch as much of Sage contributors usually do.



---

archive/issue_comments_056019.json:
```json
{
    "body": "apply trac_6812_integer_vectors_mod_permgroup.patch",
    "created_at": "2011-10-18T14:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56019",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

apply trac_6812_integer_vectors_mod_permgroup.patch



---

archive/issue_comments_056020.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-10-18T14:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56020",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056021.json:
```json
{
    "body": "All tests pass with -long and -optinal on the sage-combinat repository. I think the problems come from the two dependencies.",
    "created_at": "2011-10-19T17:42:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56021",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

All tests pass with -long and -optinal on the sage-combinat repository. I think the problems come from the two dependencies.



---

archive/issue_comments_056022.json:
```json
{
    "body": "Why does want the patchbot applies systematically the two patches... Where should I put the following line to make the patchbot remember it permanently ?\n\napply trac_6812_integer_vectors_mod_permgroup.patch",
    "created_at": "2011-10-19T19:00:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56022",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Why does want the patchbot applies systematically the two patches... Where should I put the following line to make the patchbot remember it permanently ?

apply trac_6812_integer_vectors_mod_permgroup.patch



---

archive/issue_comments_056023.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-11-16T21:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56023",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_056024.json:
```json
{
    "body": "This deserves a proper refactoring with ClonableIntArray...\n\nA new version is on the way.",
    "created_at": "2011-11-16T21:01:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56024",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

This deserves a proper refactoring with ClonableIntArray...

A new version is on the way.



---

archive/issue_comments_056025.json:
```json
{
    "body": "Hi Nicolas!\n\nSome questions: When we met in Orsay, we discussed some speed-ups of your code. Are they part of the attached patch? And couldn't one say that *for now* the patch needs review, and the transition to ClonableIntArray can be done on a different ticket? It would be nice to have the stuff in Sage, finally!",
    "created_at": "2012-05-18T14:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56025",
    "user": "https://github.com/simon-king-jena"
}
```

Hi Nicolas!

Some questions: When we met in Orsay, we discussed some speed-ups of your code. Are they part of the attached patch? And couldn't one say that *for now* the patch needs review, and the transition to ClonableIntArray can be done on a different ticket? It would be nice to have the stuff in Sage, finally!



---

archive/issue_comments_056026.json:
```json
{
    "body": "Yes, it would be very nice to have it in Sage...\n\nThe latest version of the patch is in the combinat queue. I didn't touch it for one mounth. However, finalize this patch is one of the things around the top of my todo list. After, the next week (positions application time en France...), the plan is to resubmit a version of the patch handling 0-1 enumeration (using a 'max_part' extra argument like in IntegerVectors and like) and implement the parent also as a QuotientSet with lift and retract method from IntegerVectors.\n\nIf no problem come to me before, I will update a new version before the end of the month.",
    "created_at": "2012-05-18T15:06:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56026",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Yes, it would be very nice to have it in Sage...

The latest version of the patch is in the combinat queue. I didn't touch it for one mounth. However, finalize this patch is one of the things around the top of my todo list. After, the next week (positions application time en France...), the plan is to resubmit a version of the patch handling 0-1 enumeration (using a 'max_part' extra argument like in IntegerVectors and like) and implement the parent also as a QuotientSet with lift and retract method from IntegerVectors.

If no problem come to me before, I will update a new version before the end of the month.



---

archive/issue_comments_056027.json:
```json
{
    "body": "Replying to [comment:47 nborie]:\n> \n> The latest version of the patch is in the combinat queue.\n\nThat means, including our discussion of last November, I guess.\n\nCould you remind me how I can obtain the current version of the patch?",
    "created_at": "2012-05-18T15:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56027",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:47 nborie]:
> 
> The latest version of the patch is in the combinat queue.

That means, including our discussion of last November, I guess.

Could you remind me how I can obtain the current version of the patch?



---

archive/issue_comments_056028.json:
```json
{
    "body": "Unfortunetly, I can update the last version...\n\nI need to download the 5.0, update the combinat queue and probably rebase my patch...\n\nPossibly, you can have access to it browsing the sources at : http://combinat.sagemath.org/patches/ \n\nHowever, I don't know if this latest version can be applied on any version of Sage.",
    "created_at": "2012-05-18T15:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56028",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Unfortunetly, I can update the last version...

I need to download the 5.0, update the combinat queue and probably rebase my patch...

Possibly, you can have access to it browsing the sources at : http://combinat.sagemath.org/patches/ 

However, I don't know if this latest version can be applied on any version of Sage.



---

archive/issue_comments_056029.json:
```json
{
    "body": "I am currently donwloading the 5.0 . Florent and Nicolas already make the queue apply on 5.0 .\nIf you can provide a relatively \"small\" reviewer patch (including correcting my English), I can promise you to do something this week end. I have no technical or algorithmical problem to finalize this patch. The code is already in my head and I have just to write it down.\n\nDima visited me last week in Orsay and he is also interested by the enumeration of integer vectors over 0 and 1 modulo the action of a permutation group. I already fixed all the details, just a (possible) rebase and some doctests should be fine before reuplaoding it.\n\nI will begin to compile the 5.0 in 5 minutes...",
    "created_at": "2012-05-18T15:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56029",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

I am currently donwloading the 5.0 . Florent and Nicolas already make the queue apply on 5.0 .
If you can provide a relatively "small" reviewer patch (including correcting my English), I can promise you to do something this week end. I have no technical or algorithmical problem to finalize this patch. The code is already in my head and I have just to write it down.

Dima visited me last week in Orsay and he is also interested by the enumeration of integer vectors over 0 and 1 modulo the action of a permutation group. I already fixed all the details, just a (possible) rebase and some doctests should be fine before reuplaoding it.

I will begin to compile the 5.0 in 5 minutes...



---

archive/issue_comments_056030.json:
```json
{
    "body": "Replying to [comment:49 nborie]:\n> I need to download the 5.0, update the combinat queue and probably rebase my patch...\n\nAt least the patch from here smoothly applies to sage-5.0. And since there are only few changes to existing files, I don't think there will be conflicts.\n\n> Possibly, you can have access to it browsing the sources at : http://combinat.sagemath.org/patches/ \n\nNo, I can't. I was searching for \"Borie\", and all I got was\n\n```\n3 weeks ago \tNicolas Borie \tGuards the refactor of integer vectors and dependencies...\n3 weeks ago \tNicolas Borie \tSome changes for integer vectors\n6 weeks ago \tNicolas Borie \tMove in Series and fold of the import fix made by florent (thanks you one more time!)\n6 weeks ago \tNicolas Borie \tMove in series\n7 weeks ago \tNicolas Borie \tSmall changes in integer vector experimental patch\n3 months ago \tNicolas Borie \tRefactoring IntegerVectors using SetFactories...\n3 months ago \tNicolas Borie \tFirst implementation of Schur/Schubert decomposition for multivariate polynomials\n3 months ago \tNicolas Borie \tFirst implementation od Schur / Schubert Decomposition of multivariate polynomials\n3 months ago \tNicolas Borie \tMerge\n3 months ago \tNicolas Borie \tFix two patch in the series (delete a name patch qremoved and replace a name qnewed)\n```\n\n\nSearching for \"integer vectors modulo permgroup\" (the commit message of the patch) didn't help either.\n\nSo, please provide an exact reference.",
    "created_at": "2012-05-18T20:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56030",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:49 nborie]:
> I need to download the 5.0, update the combinat queue and probably rebase my patch...

At least the patch from here smoothly applies to sage-5.0. And since there are only few changes to existing files, I don't think there will be conflicts.

> Possibly, you can have access to it browsing the sources at : http://combinat.sagemath.org/patches/ 

No, I can't. I was searching for "Borie", and all I got was

```
3 weeks ago 	Nicolas Borie 	Guards the refactor of integer vectors and dependencies...
3 weeks ago 	Nicolas Borie 	Some changes for integer vectors
6 weeks ago 	Nicolas Borie 	Move in Series and fold of the import fix made by florent (thanks you one more time!)
6 weeks ago 	Nicolas Borie 	Move in series
7 weeks ago 	Nicolas Borie 	Small changes in integer vector experimental patch
3 months ago 	Nicolas Borie 	Refactoring IntegerVectors using SetFactories...
3 months ago 	Nicolas Borie 	First implementation of Schur/Schubert decomposition for multivariate polynomials
3 months ago 	Nicolas Borie 	First implementation od Schur / Schubert Decomposition of multivariate polynomials
3 months ago 	Nicolas Borie 	Merge
3 months ago 	Nicolas Borie 	Fix two patch in the series (delete a name patch qremoved and replace a name qnewed)
```


Searching for "integer vectors modulo permgroup" (the commit message of the patch) didn't help either.

So, please provide an exact reference.



---

archive/issue_comments_056031.json:
```json
{
    "body": "From http://combinat.sagemath.org/patches/, I click on \"browse\" thus the URL become on MY computer : http://combinat.sagemath.org/patches/file/0079d727f7b8 (I don't know about the exad\u00e9cimal code after file/ ). Here I see a list of all files (patches and the series) in the repository and I click on the good patch. The URL become : \nhttp://combinat.sagemath.org/patches/file/0079d727f7b8/trac_6812_integer_vectors_mod_permgroup.patch\n\nI don't know if the links will work on your computer. Once you will have this page, click on 'raw', it downloaded the patch from the repository when I tested just 1 minute ago.\n\nI am sorry but I really don't manage the use of this mercurial web interface for repository. And as I said before, I will try to do something in the two days to come..\n\nCurrently, I just finish to build Sage and the patch doesn't need rebase for 5.0, I apply and Sage started with errors. This patch currently depends on : refactor_integer_vectors_clonableintarray-nb.patch #-4_7_2 # very experimental\nwhich is just before in the combinat-queue. I will make the patch for 6812 independent shortly.",
    "created_at": "2012-05-18T21:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56031",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

From http://combinat.sagemath.org/patches/, I click on "browse" thus the URL become on MY computer : http://combinat.sagemath.org/patches/file/0079d727f7b8 (I don't know about the exadécimal code after file/ ). Here I see a list of all files (patches and the series) in the repository and I click on the good patch. The URL become : 
http://combinat.sagemath.org/patches/file/0079d727f7b8/trac_6812_integer_vectors_mod_permgroup.patch

I don't know if the links will work on your computer. Once you will have this page, click on 'raw', it downloaded the patch from the repository when I tested just 1 minute ago.

I am sorry but I really don't manage the use of this mercurial web interface for repository. And as I said before, I will try to do something in the two days to come..

Currently, I just finish to build Sage and the patch doesn't need rebase for 5.0, I apply and Sage started with errors. This patch currently depends on : refactor_integer_vectors_clonableintarray-nb.patch #-4_7_2 # very experimental
which is just before in the combinat-queue. I will make the patch for 6812 independent shortly.



---

archive/issue_comments_056032.json:
```json
{
    "body": "Great, thank you! To my surprise, there is fuzz 2 for two hunks. But it does apply!",
    "created_at": "2012-05-18T21:30:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56032",
    "user": "https://github.com/simon-king-jena"
}
```

Great, thank you! To my surprise, there is fuzz 2 for two hunks. But it does apply!



---

archive/issue_comments_056033.json:
```json
{
    "body": "Too bad. Apparently, it has another dependency, namely one that creates the module integer_vector_cython. What are the dependencies?",
    "created_at": "2012-05-18T21:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56033",
    "user": "https://github.com/simon-king-jena"
}
```

Too bad. Apparently, it has another dependency, namely one that creates the module integer_vector_cython. What are the dependencies?



---

archive/issue_comments_056034.json:
```json
{
    "body": "Replying to [comment:54 SimonKing]:\n> What are the dependencies?\n\nSorry, now I see that you name refactor_integer_vectors_clonableintarray-nb.patch as a dependency. Anyway, if you intend to lift that dependency, I'll just wait the few days until you previde a new patch.",
    "created_at": "2012-05-18T21:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56034",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:54 SimonKing]:
> What are the dependencies?

Sorry, now I see that you name refactor_integer_vectors_clonableintarray-nb.patch as a dependency. Anyway, if you intend to lift that dependency, I'll just wait the few days until you previde a new patch.



---

archive/issue_comments_056035.json:
```json
{
    "body": "Yes, I will follow your comments done before... I will propose a new version this week end and the possible ameliorations will be part of separate tickets. The use of Clonable integer array is ok and fine because all is in Sage. For the rest, I will skip the dependencies and place some TODO in the code for further links with the combinat code.",
    "created_at": "2012-05-18T22:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56035",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Yes, I will follow your comments done before... I will propose a new version this week end and the possible ameliorations will be part of separate tickets. The use of Clonable integer array is ok and fine because all is in Sage. For the rest, I will skip the dependencies and place some TODO in the code for further links with the combinat code.



---

archive/issue_comments_056036.json:
```json
{
    "body": "Replying to [comment:56 nborie]:\n> I will propose a new version this week end and the possible ameliorations will be part of separate tickets. The use of Clonable integer array is ok and fine because all is in Sage.\n\nGreat! And will the Cython stuff we discussed in Paris also be part of that patch?\n\nFor the record: I finally re-implemented my algorithm for the computation of fundamental invariants of non-modular invariant rings of finite groups for the special case of permutation groups, using your implementation of orbits. I should have done that earlier. After all, thanks to your work on enumerating orbits, it will probably be a lot faster than my original implementation in Singular (which dealt very inefficiently with orbits).",
    "created_at": "2012-05-18T22:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56036",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:56 nborie]:
> I will propose a new version this week end and the possible ameliorations will be part of separate tickets. The use of Clonable integer array is ok and fine because all is in Sage.

Great! And will the Cython stuff we discussed in Paris also be part of that patch?

For the record: I finally re-implemented my algorithm for the computation of fundamental invariants of non-modular invariant rings of finite groups for the special case of permutation groups, using your implementation of orbits. I should have done that earlier. After all, thanks to your work on enumerating orbits, it will probably be a lot faster than my original implementation in Singular (which dealt very inefficiently with orbits).



---

archive/issue_comments_056037.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-05-20T09:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56037",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056038.json:
```json
{
    "body": "Ok, here is a last version :\n\n- Including categories of quotient of set and (In)finite enumerated set\n- Using the cython data structure based on C array\n- Tests of coherences with others features from combinat (Partition, monomials, graphs)\n- Handling of 0-1 enumeration (like adjacent matrix of graph)\n\nOn this last Patch, all tests pass with --long and --optional for the two new files. I didn't run all tests of Sage but this new feature is orthogonal with other part of Sage. The docbuild produce no warning and the doc looks clean.\n\nTo present one other test, here is the way to build all unlabeled graphs over 7 vertices :\n\n```\nsage: G = TransitiveGroup(21,38)\nsage: G.cardinality() == factorial(7)\nTrue\nsage: S = IntegerVectorsModPermutationGroup(G, max_part=1)\nsage: S._cardinality_from_iterator()\n1044\n```\n\nThis module, not optimized for the graphs do that in less than 1 minutes on my 4 years old macbook. As improvement for the future, the code is trivially \"parallelizable\". But this parallelization should be done on SearchForest and not on this module.\n\nFor the reviewer, please be careful with my English. I still try to correct myself as much but I am sure some sentences are not full-sense and there are probably some mistakes that flyspell (and me) didn't catch.\n\napply trac_6812_integer_vectors_mod_permgroup.patch",
    "created_at": "2012-05-20T09:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56038",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Ok, here is a last version :

- Including categories of quotient of set and (In)finite enumerated set
- Using the cython data structure based on C array
- Tests of coherences with others features from combinat (Partition, monomials, graphs)
- Handling of 0-1 enumeration (like adjacent matrix of graph)

On this last Patch, all tests pass with --long and --optional for the two new files. I didn't run all tests of Sage but this new feature is orthogonal with other part of Sage. The docbuild produce no warning and the doc looks clean.

To present one other test, here is the way to build all unlabeled graphs over 7 vertices :

```
sage: G = TransitiveGroup(21,38)
sage: G.cardinality() == factorial(7)
True
sage: S = IntegerVectorsModPermutationGroup(G, max_part=1)
sage: S._cardinality_from_iterator()
1044
```

This module, not optimized for the graphs do that in less than 1 minutes on my 4 years old macbook. As improvement for the future, the code is trivially "parallelizable". But this parallelization should be done on SearchForest and not on this module.

For the reviewer, please be careful with my English. I still try to correct myself as much but I am sure some sentences are not full-sense and there are probably some mistakes that flyspell (and me) didn't catch.

apply trac_6812_integer_vectors_mod_permgroup.patch



---

archive/issue_comments_056039.json:
```json
{
    "body": "Attachment [trac_6812_integer_vectors_mod_permgroup.patch](tarball://root/attachments/some-uuid/ticket6812/trac_6812_integer_vectors_mod_permgroup.patch) by nborie created at 2012-05-20 10:59:39",
    "created_at": "2012-05-20T10:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56039",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Attachment [trac_6812_integer_vectors_mod_permgroup.patch](tarball://root/attachments/some-uuid/ticket6812/trac_6812_integer_vectors_mod_permgroup.patch) by nborie created at 2012-05-20 10:59:39



---

archive/issue_comments_056040.json:
```json
{
    "body": "I just fix an import :\n\nIncreasingIntArray will move from sage.structure.list_clone to sage.structure.list_clone_demo (the patch moving the code is in the combinat queue) and I anticipate this change. All tests should pass on this new version.",
    "created_at": "2012-05-20T11:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56040",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

I just fix an import :

IncreasingIntArray will move from sage.structure.list_clone to sage.structure.list_clone_demo (the patch moving the code is in the combinat queue) and I anticipate this change. All tests should pass on this new version.



---

archive/issue_comments_056041.json:
```json
{
    "body": "As the patchbot change of mind every time, I had the following :\n\napply trac_6812_integer_vectors_mod_permgroup.patch",
    "created_at": "2012-05-20T11:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56041",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

As the patchbot change of mind every time, I had the following :

apply trac_6812_integer_vectors_mod_permgroup.patch



---

archive/issue_comments_056042.json:
```json
{
    "body": "We have\n\n```\n    def orbit(self, v):\n        assert isinstance(v, (list, ClonableIntArray)), '%s shoud be a Python list or an element of %s'%(v, self)\n        try:\n            if v.parent() is self:\n                return orbit(self._sgs, v)\n        except:\n            return orbit(self._sgs, self.element_class(self, v, check=False))\n```\n\n\nBy consequence, if the input is a clonable int array that belongs to a different parent, None is returned. I think there should better an error be raised.",
    "created_at": "2012-05-20T12:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56042",
    "user": "https://github.com/simon-king-jena"
}
```

We have

```
    def orbit(self, v):
        assert isinstance(v, (list, ClonableIntArray)), '%s shoud be a Python list or an element of %s'%(v, self)
        try:
            if v.parent() is self:
                return orbit(self._sgs, v)
        except:
            return orbit(self._sgs, self.element_class(self, v, check=False))
```


By consequence, if the input is a clonable int array that belongs to a different parent, None is returned. I think there should better an error be raised.



---

archive/issue_comments_056043.json:
```json
{
    "body": "Thanks for this comment and for the further to come. There are probably much more things to improve in the current code. I hope the current patch can allow you to play with invariants of permutation groups. However, I won't touch this patch anymore until one or two weeks. I am sorry but I need to prepare important dates for my future. I have an audition Tuesday for an associate professor position in the Faug\u00e8re'team PolSys and I must focus my work around the preparation of such appointments.\n\nAnyway, I will read all this page once I could come back to this stuff. Feel free to give some comments and commands around this module to improve the code.\n\nthe algorithmic details are explain in French in (with some Benchmarks):\nhttp://tel.archives-ouvertes.fr/docs/00/65/67/89/PDF/VD2_BORIE_NICOLAS_07122011.pdf\nIt is from page 39 to 51. It is in French but pictures should make things easy to understand.",
    "created_at": "2012-05-20T13:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56043",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Thanks for this comment and for the further to come. There are probably much more things to improve in the current code. I hope the current patch can allow you to play with invariants of permutation groups. However, I won't touch this patch anymore until one or two weeks. I am sorry but I need to prepare important dates for my future. I have an audition Tuesday for an associate professor position in the Faugère'team PolSys and I must focus my work around the preparation of such appointments.

Anyway, I will read all this page once I could come back to this stuff. Feel free to give some comments and commands around this module to improve the code.

the algorithmic details are explain in French in (with some Benchmarks):
http://tel.archives-ouvertes.fr/docs/00/65/67/89/PDF/VD2_BORIE_NICOLAS_07122011.pdf
It is from page 39 to 51. It is in French but pictures should make things easy to understand.



---

archive/issue_comments_056044.json:
```json
{
    "body": "Some more comments:\n\nThere should not only be a fast `ClonableIntArray.list()`, but also a fast\n`ClonableIntArray.tuple()`: Sometimes, one needs a tuple, not a list, and it\nwould be awkward and slow to first transfrom the clonable int array into a list\nand transform that into a tuple.\n\nI think that could be done here, or do you prefer a different ticket?\n\nYou know that my application of your work would be: Compute non-modular\ninvariant rings of permutation groups. For that purpose, it would be good if\nclonable int arrays could be used to define exponent vectors of a monomial. But\nthat should clearly be on a different ticket.",
    "created_at": "2012-05-20T15:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56044",
    "user": "https://github.com/simon-king-jena"
}
```

Some more comments:

There should not only be a fast `ClonableIntArray.list()`, but also a fast
`ClonableIntArray.tuple()`: Sometimes, one needs a tuple, not a list, and it
would be awkward and slow to first transfrom the clonable int array into a list
and transform that into a tuple.

I think that could be done here, or do you prefer a different ticket?

You know that my application of your work would be: Compute non-modular
invariant rings of permutation groups. For that purpose, it would be good if
clonable int arrays could be used to define exponent vectors of a monomial. But
that should clearly be on a different ticket.



---

archive/issue_comments_056045.json:
```json
{
    "body": "> There should not only be a fast `ClonableIntArray.list()`, but also a fast\n> `ClonableIntArray.tuple()`: Sometimes, one needs a tuple, not a list, and it\n> would be awkward and slow to first transfrom the clonable int array into a list\n> and transform that into a tuple.\n\nAdded on the todo list... But not mine todo list in fact. Florent Hivert (clone C array structure author) is going to patch his module. I will ask him if he can do something. The conversion to tuple should be implemented on the ClonableArray class in sage/structure/list_clone.pyx and thus we will get the fast conversion by inheritance. If we can optimize the conversion for integer, we will override it on the ClonableIntArray class. To avoid any conflict on merging, I will tell some words to Florent.\n\n> You know that my application of your work would be: Compute non-modular\n> invariant rings of permutation groups. For that purpose, it would be good if\n> clonable int arrays could be used to define exponent vectors of a monomial. But\n> that should clearly be on a different ticket.\n\nYep, I had to deal the same problem. For information, for the case I managed to compute with symmetric polynomials as homogeneous set of parameter (the powersums polynomials), selecting only the canonical monomials under staircase whose automorphism group is not the whole symmetric group (the orbit sum over G of the monomial is not trivially a symmetric polynomial), the enumeration engine make you find NEW secondary invariants with an average of 70% of chance. So, I can imagine your algorithmic will really save a lot of normal form computation. This rate is ok until 10 variables but falls at 30% for the only case at 14 variables (TransitiveGroup(14,61)) my algorithmic managed to compute. (you can see my algorithmic verbose here http://www.math.u-psud.fr/~borie/papers/14_61.txt)",
    "created_at": "2012-05-20T16:21:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56045",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

> There should not only be a fast `ClonableIntArray.list()`, but also a fast
> `ClonableIntArray.tuple()`: Sometimes, one needs a tuple, not a list, and it
> would be awkward and slow to first transfrom the clonable int array into a list
> and transform that into a tuple.

Added on the todo list... But not mine todo list in fact. Florent Hivert (clone C array structure author) is going to patch his module. I will ask him if he can do something. The conversion to tuple should be implemented on the ClonableArray class in sage/structure/list_clone.pyx and thus we will get the fast conversion by inheritance. If we can optimize the conversion for integer, we will override it on the ClonableIntArray class. To avoid any conflict on merging, I will tell some words to Florent.

> You know that my application of your work would be: Compute non-modular
> invariant rings of permutation groups. For that purpose, it would be good if
> clonable int arrays could be used to define exponent vectors of a monomial. But
> that should clearly be on a different ticket.

Yep, I had to deal the same problem. For information, for the case I managed to compute with symmetric polynomials as homogeneous set of parameter (the powersums polynomials), selecting only the canonical monomials under staircase whose automorphism group is not the whole symmetric group (the orbit sum over G of the monomial is not trivially a symmetric polynomial), the enumeration engine make you find NEW secondary invariants with an average of 70% of chance. So, I can imagine your algorithmic will really save a lot of normal form computation. This rate is ok until 10 variables but falls at 30% for the only case at 14 variables (TransitiveGroup(14,61)) my algorithmic managed to compute. (you can see my algorithmic verbose here http://www.math.u-psud.fr/~borie/papers/14_61.txt)



---

archive/issue_comments_056046.json:
```json
{
    "body": "Out of interest, I am trying to use my algorithm to find fundamental invariants for `TransitiveGroup(14,61)` over the rationals. The main bottleneck is the reduction of orbit sums modulo the previously found fundamental reductions (if the reduction is non-zero then the orbit sum is a new fundamental invariant). For some orbit sums in degree 8, the reduction takes several minutes!",
    "created_at": "2012-05-20T19:50:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56046",
    "user": "https://github.com/simon-king-jena"
}
```

Out of interest, I am trying to use my algorithm to find fundamental invariants for `TransitiveGroup(14,61)` over the rationals. The main bottleneck is the reduction of orbit sums modulo the previously found fundamental reductions (if the reduction is non-zero then the orbit sum is a new fundamental invariant). For some orbit sums in degree 8, the reduction takes several minutes!



---

archive/issue_comments_056047.json:
```json
{
    "body": "Replying to [comment:65 SimonKing]:\n> Out of interest, I am trying to use my algorithm to find fundamental invariants for `TransitiveGroup(14,61)` over the rationals. The main bottleneck is the reduction of orbit sums modulo the previously found fundamental reductions (if the reduction is non-zero then the orbit sum is a new fundamental invariant). For some orbit sums in degree 8, the reduction takes several minutes!\n\nYup. That's the purpose of Nicolas's algorithm: to handle large groups by avoiding such reductions.\n\nSpeaking of comparison of algorithms: we just got a Magma license to run systematic benchmarks on our computation server in Orsay in the coming months for Nicolas's paper. We should do this benchmark all together to get the best of all systems/algorithms.",
    "created_at": "2012-05-20T20:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56047",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:65 SimonKing]:
> Out of interest, I am trying to use my algorithm to find fundamental invariants for `TransitiveGroup(14,61)` over the rationals. The main bottleneck is the reduction of orbit sums modulo the previously found fundamental reductions (if the reduction is non-zero then the orbit sum is a new fundamental invariant). For some orbit sums in degree 8, the reduction takes several minutes!

Yup. That's the purpose of Nicolas's algorithm: to handle large groups by avoiding such reductions.

Speaking of comparison of algorithms: we just got a Magma license to run systematic benchmarks on our computation server in Orsay in the coming months for Nicolas's paper. We should do this benchmark all together to get the best of all systems/algorithms.



---

archive/issue_comments_056048.json:
```json
{
    "body": "What still needs review here?  Any English help still needed?\n\nA couple points on the built doc:\n* Some inconsistency in formatting, e.g. \n\n```\nIf sum is an integer, it returns a finite enumerated set containing all integer vectors maximum in their orbit for the lexicographic order and whose entries sum to `sum`.\n```\n\n  should pick `sum` or sum, preferably `sum`, I guess?\n* Similarly, sometimes there are no links, as in \n\n```\nTo get the orbit of any integer vector  under the action of the group, use the method orbit:\n```\n\n  but others are indeed hyperlinked.  Might as well get it all done for ease of browsing.\n* `last corner case :` should be `last corner case:`\n* There are lots of missing periods at ends of sentences.  That is, at the ends of sentences which are not ended by colons, which is fine.",
    "created_at": "2012-05-24T23:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56048",
    "user": "https://github.com/kcrisman"
}
```

What still needs review here?  Any English help still needed?

A couple points on the built doc:
* Some inconsistency in formatting, e.g. 

```
If sum is an integer, it returns a finite enumerated set containing all integer vectors maximum in their orbit for the lexicographic order and whose entries sum to `sum`.
```

  should pick `sum` or sum, preferably `sum`, I guess?
* Similarly, sometimes there are no links, as in 

```
To get the orbit of any integer vector  under the action of the group, use the method orbit:
```

  but others are indeed hyperlinked.  Might as well get it all done for ease of browsing.
* `last corner case :` should be `last corner case:`
* There are lots of missing periods at ends of sentences.  That is, at the ends of sentences which are not ended by colons, which is fine.



---

archive/issue_comments_056049.json:
```json
{
    "body": "Replying to [comment:67 kcrisman]:\n> What still needs review here?  Any English help still needed?\n\nSorry, I really should have focused on reviewing. Instead, I tried to use the patch in order to provide a better implementation of my algorithm on computing fundamental invariants of non-modular representations of finite groups, in the case of permutation groups.\n\nYes, the patch basically works (as confirmed by the patch bot). However, I will do some checks: My impression is that the combinat people tend to keep the most recent patch versions in the combinat queue, rather than posting them on trac.\n\nAnyway, the plan is that I provide a reviewer patch. But since I am no native speaker either, some additional help with English is certainly appreciated.",
    "created_at": "2012-05-25T06:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56049",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:67 kcrisman]:
> What still needs review here?  Any English help still needed?

Sorry, I really should have focused on reviewing. Instead, I tried to use the patch in order to provide a better implementation of my algorithm on computing fundamental invariants of non-modular representations of finite groups, in the case of permutation groups.

Yes, the patch basically works (as confirmed by the patch bot). However, I will do some checks: My impression is that the combinat people tend to keep the most recent patch versions in the combinat queue, rather than posting them on trac.

Anyway, the plan is that I provide a reviewer patch. But since I am no native speaker either, some additional help with English is certainly appreciated.



---

archive/issue_comments_056050.json:
```json
{
    "body": "I am puzzled: Is there anything special to do in order to build the combinat documentation? I tried sage -docbuild reference html, but even though integer_vectors_mod_permgroup is part of combinat/index.rst, I don't see it in the resulting documentation.",
    "created_at": "2012-05-25T11:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56050",
    "user": "https://github.com/simon-king-jena"
}
```

I am puzzled: Is there anything special to do in order to build the combinat documentation? I tried sage -docbuild reference html, but even though integer_vectors_mod_permgroup is part of combinat/index.rst, I don't see it in the resulting documentation.



---

archive/issue_comments_056051.json:
```json
{
    "body": "> I am puzzled: Is there anything special to do in order to build the combinat documentation? I tried sage -docbuild reference html, but even though integer_vectors_mod_permgroup is part of combinat/index.rst, I don't see it in the resulting documentation.\nTry `sage -b` first (maybe after touching the file); sometimes I forget to do that.",
    "created_at": "2012-05-25T14:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56051",
    "user": "https://github.com/kcrisman"
}
```

> I am puzzled: Is there anything special to do in order to build the combinat documentation? I tried sage -docbuild reference html, but even though integer_vectors_mod_permgroup is part of combinat/index.rst, I don't see it in the resulting documentation.
Try `sage -b` first (maybe after touching the file); sometimes I forget to do that.



---

archive/issue_comments_056052.json:
```json
{
    "body": "Replying to [comment:70 kcrisman]:\n> Try `sage -b` first (maybe after touching the file);\n\nI had done that. But it seems I was simply stupid. For whatever reason, I did not find the html file, even though it was present. Anyway, I am now reading it...",
    "created_at": "2012-05-25T14:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56052",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:70 kcrisman]:
> Try `sage -b` first (maybe after touching the file);

I had done that. But it seems I was simply stupid. For whatever reason, I did not find the html file, even though it was present. Anyway, I am now reading it...



---

archive/issue_comments_056053.json:
```json
{
    "body": "In the function lex_cmp_partial, I see that the `__getitem__` method of clonable int arrays is called repeatedly. Calling `__getitem__` means: It is tested whether the argument is an integer or a slice, and whether the integer is non-negative and smaller than the length of the array.\n\nI would think that lex_cmp_partial is called very often and is thus time critical, isn't it? Then, one should be a bit more direct: One should test saneness of the argument \"`step`\" only once, and should then directly access `v1._list[i]` and `v2._list[i]`. After all, v1 and v2 already are cdefined.\n\nI suppose the corresponding change will be part of my reviewer patch, but I'd appreciate if Nicolas would send me a couple of examples, so that I can see whether there is a speed-up.",
    "created_at": "2012-05-25T16:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56053",
    "user": "https://github.com/simon-king-jena"
}
```

In the function lex_cmp_partial, I see that the `__getitem__` method of clonable int arrays is called repeatedly. Calling `__getitem__` means: It is tested whether the argument is an integer or a slice, and whether the integer is non-negative and smaller than the length of the array.

I would think that lex_cmp_partial is called very often and is thus time critical, isn't it? Then, one should be a bit more direct: One should test saneness of the argument "`step`" only once, and should then directly access `v1._list[i]` and `v2._list[i]`. After all, v1 and v2 already are cdefined.

I suppose the corresponding change will be part of my reviewer patch, but I'd appreciate if Nicolas would send me a couple of examples, so that I can see whether there is a speed-up.



---

archive/issue_comments_056054.json:
```json
{
    "body": "Still in lex_cmp_partial: If the two list segments are equal, then each pair of items is compared twice, namely:\n\n```\n    for i in range(step):\n        if v1[i] > v2[i]:\n            return 1\n        if v1[i] < v2[i]:\n            return -1\n```\n\nHence, if they coincide in the first 10 positions and differ in the 11th, then 21 or 22 comparisons are needed to find the bigger vector. But if one does\n\n```\n    for i in range(step):\n        if v1[i] != v2[i]:\n            break\n    if i<step:\n        if v1[i]<v2[i]:\n            return -1\n        else:\n            return 1\n    return 0\n```\n\nthen only 11 or 12 comparisons are needed.",
    "created_at": "2012-05-25T16:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56054",
    "user": "https://github.com/simon-king-jena"
}
```

Still in lex_cmp_partial: If the two list segments are equal, then each pair of items is compared twice, namely:

```
    for i in range(step):
        if v1[i] > v2[i]:
            return 1
        if v1[i] < v2[i]:
            return -1
```

Hence, if they coincide in the first 10 positions and differ in the 11th, then 21 or 22 comparisons are needed to find the bigger vector. But if one does

```
    for i in range(step):
        if v1[i] != v2[i]:
            break
    if i<step:
        if v1[i]<v2[i]:
            return -1
        else:
            return 1
    return 0
```

then only 11 or 12 comparisons are needed.



---

archive/issue_comments_056055.json:
```json
{
    "body": "For example:\n\n```\nsage: cython(\"\"\"\n....: def test1(list L1, list L2, int step):\n....:     cdef int i\n....:     for i in range(step):\n....:         if L1[i]>L2[i]:\n....:             return 1\n....:         if L1[i]<L2[i]:\n....:             return -1\n....:     return 0\n....: def test2(list L1, list L2, int step):\n....:     cdef int i\n....:     for i in range(step):\n....:         if L1[i]!=L2[i]:\n....:             break\n....:     if i<step:\n....:         if L1[i]<L2[i]:\n....:             return -1\n....:         if L1[i]>L2[i]:\n....:             return 1\n....:     return 0\n....: \"\"\")\nsage: L1 = [1]*10+[1,2,3,4,5]\nsage: L2 = [1]*10+[5,4,3,2,1,0]\nsage: test1(L1,L2,9)\n0\nsage: test2(L1,L2,9)\n0\nsage: test1(L1,L2,14)\n-1\nsage: test2(L1,L2,14)\n-1\nsage: test1(L2,L1,14)\n1\nsage: test2(L2,L1,14)\n1\nsage: %timeit test1(L1,L2,14)\n625 loops, best of 3: 1.41 \u00b5s per loop\nsage: %timeit test2(L1,L2,14)\n625 loops, best of 3: 872 ns per loop\nsage: %timeit test1(L2,L1,14)\n625 loops, best of 3: 1.22 \u00b5s per loop\nsage: %timeit test2(L2,L1,14)\n625 loops, best of 3: 976 ns per loop\nsage: %timeit test1(L1,L2,10)\n625 loops, best of 3: 1.17 \u00b5s per loop\nsage: %timeit test2(L1,L2,10)\n625 loops, best of 3: 872 ns per loop\n```\n\nSo, it seems to make a small but noticeable difference.",
    "created_at": "2012-05-25T16:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56055",
    "user": "https://github.com/simon-king-jena"
}
```

For example:

```
sage: cython("""
....: def test1(list L1, list L2, int step):
....:     cdef int i
....:     for i in range(step):
....:         if L1[i]>L2[i]:
....:             return 1
....:         if L1[i]<L2[i]:
....:             return -1
....:     return 0
....: def test2(list L1, list L2, int step):
....:     cdef int i
....:     for i in range(step):
....:         if L1[i]!=L2[i]:
....:             break
....:     if i<step:
....:         if L1[i]<L2[i]:
....:             return -1
....:         if L1[i]>L2[i]:
....:             return 1
....:     return 0
....: """)
sage: L1 = [1]*10+[1,2,3,4,5]
sage: L2 = [1]*10+[5,4,3,2,1,0]
sage: test1(L1,L2,9)
0
sage: test2(L1,L2,9)
0
sage: test1(L1,L2,14)
-1
sage: test2(L1,L2,14)
-1
sage: test1(L2,L1,14)
1
sage: test2(L2,L1,14)
1
sage: %timeit test1(L1,L2,14)
625 loops, best of 3: 1.41 µs per loop
sage: %timeit test2(L1,L2,14)
625 loops, best of 3: 872 ns per loop
sage: %timeit test1(L2,L1,14)
625 loops, best of 3: 1.22 µs per loop
sage: %timeit test2(L2,L1,14)
625 loops, best of 3: 976 ns per loop
sage: %timeit test1(L1,L2,10)
625 loops, best of 3: 1.17 µs per loop
sage: %timeit test2(L1,L2,10)
625 loops, best of 3: 872 ns per loop
```

So, it seems to make a small but noticeable difference.



---

archive/issue_comments_056056.json:
```json
{
    "body": "When I see\n\n```\n            for child in children:\n                if child not in new_to_analyse:\n                    new_to_analyse.append(child)\n```\n\nin the cpdef function \"orbit\" in sage.combinat.enumeration_mod_permgroup.pyx, it seems to me that new_to_analyse should rather be a set, not a list, since the containment test \"child not in new_to_analyse\" works a *lot* faster on (long) sets than lists.\n\nCreate a relatively large set of random ints, and get the corresponding list (unsorted, apparently):\n\n```\nsage: S = set(randint(1,20000) for _ in range(5000))\nsage: L = list(S)\nsage: L[:10]\n[16384, 5019, 16203, 8195, 16388, 8197, 16391, 600, 16394, 8204]\n```\n\nNow, define one function operating on lists and another operating on sets that add the integers from 0 to 10000 to the list or set - but only if it isn't in the list/set yet.\n\n```\nsage: cython(\"\"\"\n....: def test1(list L):\n....:     cdef int i\n....:     for i in range(10000):\n....:         if i not in L:\n....:             L.append(i)\n....: def test2(set S):\n....:     cdef int i\n....:     for i in range(10000):\n....:         S.add(i)\n....: \"\"\")\nsage: len(L)\n4426\nsage: %time test1(L)\nCPU times: user 2.11 s, sys: 0.00 s, total: 2.12 s\nWall time: 2.12 s\nsage: len(L)\n12240\n```\n\nThe operation on the set is so much faster that I'm measuring it with timeit, also taking the time to copy the set (so that the length is preserved when running the loop for the timing):\n\n```\nsage: len(S)\n4426\nsage: %timeit test2(copy(S))\n625 loops, best of 3: 1.12 ms per loop\nsage: len(S)\n4426\n```\n\n\nHence, the same operation (at least in my proof-of-concept) is roughly 2000 times faster on sets than on lists.\n\nThe disadvantage is that the output of orbit() would be in a random order, so that to the very least it has to be sorted in the doc tests. Do you want that the output of orbit() is a sorted list (which would of course be easy to implement)?",
    "created_at": "2012-05-25T17:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56056",
    "user": "https://github.com/simon-king-jena"
}
```

When I see

```
            for child in children:
                if child not in new_to_analyse:
                    new_to_analyse.append(child)
```

in the cpdef function "orbit" in sage.combinat.enumeration_mod_permgroup.pyx, it seems to me that new_to_analyse should rather be a set, not a list, since the containment test "child not in new_to_analyse" works a *lot* faster on (long) sets than lists.

Create a relatively large set of random ints, and get the corresponding list (unsorted, apparently):

```
sage: S = set(randint(1,20000) for _ in range(5000))
sage: L = list(S)
sage: L[:10]
[16384, 5019, 16203, 8195, 16388, 8197, 16391, 600, 16394, 8204]
```

Now, define one function operating on lists and another operating on sets that add the integers from 0 to 10000 to the list or set - but only if it isn't in the list/set yet.

```
sage: cython("""
....: def test1(list L):
....:     cdef int i
....:     for i in range(10000):
....:         if i not in L:
....:             L.append(i)
....: def test2(set S):
....:     cdef int i
....:     for i in range(10000):
....:         S.add(i)
....: """)
sage: len(L)
4426
sage: %time test1(L)
CPU times: user 2.11 s, sys: 0.00 s, total: 2.12 s
Wall time: 2.12 s
sage: len(L)
12240
```

The operation on the set is so much faster that I'm measuring it with timeit, also taking the time to copy the set (so that the length is preserved when running the loop for the timing):

```
sage: len(S)
4426
sage: %timeit test2(copy(S))
625 loops, best of 3: 1.12 ms per loop
sage: len(S)
4426
```


Hence, the same operation (at least in my proof-of-concept) is roughly 2000 times faster on sets than on lists.

The disadvantage is that the output of orbit() would be in a random order, so that to the very least it has to be sorted in the doc tests. Do you want that the output of orbit() is a sorted list (which would of course be easy to implement)?



---

archive/issue_comments_056057.json:
```json
{
    "body": "Thanks so much for your comments!!!\n\nI didn't know Cython have a set data structure and YES, deleting the doubles at each step is the right way to take care of automorphism group of the vector, I must have used set!\n\nYou already explain to me at Orsay for the getitem with ClonableIntArray, it is an another mistake from me to not having updated the old code with that.\n\nI worked a lot on the algorithmic but I am a poor python/cython programmer. All your detailed comments make me understand what need to be done to produce an efficient code, thanks very much for this didactical approach.\n\nFrom my point of view, orbit() should return a set and not a list (mathematically and computationally speaking). Sorting it deserve to be only the choice of the user.\n\nI prepare for you some interesting benchmarks. Most of them consists in generating all canonical vectors under staircase for cyclic groups, symmetric groups and some transitive groups if you have installed the optional packages database_gap.",
    "created_at": "2012-05-25T17:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56057",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Thanks so much for your comments!!!

I didn't know Cython have a set data structure and YES, deleting the doubles at each step is the right way to take care of automorphism group of the vector, I must have used set!

You already explain to me at Orsay for the getitem with ClonableIntArray, it is an another mistake from me to not having updated the old code with that.

I worked a lot on the algorithmic but I am a poor python/cython programmer. All your detailed comments make me understand what need to be done to produce an efficient code, thanks very much for this didactical approach.

From my point of view, orbit() should return a set and not a list (mathematically and computationally speaking). Sorting it deserve to be only the choice of the user.

I prepare for you some interesting benchmarks. Most of them consists in generating all canonical vectors under staircase for cyclic groups, symmetric groups and some transitive groups if you have installed the optional packages database_gap.



---

archive/issue_comments_056058.json:
```json
{
    "body": "Attachment [benchmarks_generating_orbit_sum.py](tarball://root/attachments/some-uuid/ticket6812/benchmarks_generating_orbit_sum.py) by nborie created at 2012-05-25 19:24:21\n\nFunction to use for a good k-tests",
    "created_at": "2012-05-25T19:24:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56058",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Attachment [benchmarks_generating_orbit_sum.py](tarball://root/attachments/some-uuid/ticket6812/benchmarks_generating_orbit_sum.py) by nborie created at 2012-05-25 19:24:21

Function to use for a good k-tests



---

archive/issue_comments_056059.json:
```json
{
    "body": "Attachment [benchmarks_generation_orbit_sum.txt](tarball://root/attachments/some-uuid/ticket6812/benchmarks_generation_orbit_sum.txt) by nborie created at 2012-05-25 19:24:51\n\nOld results of speed",
    "created_at": "2012-05-25T19:24:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56059",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Attachment [benchmarks_generation_orbit_sum.txt](tarball://root/attachments/some-uuid/ticket6812/benchmarks_generation_orbit_sum.txt) by nborie created at 2012-05-25 19:24:51

Old results of speed



---

archive/issue_comments_056060.json:
```json
{
    "body": "I just added two files providing a good k-test (especially for invariant theory):\n\nThe function to use is: TEST_generation_orbit_sum\nThe function is in the file: benchmarks_generating_orbit_sum.py\n\nThe good tests to run are the following (depending the size you want to test):\n* TEST_generation_orbit_sum(TransitiveGroup(8,1), verbose=True) (~2 sec)\n* TEST_generation_orbit_sum(TransitiveGroup(9,1), verbose=True) (~20 sec)\n* TEST_generation_orbit_sum(TransitiveGroup(10,1), verbose=True) (~3 min)\n\nAll the complexity are contained in such examples.\n\nFor graphs lovers and the change from list to set, you should use a test including vector with large automorphism group like :\n\n```\nsage: G = TransitiveGroup(15,28)          \nsage: S = IntegerVectorsModPermutationGroup(G, max_part=1)\nsage: timeit('S._cardinality_from_iterator()')\n5 loops, best of 3: 1.3 s per loop\n```\n\nThis test build the 156 graphs over 6 vertices enumerated up to an isomorphism. And vectors whose entries are 0 or 1 have 'often' large automorphism group.\n\nComparing the old implementation with Python list (and 2 years of development of Sage), the module is currently 3 or 4 times faster.",
    "created_at": "2012-05-25T19:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56060",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

I just added two files providing a good k-test (especially for invariant theory):

The function to use is: TEST_generation_orbit_sum
The function is in the file: benchmarks_generating_orbit_sum.py

The good tests to run are the following (depending the size you want to test):
* TEST_generation_orbit_sum(TransitiveGroup(8,1), verbose=True) (~2 sec)
* TEST_generation_orbit_sum(TransitiveGroup(9,1), verbose=True) (~20 sec)
* TEST_generation_orbit_sum(TransitiveGroup(10,1), verbose=True) (~3 min)

All the complexity are contained in such examples.

For graphs lovers and the change from list to set, you should use a test including vector with large automorphism group like :

```
sage: G = TransitiveGroup(15,28)          
sage: S = IntegerVectorsModPermutationGroup(G, max_part=1)
sage: timeit('S._cardinality_from_iterator()')
5 loops, best of 3: 1.3 s per loop
```

This test build the 156 graphs over 6 vertices enumerated up to an isomorphism. And vectors whose entries are 0 or 1 have 'often' large automorphism group.

Comparing the old implementation with Python list (and 2 years of development of Sage), the module is currently 3 or 4 times faster.



---

archive/issue_comments_056061.json:
```json
{
    "body": "Replying to [comment:76 nborie]:\n> From my point of view, orbit() should return a set and not a list (mathematically and computationally speaking). Sorting it deserve to be only the choice of the user.\n\nOK. What I had a few minutes ago was: Compute with sets internally and return an ordered list. But if you agree that a set is nicer then I can change it (means: Change the doc tests and the specification of the output).\n\nAnd thank you for the benchmarks!",
    "created_at": "2012-05-25T19:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56061",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:76 nborie]:
> From my point of view, orbit() should return a set and not a list (mathematically and computationally speaking). Sorting it deserve to be only the choice of the user.

OK. What I had a few minutes ago was: Compute with sets internally and return an ordered list. But if you agree that a set is nicer then I can change it (means: Change the doc tests and the specification of the output).

And thank you for the benchmarks!



---

archive/issue_comments_056062.json:
```json
{
    "body": "There are two problems with the orbit() method:\n\n```\n        assert isinstance(v, (list, ClonableIntArray)), '%s shoud be a Python list or an element of %s'%(v, self)\n        try:\n            if v.parent() is self:\n                return orbit(self._sgs, v)\n        except:\n            return orbit(self._sgs, self.element_class(self, v, check=False))\n```\n\nThat means that *None* is returned if v happens to be a ClonableIntArray with a different parent. Shouldn't v be transformed into an element of `self` instead?\n\nAnd is it really a good idea to convert v into an element of `self` without checking?",
    "created_at": "2012-05-25T20:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56062",
    "user": "https://github.com/simon-king-jena"
}
```

There are two problems with the orbit() method:

```
        assert isinstance(v, (list, ClonableIntArray)), '%s shoud be a Python list or an element of %s'%(v, self)
        try:
            if v.parent() is self:
                return orbit(self._sgs, v)
        except:
            return orbit(self._sgs, self.element_class(self, v, check=False))
```

That means that *None* is returned if v happens to be a ClonableIntArray with a different parent. Shouldn't v be transformed into an element of `self` instead?

And is it really a good idea to convert v into an element of `self` without checking?



---

archive/issue_comments_056063.json:
```json
{
    "body": "Here is orbit() returning None:\n\n```\nsage: I =  IntegerVectorsModPermutationGroup(SymmetricGroup(5),5)\nsage: J =  IntegerVectorsModPermutationGroup(AlternatingGroup(5),5)\nsage: v = J([1,1,1,2,0], check=False)\nsage: print I.orbit(v)\nNone\n```\n",
    "created_at": "2012-05-25T20:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56063",
    "user": "https://github.com/simon-king-jena"
}
```

Here is orbit() returning None:

```
sage: I =  IntegerVectorsModPermutationGroup(SymmetricGroup(5),5)
sage: J =  IntegerVectorsModPermutationGroup(AlternatingGroup(5),5)
sage: v = J([1,1,1,2,0], check=False)
sage: print I.orbit(v)
None
```




---

archive/issue_comments_056064.json:
```json
{
    "body": "With the patch that I almost finished (not posted yet), I get\n\n```\nsage: TEST_generation_orbit_sum(TransitiveGroup(8,1), verbose=True)\nFor G be the transitive group number 1 of degree 8\nCardinality of G : 8\n  \nCardinality of secondary invariants : 5040\nNumber of canonical monomials under staircase : 18297\nTotal time : 1.49698710442\n ------------------------------------- \n(1.4969871044158936, 18297, 8)\nsage: TEST_generation_orbit_sum(TransitiveGroup(9,1), verbose=True)\nFor G be the transitive group number 1 of degree 9\nCardinality of G : 9\n  \nCardinality of secondary invariants : 40320\nNumber of canonical monomials under staircase : 153974\nTotal time : 13.5961458683\n ------------------------------------- \n(13.596145868301392, 153974, 9)\nsage: TEST_generation_orbit_sum(TransitiveGroup(10,1), verbose=True)\nFor G be the transitive group number 1 of degree 10\nCardinality of G : 10\n  \nCardinality of secondary invariants : 362880\nNumber of canonical monomials under staircase : 1452325\nTotal time : 140.386005878\n ------------------------------------- \n(140.3860058784485, 1452325, 10)\nsage: G = TransitiveGroup(15,28)\nsage: S = IntegerVectorsModPermutationGroup(G, max_part=1)\nsage: timeit('S._cardinality_from_iterator()')\n5 loops, best of 3: 415 ms per loop\n```\n\n\nWithout the patch, I get\n\n```\nsage: TEST_generation_orbit_sum(TransitiveGroup(8,1), verbose=True)\nFor G be the transitive group number 1 of degree 8\nCardinality of G : 8\n  \nCardinality of secondary invariants : 5040\nNumber of canonical monomials under staircase : 18297\nTotal time : 1.58537387848\n ------------------------------------- \n(1.585373878479004, 18297, 8)\nsage: TEST_generation_orbit_sum(TransitiveGroup(9,1), verbose=True)\nFor G be the transitive group number 1 of degree 9\nCardinality of G : 9\n  \nCardinality of secondary invariants : 40320\nNumber of canonical monomials under staircase : 153974\nTotal time : 15.0423038006\n ------------------------------------- \n(15.042303800582886, 153974, 9)\nsage: TEST_generation_orbit_sum(TransitiveGroup(10,1), verbose=True)\nFor G be the transitive group number 1 of degree 10\nCardinality of G : 10\n  \nCardinality of secondary invariants : 362880\nNumber of canonical monomials under staircase : 1452325\nTotal time : 162.007292032\n ------------------------------------- \n(162.00729203224182, 1452325, 10)\nsage: G = TransitiveGroup(15,28)\nsage: S = IntegerVectorsModPermutationGroup(G, max_part=1)\nsage: timeit('S._cardinality_from_iterator()')\n5 loops, best of 3: 933 ms per loop\n```\n\n\nSo, it is roughly 10% to 50% improvement (even though I am currently still converting the set to sorted lists).",
    "created_at": "2012-05-25T20:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56064",
    "user": "https://github.com/simon-king-jena"
}
```

With the patch that I almost finished (not posted yet), I get

```
sage: TEST_generation_orbit_sum(TransitiveGroup(8,1), verbose=True)
For G be the transitive group number 1 of degree 8
Cardinality of G : 8
  
Cardinality of secondary invariants : 5040
Number of canonical monomials under staircase : 18297
Total time : 1.49698710442
 ------------------------------------- 
(1.4969871044158936, 18297, 8)
sage: TEST_generation_orbit_sum(TransitiveGroup(9,1), verbose=True)
For G be the transitive group number 1 of degree 9
Cardinality of G : 9
  
Cardinality of secondary invariants : 40320
Number of canonical monomials under staircase : 153974
Total time : 13.5961458683
 ------------------------------------- 
(13.596145868301392, 153974, 9)
sage: TEST_generation_orbit_sum(TransitiveGroup(10,1), verbose=True)
For G be the transitive group number 1 of degree 10
Cardinality of G : 10
  
Cardinality of secondary invariants : 362880
Number of canonical monomials under staircase : 1452325
Total time : 140.386005878
 ------------------------------------- 
(140.3860058784485, 1452325, 10)
sage: G = TransitiveGroup(15,28)
sage: S = IntegerVectorsModPermutationGroup(G, max_part=1)
sage: timeit('S._cardinality_from_iterator()')
5 loops, best of 3: 415 ms per loop
```


Without the patch, I get

```
sage: TEST_generation_orbit_sum(TransitiveGroup(8,1), verbose=True)
For G be the transitive group number 1 of degree 8
Cardinality of G : 8
  
Cardinality of secondary invariants : 5040
Number of canonical monomials under staircase : 18297
Total time : 1.58537387848
 ------------------------------------- 
(1.585373878479004, 18297, 8)
sage: TEST_generation_orbit_sum(TransitiveGroup(9,1), verbose=True)
For G be the transitive group number 1 of degree 9
Cardinality of G : 9
  
Cardinality of secondary invariants : 40320
Number of canonical monomials under staircase : 153974
Total time : 15.0423038006
 ------------------------------------- 
(15.042303800582886, 153974, 9)
sage: TEST_generation_orbit_sum(TransitiveGroup(10,1), verbose=True)
For G be the transitive group number 1 of degree 10
Cardinality of G : 10
  
Cardinality of secondary invariants : 362880
Number of canonical monomials under staircase : 1452325
Total time : 162.007292032
 ------------------------------------- 
(162.00729203224182, 1452325, 10)
sage: G = TransitiveGroup(15,28)
sage: S = IntegerVectorsModPermutationGroup(G, max_part=1)
sage: timeit('S._cardinality_from_iterator()')
5 loops, best of 3: 933 ms per loop
```


So, it is roughly 10% to 50% improvement (even though I am currently still converting the set to sorted lists).



---

archive/issue_comments_056065.json:
```json
{
    "body": "Replying to [comment:79 SimonKing]:\n> There are two problems with the orbit() method:\n> {{{\n>         assert isinstance(v, (list, ClonableIntArray)), '%s shoud be a Python list or an element of %s'%(v, self)\n>         try:\n>             if v.parent() is self:\n>                 return orbit(self._sgs, v)\n>         except:\n>             return orbit(self._sgs, self.element_class(self, v, check=False))\n> }}}\n> That means that *None* is returned if v happens to be a ClonableIntArray with a different parent. Shouldn't v be transformed into an element of `self` instead?\n> \n> And is it really a good idea to convert v into an element of `self` without checking?\n\nYes, this piece of code is horribly ugly... The point is that the orbit method will work with any integer vector. v doesn't need to be canonical. I don't have a use case but I was thinking it would be more convenient to allow the user to use this method for any integer vector (canonical or not). \n\nAfter for safety, I don't know the consequence of such a choice on the lung run.\n\nAnyway, the test is_canonical should be very very much faster than the full expansion of an orbit and a user who want just an orbit can also compute his own function.",
    "created_at": "2012-05-25T20:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56065",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Replying to [comment:79 SimonKing]:
> There are two problems with the orbit() method:
> {{{
>         assert isinstance(v, (list, ClonableIntArray)), '%s shoud be a Python list or an element of %s'%(v, self)
>         try:
>             if v.parent() is self:
>                 return orbit(self._sgs, v)
>         except:
>             return orbit(self._sgs, self.element_class(self, v, check=False))
> }}}
> That means that *None* is returned if v happens to be a ClonableIntArray with a different parent. Shouldn't v be transformed into an element of `self` instead?
> 
> And is it really a good idea to convert v into an element of `self` without checking?

Yes, this piece of code is horribly ugly... The point is that the orbit method will work with any integer vector. v doesn't need to be canonical. I don't have a use case but I was thinking it would be more convenient to allow the user to use this method for any integer vector (canonical or not). 

After for safety, I don't know the consequence of such a choice on the lung run.

Anyway, the test is_canonical should be very very much faster than the full expansion of an orbit and a user who want just an orbit can also compute his own function.



---

archive/issue_comments_056066.json:
```json
{
    "body": "Replying to [comment:82 nborie]:\n> Yes, this piece of code is horribly ugly... The point is that the orbit method will work with any integer vector. v doesn't need to be canonical. I don't have a use case but I was thinking it would be more convenient to allow the user to use this method for any integer vector (canonical or not). \n\nAgreed. So, check=False should be fine.\n\nBut I do think that the orbit method should try to convert the input vector from a different parent into self, and should certainly not return \"None\".\n\n> Anyway, the test is_canonical should be very very much faster than the full expansion of an orbit\n\nOf course. The algorithm for is_canonical looks almost the same as the full expansion of an orbit, but if it is in fact non-canonical then the function will return \"False\" before finishing the computation of the whole orbit.\n\nBy the way, I made some further tweaks and am now down to\n\n```\nsage: TEST_generation_orbit_sum(TransitiveGroup(8,1), verbose=True)\nFor G be the transitive group number 1 of degree 8\nCardinality of G : 8\n  \nCardinality of secondary invariants : 5040\nNumber of canonical monomials under staircase : 18297\nTotal time : 1.43067121506\n ------------------------------------- \n(1.430671215057373, 18297, 8)\nsage: TEST_generation_orbit_sum(TransitiveGroup(9,1), verbose=True)\nFor G be the transitive group number 1 of degree 9\nCardinality of G : 9\n  \nCardinality of secondary invariants : 40320\nNumber of canonical monomials under staircase : 153974\nTotal time : 12.9384939671\n ------------------------------------- \n(12.938493967056274, 153974, 9)\nsage: TEST_generation_orbit_sum(TransitiveGroup(10,1), verbose=True)\nFor G be the transitive group number 1 of degree 10\nCardinality of G : 10\n  \nCardinality of secondary invariants : 362880\nNumber of canonical monomials under staircase : 1452325\nTotal time : 134.613152981\n ------------------------------------- \n(134.61315298080444, 1452325, 10)\nsage: G = TransitiveGroup(15,28)\nsage: S = IntegerVectorsModPermutationGroup(G, max_part=1)\nsage: timeit('S._cardinality_from_iterator()')\n5 loops, best of 3: 408 ms per loop\n```\n",
    "created_at": "2012-05-25T21:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56066",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:82 nborie]:
> Yes, this piece of code is horribly ugly... The point is that the orbit method will work with any integer vector. v doesn't need to be canonical. I don't have a use case but I was thinking it would be more convenient to allow the user to use this method for any integer vector (canonical or not). 

Agreed. So, check=False should be fine.

But I do think that the orbit method should try to convert the input vector from a different parent into self, and should certainly not return "None".

> Anyway, the test is_canonical should be very very much faster than the full expansion of an orbit

Of course. The algorithm for is_canonical looks almost the same as the full expansion of an orbit, but if it is in fact non-canonical then the function will return "False" before finishing the computation of the whole orbit.

By the way, I made some further tweaks and am now down to

```
sage: TEST_generation_orbit_sum(TransitiveGroup(8,1), verbose=True)
For G be the transitive group number 1 of degree 8
Cardinality of G : 8
  
Cardinality of secondary invariants : 5040
Number of canonical monomials under staircase : 18297
Total time : 1.43067121506
 ------------------------------------- 
(1.430671215057373, 18297, 8)
sage: TEST_generation_orbit_sum(TransitiveGroup(9,1), verbose=True)
For G be the transitive group number 1 of degree 9
Cardinality of G : 9
  
Cardinality of secondary invariants : 40320
Number of canonical monomials under staircase : 153974
Total time : 12.9384939671
 ------------------------------------- 
(12.938493967056274, 153974, 9)
sage: TEST_generation_orbit_sum(TransitiveGroup(10,1), verbose=True)
For G be the transitive group number 1 of degree 10
Cardinality of G : 10
  
Cardinality of secondary invariants : 362880
Number of canonical monomials under staircase : 1452325
Total time : 134.613152981
 ------------------------------------- 
(134.61315298080444, 1452325, 10)
sage: G = TransitiveGroup(15,28)
sage: S = IntegerVectorsModPermutationGroup(G, max_part=1)
sage: timeit('S._cardinality_from_iterator()')
5 loops, best of 3: 408 ms per loop
```




---

archive/issue_comments_056067.json:
```json
{
    "body": "Replying to [comment:83 SimonKing]:\n> But I do think that the orbit method should try to convert the input vector from a different parent into self, and should certainly not return \"None\".\n\nYes! None is not an option here. It must return a set or raise an error.\n\n> Of course. The algorithm for is_canonical looks almost the same as the full expansion of an orbit, but if it is in fact non-canonical then the function will return \"False\" before finishing the computation of the whole orbit.\n\nAnd more than that, there is a king of gardener lemma inside the is_canonical method, the partial_lex comparison cut some branches of the orbit just by reading the first entries.\n\nI also think the change from list to set produce more than x2 speedup, it is probably an exponential optimization, you should try before and after with graphs over 7 vertices :\n\n```\nsage: G = TransitiveGroup(21,38)          \nsage: S = IntegerVectorsModPermutationGroup(G, max_part=1)\nsage: time S._cardinality_from_iterator()\n1044\nTime: CPU 128.64 s, Wall: 136.10 s\n```\n\nIt become to be a large test for this last one. (1044 symmetric matrices of size 7)\n\nA student of Florent Hivert had to master project to parallelize SearchForest. Imagine what such module can need by inheritance... (with possible adaptations according changes of SearchForest)",
    "created_at": "2012-05-25T21:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56067",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Replying to [comment:83 SimonKing]:
> But I do think that the orbit method should try to convert the input vector from a different parent into self, and should certainly not return "None".

Yes! None is not an option here. It must return a set or raise an error.

> Of course. The algorithm for is_canonical looks almost the same as the full expansion of an orbit, but if it is in fact non-canonical then the function will return "False" before finishing the computation of the whole orbit.

And more than that, there is a king of gardener lemma inside the is_canonical method, the partial_lex comparison cut some branches of the orbit just by reading the first entries.

I also think the change from list to set produce more than x2 speedup, it is probably an exponential optimization, you should try before and after with graphs over 7 vertices :

```
sage: G = TransitiveGroup(21,38)          
sage: S = IntegerVectorsModPermutationGroup(G, max_part=1)
sage: time S._cardinality_from_iterator()
1044
Time: CPU 128.64 s, Wall: 136.10 s
```

It become to be a large test for this last one. (1044 symmetric matrices of size 7)

A student of Florent Hivert had to master project to parallelize SearchForest. Imagine what such module can need by inheritance... (with possible adaptations according changes of SearchForest)



---

archive/issue_comments_056068.json:
```json
{
    "body": "Without patch\n\n```\nsage: G = TransitiveGroup(21,38)\nsage: S = IntegerVectorsModPermutationGroup(G, max_part=1)\nsage: %time S._cardinality_from_iterator()\nCPU times: user 54.56 s, sys: 0.02 s, total: 54.58 s\nWall time: 54.64 s\n1044\n```\n\nWith patch\n\n```\nsage: G = TransitiveGroup(21,38)\nsage: S = IntegerVectorsModPermutationGroup(G, max_part=1)\nsage: %time S._cardinality_from_iterator()\nCPU times: user 9.36 s, sys: 0.01 s, total: 9.37 s\nWall time: 9.38 s\n1044\n```\n\nSo, yes, it scales well...",
    "created_at": "2012-05-25T21:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56068",
    "user": "https://github.com/simon-king-jena"
}
```

Without patch

```
sage: G = TransitiveGroup(21,38)
sage: S = IntegerVectorsModPermutationGroup(G, max_part=1)
sage: %time S._cardinality_from_iterator()
CPU times: user 54.56 s, sys: 0.02 s, total: 54.58 s
Wall time: 54.64 s
1044
```

With patch

```
sage: G = TransitiveGroup(21,38)
sage: S = IntegerVectorsModPermutationGroup(G, max_part=1)
sage: %time S._cardinality_from_iterator()
CPU times: user 9.36 s, sys: 0.01 s, total: 9.37 s
Wall time: 9.38 s
1044
```

So, yes, it scales well...



---

archive/issue_comments_056069.json:
```json
{
    "body": "Speed-ups and doc fixes",
    "created_at": "2012-05-25T22:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56069",
    "user": "https://github.com/simon-king-jena"
}
```

Speed-ups and doc fixes



---

archive/issue_comments_056070.json:
```json
{
    "body": "Attachment [trac_6812_reviewer.patch](tarball://root/attachments/some-uuid/ticket6812/trac_6812_reviewer.patch) by @simon-king-jena created at 2012-05-25 22:09:35\n\nMy patch is posted.\n\nI hesitate to directly give it a positive review, since I somehow think that my patch is not just a reviewer patch (in spite of its name), because it changes the code non-trivially. So, please have a closer look on it!\n\nApart from the code changes, I went through the doc strings and tried to fix some grammar. But I am not a native speaker - take my changes with a grain of salt...\n\nApply trac_6812_integer_vectors_mod_permgroup.patch trac_6812_reviewer.patch]",
    "created_at": "2012-05-25T22:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56070",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac_6812_reviewer.patch](tarball://root/attachments/some-uuid/ticket6812/trac_6812_reviewer.patch) by @simon-king-jena created at 2012-05-25 22:09:35

My patch is posted.

I hesitate to directly give it a positive review, since I somehow think that my patch is not just a reviewer patch (in spite of its name), because it changes the code non-trivially. So, please have a closer look on it!

Apart from the code changes, I went through the doc strings and tried to fix some grammar. But I am not a native speaker - take my changes with a grain of salt...

Apply trac_6812_integer_vectors_mod_permgroup.patch trac_6812_reviewer.patch]



---

archive/issue_comments_056071.json:
```json
{
    "body": "It seems the patch bot didn't get it.\n\nApply trac_6812_integer_vectors_mod_permgroup.patch trac_6812_reviewer.patch",
    "created_at": "2012-05-25T22:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56071",
    "user": "https://github.com/simon-king-jena"
}
```

It seems the patch bot didn't get it.

Apply trac_6812_integer_vectors_mod_permgroup.patch trac_6812_reviewer.patch



---

archive/issue_comments_056072.json:
```json
{
    "body": "Fixing a corner case, adding a doc test",
    "created_at": "2012-05-26T07:22:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56072",
    "user": "https://github.com/simon-king-jena"
}
```

Fixing a corner case, adding a doc test



---

archive/issue_comments_056073.json:
```json
{
    "body": "Attachment [trac_6812_reviewer2.patch](tarball://root/attachments/some-uuid/ticket6812/trac_6812_reviewer2.patch) by @simon-king-jena created at 2012-05-26 07:26:20\n\nI posted an additional reviewer patch. Namely, in my first patch, I forgot to add a doctest (shame on me), and consequently the code contained a bug: Integer vectores `[1,2,3,1]` and `[1,2,3]` would have compared equal. That' fixed and tested with the second reviewer patch.\n\nFor the record: I give a positive review to Nicolas' patch. My first reviewer patch needs review, I believe. The second patch is trivial enough to be considered a \"real\" reviewer patch.\n\nApply trac_6812_integer_vectors_mod_permgroup.patch trac_6812_reviewer.patch trac_6812_reviewer2.patch",
    "created_at": "2012-05-26T07:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56073",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [trac_6812_reviewer2.patch](tarball://root/attachments/some-uuid/ticket6812/trac_6812_reviewer2.patch) by @simon-king-jena created at 2012-05-26 07:26:20

I posted an additional reviewer patch. Namely, in my first patch, I forgot to add a doctest (shame on me), and consequently the code contained a bug: Integer vectores `[1,2,3,1]` and `[1,2,3]` would have compared equal. That' fixed and tested with the second reviewer patch.

For the record: I give a positive review to Nicolas' patch. My first reviewer patch needs review, I believe. The second patch is trivial enough to be considered a "real" reviewer patch.

Apply trac_6812_integer_vectors_mod_permgroup.patch trac_6812_reviewer.patch trac_6812_reviewer2.patch



---

archive/issue_comments_056074.json:
```json
{
    "body": "I was just double checking everything... You really done a lot of work finally, really much as I expected. My first patch was not so much ready.\n\nAs you posted another reviewer patch, once I will test everything, I will perhaps merge the 3 patches into a final one for the release manager.",
    "created_at": "2012-05-26T07:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56074",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

I was just double checking everything... You really done a lot of work finally, really much as I expected. My first patch was not so much ready.

As you posted another reviewer patch, once I will test everything, I will perhaps merge the 3 patches into a final one for the release manager.



---

archive/issue_comments_056075.json:
```json
{
    "body": "Attachment [trac_6812_integer_vectors_mod_permgroup-final.patch](tarball://root/attachments/some-uuid/ticket6812/trac_6812_integer_vectors_mod_permgroup-final.patch) by nborie created at 2012-05-26 08:41:12\n\nI am completely agree with all corrections and improvements provided by the two reviewer patches from Simon. I just merge them into my first proposition.\n\nThe current implementation pass all my corner cases around invariant theory. All tests pass, the documentation seems good to me and the code looks ready to go. I give the patch a positive review.\n\nThis is a three years old wanted improvement (beginning of my PhD thesis) and Sage changed so much these last three years.... Thanks you Simon for the hours you spent on finalizing this and thanks you Karl for English suggestions/corrections (especially those sent by mail 6 month ago...)\n\napply trac_6812_integer_vectors_mod_permgroup-final.patch",
    "created_at": "2012-05-26T08:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56075",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Attachment [trac_6812_integer_vectors_mod_permgroup-final.patch](tarball://root/attachments/some-uuid/ticket6812/trac_6812_integer_vectors_mod_permgroup-final.patch) by nborie created at 2012-05-26 08:41:12

I am completely agree with all corrections and improvements provided by the two reviewer patches from Simon. I just merge them into my first proposition.

The current implementation pass all my corner cases around invariant theory. All tests pass, the documentation seems good to me and the code looks ready to go. I give the patch a positive review.

This is a three years old wanted improvement (beginning of my PhD thesis) and Sage changed so much these last three years.... Thanks you Simon for the hours you spent on finalizing this and thanks you Karl for English suggestions/corrections (especially those sent by mail 6 month ago...)

apply trac_6812_integer_vectors_mod_permgroup-final.patch



---

archive/issue_comments_056076.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-26T08:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56076",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056077.json:
```json
{
    "body": "I'm adding a very minor review patch for a few issues.  This is an amazing contribution!\n\nAlso, can you fix this?\n\n```\n# User \"sage-combinat script\"\n```\n",
    "created_at": "2012-05-26T15:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56077",
    "user": "https://github.com/kcrisman"
}
```

I'm adding a very minor review patch for a few issues.  This is an amazing contribution!

Also, can you fix this?

```
# User "sage-combinat script"
```




---

archive/issue_comments_056078.json:
```json
{
    "body": "Attachment [trac_6812-reviewer.patch](tarball://root/attachments/some-uuid/ticket6812/trac_6812-reviewer.patch) by @kcrisman created at 2012-05-26 15:41:05\n\nPatchbot apply trac_6812_integer_vectors_mod_permgroup-final.patch and trac_6812-reviewer.patch.",
    "created_at": "2012-05-26T15:41:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56078",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_6812-reviewer.patch](tarball://root/attachments/some-uuid/ticket6812/trac_6812-reviewer.patch) by @kcrisman created at 2012-05-26 15:41:05

Patchbot apply trac_6812_integer_vectors_mod_permgroup-final.patch and trac_6812-reviewer.patch.



---

archive/issue_comments_056079.json:
```json
{
    "body": "Karl reasonably didn't change the status of the ticket. I definitely agree with his patch which fix a lot of typos. Thanks a lot for this reading and the associated patch which applied smoothly on the previous one.\n\nIf needed (or just for convenience), the release manager can ask me merging the two patch, if not\n\napply trac_6812_integer_vectors_mod_permgroup-final.patch trac_6812-reviewer.patch",
    "created_at": "2012-05-29T11:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56079",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```

Karl reasonably didn't change the status of the ticket. I definitely agree with his patch which fix a lot of typos. Thanks a lot for this reading and the associated patch which applied smoothly on the previous one.

If needed (or just for convenience), the release manager can ask me merging the two patch, if not

apply trac_6812_integer_vectors_mod_permgroup-final.patch trac_6812-reviewer.patch



---

archive/issue_events_007046.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-06-14T06:37:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6812#event-7046"
}
```



---

archive/issue_comments_056080.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-06-14T06:37:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56080",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_056081.json:
```json
{
    "body": "Congratulations Nicolas!\n\nAnd thanks you all for getting this great new feature into Sage.",
    "created_at": "2012-06-15T20:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6812#issuecomment-56081",
    "user": "https://github.com/nthiery"
}
```

Congratulations Nicolas!

And thanks you all for getting this great new feature into Sage.
