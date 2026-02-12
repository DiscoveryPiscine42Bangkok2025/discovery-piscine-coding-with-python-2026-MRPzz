from checkmate import checkmate

def main():
        print("Test 1 :")

        board1 = """\
        R...
        .K..
        ..P.
        ....\
        """

        checkmate(board1)
        print("-" * 20)
        
        print("Test 2 (Queen kill):")
        board2 = """\
        KQ...
        .R...
        ..B..
        .....
        .....\
        """
        checkmate(board2)
        print("-" * 20)


        print("Test 3 (Rook kill):")
        board3 = """\
        ..K..
        .....
        ..R..
        .....
        .....\
        """
        checkmate(board3)
        print("-" * 20)


        print("Test 4 (Pawn Block Queen):")
        board4 = """\
        Q....
        .P...
        ..K..
        .....
        .....\
        """
        checkmate(board4)
        print("-" * 20)


        print("Test 5 (not NxN):")
        board5 = """\
        Q....
        .P...
        ..K..
        ....\
        """
        checkmate(board5)
        print("-" * 20)


        print("Test 6 (Bishop Kill):")
        board6 = """\
        .....
        .B...
        .....
        .....
        ....K\
        """
        checkmate(board6)
        print("-" * 20)


if __name__ == "__main__":
        main()
