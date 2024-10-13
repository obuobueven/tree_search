# 2048游戏
# 创建一个地图类，具有map属性，是一个4x4的二维数组，每个元素是一个数字。
# 实现游戏的运行逻辑，包括：
# 1. 随机生成两个数字
# 2. 合并相同数字
# 3. 移动数字
# 4. 判断游戏是否结束

import random

class Game:
    def __init__(self):
        self.map = [[0] * 4 for _ in range(4)]  # 初始化一个4x4的地图
        self.map_init()  # 随机生成两个数字

    def map_init(self):
        for _ in range(2):  # 生成两个随机数字
            x, y = self.random_empty_position()
            if x is not None and y is not None:
                self.map[x][y] = random.choice([2, 4])

# 返回一个随机的空位置
    def random_empty_position(self):
        empty_positions = [(i, j) for i in range(4) for j in range(4) if self.map[i][j] == 0]
        if not empty_positions:  # 如果没有空位置，游戏结束
            self.end_game()
        return random.choice(empty_positions)# 返回随机的空位置
    
# 添加随机数字   
    def add_random_number(self):
        # 随机生成一个数字
        x, y = self.random_empty_position()
        if x is not None and y is not None:
            self.map[x][y] = random.choice([2, 4])

# 实现map的打印
    def print_map(self):
        for row in self.map:
            print(row)


    def merge(self):
        # 实现合并相同数字的逻辑
        # 在这个方法里添加适当逻辑，确保合并过程不会造成重复合并
        pass

# 移动函数
    def move(self, direction: int):
       try:
           moved = False
           if direction not in [0, 1, 2, 3]:  # 0: 上，1: 下，2: 左，3: 右
               raise ValueError("方向错误！")
           
           # 根据方向处理移动
           if direction in [0, 1]:  # 上下移动
               for col in range(4):
                   # 提取列
                   temp = [self.map[row][col] for row in range(4)]
                   new_temp = self._move_line(temp, direction == 0)  # 0为上，1为下
                   for row in range(4):
                       self.map[row][col] = new_temp[row]
                   # 如果新列与原列不相同，标记为移动
                   if new_temp != temp:
                       moved = True
   
           else:  # 左右移动
               for row in range(4):
                   temp = self.map[row][:]  # 复制行
                   new_temp = self._move_line(temp, direction == 2)  # 2为左，3为右
                   self.map[row] = new_temp
                   # 如果新行与原行不相同，标记为移动
                   if new_temp != temp:
                       moved = True
   
           # 若移动发生，随机生成新数字
           if moved:
               self.add_random_number()
   
       except Exception as e:
           print(f"发生错误: {e}")

# 更新游戏状态
    def _move_line(self, line: list, left: bool) -> list:
        """处理一行或一列的移动和合并逻辑"""
        if left:  # 左移
            new_line = [num for num in line if num != 0]  # 去除零
            merged_line = []
            skip = False
            for i in range(len(new_line)):
                if skip:
                    skip = False
                    continue
                if i < len(new_line) - 1 and new_line[i] == new_line[i + 1]:  # 合并
                    merged_line.append(new_line[i] * 2)
                    skip = True
                else:
                    merged_line.append(new_line[i])
            # 补零
            return merged_line + [0] * (4 - len(merged_line))
        else:  # 右移
            new_line = [num for num in line if num != 0][::-1]  # 去除零并反转
            merged_line = []
            skip = False
            for i in range(len(new_line)):
                if skip:
                    skip = False
                    continue
                if i < len(new_line) - 1 and new_line[i] == new_line[i + 1]:  # 合并
                    merged_line.append(new_line[i] * 2)
                    skip = True
                else:
                    merged_line.append(new_line[i])
            # 补零
            return [0] * (4 - len(merged_line)) + merged_line[::-1]

# 判断游戏是否结束
    def is_game_over(self) -> bool:
        # 判断游戏是否结束
        # 1 存在空位置，游戏继续
        if 0 in [num for row in self.map for num in row]:
            return False
        # 2 无相邻的相同数字，游戏结束
        for i in range(3):
            for j in range(3):
                if self.map[i][j] == self.map[i+1][j] or self.map[i][j] == self.map[i][j+1]:  # 存在相同数字，游戏继续
                    return False

        # 无相同数字，游戏结束
        
        return True

    def run(self):
        try:
            while not self.is_game_over():
                # 执行用户输入
                # 如果用户按回车键，则结束游戏
                user_input = input("请输入方向（0: 上，1: 下，2: 左，3: 右），或直接按回车结束游戏：")
                if user_input == "":
                    break
            
                direction = int(user_input)
                self.move(direction)
                self.print_map()

                # 判断游戏是否结束

        except Exception as e:
            print(f"发生错误: {e}")

    def end_game(self):
        # 结束游戏的逻辑
        print("游戏结束！")



game = Game()
print("初始状态：")
game.print_map()

game.run()


