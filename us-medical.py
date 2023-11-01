import csv

age_list = []
children = []
insurance_dict_all = {}

with open('insurance.csv') as insurance_file:

    insurance_dict = csv.DictReader(insurance_file, delimiter=',')
    count = 0
    for item in insurance_dict:

        count += 1
        age_list.append(int(item['age']))
        children.append((item['children']))
        insurance_dict_all.update({str(count): {
            'age': item['age'],
            'gender': item['sex'],
            'bmi': item['bmi'],
            'children': item['children'],
            'smoker': item['smoker'],
            'region': item['region'],
            'charges': float(item['charges'])


        }})


def avg_of_patient(list):
    return round(sum(list)/len(list))


male_cost_avg = []
female_cost_avg = []


def cost_avg_gender(dict):
    count = 0
    for key, values in dict.items():
        for k, v in values.items():
            count += 1
            if v == 'male':
                male_cost_avg.append(dict[key]['charges'])
            elif v == 'female':
                female_cost_avg.append(dict[key]['charges'])
    male_avg = float(sum(male_cost_avg)/len(male_cost_avg))
    female_avg = float(sum(female_cost_avg)/len(female_cost_avg))
    print(f'avg fro males in insurance is {male_avg}')
    print(f'avg fro females in insurance is {female_avg}')

    return male_cost_avg, female_cost_avg


cost_avg_gender(insurance_dict_all)


dict_for_all_by_region = {
    "southwest": [],
    'southeast': [],
    'northwest': [],
    'northeast': []}


def classfiy_dict_by_regen(dict):
    for key, value in dict.items():
        for k, v in value.items():
            if k == 'region':
                if v == 'southwest':
                    dict_for_all_by_region['southwest'].append({key: value})
                elif v == 'southeast':
                    dict_for_all_by_region['southeast'].append({key: value})
                elif v == 'northwest':
                    dict_for_all_by_region['northwest'].append({key: value})
                elif v == 'northeast':
                    dict_for_all_by_region['northeast'].append({key: value})
    return dict_for_all_by_region


print(classfiy_dict_by_regen(insurance_dict_all))



