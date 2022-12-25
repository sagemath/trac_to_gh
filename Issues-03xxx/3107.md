# Issue 3107: [with patch, with positive review] Triangulation doesn't automatically happen for x3d output of 3d objects

archive/issues_003107.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: editor_gfurnish\n\n```\nsage: P = plot3d(lambda x,y: 4 - x^3 - y^2, (-2,2), (-2,2), color='green')\nprint P.x3d()\n\n<X3D version='3.0' profile='Immersive' xmlns:xsd='http://www.w3.org/2001/XMLSchema-instance' xsd:noNamespaceSchemaLocation=' http://www.web3d.org/specifications/x3d-3.0.xsd '>\n<head>\n<meta name='title' content='sage3d'/>\n</head>\n<Scene>\n<Viewpoint position='0 0 6'/>\n<Shape>\n<IndexedFaceSet coordIndex=',-1'>\n  <Coordinate point=''/>\n</IndexedFaceSet>\n<Appearance><Material diffuseColor='0 1.0 0.0' shininess='1' specularColor='0.0 0.0 0.0'/></Appearance></Shape>\n\n</Scene>\n</X3D>\n\n```\n\nNote the empyt vertex data. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3107\n\n",
    "closed_at": "2008-06-15T23:11:40Z",
    "created_at": "2008-05-06T00:47:16Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch, with positive review] Triangulation doesn't automatically happen for x3d output of 3d objects",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3107",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

Keywords: editor_gfurnish

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

archive/issue_comments_021428.json:
```json
{
    "body": "Attachment [3107-x3d-triangulation.patch](tarball://root/attachments/some-uuid/ticket3107/3107-x3d-triangulation.patch) by @robertwb created at 2008-05-07 06:45:32",
    "created_at": "2008-05-07T06:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3107#issuecomment-21428",
    "user": "https://github.com/robertwb"
}
```

Attachment [3107-x3d-triangulation.patch](tarball://root/attachments/some-uuid/ticket3107/3107-x3d-triangulation.patch) by @robertwb created at 2008-05-07 06:45:32



---

archive/issue_comments_021429.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_gfurnish\".",
    "created_at": "2008-06-15T21:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3107#issuecomment-21429",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_gfurnish".



---

archive/issue_comments_021430.json:
```json
{
    "body": "Merged in Sage 3.0.3.rc0",
    "created_at": "2008-06-15T23:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3107#issuecomment-21430",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.3.rc0



---

archive/issue_comments_021431.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-15T23:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3107#issuecomment-21431",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_007022.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-15T23:11:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3107",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3107#event-7022"
}
```



---

archive/issue_events_007023.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-16T00:07:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3107",
    "milestone": "sage-3.0.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3107#event-7023"
}
```
