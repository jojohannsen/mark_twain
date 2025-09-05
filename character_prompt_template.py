"""
Character Prompt Template for Mark Twain Characters
Uses LangChain ChatPromptTemplate to generate conversational prompts
"""

from langchain_core.prompts import ChatPromptTemplate
from mark_twain_characters import mark_twain_characters


def create_character_prompt_template():
    """
    Creates a ChatPromptTemplate for Mark Twain character conversations.
    
    Template variables:
    - character_name: The character's display name
    - character_description: Full character description
    - character_speech: How they speak and express themselves
    - character_worldview: How they see themselves and others
    - conversation_goal: The character's goal in the conversation
    
    Returns:
        ChatPromptTemplate: Ready-to-use prompt template
    """
    
    system_template = """You are {character_name}, a character from Mark Twain's literary works.

CHARACTER BACKGROUND:
{character_description}

HOW YOU SPEAK AND THINK:
{character_speech}

YOUR WORLDVIEW:
{character_worldview}

CONVERSATION INSTRUCTIONS:
You are having a conversation with another person. Be friendly, conversational, and stay true to your character's voice, dialect, and personality. Besides being engaging in conversation, you are also - not too intrusively - interested in your goal: {conversation_goal}

Respond as {character_name} would, using their characteristic speech patterns, vocabulary, and perspective on life. Keep your goal in mind but don't force it - let it emerge naturally through the conversation."""

    return ChatPromptTemplate.from_messages([
        ("system", system_template)
    ])


def get_character_prompt(character_id: str, conversation_goal: str):
    """
    Generate a complete prompt for a specific Mark Twain character.
    
    Args:
        character_id (str): Key from mark_twain_characters dict (e.g., "huckleberry_finn")
        conversation_goal (str): What the character wants to achieve in conversation
        
    Returns:
        Formatted prompt messages ready for an LLM
        
    Raises:
        KeyError: If character_id is not found in mark_twain_characters
    """
    
    if character_id not in mark_twain_characters:
        available_ids = list(mark_twain_characters.keys())
        raise KeyError(f"Character '{character_id}' not found. Available characters: {available_ids}")
    
    character = mark_twain_characters[character_id]
    template = create_character_prompt_template()
    
    # Build character speech patterns from example conversations
    speech_examples = character.get('example_conversations', '').replace('•', '-')
    
    # Combine self-perception and view of others for worldview
    worldview = f"How you see yourself: {character.get('self_perception', '')}\n\nHow you view others: {character.get('view_of_others', '').replace('•', '-')}"
    
    # Generate the prompt
    prompt_messages = template.invoke({
        "character_name": character["name"],
        "character_description": character["description"],
        "character_speech": speech_examples,
        "character_worldview": worldview,
        "conversation_goal": conversation_goal
    })
    
    return prompt_messages


# Example usage and testing
if __name__ == "__main__":
    print("Mark Twain Character Prompt Generator")
    print("=" * 40)
    
    # Test with Huckleberry Finn
    try:
        goal = "convince someone to join you on an adventure down the Mississippi River"
        prompt = get_character_prompt("huckleberry_finn", goal)
        
        print(f"\nGenerated prompt for Huckleberry Finn:")
        print("-" * 40)
        for message in prompt.messages:
            print(f"Role: {message.__class__.__name__}")
            print(f"Content: {message.content[:200]}...")
            print()
            
    except KeyError as e:
        print(f"Error: {e}")
        
    # Show available characters
    print("Available character IDs:")
    for char_id in mark_twain_characters.keys():
        print(f"  - {char_id}")