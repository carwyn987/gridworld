import numpy as np
import unittest
from src.gridworld_generators import generate_single_gridworld, step_gridworld

class TestExample(unittest.TestCase):
    def test_generation(self):
        result = generate_single_gridworld(4,4,4,4)
        self.assertEqual(sum(sum(result != 0)), 4)
 

    def test_step_forward(self):
        # 1 = up, 2 = down, 3 = left, 4 = right
        my_gridworld_t0 = np.array([[2, 0, 0, 0],
                                    [0, 4, 2, 0],
                                    [0, 0, 4, 1],
                                    [3, 0, 0, 0]])

        my_gridworld_t1 = np.array([[0, 0, 0, 0],
                                    [2, 0, 4, 1],
                                    [0, 0, 2, 4],
                                    [0, 0, 0, 0]])

        my_gridworld_t2 = np.array([[0, 0, 0, 1],
                                    [0, 0, 0, 4],
                                    [2, 0, 0, 0],
                                    [0, 0, 2, 0]])

        my_gridworld_t3 = np.array([[0, 0, 0, 0],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0],
                                    [2, 0, 0, 0]])

        my_gridworld_t4_plus = np.array([[0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0]])

        assert (step_gridworld(my_gridworld_t0) == my_gridworld_t1).all()
        assert (step_gridworld(my_gridworld_t1) == my_gridworld_t2).all()
        assert (step_gridworld(my_gridworld_t2) == my_gridworld_t3).all()
        assert (step_gridworld(my_gridworld_t3) == my_gridworld_t4_plus).all()
        assert (step_gridworld(my_gridworld_t4_plus) == my_gridworld_t4_plus).all()        

    # def test_random(self):
    #     result = generate_single_gridworld(4,4,4,4)
    #     print(result)
    #     print(step_gridworld(result))
        

if __name__ == "__main__":
    unittest.main()