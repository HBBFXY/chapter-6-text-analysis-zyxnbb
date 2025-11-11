from collections import Counter

def detailed_frequency_analysis(text):
    """
    详细的频率分析，包含大小写区分版本
    
    参数:
    text -- 输入的字符串
    """
    if not text:
        print("字符串为空")
        return
    
    # 版本1：不区分大小写
    letters_lower = [char.lower() for char in text if char.isalpha()]
    
    # 版本2：区分大小写
    letters_original = [char for char in text if char.isalpha()]
    
    print(f"原始字符串: '{text}'")
    print("=" * 50)
    
    # 不区分大小写的分析
    if letters_lower:
        counter_lower = Counter(letters_lower)
        sorted_lower = sorted(counter_lower.items(), 
                            key=lambda x: (-x[1], x[0]))
        
        print("不区分大小写分析:")
        print("-" * 25)
        for char, count in sorted_lower:
            percentage = (count / len(letters_lower)) * 100
            print(f"'{char}': {count:2d} 次 ({percentage:5.1f}%)")
    
    # 区分大小写的分析
    if letters_original:
        counter_original = Counter(letters_original)
        sorted_original = sorted(counter_original.items(), 
                               key=lambda x: (-x[1], x[0]))
        
        print("\n区分大小写分析:")
        print("-" * 25)
        for char, count in sorted_original:
            percentage = (count / len(letters_original)) * 100
            print(f"'{char}': {count:2d} 次 ({percentage:5.1f}%)")
    
    # 统计信息
    print("\n统计摘要:")
    print("-" * 25)
    print(f"总字符数: {len(text)}")
    print(f"字母字符数: {len(letters_original)}")
    print(f"不同字母数(不区分大小写): {len(set(letters_lower)) if letters_lower else 0}")
    print(f"不同字母数(区分大小写): {len(set(letters_original)) if letters_original else 0}")

# 测试详细版本
def test_detailed_analysis():
    """测试详细分析版本"""
    test_cases = [
        "Hello World",
        "Python Programming",
        "AaBbCc",  # 测试大小写区分
        "123!@#",  # 无字母情况
        ""  # 空字符串
    ]
    
    for test_case in test_cases:
        print("\n" + "="*60)
        detailed_frequency_analysis(test_case)

if __name__ == "__main__":
    # 运行详细分析测试
    test_detailed_analysis()
