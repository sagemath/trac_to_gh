# Issue 5465: render3d for groebner fans is totally broken

archive/issues_005465.json:
```json
{
    "body": "Assignee: mhampton\n\n\n```\nteragon:~ wstein$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: P.<a,b,c> = PolynomialRing(QQ,3, order='lex')\nsage: sage.rings.ideal.Katsura(P,3).groebner_fan().render3d()\n---------------------------------------------------------------------------\nUnboundLocalError                         Traceback (most recent call last)\n| Sage Version 3.4.alpha0, Release Date: 2009-02-24                  |\n| Type notebook() for the GUI, and license() for information.        |\n/Users/wstein/.sage/temp/teragon.local/68617/_Users_wstein__sage_init_sage_0.py in <module>()\n\n/Users/wstein/build/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.pyc in render3d(self, verbose)\n   1067         g_cones_ieqs = [self._cone_to_ieq(q) for q in g_cones_facets]\n   1068         # Now the cones are intersected with a plane:\n-> 1069         cone_info = [ieq_to_vert(q,linearities=[[1,-1,-1,-1,-1]]) for q in g_cones_ieqs]\n   1070 \tif verbose:\n   1071 \t    for x in cone_info:\n\n/Users/wstein/build/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/geometry/polyhedra.pyc in ieq_to_vert(in_list, linearities, cdd_type, verbose)\n   1268             adj_index = index\n   1269     # read the vertices and rays:\n-> 1270     for index in range(vert_index,len(ans_lines)):\n   1271         a_line = ans_lines[index]\n   1272         if a_line.find('end') != -1: break\n\nUnboundLocalError: local variable 'vert_index' referenced before assignment\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5465\n\n",
    "created_at": "2009-03-10T08:03:00Z",
    "labels": [
        "geometry",
        "major",
        "bug"
    ],
    "title": "render3d for groebner fans is totally broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5465",
    "user": "was"
}
```
Assignee: mhampton


```
teragon:~ wstein$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: P.<a,b,c> = PolynomialRing(QQ,3, order='lex')
sage: sage.rings.ideal.Katsura(P,3).groebner_fan().render3d()
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
| Sage Version 3.4.alpha0, Release Date: 2009-02-24                  |
| Type notebook() for the GUI, and license() for information.        |
/Users/wstein/.sage/temp/teragon.local/68617/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/build/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.pyc in render3d(self, verbose)
   1067         g_cones_ieqs = [self._cone_to_ieq(q) for q in g_cones_facets]
   1068         # Now the cones are intersected with a plane:
-> 1069         cone_info = [ieq_to_vert(q,linearities=[[1,-1,-1,-1,-1]]) for q in g_cones_ieqs]
   1070 	if verbose:
   1071 	    for x in cone_info:

/Users/wstein/build/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/geometry/polyhedra.pyc in ieq_to_vert(in_list, linearities, cdd_type, verbose)
   1268             adj_index = index
   1269     # read the vertices and rays:
-> 1270     for index in range(vert_index,len(ans_lines)):
   1271         a_line = ans_lines[index]
   1272         if a_line.find('end') != -1: break

UnboundLocalError: local variable 'vert_index' referenced before assignment
```


Issue created by migration from https://trac.sagemath.org/ticket/5465





---

archive/issue_comments_042424.json:
```json
{
    "body": "This needs to have a better error message - the example here is trying to render a 2D fan with render3d, which doesn't make sense.  So the code should check the dimension first, which I will do this week (I am currently traveling until Tuesday which makes development a bit harder).\n-Marshall",
    "created_at": "2009-03-14T15:42:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5465#issuecomment-42424",
    "user": "mhampton"
}
```

This needs to have a better error message - the example here is trying to render a 2D fan with render3d, which doesn't make sense.  So the code should check the dimension first, which I will do this week (I am currently traveling until Tuesday which makes development a bit harder).
-Marshall



---

archive/issue_comments_042425.json:
```json
{
    "body": "Attachment\n\nAdds some more informative error messages",
    "created_at": "2009-03-20T18:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5465#issuecomment-42425",
    "user": "mhampton"
}
```

Attachment

Adds some more informative error messages



---

archive/issue_comments_042426.json:
```json
{
    "body": "REFEREE REPORT\n\n\n\nThe patch **trac_5465_1.patch** applies OK against Sage 3.4, all doctests pass with the `-long` option as well. Since the purpose of the patch is to add more meaningful error messages, I tried to get those two more meaningful messages. First, for the case where the number of generators is < 3:\n\n```\nsage: # first for the case of S.ngens() < 3...\nsage: R.<x,y> = PolynomialRing(QQ,2)\nsage: G = R.ideal([y^3 - x^2, y^2 - 13*x]).groebner_fan()\nsage: G.render()\nFor 2-D fan rendering the polynomial ring must have 3 variables (or more, which are ignored).\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (118, 0))\n\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/home/mvngu/.sage/temp/sage.math.washington.edu/16843/_home_mvngu__sage_init_sage_0.py in <module>()\n\n/home/mvngu/scratch/sage-3.4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.pyc in render(self, file, larger, shift, rgbcolor, polyfill, scale_colors)\n    902         if S.ngens() < 3:\n    903             print \"For 2-D fan rendering the polynomial ring must have 3 variables (or more, which are ignored).\"\n--> 904             raise NotImplementedError\n    905         cmd = 'render'\n    906         if shift:\n\nNotImplementedError:\n```\n\nYep, the error message is certainly now more comprehensible than something like `UnboundLocalError` which misses the main point that the number of generators is not of the required size.  Now, for the case where the number of generators is not 4:\n\n```\nsage: # second, for the case of S.ngens() != 4...\nsage: P.<a,b,c> = PolynomialRing(QQ, 3, order=\"lex\")\nsage: sage.rings.ideal.Katsura(P,3).groebner_fan().render3d()\nFor 3-D fan rendering the polynomial ring must have 4 variables\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/home/mvngu/.sage/temp/sage.math.washington.edu/16843/_home_mvngu__sage_init_sage_0.py in <module>()\n\n/home/mvngu/scratch/sage-3.4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.pyc in render3d(self, verbose)\n   1070         if S.ngens() != 4:\n   1071             print \"For 3-D fan rendering the polynomial ring must have 4 variables\"\n-> 1072             raise NotImplementedError\n   1073         g_cones = [q.groebner_cone() for q in self.reduced_groebner_bases()]\n   1074         g_cones_facets = [q.facets() for q in g_cones]\n\nNotImplementedError:\n```\n\nAgain, I see a `NotImplementedError` which is certainly more comprehensible than the error message reported above by William Stein. And finally, given the correct number of generators, we have a nice Groebner fan :-) Positive review for the problem that the patch fixes.",
    "created_at": "2009-03-26T08:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5465#issuecomment-42426",
    "user": "mvngu"
}
```

REFEREE REPORT



The patch **trac_5465_1.patch** applies OK against Sage 3.4, all doctests pass with the `-long` option as well. Since the purpose of the patch is to add more meaningful error messages, I tried to get those two more meaningful messages. First, for the case where the number of generators is < 3:

```
sage: # first for the case of S.ngens() < 3...
sage: R.<x,y> = PolynomialRing(QQ,2)
sage: G = R.ideal([y^3 - x^2, y^2 - 13*x]).groebner_fan()
sage: G.render()
For 2-D fan rendering the polynomial ring must have 3 variables (or more, which are ignored).
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (118, 0))

