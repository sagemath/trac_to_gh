# Issue 7477: Matroids

archive/issues_007477.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  kcrisman yomcat\n\nMatroids in Sage could be interesting from the educational point of view, as there are not so many ways to play with matroids on a computer, but also from the algorithmic point of view, as the Graph Theory section could use some help from the Matroid Union and Matroid Intersection Theorems... ( see #7476 )\n\nMacek is a GPL+C implementation of them http://www.fi.muni.cz/~hlineny/MACEK/ which I never tried but may be a good starting point !\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7477\n\n",
    "created_at": "2009-11-17T06:37:48Z",
    "labels": [
        "numerical",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.12",
    "title": "Matroids",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7477",
    "user": "ncohen"
}
```
Assignee: jkantor

CC:  kcrisman yomcat

Matroids in Sage could be interesting from the educational point of view, as there are not so many ways to play with matroids on a computer, but also from the algorithmic point of view, as the Graph Theory section could use some help from the Matroid Union and Matroid Intersection Theorems... ( see #7476 )

Macek is a GPL+C implementation of them http://www.fi.muni.cz/~hlineny/MACEK/ which I never tried but may be a good starting point !

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7477





---

archive/issue_comments_063021.json:
```json
{
    "body": "I think adding macek to Sage will be a lot of work... .\n\nAnother option is to add my code\nhttp://boxen.math.washington.edu/home/wdj/sagefiles/matroid_class.sage\nI don't have time right now to add this to Sage properly, due to teaching obligations. However, if anyone is interested, I can at least act as one of the referees. If not, I will try to get to this next semester.",
    "created_at": "2010-09-26T11:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63021",
    "user": "wdj"
}
```

I think adding macek to Sage will be a lot of work... .

Another option is to add my code
http://boxen.math.washington.edu/home/wdj/sagefiles/matroid_class.sage
I don't have time right now to add this to Sage properly, due to teaching obligations. However, if anyone is interested, I can at least act as one of the referees. If not, I will try to get to this next semester.



---

archive/issue_comments_063022.json:
```json
{
    "body": "Attachment [matroids-beezer-20110105.sage](tarball://root/attachments/some-uuid/ticket7477/matroids-beezer-20110105.sage) by rbeezer created at 2011-03-02 04:57:07\n\nI attended a short course on matroids at the US national math meetings in January 2011, and spent the two days hacking up as much about matroids as I could.  I knew David Joyner had done something similar, but I purposely did not look at his work first.  So you will see some common ideas and some differences.\n\nThis is definitely not pretty, nor efficient.  The goal was to implement as much functionality as quickly as possible, so there are obvious places where things should be done differently.  But it is clear that much of the hard work can be shipped off to Sage routines for graph theory, linear algebra and combinatorics.\n\nImplements vector matroid, cycle matroid, bicircular matroid, transversal matroid, uniform matroid, and duals of matroids.",
    "created_at": "2011-03-02T04:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63022",
    "user": "rbeezer"
}
```

Attachment [matroids-beezer-20110105.sage](tarball://root/attachments/some-uuid/ticket7477/matroids-beezer-20110105.sage) by rbeezer created at 2011-03-02 04:57:07

I attended a short course on matroids at the US national math meetings in January 2011, and spent the two days hacking up as much about matroids as I could.  I knew David Joyner had done something similar, but I purposely did not look at his work first.  So you will see some common ideas and some differences.

This is definitely not pretty, nor efficient.  The goal was to implement as much functionality as quickly as possible, so there are obvious places where things should be done differently.  But it is clear that much of the hard work can be shipped off to Sage routines for graph theory, linear algebra and combinatorics.

Implements vector matroid, cycle matroid, bicircular matroid, transversal matroid, uniform matroid, and duals of matroids.



---

archive/issue_comments_063023.json:
```json
{
    "body": "There is serious interest from the matroid theory community in creating a Sage package. It would provide similar functionality to the graph theory package: lots of methods (extensions, representations, Tutte polynomials, connectivity tests, isomorphism and minor testing, ...) and a database with named matroids and small matroids.\n\nMacek has several shortcomings that make it unsuitable; I will mention a few. It only works for representable matroids over the (small number of) partial fields implemented. It has an esoteric command language based on vertex-labelled trees. It has bugs. For instance, it cannot read its own output without modification, and is known not to detect minors when they are clearly present. Its author considers it \"done\", and will not support it.",
    "created_at": "2011-03-25T09:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63023",
    "user": "Stefan"
}
```

There is serious interest from the matroid theory community in creating a Sage package. It would provide similar functionality to the graph theory package: lots of methods (extensions, representations, Tutte polynomials, connectivity tests, isomorphism and minor testing, ...) and a database with named matroids and small matroids.

Macek has several shortcomings that make it unsuitable; I will mention a few. It only works for representable matroids over the (small number of) partial fields implemented. It has an esoteric command language based on vertex-labelled trees. It has bugs. For instance, it cannot read its own output without modification, and is known not to detect minors when they are clearly present. Its author considers it "done", and will not support it.



---

archive/issue_comments_063024.json:
```json
{
    "body": "(plus it would speedup the method Graph.edge_disjoint_spanning_tree which is deeeaaad slow right now)",
    "created_at": "2011-03-25T10:11:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63024",
    "user": "ncohen"
}
```

(plus it would speedup the method Graph.edge_disjoint_spanning_tree which is deeeaaad slow right now)



---

archive/issue_comments_063025.json:
```json
{
    "body": "Replying to [comment:3 Stefan]:\n\nHi Stefan,\n\nThanks for the information on MACEK.  I didn't know the details, but it looked to me like all support had ended, so it is good to have the confirmation.\n\nWhat will it take to get the matroid community started with Sage?\n\nRob",
    "created_at": "2011-03-25T16:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63025",
    "user": "rbeezer"
}
```

Replying to [comment:3 Stefan]:

Hi Stefan,

Thanks for the information on MACEK.  I didn't know the details, but it looked to me like all support had ended, so it is good to have the confirmation.

What will it take to get the matroid community started with Sage?

Rob



---

archive/issue_comments_063026.json:
```json
{
    "body": "Neither Rob's code nor mine is a patch. Any preference? I'm happy to convert my code into a patch and try to integrate Rob's new aspects in, or Rob can create a patch from his.",
    "created_at": "2011-03-25T17:19:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63026",
    "user": "wdj"
}
```

Neither Rob's code nor mine is a patch. Any preference? I'm happy to convert my code into a patch and try to integrate Rob's new aspects in, or Rob can create a patch from his.



---

archive/issue_comments_063027.json:
```json
{
    "body": "Replying to [comment:5 rbeezer]:\n> Replying to [comment:3 Stefan]:\n>\n> What will it take to get the matroid community started with Sage?\n\nShort answer (I sent you a longer by email): the matroid community has already started. We had a [meeting](http://msor.victoria.ac.nz/Main/MatroidComputation) in December, and will have a followup meeting in June. Several people have committed themselves to the effort.\n\nBy the way, I changed the \"Component\" field to combinatorics. I hope that's ok.",
    "created_at": "2011-03-25T21:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63027",
    "user": "Stefan"
}
```

Replying to [comment:5 rbeezer]:
> Replying to [comment:3 Stefan]:
>
> What will it take to get the matroid community started with Sage?

Short answer (I sent you a longer by email): the matroid community has already started. We had a [meeting](http://msor.victoria.ac.nz/Main/MatroidComputation) in December, and will have a followup meeting in June. Several people have committed themselves to the effort.

By the way, I changed the "Component" field to combinatorics. I hope that's ok.



---

archive/issue_comments_063028.json:
```json
{
    "body": "Changing component from numerical to combinatorics.",
    "created_at": "2011-03-25T21:55:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63028",
    "user": "Stefan"
}
```

Changing component from numerical to combinatorics.



---

archive/issue_comments_063029.json:
```json
{
    "body": "Replying to [comment:6 wdj]:\n> Neither Rob's code nor mine is a patch. Any preference? I'm happy to convert my code into a patch and try to integrate Rob's new aspects in, or Rob can create a patch from his.\n\nHi David,\n\nSorry for the delay in replying to this - recovering from Bug Days.\n\nI think the computational matroid folks are quite serious about moving a lot of their work to Sage.  Maybe it would be best if we let them decide what structure will work best for their purposes, rather than putting in something now that may not work well long-term?\n\nYou and I could probably best help them by advising and reviewing their contributions, I think.\n\nBut we shouldn't wait for them forever.  ;-)\n\nRob",
    "created_at": "2011-03-29T04:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63029",
    "user": "rbeezer"
}
```

Replying to [comment:6 wdj]:
> Neither Rob's code nor mine is a patch. Any preference? I'm happy to convert my code into a patch and try to integrate Rob's new aspects in, or Rob can create a patch from his.

Hi David,

Sorry for the delay in replying to this - recovering from Bug Days.

I think the computational matroid folks are quite serious about moving a lot of their work to Sage.  Maybe it would be best if we let them decide what structure will work best for their purposes, rather than putting in something now that may not work well long-term?

You and I could probably best help them by advising and reviewing their contributions, I think.

But we shouldn't wait for them forever.  ;-)

Rob



---

archive/issue_comments_063030.json:
```json
{
    "body": "I am brand new to Sage development, but I do a lot of work with matroids and would like to see them implemented in Sage.\n\nI will be teaching a graduate course in algebraic combinatorics this fall.  I am thinking of having my students create a Matroid sage class as a group project.  E.g., they could implement the conversions between all the various ways of presenting a matroid; basic constructions like direct sum and dual; and the Tutte polynomial.\n\nThoughts?\n\nJeremy Martin (University of Kansas)",
    "created_at": "2012-07-10T20:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63030",
    "user": "jeremy.l.martin"
}
```

I am brand new to Sage development, but I do a lot of work with matroids and would like to see them implemented in Sage.

I will be teaching a graduate course in algebraic combinatorics this fall.  I am thinking of having my students create a Matroid sage class as a group project.  E.g., they could implement the conversions between all the various ways of presenting a matroid; basic constructions like direct sum and dual; and the Tutte polynomial.

Thoughts?

Jeremy Martin (University of Kansas)



---

archive/issue_comments_063031.json:
```json
{
    "body": "Sounds like a great idea! You may want to try using the code attached here as a starting point.  Also, the sage-combinat folks have some great infrastructure for things like categories, and you should ask them about that.  But I think this is a very reasonable project.  Especially if you could somehow implement graph.matroid() and/or vecspace.basis.matroid - in the sense that one could have a graph, and then get a matroid they could do stuff with from it.",
    "created_at": "2012-07-10T20:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63031",
    "user": "kcrisman"
}
```

Sounds like a great idea! You may want to try using the code attached here as a starting point.  Also, the sage-combinat folks have some great infrastructure for things like categories, and you should ask them about that.  But I think this is a very reasonable project.  Especially if you could somehow implement graph.matroid() and/or vecspace.basis.matroid - in the sense that one could have a graph, and then get a matroid they could do stuff with from it.



---

archive/issue_comments_063032.json:
```json
{
    "body": "Hi!\n\nThere's a significant effort going on behind the screens to get matroids into Sage. You can get to our work-in-progress code at\n\nhttps://bitbucket.org/matroid/sage_matroids/\n\nand we've got a mailing list at\n\nhttps://groups.google.com/group/sage-matroid\n\nPlease join in the discussion. There is still plenty to be done.\n\nA quick description of our current status: we've got an abstract Matroid class with a bunch of subclasses: BasisMatroid, LinearMatroid, RankMatroid, CircuitClosuresMatroid are the main ones. There is support for minors and abstract duality. We have a rather fast isomorphism test, and a host of methods for standard queries. There's also a library of common matroids, and a constructor that takes various inputs (including Sage graphs). So you can write\n\nM = Matroid(G)\n\nWe think we need some minor coding and major documentation-string-writing before we want to submit it to Sage.",
    "created_at": "2012-07-10T21:32:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63032",
    "user": "Stefan"
}
```

Hi!

There's a significant effort going on behind the screens to get matroids into Sage. You can get to our work-in-progress code at

https://bitbucket.org/matroid/sage_matroids/

and we've got a mailing list at

https://groups.google.com/group/sage-matroid

Please join in the discussion. There is still plenty to be done.

A quick description of our current status: we've got an abstract Matroid class with a bunch of subclasses: BasisMatroid, LinearMatroid, RankMatroid, CircuitClosuresMatroid are the main ones. There is support for minors and abstract duality. We have a rather fast isomorphism test, and a host of methods for standard queries. There's also a library of common matroids, and a constructor that takes various inputs (including Sage graphs). So you can write

M = Matroid(G)

We think we need some minor coding and major documentation-string-writing before we want to submit it to Sage.



---

archive/issue_comments_063033.json:
```json
{
    "body": "Thanks!  I will join that Google group and see what I can do to help.\n\nRight now I am at a sage-combinat workshop at the IMA.  There is significant interest among the algebraic combinatorialists here in implementing matroids for Sage; on the other hand, I'm not sure if the sage-combinat folks know about the sage-matroid project.  I will make an announcement about it and invite people to get involved.\n\nJeremy",
    "created_at": "2012-07-11T11:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63033",
    "user": "jeremy.l.martin"
}
```

Thanks!  I will join that Google group and see what I can do to help.

Right now I am at a sage-combinat workshop at the IMA.  There is significant interest among the algebraic combinatorialists here in implementing matroids for Sage; on the other hand, I'm not sure if the sage-combinat folks know about the sage-matroid project.  I will make an announcement about it and invite people to get involved.

Jeremy



---

archive/issue_comments_063034.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-05-01T17:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63034",
    "user": "Stefan"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063035.json:
```json
{
    "body": "Note: needs Sage 5.9.rc1 to build (because the package list is now generated automatically in setup.py, this used to be manual).\n\nNote: the documentation builds fine from scratch, but I sometimes have trouble when adding these patches to an already built reference manual.",
    "created_at": "2013-05-01T17:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63035",
    "user": "Stefan"
}
```

Note: needs Sage 5.9.rc1 to build (because the package list is now generated automatically in setup.py, this used to be manual).

Note: the documentation builds fine from scratch, but I sometimes have trouble when adding these patches to an already built reference manual.



---

archive/issue_comments_063036.json:
```json
{
    "body": "This review will take a lifetime, but right now all I can say is that the code of `circuits`, `cocircuits`, `noncospanning_cocircuits`, and `nonspanning_circuits` look awfully similar.\n\nAnd there are some parts of the code that are commented out, like that\n\n```\n+# def bitset_pickle_test(data):                                                                                                                                                               \n+#     \"\"\"                                                                                                                                                                                     \n+#     Converts the list of integers ``data`` into a bitset, which gets pickled.                                                                                                               \n+#     \"\"\"                                                                                                                                                                                     \n+#     cdef bitset_t bs                                                                                                                                                                        \n+#     m = max(data)                                                                                                                                                                           \n+#     bitset_init(bs, m+1)                                                                                                                                                                    \n+#     bitset_clear(bs)                                                                                                                                                                        \n+#     for i in data:                                                                                                                                                                          \n+#         bitset_add(bs, i)                                                                                                                                                                   \n+#     p = bitset_pickle(bs)                                                                                                                                                                   \n+#     bitset_free(bs)                                                                                                                                                                         \n+#     return p              \n```\n\nOr 4 functions in the matroid catalog.\n\nNathann",
    "created_at": "2013-05-01T17:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63036",
    "user": "ncohen"
}
```

This review will take a lifetime, but right now all I can say is that the code of `circuits`, `cocircuits`, `noncospanning_cocircuits`, and `nonspanning_circuits` look awfully similar.

And there are some parts of the code that are commented out, like that

```
+# def bitset_pickle_test(data):                                                                                                                                                               
+#     """                                                                                                                                                                                     
+#     Converts the list of integers ``data`` into a bitset, which gets pickled.                                                                                                               
+#     """                                                                                                                                                                                     
+#     cdef bitset_t bs                                                                                                                                                                        
+#     m = max(data)                                                                                                                                                                           
+#     bitset_init(bs, m+1)                                                                                                                                                                    
+#     bitset_clear(bs)                                                                                                                                                                        
+#     for i in data:                                                                                                                                                                          
+#         bitset_add(bs, i)                                                                                                                                                                   
+#     p = bitset_pickle(bs)                                                                                                                                                                   
+#     bitset_free(bs)                                                                                                                                                                         
+#     return p              
```

Or 4 functions in the matroid catalog.

Nathann



---

archive/issue_comments_063037.json:
```json
{
    "body": "What do you mean by the comment that those functions look similar? They compute similar, but not identical, information from the matroid. And all four are useful to end users.\n\nI guess we should have gotten rid of commented out parts (though Sage has plenty of that floating around in its source). I'll revise that soon.",
    "created_at": "2013-05-01T18:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63037",
    "user": "Stefan"
}
```

What do you mean by the comment that those functions look similar? They compute similar, but not identical, information from the matroid. And all four are useful to end users.

I guess we should have gotten rid of commented out parts (though Sage has plenty of that floating around in its source). I'll revise that soon.



---

archive/issue_comments_063038.json:
```json
{
    "body": "Hellooooooo !\n\n> What do you mean by the comment that those functions look similar? They compute similar, but not identical, information from the matroid. And all four are useful to end users.\n\nNonono, of course you need them. I was just saying that perhaps there could have been an internal function computing all 4 things, exposed in 4 differents ways to the user. This way there is no copy/paste of code.\n\n> I guess we should have gotten rid of commented out parts (though Sage has plenty of that floating around in its source). I'll revise that soon.\n\nNonono I'm sorry I said that, I will give you lengthier reviews soon. Otherwise it will make you update the patch every day...  `:-)`\n\nNathann",
    "created_at": "2013-05-01T18:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63038",
    "user": "ncohen"
}
```

Hellooooooo !

> What do you mean by the comment that those functions look similar? They compute similar, but not identical, information from the matroid. And all four are useful to end users.

Nonono, of course you need them. I was just saying that perhaps there could have been an internal function computing all 4 things, exposed in 4 differents ways to the user. This way there is no copy/paste of code.

> I guess we should have gotten rid of commented out parts (though Sage has plenty of that floating around in its source). I'll revise that soon.

Nonono I'm sorry I said that, I will give you lengthier reviews soon. Otherwise it will make you update the patch every day...  `:-)`

Nathann



---

archive/issue_comments_063039.json:
```json
{
    "body": "Hellooooooooooo again !\n\nWell, I've been spending some time on that code, and I first have to say that it is awfully clean. I was a bit afraid that something developped outside of Sage would be more combinat-like, and that is not the case at all here.\n\nThe other thing is that, stupid as it may seem, I had not realized until a couple of minutes that I cannot realistically review 21 000 lines of code by myself. I mean, with a real job that I have to do, with 3 meals per day, everything. Looks complicated. This is one of the problems of developping everything for a while then trying to create a single patch out of it.\n\nI will be glad to spend time on that, and also to work with the code later, but yep, I guess that I cannot review 21 000 lines of code `:-)`\n\nI think that in this case, as the code looks preeeeetty clean and all, the best would really be to ask on sage-devel whether :\n1) We take it in without a review (as if it were a spkg, actually)\n2) Somebody (or many persons) are willing to review it together\n\nPerhaps it would also help if you were to say in your message how you produced this code. If many persons wrote that code, if many tried it...\n\nI think that I can't do more. Otherwise, I know that I will not set this to \"positive review\" before I am convinced that every single choice is a good one, or at least having asked about it. And after having thought for a while about each line, wondering if it is the best way to do it. I already spent weeks on easier reviews, and I know that I cannot do that one `:-)`\n\nNathann",
    "created_at": "2013-05-02T17:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63039",
    "user": "ncohen"
}
```

Hellooooooooooo again !

Well, I've been spending some time on that code, and I first have to say that it is awfully clean. I was a bit afraid that something developped outside of Sage would be more combinat-like, and that is not the case at all here.

The other thing is that, stupid as it may seem, I had not realized until a couple of minutes that I cannot realistically review 21 000 lines of code by myself. I mean, with a real job that I have to do, with 3 meals per day, everything. Looks complicated. This is one of the problems of developping everything for a while then trying to create a single patch out of it.

I will be glad to spend time on that, and also to work with the code later, but yep, I guess that I cannot review 21 000 lines of code `:-)`

I think that in this case, as the code looks preeeeetty clean and all, the best would really be to ask on sage-devel whether :
1) We take it in without a review (as if it were a spkg, actually)
2) Somebody (or many persons) are willing to review it together

Perhaps it would also help if you were to say in your message how you produced this code. If many persons wrote that code, if many tried it...

I think that I can't do more. Otherwise, I know that I will not set this to "positive review" before I am convinced that every single choice is a good one, or at least having asked about it. And after having thought for a while about each line, wondering if it is the best way to do it. I already spent weeks on easier reviews, and I know that I cannot do that one `:-)`

Nathann



---

archive/issue_comments_063040.json:
```json
{
    "body": "I fully understand that you can't - I know I couldn't! I'll post on sage-devel to ask what's to be done.\n\n--Stefan.",
    "created_at": "2013-05-02T18:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63040",
    "user": "Stefan"
}
```

I fully understand that you can't - I know I couldn't! I'll post on sage-devel to ask what's to be done.

--Stefan.



---

archive/issue_comments_063041.json:
```json
{
    "body": "Here are two alternate approaches to such a patch bomb.\n* Ask the authors to parcel it out into manageable chunks.  Given that they have their own bitbucket repository, hopefully it wouldn't be horribly difficult to separate out e.g. the examples, the core functionality, the extended functionality, and then make this a metaticket.\n* Have the authors partially review it for each other; if there are truly 3-5 separate developers, they may be able to vouch for each others' code.  I think in this case some non-matroid-project person such as Nathann should look at the overall structure, but I agree that doing it all together is nearly impossible.\n\nI, too, was very impressed with the general layout of this project; a lot of thought has gone into this.",
    "created_at": "2013-05-02T18:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63041",
    "user": "kcrisman"
}
```

Here are two alternate approaches to such a patch bomb.
* Ask the authors to parcel it out into manageable chunks.  Given that they have their own bitbucket repository, hopefully it wouldn't be horribly difficult to separate out e.g. the examples, the core functionality, the extended functionality, and then make this a metaticket.
* Have the authors partially review it for each other; if there are truly 3-5 separate developers, they may be able to vouch for each others' code.  I think in this case some non-matroid-project person such as Nathann should look at the overall structure, but I agree that doing it all together is nearly impossible.

I, too, was very impressed with the general layout of this project; a lot of thought has gone into this.



---

archive/issue_comments_063042.json:
```json
{
    "body": "Looks pretty solid. I think you can review the mathematical correctness among yourself. You should have somebody who is more familiar with Sageisms to look at code style, then it should be ready to go. There are some small code style issues that would have been easier if you had started with a smaller chunk of code.\n\nPEP8 whitespace http://www.python.org/dev/peps/pep-0008/#other-recommendations\n\n```\ni = i + 1   # yes\ni=i+1       # no\n```\n\n\nDocstring markup http://www.sagemath.org/doc/developer/conventions.html#docstring-markup-with-rest-and-sphinx:\n* `EXAMPLES::` not `EXAMPLE::` (though thats also misspelled in other places in the sage library)\n* Imperative: \"Test that foo is bar\" instead of \"Tests that foo is bar\".\n* `INPUT:` should include type information and our formatting:\n  {{{\n- ``n``: The dimension of the projective space.             # no\n- ``n`` -- positive integer. The dimension of the projective space.  # yes\n    }}}\n  * We have markup for referencing other docstrings\n    {{{\n... see :class:`OtherClass` ...\n... or :meth:`other_method` ...\n    }}}\n    that you might want to use more consistently.\n\nThe SetSystem should probably be factored out and integrated into `sage.sets`.\n\nYour private reimplementation of all matrix functionality has a lot of code-smell. If the only reason is that pivoting is too slow then you should look into fixing that instead of writing your own matrix implementation. \n\nWhats this (left-over debugging?):\n\n```\n  #if d>0: \n  #    F=Fa+Fb \n  #    self._q_projection=self._q_projection.matrix_from_rows_and_columns(F,F) \n```\n",
    "created_at": "2013-05-03T14:31:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63042",
    "user": "vbraun"
}
```

Looks pretty solid. I think you can review the mathematical correctness among yourself. You should have somebody who is more familiar with Sageisms to look at code style, then it should be ready to go. There are some small code style issues that would have been easier if you had started with a smaller chunk of code.

PEP8 whitespace http://www.python.org/dev/peps/pep-0008/#other-recommendations

```
i = i + 1   # yes
i=i+1       # no
```


Docstring markup http://www.sagemath.org/doc/developer/conventions.html#docstring-markup-with-rest-and-sphinx:
* `EXAMPLES::` not `EXAMPLE::` (though thats also misspelled in other places in the sage library)
* Imperative: "Test that foo is bar" instead of "Tests that foo is bar".
* `INPUT:` should include type information and our formatting:
  {{{
- ``n``: The dimension of the projective space.             # no
- ``n`` -- positive integer. The dimension of the projective space.  # yes
    }}}
  * We have markup for referencing other docstrings
    {{{
... see :class:`OtherClass` ...
... or :meth:`other_method` ...
    }}}
    that you might want to use more consistently.

The SetSystem should probably be factored out and integrated into `sage.sets`.

Your private reimplementation of all matrix functionality has a lot of code-smell. If the only reason is that pivoting is too slow then you should look into fixing that instead of writing your own matrix implementation. 

Whats this (left-over debugging?):

```
  #if d>0: 
  #    F=Fa+Fb 
  #    self._q_projection=self._q_projection.matrix_from_rows_and_columns(F,F) 
