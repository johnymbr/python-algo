from typing import List


def reconstruct_queue(people: List[List[int]]) -> List[List[int]]:
    people.sort(key=lambda x: x[0])

    