---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/16843/_home_mvngu__sage_init_sage_0.py in <module>()

/home/mvngu/scratch/sage-3.4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.pyc in render(self, file, larger, shift, rgbcolor, polyfill, scale_colors)
    902         if S.ngens() < 3:
    903             print "For 2-D fan rendering the polynomial ring must have 3 variables (or more, which are ignored)."
--> 904             raise NotImplementedError
    905         cmd = 'render'
    906         if shift:

NotImplementedError:
```

Yep, the error message is certainly now more comprehensible than something like `UnboundLocalError` which misses the main point that the number of generators is not of the required size.  Now, for the case where the number of generators is not 4:

```
sage: # second, for the case of S.ngens() != 4...
sage: P.<a,b,c> = PolynomialRing(QQ, 3, order="lex")
sage: sage.rings.ideal.Katsura(P,3).groebner_fan().render3d()
For 3-D fan rendering the polynomial ring must have 4 variables
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/mvngu/.sage/temp/sage.math.washington.edu/16843/_home_mvngu__sage_init_sage_0.py in <module>()

/home/mvngu/scratch/sage-3.4/local/lib/python2.5/site-packages/sage/rings/polynomial/groebner_fan.pyc in render3d(self, verbose)
   1070         if S.ngens() != 4:
   1071             print "For 3-D fan rendering the polynomial ring must have 4 variables"
-> 1072             raise NotImplementedError
   1073         g_cones = [q.groebner_cone() for q in self.reduced_groebner_bases()]
   1074         g_cones_facets = [q.facets() for q in g_cones]

NotImplementedError:
```

Again, I see a `NotImplementedError` which is certainly more comprehensible than the error message reported above by William Stein. And finally, given the correct number of generators, we have a nice Groebner fan :-) Positive review for the problem that the patch fixes.



---

archive/issue_comments_042427.json:
```json
{
    "body": "Well, to be absolutely pedantic: Shouldn't we add doctests that check the error messages being raised?\n\nI am happy to merge the patch \"as is\", but if someone wanted to submit such a patch I would not be unhappy ;)\n\nCheers,\n\nMichael",
    "created_at": "2009-03-26T23:14:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5465#issuecomment-42427",
    "user": "mabshoff"
}
```

Well, to be absolutely pedantic: Shouldn't we add doctests that check the error messages being raised?

I am happy to merge the patch "as is", but if someone wanted to submit such a patch I would not be unhappy ;)

Cheers,

Michael



---

archive/issue_comments_042428.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-26T23:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5465#issuecomment-42428",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_042429.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-26T23:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5465#issuecomment-42429",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_042430.json:
```json
{
    "body": "Replying to [comment:5 mabshoff]:\n> Well, to be absolutely pedantic: Shouldn't we add doctests that check the error messages being raised?\n> \n> I am happy to merge the patch \"as is\", but if someone wanted to submit such a patch I would not be unhappy ;)\n\n\nSome happiness is available at #5619 :-)",
    "created_at": "2009-03-27T03:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5465#issuecomment-42430",
    "user": "mvngu"
}
```

Replying to [comment:5 mabshoff]:
> Well, to be absolutely pedantic: Shouldn't we add doctests that check the error messages being raised?
> 
> I am happy to merge the patch "as is", but if someone wanted to submit such a patch I would not be unhappy ;)


Some happiness is available at #5619 :-)
