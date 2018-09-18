class CorrectForDeletions():

    def __init__(self):
        pass

    def __del__(self):
        pass

    def find_missing_blocks(self, sequence_blocks_A, sequence_blocks_B):

        missing_sequence_blocks=[]
        new_sequence_blocks = []
        new_sequence_blocks.append(sequence_blocks_B)

        for i in range(len(sequence_blocks_A)):
            current_block = sequence_blocks_A[(len(sequence_blocks_A)-1-i)]

            if current_block in sequence_blocks_B:

                pass

            elif current_block*(-1) in sequence_blocks_B:

                pass

            else:

                if (current_block + 1) in sequence_blocks_B:

                    sequence_blocks_B.insert((sequence_blocks_B.index(current_block+1)), current_block)
                    missing_sequence_blocks.append(current_block)

                elif ((current_block+1)*-1) in sequence_blocks_B:
                    sequence_blocks_B.insert((sequence_blocks_B.index((current_block+1)*-1)+1), current_block*-1)
                    missing_sequence_blocks.append(current_block*-1)

                pass


        return sequence_blocks_B, missing_sequence_blocks


    def find_inserted_blocks(self, sequence_blocks_A, sequence_blocks_B):

        inserted_sequence_blocks = []

        for i in range(len(sequence_blocks_B)):
            if abs(sequence_blocks_B[i]) not in sequence_blocks_A:
                inserted_sequence_blocks.append(sequence_blocks_B[i])
                pass
            else:
                pass

        for i in range(len(inserted_sequence_blocks)):
            sequence_blocks_B.remove(inserted_sequence_blocks[i])

        return sequence_blocks_B, inserted_sequence_blocks