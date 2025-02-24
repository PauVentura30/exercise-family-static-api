"""
He verificado que funciona el codigo con postman, no se si esta bien haberlo verificado con eso pero asi lo hice y funciona.
"""

#la clase familystructure para especificar y hacer los endpoints
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    #genera id a los miembros añadidos, no tocar
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        if "id" not in member:  # Solo genera ID si no se ha dado uno
            member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        member["lucky_numbers"] = list(member.get("lucky_numbers", set()))
        self._members.append(member)
        return member


    def delete_member(self, id):
        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                self._members.pop(position)
                return {"done": True}  # Enviar un JSON con 'done: true'
        return {"error": "Member not found"}, 404

            
    def get_member(self, id):
        for member in self._members:
            if member["id"] == int(id):
                return member
        return {"error": "Member not found"}, 404  # Enviar error si el miembro no existe


    #devuelve la lista con todos los miembros
    def get_all_members(self):
        return self._members