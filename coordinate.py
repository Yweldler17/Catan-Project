

class Intersection:
    def __init__(self, intersection_index, status):
        self.intersection_index = intersection_index
        self.status = status

    def __str__(self):
        return_val = ''
        return_val += 'Coordinate Code: {}\n'.format(
            self.intersection_index
        )
        return_val += 'Status: {}'.format(
            self.status
        )

        return return_val
