import json
from dataclasses import dataclass, field, make_dataclass

DynamicDataClass = make_dataclass("DynamicClass", [("name", str), ("value", int)])


@dataclass()
class DataClass:
    """
    frozen=True : data classes immutable (read-only)

    """
    __slots__ = ('x', 'y')
    #Reducing the memory footprint of dataclass instances

    attr1: str
    attr2: float = 0.0
    attr3: list = None
    attr4: list = field(default_factory=list)
    attr5: list = field(default_factory=lambda: [])

    def __post_init__(self):
        """
        perform additional processing after the object is initialized
        - customize how a field is initialized
        :return:
        """
        pass

    def __repr__(self):
        """
        customize the string representation
        :return:
        """

    def __str__(self):
        """

        :return:
        """
        pass

    def __eq__(self, other):
        """

        :param other:
        :return:
        """
        pass

    def __lt__(self, other):
        """

        :param other:
        :return:
        """
        pass





@dataclass
class UserProfile:
    username: str
    email: str


json_data = '{"username": "johndoe", "email": "john@example.com"}'
user_profile = UserProfile(**json.loads(json_data))
print(user_profile)  # Output: UserProfile(username='johndoe', email='john@example.com')
