# Issue 6647: Permutation Group improvements

archive/issues_006647.json:
```json
{
    "body": "Assignee: nborie\n\nCC:  sage-combinat\n\nKeywords: permutationgroup, orbit, stabilizer, transversal\n\nAdd transversal, orbit, stabilizer to PermutationGroup sage object.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6647\n\n",
    "created_at": "2009-07-28T12:10:21Z",
    "labels": [
        "group theory",
        "major",
        "enhancement"
    ],
    "title": "Permutation Group improvements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6647",
    "user": "nborie"
}
```
Assignee: nborie

CC:  sage-combinat

Keywords: permutationgroup, orbit, stabilizer, transversal

Add transversal, orbit, stabilizer to PermutationGroup sage object.

Issue created by migration from https://trac.sagemath.org/ticket/6647





---

archive/issue_comments_054512.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-07-28T13:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54512",
    "user": "nborie"
}
```

Attachment



---

archive/issue_comments_054513.json:
```json
{
    "body": "This is a nice addition. I have a question though.\n\nIn the docstring for a transversal, you have `Return a list of representatives of the orbit of the given integer in the group.` The usual definition (as one finds for example in wikipedia) is `... given a subgroup H of a group G, a right (respectively left) transversal is a set containing exactly one element from each right (respectively left) coset of H.`. I'm just wondering if this docstring is a bit confusing?",
    "created_at": "2009-07-28T14:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54513",
    "user": "wdj"
}
```

This is a nice addition. I have a question though.

In the docstring for a transversal, you have `Return a list of representatives of the orbit of the given integer in the group.` The usual definition (as one finds for example in wikipedia) is `... given a subgroup H of a group G, a right (respectively left) transversal is a set containing exactly one element from each right (respectively left) coset of H.`. I'm just wondering if this docstring is a bit confusing?



---

archive/issue_comments_054514.json:
```json
{
    "body": "Hello wdj,\n\nThis is one piece i need for strong generating system thus generate integer vector up to action of a permgroup thus invariant theory of multivariate polynomials. The road will be long...\n\nMy English is pretty horrible. You're definitely right. I don't really know in which order place my words and that can change the meaning. Here I Think the transversals as Representative of the quotient G/G_{integer} where G_{integer} = subgroup of G which stabilize integer.\n\nThe reviewer have to feel free of correcting, susgesting improvement and hiting me for my mistakes.",
    "created_at": "2009-07-28T14:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54514",
    "user": "nborie"
}
```

Hello wdj,

This is one piece i need for strong generating system thus generate integer vector up to action of a permgroup thus invariant theory of multivariate polynomials. The road will be long...

My English is pretty horrible. You're definitely right. I don't really know in which order place my words and that can change the meaning. Here I Think the transversals as Representative of the quotient G/G_{integer} where G_{integer} = subgroup of G which stabilize integer.

The reviewer have to feel free of correcting, susgesting improvement and hiting me for my mistakes.



---

archive/issue_comments_054515.json:
```json
{
    "body": "Replying to [comment:5 nborie]:\n> Hello wdj,\n> \n> This is one piece i need for strong generating system thus generate integer vector up to action of a permgroup thus invariant theory of multivariate polynomials. The road will be long...\n> \n> My English is pretty horrible. You're definitely right. I don't really know in which order place my words and that can change the meaning. Here I Think the transversals as Representative of the quotient G/G_{integer} where G_{integer} = subgroup of G which stabilize integer.\n> \n> The reviewer have to feel free of correcting, susgesting improvement and hiting me for my mistakes.\n\n\nI would replace `Return a list of representatives of the orbit of the given integer in the group` by \n`If G is a permutation group acting on the set X = {1, 2, ...., n} and H is the stabilizer subgroup of <integer>, a right (respectively left) transversal is a set containing exactly one element from each right (respectively left) coset of H. This method returns a right transversal of G by H.`\n\nHowever, if this is to be reviewed by applying 6620 and then this patch, I can tell you that I had a problem \ndoing that.",
    "created_at": "2009-07-28T18:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54515",
    "user": "wdj"
}
```

Replying to [comment:5 nborie]:
> Hello wdj,
> 
> This is one piece i need for strong generating system thus generate integer vector up to action of a permgroup thus invariant theory of multivariate polynomials. The road will be long...
> 
> My English is pretty horrible. You're definitely right. I don't really know in which order place my words and that can change the meaning. Here I Think the transversals as Representative of the quotient G/G_{integer} where G_{integer} = subgroup of G which stabilize integer.
> 
> The reviewer have to feel free of correcting, susgesting improvement and hiting me for my mistakes.


I would replace `Return a list of representatives of the orbit of the given integer in the group` by 
`If G is a permutation group acting on the set X = {1, 2, ...., n} and H is the stabilizer subgroup of <integer>, a right (respectively left) transversal is a set containing exactly one element from each right (respectively left) coset of H. This method returns a right transversal of G by H.`

However, if this is to be reviewed by applying 6620 and then this patch, I can tell you that I had a problem 
doing that.



---

archive/issue_comments_054516.json:
```json
{
    "body": "Changing keywords from \"permutationgroup, orbit, stabilizer, transversal\" to \"permutationgroup, orbit, stabilizer, transversal, strong generating system\".",
    "created_at": "2009-08-12T14:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54516",
    "user": "nborie"
}
```

Changing keywords from "permutationgroup, orbit, stabilizer, transversal" to "permutationgroup, orbit, stabilizer, transversal, strong generating system".



---

archive/issue_comments_054517.json:
```json
{
    "body": "Add a strong generating system method.\n\nI really need this method and so, this first implementation is not very good. The data structure (list of list) is dense and perhaps not very adapted (the python list begin at zero and the structure should be in correlation with positions and integer...(Dictionary? , family?, ...) ). This is really not optimized (I am waiting for LinGap...). If it goes in Sage as a first version, one could easily improve it...  \n \nComments, corrections, suggestions welcome!\n\nWdj : What kind of problem ? Is it a problem of export ? ... On the sage-combinat queue, the two patch work well...",
    "created_at": "2009-08-12T14:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54517",
    "user": "nborie"
}
```

Add a strong generating system method.

I really need this method and so, this first implementation is not very good. The data structure (list of list) is dense and perhaps not very adapted (the python list begin at zero and the structure should be in correlation with positions and integer...(Dictionary? , family?, ...) ). This is really not optimized (I am waiting for LinGap...). If it goes in Sage as a first version, one could easily improve it...  
 
Comments, corrections, suggestions welcome!

Wdj : What kind of problem ? Is it a problem of export ? ... On the sage-combinat queue, the two patch work well...



---

archive/issue_comments_054518.json:
```json
{
    "body": "Replying to [comment:8 nborie]:\n> Add a strong generating system method.\n> \n...\n> \n> Wdj : What kind of problem ? Is it a problem of export ? ... On the sage-combinat queue, the two patch work well...\n\nI've forgotten now the exact problem. I guess hg_sage.apply did not work for me. What does \"the sage-combinat queue\" mean? Does sage-combinat have their own trac system?",
    "created_at": "2009-08-12T14:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54518",
    "user": "wdj"
}
```

Replying to [comment:8 nborie]:
> Add a strong generating system method.
> 
...
> 
> Wdj : What kind of problem ? Is it a problem of export ? ... On the sage-combinat queue, the two patch work well...

I've forgotten now the exact problem. I guess hg_sage.apply did not work for me. What does "the sage-combinat queue" mean? Does sage-combinat have their own trac system?



---

archive/issue_comments_054519.json:
```json
{
    "body": "We just work with in special branch with a special mercurial queue I think... (the system is so complicated...)\n\n\n```\nnicolas@Lancelot:/opt/sage/devel/sage-combinat$ hg qtop\ntrac_6647_permutationgroup_improvement.patch\nnicolas@Lancelot:/opt/sage/devel/sage-combinat$ hg qpop\nNow at: trac_6620.patch\nnicolas@Lancelot:/opt/sage/devel/sage-combinat$ hg qpush\napplying trac_6647_permutationgroup_improvement.patch\nNow at: trac_6647_permutationgroup_improvement.patch\nnicolas@Lancelot:/opt/sage/devel/sage-combinat$ sage -b\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nTime to execute 0 commands: 1.28746032715e-05 seconds\nFinished compiling Cython code (time = 0.407410144806 seconds)\nrunning install\nrunning build\nrunning build_py\ncopying sage/groups/perm_gps/permgroup.py -> build/lib.linux-i686-2.6/sage/groups/perm_gps\nrunning build_ext\nTotal time spent compiling C/C++ extensions:  0.0105719566345 seconds.\nrunning install_lib\ncopying build/lib.linux-i686-2.6/sage/groups/perm_gps/permgroup.py -> /opt/sage/local/lib/python2.6/site-packages/sage/groups/perm_gps\nbyte-compiling /opt/sage/local/lib/python2.6/site-packages/sage/groups/perm_gps/permgroup.py to permgroup.pyc\nrunning install_egg_info\nRemoving /opt/sage/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\nWriting /opt/sage/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\n\nreal\t0m1.391s\nuser\t0m1.132s\nsys\t0m0.252s\nnicolas@Lancelot:/opt/sage/devel/sage-combinat$ \n```\n\n\nhg = hg_sage in my shell\n\nI never use hg apply in fact as I work every times with the shared combinat branch and repository...\n--> http://combinat.sagemath.org/patches/",
    "created_at": "2009-08-12T14:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54519",
    "user": "nborie"
}
```

We just work with in special branch with a special mercurial queue I think... (the system is so complicated...)


```
nicolas@Lancelot:/opt/sage/devel/sage-combinat$ hg qtop
trac_6647_permutationgroup_improvement.patch
nicolas@Lancelot:/opt/sage/devel/sage-combinat$ hg qpop
Now at: trac_6620.patch
nicolas@Lancelot:/opt/sage/devel/sage-combinat$ hg qpush
applying trac_6647_permutationgroup_improvement.patch
Now at: trac_6647_permutationgroup_improvement.patch
nicolas@Lancelot:/opt/sage/devel/sage-combinat$ sage -b

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Time to execute 0 commands: 1.28746032715e-05 seconds
Finished compiling Cython code (time = 0.407410144806 seconds)
running install
running build
running build_py
copying sage/groups/perm_gps/permgroup.py -> build/lib.linux-i686-2.6/sage/groups/perm_gps
running build_ext
Total time spent compiling C/C++ extensions:  0.0105719566345 seconds.
running install_lib
copying build/lib.linux-i686-2.6/sage/groups/perm_gps/permgroup.py -> /opt/sage/local/lib/python2.6/site-packages/sage/groups/perm_gps
byte-compiling /opt/sage/local/lib/python2.6/site-packages/sage/groups/perm_gps/permgroup.py to permgroup.pyc
running install_egg_info
Removing /opt/sage/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /opt/sage/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info

