# Issue 3107: Triangulation doesn't automatically happen for x3d output of 3d objects

archive/issues_003107.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: P = plot3d(lambda x,y: 4 - x^3 - y^2, (-2,2), (-2,2), color='green')\nprint P.x3d()\n\n<X3D version='3.0' profile='Immersive' xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation=' http://www.web3d.org/specifications/x3d-3.0.xsd '>\n<head>\n<meta name='title' content='sage3d'/>\n</head>\n<Scene>\n<Viewpoint position='0 0 6'/>\n<Shape>\n<IndexedFaceSet coordIndex=',-1'>\n  <Coordinate point=''/>\n</IndexedFaceSet>\n<Appearance><Material diffuseColor='0 1.0 0.0' shininess='1' specularColor='0.0 0.0 0.0'/></Appearance></Shape>\n\n</Scene>\n</X3D>\n\n```\n\n\nNote the empyt vertex data. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3107\n\n",
    "created_at": "2008-05-06T00:47:16Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "Triangulation doesn't automatically happen for x3d output of 3d objects",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3107",
    "user": "@robertwb"
}
```
Assignee: @williamstein


```
sage: P = plot3d(lambda x,y: 4 - x^3 - y^2, (-2,2), (-2,2), color='green')
print P.x3d()

<X3D version='3.0' profile='Immersive' xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation=' http://www.web3d.org/specifications/x3d-3.0.xsd '>
<head>
<meta name='title' content='sage3d'/>
</head>
<Scene>
<Viewpoint position='0 0 6'/>
<Shape>
<IndexedFaceSet coordIndex=',-1'>
  <Coordinate point=''/>
</IndexedFaceSet>
<Appearance><Material diffuseColor='0 1.0 0.0' shininess='1' specularColor='0.0 0.0 0.0'/></Appearance></Shape>

</Scene>
</X3D>

```


Note the empyt vertex data. 

Issue created by migration from https://trac.sagemath.org/ticket/3107





---

archive/issue_comments_021472.json:
```json
{
    "body": "Attachment [3107-x3d-triangulation.patch](tarball://root/attachments/some-uuid/ticket3107/3107-x3d-triangulation.patch) by @robertwb created at 2008-05-07 06:45:32",
    "created_at": "2008-05-07T06:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3107#issuecomment-21472",
    "user": "@robertwb"
}
```

Attachment [3107-x3d-triangulation.patch](tarball://root/attachments/some-uuid/ticket3107/3107-x3d-triangulation.patch) by @robertwb created at 2008-05-07 06:45:32



---

archive/issue_comments_021473.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_gfurnish\".",
    "created_at": "2008-06-15T21:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3107#issuecomment-21473",
    "user": "@craigcitro"
}
```

Changing keywords from "" to "editor_gfurnish".



---

archive/issue_comments_021474.json:
```json
{
    "body": "Merged in Sage 3.0.3.rc0",
    "created_at": "2008-06-15T23:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3107#issuecomment-21474",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.rc0



---

archive/issue_comments_021475.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-15T23:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3107#issuecomment-21475",
    "user": "mabshoff"
}
```

Resolution: fixed
