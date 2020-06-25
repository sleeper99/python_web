import json

result = json.loads('[{"GroupID":"20742325","GroupName":"udev/Udev","ParentID":null},{"GroupID":"20742328",'
                    '"GroupName":"udev/Udev","ParentID":null},{"GroupID":"20742330","GroupName":"uganda/Uganda",'
                    '"ParentID":null},{"GroupID":"20742333","GroupName":"uganda/Uganda","ParentID":null},'
                    '{"GroupID":"20743787","GroupName":"america/usa","ParentID":null},{"GroupID":"20743789",'
                    '"GroupName":"america/usa","ParentID":null},{"GroupID":"20748771","GroupName":"america/usa",'
                    '"ParentID":null},{"GroupID":"20748773","GroupName":"america/usa","ParentID":null},'
                    '{"GroupID":"20760275","GroupName":"america/usa","ParentID":"20742330"},{"GroupID":"20760277",'
                    '"GroupName":"america/usa","ParentID":"20742330"},{"GroupID":"20760939","GroupName":"america/usa",'
                    '"ParentID":"20760275"},{"GroupID":"20760941","GroupName":"america/usa",'
                    '"ParentID":"20760275"},{"GroupID":"20762860","GroupName":"america/usa",'
                    '"ParentID":"20760941"},{"GroupID":"20762862","GroupName":"america/usa",'
                    '"ParentID":"20760941"}]')

# get all top level
units = []
for i in range(len(result) - 1, -1, -1):
    if result[i]["ParentID"] is None:
        units.append({
            "GroupID": result[i]["GroupID"],
            "GroupName": result[i]["GroupName"],
            "ParentID": result[i]["ParentID"],
            "Children": None
        })
        del result[i]

# get children
sub_group = units
while result:
    children_group = []
    for group_index in range(len(sub_group)):
        if len(result) == 0:
            break
        for i in range(len(result) - 1, -1, -1):
            if result[i]["ParentID"] == sub_group[group_index]["GroupID"]:
                if sub_group[group_index]["Children"] is None:
                    sub_group[group_index]["Children"] = []
                children = {
                    "GroupID": result[i]["GroupID"],
                    "GroupName": result[i]["GroupName"],
                    "ParentID": result[i]["ParentID"],
                    "Children": None
                }
                sub_group[group_index]["Children"].append(children)
                children_group.append(children)
                del result[i]
    sub_group = children_group
