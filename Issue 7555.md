# Issue 7555: Fix Cayley tables, add operation tables

archive/issues_007555.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  jason dimpase nthiery\n\nKeywords: cayley table, operation table\n\nCayley tables for permutation groups are broken, see #7340.\n\nFor other finite algebraic structures, it would be useful for educational purposes to have tables for whatever operation(s) may be present.\n\nText file included here provides a class that creates a Cayley table object, it can be generalized to provide a similar table for any object with an addition or multiplication - general groups and rings would be the first places to use it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7555\n\n",
    "created_at": "2009-11-29T18:55:58Z",
    "labels": [
        "algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Fix Cayley tables, add operation tables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7555",
    "user": "rbeezer"
}
```
Assignee: AlexGhitza

CC:  jason dimpase nthiery

Keywords: cayley table, operation table

Cayley tables for permutation groups are broken, see #7340.

For other finite algebraic structures, it would be useful for educational purposes to have tables for whatever operation(s) may be present.

Text file included here provides a class that creates a Cayley table object, it can be generalized to provide a similar table for any object with an addition or multiplication - general groups and rings would be the first places to use it.

Issue created by migration from https://trac.sagemath.org/ticket/7555





---

archive/issue_comments_064214.json:
```json
{
    "body": "Attachment [trac_7555_cayley_table.txt](tarball://root/attachments/some-uuid/ticket7555/trac_7555_cayley_table.txt) by rbeezer created at 2009-11-29 18:57:39\n\nExperimental Cayley table class, cut/paste into a notebook cell",
    "created_at": "2009-11-29T18:57:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64214",
    "user": "rbeezer"
}
```

Attachment [trac_7555_cayley_table.txt](tarball://root/attachments/some-uuid/ticket7555/trac_7555_cayley_table.txt) by rbeezer created at 2009-11-29 18:57:39

Experimental Cayley table class, cut/paste into a notebook cell



---

archive/issue_comments_064215.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-11-29T18:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64215",
    "user": "rbeezer"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_064216.json:
```json
{
    "body": "Patch contains a new class, `OperationTable`.\n\nThis is meant for educational applications, and is unlikely to be used for anything much bigger than can be displayed on a screen or a sheet of paper.  So the speed (it is a bit slow) is not a concern.\n\nSince it only requires a binary operation, I created the groupoids directory, based on the existence of  a category by the same name.\n\nNext thing will be an application of this class to generic groups, fixing #7340.  There are stubs left here for methods to create color and grayscale graphics of the tables.",
    "created_at": "2010-03-15T23:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64216",
    "user": "rbeezer"
}
```

Patch contains a new class, `OperationTable`.

This is meant for educational applications, and is unlikely to be used for anything much bigger than can be displayed on a screen or a sheet of paper.  So the speed (it is a bit slow) is not a concern.

Since it only requires a binary operation, I created the groupoids directory, based on the existence of  a category by the same name.

Next thing will be an application of this class to generic groups, fixing #7340.  There are stubs left here for methods to create color and grayscale graphics of the tables.



---

archive/issue_comments_064217.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-15T23:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64217",
    "user": "rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064218.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-17T01:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64218",
    "user": "rbeezer"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064219.json:
```json
{
    "body": "It seems a better place to place this is within the categories framework, making it available automatically in a large number of situations.  So it is being reworked right now.  The main routine won't change much at all, so time spent reviewing largely won't need to be redone.  But you'll want to wait on testing.  I'll have an updated patch soon.",
    "created_at": "2010-03-17T01:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64219",
    "user": "rbeezer"
}
```

It seems a better place to place this is within the categories framework, making it available automatically in a large number of situations.  So it is being reworked right now.  The main routine won't change much at all, so time spent reviewing largely won't need to be redone.  But you'll want to wait on testing.  I'll have an updated patch soon.



---

archive/issue_comments_064220.json:
```json
{
    "body": "Attachment [trac_7555_operation_table.patch](tarball://root/attachments/some-uuid/ticket7555/trac_7555_operation_table.patch) by rbeezer created at 2010-03-18 04:44:07",
    "created_at": "2010-03-18T04:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64220",
    "user": "rbeezer"
}
```

Attachment [trac_7555_operation_table.patch](tarball://root/attachments/some-uuid/ticket7555/trac_7555_operation_table.patch) by rbeezer created at 2010-03-18 04:44:07



---

archive/issue_comments_064221.json:
```json
{
    "body": "I've tied the new `OperationTable` class into the categories framework as a multiplication table for Semigroups and as an addition table for Commutative Additive Semigroups.  I've also added it as a Cayley table for groups, since I'd like to later expand this somewhat to take advantage of the extra structure in groups.\n\nThe old Cayley table was used to build Latin squares.  I believe the behavior now with the new cayley table will be identical - IF the identity is the first element of the group.\n\nHad a hard time constructing a nontrivial finite additive semigroup, so the documentation there is barebones right now.\n\nAs more structures become available in the categories this should be all ready to go, unchanged.  Right now it already makes the multiplication table available for all groups, rather than just permutation groups.",
    "created_at": "2010-03-18T04:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64221",
    "user": "rbeezer"
}
```

I've tied the new `OperationTable` class into the categories framework as a multiplication table for Semigroups and as an addition table for Commutative Additive Semigroups.  I've also added it as a Cayley table for groups, since I'd like to later expand this somewhat to take advantage of the extra structure in groups.

The old Cayley table was used to build Latin squares.  I believe the behavior now with the new cayley table will be identical - IF the identity is the first element of the group.

Had a hard time constructing a nontrivial finite additive semigroup, so the documentation there is barebones right now.

As more structures become available in the categories this should be all ready to go, unchanged.  Right now it already makes the multiplication table available for all groups, rather than just permutation groups.



---

archive/issue_comments_064222.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-18T04:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64222",
    "user": "rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064223.json:
```json
{
    "body": "Hi Rob!\n\nVery nice patch! I'll sure use it soon :-)\n\nReplying to [comment:4 rbeezer]:\n> I've tied the new `OperationTable` class into the categories framework as a multiplication table for Semigroups and as an addition table for Commutative Additive Semigroups.  I've also added it as a Cayley table for groups, since I'd like to later expand this somewhat to take advantage of the extra structure in groups.\n\nThat's the way to go!\n\nOut of curiosity: what are the specific features of groups that could\nbe useful?\n\n> The old Cayley table was used to build Latin squares.  I believe the behavior now with the new cayley table will be identical - IF the identity is the first element of the group.\n\nIsn't that more \"if the elements are listed in the same order\"?\n\n> Had a hard time constructing a nontrivial finite additive semigroup, so the documentation there is barebones right now.\n\nIn waiting for something better, you may want to include a test with a\ncommutative additive group like:\n\n\n```\n    sage: Z5 = IntegerModRing(5)\n```\n\n\nBy the way:\n\n\n```\n    sage: from sage.categories.examples.commutative_additive_monoids import FreeCommutativeAdditiveMonoid\n    sage: F=FreeCommutativeAdditiveMonoid(('a', 'b'))\n```\n\n\nIs better constructed as::\n\n\n```\n    sage: F = CommutativeAdditiveMonoids().example(('a','b'))\n```\n\n\nAnd actually should eventually become:\n\n\n```\n    sage: F = CommutativeAdditiveMonoids().free(('a','b'))\n```\n\n\n\n\n> As more structures become available in the categories this should be all ready to go, unchanged.  Right now it already makes the multiplication table available for all groups, rather than just permutation groups.\n\nAnd for semigroups, which I am very interested in :-) Actually, it\ncould be generalized to Magmas() (just a binary operation, not\nnecessarily associative) once we have this category.\n\nI browsed quickly through the patch. Here are some suggestions for\nimprovements:\n\n- Pass the operation as a function (like operator.mul)\n  Then OperationTable will be useful for any binary operation\n\n- For addition or multiplication, the user won't call directly\n  OperationTable, but rather use S.addition_table() /\n  S.multiplication_table(). So I would remove the guessing\n  feature, and make ``operation`` a required parameter.\n\n  (and possibly add an operation_symbol = \"+\" option?)\n\n- Remove the restriction for the empty operation table, unless\n  absolutely necessary.\n\n- comparisons by < do not seem that meaningful. I would just test\n  equality of operation tables. Then, there are two possible\n  semantics:\n\n   - two tables are equal if they correspond to the same algebraic\n     structure, operation and element order\n\n   - two tables are equal if they are equal as \"functions\", i.e. the\n     two operations both map the i-th and j-th element to the same\n     k-th element (that's what the current comparison by list of ints\n     does)\n\n  I don't have a preference yet.\n\nNote: in many other places, we will need a class for matrices with row\nand indices indexed by any objects, and not just integers. This is a\ngood first step, and it will remain to extract a more general super\nclass. To prepare the ground, I would suggest the following:\n\n   - Rename list to index_set, or maybe row_index_set, to avoid\n   confusion with the usual semantic of list.\n\n   - dict is a bit vague. It is related to ranking (see EnumeratedSets).\n   Maybe row_rank, or row_rank_dict.\n\nIs ascii_table really needed? I would tend to just implement _repr_,\nand not teach the user another specific way of getting the\nrepresentation.\n\nBy the way: several other Sage objects (like matrices, partitions,\n...) are starting to have a 2d ascii art representation.  We should\nstandardize the handling of those.\n\nPlease add (and use?) a __getitem__ method. It will make\nOperationTable not only useful for printing, but also as a useful data\nstructure for computations.\n\nThe last issue is the name of the methods. When we discussed this at\nSage Days 15, we had settled for P.product(x,y) and P.summation(x,y)\nas names for the two operations (the choice was not that clear, and\nthe prevailing argument has been consistency with prod and sum\nrespectively, and naming the *result* of the operation on x and y)\n[1]. Consistency would then call for P.product_table and\nP.summation_table, though that is not so nice.\n\n\n[1] http://trac.sagemath.org/sage_trac/wiki/CategoriesRoadMap\n\nCheers,\n\t\t\t\tNicolas",
    "created_at": "2010-03-18T11:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64223",
    "user": "nthiery"
}
```

Hi Rob!

Very nice patch! I'll sure use it soon :-)

Replying to [comment:4 rbeezer]:
> I've tied the new `OperationTable` class into the categories framework as a multiplication table for Semigroups and as an addition table for Commutative Additive Semigroups.  I've also added it as a Cayley table for groups, since I'd like to later expand this somewhat to take advantage of the extra structure in groups.

That's the way to go!

Out of curiosity: what are the specific features of groups that could
be useful?

> The old Cayley table was used to build Latin squares.  I believe the behavior now with the new cayley table will be identical - IF the identity is the first element of the group.

Isn't that more "if the elements are listed in the same order"?

> Had a hard time constructing a nontrivial finite additive semigroup, so the documentation there is barebones right now.

In waiting for something better, you may want to include a test with a
commutative additive group like:


```
    sage: Z5 = IntegerModRing(5)