```




---

archive/issue_comments_063043.json:
```json
{
    "body": "This looks wildly useful, not just for educational purposes. I always wanted to play around with the matroid Hopf algebra, for example...\n\nThe remarks below are mostly random and not always to the point. Most of the code is beyound my grasp due to the use of Cython and bitsets and partly due to advanced matroid theory. I'm just looking at random points which seem relevant and/or understandable to me.\n\nWhat does this mean:\n\n```\nIt is up to the child class to update its data structure make information  \nrelative to the new basis more accessible. \n```\n\n\nTypo \"an an\":\n\n```\nif `I` is covered by a matching an an appropriate bipartite graph\n```\n\nThat said, \"covered by\" might be useless, given that you're not saying \"maximum matching\".\n\nIn the next line, do you really mean \"maximal matching\", or rather \"maximum matching\"? (I don't know what you want.)\n\nTypo \"Compute a the rank\". Also, look out for \"the the\" errors, you got 2 of them.\n\nAny chances to get some comments on `cdef  __fundamental_cocircuit` and `cdef  __fundamental_circuit`? I can't say the code is self-explanatory... Is the \"fundamental circuit\" of a basis B and an element y the set of all elements of B that could be replaced by y, united with {y}? I see why this is a circuit (when y is not in B, that is) but I haven't seen this notation used anywhere...\n\nMissing \"of\" in \"of the flats the matroid\" and in \"of the coflats the matroid\". Also, typos: \"wheter\", \"distinguised\", \"commom\".\n\nDoes the docstring of `cpdef _augment(self, X, Y):` want to say something like \"nonempty (if possible) subset `I`\" or \"maximum subset `I`\"? Just a subset is a bit boring...\n\nIs matroid union implemented? I can't find it in the code...\n\nThe \"if\" in \"with the property that if no modular triple of hyperplanes has exactly two members in the modular cut\" looks out of place. Incidentally, a definition of the notion of \"hyperplane\" would be of use, too; I didn't know of that notion so far.\n\nThe `max_weight_independent` method raises an error if the ground set is empty and the weights keyword is set, something that might happen in practice in recursive definitions:\n\n```\nsage: M = matroids.Uniform(0,0)            \nsage: wt = {}                             \nsage: M.max_weight_independent(weights=wt)\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n<ipython-input-10-89b2ef4dae56> in <module>()\n----> 1 M.max_weight_independent(weights=wt)\n\n/home/darij/sage-5.9/local/lib/python2.7/site-packages/sage/matroids/matroid.so in sage.matroids.matroid.Matroid.max_weight_independent (sage/matroids/matroid.c:25219)()\n\n/home/darij/sage-5.9/local/lib/python2.7/site-packages/sage/matroids/matroid.so in sage.matroids.matroid.Matroid.max_weight_independent (sage/matroids/matroid.c:24847)()\n\nIndexError: list index out of range\n```\n\n\nThis is due to the `if wt[-1][1] < 0:` line, of course. Same for `max_weight_coindependent`.\n\nThis just looks weird:\n\n```\n                if self.full_rank()==0: \n\t            return True             \n\t        if self.full_rank()==0 or self.full_corank()==0: \n\t            return True  \n```\n\n\nOne of the A's should probably be an Atranspose in:\n\n```\n                If the matroid is represented by `[I_1 A]`, then the dual is represented by `[-A I_2]` for appropriately sized \n\t        identity matrices `I_1, I_2`. \n```\n\n(The minus sign, on the other hand, I don't see the reason for...)\n\nFeature suggestion, if not already implemented: a method to test if a given weight function is generic, i. e., has exactly one maximizing basis. Of course, this is easy thanks to the exchange graph, as one only needs to find a maximizing basis and then check that all its exchange neighbours have strictly smaller weight. This function is useful to some Hopf-algebraic constructions.",
    "created_at": "2013-05-11T06:34:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63043",
    "user": "darij"
}
```

This looks wildly useful, not just for educational purposes. I always wanted to play around with the matroid Hopf algebra, for example...

The remarks below are mostly random and not always to the point. Most of the code is beyound my grasp due to the use of Cython and bitsets and partly due to advanced matroid theory. I'm just looking at random points which seem relevant and/or understandable to me.

What does this mean:

```
It is up to the child class to update its data structure make information  
relative to the new basis more accessible. 
```


Typo "an an":

```
if `I` is covered by a matching an an appropriate bipartite graph
```

That said, "covered by" might be useless, given that you're not saying "maximum matching".

In the next line, do you really mean "maximal matching", or rather "maximum matching"? (I don't know what you want.)

Typo "Compute a the rank". Also, look out for "the the" errors, you got 2 of them.

Any chances to get some comments on `cdef  __fundamental_cocircuit` and `cdef  __fundamental_circuit`? I can't say the code is self-explanatory... Is the "fundamental circuit" of a basis B and an element y the set of all elements of B that could be replaced by y, united with {y}? I see why this is a circuit (when y is not in B, that is) but I haven't seen this notation used anywhere...

Missing "of" in "of the flats the matroid" and in "of the coflats the matroid". Also, typos: "wheter", "distinguised", "commom".

Does the docstring of `cpdef _augment(self, X, Y):` want to say something like "nonempty (if possible) subset `I`" or "maximum subset `I`"? Just a subset is a bit boring...

Is matroid union implemented? I can't find it in the code...

The "if" in "with the property that if no modular triple of hyperplanes has exactly two members in the modular cut" looks out of place. Incidentally, a definition of the notion of "hyperplane" would be of use, too; I didn't know of that notion so far.

The `max_weight_independent` method raises an error if the ground set is empty and the weights keyword is set, something that might happen in practice in recursive definitions:

```
sage: M = matroids.Uniform(0,0)            
sage: wt = {}                             
sage: M.max_weight_independent(weights=wt)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-10-89b2ef4dae56> in <module>()
----> 1 M.max_weight_independent(weights=wt)

