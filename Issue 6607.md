# Issue 6607: Quadratics in GF(2^m)

archive/issues_006607.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: quadratics, characteristic 2\n\nAdded specialized code for factoring quadratic polynomials over GF(2^m).\n\nIssue created by migration from https://trac.sagemath.org/ticket/6607\n\n",
    "created_at": "2009-07-23T22:36:10Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "Quadratics in GF(2^m)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6607",
    "user": "wakep"
}
```
Assignee: tbd

Keywords: quadratics, characteristic 2

Added specialized code for factoring quadratic polynomials over GF(2^m).

Issue created by migration from https://trac.sagemath.org/ticket/6607





---

archive/issue_comments_054095.json:
```json
{
    "body": "Please follow coding conventions, especially those documented in the [Developers' Guide](http://www.sagemath.org/doc/developer/conventions.html#python-coding-conventions) and [PEP-0008](http://www.python.org/dev/peps/pep-0008/). Don't be afraid to use white spaces in your code. The patch contains codes that are squeezed together; this is difficult to read. For example, this is bad:\n\n```\ndef gftwosqrt(r): \n    \"\"\" \n    Quickly finds the squareroot of an element in GF(2^m) \n    \"\"\"\n    F=r.parent() \n    c=F.cardinality() \n    return r**(c/2)\n```\n\nand you should do this instead:\n\n```\ndef gftwosqrt(r): \n    \"\"\" \n    Quickly finds the squareroot of an element in GF(2^m)\n    \n    INPUT:\n    \n    <explain any input to this function>\n    \n    OUTPUT:\n    \n    <what's the expected output of this function?>\n    \n    EXAMPLES::\n    \n        <add-more-doctests-here>\n    \"\"\"\n    F = r.parent() \n    c = F.cardinality() \n    return r**(c/2)\n```\n\nFor more information about writing docstrings, see [this section](http://www.sagemath.org/doc/developer/conventions.html#documentation-strings). Apart from these, there are other reasons to reject the patch, as documented [here](http://www.sagemath.org/doc/developer/trac.html).",
    "created_at": "2009-08-04T07:13:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6607#issuecomment-54095",
    "user": "mvngu"
}
```

Please follow coding conventions, especially those documented in the [Developers' Guide](http://www.sagemath.org/doc/developer/conventions.html#python-coding-conventions) and [PEP-0008](http://www.python.org/dev/peps/pep-0008/). Don't be afraid to use white spaces in your code. The patch contains codes that are squeezed together; this is difficult to read. For example, this is bad:

```
def gftwosqrt(r): 
    """ 
    Quickly finds the squareroot of an element in GF(2^m) 
    """
    F=r.parent() 
    c=F.cardinality() 
    return r**(c/2)
```

and you should do this instead:

```
def gftwosqrt(r): 
    """ 
    Quickly finds the squareroot of an element in GF(2^m)
    
    INPUT:
    
    <explain any input to this function>
    
    OUTPUT:
    
    <what's the expected output of this function?>
    
    EXAMPLES::
    
        <add-more-doctests-here>
    """
    F = r.parent() 
    c = F.cardinality() 
    return r**(c/2)
```

For more information about writing docstrings, see [this section](http://www.sagemath.org/doc/developer/conventions.html#documentation-strings). Apart from these, there are other reasons to reject the patch, as documented [here](http://www.sagemath.org/doc/developer/trac.html).



---

archive/issue_comments_054096.json:
```json
{
    "body": "fixed old patch... better documentation etc",
    "created_at": "2009-08-13T04:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6607#issuecomment-54096",
    "user": "wakep"
}
```

fixed old patch... better documentation etc



---

archive/issue_comments_054097.json:
```json
{
    "body": "Attachment\n\nfixed references",
    "created_at": "2009-08-17T21:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6607#issuecomment-54097",
    "user": "wakep"
}
```

Attachment

fixed references



---

archive/issue_comments_054098.json:
```json
{
    "body": "quad.patch should replace 12538.patch",
    "created_at": "2009-08-26T23:26:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6607#issuecomment-54098",
    "user": "wakep"
}
```

quad.patch should replace 12538.patch



---

archive/issue_comments_054099.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-15T10:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6607#issuecomment-54099",
    "user": "AlexGhitza"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_054100.json:
```json
{
    "body": "This has been sitting for a while and got some bitrot.  It doesn't apply cleanly against sage-4.2.\n\nPreston, can you rebase it on sage-4.2?  I'll try to review it quickly after that so you don't have to do this again.\n\nActually, while you're at it, do you want to just put up a new standalone patch?  As it stands now, quad.patch is dependent on 12538.patch.",
    "created_at": "2009-11-15T10:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6607#issuecomment-54100",
    "user": "AlexGhitza"
}
```

This has been sitting for a while and got some bitrot.  It doesn't apply cleanly against sage-4.2.

Preston, can you rebase it on sage-4.2?  I'll try to review it quickly after that so you don't have to do this again.

Actually, while you're at it, do you want to just put up a new standalone patch?  As it stands now, quad.patch is dependent on 12538.patch.
