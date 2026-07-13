class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Target bisa dicapai, kalau tiap element di triplets an, bn, cn, ada kombinasi dimana
        # ketika kita gabung t1, t2, t3 merupakan maksimum dari an, bn, cn. Jadi kalau ada satu an, bn, cn diatas itu bisa merusak target. 
        # Tiap triplet yang ada target, wajib mempunyai properti ini

        check = [0, 0 , 0]
        for triplet in triplets:
            if any(triplet[i] > target[i] for i in range(len(target))):
                continue
            check = [max(check[i], triplet[i]) for i in range(len(check))]
        
        return all(check[i] == target[i] for i in range(len(triplet)))