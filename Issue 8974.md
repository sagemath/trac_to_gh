# Issue 8974: Added eigenvalues, eigenvector, eigenspaces and minpoly to vector space endomorphisms

archive/issues_008974.json:
```json
{
    "body": "Assignee: jason, was\n\nKeywords: eigenvalues\n\nAdded the functions eigenvalues, eigenvectors, eigenspaces and minpoly to the FreeModuleMorphism class (only for endomorphisms of vector spaces).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8974\n\n",
    "created_at": "2010-05-15T20:50:25Z",
    "labels": [
        "linear algebra",
        "trivial",
        "enhancement"
    ],
    "title": "Added eigenvalues, eigenvector, eigenspaces and minpoly to vector space endomorphisms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8974",
    "user": "mmarco"
}
```
Assignee: jason, was

Keywords: eigenvalues

Added the functions eigenvalues, eigenvectors, eigenspaces and minpoly to the FreeModuleMorphism class (only for endomorphisms of vector spaces).

Issue created by migration from https://trac.sagemath.org/ticket/8974





---

archive/issue_comments_082785.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-05-15T21:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82785",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_082786.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-15T21:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82786",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082787.json:
```json
{
    "body": "Hmm. This is certainly functionality that we should have, but I don't agree with the implementation: I strongly feel that these linear-algebra methods should have *identical* behaviour for a matrix and for the corresponding morphism object. Your `eigenvectors` method takes an argument and returns the eigenvectors for that given eigenvalue, which isn't what the matrix one does. Similarly, `eigenspaces` for matrices makes a field extension if the eigenspaces aren't defined over the base field, while yours just returns the empty list. \n\nAlso, the underlying implementation should just call the existing one rather than doing the linear algebra anew. (E.g. for computing eigenvectors I think there are nasty cases with badly-conditioned matrices where just computing the kernel of X - lambda * identity blows up, and one can work around this using various devious tricks; it's not great if we have two different eigenvector methods and we have to fix them both separately.)",
    "created_at": "2010-06-14T10:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82787",
    "user": "davidloeffler"
}
```

Hmm. This is certainly functionality that we should have, but I don't agree with the implementation: I strongly feel that these linear-algebra methods should have *identical* behaviour for a matrix and for the corresponding morphism object. Your `eigenvectors` method takes an argument and returns the eigenvectors for that given eigenvalue, which isn't what the matrix one does. Similarly, `eigenspaces` for matrices makes a field extension if the eigenspaces aren't defined over the base field, while yours just returns the empty list. 

