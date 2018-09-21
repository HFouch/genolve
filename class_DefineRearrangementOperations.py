from class_RearrangementOperationExecution import RearrangementOperationExecution
from class_SequenceBlockAndEdgeSeriesIdentification import SequenceBlockAndEdgeSeriesIdentification


class DefineRearrangementOperations:

    def __init__(self):
        pass

    def __del__(self):
        pass

    #DEF: Identify all possible instances of inversions
    def inversion_identification(self, working_edge_series):
        edge_series = []
        edge_series.extend(working_edge_series)
        Inversion_operations = []


        # 1. iterate through the list of edge pairs.
        # 2. calculate the possible inversion partners for the current edge pair.
        # 3. determine whether an inversion partner is present in the list of edge pairs.
        # 4. if present, append the current edge pair and its partner to the list of Inversions
        for edge_pair in range(len(edge_series)):

            current_edge_pair = edge_series[edge_pair]
            edge1 = current_edge_pair[0]
            edge2 = current_edge_pair[1]
            orientation_edge1 = edge1/abs(edge1)
            orientation_edge2 = edge2/abs(edge2)


            #Calculation of inversion partner
            if orientation_edge1 > 0:
                compatible_edge_partner_1 = (abs(edge1) + 1) * orientation_edge1 * (-1)

            else:
                compatible_edge_partner_1 = (abs(edge1) - 1) * orientation_edge1 * (-1)


            if orientation_edge2 > 0:
                compatible_edge_partner_2 = (abs(edge2) - 1) * orientation_edge2 * (-1)

            else:
                compatible_edge_partner_2 = (abs(edge2) + 1) * orientation_edge2 * (-1)


            inversion_partner = (int(compatible_edge_partner_1), int(compatible_edge_partner_2))


            #Determination of whether the inversion partner is present in the the series of edge pairs
            if inversion_partner in edge_series:
                x = int(inversion_partner[0])
                y = int(inversion_partner[1])
                inversion_partner = (x,y)
                inversion_partner_position = edge_series.index(inversion_partner)
                edge_series[inversion_partner_position] = (1,1)

                Inversion_operations.append((current_edge_pair, inversion_partner))



            else:
                pass

        return Inversion_operations

    def translocation_identification(self, edge_series, sequence_blocks):
        Translocation_operations = []
        adjacent_translocations = []

        # 1. iterate through the list of edge pairs.
        # 2. for each edge calculate the compatible sequence block for the occurance of a translocation
        # 3. determine whether the translocation of the compatible sequence block to the edge pair is a valid operation
        # 4. if the operation is valid, append it to the list of Translocations

        for edge_pair in range(len(edge_series)):

            current_edge_pair = edge_series[edge_pair]

            edge1 = current_edge_pair[0]
            edge2 = current_edge_pair[1]
            orientation_edge1 = edge1 / abs(edge1)
            orientation_edge2 = edge2 / abs(edge2)


            #Calculation of compatible sequence block
            if orientation_edge1 > 0:
                compatible_sequence_block_1 = (abs(edge1) + 1) * orientation_edge1

            else:
                compatible_sequence_block_1 = (abs(edge1) - 1) * orientation_edge1

            if orientation_edge2 > 0:
                compatible_sequence_block_2 = (abs(edge2) - 1) * orientation_edge2
            else:
                compatible_sequence_block_2 = (abs(edge2) + 1) * orientation_edge2

            compatible_sequence_block = (int(compatible_sequence_block_1), int(compatible_sequence_block_2))




            #Determination of whether the translocation of the sequence block is a valid operations
            if compatible_sequence_block[0] in sequence_blocks and compatible_sequence_block[1] in sequence_blocks:
                position_block1 = sequence_blocks.index(compatible_sequence_block[0])
                position_block2 = sequence_blocks.index(compatible_sequence_block[1])
                position_edge1 = sequence_blocks.index(edge1)

                if position_block1 < position_block2 and position_edge1 not in range(position_block1, position_block2):
                    Translocation_operations.append((current_edge_pair, compatible_sequence_block))

                elif position_block1 == position_block2:
                    Translocation_operations.append((current_edge_pair, compatible_sequence_block))


                else:
                    pass
            else:
                pass



        return Translocation_operations

    def inverted_translocation_identification(self, edge_series, sequence_blocks):
        Inverted_Translocation_operations =[]

        # 1. iterate through the list of edge pairs.
        # 2. for each edge calculate the compatible sequence block for the occurance of an inverted translocation
        # 3. determine whether the inverted translocation of the compatible sequence block to the edge pair is a valid operation
        # 4. if the operation is valid, append it to the list of Inverted_translocations

        for edge_pair in range(len(edge_series)):
            current_edge_pair = edge_series[edge_pair]
            edge1 = current_edge_pair[0]
            edge2 = current_edge_pair[1]
            orientation_edge1 = edge1 / abs(edge1)
            orientation_edge2 = edge2 / abs(edge2)


            


            #Calculation of the compatible sequence block
            if orientation_edge1 > 0:
                compatible_sequence_block_1 = (abs(edge1) + 1) * orientation_edge1 * (-1)

            else:
                compatible_sequence_block_1 = (abs(edge1) - 1) * orientation_edge1 * (-1)

            if orientation_edge2 > 0:
                compatible_sequence_block_2 = (abs(edge2) - 1) * orientation_edge2 * (-1)
            else:
                compatible_sequence_block_2 = (abs(edge2) + 1) * orientation_edge2 * (-1)

            compatible_sequence_block = (int(compatible_sequence_block_2), int(compatible_sequence_block_1))


            #Determination of whether the inverted translocation of the compatible sequence block to the current edge pair is a valid operation
            if compatible_sequence_block[0] in sequence_blocks and compatible_sequence_block[1] in sequence_blocks:
                position_block1 = sequence_blocks.index(compatible_sequence_block[0])

                position_block2 = sequence_blocks.index(compatible_sequence_block[1])
                position_edge1 = sequence_blocks.index(edge1)

                if position_block1 < position_block2 and position_edge1 not in range(position_block1, position_block2):
                    Inverted_Translocation_operations.append((current_edge_pair, compatible_sequence_block))


                elif position_block1 == position_block2:
                    Inverted_Translocation_operations.append((current_edge_pair, compatible_sequence_block))
                                                             
                else:
                    pass
            else:
                pass


        return Inverted_Translocation_operations

    def removal_of_equivalent_translocations(self, Translocations, sequence_blocks):
        #For the removal of adjecent translocation operations, i.e. [1,2,3,7,8,4,5,6,9,10] the movement of block (7,8) to edge(6,9) is equivalent to that of block(4,6) to edge(3,7)
        i =0
        while i < len(Translocations):
            current_translocation = Translocations[i]

            j = 0
            while j < len(Translocations):
                other_translocation = Translocations[j]

                if sequence_blocks.index(current_translocation[1][1]) == sequence_blocks.index(
                    other_translocation[1][0]) - 1 and sequence_blocks.index(current_translocation[1][0]) == sequence_blocks.index(
                    other_translocation[0][1]):

                    Translocations.remove(other_translocation)

                else:
                    pass
                j += 1
            i += 1


        return Translocations




    def final_inversion_search(self, sequence_blocks, other_inversions):
        i = 0
        while i < len(sequence_blocks):
            if sequence_blocks[i] < 0:
                current = sequence_blocks[i]
                find_block = DefineRearrangementOperations()
                perform_operation = find_block.invert_block(sequence_blocks, i, current)

                sequence_blocks = perform_operation[0]
                operation = perform_operation[1]
                i = perform_operation[2]
                other_inversions.append(operation)


            else:
                i += 1

        return (sequence_blocks, other_inversions)


    def invert_block(self, sequence_blocks, i, current):
        perform_operation = RearrangementOperationExecution()
        while sequence_blocks[i] < 0:
            i += 1
        else:
            edge_1 = (sequence_blocks[sequence_blocks.index(current)-1], current)
            edge_2 = (sequence_blocks[i-1], sequence_blocks[i])
            inversion = (edge_1, edge_2)
            invert = perform_operation.excecute_inversion(inversion, sequence_blocks)
            sequence_blocks = invert [0]
            inversion_position = invert[1]
            operation = ('INV', inversion, inversion_position)
        return (sequence_blocks, operation, i)


    def final_translocation_search(self, sequence_blocks, blocks, list_of_final_translocations):

        generate_the_series_of_edges = SequenceBlockAndEdgeSeriesIdentification()
        find_translocations = DefineRearrangementOperations()
        edge_series = generate_the_series_of_edges.generate_edge_series(sequence_blocks)



        if len(edge_series) == 0:

            return sequence_blocks, list_of_final_translocations


        while len(edge_series) != 0:
            new_translocations = []

            while len(new_translocations) == 0:

                i = 0

                while i < len(edge_series):

                    current_edge = edge_series[i]
                    search_for_translocations = find_translocations.translocation_search(current_edge, sequence_blocks,
                                                                                         blocks)

                    new_sequence_blocks = search_for_translocations[0]
                    blocks = search_for_translocations[1]
                    new_translocations = search_for_translocations[2]

                    if len(new_translocations) == 0:
                        i += 1

                    else:
                        list_of_final_translocations.append(new_translocations)
                        sequence_blocks = new_sequence_blocks
                        edge_series = generate_the_series_of_edges.generate_edge_series(sequence_blocks)


                        return find_translocations.final_translocation_search(sequence_blocks, blocks,
                                                                       list_of_final_translocations)

                else:

                    block_removal = find_translocations.perform_block_removal(edge_series, sequence_blocks, blocks)
                    edge_series = block_removal[0]
                    sequence_blocks = block_removal[1]
                    blocks = block_removal[2]

                    return find_translocations.final_translocation_search( sequence_blocks, blocks,
                                                                   list_of_final_translocations)


    def translocation_search(self, current_edge_pair, sequence_blocks, blocks):

        execute_translocation = RearrangementOperationExecution()
        identified_translocation = []
        blocks_list = []
        for i in range(len(blocks)):
            blocks_list.append((blocks[i][0], blocks[i][-1]))

        i = 0

        edge1 = current_edge_pair[0]
        edge2 = current_edge_pair[1]

        compatible_sequence_block_1 = (abs(edge1) + 1)
        compatible_sequence_block_2 = (abs(edge2) - 1)

        compatible_sequence_block = (int(compatible_sequence_block_1), int(compatible_sequence_block_2))


        if compatible_sequence_block[0] in sequence_blocks and compatible_sequence_block[1] in sequence_blocks:
            position_block1 = sequence_blocks.index(compatible_sequence_block[0])
            position_block2 = sequence_blocks.index(compatible_sequence_block[1])
            position_edge1 = sequence_blocks.index(edge1)

            if position_block1 < position_block2 and position_edge1 not in range(position_block1,
                                                                                 position_block2):
                translocation = (current_edge_pair, compatible_sequence_block)
                add_to_list = ('TRN', current_edge_pair, compatible_sequence_block)
                identified_translocation.append(add_to_list)
                execute = execute_translocation.excecute_translocation(translocation, sequence_blocks)
                sequence_blocks = execute[0]



            elif position_block1 == position_block2:

                translocation = (current_edge_pair, compatible_sequence_block)
                add_to_list = ('TRN', current_edge_pair, compatible_sequence_block)
                identified_translocation.append(add_to_list)
                execute = execute_translocation.excecute_translocation(translocation, sequence_blocks)
                sequence_blocks = execute[0]



        elif compatible_sequence_block in blocks_list:
            block_position = blocks_list.index(compatible_sequence_block)

            new_sequence_blocks = sequence_blocks[:sequence_blocks.index(current_edge_pair[0]) + 1] + blocks[
                block_position] + sequence_blocks[sequence_blocks.index(current_edge_pair[0]) + 1:]
            sequence_blocks = new_sequence_blocks

            add_to_list = ('TRN', current_edge_pair, (blocks[i][0], blocks[i][-1]))
            identified_translocation.append(add_to_list)
            blocks.remove(blocks[i])

        return sequence_blocks, blocks, identified_translocation


    def perform_block_removal(self, edge_series, sequence_blocks, blocks):

        block_to_remove = sequence_blocks[
                          sequence_blocks.index(edge_series[0][1]):sequence_blocks.index(edge_series[1][0]) + 1]

        blocks.append(block_to_remove)
        for i in range(len(block_to_remove)):
            sequence_blocks.remove(block_to_remove[i])

        generate_the_series_of_edges = SequenceBlockAndEdgeSeriesIdentification()
        edge_series = generate_the_series_of_edges.generate_edge_series(sequence_blocks)

        return edge_series, sequence_blocks, blocks





