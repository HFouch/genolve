class Translocation:

    def __init__(self):
        pass

    def __del__(self):
        pass

    def Locate_translocations(self, working_edge_series, score):
        Translocations = []
        edge_position = 0
        number_of_edges_considered = 0


        while number_of_edges_considered < len(working_edge_series):
            current_edge = working_edge_series[edge_position]

            find_translocation = Translocation()
            current_translocation = find_translocation.partner(current_edge, working_edge_series)

            if current_translocation != 0:

                Translocations.append(current_translocation)
                working_edge_series.remove(current_translocation[0])
                working_edge_series.remove(current_translocation[1])
                working_edge_series.remove(current_translocation[2])
                find_a_better_name = 0


            else:
                find_a_better_name = 1

                pass

            edge_position = edge_position + find_a_better_name
            number_of_edges_considered = number_of_edges_considered + find_a_better_name

        if len(Translocations) != 0:
            score = score + len(Translocations)
            return working_edge_series, score, Translocations

        else:
            return 0



    def partner(self, current_edge, working_edge_series):
        translocation_partner = 0
        for i in range (0, len(working_edge_series)):
            if working_edge_series[i][1] == current_edge[0]+1:
                translocation_partner = working_edge_series[i]
                break
            elif working_edge_series[i][1] == current_edge[0]-1:
                translocation_partner = working_edge_series[i]
                break
            else:
                pass
        if translocation_partner != 0:
            find_translocation = Translocation()
            current_translocation = find_translocation.position(current_edge, translocation_partner, working_edge_series)
            if current_translocation != 0:
                return current_translocation
            else:
                return 0
        else:
            return 0


    def position(self, current_edge, translocation_partner, working_edge_series):

        min_edge = min(current_edge[1], translocation_partner[0])
        max_edge = max(current_edge[1], translocation_partner[0])

        if (min_edge-1, max_edge+1) in working_edge_series:
            translocation_position = (min_edge-1, max_edge+1)
            return current_edge, translocation_partner, translocation_position

        else:
            return 0
