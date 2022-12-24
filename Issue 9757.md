# Issue 9757: implement Watkins-Delaunay's algorithm for computing modular degrees in Sage

archive/issues_009757.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @qed777 @robertwb @JohnCremona\n\nRelevant paper:\n\n    http://www.emis.ams.org/journals/EM/expmath/volumes/11/11.4/pp487_502.pdf\n\nWhen this is done and of comparable speed to the current modular degree code in Sage, then Sympow can be moved from standard to optional (or worse) as a Sage spkg.  Implementation options:\n\n* Build on top of the Dokchiter l-series code in Sage (via PARI)\n\n* Build something on Robert Bradshaw's soon-to-be-in-Sage re-implementation of Dokchitser:   #9193\n\nIssue created by migration from https://trac.sagemath.org/ticket/9758\n\n",
    "created_at": "2010-08-17T22:29:48Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "implement Watkins-Delaunay's algorithm for computing modular degrees in Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9757",
    "user": "@williamstein"
}
```
Assignee: @williamstein

CC:  @qed777 @robertwb @JohnCremona

Relevant paper:

    http://www.emis.ams.org/journals/EM/expmath/volumes/11/11.4/pp487_502.pdf

When this is done and of comparable speed to the current modular degree code in Sage, then Sympow can be moved from standard to optional (or worse) as a Sage spkg.  Implementation options:

* Build on top of the Dokchiter l-series code in Sage (via PARI)

* Build something on Robert Bradshaw's soon-to-be-in-Sage re-implementation of Dokchitser:   #9193

Issue created by migration from https://trac.sagemath.org/ticket/9758





---

archive/issue_comments_095577.json:
```json
{
    "body": "Kirkby said:\n> It would be good to state on the ticket what level of student project\n> this is (undergrad, postgrad), and the skill set needed (C, Python\n> etc). I expect you would prefer it in Python, though I think\n> personally a C implementation like Mark's, which you can easily call\n> from Python, would be more beneficial to the scientific community in\n> general - not everyone is using Sage/Python.\n\nGood idea.  \n\nLevel: graduate student or greater, with a background in number theory.\n\nSkill set needed:  read C, write Python, possibly Cython later for speed purposes. \n\nC versus Python: the implementation can depend on absolutely anything in Sage; for this I'm not concerned about providing a general tool for the scientific community.",
    "created_at": "2010-08-19T00:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9757#issuecomment-95577",
    "user": "@williamstein"
}
```

Kirkby said:
> It would be good to state on the ticket what level of student project
> this is (undergrad, postgrad), and the skill set needed (C, Python
> etc). I expect you would prefer it in Python, though I think
> personally a C implementation like Mark's, which you can easily call
> from Python, would be more beneficial to the scientific community in
> general - not everyone is using Sage/Python.

Good idea.  

Level: graduate student or greater, with a background in number theory.

Skill set needed:  read C, write Python, possibly Cython later for speed purposes. 

C versus Python: the implementation can depend on absolutely anything in Sage; for this I'm not concerned about providing a general tool for the scientific community.



---

archive/issue_comments_095578.json:
```json
{
    "body": "I'm adding John Cremona to this, as I think this is his area of interest. If not, John can delete himself!\n\nFor anyone taking this project on, it may be useful to know that in the opinion of Mark Watkins, double-precsion maths is **probably** good enough for computing the modular degrees. That would no doubt make the code simpler and faster than using MPFR. See\n\nhttp://groups.google.co.uk/group/sage-devel/msg/ecac09831622179c\n\nStrange as it may seem, fixing the SYMPOW bug (#9703) was actually one of the more interesting changes I've made to Sage. It required reading the paper in the quad double package to understand how that was supposed to work, then reading the Intel manual on the 387 processor to sort out how to get the processor to work as required by quad double. \n\nDave",
    "created_at": "2010-08-31T09:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9757#issuecomment-95578",
    "user": "drkirkby"
}
```

I'm adding John Cremona to this, as I think this is his area of interest. If not, John can delete himself!

For anyone taking this project on, it may be useful to know that in the opinion of Mark Watkins, double-precsion maths is **probably** good enough for computing the modular degrees. That would no doubt make the code simpler and faster than using MPFR. See

http://groups.google.co.uk/group/sage-devel/msg/ecac09831622179c

Strange as it may seem, fixing the SYMPOW bug (#9703) was actually one of the more interesting changes I've made to Sage. It required reading the paper in the quad double package to understand how that was supposed to work, then reading the Intel manual on the 387 processor to sort out how to get the processor to work as required by quad double. 

Dave



---

archive/issue_comments_095579.json:
```json
{
    "body": "Here's one case which can be used for testing (I have correspondence with Mark Watkins which explains the problem and how to fix it, and will open a new ticket for that):\n\n```\nsage: E = EllipticCurve([1,-1,0,-318360868065,-69208434591226115]) \nsage: E.modular_degree(algorithm='magma')                         \n2417135616\n```\n\nbut\n\n```\nsage: E = EllipticCurve([1,-1,0,-318360868065,-69208434591226115]) \nsage: E.modular_degree()    \n# boom\n```\n",
    "created_at": "2012-09-29T22:07:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9757#issuecomment-95579",
    "user": "@JohnCremona"
}
```

Here's one case which can be used for testing (I have correspondence with Mark Watkins which explains the problem and how to fix it, and will open a new ticket for that):

```
sage: E = EllipticCurve([1,-1,0,-318360868065,-69208434591226115]) 
sage: E.modular_degree(algorithm='magma')                         
2417135616
```

but

```
sage: E = EllipticCurve([1,-1,0,-318360868065,-69208434591226115]) 
sage: E.modular_degree()    
# boom
```

