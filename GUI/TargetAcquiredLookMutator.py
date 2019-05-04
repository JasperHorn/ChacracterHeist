
from CharacterObserver import CharacterObserver

class TargetAcquiredLookMutator(CharacterObserver):
    def __init__(self, looksRepository, visualizer, character,
                 objectType, newSymbol, newStyle):
        self.looksRepository = looksRepository
        self.visualizer = visualizer
        self.objectType = objectType
        self.newSymbol = newSymbol
        self.newStyle = newStyle

        character.subscribe(self)

    def characterGotTarget(self):
        self.looksRepository.defineObjectLook(self.objectType, self.newSymbol,
                                              self.newStyle)
        self.visualizer.redraw(self.objectType)
