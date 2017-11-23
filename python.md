# book_list
- A Byte of Python
- Python For Data Analysis
    - **与外界进行交互**:读写各种各样的文件格式和数据库
    - **准备**:对数据进行清理、休整、整合、规范化、重塑、切片切块、变形等处理以便进行分析。
    - **转换**:对数据集做一些数学和统计运算以产生新的数据集。
    - **建模和计算**:将数据跟统计模型、机器学习算法或其他计算工具联系起来。
    - **展示**:创建交互式的或静态的图片或文字摘要。
- learn python the hard way
- Head First Python


# important Python libraries(重要的Python库)
- IPython:Python 科学计算标准工具集的组成部分，它将其他所有东西联系到了一起。
- NumPy(Numerical Python):科学计算的基础包。
- Pandas(panel data & Python data analysis):使我们能够快速便捷地处理结构化数据的大量数据结构和函数。
- matpoltlib:是最流行的用于绘制数据库图表的 Python 库。它和 IPython 结合的很好。
- SciPy:是一组专门解决科学计算中各种标准问题域的包的集合。

# python2 & python3
- ```input()```在python2中是把输入的数据直接当做代码来执行,Python3把这个函数删了.用```raw_input()```替代输入. 

# Terminology(术语)
- Literal Constants(字面常量):你用的就是它字面意义上的值或是内容.它是一个 常量，因为它的值不能被改变。
- Escape Sequence(转义序列)
- Identifiers(标识符)
- Physical Line(物理行):在编程写程序时你所看到的内容.
- Logical Line(逻辑行):是Python所看到的内容.Python会假定没一个物理行,会对应一个逻辑行.
- Data Type(数据类型)
- Explicit Line Joining(显示行连接)
- Implicit Line Joining(隐式行连接)
- Indentation(缩进)
- block(块)
- Expressions(表达式)
- Operators(运算符)
- Operands(操作数)
- Membership Tests(成员资格测试):in, not in
- Identity Tests(资格测试):is, is not
- iterates(迭代)
- sequence(序列)
- Parameters(形参)
- Arguments(实参)
- global(全局)
- local(局部)
- scope(作用域)
- namespace(命名空间)
- Keyword Arguments(关键字参数)
- Documentation Strings(文档字符串)



- structured data(结构化数据)
- column-oriented(面向列)
- panel data(面板数据):这是计量经济学中有关多维结构化数据集的一个术语。
- Munge/Munging/Wrangling(数据规整)
- Pesudocode(伪码)
- Syntactic sugar(语法糖)
- JSON(JavaScript Object Notation):一种常用的 Web 数据格式
- list comprehension(列表推倒式):这是一种在一组字符串(或一组别的对象)上执行一条相同的操作(如 json.loads)的简洁方式。
- summary view(摘要试图):主要用于显示较大的 DataFrame 对象。


# about Python(关于Python)
- Python 时一种极少能声言兼具简单与功能强大的变成语言.
- Python是一款易于学习且功能强大的编程语言.它具有高效率的数据结构,能够简单又有效地实现面向对象编程.
- Python简洁的语法与动态输入之特性,加之其解释性语言的本质,使得它成为一种在多种领域与绝大多数平台都能进行脚本编写与应用快速开发工作的理想语言.
- Python的创造者:吉多.范罗苏姆(Guido van Rossum).
- 大多数软件都是由两部分代码组成的：少量需要占用大部分执行时间的代码，以及大量不经常执行的“粘合剂代码”
- 粘合剂代码的执行时间通常是微不足道的。开发人员的精力几乎都是花在优化计算瓶颈上面的，有时更是直接转用更低级的语言(比如C)。
- Python 不仅适用于研究和原型构建，同时也适用于构建生产系统。
- Python 不适合要求延迟非常小的应用程序(如高频交易系统)，以及高并发、多线程的应用程序。
- 构建一项软件设计有两种方式:一种是将软件设计的足够简单以至于明显找不到缺陷,另一种时将软件设计的足够复杂以至于找不到明显缺陷.
- 在人生中取得成功,与其说是靠天才与机会,不如说靠专注与毅力.
- 使用help('') 获取所有有关Python的信息.


# basic(基础)
- 你应该在你的程序中尽可能多地使用有用的注释：这样做对你的程序的读者来说非常有用。请记住，这个人可以是六个月后的你！
    - 解释假设
    - 说明重要的决定
    - 解释重要的细节
    - 说明你想要解决的问题
    - 说明你想要在程序中克服的问题。
- ```name + 'is' + str(age)``` 这样实现是很丑陋的.应该使用格式化方法.
- ```print('{} was {} years old when he wrote this book'.format(name, age))```大括号内可以没有序号
- ```print('{0:_^11}'.format('hello'))```定义字符串长度为11
- ```print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))```基于关键词输出
- ```print('a'),```后面会去掉换行符
- ```r"New \n"```采用原始字符串
- 处理正则表达式时应该全程使用原始字符串.否则会有大量Back whacking需要处理.  
- Python没有单独的long类型int类型可以指任何大小的整数.
- Python中一切都是对象,包括数字,字符串与函数.
- Python鼓励每一行使用一局独立语句从而使得代码更加可读.
- 如果在一行物理行中指定多行逻辑行,那么必须通过使用分号(;)来明确表明逻辑行或语句的结束.
- 如果有一行非常长的代码,可以通过使用反斜杠将其拆分成多个物理行.这被称作显式行连接.
- 逻辑行以括号开始,可以是方括号或花括号,但不能是结束括号.这被称作隐式连接.
- Python中没有单独的char数据类型.它并非切实必要,并且我相信你不会想念它的.
- 字符串是不可变的,一旦你创造了一串字符串,你就不能再改变它.这并非一件坏事.
- 赋值(assignment)操作也叫做绑定(binding)，因为我们其实是姜一个名称和一个对象绑定到一起。已经赋值的变量有时也被称为已绑定变量(bound variable)
- 当你将对象以参数的形式传入函数时，其实只是传入了一个引用而已，不会发生任何复制。因此，Python被称为是按引用传递的。
- python是一种强类型语言，也就是说，所有对象都有一个特定的类型(或类)，隐式转换只在很明显的情况下才会发生。
- Python 中的对象有属性(attribute，即存储在该对象那个“内部”的其他Python对象)
- Python 中的对象有方法(method，与该对象有关的能够访问其内部数据的函数)。
- 一般来说，你可能不会关心对象的类型，而只是想直到它到底有没有某些方法或行为。
- 只要一个对象实现了迭代器协议(iterator protocol)，你就可以确认它是可迭代的。
- ```from some_module import PI as pi, g as gf```
- 要判断两个引用是否指向同一个对象，可以使用 is 关键字。 注意， == 是判断值，这不是一回事。
- is 和 is not 常常用于判断变量是否为 None， 因为None的实例只有一个。
- 大部分Python对象是可变的(mutable)，字符串和元组是不可变的(immutable)。————不能修改原内存块的数据。
- 仅仅因为“可以修改某个对象”并不代表“就该那么做”。这种行为在编程中也教做副作用(side effect)。
    - 在编写一个函数时，任何副作用都应该通过该函数的文档或注释明确地告知用户。
    - 即时可以使用可变对象，也应该尽量避免副作用且注重不变性(immutability)