```


By the way:


```
    sage: from sage.categories.examples.commutative_additive_monoids import FreeCommutativeAdditiveMonoid
    sage: F=FreeCommutativeAdditiveMonoid(('a', 'b'))
```


Is better constructed as::


```
    sage: F = CommutativeAdditiveMonoids().example(('a','b'))
```


And actually should eventually become:


```
    sage: F = CommutativeAdditiveMonoids().free(('a','b'))
```




> As more structures become available in the categories this should be all ready to go, unchanged.  Right now it already makes the multiplication table available for all groups, rather than just permutation groups.

And for semigroups, which I am very interested in :-) Actually, it
could be generalized to Magmas() (just a binary operation, not
necessarily associative) once we have this category.

I browsed quickly through the patch. Here are some suggestions for
improvements:

- Pass the operation as a function (like operator.mul)
  Then OperationTable will be useful for any binary operation

- For addition or multiplication, the user won't call directly
  OperationTable, but rather use S.addition_table() /
  S.multiplication_table(). So I would remove the guessing
  feature, and make ``operation`` a required parameter.

  (and possibly add an operation_symbol = "+" option?)

- Remove the restriction for the empty operation table, unless
  absolutely necessary.

- comparisons by < do not seem that meaningful. I would just test
  equality of operation tables. Then, there are two possible
  semantics:

   - two tables are equal if they correspond to the same algebraic
     structure, operation and element order

   - two tables are equal if they are equal as "functions", i.e. the
     two operations both map the i-th and j-th element to the same
     k-th element (that's what the current comparison by list of ints
     does)

  I don't have a preference yet.

Note: in many other places, we will need a class for matrices with row
and indices indexed by any objects, and not just integers. This is a
good first step, and it will remain to extract a more general super
class. To prepare the ground, I would suggest the following:

   - Rename list to index_set, or maybe row_index_set, to avoid
   confusion with the usual semantic of list.

   - dict is a bit vague. It is related to ranking (see EnumeratedSets).
   Maybe row_rank, or row_rank_dict.

Is ascii_table really needed? I would tend to just implement _repr_,
and not teach the user another specific way of getting the
representation.

By the way: several other Sage objects (like matrices, partitions,
...) are starting to have a 2d ascii art representation.  We should
standardize the handling of those.

Please add (and use?) a __getitem__ method. It will make
OperationTable not only useful for printing, but also as a useful data
structure for computations.

The last issue is the name of the methods. When we discussed this at
Sage Days 15, we had settled for P.product(x,y) and P.summation(x,y)
as names for the two operations (the choice was not that clear, and
the prevailing argument has been consistency with prod and sum
respectively, and naming the *result* of the operation on x and y)
[1]. Consistency would then call for P.product_table and
P.summation_table, though that is not so nice.


[1] http://trac.sagemath.org/sage_trac/wiki/CategoriesRoadMap

Cheers,
				Nicolas



---

archive/issue_comments_064224.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-18T11:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64224",
    "user": "nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064225.json:
```json
{
    "body": "Replying to [comment:5 nthiery]:\n\nDear Nicolas,\n\nI knew you'd have some comments!  Thanks for all the helpful advice and suggestions, on categories, and in general.\n\n> That's the way to go!\n\nYes, it certainly is.  ;-)\n\n> Out of curiosity: what are the specific features of groups that could\n> be useful?\n\nGrab a normal subgroup, as close to size sqrt(n) as you can get (perhaps automatically), then order elements in bunches as cosets.  You can sometimes see the quotient structure in the table, especially if done graphically.  But maybe this belongs higher up the hierarchy?\n\n> > The old Cayley table was used to build Latin squares.  I believe the behavior now with the new cayley table will be identical - IF the identity is the first element of the group.\n>\n> Isn't that more \"if the elements are listed in the same order\"?\n\nThat would of course be sufficient.  The code is a bit cryptic, but it appeared to me that if the identity was first, then the elements were numbered in the order they were listed.  But I didn't study it that carefully, since I was going to pull it out anyway.  Hopefully the change doesn't cause anybody any trouble.\n\n> In waiting for something better, you may want to include a test with a\n> commutative additive group like:\n>\n> {{{\n>     sage: Z5 = IntegerModRing(5)\n> }}}\n\nI tried this repeatedly.  You get `addition_table` with tab completion, but then\n\n\n```\nAttributeError: 'IntegerModRing_generic' object has no attribute 'addition_table'\n```\n\n\nwhen you try to execute it. Similarly for `cayley_graph`.  And `FiniteField`s I just assumed rings were not plugged-in yet.  Is there an easy fix?\n\n\n> Is better constructed as::\n>\n> {{{\n>     sage: F = CommutativeAdditiveMonoids().example(('a','b'))\n> }}}\n\nWill do.\n\n> Actually, it\n> could be generalized to Magmas() (just a binary operation, not\n> necessarily associative) once we have this category.\n\nYes, I wanted this category.  Will there be two - additive and multiplicative?  Also called \"groupoids\" if we want avoid confusion with the CAS.  Doing `search_src` on \"magma\" turns up lots of things related to the program, not the structure.\n\n> I browsed quickly through the patch. Here are some suggestions for\n> improvements:\n>\n>  - Pass the operation as a function (like operator.mul)\n>    Then OperationTable will be useful for any binary operation\n>\n>  - For addition or multiplication, the user won't call directly\n>    OperationTable, but rather use S.addition_table() /\n>    S.multiplication_table(). So I would remove the guessing\n>    feature, and make ``operation`` a required parameter.\n\nGuessing was a \"feature\" before I found categories.  It'll go away.\n\n>    (and possibly add an operation_symbol = \"+\" option?)\n>\n>  - Remove the restriction for the empty operation table, unless\n>    absolutely necessary.\n\nDidn't check, but thought I'd have to add lots more logic to handle this case.  Maybe not.\n\n>  - Rename list to index_set, or maybe row_index_set, to avoid\n>    confusion with the usual semantic of list.\n\nHow about \"headings\"?\n\n>  - dict is a bit vague. It is related to ranking (see EnumeratedSets).\n>    Maybe row_rank, or row_rank_dict.\n\nThe returned dictionary pairs elements with their names.  Names can be any string, not just integers, so this doesn't feel like a ranking or an enumerated set to me.  It's more of a translation table.  So maybe there is a better name.  \"translation\"?  But I think rank would be confusing.\n\n> Is ascii_table really needed? I would tend to just implement _repr_,\n> and not teach the user another specific way of getting the\n> representation.\n\nOK\n\n> By the way: several other Sage objects (like matrices, partitions,\n> ...) are starting to have a 2d ascii art representation.  We should\n> standardize the handling of those.\n\nYes, I did much the same thing once already for Sudoku puzzles.\n\n> Please add (and use?) a __getitem__ method. It will make\n> OperationTable not only useful for printing, but also as a useful data\n> structure for computations.\n\nNot sure how you mean this to work?  If T is a table, then T[i]=<element>, or T[i,j]=<table-entry>??  More precisely,.....\n\n> The last issue is the name of the methods. When we discussed this at\n> Sage Days 15, we had settled for P.product(x,y) and P.summation(x,y)\n> as names for the two operations (the choice was not that clear, and\n> the prevailing argument has been consistency with prod and sum\n> respectively, and naming the *result* of the operation on x and y)\n> [1]. Consistency would then call for P.product_table and\n> P.summation_table, though that is not so nice.\n\nI really had students in mind as I built this, though everybody might find it useful.  \"product\" is OK, \"summation\" sounds like more than two terms.  In any event, what about having both (ie product and multiplication, summation and addition)?  I know people don't like this, and it clutters up tab-completion.  Permutation groups had `multiplication_table` as an alias for `cayley_table`.  I'd really like this to be dead-obvious for the beginner finding their way in Sage.\n\nThanks again for the interest and help!\n\nRob",
    "created_at": "2010-03-18T18:01:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64225",
    "user": "rbeezer"
}
```

Replying to [comment:5 nthiery]:

Dear Nicolas,

I knew you'd have some comments!  Thanks for all the helpful advice and suggestions, on categories, and in general.

> That's the way to go!

Yes, it certainly is.  ;-)

> Out of curiosity: what are the specific features of groups that could
> be useful?

Grab a normal subgroup, as close to size sqrt(n) as you can get (perhaps automatically), then order elements in bunches as cosets.  You can sometimes see the quotient structure in the table, especially if done graphically.  But maybe this belongs higher up the hierarchy?

> > The old Cayley table was used to build Latin squares.  I believe the behavior now with the new cayley table will be identical - IF the identity is the first element of the group.
>
> Isn't that more "if the elements are listed in the same order"?

That would of course be sufficient.  The code is a bit cryptic, but it appeared to me that if the identity was first, then the elements were numbered in the order they were listed.  But I didn't study it that carefully, since I was going to pull it out anyway.  Hopefully the change doesn't cause anybody any trouble.

> In waiting for something better, you may want to include a test with a
> commutative additive group like:
>
> {{{
>     sage: Z5 = IntegerModRing(5)
> }}}

I tried this repeatedly.  You get `addition_table` with tab completion, but then


```
AttributeError: 'IntegerModRing_generic' object has no attribute 'addition_table'
```


when you try to execute it. Similarly for `cayley_graph`.  And `FiniteField`s I just assumed rings were not plugged-in yet.  Is there an easy fix?


> Is better constructed as::
>
> {{{
>     sage: F = CommutativeAdditiveMonoids().example(('a','b'))
> }}}

Will do.

> Actually, it
> could be generalized to Magmas() (just a binary operation, not
> necessarily associative) once we have this category.

Yes, I wanted this category.  Will there be two - additive and multiplicative?  Also called "groupoids" if we want avoid confusion with the CAS.  Doing `search_src` on "magma" turns up lots of things related to the program, not the structure.

> I browsed quickly through the patch. Here are some suggestions for
> improvements:
>
>  - Pass the operation as a function (like operator.mul)
>    Then OperationTable will be useful for any binary operation
>
>  - For addition or multiplication, the user won't call directly
>    OperationTable, but rather use S.addition_table() /
>    S.multiplication_table(). So I would remove the guessing
>    feature, and make ``operation`` a required parameter.

Guessing was a "feature" before I found categories.  It'll go away.

>    (and possibly add an operation_symbol = "+" option?)
>
>  - Remove the restriction for the empty operation table, unless
>    absolutely necessary.

Didn't check, but thought I'd have to add lots more logic to handle this case.  Maybe not.

>  - Rename list to index_set, or maybe row_index_set, to avoid
>    confusion with the usual semantic of list.

How about "headings"?

>  - dict is a bit vague. It is related to ranking (see EnumeratedSets).
>    Maybe row_rank, or row_rank_dict.

The returned dictionary pairs elements with their names.  Names can be any string, not just integers, so this doesn't feel like a ranking or an enumerated set to me.  It's more of a translation table.  So maybe there is a better name.  "translation"?  But I think rank would be confusing.

> Is ascii_table really needed? I would tend to just implement _repr_,
> and not teach the user another specific way of getting the
> representation.

OK

> By the way: several other Sage objects (like matrices, partitions,
> ...) are starting to have a 2d ascii art representation.  We should
> standardize the handling of those.

Yes, I did much the same thing once already for Sudoku puzzles.

> Please add (and use?) a __getitem__ method. It will make
> OperationTable not only useful for printing, but also as a useful data
> structure for computations.

Not sure how you mean this to work?  If T is a table, then T[i]=<element>, or T[i,j]=<table-entry>??  More precisely,.....

> The last issue is the name of the methods. When we discussed this at
> Sage Days 15, we had settled for P.product(x,y) and P.summation(x,y)
> as names for the two operations (the choice was not that clear, and
> the prevailing argument has been consistency with prod and sum
> respectively, and naming the *result* of the operation on x and y)
> [1]. Consistency would then call for P.product_table and
> P.summation_table, though that is not so nice.

I really had students in mind as I built this, though everybody might find it useful.  "product" is OK, "summation" sounds like more than two terms.  In any event, what about having both (ie product and multiplication, summation and addition)?  I know people don't like this, and it clutters up tab-completion.  Permutation groups had `multiplication_table` as an alias for `cayley_table`.  I'd really like this to be dead-obvious for the beginner finding their way in Sage.

Thanks again for the interest and help!

Rob



---

archive/issue_comments_064226.json:
```json
{
    "body": "Hi!\n\nReplying to [comment:7 rbeezer]:\n> I knew you'd have some comments!  Thanks for all the helpful advice and suggestions, on categories, and in general.\n\n:-)\n\n> > Out of curiosity: what are the specific features of groups that could\n> > be useful?\n> Grab a normal subgroup, as close to size sqrt(n) as you can get (perhaps automatically), then order elements in bunches as cosets.  You can sometimes see the quotient structure in the table, especially if done graphically.  But maybe this belongs higher up the hierarchy?\n\nOk. Or maybe it can be just a helper function for how to list the\nelements by default, which would be overridden in Groups.\n\n> > In waiting for something better, you may want to include a test with a\n> > commutative additive group like:\n> >\n> > {{{\n> >     sage: Z5 = IntegerModRing(5)\n> > }}}\n> \n> I tried this repeatedly.  You get `addition_table` with tab completion, but then\n> \n> {{{\n> AttributeError: 'IntegerModRing_generic' object has no attribute 'addition_table'\n> }}}\n> \n> when you try to execute it. Similarly for `cayley_graph`.  And `FiniteField`s I just assumed rings were not plugged-in yet.  Is there an easy fix?\n\nSee #8562, which you are very welcome to review :-) IntegerModRing's\nwere not yet categorified. I'll upload a patch after running the full\ntests on it.\n\n> > Actually, it could be generalized to Magmas() (just a binary\n> > operation, not necessarily associative) once we have this\n> > category.\n> \n> Yes, I wanted this category.  Will there be two - additive and multiplicative?  Also called \"groupoids\" if we want avoid confusion with the CAS.  Doing `search_src` on \"magma\" turns up lots of things related to the program, not the structure.\n\nWith groupds, there is a possible confusion with the other use of\ngroupoids (http://en.wikipedia.org/wiki/Groupoid) which is about\nhaving a partially defined operation; but with associativity holding\nwhenever meaningful.\n\nThanks to the s, there is no naming clash between Magmas and Magma, so\nthat's probably fine (http://en.wikipedia.org/wiki/Magma_%28algebra%29)\n\n> Guessing was a \"feature\" before I found categories.  It'll go away.\n\nGreat.\n\n> >    (and possibly add an operation_symbol = \"+\" option?)\n> >\n> >  - Remove the restriction for the empty operation table, unless\n> >    absolutely necessary.\n> \n> Didn't check, but thought I'd have to add lots more logic to handle this case.  Maybe not.\n\nOk; let me know how it goes.\n\n> >  - Rename list to index_set, or maybe row_index_set, to avoid\n> >    confusion with the usual semantic of list.\n> \n> How about \"headings\"?\n\nThinking twice about it, I vote for m.column_keys() / m.row_keys() for\nconsistency with the d.keys() of a dictionary (which we also use for\nFamily's, and CombinatorialFreeModule elements).\n\n> >  - dict is a bit vague. It is related to ranking (see EnumeratedSets).\n> >    Maybe row_rank, or row_rank_dict.\n> \n\n> The returned dictionary pairs elements with their names.\n\nAh, ok, sorry; I thought it would map an element to its position in\nthe list.\n\n>  So maybe there is a better name.  \"translation\"?\n\nnames_of_elements? or just names? labels? element_labels?\n\n> > By the way: several other Sage objects (like matrices, partitions,\n> > ...) are starting to have a 2d ascii art representation.  We should\n> > standardize the handling of those.\n> \n> Yes, I did much the same thing once already for Sudoku puzzles.\n\nAnother coming soon usage will be character tables.\n\n> > Please add (and use?) a __getitem__ method. It will make\n> > OperationTable not only useful for printing, but also as a useful data\n> > structure for computations.\n> \n> Not sure how you mean this to work?  If T is a table, then T[i]=<element>, or T[i,j]=<table-entry>??  More precisely,.....\n\nThey multiplication table looks very much like a matrix, so one would\nwant, for u,v elements (not names/labels) of the group to have m[u,v]\nbe u*v.\n\n> I really had students in mind as I built this, though everybody might find it useful.  \"product\" is OK, \"summation\" sounds like more than two terms.  In any event, what about having both (ie product and multiplication, summation and addition)?  I know people don't like this, and it clutters up tab-completion.  Permutation groups had `multiplication_table` as an alias for `cayley_table`.  I'd really like this to be dead-obvious for the beginner finding their way in Sage.\n\nYeah, hard point. multiplication / addition is consistent with __mul__\nand __add__. So that's probably ok without cluttering the namespace.\n\nBy the way: congrats on being essentially the first non Sage-Combinat\ncontributer to categories :-) How did it go?\n\nCheers,\n\t\t\t\tNicolas",
    "created_at": "2010-03-19T22:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64226",
    "user": "nthiery"
}
```

Hi!

Replying to [comment:7 rbeezer]:
> I knew you'd have some comments!  Thanks for all the helpful advice and suggestions, on categories, and in general.

:-)

> > Out of curiosity: what are the specific features of groups that could
> > be useful?
> Grab a normal subgroup, as close to size sqrt(n) as you can get (perhaps automatically), then order elements in bunches as cosets.  You can sometimes see the quotient structure in the table, especially if done graphically.  But maybe this belongs higher up the hierarchy?

Ok. Or maybe it can be just a helper function for how to list the
elements by default, which would be overridden in Groups.

> > In waiting for something better, you may want to include a test with a
> > commutative additive group like:
> >
> > {{{
> >     sage: Z5 = IntegerModRing(5)
> > }}}
> 
> I tried this repeatedly.  You get `addition_table` with tab completion, but then
> 
> {{{
> AttributeError: 'IntegerModRing_generic' object has no attribute 'addition_table'
> }}}
> 
> when you try to execute it. Similarly for `cayley_graph`.  And `FiniteField`s I just assumed rings were not plugged-in yet.  Is there an easy fix?

See #8562, which you are very welcome to review :-) IntegerModRing's
were not yet categorified. I'll upload a patch after running the full
tests on it.

> > Actually, it could be generalized to Magmas() (just a binary
> > operation, not necessarily associative) once we have this
> > category.
> 
> Yes, I wanted this category.  Will there be two - additive and multiplicative?  Also called "groupoids" if we want avoid confusion with the CAS.  Doing `search_src` on "magma" turns up lots of things related to the program, not the structure.

With groupds, there is a possible confusion with the other use of
groupoids (http://en.wikipedia.org/wiki/Groupoid) which is about
having a partially defined operation; but with associativity holding
whenever meaningful.

Thanks to the s, there is no naming clash between Magmas and Magma, so
that's probably fine (http://en.wikipedia.org/wiki/Magma_%28algebra%29)

> Guessing was a "feature" before I found categories.  It'll go away.

Great.

> >    (and possibly add an operation_symbol = "+" option?)
> >
> >  - Remove the restriction for the empty operation table, unless
> >    absolutely necessary.
> 
> Didn't check, but thought I'd have to add lots more logic to handle this case.  Maybe not.

Ok; let me know how it goes.

> >  - Rename list to index_set, or maybe row_index_set, to avoid
> >    confusion with the usual semantic of list.
> 
> How about "headings"?

Thinking twice about it, I vote for m.column_keys() / m.row_keys() for
consistency with the d.keys() of a dictionary (which we also use for
Family's, and CombinatorialFreeModule elements).

> >  - dict is a bit vague. It is related to ranking (see EnumeratedSets).
> >    Maybe row_rank, or row_rank_dict.
> 

> The returned dictionary pairs elements with their names.

Ah, ok, sorry; I thought it would map an element to its position in
the list.

>  So maybe there is a better name.  "translation"?

names_of_elements? or just names? labels? element_labels?

> > By the way: several other Sage objects (like matrices, partitions,
> > ...) are starting to have a 2d ascii art representation.  We should
> > standardize the handling of those.
> 
> Yes, I did much the same thing once already for Sudoku puzzles.

Another coming soon usage will be character tables.

> > Please add (and use?) a __getitem__ method. It will make
> > OperationTable not only useful for printing, but also as a useful data
> > structure for computations.
> 
> Not sure how you mean this to work?  If T is a table, then T[i]=<element>, or T[i,j]=<table-entry>??  More precisely,.....

They multiplication table looks very much like a matrix, so one would
want, for u,v elements (not names/labels) of the group to have m[u,v]
be u*v.

> I really had students in mind as I built this, though everybody might find it useful.  "product" is OK, "summation" sounds like more than two terms.  In any event, what about having both (ie product and multiplication, summation and addition)?  I know people don't like this, and it clutters up tab-completion.  Permutation groups had `multiplication_table` as an alias for `cayley_table`.  I'd really like this to be dead-obvious for the beginner finding their way in Sage.

Yeah, hard point. multiplication / addition is consistent with __mul__
and __add__. So that's probably ok without cluttering the namespace.

By the way: congrats on being essentially the first non Sage-Combinat
contributer to categories :-) How did it go?

Cheers,
				Nicolas



---

archive/issue_comments_064227.json:
```json
{
    "body": "Hi Nicolas,\n\nBeen working most of the day straightening this up.\n\nAllowing more general operations is a big improvement.  See example of table of commutators of a finite group once I get a patch up.  ;-)\n\n> Ok. Or maybe it can be just a helper function for how to list the\n> elements by default, which would be overridden in Groups.\n\nI'll include a note in the source to this effect.\n\n> See #8562, which you are very welcome to review :-) IntegerModRing's\n> were not yet categorified. I'll upload a patch after running the full\n> tests on it.\n\nAah - that answers lots of questions.  Thanks.  \"categorified\"??  Your English is excellent, but that is pretty bad.  ;-) ;-)  ;-)  (But it was I might have said too).\n\n> > > Actually, it could be generalized to Magmas() (just a binary\n> > > operation, not necessarily associative) once we have this\n> > > category.\n> > \n> > Yes, I wanted this category.  Will there be two - additive and multiplicative?  Also called \"groupoids\" if we want avoid confusion with the CAS.  Doing `search_src` on \"magma\" turns up lots of things related to the program, not the structure.\n> \n> With groupds, there is a possible confusion with the other use of\n> groupoids (http://en.wikipedia.org/wiki/Groupoid) which is about\n> having a partially defined operation; but with associativity holding\n> whenever meaningful.\n> \n> Thanks to the s, there is no naming clash between Magmas and Magma, so\n> that's probably fine (http://en.wikipedia.org/wiki/Magma_%28algebra%29)\n\nGot it.\n\n> > Didn't check, but thought I'd have to add lots more logic to handle this case.  Maybe not.\n> \n> Ok; let me know how it goes.\n\nNot too bad.  Empty latex table is nice, empty ascii table is so-so, but not worth anymore effort.\n\n> > >  - Rename list to index_set, or maybe row_index_set, to avoid\n> > >    confusion with the usual semantic of list.\n> > \n> > How about \"headings\"?\n> \n> Thinking twice about it, I vote for m.column_keys() / m.row_keys() for\n> consistency with the d.keys() of a dictionary (which we also use for\n> Family's, and CombinatorialFreeModule elements).\n\nI did index_set.  ;-(\n\n> > >  - dict is a bit vague. It is related to ranking (see EnumeratedSets).\n> > >    Maybe row_rank, or row_rank_dict.\n> > \n> \n> > The returned dictionary pairs elements with their names.\n> \n> Ah, ok, sorry; I thought it would map an element to its position in\n> the list.\n> \n> >  So maybe there is a better name.  \"translation\"?\n> \n> names_of_elements? or just names? labels? element_labels?\n\nUsed translation.  :-(\n\n\n> They multiplication table looks very much like a matrix, so one would\n> want, for u,v elements (not names/labels) of the group to have m[u,v]\n> be u*v.\n\nOK, that should be easy.\n\n> Yeah, hard point. multiplication / addition is consistent with __mul__\n> and __add__. So that's probably ok without cluttering the namespace.\n> \n> By the way: congrats on being essentially the first non Sage-Combinat\n> contributer to categories :-) How did it go?\n\nNice.  I like it.  I'm a fan.  And your ring patch will help me recognize when/how categorification happens.\n\nI'm running out of time on this, it's semester break this week, so I'll throw something up soon.\n\nRob",
    "created_at": "2010-03-19T22:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64227",
    "user": "rbeezer"
}
```

Hi Nicolas,

Been working most of the day straightening this up.

Allowing more general operations is a big improvement.  See example of table of commutators of a finite group once I get a patch up.  ;-)

> Ok. Or maybe it can be just a helper function for how to list the
> elements by default, which would be overridden in Groups.

I'll include a note in the source to this effect.

> See #8562, which you are very welcome to review :-) IntegerModRing's
> were not yet categorified. I'll upload a patch after running the full
> tests on it.

Aah - that answers lots of questions.  Thanks.  "categorified"??  Your English is excellent, but that is pretty bad.  ;-) ;-)  ;-)  (But it was I might have said too).

> > > Actually, it could be generalized to Magmas() (just a binary
> > > operation, not necessarily associative) once we have this
> > > category.
> > 
> > Yes, I wanted this category.  Will there be two - additive and multiplicative?  Also called "groupoids" if we want avoid confusion with the CAS.  Doing `search_src` on "magma" turns up lots of things related to the program, not the structure.
> 
> With groupds, there is a possible confusion with the other use of
> groupoids (http://en.wikipedia.org/wiki/Groupoid) which is about
> having a partially defined operation; but with associativity holding
> whenever meaningful.
> 
> Thanks to the s, there is no naming clash between Magmas and Magma, so
> that's probably fine (http://en.wikipedia.org/wiki/Magma_%28algebra%29)

Got it.

> > Didn't check, but thought I'd have to add lots more logic to handle this case.  Maybe not.
> 
> Ok; let me know how it goes.

Not too bad.  Empty latex table is nice, empty ascii table is so-so, but not worth anymore effort.

> > >  - Rename list to index_set, or maybe row_index_set, to avoid
> > >    confusion with the usual semantic of list.
> > 
> > How about "headings"?
> 
> Thinking twice about it, I vote for m.column_keys() / m.row_keys() for
> consistency with the d.keys() of a dictionary (which we also use for
> Family's, and CombinatorialFreeModule elements).

I did index_set.  ;-(

> > >  - dict is a bit vague. It is related to ranking (see EnumeratedSets).
> > >    Maybe row_rank, or row_rank_dict.
> > 
> 
> > The returned dictionary pairs elements with their names.
> 
> Ah, ok, sorry; I thought it would map an element to its position in
> the list.
> 
> >  So maybe there is a better name.  "translation"?
> 
> names_of_elements? or just names? labels? element_labels?

Used translation.  :-(


> They multiplication table looks very much like a matrix, so one would
> want, for u,v elements (not names/labels) of the group to have m[u,v]
> be u*v.

OK, that should be easy.

> Yeah, hard point. multiplication / addition is consistent with __mul__
> and __add__. So that's probably ok without cluttering the namespace.
> 
> By the way: congrats on being essentially the first non Sage-Combinat
> contributer to categories :-) How did it go?

Nice.  I like it.  I'm a fan.  And your ring patch will help me recognize when/how categorification happens.

I'm running out of time on this, it's semester break this week, so I'll throw something up soon.

Rob



---

archive/issue_comments_064228.json:
```json
{
    "body": "Illustrates doctest failure",
    "created_at": "2010-03-20T02:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64228",
    "user": "rbeezer"
}
```

Illustrates doctest failure



---

archive/issue_comments_064229.json:
```json
{
    "body": "Attachment [trac_7555_doctest_failure.patch](tarball://root/attachments/some-uuid/ticket7555/trac_7555_doctest_failure.patch) by rbeezer created at 2010-03-20 18:10:57\n\nIgnore that doctest failure patch - I found the problem.",
    "created_at": "2010-03-20T18:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64229",
    "user": "rbeezer"
}
```

Attachment [trac_7555_doctest_failure.patch](tarball://root/attachments/some-uuid/ticket7555/trac_7555_doctest_failure.patch) by rbeezer created at 2010-03-20 18:10:57

Ignore that doctest failure patch - I found the problem.



---

archive/issue_comments_064230.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-20T21:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64230",
    "user": "rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064231.json:
```json
{
    "body": "Attachment [trac_7555_operation_table-categories.patch](tarball://root/attachments/some-uuid/ticket7555/trac_7555_operation_table-categories.patch) by rbeezer created at 2010-03-20 21:25:41\n\nPatch is complete enough to review.\n\n`__getitem__` implemented.\n\nrow_keys/column_keys are the latest name for elements in headings-order.\n\nLeft `translation` dictionary as-is.\n\n`addition_table` is a stub of sorts.  Has a doctest, and so on, but can be much better documented when `IntegerModRing` is settled at #8562.  It'll mostly be a cut/paste job from `multiplication_table` with new examples.  \n\nBut I'd like this to move forward independently, since my time will be limited for a few weeks.",
    "created_at": "2010-03-20T21:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64231",
    "user": "rbeezer"
}
```

Attachment [trac_7555_operation_table-categories.patch](tarball://root/attachments/some-uuid/ticket7555/trac_7555_operation_table-categories.patch) by rbeezer created at 2010-03-20 21:25:41

Patch is complete enough to review.

`__getitem__` implemented.

row_keys/column_keys are the latest name for elements in headings-order.

Left `translation` dictionary as-is.

`addition_table` is a stub of sorts.  Has a doctest, and so on, but can be much better documented when `IntegerModRing` is settled at #8562.  It'll mostly be a cut/paste job from `multiplication_table` with new examples.  

But I'd like this to move forward independently, since my time will be limited for a few weeks.



---

archive/issue_comments_064232.json:
```json
{
    "body": "Hi Rob!\n\nReplying to [comment:11 rbeezer]:\n> Patch is complete enough to review.\n> But I'd like this to move forward independently, since my time will be limited for a few weeks.\n\nThanks for you work on this. This sounds very good, so will set up a\npositive review as soon as I get a running 4.3.4 sage to launch the\ntests.\n\nThree minor thing I am hesitating about:\n\n- Do we really want coercion in __getitem__. By default, I would tend\n  to not do it for efficiency, unless a strong use case comes up in\n  practice.\n\n- In OperationTable, there is now a bit of redundancy between S and\n  elements; the only place where S is used is to coerce the elements.\n  In particular, what about just accepting:\n\n\tOperationTable(iterable, operation)\n\n   where iterable is any iterable (up to the user to make sure that it\n   is finite).\n\n   No big deal; this can be added later if desirable.\n\nI'll probably post a small reviewer patch with once I can double check\nthe html doc with micro typos and, if you agree, removing coercion in\n__getitem__.\n\nCheers,\n\t\t\t\tNicolas",
    "created_at": "2010-03-21T08:10:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64232",
    "user": "nthiery"
}
```

Hi Rob!

Replying to [comment:11 rbeezer]:
> Patch is complete enough to review.
> But I'd like this to move forward independently, since my time will be limited for a few weeks.

Thanks for you work on this. This sounds very good, so will set up a
positive review as soon as I get a running 4.3.4 sage to launch the
tests.

Three minor thing I am hesitating about:

- Do we really want coercion in __getitem__. By default, I would tend
  to not do it for efficiency, unless a strong use case comes up in
  practice.

- In OperationTable, there is now a bit of redundancy between S and
  elements; the only place where S is used is to coerce the elements.
  In particular, what about just accepting:

	OperationTable(iterable, operation)

   where iterable is any iterable (up to the user to make sure that it
   is finite).

   No big deal; this can be added later if desirable.

I'll probably post a small reviewer patch with once I can double check
the html doc with micro typos and, if you agree, removing coercion in
__getitem__.

Cheers,
				Nicolas



---

archive/issue_comments_064233.json:
```json
{
    "body": "Replying to [comment:9 rbeezer]:\n> Been working most of the day straightening this up.\n\nThanks!\n\n> Allowing more general operations is a big improvement.  See example of table of commutators of a finite group once I get a patch up.  ;-)\n\nCool :-)\n> Aah - that answers lots of questions.  Thanks.  \"categorified\"??  Your English is excellent, but that is pretty bad.  ;-) ;-)  ;-)  (But it was I might have said too).\n\n:-)\n\n> Not too bad.  Empty latex table is nice, empty ascii table is so-so, but not worth anymore effort.\n\nCool. Florent will appreciate not to have to handle yet another empty object :-)",
    "created_at": "2010-03-21T08:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64233",
    "user": "nthiery"
}
```

Replying to [comment:9 rbeezer]:
> Been working most of the day straightening this up.

Thanks!

> Allowing more general operations is a big improvement.  See example of table of commutators of a finite group once I get a patch up.  ;-)

Cool :-)
> Aah - that answers lots of questions.  Thanks.  "categorified"??  Your English is excellent, but that is pretty bad.  ;-) ;-)  ;-)  (But it was I might have said too).

:-)

> Not too bad.  Empty latex table is nice, empty ascii table is so-so, but not worth anymore effort.

Cool. Florent will appreciate not to have to handle yet another empty object :-)



---

archive/issue_comments_064234.json:
```json
{
    "body": "Replying to [comment:12 nthiery]:\nHi Nicolas,\n\n> Three minor thing I am hesitating about:\n\nI only see two, not that I'm looking for trouble.\n\n>  - Do we really want coercion in __getitem__. By default, I would tend\n>    to not do it for efficiency, unless a strong use case comes up in\n>    practice.\n\nCoercion here could go away - I've perhaps gone overboard with coercion, envisioning students typing in strings that are not really elements, such as permutations.  So I want to keep coercion in `__init__`.  You are right, if no coercion in `__getitem__` then the object does not need to hold a reference to S.\n\n\n>  - In OperationTable, there is now a bit of redundancy between S and\n>    elements; the only place where S is used is to coerce the elements.\n>    In particular, what about just accepting:\n>\n>       OperationTable(iterable, operation)\n>\n>    where iterable is any iterable (up to the user to make sure that it\n>    is finite).\n>\n>    No big deal; this can be added later if desirable.\n\nThis struck me as a good idea at first, but again, I'd like a chance to coerce the contents of `elements` (when present) into something (S, a parent), so I'd really like to keep this feature.  It's only on creation, and only once per element.  I find coercion is a hard idea for students to come to grips with, so I'd like to help out as much as possible here and not assume that the input is pure.\n\n> I'll probably post a small reviewer patch with once I can double check\n> the html doc with micro typos and, if you agree, removing coercion in\n> __getitem__.\n\nSure, you can clean-up `__getitem__` to suit your tastes.\n\nThanks for all your help with this.\n\nRob\n\nPS  I'm glad I can make Florent's life that much easier.  ;-)",
    "created_at": "2010-03-22T02:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64234",
    "user": "rbeezer"
}
```

Replying to [comment:12 nthiery]:
Hi Nicolas,

> Three minor thing I am hesitating about:

I only see two, not that I'm looking for trouble.

>  - Do we really want coercion in __getitem__. By default, I would tend
>    to not do it for efficiency, unless a strong use case comes up in
>    practice.

Coercion here could go away - I've perhaps gone overboard with coercion, envisioning students typing in strings that are not really elements, such as permutations.  So I want to keep coercion in `__init__`.  You are right, if no coercion in `__getitem__` then the object does not need to hold a reference to S.


>  - In OperationTable, there is now a bit of redundancy between S and
>    elements; the only place where S is used is to coerce the elements.
>    In particular, what about just accepting:
>
>       OperationTable(iterable, operation)
>
>    where iterable is any iterable (up to the user to make sure that it
>    is finite).
>
>    No big deal; this can be added later if desirable.

This struck me as a good idea at first, but again, I'd like a chance to coerce the contents of `elements` (when present) into something (S, a parent), so I'd really like to keep this feature.  It's only on creation, and only once per element.  I find coercion is a hard idea for students to come to grips with, so I'd like to help out as much as possible here and not assume that the input is pure.

> I'll probably post a small reviewer patch with once I can double check
> the html doc with micro typos and, if you agree, removing coercion in
> __getitem__.

Sure, you can clean-up `__getitem__` to suit your tastes.

Thanks for all your help with this.

Rob

PS  I'm glad I can make Florent's life that much easier.  ;-)



---

archive/issue_comments_064235.json:
```json
{
    "body": "Hi Robert,\n\nThe updated patch contains the following changes:\n\n- OperationTable is moved in sage.matrix.operation_table\n\n- multiplication_table and addition_table are moved in the new\n  categories Magmas and AdditiveMagmas respectively (sorry, this\n  introduces a dependency on #8579; but there will be many changes\n  soon in Semigroups, and this will avoid later conflicts when moving\n  things around)\n\n- __getitem__ does not do coercion anymore\n\n- The input can be a finite iterable, as in:\n\n\n```\n        sage: T = OperationTable([False, True], operator.or_, names = 'elements')\n        sage: T\n            .  False  True\n             +------------\n        False| False  True\n         True|  True  True\n```\n\n\n- self._elts (and thus the column/row keys) is a tuple (reduces the\n  risk of accidently changing its content)\n\n- a couple minor doc improvements: using directly :: at the end of a\n  sentence describing the next example, putting default values within\n  () ...\n\n- I allowed myself to change the '+' and '*' to operator.add and\n  operator.mul, for a more uniform logic (anyway, the basic user\n  won't use OperationTable directly, and for the others, it is nice\n  to show them directly the general approach).\n\nGiven that all the code was moved around, a reviewer patch would not\nhave brought any useful information. So I just folded everything\ntogether.\n\nAll tests pass on my ubuntu laptop.",
    "created_at": "2010-03-22T21:36:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64235",
    "user": "nthiery"
}
```

Hi Robert,

The updated patch contains the following changes:

- OperationTable is moved in sage.matrix.operation_table

- multiplication_table and addition_table are moved in the new
  categories Magmas and AdditiveMagmas respectively (sorry, this
  introduces a dependency on #8579; but there will be many changes
  soon in Semigroups, and this will avoid later conflicts when moving
  things around)

- __getitem__ does not do coercion anymore

- The input can be a finite iterable, as in:


```
        sage: T = OperationTable([False, True], operator.or_, names = 'elements')
        sage: T
            .  False  True
             +------------
        False| False  True
         True|  True  True
