import numpy as np

def calculate_standard_score(scores, target_score):
    """
    偏差値を計算する関数
    
    Args:
        scores (list): 全員の得点のリスト
        target_score (float): 偏差値を計算したい個人の得点
    
    Returns:
        float: 偏差値
    """
    mean = np.mean(scores)  # 平均値
    std = np.std(scores, ddof=0)  # 標準偏差
    
    # 標準偏差が0の場合（全員同じ点数）は偏差値を50とする
    if std == 0:
        return 50.0
    
    # 偏差値の計算
    standard_score = 50 + 10 * (target_score - mean) / std
    return standard_score

def main():
    # サンプルデータ
    scores = [80, 75, 90, 85, 70, 95, 65, 88, 72, 82]
    target_score = 85
    
    # 偏差値の計算
    result = calculate_standard_score(scores, target_score)
    
    print(f"全員の得点: {scores}")
    print(f"平均点: {np.mean(scores):.2f}")
    print(f"標準偏差: {np.std(scores, ddof=0):.2f}")
    print(f"得点 {target_score} の偏差値: {result:.2f}")

if __name__ == "__main__":
    main() 