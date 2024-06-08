import random

# Define lists of story elements
characters = ["Alice", "Bob", "Charlie", "David", "Eve"]
locations = ["a forest", "a castle", "a beach", "a spaceship", "a city"]
actions = ["discovered a hidden treasure", "fell in love", "went on an adventure", "solved a mystery"]
outcomes = ["and they lived happily ever after.", "but tragedy struck.", "and a new chapter began."]

# Function to generate a random paragraph
def generate_random_paragraph():
    paragraph = ""
    word_count = 0

    while word_count < 200:
        character = random.choice(characters)
        location = random.choice(locations)
        action = random.choice(actions)
        outcome = random.choice(outcomes)

        sentence = f"{character} was in {location} when they {action}. {outcome} "
        word_count += len(sentence.split())
        paragraph += sentence

    return paragraph

# Generate and print a random story with at least 200 words
random_story = generate_random_paragraph()
print(random_story)
