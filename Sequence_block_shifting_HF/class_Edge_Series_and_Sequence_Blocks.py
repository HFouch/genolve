import numpy as np

class EdgeSeriesAndSequenceBlocks:

    def __init__(self):
        pass

    def __del__(self):
        pass

    def ListSequenceBlocks(self, filename):
        names_and_positions_of_sequence_blocks = np.loadtxt(filename, delimiter='\t', unpack=True, dtype=object)
        sequence_block_names = names_and_positions_of_sequence_blocks[0, :]
        sequence_blocks = []
        for i in range(0, len(sequence_block_names)):
            sequence_blocks.append(sequence_block_names[i])

        return sequence_blocks


    def GenerateEdgesSeries(self, sequence_blocks):

        edge_series = []

        # Generation of the list of non-consecutive edges
        for i in range(0, len(sequence_blocks) - 1):
            if int(sequence_blocks[i + 1]) - int(sequence_blocks[i]) == 1:
                pass
            elif int(sequence_blocks[i + 1]) - int(sequence_blocks[i]) == -1:
                pass
            else:
                edge = (int(sequence_blocks[i]), int(sequence_blocks[i + 1]))
                edge_series.append(edge)

        return edge_series


    def RemoveNonViableEdges(self, edge_series, working_edge_series, sequence_blocks):
        edges_to_be_removed = []
        sequence_block_borders = []
        edge_with_compatible_sequence_block = []
        #Loop for every edge in edge list
        for i in range(0, len(working_edge_series)):
            edge_number = int(i)
            current_edge = working_edge_series[edge_number]

            #Defining upper and lower edges
            lower_edge = min(current_edge[0], current_edge[1])
            upper_edge = max(current_edge[0], current_edge[1])


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
                    sequence_block_borders.append((lower_adjacent_edge, upper_adjacent_edge))
                    edge_with_compatible_sequence_block.append((current_edge,(lower_adjacent_edge, upper_adjacent_edge)))
                    pass

            else:
                if lower_edge_position in range(upper_adjacent_edge_position, lower_adjacent_edge_position):
                    edges_to_be_removed.append(current_edge)
                else:
                    sequence_block_borders.append((upper_adjacent_edge, lower_adjacent_edge))
                    edge_with_compatible_sequence_block.append((current_edge,(upper_adjacent_edge, lower_adjacent_edge)))
                    pass

        #Removal of those edges that fall within their compatible sequence blocks from the list of edges that will subsequently be used
        for i in range(0, len(edges_to_be_removed)):
            working_edge_series.remove(edges_to_be_removed[i])
            edge_series.remove(edges_to_be_removed[i])


        return edge_series, working_edge_series, sequence_block_borders, edge_with_compatible_sequence_block


