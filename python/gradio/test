import gradio as gr
import random
import time
import numpy as np
#输入文本处理程序
# def greet(name):
#     return "Hello " + name + "!"
#接口创建函数
#fn设置处理函数，inputs设置输入接口组件，outputs设置输出接口组件
#fn,inputs,outputs都是必填函数

############# text一行，没有提示##################
# demo = gr.Interface(fn=greet, inputs="text", outputs="text")  #
############# text一行，没有提示 Textbox多行有提示##################
# demo = gr.Interface(
#     fn=greet,
#     # 自定义输入框
#     # 具体设置方法查看官方文档
#     inputs=gr.Textbox(lines=3, placeholder="Name Here...",label="my input"), #
#     outputs="text",
# )
############# checkbox选中值是1未选中是0,number数字类型，slider 滑动条#############
# def greet2(name, is_morning, temperature):
#     salutation = "Good morning" if is_morning else "Good evening"
#     greeting = f"{salutation} {name}. It is {temperature} degrees today"
#     celsius = (temperature - 32) * 5 / 9
#     return greeting, round(celsius, 2)
# demo = gr.Interface(
#     fn=greet2,
#     #按照处理程序设置输入组件
#     inputs=["text", "checkbox", gr.Slider(0, 100)],
#     #按照处理程序设置输出组件
#     outputs=["text", "number"],
# )

#############radio 单选#####################
# def calculator(num1, operation, num2):
#     if operation == "add":
#         return num1 + num2
#     elif operation == "subtract":
#         return num1 - num2
#     elif operation == "multiply":
#         return num1 * num2
#     elif operation == "divide":
#         return num1 / num2
#
# demo = gr.Interface(
#     calculator,
#     ["number", gr.inputs.Radio(["add", "subtract", "multiply", "divide"]), "number"],
#     "number",
#     live=True,
# )
# ########raise gr.Error提示框，examples列表，title标题，description左上角的描述文字，article左下角的文
# def calculator(num1, operation, num2):
#     if operation == "add":
#         return num1 + num2
#     elif operation == "subtract":
#         return num1 - num2
#     elif operation == "multiply":
#         return num1 * num2
#     elif operation == "divide":
#         if num2 == 0:
#             # 设置报错弹窗
#             raise gr.Error("Cannot divide by zero!")
#         return num1 / num2
# demo = gr.Interface(
#     calculator,
#     # 设置输入
#     [
#         "number",
#         gr.Radio(["add", "subtract", "multiply", "divide"]),
#         "number"
#     ],
#     # 设置输出
#     "number",
#     # 设置输入参数示例
#     examples=[
#         [5, "add", 3],
#         [4, "divide", 2],
#         [-4, "multiply", 2.5],
#         [0, "subtract", 1.2],
#     ],
#     # 设置网页标题
#     title="Toy Calculator",
#     # 左上角的描述文字
#     description="Here's a sample toy calculator. Enjoy!",
#     # 左下角的文字
#     article = "Check out the examples",
# )

###########json,label############
# scores = []
# def track_score(score):
#     scores.append(score)
#     #返回分数top3
#     top_scores = sorted(scores, reverse=True)[:3]
#     return top_scores
# demo = gr.Interface(
#     track_score,
#     gr.Number(label="Score"),
#     gr.JSON(label="Top Scores")
# )



####################block button 点击执行############
# with gr.Blocks() as demo:
#     #设置输入组件
#     name = gr.Textbox(label="Name")
#     # 设置输出组件
#     output = gr.Textbox(label="Output Box")
#     #设置按钮
#     greet_btn = gr.Button("Greet")
#     #设置按钮点击事件
#     greet_btn.click(fn=greet, inputs=name, outputs=output)
#################block的change监听执行#########################

# def welcome(name):
#     return f"Welcome to Gradio, {name}!"
# with gr.Blocks() as demo:
#     gr.Markdown(
#     """
#     # Hello World!
#     Start typing below to see the output.
#     """)
#     inp = gr.Textbox(placeholder="What is your name?")
#     out = gr.Textbox()
#     #设置change事件
#     inp.change(fn = welcome, inputs = inp, outputs = out) #
######################页面布局##########################
##############tab#############markdown 备注
#########水平、垂直、折叠#########
# def flip_text(x):
#     return x[::-1]
# def flip_image(x):
#     return np.fliplr(x)
# with gr.Blocks() as demo:
#     #用markdown语法编辑输出一段话
#     gr.Markdown("Flip text or image files using this demo.")
#     # 设置tab选项卡
#     with gr.Tab("Flip Text"):
#         #Blocks特有组件，设置所有子组件按垂直排列
#         #垂直排列是默认情况，不加也没关系
#         with gr.Column():
#             text_input = gr.Textbox()
#             text_output = gr.Textbox()
#             text_button = gr.Button("Flip")
#     with gr.Tab("Flip Image"):
#         #Blocks特有组件，设置所有子组件按水平排列
#         with gr.Row():
#             image_input = gr.Image()
#             image_output = gr.Image()
#         image_button = gr.Button("Flip")
#     #设置折叠内容
#     with gr.Accordion("Open for More!"):
#         gr.Markdown("Look at me...")
#     text_button.click(flip_text, inputs=text_input, outputs=text_output)
#     image_button.click(flip_image, inputs=image_input, outputs=image_output)

