#!/usr/bin/python3
'''Console - entry point of command intepreter class defination'''
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User

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
    """Usage: create <class>
    Create a new class instance and print its id.
    """
    argl = parse(arg)
    if len(argl) == 0:
        print("** class name missing **")
        return
    class_name = argl[0]
    if class_name not in storage.all():
        print("** class doesn't exist **")
    else:
        new_instance = storage.all()[class_name]()
        storage.new(new_instance)
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
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
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            all_objs = storage.all()
            if key not in all_objs:
                print("** no instance found **")
                return
            print(all_objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = arg[0]
        if class_name not in storage.all():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print(" instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
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
        """Updates an instance based on the class name and id
        by adding or updating an attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.all():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]
        obj = all_objs[key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

