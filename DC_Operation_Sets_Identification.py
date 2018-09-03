from class_Operation_Sets_Identification_PLAY import RouteIdentification
from class_defining_edge_series import EdgeSeriesAndSequenceBlocks

if __name__ == '__main__':
     filename = 'GenomeB_names_positions.txt'

     generate_list_of_sequence_blocks = EdgeSeriesAndSequenceBlocks()
     sequence_blocks = generate_list_of_sequence_blocks.ListSequenceBlocks(filename)

     excecute = RouteIdentification()
     route = []
     Paths = []
     excecute.Identify_Routes(sequence_blocks, route, Paths)
