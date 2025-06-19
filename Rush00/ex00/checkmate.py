def checkmate(board: str):
    board = board.strip().split('\n')
    size = len(board)

    # ตรวจสอบว่าเป็นกระดานสี่เหลี่ยม
    for row in board:
        if len(row) != size:
            print("Error")
            return

    # หาตำแหน่งของ King
    king_pos = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Error")
        return

    def in_bounds(x, y):
        return 0 <= x < size and 0 <= y < size

    def is_pawn_attacking():
        x, y = king_pos
        # Pawn ฝั่งตรงข้ามโจมตีเฉียงขึ้นซ้าย-ขวา (เพราะ K เป็นหมากขาว)
        for dx, dy in [(-1, -1), (-1, 1)]:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and board[nx][ny] == 'P':
                return True
        return False

    def is_bishop_attacking():
        x, y = king_pos
        for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            while in_bounds(nx, ny):
                piece = board[nx][ny]
                if piece == '.':
                    nx += dx
                    ny += dy
                elif piece in ('B', 'Q'):
                    return True
                else:
                    break
        return False

    def is_rook_attacking():
        x, y = king_pos
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            while in_bounds(nx, ny):
                piece = board[nx][ny]
                if piece == '.':
                    nx += dx
                    ny += dy
                elif piece in ('R', 'Q'):
                    return True
                else:
                    break
        return False

    if is_pawn_attacking() or is_bishop_attacking() or is_rook_attacking():
        print("Success")
    else:
        print("Fail")