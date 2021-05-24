import maya.cmds as cmds

# Change the current time  in current time units
#
for x in range(500):
    cmds.currentTime( x , update=True)
    path = "F:/two_b/"+ "two_b_" + str(x) + ".obj"
    cmds.file(path, pr=1, ea=1, force=1, options="groups=1;ptgroups=1;materials=1;smoothing=1;normals=1",type="OBJexport")