```


- self._elts (and thus the column/row keys) is a tuple (reduces the
  risk of accidently changing its content)

- a couple minor doc improvements: using directly :: at the end of a
  sentence describing the next example, putting default values within
  () ...

- I allowed myself to change the '+' and '*' to operator.add and
  operator.mul, for a more uniform logic (anyway, the basic user
  won't use OperationTable directly, and for the others, it is nice
  to show them directly the general approach).

Given that all the code was moved around, a reviewer patch would not
have brought any useful information. So I just folded everything
together.

All tests pass on my ubuntu laptop.



---

archive/issue_comments_064236.json:
```json
{
    "body": "Oh, Rob, I forgot to mention: your changes are good! So this patch just needs a cross positive review from you on my changes, and I consider it as good to go.",
    "created_at": "2010-03-22T21:41:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64236",
    "user": "nthiery"
}
```

Oh, Rob, I forgot to mention: your changes are good! So this patch just needs a cross positive review from you on my changes, and I consider it as good to go.



---

archive/issue_comments_064237.json:
```json
{
    "body": "Hi Nicolas,\n\nThanks for all your help, and attention to this.  Changes look good, but I had trouble with #8579, so I haven't been able to test them.  Thanks for adding magmas - that is where this belongs.\n\nMore comments when I can test more.\n\nRob",
    "created_at": "2010-03-23T04:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64237",
    "user": "rbeezer"
}
```

Hi Nicolas,

Thanks for all your help, and attention to this.  Changes look good, but I had trouble with #8579, so I haven't been able to test them.  Thanks for adding magmas - that is where this belongs.

More comments when I can test more.

Rob



---

archive/issue_comments_064238.json:
```json
{
    "body": "Replying to [comment:17 rbeezer]:\n> Hi Nicolas,\n> \n> Thanks for all your help, and attention to this.  Changes look good, but I had trouble with #8579, so I haven't been able to test them.  Thanks for adding magmas - that is where this belongs.\n> \n> More comments when I can test more.\n\nOops, sorry, I forgot to mention the trivial syntactic dependency of #8579 on #7880.",
    "created_at": "2010-03-23T07:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64238",
    "user": "nthiery"
}
```

Replying to [comment:17 rbeezer]:
> Hi Nicolas,
> 
> Thanks for all your help, and attention to this.  Changes look good, but I had trouble with #8579, so I haven't been able to test them.  Thanks for adding magmas - that is where this belongs.
> 
> More comments when I can test more.

Oops, sorry, I forgot to mention the trivial syntactic dependency of #8579 on #7880.



---

archive/issue_comments_064239.json:
```json
{
    "body": "Hi there,\n\nThe patch which is on sage-combinat queue (which seems to have to difference\nwhich the one here) causes the following failure. This is with with\nsage-4.3.4, on sage.saegmath.org and on my laptop (openSuSE 11.1):\n\n```\nsage -t  \"4.3.4/devel/sage-combinat/sage/categories/groups.py\"\n**********************************************************************\nFile \"/usr/local/sage/sage-4.3.4/devel/sage-combinat/sage/categories/groups.py\", line 138:\n    sage: T.column_keys()\nExpected:\n    [(), (5,6,7), (5,7,6)...(1,4,2,3)(5,7)]\nGot:\n    ((), (5,6,7), (5,7,6), (1,2)(3,4), (1,2)(3,4)(5,6,7), (1,2)(3,4)(5,7,6), (1,3,2,4)(6,7), (1,3,2,4)(5,6), (1,3,2,4)(5,7), (1,4,2,3)(6,7), (1,4,2,3)(5,6), (1,4,2,3)(5,7))\n**********************************************************************\nFile \"/usr/local/sage/sage-4.3.4/devel/sage-combinat/sage/categories/groups.py\", line 159:\n    sage: M.cayley_table()\nExpected:\n    *  a b c d e f\n    +------------\n    a| c e a f b d\n    b| d f b e a c\n    c| a b c d e f\n    d| b a d c f e\n    e| f d e b c a\n    f| e c f a d b\nGot:\n    *  a b c d e f\n     +------------\n    a| d c b a f e\n    b| e f a b c d\n    c| f e d c b a\n    d| a b c d e f\n    e| b a f e d c\n    f| c d e f a b\n    <BLANKLINE>\n**********************************************************************\n1 items had failures:\n   2 of  35 in __main__.example_5\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/averell/.sage//tmp/.doctest_groups.py\n         [17.4 s]\nsage -t  sage/categories/magmas.py\n**********************************************************************\nFile \"/mnt/usb1/scratch/hivert/sage-4.3.4-sage.math.washington.edu-x86_64-Linux/devel/sage-combinat/sage/categories/magmas.py\", line 195:\n    sage: T.column_keys()\nExpected:\n    ['a', 'b', 'ab', 'ba']\nGot:\n    ('a', 'b', 'ab', 'ba')\n**********************************************************************\nFile \"/mnt/usb1/scratch/hivert/sage-4.3.4-sage.math.washington.edu-x86_64-Linux/devel/sage-combinat/sage/categories/magmas.py\", line 254:\n    sage: T.column_keys()\nExpected:\n    [(), (1,2,3), (1,3,2)]\nGot:\n    ((), (1,2,3), (1,3,2))\n**********************************************************************\n1 items had failures:\n   2 of  22 in __main__.example_5\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/hivert/dot_sage/tmp/.doctest_magmas.py\n         [3.9 s]\n```\n",
    "created_at": "2010-03-23T13:46:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64239",
    "user": "hivert"
}
```

Hi there,

The patch which is on sage-combinat queue (which seems to have to difference
which the one here) causes the following failure. This is with with
sage-4.3.4, on sage.saegmath.org and on my laptop (openSuSE 11.1):

```
sage -t  "4.3.4/devel/sage-combinat/sage/categories/groups.py"
**********************************************************************
File "/usr/local/sage/sage-4.3.4/devel/sage-combinat/sage/categories/groups.py", line 138:
    sage: T.column_keys()
