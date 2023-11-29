#!/usr/bin/python3
'''Console - entry point of command intepreter class defination'''
import cmd
import shlex
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    '''command intepreter for hbnb project'''
    prompt = '(hbnb)'

    def do_quit(self, arg):
        '''Exit program'''
        return True

    def do_EOF(self,arg):
        '''Exit the program with Ctrl+d'''
        print()
        return True

    def emptyline(self):
        '''Do nothing on empty file'''
        pass
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id.
        Usage: create <class name>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("**class name missing**")
        else:
            cls_name = args[0]
        if cls_name not in storage.all():
            print("**class doesnt exist**")
            return
        new_instance = eval(f"{cls_name}")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.
        Usage: show <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.all():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                all_objs = storage.all()
                if key not in all_objs:
                    print("** no instance found **")
                else:
                    print(all_objs[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.all():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                all_objs = storage.all()
                if key not in all_objs:
                    print("** no instance found **")
                else:
                    del all_objs[key]
                    storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        Usage: all [class name]
        """
        args = shlex.split(arg)
        all_objs = storage.all()

        if len(args) == 0:
            print([str(obj) for obj in all_objs.values()])
        else:
            class_name = args[0]
            if class_name not in storage.all():
                print("** class doesn't exist **")
            else:
                print([str(obj) for key, obj in all_objs.items()
                       if key.startswith(class_name + '.')])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating an attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.all():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                key = "{}.{}".format(class_name, obj_id)
                all_objs = storage.all()
                if key not in all_objs:
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attribute_name = args[2]
                    attribute_value = args[3]
                    obj = all_objs[key]
                    setattr(obj, attribute_name, attribute_value)
                    obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

