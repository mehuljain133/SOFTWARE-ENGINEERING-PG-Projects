# Unit-II Software process: The software lifecycle, the waterfall model and variations, risk-driven approaches, introduction to evolutionary and prototyping approaches, agile process models, system classifications

# Unit-II Software Process: Overview and Code Representation

# 1. The Software Lifecycle: Stages of software development from inception to retirement.
# - This model helps organize the stages of a software project, such as:
#   - Requirement gathering
#   - Design
#   - Implementation
#   - Testing
#   - Deployment
#   - Maintenance

# We will simulate this lifecycle in code.

class SoftwareLifecycle:
    def __init__(self, project_name):
        self.project_name = project_name
        self.phase = "Requirement Gathering"
    
    def advance_phase(self):
        if self.phase == "Requirement Gathering":
            self.phase = "Design"
        elif self.phase == "Design":
            self.phase = "Implementation"
        elif self.phase == "Implementation":
            self.phase = "Testing"
        elif self.phase == "Testing":
            self.phase = "Deployment"
        elif self.phase == "Deployment":
            self.phase = "Maintenance"
        else:
            self.phase = "Completed"
    
    def __str__(self):
        return f"Project {self.project_name} is currently in the {self.phase} phase."


# Simulate Software Lifecycle Process
project = SoftwareLifecycle("Inventory Management System")
for _ in range(7):  # Progress through all lifecycle stages
    print(project)
    project.advance_phase()

print("\n--- Software Process Models ---")

# 2. The Waterfall Model (Linear sequential model)
# - The Waterfall Model is a linear approach, where each phase must be completed before the next one begins.

def waterfall_model():
    phases = [
        "Requirement Analysis",
        "System Design",
        "Implementation",
        "Integration and Testing",
        "Deployment",
        "Maintenance"
    ]
    
    for phase in phases:
        print(f"Executing phase: {phase}")
        
# Simulate Waterfall Model Process
print("\nWaterfall Model Process:")
waterfall_model()

# 3. Risk-driven Approaches
# - Risk-driven approaches focus on identifying and addressing potential risks early in the software process.

class RiskDrivenApproach:
    def __init__(self, risks):
        self.risks = risks

    def evaluate_risks(self):
        for risk, probability in self.risks.items():
            if probability > 0.5:
                print(f"High risk: {risk} - take action!")
            else:
                print(f"Low risk: {risk} - monitor.")

# Define Risks and Risk Management Strategy
risks = {
    "Requirement ambiguity": 0.7,
    "Technical complexity": 0.4,
    "Market changes": 0.6,
    "Team availability": 0.2
}

# Simulate Risk-driven approach
risk_model = RiskDrivenApproach(risks)
print("\nRisk-driven Approach Evaluation:")
risk_model.evaluate_risks()

# 4. Evolutionary and Prototyping Approaches
# - Evolutionary models focus on iterative development where the software is refined over time.
# - Prototyping involves creating a mockup or early version to gain feedback and then iterating.

class Prototype:
    def __init__(self, prototype_version):
        self.prototype_version = prototype_version
    
    def build_prototype(self):
        print(f"Building prototype version {self.prototype_version}...")
    
    def get_feedback(self):
        print(f"Collecting feedback for prototype version {self.prototype_version}...")

# Simulate Prototyping Approach
proto = Prototype("1.0")
print("\nPrototyping Approach:")
proto.build_prototype()
proto.get_feedback()

# 5. Agile Process Models
# - Agile processes promote adaptive planning, early delivery, and continuous improvement.

class AgileProcess:
    def __init__(self, sprint_length):
        self.sprint_length = sprint_length  # in days
        self.sprints = 0

    def plan_sprint(self):
        print(f"Planning Sprint {self.sprints + 1} ({self.sprint_length} days)")

    def review_sprint(self):
        print(f"Reviewing Sprint {self.sprints + 1}")

    def complete_sprint(self):
        self.sprints += 1
        print(f"Sprint {self.sprints} completed.")

# Simulate Agile Process with 3 Sprints
agile_model = AgileProcess(14)  # Sprint length is 14 days
print("\nAgile Process:")
for _ in range(3):
    agile_model.plan_sprint()
    agile_model.complete_sprint()
    agile_model.review_sprint()

# 6. System Classifications
# - Software systems can be classified into categories based on their complexity and scope.

class SystemClassification:
    def __init__(self, system_type):
        self.system_type = system_type

    def classify_system(self):
        classifications = {
            "Simple": "Small-scale systems with few users, easy to design and deploy.",
            "Medium": "Systems with moderate complexity and multiple users.",
            "Complex": "Large-scale systems involving multiple subsystems and high-level integration."
        }
        return classifications.get(self.system_type, "Unknown system type")

# Classify a few systems
system_types = ["Simple", "Medium", "Complex", "Unknown"]
print("\nSystem Classifications:")
for system_type in system_types:
    system = SystemClassification(system_type)
    print(f"System Type: {system_type} -> {system.classify_system()}")

# Summary:
"""
1. Software Lifecycle: Represents the stages of a software project, helping organize development.
2. Waterfall Model: A linear, sequential approach where each phase is completed before the next.
3. Risk-driven Approach: Focuses on identifying and addressing risks early in the process.
4. Evolutionary & Prototyping Approaches: Iterative methods that build early versions and refine over time.
5. Agile Model: Emphasizes adaptive planning and early delivery through multiple short sprints.
6. System Classifications: Categorizes systems as Simple, Medium, or Complex based on scale and complexity.
"""

