import catan


class Road:
    def __init__(self, index, coordinate_1, coordinate_2):
        self.index = index
        self.coordinates = {
            1: coordinate_1,
            2: coordinate_2
        }
        self.status = 'open'

    def set_status(self, status):
        self.status = 'status'

    def __str__(self):
        return_val = ''
        return_val += 'Road Number: {}\n'.format(
            self.index
        )
        coordinate_str = ''
        for key in self.coordinates:
            coordinate_str += 'Coordinate {}: {}\n'.format(
                key,
                self.coordinates[key]
            )
        return_val += coordinate_str
        return_val += 'Status: {}'.format(
            self.status
        )
        return return_val
