import unittest
import sys
import os

# 親ディレクトリのパスを追加して、標準スコアモジュールをインポート
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from standard_score import calculate_standard_score

class TestStandardScore(unittest.TestCase):
    def test_calculate_standard_score(self):
        # テストケース1: 標準的なケース
        scores = [80, 75, 90, 85, 70, 95, 65, 88, 72, 82]
        target_score = 85
        result = calculate_standard_score(scores, target_score)
        self.assertAlmostEqual(result, 55.26, places=2)

        # テストケース2: 平均点と同じ場合
        scores = [80, 80, 80, 80, 80]
        target_score = 80
        result = calculate_standard_score(scores, target_score)
        self.assertEqual(result, 50.0)

        # テストケース3: 標準偏差が0の場合（全員同じ点数）
        scores = [100, 100, 100, 100, 100]
        target_score = 100
        result = calculate_standard_score(scores, target_score)
        self.assertEqual(result, 50.0)

        # テストケース4: 極端に高い点数
        scores = [50, 60, 70, 80, 90]
        target_score = 100
        result = calculate_standard_score(scores, target_score)
        self.assertGreater(result, 50.0)

        # テストケース5: 極端に低い点数
        scores = [50, 60, 70, 80, 90]
        target_score = 40
        result = calculate_standard_score(scores, target_score)
        self.assertLess(result, 50.0)

if __name__ == '__main__':
    unittest.main() 