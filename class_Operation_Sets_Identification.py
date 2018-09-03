from class_defining_rearrangment_operations import RearrangementOperationIdentification
from class_execute_rearrangement_operations import RearrangementOperationExcecution
from class_defining_edge_series import EdgeSeriesAndSequenceBlocks


class RouteIdentification:

    route = []
    Paths = []
    is_last_operation = 0

    def __init__(self):
        pass

    def __del__(self):
        pass

    def Identify_Routes(self, sequence_blocks):


        generate_the_series_of_edges = EdgeSeriesAndSequenceBlocks()
        edge_series = generate_the_series_of_edges.GenerateEdgesSeries(sequence_blocks)

        find_rearrangement_operations = RearrangementOperationIdentification()
        Inversions = find_rearrangement_operations.InversionIdentification(edge_series)
        Translocations = find_rearrangement_operations.TranslocationIdentification(edge_series, sequence_blocks)
        Inverted_translocations = find_rearrangement_operations.InvertedTranslocationIdentification(edge_series,
                                                                                                    sequence_blocks)
        Operations = []
        Operations.extend(Inversions)
        Operations.extend(Translocations)
        Operations.extend(Inverted_translocations)

        print()
        print('OPERATIONS:   ', Operations)
        print()

        excecute = RouteIdentification()

        if len(Operations) == 0:
            print('FINAL ROUTE:   ', RouteIdentification.route)

            RouteIdentification.Paths.append(RouteIdentification.route)

            RouteIdentification.route.pop()
            if RouteIdentification.is_last_operation == 'yes':
                RouteIdentification.route.pop()

            pass

        else:

            for i in range(len(Operations)):
                if i < len(Operations)-1:
                    RouteIdentification.is_last_operation = 'no'
                else:
                    RouteIdentification.is_last_operation = 'yes'

                current_opperation = Operations[i]

                new_sequence_blocks = excecute.Excecute_Opperations(current_opperation, Inversions, Translocations, Inverted_translocations, sequence_blocks)

                excecute.Identify_Routes(new_sequence_blocks)






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



        RouteIdentification.route.append(operation)

        print()
        print('WORKING ROUTE:   ', RouteIdentification.route)
        print()


        return new_sequence_blocks