Expected:
    [(), (5,6,7), (5,7,6)...(1,4,2,3)(5,7)]
Got:
    ((), (5,6,7), (5,7,6), (1,2)(3,4), (1,2)(3,4)(5,6,7), (1,2)(3,4)(5,7,6), (1,3,2,4)(6,7), (1,3,2,4)(5,6), (1,3,2,4)(5,7), (1,4,2,3)(6,7), (1,4,2,3)(5,6), (1,4,2,3)(5,7))
**********************************************************************
File "/usr/local/sage/sage-4.3.4/devel/sage-combinat/sage/categories/groups.py", line 159:
    sage: M.cayley_table()
Expected:
    *  a b c d e f
    +------------
    a| c e a f b d
    b| d f b e a c
    c| a b c d e f
    d| b a d c f e
    e| f d e b c a
    f| e c f a d b
Got:
    *  a b c d e f
     +------------
    a| d c b a f e
    b| e f a b c d
    c| f e d c b a
    d| a b c d e f
    e| b a f e d c
    f| c d e f a b
    <BLANKLINE>
**********************************************************************
1 items had failures:
   2 of  35 in __main__.example_5
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/averell/.sage//tmp/.doctest_groups.py
         [17.4 s]
sage -t  sage/categories/magmas.py
**********************************************************************
File "/mnt/usb1/scratch/hivert/sage-4.3.4-sage.math.washington.edu-x86_64-Linux/devel/sage-combinat/sage/categories/magmas.py", line 195:
    sage: T.column_keys()
