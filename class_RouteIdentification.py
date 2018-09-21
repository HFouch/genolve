from class_DefineRearrangementOperations import DefineRearrangementOperations
from class_RearrangementOperationExecution import RearrangementOperationExecution
from class_SequenceBlockAndEdgeSeriesIdentification import SequenceBlockAndEdgeSeriesIdentification



class RouteIdentification:




    def __init__(self):
        pass

    def __del__(self):
        pass

    def identify_routes(self, sequence_blocks, route, Paths, level):


        generate_the_series_of_edges = SequenceBlockAndEdgeSeriesIdentification()
        edge_series = generate_the_series_of_edges.generate_edge_series(sequence_blocks)


        find_rearrangement_operations = DefineRearrangementOperations()
        Inversions = find_rearrangement_operations.inversion_identification(edge_series)
        Raw_Translocations = find_rearrangement_operations.translocation_identification(edge_series, sequence_blocks)
        Translocations = find_rearrangement_operations.removal_of_equivalent_translocations(Raw_Translocations, sequence_blocks)
        Inverted_translocations = find_rearrangement_operations.inverted_translocation_identification(edge_series,
                                                                                                    sequence_blocks)

        Operations = []
        Operations.extend(Inversions)
        Operations.extend(Translocations)
        Operations.extend(Inverted_translocations)

        if len(Operations) != 0:
          Operations.append('Catch_all')

        find_routes = RouteIdentification()


        if len(edge_series) == 0:

            Paths.append(route[:])

            if route[-1] == 'FINAL_INVERSIONS':

                route.pop()
                route.pop()


            elif route[-1] == 'FINAL_TRANSLOCATIONS':

                route.pop()
                route.pop()

            route.pop()
            level -= 1


            pass

        elif len(Operations) == 0:

            final_inversions = []
            search_final_inversions = find_rearrangement_operations.final_inversion_search(sequence_blocks,
                                                                                           final_inversions)

            new_sequence_blocks = search_final_inversions[0]
            inversions_found = search_final_inversions[1]

            if len(inversions_found) != 0:

                route.append(final_inversions[:])
                route.append(('FINAL_INVERSIONS'))
                level += 1


                find_routes.identify_routes(new_sequence_blocks, route, Paths, level)

            else:

                find_translocations = DefineRearrangementOperations()
                list_of_final_translocations  = []
                blocks = []
                search_final_tranlocations = find_translocations.final_translocation_search(sequence_blocks, blocks, list_of_final_translocations)
                new_sequence_blocks = search_final_tranlocations[0]
                translocations_found = search_final_tranlocations[1]


                if len(translocations_found) != 0:

                    final_translocations = []
                    for i in range(len(translocations_found)):
                        final_translocations.append(translocations_found[i][0])

                    route.append(final_translocations[:])
                    route.append('FINAL_TRANSLOCATIONS')

                    find_routes.identify_routes(new_sequence_blocks, route, Paths, level)

                else:
                    print('FD sequence_blocks:   ', sequence_blocks)
                    Paths.append(route[:])
                    route.pop()
                    level -= 1
                    pass



        else:
            level += 1
            for i in range(len(Operations)):
                current_opperation = Operations[i]

                if current_opperation == 'Catch_all':

                    if level == 1:
                        break

                    else:
                        if route[-1] == 'FINAL_INVERSIONS':

                            route.pop()
                            route.pop()


                        elif route[-1] =='FINAL_TRANSLOCATIONS':

                            route.pop()
                            route.pop()

                        route.pop()
                        level -= 1


                        pass


                else:
                    excecute_operation = RearrangementOperationExecution()
                    excecute = excecute_operation.execute_operations(current_opperation, Inversions, Translocations,
                                                                Inverted_translocations, sequence_blocks)

                    new_sequence_blocks = excecute[0]
                    route.append(excecute[1])

                    find_routes.identify_routes(new_sequence_blocks, route, Paths, level)

        return Paths