Also, the underlying implementation should just call the existing one rather than doing the linear algebra anew. (E.g. for computing eigenvectors I think there are nasty cases with badly-conditioned matrices where just computing the kernel of X - lambda * identity blows up, and one can work around this using various devious tricks; it's not great if we have two different eigenvector methods and we have to fix them both separately.)



---

archive/issue_comments_082788.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-06-14T10:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82788",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_082789.json:
```json
{
    "body": "I agree that using the same methods for matrices and morphisms would be desiderable, but in my implementation i prefeared the mathematical correctedness. I mean, if a morphism is defined in a vector space over QQ, it doesn't make sense to say that its eigenvalues are numbers in a bigger field. Strictly speaking, they are not eigenvalues of this morphism (they are eigenvalues of a morphism defined in a bigger vector space, that can be defined in a natural way from this first morphism). If we include the functionality as a function of the vector space, i think it makes sense to be mathematically correct in this sense.\n\nMaybe a better way to implement this would be to call the methods of the underlying matrix (avoiding thus the duplicity of code) and then select only the values that belong to the base field (keeping thus the mathematical correctedness).",
    "created_at": "2010-06-14T11:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82789",
    "user": "mmarco"
}
```

I agree that using the same methods for matrices and morphisms would be desiderable, but in my implementation i prefeared the mathematical correctedness. I mean, if a morphism is defined in a vector space over QQ, it doesn't make sense to say that its eigenvalues are numbers in a bigger field. Strictly speaking, they are not eigenvalues of this morphism (they are eigenvalues of a morphism defined in a bigger vector space, that can be defined in a natural way from this first morphism). If we include the functionality as a function of the vector space, i think it makes sense to be mathematically correct in this sense.

Maybe a better way to implement this would be to call the methods of the underlying matrix (avoiding thus the duplicity of code) and then select only the values that belong to the base field (keeping thus the mathematical correctedness).



---

archive/issue_comments_082790.json:
```json
{
    "body": "I don't like the inconsistency. After all, matrices have base rings too, and your argument applies identically to the matrices rather than the endomorphism objects.\n\nIf you don't like the way it's currently implemented for matrices, you can start a debate on sage-devel if you want. It's perfectly possible that it could be changed, with an optional argument called something like \"base_extend\" to give users the option to choose whichever behaviour they want. But I absolutely insist that the behaviour should be the same for matrices and for morphisms of vector spaces represented by matrices.\n\nDavid",
    "created_at": "2010-06-14T11:52:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82790",
    "user": "davidloeffler"
}
```

I don't like the inconsistency. After all, matrices have base rings too, and your argument applies identically to the matrices rather than the endomorphism objects.

If you don't like the way it's currently implemented for matrices, you can start a debate on sage-devel if you want. It's perfectly possible that it could be changed, with an optional argument called something like "base_extend" to give users the option to choose whichever behaviour they want. But I absolutely insist that the behaviour should be the same for matrices and for morphisms of vector spaces represented by matrices.

David



---

archive/issue_comments_082791.json:
```json
{
    "body": "Fine with me then. I will rewrite the functions makind them just call the methods asociated to the underlying matrices, and start the debate in sage-devel. \n\nJust one question: would you agree to, for instance, convert the output of the eigenvectors function in an element of the vector space (instead of just the tuple that the matrix method returns)?",
    "created_at": "2010-06-14T12:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82791",
    "user": "mmarco"
}
```

Fine with me then. I will rewrite the functions makind them just call the methods asociated to the underlying matrices, and start the debate in sage-devel. 

Just one question: would you agree to, for instance, convert the output of the eigenvectors function in an element of the vector space (instead of just the tuple that the matrix method returns)?



---

archive/issue_comments_082792.json:
```json
{
    "body": "The matrix eigenvectors method returns *vectors,* not tuples. And so should the new one (but make sure it does the right thing in non-ambient vector spaces).",
    "created_at": "2010-06-14T13:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82792",
    "user": "davidloeffler"
}
```

The matrix eigenvectors method returns *vectors,* not tuples. And so should the new one (but make sure it does the right thing in non-ambient vector spaces).



---

archive/issue_comments_082793.json:
```json
{
    "body": "Hhmmm, the more i think about it, the less clear i see that it is a good idea to give results outside the base field (or vectorspace). \n\nDoes it really make sense to return as eigenvector some object that cannot be fed into the endomorphism procedure? That sounds like a very natural thing to do to check the correctedness of the result.\n\nI think i will wait until the duscusion about these procedures in matrix objects to decide the best way to implement them, unless you think there is some rush.",
    "created_at": "2010-06-14T19:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82793",
    "user": "mmarco"
}
```

Hhmmm, the more i think about it, the less clear i see that it is a good idea to give results outside the base field (or vectorspace). 

Does it really make sense to return as eigenvector some object that cannot be fed into the endomorphism procedure? That sounds like a very natural thing to do to check the correctedness of the result.

I think i will wait until the duscusion about these procedures in matrix objects to decide the best way to implement them, unless you think there is some rush.



---

archive/issue_comments_082794.json:
```json
{
    "body": "Attachment\n\nA Second patch with a new implementation (must be aplied after the previous one)",
    "created_at": "2010-06-20T00:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82794",
    "user": "mmarco"
}
```

Attachment

A Second patch with a new implementation (must be aplied after the previous one)



---

archive/issue_comments_082795.json:
```json
{
    "body": "In view that the discusion about the change of the matrix functions is idle, i have implemented it.\n\nSo with this patch, the functions eigenvalues and eigenvectors can be called on matrices with the option extend=False (although i have noted that they are broken in matrices over the reals). I didn't change anything in the computation process; just parse the output to select the values in the base ring.\n\nWith that change, i have redone my implementation of these functions for homomorphism objects (an erased the eigenspaces functions, which i don't think make much sense to be translated directly from matrices such as it is). Now they just call the corresponding functions of the underlying matrices, and parse the output to convert the eigenvectors into elements of the corresponding vector space.",
    "created_at": "2010-06-20T00:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82795",
    "user": "mmarco"
}
```

In view that the discusion about the change of the matrix functions is idle, i have implemented it.

So with this patch, the functions eigenvalues and eigenvectors can be called on matrices with the option extend=False (although i have noted that they are broken in matrices over the reals). I didn't change anything in the computation process; just parse the output to select the values in the base ring.

With that change, i have redone my implementation of these functions for homomorphism objects (an erased the eigenspaces functions, which i don't think make much sense to be translated directly from matrices such as it is). Now they just call the corresponding functions of the underlying matrices, and parse the output to convert the eigenvectors into elements of the corresponding vector space.



---

archive/issue_comments_082796.json:
```json
{
    "body": "Attachment\n\neigenvalues eigenvectors and minpoly functions for vectorspace endomorphims",
    "created_at": "2010-06-20T14:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82796",
    "user": "mmarco"
}
```

Attachment

eigenvalues eigenvectors and minpoly functions for vectorspace endomorphims



---

archive/issue_comments_082797.json:
```json
{
    "body": "Attachment\n\nadded the extend=False option for matrix eigenvalues and eigenvectors_left",
    "created_at": "2010-06-20T14:04:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82797",
    "user": "mmarco"
}
```

Attachment

added the extend=False option for matrix eigenvalues and eigenvectors_left



---

archive/issue_comments_082798.json:
```json
{
    "body": "Ok, this last two patches (track_8974_added_eigenfunctions_module.patch and track_8974_solved_nonimplemented_extfalse.patch) should do it. They contain respectively the new functions for endomorphisms, and the extend=False option for matrices (solving the nonimplemented error when it does not apply). They don't need any previous patches.",
    "created_at": "2010-06-20T14:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82798",
    "user": "mmarco"
}
```

Ok, this last two patches (track_8974_added_eigenfunctions_module.patch and track_8974_solved_nonimplemented_extfalse.patch) should do it. They contain respectively the new functions for endomorphisms, and the extend=False option for matrices (solving the nonimplemented error when it does not apply). They don't need any previous patches.



---

archive/issue_comments_082799.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-20T14:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82799",
    "user": "mmarco"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_082800.json:
```json
{
    "body": "With your new patches, eigenvectors_left accepts the extend parameter but eigenvectors_right doesn't; and bases for free module morphism eigenspaces are returned as lists, while bases for matrix eigenspaces are returned as sequences. I've done a tiny patch that fixes these slight inconsistencies and tidies up the docstrings a bit. Marco: if you're happy with my changes please feel free to set this to \"positive_review\".",
    "created_at": "2010-06-28T17:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82800",
    "user": "davidloeffler"
}
```

With your new patches, eigenvectors_left accepts the extend parameter but eigenvectors_right doesn't; and bases for free module morphism eigenspaces are returned as lists, while bases for matrix eigenspaces are returned as sequences. I've done a tiny patch that fixes these slight inconsistencies and tidies up the docstrings a bit. Marco: if you're happy with my changes please feel free to set this to "positive_review".



---

archive/issue_comments_082801.json:
```json
{
    "body": "apply over the two previous patches",
    "created_at": "2010-06-28T17:28:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82801",
    "user": "davidloeffler"
}
```

apply over the two previous patches



---

archive/issue_comments_082802.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-28T18:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82802",
    "user": "mmarco"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082803.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-06-28T18:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82803",
    "user": "mmarco"
}
```

Attachment



---

archive/issue_comments_082804.json:
```json
{
    "body": "Apply `track_8974_added_eigenfunctions_module.patch`, `track_8974_solved_nonimplemented_extfalse.patch` and `trac_8974_reviewer.patch`.",
    "created_at": "2010-06-28T18:51:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82804",
    "user": "davidloeffler"
}
```

Apply `track_8974_added_eigenfunctions_module.patch`, `track_8974_solved_nonimplemented_extfalse.patch` and `trac_8974_reviewer.patch`.



---

archive/issue_comments_082805.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T08:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8974#issuecomment-82805",
    "user": "mpatel"
}
```

Resolution: fixed
