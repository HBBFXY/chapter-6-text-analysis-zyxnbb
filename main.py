from collections import Counter

def print_letters_by_frequency_counter(text):
    """
    使用Counter按字符出现频率降序打印字母
    
    参数:
    text -- 输入的字符串
    """
    # 过滤出字母字符并转换为小写
    letters = [char.lower() for char in text if char.isalpha()]
    
    if not letters:
        print("字符串中没有字母字符")
        return
    
    # 使用Counter统计频率
    char_counter = Counter(letters)
    
    # 按频率降序排序，频率相同的按字母顺序排序
    sorted_chars = sorted(char_counter.items(), 
                         key=lambda x: (-x[1], x[0]))
    
    # 打印结果
    print(f"字符串: '{text}'")
    print("字母按频率降序排列:")
    print("-" * 30)
    
    for char, count in sorted_chars:
        print(f"'{char}': 出现 {count} 次")
        
    # 可选：显示频率分布图
    display_frequency_chart(sorted_chars)

def display_frequency_chart(sorted_chars):
    """显示简单的频率分布图"""
    if not sorted_chars:
        return
    
    max_count = sorted_chars[0][1]
    print("\n频率分布图:")
    print("-" * 20)
    
    for char, count in sorted_chars:
        bar_length = int((count / max_count) * 20)  # 最大长度20
        bar = '█' * bar_length
        print(f"{char}: {bar} ({count})")

# 测试Counter版本
def test_counter_version():
    """测试Counter版本"""
    test_strings = [
        "Hello World",
        "Mississippi",
        "The quick brown fox jumps over the lazy dog"
    ]
    
    for test_str in test_strings:
        print("\n" + "="*50)
        print_letters_by_frequency_counter(test_str)
