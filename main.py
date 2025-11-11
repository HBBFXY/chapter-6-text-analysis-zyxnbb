from collections import Counter
import string

class FrequencyAnalyzer:
    """频率分析器类"""
    
    def __init__(self):
        self.history = []
    
    def analyze(self, text, case_sensitive=False):
        """分析文本的频率"""
        if not text:
            return "字符串为空"
        
        # 过滤字母字符
        if case_sensitive:
            letters = [char for char in text if char.isalpha()]
        else:
            letters = [char.lower() for char in text if char.isalpha()]
        
        if not letters:
            return "没有找到字母字符"
        
        # 统计频率
        counter = Counter(letters)
        total_letters = len(letters)
        
        # 排序
        sorted_result = sorted(counter.items(), 
                             key=lambda x: (-x[1], x[0]))
        
        # 保存到历史记录
        analysis_result = {
            'text': text,
            'case_sensitive': case_sensitive,
            'result': sorted_result,
            'total_letters': total_letters
        }
        self.history.append(analysis_result)
        
        return sorted_result, total_letters
    
    def display_analysis(self, text, case_sensitive=False):
        """显示分析结果"""
        result = self.analyze(text, case_sensitive)
        
        if isinstance(result, str):
            print(result)
            return
        
        sorted_chars, total_letters = result
        
        sensitivity = "区分大小写" if case_sensitive else "不区分大小写"
        print(f"\n字符串: '{text}'")
        print(f"分析模式: {sensitivity}")
        print("=" * 40)
        
        for char, count in sorted_chars:
            percentage = (count / total_letters) * 100
            bar = '█' * int((count / sorted_chars[0][1]) * 20)
            print(f"'{char}': {count:2d}次 |{bar:<20}| {percentage:5.1f}%")
        
        print(f"\n总字母数: {total_letters}")
        print(f"不同字母数: {len(sorted_chars)}")
    
    def show_history(self):
        """显示分析历史"""
        if not self.history:
            print("没有分析历史")
            return
        
        print("\n分析历史:")
        print("=" * 50)
        for i, analysis in enumerate(self.history, 1):
            print(f"{i}. 文本: '{analysis['text'][:30]}{'...' if len(analysis['text']) > 30 else ''}'")
            print(f"   模式: {'区分大小写' if analysis['case_sensitive'] else '不区分大小写'}")
            print(f"   字母数: {analysis['total_letters']}")
            print()

def main():
    """主程序"""
    analyzer = FrequencyAnalyzer()
    
    while True:
        print("\n" + "="*60)
        print("字符频率分析器")
        print("="*60)
        print("1. 分析字符串")
        print("2. 区分大小写分析")
        print("3. 显示分析历史")
        print("4. 退出")
        
        choice = input("\n请选择操作 (1-4): ").strip()
        
        if choice == '1':
            text = input("请输入要分析的字符串: ")
            analyzer.display_analysis(text, case_sensitive=False)
        
        elif choice == '2':
            text = input("请输入要分析的字符串: ")
            analyzer.display_analysis(text, case_sensitive=True)
        
        elif choice == '3':
            analyzer.show_history()
        
        elif choice == '4':
            print("感谢使用，再见！")
            break
        
        else:
            print("无效选择，请重新输入")

if __name__ == "__main__":
    main()
