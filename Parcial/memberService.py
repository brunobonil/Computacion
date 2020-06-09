from repository import Repository


class MemberService():
    def add_member(self, member):
        ultKey = -1
        for key in Repository.membersList:
            ultKey = key
        ultKey = ultKey + 1
        Repository.membersList[ultKey] = member.__dict__
        return (ultKey)

    def update_member(self, legajo, member):
        existe = False
        for miembros in Repository.membersList:
            if miembros == legajo:
                existe = True
                break
        if existe:
            dicc = Repository.membersList
            dicc[legajo] = {'_name': member.name,
                            '_surname': member.surname,
                            '_age': member.age,
                            '_phone': member.phone}
        else:
            raise ValueError

    def delete_member(self, key):
        existe = False
        for miembros in Repository.membersList:
            if miembros == key:
                existe = True
                break
        if existe:
            del Repository.membersList[key]
        else:
            raise ValueError
