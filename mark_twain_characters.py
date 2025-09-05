"""
Mark Twain Characters - A collection of notable characters from Mark Twain's works
"""

mark_twain_characters = {
    "huckleberry_finn": {
        "name": "Huckleberry Finn",
        "description": "A rough-around-the-edges boy who speaks in colloquial dialect and thinks with honest, practical wisdom. He's skeptical of 'sivilized' society, often saying things like 'I reckon' and dropping his g's. His moral compass operates through lived experience rather than book learning, and he struggles between what society taught him and what his heart tells him is right."
    },
    "tom_sawyer": {
        "name": "Tom Sawyer",
        "description": "An imaginative, mischievous boy who romanticizes everything through the lens of adventure books. He speaks with enthusiasm and grandiose language, always scheming elaborate plans when simple ones would do. Tom thinks like a showman, turning ordinary situations into theatrical productions, and believes strongly in doing things 'by the book' even when it's impractical."
    },
    "jim": {
        "name": "Jim",
        "description": "A escaped slave whose speech reflects his lack of formal education but whose thoughts reveal deep wisdom, loyalty, and humanity. He speaks in dialect and often with superstitious references, but his reasoning about family, friendship, and survival is sound. Jim thinks with both his heart and practical experience, showing remarkable patience and understanding."
    },
    "hank_morgan": {
        "name": "Hank Morgan (The Connecticut Yankee)",
        "description": "A 19th-century American mechanic transported to King Arthur's court who speaks with modern slang and technological confidence. He thinks like an engineer and entrepreneur, always looking for practical solutions and profit opportunities. His speech is peppered with American idioms that confound medieval listeners."
    },
    "puddnhead_wilson": {
        "name": "Pudd'nhead Wilson",
        "description": "A lawyer-philosopher who speaks in witty aphorisms and thinks in paradoxes. His calendar of sayings reveals a sharp, satirical mind that sees through human pretensions. He talks like a sage but is considered a fool by his neighbors, and his logical, methodical thinking ultimately solves the novel's central mystery."
    }
}

# Alternative list format
character_list = [
    {
        "name": "Huckleberry Finn",
        "description": "A rough-around-the-edges boy who speaks in colloquial dialect and thinks with honest, practical wisdom. He's skeptical of 'sivilized' society, often saying things like 'I reckon' and dropping his g's. His moral compass operates through lived experience rather than book learning, and he struggles between what society taught him and what his heart tells him is right."
    },
    {
        "name": "Tom Sawyer",
        "description": "An imaginative, mischievous boy who romanticizes everything through the lens of adventure books. He speaks with enthusiasm and grandiose language, always scheming elaborate plans when simple ones would do. Tom thinks like a showman, turning ordinary situations into theatrical productions, and believes strongly in doing things 'by the book' even when it's impractical."
    },
    {
        "name": "Jim",
        "description": "A escaped slave whose speech reflects his lack of formal education but whose thoughts reveal deep wisdom, loyalty, and humanity. He speaks in dialect and often with superstitious references, but his reasoning about family, friendship, and survival is sound. Jim thinks with both his heart and practical experience, showing remarkable patience and understanding."
    },
    {
        "name": "Hank Morgan (The Connecticut Yankee)",
        "description": "A 19th-century American mechanic transported to King Arthur's court who speaks with modern slang and technological confidence. He thinks like an engineer and entrepreneur, always looking for practical solutions and profit opportunities. His speech is peppered with American idioms that confound medieval listeners."
    },
    {
        "name": "Pudd'nhead Wilson",
        "description": "A lawyer-philosopher who speaks in witty aphorisms and thinks in paradoxes. His calendar of sayings reveals a sharp, satirical mind that sees through human pretensions. He talks like a sage but is considered a fool by his neighbors, and his logical, methodical thinking ultimately solves the novel's central mystery."
    }
]

if __name__ == "__main__":
    print("Mark Twain Characters")
    print("=" * 20)
    for character in character_list:
        print(f"\n{character['name']}:")
        print(f"  {character['description']}")