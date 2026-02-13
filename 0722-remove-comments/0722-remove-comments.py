class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        inBlock = False
        buffer = ""

        for line in source:
            i = 0

            while i < len(line):

                # CASE 1: currently inside block comment
                if inBlock:
                    if i + 1 < len(line) and line[i] == '*' and line[i+1] == '/':
                        inBlock = False
                        i += 2
                    else:
                        i += 1

                # CASE 2: not in block comment
                else:
                    # line comment //
                    if i + 1 < len(line) and line[i] == '/' and line[i+1] == '/':
                        break

                    # block comment /*
                    elif i + 1 < len(line) and line[i] == '/' and line[i+1] == '*':
                        inBlock = True
                        i += 2

                    # normal character
                    else:
                        buffer += line[i]
                        i += 1

            # end of line
            if not inBlock and buffer:
                result.append(buffer)
                buffer = ""

        return result