/home/darij/sage-5.9/local/lib/python2.7/site-packages/sage/matroids/matroid.so in sage.matroids.matroid.Matroid.max_weight_independent (sage/matroids/matroid.c:25219)()

/home/darij/sage-5.9/local/lib/python2.7/site-packages/sage/matroids/matroid.so in sage.matroids.matroid.Matroid.max_weight_independent (sage/matroids/matroid.c:24847)()

IndexError: list index out of range
```


This is due to the `if wt[-1][1] < 0:` line, of course. Same for `max_weight_coindependent`.

This just looks weird:

```
                if self.full_rank()==0: 
	            return True             
	        if self.full_rank()==0 or self.full_corank()==0: 
	            return True  
```


One of the A's should probably be an Atranspose in:

```
                If the matroid is represented by `[I_1 A]`, then the dual is represented by `[-A I_2]` for appropriately sized 
	        identity matrices `I_1, I_2`. 
```

(The minus sign, on the other hand, I don't see the reason for...)

Feature suggestion, if not already implemented: a method to test if a given weight function is generic, i. e., has exactly one maximizing basis. Of course, this is easy thanks to the exchange graph, as one only needs to find a maximizing basis and then check that all its exchange neighbours have strictly smaller weight. This function is useful to some Hopf-algebraic constructions.



---

archive/issue_comments_063044.json:
```json
{
    "body": "Thanks for all your kind words, and for your suggestions! Michael Welsh and I worked on them, and the improved code is now on the ticket. Below I'll address your concerns one by one.\n\nTo ncohenn:\n\n- Similar code for circuits(), cocircuits(), nonspanning_circuits(), nonspanning_cocircuits().\n  Organizing the code into a common, abstract function is not worth the trouble, in my opinion.\n  It will be hard to do so without incurring a speed loss in these exponential-in-the-worst-case\n  methods.\n- Lingering commented-out code from development has been removed.\n\nTo vbraun:\n\n- PEP8 compliance has been achieved, except for line lengths.\n- Docstring markup should be much closer to Sage's standards (we use imperatives everywhere, EXAMPLES is plural, INPUT, OUTPUT singular. I did not revisit all inputs to see if they specify type clearly, and did not work on\n  referencing markup).\n- SetSystem has twofold functionality right now. It serves as return type for methods like circuits(). We plan to change this in the future: the \"yield\" keyword did not work in Cython when we started out.\n  The other function is partition refinement for isomorphism testing. This is mostly of internal use, and makes use of some tweaks. I think a revised SetSystem definitely has its place in sage.sets, but our current effort is\n  not nearly polished enough, and is best kept for internal use by the Matroid code.\n- Matrix functionality: touching Sage's matrix code was daunting: finite field matrices seem to use floating-point implementations, and I did not want to risk speed regressions elsewhere in Sage. I'm following the M4R1\n  and related efforts with interest, and once they are viable, moving our code back to them is easy enough.\n\nTo darij\n\n- We want this code to be useful enough, and fast enough, to answer our research questions. These questions routinely generate and compare hundreds of thousands matroids, so\n  we aimed for efficiency that matches the best C code out there (Macek and Gordon Royle's private code). We're not there in all methods, but our binary matroids and our isomorphism\n  test are really fast.\n- I added an example to the description of BasisExchangeMatroid to clarify what a child class might do.\n- I expanded the description of the (not yet implemented) class TransversalMatroid a little.\n- I fixed the typos mentioned.\n- Yes, \"augment\" will return the maximal such set.\n- The B-fundamental circuit of e is the unique circuit contained in B+e. This is standard terminology in matroid theory. I added a line to the method explaining this. I was somewhat surprised that we have no user-facing\n  version of it, but that'll be for a later trac ticket.\n- The B-fundamental cocircuit of e is the unique cocircuit meeting B only in e. This is the dual notion of the previous item.\n- Matroid union is on my wish list. Again, a later trac ticket.\n- I added a definition of hyperplane, and removed the offending \"if\".\n- Added an extra check to max_weight_independent and max_weight_coindependent (and two doctests covering this case)\n- Removed the double check on self.full_rank()\n- Added the transpose. The minus sign is to ensure the row spaces of the matrices are orthogonal complements of each other.\n- Feature suggestion: I suggest opening a trac ticket. Do you want just True or False, or a list of all maximizing bases? Maybe an option to max_weight_independent would suffice (e.g. find_all=False)? Oh, wait, that is\n  expensive to compute when the weight function is constant.",
    "created_at": "2013-05-13T14:44:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63044",
    "user": "Stefan"
}
```

Thanks for all your kind words, and for your suggestions! Michael Welsh and I worked on them, and the improved code is now on the ticket. Below I'll address your concerns one by one.

To ncohenn:

- Similar code for circuits(), cocircuits(), nonspanning_circuits(), nonspanning_cocircuits().
  Organizing the code into a common, abstract function is not worth the trouble, in my opinion.
  It will be hard to do so without incurring a speed loss in these exponential-in-the-worst-case
  methods.
- Lingering commented-out code from development has been removed.

To vbraun:

- PEP8 compliance has been achieved, except for line lengths.
- Docstring markup should be much closer to Sage's standards (we use imperatives everywhere, EXAMPLES is plural, INPUT, OUTPUT singular. I did not revisit all inputs to see if they specify type clearly, and did not work on
  referencing markup).
- SetSystem has twofold functionality right now. It serves as return type for methods like circuits(). We plan to change this in the future: the "yield" keyword did not work in Cython when we started out.
  The other function is partition refinement for isomorphism testing. This is mostly of internal use, and makes use of some tweaks. I think a revised SetSystem definitely has its place in sage.sets, but our current effort is
  not nearly polished enough, and is best kept for internal use by the Matroid code.
- Matrix functionality: touching Sage's matrix code was daunting: finite field matrices seem to use floating-point implementations, and I did not want to risk speed regressions elsewhere in Sage. I'm following the M4R1
  and related efforts with interest, and once they are viable, moving our code back to them is easy enough.

To darij

- We want this code to be useful enough, and fast enough, to answer our research questions. These questions routinely generate and compare hundreds of thousands matroids, so
  we aimed for efficiency that matches the best C code out there (Macek and Gordon Royle's private code). We're not there in all methods, but our binary matroids and our isomorphism
  test are really fast.
- I added an example to the description of BasisExchangeMatroid to clarify what a child class might do.
- I expanded the description of the (not yet implemented) class TransversalMatroid a little.
- I fixed the typos mentioned.
- Yes, "augment" will return the maximal such set.
- The B-fundamental circuit of e is the unique circuit contained in B+e. This is standard terminology in matroid theory. I added a line to the method explaining this. I was somewhat surprised that we have no user-facing
  version of it, but that'll be for a later trac ticket.
- The B-fundamental cocircuit of e is the unique cocircuit meeting B only in e. This is the dual notion of the previous item.
- Matroid union is on my wish list. Again, a later trac ticket.
- I added a definition of hyperplane, and removed the offending "if".
- Added an extra check to max_weight_independent and max_weight_coindependent (and two doctests covering this case)
- Removed the double check on self.full_rank()
- Added the transpose. The minus sign is to ensure the row spaces of the matrices are orthogonal complements of each other.
- Feature suggestion: I suggest opening a trac ticket. Do you want just True or False, or a list of all maximizing bases? Maybe an option to max_weight_independent would suffice (e.g. find_all=False)? Oh, wait, that is
  expensive to compute when the weight function is constant.



---

archive/issue_comments_063045.json:
```json
{
    "body": "Thanks for the answers! As for the maximizing bases, I just wanted a True or False; that alone should not be expensive.\n\nI shouldn't be burdening you with additional work; I would normally be adding those methods myself if it wasn't for cython (the bitsets scared me as well, but that turned out to be unfounded). If you want people to add functionality, maybe you could document the internal functions better, such as `__move_current_basis` (not obvious from the title what it does; the same function with only 1 underscore is well-documented), and explain what the pattern behind 2 underscores vs. 1 underscores is (I guess 2-underscore functions take bitsets as input whereas 1-underscore ones use python types?). The doc of `nxksrd` is too brief; it suggests that the function returns the next k-subset, while apparently what it does is transforming the k-subset in place and returning something that is more like an error code. But take these suggestions with a grain of salt, as I'm not exactly an experienced programmer...\n\nA few things you might still want to fix (sorry for not mentioning them earlier):\n\n- You write `# the engine` twice in `basis_exchange_matroid.pyx` (once on line 199 and again on line 276). A bit confusing ;)\n\n- The docstring of method `_with_coloop` incorrectly states that the input is \"Nothing\".\n\n- Typos \"succesively\" and \"distinguised\".\n\nOn an unrelated note: WTF our finite field matrices use floating-point algorithms???",
    "created_at": "2013-05-14T00:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63045",
    "user": "darij"
}
```

Thanks for the answers! As for the maximizing bases, I just wanted a True or False; that alone should not be expensive.

I shouldn't be burdening you with additional work; I would normally be adding those methods myself if it wasn't for cython (the bitsets scared me as well, but that turned out to be unfounded). If you want people to add functionality, maybe you could document the internal functions better, such as `__move_current_basis` (not obvious from the title what it does; the same function with only 1 underscore is well-documented), and explain what the pattern behind 2 underscores vs. 1 underscores is (I guess 2-underscore functions take bitsets as input whereas 1-underscore ones use python types?). The doc of `nxksrd` is too brief; it suggests that the function returns the next k-subset, while apparently what it does is transforming the k-subset in place and returning something that is more like an error code. But take these suggestions with a grain of salt, as I'm not exactly an experienced programmer...

A few things you might still want to fix (sorry for not mentioning them earlier):

- You write `# the engine` twice in `basis_exchange_matroid.pyx` (once on line 199 and again on line 276). A bit confusing ;)

- The docstring of method `_with_coloop` incorrectly states that the input is "Nothing".

- Typos "succesively" and "distinguised".

On an unrelated note: WTF our finite field matrices use floating-point algorithms???



---

archive/issue_comments_063046.json:
```json
{
    "body": "I think you started studying the code in the wrong file. The main entry point is matroid.pyx. This is an abstract class of which all others derive. It implements all functionality in terms of just the rank function (ok... it'll convert to BasisMatroid for things like isomorphism testing). It should be fairly straightforward, and the code does not swerve far from pure Python.\n\nBasisExchangeMatroid is a common framework for BasisMatroid and LinearMatroid. Internally the groundset is translated to a list of integers, which are used for bitset indexing. So we have\n\n* regular methods. User-facing, expected to be careful with input checking.\n* underscored methods. May assume properties regarding their input (type is frozenset, elements are from groundset, two sets are disjoint, ...)\n* doubly underscored methods. Very internal use (usually cdef). Use the encoded version of the groundset, and may have bitset arguments into which the return value is copied.\n\nI think most people who will be adding code, will not move beyond the first underscore (things like union() belong in the generic Matroid class anyway). But certainly the cdef methods deserve a little bit of an explanation.\n\nAnd yes:\n\n```\nsage: A = Matrix(GF(7), [[1,0,1,1],[0,1,1,2]])\nsage: type(A)\nsage.matrix.matrix_modn_dense_float.Matrix_modn_dense_float\n```\n\nIn our matroid code we store the entries simply as a list of GF(q) elements, with some splicing commands for row operations. Results in a 10- to 20-time speedup in places. It's weird.\n\nI hope I'll get around to doing the further edits soon!",
    "created_at": "2013-05-14T02:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63046",
    "user": "Stefan"
}
```

