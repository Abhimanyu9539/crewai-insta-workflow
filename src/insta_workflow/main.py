#!/usr/bin/env python
import sys
import warnings
import agentops
from datetime import datetime

from insta_workflow.crew import InstaWorflow

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

import dotenv
dotenv.load_dotenv()

# Initialize AgentOps client
agentops.init()


# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    # Topic-based content example
    inputs = {
        'topic': 'Motivational Quotes',
        'brand_voice': 'Inspirational',
        'content_type': 'single_post',
        'content_length': 'Short',
        'num_variations': 3,
        'target_account': ''  # Empty for topic mode
    }
    
    try:
        from opik.integrations.crewai import track_crewai

        track_crewai(project_name="crewai-insta-workflow")

        my_crew =  InstaWorflow().crew()
        result = my_crew.kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def run_topic(topic: str = None, brand_voice: str = 'professional'):
    """
    Run the crew for topic-based content creation.
    """
    inputs = {
        'topic': topic or 'AI in sustainable fashion',
        'brand_voice': brand_voice,
        'content_type': 'single_post',
        'content_length': 'medium',
        'num_variations': 3,
        'target_account': ''  # Empty for topic mode
    }
    
    try:
        result = InstaWorflow().crew().kickoff(inputs=inputs)
        print(f"\n🎉 Content created successfully for topic: {inputs['topic']}")
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running topic workflow: {e}")


def run_mimic(target_account: str = None, topic: str = None):
    """
    Run the crew for account mimicking content creation.
    """
    inputs = {
        'target_account': target_account or 'nike',
        'topic': topic or 'content in their typical style',
        'brand_voice': 'authentic',  # Use authentic for mimicking
        'content_type': 'single_post',
        'content_length': 'medium',
        'num_variations': 3
    }
    
    try:
        result = InstaWorflow().crew().kickoff(inputs=inputs)
        print(f"\n🎉 Content created successfully mimicking @{inputs['target_account']}")
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running mimic workflow: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'topic': 'AI and technology trends',
        'brand_voice': 'professional',
        'content_type': 'single_post',
        'content_length': 'medium',
        'num_variations': 3,
        'target_account': ''
    }
    
    try:
        InstaWorflow().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        InstaWorflow().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'topic': 'Social media marketing tips',
        'brand_voice': 'inspirational',
        'content_type': 'carousel',
        'content_length': 'medium',
        'num_variations': 2,
        'target_account': ''
    }
    
    try:
        InstaWorflow().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


def interactive():
    """
    Run the crew in interactive mode with user inputs.
    """
    print("🎨 Instagram Content Creator - Interactive Mode")
    print("=" * 50)
    
    # Get mode from user
    print("\nChoose content creation mode:")
    print("1. Topic-based content")
    print("2. Mimic account style")
    
    while True:
        choice = input("\nEnter choice (1 or 2): ").strip()
        if choice in ['1', '2']:
            break
        print("❌ Please enter 1 or 2")
    
    if choice == '1':
        # Topic-based mode
        topic = input("\nEnter topic (e.g., 'AI in fashion'): ").strip()
        if not topic:
            topic = "AI in sustainable fashion"
        
        print("\nBrand voice options: professional, casual, inspirational, educational, humorous")
        brand_voice = input("Enter brand voice (or press Enter for 'professional'): ").strip()
        if not brand_voice:
            brand_voice = "professional"
        
        print(f"\n🚀 Creating content for topic: '{topic}' with {brand_voice} voice...")
        result = run_topic(topic, brand_voice)
        
    else:
        # Mimic mode
        account = input("\nEnter Instagram account to mimic (e.g., 'nike'): ").strip()
        if not account:
            account = "nike"
        
        topic = input("Enter topic (optional, press Enter for their typical style): ").strip()
        if not topic:
            topic = None
        
        print(f"\n🚀 Creating content mimicking @{account}...")
        result = run_mimic(account, topic)
    
    print("\n✅ Content creation completed!")


if __name__ == "__main__":
    """
    Entry point for running the crew with different modes.
    
    Usage:
        python main.py                    # Run with default inputs
        python main.py interactive        # Interactive mode
        python main.py topic "AI trends"  # Topic mode with custom topic
        python main.py mimic "nike"       # Mimic mode with target account
    """
    
    if len(sys.argv) == 1:
        # Default run
        print("🚀 Running Instagram Content Crew with default inputs...")
        run()
    
    elif len(sys.argv) >= 2:
        command = sys.argv[1].lower()
        
        if command == "interactive":
            interactive()
        
        elif command == "topic":
            topic = sys.argv[2] if len(sys.argv) > 2 else "AI in sustainable fashion"
            brand_voice = sys.argv[3] if len(sys.argv) > 3 else "professional"
            print(f"🚀 Running topic-based content creation for: {topic}")
            run_topic(topic, brand_voice)
        
        elif command == "mimic":
            account = sys.argv[2] if len(sys.argv) > 2 else "nike"
            topic = sys.argv[3] if len(sys.argv) > 3 else None
            print(f"🚀 Running account mimicking for: @{account}")
            run_mimic(account, topic)
        
        elif command == "train":
            if len(sys.argv) < 4:
                print("❌ Usage: python main.py train <n_iterations> <filename>")
                sys.exit(1)
            train()
        
        elif command == "test":
            if len(sys.argv) < 4:
                print("❌ Usage: python main.py test <n_iterations> <eval_llm>")
                sys.exit(1)
            test()
        
        elif command == "replay":
            if len(sys.argv) < 3:
                print("❌ Usage: python main.py replay <task_id>")
                sys.exit(1)
            replay()
        
        else:
            print("❌ Unknown command. Available commands:")
            print("  python main.py                    # Default run")
            print("  python main.py interactive        # Interactive mode")
            print("  python main.py topic 'AI trends'  # Topic mode")
            print("  python main.py mimic 'nike'       # Mimic mode")
            print("  python main.py train <n> <file>   # Train crew")
            print("  python main.py test <n> <llm>     # Test crew")
            print("  python main.py replay <task_id>   # Replay execution")