
class Place:
    def __init__(self, name, country, priority, status):
        """
            Set the name, name, priority and status of each item to self.**** on initialisation
        """
        self.name = name
        self.country = country
        self.priority = priority
        self.status = status

    def mark_song(self, status):
        """
            Used to mark the song status
        """
        self.status = status
