def change_param_value(chimes_mode_status):
    if chimes_mode_status in ['CHIMES_STATUS_ENABLE', 2]:
        return 1
    if chimes_mode_status in ['CHIMES_STATUS_DISABLE', 1]:
        return 2
    return 0


def parse_inner_group_statuses_dict(inner_statuses_dict):
    lst_of_groups = []
    temp_group_statuses = {}
    for grp_st_key, grp_st_val in inner_statuses_dict.items():
        if grp_st_key == 'groups_statuses':
            for inner_grp_dict in grp_st_val:
                for key, value in inner_grp_dict.items():
                    if key == 'group_chimes_status':
                        temp_group_statuses[key] = change_param_value(value)
                    else:
                        temp_group_statuses[key] = value
                lst_of_groups.append(temp_group_statuses.copy())
        else:
            temp_group_statuses[grp_st_key] = grp_st_val
    return lst_of_groups

def get_teardown_params_1(param):
    teardown_param = {}
    for param_name, param_value in param.items():
        if param_name == 'chimes_status':
            teardown_param[param_name] = change_param_value(param_value)
        elif param_name == 'groups_statuses':
            lst_of_groups = []
            temp_group_statuses = {}

            teardown_param[param_name] = {'groups_statuses': parse_inner_group_statuses_dict(param_value)}

        else:
            teardown_param[param_name] = param_value
    return teardown_param


def get_teardown_params(data):
    def update_status(status):
        if status == 1:
            return 2
        elif status == 2:
            return 1
        return 0

    # Update chimes_status
    chimes_status = data.get("chimes_status")
    if chimes_status is not None:
        data["chimes_status"] = update_status(chimes_status)
    else:
        data["chimes_status"] = 0

    # Update group_chimes_status
    groups_statuses = data.get("groups_statuses", {}).get("groups_statuses", [])
    for group_status in groups_statuses:
        if isinstance(group_status, dict):
            group_chimes_status = group_status.get("group_chimes_status")
            if group_chimes_status is not None:
                group_status["group_chimes_status"] = update_status(group_chimes_status)
            else:
                group_status["group_chimes_status"] = 0
        else:
            group_status["group_chimes_status"] = 0

    return data

teardown_param = get_teardown_params({'chimes_status': 1, 'groups_statuses': {'groups_statuses': [{'group_chimes_status': 1, 'group_id': '00000002'}, {'group_chimes_status': 1, 'group_id': '00000003'}]}, 'hub_id': '76496A8E'})

teardown_param_1 = get_teardown_params({"chimes_status" : 1, "groups_statuses" : {"groups_statuses": [{"group_id" : "00000002", "group_chimes_status": 1}, {"group_id" : "00000003", "group_chimes_status": 1}] }, "hub_id": "dark_magenta.hex_id.as_str" })

teardown_param_2 = get_teardown_params({"chimes_status" : 1, "groups_statuses" : {"groups_statuses": [{"group_id" : "00000002", "group_chimes_status": 1}] }, "hub_id": "dark_magenta.hex_id.as_str" })

print(teardown_param)
print(teardown_param_1)
print(teardown_param_2)

params = {"hub_id": "AAAAAAAA"}

print("Return chimes mode to start status on HUB: {}".format(params["hub_id"]))