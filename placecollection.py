from place import Place


class PlaceCollection:
    def __init__(self):
        """
            This function is to initialize an empty list for Place object
        """
        self.places = []

    def get_places(self,name):
        """
            This function used the method to return a selected single place object by user.
        """
        for place in self.places:
            if place[0].name == name:
                return place[0]
