# [ColorFormatter](https://github.com/bifidy/ColorFormatter)

## 简介

>附在顶上，[Colors](http://www.packal.org/workflow/colors) 是具有相同功能且更为完善的同类工具，如有相关需求，请优先尝试。

这是一个简单的 [Alfred](http://alfredapp.com/) workflow，使用 python 编写。

主要功能是将表示**颜色**的字符串格式化为代码，省去重复编写的麻烦。

由于结尾讲到的原因，这只是一个实验品，不会再做更新。

不过，源代码依然可以作为制作 workflow 的 Demo，如果你有兴趣参考并自己编写一个 workflow 的话，这里有一篇相对详细的[教程](http://myg0u.com/python/2015/05/23/tutorial-alfred-workflow.html)，作者 [Manyu Gou](https://github.com/wswuai)。

Demo 中唯一有捏捏价值的是 [xmlhandle](https://github.com/bifidy/ColorFormatter/blob/master/source/xmlhandle.py) 中用以生成 XML 的片段，因为 Alfred 展示需要固定格式的 XML，在写其它 workflow 的时候，可以直接拿来用。

诶，其实我的 python 写的蛮烂，阅读代码时有任何不悦的感受，还望轻喷 `m(_ _)m`

## 使用方法

>前提：有一个可以使用 `Workflow` 的 **Alfred**

1. 下载 `ColorFormatter.alfredworkflow`，双击安装;
2. 默认的 keyword 是 `cl`，然后回车确定，输入（粘贴更佳）符合格式 (`#xxxxxx`) 的十六进制颜色值
3. 根据右侧快捷键选择对应的颜色格式（好吧，只有 Objective-C 的 `UIColor` = =），好了，它已经在你的粘贴版里了。
4. 粘贴到需要的位置呗~

## 故事 

这其实是一件比较悲剧的事情，第一天写了个雏形，心急火燎的发出来，坐等掌声一片。然后第一个回复是 `这个之前早就有了` = =

然后我抛砖引玉的获得了一个功能完善到反正我是没挑出来毛病的链接 [Colors](http://www.packal.org/workflow/colors)

本着不重复造轮子的原则，如果没有什么别的需要，这个版本就是最终形态了。

最后不得不说一句，最大的收获是 GET 到了一个很 nice 的 Alfred 资源网站:[http://www.packal.org](http://www.packal.org)。

记得有句什么诗是用来歌颂这种“关一扇门，开一扇窗”的狗屎运的，一时想不起，请看官自行脑补好了(≖ ‿ ≖)✧

就是这样，再会。



