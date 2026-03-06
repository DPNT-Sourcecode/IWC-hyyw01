class HelloSolution:
    # friend_name = unicode string

    def _validate_name(self, name: str) -> None:
        if not name:
            raise ValueError("Name can not be empty")

    def hello(self, friend_name):
        self._validate_name(name=friend_name)
        return "I don't know what the message should be"

