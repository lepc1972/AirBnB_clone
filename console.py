#!/usr/bin/python3
"""
Module Console
"""
import cmd
from models.engine.file_storage import FileStorage
import shlex
import sys
import json
from models.base_model import BaseModel
from models import storage


class HBNBcommand(cmd.Cmd):
      """ HBNB CLASS """
      prompt = '(hbnb)'
      def do_EOF(self, args):
            """ End Of Line"""
            print()
            return True
      def do_quit(self, args):
            """ Close cmd """
            return True
      def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass

      def do_create(self, args):
            '''
            Create a new instance of class BaseModel and saves it
            to the JSON file.
            '''
            if len(args) == 0:
                  print("** class name missing **")
                  return
            try:
                  args = shlex.split(args)
                  new_instance = eval(args[0])()
                  new_instance.save()
                  print(new_instance.id)

            except:
                  print("** class doesn't exist **")

      def do_show(self, args):
            '''
            Print the string representation of an instance baed on
            the class name and id given as args.
            '''
            args = shlex.split(args)
            if len(args) == 0:
                  print("** class name missing **")
                  return
            if len(args) == 1:
                  print("** instance id missing **")
                  return
            storage = FileStorage()
            storage.reload()
            obj_dict = storage.all()
            try:
                  eval(args[0])
            except NameError:
                  print("** class doesn't exist **")
                  return
            key = args[0] + "." + args[1]
            key = args[0] + "." + args[1]
            try:
                  value = obj_dict[key]
                  print(value)
            except KeyError:
                  print("** no instance found **")


      def do_all(self, args):
            """Prints all string representation of all instances.
            """
            if args:
                  words = line.split(' ')
                  if words[0] not in storage.classes():
                        print("** class doesn't exist **")
                  else:
                        l = [str(obj) for key, obj in storage.all().items()
                       if type(obj).__name__ == words[0]]
                  print(l)
            else:
                  l = [str(obj) for key, obj in storage.all().items()]
            print(l)

      def do_update(self, args):
        '''
            Update an instance based on the class name and id
            sent as args.
        '''
        storage = FileStorage()
        storage.reload()
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        obj_dict = storage.all()
        try:
            obj_value = obj_dict[key]
        except KeyError:
            print("** no instance found **")
            return
        try:
            attr_type = type(getattr(obj_value, args[2]))
            args[3] = attr_type(args[3])
        except AttributeError:
            pass
        setattr(obj_value, args[2], args[3])
        obj_value.save()

if __name__ == "__main__":
      """Infinte loop"""
      HBNBcommand().cmdloop()
 
