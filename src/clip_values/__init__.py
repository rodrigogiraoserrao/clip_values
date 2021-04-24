class clip:
    def __init__(self, value):
        self._value = value
        self._bound = None

    def between_(self, bound):
        self._bound = bound
        return self

    def and_(self, bound):
        return min(max(bound, self._bound), max(self._value, min(bound, self._bound)))
