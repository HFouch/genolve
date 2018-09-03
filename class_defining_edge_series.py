import numpy as np

class EdgeSeriesAndSequenceBlocks:

    def __init__(self):
        pass

    def __del__(self):
        pass

    #DEF: use the tab delimited input file to generate a list of sequence blocks
    def ListSequenceBlocks(self, filename):
        names_and_positions_of_sequence_blocks = np.loadtxt(filename, delimiter='\t', unpack=True, dtype=object)
        sequence_block_names = names_and_positions_of_sequence_blocks[0, :]
        sequence_blocks = []
        for i in range(0, len(sequence_block_names)):
            sequence_blocks.append(int(sequence_block_names[i]))

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