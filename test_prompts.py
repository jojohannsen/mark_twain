"""
Test script to demonstrate the character prompt templates
"""

from character_prompt_template import get_character_prompt, mark_twain_characters


def display_full_prompt(character_id: str, goal: str):
    """Display the complete generated prompt for a character"""
    
    print(f"\n{'='*60}")
    print(f"CHARACTER: {mark_twain_characters[character_id]['name']}")
    print(f"GOAL: {goal}")
    print(f"{'='*60}")
    
    try:
        prompt = get_character_prompt(character_id, goal)
        
        # Display the full system message
        system_message = prompt.messages[0]
        print("\nFULL SYSTEM PROMPT:")
        print("-" * 40)
        print(system_message.content)
        
    except KeyError as e:
        print(f"Error: {e}")


def main():
    # Test different characters with different goals
    test_cases = [
        ("huckleberry_finn", "convince someone to join you on an adventure down the Mississippi River"),
        ("tom_sawyer", "recruit someone for your latest elaborate scheme"),
        ("jim", "find information about your family while staying safe"),
        ("hank_morgan", "explain modern technology to medieval people"),
        ("puddnhead_wilson", "share some wisdom about human nature")
    ]
    
    print("Mark Twain Character Prompt Examples")
    
    for character_id, goal in test_cases:
        display_full_prompt(character_id, goal)
        
        # Ask if user wants to continue
        if character_id != test_cases[-1][0]:  # Not the last one
            input("\nPress Enter to continue to next character...")


if __name__ == "__main__":
    main()