from abc_story import StoryPart

class StoryStart(StoryPart):

    def get_story_part(self) -> str:
        return "Once upon a time in a distant galaxy..."
