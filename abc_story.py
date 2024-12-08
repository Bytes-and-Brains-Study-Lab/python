from abc import ABC, abstractmethod

class StoryPart(ABC):
    @abstractmethod
    def get_story_part(self) -> str:
        """
        This method should return a string containing the part of the story.
        """
        pass