I think you started studying the code in the wrong file. The main entry point is matroid.pyx. This is an abstract class of which all others derive. It implements all functionality in terms of just the rank function (ok... it'll convert to BasisMatroid for things like isomorphism testing). It should be fairly straightforward, and the code does not swerve far from pure Python.

BasisExchangeMatroid is a common framework for BasisMatroid and LinearMatroid. Internally the groundset is translated to a list of integers, which are used for bitset indexing. So we have

* regular methods. User-facing, expected to be careful with input checking.
* underscored methods. May assume properties regarding their input (type is frozenset, elements are from groundset, two sets are disjoint, ...)
* doubly underscored methods. Very internal use (usually cdef). Use the encoded version of the groundset, and may have bitset arguments into which the return value is copied.

I think most people who will be adding code, will not move beyond the first underscore (things like union() belong in the generic Matroid class anyway). But certainly the cdef methods deserve a little bit of an explanation.

And yes:

```
sage: A = Matrix(GF(7), [[1,0,1,1],[0,1,1,2]])
sage: type(A)
sage.matrix.matrix_modn_dense_float.Matrix_modn_dense_float
```

In our matroid code we store the entries simply as a list of GF(q) elements, with some splicing commands for row operations. Results in a 10- to 20-time speedup in places. It's weird.

I hope I'll get around to doing the further edits soon!



---

archive/issue_comments_063047.json:
```json
{
    "body": "Can you be more specific about which matrix functions are slow? And yes, it is intentional that matrices over certain finite fields are stored as floats --- with SSE you can do 4 float operations in one instruction.",
    "created_at": "2013-05-14T11:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63047",
    "user": "vbraun"
}
```

Can you be more specific about which matrix functions are slow? And yes, it is intentional that matrices over certain finite fields are stored as floats --- with SSE you can do 4 float operations in one instruction.



---

archive/issue_comments_063048.json:
```json
{
    "body": "vbraun: specifically, operations where the entries of the matrix (over GF(7), say) are changed frequently, if my memory serves me right. I'll come up with some speed tests in a week or two, but right now I'm overwhelmed with work and life.\n\nAlso: it looks like there are segmentation faults reported by the patchbot... I knew some things broke after Nathann's work on designs, will have to fix that.",
    "created_at": "2013-05-17T21:45:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63048",
    "user": "Stefan"
}
```

vbraun: specifically, operations where the entries of the matrix (over GF(7), say) are changed frequently, if my memory serves me right. I'll come up with some speed tests in a week or two, but right now I'm overwhelmed with work and life.

Also: it looks like there are segmentation faults reported by the patchbot... I knew some things broke after Nathann's work on designs, will have to fix that.



---

archive/issue_comments_063049.json:
```json
{
    "body": "I posted some info on slow matrix functions on https://groups.google.com/d/topic/sage-devel/5PdRIUic2Es/discussion\n\nAnd the example is not contrived: we genuinely saw a 10- to 20-fold speedup in the LinearMatroid performance.",
    "created_at": "2013-05-20T19:14:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63049",
    "user": "Stefan"
}
```

I posted some info on slow matrix functions on https://groups.google.com/d/topic/sage-devel/5PdRIUic2Es/discussion

And the example is not contrived: we genuinely saw a 10- to 20-fold speedup in the LinearMatroid performance.



---

archive/issue_comments_063050.json:
```json
{
    "body": "I spent a good chunk of the afternoon looking over the documentation and wrestling with `intersphinx`.\n\nFollowing are all pretty routine, though maybe the messages from exceptions needs discussion.  Second post is about more mysterious stuff.\n\nI'm doing\n\n\n```\nsage -docbuild reference html\n```\n\n\nand might turn to PDF output once this is settled.  I'd be happy to ride herd on documentation as part of a group review.  By and large, it looks excellent - I like many of the extras, like a discussion on subclassing and accurate synopses and lists at the top of modules.  Nits:\n\n(1) Set up code in the small patch all looks routine to my eye (except see next post).  I have some experience with this, but will not say I am expert at it, so a second look is probably in order.  (Interesting to see how little is actually required to add in a whole new field.)  On the downside, having \"matroid\" at the top level is now going to make it harder to auto-complete the top-level \"matrix\" at the command line.  ;-)\n\n(2) In \"Creating mew Matroid subclasses\": \"For incidental use, the RankMatroid subclass.\" needs another \"use\"?\n\n(3) In documentation of matroid.is_isomorphism() the EXAMPLES all have an extra indent.  Again with matroid.minor, matroid.equals.  You might troll for more of these across all modules.\n\n(4) I see \"MatroidError\" instances in the documentation, specifically here at matroid.max_independent.  Is there a precedent for custom exceptions elsewhere in Sage?  More commonly errors are TypeError or ValueError it seems to me.  (Yes, PEP8 says differently.)  And I find the \"Problem with a matroid operation:\" redundant.  I believe it is a Python convention to have error messages begin with a lower case, to follow the colon (but cannot find a reference for this).\n\nI'd be inclined to replace\n\n\n```\nMatroidError: Problem with a matroid operation: 'Input is not a subset of the groundset.'\n```\n\n\nwith something like\n\n\n```\nValueError: 'input set is not a subset of the groundset.'\n```\n\n\nEven better is to repeat the problem input in the error message.  Here:\n\n\n```\nValueError: 'input set ['x'] is not a subset of the groundset.'\n```\n\n\n\nThere is usually enough context provided automatically, but echioing the bad input is often very helpful.  Also consider making the text of error messages somewhat unique, so that searches will land a user at the right place in the reference manual.  \n\n\n(5) Apparently-minor documentation warnings follow.  Should be trivial to fix.\n\n\n```\n[matroids ] /sage/sage-5.10.beta4/local/lib/python2.7/site-packages/sage/matroids/catalog.py:docstring of sage.matroids.catalog.NonVamos:3: WARNING: Inline interpreted text or phrase reference start-string without end-string.\n[matroids ] /sage/sage-5.10.beta4/local/lib/python2.7/site-packages/sage/matroids/catalog.py:docstring of sage.matroids.catalog.P8pp:1: WARNING: Inline interpreted text or phrase reference start-string without end-string.\n[matroids ] /sage/sage-5.10.beta4/local/lib/python2.7/site-packages/sage/matroids/catalog.py:docstring of sage.matroids.catalog.P8pp:1: WARNING: Inline interpreted text or phrase reference start-string without end-string.\n[matroids ] <autodoc>:0: WARNING: Bullet list ends without a blank line; unexpected unindent.\n```\n",
    "created_at": "2013-05-25T00:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63050",
    "user": "rbeezer"
}
```

I spent a good chunk of the afternoon looking over the documentation and wrestling with `intersphinx`.

Following are all pretty routine, though maybe the messages from exceptions needs discussion.  Second post is about more mysterious stuff.

I'm doing


```
sage -docbuild reference html
```


and might turn to PDF output once this is settled.  I'd be happy to ride herd on documentation as part of a group review.  By and large, it looks excellent - I like many of the extras, like a discussion on subclassing and accurate synopses and lists at the top of modules.  Nits:

(1) Set up code in the small patch all looks routine to my eye (except see next post).  I have some experience with this, but will not say I am expert at it, so a second look is probably in order.  (Interesting to see how little is actually required to add in a whole new field.)  On the downside, having "matroid" at the top level is now going to make it harder to auto-complete the top-level "matrix" at the command line.  ;-)

(2) In "Creating mew Matroid subclasses": "For incidental use, the RankMatroid subclass." needs another "use"?

(3) In documentation of matroid.is_isomorphism() the EXAMPLES all have an extra indent.  Again with matroid.minor, matroid.equals.  You might troll for more of these across all modules.

(4) I see "MatroidError" instances in the documentation, specifically here at matroid.max_independent.  Is there a precedent for custom exceptions elsewhere in Sage?  More commonly errors are TypeError or ValueError it seems to me.  (Yes, PEP8 says differently.)  And I find the "Problem with a matroid operation:" redundant.  I believe it is a Python convention to have error messages begin with a lower case, to follow the colon (but cannot find a reference for this).

I'd be inclined to replace


```
MatroidError: Problem with a matroid operation: 'Input is not a subset of the groundset.'
```


with something like


```
ValueError: 'input set is not a subset of the groundset.'
```


Even better is to repeat the problem input in the error message.  Here:


```
ValueError: 'input set ['x'] is not a subset of the groundset.'
```



There is usually enough context provided automatically, but echioing the bad input is often very helpful.  Also consider making the text of error messages somewhat unique, so that searches will land a user at the right place in the reference manual.  


(5) Apparently-minor documentation warnings follow.  Should be trivial to fix.


```
[matroids ] /sage/sage-5.10.beta4/local/lib/python2.7/site-packages/sage/matroids/catalog.py:docstring of sage.matroids.catalog.NonVamos:3: WARNING: Inline interpreted text or phrase reference start-string without end-string.
[matroids ] /sage/sage-5.10.beta4/local/lib/python2.7/site-packages/sage/matroids/catalog.py:docstring of sage.matroids.catalog.P8pp:1: WARNING: Inline interpreted text or phrase reference start-string without end-string.
[matroids ] /sage/sage-5.10.beta4/local/lib/python2.7/site-packages/sage/matroids/catalog.py:docstring of sage.matroids.catalog.P8pp:1: WARNING: Inline interpreted text or phrase reference start-string without end-string.
[matroids ] <autodoc>:0: WARNING: Bullet list ends without a blank line; unexpected unindent.
```




---

archive/issue_comments_063051.json:
```json
{
    "body": "Some errors with building the HTML documentation follow.  I think this is from using intersphinx, but am not certain.  Perhaps also related to the `conf.py` files.  I'll ping John Palmieri off-list to see if he wants to take a look.  On 5.10.beta2, but very similar behaviour on 5.10.beta4.\n\nTwo files in `devel/sage/doc/en/reference`:  `conf.py` and `conf_sub.py`.  The first has a long list of top-level sections of the documentation.  But to my eye it seems we use the second and not the first (and setup patch here also seems to reference the second).\n\nI added `'matroids'` to the first and tried rebuilding (two passes).  Then tried rebuilding with \n\n`sage -docbuild reference html -S -aE`\n\nwhich my notes say will for a rebuild from scratch.  \n\nHere are the symptoms I'm trying to fix.  Many many of these, and indeed the `objects.inv` is not created for the matroids section.\n\n\n```\n[homology ] WARNING: intersphinx inventory '/sage/sage-5.10.beta2/devel/sage/doc/output/html/en/reference/matroids/objects.inv' not fetchable due to <type 'exceptions.IOError'>: [Errno 2] No such file or directory: '/sage/sage-5.10.beta2/devel/sage/doc/output/html/en/reference/matroids/objects.inv'\n```\n\n\nI get about seven of these.  Perhaps it is due to cdef'ed class definitions.  That is a guess.  However, limited Googling suggests this can be fixed with a proper `conf.py`, so maybe another symptom of the same problem.  For each file/module, it seem severe enough to keep the whole module's worth of documentation from rendering at all - there is just a title, and no real content.\n\n\n```\n[reference] /sage/sage-5.10.beta2/devel/sage/doc/en/reference/matroids/sage/matroids/basis_exchange_matroid.rst:11: WARNING: autodoc can't import/find module 'sage.matroids.basis_exchange_matroid', it reported error: \"'module' object has no attribute 'BasisExchangeMatroid'\", please check your spelling and sys.path\n```\n",
    "created_at": "2013-05-25T00:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63051",
    "user": "rbeezer"
}
```

Some errors with building the HTML documentation follow.  I think this is from using intersphinx, but am not certain.  Perhaps also related to the `conf.py` files.  I'll ping John Palmieri off-list to see if he wants to take a look.  On 5.10.beta2, but very similar behaviour on 5.10.beta4.

Two files in `devel/sage/doc/en/reference`:  `conf.py` and `conf_sub.py`.  The first has a long list of top-level sections of the documentation.  But to my eye it seems we use the second and not the first (and setup patch here also seems to reference the second).

I added `'matroids'` to the first and tried rebuilding (two passes).  Then tried rebuilding with 

`sage -docbuild reference html -S -aE`

which my notes say will for a rebuild from scratch.  

Here are the symptoms I'm trying to fix.  Many many of these, and indeed the `objects.inv` is not created for the matroids section.


```
[homology ] WARNING: intersphinx inventory '/sage/sage-5.10.beta2/devel/sage/doc/output/html/en/reference/matroids/objects.inv' not fetchable due to <type 'exceptions.IOError'>: [Errno 2] No such file or directory: '/sage/sage-5.10.beta2/devel/sage/doc/output/html/en/reference/matroids/objects.inv'
```


I get about seven of these.  Perhaps it is due to cdef'ed class definitions.  That is a guess.  However, limited Googling suggests this can be fixed with a proper `conf.py`, so maybe another symptom of the same problem.  For each file/module, it seem severe enough to keep the whole module's worth of documentation from rendering at all - there is just a title, and no real content.


```
[reference] /sage/sage-5.10.beta2/devel/sage/doc/en/reference/matroids/sage/matroids/basis_exchange_matroid.rst:11: WARNING: autodoc can't import/find module 'sage.matroids.basis_exchange_matroid', it reported error: "'module' object has no attribute 'BasisExchangeMatroid'", please check your spelling and sys.path
```




---

archive/issue_comments_063052.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-05-25T00:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63052",
    "user": "Stefan"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063053.json:
```json
{
    "body": "Hi,\n\nI've had trouble building the documentation. I guess adding an extra folder is not easily accounted for. My recipe was\n\n* delete the doc/output directory\n* delete all auto-generated content in doc/en/reference/matroids\n* do a \"make doc\"\n\nI'll get to the other issues mentioned soon.",
    "created_at": "2013-05-25T00:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63053",
    "user": "Stefan"
}
```

Hi,

I've had trouble building the documentation. I guess adding an extra folder is not easily accounted for. My recipe was

* delete the doc/output directory
* delete all auto-generated content in doc/en/reference/matroids
* do a "make doc"

I'll get to the other issues mentioned soon.



---

archive/issue_comments_063054.json:
```json
{
    "body": "Hey Rob,\n\nIt's saying it can't find that file `/sage/sage-5.10.beta2/devel/sage/doc/output/html/en/reference/matroids/objects.inv`. It probably doesn't exist. When doing top-level doc stuff, I always run\n\n```\nsage -docbuild all html\n```\n\nI'd try that first.\n\nAlso I'm somewhat scared of deleting the entire output directory now. I once did that and consistently got the error your is getting, even doing `docbuild all` (I ended up reinstalling sage, but that's more because I wanted to upgrade anyways.) Perhaps `make doc` does a few extra things then `docbuild all` does...?\n\nStefan,\n\nThe bullet points need to be formatted like this:\n\n```\nSome text saying a list:\n\n- the first level, note the blank line\n- but this needs a sublist:\n\n  - Note the indentation and the blank line inbetween.\n\n- A line which needs a break\n  will go like this.\n```\n\nI believe that should take care of the sphinx errors.\n\nBest,\n\nTravis",
    "created_at": "2013-05-25T02:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63054",
    "user": "tscrim"
}
```

Hey Rob,

It's saying it can't find that file `/sage/sage-5.10.beta2/devel/sage/doc/output/html/en/reference/matroids/objects.inv`. It probably doesn't exist. When doing top-level doc stuff, I always run

```
sage -docbuild all html
```

I'd try that first.

Also I'm somewhat scared of deleting the entire output directory now. I once did that and consistently got the error your is getting, even doing `docbuild all` (I ended up reinstalling sage, but that's more because I wanted to upgrade anyways.) Perhaps `make doc` does a few extra things then `docbuild all` does...?

Stefan,

The bullet points need to be formatted like this:

```
Some text saying a list:

