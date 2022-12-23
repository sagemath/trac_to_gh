# Issue 6074: Planar graph generation

archive/issues_006074.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  ncohen mvngu slelievre\n\nEssentially, this shouldn't be too difficult to implement in Sage:\n\nhttp://cs.anu.edu.au/~bdm/papers/plantri-full.pdf\n\nThe basic steps to generate plane graphs (graphs embedded in the plane) of minimum degree at least `d`, connectivity at least `k`, number of edges at least `e`, and max face size at most `p`, are:\n\n1. Implement section 1.3 of the above paper. This allows for a much faster implementation of automorphism group and isomorphism in the case of plane graphs.\n\n2. Generate all planar triangluations, with min degree at least `max(d,3)`, connectivity at least `max(k,3)`. This is described in section 1.2, mainly the third paragraph. Essentially, you start with K_4, and you augment by one of the three moves E_3, E_4, or E_5. The \"backwards\" step in canonical augmentation here is to first try to remove the least-labeled vertex of degree 3, i.e. try to undo E_3 if possible, or degree 4 if that is possible, i.e. try to undo E_4 if possible, then finally checking for degree 5.\n\n3. Use these, together with edge deletion and canonical augmentation, to generate all plane graphs.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6074\n\n",
    "created_at": "2009-05-18T19:06:13Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "Planar graph generation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6074",
    "user": "rlm"
}
```
Assignee: rlm

CC:  ncohen mvngu slelievre

Essentially, this shouldn't be too difficult to implement in Sage:

http://cs.anu.edu.au/~bdm/papers/plantri-full.pdf

The basic steps to generate plane graphs (graphs embedded in the plane) of minimum degree at least `d`, connectivity at least `k`, number of edges at least `e`, and max face size at most `p`, are:

1. Implement section 1.3 of the above paper. This allows for a much faster implementation of automorphism group and isomorphism in the case of plane graphs.

2. Generate all planar triangluations, with min degree at least `max(d,3)`, connectivity at least `max(k,3)`. This is described in section 1.2, mainly the third paragraph. Essentially, you start with K_4, and you augment by one of the three moves E_3, E_4, or E_5. The "backwards" step in canonical augmentation here is to first try to remove the least-labeled vertex of degree 3, i.e. try to undo E_3 if possible, or degree 4 if that is possible, i.e. try to undo E_4 if possible, then finally checking for degree 5.

3. Use these, together with edge deletion and canonical augmentation, to generate all plane graphs.

Issue created by migration from https://trac.sagemath.org/ticket/6074





---

archive/issue_comments_048351.json:
```json
{
    "body": "Add myself since I'm interested in (implementing the ideas of) this ticket.",
    "created_at": "2009-05-19T02:08:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6074#issuecomment-48351",
    "user": "mvngu"
}
```

Add myself since I'm interested in (implementing the ideas of) this ticket.



---

archive/issue_comments_048352.json:
```json
{
    "body": "Related subject, recently published : Uniform random sampling of planar graphs in linear time \n\nThe paper and a Java implementation are available on :\nhttp://algo.inria.fr/fusy/",
    "created_at": "2009-07-04T09:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6074#issuecomment-48352",
    "user": "ncohen"
}
```

Related subject, recently published : Uniform random sampling of planar graphs in linear time 

The paper and a Java implementation are available on :
http://algo.inria.fr/fusy/



---

archive/issue_comments_048353.json:
```json
{
    "body": "Now partially available via plantri spkg : #16970",
    "created_at": "2014-11-14T13:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6074#issuecomment-48353",
    "user": "chapoton"
}
```

Now partially available via plantri spkg : #16970



---

archive/issue_comments_048354.json:
```json
{
    "body": "Changing keywords from \"\" to \"planar graph, triangulation\".",
    "created_at": "2018-06-27T07:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6074#issuecomment-48354",
    "user": "slelievre"
}
```

Changing keywords from "" to "planar graph, triangulation".



---

archive/issue_comments_048355.json:
```json
{
    "body": "Replying to [comment:2 ncohen]:\n> Related subject, recently published : Uniform random sampling of planar graphs in linear time \n> \n> The paper and a Java implementation are available on :\n> http://algo.inria.fr/fusy/\n\nFor future reference, Eric Fusy's page is now at:\nhttp://www.lix.polytechnique.fr/Labo/Eric.Fusy/\n\nExcerpt of that page about that paper and Java implementation:\n\n> **Uniform random sampling of planar graphs in linear time.**\n>\n> Random Structures and Algorithms 35(4): 464-522 (2009).\n> [pdf](http://www.lix.polytechnique.fr/Labo/Eric.Fusy/Articles/Fusy08_planar_graphs.pdf)\n>\n> Short version, under the title \"Quadratic exact-size and linear approximate-size random generation of planar graphs\": Proceedings of the AofA'05 Conference (Analysis of Algorithms-2005), published in Discrete Mathematics and Theoretical Computer Science (DMTCS) Proceedings, vol AD, pp. 125-138 (2005).\n> [pdf](http://www.lix.polytechnique.fr/Labo/Eric.Fusy/Articles/FusyAofa.pdf)\n>\n> Implementation (in java) [tar.gz](http://www.lix.polytechnique.fr/Labo/Eric.Fusy/Programs/BoltzmannPlanarGraphs.tar.gz)\n\nRegarding plantri, one can now install it as an optional package by running the following in a terminal\n\n```\nsage -i plantri\n```\n\n(not sure if one needs to then run `make` from the directory where Sage is installed).",
    "created_at": "2018-06-27T07:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6074",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6074#issuecomment-48355",
    "user": "slelievre"
}
```

Replying to [comment:2 ncohen]:
> Related subject, recently published : Uniform random sampling of planar graphs in linear time 
> 
> The paper and a Java implementation are available on :
> http://algo.inria.fr/fusy/

For future reference, Eric Fusy's page is now at:
http://www.lix.polytechnique.fr/Labo/Eric.Fusy/

Excerpt of that page about that paper and Java implementation:

> **Uniform random sampling of planar graphs in linear time.**
>
> Random Structures and Algorithms 35(4): 464-522 (2009).
> [pdf](http://www.lix.polytechnique.fr/Labo/Eric.Fusy/Articles/Fusy08_planar_graphs.pdf)
>
> Short version, under the title "Quadratic exact-size and linear approximate-size random generation of planar graphs": Proceedings of the AofA'05 Conference (Analysis of Algorithms-2005), published in Discrete Mathematics and Theoretical Computer Science (DMTCS) Proceedings, vol AD, pp. 125-138 (2005).
> [pdf](http://www.lix.polytechnique.fr/Labo/Eric.Fusy/Articles/FusyAofa.pdf)
>
> Implementation (in java) [tar.gz](http://www.lix.polytechnique.fr/Labo/Eric.Fusy/Programs/BoltzmannPlanarGraphs.tar.gz)

Regarding plantri, one can now install it as an optional package by running the following in a terminal

```
sage -i plantri
```

(not sure if one needs to then run `make` from the directory where Sage is installed).
