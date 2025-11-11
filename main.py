def print_letters_by_frequency(text):
    """
    按字符出现频率降序打印字母
    
    参数:
    text -- 输入的字符串
    """
    # 创建字典统计字符频率
    char_count = {}
    
    # 统计每个字符的出现次数
    for char in text:
        if char.isalpha():  # 只统计字母字符
            char_lower = char.lower()  # 不区分大小写
            char_count[char_lower] = char_count.get(char_lower, 0) + 1
    
    if not char_count:
        print("字符串中没有字母字符")
        return
    
    # 按频率降序排序，频率相同的按字母顺序排序
    sorted_chars = sorted(char_count.items(), 
                         key=lambda x: (-x[1], x[0]))
    
    # 打印结果
    print(f"字符串: '{text}'")
    print("字母按频率降序排列:")
    print("-" * 30)
    
    for char, count in sorted_chars:
        print(f"'{char}': 出现 {count} 次")

# 测试函数
def test_frequency_analysis():
    """测试频率分析函数"""
    test_cases = [
        "Hello World",
        "Programming is fun",
        "Mississippi",
        "A man a plan a canal Panama",
        "12345!!!",  # 没有字母的情况
        "",  # 空字符串
        "a"  # 单个字符
    ]
    
    for test_case in test_cases:
        print("\n" + "="*50)
        print_letters_by_frequency(test_case)

# 交互式版本
def interactive_frequency_analysis():
    """交互式频率分析"""
    while True:
        print("\n" + "="*50)
        user_input = input("请输入要分析的字符串 (输入 'quit' 退出): ")
        
        if user_input.lower() == 'quit':
            print("程序结束，再见！")
            break
        
        print_letters_by_frequency(user_input)

if __name__ == "__main__":
    # 运行测试
    test_frequency_analysis()
    
    # 运行交互式版本
    interactive_frequency_analysis()
