class RearrangementOperationExecution():
    def __init__(self):
        pass
    def __del__(self):
        pass

    def execute_operations(self, current_operation, Inversions, Translocations, Inverted_translocations, sequence_blocks ):

        excecute_operation = RearrangementOperationExecution()

        if current_operation in Inversions:
            classification = 'Inv'
            excecute_inversion = excecute_operation.excecute_inversion(current_operation, sequence_blocks)
            new_sequence_blocks = excecute_inversion[0]
            inversion_position = excecute_inversion[1]
            operation = (classification, current_operation, inversion_position)



        elif current_operation in Translocations:
            classification = 'Trn'
            excecute_translocation = excecute_operation.excecute_translocation(current_operation,
                                                                               sequence_blocks)
            new_sequence_blocks = excecute_translocation[0]
            translocation_position = excecute_translocation[1]
            operation = (classification, current_operation, translocation_position)



        elif current_operation in Inverted_translocations:
            classification = 'Inv_trn'
            excecute_inverted_translocation = excecute_operation.excecute_inverted_translocation(
                current_operation,
                sequence_blocks)
            new_sequence_blocks = excecute_inverted_translocation[0]
            inverted_translocation_position = excecute_inverted_translocation[1]
            operation = (classification, current_operation, inverted_translocation_position)




        return (new_sequence_blocks, operation)


    def excecute_inversion(self, inversion, sequence_blocks):

        #temp = the segment of sequence block to be inverted
        temp = sequence_blocks[sequence_blocks.index(inversion[0][1]):sequence_blocks.index(inversion[1][0])+1]

        inverted_sequence = []

        #the determination of the inversion position -  (for the purpose of having the information available when creating the VCF output)
        inversion_position = ((sequence_blocks.index(inversion[0][1]), sequence_blocks.index(inversion[1][0])+1))
        #inversion_position = (position of left-most sequence block of the inverted segment, position of the right-most sequence block of the inverted segment)

        for i in range(len(temp)):
            current_sequence_block = temp[i]*(-1)
            inverted_sequence.append(current_sequence_block)

        new_sequence_blocks = sequence_blocks[:sequence_blocks.index(inversion[0][0])+1] + inverted_sequence[::-1] + sequence_blocks[sequence_blocks.index(inversion[1][1]):]

        return new_sequence_blocks, inversion_position

    def excecute_translocation(self, translocation, sequence_blocks):


        #temp = the segment of sequence blocks to be translocated
        temp = sequence_blocks[sequence_blocks.index(translocation[1][0]):sequence_blocks.index(translocation[1][1])+1]

        #temp_sequence_blocks = the list of sequence blocks with the segment to be translocated removed
        temp_sequence_blocks = sequence_blocks[:sequence_blocks.index(translocation[1][0])] + sequence_blocks[sequence_blocks.index(translocation[1][1])+1:]

        new_sequence_blocks = temp_sequence_blocks[:temp_sequence_blocks.index(translocation[0][0])+1] + temp[::] + temp_sequence_blocks[temp_sequence_blocks.index(translocation[0][1]):]

        # the determination of the translocation position (for the purpose of having the information available when creating the VCF output)
        translocation_position = ((sequence_blocks.index(translocation[1][0]),sequence_blocks.index(translocation[1][1])+1),sequence_blocks.index(translocation[0][0]))
        # inversion_position = ((position of left-most sequence block of the translocated segment, position of the right-most sequence block of the translocated segment), edge pair to which the sequence block is translocated)


        return new_sequence_blocks, translocation_position

    def excecute_inverted_translocation(self, inverted_translocation, sequence_blocks):

        #temp = segement of sequence blocks to be inverted and tranlocated
        temp = sequence_blocks[sequence_blocks.index(inverted_translocation[1][0]):sequence_blocks.index(inverted_translocation[1][1])+1]

        inverted_sequence = []

        for i in range(len(temp)):
            current_sequence_block = temp[i]*(-1)
            inverted_sequence.append(current_sequence_block)

        # temp_sequence_blocks = the list of sequence blocks with the segment to be inverted and translocated removed
        temp_sequence_blocks = sequence_blocks[:sequence_blocks.index(inverted_translocation[1][0])] + sequence_blocks[sequence_blocks.index(inverted_translocation[1][1])+1:]

        new_sequence_blocks  = temp_sequence_blocks[:temp_sequence_blocks.index(inverted_translocation[0][0])+1] +inverted_sequence[::-1] + temp_sequence_blocks[temp_sequence_blocks.index(inverted_translocation[0][1]):]

        # the determination of the inverted translocation position (for the purpose of having the information available when creating the VCF output)
        inverted_translocation_position = ((sequence_blocks.index(inverted_translocation[1][0]),sequence_blocks.index(inverted_translocation[1][1])+1),sequence_blocks.index(inverted_translocation[0][0] ))
        # inversion_position = ((position of left-most sequence block of the translocated segment, position of the right-most sequence block of the translocated segment), edge pair to which the sequence block is translocated after inversion)

        return new_sequence_blocks, inverted_translocation_position

