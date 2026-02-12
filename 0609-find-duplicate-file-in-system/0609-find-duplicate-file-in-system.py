from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
    
        for path in paths:
            parts = path.split(' ')
            root = parts[0] 
            
            for file in parts[1:]:
                name, content = file.split('(')
                content = content[:-1] 
                full_path = f"{root}/{name}"
                freq[content].append(full_path)
        
        return [group for group in freq.values() if len(group) > 1]
