Title: 基于 Koboldcpp 的本地 AI 翻译和研究助手
Date: 2025-02-18 23:00
Category: Tutorial
Tags: fedora, llm
Slug: local-research-assistant-with-koboldcpp-pot-and-gpt4all
Authors: lovenemesis

紧接上文，这次将以 Fedora 41 为例，搭建另一组基于大语言模型工具，适合**仅有核显的办公轻薄本**在有隐私顾虑和网络受限的场景下继续学术研究。这里介绍的思路及基本步骤亦适用于 OSX 及 Windows 系统。

## Koboldcpp: 多用途的本地 LLM 运行环境

[Koboldcpp](https://github.com/LostRuins/koboldcpp) 是基于知名 LLM 推理引擎 [llama.cpp](https://github.com/ggerganov/llama.cpp) 的外围封装，提供了多种灵活的运行方式。相比于其他流行的本地 LLM 部署方式（比如 [ollama](https://github.com/ollama/ollama) 以及本站之前介绍过的 [Llamafile](https://github.com/Mozilla-Ocho/llamafile) ），Koboldcpp 的优势有：

* 较为紧密的**跟进上游项目的进展**，后端和模型支持很及时
* 本身**无需安装**即可直接运行，无需处理繁复的依赖关系
* **内建通用性极佳的 Vulkan GPU 加速后端 **，不强制依赖专用显存，非常适用于仅具备核显和极少显存的办公轻薄本
* 除了自家的 Kobold AI 接口，也提供**兼容于 OpenAI 和 Ollama 接口服务**，无缝衔接各类第三方 AI 应用
* 除了文字生成模型，还可以**加载并运行语音识别、声音转文字甚至图片生成模型**，用途多样

更多的详情可以参考项目的[ Wiki 说明文件](https://github.com/LostRuins/koboldcpp/wiki)。Koboldcpp 提供了适用于多种平台的预编译版本，适用于无 AVX 的古老 CPU、新旧版本 CUDA、Mac Metal 等各种环境。由于接下来主要在办公轻薄本上运行，所以会以 Vulkan 后端的版本用作说明：

1. 前往[项目发布页面](https://github.com/LostRuins/koboldcpp/releases)，下载最新发布版本 `Assets` 中的 `koboldcpp-linux-x64-nocuda`（Linux X86_64） ，这个版本不包含 CUDA 运行时环境，所以仅有 70MB 左右
2. 将下载好的文件放到任意一个自己觉得合适的位置: 
```
mv -v koboldcpp-linux-x64-nocuda $HOME/bin/koboldcpp
```
3. 赋予其可执行权限: 
```
chmod +x $HOME/bin/koboldcpp
```

## 模型文件: Qwen2.5 和 DeepSeek-R1-Distill

学术研究的场景下大致有外语翻译、文本总结和分析的需求。基于本文撰写时，遵循开源协议发表的 LLM 中这两方面做的比较好的便是支持 29 中自然语言的 [Qwen2.5](https://qwen2.org/qwen2-5-coder/) 和具备深度推理功能的 [DeekSeek-R1](https://api-docs.deepseek.com/news/news250120)了 。当然后者受限于设备性能，仅能选择体积较小的蒸馏版。考虑到大多数办公轻薄本仅有 16G 融合内存，所以后续的描述以下述两款 `Q5_k_M` 量化的 7B 模型 为例，若内存充裕的话，可以选择相应模型更大参数的版本：

* [通义千问2.5-7B-Instruct](https://www.modelscope.cn/models/Qwen/Qwen2.5-7B-Instruct-GGUF/resolve/master/qwen2.5-7b-instruct-q5_k_m.gguf) : 用于外文和中文双向互译
* [DeepSeek-R1-Distill-Qwen-7B](https://www.modelscope.cn/models/bartowski/DeepSeek-R1-Distill-Qwen-7B-GGUF/resolve/master/DeepSeek-R1-Distill-Qwen-7B-Q5_K_M.gguf)：用于数学和逻辑推理

模型文件较大，下载完成需要一定的时间，之后将其挪动到任意一个自己觉得合适的位置，比如 `$HOME/gguf`。

## 使用 Koboldcpp 运行模型文件

如果在终端以不带任何参数的方式运行 Koboldcpp 的话，会打开其图形化的启动器:

```
$HOME/bin/koboldcpp
***
Welcome to KoboldCpp - Version 1.83.1
For command line arguments, please refer to --help
***
Unable to detect VRAM, please set layers manually.
Auto Selected Default Backend...
```

此时仅需做少许配置：

* "Presets" 选择 "Use Vulkan""
* "GPU layers" 默认的 "-1" 代表根据侦测到的可用显存将模型加载到显存中，进一步提升推理速度，也可以根据实际应用场景自行指定，这里的两款 7B 模型至多 29 层
* "GGUF Text Model": 选择上面下载的其中任意一个 GGUF 模型文件
* 适当的将 "Context Size"" 调整至 "8192"

之后点击 "Launch"，便可以启动其内建名为 “Kobold Lite” 的图形界面。从 1.83 版本起它已经可以根据加载 GGUF 模型里包含的信息自动应用匹配的聊天模板了，但对于包含深度推理的 DeepSeek 模型来说，模板里默认的单次 512 的输出量明显不够用，需要调整一下：

1. 在 Kobold Lite 界面里点击 "Settings"
2. 切换至 "Samplers"，找到 "Max Output" 参数
3. 滑块最大也仅能到 1024，但可以通过点击上方的数字输入更大的值，比如 2048

笔者分别在搭载 AMD Ryzen 5600U 轻薄本和 AMD Rayzen 6850HS 的办公本做了测试，相比之前受制于显存仅能使用 CPU 的结果来看，**来自 Vulkan 的 GPU 加速使得推理时间缩短了 70% 左右，实际体验的改善非常明显**。至于为什么没有更快，大概率是内存瓶颈的缘故了。

## 使用 Koboldcpp 命令行的方式运行模型文件

虽说 Koboldcpp 的 Launcher 和 Kobold Lite 功能全面，但是毕竟是个不支持国际化的全英文界面，并非适用所有学术研究人员。另一方面，上述提及的 Launcher 和 Kobold Lite 配置是独立保存的，每次启动时都手动指定加载配置文件略显麻烦。所以接下来将采取命令行的方式将 Koboldcpp 的模型启动和配置整合成一键运行脚本。

对于需要传给 Launcher 选项来说比较直观：

* `--model` ：指定模型文件名
* `--usevulkan` ： 指定使用基于 Vulkan GPU 加速后端
* `--gpulayers` ：用 `-1` 做自动检测或者指定一个具体值
* `--skiplauncher` ： 略过 Launcher 启动器
* `--quiet` : 避免在命令行终端打印输入提示词和生成的结果
* `--contextsize` ： 指定更大的上下文窗口

而对于 Kobold Lite 里 "Max Output" 的配置，根据官网的说明和与项目作者的沟通，需要在聊天模板的层面指定，再通过 `--chatcompletionsadapter` 参数指定调整后的聊天模板。

参考项目源代码的自动识别模板，适用于 DeepSeek R1 的聊天模板如下：

```
{
  "system_start": "",
  "system_end": "",
  "user_start": "<｜User｜>",
  "user_end": "",
  "assistant_start": "<｜Assistant｜>",
  "assistant_end": "<｜end▁of▁sentence｜>",
  "max_length": 2048
}
```
注意最后增加的 "max_length" 参数，然后将其保存为 `$HOME/gguf/deepseek-maxlength.json` 以被调用。于是完整的命令行为：

```
$HOME/bin/koboldcpp --model $HOME/gguf/DeepSeek-R1-Distill-Qwen-7B-Q5_K_M.gguf --usevulkan --gpulayers -1 --skiplauncher --quiet --contextsize 12288 --chatcompletionsadapter $HOME/gguf/deepseek-maxlength.json
```

类似的，Qwen2.5 的聊天模板附加 "max_length" 参数后为：

```
{
        "system_start": "<|im_start|>system\n\n",
        "system_end": "<|im_end|>\n\n",
        "user_start": "<|im_start|>user\n\n",
        "user_end": "<|im_end|>\n\n",
        "assistant_start": "<|im_start|>assistant\n\n",
        "assistant_end": "<|im_end|>\n\n",
        "tools_start": "\n\n# Tools\n\nYou may call one or more functions to assist with the user query.\n\nYou are provided with function signatures within <tools></tools> XML tags:\n\n<tools>\n",
        "tools_end": "\n</tools>\n\nFor each function call, return a json object with function name and arguments within <tool_call></tool_call> XML tags:\n<tool_call>\n{\"name\": <function-name>, \"arguments\": <args-json-object>}\n</tool_call><|im_end|>\n",
        "max_length": 2048
}
```
保存为 `$HOME/gguf/qwen2-maxlength.json`，相应的命令行唤起方式则为：

```
$HOME/bin/koboldcpp --model $HOME/gguf/qwen2.5-7b-instruct-q5_k_m.gguf --usevulkan --gpulayers -1 --skiplauncher --quiet --contextsize 12288 --chatcompletionsadapter $HOME/gguf/qwen2-maxlength.json
```

之后将上述命令放置入偏好的终端脚本或批处理文件中保存即可。后续当运行这个脚本或者批处理文件的时候，Koboldcpp 将在后台以进程方式且不在浏览器打开 Kobold Lite，但在 `http://localhost:5001` 上提供其他应用访问的 KoboldAI、OpenAI 和 Ollama 三种风格 API。如需退出，关闭终端终端窗口即可。

当然可以进一步利用 "systemd" 的方式彻底将其服务化并纳入用户的登录进程管理，并不过这并不影响外围应用的访问，所以不再赘述。

## pot-app: 跨平台的翻译工具

接下来我们看下如何利用上述配置好的 LLM 帮助外文文献的阅读。[pot-app](https://pot-app.com/) 是一款跨平台的翻译工具，使用 Rust 搭配  Web 技术开发的界面十分友好。其官网提供[常见桌面操作系统的下载](https://pot-app.com/download.html)，此外 Linux 用户亦可从 Flathub 下载：

```
flatpak install flathub com.pot_app.pot
```

由于 pot-app 启动后默认会在托盘区，所以如果在 Linux 平台使用 GNOME 桌面环境的话，还需要安装下述插件才能看到，在 Fedora 上为：

```
pkcon install gnome-shell-extension-appindicator 
```

之后启动 pot-app 进行如下配置：

1. 点击系统托盘区，选择"偏好设置"
2. 点击"翻译设置"，将"语种检测引擎"选择为"本地"，根据需要可以开启"窗口默认置顶"
3. 点击"服务设置"，选择"翻译"
4. 点击"添加内置服务"，在弹出的列表中选择"OpenAI"
5. 在接着的配置界面中，输入下列信息：

* "配置名称" ：什么都行，比如 "Koboldcpp"
* "流式输出"：勾选
* "请求地址" ：`http://localhost:5001/v1/chat/completions`
* "Api Key" : 什么都行，比如 `nokey`
* "模型" ： 填入 "qwen2.5"

最后点击配置界面中的“保存”，如果一切无误且以命令行运行的 Koboldcpp 保持开启的的话，pot-app 会自动检测下并关闭配置界面。此时可以根据需求删除或禁用服务列表中的其他服务。

如果是 Win 或者 OS X 系统，那么根据[官网教程](https://pot-app.com/docs/invoke.html#%E7%8E%B0%E6%9C%89%E7%94%A8%E6%B3%95-%E5%BF%AB%E6%8D%B7%E5%88%92%E8%AF%8D%E7%BF%BB%E8%AF%91-%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8)再安装额外的支持插件后，即可实现划词翻译了，弹出的窗口中名为 "Koboldcpp" 字段内的内容便是基于本地大语言模型的翻译结果了。

### pot-app 在 Wayland 环境下的配置

但在 Linux，特别是默认使用 Wayland 的 GNOME 桌面环境上来说，划词翻译和文字识别均无法正常工作。经过一番测试，此时使用系统快捷键使用[外部调用](https://pot-app.com/docs/invoke.html)的方式兼容性更好一些。

#### 划词翻译

这里以 GNOME 47 为例：

1. 打开系统的"设置"页面，在左侧列表找到"键盘"
2. 滚动到最底端，点击"查看及自定义快捷键"
3. 在弹出的窗口中选择 "自定义快捷键"，然后点击"添加""
4. 根据[官网指南](https://pot-app.com/docs/invoke.html)，在弹出的配置窗口中填入下述内容：

	1. “名称” : 什么都行，不过 “翻译” 比较合适
	2. “命令” ：`curl "127.0.0.1:60828/selection_translate"`
	3. “快捷键” ： 比如 `Super + T` 

之后在 GNOME 桌面环境下，选择需要翻译的文本后，再按下刚才指定的快捷键，就能唤起 "pot-app" 的翻译窗口了。

#### 文字识别和截图翻译

目前能完美适配 GNOME Wayland 环境的截图工具也就是 GNOME 内置的截图了。根据官网描述的的调用流程，可以**将最新的内置截图复制到指定的缓存目录，再调用 `curl` 发送请求文字识别**。对于从 Flathub 安装的版本，可以使用下述脚本实现：

```
#!/bin/bash
mkdir -p "$HOME/.var/app/com.pot_app.pot/cache/com.pot-app.desktop" && \
cp "$(ls -t $HOME/图片/截图/*.png | head -n1)" "$HOME/.var/app/com.pot_app.pot/cache/com.pot-app.desktop/pot_screenshot_cut.png" && \
curl "127.0.0.1:60828/ocr_recognize?screenshot=false"
```

其中 `$HOME/图片/截图` 需要根据当前用户的语言做调整，指定到实际内置截图工具的默认保存目录。由于自定义快捷键不支持连续输入，所以需要之后将上述内容保存至一个当前用户可以访问脚本文件，比如 `potocr.sh`，之后仿照划词翻译的方式在 GNOME 系统的“自定义快捷键”中配置：

1. “名称” : 什么都行，不过 “识别” 比较合适
2. “命令” ：`potocr.sh`
3. “快捷键” ： 比如 `Super + C`

 之后在 GNOME 桌面环境下，使用内置截图完成后，再按下刚才指定的快捷键，就能唤起 "pot-app" 的文字识别窗口，并可关联翻译。

多说一句，其 "pot-app"" 插件系统提供的 [RapidOCR 识别插件](https://github.com/pot-app/pot-app-recognize-plugin-rapid)对于中文的识别率明显好于系统默认，推荐安装。

## GPT4All: 跨平台的个人文档知识库

[GPT4All](https://github.com/nomic-ai/gpt4all) 是一款注重隐私的大语言模型应用程序：

* 使用 Qt 构建的图形界面，
* 内建的 Nomic AI  Embedding 引擎，可以针对本地文档创建知识库，支持 docx、pdf、txt、md、rst 格式的文件
* 支持对单一 Excel 文件分析并解答

借助它，可以**实现离线个人版本的 RAG（检索增强生成）**，非常适合研究文献的处理。

其[官网](https://www.nomic.ai/gpt4all)提供了各个平台的下载，甚至包括 Windows ARM 版本。对于 Linux 用户来说，还可以使用 Flathub 社区维护版本：

```
flatpak install flathub io.gpt4all.gpt4all
```

虽说 GPT4All 包含的推理引擎也支持 Vulkan 后端设备，但是其相比 "Koboldcpp" 的 上游 Vulkan 实现来说，在可以使用 GPU 加速的模型选择方面限制很多，不支持精度较佳的 K_M 量化模型。所以接下来我们将配置它使用我们通过 Koboldcpp 在命令行状态提供的 OpenAI 实现聊天：

1. 点击“模型”
2. 点击“添加模型”，并选择 "All" 查看全部
3. 向下滚动列表，直到找到 "OpenAI-compatible"，输入以下信息：
	1. "enter $API_KEY" : 什么都行，比如 `nokey`
	2. "输入 $BASE_URL" : `http://localhost:5001/v1`
	3. "输入 $MODEL_NAME" : `deepseek-r1-distill-qwen`
4. 最后点击 "Install" 

之后我们便可以调用 "Koboldcpp" 使用 Vulkan GPU 加速的方式与本地文档进行聊天了。GPT4All 的聊天窗口对于 DeepSeek-R1 的思考模式做了适配，会默认折叠起来，很方便。

当然，也可以类似的配置 qwen2.5，实现一般的知识检索和问答。

注意**本地文档索引的生成依然是依赖内建的 Nomic AI 的 Embedding 引擎**，是无法利用 Vulkan GPU 加速的。不过 Embedding 本身计算量并不大，哪怕是 CPU 加速中等尺寸的本地文档集合也用不了太久时间。