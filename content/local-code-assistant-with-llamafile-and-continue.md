Title: 基于 llamafile 和 Continue 的本地AI代码助手
Date: 2024-12-02 19:10
Category: Tutorial
Tags: fedora, llm
Slug: local-code-assistant-with-llamafile-and-continue
Authors: lovenemesis

继“数字货币”和“区块链”之后，IT 业界目前最火的概念毫无疑问就是 “AI“ 了。些许值得庆幸的是，在经过一年多的发展后，名为 “AI” 实为 “LLM（大语言模型）”的领域已经有一些较为成熟的本地运行的方案，可以满足有隐私顾虑和网络受限的场景。本文将以 Fedora 41 为例介绍涉及的工具和对应的配置，搭建基于大语言模型的代码助手，其思路及基本步骤亦适用于 OSX 及 Windows 系统。

## Llamafile: 本地运行 LLM 的分发和部署环境

[Llamafile](https://github.com/Mozilla-Ocho/llamafile) 是来自 [Mozilla Ocho](https://github.com/Mozilla-Ocho) 的一个开源项目，提供了分发和部署 LLM  运行环境的简便方法。相比于其他流行的本地 LLM 部署方式（比如 [ollama](https://github.com/ollama/ollama) 或者 [LlamaEdge](https://github.com/LlamaEdge/LlamaEdge) ），Llamafile 的优势有：

* 单一二进制文件即可实现运行**跨平台**（Linux、OSX 及 Windows）**跨架构**（X86_64 及 ARM64）运行
* 本身**无需安装**即可直接运行，无需处理繁复的依赖关系
* **不强行要求系统上安装的 ROCm 或者 CUDA 框架**，只要正确安装对应的显卡驱动即可实现 GPU 加速
* 以沙箱方式运行的**兼容于 OpenAI 接口服务**，安全且无缝衔接各类第三方 AI 应用
* 可以将运行时环境、模型文件和运行参数**封装成一个文件**，便于分发

更多的详情可以参考项目的[首页说明文件](https://github.com/Mozilla-Ocho/llamafile/blob/main/README.md)。该项目也提供了一些流行 LLM 模型的预封装文件，下载后即可运行。

由于我们接下来用于代码助手领域的大语言的模型并未预先封装，所以我们只需要下载最新的 `llamafile` 文件用作运行时环境即可：

1. 前往[项目发布页面](https://github.com/Mozilla-Ocho/llamafile/releases)，下载最新发布版本 `Assets` 中的 `llamafile-X.X.X`文件，本文撰写时为 `llamafile-0.9.0`
2. 将下载好的文件放到合适的位置: 
```
mv -v llamafile-0.9.0 $HOME/bin/llamafile
```

3. 赋予其可执行权限:
```
chmod +x $HOME/bin/llamafile
```
4. 如果是 Windows 系统，记得为其添加上 `.exe` 的后缀名

## 模型文件: Qwen2.5-coder

有了运行时环境，接下来就需要 LLM 的模型文件本身了。本文撰写时，专注于代码生成领域相对较新的开源的 LLM 是 [Qwen2.5-coder](https://qwen2.org/qwen2-5-coder/)，支持 92 种编程语言和中英两种自然语言，其 7B 版本提供了接近 GPT3.5-Turbo 的性能，而 32B 则更是比肩 GPT4o。

大语言模型文件以多种格式分发，隶属于 [llama.cpp](https://github.com/ggerganov/llama.cpp) 家族的 [Llamafile](https://github.com/Mozilla-Ocho/llamafile) 需要配合 GGUF 格式使用。同时受限于本地设备的性能和显存，需要选择体积较小的量化后版本。结合上述限制，再依据代码助手的使用场景，**需要搭配使用两种训练风格的模型文件**：

*  Instruct 风格适合对于自然语言指令的理解并将据此生成代码：[通义千问2.5-代码-7B-Instruct-GGUF](https://www.modelscope.cn/models/Qwen/Qwen2.5-Coder-7B-Instruct-GGUF/resolve/master/qwen2.5-coder-7b-instruct-q5_k_m.gguf)（显存少于 12G）或[通义千问2.5-代码-14B-Instruct-GGUF](https://www.modelscope.cn/models/Qwen/Qwen2.5-Coder-14B-Instruct-GGUF/resolve/master/qwen2.5-coder-14b-instruct-q5_k_m.gguf)（显存大于或等于 12G）
* Base 风格适合根据上下文代码或文字做自动补充：[Qwen2.5-Coder-1.5B-GGUF](https://www.modelscope.cn/models/QuantFactory/Qwen2.5-Coder-1.5B-GGUF/resolve/master/Qwen2.5-Coder-1.5B.Q5_K_M.gguf)（显存少于 12G）或[Qwen2.5-Coder-7B-GGUF](https://www.modelscope.cn/models/QuantFactory/Qwen2.5-Coder-7B-GGUF/resolve/master/Qwen2.5-Coder-7B.Q5_K_M.gguf)（显存大于或等于 12G）


模型文件较大，下载完成需要一定的时间，之后将其挪动到任意一个自己觉得合适的位置，比如 `$HOME/gguf`。后续以显存少于 12G 的模型示例，若显存充裕请自行替换相应模型名称即可。

## 使用 Llamafile 调用 Qwen2.5-Coder

现在可以使用 `llamafile` 尝试加载一下模型文件，检测一下 GPU 推理加速的状态：

```
$ llamafile -m qwen2.5-coder-7b-instruct-q5_k_m.gguf -ngl 999 --log-disable
```

参数解析：

* `-m` 指定了加载的模型 gguf 文件名
* `-ngl 999` 代表尽可能的将模型文件中的 GPU 层数加载到显存中
* `--log-disable` 代表禁用在运行目录写入持久性日志文件

```
software: llamafile 0.9.0
model:    qwen2.5-coder-7b-instruct-q5_k_m.gguf
compute:  AMD Radeon 780M
server:   http://127.0.0.1:8080/
A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.
>>>
```

若能看到类似上文的终端聊天界面，代表运行成功。其中 `computer` 部分指示了用于推理的设备，如果匹配自己的 GPU 型号便代表 GPU 推理加速正确启用，同时也能看到它在本地启用了一个监听 `8080`端口 的服务，可供使用 “OpenAI 兼容 API” 的接口第三方应用调用。

上述的指令便足以在使用最新内核的 Fedora 41 上的调用 AMD 7000 系列显卡实现推理加速。若是上述指令显示的是使用 CPU 加速，可能需要根据配置和操作系统不同设定 `HSA_OVERRIDE_GFX_VERSION` 环境变量或者额外传入 `--nocompile` 参数，可以参考 [Llamafile](https://github.com/Mozilla-Ocho/llamafile) 的项目首页进一步获知，在此不再赘述。

试着跟它对话几句后，感受下性能，之后使用 `Ctrl +C` 退出并结束。因为后续在代码助手的交互场景，只需要有 “OpenAI 兼容 API” 的服务即可。接下来，无论是使用诸如 [zellij](https://github.com/zellij-org/zellij) 之类的终端分屏器或者打开两个标签页的方式，**分别以仅服务器模式启动两个模型**，如果遵循上面的假设存放路径的话，那么完整的命令为：

```
$HOME/bin/llamafile -m $HOME/gguf/qwen2.5-coder-7b-instruct-q5_k_m.gguf -ngl 999 --server --nobrowser --log-disable
```
和
```
$HOME/bin/llamafile -m $HOME/gguf/Qwen2.5-Coder-1.5B.Q5_K_M.gguf -ngl 999 --server --port 8081 --nobrowser --log-disable
```

注意这里我们为运行 Base 模型的 `llamafile` 服务进程指派了另一个端口 `8081`，避免与运行 Instruct 模型的进程冲突。

若最终能在终端中看到类似下述的内容，代表运行成功：

```
warming up the model with an empty run
{"function":"initialize","level":"INFO","line":502,"msg":"initializing slots","n_slots":1,"tid":"12066432","timestamp":1733128297}
{"function":"initialize","level":"INFO","line":514,"msg":"new slot","n_ctx_slot":8192,"slot_id":0,"tid":"12066432","timestamp":1733128297}
{"function":"server_cli","level":"INFO","line":3131,"msg":"model loaded","tid":"12066432","timestamp":1733128297}

llama server listening at http://127.0.0.1:8080

{"function":"server_cli","hostname":"127.0.0.1","level":"INFO","line":3269,"msg":"HTTP server listening","port":"8080","tid":"12066432","timestamp":1733128297,"url_prefix":""}
{"function":"update_slots","level":"INFO","line":1672,"msg":"all slots are idle and system prompt is empty, clear the KV cache","tid":"12066432","timestamp":1733128297}
```

此时无需使用 `Ctrl +C` 退出，可以暂搁置一旁，马上就要用到。


## Continue.dev 代码助手

代码助手显然是不甘于屈居于终端的，必然要和开发工具关联起来。[Continue.dev](https://github.com/continuedev/continue)是一款适用于 VS Code 和 Jetbrains 家族的 IDE 插件，内建了对于 [Llamafile](https://github.com/Mozilla-Ocho/llamafile) 的良好支持。参考[官方文档的说明](https://docs.continue.dev/getting-started/install)安装并下载插件后（体积较大请有耐心），很快能看到它的配置向导部分。此时可以点击 "Skip"，然后**点击插件侧栏内的齿轮样按钮**，打开其 JSON 格式的配置文件，下面介绍并说明需要修改的几个字段：

```
"models": [
    {
      "title": "qwen2.5-coder:7b",
      "provider": "llamafile",
      "model": "qwen2.5-coder:7b"
    }
  ],
```

这里重要的是 `provider` 字段，这里将提示 [Continue.dev](https://github.com/continuedev/continue)以兼容 [Llamafile](https://github.com/Mozilla-Ocho/llamafile) 的方式构建 API 请求，传至运行在 `8080` 端口的 Instruct 模型。


```
"tabAutocompleteModel": {
    "title": "qwen2.5-coder:1.5b",
    "provider": "llamafile",
    "model": "qwen2.5-coder:1.5b",
    "apiBase": "http://127.0.0.1:8081"
  },
```

类似的，这里依然提示 [Continue.dev](https://github.com/continuedev/continue)以兼容 [Llamafile](https://github.com/Mozilla-Ocho/llamafile) 的方式构建 API 请求，但通过额外指定 `apiBase`的方式传给运行在 `8081` 端口的 Base 模型。

```
"embeddingsProvider": {
    "provider": "transformers.js"
  },
```

如果在诸如 [VSCodium](https://vscodium.com/) 的 VS Code 家族的 IDE 使用[Continue.dev](https://github.com/continuedev/continue)，还可以向上面那样利用捆绑的 [Transformer.js](https://huggingface.co/docs/transformers.js/index) 和 `all-MiniLM-L6-v2` Embedding 模型对当前工作目录创建本地索引，为[代码仓库级别的交互问题](https://docs.continue.dev/customize/deep-dives/codebase)提供必要的上下文。注意 JetBrains 家族的 IDE 里的插件尚不支持此方式。

虽说理论上这一步也可以借助 [Llamafile](https://github.com/Mozilla-Ocho/llamafile) 的方式再运行一个为 Embedding 用途优化的模型以 GPU 加速方式实现，但在实际使用过程中索引并不频繁，且在现代的 CPU 完成索引并不慢，在本地资源有限的情况下就不增加复杂度了。

接下来保存编辑后的配置文件，此时应该可以看到侧栏中 [Continue.dev](https://github.com/continuedev/continue) 的聊天框中出现了上述设置的 `qwen2.5-coder:7b`的模型名，**至此所有配置完成**，此时可以开始领略在其[官方教程](https://docs.continue.dev/getting-started/overview)中演示到的各种能力了。

后续的使用中，只要通过偏好的快捷脚本或批处理方式分别启动对应 Instruct 和 Base 模型的两个 [Llamafile](https://github.com/Mozilla-Ocho/llamafile)进程，之后就可以**在 IDE 中享受有大语言模型助力的编码时光**了，哪怕前往渡假地的飞机上没有网络。
