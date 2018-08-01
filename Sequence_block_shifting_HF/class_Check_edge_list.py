class CheckEdgeList:
    def __init__(self):
        pass
    def __del__(self):
        pass

    def RemoveNonViableEdges(self, list_of_edges, sequence_blocks):
        edge_list = list_of_edges
        edges_to_be_removed = []

        #Loop for every edge in edge list
        for i in range(0, len(edge_list)):
            edge_number = int(i)
            current_edge = edge_list[edge_number]

            #Defining upper and lower edges
            if current_edge[0] > current_edge[1]:
                lower_edge = current_edge[1]
                upper_edge = current_edge[0]
            else:
                lower_edge = current_edge[0]
                upper_edge = current_edge[1]

            lower_edge_position = sequence_blocks.index(str(lower_edge))
            upper_edge_position = sequence_blocks.index(str(upper_edge))

            lower_adjacent_edge = int(lower_edge) + 1
            lower_adjacent_edge_position = sequence_blocks.index(str(lower_adjacent_edge))

            upper_adjacent_edge = int(upper_edge) - 1
            upper_adjacent_edge_position = sequence_blocks.index(str(upper_adjacent_edge))


            #Generation of list of edges that fall within their compatible sequence blocks
            if lower_adjacent_edge_position < upper_adjacent_edge_position:
                if lower_edge_position in range(lower_adjacent_edge_position, upper_adjacent_edge_position):
                   edges_to_be_removed.append(current_edge)

                else:
                    pass

            else:
                if lower_edge_position in range(upper_adjacent_edge_position, lower_adjacent_edge_position):
                    edges_to_be_removed.append(current_edge)
                else:
                    pass

        #Removal of those edges that fall within their compatible sequence blocks from the list of edges that will subsequently be used
        for i in range(0, len(edges_to_be_removed)):
            edge_list.remove(edges_to_be_removed[i])


        return edge_list
