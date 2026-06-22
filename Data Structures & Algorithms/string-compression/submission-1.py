class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        curr = ''
        count = 0

        for ch in chars:
            if curr == '':
                curr = ch
                count = 1

            elif ch == curr:
                count += 1

            else:
                s.append(curr)
                if count > 1:
                    s.extend(str(count))

                curr = ch
                count = 1

        s.append(curr)
        if count > 1:
            s.extend(str(count))

        chars[:len(s)] = s
        return len(s)