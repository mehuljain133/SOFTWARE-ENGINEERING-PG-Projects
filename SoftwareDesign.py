# Unit-V Software design: Design for reuse, design for change, design notations, design evaluation and validation.

# Unit-V Software Design: Overview and Code Representation

# 1. Design for Reuse
# - Design for reuse focuses on creating software components that can be reused in different projects to increase efficiency.
# We will simulate the design of reusable components that can be incorporated into multiple software systems.

class ReusableComponent:
    def __init__(self, component_name, functionality):
        self.component_name = component_name
        self.functionality = functionality
    
    def reuse_component(self):
        print(f"\nReusing component: {self.component_name}")
        print(f"Functionality: {self.functionality}")
    
    def __str__(self):
        return f"Component Name: {self.component_name}, Functionality: {self.functionality}"

# Simulate Reusable Component Design
component = ReusableComponent("Authentication Module", "Handles user login, registration, and password recovery.")
component.reuse_component()

# 2. Design for Change
# - Design for change emphasizes making the system flexible enough to accommodate changes over time.
# We will simulate a simple system where design changes can be made without major disruptions.

class ChangeableSystem:
    def __init__(self, system_name):
        self.system_name = system_name
        self.modules = []
    
    def add_module(self, module):
        self.modules.append(module)
    
    def update_module(self, module_index, new_module):
        if 0 <= module_index < len(self.modules):
            self.modules[module_index] = new_module
            print(f"Module at index {module_index} updated.")
        else:
            print("Module index out of range.")
    
    def display_system(self):
        print(f"\nSystem: {self.system_name}")
        for module in self.modules:
            print(f"Module: {module}")

# Simulate Design for Change
system = ChangeableSystem("E-Commerce System")
system.add_module("User Authentication")
system.add_module("Product Catalog")
system.add_module("Shopping Cart")

# Display initial system design
system.display_system()

# Update a module to reflect design changes
system.update_module(1, "Product Catalog with Recommendations")
system.display_system()

# 3. Design Notations
# - Design notations represent the structure and behavior of software using visual elements like diagrams, pseudo-code, and models.
# We will simulate a simple class diagram using text-based notation.

class DesignNotation:
    def __init__(self, notation_type, content):
        self.notation_type = notation_type
        self.content = content
    
    def display_notation(self):
        print(f"\n{self.notation_type} Notation:")
        print(self.content)

# Simulate Design Notations (Class Diagram Example)
class_diagram = """
Class Diagram:

+------------------+
|   User           |
+------------------+
| - userID         |
| - userName       |
| - email          |
+------------------+
| + login()        |
| + register()     |
| + resetPassword()|
+------------------+

+------------------+
|   Product        |
+------------------+
| - productID      |
| - productName    |
| - price          |
+------------------+
| + getDetails()   |
| + addReview()    |
+------------------+
"""
notation = DesignNotation("Class", class_diagram)
notation.display_notation()

# 4. Design Evaluation and Validation
# - Design evaluation ensures the system meets the requirements, and validation confirms that the system works as intended.
# We will simulate evaluating the design for correctness and validating against user requirements.

class DesignEvaluation:
    def __init__(self, design, requirements):
        self.design = design
        self.requirements = requirements
    
    def evaluate_design(self):
        print("\nEvaluating Design...")
        for requirement in self.requirements:
            if requirement not in self.design:
                print(f"Warning: Design does not fulfill requirement: {requirement}")
            else:
                print(f"Design meets the requirement: {requirement}")
    
    def validate_design(self):
        print("\nValidating Design...")
        if "User Authentication" in self.design and "Product Catalog" in self.design:
            print("Design is valid. The necessary modules are present.")
        else:
            print("Design is invalid. Some required modules are missing.")

# Simulate Design Evaluation and Validation
design = ["User Authentication", "Product Catalog", "Shopping Cart"]
requirements = ["User Authentication", "Product Catalog", "Payment System"]
evaluation = DesignEvaluation(design, requirements)
evaluation.evaluate_design()
evaluation.validate_design()

# Summary:
"""
1. Design for Reuse: Involves creating reusable components that can be used across multiple systems or projects.
2. Design for Change: Ensures that systems are flexible and easy to modify as requirements change over time.
3. Design Notations: Uses visual representations like class diagrams, pseudo-code, or models to communicate design structure and behavior.
4. Design Evaluation and Validation: Ensures that the design meets requirements and works as intended by evaluating and validating it against project needs.
"""


