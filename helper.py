class RoleSelector:
    def __init__(self, number_of_members: int):
        print(number_of_members)
        print(type(number_of_members))
        self.number_of_members = number_of_members
        self.number_of_mafia = int(number_of_members*.3)
        self.number_of_doctor = number_of_members // 10
        self.number_of_sheriff = number_of_members // 10
        self.number_of_civil = int(self.number_of_members -
                                   self.number_of_sheriff -
                                   self.number_of_mafia -
                                   self.number_of_doctor)

    def to_dict(self):
        return {
            'number_of_members': self.number_of_members,
            'number_of_civil': self.number_of_civil,
            'number_of_mafia': self.number_of_mafia,
            'number_of_doctor': self.number_of_doctor,
            'number_of_sheriff': self.number_of_sheriff
        }