Expected:
    ['a', 'b', 'ab', 'ba']
Got:
    ('a', 'b', 'ab', 'ba')
**********************************************************************
File "/mnt/usb1/scratch/hivert/sage-4.3.4-sage.math.washington.edu-x86_64-Linux/devel/sage-combinat/sage/categories/magmas.py", line 254:
    sage: T.column_keys()
Expected:
    [(), (1,2,3), (1,3,2)]
Got:
    ((), (1,2,3), (1,3,2))
**********************************************************************
1 items had failures:
   2 of  22 in __main__.example_5
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/hivert/dot_sage/tmp/.doctest_magmas.py
         [3.9 s]
```




---

archive/issue_comments_064240.json:
```json
{
    "body": "Hi Florent,\n\nNicolas changed a list to a tuple, so that explains part of this.  Not sure why the table changed.  I'll be working on this about 12 hours from now, so will double-check everything then.\n\nRob",
    "created_at": "2010-03-23T14:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64240",
    "user": "rbeezer"
}
```

Hi Florent,

Nicolas changed a list to a tuple, so that explains part of this.  Not sure why the table changed.  I'll be working on this about 12 hours from now, so will double-check everything then.

Rob



---

archive/issue_comments_064241.json:
```json
{
    "body": "Thanks Florent for catching this. Ooops, I indeed apparently forgot to rerun some tests after the list -> tuple change.\n\nFor the other one: I had made the assumption that G=SL(2,2) was a proper enumerated set, that is G.list() == list(G). It is not, which is a bug.\n\nI guess we can ignore this, and just update the doctest output. I'll put up an updated patch when I am back home (in 2-3 hours) unless someone beats me to it.",
    "created_at": "2010-03-23T15:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64241",
    "user": "nthiery"
}
```

Thanks Florent for catching this. Ooops, I indeed apparently forgot to rerun some tests after the list -> tuple change.

For the other one: I had made the assumption that G=SL(2,2) was a proper enumerated set, that is G.list() == list(G). It is not, which is a bug.

I guess we can ignore this, and just update the doctest output. I'll put up an updated patch when I am back home (in 2-3 hours) unless someone beats me to it.



---

archive/issue_comments_064242.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-23T15:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64242",
    "user": "nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064243.json:
```json
{
    "body": "Back online for a couple minutes. I'll upload an updated patch shortly.\n\nSL bug on: #8588",
    "created_at": "2010-03-23T16:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64243",
    "user": "nthiery"
}
```

Back online for a couple minutes. I'll upload an updated patch shortly.

SL bug on: #8588



---

archive/issue_comments_064244.json:
```json
{
    "body": "Replaces all the previous ones",
    "created_at": "2010-03-23T16:35:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64244",
    "user": "nthiery"
}
```

Replaces all the previous ones



---

archive/issue_comments_064245.json:
```json
{
    "body": "Attachment [trac_7555_operation_table-categories.2.patch](tarball://root/attachments/some-uuid/ticket7555/trac_7555_operation_table-categories.2.patch) by nthiery created at 2010-03-23 16:37:54\n\nDone. Diff to previous version on: http://combinat.sagemath.org/hgwebdir.cgi/patches/diff/233de3ecbcb7/trac_7555_operation_table-categories.patch",
    "created_at": "2010-03-23T16:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64245",
    "user": "nthiery"
}
```

Attachment [trac_7555_operation_table-categories.2.patch](tarball://root/attachments/some-uuid/ticket7555/trac_7555_operation_table-categories.2.patch) by nthiery created at 2010-03-23 16:37:54

Done. Diff to previous version on: http://combinat.sagemath.org/hgwebdir.cgi/patches/diff/233de3ecbcb7/trac_7555_operation_table-categories.patch



---

archive/issue_comments_064246.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-23T16:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64246",
    "user": "nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064247.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-23T17:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64247",
    "user": "jason"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064248.json:
```json
{
    "body": "This is fantastic.  Here are some more very minor things:\n\n* two typos in the docs for _name_maker: \"fromatting\" and \"adictionary\"\n* in column_keys, the OUTPUT: header looks weird without a blank line between it and the following text\n* The first example on _ascii_table doesn't look like the top row lines up with the first column (the +---- line should be padded with one more space on the left)\n\nAnd an enhancement:\n\n* If it makes sense to support slice notation in get_item, or multiple rows/columns, to get a submatrix (subtable), then it would be easy to call the sage.misc.misc_c.normalize_index on the indices that you are already finding in _get_item_ to easily get a nice subtable.",
    "created_at": "2010-03-23T17:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64248",
    "user": "jason"
}
```

This is fantastic.  Here are some more very minor things:

* two typos in the docs for _name_maker: "fromatting" and "adictionary"
* in column_keys, the OUTPUT: header looks weird without a blank line between it and the following text
* The first example on _ascii_table doesn't look like the top row lines up with the first column (the +---- line should be padded with one more space on the left)

And an enhancement:

* If it makes sense to support slice notation in get_item, or multiple rows/columns, to get a submatrix (subtable), then it would be easy to call the sage.misc.misc_c.normalize_index on the indices that you are already finding in _get_item_ to easily get a nice subtable.



---

archive/issue_comments_064249.json:
```json
{
    "body": "(I should add that the enhancement above is not the \"needs work\" request.\u00a0 Also, I mainly read the documentation, but didn't look at the code too much, so my points above are not a review of the code.)",
    "created_at": "2010-03-23T21:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64249",
    "user": "jason"
}
```

(I should add that the enhancement above is not the "needs work" request.  Also, I mainly read the documentation, but didn't look at the code too much, so my points above are not a review of the code.)



---

archive/issue_comments_064250.json:
```json
{
    "body": "Replying to [comment:24 jason]:\n> This is fantastic.  Here are some more very minor things:\n\nJason,\n\nThanks for catching a few details, and for the suggestion.\n\nThis is getting mixed up with a bunch of other patches, so I'd like to finalize it.  I have to come back and improve the documentation for the addition table (once integer mod rings are straightened away), so I'll look into slicing then.\n\nThanks again,\nRob",
    "created_at": "2010-03-24T03:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64250",
    "user": "rbeezer"
}
```

Replying to [comment:24 jason]:
> This is fantastic.  Here are some more very minor things:

Jason,

Thanks for catching a few details, and for the suggestion.

This is getting mixed up with a bunch of other patches, so I'd like to finalize it.  I have to come back and improve the documentation for the addition table (once integer mod rings are straightened away), so I'll look into slicing then.

Thanks again,
Rob



---

archive/issue_comments_064251.json:
```json
{
    "body": "Attachment [trac_7555_minor-fixups.patch](tarball://root/attachments/some-uuid/ticket7555/trac_7555_minor-fixups.patch) by rbeezer created at 2010-03-24 05:11:20",
    "created_at": "2010-03-24T05:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64251",
    "user": "rbeezer"
}
```

Attachment [trac_7555_minor-fixups.patch](tarball://root/attachments/some-uuid/ticket7555/trac_7555_minor-fixups.patch) by rbeezer created at 2010-03-24 05:11:20



---

archive/issue_comments_064252.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-24T05:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64252",
    "user": "rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064253.json:
```json
{
    "body": "Hi Nicolas,\n\nYour changes all look good - thanks for those.  Feel free to add yourself to the author field - it'd be good to \"share\" a patch with you.  So this is a positive review on those.\n\nWith latest \"fixup\" patch, passes all tests in Sage library, docs build without warnings and look OK.\n\nNow the ball is in your court.  A handful of little things, in a separate patch so they are easy to isolate.\n\n- self._S is removed, since it is not needed in `__getitem__` anymore\n\n- \"\\\\cdot\" with two backslashesfor latex symbol for generic operation, my mistake\n\n- four fixes from Jason (above)\n\n- title for reference manual, and GPL header in sage/matrix/operation_table.py\n\n- fixed a reference to semigroups which has now moved\n\nSo I believe you could check these and we'd be done?\n\nRob",
    "created_at": "2010-03-24T05:19:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64253",
    "user": "rbeezer"
}
```

Hi Nicolas,

Your changes all look good - thanks for those.  Feel free to add yourself to the author field - it'd be good to "share" a patch with you.  So this is a positive review on those.

With latest "fixup" patch, passes all tests in Sage library, docs build without warnings and look OK.

Now the ball is in your court.  A handful of little things, in a separate patch so they are easy to isolate.

- self._S is removed, since it is not needed in `__getitem__` anymore

- "\\cdot" with two backslashesfor latex symbol for generic operation, my mistake

- four fixes from Jason (above)

- title for reference manual, and GPL header in sage/matrix/operation_table.py

- fixed a reference to semigroups which has now moved

So I believe you could check these and we'd be done?

Rob



---

archive/issue_comments_064254.json:
```json
{
    "body": "Replying to [comment:27 rbeezer]:\n> Feel free to add yourself to the author field - it'd be good to \"share\" a patch with you.\n\nThanks for the offer! It'd be a pleasure indeed. Now, you really wrote the bulk of the code. I just did my reviewer's job: all in all, my main code contribution is the writing of the Magmas category, which is not much and for which I'll get credit separately. \n\nIt was a pleasure working as a team on this patch, and I am looking forward writing another patch together :-) \n\n> With latest \"fixup\" patch, passes all tests in Sage library, docs build without warnings and look OK.\n> ...\n> So I believe you could check these and we'd be done?\n\nYour fixups look good! I just changed the copyright header as per the\ntemplate in http://www.sagemath.org/doc/developer/conventions.html,\nand used the occasion to replace a r'\\blah' into '\\\\blah' in the\ndoctests for consistency with the other occurrences in this file.\n\nI reran the tests on the file itself, and on the category code, which I\nbelieve is sufficient. So, on my account, it's now all good to go. Feel\nfree to set a positive review once you have double checked my changes.",
    "created_at": "2010-03-24T08:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64254",
    "user": "nthiery"
}
```

Replying to [comment:27 rbeezer]:
> Feel free to add yourself to the author field - it'd be good to "share" a patch with you.

Thanks for the offer! It'd be a pleasure indeed. Now, you really wrote the bulk of the code. I just did my reviewer's job: all in all, my main code contribution is the writing of the Magmas category, which is not much and for which I'll get credit separately. 

It was a pleasure working as a team on this patch, and I am looking forward writing another patch together :-) 

> With latest "fixup" patch, passes all tests in Sage library, docs build without warnings and look OK.
> ...
> So I believe you could check these and we'd be done?

Your fixups look good! I just changed the copyright header as per the
template in http://www.sagemath.org/doc/developer/conventions.html,
and used the occasion to replace a r'\blah' into '\\blah' in the
doctests for consistency with the other occurrences in this file.

I reran the tests on the file itself, and on the category code, which I
believe is sufficient. So, on my account, it's now all good to go. Feel
free to set a positive review once you have double checked my changes.



---

archive/issue_comments_064255.json:
```json
{
    "body": "Attachment [trac_7555_minor-fixups-nt.patch](tarball://root/attachments/some-uuid/ticket7555/trac_7555_minor-fixups-nt.patch) by nthiery created at 2010-03-24 08:47:45",
    "created_at": "2010-03-24T08:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64255",
    "user": "nthiery"
}
```

Attachment [trac_7555_minor-fixups-nt.patch](tarball://root/attachments/some-uuid/ticket7555/trac_7555_minor-fixups-nt.patch) by nthiery created at 2010-03-24 08:47:45



---

archive/issue_comments_064256.json:
```json
{
    "body": "Attachment [trac_7555_operation_table-categories-all-in-one.patch](tarball://root/attachments/some-uuid/ticket7555/trac_7555_operation_table-categories-all-in-one.patch) by nthiery created at 2010-03-24 08:49:27\n\nApply only this one",
    "created_at": "2010-03-24T08:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64256",
    "user": "nthiery"
}
```

Attachment [trac_7555_operation_table-categories-all-in-one.patch](tarball://root/attachments/some-uuid/ticket7555/trac_7555_operation_table-categories-all-in-one.patch) by nthiery created at 2010-03-24 08:49:27

Apply only this one



---

archive/issue_comments_064257.json:
```json
{
    "body": "Jason: feel free to add yourself as a reviewer",
    "created_at": "2010-03-24T08:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64257",
    "user": "nthiery"
}
```

Jason: feel free to add yourself as a reviewer



---

archive/issue_comments_064258.json:
```json
{
    "body": "OK, all done.  This has a (cumulative) positive review.\n\nThanks, Jason, for the contributions, and thanks, Nicolas, for stepping in with all the prompt help with categories and useful fixes and enhancements.  When #8562 is done the addition table docstring can be expanded - doing this is #8596.\n\nTo do:  Add slicing as Jason suggests, make graphical output (#8598).\n\nRelease manager:\n\nThis needs #7880 first, then #8579.  Apply just the \"all-in-one\" patch.  Once merged, #7340 (the root motivator) can be marked fixed.",
    "created_at": "2010-03-24T15:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64258",
    "user": "rbeezer"
}
```

OK, all done.  This has a (cumulative) positive review.

Thanks, Jason, for the contributions, and thanks, Nicolas, for stepping in with all the prompt help with categories and useful fixes and enhancements.  When #8562 is done the addition table docstring can be expanded - doing this is #8596.

To do:  Add slicing as Jason suggests, make graphical output (#8598).

Release manager:

This needs #7880 first, then #8579.  Apply just the "all-in-one" patch.  Once merged, #7340 (the root motivator) can be marked fixed.



---

archive/issue_comments_064259.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-24T15:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64259",
    "user": "rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064260.json:
```json
{
    "body": "Merged \"trac_7555_operation_table-categories-all-in-one.patch\" in 4.4.alpha0",
    "created_at": "2010-04-15T20:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64260",
    "user": "jhpalmieri"
}
```

Merged "trac_7555_operation_table-categories-all-in-one.patch" in 4.4.alpha0



---

archive/issue_comments_064261.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T20:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7555#issuecomment-64261",
    "user": "jhpalmieri"
}
```

Resolution: fixed
