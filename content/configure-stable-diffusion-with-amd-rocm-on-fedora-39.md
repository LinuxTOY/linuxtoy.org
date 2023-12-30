Title: 在 Fedora 39 上配置 AMD ROCm 加速的 Stable Diffusion
Date: 2023-12-30 12:35
Category: Howto
Tags: fedora, amd, ai
Slug: configure-stable-diffusion-with-amd-rocm-on-fedora-39
Authors: lovenemesis

随着硬件性能的提升和技术的改进，以往仅能通过云端服务体验的生成式 AI 绘图也出现了可以在本地运行的版本，其中最受欢迎的就是[Stable Diffusion](https://stability.ai/stable-image) 。以往这个过程需要依赖 [Nvidia 显卡及闭源的 CUDA 框架](https://developer.nvidia.com/cuda-toolkit)，经过一系列社区开发者的努力，现在能在 [Fedora 39](https://fedoramagazine.org/announcing-fedora-linux-39/) 中经过简单的配置，用开源社区友好的 AMD 显卡加速本地运行的[Stable Diffusion](https://stability.ai/stable-image)。

## 安装 AMD ROCm 计算框架 ##

[AMD 的 ROCm 计算框架](https://www.amd.com/en/products/software/rocm.html) 严格上来讲[仅支持少数几个面向企业的 Linux 发行版](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/tutorial/quick-start.html)，但得益于 Fedora 异构计算兴趣小组成员的努力，ROCm 框架中相当一部分软件包已经进入了 Fedora 的标准仓库中，截至本文发布时为 ROCm 5.7.1 版本。详细的步骤推荐参考[Fedora Wiki](https://fedoraproject.org/wiki/SIGs/HC)，这里简单说明下：

* 将当前用户添加到 `video` 组使得非 `root` 用户亦可使用显卡加速功能：`sudo usermod -a -G video $LOGNAME`
* 安装对应运行时环境、编译工具和辅助工具：`pkcon install rocminfo rocm-opencl rocm-hip rocm-smi`

这一步就完成了！由于 Fedora 38 之后的内核已经开启了 GPU 计算支持，这一步甚至比在官方支持的 Linux 发行版上安装还要简单。

此时可以尝试运行 `rocminfo` 确保显卡已经被 ROCm 框架正确识别。 

## 配置 Conda 安装 Python 3.11 ##

[Fedora 39 中默认预装的 Python 3.12](https://fedoraproject.org/wiki/Changes/Python3.12) 很可惜暂时还不被 [Stable Diffusion](https://stability.ai/stable-image) 支持，所以我们需要使用 [Conda](https://conda.io/) 创建一个使用 Python 3.11 的单独运行环境。所幸的是 Fedora 中已经收录了较新的 Conda 版本，直接从软件仓库安装配置即可：

* 从软件仓库安装：`pkcon install conda python3-pip`
* 创建使用 Python 3.11 的运行环境： `conda create -n py311 python=3.11 -y`
* 打开一个新的终端，启用刚刚创建的运行环境：`conda activate py311`

## 安装适用于 ROCm 的 PyTorch ##

[Stable Diffusion](https://stability.ai/stable-image) 的底层运用了流行的 PyTorch 框架，这里我们需要安装其支持 ROCm 的版本，而又因为 Pytorch 尚未提供 Conda 版本的软件包，所以又需要使用 pip 安装…… 参考其[PyTorch 官方页面](https://pytorch.org/get-started/locally/)，在刚才**启用的 Python 3.11 环境**中，运行如下命令安装目前尚处于预览阶段但支持 ROCm 5.7 的版本：

`pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm5.7`

这一步骤涉及约 1.8GB 的依赖安装，用时较长且需要稳定的网络环境。

安装过后，建议参考[官网的验证过程](https://pytorch.org/get-started/locally/#linux-verification)确保可以正确识别到显卡加速支持。

## Stable Diffusion Web UI ##

流行的 [Stable Diffusion Web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)的[一键式安装脚本](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Install-and-Run-on-AMD-GPUs)尚未支持 ROCm 5.7 版本，所以需要使用手动安装的方式。

* 下载其[发布版源代码包](https://github.com/AUTOMATIC1111/stable-diffusion-webui/releases)，本文发布时[为 1.7.0 版本](https://github.com/AUTOMATIC1111/stable-diffusion-webui/releases/tag/v1.7.0)。
* 解压并进入其目录：`tar xf stable-diffusion-webui-1.7.0.tar.gz && cd stable-diffusion-webui-1.7.0`
* 利用 pip 解决其依赖关系：`pip3 install -r requirements.txt`

这一步骤涉及约 4.5GB 的依赖安装，默认会下载 `v1-5-pruned-emaonly.safetensors` 版本的 checkpoint，用时较长且需要稳定的网络环境。

至此安装步骤完成～

## 启动及运行 ##

启动和运行有几点需要注意的：

* 记得切换至 Python 3.11 环境：`conda activate py311`
* 除非使用的是 AMD ROCm 正式支持的显卡，绝大部分消费级别显卡需要添加环境变量以声明显卡型号，例如笔者使用的 Radeon 7800 XT 启动时需要添加 `HSA_OVERRIDE_GFX_VERSION=11.0.0`
* 直接在 `stable-diffusion-webui-1.7.0` 目录下运行 `launch.py --listen` 即可，比如笔者为 `HSA_OVERRIDE_GFX_VERSION=11.0.0 python launch.py --listen`
* 如果需要使用 WebUI 的插件支持的话，参照[其 Github Wiki](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Extensions) 添加运行时参数 `--enable-insecure-extension-access`
* 更多的 Checkpoint 和 Refiner 可以[在 Hugging Face 找到](https://huggingface.co/stabilityai)。
* 工作的时候可以在另一个终端使用 `watch -n 1 -d rocm-smi` 监控 GPU 加速的运行状态。

## 法律声明 ##

使用过程中请[遵守 Stability AI 的使用条款](https://stability.ai/use-policy)并[尊重其他艺术家原创工作](https://stability.ai/s/Grassroots-innovation-in-open-models-suggested-amendments-to-the-AI-Act.pdf)，其结果切记**不可用于任何商业获利、歪曲事实、损害他人或违法所在国家法律的场景**。

## 参考 ##

* [AMD显卡满血Stable Diffusion无脑部署笔记](https://zhuanlan.zhihu.com/p/656480759)
* [How to use Stable Diffusion](https://stable-diffusion-art.com/beginners-guide/)

