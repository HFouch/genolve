from class_defining_rearrangment_operations import RearrangementOperationIdentification
from class_execute_rearrangement_operations import RearrangementOperationExcecution
from class_defining_edge_series import EdgeSeriesAndSequenceBlocks


class RouteIdentification:


    is_last_operation = 0

    def __init__(self):
        pass

    def __del__(self):
        pass

    def Identify_Routes(self, sequence_blocks, route, Paths, level, level_1_counter):


        generate_the_series_of_edges = EdgeSeriesAndSequenceBlocks()
        edge_series = generate_the_series_of_edges.GenerateEdgesSeries(sequence_blocks)

        find_rearrangement_operations = RearrangementOperationIdentification()
        Inversions = find_rearrangement_operations.InversionIdentification(edge_series)
        Raw_Translocations = find_rearrangement_operations.TranslocationIdentification(edge_series, sequence_blocks)
        Translocations = find_rearrangement_operations.remove_equivalent_operations(Raw_Translocations)

        Inverted_translocations = find_rearrangement_operations.InvertedTranslocationIdentification(edge_series,
                                                                                                    sequence_blocks)



        Operations = []
        Operations.extend(Inversions)
        Operations.extend(Translocations)
        Operations.extend(Inverted_translocations)


        if level == 1:
            Operations.append('Catch_all')


        find_routes = RouteIdentification()


        if len(Operations) == 0:

            Paths.append(route[:])

            route.pop()
            level -= 1

            if RouteIdentification.is_last_operation == 'yes':
                route.pop()
                level -=1



            pass

        else:
            level += 1


            for i in range(len(Operations)):
                if i < len(Operations)-1:
                    RouteIdentification.is_last_operation = 'no'
                else:
                    RouteIdentification.is_last_operation = 'yes'



                current_opperation = Operations[i]

                if current_opperation == 'Catch_all':

                    route.clear()
                    pass

                else:
                    excecute = find_routes.Excecute_Opperations(current_opperation, Inversions, Translocations, Inverted_translocations, sequence_blocks)

                    new_sequence_blocks = excecute[0]
                    route.append(excecute[1])

                    find_routes.Identify_Routes(new_sequence_blocks, route, Paths, level, level_1_counter)

        return Paths



    def Excecute_Opperations(self, current_operation, Inversions, Translocations, Inverted_translocations, sequence_blocks ):

        excecute_operation = RearrangementOperationExcecution()

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