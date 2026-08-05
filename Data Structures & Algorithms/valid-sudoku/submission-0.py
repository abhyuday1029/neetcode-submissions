class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap_row = defaultdict(set)
        hashmap_col = defaultdict(set)
        hashmap_subgrid = defaultdict(set)

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == '.':
                    continue
                if num in hashmap_row[i] or num in hashmap_col[j] or num in hashmap_subgrid[(i//3, j//3)]:
                    return False
                hashmap_row[i].add(num)
                hashmap_col[j].add(num)
                hashmap_subgrid[(i//3, j//3)].add(num)
        return True
        