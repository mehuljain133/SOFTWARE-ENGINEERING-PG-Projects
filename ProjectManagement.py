# Unit-III Project management: Relationship to lifecycle, project planning, project control, project organization, risk management, cost models, configuration management, version control, quality assurance, metrics. 

# Unit-III Project Management: Overview and Code Representation

# 1. Relationship to Lifecycle
# - Project management integrates with the software lifecycle, guiding the planning, execution, and control of projects.
# The phases of project management are aligned with the software lifecycle, helping ensure on-time delivery, quality, and cost control.

class ProjectLifecycle:
    def __init__(self, project_name):
        self.project_name = project_name
        self.phase = "Initiation"
    
    def advance_phase(self):
        if self.phase == "Initiation":
            self.phase = "Planning"
        elif self.phase == "Planning":
            self.phase = "Execution"
        elif self.phase == "Execution":
            self.phase = "Monitoring & Control"
        elif self.phase == "Monitoring & Control":
            self.phase = "Closure"
        else:
            self.phase = "Completed"
    
    def __str__(self):
        return f"Project {self.project_name} is currently in the {self.phase} phase."

# Simulate Project Lifecycle Process
project_lifecycle = ProjectLifecycle("E-commerce Platform Development")
for _ in range(6):  # Progress through all project phases
    print(project_lifecycle)
    project_lifecycle.advance_phase()

print("\n--- Project Management Concepts ---")

# 2. Project Planning
# - Project planning involves defining scope, goals, tasks, timelines, and resource allocation.
# - Here's a simple planning approach where tasks are listed, assigned, and deadlines are set.

class ProjectPlanning:
    def __init__(self, project_name):
        self.project_name = project_name
        self.tasks = []
    
    def add_task(self, task_name, assignee, deadline):
        self.tasks.append({"task": task_name, "assignee": assignee, "deadline": deadline})
    
    def display_plan(self):
        print(f"Project Plan for {self.project_name}:")
        for task in self.tasks:
            print(f"Task: {task['task']} | Assignee: {task['assignee']} | Deadline: {task['deadline']}")

# Simulate Project Planning
planning = ProjectPlanning("E-commerce Platform Development")
planning.add_task("Requirement Gathering", "Alice", "2025-06-01")
planning.add_task("UI/UX Design", "Bob", "2025-06-15")
planning.add_task("Backend Development", "Charlie", "2025-07-01")
planning.add_task("Testing", "David", "2025-07-15")
planning.display_plan()

# 3. Project Control
# - Project control involves monitoring progress, managing changes, and ensuring the project stays on track.

class ProjectControl:
    def __init__(self):
        self.progress = 0  # Percentage of task completion
    
    def update_progress(self, progress):
        self.progress = progress
        print(f"Project Progress: {self.progress}%")
    
    def control_actions(self):
        if self.progress < 50:
            print("Project is behind schedule. Take corrective actions.")
        elif self.progress < 80:
            print("Project is on track. Keep monitoring.")
        else:
            print("Project is near completion. Final adjustments needed.")

# Simulate Project Control
control = ProjectControl()
control.update_progress(40)
control.control_actions()
control.update_progress(75)
control.control_actions()

# 4. Risk Management
# - Identifying, evaluating, and mitigating risks during the project lifecycle.

class RiskManagement:
    def __init__(self, risks):
        self.risks = risks
    
    def evaluate_risks(self):
        for risk, severity in self.risks.items():
            if severity > 0.7:
                print(f"High risk: {risk} - immediate attention required.")
            elif severity > 0.3:
                print(f"Medium risk: {risk} - monitor regularly.")
            else:
                print(f"Low risk: {risk} - continue with normal process.")

# Define risks for the project
risks = {
    "Requirement changes": 0.8,
    "Team turnover": 0.4,
    "Technological challenges": 0.6,
    "Supplier delays": 0.3
}

# Simulate Risk Management
risk_management = RiskManagement(risks)
print("\nRisk Management Evaluation:")
risk_management.evaluate_risks()

# 5. Cost Models
# - Cost estimation involves calculating the project's budget based on factors like complexity, time, and resources.

class CostModel:
    def __init__(self, hourly_rate, hours_estimated, team_size):
        self.hourly_rate = hourly_rate
        self.hours_estimated = hours_estimated
        self.team_size = team_size
    
    def calculate_cost(self):
        total_cost = self.hourly_rate * self.hours_estimated * self.team_size
        return total_cost

# Simulate Cost Model
cost_model = CostModel(hourly_rate=50, hours_estimated=500, team_size=5)
estimated_cost = cost_model.calculate_cost()
print(f"\nEstimated project cost: ${estimated_cost}")

# 6. Configuration Management and Version Control
# - Managing different versions of software artifacts, ensuring integrity and consistency.

class VersionControl:
    def __init__(self):
        self.versions = {}
    
    def add_version(self, version, description):
        self.versions[version] = description
        print(f"Version {version} added: {description}")
    
    def get_version(self, version):
        if version in self.versions:
            return self.versions[version]
        else:
            return "Version not found."

# Simulate Version Control
version_control = VersionControl()
version_control.add_version("v1.0", "Initial release")
version_control.add_version("v1.1", "Bug fixes and minor updates")
print(f"\nVersion v1.0 details: {version_control.get_version('v1.0')}")
print(f"Version v1.1 details: {version_control.get_version('v1.1')}")

# 7. Quality Assurance
# - Ensures the product meets quality standards through testing, reviews, and process improvement.

class QualityAssurance:
    def __init__(self, test_cases):
        self.test_cases = test_cases
    
    def perform_tests(self):
        print("Performing quality assurance tests:")
        for test_case in self.test_cases:
            print(f"Running test: {test_case}")
            print(f"Test result for {test_case}: Passed")

# Simulate Quality Assurance
qa = QualityAssurance(test_cases=["Unit Test 1", "Integration Test", "UI/UX Test"])
qa.perform_tests()

# 8. Metrics
# - Metrics are used to measure the success, progress, and quality of the project.

class ProjectMetrics:
    def __init__(self, completed_tasks, total_tasks, defect_rate):
        self.completed_tasks = completed_tasks
        self.total_tasks = total_tasks
        self.defect_rate = defect_rate
    
    def calculate_progress(self):
        progress = (self.completed_tasks / self.total_tasks) * 100
        return progress
    
    def calculate_defect_density(self):
        return self.defect_rate / self.total_tasks

# Simulate Project Metrics
metrics = ProjectMetrics(completed_tasks=15, total_tasks=20, defect_rate=3)
print(f"\nProject Progress: {metrics.calculate_progress():.2f}%")
print(f"Defect Density: {metrics.calculate_defect_density():.2f} defects per task")

# Summary:
"""
1. Relationship to Lifecycle: Project management guides the entire software lifecycle, from initiation to closure.
2. Project Planning: Involves defining tasks, assigning resources, and setting deadlines.
3. Project Control: Monitors progress and manages corrective actions to keep the project on track.
4. Risk Management: Identifies and mitigates risks to avoid potential issues during the project.
5. Cost Models: Estimates the cost of the project based on time, resources, and hourly rates.
6. Configuration Management & Version Control: Ensures that software artifacts are properly managed across versions.
7. Quality Assurance: Ensures that the software meets required standards through testing and process improvement.
8. Metrics: Measures project progress, quality, and defect density to monitor success.
"""

