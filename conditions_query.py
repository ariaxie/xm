def query_schedule(name=None, shift=None, department=None, group=None, day=None, keyword=None):
    schedule_result = []
    user_info = get_users_data()
    for line_result_list in user_info:
        name_actual_result, shift_actual_result, department_actual_result, group_actual_result, is_leader = line_result_list
        schedule_shift_dict = schedule_shift()
        day_shift = get_day_of_shift(schedule_shift_dict, day)
        if keyword == 'leader' and is_leader == 1:
            data = dict(name=name_actual_result, shift=shift_actual_result, department=department_actual_result,
                        group=group_actual_result, day=schedule_shift_dict[shift_actual_result])
            schedule_result.append(data)

        if keyword == 'all_work' and get_all_work_data(line_result_list[0]):
            data = dict(name=name_actual_result, shift=shift_actual_result, department=department_actual_result,
                        group=group_actual_result, day=schedule_shift_dict[shift_actual_result])
            schedule_result.append(data)

        if (name or shift or department or group) in line_result_list:
            data = dict(name=name_actual_result, shift=shift_actual_result, department=department_actual_result,
                        group=group_actual_result, day=schedule_shift_dict[shift_actual_result])
            schedule_result.append(data)
        if day_shift in line_result_list:
            data = dict(name - name_actual_result, shift=shift_actual_result, department=department_actual_result,
                        group=group_actual_result, day=schedule_shift_dict[day_shift])
            schedule_result.append(data)
    return schedule_result


def get_all_work_data(name):
    with open('schedule.csv', 'r') as csv_file:
        for u in csv_file:
            if len(set(u.strip().split(','))) == 1 and name in set(u.strip().split(',')):
                return name


def get_users_data():
    schedule_list = []
    with open('users.csv', 'r') as csv_file:
        for line in csv_file.readlines():
            line_result_list = line.split(',')[0:5]
            try:
                line_result_list[-1] = int(line_result_list[-1].strip())
            except ValueError:
                pass
            schedule_list.append(line_result_list)
        return schedule_list


def get_day_of_shift(schedule_shift_dict, day):
    for shift, days in schedule_shift_dict.items():
        if bool(day) and day in days:
            return shift
    return None


def schedule_shift():
    schedule_shift = {'A': '周一、周三、周五', 'B': '周二、周四'}
    return schedule_shift


if __name__ == '__main__':
    res = query_schedule(name='王霞', keyword='all_work')
    print(res)
