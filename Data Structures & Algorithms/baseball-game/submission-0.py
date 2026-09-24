class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for ops in operations:
            if ops == '+':
                a, b = record.pop(), record.pop()
                record.extend([b,a,a+b])
            elif ops == 'C':
                record.pop()
            elif ops == 'D':
                a = record.pop()
                record.extend([a, 2*a])
            else:
                record.append(int(ops))
        return sum(record)
        