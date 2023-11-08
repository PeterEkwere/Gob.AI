#!/usr/bin/python3
"""
    This is the Console Script that would manage all CRUD Operations
    Author: Peter Ekwere
"""
import cmd
import sys
from models.base_model import BaseModel
from models.ingredients import Ingredient
from models.recipe import Recipe
from models.user import User
from models.__init__ import storage
from models.engine.file_storage import FileStorage
sys.path.append("..")

class Gob_console(cmd.Cmd):
    """ Gob_console is a command-line console for managing The Gob web app

    Args:
        cmd (cmd.Cmd): A subclass of the cmd class for creating a command-line interface.
    """
    prompt = "Gob-> "
    
    class_names  = {
        BaseModel: 'BaseModel',
        Recipe: 'Recipe',
        User: 'User',
        Ingredient: 'Ingredient'
    }

    def do_EOF(self, *args):
        """ This Method handles the EOF command
        """
        return True
    
    def do_quit(self, *args):
        """ This Method Handles the quit Command
        """
        return True
    
    def do_emptyline(self, *args):
        """ This Method implements the emptyline
        """
        return False
    
    def do_help(self, *args):
        """ This function Handles the help command
        """
        cmd.Cmd.do_help(self, *args)
    
    def do_create(self, model):
        """ This Method will create a new Model
        """
        if model is None or len(model) < 1:
            print("<- class doesnt exist ->")
            return False
        elif model not in self.class_names.values():
            print("<- class does't exist ->")
            return False
        else:
            for key, value in self.class_names.items():
                if model == value:
                    new_instance = key()
                    new_instance.save()
                    print(f"{new_instance.id}")
                    
    def do_show(self, model):
        """ This Method prints a model based on its ID
        """
        arguments = model.split()
        if len(arguments) == 0:
            print("<- class name missing ->")
            return False
        elif len(arguments) == 1:
            print("<- instance id mising ->")
            return False
        elif arguments[0] not in self.class_names.values():
            print("<- class doesn't Exist ->")
            return False
        else:
            for key, value in self.class_names.items():
                if arguments[0] == value:
                    class_dict = storage.all()
                    instance = f"{arguments[0]}.{arguments[1]}"
                    if instance in class_dict:
                        instance_dict = class_dict[instance]
                        print(f"{instance_dict}")
                        storage.save()
                    else:
                        print("<- no instance found ->")
                        return False
                    
    def do_destroy(self, model):
        """ This Method prints a model based on its ID
        """
        arguments = model.split()
        if len(arguments) == 0:
            print("<- class name missing ->")
            return False
        elif len(arguments) == 1:
            print("<- instance id mising ->")
            return False
        elif arguments[0] not in self.class_names.values():
            print("<- class doesn't Exist ->")
            return False
        else:
            for key, value in self.class_names.items():
                if arguments[0] == value:
                    class_dict = storage.all()
                    instance = f"{arguments[0]}.{arguments[1]}"
                    if instance in class_dict:
                        del class_dict[instance]
                        storage.save()
                    else:
                        print("<- no instance found ->")
                        return False
                    
    def do_all(self, args):
        """ This method prints all the models of a class when an argument is passed OR
            prints all models when no argument is passed 
        """
        arguments = args.split()
        
        if len(arguments) > 1:
            return False
        elif len(arguments) == 1:
            Class = arguments[0]
            class_dict = storage.all()
            model_list = []
            
            if Class not in self.class_names.values():
                print("<-- Class doesn't Exist -->")
                return False
            
            for key, value in class_dict.items():
                class_name = value.__class__.__name__
                if class_name == Class:
                    model = str(class_dict[key])
                    print(model)
                    model_list.append(model)
            print(model_list)
        else:
            model_list = []
            class_dict = storage.all()
            
            for an_object in class_dict:
                model = str(class_dict[an_object])
                model_list.append(model)
            print(model_list)
            
    def do_count(self, args):
        """ This method counts the amount of models in the file storage
        """
        class_dict = storage.all()
        arguments = args.split()
        
        if len(arguments) < 0:
            print("<- class name missing ->")
            return False
        elif len(arguments) > 0:
            count = 0
            Class = arguments[0]
            
            if Class not in self.class_names.values():
                print("<- class doesn't exist ->")
                return False
            else:
                for key, value in class_dict.items():
                    class_name = value.__class__.__name__
                    if Class == class_name:
                        count += 1
                print(count)
                
    def do_update(self, args):
        """ Updates a certain object with new info """
        c_name = c_id = att_name = att_val = kwargs = ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class name not present
            print("** class name missing **")
            return
        if c_name not in Gob_console.classes:  # class name invalid
            print("** class doesn't exist **")
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = c_name + "." + c_id

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # isolate args
            args = args[2]
            if args and args[0] == '\"':  # check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # if att_name was not quoted arg
            if not att_name and args[0] != ' ':
                att_name = args[0]
            # check for quoted val arg
            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # if att_val was not quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # iterate through attr names and values
        for i, att_name in enumerate(args):
            # block only runs on even iterations
            if (i % 2 == 0):
                att_val = args[i + 1]  # following item is value
                if not att_name:  # check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # check for att_value
                    print("** value missing **")
                    return
                # type cast as necessary
                if att_name in Gob_console.types:
                    att_val = Gob_console.types[att_name](att_val)

                # update dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # save updates to file
        
    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")
   
        
            
    
    
if __name__ == "__main__":
    Gob_console().cmdloop()