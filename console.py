#!/usr/bin/python3
'''Console - entry point of command intepreter class defination'''
import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

