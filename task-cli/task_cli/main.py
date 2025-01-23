import task_cli.operations as operations 
import argparse

def main():
    parser = argparse.ArgumentParser(description='CRUD operations on the tasks')
    subparsers = parser.add_subparsers(dest='command', help='Sub-command help')

    # Add subparser for 'add' command
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('task', type=str, help='The task to add')
    parser_add.add_argument('--change_status',choices=['in-progress','done','todo'])

    # Add subparser for 'update' command
    parser_update = subparsers.add_parser('update', help='Update a task by id')
    parser_update.add_argument('id', type=int, help='The id of the task to update')
    parser_update.add_argument('task', type=str, help='The updated task')

    # Add subparser for 'delete' command
    parser_delete = subparsers.add_parser('delete', help='Delete a task by id')
    parser_delete.add_argument('id', type=int, help='The id of the task to delete')

    # Add subparser for 'list' command
    parser_list = subparsers.add_parser('list', help='List the tasks and the details')
    parser_list.add_argument('bystatus', choices=['all','todo', 'done', 'in-progress'], help='Filter tasks by status')

    #Add subparser for 'mark-in-progress' command
    parser_mark_in_progress = subparsers.add_parser('mark-in-progress', help="Mark the status as in progress for the id given")
    parser_mark_in_progress.add_argument('id',help='The id of the task to update')

    #Add subparser for 'mark-done' command
    parser_mark_done = subparsers.add_parser('mark-done', help="Mark the status as done for the id given")
    parser_mark_done.add_argument('id',help='The id of the task to update')

    args = parser.parse_args()

    if args.command:
        function = getattr(operations,args.command)
        function(args)
        print(operations.fetch_data())
        
if __name__ == "__main__":
    main()