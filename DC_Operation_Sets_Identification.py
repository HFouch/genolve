from class_RouteIdentification import RouteIdentification
from class_SequenceBlockAndEdgeSeriesIdentification import SequenceBlockAndEdgeSeriesIdentification
from class_CorrectForInsertionsAndDeletions import CorrectForDeletions
import sys

recursion_limit = 4000
sys.setrecursionlimit(recursion_limit)


rec_limit = sys.getrecursionlimit()


if __name__ == '__main__':

     filenameB = 'genomeB.txt'
     filenameA = 'genomeA.txt'

     generate_list_of_sequence_blocks = SequenceBlockAndEdgeSeriesIdentification()
     sequence_blocks_B = generate_list_of_sequence_blocks.list_sequence_blocks(filenameB)
     sequence_blocks_A = generate_list_of_sequence_blocks.list_sequence_blocks(filenameA)

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
     Completely_transformed = []
     number_of_final_inversions = 0

     sequence_blocks = sequence_blocks_B

     print('Sequence blocks:  ', sequence_blocks)

     Sets_of_operations = execute.identify_routes(sequence_blocks, route, Paths, level)



    # shortest = Sets_of_operations[0]
     print()
     print()
     print()
     print('          PATHS')
     print()

     for i in range(len(Sets_of_operations)):
          if 'FINAL_INVERSIONS' in Sets_of_operations[i]:
               Sets_of_operations[i].remove('FINAL_INVERSIONS')
          print(Sets_of_operations[i])
          print()
          #current = Sets_of_operations[i]
          #if len(current) < len(shortest):
           #    shortest = current
            #   pass
         # else:
          #     pass

     #print(shortest)
     #print(len(shortest))
