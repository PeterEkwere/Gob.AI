#!/usr/bin/python3
"""
    This is the Console Script that would manage all CRUD Operations
    Author: Peter Ekwere
"""
import cmd
import sys
from models.base_model import BaseModel
from models.comment import Comment
from models.ingredients import Ingredient
from models.recipe import Recipe
from models.user import User
from models.__init__ import storage
from models.__init__ import FileStorage
sys.path.append("..")

class Gob_console(cmd.Cmd):
    """ Gob_console is a command-line console for managing The Gob web app

    Args:
        cmd (cmd.Cmd): A subclass of the cmd class for creating a command-line interface.
    """
    prompt = "Gob-> "
    
    class_names  = {
        BaseModel: 'BaseModel',
        Comment: 'Comment',
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
                
   #def do_update()   
        
            
    
    
if __name__ == "__main__":
    Gob_console().cmdloop()