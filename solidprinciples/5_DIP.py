# Dependency Inversion Principle
# This principle suggests that below two points.
# High-level modules should not depend on low-level modules. Both should depend on abstractions.
# Abstractions should not depend on details. Details should depend on abstractions. 

########## Violation ########
class BackendDevelopers:
    """This is a low-level module"""
    @staticmethod
    def python():
        print("Writing Python code")

class FrontendDevelopers:
    """This is a low-level module"""
    @staticmethod
    def javascript():
        print("Writing JavaScript code")

class Projects:
    """This is a high-level module"""
    def __init__(self):
        self.backend = BackendDevelopers()
        self.frontend = FrontendDevelopers()
    def develop(self):
        self.backend.python()
        self.frontend.javascript()
        return "Develop codebase"


class FrontendDeveloper:

    def developer(self):
        return f"Javascript: {self.javascript()} React JS: {self.reactjs()}"

    @staticmethod
    def javascript():
        return "Must be an expert in Javascript."

    @staticmethod
    def reactjs():
        return "Must be an expert in React JS." 

class BackendDeveloper:

    def developer(self):
        return f"Python: {self.python()} PHP: {self.php()}"

    @staticmethod
    def python():
        return "Must be an expert in Python."

    @staticmethod
    def php():
        return "Must be an expert in PHP."

class Developers:

    def __init__(self):
        self.frontend = FrontendDeveloper()
        self.backend = BackendDeveloper()

    def developer(self):
        return f"{self.frontend.developer()} {self.backend.developer()}"

class Project:

    def __init__(self):
        self.developers = Developers()

    def developer(self):
        return self.developers.developer()

project = Project()
print(project.developer())                                