###############yield#######实时变化###########
#生成steps张图片，每隔1秒钟返回
# def fake_diffusion(steps):
#     for _ in range(steps):
#         time.sleep(1)
#         image = np.random.randint(255, size=(300, 600, 3))
#         yield image
# demo = gr.Interface(fake_diffusion,
#                     #设置滑窗，最小值为1，最大值为10，初始值为3，每次改动增减1位
#                     inputs=gr.Slider(1, 10, value=3, step=1),
#                     outputs="image")
# #生成器必须要queue函数
# demo.queue()
#################输出可交互########################
# def greet(name):
#     return "Hello " + name + "!"
# with gr.Blocks() as demo:
#     name = gr.Textbox(label="Name")
#     # 不可交互
#     # output = gr.Textbox(label="Output Box")
#     # 可交互
#     output = gr.Textbox(label="Output", interactive=True)
#     greet_btn = gr.Button("Greet")
#     greet_btn.click(fn=greet, inputs=name, outputs=output)


################# 多个button多按几次不变###########################
# def increase(num):
#     return num + 1
# with gr.Blocks() as demo:
#     a = gr.Number(label="a")
#     b = gr.Number(label="b")
#     # 要想b>a，则使得b = a+1
#     atob = gr.Button("b > a")
#     atob.click(increase, a, b)
#     # 要想a>b，则使得a = b+1
#     btoa = gr.Button("a > b")
#     btoa.click(increase, b, a)

######################返回值是输入输出，同时改变输入输出##########
# with gr.Blocks() as demo:
#     food_box = gr.Number(value=10, label="Food Count")
#     status_box = gr.Textbox()
#     def eat(food):
#         if food > 0:
#             return food - 1, "full"
#         else:
#             return 0, "hungry"
#     gr.Button("EAT").click(
#         fn=eat,
#         inputs=food_box,
#         #根据返回值改变输入组件和输出组件
#         outputs=[food_box, status_box]
#     )
# with gr.Blocks() as demo:
#     food_box = gr.Number(value=10, label="Food Count")
#     status_box = gr.Textbox()
#     def eat(food):
#         if food > 0:
#             return {food_box: food - 1, status_box: "full"}
#         else:
#             return {status_box: "hungry"}
#     gr.Button("EAT").click(
#         fn=eat,
#         inputs=food_box,
#         outputs=[food_box, status_box]
#     )

#######################update 更新输出框的样式 组件配置修改##########

# def change_textbox(choice):
#     #根据不同输入对输出控件进行更新
#     if choice == "short":
#         return gr.update(lines=2, visible=True, value="Short story: ")
#     elif choice == "long":
#         return gr.update(lines=8, visible=True, value="Long story...")
#     else:
#         return gr.update(visible=False)
# with gr.Blocks() as demo:
#     radio = gr.Radio(
#         ["short", "long", "none"], label="Essay Length to Write?"
#     )
#     text = gr.Textbox(lines=2, interactive=True)
#     radio.change(fn=change_textbox, inputs=radio, outputs=text)


############布局#####################
# with gr.Blocks() as demo:
#     with gr.Row():
#         img1 = gr.Image()
#         text1 = gr.Text()
#     btn1 = gr.Button("button")
#
# with gr.Blocks() as demo:
#     with gr.Row():
#         text1 = gr.Textbox(label="t1")
#         slider2 = gr.Textbox(label="s2")
#         drop3 = gr.Dropdown(["a", "b", "c"], label="d3")
#     with gr.Row():
#         # scale与相邻列相比的相对宽度。例如，如果列A的比例为2，列B的比例为1，则A的宽度将是B的两倍。
#         # min_width设置最小宽度，防止列太窄
#         with gr.Column(scale=2, min_width=600):
#             text1 = gr.Textbox(label="prompt 1")
#             text2 = gr.Textbox(label="prompt 2")
#             inbtw = gr.Button("Between")
#             text4 = gr.Textbox(label="prompt 1")
#             text5 = gr.Textbox(label="prompt 2")
#         with gr.Column(scale=1, min_width=600):
#             img1 = gr.Image("test.png")
#             btn = gr.Button("Go")

######################多选####CheckboxGroup#################
with gr.Blocks() as demo:
    # 出错提示框
    error_box = gr.Textbox(label="Error", visible=False)

    # 输入框
    name_box = gr.Textbox(label="Name")
    age_box = gr.Number(label="Age")
    symptoms_box = gr.CheckboxGroup(["Cough", "Fever", "Runny Nose"])
    submit_btn = gr.Button("Submit")

    # 输出不可见
    with gr.Column(visible=False) as output_col:
        diagnosis_box = gr.Textbox(label="Diagnosis")
        patient_summary_box = gr.Textbox(label="Patient Summary")

    def submit(name, age, symptoms):
        if len(name) == 0:
            return {error_box: gr.update(value="Enter name", visible=True)}
        if age < 0 or age > 200:
            return {error_box: gr.update(value="Enter valid age", visible=True)}
        return {
            output_col: gr.update(visible=True),
            diagnosis_box: "covid" if "Cough" in symptoms else "flu",
            patient_summary_box: f"{name}, {age} y/o"
        }

    submit_btn.click(
        submit,
        [name_box, age_box, symptoms_box],
        [error_box, diagnosis_box, patient_summary_box, output_col],
    )

##################render####################
# input_textbox = gr.Textbox()
#
# with gr.Blocks() as demo:
#     # 提供示例输入给input_textbox，示例输入以嵌套列表形式设置
#     gr.Examples(["hello", "bonjour", "merhaba"], input_textbox)
#     # render函数渲染input_textbox
#     input_textbox.render()

############ 修改blocks的背景颜色#############
# with gr.Blocks(css=".gradio-container {background-color: red}") as demo:
#     box1 = gr.Textbox(value="Good Job")
#     box2 = gr.Textbox(value="Failure")

# 这里用的是id属性设置
# with gr.Blocks(css="#warning {background-color: red}") as demo:
#     box1 = gr.Textbox(value="Good Job", elem_id="warning")
#     box2 = gr.Textbox(value="Failure")
#     box3 = gr.Textbox(value="None", elem_id="warning")


demo.launch()

