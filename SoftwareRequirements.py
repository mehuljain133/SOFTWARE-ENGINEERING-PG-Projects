# Unit-IV Software requirements: Requirements analysis, functional and non-functional requirements elicitation, analysis tools, requirements definition, requirements specification, static and dynamic specifications, requirements review. 

# Unit-IV Software Requirements: Overview and Code Representation

# 1. Requirements Analysis
# - Requirements analysis is the process of understanding and documenting what is needed from a software system.
# We will simulate the process of analyzing functional and non-functional requirements, as well as performing elicitation.

class RequirementsAnalysis:
    def __init__(self):
        self.functional_requirements = []
        self.non_functional_requirements = []
    
    def add_functional_requirement(self, requirement):
        self.functional_requirements.append(requirement)
    
    def add_non_functional_requirement(self, requirement):
        self.non_functional_requirements.append(requirement)
    
    def display_requirements(self):
        print("\nFunctional Requirements:")
        for req in self.functional_requirements:
            print(f"- {req}")
        
        print("\nNon-Functional Requirements:")
        for req in self.non_functional_requirements:
            print(f"- {req}")

# Simulate Requirements Analysis
analysis = RequirementsAnalysis()
analysis.add_functional_requirement("User should be able to log in.")
analysis.add_functional_requirement("Admin should be able to add/edit users.")
analysis.add_non_functional_requirement("The system should respond within 2 seconds.")
analysis.add_non_functional_requirement("The system should handle 1000 concurrent users.")
analysis.display_requirements()

# 2. Elicitation
# - Requirements elicitation is the process of gathering the needs and requirements from stakeholders.

class RequirementsElicitation:
    def __init__(self, stakeholders):
        self.stakeholders = stakeholders
        self.requirements = []
    
    def gather_requirements(self):
        print(f"Gathering requirements from {', '.join(self.stakeholders)}...")
        # Simulate gathering requirements from stakeholders
        self.requirements.append("User should be able to reset their password.")
        self.requirements.append("System should have role-based access control.")
    
    def display_requirements(self):
        print("\nElicited Requirements:")
        for req in self.requirements:
            print(f"- {req}")

# Simulate Requirements Elicitation
elicitation = RequirementsElicitation(stakeholders=["Business Analyst", "Client", "End User"])
elicitation.gather_requirements()
elicitation.display_requirements()

# 3. Analysis Tools
# - We can use various analysis tools such as UML diagrams, decision matrices, and use cases for requirements analysis.
# Here, we simulate a simple decision matrix for analyzing trade-offs between requirements.

class AnalysisTool:
    def __init__(self, tool_type):
        self.tool_type = tool_type
    
    def use_tool(self):
        if self.tool_type == "Decision Matrix":
            print("\nUsing Decision Matrix to analyze trade-offs:")
            trade_offs = {
                "Speed vs Quality": "Speed is prioritized to meet launch deadline.",
                "Cost vs Features": "Features are limited to reduce development cost."
            }
            for decision, reason in trade_offs.items():
                print(f"{decision}: {reason}")
        else:
            print(f"\n{self.tool_type} tool is not implemented.")

# Simulate Analysis Tool Usage
analysis_tool = AnalysisTool(tool_type="Decision Matrix")
analysis_tool.use_tool()

# 4. Requirements Definition and Specification
# - Requirements definition involves formalizing and documenting requirements.
# - The specification includes detailed descriptions of system behavior, interfaces, and constraints.

class RequirementsDefinition:
    def __init__(self):
        self.specifications = []
    
    def add_specification(self, spec):
        self.specifications.append(spec)
    
    def display_specifications(self):
        print("\nRequirements Specification:")
        for spec in self.specifications:
            print(f"- {spec}")

# Simulate Requirements Definition and Specification
definition = RequirementsDefinition()
definition.add_specification("The system should authenticate users via email and password.")
definition.add_specification("The system should allow users to change their passwords securely.")
definition.display_specifications()

# 5. Static and Dynamic Specifications
# - Static specifications describe the system's structure (e.g., data models, architecture).
# - Dynamic specifications describe system behavior (e.g., use cases, interactions).

class StaticAndDynamicSpecifications:
    def __init__(self):
        self.static_specs = []
        self.dynamic_specs = []
    
    def add_static_specification(self, static_spec):
        self.static_specs.append(static_spec)
    
    def add_dynamic_specification(self, dynamic_spec):
        self.dynamic_specs.append(dynamic_spec)
    
    def display_specifications(self):
        print("\nStatic Specifications (Structure):")
        for spec in self.static_specs:
            print(f"- {spec}")
        
        print("\nDynamic Specifications (Behavior):")
        for spec in self.dynamic_specs:
            print(f"- {spec}")

# Simulate Static and Dynamic Specifications
specifications = StaticAndDynamicSpecifications()
specifications.add_static_specification("System has a User class with fields: name, email, password.")
specifications.add_static_specification("The database has tables for Users, Roles, and Permissions.")
specifications.add_dynamic_specification("User login should trigger authentication process.")
specifications.add_dynamic_specification("User registration triggers an email confirmation.")
specifications.display_specifications()

# 6. Requirements Review
# - A review process involves stakeholders checking the requirements for completeness, consistency, and clarity.

class RequirementsReview:
    def __init__(self, requirements):
        self.requirements = requirements
    
    def review(self):
        print("\nReviewing Requirements:")
        for req in self.requirements:
            if "should" not in req:
                print(f"Warning: Requirement '{req}' is not phrased as a 'should' statement.")
            else:
                print(f"Requirement '{req}' is valid.")

# Simulate Requirements Review
review = RequirementsReview(requirements=[
    "User should be able to log in.",
    "Admin should be able to add/edit users.",
    "System allow password reset."
])
review.review()

# Summary:
"""
1. Requirements Analysis: Involves identifying functional and non-functional requirements.
2. Elicitation: Gathering requirements from stakeholders such as business analysts, clients, and users.
3. Analysis Tools: Tools like decision matrices help analyze trade-offs in requirements.
4. Requirements Definition & Specification: Involves formalizing and documenting requirements in detail.
5. Static & Dynamic Specifications: Static specs describe system structure; dynamic specs describe behavior.
6. Requirements Review: Ensures completeness, consistency, and clarity of requirements.
"""

