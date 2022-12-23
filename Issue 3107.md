# Issue 3107: Triangulation doesn't automatically happen for x3d output of 3d objects

Issue created by migration from https://trac.sagemath.org/ticket/3107

Original creator: robertwb

Original creation time: 2008-05-06 00:47:16

Assignee: was


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


---

Attachment


---

Comment by craigcitro created at 2008-06-15 21:41:07

Changing keywords from "" to "editor_gfurnish".


---

Comment by mabshoff created at 2008-06-15 23:11:40

Merged in Sage 3.0.3.rc0


---

Comment by mabshoff created at 2008-06-15 23:11:40

Resolution: fixed
