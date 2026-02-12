def checkmate(board):
    board_list = board.split()
    size = len(board_list)

    # ตรวจ n x n
    for row in board_list:
        if len(row) != size:
            print("Error, Not n x n")
            return
    print(board_list)
    # หา King
    king_count = 0
    r_king = -1
    c_king = -1

    for i in range(size):
        for j in range(size):
            if board_list[i][j] == "K":
                king_count += 1
                r_king = i
                c_king = j

    if king_count != 1:
        print("Error")
        return

    print("King Position:", r_king, c_king)

    for r in range(size):
        for c in range(size):
            pos = board_list[r][c]
            
            if pos == "P":
                if 0 <= r-1 < size and 0 <= c-1 < size:
                    if r-1 == r_king and c-1 == c_king:
                        print("Success, By Pawn")
                        return
                if 0 <= r-1 < size and 0 <= c+1 < size:
                    if r-1 == r_king and c+1 == c_king:
                        print("Success, By Pawn")
                        return

            elif pos == "B":
                patterns = [(-1,-1), (-1,1), (1,-1), (1,1)] 
                for p_r, p_c in patterns:  
                    nr, nc = r + p_r, c + p_c   ## ตำแหน่งใหม่ = ตำแหน่งเดิม + เวกเตอร์การเคลื่อนที่
                    while 0 <= nr < size and 0 <= nc < size: 
                        if board_list[nr][nc] == "K":  
                            print("Success, By Bishop")
                            return
                        if board_list[nr][nc] != ".":   
                            break     
                        nr += p_r     ## เอาตำแหน่งล่าสุด + เวกเตอร์เพื่อจะขยับต่อ
                        nc += p_c

            elif pos == "R":
                patterns = [(-1,0), (1,0), (0,-1), (0,1)]
                for p_r, p_c in patterns:
                    nr, nc = r + p_r, c + p_c
                    while 0 <= nr < size and 0 <= nc < size:
                        if board_list[nr][nc] == "K":
                            print("Success, By Rook")
                            return
                        if board_list[nr][nc] != ".":
                            break
                        nr += p_r
                        nc += p_c

            elif pos == "Q":
                patterns = [(-1,-1), (-1,1), (1,-1), (1,1), (-1,0), (1,0), (0,-1), (0,1)]
                for p_r, p_c in patterns:
                    nr, nc = r + p_r, c + p_c
                    while 0 <= nr < size and 0 <= nc < size:
                        if board_list[nr][nc] == "K":
                            print("Success, By Queen")
                            return
                        if board_list[nr][nc] != ".":
                            break
                        nr += p_r
                        nc += p_c

    print("Fail")
