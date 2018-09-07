from class_Operation_Sets_Identification import RouteIdentification
from class_defining_edge_series import EdgeSeriesAndSequenceBlocks
from class_check_for_deletions import CorrectForDeletions

if __name__ == '__main__':
     filenameB = 'GenomeB_names_positions.txt'
     filenameA = 'GenomeA_names_positions.txt'

     generate_list_of_sequence_blocks = EdgeSeriesAndSequenceBlocks()
     sequence_blocks_B = generate_list_of_sequence_blocks.ListSequenceBlocks(filenameB)
     sequence_blocks_A = generate_list_of_sequence_blocks.ListSequenceBlocks(filenameA)

     find_large_indels = CorrectForDeletions()
     correct_for_deletions = find_large_indels.find_missing_blocks(sequence_blocks_A, sequence_blocks_B)

     sequence_blocks_B = correct_for_deletions[0]
     deleted_sequence_blocks = correct_for_deletions[1]

     correct_for_insertions = find_large_indels.find_inserted_blocks(sequence_blocks_A, sequence_blocks_B)

     sequence_blocks_B = correct_for_insertions[0]
     inserted_sequnce_blocks = correct_for_insertions[1]



     execute = RouteIdentification()
     route = []
     Paths = []
     level = 0
     level_1_counter = 0
     sequence_blocks = sequence_blocks_B
     Sets_of_operations = execute.Identify_Routes(sequence_blocks, route, Paths, level, level_1_counter)

     for i in range(len(Sets_of_operations)):
          print(Sets_of_operations[i])