real	0m1.391s
user	0m1.132s
sys	0m0.252s
nicolas@Lancelot:/opt/sage/devel/sage-combinat$ 
```


hg = hg_sage in my shell

I never use hg apply in fact as I work every times with the shared combinat branch and repository...
--> http://combinat.sagemath.org/patches/



---

archive/issue_comments_054520.json:
```json
{
    "body": "I fix a problem : any stabilizer must have the same degree of the permgroup in argument. I hardcoded that because I don't know how to do that in a better way...",
    "created_at": "2009-08-13T10:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54520",
    "user": "nborie"
}
```

I fix a problem : any stabilizer must have the same degree of the permgroup in argument. I hardcoded that because I don't know how to do that in a better way...



---

archive/issue_comments_054521.json:
```json
{
    "body": "I wonder if this patch was been submitted to the wrong trac system. I guess what the author is saying in some comments above is that the patch is to be applied to the sage-combinat version of sage, not the \"standard\" version. If that is correct, then either the patch should be submitted t the sage-combinat trac or rebased for the \"standard\" version. If that is not correct, then a better explanation of why it does not apply to the \"standard\" sage could be helpful.",
    "created_at": "2009-08-13T10:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54521",
    "user": "wdj"
}
```

I wonder if this patch was been submitted to the wrong trac system. I guess what the author is saying in some comments above is that the patch is to be applied to the sage-combinat version of sage, not the "standard" version. If that is correct, then either the patch should be submitted t the sage-combinat trac or rebased for the "standard" version. If that is not correct, then a better explanation of why it does not apply to the "standard" sage could be helpful.



---

archive/issue_comments_054522.json:
```json
{
    "body": "I am very sorry for all the misunderstanding I produce... I think there is only one trac and only one sage. Franco or Nicolas (Thi\u00e9ry) could say that better than me but i think we work with a special repository but we try to say the closer we can to the real sage version. I think that is my fault and and should try to work with different version of sage on my computer. I really should based that for the standard version... I really think there is only one way to go in sage (the trac, the only...).\n\nSorry and thank for your comments. I continue my formation on sage...",
    "created_at": "2009-08-13T11:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54522",
    "user": "nborie"
}
```

I am very sorry for all the misunderstanding I produce... I think there is only one trac and only one sage. Franco or Nicolas (Thiéry) could say that better than me but i think we work with a special repository but we try to say the closer we can to the real sage version. I think that is my fault and and should try to work with different version of sage on my computer. I really should based that for the standard version... I really think there is only one way to go in sage (the trac, the only...).

Sorry and thank for your comments. I continue my formation on sage...



---

archive/issue_comments_054523.json:
```json
{
    "body": "I installed a new sage 4.1 and applyed only #6620 and #6647... It seems to work for me.\n\n```\nnicolas@Lancelot:~/sage_standard$ ./sage -t devel/sage-main/sage/groups/perm_gps/permgroup.py\nsage -t  \"devel/sage-main/sage/groups/perm_gps/permgroup.py\"\n\t [5.0 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 5.0 seconds\nnicolas@Lancelot:~/sage_standard$ \n```\n\nI must disturb the combinat guys too because the combinat wiki don't say how to interface from combinat patches to trac patches. If someone can tell me how it would normally work...",
    "created_at": "2009-08-13T15:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54523",
    "user": "nborie"
}
```

I installed a new sage 4.1 and applyed only #6620 and #6647... It seems to work for me.

```
nicolas@Lancelot:~/sage_standard$ ./sage -t devel/sage-main/sage/groups/perm_gps/permgroup.py
sage -t  "devel/sage-main/sage/groups/perm_gps/permgroup.py"
	 [5.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 5.0 seconds
nicolas@Lancelot:~/sage_standard$ 
```

I must disturb the combinat guys too because the combinat wiki don't say how to interface from combinat patches to trac patches. If someone can tell me how it would normally work...



---

archive/issue_comments_054524.json:
```json
{
    "body": "This still doesn't work for me. I don't understand the problem. On 4.1.alpha3, I ran\n\n\n```\nsage: hg_sage.apply(\"/Users/davidjoyner/sagefiles/trac_6620.patch\")\n```\n\nThis worked fine. Then I ran\n\n\n```\nsage: hg_sage.apply(\"/Users/davidjoyner/sagefiles/trac_6647_permutationgroup_improvement_2.patch\")\n```\n\nbut this did not apply and instead opened up vi. I aborted the patch, since I didn't know what else to do.",
    "created_at": "2009-08-14T00:49:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54524",
    "user": "wdj"
}
```

This still doesn't work for me. I don't understand the problem. On 4.1.alpha3, I ran


```
sage: hg_sage.apply("/Users/davidjoyner/sagefiles/trac_6620.patch")
```

This worked fine. Then I ran


```
sage: hg_sage.apply("/Users/davidjoyner/sagefiles/trac_6647_permutationgroup_improvement_2.patch")
```

but this did not apply and instead opened up vi. I aborted the patch, since I didn't know what else to do.



---

archive/issue_comments_054525.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-08-16T15:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54525",
    "user": "nborie"
}
```

Attachment



---

archive/issue_comments_054526.json:
```json
{
    "body": "I hope it will be Ok now. Jason Bandlow noticed that hg informations was missing in my patches. Beginner mystake : I did not export my patches (hg export) but just upload the files from .hg/patches to the trac. Sorry for that...",
    "created_at": "2009-08-16T15:53:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54526",
    "user": "nborie"
}
```

I hope it will be Ok now. Jason Bandlow noticed that hg informations was missing in my patches. Beginner mystake : I did not export my patches (hg export) but just upload the files from .hg/patches to the trac. Sorry for that...



---

archive/issue_comments_054527.json:
```json
{
    "body": "This (and the dependency #6620) applied fine to 4.1.1.rc2, on an intel macbook running 10.4.11. Although sage -testall gave\n\n\n```\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/interfaces/maxima.py\"\n        sage -t  \"devel/sage/sage/symbolic/expression.pyx\"\n```\n\nI think these are unrelated (and known) failures.\n\nDocstrings look good. Positive review from me. Are there other tests (eg, other platforms) needed to run before changing :needs\" to \"positive\"?",
    "created_at": "2009-08-18T19:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54527",
    "user": "wdj"
}
```

This (and the dependency #6620) applied fine to 4.1.1.rc2, on an intel macbook running 10.4.11. Although sage -testall gave


```
The following tests failed:


        sage -t  "devel/sage/sage/interfaces/maxima.py"
        sage -t  "devel/sage/sage/symbolic/expression.pyx"
