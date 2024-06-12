import os
import pandas as pd
import statsmodels.api as sm
#安装statsmodels包

root = "D:\\"
# root路径后期需要修改,就是在文件路径前面的部分，后面输出也要用到这个

# 读取统计文件,文件名也需要修改，目前用的是测试文件名
static = pd.read_csv(os.path.join(root, "input.csv")) 

def perform_regression(df, independent_var, dependent_var):
    print(independent_var, dependent_var)
    x = df[[independent_var]]  # 自变量
    x = sm.add_constant(x)     # 添加常数项
    y = df[dependent_var]      # 因变量
    model = sm.OLS(y, x).fit()
    
    if model.pvalues[independent_var]<=0.05:
        result=f"independent:{independent_var}, dependent:{dependent_var}, p-value is {model.pvalues[independent_var]}, coefficient is {model.params[independent_var]}"
        #print(model.summary())        
        return result
    else:
        return 0


result_list=[]
# 对每个因变量进行回归分析并输出 p 值
for dep in ["a","b","c"]:#设定需要的因变量列名,如果只有只有一个因变量就可以注销掉这一行把下面的块提前。或者直接就在[]里写一个名字
    #记着因变量列名一定是我们数据集里的列名
    for indep in static.columns[0:10]:#这里第1列到第11都是我想作为自变量跑一下的列。记着列数-1
        result=perform_regression(static, indep, dep)
        if result!=0:
            result_list.append(result)

with open(os.path.join(root, "output.txt"), 'w') as file:#改输出文件名字的话改那个output.txt
    #输出到一个txt里面，可以去excel里手动分列
    #结果就是告诉你自变量，因变量，p值
    for line in result_list:
        file.write(line + '\n')

    

