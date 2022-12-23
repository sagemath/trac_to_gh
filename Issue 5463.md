# Issue 5463: [with patch, needs review] new section for tutorial about functions vs. expressions, etc.

archive/issues_005463.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nThere are lots of questions sage-support in which people trying to do basic calculus or plotting have gotten confused about how to specify a \"function\" to be plotted, differentiated, etc. The attached patch adds a section to the tutorial with some remarks about this issue.\n\nSee [http://www.math.washington.edu/~palmieri/tutorial/tour_functions.html](http://www.math.washington.edu/~palmieri/tutorial/tour_functions.html) for a typeset version (although you can just type 'sage -docbuild tutorial html' to get your own version).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5463\n\n",
    "created_at": "2009-03-09T23:27:00Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] new section for tutorial about functions vs. expressions, etc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5463",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

There are lots of questions sage-support in which people trying to do basic calculus or plotting have gotten confused about how to specify a "function" to be plotted, differentiated, etc. The attached patch adds a section to the tutorial with some remarks about this issue.

See [http://www.math.washington.edu/~palmieri/tutorial/tour_functions.html](http://www.math.washington.edu/~palmieri/tutorial/tour_functions.html) for a typeset version (although you can just type 'sage -docbuild tutorial html' to get your own version).


Issue created by migration from https://trac.sagemath.org/ticket/5463





---

archive/issue_comments_042416.json:
```json
{
    "body": "Looks good to me.  Well I sort of don't like the **'s instead of ^'s, but that's just a very minor style issue. All of the actual text looks good, and I like the description. \n\nThe ReST here looks funny: http://www.math.washington.edu/~palmieri/tutorial/tour_functions.html\n\nI.e., in each of the code blocks there is some text afterwards explaining the example, and it is typeset as code instead of text.  I don't know why.   Again, just a minor ReST issue.  Mhansen?",
    "created_at": "2009-03-10T07:06:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5463#issuecomment-42416",
    "user": "was"
}
```

Looks good to me.  Well I sort of don't like the **'s instead of ^'s, but that's just a very minor style issue. All of the actual text looks good, and I like the description. 

The ReST here looks funny: http://www.math.washington.edu/~palmieri/tutorial/tour_functions.html

I.e., in each of the code blocks there is some text afterwards explaining the example, and it is typeset as code instead of text.  I don't know why.   Again, just a minor ReST issue.  Mhansen?



---

archive/issue_comments_042417.json:
```json
{
    "body": "Yep, the ReST output does look funny, i.e. it seems that there is a lot of text that shouldn't be verbatim is rendered verbatim.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-10T16:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5463#issuecomment-42417",
    "user": "mabshoff"
}
```

Yep, the ReST output does look funny, i.e. it seems that there is a lot of text that shouldn't be verbatim is rendered verbatim.

Cheers,

Michael



---

archive/issue_comments_042418.json:
```json
{
    "body": "Sorry about the ReST output.  I was trying to balance two things, and failed.  Given my limited knowledge of ReST, I can either make all of the sage output accessible to doctesting, or I can have the text indented the way I want for an enumerated list, but not both.  In the new version of the patch (along with updated html on the cited web page), I've gone for the first option: doctesting sees and tests all of the examples.\n\n(I also changed \"**\" to carets, since I don't care much one way or the other, and was expressed a preference.)",
    "created_at": "2009-03-10T18:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5463#issuecomment-42418",
    "user": "jhpalmieri"
}
```

Sorry about the ReST output.  I was trying to balance two things, and failed.  Given my limited knowledge of ReST, I can either make all of the sage output accessible to doctesting, or I can have the text indented the way I want for an enumerated list, but not both.  In the new version of the patch (along with updated html on the cited web page), I've gone for the first option: doctesting sees and tests all of the examples.

(I also changed "**" to carets, since I don't care much one way or the other, and was expressed a preference.)



---

archive/issue_comments_042419.json:
```json
{
    "body": "Attachment\n\nMerged in Sage 3.4.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-10T20:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5463#issuecomment-42419",
    "user": "mabshoff"
}
```

Attachment

Merged in Sage 3.4.final.

Cheers,

Michael



---

archive/issue_comments_042420.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-10T20:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5463",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5463#issuecomment-42420",
    "user": "mabshoff"
}
```

Resolution: fixed
