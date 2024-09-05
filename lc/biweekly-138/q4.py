from functools import cmp_to_key


class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        damage_health = list(zip(damage, health))
        p = power

        def cmpt(a, b):
            (d_a, h_a) = a
            (d_b, h_b) = b
            return (
                d_a * ceil(h_a / p)
                + d_b * (ceil((h_a) / p) + ceil(h_b / p))
                - (d_b * ceil(h_b / p) + d_a * (ceil((h_a) / p) + ceil(h_b / p)))
            )

        damage_health.sort(key=cmp_to_key(cmpt))

        curr_damage = sum(damage)
        inflicted = 0
        for damage, health in damage_health:
            inflicted += curr_damage * math.ceil(health / p)
            curr_damage -= damage

        return inflicted
