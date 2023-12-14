#!/usr/bin/python3
'''Console - entry point of command intepreter class defination'''
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State


class HBNBCommand(cmd.Cmd):
    '''command intepreter for hbnb project'''
    prompt = '(hbnb)'

    def do_quit(self, arg):
        '''Exit program'''
        return True

    def do_EOF(self, arg):
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
        argl = shlex.split(arg)
        if len(argl) == 0:
            print("** class name missing **")
            return
        class_name = argl[0]
        class_mapping = {
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review}

        if class_name not in class_mapping:
            print("** class doesn't exist **")
        else:
            new_instance = class_mapping[class_name]()
            storage.new(new_instance)
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id.
        Usage: show <class name> <id>
        """
        if arg.count('"') % 2 != 0:
            print("Error: Unbalanced quotes")
            return

        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            class_mapping = {
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Place': Place,
                    'Review': Review}
            if class_name not in class_mapping:
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
        class_name = args[0]
        class_mapping = {
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review}
        if class_name not in class_mapping:
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
            class_mapping = {
                    'State': State,
                    'City': City,
                    'Amenity': Amenity,
                    'Place': Place,
                    'Review': Review}
            if class_name not in class_mapping:
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
        class_mapping = {
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review}
        if class_name not in class_mapping:
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

    def do_show_id(self, arg):
        """retrieves an instance based on its id
        usage: <class name>. show(<id>)"""
        args = shlex.split(arg)
        if len(args) < 2 or args[1] != '.show(' or not args[2].endswith(')'):
            print("** Invalid syntax. Usage: <class name>.show(<id>) **")
            return
        class_name = args[0]
        obj_id = args[2][:-1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()

        if key in all_objs:
            print(all_objs[key])
        else:
            print("** No instance found with ID:{}".format(obj_id))


    def do_all_class(self, arg):
        """retrieves all instances of a class:
            usage: <class name.all()>
        """
        args = shlex.split(arg)
        class_name = args[0]
        all_objs = storage.all()
        class_instances = [str(obj) for key, obj in all_objs.items() if key.startswith(class_name + '.')]

        if class_instances:
            print(class_instances)
        else:
            print("** No instances found for class:{}".format(class_name))


    def do_count_class(self, arg):  
        """Retrieves the number of instances of a class
            usage: <class name>.count()
        """
        class_name = arg.split('.')[0]
        all_objs = storage.all()

        count = sum(1 for key in all_objs.keys() if key.startswith(class_name + '.'))
        print(count)


    def do_show_id(self, arg):
        """
            Retrieves an instance based on its ID: <class name>.show(<id>).
            Usage: <class name>.show(<id>)
        """
        args = shlex.split(arg)

        if len(args) != 3 or args[1] != 'show(' or not args[2].endswith(')'):
            print("** Invalid syntax. Usage: <class name>.show(<id>)")
            return

        class_name = args[0]
        obj_id = args[2][:-1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()

        if key in all_objs:
            print(all_objs[key])
        else:
            print("** No instance found with ID: {}".format(obj_id))

    def do_destroy_id(self, arg):
        """
            Destroys an instance based on its ID: <class name>.destroy(<id>).
            Usage: <class name>.destroy(<id>)
        """
        args = shlex.split(arg)

        if len(args) != 3 or args[1] != 'destroy(' or not args[2].endswith(')'):
            print("** Invalid syntax. Usage: <class name>.destroy(<id>)")
            return

        class_name = args[0]
        obj_id = args[2][:-1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()

        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** No instance found with ID: {}".format(obj_id))


    def update_by_id(self, arg):
        """
            Updates an instance based on its ID: <class name>.update(<id>, <attribute name>, <attribute value>).
         Usage: <class name>.update(<id>, <attribute name>, <attribute value>)
        """
        args = shlex.split(arg)

        if len(args) < 4 or args[1] != 'update(' or not args[-1].endswith(')'):
            print("** Invalid syntax. Usage: <class name>.update(<id>, <attribute name>, <attribute value>)")
            return
        class_name = args[0]
        obj_id = args[2]
        attribute_name = args[3]
        attribute_value = args[4][:-1]  
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()

        if key not in all_objs:
            print("** No instance found with ID: {}".format(obj_id))
            return
        obj = all_objs[key]
        setattr(obj, attribute_name, attribute_value)
        storage.save()

    def do_update_dict(self, arg):
        """
            Updates an instance based on its ID with a dictionary: <class name>.update(<id>, <dictionary representation>).
            Usage: <class name>.update(<id>, <dictionary representation>)
        """
        args = shlex.split(arg)

        if len(args) < 4 or args[1] != 'update(' or not args[-1].endswith(')'):
            print("** Invalid syntax. Usage: <class name>.update(<id>, <dictionary representation>)")
            return

        class_name = args[0]
        obj_id = args[2]
        dictionary_str = args[3][1:-1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()

        if key not in all_objs:
            print("** No instance found with ID: {}".format(obj_id))
            return

        obj = all_objs[key]
        try:
            update_dict = eval(dictionary_str)
        except Exception as e:
            print("** Invalid dictionary representation: {}".format(e))
            return
        for attr, value in update_dict.items():
            setattr(obj, attr, value)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
