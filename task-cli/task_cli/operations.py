from datetime import datetime
import json
def add(args):
    data = fetch_data()
    idSeries = data.keys()
    idSeries = [int(id) for id in idSeries]
    if len(idSeries) != 0:
        current_max_id = max(idSeries)
        id = current_max_id + 1
    else:
        id = 0
    if args.change_status != None: 
        status = args.change_status
    else:
        status = 'todo'
    data[id] = {'description' : args.task, 'status' : status, 'createdAt' : str(datetime.now()), 'updatedAt' : str(datetime.now())}
    modify_data(data)

def update(args):
    data = fetch_data()
    data[str(args.id)]['description'] = args.task
    modify_data(data)

def delete(args):
    data = fetch_data()
    del data[str(args.id)]
    modify_data(data)

def list(args):
    data = fetch_data()
    if args.bystatus == 'all':
        print(data)
    else:
        filteredData = {id:todoData for id,todoData in data.items() if todoData['status'] == args.bystatus}
        print(filteredData)

def mark_in_progress(args):
    data = fetch_data()
    data[args.id]['status'] = 'in-progress'
    modify_data(data)

def mark_done(args):
    data = fetch_data()
    data[args.id]['status'] = 'done'
    modify_data(data)

def modify_data(data):
    with open('data.json', 'w') as f:
        json.dump(data,f,indent=4)

def fetch_data():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data
