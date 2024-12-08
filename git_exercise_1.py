import os
import importlib.util
from abc_story import StoryPart

def load_story_parts(directory="answers"):
    """
    Dynamically load story parts from Python files in the given directory.
    Only files named 'story_part_x.py' (where x is a number) will be processed.
    """

    story_parts = []

    for filename in os.listdir(directory):
        if filename.startswith("story_part_") and filename.endswith(".py"):
            file_path = os.path.join(directory, filename)
            module_name = filename[:-3]  # Strip '.py' extension

            # Dynamically load the module
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Find classes inheriting from StoryPart
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if (
                    isinstance(attribute, type)
                    and issubclass(attribute, StoryPart)
                    and attribute is not StoryPart
                ):
                    # Instantiate and add the story part
                    instance = attribute()
                    story_parts.append(instance.get_story_part())

    return story_parts

def main():
    directory = "answers"
    if not os.path.exists(directory):
        print(f"Directory '{directory}' not found. Please create it and add story parts.")
        return

    # Load story parts
    story_parts = load_story_parts(directory)
    if not story_parts:
        print("No valid story parts found. Please ensure files are named 'story-part-x.py' and contain valid classes.")
        return

    # Print the full story
    print("Here is the assembled story:\n")
    print("\n".join(story_parts))

if __name__ == "__main__":
    main()

import os
