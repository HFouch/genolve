
class Inversion:
    def __init__(self):
        pass
    def __del__(self):
        pass

    def Locate_inversions(self, working_edge_series, score):
        Inversions = []
        edge_position = 0
        number_of_edges_considered = 0

        while number_of_edges_considered < len(working_edge_series):
            current_edge = working_edge_series[edge_position]

            find_inversion = Inversion()
            current_inversion = find_inversion.partner(current_edge, working_edge_series)

            if current_inversion != 0:
                Inversions.append(current_inversion)
                working_edge_series.remove(current_inversion[0])
                working_edge_series.remove(current_inversion[1])
                find_a_better_name = 0

            else:
                find_a_better_name = 1
                pass

            edge_position = edge_position + find_a_better_name
            number_of_edges_considered = number_of_edges_considered + find_a_better_name

        if len(Inversions) != 0:
            score = score + len(Inversions)
            return working_edge_series, score, Inversions

        else:
            return 0


    def partner(self, current_edge, working_edge_series):

        if (current_edge[0]+1, current_edge[1]+1) in working_edge_series:
            inversion_partener = (current_edge[0]+1, current_edge[1]+1)
            return (current_edge, inversion_partener)

        elif (current_edge[0]-1, current_edge[1]-1) in working_edge_series:
            inversion_partener = (current_edge[0]-1, current_edge[1]-1)
            return (current_edge, inversion_partener)

        else:
            return 0


