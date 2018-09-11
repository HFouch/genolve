class RearrangementOperationIdentification():

    def __init__(self):
        pass

    def __del__(self):
        pass

    #DEF: Identify all possible instances of inversions
    def InversionIdentification(self, working_edge_series):
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

    def TranslocationIdentification(self, edge_series, sequence_blocks):
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

    def InvertedTranslocationIdentification(self, edge_series, sequence_blocks):
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

    def remove_equivalent_operations(self, Translocations, sequence_blocks):
        list_of_translocations = []
        list_of_translocations.extend(Translocations)

        i =0
        while i < len(Translocations):
            current_translocation = Translocations[i]

            j = 0
            while j < len(Translocations):
                other_translocation = Translocations[j]

                if sequence_blocks.index(current_translocation[1][1]) == sequence_blocks.index(
                    other_translocation[1][0]) - 1 :
                    Translocations.remove(other_translocation)

                else:
                    pass
                j += 1
            i += 1


        return Translocations



