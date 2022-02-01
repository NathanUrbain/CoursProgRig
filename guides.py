
# Maya imports
from maya import cmds



def create_guides(number, name, guidetype):
    """Create guides
    """
    
    guides = []
    guide_parent = cmds.createNode("transform", name="{}_grp".format(name))
    cmds.addAttr(guide_parent, longName="nguides", attributeType="message", multi=True)
    guide_idx = 0
    
    for i in range(1, number+1):
        idx = i
        id = "0{0}".format(idx)
        if idx > 9:
            id = "{0}".format(idx)
        _name="{0}{1}Shape".format(name, id)
        
        while cmds.objExists(_name):
            idx += 1
            id = "0{0}".format(idx)
            if idx > 9:
                id = "{0}".format(idx)
            _name="{0}{1}Shape".format(name, id)

        _guide = cmds.createNode(
            "locator", name=_name)
        _guide = cmds.listRelatives(_guide, parent=True, path=True)[0]
        cmds.addAttr(_guide, longName="nguide", dataType="string")
        cmds.setAttr("{0}.nguide".format(_guide), guidetype, type="string")
        cmds.connectAttr(
            "{0}.message".format(_guide),
            "{0}.nguides[{1}]".format(guide_parent, guide_idx))
        guide_idx += 1

        guides.extend([_guide])
        
    cmds.parent(guides, guide_parent)
    return guides
