Title: 使用 stable-diffusion.cpp 实现本地文生图
Date: 2024-09-04 07:30
Category: Howto
Tags: fedora, stable-diffusion, llm, ai
Slug: use-stable-diffusion-cpp-to-generate-image-from-text-locally
Authors: lovenemesis

之前在本站分享过[使用 PyRotch 在 AMD ROCm 框架实现的 Stable Diffusion](https://linuxtoy.org/archives/configure-stable-diffusion-with-amd-rocm-on-fedora-40.html) 文生图应用配置教程。这个方案需要安装特定版本 PyTorch 且涉及一系列复杂的依赖关系，运行起来也对系统的硬件配置有不小要求。近期又由于 AMD 在新版 ROCm 移除了对于移动版 Radeon 显卡的支持，促使笔者开始寻找替代解决方案，此时发现[支持 Vulkan 后端的 stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp) 是个颇有希望的替代品。

**stable-diffusion.cpp** 有如下特点：

* 基于 [ggml](https://github.com/ggerganov/ggml) 的完全 C/C++ 实现，轻量且无过多外部依赖
* 可直接读取 `safetensor` 类型的模型，无需预先转换成 `gguf`
* 支持 SD 全系列、Flux 和 Photomaker 模型
* 支援 CPU/AVX512、CUDA、ROCm、Metal、Vulkan 甚至 [Intel SYCL](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html) 后端

其中对于 Vulkan 这一跨平台跨厂商的支持尤其值得一提，简化了在复杂多样环境下的部署难度。下面以 Fedora 40 为例说明如何安装和配置使用 Vulkan 后端的 stable-diffusion.cpp。

### 安装编译依赖 ###

Vulkan 后端编译所需的全部依赖都可以在绝大多数发行版软件仓库找到，在 Fedora 40 上运行以下命令即可安装：

```
pkcon install git cmake ccache glslc glslang vulkan-headers vulkan-validation-layers vulkan-tools vulkan-loader-devel 
```

### 获取项目最新源代码 ###

```
git clone --recursive https://github.com/leejet/stable-diffusion.cpp
cd stable-diffusion.cpp
```

代码整体很小，不过过程中依然注意需要保持网络环境稳定。

### 编译及安装 ###

参照其[项目首页](https://github.com/leejet/stable-diffusion.cpp/blob/master/README.md)，可知需要额外传入编译参数启用 Vulkan 后端支持

```
mkdir build && cd build
cmake .. -DSD_VULKAN=ON
cmake --build . --config Release
```

依赖关系没问题的话，编译过程在一般笔记本5分钟之内即可完成。

### 测试并安装 ###

项目首页的各个例子参考了[stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) 的目录结构，均假设模型文件存放在固定目录下，类似的，我们亦可创建对应的输出文件存放路径。

```
mkdir ../models ../outputs
```

将下载的模型文件移动到刚才创建的  `models` 目录，这里以 SD3 Medium 为例，之后可以尝试如下命令验证下结果：

```
./bin/sd -m ../models/sd3_medium_incl_clips_t5xxlfp16.safetensors -W 1024 -H 1024 -s -1 --cfg-scale 7.0 --sampling-method euler --vae-on-cpu -o ../outputs/$(date +"%Y%m%dT%H%M%S").png -p 'a lovely penguin holding a sign saying \"LinuxTOY.org\", defocus, background of a server room'
```

关于参数有几点需要注意的：

* `--vae-on-cpu` 几乎是必备的
* 随机种子默认是固定的 42，使用任意负数代表随机
* 可以使用 `$(date +"%Y%m%dT%H%M%S").png` 用作包含时间戳的输出文件名

在笔者配备了 AMD Radeon 7800XT 显卡的机器上，得出了如下的图片

![gajim 1.4 main window]({filename}/images/sd.cpp-sample.png)

这个结果大约用时 1分20秒，和之前使用 PyTorch 方案的几乎无差别。

如果以上结果均未遇到问题的话，那么就可以将其安装到系统目录便于其他用户访问。

```
sudo make install
```

至此全部配置完成

### 总结 ###

相比 PyTorch 版本的 stablde-diffusion 配置来说，这个 C++ 版本的实现在依赖关系和安装体积上要简练很多；而相比其他的跨平台跨厂商的实现，利用 Vulkan 后端能实现显卡的满负载运行，避免了算力的浪费。目前这个项目活跃度很高，值得对于本地文生图方案感兴趣的童鞋持续关注。
