from unittest import TestCase
from main import MapMatching
import numpy as np

class Testmapmatching(TestCase):
    def test_find_link(self):
        a=np.array(range(0,10,2))
        zero=np.zeros(5)
        links = [[[0, 0], [10, 0]], [[0, 0], [0, 10]], [[10, 0], [10, 10]], [[0, 10], [10, 10]]]
        myclass = MapMatching(a, zero, links)
        print(myclass.find_link(a,zero))


    def test_point_to_curve(self):
        a = np.array(range(10))
        b = np.random.randint(-1, 1, 10)
        expect = [[0, v] for v in np.array(range(0, 10))]
        links = [[[0, 0], [10, 0]], [[0, 0], [0, 10]], [[10, 0], [10, 10]], [[0, 10], [10, 10]]]
        myclass = MapMatching(b, a, links)
        modified = myclass.point_to_curve()
        print(modified)
        assert(expect==modified)

    def test_rot_deg(self):
        m = np.random.randint(-10, 0, 10)
        m_diff = np.random.randint(-5, 0, 10)
        links = [[[0,0],[10,0]],[[0,0],[0,10]],[[10,0],[10,10]],[[0,10],[10,10]]]
        myclass = MapMatching(m,m_diff,links)
        x, y = myclass.rot_deg()
        print(x)
        print(y)
        assert (all(item <= 0 for item in x))
        assert (all(item >= 0 for item in y))


if __name__ == '__main__':
    unittest.main()