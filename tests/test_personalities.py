# test_personalities.py

import unittest
from personalities_list import personalities

class TestPersonalities(unittest.TestCase):
    def test_personality_traits(self):
        allowed_traits = ['Professionalism', 'Determination', 'Ambition', 'Loyalty', 'Sportsmanship', 'Pressure', 'Temperament','Leadership']
        for personality, traits in personalities.items():
            for trait, value in traits.items():
                self.assertIn(trait, allowed_traits, f"Trait '{trait}' in personality '{personality}' is not allowed")
                # Here you can also check if the values are within an expected range, if necessary
                # e.g. self.assertTrue(0 <= value <= 10, "Trait value is out of range")

if __name__ == '__main__':
    unittest.main()
