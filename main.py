# -*- coding: UTF-8 -*-

import sys
import maya.cmds as cmds
import maya.api.OpenMaya as OpenMaya
import maya.mel as mel
import maya.api.OpenMayaUI as OpenMayaUI

reload(sys)
sys.setdefaultencoding('utf-8')
# Fix Chinese
def utf_8String(StringT):
    utf_8String = StringT
    utf_8String.encode('utf-8')
    utf_8String = unicode(utf_8String, "utf-8")
    return utf_8String

def bakePivots():
    selection = cmds.ls(sl=1)
    for s_object in selection:
        pivot = cmds.xform( s_object, query=True, pivots=True, worldSpace=True)

        colorset_name = s_object + ': colorSet0'
        target_colorset = cmds.polyColorSet(query=True, currentColorSet=True)
        if target_colorset is None:
            cmds.polyColorSet(create=True, clamped=False, rpt='RGBA', colorSet=colorset_name)
        cmds.polyColorPerVertex(s_object, clamped=False, colorB=pivot[2], colorG=pivot[1], colorR=pivot[0], representation=4)

def bakePhaseID():
    selection = cmds.ls(sl=1)
    for s_object in selection:
        cmds.select(clear=True)
        cmds.polySeparate(s_object)
        separated_meshes = cmds.ls(sl=1)
        index = 0

        # create phase ID for each leaf
        for m in separated_meshes:
            color_v = index
            index = index % 256
            index_alpha = index / 255.0
            index += 1

            cmds.select(clear=True)
            cmds.select(m)

            colorset_name = s_object + ': colorSet0'
            target_colorset = cmds.polyColorSet(query=True, currentColorSet=True)
            if target_colorset is None:
                cmds.polyColorSet(create=True, clamped=False, rpt='RGBA', colorSet=colorset_name)

            cmds.polyColorPerVertex(m, alpha=index_alpha, clamped=False, representation=4)

        # unit again
        united_poly = cmds.polyUnite(separated_meshes)
        s_object = cmds.rename(united_poly[0], s_object)

        # delete transform histories
        history = cmds.listHistory(s_object) or []
        print s_object + ': history', history
        deform_history = cmds.ls(history, type="geometryFilter", long=True)
        print s_object + ': deformHistory', deform_history
        cmds.bakePartialHistory(s_object, prePostDeformers=True)

def mainGui():
    window_name = 'Export_Wind_Parameters_Tool1.0'
    window_title = 'Export_Wind_Parameters_Tool1.0'

    # Prevent duplicate windows
    try:
      cmds.deleteUI(window_name)
    except:
      pass

    window = cmds.window(window_name, title = window_title)
    form = cmds.formLayout()
    # editor = cmds.spNarrowPolyViewer()
    column = cmds.columnLayout(adjustableColumn=True)

    cmds.button(label="Bake Pivot", ann = "Bake pivot to vertex color xyz", command='bakePivots()')
    cmds.button(label="Bake Phase ID", ann = "Bake Phase ID to vertex color w", command='bakePhaseID()')

    cmds.showWindow(window)

mainGui()