- the first level, note the blank line
- but this needs a sublist:

  - Note the indentation and the blank line inbetween.

- A line which needs a break
  will go like this.
```

I believe that should take care of the sphinx errors.

Best,

Travis



---

archive/issue_comments_063055.json:
```json
{
    "body": "Dear Travis,\n\nThanks for the suggestions.\n\nReplying to [comment:34 tscrim]:\n> {{{\n> sage -docbuild all html\n> }}}\n> I'd try that first.\n\nThat's looking much better!  And without editing a `conf.py`  I'll take it up more seriously in the morning.\n\n> Also I'm somewhat scared of deleting the entire output directory now. I once did that and consistently got the error your is getting, even doing `docbuild all` (I ended up reinstalling sage, but that's more because I wanted to upgrade anyways.) Perhaps `make doc` does a few extra things then `docbuild all` does...?\n\nWell, I just nuked all of `doc/output` to make it rebuild and it seems to have run fine.  Again, I'll double-check in the AM.  I wonder what is different, and what needs to change to get `-docbuild` to just do one part of the docs?\n\nThanks,\nRob",
    "created_at": "2013-05-25T03:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63055",
    "user": "rbeezer"
}
```

Dear Travis,

Thanks for the suggestions.

Replying to [comment:34 tscrim]:
> {{{
> sage -docbuild all html
> }}}
> I'd try that first.

That's looking much better!  And without editing a `conf.py`  I'll take it up more seriously in the morning.

> Also I'm somewhat scared of deleting the entire output directory now. I once did that and consistently got the error your is getting, even doing `docbuild all` (I ended up reinstalling sage, but that's more because I wanted to upgrade anyways.) Perhaps `make doc` does a few extra things then `docbuild all` does...?

Well, I just nuked all of `doc/output` to make it rebuild and it seems to have run fine.  Again, I'll double-check in the AM.  I wonder what is different, and what needs to change to get `-docbuild` to just do one part of the docs?

Thanks,
Rob



---

archive/issue_comments_063056.json:
```json
{
    "body": "Deleting doc/output is supposed to work, I do it all the time and its works fine. There might have been bugs in specific older Sage versions, though ;-)",
    "created_at": "2013-05-25T10:40:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63056",
    "user": "vbraun"
}
```

Deleting doc/output is supposed to work, I do it all the time and its works fine. There might have been bugs in specific older Sage versions, though ;-)



---

archive/issue_comments_063057.json:
```json
{
    "body": "Reading more of the code, is there a reason for why the bitset enhancements don't go into `sage.misc.bitset`? They seem to be useful enough, so why hide it in the matroid directory?",
    "created_at": "2013-05-26T10:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63057",
    "user": "vbraun"
}
```

Reading more of the code, is there a reason for why the bitset enhancements don't go into `sage.misc.bitset`? They seem to be useful enough, so why hide it in the matroid directory?



---

archive/issue_comments_063058.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-05-28T22:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63058",
    "user": "Stefan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063059.json:
```json
{
    "body": "I just uploaded a new version of the patch. I tested it against 5.10.beta4, I hope it didn't break on 5.10.beta5... \n\nItems fixed:\n\n* Fixed multiline doctests to have ....:\n\nResponding to darij:\n\n* Improved documentation of cdef methods (especially doubly-underscored ones)\n* Corrected _with_coloop docstring\n* Corrected typos\n\nResponding to rbeezer:\n\n* Fixed (2)\n* Fixed EXAMPLES indentation (3)\n* Got rid of MatroidError, made error messages lower case. Did not change content of messages, leaving it for future improvements (4)\n* Fixed the documentation (5)\n\nResponding to vbraun (some comments are replies to issues from sage-devel):\n\n* I'm happy to move the bitset enhancements into the rest of Sage (I think you're right that they belong there), but I'd like to wait until after this patch has been accepted. It just keeps it less of a moving target, and reduces the risk of having to rebase.\n* Fixed/removed some import statements that got broken (this caused the segfaults)\n* Made the lean_matrix interfaces agree with Sage's Matrices to the largest extent (see comments near top of linear_matroid.pyx). \n\nThe LinearMatroid class only uses the trivial nonstandard ``is_nonzero`` method now. The subclasses BinaryMatroid, TernaryMatroid, QuaternaryMatroid, RegularMatroid use a few more methods that have no Sage Matrix equivalent, but all are flagged in the code, and it should be possible to replace them. One last remark: the lean_matrix.pyx code is ONLY used as internal data structure, we don't expose any of it to the user (unless they try really hard). Everything the user sees is a normal Sage matrix.",
    "created_at": "2013-05-28T22:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63059",
    "user": "Stefan"
}
```

I just uploaded a new version of the patch. I tested it against 5.10.beta4, I hope it didn't break on 5.10.beta5... 

Items fixed:

* Fixed multiline doctests to have ....:

Responding to darij:

* Improved documentation of cdef methods (especially doubly-underscored ones)
* Corrected _with_coloop docstring
* Corrected typos

Responding to rbeezer:

* Fixed (2)
* Fixed EXAMPLES indentation (3)
* Got rid of MatroidError, made error messages lower case. Did not change content of messages, leaving it for future improvements (4)
* Fixed the documentation (5)

Responding to vbraun (some comments are replies to issues from sage-devel):

* I'm happy to move the bitset enhancements into the rest of Sage (I think you're right that they belong there), but I'd like to wait until after this patch has been accepted. It just keeps it less of a moving target, and reduces the risk of having to rebase.
* Fixed/removed some import statements that got broken (this caused the segfaults)
* Made the lean_matrix interfaces agree with Sage's Matrices to the largest extent (see comments near top of linear_matroid.pyx). 

The LinearMatroid class only uses the trivial nonstandard ``is_nonzero`` method now. The subclasses BinaryMatroid, TernaryMatroid, QuaternaryMatroid, RegularMatroid use a few more methods that have no Sage Matrix equivalent, but all are flagged in the code, and it should be possible to replace them. One last remark: the lean_matrix.pyx code is ONLY used as internal data structure, we don't expose any of it to the user (unless they try really hard). Everything the user sees is a normal Sage matrix.



---

archive/issue_comments_063060.json:
```json
{
    "body": "I get some docbuild errors, e.g.\n\n```\n[reference] /home/vbraun/opt/sage-5.10.beta5/devel/sage/doc/en/reference/matroids/sage/matroids/basis_exchange_matroid.rst:11: WARNING: autodoc can't import/find module 'sage.matroids.basis_exchange_matroid', it reported error: \"'module' object has no attribute 'BasisExchangeMatroid'\", please check your spelling and sys.path\n[matroids ] /home/vbraun/opt/sage-5.10.beta5/devel/sage/doc/en/reference/matroids/index.rst:7: WARNING: toctree contains reference to nonexisting document 'matroids/sage/matroids/constructor'\n```\n",
    "created_at": "2013-05-29T12:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63060",
    "user": "vbraun"
}
```

I get some docbuild errors, e.g.

```
[reference] /home/vbraun/opt/sage-5.10.beta5/devel/sage/doc/en/reference/matroids/sage/matroids/basis_exchange_matroid.rst:11: WARNING: autodoc can't import/find module 'sage.matroids.basis_exchange_matroid', it reported error: "'module' object has no attribute 'BasisExchangeMatroid'", please check your spelling and sys.path
[matroids ] /home/vbraun/opt/sage-5.10.beta5/devel/sage/doc/en/reference/matroids/index.rst:7: WARNING: toctree contains reference to nonexisting document 'matroids/sage/matroids/constructor'
```




---

archive/issue_comments_063061.json:
```json
{
    "body": "PS: the fact that you are more likely to get conflicts when you also improve other parts of Sage is **not** an excuse for not doing it ;-) You should have separated out the bitset improvements into a different ticket, this would have made this ticket less of a patch bomb, helped with reviewing, and made conflicts (if any) more manageable.",
    "created_at": "2013-05-29T12:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63061",
    "user": "vbraun"
}
```

PS: the fact that you are more likely to get conflicts when you also improve other parts of Sage is **not** an excuse for not doing it ;-) You should have separated out the bitset improvements into a different ticket, this would have made this ticket less of a patch bomb, helped with reviewing, and made conflicts (if any) more manageable.



---

archive/issue_comments_063062.json:
```json
{
    "body": "Yes, you're right, I didn't look closely enough at the docbuild process. It is related to lazy_import: if I change all.py to do a regular import, then the documentation builds just fine... I guess I'll have to ask sage-devel for advice on that.\n\nAnd opening a separate ticket: that's definitely a good solution, why didn't I think of that?",
    "created_at": "2013-05-29T14:34:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63062",
    "user": "Stefan"
}
```

Yes, you're right, I didn't look closely enough at the docbuild process. It is related to lazy_import: if I change all.py to do a regular import, then the documentation builds just fine... I guess I'll have to ask sage-devel for advice on that.

And opening a separate ticket: that's definitely a good solution, why didn't I think of that?



---

archive/issue_comments_063063.json:
```json
{
    "body": "Replying to [comment:39 vbraun]:\n> I get some docbuild errors, e.g.\n\nMe, too.  I got a bit of advice from John Palmieri off-list, but that did not do the trick.  FWIW, no matter how hard I try to rebuild from scratch, these persist.  I was about to poll sage-devel, but I see that has started.  \n\nOnce this gets sorted, I should be able to finish a review of the documentation part of this.\n\nRob",
    "created_at": "2013-05-29T17:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63063",
    "user": "rbeezer"
}
```

Replying to [comment:39 vbraun]:
> I get some docbuild errors, e.g.

Me, too.  I got a bit of advice from John Palmieri off-list, but that did not do the trick.  FWIW, no matter how hard I try to rebuild from scratch, these persist.  I was about to poll sage-devel, but I see that has started.  

Once this gets sorted, I should be able to finish a review of the documentation part of this.

Rob



---

archive/issue_comments_063064.json:
```json
{
    "body": "This change ought to fix the docbuilding problems:\n\n```diff\ndiff --git a/doc/en/reference/conf.py b/doc/en/reference/conf.py\n--- a/doc/en/reference/conf.py\n+++ b/doc/en/reference/conf.py\n@@ -94,6 +94,7 @@\n     'libs',\n     'logic',\n     'matrices',\n+    'matroids',\n     'misc',\n     'modabvar',\n     'modfrm',\n```\n\nHowever, I think a better solution is to auto-generated this list. Volker, you know the docbuild system. Can you look at my patch?",
    "created_at": "2013-05-29T21:00:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63064",
    "user": "jhpalmieri"
}
```

This change ought to fix the docbuilding problems:

```diff
diff --git a/doc/en/reference/conf.py b/doc/en/reference/conf.py
--- a/doc/en/reference/conf.py
+++ b/doc/en/reference/conf.py
@@ -94,6 +94,7 @@
     'libs',
     'logic',
     'matrices',
+    'matroids',
     'misc',
     'modabvar',
     'modfrm',
