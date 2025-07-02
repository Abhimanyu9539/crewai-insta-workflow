#!/usr/bin/env python
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

@CrewBase
class InstaWorkflow():
    """Instagram Content Creation Workflow with two separate crews"""
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def trend_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['trend_researcher'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            max_iter=3
        )

    @agent
    def creative_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['creative_writer'], 
            verbose=True,
            max_iter=2
        )

    @agent
    def style_editor(self) -> Agent:
        return Agent(
            config=self.agents_config['style_editor'],
            verbose=True,
            max_iter=2
        )

    @task
    def research_trends_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_trends_task'],
        )

    @task
    def analyze_account_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_account_task'],
        )

    @task
    def create_content_variations_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_content_variations_task'],
        )

    @task
    def mimic_account_content_task(self) -> Task:
        return Task(
            config=self.tasks_config['mimic_account_content_task'],
        )

    @task
    def optimize_content_task(self) -> Task:
        return Task(
            config=self.tasks_config['optimize_content_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the default Insta Workflow crew"""
        return Crew(
            agents=self.agents,  # Automatically includes all agents
            tasks=self.tasks,    # Automatically includes all tasks
            process=Process.sequential,
            verbose=True,
        )