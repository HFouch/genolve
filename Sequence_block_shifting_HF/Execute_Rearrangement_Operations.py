if __name__ == "__main__":

    filename = '/home/18969577/Documents/Genolve/Shuffling/Sequence_block_rearrangements/GenomeB_names_positions'

    from class_Edge_Series_and_Sequence_Blocks import EdgeSeriesAndSequenceBlocks
    from class_Inversion_Identification import Inversion
    from class_Translocation_Identification import Translocation

    generate_list_of_sequence_blocks = EdgeSeriesAndSequenceBlocks()
    sequence_blocks = generate_list_of_sequence_blocks.ListSequenceBlocks(filename)

    generate_the_series_of_edges = EdgeSeriesAndSequenceBlocks()
    edge_series = generate_the_series_of_edges.GenerateEdgesSeries(sequence_blocks)
    working_edge_series = generate_the_series_of_edges.GenerateEdgesSeries(sequence_blocks)

    score = 0
    List_of_inversions = []
    List_of_translocations = []

    find_inversions = Inversion()
    Inversions = find_inversions.Locate_inversions(working_edge_series, score)
    working_edge_series = Inversions[0]
    score = Inversions[1]
    List_of_inversions = Inversions[2]

    find_translocations = Translocation()
    Translocations = find_translocations.Locate_translocations(working_edge_series, score)
    working_edge_series = Translocations[0]
    score = Translocations[1]
    List_of_translocations = Translocations[2]

    sequence_block_borders = []
    edges_with_compatible_sequence_blocks = []
    remove_non_viable_edges = EdgeSeriesAndSequenceBlocks()
    find_viable_edges = remove_non_viable_edges.RemoveNonViableEdges(edge_series, working_edge_series, sequence_blocks)

    edge_series = find_viable_edges[0]
    working_edge_series = find_viable_edges[1]
    sequence_block_borders = find_viable_edges[2]
    edges_with_compatible_sequence_blocks = find_viable_edges[3]


    print('SBs', edges_with_compatible_sequence_blocks)
    print('INVs', List_of_inversions)
    print('TRNs', List_of_translocations)