```

However, I think a better solution is to auto-generated this list. Volker, you know the docbuild system. Can you look at my patch?



---

archive/issue_comments_063065.json:
```json
{
    "body": "Attachment [trac_7477-docbuild.patch](tarball://root/attachments/some-uuid/ticket7477/trac_7477-docbuild.patch) by jhpalmieri created at 2013-05-29 21:02:02\n\n(If you want, we can move my patch to a different ticket and have it be a prerequisite for this one.)",
    "created_at": "2013-05-29T21:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63065",
    "user": "jhpalmieri"
}
```

Attachment [trac_7477-docbuild.patch](tarball://root/attachments/some-uuid/ticket7477/trac_7477-docbuild.patch) by jhpalmieri created at 2013-05-29 21:02:02

(If you want, we can move my patch to a different ticket and have it be a prerequisite for this one.)



---

archive/issue_comments_063066.json:
```json
{
    "body": "Replying to [comment:43 jhpalmieri]:\n> This change ought to fix the docbuilding problems:\n\nYes, it does, thanks.  I had tried that, but was just trying to build the reference only and there was no inventory file.  So when you apply the patches here, try\n\n\n```\nsage -docbuild all html\n```\n\n\nfirst to get a proper collection of HTML documentation.  Maybe John's change should just go in Stefan's setup patch - seems like that is where it belongs.  Autogeneration could be something new?\n\nAnd I'm wondering if inventories should get rebuilt on smaller units of the documentation.  I'll ask that on sage-devel so as to not clutter this any further.",
    "created_at": "2013-05-29T21:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63066",
    "user": "rbeezer"
}
```

Replying to [comment:43 jhpalmieri]:
> This change ought to fix the docbuilding problems:

Yes, it does, thanks.  I had tried that, but was just trying to build the reference only and there was no inventory file.  So when you apply the patches here, try


```
sage -docbuild all html
```


first to get a proper collection of HTML documentation.  Maybe John's change should just go in Stefan's setup patch - seems like that is where it belongs.  Autogeneration could be something new?

And I'm wondering if inventories should get rebuilt on smaller units of the documentation.  I'll ask that on sage-devel so as to not clutter this any further.



---

archive/issue_comments_063067.json:
```json
{
    "body": "You should just be able to do `sage --docbuild reference/matroids inventory` and then `sage --docbuild reference/matroids html`. Building the documentation this way is a lot like running LaTeX: you need to run it several times to resolve references, links, etc. Running `sage --docbuild all html` (and the same with `pdf` in place of `html`) automates the process, building the docs twice. Using any other options just builds once. (This was a design decision discussed at #6495.)",
    "created_at": "2013-05-29T21:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63067",
    "user": "jhpalmieri"
}
```

You should just be able to do `sage --docbuild reference/matroids inventory` and then `sage --docbuild reference/matroids html`. Building the documentation this way is a lot like running LaTeX: you need to run it several times to resolve references, links, etc. Running `sage --docbuild all html` (and the same with `pdf` in place of `html`) automates the process, building the docs twice. Using any other options just builds once. (This was a design decision discussed at #6495.)



---

archive/issue_comments_063068.json:
```json
{
    "body": "Thanks, John.  Just obsoleted much of my post to sage-devel.  ;-)  I'd read some of #6495 but not carefully enough to follow all the nuances.\n\nI've been away too long - need to get caught up.  Sorry for the noise.",
    "created_at": "2013-05-29T21:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63068",
    "user": "rbeezer"
}
```

Thanks, John.  Just obsoleted much of my post to sage-devel.  ;-)  I'd read some of #6495 but not carefully enough to follow all the nuances.

I've been away too long - need to get caught up.  Sorry for the noise.



---

archive/issue_comments_063069.json:
```json
{
    "body": "I can confirm that the docbuild patch fixes our problems. I also found that the PDF didn't build. The current update fixes that.",
    "created_at": "2013-05-30T02:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63069",
    "user": "Stefan"
}
```

I can confirm that the docbuild patch fixes our problems. I also found that the PDF didn't build. The current update fixes that.



---

archive/issue_comments_063070.json:
```json
{
    "body": "Replying to [comment:40 vbraun]:\n> PS: the fact that you are more likely to get conflicts when you also improve other parts of Sage is **not** an excuse for not doing it ;-) You should have separated out the bitset improvements into a different ticket, this would have made this ticket less of a patch bomb, helped with reviewing, and made conflicts (if any) more manageable.\n\nCompletely agreed.",
    "created_at": "2013-05-30T13:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63070",
    "user": "jdemeyer"
}
```

Replying to [comment:40 vbraun]:
> PS: the fact that you are more likely to get conflicts when you also improve other parts of Sage is **not** an excuse for not doing it ;-) You should have separated out the bitset improvements into a different ticket, this would have made this ticket less of a patch bomb, helped with reviewing, and made conflicts (if any) more manageable.

Completely agreed.



---

archive/issue_comments_063071.json:
```json
{
    "body": "John's docbuilding patch looks good to me.\n\nRob: are you still proof reading the documentation?",
    "created_at": "2013-05-30T14:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63071",
    "user": "vbraun"
}
```

John's docbuilding patch looks good to me.

Rob: are you still proof reading the documentation?



---

archive/issue_comments_063072.json:
```json
{
    "body": "Replying to [comment:50 vbraun]:\n> Rob: are you still proof reading the documentation?\n\nYes, hope to finish by the end of the weekend (will be way next week at a conference).\n\n\"proof reading\" might be a bit strong.  I'm looking for adherence to our conventions and only reporting minor problems as I go.  Generally, it is in great shape.  (And of course, way better than some of the older bits of Sage.)  Now that I can actually build all of the documentation, I should be able to wrap it up soon.\n\nJohn's patch looks good to  me.  I guess the onus will be to now keep the exclusions up-to-date (eg static, template) if new ones come along.  I had not looked too carefully before - it does not really belong in the setup patch here.  Does it make sense to put it on its own ticket, so it does not get buried in this (big) ticket?  Make it a dependency of this ticket?",
    "created_at": "2013-05-30T18:23:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63072",
    "user": "rbeezer"
}
```

Replying to [comment:50 vbraun]:
> Rob: are you still proof reading the documentation?

Yes, hope to finish by the end of the weekend (will be way next week at a conference).

"proof reading" might be a bit strong.  I'm looking for adherence to our conventions and only reporting minor problems as I go.  Generally, it is in great shape.  (And of course, way better than some of the older bits of Sage.)  Now that I can actually build all of the documentation, I should be able to wrap it up soon.

John's patch looks good to  me.  I guess the onus will be to now keep the exclusions up-to-date (eg static, template) if new ones come along.  I had not looked too carefully before - it does not really belong in the setup patch here.  Does it make sense to put it on its own ticket, so it does not get buried in this (big) ticket?  Make it a dependency of this ticket?



---

archive/issue_comments_063073.json:
```json
{
    "body": "I moved the docbuilding patch to #14669.",
    "created_at": "2013-05-30T18:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63073",
    "user": "jhpalmieri"
}
```

I moved the docbuilding patch to #14669.



---

archive/issue_comments_063074.json:
```json
{
    "body": "Just for the record, I made tickets #14666 #14667 #14668 to address the suggestions made in this thread that we haven't implemented right away.",
    "created_at": "2013-05-30T19:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63074",
    "user": "Stefan"
}
```

Just for the record, I made tickets #14666 #14667 #14668 to address the suggestions made in this thread that we haven't implemented right away.



---

archive/issue_comments_063075.json:
```json
{
    "body": "About #14668: better yet, add the bitset code **only** in #14668 (as if it never existed in `sage/matroids/bitset_tools.pyx`) and make this ticket depend on #14668.",
    "created_at": "2013-05-30T20:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63075",
    "user": "jdemeyer"
}
```

About #14668: better yet, add the bitset code **only** in #14668 (as if it never existed in `sage/matroids/bitset_tools.pyx`) and make this ticket depend on #14668.



---

archive/issue_comments_063076.json:
```json
{
    "body": "Dear Stefan,\n\nOK, here's the result of another pass - got through two sections this time.  Some of this may be systematic, I'll let you decide what needs mass editing, and what might be one-off.  Generally, the documentation is really very good.  Lots of thought has gone into it and I'm sure it will be easy for new users to get up-to-speed quickly.  Most of this is annoying details (yes, I said annoying).  Some themes, amplified in specific comments below:\n\n1.  Single backticks get TeX treatment for mathematics.  Small chunks of code need double backticks.  This might be isolated in small parts of the constructor file.\n2.  Making references to documentation of other classes (inside or outside of the matroids package) would be better as live links, definitely when you say \"see...\".\n3.  I'm not too dogmatic about long lines in doctests, but an effort should be made to line-break both input and output in the cases where it goes on forever.\n4.  Lots of \"simple\" methods without OUTPUT sections.  Yes, it seems silly to just say \"foo() returns all the foo's of the matroid.\"  I like to provide some very basic idea of what a foo is if possible, then the documentation seems worthwhile.  I've learned a lot of math by reading Sage documentation.\n\nI know this seems like a lot of trouble, but it will be worthwhile in the long run.  I'm thinking this package might be a very good example for others to follow if they wish to add-in other new areas of mathematics.\n\nRob\n\n\n\nMatroid construction (constructor.pyx):\n\n  \"For EXAMPLES:\" appears at least twice, probably a mass substitution hitting the phrase  \"For example\".  Perhaps more in other files?\n\n  The flexibility of the Matroid() constructor in the first two arguments may drive you crazy some day down the road.  I am not suggesting you change it - just a comment.\n\n  \"A matroid specified by a list of circuits gets converted to a BasisMatroid internally:\"\n  Making BasisMatroid a link to the class would be an improvement.\n\n  \"Note: if a groundset is specified, we assume it is in the same order as G.edge_iterator() provides:\"\n  It'd be nice if small chunks of code were typeset as such, here  ``G.edge_iterator()``\n\n  Code:  \"If that fails, we simply use a list `[0..m-1]`\"\n  The single backticks are giving TeX, this should definitely be code, hence two backticks\n  Probably the (i,j) preceding is similar, though we could debate if that is math or code.\n\n  Code:  \"When the ``graph`` keyword is used, a variety of inputs can be converted to a graph automatically. The following\n  uses a graph6 string (see the ``Graph()`` method's documentation)::\"\n  Formatting of the keyword is exactly correct.  Perhaps \"Graph()\" should definitely be a link when it is used in a suggestion to go there.\n\n  Code:  \"sage: M = Matroid(circuit_closures={3: ['edfg', 'acdg', 'bcfg', 'cefh', 'afgh', 'abce', 'abdf', 'begh', 'bcdh', 'adeh'], 4: ['abcdefgh']})\n  Makes a very long line in the documentation, which puts up a scrollable box in my browser.\n  You could define the the long list on its own line, then just reference it, or I think there is enough flexibility on where you can line break the command (maybe open the dictionary, put each key/value on its own line, mildly indented, then close dictionary at start of a subsequent line?).\n\n\nAbstract class (matroid.pyx)\n\n  URL in [GG12] seems broken\n\n  Doctest output:\n   \"sage: M = matroids.named_matroids.Fano()\n    sage: sorted([sorted(C) for C in M.circuits()])\n    [['a', 'b', 'c', 'g'], ['a', 'b', 'd', 'e'], ['a', 'b', 'f'], ['a', 'c', 'd', 'f'], ['a', 'c', 'e'], ['a', 'd', 'g'], ['a', 'e', 'f', 'g'], ['b', 'c', 'd'], ['b', 'c', 'e', 'f'], ['b', 'd', 'f', 'g'], ['b', 'e', 'g'], ['c', 'd', 'e', 'g'], ['c', 'f', 'g'], ['d', 'e', 'f']]\"\n  You can line-break output at any whitespace and the test should succeed.  Here, you could put each interior list\non a line of its own.  I have not looked at the PDF version, but I suspect this will just run off the right edge of the page.\n\n  f-vector() documentation:\n    Has a list with just one item for output.  Probably does not need to be a list.  Ditto for flats().  I'm seeing more like this.  I'm inclined to just write a paragraph, unless returning a pair, triple, or ...\n\n  groundset():\n     Not sure an INPUT section is necessary if there is none.  Even though this is an abstract method, maybe the OUTPUT should be documented?\n\n  is_connected(), is_cosimple() (and more is_ methods) lack OUTPUT, even if it seems silly to have it.\n\n  \"loops() Return the set of loops of the matroid.\"  Is it easy to say in an OUTPUT section what a loop is?  Some people learn mathematics by reading the documentation.  You do not have to go overboard, but can you say in one sentence what a loop is?  It makes the documantation look less vacuous.  (eg OUTPUT: A list of the loops of the matroid.  A loop is a one-element dependent set.)",
    "created_at": "2013-05-31T01:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63076",
    "user": "rbeezer"
}
```

Dear Stefan,

OK, here's the result of another pass - got through two sections this time.  Some of this may be systematic, I'll let you decide what needs mass editing, and what might be one-off.  Generally, the documentation is really very good.  Lots of thought has gone into it and I'm sure it will be easy for new users to get up-to-speed quickly.  Most of this is annoying details (yes, I said annoying).  Some themes, amplified in specific comments below:

1.  Single backticks get TeX treatment for mathematics.  Small chunks of code need double backticks.  This might be isolated in small parts of the constructor file.
2.  Making references to documentation of other classes (inside or outside of the matroids package) would be better as live links, definitely when you say "see...".
3.  I'm not too dogmatic about long lines in doctests, but an effort should be made to line-break both input and output in the cases where it goes on forever.
4.  Lots of "simple" methods without OUTPUT sections.  Yes, it seems silly to just say "foo() returns all the foo's of the matroid."  I like to provide some very basic idea of what a foo is if possible, then the documentation seems worthwhile.  I've learned a lot of math by reading Sage documentation.

I know this seems like a lot of trouble, but it will be worthwhile in the long run.  I'm thinking this package might be a very good example for others to follow if they wish to add-in other new areas of mathematics.

Rob



Matroid construction (constructor.pyx):

  "For EXAMPLES:" appears at least twice, probably a mass substitution hitting the phrase  "For example".  Perhaps more in other files?

  The flexibility of the Matroid() constructor in the first two arguments may drive you crazy some day down the road.  I am not suggesting you change it - just a comment.

  "A matroid specified by a list of circuits gets converted to a BasisMatroid internally:"
  Making BasisMatroid a link to the class would be an improvement.

  "Note: if a groundset is specified, we assume it is in the same order as G.edge_iterator() provides:"
  It'd be nice if small chunks of code were typeset as such, here  ``G.edge_iterator()``

  Code:  "If that fails, we simply use a list `[0..m-1]`"
  The single backticks are giving TeX, this should definitely be code, hence two backticks
  Probably the (i,j) preceding is similar, though we could debate if that is math or code.

  Code:  "When the ``graph`` keyword is used, a variety of inputs can be converted to a graph automatically. The following
  uses a graph6 string (see the ``Graph()`` method's documentation)::"
  Formatting of the keyword is exactly correct.  Perhaps "Graph()" should definitely be a link when it is used in a suggestion to go there.

  Code:  "sage: M = Matroid(circuit_closures={3: ['edfg', 'acdg', 'bcfg', 'cefh', 'afgh', 'abce', 'abdf', 'begh', 'bcdh', 'adeh'], 4: ['abcdefgh']})
  Makes a very long line in the documentation, which puts up a scrollable box in my browser.
  You could define the the long list on its own line, then just reference it, or I think there is enough flexibility on where you can line break the command (maybe open the dictionary, put each key/value on its own line, mildly indented, then close dictionary at start of a subsequent line?).


Abstract class (matroid.pyx)

  URL in [GG12] seems broken

  Doctest output:
   "sage: M = matroids.named_matroids.Fano()
    sage: sorted([sorted(C) for C in M.circuits()])
    [['a', 'b', 'c', 'g'], ['a', 'b', 'd', 'e'], ['a', 'b', 'f'], ['a', 'c', 'd', 'f'], ['a', 'c', 'e'], ['a', 'd', 'g'], ['a', 'e', 'f', 'g'], ['b', 'c', 'd'], ['b', 'c', 'e', 'f'], ['b', 'd', 'f', 'g'], ['b', 'e', 'g'], ['c', 'd', 'e', 'g'], ['c', 'f', 'g'], ['d', 'e', 'f']]"
  You can line-break output at any whitespace and the test should succeed.  Here, you could put each interior list
on a line of its own.  I have not looked at the PDF version, but I suspect this will just run off the right edge of the page.

  f-vector() documentation:
    Has a list with just one item for output.  Probably does not need to be a list.  Ditto for flats().  I'm seeing more like this.  I'm inclined to just write a paragraph, unless returning a pair, triple, or ...

  groundset():
     Not sure an INPUT section is necessary if there is none.  Even though this is an abstract method, maybe the OUTPUT should be documented?

  is_connected(), is_cosimple() (and more is_ methods) lack OUTPUT, even if it seems silly to have it.

  "loops() Return the set of loops of the matroid."  Is it easy to say in an OUTPUT section what a loop is?  Some people learn mathematics by reading the documentation.  You do not have to go overboard, but can you say in one sentence what a loop is?  It makes the documantation look less vacuous.  (eg OUTPUT: A list of the loops of the matroid.  A loop is a one-element dependent set.)



---

archive/issue_comments_063077.json:
```json
{
    "body": "I made most of the changes detailed below (I'll leave it to Stefan to upload and make sure I didn't break anything)\n\nReplying to [comment:55 rbeezer]:\n> 1.  I'm not too dogmatic about long lines in doctests, but an effort should be made to line-break both input and output in the cases where it goes on forever.\n\nYou haven't got to catalog.py yet (it's horrible for this), but is there a general guideline on characters per line?\n\n> 1.  Lots of \"simple\" methods without OUTPUT sections.  Yes, it seems silly to just say \"foo() returns all the foo's of the matroid.\"  I like to provide some very basic idea of what a foo is if possible, then the documentation seems worthwhile.  I've learned a lot of math by reading Sage documentation.\n\nI changed all of those that I am able to (some I don't know what they are).\n\n> \n>   Code:  \"If that fails, we simply use a list `[0..m-1]`\"\n>   The single backticks are giving TeX, this should definitely be code, hence two backticks\n>   Probably the (i,j) preceding is similar, though we could debate if that is math or code.\n\nThere were lots like this, so I left them as they are, as that's a debate I don't really want to have.\n\n> \n>   f-vector() documentation:\n>     Has a list with just one item for output.  Probably does not need to be a list.  Ditto for flats().  I'm seeing more like this.  I'm inclined to just write a paragraph, unless returning a pair, triple, or ...\n\nI'm confused. f_vector() returns a list [f_0, ..., f_r] where f_i is the number of flats of rank i, and r the rank of the matroid. That's got more than one thing in it. And flats() returns a SetSystem, not a list, and there's normally a lot more than one flat at a given rank.\n\n\nMichael",
    "created_at": "2013-05-31T20:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63077",
    "user": "yomcat"
}
```

I made most of the changes detailed below (I'll leave it to Stefan to upload and make sure I didn't break anything)

Replying to [comment:55 rbeezer]:
> 1.  I'm not too dogmatic about long lines in doctests, but an effort should be made to line-break both input and output in the cases where it goes on forever.

You haven't got to catalog.py yet (it's horrible for this), but is there a general guideline on characters per line?

> 1.  Lots of "simple" methods without OUTPUT sections.  Yes, it seems silly to just say "foo() returns all the foo's of the matroid."  I like to provide some very basic idea of what a foo is if possible, then the documentation seems worthwhile.  I've learned a lot of math by reading Sage documentation.

I changed all of those that I am able to (some I don't know what they are).

> 
>   Code:  "If that fails, we simply use a list `[0..m-1]`"
>   The single backticks are giving TeX, this should definitely be code, hence two backticks
>   Probably the (i,j) preceding is similar, though we could debate if that is math or code.

There were lots like this, so I left them as they are, as that's a debate I don't really want to have.

> 
>   f-vector() documentation:
>     Has a list with just one item for output.  Probably does not need to be a list.  Ditto for flats().  I'm seeing more like this.  I'm inclined to just write a paragraph, unless returning a pair, triple, or ...

I'm confused. f_vector() returns a list [f_0, ..., f_r] where f_i is the number of flats of rank i, and r the rank of the matroid. That's got more than one thing in it. And flats() returns a SetSystem, not a list, and there's normally a lot more than one flat at a given rank.


Michael



---

archive/issue_comments_063078.json:
```json
{
    "body": "Thanks, Michael.\n\nComments interspersed.\n\nReplying to [comment:56 yomcat]:\n> You haven't got to catalog.py yet (it's horrible for this), but is there a general guideline on characters per line?\n\n \"Python Enhancemant Proposal 8\", aka PEP 8, http://www.python.org/dev/peps/pep-0008/\n\nsays \"max 79 characters\"\n\n> > \n> >   Code:  \"If that fails, we simply use a list `[0..m-1]`\"\n> >   The single backticks are giving TeX, this should definitely be code, hence two backticks\n> >   Probably the (i,j) preceding is similar, though we could debate if that is math or code.\n> \n> There were lots like this, so I left them as they are, as that's a debate I don't really want to have.\n\nYes, no need to debate, but `[0..m-1]` is definitely code and should definitely be in double backticks.  I don't want to debate either - but it is often extremely clear if you have code or math, and these should be formatted right.\n\n> > \n> >   f-vector() documentation:\n> >     Has a list with just one item for output.  Probably does not need to be a list.  Ditto for flats().  I'm seeing more like this.  I'm inclined to just write a paragraph, unless returning a pair, triple, or ...\n> \n> I'm confused. f_vector() returns a list [f_0, ..., f_r] where f_i is the number of flats of rank i, and r the rank of the matroid. That's got more than one thing in it. And flats() returns a SetSystem, not a list, and there's normally a lot more than one flat at a given rank.\n\nMy mistake, not clear.  The OUTPUT section documents a single output of trhe function and is formatted as a list with one item.  I don't think a list is necessary.  INPUT will often have many items, and a list is natural.  There are lots of OUTPUT done as a one-item list.  `f_vector()` was just the first one I saw.",
    "created_at": "2013-06-01T03:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63078",
    "user": "rbeezer"
}
```

Thanks, Michael.

Comments interspersed.

Replying to [comment:56 yomcat]:
> You haven't got to catalog.py yet (it's horrible for this), but is there a general guideline on characters per line?

 "Python Enhancemant Proposal 8", aka PEP 8, http://www.python.org/dev/peps/pep-0008/

says "max 79 characters"

> > 
> >   Code:  "If that fails, we simply use a list `[0..m-1]`"
> >   The single backticks are giving TeX, this should definitely be code, hence two backticks
> >   Probably the (i,j) preceding is similar, though we could debate if that is math or code.
> 
> There were lots like this, so I left them as they are, as that's a debate I don't really want to have.

Yes, no need to debate, but `[0..m-1]` is definitely code and should definitely be in double backticks.  I don't want to debate either - but it is often extremely clear if you have code or math, and these should be formatted right.

> > 
> >   f-vector() documentation:
> >     Has a list with just one item for output.  Probably does not need to be a list.  Ditto for flats().  I'm seeing more like this.  I'm inclined to just write a paragraph, unless returning a pair, triple, or ...
> 
> I'm confused. f_vector() returns a list [f_0, ..., f_r] where f_i is the number of flats of rank i, and r the rank of the matroid. That's got more than one thing in it. And flats() returns a SetSystem, not a list, and there's normally a lot more than one flat at a given rank.

My mistake, not clear.  The OUTPUT section documents a single output of trhe function and is formatted as a list with one item.  I don't think a list is necessary.  INPUT will often have many items, and a list is natural.  There are lots of OUTPUT done as a one-item list.  `f_vector()` was just the first one I saw.



---

archive/issue_comments_063079.json:
```json
{
    "body": "My 2 cents on `OUTPUT:` and `INPUT:` blocks. If there is no input other than `self`, there is no need for an `INPUT:` IMO since with `self`, the input is clear. For output blocks, if the short description of the method (i.e. the first line) tells the object that it returns, I don't see the need to write an `OUTPUT:` block. Additionally if the object needs description (mathematically), then I think that should go in the second paragraph of the documentation. For example:\n\n```\ndef loops(self):\n    \"\"\"\n    Return the loops of ``self``.\n\n    A *loop* is a one-element dependent subset.\n\n    EXAMPLES::\n\n        ...\n\ndef is_cosimple(self):\n    \"\"\"\n    Return ``True`` if ``self`` is cosimple.\n\n    A matriod is *cosimple* if ...\n\n    EXAMPLES::\n\n        ...\n```\n\nAlso if you find yourself needing a (longer) definition multiple times, either explicitly referencing the method/function with the definition or using a `.. SEEALSO::` block is a good way to go IMO. I think this is a good balance between descriptive, straight-forward, and simple. However I'm somewhat splitting hairs here.\n\nAdditionally, I would like to see #14668 as a dependency and only have the bitset code there.",
    "created_at": "2013-06-01T15:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63079",
    "user": "tscrim"
}
```

My 2 cents on `OUTPUT:` and `INPUT:` blocks. If there is no input other than `self`, there is no need for an `INPUT:` IMO since with `self`, the input is clear. For output blocks, if the short description of the method (i.e. the first line) tells the object that it returns, I don't see the need to write an `OUTPUT:` block. Additionally if the object needs description (mathematically), then I think that should go in the second paragraph of the documentation. For example:

```
def loops(self):
    """
    Return the loops of ``self``.

    A *loop* is a one-element dependent subset.

    EXAMPLES::

        ...

def is_cosimple(self):
    """
    Return ``True`` if ``self`` is cosimple.

    A matriod is *cosimple* if ...

    EXAMPLES::

        ...
