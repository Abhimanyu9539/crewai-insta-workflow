from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class InstaWorflow():
    """Insta Workflow crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def trend_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['trend_researcher'], # type: ignore[index]
            verbose=True
        )

    @agent
    def creative_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['creative_writer'], 
            verbose=True
        )

    @agent
    def style_editor(self) -> Agent:
        return Agent(
            config=self.agents_config['style_editor'],
            verbose=True
        )

    @task
    def research_trends_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_trends_task'],
            output_file='report.md'
        )

    @task
    def create_content_variations_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_content_variations_task'],
            output_file='content_vars.md'
        )

    @task
    def optimize_content_task(self) -> Task:
        return Task(
            config=self.tasks_config['optimize_content_task'],
            output_file='content.md'
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Insta Worklflow crew"""
        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
            
        )
