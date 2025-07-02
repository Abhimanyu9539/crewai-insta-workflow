#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from insta_workflow.crew import InstaWorkflow

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def create_topic_content(topic: str, brand_voice: str = "professional", 
                        content_type: str = "single_post", content_length: str = "medium",
                        num_variations: int = 3):
    """
    Create topic-based Instagram content
    """
    inputs = {
        'topic': topic,
        'brand_voice': brand_voice,
        'content_type': content_type,
        'content_length': content_length,
        'num_variations': num_variations,
        'target_account': 'none',  # Set to 'none' for topic mode
        'current_date': datetime.now().strftime("%Y-%m-%d"),
        'current_year': str(datetime.now().year)
    }
    
    try:
        print(f"\n🚀 Creating topic-based content for: {topic}")
        print(f"   Brand voice: {brand_voice}")
        print(f"   Content type: {content_type}")
        print(f"   Variations: {num_variations}")
        
        workflow = InstaWorkflow()
        
        # For topic mode, we'll use specific tasks
        crew = workflow.crew()
        
        # Run only the tasks needed for topic mode
        crew.tasks = [
            workflow.research_trends_task(),
            workflow.create_content_variations_task(),
            workflow.optimize_content_task()
        ]
        
        result = crew.kickoff(inputs=inputs)
        
        print(f"\n✅ Topic-based content created successfully!")
        return result
        
    except Exception as e:
        print(f"\n❌ Error creating topic content: {str(e)}")
        raise


def create_mimic_content(target_account: str, topic: str = None, 
                        content_type: str = "single_post", content_length: str = "medium",
                        num_variations: int = 3):
    """
    Create content mimicking an Instagram account's style
    """
    # Clean account handle
    target_account = target_account.replace("@", "").strip()
    
    inputs = {
        'target_account': target_account,
        'topic': topic or f"content in @{target_account}'s typical style",
        'brand_voice': 'authentic',
        'content_type': content_type,
        'content_length': content_length,
        'num_variations': num_variations,
        'current_date': datetime.now().strftime("%Y-%m-%d"),
        'current_year': str(datetime.now().year)
    }
    
    try:
        print(f"\n🚀 Creating content mimicking: @{target_account}")
        if topic:
            print(f"   Topic: {topic}")
        print(f"   Content type: {content_type}")
        print(f"   Variations: {num_variations}")
        
        workflow = InstaWorkflow()
        
        # For mimic mode, we'll use specific tasks
        crew = workflow.crew()
        
        # Run only the tasks needed for mimic mode
        crew.tasks = [
            workflow.analyze_account_task(),
            workflow.mimic_account_content_task(),
            workflow.optimize_content_task()
        ]
        
        result = crew.kickoff(inputs=inputs)
        
        print(f"\n✅ Mimic content created successfully!")
        return result
        
    except Exception as e:
        print(f"\n❌ Error creating mimic content: {str(e)}")
        raise


def run():
    """
    Run the crew with default inputs
    """
    return create_topic_content(
        topic="AI in sustainable fashion",
        brand_voice="professional",
        content_type="single_post",
        content_length="medium",
        num_variations=3
    )


def interactive():
    """
    Run the crew in interactive mode
    """
    print("\n🎨 Instagram Content Creator - Interactive Mode")
    print("=" * 50)
    
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
        topic = input("\nEnter topic: ").strip() or "AI in sustainable fashion"
        
        print("\nBrand voice options: professional, casual, inspirational, educational, humorous")
        brand_voice = input("Enter brand voice (default: professional): ").strip() or "professional"
        
        print("\nContent type options: single_post, carousel, reel")
        content_type = input("Enter content type (default: single_post): ").strip() or "single_post"
        
        print("\nContent length options: short, medium, long")
        content_length = input("Enter content length (default: medium): ").strip() or "medium"
        
        num_str = input("\nNumber of variations (default: 3): ").strip()
        num_variations = int(num_str) if num_str.isdigit() else 3
        
        create_topic_content(
            topic=topic,
            brand_voice=brand_voice,
            content_type=content_type,
            content_length=content_length,
            num_variations=num_variations
        )
        
    else:
        # Mimic mode
        account = input("\nEnter Instagram account to mimic: ").strip() or "nike"
        
        topic = input("Enter topic (optional): ").strip() or None
        
        print("\nContent type options: single_post, carousel, reel")
        content_type = input("Enter content type (default: single_post): ").strip() or "single_post"
        
        print("\nContent length options: short, medium, long")
        content_length = input("Enter content length (default: medium): ").strip() or "medium"
        
        num_str = input("\nNumber of variations (default: 3): ").strip()
        num_variations = int(num_str) if num_str.isdigit() else 3
        
        create_mimic_content(
            target_account=account,
            topic=topic,
            content_type=content_type,
            content_length=content_length,
            num_variations=num_variations
        )


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("🚀 Running with default inputs...")
        run()
    
    elif sys.argv[1].lower() == "interactive":
        interactive()
    
    elif sys.argv[1].lower() == "topic":
        topic = sys.argv[2] if len(sys.argv) > 2 else "AI in sustainable fashion"
        brand_voice = sys.argv[3] if len(sys.argv) > 3 else "professional"
        create_topic_content(topic, brand_voice)
    
    elif sys.argv[1].lower() == "mimic":
        if len(sys.argv) < 3:
            print("❌ Usage: python main.py mimic <account> [topic]")
            sys.exit(1)
        account = sys.argv[2]
        topic = sys.argv[3] if len(sys.argv) > 3 else None
        create_mimic_content(account, topic)
    
    else:
        print("\n📖 Usage:")
        print("  python main.py                    # Default run")
        print("  python main.py interactive        # Interactive mode")
        print("  python main.py topic 'topic'      # Topic mode")
        print("  python main.py mimic 'account'    # Mimic mode")