- 最好使用圆括号操作符来对运算符与操作数进行分组,以更加明确地指定优先级.这也可以使得程序更加可读.但不要过度使用.
- ```print 'a', 3``` Python 会自动帮我们在两个对象之间加上空格,呈现一个整洁的输出结果.这就是Python人性化的范例. 


# standard type(标准类型)
- str 字符串类型。Python 2.x 中只有 ASCII值，而Python 3 中则是Unicode
- unicode Unicode 字符串类型
- float 双精度(64位)浮点数。注意，这里没有专门的 double 类型。
- int 有符号整数，其最大值由平台决定(是32位还是64位)。
- long 任意精度的有符号整数，大的 int 值会被自动转换为 long。
- fval = 6.78e-5 可以用科学计数法表示。
- Python 3中，整数除法除不尽时就会产生一个浮点数。
- 但是在 Python 2.7 及一下版本中，添加一条语句到自定义模块的顶部即可  from __future__ import division，或者使用 3 / float(2)
- 要得到C风格的整数除法(如果除不尽，就丢弃小数部分)，使用除后圆整运算符 (//)
- Python 字符串是不可变的。要修改字符串就只能创建一个新的。
- 许多Python对象都可以用 str() 函数转换为字符串。
- 由于字符串其实是一串字符序列，因此可以被当做某种序列类型(如列表、元组等)进行处理。如 [:3]
- \ 是转义符(escape character),也就是说，它可以用于指定特殊字符(\n 或 unicode字符)
- 在字符串最左边引号前加上r，它表示所有字符应该按照原本的样子进行解释。
- 字符串格式化要用实参替换这些格式化形参，需要用到二元运算符%以及由值组成的元组。
- 几乎所有内置的Python类型以及任何定义了__nonzero__魔术方法的类都能在if语句中被解释为True或False。Python中大部分对象都有真假概念。
- 要想直到某个对象究竟会被强制转换成哪个布尔值，使用bool()函数即可。
- bool、int、str、float等类型也可用作将值转换成该类型的函数。
- None是Python的空值类型。如果一个函数没有显示的返回值，则隐式返回None。
- 我们要牢记，None不是一个保留关键字，它只是NoneType的一个实例而已。
- Python内置的datetime模块提供了datetime、date、time等类型。datetime类型是用的最多的，它合并了保存在date和time中的信息。
- ```from datetime import datetime, date, time```
- 两个datetime对象的差会产生一个datetime.datedelta类型
- 将一个timedelta加到一个datetime上会产生一个新的datetime



# 运算符与表达式
- 运算符
    - lambda
    - if elif else, for in else, while else
    - or
    - and
    - not x
    - in, not in, is, is not, <, <=, >, >=, !=, ==
    - |, ^, &
    - << >>
    - +, -, *, /, //, %, **
    - +x, -x, ~x
    - x[index]
    - x[index:index], x(arguments...), x.attribute
    - (expressions...), [expressions...], {key: value...}, {expressions...}
- 表达式
    - value = true-expr if condition else false-expr 三元表达式。如果条件表达式非常复杂，就可能会牺牲可读性。




# control flow(控制流)
- 如果任何一个条件为True，则其后的elif或else块都不会执行。
- 对于用and或or组成的复合条件，各条件是按从左到右的顺序求值的，而且是短路型的。
- Python中不存在switch语句
- while 循环定义了一个条件和一个代码块,只要条件部位False或循环没有被break显式终止,则代码块将一直不断地执行下去.
- while语句同样可以拥有else子句作为可选项.
- for语句同样可以拥有else子句,它总会在for循环结束后开始执行,除非程序遇到了break语句.
- range()每次只会生成一个数字,如果希望获得完整的序列,要使用```list(range(5))```
- ```for i in range(1,5)``` 等价于 ```for i in [1,2,3,4]```
- for循环用于对集合(列表或元组)或迭代器进行迭代。
- for循环能再任何队列中工作.
- Python中的for和C++中的完全不同,和C#中的foreach相似,和Java1.5中的for (int i : IntArray)没什么区别.
- ```for (int i = 0; i < 5; i++)``` 等价于 ```for i in range(5)```后者更简单,更具表现力,且更不容易出错.
- break 关键字用于使for循环完全退出。
- 如果你中断了一个for或while,那么相应循环中的else块都将不会被执行.
- continue 关键字用于使用for循环提前进入下一次迭代。
- 如果集合或迭代器中的元素是序列类型(比如元组或列表)，那么还可以非常方便地蒋这些元素拆散成for语句中的多个变量
- pass是Python中的“空操作”语句。它可以被用在那些没有任何功能的代码块中。
- 由于Python是根据空白符划分代码块的，所有它的存在是很有必要的。
- 开发一个新功能时，尝尝会将pass用作代码中的占位符。



# Modules(模块)
- 如果你想在你所编写的别的程序中重用一些函数的话,答案是模块(Modules).
- 最简单编写模块的方法便是创建一个包含函数,变量以.py为后缀的文件.
- 另一种方法时编写Python解释器本身的本地语言.你可以使用C来编写Python模块,并在编译后,通过Python解释器在Python代码中使用它们.
- 标准库就是一系列模块.
- sys模块包含了与Python解释器及其环境相关的功能,也就是所谓的系统功能(system)
- 初始化工作只需在我们第一次导入模块时完成.
- ```sys.argv```包含了命令行参数(Command Line Arguments),这一列表,也就是使用命令行传递程序的参数.
- ```sys.path``` Python解释器首先会寻找模块,它会从它的sys.path变量所提供的目录中进行搜索.该目录包括了包含导入模块的字典名称列表.第一段字符串是空的,它代表程序启动的目录,这意味着你可以直接导入位于启动目录中的模块.否则,你必须将模块放置在sys.path内所列出的目录中.
- ```import os; print(os.getcwd())```可以用来查看目前程序所在目录.



# tuple(元组)
- Python 的数据结构简单而强大。精通其用法是称为专家级Python程序员的关键环节。
- tuple 元组是一种一维的、定长的、不可变的Python对象序列。最简单的创建方式是一组以逗号隔开的值，在更复杂的表达式中定义元组时，常常需要用圆括号将值围起来。
- 通过调用tuple()任何序列或迭代器都可以被转换为元组
- 跟大部分其他序列类型一样，元组的元素也可以通过方括号[]进行访问。序列是从0开始索引的。
- 虽然存储在元组中的对象本身可能是可变的，但一旦创建完毕，存放在各个插槽中的对象就不能在被修改了。
```Python
tup = tuple(['foo', [1, 2], True])
tup[1].append(3)
```
- 元组可以通过 + 运算符连接起来以产生更长的元组
- 对一个元组乘以一个整数，相当于是连接该元组的多个副本。注意对象本身不会被复制的，这里涉及的只是他们的引用
- 如果对元组型变量表达式进行赋值，Python就会尝试将等号右侧的值进行拆包(unpacking),嵌套元组也能被拆包。
- 利用上述功能可以非常轻松地交换变量名。 b, a = a, b
- 变量拆包功能常用于对由元组或列表组成的序列进行迭代，另一个常见的用法是处理从函数中返回多个值。
```Python
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    pass
```
- 由于元组的大小和内存不能被修改，所以实例方法很少。最有用的是count(列表也是如此)。计算指定值出现的次数。 



# list(列表)
- 跟元组相比，列表(list)是变长的，而且其内容也是可以修改的。它可以通过[] 和 list() 进行定义。
- .append .insert .pop .remove .extend .sort
- insert 的计算量要比 append 大，因为后续的引用必须被移动，以便为新元素腾地方。
- 如果不考虑(使用append和remove时的)性能，Python列表可以是一种非常不错的“多重集合”数据结构。
- 通过 in 关键字，可以判断列表中是否含有某个值。
- 注意，判断列表是否含有某个值的操作比字典(dict)和集合(set)慢得多，因为Python会对列表中的值进行先行扫描，而另外两个(基于哈希表)则可以瞬间完成判断。
- 跟元组一样，用 + 将两个列表加起来即可实现合并。
- 对于一个已定义的列表，可以用extend方法一次性添加多个元素。
- 注意，列表的合并是一种相当费资源的操作，因为必须创建一个新的列表并将所有对象赋值过去。而用extend将元素附加到现有列表(尤其是在构建一个大列表时)就会好很多。
- 调用列表的sort方法可以是想爱你就地排序(无须创建新的对象)。
- sort有几个很不错的选项。一个是次要排序键，即一个能够产生可用于排序的值的函数。b.sort(key=len)
- 二分搜索及维护有序列表：内置的bisect模块实现了二分查找以及对有序列表的插入操作。
- bisect.bisect 可以找出新元素应该被插入到那个位置才能保持原列表的有序性，而bisect.insort则确实地将新元素插入到那个位置上去。
- bisect模块的函数不会判断原列表是否是有序的，因为这样做开销太大了。因此，将它们用于无序列表虽然不会报错，但是可能会导致不正确的结果。
- 通过切片标记法，你可以选取序列类型(数组、元组、NumPy数组等)的子集，其基本形式由索引运算符[]以及传入其中的 start:stop 构成。
- 切片还可以被赋值为一段序列： seq[3:4] = [6:3]
- 由于start索引处的元素是被包括在内的，而stop索引处的元素是未被包括在内的，所以结果中的元素数量是stop - start
- start或stop都是可以省略的，此时他们分别默认为序列的起始处和结尾处。
- 负数索引从序列的末尾开始切片。
- 还可以在第二个冒号后面加上步长(step)。比如每个一位取出一个元素： seq[::2]
- 上述方法使用-1是一个很巧妙的办法，它可以实现列表或元组的反序： seq[::-1]
- enumerate 可以逐个返回序列的(i, value)元组
- mapping = dict((value, i) for i, value in enumerate(some_list): 求取一个序列值映射到其所在位置的字典。
- sorted函数可以将任何序列返回为一个新的有序列表，
- sorted和set结合起来可以的到一个由序列中唯一元素组成的有序列表sorted(set('this is just some string'))
- zip 用于将多个序列(列表、元组)中的元素“配对”，从而产生一个新的元组列表。
- zip 可以接受任意数量的序列，最终的到的元组数量由最短的序列决定。
- zip 最常见的用法是同时迭代多个序列，还可以结合enumerate一起使用
- 对于“已压缩的”(zipped)序列，zip还可以对该序列进行“解压”(unzip)。其实就是将一组行转换为一组列。
- first_names, last_names = zip(*names)
- 函数调用中星号(*seq)相当于： (seq[0], seq[1],...,seq[len(seq)-1])
- reversed 用于按逆序迭代序列中的元素： list(reversed(range(10)))



# dict(字典)
- 字典(dict)可算是Python中最重要的内置数据结构。
- 它更常见的名字是哈希映射(hash map)或相联数组(associative array)。
- 它是一种大小可变的键值对集，其中的键(key)和值(value)都是python对象。
- 创建字典的方式之一是：使用大括号{}并用冒号:分隔键和值。
- 判断字典中是否存在某个键，语法和在列表和元组中判断是否存在某个值是一样的：'b' in d1
- 使用del关键字或pop()方法(删除指定值后将其返回)可以删除值。
- keys()和values()方法分别用于获取键和值的列表。虽然键值对没有特定的顺序，但这两个函数会以相同的顺序输出键和值。
- 在python 3中，dict.keys()和dict.values()会返回迭代器而不是列表。
- 利用update()方法，一个字典可以被合并到另一个字典中去。
- 字典本质上就是一个二元元组集，所以我们完全可以用dict()类型函数直接处理二元元组列表 dict(zip(range(5), reversed(range(5))))
- 字典推导式是构建字典的另一种优雅的方式。
- dict的get和set方法可以接受一个可供返回的默认值，value = some_dict.get(key, default_value),
- value = some_dict.get(key) 如果key不存在，则get默认返回None， 而pop则会引发一个异常。
- 在设置值的时候，常常会将字典中的值处理成别的类型(比如列表).
```Python
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)
```
- 字典的setdefalut方法刚好能达到上述的目的,上面的if-else模块可以写成 
```Python by_letter.setdefalut(letter, []).append(word)```
- 内置的collections模块有一个教做defalutdict的类,它可以使上述过程更简单.传入一个类型或函数(用于生成字典各插槽所使用的默认值)即可创建出一个defalutdict
```Python
from collections import defaultdict
by_layer = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
```
- defaultdict的初始化器只需要一个可调用对象(例如各种函数),并不需要明确的类型.因此,如果你想要将默认值设置为4,只需传入一个能返回4的函数```Python counts = defaultdict(lambda: 4) ```
- 虽然字典的value可以是任何Python对象,但是key必须是不可变对象,如标量类型(如:整数\浮点数\字符串)或元组(元组中的所有对象也必须是不可变的)
- 上述内容的术语是可哈希性(hashability)或者翻译成可散列性.
- 通过hash函数,你可以判断某个对象是否是可哈希的(即可以用作字典的键): hash("string")
- 如果要将列表当做键,最简单的办法就是将其转换成元组:dict1[tuple([1, 2, 3])] = 5


# set(集合)
- 集合(set)是由唯一元素组成的无序集.
- 可以将其看成是只有键而没有值的字典.
- 集合的创建方式有二:使用set()函数,或用大括号包起来的集合字面量.
- 集合支持各种数学集合运算,如并(或)(|)\交(与)(&)\差(-)以及对称差(异或)(^)等.
- 可以判断一个集合是否是另一个集合的子集(原集合包含于新集合)或超集(原集合包含新集合)
```Python
{1, 2, 3}.issubset(a_set)
a_set.issupperset({1, 2, 3})
```
- 不难看出,如果两个集合内容相等,则他们就是相等的: {1, 2, 3} == {3, 2, 1}


# comprehensions(推导式)
- 列表推导式是最受欢迎的Python语言特性之一.
- [expr for val in collection if condition]
```Python
result = []
for val in collection:
    if condition:
        result.append(expr)
```
- 集合和字典的推导式是该思想的一种自然延伸,语法差不多.
```Python
- dict_comp = {key-expr : value-expr for value in collection if codition}
- set_comp = {expr for value in collection if condition}
```
```Python
    strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
    loc_mapping = {val : index for index, val in enumerate(strings)}
```
```Python
    some_tuples = [(1,2,3), (4, 5, 6), (7, 8, 9)]
    flattened = [x for tup in some_tuples for x in tup if x > 5]
    # 用嵌套for循环实现上述功能
    flattened = []
    for tup in some_tuples:
        for x in tup
            if x > 5:
                flattened.append(x)
```
- 你可以编写任意多层的嵌套,但是如果嵌套超过两三层的话,可能你就得思考一下数据结构设计有没有问题了.
- 一定要注意上述内容和"列表推导式中的列表推导式"之间的区别:如下语句是正确的,但结果不同.
```Python 
[[x for x in tup] for tup in some_tuples]
```



# function(函数)
- 函数是Python中最主要也是最重要的代码组织和重复手段.
- 我严重认为大部分程序员在做数据分析工作时所编写的函数不够多.
- 函数是用def关键字声明的.
- 如果到达函数末尾时没有遇到任何一个return语句,则返回None
- 函数可以有一些位置参数(Position)和一些关键字参数(keyword).关键字参数常用于指定默认值或可选参数.
- 函数参数的主要限制在于:关键字参数必须位于位置参数之后.
- 你可以以任何顺序指定关键字参数.也就是说,你不用死记硬背函数的关键字参数顺序,只要记得他们的名字就可以了.


## namespace(命名空间),scope(作用域),以及local(局部)
- 当你在一个函数的定义中生命变量时,它们不会以任何方式与身处函数之外但具有相同名称的变量产生关系.
- 函数可以访问两种不同作用域中的变量:全局(global)(next-to-last)和局部(local)(innermost).
- Python有一种更科学的用于描述变量作用域(scope)的名称,即命名空间(namespace).
- 任何在函数中赋值的变量默认都是被分配到局部命名空间(local namespace)中的.
- 你可以使用定义于函数之外的变量值(函数中没有同名变量).然而,这种方式不会受到孤立而且应该避免,因为它使程序含糊不清.
- 局部命名空间是在函数被调用时创建的,函数参数会立即填入该命名空间.在函数执行完毕后,局部命名空间就会被销毁(除了闭包).
- 虽然可以在函数中对全局变量进行赋值操作,但是那些变量必须用global关键字声明成全局的才行.
- 我常常建议人们不要频繁使用global关键字.因为全局变量一般是用于存放系统的某些状态的.
- 使用global时,将影响到我们在主代码块中使用相同名称的值.
- 如果你发现自己用了很多global,那可能就说明要用类了.
```Python
a = []  # a is global variable
def bind_a_variable():
    global a
    for i in range(5):
        a.append(i)
```
- 可以在任何位置进行函数生命,即使是局部函数(在外层函数被调用之后才会被动态创建出来)也是可以的.
- 严格意义上来说,所有函数都是某个作用域的局部函数,这个作用域可能刚好就是模块级的作用域.Built-in(outtermost)


## arguments(参数)
- 对于一些函数,你可能希望使用一些参数可选并使用默认值,以避免用户不想为他们提供值.可以使用默认参数值.
- 要注意,默认参数值应该是常数.更确切地说,默认参数值应该是不可变的.
- 只有位于参数列表末尾的参数才能被赋予默认参数值.```def func(a=5, b)```是无效的.
- 如果你有一些具有许多参数的函数,而你又希望只对其中一些进行指定,那么可以通过命名它们来给这些参数赋值.
- 关键字参数-我们使用命名(关键字)而非位置(一直以来我们所使用的方式)来指定函数中的参数.
- 关键字参数有量大优点:
    - 我们不再需要考虑参数的顺序,函数的使用将更加容易.
    - 我们可以只对那些我们希望赋予的参数赋值,只要其它的参数都具有默认参数.
- 有时你可能想定义的函数里面能够有任意数量的变量,也就是参数数量是可变的,这可以通过使用星号来实现.
    - 当我们声明一个*param时,从此处开始直到结束的所有位置参数(Positional Arguments)都将被汇集成一个称为param的元组(Tuple)
    - 当我们生命一个**param时,从此处开始直到结束的所有关键字参数都将被汇集成一个名为param的字典(Dictionary)


## return(返回值)
- 如果函数没有return语句则默认返回None,即没一个函数都在其末尾隐含了一句```return None```
- 如果return语句没有搭配任何一个值,则代表返回None
- 使用pass可以让函数不使用默认的return
- 函数可以返回多个值.其实只返回了一个对象,也就是一个元组,最后该元组会被拆包到各个结果变量中.
- 还有一种非常具有吸引力的多值返回方式,返回字典:return {'a' : a, 'b' : b, 'c' : c}
```Python
def f():
    a = 5
    b = 6
    c = 7
    return a, b, c
    # return {'a': a, 'b': b, 'c': c}
a, b, c = f()
```


## DocStrings(文档字符串)
- 函数的第一行中的逻辑行中的字符串时该函数的文档字符串(DocString).
- 文档字符串也适用于模块(Mudules)与类(Class)
- 编写约定:第一行以某一大写字母开始，以句号结束。第二行为空行，后跟的第三行开始是任何详细的解释说明.
- 使用函数的__doc__属性来获取其文档字符串.
- help()函数的用途便是获取函数的__doc__属性,并以一种整洁的方式呈现.
- 自动化工具可以以这种方式检索你程序中的文档.
- 你的Python发型版中附带的pydoc命令与help()使用文档字符串的方式类似.


## 函数亦为对象
- 由于Python函数都是对象,因此,在其他语言中较难表达的一些设计思想Python中就要简单很多了.
```Python
import re  # 正则表达式模块
states = ['  Alabama ', 'georgia!', 'Georgia', 'georgia', 'FIOrIda', 'south    carolina##',  'West virginal?']
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)
clean_ops = [str.strip, remove_punctuation, str.title]
def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value)
        result.append(value)
    return result
clean_strings(stats, clean_ops)
```
- 上面例子中的多函数模式使你能再很高的层次上轻松修改字符串的转换方式.此时的clean_strings也更具有可重复性!
- 还可以将函数用作其他函数的参数,比如内置的map函数: map(remove_punctuation, states)


## 匿名(mambda)函数
- Python 中有一种被称为匿名函数或lambda函数的东西,其实是一种非常简单的函数:仅由单条语句组成,该语句的结果就是返回值.
- 它们是通过lambda关键字定义的,这个关键字没有别的含义,仅仅是说"我们正在生命的是一个匿名函数"
```Python
def short_function(x):
    return x * 2
equiv_anon = lambda x: x * 2
```
- lambda函数在数据分析中非常方便,因为你会发现很多数据转换函数都以函数作为参数的.直接传入lambda函数比编写完整函数声明要少输入很多字(也更清洗),甚至比将lambda函数赋值给一个变量还要少输入很多字.
```Python
def apply_to_list(some_list, f):
    return [f(x) for x in some_list]
ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)  # 这里我们非常轻松的传入一个自定义运算符给apply_to_list
```
- 根据各字符串不同字母的数量对其进行排序: strings.sort(key = lambda x: len(set(list(x))))
- lambda函数之所以会被称为匿名函数,原因之一就是这种函数对象本身是没有提供名称属性的.


## 闭包:返回函数的函数
- 闭包(closure)不是什么很可怕的东西.如果用对了敌方,他们其实可以非常强大!
- 简而言之,闭包就是由其他函数动态生成并返回的函数.
- 其关键性质是,被返回的函数可以访问其创建者的局部命名空间中的变量.
- 闭包和标准Python函数之间的区别在于:即使其创建者已经执行完毕,闭包仍能继续访问其创建这的局部命名空间.
```Python
def make_watcher():
    have_seen = {}
    def has_been_seen(x):
        if x in have_seen:
            return True
        else:
            have_seen[x] = True
            return False
    return has_been_seen
vals = [5, 6, 1, 5, 1, 6, 3, 5]
[make_watcher(x) for x in vals]
```
- 注意一个技术限制:虽然可以修改任何内部状态对象(比如向字典添加键值对),但不能绑定外层函数作用域中的变量.
- 一个解决办法是:修改字典或列表,而不是绑定变量. 
```Python
def make_counter():
    count = [0]
    def counter():
        count[0] += 1
        return count[0]
    return counter
```
- 在实际工作中,你可以编写带有大量选项的非常一般化的函数,然后再组装出更简单更专门化的函数.
```Python
def format_and_pad(template, space):
    def formatter(x):
        return (template % x).rjust(space)
    return formatter
fmt = format_and_pad('%.4f', 15)
fmt(1.756)
```
- 这种模式其实也能用类来实现(虽然会更啰嗦一点)
- 闭包外部参考:
    - 当内嵌函数引用了包含它的函数(enclosing function)中的变量后，这些变量会被保存在enclosingfunction的__closure__属性中,成为enclosing function本身的一部分；也就是说，这些变量的生命周期会和enclosing function一样。
    - 闭包只是在表现形式上跟函数类似，但实际上不是函数。
    - 闭包在运行时可以有多个实例，不同的引用环境(这里就是prefix变量)和相同的函数(这里就是greeting)组合可以产生不同的实例。
    - 在Python中创建一个闭包可以归结为以下三点：
        - 闭包函数必须有内嵌函数
        - 内嵌函数需要引用该嵌套函数上一级namespace中的变量
        - 闭包函数必须返回内嵌函数


## 扩展调用语法和*args, **kwargs
- 在Python中,函数参数的工作方式其实很简单.
- 当编写func(a, b, c, d=some, e=value)时,位置和关键字参数分别是被打包成元组和字典.函数实际接收到的是一个元组args和一个字典kwargs.
```Python
a, b, c = args
d = kwargs.get('d', d_default_value)
e = kwargs.get('e', e_defalut_value)
```
```Python
def say_hello_then_call_f(f, *args, **kwargs):
    print 'args is', args
    print 'kwargs is' kwargs
    print("hello! Now I'm going to call %s" % f)
    print f(*args, **kwargs)
def g(x, y, z=1):
    return (x + y) / z
```


## 柯里化:部分参数应用
- 柯里化(currying)是一个有趣的计算机科学术语,它指的是通过"部分参数应用"(partial argument application)从现有函数派生出新函数的技术.
```Python
def add_number(x, y):
    return x + y
add_five = lambda y: add_number(5, y)
```
- add_number的第二个参数称为柯里化的(curried).这里没什么特别的东西,其实就只是定义了一个可以调用现有函数的新函数而已.
- 内置的functools模块可以用partial函数将此过程简化
```Python
from functools import partial
add_five = partial(add_numbers, 5)
```


## 生成器
- 能以一种一致的方式对序列进行迭代(比如列表中的对象或文件中的行)是Python的一个重要特点.
- 这是通过一种叫迭代器协议(iterator protocol,它是一种使对象可迭代的通用方式)的方式实现的.
- 当你编写```Python for key in some_dict ``` 时Python解释器受限会尝试从some_dict创建一个迭代器:
```Python
dict_iterator = iter(some_dict)
```
- 迭代器是一种特殊对象,它可以在诸如for循环之类的上下文中向Python解释器传送对象.
- 大部分能接收列表之类的对象的方法也都可以接受任何可迭代对象.
- 生成器(generator)是构造新的可迭代对象的一种简单方式.
- 一般的函数执行后只会返回单个值,而生成器则是以延迟的方式返回一个值序列,即每返回一个值之后暂停,直到下一个值被请求时再继续.
- 要创建一个迭代器,只需将函数中的return替换为yeild即可.
```python
def squares(n=10):
    print 'Generating squares from 1 to %d' % (n ** 2)
    for i in xrange(1, n + 1):
        yield i ** 2
```
- 调用改生成器时,没有任何代码会被立即执行,直到你从该生成器中请求元素时,它才会开始执行代码.
```python
gen = squares()
for x in gen:
    print x,
```
找出"将1美元(即100美分)兑换成任意一组硬币"的所有唯一方式.
```python
def make_change(amount, coins=[1, 5, 10, 25], hand=None):
    hand = [] if hand is None else hand
    if amount == 0:
        yield hand
    for coin in coins:
        if coin > amount or (len(hand) > 0 and hand[-1] < coin):
            continue
        for result in make_change(amount - coin, coins = coins, hand = hand + [coin]):
            yield result


for way in make_change(100, coins =[10, 25, 50]):
    print way
```

### 生成器表达式
- 生成器表达式(generator expression)是构造生成器的最简单方式.生成器也有一个类似于列表,字典,集合推导式的东西,其创建方式为,把列表推导式两端的方括号改成圆括号:
```python
gen = (x ** 2 for x in xrange(100))
```
- 生成器表达式可用于任何接受生成器的Python函数
```python
sum(x ** 2 for x in xrange(100)
dict((i, i ** 2) for i in xrange(5))
```

### itertools模块
- 标准库itertools模块中有一组用于许多长剑数据算法的生成器.
> 书中这部分内容没理解.

#  file and operating system(文件和操作系统)
- Python文件处理很简单,这也是Python在文本和文件处理方面流行的原因.
- 为了打开一个文件以便读写,可以使用内置的open()函数以及一个相对或绝对文件路径.
```python
path = 'ch13/segismundo.txt' # 相对路径
f = open(path)
```
- 默认,文件是以只读('r')打开的.然后我们可以像处理列表那样来处理这个文件句柄f.
- 从文件中取出的行都带有完整的行结束符(EOL),为得到一组没有EOL的行:
```python
line = [x.rstrip() for x in open(path)]
```
如果用'w'模式打开文件,就会有一个新文件创建在path中表示的位置,并覆盖掉该位置原来的任何数据.
要将文本写入文件,可以使用该文件的write或writelines方法.
```python
with open('tmp.txt', 'w') as handle:
    handle.writelines(x for x in open(path) if len(x) >1)

open('tmp.txt').readlines()
```

**Python的文件模式**
模式 | 说明
---|---
r | 只读模式
w | 只写模式.创建新文件(删除同名的任何文件)
a | 附加到现有文件(如果文件不存在则创建一个)
r+ | 读写模式
b | 附加说明某模式用于二进制文件, 即'rb'或'wb'
U | 通用换行模式.单独使用'U'或附加到其他读模式(如'rU')

**重要的Python文件方法或属性**
方法 | 说明
---|---
read([size]) | 以字符串形式返回文件数据,可选的size用于说明读取的字节数
readlines([size]) | 将未见返回为行列表,可选参数size
write(str) | 将字符串写入文件
close() | 关闭句柄
flush() | 清空内部I/O缓存区,并将数据强行写回磁盘
seek(pos) | 移动到指定的文件位置(整数)
tell() | 以整数形式返回当前文件位置
closed | 如果万能键已关闭,则为True 




# 异常处理
- 优雅地处理Python错误或异常是构建健壮程序的重要环节。
```Python
def attempt_float(x):
    try:
        return float(x)
    '''
    只需要编写一个由异常类组成的元组，即可捕获多个异常，
    但是TypeError(输入的参数不是字符串或数值)可能意味着程序中存在合法性bug。
    '''
    except (TypeError, ValueErroe): 
        return x
# -----------------
f = open(path, 'w')
try:
    write_to_file(f)
except:
    print 'Failed'      # except 后面加上异常类型可以只针对某种异常进行处理
else:
    print 'Succeeded'   # 只在try块成功时执行
finally:
    f.close()           # 文件句柄f适中都会被关闭
```
- 对于非常长的范围，建议使用xrange，其参数跟range一样，但它不会预先产生所有的值并将他们保存到列表中(可能会非常大)，而是返回一个用于逐个产生整数的迭代器。
- 在Python 3中，range始终返回迭代器，因此也就没有必要使用xrange函数了。





IPython
================================================================================
- reset 重置所有变量
- evn 显示环境变量
## about IPython
- execute explore & edit-complie-run
- 输出的可读性更好，和 print 的普通输出形式有着显著区别。
- IPython 和主流编辑器、IDE 之间的交互。
- 我们非常有必要了解 Python 标准库、NumPy、pands 以及本书中所用到的其他库的性能特点。在大型数据分析应用程序中，这些不起眼的毫秒数是会不断累积的。


## Tab 
- 当前命名空间中任何与已输入的字符串相匹配的变量(对象、函数)都会被找出来。
- 甚至是文件路径(/)
- 函数关键字参数


## object introspection (内省)
- 在对象前面或后面加上一个 ？ 就可以将有关该对象的一些通用信息显示出来。
- 如果该对象是一个函数或实例方法，则其 docstring (如果有的话) 也会被显示出来。使用 ?? 还将显示其源代码。
- ? 还可以搜索 IPhone 命名空间，再配以通配符 * 即可显示出所有与之相匹配的名称。


## Execute the code in the clipboard
- 使用 Ctrl-V 的方式粘贴代码是模拟在 Python 中逐行输入代码，换行符会被处理为 <return> ，我们应该使用 %paste 或 %cpaste 这两个魔术函数。
- %paste 可以承载剪贴板中的一切文本，并在 shell 中以整体形式自动执行。
- %cpaste 在最终执行之前，想粘贴多少代码就粘贴多少。最终使用 -- 加回车，以整体形式手动执行。Ctrl-C 可以终止 %cpaste 提示符。


## Shortcuts
- Ctrl-P 或上箭头     # 向后搜索历史中以当前输入的文本开头的命令
- Ctrl-N 或下箭头     # 向前搜索历史中以当前输入的文本开头的命令
- Ctrl-R              # 按行读取的方向历史搜索(部分匹配)
- Ctrl-V              # 从剪贴板粘贴文本
- Ctrl-C              # 终止当前正在执行的代码
- Ctrl-A              # 将光标移动到行首
- Ctrl-E              # 将光标移动到行尾
- Ctrl-K              # 删除光标从开始至行尾的文本
- Ctrl-U              # 清楚当前行的所有文本
- Ctrl-F              # 将光标向前移动一个字符
- Ctrl-B              # 将光标向后移动一个字符
- Ctrl-L              # 清屏
- Ctrl_J              # Enter


## %run
- 脚本是在一个命名空间中运行的，所以其行为应在跟在标准命令环境中执行时一样。此后，该文件中定义的全部变量就可以在当前 IPython shell 中访问了。
- 如果希望脚本能够访问在交互式 IPython 命名空间(interactive)中定义的变量，就应该使用 %run -i
- 任何代码在执行时，只要按下"Ctrl-C"，就会引发一个 KeyboardInterrupt。除一些非常特殊的情况之外，绝大部分 Python 程序都将立即停止执行。
- 当 Python 代码已经调用了某个已编译的扩展模块时，"Ctrl-C"将无法立即停止执行。要么等待 Python 解释器重获控制权，要么只能任务管理器强制终止。


## Exception and trace
- 如果 %run 发生了异常，IPython 默认会输出整个调用traceback(栈跟踪)，其中还会附上调用栈各点附近的上下文参考。
- %xmode 可以控制上下文代码参考的数量。
- post-mortem debugging (事后调试)


## Magic Command
- ?           # See the help
- %quickref   # Show a quick reference sheet
- %magic      # Pint information about the magic function system
- %debug      # Activate the interactive debugger.
- %hist       # Alias for '%history'.
- %pdb        # Control the automatic calling of the pdb intercative debugger.
- %paste      # Paste & execute a pre-formatted code block from clipboard.
- %cpaste     # Paste & execute a pre-formatted code block from clipboard.
- %reset      # Resets the namescape by removing all names defined by the user.
- %page       # Pretty print the objet and display it through a pager.
- %run        # Run the named file inside IPython as a program.
- %who        # Print all interactive variables, with some minimal formatting.
- %whos       # Like %who, but gives some extra information about each variable.
- %xdel       # Delete a variable, trying to clear it from anywhere that.
- %logstart   # logging anywhere in a session
- %logoff
- %logon
- %logstate
- %logstop


## GUI console based on QT
- ipython qtconsole --pylab=inline


## matpoltlib & pylab mode
- 标准 Python shell 中创建一个 matplotlib，GUI的事件循环会接管 Python 会话的控制权。
- ipython --pylab 标记来集成 matplotlib


## 搜索并重用历史命令
- 只需要很少的按键次数即可搜索、自动完成并执行之前已经执行过的命令。
- 在会话间持久化命令历史。
- 将输入、输出历史记录到日志文件。


## 输入和输出变量
- Ipython 会将输入和输出的引用保存在一些特殊的变量中。最近两个输出结果分别保存在 _ 和 __ 中。
- _27 第27行的输出变量
- _i27 第27行的输入变量，由于输入变量是字符串，因此可以用 exec 关键字重新执行。
- 在处理非常大的数据集时，一定要注意 IPython 的输入输出历史，它会导致所有的对象引用都无法被垃圾收集器处理(即施放内存)，对于这种情况，谨慎地使用 %xdel 和 %reset 将有助于避免出现内存方面的问题。


## 与操作系统交互
- 在 IPython 中，以感叹号开头的命令行表示气候的所有内容需要在系统 shell 中执行。
- 将 shell 命令的控制台输出存放到变量中： ip_info = !ipconfig
- 使用当前环境中定义的 Python 值。 只需在变量名钱加上 $ 即可： ！ls $var_name
- !cmd                # Run cells with cmd in a subprocess.
- output = !cmd args
- %alias
- %bookmark           # Manage IPython's bookmark system. 与别名的区别在于，他们会被自动持久化。
-     %bookmark-l     # list all bookmarks 
- %cd
- %pwd
- %pushd
- %popd
- %dirs
- %dhist
- %env
- %alias              # Define an alias for a system command.


## 交互式调试器
- 调试代码的最佳时机就是错误刚刚发生时。在发生异常之后马上输入 %debug 命令，将会调用事后调试器，并直接跳转到引发异常的那个栈帧(stack frame)。
- 要想精通这个交互式调试器，必须经过大量的实践才行。在 IPython 中调试程序往往会带来更高的生产率。
- 输入 u(up) d(down) 即可在栈跟踪的各级别之间切换
- %pdb                # Contro the automatic calling of the pdb interactive debugger.
- (I)Python 调试器命令
    - h(elp)          # 显示命令列表
    - help            # 显示 command 的文档
    - c(ontinue)      # 恢复程序的执行
    - q(uit)          # 退出调试器，不再执行任何代码
    - b(reak) [number]# 在当前文件的第 [number] 行设置一个断点
    - b path/to/[file.py:number]   # 在指定文件的第 [number] 行设置一个断点
    - s(tep)          # 单步进入函数调试
    - n(ext)          # 执行当前行，并前进到当前级别的下一行
    - u(p)/d(own)     # 在函数调用栈中向上或向下移动
    - a(rgs)          # 显示当前函数的参数
    - debug [statmenet]   # 在新的(递归)调试器中调用语句 [statment]
    - l(ist) [statment]   # 显示当前行，以及当前栈级别上的上下文参考代码
    - w(here)         # 打印当前位置的完整栈跟踪(包括上下文参考代码) 
- pdb.set_trace


## 性能分析
- %time               # Time execution of a Python statement or expression.
- %timeit             # Time execution of a Python statement or expression. Many times to perform.
- %prun               # Run a statement through the python code profiler.
- $run -p
- %lprun


## IPython HTML Notebook
- 基于 Web 技术的交互式计算文档格式。它已经称为一种非常棒的交互式计算工具，同时还是科研和教学的一种理想媒介。
- 它有一种基于 JSON 的文档格式 .ipynb, 使你可以轻松分享代码、输出结果以及图片等内容。将 .ipynb 文件发布到网上以供所有人查阅。
- IPython Notebook 应用程序是一个运行于命令行上的轻量级服务器进程。
- ipython notebook --pylab=inline 可以启动 IPython Notebook 服务器。


HardWay
================================================================================
- 多行注释第一个"""必须在一行的行首"""       
- print() 用于输出内容
    - print("text", end=''), end=''用于指定text后面的字符，默认是 \n 会在一行的结尾有一个 \n
    - 打印出来后我的字符串前面有个 u ，像 u'35' 这样。 它表示 Python 告诉你你的字符串是 unicode。使用 %s 就一切正常了。 
    - 用%r输出会按照写出来的方式（或者近似方式）打印，它是用来debug的原始格式。
    - 三个引号 """ 可以定义多行字符串，而 % 是字符串的格式化工具 """。  
-'python -m pydoc docstring' pydoc模块可以从python代码中获取docstring，然后生成帮助信息。
    - python -m pydoc -w atexit   //在当前目录创建atexit.html，生成HTML输出
    - python -m pydoc -p 5000    //启动一个Web服务器监听http://localhost:5000/在线浏览帮助文档
    - 命令行参数是字符串，就算你在命令行输入数字，你也需要用 int() 把它先转成数字。
- input() 用于获取用户输入
    - python3.x系列不再有 raw_input 函数。3.x中 input 和从前的 raw_input 等效
- open(file_name) 返回一个 file_obj，这个 object 本身并不是文件的内容。 
    - 可以把它想象成一个磁带机。可以随意访问内容的任意位置，并且它有一个用来读取数据的“磁头”，你可以通过这个“磁头”来操作文件。 
    - Python 不会限制你打开文件的次数，事实上有时候多次打开同一个文件是一件必须的事情。
    - file_obj.truncate([size]) 方法用于从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除。
    - 如果你用 open(file_name,'w') 模式打开文件，那么 file_obj.truncate() 不是必须的，因为 open(file_name,'w') 会"truncating the file first"。
- 'import' 用于从外部导入其他python功能模块，也可以作为提示，在读代码时了解代码用到了哪些功能。我们把这些导入的功能称作模组。也有人称作“库(libraries)”。
    - 'from sys import argv' sys 是一个代码库，这句话的意思是从库里取出 argv 这个功能来，供我使用。
        - argv 参数变量(argument variable)，是一个非常标准的编程术语。在其他的编程语言里你也可以看到它。这个变量包含了你传递给 Python 的参数。
        - argv 解包(unpack)，将运行时的所有参数放到 argv 里。它的含义很简单：“把 argv 中的东西解包，将所有的参数依次赋予左边的变量名”。
    - 'import os' 导入os模块
        - os.getcwd() #获取当前路径
        - os.chdir("D:\\test") #跳到目标路径下 
    - 'from os.path import exists' 
        - exists() 这个函数将文件名字符串作为参数，如果文件存在的话，它将返回 True，否则将返回 False
- read() 一旦运行， 文件就会被读到结尾并且被 close 掉
- write()
    - file.write("stuff") 在 file.close() 后才会真正写入文件内容。
    - round() 除非对精确度没什么要求,否则尽量避开用 round() 函数。对浮点数精度要求如果很高的话，用 decimal 模块。
    - 'def function(*args)' 中的 * 的功能是把函数的所有参数都接受进来，然后放到名字叫 args 的列表中去。和 argv 差不多，只不过前者是用在函数上面，但一般不常用。
        - 函数的参数的个数限制取决于 Python 的版本和操作系统，不过就算有限，限值也是很大的。实际应用中，5 个参数就不少了，再多就会让人头疼了。
- seek() 方法用于移动文件读取指针到指定位置。该函数没有返回值。
    - file_obj.seek(offset[, whence])
    - offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
    - whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；
        - 0代表从文件开头开始算起，
        - 1代表从当前位置开始算起，
        - 2代表从文件末尾算起。   
    - 函数的处理对象是字节而非行，所以 seek(0) 只是转到文件的 0 byte，也就是第一个 byte 的位置。            
- readline() 里边的代码会扫描文件的每一个字节，直到找到一个 \n 为止，然后它停止读取文件，并且返回此前的文件内容。
    - 函数返回的内容中包含 \n
        - file_obj.readline() 文件对象会记录每次调用 readline() 后的读取位置。
- pass 就是什么也不做，只是为了防止语法错误。
- '__future__' Python 3.x 引入了一些与 Python 2 不兼容的关键字和特性，在 Python 2 中，可以通过内置的 __future__ 模块导入这些新内容。如果希望在 Python 2 环境下写的代码也可以在 Python 3.x 中运行，建议使用 __future__ 模块，它必须放在文件的开头。
    - 'from __future__ import print_function' 在 python 2 中使用 print('xxx',end = ' ') 格式的 print() 函数
- range(n1, n2, setp) 函数会从第一个数到最后一个，但不包含最后一个数字。所以它在n2-1的时候就停止了。这种含首不含尾的方式是循环中极其常见的一种用法。setp 指定两个数之间相隔的步幅。
- elements.append(element) 的功能是在列表的末尾追加元素。
- for-loop 
    - 在循环开始时就定义了循环变量，当然每次循环它都会被重新定义一次
    - for-loop 只能对一些东西的集合进行循环，while-loop 可以针对任意对象进行循环。
    - 一般任务用 for-loop 更加容易一些。
- while-loop 检查布尔表达式的真假，执行下面的代码，完后再回到 while 所在位置，如此重复进行，直到 while 表达式为 False 为止。
    - 尽量少用 while-loop，大部分时候使用 for-loop 是更好的选择。
    - 重复检查你的 while 语句，确定测试的布尔表达式最终会变为 False。
    - 如果不确定，就在 while-loop 的结尾打印出测试值，看看它的变化。
- #coding=gbk
    - 直接使用 u'中文' 形式，指明以unicode编码,解码方式会以顶部 #coding定义的编码方式，如果不写，以操作系统当前编码方法，建议写上#coding，因为要让操作系统编码和源文件编码经常会不一样。推荐使用这种方式。
- import random
    - random.random() // 0~1 的随机浮点数
    - random.uniform(a, b) // a~b 的随机浮点数
    - random.randint(a, b) // a~b 的随机整数
    - random.randrange([start,]stop[,step]) // 按指定基数递增的集合中 获取一个随机数
    - random.choice(sequence) // 从序列中获取一个随机元素
    - random.shuffle(lst) // 将一个列表中的元素打乱
    - random.sample(sequence,k) // 从指定序列中随机获取指定长度的片断
- iPython 
    - http://ipython.org/ 
    - IPython 是一个加强版的交互式 Shell
    - IPython 3 是整合 IPython 所有功能发布的最后一个版本。在新的版中，语言无关的代码，例如 notebook，将会移动到 Jupyter 下发布。
- 数学计算
    - 5 ** 3                  // 立方
    - 17 ** 0.5               // 平方根
    - 8 ** (1.0 / 3)          // 立方根
- error
    - SyntaxError: invalid syntax
        - from 写成 form 
    - ValueError: not enough values to unpack (expected 4, got 3)
        - 传递参数错误，用于解包的参数变量不足（预期为4个，得到3个）
    - ImportError: cannot import name 'arvg'
        - argv 写成 arvg .
    - SyntaxError: from __future__ imports must occur at the beginning of the file
        - from __future__ imports 必须放在文件的开头