import catan


class CatanTile:
    # Initialize the Catan Board with all the options for resources, numbers to be rolled,
    # settlements/roads, port options
    def __init__(self, index, resource, value):
        self.index = index
        self.resource = resource
        self.value = value
        self.coordinates = []
        self.road_slots = []

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def set_road_slots(self, road_slots):
        self.road_slots = road_slots

    def __str__(self):
        return_val = ''
        return_val += 'Tile Number: {}\n'.format(
            self.index
        )
        return_val += 'Resource: {}\n'.format(
            catan.RESOURCE_NAMES[self.resource]
        )
        return_val += 'Value: {}\n'.format(
            self.value
        )

        return return_val
