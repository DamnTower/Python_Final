# python_final 18网新郑梓轩181012147Python期末项目

- [**项目代码Github URL**](https://github.com/DamnTower/Python_Final/blob/master/main.py)

- [**项目pythonanywhere URL**](http://juin1999.pythonanywhere.com/)

- **数据传递描述:** 

用户在前端下拉框想要查看的数据后，点击**go** 后，会反馈到HTML文件中的图表，同时显示文字描述和对应的数据。
----
用户直接点击导航栏的选项会跳转到相应的图表和描述，隐藏数据，使界面更简洁
----
用户在任意图表界面点击**回到首页**即可跳转回首页，阅览项目描述。



- **在项目中，我实现了：**

   1.HTML档：

   - 设计导航栏，并为导航栏增添CSS样式。

   - 页面为可交互图表。

   - 加入了文本描述内容。

   - 链接了static文档中的CSS文件，让四个页面的样式相同，整体更加美观。

   2.Python档：

   （1）调用模块

   - flask

   - pandas

   - plotly

   - pyecharts
  （2）部署到Pythonanywhere。

   

   - **Web App动作描述：**

   - 上方设有导航栏，可自行选择5个页面，每个页面故事不同。 通过下拉框选择图标，点击“go”也可以跳转到对应的界面。
   通过地图，直方图，折线图等呈现不同的数据。可通过按钮筛选呈现的数据。
   
   - **项目文件**
   * 1.[项目代码文件：](https://github.com/DamnTower/Python_Final/blob/master/main.py)
   py文件，在flask框架下实现了图表和数据展示以及用户交互功能。
   * 2.[templates文件夹：](https://github.com/DamnTower/Python_Final/tree/master/templates)
   用于存储html文件，与项目的python文件进行链接，实现了图表数据的展示，文字档描述以及页面设计。
   * 3.[static文件夹：](https://github.com/DamnTower/Python_Final/tree/master/static)
   用于存储css样式表，并外链到所有的html文件。
   * 4.[data文件夹：](https://github.com/DamnTower/Python_Final/tree/master/data)
   用于存储17级协作成员提供的csv数据表
   * 5.[交互式可视化图html档文件夹：](https://github.com/DamnTower/Python_Final/tree/master/%E4%BA%A4%E4%BA%92%E5%BC%8F%E5%8F%AF%E8%A7%86%E5%8C%96%E5%9B%BEhtml%E6%A1%A3)
   用于存储可视化图表html档，可实现图表交互。
   
