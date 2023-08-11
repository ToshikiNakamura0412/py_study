import yaml

def load_data_from_yaml(path):
    with open(path) as file:
        data = yaml.safe_load(file)
    return data

if __name__ == '__main__':
    data = load_data_from_yaml('test.yaml')
    print('data:')
    print(data)
    print()

    for count, task in enumerate(data['task']):
        # print(task)
        if task['task_type'] == 'detect_line':
            print(task['task_type'])
            print('\tnode0_id: ', task['edge']['node0_id'])
            print('\tnode1_id: ', task['edge']['node1_id'])
            print()

        if task['task_type'] == 'announce':
            print(task['task_type'])
            print('\tnode0_id: ', task['edge']['node0_id'])
            print('\tnode1_id: ', task['edge']['node1_id'])
            print()
