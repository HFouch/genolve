'''
Here a text file containing the sequence block names and positions of genome B serves as the input.
A list containing only the sequence block names is generated.
The series of viable edges is constructed
The sequence block compatible to each of the viable edges is moved individually to generate the same amount of intermediate genomes as there was viable edges
The sequence blocks of each of these intermediate genomes are written to text files (just for confirmation that what needs to happen does happen)
A list containing tuples of (the intermediate genome number, the number of edges generated from it) is created
Only those genomes with a minimum number of edges are retained (i.e. thae rest are excluded from further analysis)

Note that it has been established that excluding intermediate genomes or evolutionary paths based only on the number of edges is not feasible.
'''



import numpy as np
from class_Sequence_Block_Rearrangments import EdgeSeries
from class_Sequence_Block_Rearrangments import MoveSequenceBlock
from class_Sequence_Block_Rearrangments import WriteArrayToTextFile
from class_Check_edge_list import CheckEdgeList

if __name__ == "__main__":

    filenameB = '/home/18969577/Documents/Genolve/Shuffling/Sequence_block_rearrangements/GenomeB_names_positions'

    #Generation of list of sequence blocks
    names_and_positions_of_sequence_blocks = np.loadtxt(filenameB, delimiter='\t', unpack=True, dtype=object)
    sequence_block_names = names_and_positions_of_sequence_blocks[0, :]
    sequence_blocks = []
    for i in range(0, len(sequence_block_names)):
        sequence_blocks.append(sequence_block_names[i])

    #Generation of series of edges
    generate_edge_list = EdgeSeries()
    edge_list = generate_edge_list.GenerateEdgesSeries(filenameB)

    # Removal of edges that falls within their compatible sequence blocks
    remove_nonviable_edge = CheckEdgeList()
    exclude_edge = remove_nonviable_edge.RemoveNonViableEdges(edge_list, sequence_blocks)
    edge_list = exclude_edge

    #Generation of new edge list after performing the applicable rearrangments
    rearrangement_operations_performed = []
    new_edge_series = []
    for i in range(0, len(edge_list)):
        edge_number = int(i)
        current_edge = edge_list[edge_number]

        #Execution of all possible rearrangment operations
        moving_sequence_blocks = MoveSequenceBlock()
        execute_sequence_block_shift = moving_sequence_blocks.MoveBlock(filenameB, current_edge)
        #Edge list generated from new intermediate genome
        new_edge_list = generate_edge_list.GenerateNewEdgesSeries(execute_sequence_block_shift)
        #List containing the list of edges for all intermediate genome possiblities
        new_edge_series.append(new_edge_list)

        #Generation of output files
        path, *remainder = filenameB.rpartition('/')
        output_filename = path + '/' + 'Sequence_blocks_moved_EdgeNumber_' + str(edge_number + 1) + '.txt'
        output_file = WriteArrayToTextFile()
        output_file.WriteToTxt(execute_sequence_block_shift, output_filename)

    #Generation of list containing, for each intermediate genome, the genome number and number of edges
    len_new_edge_lists = []
    list_of_edge_lengths = []
    for i in range(0, len(new_edge_series)):
        edge_list_number = int(i)
        edge_list_length = len(new_edge_series[edge_list_number])
        len_new_edge_lists.append((edge_list_number, edge_list_length))
        list_of_edge_lengths.append(edge_list_length)


    #Exclution of paths, with an edge number below the minimum edge number, from further
    paths_to_exclude = []
    min_edge_number = min(list_of_edge_lengths) + 1


    for i in range(0, len(len_new_edge_lists)):
        if len_new_edge_lists[i][1] > (int(min_edge_number)):
            paths_to_exclude.append(edge_list[len_new_edge_lists[i][0]])
        else:
            pass

    for i in range (0, len(paths_to_exclude)):
        edge_list.remove(paths_to_exclude[i])

    print('New sequence block lists written to ', path)