```

Also if you find yourself needing a (longer) definition multiple times, either explicitly referencing the method/function with the definition or using a `.. SEEALSO::` block is a good way to go IMO. I think this is a good balance between descriptive, straight-forward, and simple. However I'm somewhat splitting hairs here.

Additionally, I would like to see #14668 as a dependency and only have the bitset code there.



---

archive/issue_comments_063080.json:
```json
{
    "body": "For the record, `self` is not considered an argument for docstring purposes. Skip `INPUT` if `self` is the only argument, and list everything except `self` otherwise. The `OUTPUT` is a good place to say something about the type of the output. Can be very short:\n\n```\ndef is_cosimple(self):\n    \"\"\"\n    Test whether the matroid is cosimple.\n\n    A matriod is *cosimple* if ...\n\n    OUTPUT:\n\n    Boolean.\n\n    EXAMPLES::\n    ...\n```\n\nIts not silly, since Python is dynamically typed it is generally not obvious what the result type will be.",
    "created_at": "2013-06-01T15:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63080",
    "user": "vbraun"
}
```

For the record, `self` is not considered an argument for docstring purposes. Skip `INPUT` if `self` is the only argument, and list everything except `self` otherwise. The `OUTPUT` is a good place to say something about the type of the output. Can be very short:

```
def is_cosimple(self):
    """
    Test whether the matroid is cosimple.

    A matriod is *cosimple* if ...

    OUTPUT:

    Boolean.

    EXAMPLES::
    ...
```

Its not silly, since Python is dynamically typed it is generally not obvious what the result type will be.



---

archive/issue_comments_063081.json:
```json
{
    "body": "Ok, the bitset code is now separated into a patch in #14668 (where I also did a bit of cleanup in directly surrounding code).",
    "created_at": "2013-06-07T03:09:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63081",
    "user": "Stefan"
}
```

Ok, the bitset code is now separated into a patch in #14668 (where I also did a bit of cleanup in directly surrounding code).



---

archive/issue_comments_063082.json:
```json
{
    "body": "Attachment [trac_7477_setup_doc_load-oldish.patch](tarball://root/attachments/some-uuid/ticket7477/trac_7477_setup_doc_load-oldish.patch) by Stefan created at 2013-06-15 00:48:39\n\nMatroid setup, autoload, documentation",
    "created_at": "2013-06-15T00:48:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63082",
    "user": "Stefan"
}
```

Attachment [trac_7477_setup_doc_load-oldish.patch](tarball://root/attachments/some-uuid/ticket7477/trac_7477_setup_doc_load-oldish.patch) by Stefan created at 2013-06-15 00:48:39

Matroid setup, autoload, documentation



---

archive/issue_comments_063083.json:
```json
{
    "body": "apply trac_7477_setup_doc_load.patch, trac_7477_code.patch\n\nI just uploaded a revision. I revisited all documentation strings, adding mathematical explanations, cross references, and revisiting the OUTPUT blocks with the above suggestions in mind. The documentation builds without warnings or errors, I believe.",
    "created_at": "2013-06-15T00:56:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63083",
    "user": "Stefan"
}
```

apply trac_7477_setup_doc_load.patch, trac_7477_code.patch

I just uploaded a revision. I revisited all documentation strings, adding mathematical explanations, cross references, and revisiting the OUTPUT blocks with the above suggestions in mind. The documentation builds without warnings or errors, I believe.



---

archive/issue_comments_063084.json:
```json
{
    "body": "Replying to [comment:62 Stefan]:\n> I just uploaded a revision. \n\nThanks, Stefan.  At Sage Days all next week, so I'll try to give it a look sometime then.",
    "created_at": "2013-06-16T03:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63084",
    "user": "rbeezer"
}
```

Replying to [comment:62 Stefan]:
> I just uploaded a revision. 

Thanks, Stefan.  At Sage Days all next week, so I'll try to give it a look sometime then.



---

archive/issue_comments_063085.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-18T18:41:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63085",
    "user": "rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063086.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd48\".",
    "created_at": "2013-06-18T18:41:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63086",
    "user": "rbeezer"
}
```

Changing keywords from "" to "sd48".



---

archive/issue_comments_063087.json:
```json
{
    "body": "This looks real good to me.  I'm with Volker at Sage Days 48 and he has reviewed the code (and integration with Sage).  I'll check off on the documentation, which looks excellent.   The HTML output looks good, as do the 145 pages of the PDF reference manual.\n\nAll doctests in sage/matroids pass on 5.10rc2 with dependencies.\n\nSo, positive review.\n\nBe prepared for a few hiccups once this gets merged into a beta and gets tested across a diverse collection of systems.  Hooefully this will also go into an early stage of the 5.11 series.  Thanks for your patience with the review process.\n\nAnd thanks for the major contribution to Sage.  I hope this makes your meeting later this month even more productive.\n\nNext up: a thematic tutorial!  ;-)\n\nRob",
    "created_at": "2013-06-18T18:41:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63087",
    "user": "rbeezer"
}
```

This looks real good to me.  I'm with Volker at Sage Days 48 and he has reviewed the code (and integration with Sage).  I'll check off on the documentation, which looks excellent.   The HTML output looks good, as do the 145 pages of the PDF reference manual.

All doctests in sage/matroids pass on 5.10rc2 with dependencies.

So, positive review.

Be prepared for a few hiccups once this gets merged into a beta and gets tested across a diverse collection of systems.  Hooefully this will also go into an early stage of the 5.11 series.  Thanks for your patience with the review process.

And thanks for the major contribution to Sage.  I hope this makes your meeting later this month even more productive.

Next up: a thematic tutorial!  ;-)

Rob



---

archive/issue_comments_063088.json:
```json
{
    "body": "That is great news! Nathann, Karl-Dieter, Darij, Travis, Rob, Volker, thanks a lot for helping with the review! I'm very happy that we are finally going to be an official part of Sage!\n\nI'll keep an eye out for the hiccups. We've already been through a weird one while the code was in development (see the file minorfix.h).",
    "created_at": "2013-06-18T18:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63088",
    "user": "Stefan"
}
```

That is great news! Nathann, Karl-Dieter, Darij, Travis, Rob, Volker, thanks a lot for helping with the review! I'm very happy that we are finally going to be an official part of Sage!

I'll keep an eye out for the hiccups. We've already been through a weird one while the code was in development (see the file minorfix.h).



---

archive/issue_comments_063089.json:
```json
{
    "body": "Replying to [comment:65 Stefan]:\n> That is great news! Nathann, Karl-Dieter, Darij, Travis, Rob, Volker, thanks a lot for helping with the review!\n\nI did not intend to exclude any reviewers from the \"Reviewers\" field - so please add yourself if you wish to be part of that.\n\nRob",
    "created_at": "2013-06-18T19:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63089",
    "user": "rbeezer"
}
```

Replying to [comment:65 Stefan]:
> That is great news! Nathann, Karl-Dieter, Darij, Travis, Rob, Volker, thanks a lot for helping with the review!

I did not intend to exclude any reviewers from the "Reviewers" field - so please add yourself if you wish to be part of that.

Rob



---

archive/issue_comments_063090.json:
```json
{
    "body": "Never use\n\n```\nexcept:\n```\n\nwithout specifying an exception. Catch a specific exception instead, or if you must use a catch-all, use\n\n```\nexcept StandardError:\n```\n\n(or `BaseException` if you really need to catch everything, including `KeyboardInterrupt`)",
    "created_at": "2013-06-18T20:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63090",
    "user": "jdemeyer"
}
```

Never use

```
except:
```

without specifying an exception. Catch a specific exception instead, or if you must use a catch-all, use

```
except StandardError:
```

(or `BaseException` if you really need to catch everything, including `KeyboardInterrupt`)



---

archive/issue_comments_063091.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-06-18T20:47:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63091",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_063092.json:
```json
{
    "body": "This needs to be rebased to #9880:\n\n```\nsage -t --long devel/sage/sage/matroids/matroid.pyx\n**********************************************************************\nFile \"devel/sage/sage/matroids/matroid.pyx\", line 188, in sage.matroids.matroid\nFailed example:\n    M.tutte_polynomial(var('x'), var('y'))\nExpected:\n    x^2*y^2 + 2*x*y^3 + x^3 + y^4 + 3*x^2*y + 3*x*y^2 + y^3\nGot:\n    x^2*y^2 + 2*x*y^3 + y^4 + x^3 + 3*x^2*y + 3*x*y^2 + y^3\n**********************************************************************\nFile \"devel/sage/sage/matroids/matroid.pyx\", line 362, in sage.matroids.matroid.Matroid\nFailed example:\n    M.tutte_polynomial(var('x'), var('y'))\nExpected:\n    x^2*y^2 + 2*x*y^3 + x^3 + y^4 + 3*x^2*y + 3*x*y^2 + y^3\nGot:\n    x^2*y^2 + 2*x*y^3 + y^4 + x^3 + 3*x^2*y + 3*x*y^2 + y^3\n**********************************************************************\n```\n",
    "created_at": "2013-06-19T06:43:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63092",
    "user": "jdemeyer"
}
```

This needs to be rebased to #9880:

```
sage -t --long devel/sage/sage/matroids/matroid.pyx
**********************************************************************
File "devel/sage/sage/matroids/matroid.pyx", line 188, in sage.matroids.matroid
Failed example:
    M.tutte_polynomial(var('x'), var('y'))
Expected:
    x^2*y^2 + 2*x*y^3 + x^3 + y^4 + 3*x^2*y + 3*x*y^2 + y^3
Got:
    x^2*y^2 + 2*x*y^3 + y^4 + x^3 + 3*x^2*y + 3*x*y^2 + y^3
**********************************************************************
File "devel/sage/sage/matroids/matroid.pyx", line 362, in sage.matroids.matroid.Matroid
Failed example:
    M.tutte_polynomial(var('x'), var('y'))
Expected:
    x^2*y^2 + 2*x*y^3 + x^3 + y^4 + 3*x^2*y + 3*x*y^2 + y^3
Got:
    x^2*y^2 + 2*x*y^3 + y^4 + x^3 + 3*x^2*y + 3*x*y^2 + y^3
**********************************************************************
```




---

archive/issue_comments_063093.json:
```json
{
    "body": "Uploaded new version:\n\n* no more blanket except: statements\n* all tests pass on 5.11.beta1\n* minor addition to documentation of matroids_catalog.py",
    "created_at": "2013-06-20T02:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63093",
    "user": "Stefan"
}
```

Uploaded new version:

* no more blanket except: statements
* all tests pass on 5.11.beta1
* minor addition to documentation of matroids_catalog.py



---

archive/issue_comments_063094.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-20T02:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63094",
    "user": "Stefan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063095.json:
```json
{
    "body": "Just FYI, there are some people working on getting some form of hyperplane arrangements into Sage, and I've alerted them to this effort :-)",
    "created_at": "2013-06-20T02:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63095",
    "user": "kcrisman"
}
```

Just FYI, there are some people working on getting some form of hyperplane arrangements into Sage, and I've alerted them to this effort :-)



---

archive/issue_comments_063096.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-20T04:21:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63096",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063097.json:
```json
{
    "body": "Please use spaces for indentation, not TABs, even in the non-Python file `sage/matroids/minorfix.h`.",
    "created_at": "2013-06-20T07:18:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63097",
    "user": "jdemeyer"
}
```

Please use spaces for indentation, not TABs, even in the non-Python file `sage/matroids/minorfix.h`.



---

archive/issue_comments_063098.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-06-20T07:18:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63098",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_063099.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-20T12:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63099",
    "user": "Stefan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063100.json:
```json
{
    "body": "Tabs changed to spaces",
    "created_at": "2013-06-20T12:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63100",
    "user": "Stefan"
}
```

Tabs changed to spaces



---

archive/issue_comments_063101.json:
```json
{
    "body": "positive_review assuming that only the TABs changed.",
    "created_at": "2013-06-20T12:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63101",
    "user": "jdemeyer"
}
```

positive_review assuming that only the TABs changed.



---

archive/issue_comments_063102.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-20T12:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63102",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063103.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-06-20T21:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63103",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_063104.json:
```json
{
    "body": "Solaris doesn't like `_N` as it uses that internally for other purposes. So you must use a different (either longer or either without leading underscore) variable name instead of `_N` in `sage/matroids/set_system.pxd`",
    "created_at": "2013-06-21T06:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63104",
    "user": "jdemeyer"
}
```

Solaris doesn't like `_N` as it uses that internally for other purposes. So you must use a different (either longer or either without leading underscore) variable name instead of `_N` in `sage/matroids/set_system.pxd`



---

archive/issue_comments_063105.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2013-06-21T06:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63105",
    "user": "jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_063106.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2013-06-21T06:15:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63106",
    "user": "jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_063107.json:
```json
{
    "body": "Matroid code",
    "created_at": "2013-06-21T14:13:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63107",
    "user": "Stefan"
}
```

Matroid code



---

archive/issue_comments_063108.json:
```json
{
    "body": "Attachment [trac_7477_code.patch](tarball://root/attachments/some-uuid/ticket7477/trac_7477_code.patch) by Stefan created at 2013-06-21 14:14:39\n\nReplaced some variable names. All doctests pass.",
    "created_at": "2013-06-21T14:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63108",
    "user": "Stefan"
}
```

Attachment [trac_7477_code.patch](tarball://root/attachments/some-uuid/ticket7477/trac_7477_code.patch) by Stefan created at 2013-06-21 14:14:39

Replaced some variable names. All doctests pass.



---

archive/issue_comments_063109.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-06-21T14:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63109",
    "user": "Stefan"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063110.json:
```json
{
    "body": "Looks good.\n\nIn C/C++, identifiers starting with an underscore and followed by an upper case letter are reserved. So Solaris is standards-compliant in this case.",
    "created_at": "2013-06-21T17:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63110",
    "user": "vbraun"
}
```

Looks good.

In C/C++, identifiers starting with an underscore and followed by an upper case letter are reserved. So Solaris is standards-compliant in this case.



---

archive/issue_comments_063111.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-21T17:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63111",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063112.json:
```json
{
    "body": "So, just to be clear, to avoid\n\n```\nWARNING: intersphinx inventory '/Users/.../sage-5.11.beta1/devel/sage/doc/output/html/en/reference/matroids/objects.inv' not fetchable due to <type 'exceptions.IOError'>: \n```\n\nerrors, in the future we have to always do\n\n```\nsage -docbuild all html\n```\n\nor do this inventory thing?  I don't see any mention in the [documentation](http://www.sagemath.org/doc/developer/sage_manuals.html?highlight=docbuild), nor at #14699, and I am using 5.11.beta1 here.",
    "created_at": "2013-06-24T18:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63112",
    "user": "kcrisman"
}
```

So, just to be clear, to avoid

```
WARNING: intersphinx inventory '/Users/.../sage-5.11.beta1/devel/sage/doc/output/html/en/reference/matroids/objects.inv' not fetchable due to <type 'exceptions.IOError'>: 
```

errors, in the future we have to always do

```
sage -docbuild all html
```

or do this inventory thing?  I don't see any mention in the [documentation](http://www.sagemath.org/doc/developer/sage_manuals.html?highlight=docbuild), nor at #14699, and I am using 5.11.beta1 here.



---

archive/issue_comments_063113.json:
```json
{
    "body": "Only the reference manual uses the two-step build process, so its either \n\n```\n   sage -docbuild reference inventory     # only necessary if inventory changed\n   sage -docbuild reference/DIR\n```\n\nor \n\n```\n   sage -docbuild reference html\n```\n",
    "created_at": "2013-06-24T19:08:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63113",
    "user": "vbraun"
}
```

Only the reference manual uses the two-step build process, so its either 

```
   sage -docbuild reference inventory     # only necessary if inventory changed
   sage -docbuild reference/DIR
```

or 

```
   sage -docbuild reference html
```




---

archive/issue_comments_063114.json:
```json
{
    "body": "I had a problem with the latter, though.  Anyway, I won't be changing the inventory much soon...",
    "created_at": "2013-06-24T19:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63114",
    "user": "kcrisman"
}
```

I had a problem with the latter, though.  Anyway, I won't be changing the inventory much soon...



---

archive/issue_comments_063115.json:
```json
{
    "body": "Replying to [comment:82 kcrisman]:\n> I had a problem with the latter, though.  Anyway, I won't be changing the inventory much soon...\nI suppose the latter Sage call  was meant to replace the last line from the 1st code snippet, not both of them.",
    "created_at": "2013-07-28T19:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63115",
    "user": "dimpase"
}
```

Replying to [comment:82 kcrisman]:
> I had a problem with the latter, though.  Anyway, I won't be changing the inventory much soon...
I suppose the latter Sage call  was meant to replace the last line from the 1st code snippet, not both of them.



---

archive/issue_comments_063116.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-07-30T10:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63116",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_063117.json:
```json
{
    "body": "Please rebase to #8386.",
    "created_at": "2013-07-30T10:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63117",
    "user": "jdemeyer"
}
```

Please rebase to #8386.



---

archive/issue_comments_063118.json:
```json
{
    "body": "Attachment [trac_7477_setup_doc_load.patch](tarball://root/attachments/some-uuid/ticket7477/trac_7477_setup_doc_load.patch) by Stefan created at 2013-07-30 16:07:25\n\nMatroid setup, autoload, documentation",
    "created_at": "2013-07-30T16:07:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63118",
    "user": "Stefan"
}
```

Attachment [trac_7477_setup_doc_load.patch](tarball://root/attachments/some-uuid/ticket7477/trac_7477_setup_doc_load.patch) by Stefan created at 2013-07-30 16:07:25

Matroid setup, autoload, documentation



---

archive/issue_comments_063119.json:
```json
{
    "body": "Rebased to #8386, only the reference manual's index needed updating because of a new entry introduced by #8386.",
    "created_at": "2013-07-30T17:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63119",
    "user": "Stefan"
}
```

Rebased to #8386, only the reference manual's index needed updating because of a new entry introduced by #8386.



---

archive/issue_comments_063120.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-07-30T17:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63120",
    "user": "Stefan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_063121.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-08-01T01:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63121",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063122.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-08-16T21:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63122",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_063123.json:
```json
{
    "body": "Wow. Sooooo it's in Sage now `:-P`",
    "created_at": "2013-08-17T07:25:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7477#issuecomment-63123",
    "user": "ncohen"
}
```

Wow. Sooooo it's in Sage now `:-P`