```

I think these are unrelated (and known) failures.

Docstrings look good. Positive review from me. Are there other tests (eg, other platforms) needed to run before changing :needs" to "positive"?



---

archive/issue_comments_054528.json:
```json
{
    "body": "Attachment\n\nreviewer patch; fix ReST formatting typos",
    "created_at": "2009-08-25T02:02:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54528",
    "user": "mvngu"
}
```

Attachment

reviewer patch; fix ReST formatting typos



---

archive/issue_comments_054529.json:
```json
{
    "body": "The patch `trac_6647-reviewer.patch` fixes some ReST formatting typos found in `trac_6647_permutationgroup_improvement_2.patch`. Such typos result in warnings when building the reference manual. If people are happy with the changes in `trac_6647-reviewer.patch`, then patches should be merged in this order:\n\n1. `trac_6647_permutationgroup_improvement_2.patch`\n2. `trac_6647-reviewer.patch`",
    "created_at": "2009-08-25T02:05:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54529",
    "user": "mvngu"
}
```

The patch `trac_6647-reviewer.patch` fixes some ReST formatting typos found in `trac_6647_permutationgroup_improvement_2.patch`. Such typos result in warnings when building the reference manual. If people are happy with the changes in `trac_6647-reviewer.patch`, then patches should be merged in this order:

1. `trac_6647_permutationgroup_improvement_2.patch`
2. `trac_6647-reviewer.patch`



---

archive/issue_comments_054530.json:
```json
{
    "body": "The reviewer ReST fixes seems good to me. Thanks for fix it. As I don't manage the trac when review over review appear, I leave another people change the status to positive...",
    "created_at": "2009-08-25T12:11:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54530",
    "user": "nborie"
}
```

The reviewer ReST fixes seems good to me. Thanks for fix it. As I don't manage the trac when review over review appear, I leave another people change the status to positive...



---

archive/issue_comments_054531.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-25T17:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54531",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_054532.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac_6647_permutationgroup_improvement_2.patch`\n2. `trac_6647-reviewer.patch`",
    "created_at": "2009-08-25T17:47:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54532",
    "user": "mvngu"
}
```

Merged patches in this order:

1. `trac_6647_permutationgroup_improvement_2.patch`
2. `trac_6647-reviewer.patch`



---

archive/issue_comments_054533.json:
```json
{
    "body": "This may have caused a doctest failure -- see #7206.",
    "created_at": "2009-10-14T03:07:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6647",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6647#issuecomment-54533",
    "user": "ddrake"
}
```

This may have caused a doctest failure -- see #7206.
