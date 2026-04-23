class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)

        blocks = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                value = board[i][j]
                if value == ".":
                    continue
                elif value in rows[i] or value in columns[j] or value in blocks[(i // 3, j // 3)]:
                    return False
                rows[i].add(value)
                columns[j].add(value)
                blocks[(i // 3, j // 3)].add(value)
        
        return True
