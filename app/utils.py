class Status:

    def __init__(self):
        self._school_list = None
        self._recruit = None

    @property
    def school_list(self):
        return self._school_list

    @school_list.setter
    def school_list(self, value):
        self._school_list = value

    @property
    def recruit(self):
        return self._recruit

    @recruit.setter
    def recruit(self, value):
        self._recruit = value
