import click
import yaml
import os

todo_path = os.path.expanduser("~") + "/.toopy.yaml"
try:
    with open(todo_path) as file:
        todo_list = yaml.load(file, Loader=yaml.FullLoader)
except:
    todo_file = open(todo_path, "w+")
    todo_file.write("[]")
    todo_list = [] 

def append_yaml(list, yaml_path, item):
    list.append(item)
    with open (yaml_path, "w") as file:
        yaml.dump(list, file)
        return item

def remove_yaml(list, yaml_path, item_number):
    deleted_item = str(list[int(item_number) - 1])
    del list[int(item_number) - 1]
    with open (yaml_path, "w") as file:
        yaml.dump(list, file)
        return deleted_item

@click.command()
@click.option("-a", default="",  help="Add a task.")
@click.option("-r", default="",  help="Remove a task.")
@click.option("--onlyprint", is_flag=True, help="Doesn't print anything if there aren't any tasks.")
def cli(a, r, onlyprint):
    if a:
        click.echo("+ " + append_yaml(todo_list, todo_path, a))
        return
    if r:
        try:
            click.echo("- " + remove_yaml(todo_list, todo_path, r))
        except IndexError:
            click.echo("Error: task doesn't exist")
        return
    if onlyprint != True or len(todo_list) != 0:
        click.echo("You have " + str(len(todo_list)) + " task(s):")
        task_number = 1
        for task in todo_list:
            print(str(task_number) + " > " + task)
            task_number += 1
