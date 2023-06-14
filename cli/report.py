class Report:
    def __init__(self, output_file='report.txt'):
        self.output_file = output_file

    def generate(self):
        # 在这里编写生成巡检报告的代码
        with open(self.output_file, 'w') as f:
            f.write('This is a sample report.\n')
        print(f"Report generated and saved to {self.output_file}.")